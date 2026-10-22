"""Gateway tests against a fake vLLM upstream (no GPU needed).
Run from kit/gateway:  python -m pytest -q
"""
import json
import os
import sqlite3
import sys
import tempfile

import httpx
import pytest
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

HERE = os.path.dirname(os.path.abspath(__file__))
os.environ["GATEWAY_DB"] = os.path.join(tempfile.mkdtemp(), "test.db")
os.environ["ADMIN_TOKEN"] = "t0ken"
os.environ["MODELS_FILE"] = os.path.join(HERE, "..", "models.json")
sys.path.insert(0, os.path.join(HERE, ".."))
import app as gw  # noqa: E402

# ---------- fake vLLM
fake = FastAPI()


@fake.post("/v1/chat/completions")
async def fake_chat(request: Request):
    body = await request.json()
    if body.get("stream"):
        assert body["stream_options"]["include_usage"] is True

        async def gen():
            for tok in ["Hel", "lo"]:
                yield f'data: {json.dumps({"id": "x", "object": "chat.completion.chunk", "choices": [{"delta": {"content": tok}, "index": 0}]})}\n\n'
            yield f'data: {json.dumps({"id": "x", "object": "chat.completion.chunk", "choices": [], "usage": {"prompt_tokens": 1000, "completion_tokens": 500, "prompt_tokens_details": {"cached_tokens": 200}}})}\n\n'
            yield "data: [DONE]\n\n"
        return StreamingResponse(gen(), media_type="text/event-stream")
    return {"id": "x", "object": "chat.completion", "choices": [{"message": {"role": "assistant", "content": "Hello"}, "index": 0, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 1000, "completion_tokens": 500}}


@fake.get("/health")
async def fake_health():
    return {"ok": True}


@pytest.fixture
async def client():
    async with gw.app.router.lifespan_context(gw.app):
        # route every upstream call into the fake app
        gw.app.state.client = httpx.AsyncClient(transport=httpx.ASGITransport(app=fake), base_url="http://fake", timeout=30)
        for k, m in gw.app.state.models.items():
            if not k.startswith("_"):
                m["upstream"] = "http://fake"
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=gw.app), base_url="http://gw") as c:
            yield c


async def make_key(c):
    r = await c.post("/admin/keys", json={"name": "test"}, headers={"x-admin-token": "t0ken"})
    assert r.status_code == 200, r.text
    return r.json()["key"]


@pytest.mark.anyio
async def test_auth_required(client):
    r = await client.post("/v1/chat/completions", json={"model": "hy4-preview", "messages": []})
    assert r.status_code == 401


@pytest.mark.anyio
async def test_non_stream_billing(client):
    key = await make_key(client)
    r = await client.post("/v1/chat/completions", json={"model": "hy4-preview", "messages": [{"role": "user", "content": "hi"}]}, headers={"authorization": f"Bearer {key}"})
    assert r.status_code == 200
    assert r.json()["usage"]["completion_tokens"] == 500
    con = sqlite3.connect(os.environ["GATEWAY_DB"])
    row = con.execute("SELECT prompt_tokens, completion_tokens, cost_micro_usd FROM usage ORDER BY id DESC LIMIT 1").fetchone()
    # 1000 prompt at $0.792/M + 500 completion at $2.376/M = $0.000792 + $0.001188 = $0.00198 = 1980 micro-USD
    assert row == (1000, 500, 1980)


@pytest.mark.anyio
async def test_stream_billing_with_cache(client):
    key = await make_key(client)
    async with client.stream("POST", "/v1/chat/completions", json={"model": "glm-5.3", "messages": [{"role": "user", "content": "hi"}], "stream": True}, headers={"authorization": f"Bearer {key}"}) as r:
        assert r.status_code == 200
        text = "".join([chunk async for chunk in r.aiter_text()])
    assert "Hel" in text and "[DONE]" in text
    con = sqlite3.connect(os.environ["GATEWAY_DB"])
    row = con.execute("SELECT prompt_tokens, cached_tokens, completion_tokens, cost_micro_usd, streamed FROM usage ORDER BY id DESC LIMIT 1").fetchone()
    # glm-5.3: 800 uncached at $0.075/M + 200 cached at $0.0375/M + 500 completion at $1.33/M
    expected = round((800 * 0.075 + 200 * 0.0375 + 500 * 1.33) / 1e6 * 1e6)
    assert row == (1000, 200, 500, expected, 1)


@pytest.mark.anyio
async def test_unknown_model(client):
    key = await make_key(client)
    r = await client.post("/v1/chat/completions", json={"model": "nope", "messages": []}, headers={"authorization": f"Bearer {key}"})
    assert r.status_code == 404


@pytest.mark.anyio
async def test_feeds(client):
    r = await client.get("/v1/models")
    ids = [m["id"] for m in r.json()["data"]]
    assert "hy4-preview" in ids and "glm-5.3" in ids and "step-5-preview" not in ids  # step-5 disabled
    r = await client.get("/openrouter/models")
    doc = r.json()["data"][0]
    assert doc["schema_version"] == "2.4"
    assert doc["input_modalities"][0]["pricing"][0]["cost_usd"] == "0.000000792"
    assert doc["output_modalities"][0]["pricing"][0]["cost_usd"] == "0.000002376"
    assert doc["output_modalities"][0]["streaming"] is True
    assert "tools" in doc["output_modalities"][0]["supported_parameters"]


@pytest.mark.anyio
async def test_health_and_usage_report(client):
    r = await client.get("/health")
    assert r.status_code == 200 and r.json()["status"] == "ok"
    r = await client.get("/admin/usage", headers={"x-admin-token": "t0ken"})
    assert r.status_code == 200 and "rows" in r.json()
