"""Radiant Machines inference gateway.

OpenAI-compatible reverse proxy in front of one or more vLLM servers with:
  - API keys (hashed, SQLite), per-key concurrency cap
  - streaming and non-streaming passthrough for /v1/chat/completions and /v1/completions
  - usage metering from vLLM's usage object (stream_options.include_usage is injected)
  - cost per request from models.json prices, written to SQLite (no prompt or completion content is stored)
  - Stripe Billing meter events (optional; set STRIPE_API_KEY and STRIPE_METER_EVENT)
  - /v1/models (OpenAI format) and /openrouter/models (OpenRouter provider document format, schema 2.4)
  - /health and /metrics

Run:  uvicorn app:app --host 0.0.0.0 --port 8080
Env:  GATEWAY_DB=gateway.db  ADMIN_TOKEN=...  MODELS_FILE=models.json
      STRIPE_API_KEY=sk_live_...  STRIPE_METER_EVENT=inference_usd_cents  (optional)
      MAX_CONCURRENCY_PER_KEY=16  UPSTREAM_TIMEOUT_S=600
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
import secrets
import sqlite3
import time
import uuid
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator, Optional

import httpx
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse, StreamingResponse

DB_PATH = os.environ.get("GATEWAY_DB", "gateway.db")
MODELS_FILE = os.environ.get("MODELS_FILE", os.path.join(os.path.dirname(os.path.abspath(__file__)), "models.json"))
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "")
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
STRIPE_METER_EVENT = os.environ.get("STRIPE_METER_EVENT", "inference_usd_cents")
MAX_CONCURRENCY_PER_KEY = int(os.environ.get("MAX_CONCURRENCY_PER_KEY", "16"))
UPSTREAM_TIMEOUT_S = float(os.environ.get("UPSTREAM_TIMEOUT_S", "600"))


# ----------------------------------------------------------------- storage
def db() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.execute("PRAGMA journal_mode=WAL")
    return con


def init_db() -> None:
    con = db()
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS api_keys (
            id INTEGER PRIMARY KEY,
            key_hash TEXT UNIQUE NOT NULL,
            prefix TEXT NOT NULL,
            name TEXT NOT NULL,
            stripe_customer_id TEXT,
            active INTEGER NOT NULL DEFAULT 1,
            created_at REAL NOT NULL
        );
        CREATE TABLE IF NOT EXISTS usage (
            id INTEGER PRIMARY KEY,
            ts REAL NOT NULL,
            request_id TEXT NOT NULL,
            key_id INTEGER NOT NULL,
            model TEXT NOT NULL,
            prompt_tokens INTEGER NOT NULL,
            cached_tokens INTEGER NOT NULL DEFAULT 0,
            completion_tokens INTEGER NOT NULL,
            reasoning_tokens INTEGER NOT NULL DEFAULT 0,
            cost_micro_usd INTEGER NOT NULL,
            latency_ms INTEGER NOT NULL,
            status INTEGER NOT NULL,
            streamed INTEGER NOT NULL
        );
        CREATE INDEX IF NOT EXISTS usage_key_ts ON usage(key_id, ts);
        CREATE TABLE IF NOT EXISTS stripe_pending (
            key_id INTEGER PRIMARY KEY,
            micro_usd INTEGER NOT NULL DEFAULT 0
        );
        """
    )
    con.commit()
    con.close()


def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


# ----------------------------------------------------------------- models
def load_models() -> dict[str, dict[str, Any]]:
    with open(MODELS_FILE, "r", encoding="utf-8") as f:
        doc = json.load(f)
    out = {}
    for m in doc["models"]:
        if m.get("enabled", True):
            out[m["id"]] = m
    out["_provider"] = doc.get("provider", {})
    return out


