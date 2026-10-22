# Inference marketplaces and provider programs for a small independent inference provider

Scope: where a one-person operator running open-weight LLMs (Llama, Qwen, DeepSeek, gpt-oss) on rented GPUs with vLLM or SGLang can list an OpenAI-compatible endpoint and get paid per token. All facts were read live on 2026-10-22 unless a source date is stated. "not found" means the fact is not published anywhere I could reach. "estimate" marks numbers that are estimates.

Method note: I read primary docs with the crw scraper and WebFetch. I did not sign up, log in, submit any form, or contact anyone. Some pages failed to load today (noted in Gaps). The OpenRouter application form at https://openrouter.ai/how-to-list and https://openrouter.ai/providers/apply/form rendered only its heading text, not its fields, even with JavaScript rendering and a 5 second wait, so the field list is "not found".

## Key Question 1: OpenRouter. How does a new provider join, what does it take, how are providers paid, and does a small new provider get traffic?

### Takeaway
OpenRouter accepts outside providers through a form, but it says it has a large application backlog, prioritizes proprietary-model providers and gap-fillers, and (per one secondhand report of an August 2026 event) approves roughly 1 of about 40 daily applications. Listed providers set their own USD prices, get paid by monthly invoicing, keep their list price (OpenRouter takes no markup on inference), and receive traffic by a price-and-speed routing formula that gives any endpoint a small "exploration" share and cuts traffic hard below 95% uptime.

### Cited Findings

