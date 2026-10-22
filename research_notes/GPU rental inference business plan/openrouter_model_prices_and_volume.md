# OpenRouter prices, provider counts and traffic for popular open-weight LLMs

All numbers below were read live on 2026-10-22. Sources: the public OpenRouter JSON API (`https://openrouter.ai/api/v1/models` and `https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints`), the rankings page (`https://openrouter.ai/rankings`, usage data through Oct 21, 2026) and the models listing sorted by weekly tokens (`https://openrouter.ai/models?order=top-weekly`). Raw JSON is saved beside these notes as `raw_openrouter_models.json` and one `raw_openrouter_endpoints_{author}_{slug}.json` per model (57 files). The stats script is `analyze_openrouter.py`; the weekly volumes it reads are in `weekly_tokens.json`; its output is `openrouter_tables_generated.md` and is also appended at the end of this file. Prices are USD per million tokens.

## Which slugs are current, and how were the numbers measured?

### Takeaway
Every requested slug still resolves except two (`deepseek/deepseek-r1` and `qwen/qwen3-235b-a22b` return zero endpoints), but the catalog has moved several generations past them. The requested 2025-era models together carry about 1T tokens per week, while the current leaders (DeepSeek V4.1 Flash, GLM 5.3 Flash) carry 12T to 27T each.