def cost_micro_usd(m: dict[str, Any], prompt: int, cached: int, completion: int, reasoning: int) -> int:
    """Cost in micro-dollars. Reasoning tokens are billed at the completion rate (they are
    part of completion_tokens in OpenAI-compatible usage; counted separately only for reporting)."""
    uncached = max(0, prompt - cached)
    usd = (uncached * m["prompt_usd_per_m"] + cached * m.get("cached_prompt_usd_per_m", m["prompt_usd_per_m"])
           + completion * m["completion_usd_per_m"]) / 1e6
    return int(round(usd * 1e6))


# ----------------------------------------------------------------- stripe
async def stripe_flush(key_id: int, stripe_customer_id: Optional[str], add_micro: int) -> None:
    """Accumulate cost per key and send whole cents to a Stripe Billing meter."""
    if not STRIPE_API_KEY or not stripe_customer_id:
        return
    con = db()
    con.execute("INSERT INTO stripe_pending(key_id, micro_usd) VALUES(?, ?) ON CONFLICT(key_id) DO UPDATE SET micro_usd = micro_usd + excluded.micro_usd", (key_id, add_micro))
    row = con.execute("SELECT micro_usd FROM stripe_pending WHERE key_id=?", (key_id,)).fetchone()
    pending = row[0] if row else 0
    cents = pending // 10_000
    if cents < 1:
        con.commit(); con.close(); return
    con.execute("UPDATE stripe_pending SET micro_usd = micro_usd - ? WHERE key_id=?", (cents * 10_000, key_id))
    con.commit(); con.close()
    # Stripe Billing Meter Events API: https://docs.stripe.com/api/billing/meter-event/create
    async with httpx.AsyncClient(timeout=20) as c:
        r = await c.post(
            "https://api.stripe.com/v1/billing/meter_events",
            auth=(STRIPE_API_KEY, ""),
            data={
                "event_name": STRIPE_METER_EVENT,
                "payload[stripe_customer_id]": stripe_customer_id,
                "payload[value]": str(cents),
                "identifier": f"{key_id}-{int(time.time()*1000)}-{secrets.token_hex(4)}",
            },
        )
        if r.status_code >= 300:
            # put the cents back so they are retried on the next request
            con = db()
            con.execute("UPDATE stripe_pending SET micro_usd = micro_usd + ? WHERE key_id=?", (cents * 10_000, key_id))
            con.commit(); con.close()


# ----------------------------------------------------------------- app
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    app.state.models = load_models()
    app.state.client = httpx.AsyncClient(timeout=httpx.Timeout(UPSTREAM_TIMEOUT_S, connect=10))
    app.state.sems: dict[int, asyncio.Semaphore] = {}
    app.state.counters = {"requests": 0, "errors": 0, "prompt_tokens": 0, "completion_tokens": 0, "cost_micro_usd": 0}
    yield
    await app.state.client.aclose()


app = FastAPI(title="Radiant Machines inference gateway", lifespan=lifespan)


def auth(authorization: Optional[str]) -> dict[str, Any]:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(401, "Missing API key")
    key = authorization.split(" ", 1)[1].strip()
    con = db()
    row = con.execute("SELECT id, name, stripe_customer_id, active FROM api_keys WHERE key_hash=?", (hash_key(key),)).fetchone()
    con.close()
    if not row or not row[3]:
        raise HTTPException(401, "Invalid API key")
    return {"id": row[0], "name": row[1], "stripe_customer_id": row[2]}


def sem_for(key_id: int) -> asyncio.Semaphore:
    s = app.state.sems.get(key_id)
    if s is None:
        s = app.state.sems[key_id] = asyncio.Semaphore(MAX_CONCURRENCY_PER_KEY)
    return s


