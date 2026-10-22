# November test kit

Everything needed to run the month-to-month test from the plan: serve two big open models with vLLM, put a billed OpenAI-compatible API in front of them, measure real throughput, publish an OpenRouter provider feed, and have the legal pages ready. All commands were checked against the vLLM recipes and OpenRouter provider docs as of 2026-10-22; re-check the recipe pages before the first run, they change weekly.

## Layout

| Path | What |
|---|---|
| `serving/hy4-preview.sh`, `serving/glm-5.3.sh`, `serving/step-5-preview.sh` | One-line launchers for the vLLM servers (Docker). Hardware variants via `HW=`. |
| `gateway/` | FastAPI gateway: API keys, streaming proxy, usage metering, Stripe meter events, `/v1/models`, `/openrouter/models`, `/health`, `/metrics`, admin endpoints. Tests in `gateway/tests`. |
| `gateway/models.json` | Model registry and prices (5% under the OpenRouter floors of 2026-10-22). |
| `bench/bench.sh`, `bench/summarize.py` | `vllm bench serve` sweep and the revenue-per-GPU-hour calculator. |
| `docker-compose.yml`, `Caddyfile`, `.env.example` | Gateway plus automatic TLS. |
| `legal/privacy-policy.md`, `legal/terms-of-service.md` | Drafts for attorney review. |

## Runbook

### Week of Nov 3: bring the pipeline up on one small instance

1. Rent a single GPU with a card (Koyeb H200 $3.00/hr or RTX PRO 6000 $2.20/hr) and install Docker with the NVIDIA container toolkit.
2. Serve any small model to validate the gateway end to end, for example `docker run --gpus all -p 8001:8000 vllm/vllm-openai:v0.29.0 openai/gpt-oss-120b --served-model-name hy4-preview` (temporarily reusing the `hy4-preview` id so the gateway routes to it).
3. `cd kit && cp .env.example .env`, set `ADMIN_TOKEN` and `DOMAIN`, point DNS at the box, `docker compose up -d --build`.
4. Create a key: `curl -s -X POST localhost:8080/admin/keys -H "x-admin-token: $ADMIN_TOKEN" -H 'content-type: application/json' -d '{"name":"me"}'`
5. Test: `curl https://$DOMAIN/v1/chat/completions -H "authorization: Bearer rm-..." -H 'content-type: application/json' -d '{"model":"hy4-preview","messages":[{"role":"user","content":"hi"}],"stream":true}'`
6. Check `curl localhost:8080/admin/usage -H "x-admin-token: $ADMIN_TOKEN"` shows tokens and revenue.
7. Submit the OpenRouter provider form (openrouter.ai/providers/apply/form) with `https://$DOMAIN/openrouter/models` as the models feed and the privacy policy URL. The feed validates against schema 2.4 (see `gateway/app.py`, `openrouter_doc`).

### Week of Nov 10: benchmark on the real node (2 to 3 days)

1. Rent 8x H200 (Koyeb, $24/node-hr, instant) or 8x B200 (Vultr, $28/node-hr, needs account review).
2. `HW=h200 EXTRA="--no-enable-prefix-caching" ./serving/glm-5.3.sh` and wait for `curl localhost:8002/health`.
3. `MODEL=zai-org/GLM-5.3 SERVED=glm-5.3 PORT=8002 GPUS=8 ./bench/bench.sh` (runs 3 shapes x 4 concurrencies; about 30 to 60 minutes).
4. `python bench/summarize.py --dir results --gpus 8 --rent 3.00 --prompt-usd 0.075 --completion-usd 1.33`
5. Repeat for Hy4-preview (`HW=b200 ./serving/hy4-preview.sh`, prices 0.792 / 2.376). On 8x B200 the MXFP8 checkpoint leaves little KV cache; if it will not start, lower `MAX_MODEL_LEN` to 65536, and treat 8x B300 or 8x MI355X as the real Hy4 nodes (the recipe's reference hardware).
6. Put the measured `out_tps_per_gpu` into `data/params.json` (`tps_out_per_gpu`), rerun `python -I model/model.py`, and read the new breakeven. Keep the median time to first token under about 3 seconds at the concurrency you will run; OpenRouter publishes it.

### Week of Nov 17: launch

1. Start the production node month-to-month, both models, prefix caching on (drop the `EXTRA` flag).
2. Publish pricing and the legal pages; open signups; onboard at least one unrelated paying customer at posted prices (keep the Stripe invoice; this is the IRC 195 start date).
3. If OpenRouter approves, confirm the feed, uptime and latency on your provider page the same day.

### Nov 24 to Dec 12: operate

- `/metrics` and `/admin/usage` weekly: revenue per GPU-hour versus rent, utilization, error rate. Keep uptime above 95%.
- Keep a time log (material participation) and a dated one-page plan.

### Dec 15 to Dec 28: decide

- If measured revenue per GPU-hour at measured utilization beats the rent, sign the prepaid term (specific GPUs and dates, non-refundable, ending by Dec 31, 2027) and pay by Dec 28. If not, stop the node.

## Gateway notes

- Prompt and completion bodies are never written to disk; only token counts and timings are stored (`usage` table). This is what the privacy policy promises.
- Streaming: the gateway injects `stream_options.include_usage` so vLLM's final chunk carries usage, and parses it on the way through.
- Stripe: create a Billing Meter (event name `inference_usd_cents`, aggregation sum) and a metered price on each customer's subscription; set the customer's `stripe_customer_id` when creating their key. The gateway accumulates fractional cents and sends whole cents as meter events after each request.
- Per-key concurrency cap: `MAX_CONCURRENCY_PER_KEY` (default 16). Requests over the cap get 429.
- Admin endpoints are blocked at the Caddy layer; use an SSH tunnel to port 8080.

## Tests

```
cd kit/gateway && python -m venv .venv && .venv/Scripts/pip install -r requirements.txt anyio && .venv/Scripts/python -m pytest -q
```
