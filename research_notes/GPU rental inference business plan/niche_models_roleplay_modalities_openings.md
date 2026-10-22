# Niche open-weight models, roleplay demand, other modalities, and where a small provider can plug in

All numbers below were read live on 2026-10-22 unless a row says "not checked". "Checked" column = date read. "estimate" marks my arithmetic on cited numbers. "not found" means I looked and the source did not state it. The web-search budget ran out mid-task, so some items rely on fetched primary pages only.

Method notes:
- OpenRouter model list: `GET https://openrouter.ai/api/v1/models` (468 text models) and `GET https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints` for all 449 non-alias slugs (crawled 2026-10-22). Provider counts below are distinct provider names per model from that crawl.
- Weekly and daily token figures come from https://openrouter.ai/rankings ("Usage data through Oct 21, 2026"), https://openrouter.ai/models?order=top-weekly, https://openrouter.ai/apps, and individual model pages (rendered in a browser). Model-page "Apps" token counts are shown without a labeled time window. Model-page "Activity" numbers are the latest daily bucket shown on the chart.
- OpenRouter also exposes an authenticated Datasets API (`GET https://openrouter.ai/api/v1/datasets/rankings-daily`, top 50 models per UTC day, `category=roleplay` supported, CC BY 4.0, 30 req/min, 500 req/day) per https://openrouter.ai/docs/api/api-reference/datasets/get-rankings-daily. I did not call it (needs an API key).

## Key question 1: Which open-weight models on OpenRouter have the best ratio of weekly tokens to provider count, and what do they pay per million tokens?

### Takeaway
Of 449 OpenRouter text models crawled on 2026-10-22, 384 (86%) have 3 or fewer distinct providers and 290 have exactly one. The high-volume models (DeepSeek V4.1 Flash 25.7T tokens/week, GLM 5.3 Flash 11.3T) have many providers; the community roleplay fine-tunes have one provider each and move roughly 10M to 150M tokens per day at $0.30 to $1.00 per million. Several well-known roleplay slugs (Euryale L3.3, Hermes 4 70B, Rocinante, Midnight Rose, Lumimaid, WizardLM-2 8x22B, Llama 3.1 405B) are listed on OpenRouter with zero providers today.

### Cited Findings

Provider-count distribution across all OpenRouter text models (crawl of endpoints API, checked 2026-10-22):

| Distinct providers | Models | Source |
|---|---|---|
| 0 | 8 | https://openrouter.ai/api/v1/models/{slug}/endpoints (449 slugs crawled) |
| 1 | 290 | same |
| 2 | 63 | same |
| 3 | 23 | same |
| 4 to 5 | 33 | same |
| 6 or more | 32 | same |

Top models by weekly tokens (two OpenRouter views disagree slightly; both read 2026-10-22):

| Rank | Model | Rankings page "This Week" | /models?order=top-weekly | Providers (crawl) | Checked |
|---|---|---|---|---|---|
| 1 | DeepSeek V4.1 Flash | 25.7T tokens | 27.6T | many (not counted) | 2026-10-22 |
| 2 | DeepSeek V4.1 Flash 1017 | 16.5T | 20.1T | many | 2026-10-22 |
| 3 | GLM 5.3 Flash | 11.3T | 12.5T | many | 2026-10-22 |
| 4 | MiniMax M3.1 Flash (free) | 10.3T | not listed | 1 (Minimax) | 2026-10-22 |
| 5 | MiMo-V2.6-Flash | 8.57T | 9.15T | many | 2026-10-22 |
| 6 | Hy4 preview | 8.55T | 9.74T | many | 2026-10-22 |
| 7 | Claude Opus 5.5 | 7.14T | 7.88T | closed | 2026-10-22 |
| 8 | GPT-6 Luna | 6.08T | 6.68T | closed | 2026-10-22 |
| 9 | GLM 5.3 | 5.21T | 5.75T | many | 2026-10-22 |
| 10 | Nemotron 3 Ultra (free) | 4.46T | 5.04T | 3 paid (BaseTen, DeepInfra, Venice) | 2026-10-22 |
| 11 to 13 | Hy3 3.5T; Muse Spark 1.3 Contributor 3.42T; Jev 1.13 3.21T | from /models page | 1 each (Meta; TypeSafe) for the last two | 2026-10-22 |

Sources: https://openrouter.ai/rankings and https://openrouter.ai/models?order=top-weekly.

Market share by model author, week beginning Oct 12, 2026 (share of text requests): DeepSeek 24.4%, Google 19.7%, OpenAI 18.5%, Z.ai 12.2%, Qwen 5.3%, Anthropic 4.7%, Xiaomi 2.4%, Meta Llama 2.1%, Mistral AI 2.0%, all others 8.6%. Source: https://openrouter.ai/rankings (checked 2026-10-22).

Candidate niche models: providers, prices, and traffic (endpoints API plus model pages, checked 2026-10-22). Price = USD per 1M tokens input / output. "Day" = latest daily bucket on the model page Activity chart (prompt + completion).

| Model slug | Providers (quant, ctx) | Price in/out | Latest day tokens | Top apps (tokens, window unlabeled) | Source |
|---|---|---|---|---|---|
| nousresearch/hermes-3-llama-3.1-405b | 1: DeepInfra (fp8, 131k) | $1.00 / $1.00 | 35.7M prompt + 1.88M completion | Infinite Worlds 161M, Local Keep AI 68.5M, Miniapps.ai 66.9M, Reality Fabricator 59.9M, SillyTavern 52.8M | https://openrouter.ai/nousresearch/hermes-3-llama-3.1-405b |
| nousresearch/hermes-4-405b | 1: Nebius (fp8, 131k) | $1.00 / $3.00 | not captured | SillyTavern 185M, CreatorOS Mentor 58.6M, Auresys 49.4M, G0DM0D3-pliny 46M, Mantella 28.8M | https://openrouter.ai/nousresearch/hermes-4-405b |
| nousresearch/hermes-4-70b | 0 endpoints | none | none | none | https://openrouter.ai/api/v1/models/nousresearch/hermes-4-70b/endpoints |
| nousresearch/hermes-3-llama-3.1-70b | 1: DeepInfra (fp8, 131k) | $0.70 / $0.70 | 72.4M + 3.76M | G0DM0D3-pliny 211M, fanvue-bot 117M, SillyTavern 99M, HornyDreams Prompt Improver 96.2M, WildGirl 82.8M | https://openrouter.ai/nousresearch/hermes-3-llama-3.1-70b |
| gryphe/mythomax-l2-13b | 3: Parasail (fp16, 4k) $0.08/$0.11; Mancer 2 (fp8, 8k) $0.35/$0.60; DeepInfra (fp16, 4k) $0.40/$0.40 | min $0.08/$0.11; median $0.35/$0.40 | 41M + 7.17M | Miniapps.ai 843M, CC Labs 422M, HammerAI 316M, FreedomGPT 152M, ChatSweetie 80.4M. 1-day token share: Parasail 47.7%, DeepInfra 28.7%, Mancer 23.6% | https://openrouter.ai/gryphe/mythomax-l2-13b |
| sao10k/l3.1-euryale-70b | 1: DeepInfra (fp8, 131k) | $0.85 / $0.85 | 36.2M + 1.41M (chart axis up to 80M/day) | SillyTavern 206M, Mantella 142M, stellaai 128M, Sloane 55.2M, StoryNexus 53.7M | https://openrouter.ai/sao10k/l3.1-euryale-70b |
| sao10k/l3-euryale-70b (v2.1) | 0 endpoints | none | none | none | endpoints API |
| sao10k/l3.3-euryale-70b | 0 endpoints | none | none | none | endpoints API |
| sao10k/l3-lunaris-8b | 2: Parasail (bf16) and DeepInfra (fp8) | $0.04 / $0.05 | 348M + 24.5M | HammerAI 7.21B, CoffeeCat 1.9B, Hornyt 1.3B, Halluna 1.24B, Layla 684M | https://openrouter.ai/sao10k/l3-lunaris-8b |
| anthracite-org/magnum-v4-72b | 1: Mancer 2 (fp8, 32k) | $2.50 / $5.00 | 16M + 634K | SillyTavern 132M, Candace 131M, AI Companion 130M, AI Influence Mod 62.2M, Janitor AI 51M | https://openrouter.ai/anthracite-org/magnum-v4-72b |
| thedrummer/cydonia-24b-v4.1 | 1: Parasail (bf16, 131k) | $0.30 / $0.50 (cache read $0.15) | 136M + 5.79M (axis up to 320M/day) | StoryNexus 486M, SillyTavern 193M, GnG-UnrealAngels-TG 172M, Janitor AI 143M, TeaseMe intent judge 140M | https://openrouter.ai/thedrummer/cydonia-24b-v4.1 |
| thedrummer/unslopnemo-12b | 1: Parasail (bf16, 1.0M ctx) | $0.40 / $0.40 | 21.6M + 1.4M | HammerAI 1.13B, Miniapps.ai 265M, SillyTavern 72.8M, Chub AI 41.3M, Yumina 24.5M | https://openrouter.ai/thedrummer/unslopnemo-12b |
| thedrummer/skyfall-36b-v2 | 1: Parasail (fp8, 32k) | $0.55 / $0.80 | 18.7M + 1.74M | SillyTavern 127M, AI Writer Lab 29.1M, Dark GPT 22.8M, Chub AI 22.6M, HammerAI 18.3M | https://openrouter.ai/thedrummer/skyfall-36b-v2 |
| thedrummer/rocinante-12b | 0 endpoints | none | none | none | endpoints API |
| thedrummer/anubis-70b-v1.1 | not on OpenRouter (404) | none | none | none | endpoints API |
| sophosympatheia/midnight-rose-70b | 0 endpoints | none | none | none | endpoints API |
| neversleep/llama-3-lumimaid-70b; neversleep/llama-3.1-lumimaid-8b | 0 endpoints each | none | none | none | endpoints API |
| raifle/sorcererlm-8x22b | 0 endpoints | none | none | none | endpoints API |
| alpindale/goliath-120b | 0 endpoints | none | none | none | endpoints API |
| undi95/remm-slerp-l2-13b | 1: Mancer 2 (fp8, 6k) | $0.35 / $0.65 | 11.9M + 470K | NoFilterGPT 37M, Hello Haven 2.72M, Spicy Chat AI (iOS) 994K | https://openrouter.ai/undi95/remm-slerp-l2-13b |
| mancer/weaver | 1: Mancer 2 (fp8, 8k) | $0.40 / $0.75 | not captured | not captured | endpoints API |
| mistralai/mixtral-8x22b-instruct | 1 provider (Mistral, 3 endpoints) | $2.00 / $6.00 | not captured | not captured | endpoints API |
| microsoft/wizardlm-2-8x22b | 0 endpoints | none | none | none | endpoints API |
| cognitivecomputations/dolphin-mistral-24b-venice-edition ("Venice: Uncensored") | 1: Venice (fp16, 128k) | $0.20 / $0.90 | 78.3M + 8.45M | ChamadaVIP 823M, HotLive 444M, SillyTavern 395M, Janitor AI 159M, Chub AI 144M | https://openrouter.ai/cognitivecomputations/dolphin-mistral-24b-venice-edition |
| cognitivecomputations/dolphin3.0-mistral-24b | 0 endpoints | none | none | none | endpoints API |
| minimax/minimax-m2-her (roleplay model) | 1: Minimax | $0.30 / $1.20 | 56.5M + 963K | Janitor AI 38.1M, SillyTavern 37.5M, LoreWeaver 33.3M, WaifuBot 17.7M | https://openrouter.ai/minimax/minimax-m2-her |
| deepseek/deepseek-chat-v3-0324 | 2: SiliconFlow (fp8) $0.25/$1.00; GMICloud (fp8) $0.29/$1.14 | min $0.25/$1.00 | 1.43B + 67.1M | Janitor AI 24.4B, SpellAI 3.75B, Chub AI 3.34B, SillyTavern 2.54B | https://openrouter.ai/deepseek/deepseek-chat-v3-0324 |
| qwen/qwen-2.5-72b-instruct | 1: DeepInfra (fp8, 32k) | $0.36 / $0.40 | 167M + 13.8M | Stockteller 442M, Fraction AI 199M, FreshRAG-MAS 184M | https://openrouter.ai/qwen/qwen-2.5-72b-instruct |
| meta-llama/llama-3.1-405b (base) and llama-3.1-405b-instruct | 0 endpoints each | none | none | none | endpoints API |
| mistralai/mistral-nemo | 5: Io Net $0.0166/$0.0216; DekaLLM $0.018/$0.03; DeepInfra $0.029/$0.03; Parasail $0.03/$0.03; Mistral $0.15/$0.15 | min $0.0166/$0.0216; median $0.029/$0.03 | 14.2B + 726M | HammerAI 123B, LunarCrush 13.2B, claude-mem 12.8B. DeepInfra holds 87.0% 1-day token share | https://openrouter.ai/mistralai/mistral-nemo |
| meta-llama/llama-3.3-70b-instruct | 11 endpoints | min $0.10/$0.32 (DeepInfra); median $0.45/$0.72 | not captured | not captured | endpoints API |
| google/gemma-3-27b-it | 5 | min $0.08/$0.16; median $0.08/$0.30 | not captured | not captured | endpoints API |
| deepseek/deepseek-r1-0528 | 3 | min $0.50/$2.15 | not captured | not captured | endpoints API |
| moonshotai/kimi-k2-0905 | 1: Novita | $0.60 / $2.50 | not captured | not captured | endpoints API |
| qwen/qwen3-235b-a22b-2507 | 6 | min $0.0875/$0.35 | not captured | not captured | endpoints API |
| tngtech/deepseek-r1t-chimera and r1t2-chimera | 0 endpoints | none | none | none | endpoints API |