def record(key: dict[str, Any], model: dict[str, Any], usage: dict[str, Any], request_id: str, t0: float, status: int, streamed: bool) -> int:
    prompt = int(usage.get("prompt_tokens") or 0)
    completion = int(usage.get("completion_tokens") or 0)
    cached = int(((usage.get("prompt_tokens_details") or {}).get("cached_tokens")) or 0)
    reasoning = int(((usage.get("completion_tokens_details") or {}).get("reasoning_tokens")) or 0)
    micro = cost_micro_usd(model, prompt, cached, completion, reasoning)
    con = db()
    con.execute(
        "INSERT INTO usage(ts, request_id, key_id, model, prompt_tokens, cached_tokens, completion_tokens, reasoning_tokens, cost_micro_usd, latency_ms, status, streamed) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
        (time.time(), request_id, key["id"], model["id"], prompt, cached, completion, reasoning, micro, int((time.time() - t0) * 1000), status, 1 if streamed else 0),
    )
    con.commit(); con.close()
    c = app.state.counters
    c["requests"] += 1; c["prompt_tokens"] += prompt; c["completion_tokens"] += completion; c["cost_micro_usd"] += micro
    if status >= 400:
        c["errors"] += 1
    return micro


async def proxy(request: Request, path: str, authorization: Optional[str]) -> Any:
    key = auth(authorization)
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(400, "Body must be JSON")
    model_id = body.get("model")
    model = app.state.models.get(model_id) if model_id and not str(model_id).startswith("_") else None
    if not model:
        raise HTTPException(404, f"Unknown model: {model_id}")
    if body.get("max_tokens") and int(body["max_tokens"]) > model["max_output_tokens"]:
        body["max_tokens"] = model["max_output_tokens"]
    streamed = bool(body.get("stream"))
    if streamed:
        so = dict(body.get("stream_options") or {})
        so["include_usage"] = True
        body["stream_options"] = so
    request_id = f"rm-{uuid.uuid4().hex[:16]}"
    t0 = time.time()
    url = model["upstream"].rstrip("/") + path
    sem = sem_for(key["id"])
    if sem.locked() and sem._value == 0:  # noqa: SLF001
        raise HTTPException(429, "Too many concurrent requests for this key")
    await sem.acquire()
    client: httpx.AsyncClient = app.state.client
    headers = {"content-type": "application/json", "x-request-id": request_id}

    if not streamed:
        try:
            r = await client.post(url, json=body, headers=headers)
        except httpx.HTTPError as e:
            sem.release()
            record(key, model, {}, request_id, t0, 502, False)
            raise HTTPException(502, f"Upstream error: {type(e).__name__}")
        sem.release()
        data: Any
        try:
            data = r.json()
        except Exception:
            data = {"error": {"message": r.text[:500]}}
        usage = data.get("usage") if isinstance(data, dict) else None
        micro = record(key, model, usage or {}, request_id, t0, r.status_code, False)
        asyncio.create_task(stripe_flush(key["id"], key["stripe_customer_id"], micro))
        return JSONResponse(data, status_code=r.status_code, headers={"x-request-id": request_id})

    async def gen() -> AsyncIterator[bytes]:
        usage: dict[str, Any] = {}
        status = 200
        try:
            async with client.stream("POST", url, json=body, headers=headers) as r:
                status = r.status_code
                if status >= 400:
                    err = await r.aread()
                    yield err
                    return
                buf = b""
                async for chunk in r.aiter_bytes():
                    yield chunk
                    buf += chunk
                    # parse complete SSE lines for the usage object; keep the tail
                    while b"\n" in buf:
                        line, buf = buf.split(b"\n", 1)
                        line = line.strip()
                        if line.startswith(b"data:") and b"usage" in line:
                            try:
                                obj = json.loads(line[5:].strip())
                                if isinstance(obj, dict) and obj.get("usage"):
                                    usage = obj["usage"]
                            except Exception:
                                pass
        except httpx.HTTPError as e:
            status = 502
            yield f'data: {{"error": {{"message": "Upstream error: {type(e).__name__}"}}}}\n\n'.encode()
        finally:
            sem.release()
            micro = record(key, model, usage, request_id, t0, status, True)
            asyncio.create_task(stripe_flush(key["id"], key["stripe_customer_id"], micro))

    return StreamingResponse(gen(), media_type="text/event-stream", headers={"x-request-id": request_id, "cache-control": "no-cache"})