**(a) What it is and whether it accepts outside providers**
- OpenRouter describes itself in its terms as "a large language model aggregator where users may use the Site to access third-party application programming interfaces" (Terms last updated August 31, 2026). [Source](https://openrouter.ai/terms) checked 2026-10-22
- The provider program page says: "OpenRouter routes requests across 80+ providers to serve 10M+ developers. We review every application to maintain API reliability and performance standards across the network." [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- The same page: "We currently have a large backlog of provider applications and are prioritizing providers with **proprietary models**." and "Priority is given to providers that fill gaps in our current network." [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- The live providers directory lists "95 of 95 providers" with columns for Trains, Retention, BYOK, Headquarters, Terms, Privacy, Daily tokens, Monthly tokens, Models. [Source](https://openrouter.ai/providers) checked 2026-10-22
- An OpenRouter job posting (Engineering Manager, Provider Ecosystem) says OpenRouter has "hundreds of providers and thousands of endpoints"; this conflicts with the 95 shown on the public directory. [Source](https://jobs.menlovc.com/companies/openrouter-2/jobs/95044500-engineering-manager-provider-ecosystem) checked 2026-10-22 via search result
- Stripe agreed to acquire OpenRouter on August 19, 2026; reported price $7.5B (NYT) to over $8B (Axios); OpenRouter said its name, product and roadmap continue. [Source](https://www.thestack.technology/stripe-acquires-openrouter-setting-up-a-battle-for-ai-routing-business/) checked 2026-10-22 via search result; [Source](https://www.orrick.com/en/News/2026/08/OpenRouter-to-be-Acquired-by-Stripe-to-Help-Businesses-Optimize-Token-Routing-and-Usage)
- A separate Enterprise-only path exists called Private Endpoints: "Private Endpoints are available for Enterprise Plan customers." It lets you route your own deployment of a catalog model to your own organization only; "they will never show up in public model lists, rankings, search, charts, and benchmarks." It requires a BYOK-supported host and a model already in the catalog. Up to 10 endpoints per org by default. Announced Oct 14, 2026. [Source](https://openrouter.ai/docs/guides/routing/private-endpoints) checked 2026-10-22; [Source](https://openrouter.ai/blog/announcements/private-endpoints/)

**(b) How a new provider joins and approval time**
- Docs: "If you'd like to be a model provider and sell inference on OpenRouter, fill out our form to get started." [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22 (the URL https://openrouter.ai/docs/guides/community/for-providers redirects here)
- Form page text: "Complete the form below. We review applications on a rolling basis and will follow up via email. Due to high demand, not all applications are accepted." The page is marked `robots: noindex, nofollow`. Form fields did not render. [Source](https://openrouter.ai/how-to-list) checked 2026-10-22
- Four published stages: "1. Submit your application... 2. Technical review: Our team evaluates your API compatibility, endpoint reliability, pricing, and performance against network standards. 3. Integration & testing: Accepted providers are onboarded with test traffic to validate latency, throughput, and error handling. 4. Go live." [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- Contact: "Reach out to providers@openrouter.ai". [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- Approval rate and bottleneck (secondhand, single source): "At an OpenRouter event on August 20, 2026, the team said that it receives about 40 provider applications each day and accepts about one. It also said that legal review of providers is the current bottleneck. These were event remarks, not published process data." [Source](https://dylanvu.substack.com/p/how-to-get-listed-on-openrouter-as) published 2026-08-21, checked 2026-10-22
- Approval time: not found. No published SLA or typical duration anywhere on openrouter.ai.
- Once accepted, onboarding is automated by a "provider monitor" that polls your `/v1/models` feed: "when OpenRouter's provider monitor sees a new model in your `/v1/models` response, it auto-stages the endpoint, runs baseline tests, and unhides it (makes it live) once the tests pass and pricing is configured." A new endpoint goes live only "when every test passes, pricing is present and non-zero (unless `is_free`), `is_ready` is not `false`, you already have a launched endpoint on OpenRouter (and a launched paid endpoint, for a paid entry), and the endpoint serves chat completions". [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- Providers get a dashboard at `https://openrouter.ai/provider/{provider_slug}/dashboard` with a Schema validator tab and a Provider API (`/api/v1/providers/{provider_slug}`) for rate limits, visibility, capabilities, page links and team members. [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22

**(c) Technical, uptime, latency and API requirements**
- "All providers must meet these requirements before being considered for the network. Applications that don't meet these criteria will not be reviewed." The four listed: OpenAI-Compatible API ("Your /chat/completions endpoint must be OpenAI-compatible, return usage tokens for both stream and non-stream requests, and support streaming."), List Models Endpoint ("Publish a /models endpoint returning your available models with pricing, context length, max output tokens, supported features, and datacenter locations."), Automated Payment ("Support monthly invoicing so OpenRouter can pay for inference without manual intervention."), Privacy & Data Policy ("Have a published privacy policy and clear data retention terms. Providers must disclose whether prompts are logged and if data is used for training."). [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- Tool calling is optional: "You declare which features you support (tools, structured outputs, JSON mode, etc.) in your /models endpoint. OpenRouter only routes feature-specific traffic to providers that support those features." But the docs add that testable capabilities "are never enabled from the feed, only by the capability tests passing." [Source](https://openrouter.ai/providers/apply); [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- The `/models` document format (schema 2.4) requires `id`, `hugging_face_id` ("required if the model is on Hugging Face"), `input_modalities`, `output_modalities`, pricing as `cost_usd` strings ("must be in USD"), optional `capacity` (tokens per minute), `quantization` (valid values `int4, int8, fp4, mxfp4, nvfp4, fp6, fp8, mxfp8, fp16, bf16, fp32`), `datacenters` and `deployment_region`. Only text input `prompt` tokens-per-minute capacity is applied today. [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- Uptime formula: "Your endpoint's uptime is calculated as: successful requests / total requests (excluding user errors)." Counted against uptime: 401, 402, 404, other setup errors (405, 408, 410, 421, 423, 424, 426, 498), all 500+, mid-stream errors, and "Successful requests with error finish reasons". Not counted: 400, 413, 429 ("tracked separately"), 403. [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- Uptime thresholds: "Minimum data: 100+ requests required before uptime calculation begins. Normal routing: 95%+ uptime. Degraded status: 80-94% uptime -> receives lower priority. Down status: <80% uptime -> only used as fallback." [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- Performance metrics are public: "OpenRouter publicly tracks TTFT (time to first token) and throughput (tokens/second) for all providers on each model page. Throughput is calculated as: output tokens / generation time, where generation time includes fetch latency... This means any queueing on your end will show up in your throughput metrics." Advice: "Return early 429s if under load, rather than queueing requests", "Stream tokens as soon as they're available", and send SSE keep-alive comments or "we may cancel with a fetch timeout and fallback to another provider". [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- No numeric latency or TTFT floor is published. Latency and throughput percentiles (p50, p75, p90, p99) are "calculated over a rolling 5-minute window" and users can set `preferred_min_throughput` / `preferred_max_latency` in requests. [Source](https://openrouter.ai/docs/guides/routing/provider-selection) checked 2026-10-22
- Tool-calling traffic is separately ranked by Auto Exacto. An endpoint "needs at least 100 general requests (30-minute window) and 200 tool-call requests (2-hour window) before it can be evaluated"; thresholds apply only when at least 4 providers serve the model; deprioritization at throughput more than 1.5 standard deviations below median, tool-call success more than 2 SD below median, or benchmark accuracy below "median - 2 standard deviations" of the model's first ~21 days of benchmarks. [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22

**(d) Routing: how OpenRouter picks providers by default**
- Default: "OpenRouter's default behavior is to load balance requests across providers, prioritizing price." Steps: "1. Prioritize providers that have not seen significant outages in the last 30 seconds. 2. For the stable providers, look at the lowest-cost candidates and select one weighted by inverse square of the price. 3. Use the remaining providers as fallbacks." Example: a $1/M provider is "9x more likely" to be picked first than a $3/M provider. [Source](https://openrouter.ai/docs/guides/routing/provider-selection) checked 2026-10-22
- A newer provider-facing routing page says the share depends on "your adjusted price and your speed" where adjusted price includes "Effective price: overall cache-adjusted price", "TTFT", "Reliability & quality", "429s", and "Speed: end-to-end TPS". "Competitive: endpoints inside the edge get the most traffic... Exploration: past the edge, your share drops off fast. Every endpoint still gets a small amount of traffic no matter what, so routing can see when it improves." [Source](https://openrouter.ai/docs/guides/providers/traffic-routing) checked 2026-10-22
- New endpoints: "An endpoint with little traffic starts out looking like a typical peer and moves toward its own numbers as data comes in." Limits on top: a "Breaker" that "pauses your traffic until it recovers" if reliability, quality or 429s are "far worse than your peers'"; a "Traffic cap" learned from your 429 rate; and "Short-term backoff". [Source](https://openrouter.ai/docs/guides/providers/traffic-routing) checked 2026-10-22
- Effective price "is the price your endpoint actually charged over the last 30 minutes, across all its traffic. It reflects your real cache hit rate and the mix of input and output tokens". [Source](https://openrouter.ai/docs/guides/providers/traffic-routing) checked 2026-10-22
- Routing is skipped when the user "Names specific providers", "Brings their own provider key", or "Sorts by price, throughput or latency". [Source](https://openrouter.ai/docs/guides/providers/traffic-routing) checked 2026-10-22
- Users can exclude providers by data policy: `data_collection: "deny"` and `zdr: true` route only to endpoints with matching policies. [Source](https://openrouter.ai/docs/guides/routing/provider-selection) checked 2026-10-22

**(e) How and when providers are paid; currency; fees and markup**
- "You set your own per-token pricing in USD. OpenRouter pays you for inference based on actual token usage through monthly invoicing." and "OpenRouter pays providers through monthly invoicing. Payment details are set up during onboarding." [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- Docs: "For OpenRouter to use the provider we must be able to pay for inference automatically. This can be done via auto top up or invoicing." [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- Net terms (net 30 etc.): not found. Minimum payout: not found. Whether provider payouts go through Stripe: not found (Stripe and Coinbase are named only as OpenRouter's inbound payment processors for users). [Source](https://openrouter.ai/terms) checked 2026-10-22
- Markup: "We pass through the pricing of the underlying model providers without any markup" and "Inference is billed at the provider's list price on every plan." OpenRouter's fee is user-side: "OpenRouter's fee is charged when you buy credits, 5.5% on Standard and 8% on Business, never on individual requests." BYOK: "$25,000 per month of list-price inference through BYOK with no OpenRouter fee", then "5% of what the same request would cost at list price." [Source](https://openrouter.ai/docs/faq) checked 2026-10-22; [Source](https://openrouter.ai/pricing) checked 2026-10-22
- Providers can discount: `discount_to_user` "is a decimal fraction that OpenRouter applies to your displayed pricing: user price = base price x (1 - discount_to_user)"; "A negative value applies a markup instead of a discount". [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- Whether OpenRouter negotiates a provider-side cut or wholesale price: not found in any public doc.

**(f) Traffic volume evidence**
- OpenRouter's weekly leaderboard (usage through Oct 21, 2026): #1 DeepSeek V4.1 Flash 25.7T tokens, #2 DeepSeek V4.1 Flash 1017 16.5T, #3 GLM 5.3 Flash 11.3T, #10 Nemotron 3 Ultra (free) 4.46T, all per week. Trailing 30 days: #1 deepseek 125T tokens. [Source](https://openrouter.ai/rankings) checked 2026-10-22
- Platform daily average: "roughly 1% of the platform's 21.9T daily average" (Blockworks, Oct 14, 2026, citing openrouter.ai/models). [Source](https://x.com/BlockworksAdv/article/2110415412580020472) checked 2026-10-22
- Stripe deal coverage: "OpenRouter processes more than 10 trillion tokens a day from over 400 AI models, serving more than 10 million developers". [Source](https://www.thestack.technology/stripe-acquires-openrouter-setting-up-a-battle-for-ai-routing-business/) checked 2026-10-22 via search result
- Per-provider daily tokens on the public directory (top rows): MiniMax 5.5T, DeepSeek 2.0T, Tencent Cloud 1.8T, OpenAI 1.8T, inference.net 1.7T, NVIDIA 1.3T, Together 1.1T, DeepInfra 887.6B, Novita 400.4B, Baseten 286.6B, Fireworks 262.0B. [Source](https://openrouter.ai/providers) checked 2026-10-22
- Unofficial 30-day dashboard (scraped from OpenRouter per-provider pages): "613T tokens tracked across 75 providers (~$52.3M est. gross billings)". Bottom of the leaderboard: Chutes 192B tokens ($51.4K est.), Mancer 76.8B ($14.2K est.), Tenstorrent 47.5B ($8.70K est.), SambaNova 35.1B ($12.7K est.), MARA 23.2B ($10.9K est.), Krea 22.8B ($924 est.), Ambient 1.97B ($580 est.), Featherless 369M tokens ($98 est.). "46 providers under 1% are grouped as Long tail." Revenue figures are estimates: "Treat as +/-30%." [Source](https://or-provider-dashboard.vercel.app/) checked 2026-10-22, estimate
- A second unofficial tracker (Vantage "Provider Economics", data as of 2026-10-21) reports "94 / 114 providers have observed usage" and estimates daily billings such as OpenAI $7.49M/day, Together $401.1K/day, and tiny tails like Deepgram $3.68/day. [Source](https://routers.vantage.sh/data_quality) checked 2026-10-22, estimate

**(g) Do small new providers get real traffic? Quotes**
- "Once OpenRouter lists your service, it can start sending you requests. That does not mean you will receive enough traffic to build a business... Other providers can also add the same model and remove your advantage." [Source](https://dylanvu.substack.com/p/how-to-get-listed-on-openrouter-as) checked 2026-10-22
- Blockworks on seven crypto-native providers: they "served about 211B tokens a day over the past month, roughly 1% of the platform's 21.9T daily average". Venice 86.8B/day, Phala 54.6B, Darkbloom 15.3B, io.net 14.8B, AkashML 13.2B, NEAR AI 12.6B, Chutes 5.7B. [Source](https://x.com/BlockworksAdv/article/2110415412580020472) published 2026-10-14, checked 2026-10-22
- Same article on price vs latency: Darkbloom "undercuts competitors on cost, they still experience higher latency, resulting in unfavorable routing on OpenRouter." Example: Gemma 4 26B, Darkbloom $0.067 vs leader $0.128 per M, latency 2.05s vs 0.72s, share 12.8% (fourth). "On the other models, it answers 3x to 17x slower than the leader, taking a tenth or so of traffic." [Source](https://x.com/BlockworksAdv/article/2110415412580020472) checked 2026-10-22
- Same article: for Venice, "OpenRouter carries under 10% of its revenue"; for Chutes, "Most of its demand comes through its own API and subscriptions, not OpenRouter." [Source](https://x.com/BlockworksAdv/article/2110415412580020472) checked 2026-10-22
- OpenRouter's own routing page: "Being a little behind the best costs you little" but "past the edge, your share drops off fast." [Source](https://openrouter.ai/docs/guides/providers/traffic-routing) checked 2026-10-22
- First-person blog, Reddit, HN, or X posts by a one-person provider who was listed on OpenRouter: not found after six searches (see Gaps).

**(h) Data privacy and logging rules for providers**
- Application requirement: "Have a published privacy policy and clear data retention terms. Providers must disclose whether prompts are logged and if data is used for training." [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- "If OpenRouter is not able to establish or ascertain a clear policy for a provider or endpoint, we take a conservative stance and assume that the endpoint both retains and trains on data and mark it as such." Users can enable "ZDR Only", which removes non-ZDR endpoints. The ZDR list is at `https://openrouter.ai/api/v1/endpoints/zdr`. "OpenRouter has taken the stance that in-memory caching of prompts is not considered 'retaining' data". [Source](https://openrouter.ai/docs/guides/features/zdr) checked 2026-10-22
- Each provider page shows Trains (Yes/No) and Retention (Zero retention, Retains prompts, 30 days retention, etc.) plus Terms and Privacy links; OpenRouter "in some cases creates special agreements with providers to ensure data retention or training policies that are more privacy-focused than their default policies." [Source](https://openrouter.ai/providers); [Source](https://openrouter.ai/docs/guides/features/zdr) checked 2026-10-22
- Providers set `terms_of_service_url`, `privacy_policy_url`, and `status_page_url` through the Provider API. [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- OpenRouter itself: "OpenRouter does not store your prompts or responses, unless you opt in" and stores request metadata (token counts, latency). [Source](https://openrouter.ai/docs/guides/privacy/data-collection) checked 2026-10-22
- Business/Enterprise in-region routing exists (`eu.openrouter.ai`, `us.openrouter.ai`); providers declare `datacenters[].country_code` and `deployment_region`. [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22

### Summary table: OpenRouter (checked 2026-10-22)

| Item | Finding | Source |
| --- | --- | --- |
| Accepts outside providers | Yes, by application; "large backlog"; prioritizes proprietary models and gap-fillers | https://openrouter.ai/providers/apply |
| Approval time | not found | |
| Approval rate | ~1 of ~40 per day (event remark Aug 20, 2026; secondhand) | https://dylanvu.substack.com/p/how-to-get-listed-on-openrouter-as |
| API | OpenAI-compatible /chat/completions with streaming and usage; /models feed in OR schema | https://openrouter.ai/docs/guides/providers/integration |
| Tool calling | Optional; enabled only after OR capability tests pass | same |
| Uptime | 95%+ normal; 80-94% degraded; <80% fallback only; measured after 100 requests | same |
| Latency SLA | No numeric floor; TTFT and TPS tracked publicly; throughput includes queueing | same |
| Payment | Monthly invoicing or auto top-up; USD; net terms not found | https://openrouter.ai/providers/apply |
| Fee / markup | None on inference; user pays 5.5% (Standard) or 8% (Business) on credit purchases | https://openrouter.ai/pricing |
| Providers listed | 95 | https://openrouter.ai/providers |
| Volume | ~21.9T tokens/day (Oct 2026, Blockworks citing OR); top model 25.7T/week | https://openrouter.ai/rankings |
| Smallest providers (30d, unofficial estimate) | Featherless 369M tokens (~$98), Ambient 1.97B (~$580), Chutes 192B (~$51K) | https://or-provider-dashboard.vercel.app/ |
| Privacy | Must publish privacy policy, retention, logging and training disclosure; unknown = assumed retains and trains | https://openrouter.ai/docs/guides/features/zdr |

### Inferences
- A solo operator on rented GPUs is not what OpenRouter says it is prioritizing (proprietary models, gap-fillers). The published rules do not forbid it, but the backlog and the reported 1-in-40 acceptance make it a long shot unless the operator serves a model or region OpenRouter lacks.
- The routing formula punishes TTFT and queueing, and rewards cache hit rate. A small vLLM deployment with few concurrent slots will return 429s under load; OpenRouter says that is better than queueing, but repeated 429s set a learned traffic cap, so the ceiling on revenue is the operator's real concurrency.
- Because the user-facing fee is charged on credit purchases and OpenRouter states no inference markup, the provider's gross revenue should equal list price times billed tokens (estimate; the provider contract terms are not public).
- The unofficial dashboards show a long tail of providers earning tens of dollars to a few thousand dollars a month on OpenRouter. The platform does not guarantee volume to small providers.

### Gaps
- OpenRouter's application form fields (company, legal entity, bank details, etc.) did not render; "not found".
- Net payment terms, minimum payout, payout rail (ACH, wire, Stripe) and whether a signed provider agreement exists: not found.
- Approval duration: not found.
- No first-person account from a small or solo provider that was listed on OpenRouter was found on Reddit, HN, X, or blogs. The only third-party guide (dylanvu.substack.com) is a synthesis, not a listing report.
- The 40-applications-per-day figure is from one secondhand source and is unverified.

## Key Question 2: Hugging Face Inference Providers. How to register, requirements, revenue split, billing.

### Takeaway
Hugging Face publishes a detailed, mostly self-serve technical path (OpenAI-compatible API, a huggingface.js PR, a billing endpoint in nano-USD, model mappings), but step 3 requires HF to enable your org server-side and a paid Team or Enterprise plan. HF charges users no markup and has said it "may establish revenue-sharing agreements" later; how and when HF pays providers is not published. Its public feedback thread shows many 2026 applicants, including one-GPU operators, with no staff reply since September 2025.

### Cited Findings
- "Want to be listed as an Inference Provider on the Hugging Face Hub? Let's get in touch! Please reach out to us on social networks or here on the Hub." and "Note that Step 3 will require your organization to upgrade their Hub account to a Team or Enterprise plan." [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider) checked 2026-10-22
- Nine steps: implement task APIs, submit a PR to huggingface.js, register model mappings via `POST /api/partners/{provider}/models`, implement a billing endpoint, submit a PR to huggingface_hub, get registered server-side and supply an SVG icon, write docs, open a docs PR, and "Share share share". [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider) checked 2026-10-22
- Shortcut: "If your implementation strictly follows the OpenAI API for LLMs and VLMs, you may be able to skip most of this section. In that case, simply open a PR on huggingface.js to register." [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider) checked 2026-10-22
- Gating: "To proceed with this step, we have to enable your account server-side. Make sure you have an organization on the Hub for your company, and upgrade it to a Team or Enterprise plan." [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider) checked 2026-10-22
- Validation and uptime: "Each model is tested every 6 hours by making API calls to your service... if the test fails... the provider will be temporarily removed from the list of active providers." "A failed mapping undergoes retesting every hour." Latency requirement: "For conversational models: under 5 seconds (time to first token in streaming mode)." LLMs also get "Tool calling support" and "Structured output support" tests. [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider) checked 2026-10-22
- Billing: "our intent is that our users only pay the standard provider API rates. There's no additional markup from us, we just pass through the provider costs directly." Providers must expose a POST billing API returning `costNanoUsd` per request ID; HF calls it "every minute, in batches of up to 10,000 request IDs"; "If a request is still unbilled roughly 30 minutes after it was served, we give up on it... not charged to the user." Providers must send an `Inference-Id` response header on every response including streams, and expose `pricing.input`, `pricing.output` (USD per million tokens) and `context_length` on `/v1/models`. [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider) checked 2026-10-22
- Default ranking: "The default sort is by total number of requests routed by HF over the last 7 days. This order defines which provider will be used in priority by the widget on the model page". The server-side router defaults to `:fastest` ("highest throughput in tokens per second"); `:cheapest` picks "lowest price per output token". [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider); [Source](https://huggingface.co/docs/inference-providers/index) checked 2026-10-22
- User pricing: "Hugging Face charges you the same rates as the provider, with no additional fees." PRO users get $2.00 monthly credits; Team/Enterprise $2.00 per seat; Free users must buy credits. [Source](https://huggingface.co/docs/inference-providers/pricing) checked 2026-10-22
- Revenue share: the Fireworks launch post said HF "may establish revenue-sharing agreements with its provider partners in the future"; the Scaleway post repeats this; TechCrunch (Jan 28, 2025) reported "standard provider API rates, at least for now". No current docs page describes a revenue share or how HF settles with providers. [Source](https://huggingface.co/blog/fireworks-ai); [Source](https://huggingface.co/blog/inference-providers-scaleway); [Source](https://techcrunch.com/2025/01/28/hugging-face-makes-it-easier-for-devs-to-run-ai-models-on-third-party-clouds/) checked 2026-10-22 via search results
- Partner count: 18 partners listed (Baseten, Cerebras, Cohere, DeepInfra, Fal AI, Featherless AI, Fireworks, Groq, HF Inference, Novita, Nscale, OVHcloud AI Endpoints, Public AI, Replicate, Scaleway, Together, WaveSpeedAI, Z.ai). [Source](https://huggingface.co/docs/inference-providers/index) checked 2026-10-22
- Public feedback thread #49 ("[FEEDBACK] Inference Providers", opened Jan 17, 2025 by julien-c) is the stated place to ask. Of 209 dated posts in the thread, 113 carry 2025 dates and 96 are 2026 or "days ago". The 15 Hugging Face staff replies all date between Jan 17, 2025 and Sep 23, 2025 ("PublicAI and Scaleway have been added!"). No staff reply appears after Sep 23, 2025. [Source](https://huggingface.co/spaces/huggingface/HuggingDiscussions/discussions/49?expand=true) checked 2026-10-22 (count from my scrape of the expanded thread)
- Recent small applicants in that thread with no visible reply: InfraXsky ("Hosted on a dedicated GPU server in Helsinki, Finland... Two questions: is a Team plan required for the Model Mapping step, and how are providers paid out for routed requests?", ~19 hours before 2026-10-22); Fractalyze ("The current pilot runs on one RTX 5090... Could you also share the provider commercial terms, platform fees, and payout currency, schedule, and minimums?", 2 days ago); ERON X ("Can a smaller, independent European GPU infrastructure provider join the program?", 3 days ago); Linkrra ("Models we serve on GPUs we operate ourselves... Are you currently accepting new providers", 4 days ago); VeloInfer (Aug 16, 2026, capacity from "Vast.ai, RunPod"); Gridmetry GmbH (Aug 25, 2026); Telnyx (Sep 3, 2026). [Source](https://huggingface.co/spaces/huggingface/HuggingDiscussions/discussions/49) checked 2026-10-22

### Summary table: Hugging Face Inference Providers (checked 2026-10-22)

| Item | Finding | Source |
| --- | --- | --- |
| Accepts outside providers | Yes in principle; HF must enable your org server-side | register-as-a-provider doc |
| Join path | Contact HF (social or thread #49), huggingface.js PR, Team/Enterprise plan, Model Mapping API, billing endpoint | same |
| Approval time | not found; public thread shows no staff replies since Sep 23, 2025 | thread #49 |
| API | OpenAI-compatible for LLMs; `/v1/models` with pricing and context_length; `Inference-Id` header | same |
| Uptime / latency | Tested every 6 h; TTFT under 5 s streaming; failed providers removed until retest passes (hourly) | same |
| Payment to provider | not found (HF bills users at provider rate; settlement with provider not documented) | pricing doc |
| Revenue share | None published; "may establish revenue-sharing agreements... in the future" (2025) | fireworks-ai blog |
| Currency | USD (billing API in nano-USD) | register doc |
| Partners | 18 | index page |
| Privacy | Provider docs page "should... include... data retention policies"; no other rule found | register doc |

### Inferences
- The technical bar for an OpenAI-compatible vLLM server is low (a PR plus a billing endpoint), but the practical gate is HF's manual server-side enablement, which appears to be slow or paused for small applicants based on the thread.
- A Team plan costs money (price not captured here), so the entry cost is non-zero even before any traffic.

### Gaps
- Team plan price today: not captured.
- How HF pays providers (rail, cadence, minimum): not found.
- Whether any 2026 applicant from the thread was onboarded privately: unknown.

## Key Question 3: Requesty, Unify, Martian, AIML API, NanoGPT, Featherless, Parasail, Kluster.ai, Chutes, cheapinference.com.

### Takeaway
Of this list, only NanoGPT publishes a provider intake page, and it says a single-GPU operator is "unlikely to be a fit." Chutes is open to anyone with TDX-capable bare metal but pays in Bittensor subnet tokens. Requesty, AIML API, Featherless and Parasail have no published outside-provider program; Unify and Martian have pivoted away from routing; Kluster.ai shut its inference service in July 2025; cheapinference.com is a parked domain.

### Cited Findings

| Marketplace | What it is | Accepts outside providers? | Join / approval | Pay / currency | Fees | Traffic evidence | Privacy rules | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Requesty | "AI Gateway & LLM Router for 600+ Models"; "30+ providers" | No published program; "not found" | Contact sales@requesty.ai (enterprise page) | n/a | Users: "You pay the provider's token prices, and a 5% service fee is added when you top up credits." BYOK supported | not found | not found | 2026-10-22 |
| Unify (unify.ai) | Site now sells "Models that keep learning" (continual learning); docs at docs.unify.ai redirect to a Mintlify login | No | n/a | n/a | n/a | n/a | n/a | 2026-10-22 |
| Martian (withmartian.com) | Now an interpretability research lab ("Understanding Intelligence"); points to Thesean AI for "Best Execution for LLMs" | No router marketplace found | n/a | n/a | n/a | n/a | n/a | 2026-10-22 |
| AIML API (aimlapi.com) | Aggregator of "1000+ models"; its Partner Program is for agent/app builders who route users to AIML API and earn affiliate revenue, paid "through our payments partner, Tolt" | No model-provider onboarding page found; "Contact us" only | n/a | Affiliate payouts via Tolt; provider payments not found | not found | not found | not found | 2026-10-22 |
| NanoGPT (nano-gpt.com) | Pay-per-use multi-model service with a "For Providers" page | Yes, selectively: "We work with inference providers and model developers that can offer something valuable to NanoGPT users." | Email support@nano-gpt.com or Discord with company, capacity, regions, rate limits, privacy policy, payment method, OpenAI-compatible endpoint | NanoGPT pays the provider as a customer; it asks "Whether you support credit card payments or automatic invoicing" | not found | not found | Must state "whether prompts are logged and how long they are retained" | 2026-10-22 |
| Featherless (featherless.ai) | "Serverless LLM Hosting", "Browse 40,000+ models"; it is itself a provider (listed on HF and OpenRouter) | No outside-provider program found | n/a | n/a | n/a | On OpenRouter: 369M tokens / 30d, ~$98 est. (unofficial) | n/a | 2026-10-22 |
| Parasail (parasail.io) | "The Inference Cloud for AI-native startups"; sells serverless and "Elastic endpoints" at "25% above the model's Serverless input and output token rates" | No outside-provider program found | n/a | n/a | n/a | On OpenRouter: 11.2T tokens / 30d, 1.8% share, ~$1.14M est. (unofficial) | n/a | 2026-10-22 |
| Kluster.ai | Former inference provider | No; "End of life" for Inference, Fine-Tuning and Dedicated Deployments announced July 17, 2025, effective July 24, 2025; pivot to AI code review. Site DNS failed today | n/a | n/a | n/a | n/a | n/a | 2026-10-22 |
| Chutes (chutes.ai, Bittensor SN64) | Decentralized inference subnet; CRYPTO: miners earn SN64 token emissions, not USD | Yes, permissionless with hardware limits | `btcli subnet register --netuid 64`; "The chutes network is now TEE-exclusive"; GPU hosts "must additionally be TDX-capable"; "ALL servers must be bare metal/VM, meaning it will not work on Runpod, Vast, etc."; control plane "4 cores, 32gb ram minimum"; RAM per GPU about equal to VRAM | Token emissions; "Incentives are based on total compute time"; "Incentives/weights are calculated from 7 day sum of compute". Blockworks: subnet gets "$21M - $33M a year, paid in its own token, with 41% going to miners" | Registration costs TAO (Bittensor docs) | ~4,350 GPUs; 160B tokens/day claimed by team; 5.7B/day on OpenRouter; 192B tokens/30d on OR (unofficial) | not found | 2026-10-22 |
| cheapinference.com | Parked domain: page shows "Buy This Domain" | No | n/a | n/a | n/a | n/a | n/a | 2026-10-22 |

Sources for the table:
- Requesty: [docs](https://docs.requesty.ai/) checked 2026-10-22 (quote: "You pay the provider's token prices, and a 5% service fee is added when you top up credits."); [enterprise page](https://www.requesty.ai/enterprise-new) via search; /providers returns 404.
- Unify: [unify.ai](https://unify.ai/) checked 2026-10-22; [docs redirect](https://docs.unify.ai/universal_api) redirected to app.mintlify.com login on 2026-10-22.
- Martian: [withmartian.com](https://withmartian.com/) checked 2026-10-22.
- AIML API: [partner program](https://aimlapi.com/partner-program) checked 2026-10-22 ("Payouts are handled automatically worldwide through our payments partner, Tolt").
- NanoGPT: [For Providers](https://docs.nano-gpt.com/api-reference/miscellaneous/for-providers) checked 2026-10-22. Full quote: "Size alone is not a requirement. A smaller provider can still be a strong fit if it offers a distinctive model or capability. However, if the offering is otherwise similar to providers we already support, we generally expect meaningful operational scale. A single-GPU or single-operator service is unlikely to be a fit unless it offers something genuinely unique."
- Featherless: [featherless.ai](https://featherless.ai/) checked 2026-10-22; OR volume from [or-provider-dashboard](https://or-provider-dashboard.vercel.app/) (estimate).
- Parasail: [parasail.io](https://www.parasail.io/) checked 2026-10-22; OR volume from [or-provider-dashboard](https://or-provider-dashboard.vercel.app/) (estimate).
- Kluster.ai: [EOL announcement](https://kluster.ai/blog/end-of-life-announcement) via search result on 2026-10-22; direct fetch failed (DNS).
- Chutes: [chutes-miner README](https://github.com/rayonlabs/chutes-miner) checked 2026-10-22; [Blockworks](https://x.com/BlockworksAdv/article/2110415412580020472) Oct 14, 2026; Bittensor registration cost: "To participate as a miner, you must first register your keys with the subnet in order to receive a UID on that subnet. Registration has a cost in TAO." [Source](https://docs.bittensor.com/miners) via search result (the page redirected twice on direct fetch today).
- cheapinference.com: [cheapinference.com](https://cheapinference.com) checked 2026-10-22.

Related but different domain: cheaperinference.com (Keak AI, Inc.) is live and runs a "For capacity sellers" program: "Turn unused inference capacity into revenue. Tell us where you have available capacity and its approximate dollar value. Our team will review the fit and contact you directly." It links a Seller Agreement at https://cheaperinference.com/legal/seller-agreement and says "Discuss supply and settlement". Pricing to users: "Usage based. No separate routing surcharge. Never above direct list price." [Source](https://cheaperinference.com/) checked 2026-10-22. Terms of the Seller Agreement were not read.

### Inferences
- For a USD-paid, per-token listing, this group offers one realistic door (NanoGPT, by email, with an explicit bias against single-GPU operators) and one speculative door (cheaperinference.com's capacity-seller form, terms unknown).
- Chutes is open to a solo operator who can get TDX-capable bare metal, but the pay is a volatile subnet token and the network itself subsidizes prices from emissions.

### Gaps
- NanoGPT: payment terms, cut, and approval time: not found.
- AIML API: whether it ever onboards third-party model hosts: not found.
- Chutes: current per-miner earnings in USD terms: not found (Blockworks gives only subnet-level estimates).
- cheaperinference.com Seller Agreement contents: not read.

## Key Question 4: Other gateways and providers. Which accept outside providers, and which are first-party only?

### Takeaway
The mainstream gateways (Vercel AI Gateway, Cloudflare AI Gateway, Portkey, Helicone, LiteLLM, Eden AI) route to fixed provider lists or let a user connect their own private endpoint; none runs a public marketplace that pays outside providers per token. The first-party clouds (Novita, DeepInfra, Fireworks, Baseten) sell their own inference. The crypto networks (Inference.net, Targon, Gonka, Psyche) either pay in tokens, require 8-GPU TEE nodes, or are training networks, and one (Inference.net) looks dormant on the operator side.

### Cited Findings

| Name | Type | Accepts outside providers? | Key facts | Source (checked 2026-10-22) |
| --- | --- | --- | --- | --- |
| Vercel AI Gateway | Gateway | No listing process found | "AI Gateway adds zero markup to provider token prices, including with BYOK." Default routing "based on a combination of recent uptime and latency." | https://vercel.com/docs/ai-gateway |
| Cloudflare AI Gateway | Gateway | No; fixed list of 24 providers (incl. OpenRouter, Baseten, HuggingFace) | Universal endpoint `provider` "Can be OpenAI, workers-ai, or any of our supported providers." No custom endpoint documented | https://developers.cloudflare.com/ai-gateway/usage/providers/ ; https://developers.cloudflare.com/ai-gateway/usage/universal/ |
| Portkey | Gateway | No marketplace; users can add a "Local/Privately hosted provider" (custom host, must implement a supported API spec such as OpenAI) | Self-hosted vLLM works as the user's own provider, not as a paid listing | https://portkey.ai/docs/integrations/llms/byollm |
| Eden AI | Aggregator ("~1,000 models from more than 50 providers") | Partly: providers can add their API by pull request to the open-source `edenai-apis` repo; "The team reviews pull requests and only validates strong AI APIs." Separate affiliate partner program pays commission | No per-token payout terms published | https://github.com/edenai/edenai-apis ; https://edenai.co/post/grow-your-business-by-becoming-an-eden-ai-partner (via search) |
| LiteLLM | Open-source proxy/SDK | No marketplace; any OpenAI-compatible endpoint can be configured by the user (`openai/` prefix, `api_base`) | | https://docs.litellm.ai/docs/providers/openai_compatible |
| Helicone | Observability + gateway | No marketplace | "0% markup - Pay exactly what providers charge"; BYOK | https://docs.helicone.ai/ |
| Inference.net (ex-Kuzco) | CRYPTO-origin GPU network; now a large OpenRouter provider | Operator program status unclear | Operator docs (indexed): "Operators can earn USDC by contributing their compute power to the network." Direct fetches of operator.inference.net returned 404 today; docs.devnet.inference.net 301-redirects to x.com/inference_net. Third-party review (Oct 3, 2026): "We could not find a single devnet, epoch or operator post on the company's X account in the 12 months to October 2026" and operators should "assume it earns nothing until the company says otherwise." On OpenRouter: 1.7T tokens/day, "Zero retention", 8 models | https://operator.inference.net/getting-started/introduction (search snippet); https://solanacompass.com/projects/inference ; https://openrouter.ai/providers |
| Targon (Bittensor SN4, Manifold) | CRYPTO GPU-hour marketplace with TEE | Yes, but node profiles require "exactly 8 GPUs of one listed SKU: H100, H200, B200, B300, or RTX PRO 6000 Blackwell"; "The TEE must be enabled in BIOS" (Intel TDX or AMD SEV-SNP); e.g. `h100-8x-intel` needs 1.5 TiB RAM, 128 threads, 3 TB storage | Paid per card via auctions priced in USD cents per hour (H200 target 290c, cap 350c; B200 target 420c, cap 650c) but settled from subnet emissions; "Emissions not allocated to auctions are burned." Not a per-token inference listing | https://github.com/manifold-inc/targon/blob/main/docs/miner/miner.md |
| Gonka | CRYPTO decentralized inference network | Yes, permissionless; "Registration stays free on mainnet" | Hardware: "at least 320 GB total GPU VRAM is available to each MLNode container"; listed GPUs B300, B200, RTX PRO 6000, H200, H100, A100 80GB; node server 16 cores, 64+ GB RAM, 1 TB NVMe, 100 Mbps+. Rewards in GNK; "Without [collateral], a Host receives only the base weight (20% by default)"; Proof of Compute about every 24 h; models added by governance; no USD | https://gonka.ai/docs/host/hardware-specifications/ ; https://gonka.ai/docs/host/quickstart/ |
| Nous Psyche | Decentralized TRAINING network on Solana | Not an inference marketplace | "open infrastructure that democratizes AI development by decentralizing training"; roadmap puts "Accessible Inference" after "Cooperative Training" which "begins with a permissioned testnet"; rewards not described. docs.psyche.network refused connections today | https://nousresearch.com/nous-psyche/ |
| Novita AI | First-party provider | GPU supply channel only: footer "Supply GPUs" link to gpu@novita.ai; no per-token provider listing described | On OpenRouter 400.4B tokens/day, 48 models | https://novita.ai/ ; https://openrouter.ai/providers |
| DeepInfra | First-party provider | No; "DeepInfra runs on our own cutting-edge inference optimised infrastructure, in secure US-based data centers." | On OpenRouter 887.6B tokens/day, 107 models | https://deepinfra.com/ ; https://openrouter.ai/providers |
| Fireworks AI | First-party provider | No supplier program found | On OpenRouter 262.0B tokens/day | https://fireworks.ai/ ; https://openrouter.ai/providers |
| Baseten | First-party platform | No; "Baseten for Model Labs" lets model creators "Distribute and monetize your model on Baseten infrastructure" (models, not GPUs) | On OpenRouter 286.6B tokens/day | https://www.baseten.co/ ; https://openrouter.ai/providers |

### Inferences
- None of the general-purpose gateways is an "Airbnb for inference" for sellers. They are buyers' tools. The only sell-side marketplaces that pay USD per token and accept outsiders are OpenRouter, Hugging Face (in principle), NanoGPT (selectively), and possibly cheaperinference.com.
- The decentralized networks that are permissionless (Chutes, Gonka, Targon) all now require confidential-compute hardware or very large VRAM nodes, which rules out most rented single-GPU setups (Chutes explicitly excludes RunPod and Vast).

### Gaps
- Inference.net's current operator program (if any): could not be read; the operator docs returned 404 and the devnet docs redirect to X.
- Psyche docs were unreachable (ECONNREFUSED).
- Targon payout settlement currency (USD vs alpha token) is not stated on the miner page; the auction prices are in USD cents but emissions are the pool.

## Key Question 5: Cross-cutting answers

### Takeaway
One person with rented GPUs can apply to OpenRouter today, but OpenRouter publishes no approval timeline, says it has a backlog and is prioritizing proprietary models, and one secondhand report puts acceptance near 1 in 40 per day. USD per-token payout by invoice exists at OpenRouter (monthly invoicing) and, by design, at Hugging Face (nano-USD billing API), while Chutes, Gonka and Targon pay in crypto. No marketplace publishes a provider revenue share; OpenRouter and Hugging Face both say they add no markup for users. OpenRouter expects 95%+ uptime and cuts routing priority at 80-94% and to fallback-only below 80%; Hugging Face drops a provider from the active list after a failed 6-hourly test until an hourly retest passes.

### Cited Findings

**Can one person with rented GPUs realistically get approved on OpenRouter, and how long does it take?**
- OpenRouter does not state a minimum company size or hardware ownership requirement; its listed technical requirements are the OpenAI-compatible API, /models feed, monthly invoicing support, and a published privacy policy. [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- It does state a backlog and a priority: "We currently have a large backlog of provider applications and are prioritizing providers with proprietary models." [Source](https://openrouter.ai/providers/apply) checked 2026-10-22
- Secondhand: "about 40 provider applications each day and accepts about one"; "legal review of providers is the current bottleneck." [Source](https://dylanvu.substack.com/p/how-to-get-listed-on-openrouter-as) checked 2026-10-22
- Approval time: not found.
- The same guide recommends: "Run the model on infrastructure that you operate, whether you own or rent it." and "Do not ask for a listing before the endpoint is callable." [Source](https://dylanvu.substack.com/p/how-to-get-listed-on-openrouter-as) checked 2026-10-22
- A new endpoint is only auto-unhidden if "you already have a launched endpoint on OpenRouter (and a launched paid endpoint, for a paid entry)"; the first endpoint therefore needs staff action. [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22

**Which marketplaces pay in USD by bank transfer or Stripe, and which pay only in crypto?**

| Marketplace | Currency | Rail | Cadence / minimum | Source |
| --- | --- | --- | --- | --- |
| OpenRouter | USD (prices "must be in USD") | "monthly invoicing"; rail not found | Monthly; minimum not found; net terms not found | https://openrouter.ai/providers/apply ; https://openrouter.ai/docs/guides/providers/integration |
| Hugging Face | USD (billing API in "nano-USDs") | not found | not found | https://huggingface.co/docs/inference-providers/en/register-as-a-provider |
| NanoGPT | Implied USD (asks if you accept "credit card payments or automatic invoicing") | Card or invoice, paid by NanoGPT as a customer | not found | https://docs.nano-gpt.com/api-reference/miscellaneous/for-providers |
| cheaperinference.com | Capacity stated "in USD"; settlement "Discuss supply and settlement" | not found | not found | https://cheaperinference.com/ |
| Chutes (SN64) | Crypto: SN64 subnet token emissions ("41% going to miners") | On-chain | Weights from "7 day sum of compute" | https://github.com/rayonlabs/chutes-miner ; Blockworks |
| Targon (SN4) | Crypto: subnet emissions; auction prices quoted in USD cents per card-hour | On-chain | Per auction | https://github.com/manifold-inc/targon/blob/main/docs/miner/miner.md |
| Gonka | Crypto: GNK; "Always use the ngonka denomination for balances and fees" | On-chain | Epochs "~24 hours"; rewards claimable after epoch stage | https://gonka.ai/docs/host/quickstart/ |
| Inference.net operators | Docs said USDC; program status unclear (see above) | On-chain (Solana) | not found | https://solanacompass.com/projects/inference |

**Is a published provider revenue share or markup anywhere?**
- OpenRouter: "We never mark-up the pricing of the underlying providers." Fee is on the buyer side (5.5% Standard, 8% Business on credit purchases). Provider-side cut: not found. [Source](https://openrouter.ai/docs/faq); [Source](https://openrouter.ai/pricing) checked 2026-10-22
- Hugging Face: "There's no additional markup from us, we just pass through the provider costs directly." Revenue share: "may establish revenue-sharing agreements with its provider partners in the future" (2025). [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider); [Source](https://huggingface.co/blog/fireworks-ai) checked 2026-10-22
- Vercel AI Gateway: "zero markup". Helicone: "0% markup". Requesty: 5% on top-ups. None publish a provider share. [Sources above]
- Chutes: Blockworks states the subnet-level split (41% of emissions to miners) and that Chutes "ranking among the three cheapest providers on every model it serves on OpenRouter" is "largely funded by Bittensor emissions". [Source](https://x.com/BlockworksAdv/article/2110415412580020472) checked 2026-10-22

**What uptime do they expect, and what happens on downtime?**
- OpenRouter: "Providers with 95%+ uptime receive normal routing priority. Between 80-94% uptime, traffic is reduced. Below 80%, your endpoints are used only as fallback." Plus the live "Breaker" that "pauses your traffic until it recovers" when error rate is "far above your peers'". Providers can hide an endpoint themselves via `PATCH .../visibility`, and "Unhiding re-runs the baseline tests". Also "Models past their deprecation time may be automatically hidden from the marketplace." [Source](https://openrouter.ai/providers/apply); [Source](https://openrouter.ai/docs/guides/providers/traffic-routing); [Source](https://openrouter.ai/docs/guides/providers/integration) checked 2026-10-22
- Hugging Face: 6-hourly test; on failure "the provider will be temporarily removed from the list of active providers"; retest hourly; TTFT must be under 5 seconds. [Source](https://huggingface.co/docs/inference-providers/en/register-as-a-provider) checked 2026-10-22
- NanoGPT: wants "Sufficient production capacity and operational support to handle sustained traffic reliably"; no numeric threshold. [Source](https://docs.nano-gpt.com/api-reference/miscellaneous/for-providers) checked 2026-10-22
- Chutes: no uptime number published; incentives are "total compute time" over a 7-day window, so downtime lowers weight. [Source](https://github.com/rayonlabs/chutes-miner) checked 2026-10-22

### Inferences
- For a solo operator who wants USD, the only two public marketplaces are OpenRouter and Hugging Face, and both currently gate entry by human review that appears slow (OpenRouter backlog; HF thread silent since Sep 2025). NanoGPT is a third, smaller buyer that pays like a customer and has said single-GPU operators are unlikely fits.
- A realistic plan should treat marketplace listing as a possible later channel, not the first revenue source, and should assume that if listed, traffic share will track TTFT and throughput against larger hosts of the same model.
- Crypto networks are the only permissionless routes, and all three mature ones now require TDX or SEV-SNP bare metal or 320 GB+ VRAM nodes, so rented consumer-class or single-H100 setups mostly do not qualify.

### Gaps
- No marketplace publishes provider-side contract terms (net days, minimum payout, revenue share, termination for downtime). These must be obtained from each company directly.
- No first-person report from a one-person provider on OpenRouter or Hugging Face was found; the closest evidence is the HF thread of unanswered applicants and Blockworks' analysis of small crypto providers' traffic.
- The OpenRouter application form fields are not visible without rendering that this run could not achieve.
