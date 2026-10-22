# GPU House

Research and a financial model for a small business that rents GPUs (or buys a few servers) and sells AI inference, with the 2026 US federal and California tax mechanics applied.

Live report: https://gourneau.github.io/gpu-house/ (the `docs/` folder). Long-form written report: [reports/GPU rental inference business plan.md](reports/GPU%20rental%20inference%20business%20plan.md).

## Layout

| Path | What it is |
|---|---|
| `docs/` | The published web page (static HTML, no build step). `docs/index.html` is the report; `docs/data.js` holds the model output it renders. |
| `model/model.py` | Scenario model. Reads `data/params.json`, writes `data/results.json` and `data/results.md`. Run with `python -I model/model.py` (set `CASE=typical` for the typical-throughput case). |
| `data/params.json` | Every input number with its source URL and the date it was checked. |
| `data/params_notes.md` | Why each input was chosen, and which cells are estimates. |
| `research_notes/` | Raw research notes from the web research pass, one file per topic, with citations. Includes the raw OpenRouter endpoint JSON. |
| `reports/` | The synthesized research report in markdown. |
| `kit/` | The November test kit: vLLM launch scripts for Hy4-preview, GLM 5.3 and Step 5, a billed OpenAI-compatible gateway with API keys, usage metering, Stripe meter events and an OpenRouter provider feed, a `vllm bench serve` sweep plus revenue calculator, compose with TLS, and draft privacy policy and terms. See `kit/README.md`. |

## Method

1. Web research on supply (GPU rental prices and terms of service), demand (inference marketplaces, OpenRouter pricing and volume), resale markets, throughput benchmarks, owned-hardware costs, alternative accelerators, Macs, niche models, other platforms, crypto earnings and tax rules. Every number carries a source URL and the date checked (2026-10-22).
2. A deterministic model turns those inputs into revenue per GPU-hour, an opportunity ranking per model and GPU, and scenario tables (month-to-month, 3-month, 12-month prepaid, staged test-then-prepay, Vast resale, owned hardware, hybrid) at $50k, $100k and $250k budgets and 20%, 40% and 70% utilization.
3. The web page renders the model output with charts and tables.

Nothing here is tax or legal advice. The tax section lists the rules and citations for a CPA to confirm.