@app.post("/v1/chat/completions")
async def chat(request: Request, authorization: Optional[str] = Header(default=None)):
    return await proxy(request, "/v1/chat/completions", authorization)


@app.post("/v1/completions")
async def completions(request: Request, authorization: Optional[str] = Header(default=None)):
    return await proxy(request, "/v1/completions", authorization)


# ----------------------------------------------------------------- model listings
@app.get("/v1/models")
async def list_models():
    ms = [m for k, m in app.state.models.items() if not k.startswith("_")]
    return {"object": "list", "data": [{"id": m["id"], "object": "model", "created": m.get("created", 0), "owned_by": "radiant-machines"} for m in ms]}


def openrouter_doc(m: dict[str, Any], provider: dict[str, Any]) -> dict[str, Any]:
    """OpenRouter provider model document, schema 2.4 (openrouter.ai/docs/guides/providers/integration, read 2026-10-22)."""
    per_token = lambda usd_per_m: f"{usd_per_m / 1e6:.12f}".rstrip("0").rstrip(".")  # noqa: E731
    supported = {
        "temperature": {"type": "range", "min": 0, "max": 2},
        "top_p": {"type": "range", "min": 0, "max": 1},
        "max_tokens": {"type": "integer", "min": 1, "max": m["max_output_tokens"], "unit": "token"},
        "stop": {"type": "array", "max_items": 4},
        "frequency_penalty": {"type": "range", "min": -2, "max": 2},
        "presence_penalty": {"type": "range", "min": -2, "max": 2},
        "seed": {"type": "boolean"},
        "logprobs": {"type": "boolean"},
    }
    if m.get("tools"):
        supported["tools"] = {"type": "boolean"}
        supported["tool_choice"] = {"type": "boolean"}
    if m.get("structured_outputs"):
        supported["structured_outputs"] = {"type": "boolean"}
        supported["response_format"] = {"type": "boolean"}
    if m.get("reasoning"):
        supported["reasoning"] = {"type": "boolean"}
    input_pricing = [{"type": "prompt", "unit": "token", "cost_usd": per_token(m["prompt_usd_per_m"])}]
    if m.get("cached_prompt_usd_per_m") is not None:
        input_pricing.append({"type": "cached_prompt", "unit": "token", "cost_usd": per_token(m["cached_prompt_usd_per_m"])})
    output_pricing = [{"type": "completion", "unit": "token", "cost_usd": per_token(m["completion_usd_per_m"])}]
    if m.get("reasoning"):
        output_pricing.append({"type": "internal_reasoning", "unit": "token", "cost_usd": per_token(m["completion_usd_per_m"])})
    return {
        "schema_version": "2.4",
        "id": m["id"],
        "name": m["name"],
        "hugging_face_id": m.get("hugging_face_id", ""),
        "created": m.get("created", 0),
        "quantization": m.get("quantization"),
        "tokenizer": m.get("tokenizer", "Other"),
        "description": m.get("description", ""),
        "input_modalities": [{
            "type": "text",
            "supported_inputs": {"max_context_length": {"value": m["context_length"], "unit": "token"}},
            "pricing": input_pricing,
            "capacity": [{"type": "prompt", "unit": "token", "per": "minute", "value": m.get("capacity_prompt_tpm", 1000000)}],
        }],
        "output_modalities": [{
            "type": "text",
            "max_length": {"value": m["max_output_tokens"], "unit": "token"},
            "streaming": True,
            "supported_parameters": supported,
            "pricing": output_pricing,
            "capacity": [{"type": "completion", "unit": "token", "per": "minute", "value": m.get("capacity_completion_tpm", 200000)}],
        }],
        "capacity": [{"type": "request", "unit": "request", "per": "minute", "value": m.get("capacity_rpm", 600)}],
        "is_ready": True,
        "is_free": False,
        "discount_to_user": 0,
        "openrouter": {"slug": m.get("openrouter_slug", m["id"])},
        "datacenters": provider.get("datacenters", [{"country_code": "US"}]),
        "deployment_region": provider.get("deployment_region", "US"),
    }