Other single-provider open-weight models with ≤3 providers seen in the crawl (price in/out, checked 2026-10-22): qwen/qwen3-vl-8b-instruct (Parasail, $0.25/$0.75); qwen/qwen2.5-vl-72b-instruct (Parasail, $0.80/$1.00); qwen/qwen3-coder-next (Parasail, $0.12/$0.80); microsoft/phi-4 (DeepInfra, $0.07/$0.14); meta-llama/llama-guard-4-12b (DeepInfra, $0.18/$0.18); qwen/qwen-2.5-coder-32b-instruct (Cloudflare, $0.66/$1.00); meta-llama/llama-3.1-70b-instruct (2: Bedrock, DeepInfra, $0.40/$0.40); qwen/qwen3-32b (3, $0.08/$0.28); moonshotai/kimi-k2-thinking (2); z-ai/glm-4.5-air (3, $0.13/$0.85). Source: endpoints crawl.

Who serves what on OpenRouter (distinct models per provider in the crawl, checked 2026-10-22): DeepInfra 77; Novita 48; SiliconFlow 41; Parasail 40 (includes all three TheDrummer models, Lunaris, MythoMax, Mistral Nemo); Venice 37; Phala 20; Together 19; Nebius 12; BaseTen 12; Mancer 2: 9 (MythoMax, ReMM, Weaver, Magnum v4 72B, Qwen3.8 27B, DeepSeek V4 Flash x2, GLM 4.7, gpt-oss-120b); InferenceNet 8; AkashML 7; Io Net 7; Fireworks 7; Chutes 6; Modal 6; PrimeIntellect 6; Groq 6; Near AI 3; Ionstream 3; Featherless 1 (stepfun/step-5-preview); Infermatic 0 (listed as a provider at https://openrouter.ai/api/v1/providers but no endpoints). The providers list has 114 entries.

OpenRouter category lists (API `?category=roleplay`, order as returned, sort key undocumented, checked 2026-10-22): tencent/hy4-preview, deepseek/deepseek-v4-flash, deepseek-v4.1-flash, deepseek-v4-flash-0731, z-ai/glm-5.3-flash, google/gemma-4-31b-it, xiaomi/mimo-v2.6-flash, deepseek-v3.2, gemini-3-flash-preview, gemini-3.8-flash, deepseek-v4.1-flash-1017, mimo-v2.6-pro, glm-5.2, gemini-2.5-flash-lite, gpt-6-luna, mimo-v2.5-pro, deepseek-v4-pro-0813, claude-sonnet-4.5, gemma-4-26b-a4b-it (19 models). No community fine-tune appears. Valid categories: programming, roleplay, marketing, marketing/seo, technology, science, translation, legal, finance, health, trivia, academia. Source: https://openrouter.ai/api/v1/models?category=roleplay.

### Inferences
- Ratio ranking (tokens per provider, estimate from the daily buckets above): deepseek-chat-v3-0324 (~1.5B/day over 2 providers) > mistral-nemo (~14.9B/day over 5, but DeepInfra holds 87%) > lunaris-8b (~372M/day over 2) > cydonia-24b-v4.1 (~142M/day, 1) > qwen-2.5-72b (~181M/day, 1) > dolphin venice (~87M/day, 1) > hermes-3-70b (~76M/day, 1) > minimax-m2-her (~57M/day, 1) > mythomax (~48M/day over 3) > hermes-3-405b (~38M/day, 1) > euryale-3.1-70b (~38M/day, 1) > unslopnemo (~23M/day, 1) > skyfall (~20M/day, 1) > magnum-v4-72b (~17M/day, 1).
- Revenue per model is small. Cydonia at ~142M tokens/day and $0.30/$0.50 is roughly $45/day (estimate); Euryale 3.1 at ~38M/day and $0.85 is roughly $32/day (estimate); Magnum v4 at ~17M/day and $2.50/$5 is roughly $43/day (estimate). The sum of the eleven dedicated roleplay fine-tunes and uncensored models listed above is about 560M tokens/day, or about 3.9B tokens/week (estimate), worth low thousands of dollars per week across all providers (estimate).
- The MythoMax split (Parasail at $0.08 takes 47.7% of 1-day tokens vs Mancer at $0.35 with 23.6%) shows OpenRouter's price-sensitive routing: a cheaper second endpoint on a single-provider model should capture share quickly.
- Zero-provider slugs (Euryale L3.3, Hermes 4 70B, Rocinante, Midnight Rose, Lumimaid, Goliath, SorcererLM, WizardLM-2, Llama 3.1 405B, R1T Chimera) are uncontested listings with existing search traffic and app integrations. Infermatic serves L3.3 Euryale v2.3, Anubis 70B, Magnum v4 72B and Rocinante off-OpenRouter, which shows the demand did not vanish; it moved to flat-rate subscriptions.

### Gaps
- Weekly token totals per niche model: OpenRouter shows daily chart buckets and unlabeled app totals, not a weekly number. The Datasets API would give exact daily totals for the top 50 only; I did not have an API key.
- Hermes 4 405B and Weaver daily activity were not captured.
- I could not read the roleplay-category token volumes (the old `/rankings/roleplay` page returns 404; the category view now lives in the authenticated Datasets API).

## Key question 2: Is the roleplay segment big enough to matter, and who dominates it?

### Takeaway
On OpenRouter, roleplay apps move tens of billions of tokens per day (Janitor AI 32.8B, SillyTavern 13.4B, ISEKAI ZERO 70.9B, Hello Minds 85.8B on Oct 21-22, 2026), but they mostly use cheap mainstream models (DeepSeek, GLM, Gemini Flash), not community fine-tunes. The money flows to flat-rate subscription providers (Infermatic $9-$20/mo, Arli AI $15-$160/mo, Featherless $25/mo, Venice $18-$200/mo, NovelAI from $10/mo) and to the big serverless hosts (DeepInfra, Parasail), not to the fine-tune authors.

### Cited Findings

OpenRouter apps leaderboard, "Today" (checked 2026-10-22, https://openrouter.ai/apps):

| Rank | App | Tokens (day) | Category tags |
|---|---|---|---|
| 1 | Claude Code | 2.11T | CLI Agents |
| 2 | Hermes Agent (Nous Research) | 2.07T | Personal Agents, CLI Agents |
| 3 | Kilo Code | 1.49T | CLI Agents, IDE Extensions |
| 4 | pi | 651B | CLI Agents |
| 5 | DeepSeek Harness | 575B | new |
| 6 | omp | 533B | CLI Agents |
| 7 | Codex | 347B | CLI Agents |
| 8 | Freebuff | 313B | ads-funded coding |
| 9 | OpenClaw | 260B | Personal Agents, CLI Agents |
| 10 | Strix | 252B | CLI Agents |
| 11 | Cline | 212B | IDE Extensions |
| 12 | Proto Agent | 202B | Personal Agents |
| 13 | ZCode | 186B | Programming App |
| 14 | Hello Minds, powered by Ethoswarm | 85.8B | Roleplay, Personal Agents, Creative Writing |
| 15 | OpenHands | 71.3B | CLI Agents |
| 16 | ISEKAI ZERO | 70.9B | Game ("AI adventures. Travel with your favorite characters") |
| 17 | HighLevel | 67.8B | not tagged |
| 18 | Aura | 65.9B | IDE Extensions |
| 19 | Cursor | 58.9B | Programming App |
| 20 | Nous Research API | 58.5B | General Chat |

"Top Entertainment" (same page, same day): Hello Minds 85.8B, ISEKAI ZERO 70.9B, Janitor AI 32.8B, Craft 19.1B, SillyTavern 13.4B. "Most Popular" (window unlabeled): Hermes Agent 53.1T, Claude Code 39.2T, Kilo Code 26T, Cline 19.9T. Roo Code and Chub did not appear in the visible top 20 or in Top Entertainment; Chub AI appears as a top app on individual model pages (Unslopnemo 41.3M, Skyfall 22.6M, Venice Uncensored 144M, DeepSeek V3 0324 3.34B).

Janitor AI's biggest visible model on OpenRouter is DeepSeek V3 0324 (24.4B tokens, window unlabeled) at $0.25/$1.00 with 2 providers. Source: https://openrouter.ai/deepseek/deepseek-chat-v3-0324 (checked 2026-10-22).

Flat-rate roleplay providers (checked 2026-10-22):

| Provider | Plans and prices | Models named | Hardware statement | API limits | On OpenRouter? | Buys outside GPU capacity / partner program | Source |
|---|---|---|---|---|---|---|---|
| Infermatic.ai | Free $0 (Rocinante-12B-v1.1 only); Essential $9/mo "Curated models up to 72B"; Standard $16/mo; Plus $20/mo (MOE, BETA, 72B+; premium credits for Qwen 3.8 Max, DeepSeek V4 Pro, Kimi K3, DeepSeek V4.1 Flash, GLM 5.3) | Essential: L3.3-70B-Euryale-v2.3, Anubis 70B v1.1, L3.3 70B Magnum v4 SE, Cydonia-24B-v4.3, 72B Qwen2.5 Kunou v1, L3.1 70B Hanami x1, Qwen3 VL 8B, Qwen3 Embedding 8B, multilingual-e5-base. Standard adds Strawberrylemonade L3 70B v1.1, Qwen3.6-35B-A3B, Prometheus 7b v2.0, Magnum-72b-v4. Plus adds Kokoro-82M, Cydonia 24B v4.3, Gemma 4 StyleTune 31B | "We host all models using the vLLM back end." GPU type not found | API parallel requests 1/1/2; 12/15/18 requests per minute; "No logging of prompts or responses. Unrestricted prompts and results." | Listed as a provider, 0 endpoints in crawl | not found | https://infermatic.ai/pricing and https://infermatic.ai/ |
| Mancer.tech | Credits per token; MythoMax 0.140/0.240 credits per token; ReMM-SLerp 0.140/0.260; Weaver Alpha 0.160/0.300; Magnum 72B v4 1.000/2.000; DansPE 24B 0.200/0.800; GLM 4.7 0.280/1.000; DeepSeek V4 Flash 0.076/0.200; GPT OSS 120B 0.020/0.100; Qwen3.8 27B 0.080/1.000; MythoLite free. Credit-to-dollar rate: not found (credit packs did not load). Refund if under 300,000 credits used | as listed | "We run LLMs on high-end machines" | "No filters / No guidelines / No constraints"; "You're an adult. Prompt responsibly." | Yes, as "Mancer 2", 9 models; MythoMax $0.35/$0.60, ReMM $0.35/$0.65, Weaver $0.40/$0.75, Magnum $2.50/$5.00 | not found | https://mancer.tech/models, https://mancer.tech/pricing, https://mancer.tech/ |
| Featherless.ai | Chat $25/mo (4 concurrent, 32K ctx); Developer $50 credits/mo (100 concurrent, up to 256K); Business custom (annual, "Sized to your GPUs", dedicated GPUs) | "All 40,000+ open models on every plan"; "Model size limit: None"; private fine-tunes "through hugging face" | "Dedicated H100 · MI325X · B200 · B300" | as above | Yes, 1 model (stepfun/step-5-preview) | not found | https://featherless.ai/pricing |
| Arli AI | Free $0 (12K ctx, 1 request); Core $15/mo (32K); Plus $20/mo (128K); Pro $30/mo (2 parallel, 256K); Max $160/mo (6 parallel, 512K); "Unlimited Tokens! Unlimited Requests!"; "Access Up to 552B Models"; "Zero-Log" | model list page was empty (JS) | not found | as above | not in crawl | not found | https://www.arliai.com/pricing |
| NovelAI (Anlatan) | "Our subscriptions start at $10/month"; on-demand Anlas; tier prices not checked | "NovelAI Diffusion V5"; story model "POWERED BY GLM 4.6" | Wikipedia: Anlatan was "one of the first CoreWeave customers to deploy NVIDIA's H100"; CoreWeave article title cites "0 to 40K Users in 3 Months" | n/a | no | not found | https://novelai.net/ and https://en.wikipedia.org/wiki/NovelAI |
| Venice.ai | Free; Pro $18/mo; Pro Plus $68/mo (7,500 credits); Max $200/mo (22,500 credits); "100 credits = $1"; DIEM token "= $1/day of compute" | API: Venice Uncensored 1.2 $0.20/$0.90; Venice Role Play Uncensored $0.50/$2.00; GLM 4.7 Flash Heretic (abliterated fine-tune) $0.07/$0.40; Llama 3.3 70B $0.70/$2.80; DeepSeek V4.1 Flash $0.30/$1.20 | "TEE (hardware-verified privacy)" | n/a | Yes, 37 models | not found | https://venice.ai/pricing and https://docs.venice.ai/overview/pricing |
| Chub.ai | subscription page not checked (login) | "uncensored"; "supports numerous APIs such as OpenAI (ChatGPT) or Anthropic (Claude)" | not found | n/a | app only (Chub AI appears as a top app on several model pages) | not found | https://docs.chub.ai/ |
| AI Horde (ex KoboldAI Horde) | free; "completely free and community-run"; "kudos can never be bought or sold"; "Workers earn kudos when their computers help process requests"; funded by donations and NLnet/NGI0 Core; run by Haidra, a volunteer non-profit | gallery credits AlbedoBase XL 3.1, Juggernaut XL, Flux.1-Schnell fp8, DreamShaper XL | volunteers' own GPUs | n/a | no | no money path for workers | https://aihorde.net/ and https://github.com/Haidra-Org/AI-Horde/blob/main/README.md |
| Chutes (Bittensor SN64) | Plus $10/mo (6% off PAYG); Pro $20/mo (10% off, "5X the value"); Enterprise; PAYG; Kimi K3 $1.85/$9.50; Qwen3.8 27B $0.04/$1.25; "runs image, video, speech, music and more" | as listed | miner README: "ALL servers must be bare metal/VM, meaning it will not work on Runpod, Vast, etc."; "GPU worker hosts must additionally be TDX-capable"; RAM per GPU must be at least VRAM (4x A40 needs 192 GB RAM); one control-plane server (4 cores, 32 GB) | n/a | Yes, 6 models | Yes: outside operators register with `btcli subnet register --netuid 64`; "Incentives are based on total compute time"; weights from "7 day sum of compute" | https://chutes.ai/ and https://github.com/rayonlabs/chutes-miner |
| Targon (Manifold Labs) | homepage now sells "On-demand NVIDIA GPUs"; Intel TDX confidential VMs; "Reserve GPUs for a fixed term"; per-token prices not found; miner onboarding not found | not found | TDX confidential VMs; bare metal "not confidential" | n/a | not in crawl | not found | https://targon.com/ |
| Parasail | serverless: Llama 3.3 70B FP8 $0.22/$0.50; Cydonia 24B v4.1 $0.30/$0.50; Skyfall 36B v2 $0.55/$0.80; Skyfall 31B v4.2 $0.55/$0.80; DeepSeek V4.1 Flash $0.30/$1.20; "Elastic endpoints" at "25% above the model's Serverless" rates; dedicated B300/B200/H200/H100 SXM/RTX PRO 6000/RTX 5090 "Hourly rates available on request" | as listed | "dedicated infrastructure without single-vendor dependency"; batch runs "on spare fleet capacity" with "spot instances" | n/a | Yes, 40 models | GPU partner program not found | https://www.parasail.io/ and https://www.parasail.io/pricing |

Front-end connectivity (checked 2026-10-22):
- SillyTavern cloud sources: AI Horde, OpenAI, Claude, Google AI Studio/Vertex, Mistral, OpenRouter, DeepSeek, AI21, Cohere, Perplexity, Mancer AI, DreamGen, Pollinations, NovelAI, Electron Hub, AI/ML API; local: KoboldCpp, llama.cpp, Ollama, Oobabooga, TabbyAPI. Source: https://docs.sillytavern.app/usage/api-connections/
- SillyTavern "Custom (OpenAI-compatible)" chat source "can connect to any server that supports the generic OpenAI API schema" (enter URL, add `/v1` if needed, key "if required"). Source: https://docs.sillytavern.app/usage/api-connections/openai/
- Agnai supported services: "Kobold, Novel, AI Horde, Goose, OpenAI, Claude, Replicate, OpenRouter, Mancer". Source: https://github.com/agnaistic/agnai
- RisuAI: "Supports OpenAI, Claude, Gemini, DeepInfra, Ooba, OpenRouter... and More!" plus plugins to "Add your features and providers". Source: https://github.com/kwaroran/RisuAI
- Janitor AI proxy ecosystem: guides describe community-shared free proxies and bring-your-own OpenRouter key; a 2026 guide warns a reverse proxy "can inspect, log, or refuse traffic". No evidence of paid key resale was found. Sources: https://aireiter.com/blog/janitor-ai-proxy-setup-guide ; https://www.tooljunction.io/blog/the-ultimate-guide-to-janitor-ai-everything-you-need-to-know-2026 ; https://teletype.in/@openai4geeks/janitor-ai-free-api-key (2023). Discord resale markets: not found.
- OpenRouter provider onboarding: "We currently have a large backlog of provider applications and are prioritizing providers with proprietary models."; "Priority is given to providers that fill gaps in our current network."; uptime 95%+ keeps standard routing, 80-94% reduced, below 80% fallback only; "Support monthly invoicing so OpenRouter can pay for inference"; `/models` endpoint must publish pricing, context, max output, features, datacenter locations; `/chat/completions` must be OpenAI-compatible, return usage tokens, support streaming; "Providers must disclose whether prompts are logged and if data is used for training." Sources: https://openrouter.ai/providers/apply and https://openrouter.ai/docs/use-cases/for-providers (checked 2026-10-22). Revenue share or fee terms: not found.

### Inferences
- Roleplay volume on OpenRouter is large in tokens but low in dollars. The five visible entertainment apps sum to about 222B tokens/day (estimate), or about 1.6T tokens/week (estimate). At a blended $0.20 to $0.30 per million (the DeepSeek/GLM Flash price band that dominates the roleplay category), that is roughly $0.3M to $0.5M per week across all providers (estimate), and much of it runs on free variants.
- Dedicated roleplay fine-tunes capture a small slice (about 3.9B tokens/week, estimate) because the big apps route to mainstream models. The fine-tune audience pays flat rates instead: Infermatic prices the whole Euryale/Anubis/Magnum catalog at $9/mo.
- Who dominates: for model supply, Parasail (TheDrummer catalog, Lunaris, MythoMax) and DeepInfra (Euryale, Hermes 3, Qwen 2.5 72B) on OpenRouter; off-OpenRouter, Infermatic, Arli AI and Featherless hold the subscription market; Venice holds the "uncensored" brand on OpenRouter with the highest-volume uncensored endpoint (about 87M tokens/day).
- Only Chutes pays outside GPU operators, and its bare-metal, TDX, static-IP requirements exclude rented cloud GPUs and home rigs.

### Gaps
- Chub, NovelAI tier prices, Arli AI model list: pages are JS or login-gated; not checked.
- Janitor AI monthly users: not found (Wikipedia page 404, searches exhausted).
- Infermatic, Arli, Mancer GPU hardware: not stated anywhere I could read.
- Hermes Agent at 2.07T tokens/day is tagged Personal Agent, not roleplay; it may still carry Hermes-model demand, which I could not separate.

## Key question 3: Concrete legal, payment-processor and reputational risks of serving uncensored models as a paid API from California

### Takeaway
Stripe's restricted-business list bans "adult live-chat features", "Pornography and other mature audience content (including literature...)", and "Any artificial-intelligence generated content that meets the above criteria". California SB 243 (effective Jan 1, 2026) gives users a private right of action for the greater of actual damages or $1,000 per violation against companion-chatbot "operators"; whether a bare API provider is an "operator" is not settled in the sources I read. Federal CSAM reporting (18 U.S.C. 2258A) carries fines up to $850,000 per violation for providers that knowingly fail to report, and the TAKE IT DOWN Act's 48-hour removal duty applied to covered platforms from May 19, 2026.

### Cited Findings

Payment processors (checked 2026-10-22):
- Stripe prohibited businesses include "Adult services, including prostitution, escorts, pay-per-view, sexual massages, fetish services, mail-order brides, and adult live-chat features"; "Pornography and other mature audience content (including literature, imagery, and other media)"; and "Any artificial-intelligence generated content that meets the above criteria". Source: https://stripe.com/legal/restricted-businesses
- 404 Media reported Stripe added "fetish services" and the AI-content line in a late-January 2024 terms update and cut off the platform Wishtender without explaining the specific case. Source: https://404media.co/stripe-cuts-off-platform-used-by-dominatrixes-wishtender (from search summary; article text not read)
- PayPal Acceptable Use Policy: the page returned only a title to the fetcher and the browser read timed out. Clause text: not checked. URL: https://www.paypal.com/us/legalhub/paypal/acceptableuse-full

California SB 243 (Business and Professions Code, Chapter 22.6, Section 22601 et seq.), checked 2026-10-22, from law-firm summaries because leginfo and LegiScan blocked the fetcher:
- Signed October 13, 2025; effective January 1, 2026. Source: https://natlawreview.com/article/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and
- Scope: companion chatbots that respond "with adaptive, human-like responses" and meet social or emotional needs; excludes bots "used solely for customer service, business operations, productivity", video-game bots whose "responses are limited to replies about the video game", and stand-alone voice assistants. Source: https://www.mondaq.com/unitedstates/new-technology/1730732/california-companion-chatbot-law-now-in-effect
- Duties: "clear and conspicuous notification to users that they are interacting with an AI system" where a reasonable person would be misled; disclosure that the chatbot "may not be suitable for some minors"; a published protocol "designed to prevent the chatbot from producing content related to suicidal ideation"; for known minors, "reasonable measures to prevent the companion chatbot from producing visual material depicting sexually explicit conduct" or directly stating that minors should engage in sexually explicit conduct, plus a break reminder "at least every three hours". Sources: mondaq and natlawreview links above.
- Remedy: injunctive relief, "damages equal to the greater of actual damages or $1,000 per violation, and reasonable attorney's fees and costs". Source: natlawreview link above.
- Reporting: annual reports to the Office of Suicide Prevention "Beginning on July 1, 2027". Source: mondaq link above.
- Whether an API or model provider (as opposed to the consumer app) is an "operator": not addressed in either summary. Statute text: not checked (leginfo returned 403).

Federal CSAM reporting, 18 U.S.C. 2258A (checked 2026-10-22, https://www.law.cornell.edu/uscode/text/18/2258A):
- A provider "shall, as soon as reasonably possible after obtaining actual knowledge of any facts or circumstances" of apparent violations, report to NCMEC's CyberTipline (2258A(a)(1)).
- "provider" means "an electronic communication service provider or remote computing service" (18 U.S.C. 2258E(6), https://www.law.cornell.edu/uscode/text/18/2258E).
- Penalties for a provider that "knowingly and willfully" fails to report: up to $600,000 (initial) and $850,000 (subsequent) for providers under 100,000,000 monthly active users; $850,000 and $1,000,000 for larger providers (2258A(e), as raised by the REPORT Act, Pub. L. 118-59, May 7, 2024).
- Reports must be preserved for 1 year (was 90 days before the REPORT Act), in a secure location, consistent with the NIST Cybersecurity Framework (2258A(h)).
- Generative-AI CSAM: the statute page does not mention generative AI; not found there.

TAKE IT DOWN Act, Pub. L. 119-12 (signed May 19, 2025), checked 2026-10-22, https://www.govinfo.gov/content/pkg/PLAW-119publ12/html/PLAW-119publ12.htm and https://en.wikipedia.org/wiki/TAKE_IT_DOWN_Act:
- "covered platform" means a website, online service, online application, or mobile application that "serves the public" and "primarily provides a forum for user-generated content" or for which such content is "in the regular course of trade or business" (Sec. 4(3)(A)); excludes "A provider of broadband internet access service", "Electronic mail", and services that consist "primarily of content that is not user generated but is preselected by the provider" (Sec. 4(3)(B)).
- "digital forgery" means "any intimate visual depiction of an identifiable individual created through the use of software" that is "indistinguishable from an authentic visual depiction" (Sec. 2).
- Removal "not later than 48 hours after receiving such request" (Sec. 3(a)(3)); process required "Not later than 1 year after the date of enactment" (Sec. 3(a)(1)(A)), i.e. May 19, 2026; FTC enforces.

Section 230 and product liability (checked 2026-10-22):
- Garcia v. Character Technologies (M.D. Fla.): on May 21, 2025 Judge Anne C. Conway ruled that "chatbot outputs do not reflect the human intent necessary to constitute 'speech' for First Amendment purposes" and let strict liability, negligence and wrongful-death counts proceed, treating the app as a product. Sources: https://techjusticelaw.org/cases/garcia-v-character-technologies-google-and-character-ai-co-founders-daniel-de-frietas-and-noam-shazeer/ and https://www.awkolaw.com/when-the-chatbot-becomes-the-defendant/
- Character.AI and Google settled Garcia and four related suits in January 2026, "committing to new safety features for minors". Source: https://www.awkolaw.com/when-the-chatbot-becomes-the-defendant/
- Section 230 holding: neither page addresses Section 230. One secondary blog (search summary) claimed the court did not treat Section 230 as a bar because the harm came from model output, not user content; this is not verified against the opinion. Not checked.

State chatbot and age-verification laws (checked 2026-10-22):
- AVPA tracker (information "believed to be correct as of (August 2026)") lists enacted companion/chatbot laws in California (SB 243, Jan 1, 2026), New York (S-3008C, Nov 5, 2025), Utah (HB 452), Washington (HB 2225, effective Jan 2027), Oregon (SB 1546), Hawaii, Colorado (HB 1263, effective Aug 12, 2026), Connecticut (SB 5, PA 26-15), Georgia (SB 540), Iowa (SF 2417, applies July 2027), Nebraska (LB 525), Rhode Island (SB 2195, Jan 1, 2027), New Hampshire (HB 143), with Idaho S 1297 starting 7/1/27. Requirements per state were not legible on the page. Source: https://avpassociation.com/state-laws-for-ai-chatbots
- Search summary (not independently verified): no state yet requires upfront age verification for general chatbot use; 29 states have adult-content age-verification laws in force (gadgetreview tracker updated Sept 28, 2026); Free Speech Coalition v. Paxton (2025) upheld intermediate scrutiny for adult-site laws. Sources: https://www.gadgetreview.com/?p=416283 ; https://www.eff.org/deeplinks/2025/12/year-states-chose-surveillance-over-safety-2025-review . Not checked against statute text.

Reputational signal from live traffic (checked 2026-10-22): the top apps on the uncensored and roleplay endpoints include "HotLive" (444M), "ChamadaVIP" (823M), "Hornyt" (1.3B), "HornyDreams Prompt Improver" (96.2M), "fanvue-bot" (117M), "WildGirl" (82.8M), "WaifuBot" (17.7M), "NoFilterGPT" (37M). Sources: the OpenRouter model pages for Venice Uncensored, Lunaris 8B, Hermes 3 70B, MiniMax M2-her, ReMM SLERP.

### Inferences
- A provider that sells uncensored text inference through Stripe is exposed on three list items at once (adult live-chat, mature-content literature, AI-generated content meeting those criteria). Mancer and Chub avoid naming their processor; Venice sells credits and a crypto staking path (DIEM); Chutes pays miners in TAO. This pattern suggests card-processor access is the operational bottleneck, not the law.
- SB 243 targets "operators" that make the chatbot available to users. A pure API seller is more likely a supplier than an operator, but the statute text was not read, and the $1,000-per-violation private right of action makes this worth a legal opinion before launch.
- The CSAM duty attaches to "remote computing service" providers, which an inference API plausibly is; the actual-knowledge trigger means logging and abuse-flagging choices directly affect exposure. The TAKE IT DOWN Act's covered-platform definition excludes services whose content is provider-preselected, so a bare text API is less likely covered than an image or chat app.

### Gaps
- PayPal AUP clause text: not checked.
- SB 243 statutory definitions of "operator" and "companion chatbot": not read from the statute.
- Section 230 treatment in Garcia: not verified.
- Civitai's 2025 payment-processor cutoff over AI adult content: not verified (Wikipedia page did not cover it; searches exhausted).
- Per-state requirements for the 13 listed chatbot laws: not read.

## Key question 4: Are there modalities (image, speech, OCR, embeddings) where supply is thin and a small provider could win? Which marketplaces let an outside provider plug in and get paid?

### Takeaway
OpenRouter now routes embeddings (39 models), reranking (10), transcription (Whisper, Parakeet, Deepgram, ElevenLabs), TTS (Kokoro), image (61) and video (30), but observed image and video endpoints are first-party labs only, while embeddings, Whisper and Kokoro have 1 to 3 third-party providers each. Hugging Face Inference Providers is the only general marketplace that documents how an outside provider registers, bills (nano-USD billing API, "no additional markup") and maps LoRAs; fal, Replicate and Runware run their own hardware and publish no provider program. Price floors are low: embeddings $0.005 to $0.01 per 1M tokens, Whisper $0.45 to $1.85 per 1,000 minutes, Kokoro $0.62 to $0.99 per 1M characters, FLUX schnell about $0.003 per image.

### Cited Findings

Marketplaces an outside provider can plug into (checked 2026-10-22):

| Marketplace | Outside providers can list? | How they get paid | Requirements and quotes | Source |
|---|---|---|---|---|
| OpenRouter | Yes, by application (text, embeddings, transcription, TTS observed from third parties; image and video endpoints observed only from the model's own lab) | Monthly invoicing; providers set per-token USD prices; no fee or revenue-share terms published | "large backlog of provider applications and are prioritizing providers with proprietary models"; 95%+ uptime for standard routing; OpenAI-compatible, streaming, usage tokens, `/models` with pricing and datacenter locations | https://openrouter.ai/providers/apply ; https://openrouter.ai/docs/use-cases/for-providers |
| Hugging Face Inference Providers | Yes | HF bills the user "the same rates as the provider, with no additional fees"; provider exposes a billing API returning cost per request in nano-USD, polled every minute, unbilled after ~30 minutes is not charged | Needs a Team or Enterprise org plan; implement task API schemas; PRs to huggingface.js and huggingface_hub; Model Mapping API (`POST /api/partners/{provider}/models`), including LoRA tag-filter mapping (e.g. all `lora` + `base_model:adapter:black-forest-labs/FLUX.1-dev` models to one endpoint); automatic tests every 6 hours; TTFT under 5 s for LLMs, under 30 s for other tasks; providers ranked by routed requests over 7 days | https://huggingface.co/docs/inference-providers/en/register-as-a-provider ; https://huggingface.co/docs/inference-providers/en/pricing |
| Chutes (Bittensor SN64) | Yes, as miners | TAO emissions by "total compute time" | bare metal or VM only, TDX-capable GPU hosts, static 1:1 IPs, RAM >= VRAM per GPU | https://github.com/rayonlabs/chutes-miner |
| fal.ai | No program found | n/a | "Deploy your own app on our competitively priced GPU fleet"; H100 $4.50/h list, "As low as" $2.49/h | https://fal.ai/pricing |
| Replicate | No program found; "Thousands of open-source machine learning models have been contributed by our community" but no creator payout stated | n/a | public models billed by active time only; private models billed for all online time | https://replicate.com/pricing ; https://replicate.com/docs/topics/billing |
| Runware | No provider program; "Creator Program" is for content creators (credits plus cash bonuses, 2,000+ followers) | n/a | serverless L40S $1.60/h, H100 $0.001097/s, H200 $0.00125/s, B200 $0.001667/s, B300 $0.001944/s | https://runware.ai/pricing ; https://runware.ai/creator-program |
| AI Horde | Yes, as volunteer workers | none ("kudos can never be bought or sold") | n/a | https://github.com/Haidra-Org/AI-Horde/blob/main/README.md |
| Civitai | not checked (pricing page returned 403; Buzz guide 404) | not checked | Wikipedia: Buzz "can be bought or earned"; a16z funding Nov 2023; OctoML ended its relationship Dec 2023 over generated images | https://en.wikipedia.org/wiki/Civitai |

Image generation prices (checked 2026-10-22):

| Model | Provider | Price | Source |
|---|---|---|---|
| FLUX.1 schnell | fal | $0.003 per megapixel | https://fal.ai/pricing |
| FLUX.1 dev / dev with LoRAs | fal | $0.025 / $0.035 per megapixel | https://fal.ai/pricing |
| FLUX Schnell / Dev / 1.1 Pro | Replicate | $3.00 per 1,000 images / $0.025 per image / $0.04 per image | https://replicate.com/pricing |
| FLUX-1-schnell | DeepInfra | $0.0005 x (w/1024) x (h/1024) x iterations per image | https://deepinfra.com/pricing |
| FLUX-1-dev / FLUX-2-dev / FLUX-1.1-pro | DeepInfra | $0.009 x area x (iters/25) / $0.01 x area x (iters/28) / $0.04 per image | https://deepinfra.com/pricing |
| FLUX 3 Image Klein 512x512 16 steps / Klein Base 50 steps / FLUX 3 Image 0.75K | Runware | $0.003 / $0.0089 / $0.041 per image | https://runware.ai/pricing |
| FLUX.2 dev / pro / flex / max; FLUX.1 Kontext pro / max | Together | $0.0154 / $0.03 / $0.03 per image; $0.070 per MP; $0.04 / $0.08 per MP | https://www.together.ai/pricing |
| Lustify SDXL, Anime (WAI Illustrious), Chroma, Venice SD35 | Venice | $0.01 per image each | https://docs.venice.ai/overview/pricing |
| Flux 2 Pro / Max; Qwen Image / 2 / 3; Hunyuan Image 3.0 | Venice | $0.03 / $0.09; $0.03 / $0.05 / $0.04; $0.09 per image | https://docs.venice.ai/overview/pricing |
| OpenRouter image models | 61 listed; endpoints checked for qwen/qwen-image-3 (Alibaba only), black-forest-labs/flux-3-image and flux-3-image-klein (BFL only), tencent/hy-image-v3.5-preview (Tencent only); billed per image token (e.g. flux-3-image-klein $0.0000019 per image token; gpt-image-2 $0.00003; gemini-3.1-flash-image $0.00006) | https://openrouter.ai/api/v1/models?output_modalities=image |
| Civitai | not checked | not checked | n/a |

Video prices (checked 2026-10-22):

| Model | Provider | Price | Source |
|---|---|---|---|
| Wan 2.2 A14B text-to-video | fal | $0.08 per second at 720p, $0.06 at 580p, $0.04 at 480p (16 fps) | https://fal.ai/models/fal-ai/wan/v2.2-a14b/text-to-video |
| Wan 2.5 | fal | about $0.05 per second (third-party listings; fal page not read) | https://www.costbench.com/software/ai-media-apis/fal-ai/ (not checked against fal) |
| HunyuanVideo | fal | $0.40 per video (5 s typical, 720p default); pro mode 2x | https://fal.ai/models/fal-ai/hunyuan-video |
| LTX-2 text-to-video | fal | $0.06 per second 1080p, $0.12 1440p, $0.24 2160p; 6 to 10 s clips | https://fal.ai/models/fal-ai/ltx-2/text-to-video |
| Wan 2.1 I2V 480p / 720p | Replicate | $0.09 / $0.25 per second of output | https://replicate.com/pricing |
| Wan3.0 480p / Wan3.0 Prime 480p / Kling 4.0 720p | Runware | $0.05 / $0.068 / $0.157 per second | https://runware.ai/pricing |
| Kling 1.6 Standard / Kling 2.1 Pro | Together | $0.19 / $0.32 per video | https://www.together.ai/pricing |
| LTX-2.3 Fast / LTX-2.3 Pro / LTX-2.5 Fast / LTX-2.5 Pro / MiniMax H3 768p (open weights, creator API, 1 minute 1080p) | Artificial Analysis | $3.60 / $4.80 / $7.80 / $10.20 / $4.80 per minute | https://artificialanalysis.ai/video/leaderboard/text-to-video/open-weights |
| Mochi | not found on any page read | not found | n/a |
| OpenRouter video | 30 models (alibaba/wan-3.0, wan-2.7, wan-2.6, kling v3, veo 3.1, seedance 2.x, hailuo 3, runway gen-4.5, grok imagine, heygen, flux-video); list shows no per-second price ("Variable") | https://openrouter.ai/api/v1/models?output_modalities=video |

Speech-to-text prices, USD per 1,000 minutes unless noted (checked 2026-10-22):

| Model | Provider | Price | Source |
|---|---|---|---|
| Whisper Large v3 Turbo | Groq | 0.67 | https://artificialanalysis.ai/speech-to-text |
| Wizper Large v3 / Whisper Large v3 | fal | 0.50 / 1.15 | same |
| Whisper Large v3 | Together | 1.50 (Together's own page: $0.0015 per minute, $0.0035 streaming) | same; https://www.together.ai/pricing |
| Whisper Large v3 / Incredibly Fast Whisper | Replicate | 4.23 / 1.49 | artificialanalysis |
| Parakeet TDT 0.6B v3 | Together | 1.50 | artificialanalysis |
| Parakeet RNNT 1.1B / Canary Qwen 2.5B | Replicate | 1.91 / 0.74 | artificialanalysis |
| Voxtral Mini | DeepInfra | 1.00 ($0.001 per minute); Nemotron 3.5 ASR streaming $0.0002 per minute | https://deepinfra.com/pricing |
| Deepgram Nova-3 / AssemblyAI Universal / OpenAI GPT-4o Transcribe / ElevenLabs Scribe v2 | each | 4.30 / 2.50 / 6.00 / 3.67 | artificialanalysis |
| Whisper Large V3 and Parakeet ASR | Venice | $0.0001 per audio second ($6.00 per 1,000 minutes, estimate) | https://docs.venice.ai/overview/pricing |
| openai/whisper-large-v3 on OpenRouter | DeepInfra $0.0000075, Together $0.000025, Groq $0.0000308 per unit; Deepgram Nova-3 $0.0000717 per unit (matches $4.30 per 1,000 minutes if the unit is one audio second, estimate) | 3 providers for Whisper, 1 for Parakeet (Together $0.000025) | https://openrouter.ai/api/v1/models/openai/whisper-large-v3/endpoints |

Text-to-speech prices, USD per 1M characters (checked 2026-10-22):

| Model | Provider | Price | Source |
|---|---|---|---|
| Kokoro 82M | DeepInfra | $0.99 (model page); OpenRouter endpoint shows DeepInfra $0.62 and Together $4.00 (unit inferred as per 1M characters) | https://deepinfra.com/hexgrad/Kokoro-82M ; https://openrouter.ai/api/v1/models/hexgrad/kokoro-82m/endpoints |
| Kokoro | Replicate | $0.65 | https://artificialanalysis.ai/text-to-speech |
| Kokoro / Chatterbox | fal | $20 / $25 ($0.02 and $0.025 per 1,000 characters) | https://fal.ai/pricing |
| Kokoro / Chatterbox HD / Orpheus / Qwen 3 TTS 0.6B / Inworld TTS-1.5 Max | Venice | $3.50 / $50.00 / $62.50 / $87.50 / $12.50 | https://docs.venice.ai/overview/pricing |
| Cartesia Sonic-3 | Together | $65.00 | https://www.together.ai/pricing |
| Orpheus, Chatterbox on OpenRouter | not listed (404 for canopylabs/orpheus-3b and resemble-ai/chatterbox) | n/a | endpoints API |

Embeddings and rerankers (checked 2026-10-22):

| Model | Provider(s) | Price per 1M tokens | Source |
|---|---|---|---|
| bge-base-en-v1.5 / bge-large / bge-m3 / bge-en-icl | DeepInfra | $0.005 / $0.01 / $0.01 / $0.01 | https://deepinfra.com/pricing |
| baai/bge-m3 | OpenRouter: Parasail, DeepInfra | $0.01 | https://openrouter.ai/api/v1/models/baai/bge-m3/endpoints |
| qwen/qwen3-embedding-8b | OpenRouter: Nebius $0.01, DeepInfra $0.01, SiliconFlow $0.04 | min $0.01 | https://openrouter.ai/api/v1/models/qwen/qwen3-embedding-8b/endpoints |
| gte-base, e5-base-v2, all-minilm, mpnet / gte-large, e5-large-v2, multilingual-e5-large | OpenRouter | $0.005 / $0.01 | https://openrouter.ai/api/v1/models?output_modalities=embeddings (39 models) |
| voyage-4-lite / voyage-4 / voyage-4-large; gemini-embedding-2; text-embedding-3-small / large | OpenRouter | $0.02 / $0.06 / $0.12; $0.20; $0.02 / $0.13 | same |
| Embeddings up to 150M params / 150M to 350M / Qwen3 8B | Fireworks | $0.008 / $0.016 / $0.10 | https://fireworks.ai/pricing |
| Qwen3 Embedding 0.6B and 8B / BGE-M3 | Venice | $0.0125 / $0.15 in, $0.60 out | https://docs.venice.ai/overview/pricing |
| Jina embeddings v5 / v4 / reranker v3 | Jina | token packs via Stripe, prices not shown; jina-embeddings-v4 is under the Qwen Research License ("research and non-commercial use only"); CC BY-NC models "need a commercial license" | https://jina.ai/embeddings/ |
| Rerankers | OpenRouter: 10 models (qwen/qwen3-reranker-8b via Fireworks, voyage rerank-3, cohere rerank-4, nvidia nemotron rerank free); Together lists "No matching models" for embeddings and rerank | qwen3-reranker-8b shows $0 (price not set) | https://openrouter.ai/api/v1/models?output_modalities=rerank ; https://www.together.ai/pricing |
| Trending | bge-m3 appeared in OpenRouter's "New and trending" with 1.03M tokens this week | tiny volume | https://openrouter.ai/rankings |

OCR and vision (checked 2026-10-22):

| Model | Provider(s) | Price | Source |
|---|---|---|---|
| Qwen3-VL-30B-A3B-Instruct / Nemotron 3.5 Super VL | DeepInfra | $0.15 / $0.60; $0.15 / $0.50 per 1M tokens | https://deepinfra.com/pricing |
| qwen/qwen3-vl-8b-instruct | OpenRouter: Parasail only | $0.25 / $0.75 | endpoints API |
| qwen/qwen3-vl-235b-a22b-instruct | OpenRouter: DeepInfra $0.20/$0.88 (30-day uptime 3.3%, status -5), Venice $0.21/$1.90 (93%), Parasail $0.21/$1.90 | min $0.20 / $0.88 | endpoints API |
| qwen/qwen2.5-vl-72b-instruct | OpenRouter: Parasail only | $0.80 / $1.00 | endpoints API |
| DeepSeek-OCR | not on OpenRouter (404); third-party listings: Novita $0.03 in and out per 1M tokens, Clarifai $0.20 / $0.70, Vertex AI $0.0003 per page (aggregator pages, not checked against providers) | see left | https://custom.typingmind.com/tools/estimate-llm-usage-costs/novita-ai/deepseek-ocr ; https://www.getmaxim.ai/bifrost/llm-cost-calculator/provider/vertex_ai/model/deepseek-ocr-maas |
| olmOCR-2-7B-1025-FP8 | self-host | "less than $200 USD per million pages converted"; Apache 2.0; tested on RTX 4090, L40S, A100, H100 | https://github.com/allenai/olmocr |
| dots.ocr | not found | not found | n/a |

Music (checked 2026-10-22):
- fal ACE-Step: "$0.0002 per second of generated audio" (about $0.012 per minute, estimate), "Commercial use" tag. Source: https://fal.ai/models/fal-ai/ace-step
- fal YuE page: no price shown. Source: https://fal.ai/models/fal-ai/yue
- EmpirioLabs ACE-Step 1.5 XL about $0.00025 per second; Sogni 30-second track about $0.024 (search summaries, not checked). Sources: https://empiriolabs.ai/models/ace-step-1.5-xl ; https://www.sogni.ai/models/ace-step-1-5-sft
- OpenRouter audio-output models: google/lyria-3-pro-preview and lyria-3-clip-preview (price 0, preview), openai/gpt-audio ($0.000032 per audio input unit, $0.000064 output), gpt-audio-mini. Source: https://openrouter.ai/api/v1/models?output_modalities=audio

### Inferences
- Thin-supply spots with a published buyer: Whisper Large v3 (3 OpenRouter providers, DeepInfra at $0.45 per 1,000 minutes sets the floor); Parakeet TDT 0.6B v3 (Together only); Kokoro (2 providers, $0.62 to $4.00 per 1M characters, while fal charges $20 and Venice $3.50, so a $1 to $2 price undercuts most of the market); Orpheus and Chatterbox (absent from OpenRouter; Venice charges $50 to $62.50 per 1M characters); bge-m3 and Qwen3-Embedding-8B (2 to 3 providers at $0.01); Qwen3-VL-8B and Qwen2.5-VL-72B (Parasail only); Qwen3-VL-235B (DeepInfra endpoint at 3.3% uptime, so a reliable third source would win routing).
- Image and video on OpenRouter are first-party only today, and fal, Replicate and Runware do not take outside providers. The only documented open door for image and LoRA serving is Hugging Face Inference Providers, which explicitly supports mapping all FLUX.1-dev LoRAs to one endpoint and takes no margin.
- Unit economics favor audio and embeddings for small GPUs: an L40S at $1.60 to $1.95 per hour (Runware, Modal) can serve Kokoro or Whisper far below the $0.45 per 1,000 minutes floor only at high utilization, so pricing power is thin; the win is listing presence and uptime, not price.

### Gaps
- Per-image prices for SDXL fine-tunes and Pony on fal, Replicate, Runware: not shown on their pricing pages.
- Civitai generation pricing and creator payouts: not checked (403 and 404).
- Whisper price on DeepInfra's own pricing page: not listed there (only Voxtral and Nemotron).
- OpenRouter unit for transcription and TTS pricing fields: inferred (audio seconds, characters), not documented on the pages I read.
- dots.ocr pricing: not found.

## Key question 5: Custom and fine-tuned models as a product (LoRA serving, serve-any-HF-model, dedicated endpoints) and what the market pays for dedicated capacity

### Takeaway
Together has discontinued serverless LoRA and multi-LoRA inference and now serves adapters only on dedicated endpoints; Fireworks serves fine-tunes "for the same price as base models"; vLLM supports runtime adapter loading behind a flag it labels a security risk. Dedicated H100 capacity sells for $2.90 (DeepInfra) to $8.00 (Fireworks) per GPU-hour, with Baseten at $6.50, Replicate and Together at $5.49, HF at $4.50, Modal and Runware at about $3.95.

### Cited Findings

Dedicated GPU prices per GPU-hour (checked 2026-10-22):

| Vendor | H100 | H200 | B200 | A100 80GB | L40S | Other | Source |
|---|---|---|---|---|---|---|---|
| DeepInfra (custom LLM deployments, minute granularity) | $2.90 | $3.49 | $4.89 | $1.49 | not listed | B300 $5.89 | https://deepinfra.com/pricing |
| Together Dedicated Inference | $5.49 | contact | $8.99 | not listed | not listed | GPU clusters: H100 $3.99, H200 $5.99, B200 $8.19, B300 $9.99; reserved H100 $3.69 (3-30 days) to $3.19 (91-180 days) | https://www.together.ai/pricing |
| Fireworks on-demand | $8.00 | $8.00 | $13.00 | not listed | not listed | B300 $15.00, GB300 $20.00; "Region-restricted deployments are priced at a 1.5x premium" | https://fireworks.ai/pricing |
| Baseten (per minute, hourly is my conversion) | $0.10833/min ($6.50) | not listed | $0.16633/min ($9.98) | $0.06667/min ($4.00) | not listed | H100 MIG 40GB $0.0625/min ($3.75); A10G $0.02012/min ($1.21); L4 $0.01414/min ($0.85); T4 $0.01052/min ($0.63) | https://www.baseten.co/pricing |
| Hugging Face Inference Endpoints (AWS) | $4.50 | $5.00 | not listed | $2.50 | $1.80 | L4 $0.80; T4 $0.50 | https://huggingface.co/pricing |
| fal GPU | $4.50 list; "As low as" $2.49 | not listed | not listed | not listed | not listed | billed per second | https://fal.ai/pricing |
| Replicate | $5.49 | not listed | not listed | $5.04 | $3.51 | T4 $0.81 | https://replicate.com/pricing |
| Runware serverless | $0.001097/s ($3.95) | $0.00125/s ($4.50) | $0.001667/s ($6.00) | not listed | $1.60 | RTX PRO 6000 $0.000553/s; B300 $0.001944/s ($7.00) | https://runware.ai/pricing |
| Modal | $0.001097/s ($3.95) | $0.001261/s ($4.54) | $0.001736/s ($6.25) | $0.000694/s ($2.50) | $0.000542/s ($1.95) | A100 40GB $0.000583/s; A10 $0.000306/s; L4 $0.000222/s; T4 $0.000164/s | https://modal.com/pricing |
| Parasail dedicated | "Hourly rates available on request" | same | same | not listed | not listed | RTX PRO 6000 and RTX 5090 also offered | https://www.parasail.io/pricing |

LoRA and fine-tune serving (checked 2026-10-22):
- vLLM: `--enable-lora` with `--lora-modules`; `--max-lora-rank` "controls the maximum rank allowed for LoRA adapters"; runtime loading via `POST /v1/load_lora_adapter` when `VLLM_ALLOW_RUNTIME_LORA_UPDATING` is `True`, which the docs say "comes with security risks". Source: https://docs.vllm.ai/en/latest/features/lora.html
- Together: "Serverless LoRA inference (including Serverless Multi-LoRA) has been discontinued."; adapters are "served on dedicated endpoints, not through the per-token serverless API"; several adapters can be attached "to a single LoRA-enabled dedicated endpoint". Source: https://docs.together.ai/docs/lora-inference
- Fireworks: "Serve fine-tuned models for the same price as base models." Source: https://fireworks.ai/pricing
- Featherless: Developer plan includes private fine-tunes "through hugging face"; Business plan is "Sized to your GPUs" with dedicated GPUs; catalog claim "All 40,000+ open models on every plan"; hardware "Dedicated H100 · MI325X · B200 · B300". Source: https://featherless.ai/pricing
- Hugging Face Inference Providers supports a tag-filter mapping so "any model tagged with both `lora` and `base_model:adapter:black-forest-labs/FLUX.1-dev` can be mapped to your Flux-dev LoRA inference endpoint"; only `adapterType: "lora"` is supported. Source: https://huggingface.co/docs/inference-providers/en/register-as-a-provider
- Parasail "Elastic endpoints give eligible models dedicated GPU performance, billed per token" at "25% above the model's Serverless input and output token rates". Source: https://www.parasail.io/

### Inferences
- The reference price a small company pays for a dedicated H100 endpoint is $2.90 to $8.00 per hour; a provider must beat DeepInfra's $2.90 or offer something DeepInfra does not (multi-LoRA, uncensored, custom quant, private VPC).
- Together's exit from serverless multi-LoRA removes the cheapest way for small fine-tune authors to be served per token, which leaves a gap for a vLLM multi-LoRA host that bills per token on shared GPUs.
- Featherless's "40,000+ models" positioning and Infermatic's flat $9 to $20 tiers show the market pays for breadth and flat rates, not per-token price, for community models.

### Gaps
- Fireworks and Baseten multi-LoRA limits and prices: not stated on their pricing pages.
- Featherless and Infermatic actual GPU counts and utilization: not found.
- What small companies pay for dedicated endpoints at Infermatic or Parasail: quotes only.

## Top openings and risk flags

### Takeaway
The clearest openings are second-sourcing single-provider roleplay fine-tunes on OpenRouter (Cydonia, Euryale 3.1, Hermes 3 70B/405B, Magnum v4) and listing the zero-provider slugs (Euryale L3.3, Hermes 4 70B, Rocinante, Midnight Rose, Lumimaid, WizardLM-2, Llama 3.1 405B), followed by thin-supply audio and embedding endpoints (Whisper, Parakeet, Kokoro, Orpheus, bge-m3, Qwen3-Embedding) and a Hugging Face Inference Providers listing for LoRA serving. The dollar value per model is small, so the play is breadth and uptime, with payment-processor and California companion-chatbot exposure as the main risks.

### Cited Findings

Top openings, ranked (all data checked 2026-10-22; "est." = my arithmetic on the cited daily buckets and list prices):

| Rank | Opening | Evidence | Current providers and price | Rough daily revenue at current prices (est.) | Hardware class (est.) | Source |
|---|---|---|---|---|---|---|
| 1 | Second-source thedrummer/cydonia-24b-v4.1 | ~142M tokens/day; top apps StoryNexus 486M, SillyTavern 193M, Janitor AI 143M | Parasail only, $0.30/$0.50 | about $45/day for the whole model | 1x 48GB or 80GB GPU | https://openrouter.ai/thedrummer/cydonia-24b-v4.1 |
| 2 | List the zero-provider roleplay slugs: sao10k/l3.3-euryale-70b, nousresearch/hermes-4-70b, thedrummer/rocinante-12b, sophosympatheia/midnight-rose-70b, neversleep lumimaid 70B/8B, microsoft/wizardlm-2-8x22b, meta-llama/llama-3.1-405b (base and instruct), alpindale/goliath-120b, raifle/sorcererlm-8x22b | listed on OpenRouter with 0 endpoints; Infermatic sells Euryale v2.3, Anubis, Rocinante and Magnum off-platform at $9/mo | none | not measurable until listed | 12B on one 24GB GPU; 70B on 2x 80GB (fp8 on 1x 80GB) | endpoints API; https://infermatic.ai/pricing |
| 3 | Second-source DeepInfra's single-provider roleplay 70Bs: sao10k/l3.1-euryale-70b (~38M/day, $0.85/$0.85), nousresearch/hermes-3-llama-3.1-70b (~76M/day, $0.70/$0.70) | DeepInfra only; price-sensitive routing shown by MythoMax split (Parasail 47.7% share at $0.08) | DeepInfra | about $32/day and $53/day | 1x 80GB fp8 or 2x 48GB | model pages above |
| 4 | Undercut Mancer on anthracite-org/magnum-v4-72b | ~17M/day at $2.50/$5.00; apps SillyTavern 132M, Candace 131M, AI Companion 130M | Mancer 2 only | about $43/day; a $0.80/$1.00 listing would take routing share | 1x 80GB fp8 | https://openrouter.ai/anthracite-org/magnum-v4-72b |
| 5 | Third-source deepseek/deepseek-chat-v3-0324 (legacy, Janitor AI's main model) | ~1.5B tokens/day; Janitor AI 24.4B, Chub 3.34B, SillyTavern 2.54B | SiliconFlow $0.25/$1.00, GMICloud $0.29/$1.14 | about $450/day for the whole model (blended $0.30/M, est.) | 8x 80GB (671B MoE fp8), capital heavy | https://openrouter.ai/deepseek/deepseek-chat-v3-0324 |
| 6 | Hermes 3 405B and Hermes 4 405B second source | ~38M/day (H3 405B); H4 405B apps SillyTavern 185M | DeepInfra $1/$1; Nebius $1/$3 | about $38/day (H3) | 8x 80GB fp8 | model pages |
| 7 | Transcription: Whisper Large v3 and Parakeet TDT 0.6B v3 on OpenRouter | Whisper 3 providers ($0.45 to $1.85 per 1,000 min); Parakeet Together only ($1.50 per 1,000 min) | DeepInfra, Together, Groq | volume not published | L4 or L40S | endpoints API; https://artificialanalysis.ai/speech-to-text |
| 8 | TTS: Kokoro (2 providers), Orpheus and Chatterbox (none on OpenRouter) | Kokoro $0.62 to $4.00 per 1M chars on OpenRouter vs fal $20, Venice $3.50; Orpheus $62.50 and Chatterbox HD $50 at Venice | DeepInfra, Together | volume not published | L4 or L40S | endpoints API; https://docs.venice.ai/overview/pricing ; https://fal.ai/pricing |
| 9 | Embeddings and rerank: baai/bge-m3, qwen/qwen3-embedding-8b, qwen3-reranker-8b | 2 to 3 providers at $0.01 per 1M; reranker single provider with no price | Parasail, DeepInfra, Nebius, SiliconFlow, Fireworks | tiny (bge-m3 1.03M tokens this week in trending) | any 24GB GPU | endpoints API; https://openrouter.ai/rankings |
| 10 | Vision: qwen/qwen3-vl-8b-instruct and qwen2.5-vl-72b (Parasail only); qwen3-vl-235b (DeepInfra endpoint at 3.3% uptime) | single or unreliable providers | Parasail $0.25/$0.75; $0.80/$1.00 | not published | 1x 24GB (8B); 2x 80GB (72B) | endpoints API |
| 11 | Register on Hugging Face Inference Providers as a LoRA and long-tail host | "no additional markup"; LoRA tag-filter mapping; Together dropped serverless multi-LoRA | n/a | n/a | vLLM multi-LoRA on shared GPUs | https://huggingface.co/docs/inference-providers/en/register-as-a-provider ; https://docs.together.ai/docs/lora-inference |
| 12 | Dedicated endpoints for small companies below DeepInfra's $2.90 H100-hour, or with multi-LoRA | market range $2.90 to $8.00 per H100-hour | DeepInfra, Together, Fireworks, Baseten | n/a | H100 or H200 | pricing pages above |
| 13 | Chutes miner (Bittensor SN64) for image, video, speech, music chutes | only marketplace paying outside GPU operators | n/a | paid in TAO by compute time | bare-metal TDX hosts with static IPs | https://github.com/rayonlabs/chutes-miner |

Risk flags (checked 2026-10-22):

| Risk | What the source says | Who it hits | Severity (my view) | Source |
|---|---|---|---|---|
| Stripe account loss | Prohibits "adult live-chat features", "Pornography and other mature audience content (including literature...)", and "Any artificial-intelligence generated content that meets the above criteria" | any uncensored text or image API billed through Stripe | high | https://stripe.com/legal/restricted-businesses |
| PayPal AUP | clause not checked (page did not render) | same | unknown | https://www.paypal.com/us/legalhub/paypal/acceptableuse-full |
| California SB 243 private right of action | greater of actual damages or $1,000 per violation plus attorney's fees; disclosure, suicide protocol, minor protections, reporting from July 1, 2027 | "operators" of companion chatbots; API-provider status not addressed | high for consumer apps, unclear for API | https://natlawreview.com/article/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and ; https://www.mondaq.com/unitedstates/new-technology/1730732/california-companion-chatbot-law-now-in-effect |
| 18 U.S.C. 2258A CSAM reporting | report "as soon as reasonably possible after obtaining actual knowledge"; fines up to $600,000 / $850,000 for knowing and willful failure (under 100M MAU); 1-year preservation | "remote computing service" providers, which plausibly includes inference APIs | high | https://www.law.cornell.edu/uscode/text/18/2258A ; https://www.law.cornell.edu/uscode/text/18/2258E |
| TAKE IT DOWN Act | 48-hour removal duty, process required by May 19, 2026, FTC enforcement; excludes provider-preselected content services, ISPs, email | covered platforms with user-generated content (image and chat apps more than bare APIs) | medium | https://www.govinfo.gov/content/pkg/PLAW-119publ12/html/PLAW-119publ12.htm |
| Product liability without First Amendment shield | Garcia (M.D. Fla., May 21, 2025): chatbot output not "speech"; strict liability and negligence counts survived; settled Jan 2026 with minor-safety commitments; Section 230 treatment not verified | chatbot operators; suppliers possibly as "component part" makers (Google was kept in on that theory per search summary) | medium | https://techjusticelaw.org/cases/garcia-v-character-technologies-google-and-character-ai-co-founders-daniel-de-frietas-and-noam-shazeer/ ; https://www.awkolaw.com/when-the-chatbot-becomes-the-defendant/ |
| State chatbot laws | 13 states with enacted companion or chatbot laws as of Aug 2026 (CA, NY, UT, WA, OR, HI, CO, CT, GA, IA, NE, RI, NH) plus Idaho from 7/1/27; per-state duties not read | consumer-facing operators | medium | https://avpassociation.com/state-laws-for-ai-chatbots |
| Adult-content age verification | third-party trackers count 29 states with laws in force (Sept 28, 2026); FSC v. Paxton (2025) upheld the Texas law; no state requires age verification for general chatbot use per a Feb 2026 tracker (not checked) | image and video generation with sexual content; chat apps if classified as adult sites | medium | https://www.gadgetreview.com/?p=416283 ; https://www.eff.org/deeplinks/2025/12/year-states-chose-surveillance-over-safety-2025-review |
| Reputational: adult-adjacent traffic | top apps on uncensored endpoints include HotLive (444M), ChamadaVIP (823M), Hornyt (1.3B), HornyDreams (96.2M), fanvue-bot (117M), WildGirl (82.8M), WaifuBot (17.7M), NoFilterGPT (37M) | any provider listing Venice Uncensored, Lunaris, Hermes 3 70B, M2-her, ReMM class models | medium | OpenRouter model pages cited above |
| OpenRouter onboarding | "large backlog of provider applications and are prioritizing providers with proprietary models"; "Priority is given to providers that fill gaps"; uptime under 80% means fallback-only routing | new providers | medium | https://openrouter.ai/providers/apply |
| Small revenue per niche model | the 11 dedicated roleplay and uncensored models sum to about 560M tokens/day (est.), worth low thousands of dollars per week across all providers (est.) | business case | high for a roleplay-only plan | model pages cited above |
| License limits on embeddings and some models | jina-embeddings-v4 is "research and non-commercial use only"; CC BY-NC models "need a commercial license" | embedding hosts | low to medium | https://jina.ai/embeddings/ |
| Chutes and Bittensor dependence | miners paid in TAO by 7-day compute; bare-metal TDX and static IP required; "will not work on Runpod, Vast" | GPU operators | medium | https://github.com/rayonlabs/chutes-miner |
| Civitai-style processor cutoff for AI adult images | not verified (sources unavailable in this session) | image generation with NSFW | unknown | not checked |

### Inferences
- A roleplay-first provider needs breadth (dozens of fine-tunes at flat rates, as Infermatic and Arli do) because any single model on OpenRouter earns tens of dollars a day. A modality-first provider (Whisper, Kokoro, embeddings) faces price floors near $0.01 per 1M tokens and $0.45 per 1,000 minutes but very few incumbents per model.
- Serving from California with card processing requires either a non-adult content policy (which kills the "uncensored" pitch) or a processor outside Stripe and PayPal; Venice and Chutes chose crypto rails.

### Gaps
- Exact weekly tokens and dollar spend per roleplay model (Datasets API needs a key).
- PayPal clause text, SB 243 statutory definitions, the Garcia Section 230 analysis, Civitai's processor history, Chub and NovelAI prices, Janitor AI user counts, Targon miner terms, dots.ocr and Mochi prices, and SDXL fine-tune per-image prices on fal, Replicate and Runware: all not checked in this session.
