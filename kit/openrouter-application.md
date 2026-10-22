# OpenRouter provider application: draft answers

The form at openrouter.ai/providers/apply/form is a HubSpot form with the 13 fields below (read 2026-10-22). Fill the bracketed items after the domain, email and gateway exist. Keep the free-text answers factual; the reviewers prioritize "providers that fill gaps" and say they have a backlog, so the pitch is the gap, not the company size.

| Field | Answer |
|---|---|
| Company Name | Radiant Machines |
| Website | https://[DOMAIN] (the API docs and pricing page; must be live before submitting) |
| Your Email | [you]@[DOMAIN] (they invite this address to a Slack Connect channel; use the business domain, not Gmail) |
| Display Name | Radiant Machines |
| Desired Slug | radiant |
| Distinguishing Features (select all that apply) | Unique Models; Low Pricing; High Throughput |
| Extra Details | see text below |
| URL to /models API | https://[DOMAIN]/openrouter/models (schema 2.4 document; the gateway serves it) |
| API Base URL | https://[DOMAIN]/v1 |
| URL to Privacy Policy | https://[DOMAIN]/privacy |
| URL to Terms of Service | https://[DOMAIN]/terms |
| Data Policy | see text below |
| Inference Location | US |
| HQ Location | Redwood City, California, United States |

## Extra Details (draft)

Radiant Machines serves the large open-weight models that currently have the fewest OpenRouter providers, on 8-GPU NVIDIA B200 nodes in the United States, priced below the current floor.

Models at launch: Tencent Hy4-preview (FP8, MTP speculative decoding, 262k context), Z.ai GLM-5.3 (native FP8 with FP8 KV cache and MTP, 262k context), and StepFun Step 5 Preview (FP8) as capacity allows. All three are served with vLLM 0.29 or newer using the model vendors' reference recipes, with tool calling and reasoning parsers enabled (hy_v4, glm47, step5) and native SSE streaming with usage reporting.

Pricing at launch, per million tokens: Hy4-preview $0.792 input / $2.376 output; GLM-5.3 $0.075 / $1.33; Step 5 Preview $0.95 / $2.565. Cached prompt tokens at half the input price. No per-request fees. We expect to lower prices as utilization rises.

Infrastructure: dedicated 8x B200 (180 GB) nodes with NVLink, hosted at a US cloud provider on a reserved term; prefix caching on; one gateway per node with health checks, automatic restart and rate limiting per key. Declared capacity per model is in the models feed (2M prompt tokens per minute, 400k completion tokens per minute, 600 requests per minute at launch) and will be raised as nodes are added. Target time to first token under 2 seconds at a 4k-token prompt and 95%+ uptime, both measured continuously and published on our status page.

Operations: a single engineer-owner runs the service, which is why we chose models that need a whole node rather than commodity models; we add value through throughput tuning (MTP, FP8 KV cache, concurrency limits that keep latency flat) and by being an additional independent host for models that have one to four providers today. We support monthly invoicing in USD and can start serving OpenRouter traffic the day the endpoint is approved.

## Data Policy (draft)

We do not store prompts or completions. Requests are processed in memory and discarded when the response completes; no request or response bodies are logged, sampled or backed up, and zero data retention is the default for every request. We never use prompts, completions or embeddings to train, fine-tune or evaluate models. We retain per-request metadata only (API key identifier, timestamp, model, token counts, latency, status code) for 13 months for billing and abuse prevention, and web-server access logs (IP, path, status) for 30 days. Inference runs on servers in the United States. Full policy: https://[DOMAIN]/privacy.

## Before you submit

1. The gateway must be reachable at the API base URL with TLS, and `/openrouter/models` must return the document for every model you will serve (the gateway builds it from `kit/gateway/models.json`).
2. The privacy policy and terms must be published at the URLs above (drafts in `kit/legal/`, attorney review first).
3. Use a business-domain email; the form says they invite it to Slack Connect.
4. Have the benchmark numbers from week three ready; if they ask for throughput and latency, give the measured figures (output tokens per second per node, median and p99 time to first token at the concurrency you run).
5. Do not inflate the declared capacity. OpenRouter learns a traffic cap from 429 responses and lowers routing share for endpoints that error.