@app.get("/openrouter/models")
async def openrouter_models():
    provider = app.state.models.get("_provider", {})
    ms = [m for k, m in app.state.models.items() if not k.startswith("_")]
    return {"data": [openrouter_doc(m, provider) for m in ms]}


# ----------------------------------------------------------------- ops
@app.get("/health")
async def health():
    client: httpx.AsyncClient = app.state.client
    out = {}
    for k, m in app.state.models.items():
        if k.startswith("_"):
            continue
        try:
            r = await client.get(m["upstream"].rstrip("/") + "/health", timeout=5)
            out[k] = "ok" if r.status_code == 200 else f"http {r.status_code}"
        except Exception as e:
            out[k] = f"down: {type(e).__name__}"
    ok = all(v == "ok" for v in out.values()) if out else False
    return JSONResponse({"status": "ok" if ok else "degraded", "models": out}, status_code=200 if ok else 503)


@app.get("/metrics")
async def metrics():
    c = app.state.counters
    lines = [f"gateway_requests_total {c['requests']}", f"gateway_errors_total {c['errors']}",
             f"gateway_prompt_tokens_total {c['prompt_tokens']}", f"gateway_completion_tokens_total {c['completion_tokens']}",
             f"gateway_revenue_usd_total {c['cost_micro_usd'] / 1e6:.6f}"]
    return PlainTextResponse("\n".join(lines) + "\n")


# ----------------------------------------------------------------- admin
def admin(x_admin_token: Optional[str]) -> None:
    if not ADMIN_TOKEN or x_admin_token != ADMIN_TOKEN:
        raise HTTPException(403, "Admin token required")


@app.post("/admin/keys")
async def create_key(request: Request, x_admin_token: Optional[str] = Header(default=None)):
    admin(x_admin_token)
    body = await request.json()
    name = body.get("name") or "unnamed"
    key = "rm-" + secrets.token_urlsafe(32)
    con = db()
    con.execute("INSERT INTO api_keys(key_hash, prefix, name, stripe_customer_id, created_at) VALUES(?,?,?,?,?)",
                (hash_key(key), key[:8], name, body.get("stripe_customer_id"), time.time()))
    con.commit(); con.close()
    return {"key": key, "name": name, "note": "Shown once. Store it now."}


@app.post("/admin/keys/{prefix}/revoke")
async def revoke_key(prefix: str, x_admin_token: Optional[str] = Header(default=None)):
    admin(x_admin_token)
    con = db()
    n = con.execute("UPDATE api_keys SET active=0 WHERE prefix=?", (prefix,)).rowcount
    con.commit(); con.close()
    return {"revoked": n}


@app.get("/admin/usage")
async def usage_report(x_admin_token: Optional[str] = Header(default=None), days: int = 30):
    admin(x_admin_token)
    con = db()
    since = time.time() - days * 86400
    rows = con.execute(
        "SELECT k.name, u.model, COUNT(*), SUM(u.prompt_tokens), SUM(u.completion_tokens), SUM(u.cost_micro_usd), AVG(u.latency_ms), SUM(CASE WHEN u.status>=400 THEN 1 ELSE 0 END) "
        "FROM usage u JOIN api_keys k ON k.id=u.key_id WHERE u.ts>=? GROUP BY k.name, u.model ORDER BY 6 DESC", (since,)).fetchall()
    con.close()
    return {"days": days, "rows": [{"key": r[0], "model": r[1], "requests": r[2], "prompt_tokens": r[3], "completion_tokens": r[4], "revenue_usd": round(r[5] / 1e6, 4), "avg_latency_ms": round(r[6] or 0), "errors": r[7]} for r in rows]}


@app.post("/admin/reload")
async def reload_models(x_admin_token: Optional[str] = Header(default=None)):
    admin(x_admin_token)
    app.state.models = load_models()
    return {"models": [k for k in app.state.models if not k.startswith("_")]}