### Cited Findings
- The public models list returned 468 models on 2026-10-22 — [OpenRouter models API](https://openrouter.ai/api/v1/models)
- `deepseek/deepseek-r1` returns 0 endpoints; `deepseek/deepseek-r1-0528` is live with 3 providers — [r1 endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-r1/endpoints); [r1-0528 endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-r1-0528/endpoints)
- `qwen/qwen3-235b-a22b` returns 0 endpoints; `qwen/qwen3-235b-a22b-2507` has 5 providers and `qwen/qwen3-235b-a22b-thinking-2507` has 1 (Venice) — [2507 endpoints](https://openrouter.ai/api/v1/models/qwen/qwen3-235b-a22b-2507/endpoints); [thinking-2507 endpoints](https://openrouter.ai/api/v1/models/qwen/qwen3-235b-a22b-thinking-2507/endpoints)
- `deepseek/deepseek-chat` (DeepSeek V3, Dec 2024) is still live with 2 providers (DeepInfra, SambaNova). The current DeepSeek chat line is `deepseek/deepseek-v4.1-flash` (30 providers, released Sep 10, 2026) and the `deepseek/deepseek-v4.1-flash-1017` snapshot (26 providers, Oct 17, 2026). `deepseek/deepseek-v3.2` has 12 providers — [deepseek-chat endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-chat/endpoints); [v4.1-flash endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints); [models listing q=deepseek](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=deepseek)
- `z-ai/glm-4.5` has one provider (Z.AI) and its card says "Going away December 31, 2026". `z-ai/glm-4.6` has 4 providers. The current GLM slugs are `z-ai/glm-5.3` (37 providers, 48 endpoints) and `z-ai/glm-5.3-flash` (30 providers) — [glm-4.5 card](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=glm-4.5); [glm-5.3 endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints)
- `moonshotai/kimi-k2` (0711) and `moonshotai/kimi-k2-0905` each have one provider (Novita); `kimi-k2-thinking` has 2 (Google, Novita); the newest Kimi is `moonshotai/kimi-k3` (20 providers, "2.8T parameter open-weight multimodal reasoning model") — [kimi-k2 endpoints](https://openrouter.ai/api/v1/models/moonshotai/kimi-k2/endpoints); [kimi listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=kimi)
- The newest Mistral Small is `mistralai/mistral-small-2603` ("Mistral Small 4", 1 provider: Mistral). Its card says it unifies Magistral, Pixtral and Devstral; no standalone `magistral` slug exists in the models list. The newest Mistral Medium is `mistralai/mistral-medium-3-5` (1 provider: Mistral; card says "available under open weights") — [mistral listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=mistral); [models API](https://openrouter.ai/api/v1/models)
- `qwen/qwen3-coder` (480B A35B) has 3 providers. The newest open Qwen coder is `qwen/qwen3-coder-next` (80B A3B, open-weight, 1 provider: Parasail). `qwen/qwen3-coder-flash` is proprietary ("fast and cost efficient version of their proprietary Qwen3 Coder Plus", 1 provider: Alibaba) — [qwen3-coder listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=qwen3-coder)
- `openai/gpt-oss-120b` has 22 distinct providers (24 endpoints); `openai/gpt-oss-20b` has 10 — [gpt-oss-120b endpoints](https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints); [gpt-oss-20b endpoints](https://openrouter.ai/api/v1/models/openai/gpt-oss-20b/endpoints)
- `meta-llama/llama-3.3-70b-instruct` has 10 providers; `llama-4-maverick` has 3; `llama-4-scout` has 2 — [llama-3.3 endpoints](https://openrouter.ai/api/v1/models/meta-llama/llama-3.3-70b-instruct/endpoints)
- Method: provider counts are distinct `provider_name` values in each endpoints file. Some providers list several endpoints for one model (regions, fast tiers, quantizations), so endpoint counts run higher. Min and median prices use each provider's cheapest endpoint. Endpoints priced at $0 are ignored. "Price to beat" is the current minimum minus 5 percent — [endpoints API example](https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints)
- Weekly tokens come from the models listing card label "Tokens processed in the last 7 days" (it includes the in-progress day). Ranks come from the rankings page "This Week" leaderboard with "Usage data through Oct 21, 2026". The two differ by 5 to 20 percent: DeepSeek V4.1 Flash shows 27.5T on the models page and 25.7T on the rankings page — [models listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&output_modalities=text); [rankings](https://openrouter.ai/rankings)
- The rankings page counts free variants separately: "variants of the same model, such as a free variant, are ranked separately" — [rankings](https://openrouter.ai/rankings)

### Inferences
- The requested 2025-era slugs (gpt-oss, Llama 3.3 and 4, Qwen3, DeepSeek V3 and R1, GLM 4.5 and 4.6, Kimi K2) are long-tail models on OpenRouter today. Added together they carry roughly 1T tokens per week, against 27.5T for DeepSeek V4.1 Flash alone.

### Gaps
- OpenRouter's Data API (`/api/v1/datasets/rankings-daily`) needs an API key; a keyless request returned HTTP 401. Exact daily token counts are therefore not available. Weekly volumes are the three-significant-figure values shown on the public pages — [Data API docs](https://openrouter.ai/docs/cookbook/administration/data-api)
- The rankings page shows only the top 20 models for the week. Models below that are recorded as ">20".
- `qwen/qwen3.8-2.4t-a95b` did not appear in the visible part of the Qwen listing, so its weekly volume is unknown.

## Which models have 3 or fewer providers?

### Takeaway
22 of the 56 models with live endpoints have 3 or fewer distinct providers, but nearly all of them are low-volume (under 30B tokens per week). The thin-provider models with real volume sit just above that cutoff: Tencent Hy4 preview (4 providers, 9.7T per week), StepFun Step 5 Preview (4, 2.96T), Tencent Hy3 (5, 3.49T) and Xiaomi MiMo-V2.6-Pro (5, 1.73T).

### Cited Findings
- One provider (13 models): `moonshotai/kimi-k2` (Novita, 1.86B tokens per week), `moonshotai/kimi-k2-0905` (Novita, 3.09B), `z-ai/glm-4.5` (Z.AI, 1.4B), `qwen/qwen3-235b-a22b-thinking-2507` (Venice, 670M), `qwen/qwen3-coder-next` (Parasail, 27.9B), `qwen/qwen3-coder-flash` (Alibaba, proprietary, 1.65B), `qwen/qwen3.8-flash` (Alibaba, 717B), `mistralai/mistral-small-2603` (Mistral, 5.03B), `mistralai/mistral-medium-3.1` (Mistral, 5.08B), `mistralai/mistral-medium-3-5` (Mistral, 3.19B), `minimax/minimax-m3.1-flash` (Minimax, 8.32B paid; the card says "Open weights are planned"), `z-ai/glm-5.3-flashx` (Z.AI, 158B), `meta/muse-spark-1.3-contributor` (Meta, closed weights, 3.41T) — per-model endpoints files and the models listing (see summary table below)
- Two providers (3 models): `deepseek/deepseek-chat` (DeepInfra, SambaNova; 19.3B), `meta-llama/llama-4-scout` (22.9B), `moonshotai/kimi-k2-thinking` (Google, Novita; 3.44B) — [llama-4-scout endpoints](https://openrouter.ai/api/v1/models/meta-llama/llama-4-scout/endpoints); [kimi-k2-thinking endpoints](https://openrouter.ai/api/v1/models/moonshotai/kimi-k2-thinking/endpoints)
- Three providers (6 models): `deepseek/deepseek-r1-0528` (13.8B), `meta-llama/llama-4-maverick` (19.3B), `nvidia/nemotron-3-ultra-550b-a55b` paid slug (35.2B; its free variant carries 5.02T), `nvidia/nemotron-3-super-120b-a12b` (11.7B), `qwen/qwen3-32b` (13.3B), `qwen/qwen3-coder` (18B) — [qwen3-32b endpoints](https://openrouter.ai/api/v1/models/qwen/qwen3-32b/endpoints); [nemotron listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=nemotron-3)
- Four providers: `tencent/hy4-preview` (DeepInfra, Novita, SiliconFlow, Tencent; 9.7T per week; all four post the same $0.834 in / $2.501 out), `stepfun/step-5-preview` (DeepInfra, Featherless, InferenceNet, StepFun; 2.96T; all four post $1.00 / $2.70), `mistralai/mistral-small-3.2-24b-instruct` (32.8B), `z-ai/glm-4.6` (20.3B) — [hy4-preview endpoints](https://openrouter.ai/api/v1/models/tencent/hy4-preview/endpoints); [step-5-preview endpoints](https://openrouter.ai/api/v1/models/stepfun/step-5-preview/endpoints)
- Five providers: `tencent/hy3` (Tencent, Novita, GMICloud, Phala, AtlasCloud; 3.49T; floor $0.132 / $0.528), `xiaomi/mimo-v2.6-pro` (1.73T; floor $0.387 / $0.783 at DeepInfra), `qwen/qwen3-235b-a22b-2507` (63.7B), `deepseek/deepseek-chat-v3.1` (54.3B), `moonshotai/kimi-k2.5` (35.4B), `minimax/minimax-m2.7` (33.3B) — [hy3 endpoints](https://openrouter.ai/api/v1/models/tencent/hy3/endpoints); [mimo-v2.6-pro endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-pro/endpoints)
- Hy4 preview is open-weight: the models API lists `hugging_face_id: tencent/Hy4-preview`, and the card describes "49B active parameters out of 770B total". Hy3 lists `tencent/Hy3` (295B total, 21B active). Step 5 Preview lists `stepfun-ai/Step-5-Preview` (27B active / 600B total). MiMo-V2.6-Pro lists `XiaomiMiMo/MiMo-V2.6-Pro-RL` ("over 1T parameters") — [models API](https://openrouter.ai/api/v1/models); [models listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&output_modalities=text)

### Inferences
- Low provider counts on the old slugs reflect dead demand, not an opening. The single-provider Kimi K2 and GLM 4.5 slugs carry 1 to 3B tokens per week, which is under $10K per week of gross revenue at posted prices.
- The four-provider models with trillions of weekly tokens (Hy4 preview, Step 5 Preview) are the real thin spots. Each of their providers handles 0.7T to 2.4T tokens per week, which is 5 to 25 times the per-provider load on DeepSeek V4.1 Flash.

### Gaps
- The endpoints API does not expose per-provider traffic share. Only the model web pages show a "Token share 1d" column per provider, and only the gpt-oss-120b page was read in full.

## Which models have the highest median output price?

### Takeaway
Kimi K3 is the outlier: a $5.50 floor and a $14.13 median output price across 20 providers while carrying 1.96T tokens per week. Below it, the expensive open models are Mistral Medium 3.5 ($7.50, single provider), Qwen3.8 2.4T ($6.00, five providers at the same price), Muse Spark Open ($4.25, six providers at the same price) and GLM 5.3 ($4.20 median, 37 providers, but a $1.40 floor).

### Cited Findings
- `moonshotai/kimi-k3`: min out $5.50 (Sail Research), median $14.125, max $17.25 over 20 providers; min in $0.239, median in $2.325. Chutes posts $1.85 / $9.50 (mxfp4), Fireworks $2.10 / $10.50 base and $4.50 / $22.50 fast tier, Together and BaseTen $3.00 / $15.00 — [kimi-k3 endpoints](https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints)
- `mistralai/mistral-medium-3-5`: $1.50 / $7.50, one provider (Mistral), 3.19B tokens per week — [endpoints](https://openrouter.ai/api/v1/models/mistralai/mistral-medium-3-5/endpoints)
- `qwen/qwen3.8-2.4t-a95b`: $2.00 / $6.00 at all five providers (Alibaba, Novita, SiliconFlow, Together, Venice) — [endpoints](https://openrouter.ai/api/v1/models/qwen/qwen3.8-2.4t-a95b/endpoints)
- `meta/muse-spark-open` (816B A42B, open-weight per `hugging_face_id: meta-models/Muse-Spark-Open-816B-A42B`): $1.25 / $4.25 at all six providers (BaseTen, Fireworks, Makora, Modal, Nebius, Together); 118B tokens per week — [endpoints](https://openrouter.ai/api/v1/models/meta/muse-spark-open/endpoints); [muse listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=muse-spark)
- `z-ai/glm-5.3`: floor $0.079 / $1.40 (Wafer), median $0.98 / $4.20, max $2.10 / $6.60 (Fireworks fast, BaseTen fast, ModelRun); Z.AI's own endpoint is $1.40 / $4.40 — [endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints)
- `deepseek/deepseek-v4-pro-0813`: floor $0.146 / $0.487 (Baidu), median $0.99 / $3.80, max out $8.00 over 21 providers; 1.09T tokens per week — [endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro-0813/endpoints)
- Other medians above $2.40 out: `moonshotai/kimi-k2.6` $3.50 (floor $1.892 at Baidu), `qwen/qwen3-235b-a22b-thinking-2507` $3.50 (1 provider), `z-ai/glm-5` $2.875, `moonshotai/kimi-k2.5` $2.85, `stepfun/step-5-preview` $2.70, `deepseek/deepseek-v4-pro` $2.60, `tencent/hy4-preview` $2.501, `moonshotai/kimi-k2-thinking` and `kimi-k2-0905` $2.50 — summary table below
- For contrast, the cheapest floors on high-volume models: `z-ai/glm-5.3-flash` $0.0052 / $0.145, `deepseek/deepseek-v4-flash-0731` $0.0422 / $0.1333 (Baidu), `deepseek/deepseek-v4.1-flash` $0.07 / $0.18 (Decart), `openai/gpt-oss-120b` $0.03 / $0.15 (Near AI, Venice) — [glm-5.3-flash endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints); [v4-flash-0731 endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-flash-0731/endpoints)

### Inferences
- Where every provider posts the same price (Hy4 preview, Step 5 Preview, Qwen3.8 2.4T, Muse Spark Open), the price is the model author's list price and the hosts are reselling at it. There is no price competition yet, so a new host that undercuts by 5 percent becomes the floor at once.
- Kimi K3's spread (floor $5.50, max $17.25) shows that providers can hold a 3x price gap on the same open model when few hosts can run a 2.8T-parameter checkpoint.

### Gaps
- None of the pages state why Kimi K3 output is priced at $5.50 to $17.25; the model card only says it is a 2.8T-parameter model.

## Which models carry the most weekly tokens, and how many providers share that volume?

### Takeaway
Open-weight models fill 13 of the top 20 weekly slots. DeepSeek V4.1 Flash (27.5T, 30 providers) and its 1017 snapshot (20T, 26 providers) lead, followed by GLM 5.3 Flash (12.4T, 30 providers). The best volume-per-provider ratios are Hy4 preview (2.4T per provider), MiMo-V2.6-Flash (1.0T), DeepSeek V4.1 Flash (0.9T), Step 5 Preview (0.74T) and Hy3 (0.70T).

### Cited Findings
- Weekly leaderboard ("This Week", usage data through Oct 21, 2026): 1 DeepSeek V4.1 Flash 25.7T (-31%); 2 DeepSeek V4.1 Flash 1017 16.5T (new); 3 GLM 5.3 Flash 11.3T (-12%); 4 MiniMax M3.1 Flash (free) 10.3T (new); 5 MiMo-V2.6-Flash 8.57T (-25%); 6 Hy4 preview 8.55T (+9%); 7 Claude Opus 5.5 7.14T; 8 GPT-6 Luna 6.08T; 9 GLM 5.3 5.21T (+18%); 10 Nemotron 3 Ultra (free) 4.46T (-40%); 11 DeepSeek V4 Flash 0731 4.29T (-9%); 12 Muse Spark 1.3 Contributor 3.18T; 13 Hy3 3.09T (-4%); 14 Jev 1.13 (typesafe router) 2.93T; 15 DeepSeek V4 Flash 0423 2.77T (-12%); 16 Claude Sonnet 5.5 2.53T; 17 Step 5 Preview 2.32T (-88%); 18 Claude Haiku 5.5 2.09T; 19 GPT-6.1 Sol 1.98T; 20 Kimi K3 1.72T (-35%) — [rankings](https://openrouter.ai/rankings)
- Closed or non-open entries in that top 20: Claude Opus 5.5, GPT-6 Luna, Muse Spark 1.3 Contributor (Meta only, no Hugging Face id), Jev 1.13 (a TypeSafe router, 0 endpoints on the API), Claude Sonnet 5.5, Claude Haiku 5.5, GPT-6.1 Sol. MiniMax M3.1 Flash's card says "Open weights are planned" — [models API](https://openrouter.ai/api/v1/models); [minimax listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=minimax)
- Providers sharing the volume (distinct providers from the endpoints API; weekly tokens from the models listing): DeepSeek V4.1 Flash 30 providers for 27.5T (917B each); V4.1 Flash 1017 26 for 20T (769B); GLM 5.3 Flash 30 for 12.4T (413B); Hy4 preview 4 for 9.7T (2.42T); MiMo-V2.6-Flash 9 for 9.12T (1.01T); GLM 5.3 37 for 5.73T (155B); DeepSeek V4 Flash 0731 23 for 4.63T (201B); Hy3 5 for 3.49T (698B); DeepSeek V4 Flash 0423 15 for 3.02T (201B); Step 5 Preview 4 for 2.96T (740B); Kimi K3 20 for 1.96T (98B); MiMo-V2.6-Pro 5 for 1.73T (346B); MiniMax M3 13 for 1.47T (113B); DeepSeek V4 Pro 0813 21 for 1.09T (52B) — summary table below
- Next tier (hundreds of billions per week): Qwen3.6 35B A3B 785B (10 providers), Qwen3.8 Flash 717B (1), DeepSeek V4 Pro 0423 685B (15), Gemma 4 31B 613B (12), gpt-oss-120b 568B (22), Qwen3.8 27B 485B (20), DeepSeek V3.2 303B (12), gpt-oss-20b 217B (10), GLM 5.3 FlashX 158B (1), Kimi K2.6 144B (17), Muse Spark Open 118B (6) — [gpt-oss listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=gpt-oss); [qwen3 listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=qwen3); [gemma listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=gemma-4)
- Requested legacy models: Llama 3.3 70B 39.1B per week (10 providers), Qwen3 235B A22B 2507 63.7B (5), Llama 4 Scout 22.9B (2), Llama 4 Maverick 19.3B (3), Qwen3 Coder 480B 18B (3), DeepSeek R1 0528 13.8B (3), Qwen3 32B 13.3B (3), Mistral Small 3.2 32.8B (4), GLM 4.6 20.3B (4), GLM 4.5 1.4B (1), Kimi K2 0905 3.09B (1) — [llama listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=llama); [qwen3-32b card](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=qwen3-32b); [deepseek-r1 card](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=deepseek-r1)
- Market share of text requests by author, week beginning Oct 12, 2026: DeepSeek 24.4%, Google 19.7%, OpenAI 18.5%, Z.ai 12.2%, Qwen 5.3%, Anthropic 4.7%, Xiaomi 2.4%, Meta Llama 2.1%, Mistral AI 2.0%, all others 8.6% — [rankings](https://openrouter.ai/rankings)
- Top apps by tokens today: Claude Code 2.11T, Hermes Agent 2.07T, Kilo Code 1.49T, pi 651B, DeepSeek Harness 575B — [rankings](https://openrouter.ai/rankings)
- On the gpt-oss-120b page the Activity panel shows Prompt 34B, Reasoning 2.13B and Completion 1.13B tokens, so about 91 percent of that model's tokens are prompt tokens — [gpt-oss-120b page](https://openrouter.ai/openai/gpt-oss-120b)

### Inferences
- Rough weekly gross revenue pools (weekly tokens times the floor input price; a lower bound because output tokens cost more, and a fair proxy because prompt tokens dominate): Hy4 preview about $8.1M, Step 5 Preview about $3.0M, DeepSeek V4.1 Flash about $1.9M, MiMo-V2.6-Flash about $0.9M, MiMo-V2.6-Pro about $0.67M, Hy3 about $0.46M, GLM 5.3 about $0.45M, Kimi K3 about $0.47M at the input floor but about $10.8M at the output floor, gpt-oss-120b about $17K to $85K, Llama 3.3 70B about $4K to $13K, Qwen3 32B about $1K to $4K. These are totals across all providers, not what a new entrant would capture.
- Volume moves fast between snapshots: V4.1 Flash fell 31 percent in a week while the 1017 snapshot appeared at 16.5T. Hosts that bring up new snapshots within days get traffic; hosts on old slugs lose it.
- Free variants (MiniMax M3.1 Flash free 10.3T, Nemotron 3 Ultra free 4.46T, Nemotron 3.5 Super VL free 1.39T) are promotional traffic paid for by the model author or a sponsor, not a revenue pool.

### Gaps
- Weekly volumes for `qwen/qwen3.8-2.4t-a95b` and for ranks below 20 are not shown; per-provider traffic shares are only visible on each model's web page and were read only for gpt-oss-120b.

## What price would a new provider need to post to be the cheapest?

### Takeaway
The floor is already near zero on the crowded models (gpt-oss-120b $0.03 / $0.15, GLM 5.3 Flash $0.0052 / $0.145, DeepSeek V4 Flash 0731 $0.042 / $0.133), so undercutting there buys little. The floors with room are the list-price models: Hy4 preview (beat $0.792 / $2.376), Step 5 Preview ($0.95 / $2.565), Hy3 ($0.125 / $0.502), MiMo-V2.6-Pro ($0.368 / $0.744), Kimi K3 ($0.227 / $5.225) and Muse Spark Open ($1.19 / $4.04).

### Cited Findings
- Current minimum and "price to beat" (minimum minus 5 percent), USD per million tokens, from the endpoints API checked 2026-10-22:

| Model | Min in | Min out | Cheapest provider(s) | Price to beat in / out | Median in / out |
|---|---|---|---|---|---|
| tencent/hy4-preview | 0.834 | 2.501 | DeepInfra, Novita, SiliconFlow, Tencent (tie) | 0.792 / 2.376 | 0.834 / 2.501 |
| stepfun/step-5-preview | 1.00 | 2.70 | DeepInfra, Featherless, InferenceNet, StepFun (tie) | 0.95 / 2.565 | 1.00 / 2.70 |
| tencent/hy3 | 0.132 | 0.528 | Tencent | 0.125 / 0.502 | 0.14 / 0.58 |
| xiaomi/mimo-v2.6-flash | 0.10 | 0.266 | DeepInfra | 0.095 / 0.253 | 0.14 / 0.28 |
| xiaomi/mimo-v2.6-pro | 0.387 | 0.783 | DeepInfra | 0.368 / 0.744 | 0.435 / 0.87 |
| deepseek/deepseek-v4.1-flash | 0.07 | 0.18 | Decart | 0.0665 / 0.171 | 0.2025 / 0.81 |
| deepseek/deepseek-v4.1-flash-1017 | 0.07 | 0.15 | Sail Research | 0.0665 / 0.1425 | 0.2075 / 0.69 |
| z-ai/glm-5.3-flash | 0.0052 | 0.145 | StreamLake (out) | 0.0049 / 0.138 | 0.15 / 0.50 |
| z-ai/glm-5.3 | 0.079 | 1.40 | Wafer | 0.075 / 1.33 | 0.98 / 4.20 |
| moonshotai/kimi-k3 | 0.239 | 5.50 | Sail Research | 0.227 / 5.225 | 2.325 / 14.125 |
| minimax/minimax-m3 | 0.224 | 0.88 | DeepInfra | 0.213 / 0.836 | 0.30 / 1.20 |
| meta/muse-spark-open | 1.25 | 4.25 | all six (tie) | 1.1875 / 4.0375 | 1.25 / 4.25 |
| openai/gpt-oss-120b | 0.03 | 0.15 | Near AI, Venice | 0.0285 / 0.1425 | 0.095 / 0.46 |
| openai/gpt-oss-20b | 0.018 | 0.09 | Darkbloom | 0.0171 / 0.0855 | 0.03 / 0.145 |
| meta-llama/llama-3.3-70b-instruct | 0.10 | 0.32 | DeepInfra | 0.095 / 0.304 | 0.3715 / 0.715 |
| qwen/qwen3-32b | 0.08 | 0.28 | DeepInfra | 0.076 / 0.266 | 0.14 / 0.40 |
| qwen/qwen3-coder | 0.22 | 1.00 | DeepInfra | 0.209 / 0.95 | 0.30 / 1.50 |
| qwen/qwen3-coder-next | 0.12 | 0.80 | Parasail (only) | 0.114 / 0.76 | 0.12 / 0.80 |
| qwen/qwen3-235b-a22b-2507 | 0.0875 | 0.35 | GMICloud | 0.083 / 0.3325 | 0.14 / 0.75 |
| deepseek/deepseek-r1-0528 | 0.50 | 2.15 | DeepInfra | 0.475 / 2.0425 | 0.50 / 2.18 |
| deepseek/deepseek-v3.2 | 0.07 | 0.105 | Baidu | 0.0665 / 0.0997 | 0.284 / 0.88 |
| meta-llama/llama-4-maverick | 0.1875 | 0.6525 | DigitalOcean | 0.178 / 0.62 | 0.35 / 1.00 |
| meta-llama/llama-4-scout | 0.08 | 0.24 | DeepInfra | 0.076 / 0.228 | 0.165 / 0.47 |
| mistralai/mistral-small-3.2-24b-instruct | 0.075 | 0.20 | DeepInfra | 0.071 / 0.19 | 0.092 / 0.275 |
| mistralai/mistral-small-2603 | 0.15 | 0.60 | Mistral (only) | 0.1425 / 0.57 | 0.15 / 0.60 |
| mistralai/mistral-medium-3-5 | 1.50 | 7.50 | Mistral (only) | 1.425 / 7.125 | 1.50 / 7.50 |
| moonshotai/kimi-k2-0905 | 0.60 | 2.50 | Novita (only) | 0.57 / 2.375 | 0.60 / 2.50 |
| z-ai/glm-4.6 | 0.40 | 1.60 | DeepInfra | 0.38 / 1.52 | 0.49 / 1.975 |
| google/gemma-4-31b-it | 0.10 | 0.32 | DeepInfra | 0.095 / 0.304 | 0.145 / 0.40 |

Source: the per-model endpoints files, for example [hy4-preview](https://openrouter.ai/api/v1/models/tencent/hy4-preview/endpoints), [gpt-oss-120b](https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints), [kimi-k3](https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints). Checked 2026-10-22. The full list is in the summary table at the end.

- Being the cheapest does not win the traffic. On gpt-oss-120b the weighted average price customers actually paid was $0.1006 in and $0.3853 out, against a $0.03 / $0.15 floor. The two $0.03 / $0.15 endpoints had 0.8% and 7.2% of the last day's tokens; a $0.09 / $0.36 endpoint had 24.5% and a $0.15 / $0.60 endpoint had 18.5% — [gpt-oss-120b page](https://openrouter.ai/openai/gpt-oss-120b)
- OpenRouter routes by the mode the caller picks: "Balanced (price + speed), Nitro (fastest), or Floor (cheapest)" — [gpt-oss-120b page](https://openrouter.ai/openai/gpt-oss-120b)
- The fastest gpt-oss-120b providers over the past week were Cerebras (806 tok/s average, $0.35 / $0.75), SambaNova (333 tok/s, $0.14 / $0.95) and Groq (313 tok/s, $0.15 / $0.60); the cheapest endpoints ran at 24 to 33 tok/s — [gpt-oss-120b page](https://openrouter.ai/openai/gpt-oss-120b); [endpoints](https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints)

### Inferences
- A 5 percent undercut on a crowded, near-zero floor (gpt-oss-120b at $0.0285 / $0.1425) earns the "Floor" routing slot only, which the live share data shows is a small minority of traffic. Throughput and uptime decide the Balanced and Nitro traffic.
- On the list-price models (Hy4 preview, Step 5 Preview, Muse Spark Open, Qwen3.8 2.4T) a 5 percent cut would make a new host the only sub-list-price option, which stands out on a model page where every other row shows the same number.

### Gaps
- Per-provider token share and throughput were read for gpt-oss-120b only. The same "Token share 1d" column exists on every model page but was not collected for the other models.

## Which providers appear most often, and what are their typical prices?

### Takeaway
DeepInfra is on 34 of the 56 models and posts the cheapest output price on 18 of them; its median output price equals the floor. Novita (27 models, 1.36x floor), Venice (26, 1.46x), SiliconFlow (21, 2.0x), Parasail (21, 2.0x) and GMICloud (18, 1.44x) follow. The big-name GPU clouds are rarer and pricier: Together 12 models at 3.2x floor, BaseTen 9 at 3.1x, Crusoe 8 at 3.3x, Fireworks 6 at 2.8x, SambaNova 6 at 3.2x, Groq 4 at 2.9x, Nebius 4 at 3.6x, Cerebras 2 at 3.1x. Hyperbolic and Lambda host none of these 56 models.

### Cited Findings
- Provider presence and pricing position across the 56 models with live endpoints (median of provider output price divided by that model's cheapest output price): DeepInfra 34 models, cheapest 18 times, 1.00x; Novita 27, 5, 1.36x; Venice 26, 4, 1.46x; SiliconFlow 21, 3, 2.04x; Parasail 21, 1, 2.00x; GMICloud 18, 3, 1.44x; AtlasCloud 16, 1, 2.56x; CoreWeave 14, 0, 1.95x; StreamLake 13, 3, 1.33x; DigitalOcean 13, 1, 2.35x; Phala 13, 0, 2.93x; Together 12, 2, 3.20x; Alibaba 12, 3, 2.90x; Google (Vertex) 11, 1, 2.40x; Baidu 10, 5, 1.08x; Relace 10, 0, 1.95x; BaseTen 9, 1, 3.14x; Wafer 9, 1, 1.84x; Cloudflare 9, 0, 4.00x; Crusoe 8, 0, 3.30x; SambaNova 6, 0, 3.20x; Fireworks 6, 1, 2.82x; Amazon Bedrock 6, 0, 2.20x; Nebius 4, 1, 3.57x; Chutes 4, 1, 1.09x; Groq 4, 0, 2.90x; Darkbloom 4, 2, 1.03x; Cerebras 2, 0, 3.10x; Hyperbolic 0; Lambda 0 — computed by `analyze_openrouter.py` from the endpoints files; full table at the end
- Quantization by provider: DeepInfra posts bf16, fp4, fp8 and mxfp4 endpoints; Novita bf16, fp4, fp8; Venice fp4, fp8, int4; Parasail bf16, fp4, fp8, int4; CoreWeave fp16, fp4, fp8, nvfp4; Cerebras fp16; Together, Fireworks, Groq, SambaNova and Google report quantization as unknown — provider table at the end
- Example absolute prices on gpt-oss-120b (in / out): Near AI $0.03 / $0.15 (fp4), Venice $0.03 / $0.15 (int4), CoreWeave $0.03 / $0.17, DekaLLM $0.03 / $0.18 (bf16), Crusoe $0.05 / $0.25 (bf16), BaseTen $0.10 / $0.50, SambaNova $0.14 / $0.95, Groq, Together and Nebius $0.15 / $0.60, Cerebras $0.35 / $0.75 (fp16) — [endpoints](https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints)
- Example absolute prices on GLM 5.3 Flash: BaseTen, Crusoe, Fireworks and Together all $0.15 / $0.50; floor $0.0052 / $0.145 — [endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints)
- Example absolute prices on DeepSeek V4.1 Flash: Fireworks $0.21 / $0.84, Crusoe $0.29 / $1.20 (fp8), Nebius, BaseTen and Together $0.30 / $1.20; floor $0.07 / $0.18 (Decart) — [endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints)
- Example absolute prices on Llama 3.3 70B: DeepInfra $0.10 / $0.32 (floor), SambaNova $0.45 / $0.90, Groq $0.59 / $0.79, Together $1.04 / $1.04 — [endpoints](https://openrouter.ai/api/v1/models/meta-llama/llama-3.3-70b-instruct/endpoints)
- Groq hosts only gpt-oss-120b ($0.15 / $0.60), gpt-oss-20b ($0.075 / $0.30), Llama 3.3 70B and MiniMax M2.7 ($0.60 / $1.80) among these models; Cerebras hosts gpt-oss-120b and Qwen3.8 27B ($0.99 / $1.49) — endpoints files
- Model-author first-party endpoints are often not the floor: Z.AI posts $1.40 / $4.40 on GLM 5.3 against a $0.079 / $1.40 floor; Tencent posts the floor on Hy3 and ties on Hy4 preview; Mistral is the only host on its three models — [glm-5.3 endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints); [hy3 endpoints](https://openrouter.ai/api/v1/models/tencent/hy3/endpoints)

### Inferences
- DeepInfra's strategy is to be on everything at the floor. A new small provider cannot out-price DeepInfra on breadth; it can only pick models DeepInfra has not listed or where DeepInfra is not the floor (DeepSeek V4.1 Flash, GLM 5.3, Kimi K3, Hy3, the Mistral and Alibaba-only slugs).
- The large GPU clouds (Together, Fireworks, BaseTen, Crusoe, Nebius) price at roughly 3x the floor and still hold their listings, which suggests they sell on speed, uptime and enterprise routing rather than price.

### Gaps
- Hyperbolic and Lambda were absent from every endpoints file checked; whether they host other OpenRouter models was not verified.

## Where are the openings for a new small inference provider?

### Takeaway
The clearest openings are the high-volume Chinese MoE models with four or five hosts that all post the author's list price: Tencent Hy4 preview (9.7T per week, 4 hosts, $0.834 / $2.501), Tencent Hy3 (3.49T, 5 hosts, $0.132 / $0.528), StepFun Step 5 Preview (2.96T, 4 hosts, $1.00 / $2.70, but falling 88 percent week over week) and Xiaomi MiMo-V2.6-Pro (1.73T, 5 hosts). The requested legacy models (gpt-oss, Llama 3.3, Qwen3 32B) are easy to serve on one or two GPUs but their whole OpenRouter revenue pool is a few thousand dollars per week.

### Cited Findings
- Hy4 preview: 770B total / 49B active, open weights on Hugging Face, 9.7T tokens per week (+9% week over week on the rankings page), 4 providers all at $0.834 / $2.501, 1.05M context — [card](https://openrouter.ai/models?order=top-weekly&fmt=cards&output_modalities=text); [endpoints](https://openrouter.ai/api/v1/models/tencent/hy4-preview/endpoints); [rankings](https://openrouter.ai/rankings)
- Hy3: 295B total / 21B active, open weights, 3.49T per week (-4%), 5 providers, floor $0.132 / $0.528 at Tencent, median $0.14 / $0.58, 262K context — [endpoints](https://openrouter.ai/api/v1/models/tencent/hy3/endpoints)
- Step 5 Preview: 600B total / 27B active, `hugging_face_id: stepfun-ai/Step-5-Preview`, 2.96T per week but -88% on the rankings page, 4 providers all at $1.00 / $2.70 — [endpoints](https://openrouter.ai/api/v1/models/stepfun/step-5-preview/endpoints); [rankings](https://openrouter.ai/rankings)
- MiMo-V2.6-Flash: 309B total / 15B active, open weights, 9.12T per week (-25%), 9 providers, floor $0.10 / $0.266 (DeepInfra), median $0.14 / $0.28 — [endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-flash/endpoints); [mimo listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=mimo)
- MiMo-V2.6-Pro: over 1T parameters, open weights, 1.73T per week, 5 providers, floor $0.387 / $0.783 — [endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-pro/endpoints)
- gpt-oss-120b is "optimized to run on a single H100 GPU with native MXFP4 quantization"; 22 providers; 568B tokens per week; floor $0.03 / $0.15; weighted average paid $0.1006 / $0.3853 — [gpt-oss-120b page](https://openrouter.ai/openai/gpt-oss-120b)
- Qwen3 Coder Next (80B A3B, open-weight, "non-thinking", 262K context) has a single host, Parasail, at $0.12 / $0.80 and 27.9B tokens per week — [endpoints](https://openrouter.ai/api/v1/models/qwen/qwen3-coder-next/endpoints); [card](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=qwen3-coder)
- Mistral Medium 3.5 (dense 128B, "self-hostable on as few as four GPUs and available under open weights") has a single host, Mistral, at $1.50 / $7.50 and 3.19B tokens per week — [mistral listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=mistral); [endpoints](https://openrouter.ai/api/v1/models/mistralai/mistral-medium-3-5/endpoints)
- Nemotron 3 Ultra (550B A55B, open weights) has 3 paid providers (floor DeepInfra $0.40 / $1.76, BaseTen $0.60 / $2.40) and only 35.2B paid tokens per week, while its free variant carries 5.02T — [endpoints](https://openrouter.ai/api/v1/models/nvidia/nemotron-3-ultra-550b-a55b/endpoints); [nemotron listing](https://openrouter.ai/models?order=top-weekly&fmt=cards&q=nemotron-3)

### Inferences
- Ranked openings for a small provider, judged on volume per host, price headroom and hardware need:
  1. Hy4 preview. Largest pool (about $8M per week at the input floor) split four ways, no price competition yet. Needs an 8-GPU node with roughly 770 GB of fp8 weights (8x H200 class). Price to beat: $0.792 / $2.376.
  2. Hy3. About $0.46M per week pool, five hosts, 295B parameters fit in fp8 on a single 8x H100 node with room for KV cache. Price to beat: $0.125 / $0.502.
  3. MiMo-V2.6-Flash. Largest raw volume among the thin-host models (9.12T), nine hosts, 309B parameters, floor already low at $0.10 / $0.266. Compete on throughput, not price.
  4. Step 5 Preview. Big pool but the 88 percent weekly drop says traffic is leaving; treat as short-lived.
  5. Single-host open models (Qwen3 Coder Next, Mistral Medium 3.5, Kimi K2 0905). Easy to become the second host, but each pool is under $25K per week.
  6. Legacy small models (gpt-oss-120b, gpt-oss-20b, Llama 3.3 70B, Qwen3 32B, Mistral Small 3.2). One or two GPUs each, but 10 to 22 hosts already and total pools of $1K to $85K per week; the floor is held by DeepInfra, Near AI, Venice and Darkbloom at $0.03 or less per million input tokens.
- Kimi K3 is the only high-price, high-volume open model, but a 2.8T-parameter checkpoint needs well over 1 TB of GPU memory even at 4-bit, which puts it out of reach for a small host.
- Across every model, the price floor is set by a handful of low-cost hosts (DeepInfra, Baidu, StreamLake, Darkbloom, Chutes, Near AI, Venice) that run fp4 or fp8. A new host that wants Balanced-routing traffic needs competitive tokens per second and uptime more than a lower price.

### Gaps
- GPU memory estimates above are inferred from parameter counts in the model cards; the cards do not state serving requirements, and no provider publishes its hardware.
- Week-over-week change figures come from the rankings page and are only shown for the top 20, so trend data for the thinner models is missing.
- The notes do not cover OpenRouter's provider onboarding terms, revenue share, or minimum uptime requirements; those pages were out of scope.

## Full data tables

### Takeaway
The tables below are generated by `analyze_openrouter.py` from the raw endpoint JSON saved on 2026-10-22. The summary table covers all 58 slugs fetched (56 with live endpoints), the provider table covers every provider seen, and one detail table per model lists every endpoint with its tag, quantization, context, max output, prices, cache-read price, one-day uptime and status flag.

### Cited Findings
Source for every row: `https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints` (checked 2026-10-22); weekly tokens from `https://openrouter.ai/models?order=top-weekly` and rank from `https://openrouter.ai/rankings` (checked 2026-10-22).

#### Summary table across models

Sources: https://openrouter.ai/api/v1/models and https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints for prices, counts, context; https://openrouter.ai/rankings and https://openrouter.ai/models?order=top-weekly for weekly tokens and rank. All checked 2026-10-22. Prices in USD per million tokens. Min and median are computed over distinct providers, using each provider's cheapest endpoint. Endpoints priced at $0 are ignored. 'Price to beat' is the current minimum minus 5 percent.

| Model | Providers | Endpoints | Context | Min in | Median in | Min out | Median out | Max out | Cheapest provider(s) | Price to beat (in / out) | Weekly tokens | Weekly rank | Tokens per provider |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepseek/deepseek-v4.1-flash | 30 | 38 | 1048576 | 0.07 | 0.2025 | 0.18 | 0.81 | 1.2 | Decart | 0.0665 / 0.171 | 27.5T | 1 | 917B |
| deepseek/deepseek-v4.1-flash-1017 | 26 | 30 | 1048576 | 0.07 | 0.2075 | 0.15 | 0.69 | 1.2 | Sail Research | 0.0665 / 0.1425 | 20T | 2 | 769B |
| z-ai/glm-5.3-flash | 30 | 34 | 1048576 | 0.0052 | 0.15 | 0.145 | 0.5 | 1.6 | StreamLake | 0.0049 / 0.1377 | 12.4T | 3 | 413B |
| tencent/hy4-preview | 4 | 4 | 1048576 | 0.834 | 0.834 | 2.501 | 2.501 | 2.501 | DeepInfra, Novita, SiliconFlow, Tencent | 0.7923 / 2.3759 | 9.7T | 6 | 2.42T |
| xiaomi/mimo-v2.6-flash | 9 | 9 | 1050000 | 0.1 | 0.14 | 0.266 | 0.28 | 0.35 | DeepInfra | 0.095 / 0.2527 | 9.12T | 5 | 1.01T |
| z-ai/glm-5.3 | 37 | 48 | 1048576 | 0.079 | 0.98 | 1.4 | 4.2 | 6.6 | Wafer | 0.075 / 1.33 | 5.73T | 9 | 155B |
| deepseek/deepseek-v4-flash-0731 | 23 | 26 | 1048576 | 0.0422 | 0.14 | 0.1333 | 0.28 | 1.32 | Baidu | 0.0401 / 0.1267 | 4.63T | 11 | 201B |
| tencent/hy3 | 5 | 5 | 262144 | 0.132 | 0.14 | 0.528 | 0.58 | 0.8 | Tencent | 0.1254 / 0.5016 | 3.49T | 13 | 698B |
| meta/muse-spark-1.3-contributor | 1 | 1 | 1048576 | 0.1 | 0.1 | 0.2 | 0.2 | 0.2 | Meta | 0.095 / 0.19 | 3.41T | 12 | 3.41T |
| deepseek/deepseek-v4-flash | 15 | 15 | 1048576 | 0.05 | 0.13 | 0.14 | 0.28 | 1.32 | StreamLake | 0.0475 / 0.133 | 3.02T | 15 | 201B |
| stepfun/step-5-preview | 4 | 5 | 1048576 | 1 | 1 | 2.7 | 2.7 | 2.7 | DeepInfra, Featherless, InferenceNet, StepFun | 0.95 / 2.565 | 2.96T | 17 | 740B |
| moonshotai/kimi-k3 | 20 | 28 | 1048576 | 0.239 | 2.325 | 5.5 | 14.125 | 17.25 | Sail Research | 0.2271 / 5.225 | 1.96T | 20 | 98B |
| xiaomi/mimo-v2.6-pro | 5 | 5 | 1050000 | 0.387 | 0.435 | 0.783 | 0.87 | 1.044 | DeepInfra | 0.3676 / 0.7438 | 1.73T | >20 | 346B |
| minimax/minimax-m3 | 13 | 14 | 1048576 | 0.224 | 0.3 | 0.88 | 1.2 | 2.4 | DeepInfra | 0.2128 / 0.836 | 1.47T | >20 | 113B |
| deepseek/deepseek-v4-pro-0813 | 21 | 23 | 1048576 | 0.1461 | 0.99 | 0.4871 | 3.8 | 8 | Baidu | 0.1388 / 0.4627 | 1.09T | >20 | 51.9B |
| qwen/qwen3.6-35b-a3b | 10 | 10 | 262144 | 0.05 | 0.1 | 0.7 | 1 | 1.8 | Darkbloom | 0.0475 / 0.665 | 785B | >20 | 78.5B |
| qwen/qwen3.8-flash | 1 | 2 | 1000000 | 0.15 | 0.15 | 0.47 | 0.47 | 0.47 | Alibaba | 0.1425 / 0.4465 | 717B | >20 | 717B |
| deepseek/deepseek-v4-pro | 15 | 16 | 1048576 | 0.4411 | 1.15 | 0.8822 | 2.6 | 3.83 | Baidu | 0.419 / 0.8381 | 685B | >20 | 45.7B |
| google/gemma-4-31b-it | 12 | 15 | 262144 | 0.1 | 0.145 | 0.32 | 0.4 | 1.15 | DeepInfra | 0.095 / 0.304 | 613B | >20 | 51.1B |
| openai/gpt-oss-120b | 22 | 24 | 131072 | 0.03 | 0.095 | 0.15 | 0.46 | 0.95 | Near AI, Venice | 0.0285 / 0.1425 | 568B | >20 | 25.8B |
| qwen/qwen3.8-27b | 20 | 20 | 1000000 | 0.035 | 0.2 | 1.25 | 2.3 | 3.2 | Chutes | 0.0333 / 1.1875 | 485B | >20 | 24.2B |
| deepseek/deepseek-v3.2 | 12 | 12 | 163840 | 0.07 | 0.2841 | 0.105 | 0.88 | 4.5 | Baidu | 0.0665 / 0.0997 | 303B | >20 | 25.2B |
| openai/gpt-oss-20b | 10 | 11 | 131072 | 0.018 | 0.03 | 0.09 | 0.145 | 0.3 | Darkbloom | 0.0171 / 0.0855 | 217B | >20 | 21.7B |
| z-ai/glm-5.3-flashx | 1 | 1 | 1048576 | 0.37 | 0.37 | 1.25 | 1.25 | 1.25 | Z.AI | 0.3515 / 1.1875 | 158B | >20 | 158B |
| moonshotai/kimi-k2.6 | 17 | 17 | 262144 | 0.4493 | 0.75 | 1.892 | 3.5 | 4.6 | Baidu | 0.4269 / 1.7974 | 144B | >20 | 8.47B |
| meta/muse-spark-open | 6 | 6 | 1048576 | 1.25 | 1.25 | 4.25 | 4.25 | 4.25 | BaseTen, Fireworks, Makora, Modal, Nebius, Together | 1.1875 / 4.0375 | 118B | >20 | 19.7B |
| qwen/qwen3-235b-a22b-2507 | 5 | 6 | 262144 | 0.0875 | 0.14 | 0.35 | 0.75 | 0.88 | GMICloud | 0.0831 / 0.3325 | 63.7B | >20 | 12.7B |
| deepseek/deepseek-chat-v3.1 | 5 | 5 | 163840 | 0.25 | 0.55 | 0.95 | 1.5 | 1.7 | DeepInfra | 0.2375 / 0.9025 | 54.3B | >20 | 10.9B |
| z-ai/glm-5 | 8 | 8 | 204800 | 0.6 | 0.975 | 1.92 | 2.875 | 3.2 | GMICloud, StreamLake | 0.57 / 1.824 | 41.7B | >20 | 5.21B |
| meta-llama/llama-3.3-70b-instruct | 10 | 11 | 131072 | 0.1 | 0.3715 | 0.32 | 0.715 | 2.253 | DeepInfra | 0.095 / 0.304 | 39.1B | >20 | 3.91B |
| z-ai/glm-4.7 | 6 | 7 | 204800 | 0.32 | 0.57 | 1.4 | 2.09 | 2.5 | DeepInfra | 0.304 / 1.33 | 36.2B | >20 | 6.03B |
| moonshotai/kimi-k2.5 | 5 | 5 | 262144 | 0.49 | 0.532 | 2.5 | 2.85 | 3.325 | AtlasCloud, SiliconFlow | 0.4655 / 2.375 | 35.4B | >20 | 7.08B |
| nvidia/nemotron-3-ultra-550b-a55b | 3 | 5 | 262144 | 0.4 | 0.6 | 1.76 | 2.4 | 3.125 | DeepInfra | 0.38 / 1.672 | 35.2B | paid slug >20; :free variant is rank 10 (4.46T) | 11.7B |
| minimax/minimax-m2.7 | 5 | 6 | 204800 | 0.21 | 0.3 | 0.84 | 1.2 | 1.8 | GMICloud | 0.1995 / 0.798 | 33.3B | >20 | 6.66B |
| mistralai/mistral-small-3.2-24b-instruct | 4 | 4 | 256000 | 0.075 | 0.0919 | 0.2 | 0.275 | 0.3 | DeepInfra | 0.0712 / 0.19 | 32.8B | >20 | 8.2B |
| qwen/qwen3-coder-next | 1 | 1 | 262144 | 0.12 | 0.12 | 0.8 | 0.8 | 0.8 | Parasail | 0.114 / 0.76 | 27.9B | >20 | 27.9B |
| meta-llama/llama-4-scout | 2 | 4 | 1310720 | 0.08 | 0.165 | 0.24 | 0.47 | 0.7 | DeepInfra | 0.076 / 0.228 | 22.9B | >20 | 11.4B |
| z-ai/glm-4.6 | 4 | 5 | 204800 | 0.4 | 0.49 | 1.6 | 1.975 | 2.2 | DeepInfra | 0.38 / 1.52 | 20.3B | >20 | 5.08B |
| deepseek/deepseek-chat | 2 | 3 | 163840 | 0.256 | 0.2567 | 0.712 | 0.8703 | 1.0287 | DeepInfra | 0.2432 / 0.6764 | 19.3B | >20 | 9.65B |
| meta-llama/llama-4-maverick | 3 | 3 | 524288 | 0.1875 | 0.35 | 0.6525 | 1 | 1.15 | DigitalOcean | 0.1781 / 0.6199 | 19.3B | >20 | 6.43B |
| qwen/qwen3-coder | 3 | 3 | 262144 | 0.22 | 0.3 | 1 | 1.5 | 1.8 | DeepInfra | 0.209 / 0.95 | 18B | >20 | 6B |
| deepseek/deepseek-r1-0528 | 3 | 3 | 163840 | 0.5 | 0.5 | 2.15 | 2.18 | 2.286 | DeepInfra | 0.475 / 2.0425 | 13.8B | >20 | 4.6B |
| qwen/qwen3-32b | 3 | 3 | 131072 | 0.08 | 0.14 | 0.28 | 0.4 | 0.57 | DeepInfra | 0.076 / 0.266 | 13.3B | >20 | 4.43B |
| minimax/minimax-m2.5 | 7 | 8 | 204800 | 0.27 | 0.3 | 0.95 | 1.2 | 1.2 | Venice | 0.2565 / 0.9025 | 12.2B | >20 | 1.74B |
| nvidia/nemotron-3-super-120b-a12b | 3 | 3 | 262144 | 0.08 | 0.085 | 0.4 | 0.45 | 2.4 | DeepInfra | 0.076 / 0.38 | 11.7B | >20 (free variant 514B) | 3.9B |
| minimax/minimax-m3.1-flash | 1 | 1 | 1000000 | 0.15 | 0.15 | 0.6 | 0.6 | 0.6 | Minimax | 0.1425 / 0.57 | 8.32B | 4 is the :free variant (10.3T); paid slug not in top 20 | 8.32B |
| mistralai/mistral-medium-3.1 | 1 | 3 | 131072 | 0.4 | 0.4 | 2 | 2 | 2 | Mistral | 0.38 / 1.9 | 5.08B | >20 | 5.08B |
| mistralai/mistral-small-2603 | 1 | 4 | 262144 | 0.15 | 0.15 | 0.6 | 0.6 | 0.6 | Mistral | 0.1425 / 0.57 | 5.03B | >20 | 5.03B |
| moonshotai/kimi-k2-thinking | 2 | 2 | 262144 | 0.6 | 0.6 | 2.5 | 2.5 | 2.5 | Google, Novita | 0.57 / 2.375 | 3.44B | >20 | 1.72B |
| mistralai/mistral-medium-3-5 | 1 | 3 | 262144 | 1.5 | 1.5 | 7.5 | 7.5 | 7.5 | Mistral | 1.425 / 7.125 | 3.19B | >20 | 3.19B |
| moonshotai/kimi-k2-0905 | 1 | 1 | 262144 | 0.6 | 0.6 | 2.5 | 2.5 | 2.5 | Novita | 0.57 / 2.375 | 3.09B | >20 | 3.09B |
| moonshotai/kimi-k2 | 1 | 1 | 131072 | 0.57 | 0.57 | 2.3 | 2.3 | 2.3 | Novita | 0.5415 / 2.185 | 1.86B | >20 | 1.86B |
| qwen/qwen3-coder-flash | 1 | 1 | 1000000 | 0.195 | 0.195 | 0.975 | 0.975 | 0.975 | Alibaba | 0.1852 / 0.9262 | 1.65B | >20 | 1.65B |
| z-ai/glm-4.5 | 1 | 1 | 131072 | 0.6 | 0.6 | 2.2 | 2.2 | 2.2 | Z.AI | 0.57 / 2.09 | 1.4B | >20 | 1.4B |
| qwen/qwen3-235b-a22b-thinking-2507 | 1 | 1 | 128000 | 0.45 | 0.45 | 3.5 | 3.5 | 3.5 | Venice | 0.4275 / 3.325 | 670M | >20 | 670M |
| deepseek/deepseek-r1 | 0 | 0 | None | n/a | n/a | n/a | n/a | n/a | none | n/a | not in top list | n/a | n/a |
| qwen/qwen3-235b-a22b | 0 | 0 | None | n/a | n/a | n/a | n/a | n/a | none | n/a | not in top list | n/a | n/a |
| qwen/qwen3.8-2.4t-a95b | 5 | 5 | 1048576 | 2 | 2 | 6 | 6 | 6 | Alibaba, Novita, SiliconFlow, Together, Venice | 1.9 / 5.7 | not in top list | n/a | n/a |

#### Provider frequency across the models above

Source: the endpoints files listed above (checked 2026-10-22). 'Out price vs floor' is the median of (provider output price / cheapest output price for that model). 'Times cheapest' counts models where the provider posts the lowest output price (ties count).

| Provider | Models served (of 56) | Times cheapest | Out price vs floor (median x) | In price vs floor (median x) | Quantizations offered |
|---|---|---|---|---|---|
| DeepInfra | 34 | 18 | 1 | 1.18 | bf16, fp4, fp8, mxfp4 |
| Novita | 27 | 5 | 1.36 | 1.4 | bf16, fp4, fp8, unknown |
| Venice | 26 | 4 | 1.46 | 1.67 | fp4, fp8, int4, unknown |
| SiliconFlow | 21 | 3 | 2.04 | 3.4 | fp8, int4 |
| Parasail | 21 | 1 | 2 | 2.2 | bf16, fp4, fp8, int4 |
| GMICloud | 18 | 3 | 1.44 | 1.86 | bf16, fp8 |
| AtlasCloud | 16 | 1 | 2.56 | 2.79 | fp4, fp8, int4 |
| CoreWeave | 14 | 0 | 1.95 | 2.64 | fp16, fp4, fp8, nvfp4 |
| StreamLake | 13 | 3 | 1.33 | 1.34 | fp8, unknown |
| DigitalOcean | 13 | 1 | 2.35 | 2.82 | unknown |
| Phala | 13 | 0 | 2.93 | 5.71 | nvfp4, unknown |
| Together | 12 | 2 | 3.2 | 4.64 | unknown |
| Alibaba | 12 | 3 | 2.9 | 3.11 | fp8, unknown |
| Google | 11 | 1 | 2.4 | 3 | unknown |
| Baidu | 10 | 5 | 1.08 | 1.14 | fp4, fp8 |
| Relace | 10 | 0 | 1.95 | 1 | fp4, mxfp4, unknown |
| BaseTen | 9 | 1 | 3.14 | 4.29 | fp4, fp8, unknown |
| Wafer | 9 | 1 | 1.84 | 2.29 | fp4, fp8, mxfp4, nvfp4 |
| Cloudflare | 9 | 0 | 4 | 8.8 | fp8, unknown |
| Crusoe | 8 | 0 | 3.3 | 3.95 | bf16, fp4, fp8 |
| Reka | 7 | 0 | 3.96 | 1.77 | fp8, unknown |
| Sail Research | 7 | 2 | 1.39 | 3.55 | fp4, fp8 |
| DekaLLM | 7 | 0 | 1.56 | 1.61 | bf16, fp8, unknown |
| Makora | 7 | 1 | 3.14 | 2.72 | fp4, fp8, unknown |
| AkashML | 7 | 0 | 1.58 | 2 | bf16, fp4, fp8 |
| Z.AI | 7 | 2 | 1.57 | 1.67 | fp4, fp8 |
| SambaNova | 6 | 0 | 3.2 | 4.15 | fp8, unknown |
| InferenceNet | 6 | 1 | 2.77 | 1.08 | fp4, fp8 |
| Fireworks | 6 | 1 | 2.82 | 6.54 | unknown |
| Modal | 6 | 1 | 2.94 | 8.42 | mxfp4, nvfp4, unknown |
| Amazon Bedrock | 6 | 0 | 2.2 | 4.44 | unknown |
| Mancer 2 | 5 | 0 | 2 | 3.8 | fp4, fp8 |
| Morph | 5 | 0 | 3.33 | 3.61 | fp8 |
| Mistral | 5 | 3 | 1 | 1 | nvfp4, unknown |
| Mara | 4 | 0 | 3.86 | 3.84 | unknown |
| Friendli | 4 | 0 | 3.14 | 11.55 | unknown |
| Inceptron | 4 | 0 | 2.22 | 4.15 | fp4, fp8, int4 |
| Decart | 4 | 1 | 1.72 | 4.44 | fp4, mxfp4 |
| PrimeIntellect | 4 | 0 | 5.06 | 11 | unknown |
| Nebius | 4 | 1 | 3.57 | 4.64 | fp4, fp8 |
| Chutes | 4 | 1 | 1.09 | 1.16 | fp4, fp8, int4, mxfp4 |
| ModelRun | 4 | 0 | 2.56 | 6.61 | fp4, fp8 |
| Groq | 4 | 0 | 2.9 | 4.58 | unknown |
| Minimax | 4 | 1 | 1.31 | 1.23 | fp8, unknown |
| Darkbloom | 4 | 2 | 1.03 | 1 | fp4, fp8 |
| Ionstream | 3 | 0 | 4 | 2.53 | fp8, unknown |
| OpenInference | 3 | 0 | 2.78 | 1 | fp4 |
| Io Net | 3 | 0 | 2.29 | 3.61 | fp8, unknown |
| Near AI | 3 | 1 | 1.08 | 1.14 | fp4, fp8 |
| Azure | 2 | 0 | 4.17 | 4.27 | unknown |
| DeepSeek | 2 | 0 | 4.03 | 3.33 | unknown |
| Moonshot AI | 2 | 0 | 2.42 | 7.33 | int4, mxfp4 |
| Cerebras | 2 | 0 | 3.1 | 19.98 | fp16 |
| Tencent | 2 | 2 | 1 | 1 | fp8 |
| Xiaomi | 2 | 0 | 1.08 | 1.26 | fp8 |
| Cohere | 1 | 0 | 2.1 | 3.32 | unknown |
| Meta | 1 | 1 | 1 | 1 | unknown |
| Tenstorrent | 1 | 0 | 1.43 | 1.75 | fp8 |
| Featherless | 1 | 1 | 1 | 1 | fp4 |
| StepFun | 1 | 1 | 1 | 1 | fp8 |
| NextBit | 1 | 0 | 5.17 | 28.85 | fp4 |

#### Detail tables, one per model (every endpoint)

##### deepseek/deepseek-chat-v3.1

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-chat-v3.1/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 163840.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4 | fp4 | 163840 | 32768 | 0.25 | 0.95 | 0.13 | 99.8 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 163840 | 147456 | 0.27 | 1 | n/a | 96.7 | 0 |
| SambaNova | sambanova/fp8 | fp8 | 131072 | 7168 | 0.65 | 1.5 | n/a | 97.2 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 161000 | 144900 | 0.55 | 1.65 | 0.55 | 100 | 0 |
| Mara | mara | unknown | 131072 | 117964 | 0.6 | 1.7 | n/a | 0 | -5 |

##### deepseek/deepseek-chat

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-chat/endpoints (checked 2026-10-22). Distinct providers: 2. Endpoints: 3. Model context: 163840.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4/flex | fp4 | 163840 | 147456 | 0.256 | 0.712 | n/a | 100 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 163840 | 16384 | 0.32 | 0.89 | n/a | 95.3 | 0 |
| StreamLake | streamlake | unknown | 128000 | 16000 | 0.2574 | 1.0287 | n/a | 99.8 | 0 |

##### deepseek/deepseek-r1-0528

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-r1-0528/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 163840.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4 | fp4 | 163840 | 32768 | 0.5 | 2.15 | 0.35 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 163840 | 147456 | 0.5 | 2.18 | n/a | 100 | 0 |
| StreamLake | streamlake | unknown | 128000 | 32000 | 0.571 | 2.286 | n/a | 99.9 | 0 |

##### deepseek/deepseek-v3.2

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v3.2/endpoints (checked 2026-10-22). Distinct providers: 12. Endpoints: 12. Model context: 163840.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp8 | fp8 | 131072 | 65536 | 0.07 | 0.105 | 0.007 | 96.7 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 163840 | 147456 | 0.2088 | 0.3096 | 0.0216 | 99.7 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 163840 | 16384 | 0.26 | 0.38 | 0.13 | 99.7 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 163840 | 147456 | 0.26 | 0.38 | 0.13 | 99.6 | 0 |
| Venice | venice | unknown | 160000 | 32768 | 0.2683 | 0.3902 | 0.1301 | 99.5 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 163840 | 147456 | 0.259 | 0.8 | 0.14 | 99.4 | 0 |
| DigitalOcean | digitalocean | unknown | 163840 | 147456 | 0.3 | 0.96 | 0.09 | 99.7 | 0 |
| Phala | phala | unknown | 163840 | 64000 | 1 | 1 | 0.5 | 100 | 0 |
| Friendli | friendli | unknown | 163840 | 147456 | 0.5 | 1.5 | 0.25 | 100 | 0 |
| Google | google-vertex | unknown | 163840 | 65536 | 0.56 | 1.68 | n/a | 25.8 | -5 |
| Mara | mara | unknown | 32768 | 7168 | 3 | 4.5 | n/a | 0 | 0 |
| SambaNova | sambanova | unknown | 32768 | 7168 | 3 | 4.5 | n/a | 97 | 0 |

##### deepseek/deepseek-v4-flash-0731

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-flash-0731/endpoints (checked 2026-10-22). Distinct providers: 23. Endpoints: 26. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp8 | fp8 | 1048576 | 131072 | 0.0444 | 0.1333 | 0.0014 | 100 | 0 |
| Sail Research | sail-research/us | fp4 | 1048576 | 943718 | 0.15 | 0.15 | 0.042 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 943718 | 0.15 | 0.15 | 0.042 | 100 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 943718 | 0.0422 | 0.1729 | 0.0275 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 384000 | 0.06 | 0.18 | 0.015 | 100 | 0 |
| Wafer | wafer/fast | nvfp4 | 1048576 | 943718 | 0.14 | 0.23 | 0.135 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 943718 | 0.119 | 0.238 | 0.0238 | 100 | 0 |
| BaseTen | baseten/fp8 | fp8 | 1048576 | 384000 | 0.13 | 0.26 | 0.028 | 94.4 | 0 |
| BaseTen | baseten/fp32 | fp32 | 1048576 | 384000 | 0.13 | 0.26 | 0.028 | 93.9 | 0 |
| Venice | venice | unknown | 1000000 | 32768 | 0.13 | 0.26 | 0.028 | 97.8 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 262144 | 235929 | 0.13 | 0.28 | 0.07 | 100 | 0 |
| Cohere | cohere | unknown | 1048576 | 384000 | 0.14 | 0.28 | 0.07 | 99.7 | 0 |
| Together | together | unknown | 1048576 | 943718 | 0.14 | 0.28 | 0.03 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.14 | 0.28 | 0.05 | 100 | 0 |
| Inceptron | inceptron/fp4 | fp4 | 1048576 | 943718 | 0.11 | 0.3666 | 0.027 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 384000 | 0.132 | 0.396 | 0.0042 | 99.9 | 0 |
| Reka | reka | unknown | 262144 | 131072 | 0.05 | 0.528 | 0.02 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 393216 | 0.176 | 0.528 | 0.0176 | 99.7 | 0 |
| Alibaba | alibaba/us-east-1 | unknown | 1000000 | 393216 | 0.187 | 0.561 | 0.0187 | 99.8 | -2 |
| Mancer 2 | mancer/fp8 | fp8 | 1048576 | 943718 | 0.2 | 0.6 | n/a | 99.8 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 0.22 | 0.66 | 0.028 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 0.286 | 0.858 | 0.0091 | 100 | 0 |
| Phala | phala | unknown | 1048576 | 393216 | 0.308 | 0.924 | 0.0196 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 0.4092 | 1.2276 | 0.026 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp4 | fp4 | 1048576 | 393216 | 0.44 | 1.32 | 0.028 | 100 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 0.44 | 1.32 | 0.014 | 100 | 0 |

##### deepseek/deepseek-v4-flash

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-flash/endpoints (checked 2026-10-22). Distinct providers: 15. Endpoints: 15. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 384000 | 0.07 | 0.14 | 0.014 | 100 | 0 |
| Wafer | wafer/mxfp4 | mxfp4 | 1048576 | 943718 | 0.7 | 0.17 | 0.013 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 65536 | 0.09 | 0.18 | 0.018 | 97.2 | 0 |
| Baidu | baidu/fp8 | fp8 | 1048576 | 131072 | 0.0909 | 0.1817 | 0.0182 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 0.091 | 0.182 | 0.0182 | 99.9 | 0 |
| Venice | venice | unknown | 1000000 | 32768 | 0.0966 | 0.1925 | 0.0196 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 384000 | 0.098 | 0.196 | 0.0196 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 0.13 | 0.28 | 0.028 | 99.4 | 0 |
| AtlasCloud | atlas-cloud/fp4 | fp4 | 1048576 | 393216 | 0.14 | 0.28 | 0.028 | 99.9 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.14 | 0.28 | 0.07 | 100 | 0 |
| Alibaba | alibaba/fp8/us-east-1 | fp8 | 1000000 | 393216 | 0.15 | 0.3 | 0.03 | 99.8 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 943718 | 0.05 | 0.45 | 0.05 | 100 | 0 |
| Mancer 2 | mancer/fp8 | fp8 | 1048576 | 943718 | 0.19 | 0.5 | n/a | 97.6 | 0 |
| Azure | azure/us | unknown | 1048576 | 384000 | 0.21 | 0.56 | 0.031 | 86.6 | 0 |
| Cloudflare | cloudflare | unknown | 384000 | 345600 | 0.44 | 1.32 | 0.014 | 99 | 0 |

##### deepseek/deepseek-v4-pro-0813

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro-0813/endpoints (checked 2026-10-22). Distinct providers: 21. Endpoints: 23. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp8 | fp8 | 1048576 | 393216 | 0.1624 | 0.4871 | 0.0052 | 100 | 0 |
| Sail Research | sail-research/us | fp4 | 1048576 | 384000 | 0.45 | 0.8 | 0.065 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 384000 | 0.45 | 0.8 | 0.065 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 393216 | 0.5808 | 1.7424 | 0.0581 | 99.8 | 0 |
| Alibaba | alibaba/us-east-1 | unknown | 1000000 | 393216 | 0.66 | 1.98 | 0.066 | 99.6 | -2 |
| StreamLake | streamlake | unknown | 1024000 | 384000 | 0.66 | 1.98 | 0.022 | 100 | 0 |
| DeepSeek | deepseek | unknown | 1048576 | 393216 | 0.66 | 1.98 | 0.022 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 16384 | 1.3 | 2.6 | 0.1 | 99.9 | 0 |
| Phala | phala | unknown | 1048576 | 393216 | 0.957 | 2.8776 | 0.099 | 100 | 0 |
| Ionstream | ionstream | unknown | 1048576 | 943718 | 0.37 | 2.93 | 0.088 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 0.99 | 2.97 | 0.033 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 1.056 | 3.168 | 0.0352 | 100 | 0 |
| DekaLLM | dekallm | unknown | 1048576 | 943718 | 0.88 | 3.8 | 0.15 | 99.4 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 1048576 | 943718 | 1.31 | 3.96 | 0.044 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 393216 | 1.32 | 3.96 | 0.132 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 1.32 | 3.96 | 0.044 | 98.9 | 0 |
| Together | together | unknown | 1048576 | 943718 | 1.32 | 3.96 | 0.13 | 98.8 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 943718 | 1.32 | 3.96 | 0.044 | 94.8 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 1.32 | 3.96 | 0.044 | 100 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 1.32 | 3.96 | 0.044 | 99.5 | 0 |
| Venice | venice | unknown | 1000000 | 32768 | 1.65 | 4.95 | 0.165 | 98.4 | 0 |
| Wafer | wafer/mxfp4 | mxfp4 | 1048576 | 943718 | 0.25 | 5 | 0.249 | 99.4 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 393216 | 0.1461 | 8 | 0.15 | 99.8 | 0 |

##### deepseek/deepseek-v4-pro

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro/endpoints (checked 2026-10-22). Distinct providers: 15. Endpoints: 16. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp8 | fp8 | 1048576 | 393216 | 0.4411 | 0.8822 | 0.0365 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 384000 | 0.4427 | 0.8853 | 0.0369 | 100 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 393216 | 0.9 | 1.5 | 0.25 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048576 | 943718 | 0.957 | 1.914 | 0.0798 | 99.8 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 384000 | 1.044 | 2.088 | 0.2088 | 100 | 0 |
| Reka | reka | unknown | 1048576 | 393216 | 1.05 | 2.1 | 0.21 | 98.7 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 1.15 | 2.55 | 0.2 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 16384 | 1.3 | 2.6 | 0.1 | 99.9 | 0 |
| Alibaba | alibaba/fp8 | fp8 | 1000000 | 393216 | 1.416 | 2.832 | 0.118 | 97.7 | 0 |
| Alibaba | alibaba/fp8/us-east-1 | fp8 | 1000000 | 393216 | 1.56 | 3.12 | 0.13 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 1.5016 | 3.135 | 0.135 | 96.2 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 1.6 | 3.2 | 0.135 | 100 | 0 |
| Venice | venice | unknown | 1000000 | 32768 | 1.65 | 3.301 | 0.33 | 98.4 | 0 |
| AtlasCloud | atlas-cloud/fp4 | fp4 | 1048576 | 393216 | 1.68 | 3.38 | 0.13 | 99.4 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.45 | 3.48 | 0.1 | 72.6 | -2 |
| Azure | azure/us | unknown | 1048576 | 384000 | 1.91 | 3.83 | 0.16 | 100 | 0 |

##### deepseek/deepseek-v4.1-flash-1017

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash-1017/endpoints (checked 2026-10-22). Distinct providers: 26. Endpoints: 30. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Sail Research | sail-research/fp4/us | fp4 | 1048576 | 384000 | 0.101 | 0.15 | 0.0067 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 384000 | 0.101 | 0.15 | 0.0067 | 99.9 | 0 |
| DeepInfra | deepinfra/fp8/flex | fp8 | 1048576 | 131072 | 0.0784 | 0.2352 | 0.0024 | 88.7 | -2 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 131072 | 0.098 | 0.294 | 0.0029 | 100 | 0 |
| DeepInfra | deepinfra/fp8/priority | fp8 | 1048576 | 131072 | 0.147 | 0.441 | 0.0044 | 99.9 | 0 |
| OpenInference | open-inference/fp4 | fp4 | 1048576 | 943718 | 0.07 | 0.5 | 0.008 | 99 | 0 |
| Relace | relace | unknown | 1048576 | 943718 | 0.07 | 0.5 | 0.008 | 100 | 0 |
| InferenceNet | inference-net/us | fp8 | 1040000 | 393216 | 0.08 | 0.5 | 0.008 | 100 | 0 |
| InferenceNet | inference-net/fp8 | fp8 | 1040000 | 393216 | 0.08 | 0.5 | 0.008 | 100 | 0 |
| Wafer | wafer/mxfp4 | mxfp4 | 1048576 | 943718 | 0.16 | 0.5 | 0.008 | 100 | 0 |
| Decart | decart/fp4 | fp4 | 1048576 | 262144 | 0.138 | 0.552 | 0.0028 | 99.9 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 0.1 | 0.6 | 0.003 | 100 | 0 |
| Reka | reka | unknown | 1048576 | 393216 | 0.15 | 0.6 | 0.003 | 98.3 | 0 |
| DeepSeek | deepseek | unknown | 1048576 | 393216 | 0.15 | 0.6 | 0.003 | 100 | 0 |
| Ionstream | ionstream | unknown | 1048576 | 943718 | 0.22 | 0.6 | 0.019 | 100 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.253 | 0.6 | 0.022 | 99.9 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 393216 | 0.165 | 0.66 | 0.0165 | 98.3 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 0.18 | 0.72 | 0.0036 | 99.6 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 393216 | 0.195 | 0.78 | 0.0039 | 99.7 | 0 |
| Baidu | baidu/fp8 | fp8 | 1048576 | 393216 | 0.28 | 1.13 | 0.006 | 100 | 0 |
| Crusoe | crusoe/fp8 | fp8 | 1048576 | 943718 | 0.29 | 1.2 | 0.007 | 100 | 0 |
| Makora | makora/fp8 | fp8 | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 99.5 | 0 |
| Phala | phala | unknown | 1048576 | 393216 | 0.3 | 1.2 | 0.006 | 99.4 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 0.3 | 1.2 | 0.006 | 98.4 | -2 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 0.3 | 1.2 | 0.006 | 99.9 | 0 |
| Together | together | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| PrimeIntellect | primeintellect | unknown | 1048576 | 131072 | 0.3 | 1.2 | 0.006 | 99.9 | 0 |
| BaseTen | baseten | unknown | 1048576 | 262144 | 0.3 | 1.2 | 0.007 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |

##### deepseek/deepseek-v4.1-flash

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints (checked 2026-10-22). Distinct providers: 30. Endpoints: 38. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Decart | decart/fp4 | fp4 | 1048576 | 262144 | 0.09 | 0.18 | 0.018 | 100 | 0 |
| Sail Research | sail-research/fp4/us | fp4 | 1048576 | 384000 | 0.09 | 0.25 | 0.006 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 384000 | 0.09 | 0.25 | 0.006 | 100 | 0 |
| DeepInfra | deepinfra/fp8/flex | fp8 | 1048576 | 131072 | 0.112 | 0.336 | 0.0034 | 90.8 | -2 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 131072 | 0.14 | 0.42 | 0.0042 | 100 | 0 |
| OpenInference | open-inference/fp4 | fp4 | 1048576 | 943718 | 0.07 | 0.5 | 0.008 | 99.9 | 0 |
| Relace | relace | unknown | 1048576 | 943718 | 0.07 | 0.5 | 0.008 | 99.8 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 393216 | 0.135 | 0.54 | 0.0135 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 384000 | 0.147 | 0.588 | 0.0029 | 100 | 0 |
| Baidu | baidu/fp8 | fp8 | 1048576 | 393216 | 0.15 | 0.6 | 0.003 | 100 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.253 | 0.6 | 0.022 | 98.8 | 0 |
| DeepInfra | deepinfra/fp8/priority | fp8 | 1048576 | 131072 | 0.21 | 0.63 | 0.0063 | 73.5 | -5 |
| CoreWeave | coreweave/fp8 | fp8 | 1048576 | 943718 | 0.15 | 0.65 | 0.002 | 100 | 0 |
| Wafer | wafer/mxfp4 | mxfp4 | 1048576 | 943718 | 0.19 | 0.65 | 0.012 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 393216 | 0.165 | 0.66 | 0.0165 | 100 | 0 |
| InferenceNet | inference-net/us | fp8 | 1040000 | 393216 | 0.103 | 0.715 | 0.008 | 100 | 0 |
| InferenceNet | inference-net/fp8 | fp8 | 1040000 | 393216 | 0.103 | 0.715 | 0.008 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 0.18 | 0.72 | 0.0036 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 0.195 | 0.78 | 0.0039 | 100 | 0 |
| Reka | reka | unknown | 1048576 | 393216 | 0.105 | 0.84 | 0.007 | 94.3 | 0 |
| Fireworks | fireworks/spot | unknown | 1048576 | 943718 | 0.21 | 0.84 | 0.0042 | 100 | 0 |
| Phala | phala | unknown | 1048576 | 943718 | 0.21 | 0.84 | 0.0042 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 943718 | 0.225 | 0.9 | 0.006 | 100 | 0 |
| Makora | makora/fp8 | fp8 | 1048576 | 943718 | 0.26 | 1.17 | 0.0058 | 99.9 | 0 |
| Crusoe | crusoe/fp8 | fp8 | 1048576 | 943718 | 0.29 | 1.2 | 0.007 | 100 | 0 |
| Google | google-vertex/global | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.03 | 98.5 | -2 |
| Nebius | nebius/fp8 | fp8 | 1048000 | 943200 | 0.3 | 1.2 | 0.01 | 100 | 0 |
| PrimeIntellect | primeintellect | unknown | 1048576 | 131072 | 0.3 | 1.2 | 0.03 | 100 | 0 |
| BaseTen | baseten/us | unknown | 1048576 | 262144 | 0.3 | 1.2 | 0.007 | 100 | 0 |
| Together | together | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| Modal | modal | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.03 | 100 | 0 |
| BaseTen | baseten | unknown | 1048576 | 262144 | 0.3 | 1.2 | 0.007 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 98 | -2 |
| Venice | venice/fp8 | fp8 | 1000000 | 131072 | 0.3 | 1.2 | 0.0075 | 100 | 0 |
| Fireworks | fireworks/us | unknown | 1048576 | 943718 | 0.45 | 1.8 | 0.009 | 100 | 0 |
| BaseTen | baseten/fast | unknown | 1048576 | 131072 | 0.6 | 2.4 | 0.014 | 99.8 | 0 |

##### google/gemma-4-31b-it

Source: https://openrouter.ai/api/v1/models/google/gemma-4-31b-it/endpoints (checked 2026-10-22). Distinct providers: 12. Endpoints: 15. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8/flex | fp8 | 262144 | 235929 | 0.16 | 0.32 | n/a | 99.6 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 262144 | 235929 | 0.1 | 0.34 | 0.1 | 100 | 0 |
| Venice | venice/fp4 | fp4 | 256000 | 8192 | 0.12 | 0.36 | 0.09 | 98.1 | 0 |
| Chutes | chutes/fp4 | fp4 | 131072 | 65536 | 0.12 | 0.37 | 0.012 | 95.2 | 0 |
| Crusoe | crusoe/bf16 | bf16 | 262144 | 262141 | 0.14 | 0.4 | 0.14 | 98.8 | 0 |
| Friendli | friendli | unknown | 262144 | 8192 | 0.14 | 0.4 | n/a | 100 | 0 |
| Novita | novita/bf16 | bf16 | 262144 | 131072 | 0.14 | 0.4 | n/a | 84.2 | 0 |
| Parasail | parasail/fp8 | fp8 | 262144 | 235929 | 0.15 | 0.4 | 0.06 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 262144 | 16384 | 0.2 | 0.4 | n/a | 98.4 | 0 |
| DeepInfra | deepinfra/turbo | fp4 | 262144 | 16384 | 0.135 | 0.51 | 0.075 | 99.9 | 0 |
| DeepInfra | deepinfra/fp8/priority | fp8 | 262144 | 235929 | 0.3 | 0.6 | n/a | 93.2 | 0 |
| ModelRun | modelrun/fp4 | fp4 | 262144 | 235929 | 0.75 | 1 | 0.2 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 262144 | 235929 | 0.75 | 1 | 0.25 | 95.3 | 0 |
| Io Net | io-net | unknown | 262144 | 16384 | 0.361 | 1.0925 | 0.1805 | 93.4 | 0 |
| SambaNova | sambanova | unknown | 131072 | 117964 | 0.38 | 1.15 | n/a | 99.5 | -2 |

##### meta-llama/llama-3.3-70b-instruct

Source: https://openrouter.ai/api/v1/models/meta-llama/llama-3.3-70b-instruct/endpoints (checked 2026-10-22). Distinct providers: 10. Endpoints: 11. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/turbo | fp8 | 131072 | 16384 | 0.1 | 0.32 | n/a | 99.4 | 0 |
| Novita | novita/bf16 | bf16 | 12288 | 11059 | 0.135 | 0.4 | n/a | 99.9 | 0 |
| Parasail | parasail/fp8 | fp8 | 131072 | 16384 | 0.22 | 0.5 | 0.11 | 99.5 | 0 |
| AkashML | akashml/fp8 | fp8 | 131072 | 128000 | 0.2 | 0.52 | 0.1 | 99.9 | 0 |
| CoreWeave | coreweave/fp16 | fp16 | 128000 | 115200 | 0.71 | 0.71 | 0.71 | 100 | 0 |
| Google | google-vertex/us-central1 | unknown | 128000 | 8192 | 0.72 | 0.72 | n/a | n/a | 0 |
| Google | google-vertex | unknown | 128000 | 115200 | 0.72 | 0.72 | n/a | n/a | 0 |
| Groq | groq | unknown | 131072 | 32768 | 0.59 | 0.79 | 0.295 | 100 | 0 |
| SambaNova | sambanova-turbo | unknown | 131072 | 3072 | 0.45 | 0.9 | n/a | 99.9 | 0 |
| Together | together | unknown | 131072 | 2048 | 1.04 | 1.04 | n/a | 97.9 | 0 |
| Cloudflare | cloudflare/fp8 | fp8 | 24000 | 21600 | 0.293 | 2.253 | n/a | 100 | 0 |

##### meta-llama/llama-4-maverick

Source: https://openrouter.ai/api/v1/models/meta-llama/llama-4-maverick/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 524288.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DigitalOcean | digitalocean | unknown | 128000 | 16384 | 0.1875 | 0.6525 | 0.05 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 524288 | 32768 | 0.35 | 1 | 0.17 | 99.9 | 0 |
| Google | google-vertex/us-east5 | unknown | 524288 | 8192 | 0.35 | 1.15 | n/a | n/a | 0 |

##### meta-llama/llama-4-scout

Source: https://openrouter.ai/api/v1/models/meta-llama/llama-4-scout/endpoints (checked 2026-10-22). Distinct providers: 2. Endpoints: 4. Model context: 1310720.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8/flex | fp8 | 327680 | 294912 | 0.08 | 0.24 | n/a | 67.2 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 327680 | 16384 | 0.1 | 0.3 | n/a | 99.6 | 0 |
| DeepInfra | deepinfra/fp8/priority | fp8 | 327680 | 294912 | 0.15 | 0.45 | n/a | 95.2 | 0 |
| Google | google-vertex/us-east5 | unknown | 1310720 | 8192 | 0.25 | 0.7 | n/a | n/a | 0 |

##### meta/muse-spark-1.3-contributor

Source: https://openrouter.ai/api/v1/models/meta/muse-spark-1.3-contributor/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Meta | meta | unknown | 1048576 | 943718 | 0.1 | 0.2 | 0.002 | 100 | 0 |

##### meta/muse-spark-open

Source: https://openrouter.ai/api/v1/models/meta/muse-spark-open/endpoints (checked 2026-10-22). Distinct providers: 6. Endpoints: 6. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Makora | makora/fp4 | fp4 | 1048576 | 131072 | 1.25 | 4.25 | 0.15 | 100 | 0 |
| Modal | modal | unknown | 1000000 | 262144 | 1.25 | 4.25 | 0.15 | 100 | 0 |
| Together | together | unknown | 1048576 | 943718 | 1.25 | 4.25 | 0.15 | 100 | 0 |
| Nebius | nebius/fp4 | fp4 | 1048576 | 943718 | 1.25 | 4.25 | 0.15 | 90 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 1.25 | 4.25 | 0.15 | 98.5 | 0 |
| BaseTen | baseten/fp4 | fp4 | 1048576 | 943718 | 1.25 | 4.25 | 0.15 | 100 | 0 |

##### minimax/minimax-m2.5

Source: https://openrouter.ai/api/v1/models/minimax/minimax-m2.5/endpoints (checked 2026-10-22). Distinct providers: 7. Endpoints: 8. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Venice | venice | unknown | 198000 | 32768 | 0.27 | 0.95 | 0.03 | 94.5 | -2 |
| StreamLake | streamlake | unknown | 200000 | 128000 | 0.27 | 1.08 | 0.027 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 196608 | 176947 | 0.295 | 1.2 | 0.06 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 196608 | 176947 | 0.3 | 1.2 | 0.03 | 95 | 0 |
| DigitalOcean | digitalocean | unknown | 65536 | 58982 | 0.3 | 1.2 | 0.06 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 204800 | 131100 | 0.3 | 1.2 | 0.03 | 98.8 | 0 |
| Minimax | minimax/fp8 | fp8 | 204800 | 131072 | 0.3 | 1.2 | 0.03 | 100 | 0 |
| Minimax | minimax/highspeed | fp8 | 204800 | 131072 | 0.6 | 2.4 | 0.06 | 100 | 0 |

##### minimax/minimax-m2.7

Source: https://openrouter.ai/api/v1/models/minimax/minimax-m2.7/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 6. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| GMICloud | gmicloud/fp8 | fp8 | 196608 | 176947 | 0.21 | 0.84 | 0.042 | 99.2 | 0 |
| Novita | novita/fp8 | fp8 | 204800 | 131072 | 0.27 | 1.08 | 0.054 | 99.3 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 196608 | 176947 | 0.3 | 1.2 | 0.06 | 98.4 | 0 |
| Minimax | minimax/fp8 | fp8 | 204800 | 131072 | 0.3 | 1.2 | 0.06 | 99.9 | 0 |
| Groq | groq | unknown | 196608 | 131072 | 0.6 | 1.8 | n/a | 98.5 | 0 |
| Minimax | minimax/highspeed | fp8 | 204800 | 131072 | 0.6 | 2.4 | 0.06 | 98.3 | 0 |

##### minimax/minimax-m3.1-flash

Source: https://openrouter.ai/api/v1/models/minimax/minimax-m3.1-flash/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 1000000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Minimax | minimax | unknown | 1000000 | 524288 | 0.15 | 0.6 | 0.015 | 100 | 0 |

##### minimax/minimax-m3

Source: https://openrouter.ai/api/v1/models/minimax/minimax-m3/endpoints (checked 2026-10-22). Distinct providers: 13. Endpoints: 14. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8/flex | fp8 | 524288 | 131072 | 0.224 | 0.88 | 0.0448 | 100 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 262144 | 235929 | 0.23 | 0.96 | 0.05 | 99.7 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048576 | 524288 | 0.24 | 0.96 | 0.048 | 99.7 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 524288 | 131072 | 0.28 | 1.1 | 0.056 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 1000000 | 512000 | 0.3 | 1.2 | 0.06 | 98.6 | 0 |
| Venice | venice/fp8 | fp8 | 524288 | 65536 | 0.3 | 1.2 | 0.06 | 97.5 | 0 |
| Together | together | unknown | 524288 | 471859 | 0.3 | 1.2 | 0.06 | 99.4 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 524288 | 0.3 | 1.2 | 0.06 | 99.9 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 524300 | 524288 | 0.3 | 1.2 | 0.06 | 98.7 | 0 |
| Novita | novita/fp8 | fp8 | 1000000 | 131072 | 0.3 | 1.2 | 0.06 | 100 | 0 |
| Minimax | minimax/fp8 | fp8 | 524288 | 512000 | 0.3 | 1.2 | 0.06 | 99.9 | 0 |
| ModelRun | modelrun/fp8 | fp8 | 1048576 | 943718 | 0.3 | 1.3 | 0.05 | 99.8 | 0 |
| Mara | mara | unknown | 1048576 | 943718 | 0.6 | 2.4 | n/a | 85.7 | 0 |
| SambaNova | sambanova | unknown | 1048576 | 943718 | 0.6 | 2.4 | 0.06 | 95.5 | 0 |

##### mistralai/mistral-medium-3-5

Source: https://openrouter.ai/api/v1/models/mistralai/mistral-medium-3-5/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 3. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Mistral | mistral/zdr | unknown | 262144 | 209715 | 1.5 | 7.5 | n/a | 100 | 0 |
| Mistral | mistral | unknown | 262144 | 209715 | 1.5 | 7.5 | n/a | 100 | 0 |
| Mistral | mistral/eu | unknown | 262144 | 209715 | 1.65 | 8.25 | n/a | 100 | 0 |

##### mistralai/mistral-medium-3.1

Source: https://openrouter.ai/api/v1/models/mistralai/mistral-medium-3.1/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 3. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Mistral | mistral/zdr | unknown | 131072 | 104857 | 0.4 | 2 | 0.04 | 99.9 | 0 |
| Mistral | mistral | unknown | 131072 | 104857 | 0.4 | 2 | 0.04 | 99.9 | 0 |
| Mistral | mistral/eu | unknown | 131072 | 104857 | 0.44 | 2.2 | 0.044 | 100 | 0 |

##### mistralai/mistral-small-2603

Source: https://openrouter.ai/api/v1/models/mistralai/mistral-small-2603/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 4. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Mistral | mistral/zdr | unknown | 262144 | 209715 | 0.15 | 0.6 | 0.015 | 99.8 | 0 |
| Mistral | mistral | unknown | 262144 | 209715 | 0.15 | 0.6 | 0.015 | 99.9 | 0 |
| Mistral | mistral/eu | unknown | 262144 | 209715 | 0.165 | 0.66 | 0.0165 | 100 | 0 |
| Mistral | mistral/us | unknown | 262144 | 209715 | 0.165 | 0.66 | 0.0165 | 100 | 0 |

##### mistralai/mistral-small-3.2-24b-instruct

Source: https://openrouter.ai/api/v1/models/mistralai/mistral-small-3.2-24b-instruct/endpoints (checked 2026-10-22). Distinct providers: 4. Endpoints: 4. Model context: 256000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8 | fp8 | 128000 | 16384 | 0.075 | 0.2 | n/a | 99.9 | 0 |
| Venice | venice/fp8 | fp8 | 256000 | 16384 | 0.0938 | 0.25 | n/a | 99.2 | 0 |
| Parasail | parasail/bf16 | bf16 | 131072 | 32768 | 0.09 | 0.3 | 0.05 | 100 | 0 |
| Mistral | mistral/eu | unknown | 32768 | 26214 | 0.1 | 0.3 | 0.01 | 100 | 0 |

##### moonshotai/kimi-k2-0905

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2-0905/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Novita | novita/fp8 | fp8 | 262144 | 98304 | 0.6 | 2.5 | n/a | 100 | 0 |

##### moonshotai/kimi-k2-thinking

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2-thinking/endpoints (checked 2026-10-22). Distinct providers: 2. Endpoints: 2. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Google | google-vertex | unknown | 262144 | 235929 | 0.6 | 2.5 | n/a | 85.2 | -5 |
| Novita | novita/bf16 | bf16 | 262144 | 98304 | 0.6 | 2.5 | 0.15 | 100 | 0 |

##### moonshotai/kimi-k2.5

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2.5/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| AtlasCloud | atlas-cloud/int4 | int4 | 262144 | 235929 | 0.49 | 2.5 | 0.2 | 99.4 | 0 |
| SiliconFlow | siliconflow/int4 | int4 | 262144 | 235929 | 0.5 | 2.5 | 0.15 | 100 | 0 |
| Novita | novita | unknown | 262144 | 235929 | 0.57 | 2.85 | 0.095 | 99.9 | 0 |
| Amazon Bedrock | amazon-bedrock/us-east-2 | unknown | 262144 | 131072 | 0.6 | 3 | n/a | 100 | 0 |
| Venice | venice | unknown | 256000 | 65536 | 0.532 | 3.325 | 0.209 | 100 | 0 |

##### moonshotai/kimi-k2.6

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2.6/endpoints (checked 2026-10-22). Distinct providers: 17. Endpoints: 17. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp4 | fp4 | 262144 | 235929 | 0.4493 | 1.892 | 0.0757 | 99.5 | 0 |
| Chutes | chutes/int4 | int4 | 262144 | 65535 | 0.45 | 1.95 | 0.045 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 262144 | 235929 | 0.57 | 2.4 | 0.114 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 256000 | 230400 | 0.5985 | 2.52 | 0.1008 | 97.3 | 0 |
| Inceptron | inceptron/int4 | int4 | 262144 | 235929 | 0.5621 | 3.2 | 0.169 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 262144 | 235929 | 0.77 | 3.4 | 0.14 | 99.8 | 0 |
| Novita | novita | unknown | 262144 | 235929 | 0.8 | 3.4 | 0.16 | 100 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 262144 | 235929 | 0.65 | 3.41 | 0.15 | 99.7 | 0 |
| Crusoe | crusoe/bf16 | bf16 | 262144 | 235929 | 0.7 | 3.5 | 0.35 | 99.6 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 262144 | 16384 | 0.75 | 3.5 | 0.15 | 99.6 | 0 |
| Venice | venice/int4 | int4 | 256000 | 65536 | 0.75 | 3.5 | 0.16 | 97.1 | 0 |
| Parasail | parasail/int4 | int4 | 262144 | 235929 | 0.75 | 3.5 | 0.16 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 262144 | 235929 | 0.855 | 3.6 | 0.144 | n/a | 0 |
| AtlasCloud | atlas-cloud/int4 | int4 | 262144 | 235929 | 0.95 | 4 | 0.16 | 100 | 0 |
| Cloudflare | cloudflare | unknown | 262144 | 235929 | 0.95 | 4 | 0.16 | 100 | 0 |
| Moonshot AI | moonshotai/int4 | int4 | 262144 | 235929 | 0.95 | 4 | 0.16 | 100 | 0 |
| Phala | phala | unknown | 262144 | 235929 | 1.09 | 4.6 | 0.37 | 100 | 0 |

##### moonshotai/kimi-k2

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Novita | novita/fp8 | fp8 | 131072 | 98304 | 0.57 | 2.3 | n/a | 100 | 0 |

##### moonshotai/kimi-k3

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints (checked 2026-10-22). Distinct providers: 20. Endpoints: 28. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Sail Research | sail-research/fp4/us | fp4 | 1048576 | 943718 | 1.2 | 5.5 | 0.2 | n/a | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 943718 | 1.2 | 5.5 | 0.2 | n/a | 0 |
| Decart | decart/mxfp4 | mxfp4 | 1048576 | 943718 | 1.65 | 8.25 | 0.165 | 99.8 | 0 |
| Chutes | chutes/mxfp4 | mxfp4 | 1048576 | 65535 | 1.85 | 9.5 | 0.185 | 96.3 | 0 |
| Fireworks | fireworks/spot | unknown | 1048576 | 943718 | 2.1 | 10.5 | 0.21 | 77.6 | 0 |
| Wafer | wafer/us | mxfp4 | 1048576 | 943718 | 0.36 | 11.9 | 0.359 | 100 | 0 |
| InferenceNet | inference-net/us | fp4 | 1048576 | 943718 | 0.239 | 11.936 | 0.21 | 100 | 0 |
| InferenceNet | inference-net/fp4 | fp4 | 1048576 | 943718 | 0.239 | 11.936 | 0.21 | 100 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 943718 | 0.3 | 12 | 0.25 | 99.4 | 0 |
| Phala | phala | unknown | 1048576 | 943718 | 2.55 | 12.75 | 0.255 | 99.9 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 943718 | 2.55 | 12.95 | 0.255 | 100 | 0 |
| InferenceNet | inference-net/fast | fp4 | 1048576 | 943718 | 2.04 | 13.2 | 0.35 | 99.4 | 0 |
| AkashML | akashml/fp4 | fp4 | 1048576 | 943718 | 1.2 | 14 | 1.2 | 99.7 | 0 |
| DeepInfra | deepinfra/mxfp4 | mxfp4 | 1048576 | 943718 | 2.85 | 14.25 | 0.285 | 99.9 | 0 |
| InferenceNet | inference-net/us/fast | fp4 | 1048576 | 943718 | 2.24 | 14.519 | 0.35 | 99.7 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.892 | 14.9 | 0.427 | 98.9 | 0 |
| Makora | makora/fp4 | fp4 | 1048576 | 943718 | 0.65 | 15 | 0.23 | 99.4 | 0 |
| Amazon Bedrock | amazon-bedrock/us-east-2 | unknown | 1048576 | 128000 | 3 | 15 | 0.3 | 94.2 | 0 |
| Parasail | parasail/fp4 | fp4 | 1048576 | 943718 | 3 | 15 | 0.3 | 97.4 | 0 |
| Modal | modal/mxfp4 | mxfp4 | 1048576 | 943718 | 3 | 15 | 0.3 | 100 | 0 |
| Together | together | unknown | 1048576 | 943718 | 3 | 15 | 0.3 | 99.9 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 3 | 15 | 0.3 | 97.9 | 0 |
| BaseTen | baseten/fp8 | fp8 | 1048576 | 262144 | 3 | 15 | 0.3 | 99.7 | 0 |
| Moonshot AI | moonshotai/mxfp4 | mxfp4 | 1048576 | 943718 | 3 | 15 | 0.3 | 100 | 0 |
| Wafer | wafer | mxfp4 | 1048576 | 943718 | 0.238 | 16 | 0.228 | 100 | 0 |
| Alibaba | alibaba | unknown | 1048576 | 131072 | 3.45 | 17.25 | 0.345 | 98.8 | 0 |
| Fireworks | fireworks/us | unknown | 1048576 | 943718 | 4.5 | 22.5 | 0.45 | 97.6 | 0 |
| Fireworks | fireworks/fast | unknown | 1048576 | 943718 | 4.5 | 22.5 | 0.45 | 98.5 | 0 |

##### nvidia/nemotron-3-super-120b-a12b

Source: https://openrouter.ai/api/v1/models/nvidia/nemotron-3-super-120b-a12b/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/bf16 | bf16 | 262144 | 16384 | 0.085 | 0.4 | n/a | 100 | 0 |
| DekaLLM | dekallm/fp8 | fp8 | 262144 | 235929 | 0.08 | 0.45 | n/a | 99.9 | 0 |
| Crusoe | crusoe/fp8 | fp8 | 262144 | 235929 | 0.3 | 2.4 | 0.15 | 100 | 0 |

##### nvidia/nemotron-3-ultra-550b-a55b

Source: https://openrouter.ai/api/v1/models/nvidia/nemotron-3-ultra-550b-a55b/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 5. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4/flex | fp4 | 262144 | 16384 | 0.4 | 1.76 | 0.08 | 100 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 262144 | 16384 | 0.5 | 2.2 | 0.1 | 100 | 0 |
| BaseTen | baseten/fp4/us | fp4 | 202800 | 182520 | 0.6 | 2.4 | 0.12 | 99.3 | 0 |
| BaseTen | baseten/fp4 | fp4 | 202800 | 182520 | 0.6 | 2.4 | 0.12 | 98.9 | 0 |
| Venice | venice/fp8 | fp8 | 256000 | 32768 | 0.625 | 3.125 | 0.1875 | 100 | 0 |

##### openai/gpt-oss-120b

Source: https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints (checked 2026-10-22). Distinct providers: 22. Endpoints: 24. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Near AI | near-ai/fp4 | fp4 | 131072 | 117964 | 0.03 | 0.15 | 0.015 | 97.5 | 0 |
| Venice | venice/int4 | int4 | 128000 | 32768 | 0.03 | 0.15 | 0.03 | 99.5 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 131072 | 117964 | 0.03 | 0.17 | 0.03 | 99.7 | 0 |
| DeepInfra | deepinfra/bf16 | bf16 | 131072 | 117964 | 0.037 | 0.17 | n/a | 100 | 0 |
| DekaLLM | dekallm/bf16 | bf16 | 131072 | 117964 | 0.03 | 0.18 | 0.03 | 100 | 0 |
| AkashML | akashml/bf16 | bf16 | 131072 | 117964 | 0.03 | 0.187 | 0.03 | 99.9 | 0 |
| Crusoe | crusoe/bf16 | bf16 | 131072 | 117964 | 0.05 | 0.25 | 0.05 | 99.7 | 0 |
| Mancer 2 | mancer/fp8 | fp8 | 131072 | 117964 | 0.05 | 0.25 | n/a | 99.8 | 0 |
| Novita | novita/fp4 | fp4 | 131072 | 32768 | 0.05 | 0.25 | n/a | 100 | 0 |
| Google | google-vertex/global | unknown | 131072 | 117964 | 0.09 | 0.36 | n/a | 80 | -5 |
| DigitalOcean | digitalocean | unknown | 128000 | 4096 | 0.06 | 0.42 | 0.012 | 100 | 0 |
| BaseTen | baseten/fp4/us | fp4 | 128072 | 115264 | 0.1 | 0.5 | 0.1 | 99.8 | 0 |
| BaseTen | baseten/fp4 | fp4 | 128072 | 115264 | 0.1 | 0.5 | 0.1 | 99.5 | 0 |
| Amazon Bedrock | amazon-bedrock/eu-west-1 | unknown | 131072 | 117964 | 0.15 | 0.6 | n/a | 100 | 0 |
| Nebius | nebius/fp4 | fp4 | 131072 | 117964 | 0.15 | 0.6 | n/a | 100 | 0 |
| Amazon Bedrock | amazon-bedrock | unknown | 131072 | 117964 | 0.15 | 0.6 | n/a | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 131072 | 8192 | 0.15 | 0.6 | 0.075 | 97 | 0 |
| Phala | phala | unknown | 131072 | 32768 | 0.15 | 0.6 | n/a | 99.8 | 0 |
| Together | together | unknown | 131072 | 117964 | 0.15 | 0.6 | n/a | 97.8 | 0 |
| Groq | groq | unknown | 131072 | 65536 | 0.15 | 0.6 | 0.075 | 100 | 0 |
| Parasail | parasail/fp4 | fp4 | 131072 | 117964 | 0.1 | 0.75 | 0.055 | 100 | 0 |
| Mara | mara | unknown | 131072 | 117964 | 0.15 | 0.75 | n/a | 89.5 | 0 |
| Cerebras | cerebras/fp16 | fp16 | 131072 | 40960 | 0.35 | 0.75 | 0.35 | 100 | 0 |
| SambaNova | sambanova | unknown | 131072 | 117964 | 0.14 | 0.95 | n/a | 100 | 0 |

##### openai/gpt-oss-20b

Source: https://openrouter.ai/api/v1/models/openai/gpt-oss-20b/endpoints (checked 2026-10-22). Distinct providers: 10. Endpoints: 11. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Darkbloom | darkbloom/fp8 | fp8 | 131072 | 32768 | 0.018 | 0.09 | 0.009 | 100 | 0 |
| AkashML | akashml/fp4 | fp4 | 131072 | 117964 | 0.02 | 0.1 | n/a | 100 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 131072 | 117964 | 0.03 | 0.13 | 0.03 | 100 | 0 |
| DekaLLM | dekallm/bf16 | bf16 | 131072 | 117964 | 0.029 | 0.14 | 0.029 | 100 | 0 |
| DeepInfra | deepinfra/bf16 | bf16 | 131072 | 117964 | 0.03 | 0.14 | n/a | 99.3 | 0 |
| Parasail | parasail/fp4 | fp4 | 131072 | 117964 | 0.03 | 0.15 | 0.02 | 99.9 | 0 |
| Amazon Bedrock | amazon-bedrock/eu-west-1 | unknown | 131072 | 117964 | 0.07 | 0.15 | n/a | 100 | 0 |
| Amazon Bedrock | amazon-bedrock | unknown | 131072 | 117964 | 0.07 | 0.15 | n/a | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 131072 | 8192 | 0.04 | 0.18 | n/a | 92.1 | -2 |
| Google | google-vertex/us-central1 | unknown | 131072 | 32768 | 0.07 | 0.25 | n/a | 46.2 | -5 |
| Groq | groq | unknown | 131072 | 65536 | 0.075 | 0.3 | 0.0375 | 97.2 | 0 |

##### qwen/qwen3-235b-a22b-2507

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-235b-a22b-2507/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 6. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| GMICloud | gmicloud/fp8 | fp8 | 262144 | 235929 | 0.0875 | 0.35 | 0.0175 | 0 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 262144 | 16384 | 0.09 | 0.55 | n/a | 81.8 | 0 |
| Venice | venice/fp8 | fp8 | 128000 | 16384 | 0.15 | 0.75 | n/a | 91.4 | 0 |
| Parasail | parasail/fp8 | fp8 | 131072 | 117964 | 0.14 | 0.8 | 0.05 | 100 | 0 |
| Google | google-vertex/us-south1 | unknown | 262144 | 16384 | 0.22 | 0.88 | n/a | 26 | -5 |
| Google | google-vertex/us-south1 | unknown | 262144 | 16384 | 0.25 | 1 | n/a | 27.1 | -5 |

##### qwen/qwen3-235b-a22b-thinking-2507

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-235b-a22b-thinking-2507/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 128000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Venice | venice/fp8 | fp8 | 128000 | 16384 | 0.45 | 3.5 | n/a | 100 | 0 |

##### qwen/qwen3-32b

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-32b/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8 | fp8 | 40960 | 16384 | 0.08 | 0.28 | n/a | 96 | 0 |
| Tenstorrent | tenstorrent/fp8 | fp8 | 20000 | 16400 | 0.14 | 0.4 | 0.09 | 99.7 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 131072 | 117964 | 0.14 | 0.57 | n/a | 99.4 | 0 |

##### qwen/qwen3-coder-flash

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-coder-flash/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 1000000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Alibaba | alibaba | unknown | 1000000 | 65536 | 0.195 | 0.975 | 0.039 | 100 | 0 |

##### qwen/qwen3-coder-next

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-coder-next/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Parasail | parasail/bf16 | bf16 | 262144 | 235929 | 0.12 | 0.8 | 0.07 | 100 | 0 |

##### qwen/qwen3-coder

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-coder/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/turbo | fp4 | 262144 | 65536 | 0.3 | 1 | 0.1 | 94.7 | -2 |
| Venice | venice/fp8 | fp8 | 256000 | 65536 | 0.35 | 1.5 | 0.04 | 80.3 | -2 |
| Google | google-vertex/us-south1 | unknown | 262144 | 65536 | 0.22 | 1.8 | n/a | 62 | -5 |

##### qwen/qwen3.6-35b-a3b

Source: https://openrouter.ai/api/v1/models/qwen/qwen3.6-35b-a3b/endpoints (checked 2026-10-22). Distinct providers: 10. Endpoints: 10. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Darkbloom | darkbloom/fp4 | fp4 | 262144 | 32768 | 0.05 | 0.7 | 0.025 | 100 | 0 |
| AkashML | akashml/fp8 | fp8 | 262144 | 235929 | 0.1 | 0.9 | 0.05 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 262144 | 65536 | 0.1 | 0.95 | 0.1 | 99 | 0 |
| Parasail | parasail/fp8 | fp8 | 262144 | 235929 | 0.1 | 0.95 | 0.05 | 100 | 0 |
| DekaLLM | dekallm | unknown | 262144 | 235929 | 0.1 | 1 | 0.05 | 99.6 | 0 |
| Venice | venice/fp8 | fp8 | 256000 | 65536 | 0.1 | 1 | n/a | 100 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 262144 | 235929 | 0.25 | 1.25 | 0.25 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 262144 | 65536 | 0.25 | 1.25 | 0.25 | 99.3 | 0 |
| Phala | phala | unknown | 262144 | 235929 | 0.2 | 1.27 | 0.056 | 96.8 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 262144 | 235929 | 0.24 | 1.8 | 0.15 | 96.6 | 0 |

##### qwen/qwen3.8-2.4t-a95b

Source: https://openrouter.ai/api/v1/models/qwen/qwen3.8-2.4t-a95b/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Novita | novita | unknown | 1000000 | 131072 | 2 | 6 | 0.25 | 99.8 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 131072 | 2 | 6 | 0.25 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 131072 | 2 | 6 | 0.25 | 100 | 0 |
| Venice | venice | unknown | 262144 | 65536 | 2 | 6 | 0.25 | 100 | 0 |
| Together | together | unknown | 1010000 | 909000 | 2 | 6 | 0.25 | 99.8 | 0 |

##### qwen/qwen3.8-27b

Source: https://openrouter.ai/api/v1/models/qwen/qwen3.8-27b/endpoints (checked 2026-10-22). Distinct providers: 20. Endpoints: 20. Model context: 1000000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Chutes | chutes/fp8 | fp8 | 262144 | 65536 | 0.039 | 1.25 | 0.0039 | 100 | 0 |
| Near AI | near-ai/fp8 | fp8 | 262144 | 65536 | 0.04 | 1.35 | 0.018 | 96.5 | 0 |
| Cerebras | cerebras/fp16 | fp16 | 65536 | 32768 | 0.99 | 1.49 | 0.99 | 100 | 0 |
| DeepInfra | deepinfra/bf16 | bf16 | 262144 | 235929 | 0.15 | 1.875 | 0.0375 | 100 | 0 |
| Ionstream | ionstream/fp8 | fp8 | 262144 | 65536 | 0.04 | 1.95 | 0.02 | 98.4 | 0 |
| AkashML | akashml/fp8 | fp8 | 262144 | 131072 | 0.225 | 1.98 | 0.05 | 100 | 0 |
| Darkbloom | darkbloom/fp4 | fp4 | 262144 | 32768 | 0.035 | 2.2 | 0.0175 | 73.4 | 0 |
| Reka | reka/fp8 | fp8 | 262144 | 235929 | 0.04 | 2.2 | 0.02 | 99.8 | 0 |
| Parasail | parasail/fp8 | fp8 | 262144 | 235929 | 0.24 | 2.2 | 0.05 | 99.6 | 0 |
| Modal | modal | unknown | 262144 | 235929 | 0.04 | 2.3 | 0.02 | 99.9 | 0 |
| Wafer | wafer/fp8 | fp8 | 262144 | 235929 | 0.06 | 2.3 | 0.059 | 98.3 | 0 |
| DekaLLM | dekallm | unknown | 262144 | 235929 | 0.04 | 2.5 | 0.02 | 100 | 0 |
| ModelRun | modelrun/fp4 | fp4 | 262144 | 235929 | 0.2 | 2.5 | 0.09 | 100 | 0 |
| Mancer 2 | mancer/fp8 | fp8 | 262144 | 235929 | 0.2 | 2.5 | n/a | 99.4 | 0 |
| Phala | phala | unknown | 1000000 | 262144 | 0.2 | 2.5 | 0.05 | 99.6 | -2 |
| Alibaba | alibaba | unknown | 1000000 | 131072 | 0.425 | 2.55 | 0.085 | 99.8 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 262144 | 235929 | 0.4 | 3 | 0.15 | 100 | 0 |
| Novita | novita | unknown | 1000000 | 131072 | 0.42 | 3 | 0.085 | 99.8 | 0 |
| Cloudflare | cloudflare | unknown | 262144 | 235929 | 0.45 | 3.2 | 0.05 | 100 | 0 |
| Venice | venice/fp8 | fp8 | 262144 | 65536 | 0.45 | 3.2 | n/a | 100 | 0 |

##### qwen/qwen3.8-flash

Source: https://openrouter.ai/api/v1/models/qwen/qwen3.8-flash/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 2. Model context: 1000000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Alibaba | alibaba/us-east-1 | unknown | 1000000 | 131072 | 0.15 | 0.47 | 0.016 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 131072 | 0.15 | 0.47 | 0.016 | 100 | 0 |

##### stepfun/step-5-preview

Source: https://openrouter.ai/api/v1/models/stepfun/step-5-preview/endpoints (checked 2026-10-22). Distinct providers: 4. Endpoints: 5. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| InferenceNet | inference-net/us | fp4 | 1048576 | 131072 | 1 | 2.7 | 0.05 | 100 | 0 |
| InferenceNet | inference-net/fp4 | fp4 | 1048576 | 131072 | 1 | 2.7 | 0.05 | 100 | 0 |
| Featherless | featherless/fp4 | fp4 | 262144 | 32768 | 1 | 2.7 | 0.1 | 0 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 65536 | 1 | 2.7 | 0.1 | 100 | 0 |
| StepFun | stepfun/fp8 | fp8 | 1000000 | 64000 | 1 | 2.7 | 0.1 | 100 | 0 |

##### tencent/hy3

Source: https://openrouter.ai/api/v1/models/tencent/hy3/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Tencent | tencent/fp8 | fp8 | 262144 | 128000 | 0.132 | 0.528 | 0.033 | 100 | 0 |
| Novita | novita | unknown | 262144 | 235929 | 0.14 | 0.58 | 0.035 | 100 | 0 |
| GMICloud | gmicloud/bf16 | bf16 | 262144 | 235929 | 0.14 | 0.58 | 0.035 | 99.9 | 0 |
| Phala | phala | unknown | 262144 | 235929 | 0.15 | 0.64 | 0.04 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 262144 | 131072 | 0.2 | 0.8 | 0.05 | 100 | 0 |

##### tencent/hy4-preview

Source: https://openrouter.ai/api/v1/models/tencent/hy4-preview/endpoints (checked 2026-10-22). Distinct providers: 4. Endpoints: 4. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4 | fp4 | 1048576 | 131072 | 0.834 | 2.501 | 0.042 | 99.7 | 0 |
| Novita | novita/fp8 | fp8 | 1000000 | 64000 | 0.834 | 2.501 | 0.042 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 262144 | 0.834 | 2.501 | 0.042 | 100 | 0 |
| Tencent | tencent/fp8 | fp8 | 1048576 | 64000 | 0.834 | 2.501 | 0.042 | 100 | 0 |

##### xiaomi/mimo-v2.6-flash

Source: https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-flash/endpoints (checked 2026-10-22). Distinct providers: 9. Endpoints: 9. Model context: 1050000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 943718 | 0.133 | 0.266 | 0.0027 | 98.5 | 0 |
| Darkbloom | darkbloom/fp4 | fp4 | 1048576 | 131072 | 0.1 | 0.28 | 0.05 | 99.5 | 0 |
| Makora | makora/fp8 | fp8 | 1048576 | 131072 | 0.13 | 0.28 | 0.002 | 96.5 | 0 |
| Relace | relace/mxfp4 | mxfp4 | 1048576 | 131072 | 0.13 | 0.28 | 0.003 | 99.9 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 131072 | 0.14 | 0.28 | 0.0028 | 99.6 | 0 |
| GMICloud | gmicloud/bf16 | bf16 | 1050000 | 945000 | 0.14 | 0.28 | 0.003 | 94.3 | -2 |
| Xiaomi | xiaomi/fp8 | fp8 | 1048576 | 131072 | 0.14 | 0.28 | 0.0028 | 100 | 0 |
| Io Net | io-net/fp8 | fp8 | 1048320 | 131072 | 0.15 | 0.29 | 0.025 | 99.2 | 0 |
| Venice | venice/fp8 | fp8 | 1000000 | 131072 | 0.175 | 0.35 | 0.0037 | 99.3 | 0 |

##### xiaomi/mimo-v2.6-pro

Source: https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-pro/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 1050000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 943718 | 0.387 | 0.783 | 0.0032 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 131072 | 0.435 | 0.87 | 0.0036 | 98.9 | -2 |
| GMICloud | gmicloud/bf16 | bf16 | 1050000 | 945000 | 0.435 | 0.87 | 0.004 | 99.4 | 0 |
| Xiaomi | xiaomi/fp8 | fp8 | 1048576 | 131072 | 0.435 | 0.87 | 0.0036 | 99.4 | 0 |
| StreamLake | streamlake | unknown | 1000000 | 128000 | 0.522 | 1.044 | 0.0043 | 30.8 | 0 |

##### z-ai/glm-4.5

Source: https://openrouter.ai/api/v1/models/z-ai/glm-4.5/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Z.AI | z-ai/fp8 | fp8 | 131072 | 98304 | 0.6 | 2.2 | 0.11 | 100 | 0 |

##### z-ai/glm-4.6

Source: https://openrouter.ai/api/v1/models/z-ai/glm-4.6/endpoints (checked 2026-10-22). Distinct providers: 4. Endpoints: 5. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4/flex | fp4 | 202752 | 131072 | 0.4 | 1.6 | 0.08 | n/a | 0 |
| Venice | venice/fp4 | fp4 | 198000 | 16384 | 0.43 | 1.75 | 0.08 | 80 | -5 |
| DeepInfra | deepinfra/fp4 | fp4 | 202752 | 131072 | 0.5 | 2 | 0.1 | 99.6 | 0 |
| Novita | novita/bf16 | bf16 | 204800 | 131072 | 0.55 | 2.2 | 0.11 | 99.8 | 0 |
| Z.AI | z-ai/fp4 | fp4 | 202752 | 131072 | 0.6 | 2.2 | 0.11 | 99.9 | 0 |

##### z-ai/glm-4.7

Source: https://openrouter.ai/api/v1/models/z-ai/glm-4.7/endpoints (checked 2026-10-22). Distinct providers: 6. Endpoints: 7. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4/flex | fp4 | 202752 | 131072 | 0.32 | 1.4 | 0.064 | 100 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 202752 | 131072 | 0.4 | 1.75 | 0.08 | 94.7 | 0 |
| Venice | venice/fp4 | fp4 | 198000 | 16384 | 0.4004 | 1.9292 | 0.0801 | 60.3 | 0 |
| Novita | novita/fp8 | fp8 | 204800 | 131072 | 0.54 | 1.98 | 0.099 | 99.6 | 0 |
| Google | google-vertex | unknown | 200000 | 128000 | 0.6 | 2.2 | n/a | 45.2 | -5 |
| Z.AI | z-ai/fp4 | fp4 | 202752 | 131072 | 0.6 | 2.2 | 0.11 | 99.7 | 0 |
| Mancer 2 | mancer/fp4 | fp4 | 131072 | 117964 | 0.7 | 2.5 | n/a | 64.5 | 0 |

##### z-ai/glm-5.3-flash

Source: https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints (checked 2026-10-22). Distinct providers: 30. Endpoints: 34. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 128000 | 0.0435 | 0.145 | 0.0087 | 98.8 | -5 |
| OpenInference | open-inference/fp4 | fp4 | 1048576 | 943718 | 0.0052 | 0.1985 | 0.0052 | 99.9 | 0 |
| Relace | relace | unknown | 1048576 | 131072 | 0.0052 | 0.1985 | 0.0052 | 100 | 0 |
| Wafer | wafer/nvfp4 | nvfp4 | 1048576 | 131072 | 0.074 | 0.2 | 0.073 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048576 | 943718 | 0.075 | 0.25 | 0.015 | 97.1 | 0 |
| Sail Research | sail-research/us | fp4 | 1048576 | 131072 | 0.0784 | 0.25 | 0.0261 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 131072 | 0.0784 | 0.25 | 0.0261 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 131072 | 0.084 | 0.28 | 0.0168 | 99.9 | 0 |
| InferenceNet | inference-net/us | fp4 | 1048576 | 262144 | 0.12 | 0.388 | 0.032 | 100 | 0 |
| InferenceNet | inference-net/fp4 | fp4 | 1048576 | 262144 | 0.12 | 0.388 | 0.032 | 100 | 0 |
| Phala | phala/nvfp4 | nvfp4 | 1048576 | 131072 | 0.1275 | 0.425 | 0.0255 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 131072 | 0.1312 | 0.4375 | 0.03 | 100 | 0 |
| Makora | makora | unknown | 1048576 | 131072 | 0.14 | 0.47 | 0.024 | 99.4 | 0 |
| Near AI | near-ai/fp8 | fp8 | 1048576 | 943718 | 0.08 | 0.5 | 0.012 | 92.8 | -5 |
| PrimeIntellect | primeintellect | unknown | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | 97.3 | 0 |
| Modal | modal/nvfp4 | nvfp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | n/a | 0 |
| BaseTen | baseten/fp8/us | fp8 | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | n/a | 0 |
| Crusoe | crusoe/fp4 | fp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 94.5 | 0 |
| CoreWeave | coreweave/nvfp4 | nvfp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.02 | 99.9 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | 96.1 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 99 | 0 |
| Friendli | friendli | unknown | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 262144 | 0.15 | 0.5 | 0.03 | 99.7 | -5 |
| Together | together | unknown | 1048575 | 943717 | 0.15 | 0.5 | 0.03 | 99 | -2 |
| Parasail | parasail/fp4 | fp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 99.9 | 0 |
| BaseTen | baseten/fp8 | fp8 | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | n/a | 0 |
| Venice | venice | unknown | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | 99.9 | -2 |
| DeepInfra | deepinfra/fp4 | fp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 99.9 | 0 |
| Z.AI | z-ai/fp8 | fp8 | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | 100 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.143 | 0.65 | 0.04 | 99.4 | 0 |
| Inceptron | inceptron/fp8 | fp8 | 1048576 | 943718 | 0.18 | 0.69 | 0.075 | 100 | 0 |
| NextBit | nextbit/fp4 | fp4 | 1048576 | 128000 | 0.15 | 0.75 | 0.05 | 96.9 | 0 |
| Fireworks | fireworks/us | unknown | 1048576 | 943718 | 0.225 | 0.75 | 0.045 | 100 | 0 |
| Reka | reka | unknown | 1048576 | 943718 | 0.08 | 1.6 | 0.04 | 99.9 | 0 |

##### z-ai/glm-5.3-flashx

Source: https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flashx/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Z.AI | z-ai/fp8 | fp8 | 1048576 | 131072 | 0.37 | 1.25 | 0.09 | 100 | 0 |

##### z-ai/glm-5.3

Source: https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints (checked 2026-10-22). Distinct providers: 37. Endpoints: 48. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Wafer | wafer/us | fp4 | 1048576 | 943718 | 0.079 | 1.4 | 0.078 | 100 | 0 |
| Wafer | wafer/fp4 | fp4 | 1048576 | 943718 | 0.179 | 1.4 | 0.178 | 100 | 0 |
| Inceptron | inceptron/fp4 | fp4 | 1048576 | 943718 | 0.45 | 1.96 | 0.145 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 131072 | 0.63 | 1.98 | 0.117 | 100 | 0 |
| Sail Research | sail-research/us | fp8 | 1048576 | 943718 | 0.5 | 2 | 0.08 | 100 | 0 |
| Sail Research | sail-research/fp8 | fp8 | 1048576 | 943718 | 0.5 | 2 | 0.08 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 262144 | 0.7 | 2.2 | 0.13 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048576 | 943718 | 0.7 | 2.2 | 0.13 | 100 | 0 |
| Relace | relace | unknown | 1048576 | 131072 | 0.75 | 2.4 | 0.075 | 100 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 1048576 | 131072 | 0.5625 | 2.5 | 0.125 | 98.1 | 0 |
| Phala | phala | unknown | 1048576 | 943718 | 0.84 | 2.64 | 0.156 | 97.5 | 0 |
| Decart | decart/fp4 | fp4 | 1048576 | 943718 | 0.84 | 2.71 | 0.19 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 128000 | 0.91 | 2.86 | 0.169 | 99 | 0 |
| DekaLLM | dekallm | unknown | 1048576 | 943718 | 0.18 | 2.95 | 0.15 | 99.7 | 0 |
| Fireworks | fireworks/spot | unknown | 1048576 | 943718 | 0.98 | 3.08 | 0.182 | 100 | 0 |
| Io Net | io-net/fp8 | fp8 | 262124 | 131072 | 0.49 | 3.2 | 0.15 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 131072 | 1.19 | 3.74 | 0.238 | 100 | 0 |
| Friendli | friendli | unknown | 1048576 | 943718 | 1.26 | 3.96 | 0.234 | 100 | 0 |
| InferenceNet | inference-net/fp4 | fp4 | 1048576 | 943718 | 0.08 | 4 | 0.076 | 100 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 1048576 | 943718 | 1.2 | 4 | 0.19 | 95.6 | -5 |
| Reka | reka | unknown | 1048576 | 262144 | 0.14 | 4.2 | 0.105 | 100 | 0 |
| InferenceNet | inference-net/us | fp4 | 1048576 | 943718 | 0.08 | 4.381 | 0.076 | 100 | 0 |
| Baidu | baidu/fp8 | fp8 | 1048576 | 131072 | 1.3986 | 4.3956 | 0.2597 | 99.8 | 0 |
| Makora | makora/fp4 | fp4 | 1048576 | 128000 | 0.14 | 4.4 | 0.1 | 89.4 | 0 |
| AkashML | akashml/fp8 | fp8 | 1048576 | 131072 | 0.19 | 4.4 | 0.19 | 100 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.232 | 4.4 | 0.058 | 100 | 0 |
| Mistral | mistral/zdr | nvfp4 | 1048576 | 131072 | 1.4 | 4.4 | 0.14 | 99 | 0 |
| BaseTen | baseten/fp4/us | fp4 | 1048576 | 262144 | 1.4 | 4.4 | 0.14 | 99.7 | -5 |
| Mistral | mistral/nvfp4 | nvfp4 | 1048576 | 131072 | 1.4 | 4.4 | 0.14 | 99.4 | 0 |
| Nebius | nebius/fp4 | fp4 | 1024000 | 921600 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Crusoe | crusoe/fp4 | fp4 | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 99.9 | 0 |
| PrimeIntellect | primeintellect | unknown | 1048576 | 131072 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Venice | venice | unknown | 1000000 | 131072 | 1.4 | 4.4 | 0.26 | 96.2 | 0 |
| Together | together | unknown | 1048575 | 943717 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 99.7 | 0 |
| Modal | modal | unknown | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 99.7 | 0 |
| BaseTen | baseten/fp4 | fp4 | 1048576 | 262144 | 1.4 | 4.4 | 0.14 | 95.8 | -5 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 131072 | 1.4 | 4.4 | 0.26 | 99.7 | 0 |
| Z.AI | z-ai/fp8 | fp8 | 1048576 | 131072 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Mistral | mistral/nvfp4/eu | nvfp4 | 1048576 | 131072 | 1.54 | 4.84 | 0.154 | 100 | 0 |
| Amazon Bedrock | amazon-bedrock/us-east-1 | unknown | 1048576 | 131072 | 1.68 | 5.28 | 0.312 | 99 | 0 |
| ModelRun | modelrun/fp4 | fp4 | 1048576 | 524288 | 2.1 | 6.6 | 0.4 | 100 | 0 |
| Fireworks | fireworks/fast | unknown | 1048576 | 943718 | 2.1 | 6.6 | 0.39 | 98.6 | 0 |
| BaseTen | baseten/us/fast | fp8 | 1048576 | 262144 | 2.1 | 6.6 | 0.21 | 99.9 | 0 |
| BaseTen | baseten/fast | fp8 | 1048576 | 262144 | 2.1 | 6.6 | 0.21 | 100 | 0 |
| Alibaba | alibaba/prime | unknown | 1000000 | 131072 | 2.8 | 8.8 | 0.56 | 100 | 0 |

##### z-ai/glm-5

Source: https://openrouter.ai/api/v1/models/z-ai/glm-5/endpoints (checked 2026-10-22). Distinct providers: 8. Endpoints: 8. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| StreamLake | streamlake/fp8 | fp8 | 198000 | 128000 | 0.6 | 1.92 | 0.12 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 202752 | 182476 | 0.6 | 1.92 | 0.12 | 99.9 | 0 |
| Baidu | baidu/fp8 | fp8 | 202752 | 131072 | 0.7 | 2.24 | 0.14 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 204800 | 131072 | 0.95 | 2.55 | 0.2 | 99.8 | 0 |
| Amazon Bedrock | amazon-bedrock | unknown | 202752 | 131072 | 1 | 3.2 | n/a | 100 | 0 |
| Venice | venice/fp8 | fp8 | 198000 | 32000 | 1 | 3.2 | 0.2 | 98.9 | 0 |
| Novita | novita/fp8 | fp8 | 202800 | 131072 | 1 | 3.2 | 0.2 | 100 | 0 |
| Z.AI | z-ai/fp8 | fp8 | 202752 | 131072 | 1 | 3.2 | 0.2 | 99.7 | 0 |

### Inferences
- None beyond those stated in the sections above.

### Gaps
- Endpoint status values other than 0 (for example -5 on some CoreWeave and BaseTen rows) are not documented on the pages read; they are reported as-is.
