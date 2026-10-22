# Top OpenRouter revenue models: weights, licenses, serving support, and host economics (verified 2026-10-22)

Scope: the 14 models the coordinator listed as the top revenue opportunities on OpenRouter as of 2026-10-22. For each model this file answers six questions: (1) are weights public, (2) license and paid-API terms, (3) architecture and size, (4) vLLM and SGLang support, (5) why OpenRouter hosts price it the way they do and whether hosts self-host or proxy, (6) preview status.

Method notes. OpenRouter data comes from the public endpoints API (`https://openrouter.ai/api/v1/models/<slug>/endpoints`), read on 2026-10-22. Prices there are USD per token; this file converts them to USD per million tokens. Weight sizes come from the Hugging Face API `usedStorage` field (decimal GB) unless noted; a few repos report storage that does not match the dtype math, and those cases are flagged. "Smallest 8-GPU node" uses the memory figures the coordinator gave (8x H100 640 GB, 8x H200 1,128 GB, 8x B200 1,440 GB, 8x MI300X 1,536 GB, 8x MI355X 2,304 GB) and is my estimate unless a vendor recipe states the node. Items marked "estimate" or "inference" are mine, not from a source. "Not read directly" means the claim comes from a search-result summary of a page I did not fetch.

---

## 1. tencent/hy4-preview (Tencent Hy4 preview)

### Takeaway
Weights are public under Apache 2.0, in BF16 (1,560 GB) and FP8 (814 GB). Tencent calls it "an early version of Hy4" with known reasoning issues. All four OpenRouter hosts charge exactly Tencent's international list price ($0.834 / $2.501), yet three of them list their own quantizations, so they appear to self-host at a price pegged to the lab.

### Cited Findings

**1. Weights**
- Repo `tencent/Hy4-preview`, `gated: false`, created 2026-08-27T08:52:40Z, `usedStorage` 1,560,008,337,568 bytes (about 1,560 GB), safetensors BF16 779.9B params, license tag `apache-2.0` - [HF API](https://huggingface.co/api/models/tencent/Hy4-preview)
- FP8 repo `tencent/Hy4-preview-FP8`, `gated: false`, created 2026-08-27, about 814 GB, F8_E4M3 770.3B params plus BF16 9.6B - [HF API](https://huggingface.co/api/models/tencent/Hy4-preview-FP8)
- Model card: "We open-source Hy4 preview and Hy4 preview-FP8 model weights on Hugging Face", also on ModelScope, GitCode, CNB - [HF model card](https://huggingface.co/tencent/Hy4-preview)
- OpenRouter lists the model as created 1787897375 (2026-08-28) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/tencent/hy4-preview/endpoints)

**2. License**
- Card: Hy4 preview "is released under the **Apache License 2.0**"; metadata `license: apache-2.0` - [HF model card](https://huggingface.co/tencent/Hy4-preview)
- Apache 2.0 has no MAU, revenue, attribution-in-UI, or competing-model clauses; a paid API is permitted without a separate agreement (standard license terms).

**3. Architecture and size**
- "770B" total, "49B" activated; 78 layers (first dense, 77 MoE); 256 routed + 1 shared expert, top-8 routed; hidden 6144; 1M context; MTP layer of 10B total / 0.7B active - [HF model card](https://huggingface.co/tencent/Hy4-preview)
- Hub metadata shows 780B, which the card attributes to the MTP layer - [HF model card](https://huggingface.co/tencent/Hy4-preview)
- Native precision BF16 (tensor types BF16 and F32); FP8 variant also published - [HF model card](https://huggingface.co/tencent/Hy4-preview)
- vLLM recipe index lists memory figures "BF16 (1848G)" and "MXFP8 (924G)" - [vLLM recipes, tencent](https://recipes.vllm.ai/tencent)
- Node fit (recipe): supported configs "16×B200, 8×B300, and 8×MI355X"; the main NVIDIA example serves `tencent/Hy4-preview-FP8` with `--tensor-parallel-size 8` on one 8-GPU node; MI355X MXFP8 reaches full 1,048,576 context; MI325X FP8 is limited to 139,264 context - [vLLM recipe](https://recipes.vllm.ai/tencent/Hy4-preview)

**4. Serving**
- vLLM supported-models table: "`HYV4ForCausalLM` | HY4 | `tencent/Hy4-preview`, `tencent/Hy4-preview-FP8` | ✅︎ | ✅︎" - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- vLLM recipe: "vLLM 0.29.0+", Docker image `vllm/vllm-openai:hy4-preview`, flags `--speculative-config '{"num_speculative_tokens":3,"method":"mtp"}'`, `--attention-backend FLASHMLA_SPARSE`, `--tool-call-parser hy_v4`, `--reasoning-parser hy_v4`, env `VLLM_ENABLE_HPC_OPS=1`; on MI355X "Spec decoding (native MTP, `k=3`) is opt-in" - [vLLM recipe](https://recipes.vllm.ai/tencent/Hy4-preview)
- SGLang: image `lmsysorg/sglang:hy4-preview`, `--tp-size 8`, `--reasoning-parser auto`, `--tool-call-parser auto`, NEXTN speculative decoding (3 steps, 4 draft tokens) - [HF model card](https://huggingface.co/tencent/Hy4-preview)
- The card lists no MTP, tool-parser, or reasoning-parser bugs; the only stated issues are model behavior (see item 6) - [HF model card](https://huggingface.co/tencent/Hy4-preview)

**5. OpenRouter pricing and hosts**
- Four endpoints, all at prompt $0.834 / completion $2.501 / cache read $0.042 per M: DeepInfra (fp4, 1,048,576 ctx), Novita (fp8, 1,000,000 ctx), SiliconFlow (fp8, 1,048,576 ctx), Tencent (fp8, 1,048,576 ctx) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/tencent/hy4-preview/endpoints)
- The Tencent endpoint alone carries a time-of-day override: UTC 16:00 to 00:00 prompt $0.7506 / completion $2.2509 - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/tencent/hy4-preview/endpoints)
- Tencent's domestic list price is 6 CNY input / 18 CNY output / 0.3 CNY cache hit per M (Beijing Business Today, not read directly) - [bbtnews](https://www.bbtnews.com.cn/2026/0828/603995.shtml)
- An aggregator lists the Tencent Cloud (Asia) endpoint at $0.834 / $2.501 / $0.042 (not read directly) - [Eden AI](https://www.edenai.co/models/hy4-preview)
- Tencent's legacy Hunyuan price page does not list hy4-preview and says new models move to TokenHub - [Tencent Cloud doc](https://cloud.tencent.com/document/product/1729/97731)

**6. Preview status**
- Card: "This is an early version of Hy4." "There is real headroom left in both pre-training and post-training, and we are shipping with known issues" ("spending longer than necessary reasoning through complex tasks, and a tendency to over-verify its own work"). "We'll keep iterating quickly on these." "we would rather ship early and hear what breaks" - [HF model card](https://huggingface.co/tencent/Hy4-preview)
- No statement that the preview is time-limited or that the price will change was found on the card or the OpenRouter page.

### Inferences
- $0.834 x 7.19 CNY/USD = 6.0 and $2.501 x 7.19 = 18.0, so the OpenRouter price is Tencent's CNY list price converted to USD (estimate of the FX rate used).
- DeepInfra (fp4) and the fp8 listings at Novita and SiliconFlow differ from Tencent's own fp8 endpoint in context length and max output, which is consistent with independent self-hosting at a lab-matched price rather than proxying. OpenRouter does not state which is the case.
- Smallest listed node: FP8 (814 GB) fits 8x H200 (1,128 GB) with KV headroom; BF16 (1,560 GB) fits only 8x MI355X (2,304 GB) among the listed nodes. 8x H100 (640 GB) does not hold the FP8 weights (estimate).

### Gaps
- Tencent's TokenHub USD price page was not located; the USD figure comes from an aggregator.
- Layer and expert counts for the FP8 checkpoint were not re-verified against config.json.

---

## 2. tencent/hy3 (Tencent Hunyuan 3)

### Takeaway
Open weights under Apache 2.0 (BF16, 598 GB; FP8 variant published). Supported in stable vLLM (v0.28.0+) and SGLang. OpenRouter hosts price it differently from each other and from Tencent, which is direct evidence of independent self-hosting.

### Cited Findings

**1. Weights**
- Repo `tencent/Hy3`, `gated: false`, created 2026-07-02T13:23:54Z, about 598 GB, BF16 298.8B params, `apache-2.0`, 797,888 downloads - [HF API](https://huggingface.co/api/models/tencent/Hy3)
- Card: Hy3 and Hy3-FP8 weights open-sourced on Hugging Face, ModelScope, GitCode, CNB; follows "the Hy3 Preview launch in late April" - [HF model card](https://huggingface.co/tencent/Hy3)
- Secondary coverage dates the full release to July 6, 2026 and says the April preview license had excluded the EU, UK and South Korea, a restriction dropped in the full release (not read directly) - [Digital Today](https://www.digitaltoday.co.kr/en/view/78623/tencent-hunyuan-releases-hy3-official-apache-2-0-license)
- OpenRouter created timestamp 1783344048 (2026-07-07) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/tencent/hy3/endpoints)

**2. License**
- "Hy3 is released under the **Apache License 2.0**"; metadata `apache-2.0` - [HF model card](https://huggingface.co/tencent/Hy3)
- No MAU, revenue, UI-attribution, or competing-model clauses (Apache 2.0 standard terms).

**3. Architecture and size**
- 295B total (Safetensors 299B), 21B active, MTP layer 3.8B; 192 experts top-8; 80 layers + 1 MTP; hidden 4096; 64 attention heads, 8 KV heads, head dim 128; vocab 120,832; 256K context; "Supported Precisions: BF16" - [HF model card](https://huggingface.co/tencent/Hy3)
- vLLM recipe index memory figures: "BF16 (708G), FP8 (354G), and NVFP4 (214G)" - [vLLM recipes, tencent](https://recipes.vllm.ai/tencent)
- Card hardware note: to serve on 8 GPUs "we recommend using H20-3e or other GPUs with larger memory capacity" - [HF model card](https://huggingface.co/tencent/Hy3)

**4. Serving**
- vLLM supported-models table: "`HYV3ForCausalLM` | HY3 | `tencent/Hy3-preview-Base`, `tencent/Hy3-preview`, `tencent/Hy3`, `tencent/Hy3-FP8` | ✅︎ | ✅︎" - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- vLLM recipe minimum "v0.28.0+" - [vLLM recipes, tencent](https://recipes.vllm.ai/tencent)
- Card vLLM command: `--tensor-parallel-size 8`, `--speculative-config.method mtp`, 2 speculative tokens, `--tool-call-parser hy_v3`, `--reasoning-parser hy_v3`; env `VLLM_FLASHINFER_ALLREDUCE_BACKEND=trtllm` as a fix for an "mnnvl workspace size issue" - [HF model card](https://huggingface.co/tencent/Hy3)
- Card SGLang command: `--tp-size 8`, `--tool-call-parser hunyuan`, `--reasoning-parser hunyuan`, EAGLE speculative (2 steps, 3 draft tokens); requires `transformers>=5.6.0` - [HF model card](https://huggingface.co/tencent/Hy3)

**5. OpenRouter pricing and hosts**
- Five endpoints with different prices: Tencent $0.132 / $0.528 (fp8, with UTC 16:00 to 00:00 override $0.0825 / $0.33), Novita $0.14 / $0.58 (quant unknown), GMICloud $0.14 / $0.58 (bf16), Phala $0.15 / $0.64 (unknown), AtlasCloud $0.20 / $0.80 (fp8) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/tencent/hy3/endpoints)

**6. Preview status**
- Not a preview. The current release is the full model that followed the April preview - [HF model card](https://huggingface.co/tencent/Hy3)

### Inferences
- Prices differ by host and by quantization (bf16 at GMICloud), so hosts other than Tencent are self-hosting, not proxying.
- Smallest listed node: BF16 (598 GB) is 93 percent of 8x H100 (640 GB) and the card recommends larger-memory GPUs for 8-GPU serving, so 8x H200 is the practical BF16 node; FP8 (about 300 GB, estimate from 299B params at 1 byte) fits 8x H100.

### Gaps
- The Hy3-FP8 repo size was not fetched; the FP8 size is an estimate.

---

## 3. stepfun/step-5-preview (StepFun Step 5 Preview)

### Takeaway
Weights went public on 2026-10-15 under the StepFun Model License 1.0, which is Apache-style but requires a separate commercial license for model-as-a-service businesses above US$20M revenue in any 12 months. Serving needs preview Docker images in both vLLM and SGLang (not yet in a stable release). All five OpenRouter hosts charge StepFun's $1.00 / $2.70 list price, but two of them serve fp4, so they self-host at a lab-matched price.

### Cited Findings

**1. Weights**
- Repo `stepfun-ai/Step-5-Preview`, `gated: false`, created 2026-09-20T03:15:06Z, last modified 2026-10-15T01:28:10Z, about 650 GB, safetensors F8_E4M3 564.7B + BF16 39.6B (total 604B), license tag `other`, `license_link` LICENSE.txt; files include `LICENSE.txt`, `LICENSE-CN.txt`, 24 model shards, MTP shards, vision shards - [HF API](https://huggingface.co/api/models/stepfun-ai/Step-5-Preview)
- Sibling repos `stepfun-ai/Step-5-Preview-BF16` (created 2026-09-20) and `stepfun-ai/Step-5-Preview-NVFP4` (created 2026-10-14), both `license:other` - [HF API search](https://huggingface.co/api/models?author=stepfun-ai&search=Step-5&limit=30)
- Card: "Two checkpoints are provided, FP8 and BF16"; "if a checkpoint requires authentication, you should run `hf auth login`" - [HF model card](https://huggingface.co/stepfun-ai/Step-5-Preview)
- Secondary: weights public October 15 after an API launch on September 20 (not read directly) - [Developers Digest](https://www.developersdigest.tech/blog/stepfun-step-5-preview-open-weights-oct-15-2026)
- OpenRouter created 1791462849 (2026-10-08) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/stepfun/step-5-preview/endpoints)

**2. License (StepFun Model License 1.0)**
- Card: "licensed under the StepFun Model License 1.0", "an Apache-2.0-Style license, with additional attribution and commercial-license conditions" - [HF model card](https://huggingface.co/stepfun-ai/Step-5-Preview)
- Grant (Sec. 1): "worldwide, non-exclusive, no-charge, royalty-free license to use, copy, distribute, and sublicense" - [LICENSE.txt](https://huggingface.co/stepfun-ai/Step-5-Preview/raw/main/LICENSE.txt)
- MaaS definition: "giving a third party inference or fine-tuning access to the Model or a Derivative Work"; a commercial license is required when operating a MaaS business if combined revenue "exceeds US$20,000,000" in any consecutive twelve-month period (Sec. 2(c)) - [LICENSE.txt](https://huggingface.co/stepfun-ai/Step-5-Preview/raw/main/LICENSE.txt)
- OEM clause: separate commercial license before "acting as a manufacturer or brand owner of hardware devices" that expose the model - [LICENSE.txt](https://huggingface.co/stepfun-ai/Step-5-Preview/raw/main/LICENSE.txt)
- Attribution: products with "more than 100,000,000 active users or generates revenue exceeding US$20,000,000" in a calendar month must "prominently display \"Powered by StepFun AI\"" (Sec. 2(b)); distributions must "retain all copyright, patent, trademark, and attribution notices" (Sec. 2(a)) - [LICENSE.txt](https://huggingface.co/stepfun-ai/Step-5-Preview/raw/main/LICENSE.txt)
- Termination (Sec. 5): "Any material breach of this License terminates the rights granted to You hereunder", curable within thirty days of notice. No competing-model clause. No governing law stated - [LICENSE.txt](https://huggingface.co/stepfun-ai/Step-5-Preview/raw/main/LICENSE.txt)
- Forkast reported the license "arrived on the HuggingFace repo October 15, 2026" and that an earlier piece (Oct 12) had said no license was yet published (not read directly) - [Forkast](https://forkast.news/?p=132038)

**3. Architecture and size**
- "600B" total (Safetensors 604B), "27B" active, sparse MoE; context "up to 1M tokens, with input and output combined"; input text and image (video mentioned in overview); output text - [HF model card](https://huggingface.co/stepfun-ai/Step-5-Preview)
- FP8 checkpoint: `quantization_config.quant_method = "fp8"`; vision blocks, `lm_head`, embeddings and some expert weights kept in BF16 - [HF API](https://huggingface.co/api/models/stepfun-ai/Step-5-Preview)
- Card deployment configs: FP8 on 4x B300 or 8x H200; BF16 on 8x B300 or 2x8 H200; the BF16 vLLM configs "do not guarantee enough memory for a 1M-token request" - [HF model card](https://huggingface.co/stepfun-ai/Step-5-Preview)
- SGLang cookbook: on H200 "The FP8 weights don't fit on four H200s"; NVFP4 is Blackwell only - [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/StepFun/Step-5-Preview)
- Layer and expert counts: not stated on the card. A secondary source says 92 layers (not read directly) - [tilnote](https://www.tilnote.io/en/pages/6ad3448478ea916627b973f3)

**4. Serving**
- vLLM supported-models table: "`Step5ForConditionalGeneration` | Step-5-Preview | T + I<sup>+</sup> | `stepfun-ai/Step-5-Preview`, etc. | ✅︎ | ✅︎" - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- vLLM recipe uses the dedicated image `vllm/vllm-openai:step-5-preview`; `--reasoning-parser step5`, `--tool-call-parser step5`; TP4 / TEP4 / DEP4 on B300, TP8 / TEP8 / DEP8 on H200; "TP4 uses the default MoE backend because MegaMoE requires expert parallelism"; the NVFP4 checkpoint "mixes NVFP4 and BF16 layers" - [vLLM recipe](https://recipes.vllm.ai/stepfun-ai/Step-5-Preview)
- SGLang cookbook: "Step 5 Preview support has not shipped in an SGLang release yet, so a stock pip install sglang cannot serve it." Image `lmsysorg/sglang:step-5-preview` with FlashInfer patches; `step5` reasoning and tool-call parsers; MTP via `--speculative-algorithm EAGLE --speculative-num-steps 3 ... --enable-multi-layer-eagle`; first launch compiles FlashInfer for about 15 minutes on B300 - [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/StepFun/Step-5-Preview)
- Third-party report: SGLang model-support PR #44356 was still open while cookbook PR #44357 merged; a draft vLLM PR #61727 adds Step-5 support (not read directly) - [OrcaRouter](https://www.orcarouter.ai/vi/blog/step-5-preview-serving-leak)
- Card caveats: "The full BF16 convert.py → generate.py --tp-dir file-shard workflow has not yet been validated end to end"; "Setting --dtype bfloat16 on the FP8 checkpoint does not convert its quantized weights to BF16" - [HF model card](https://huggingface.co/stepfun-ai/Step-5-Preview)
- The StepFun OpenRouter endpoint reports `supports_tool_choice` none/auto/required/function all false - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/stepfun/step-5-preview/endpoints)

**5. OpenRouter pricing and hosts**
- Five endpoints, all prompt $1.00 / completion $2.70: InferenceNet us (fp4, cache $0.05), InferenceNet fp4 (cache $0.05), Featherless (fp4, 262,144 ctx, cache $0.10, 1-day uptime 0), DeepInfra (fp8, cache $0.10), StepFun (fp8, 1,000,000 ctx, cache $0.10) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/stepfun/step-5-preview/endpoints)
- StepFun's own price is $1 per M uncached input and $2.70 per M output on the international platform; the China platform lists 7 CNY input / 20 CNY output (not read directly; StepFun's pricing page returned 404 on two URL variants) - [MindStudio](https://www.mindstudio.ai/blog/step-5-preview-pricing-api/), [Activepieces](https://www.activepieces.com/blog/step-5-api-pricing-cost-per-token-and-per-task-2026), [Artificial Analysis](https://artificialanalysis.ai/models/step-5/providers)

**6. Preview status**
- The model and all repos carry "Preview" in the name. No statement about a time limit, a future non-preview release, or a price change was found on the card, the license, or the OpenRouter page. Card evaluation data is dated "as of September 20, 2026" - [HF model card](https://huggingface.co/stepfun-ai/Step-5-Preview)

### Inferences
- The two fp4 endpoints and the differing cache-read prices ($0.05 vs $0.10) show hosts set their own quantization and cache terms, which points to self-hosting at a price matched to StepFun's list price rather than proxying.
- Smallest listed node: FP8 (650 GB) exceeds 8x H100 (640 GB); 8x H200 (1,128 GB) is the smallest listed node and matches the card's 8x H200 config. NVFP4 (about 325 GB, estimate) would fit 8x H100 by memory but NVFP4 kernels require Blackwell per both recipes.
- For a small US company below $20M in 12-month revenue, a paid API is permitted without a separate agreement; above that threshold a commercial license is required.

### Gaps
- StepFun's official pricing page could not be fetched (404 at `/docs/pricing/details` and `/docs/en/pricing/details`).
- BF16 and NVFP4 repo sizes were not fetched.

---

## 4. xiaomi/mimo-v2.6-flash (Xiaomi MiMo-V2.6-Flash)

### Takeaway
MIT-licensed open weights (178 GB, experts stored in MXFP4), 309B total / 15B active, 1M context, multimodal. Stable vLLM v0.31.0+ loads it; earlier releases cannot. Nine OpenRouter hosts price it between $0.10 and $0.175 input, with Xiaomi's own endpoint at its $0.14 / $0.28 list price, so hosts self-host.

### Cited Findings

**1. Weights**
- Repo `XiaomiMiMo/MiMo-V2.6-Flash-RL`, `gated: false`, created 2026-09-21T15:39:51Z, about 178 GB, safetensors U8 302.8B + BF16 4.1B + F8_E4M3 3.9B (total 310.8B), license `mit`, 98,097 downloads - [HF API](https://huggingface.co/api/models/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- vLLM recipe: "The checkpoint is about 173 GB on disk" - [vLLM recipe](https://recipes.vllm.ai/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- OpenRouter created 1790021264 (2026-09-21) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-flash/endpoints)

**2. License**
- Metadata "License: mit"; no additional clauses on the card - [HF model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- MIT has no revenue, MAU, UI-attribution, or competing-model clauses; paid API permitted (standard license terms).

**3. Architecture and size**
- "309B total / 15B activated parameters"; 256 routed experts, 8 active, no shared experts; 48 layers (39 SWA / 9 GA); hybrid sliding-window (128) and global attention; 1M context; 5-layer SWA MTP drafter that "Predicts 7 subsequent tokens per forward pass" - [HF model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- config.json: `model_type "mimo_v2"`, `num_hidden_layers 48`, `hidden_size 4096`, `n_routed_experts 256`, `num_experts_per_tok 8`, `max_position_embeddings 1048576`, `num_nextn_predict_layers 3`; `quantization_config`: `quant_method "fp8"`, `store_dtype "mxfp4"`, `mxfp4_block_size 32`, `weight_block_size [128,128]`, `o_proj` layers excluded - [config.json](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL/raw/main/config.json)
- vLLM recipe hardware: "4x H200 (TP4), 4x MI355X/MI325X/MI300X (TP4), or equivalent aggregate VRAM (>= 208 GB)" - [vLLM recipe](https://recipes.vllm.ai/XiaomiMiMo/MiMo-V2.6-Flash-RL)

**4. Serving**
- vLLM recipe: "vLLM 0.31.0 is the first stable release that can load the mxfp4-stored weights"; image `vllm/vllm-openai:v0.31.0`; the `mimov25-cu129` tag on the HF card "predates the mxfp4-stored-weight support"; flags `--reasoning-parser mimo`, `--tool-call-parser mimo`, `--enable-auto-tool-choice`; speculative `"method":"dflash"`, 7 tokens, drafter loaded from the local `dflash/` folder; MI300X/MI325X need a post-2026-09-30 nightly or fall back to OCP emulation at about 6.5x lower throughput - [vLLM recipe](https://recipes.vllm.ai/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- Known issue: the RL checkpoint "can get stuck re-issuing the same tool calls in agentic workloads"; the recipe recommends the MOPD checkpoint - [vLLM recipe](https://recipes.vllm.ai/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- HF card: "Stable vLLM may lag"; SGLang command `sglang serve --trust-remote-code --model-path XiaomiMiMo/MiMo-V2.6-Flash-RL --tp 8 --dp 2` with `mimo` reasoning and tool-call parsers and multi-layer EAGLE; image `lmsysorg/sglang:latest` - [HF model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- vLLM supported-models table lists `MiMoV2FlashForCausalLM` (MiMo-V2-Flash) and `MiMoV2ForCausalLM` (MiMo-V2.5-Pro) - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)

**5. OpenRouter pricing and hosts**
- Nine endpoints: Darkbloom $0.10 / $0.28 (fp4), Makora $0.13 / $0.28 (fp8), Relace $0.13 / $0.28 (mxfp4), DeepInfra $0.133 / $0.266 (fp8), Novita $0.14 / $0.28 (fp8), GMICloud $0.14 / $0.28 (bf16), Xiaomi $0.14 / $0.28 (fp8), Io Net $0.15 / $0.29 (fp8), Venice $0.175 / $0.35 (fp8) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-flash/endpoints)
- Xiaomi overseas list price: `mimo-v2.6-flash` real-time $0.14 input (cache miss), $0.0028 cache hit, $0.28 output; batch $0.07 / $0.14; domestic 1 CNY / 2 CNY; "Update Time October 20, 2026" - [Xiaomi MiMo pricing](https://mimo.mi.com/docs/pricing)

**6. Preview status**
- Not a preview. Xiaomi retired MiMo-V2.5-Pro and V2.5 on 2026-10-21 and directs users to V2.6 - [Xiaomi MiMo pricing](https://mimo.mi.com/docs/pricing)

### Inferences
- Price dispersion and the bf16 listing at GMICloud show self-hosting by most hosts; Xiaomi's endpoint is the lab at list price.
- Smallest listed node: 178 GB fits 8x H100 (640 GB) with large headroom; the recipe shows 4 GPUs suffice.
- The HF dtype counts (302.8B U8 elements) do not reconcile with the 178 GB repo size, so the U8 element count should not be used for sizing; the repo size and the recipe's 173 GB figure agree.

### Gaps
- No SGLang cookbook page for MiMo-V2.6 was located (the cookbook has a MiMo-V2-Flash page).

---

## 5. xiaomi/mimo-v2.6-pro (Xiaomi MiMo-V2.6-Pro)

### Takeaway
MIT-licensed open weights (573 GB, MXFP4-stored experts), 1.02T total / 42B active. Same serving stack as Flash (vLLM v0.31.0+). Five OpenRouter hosts price from $0.387 to $0.522 input; Xiaomi's endpoint is at its $0.435 / $0.87 list price; DeepInfra undercuts it.

### Cited Findings

**1. Weights**
- Repo `XiaomiMiMo/MiMo-V2.6-Pro-RL`, `gated: false`, created 2026-09-21T15:39:33Z, about 573 GB, safetensors U8 1,000.2B + F8_E4M3 13.4B + BF16 10.6B (total 1,024B), license `mit` - [HF API](https://huggingface.co/api/models/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- OpenRouter created 1790021259 (2026-09-21) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-pro/endpoints)

**2. License**
- Metadata "License: mit"; no extra clauses - [HF model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)

**3. Architecture and size**
- 1.02T total, 42B active; 384 routed experts, 8 active, no shared; 70 layers (60 SWA / 10 GA); hidden 6144; 128 Q / 8 KV heads; 1M context; 5-layer MTP drafter predicting 7 tokens - [HF model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- config.json: `num_hidden_layers 70`, `hidden_size 6144`, `n_routed_experts 384`, `num_experts_per_tok 8`, `max_position_embeddings 1048576`, `quantization_config` `quant_method "fp8"`, `store_dtype "mxfp4"` - [config.json](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/raw/main/config.json)
- vLLM recipe index: "MiMo-V2.6-Pro-RL | 1T / 42B | FP8 | 680G | v0.31.0+" - [vLLM recipes, XiaomiMiMo](https://recipes.vllm.ai/XiaomiMiMo)
- Card: vLLM `--tensor-parallel-size 8` single node; SGLang advanced command uses TP16 / DP2 / EP16 across `--nnodes 2` - [HF model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)

**4. Serving**
- Card: `vllm serve XiaomiMiMo/MiMo-V2.6-Pro-RL --tensor-parallel-size 8 --trust-remote-code --reasoning-parser mimo --tool-call-parser mimo --enable-auto-tool-choice`; image `vllm/vllm-openai:mimov25-cu129`; SGLang `lmsysorg/sglang:latest` with `mimo` parsers and EAGLE - [HF model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- The Flash recipe's statement that stable vLLM before 0.31.0 cannot load mxfp4-stored weights applies to the same `store_dtype` used here - [vLLM recipe](https://recipes.vllm.ai/XiaomiMiMo/MiMo-V2.6-Flash-RL)

**5. OpenRouter pricing and hosts**
- Five endpoints: DeepInfra $0.387 / $0.783 (fp8), Novita $0.435 / $0.87 (fp8), GMICloud $0.435 / $0.87 (bf16), Xiaomi $0.435 / $0.87 (fp8), StreamLake $0.522 / $1.044 (unknown, 1-day uptime 9.3 percent) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-pro/endpoints)
- Xiaomi overseas list price: `mimo-v2.6-pro` real-time $0.435 input, $0.0036 cache hit, $0.87 output; `mimo-v2.6-pro-ultraspeed` $4.35 / $8.70 - [Xiaomi MiMo pricing](https://mimo.mi.com/docs/pricing)

**6. Preview status**
- Not a preview - [HF model card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)

### Inferences
- DeepInfra's undercut and GMICloud's bf16 listing show self-hosting.
- Smallest listed node: 573 GB is 90 percent of 8x H100 (640 GB), leaving too little for KV cache, so 8x H200 (1,128 GB) is the smallest practical listed node; the recipe's 680 GB figure supports this (estimate).

### Gaps
- The MiMo-V2.6-Pro-RL vLLM recipe page itself was not fetched; version and memory figures come from the org index.

---

## 6. z-ai/glm-5.3 (Z.ai GLM-5.3)

### Takeaway
Open weights (FP8, 756 GB) under a custom "GLM-5.3 License" that is MIT-style except that licensees with over US$10B revenue must pass a Z.ai security review. 48 OpenRouter endpoints with prices from $0.079 to $2.80 input; Z.AI's own endpoint is at its $1.40 / $4.40 list price. Supported by stable vLLM (0.28/0.29+) and SGLang.

### Cited Findings

**1. Weights**
- Repo `zai-org/GLM-5.3`, `gated: false`, created 2026-08-25T06:42:50Z, about 756 GB, safetensors F8_E4M3 751.2B + BF16 2.1B (total 753.3B), `license: other`, `license_name: glm-5.3`, 1,937,342 downloads - [HF API](https://huggingface.co/api/models/zai-org/GLM-5.3)
- GIGAZINE: API and subscription access from August 14; open weights around August 28 to 29 after safety evaluation (not read directly) - [GIGAZINE](https://gigazine.net/gsc_news/en/20260829-glm-5-3-open/)
- OpenRouter created 1787086655 (2026-08-18); endpoint tag `20260816` - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints)

**2. License (GLM-5.3 License)**
- Grant: licensee may "use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software" and "run, deploy, fine-tune, or otherwise modify the Software and create derivative works from it" - [LICENSE](https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE)
- "Model as a Service" means "giving a third party access to language model inference or fine-tuning"; excludes "end-user products with model capabilities solely embedded within specific features" and "mere relaying of requests to models hosted by others" - [LICENSE](https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE)
- Threshold: if "the aggregate revenue of the Licensee and its affiliates exceeds 10 billion US dollars" over any consecutive 12 months, "the Licensee must pass Z.AI's security review before using the Software" commercially - [LICENSE](https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE)
- Notice: the copyright and permission notice "shall be included in all copies or substantial portions of the Software". No competing-model clause, no termination clause, no governing law stated - [LICENSE](https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE)

**3. Architecture and size**
- config.json: `model_type "glm_moe_dsa"`, `GlmMoeDsaForCausalLM`, `num_hidden_layers 78`, `hidden_size 6144`, `n_routed_experts 256`, `num_experts_per_tok 8`, `n_shared_experts 1`, `max_position_embeddings 1048576`, `num_nextn_predict_layers 1`, DSA indexer (`index_n_heads 32`, `index_topk 2048`), `quantization_config` `quant_method "fp8"`, `weight_block_size [128,128]` - [config.json](https://huggingface.co/zai-org/GLM-5.3/raw/main/config.json)
- Active parameter count: not on the HF card. Secondary sources give about 744B total / 40B active and say GLM-5.3 shares GLM-5.2's base (not read directly) - [GIGAZINE](https://gigazine.net/gsc_news/en/20260829-glm-5-3-open/)
- BF16 weights are a separate repo `zai-org/GLM-5.3-BF16` and "need multi-node deployment" - [vLLM recipe](https://recipes.vllm.ai/zai-org/GLM-5.3)
- SGLang: "BF16 (~1.5 TB)" fits single-node only on 8x B300 - [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.3)
- vLLM recipe hardware: "Single-node FP8: 8x H200 or 8x H20 (141 GB each)"; "Full 1M context: 8x B200 (180 GB each), with FP8 KV cache"; AMD MI300X/MI325X/MI350X/MI355X; NVFP4 on Blackwell only - [vLLM recipe](https://recipes.vllm.ai/zai-org/GLM-5.3)

**4. Serving**
- vLLM recipe: badge "vLLM 0.29.0+" but prerequisites say "vLLM 0.28.0 or newer" with `vllm==0.28.0` pinned; flags `--tensor-parallel-size 8 --kv-cache-dtype fp8`, MTP `--speculative-config.method mtp` with 5 tokens, `--tool-call-parser glm47`, `--reasoning-parser glm47`; "DeepGEMM is required" for FP8 performance; thinking always on, default effort "max" - [vLLM recipe](https://recipes.vllm.ai/zai-org/GLM-5.3)
- vLLM supported-models table lists `GlmMoeDsaForCausalLM` with GLM-5, 5.1, 5.2 examples; GLM-5.3 is not named but uses the same `glm_moe_dsa` type - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/), [config.json](https://huggingface.co/zai-org/GLM-5.3/raw/main/config.json)
- SGLang cookbook: `pip install --prerelease=allow sglang` or `lmsysorg/sglang:latest`; H200 TP8 reference; `--reasoning-parser auto` (glm45) and `--tool-call-parser auto` (glm47); MTP via EAGLE 5 steps; "NVFP4 is experimental"; "Zigzag prefill CP (`--cp-strategy zigzag`) is temporarily unavailable for GLM-5.3"; AMD spec-decode draft kernel "not yet validated"; the DFLASH drafter is CC BY-NC-ND 4.0 - [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.3)

**5. OpenRouter pricing and hosts**
- 48 endpoints. Lowest: Wafer $0.079 / $1.40 (fp4), InferenceNet $0.08 / $4.00 (fp4). Z.AI $1.40 / $4.40 (fp8). A large cluster at exactly $1.40 / $4.40: Mistral (nvfp4), BaseTen (fp4), Nebius (fp4), Crusoe (fp4), PrimeIntellect, Venice, Together, Parasail (fp8), Modal, Fireworks, Cloudflare, AtlasCloud (fp8). Highest: Alibaba prime $2.80 / $8.80, Amazon Bedrock $1.68 / $5.28 - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints)
- Z.ai list price: "GLM-5.3 | $1.4 | $0.26 | Limited-time Free | $4.4" (input, cached input, cache write, output per M) - [Z.ai pricing](https://docs.z.ai/guides/overview/pricing)

**6. Preview status**
- Not a preview.

### Inferences
- Hosts that list fp4 / nvfp4 quantizations and undercut Z.ai are self-hosting. The cluster at $1.40 / $4.40 is a mix of self-hosters pegged to list price (quantizations listed) and unknowns.
- Smallest listed node: FP8 (756 GB) fits 8x H200 (1,128 GB), matching the recipe; 8x H100 (640 GB) does not hold the weights.
- For a small US company, a paid API is permitted; the only gate is a security review above $10B revenue.

### Gaps
- Z.ai does not publish the active parameter count on the HF card; the 40B figure is secondary.

---

## 7. z-ai/glm-5.3-flash (Z.ai GLM-5.3-Flash)

### Takeaway
MIT-licensed, natively multimodal, 320B total / 18B active, FP8 weights of about 306 GiB (the HF repo reports 657 GB, likely multiple revisions). vLLM support needs the Docker image until the integration lands in the public repo. 34 OpenRouter hosts price from $0.0052 to $0.225 input; Z.AI's endpoint is at its $0.15 / $0.50 list price.

### Cited Findings

**1. Weights**
- Repo `zai-org/GLM-5.3-Flash`, `gated: false`, created 2026-08-25T06:43:14Z, `usedStorage` about 657 GB, safetensors F8_E4M3 314.4B + BF16 6.9B (total 321.3B), license `mit`, 6,421,899 downloads - [HF API](https://huggingface.co/api/models/zai-org/GLM-5.3-Flash)
- vLLM recipe: "The FP8 weights are about 306 GiB before runtime and KV-cache overhead" - [vLLM recipe](https://recipes.vllm.ai/zai-org/GLM-5.3-Flash)
- Secondary: weights released around August 26 (dates vary from Aug 20 to Aug 26 across sources, not read directly) - [DataNorth](https://datanorth.ai/news/z-ai-releases-glm-5-3-flash), [Epoch AI](https://epoch.ai/models/glm-5-3-flash)
- OpenRouter created 1787752741 (2026-08-27); endpoint tag `20260826` - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints)

**2. License**
- Metadata "License: mit"; no separate clauses - [HF model card](https://huggingface.co/zai-org/GLM-5.3-Flash)

**3. Architecture and size**
- "320B" total, "18B" active; "the first natively multimodal model in the GLM-5 series"; hybrid "sparse and linear attention" - [HF model card](https://huggingface.co/zai-org/GLM-5.3-Flash)
- config.json: `model_type "glm5_next"`, `Glm5NextForConditionalGeneration`, `num_hidden_layers 45` (11 `deepseek_sparse_attention` + 34 `linear_attention` KDA layers), `hidden_size 4096`, `n_routed_experts 288`, `num_experts_per_tok 8`, `n_shared_experts 1`, `max_position_embeddings 1048576`, `num_nextn_predict_layers 1`, vision config present, `quantization_config` `quant_method "fp8"` - [config.json](https://huggingface.co/zai-org/GLM-5.3-Flash/raw/main/config.json)
- vLLM recipe configs: TP4 on one GB200 tray, TP4 on 4x MI355X, TP4 on 4x H200; NVFP4 variant requires Blackwell - [vLLM recipe](https://recipes.vllm.ai/zai-org/GLM-5.3-Flash)

**4. Serving**
- vLLM recipe: "vLLM 0.29.0+"; "use docker before the integration is included in the public repo"; FlashInfer 0.6.17 or newer (troubleshooting says 0.6.18); flags `--tensor-parallel-size 4 --kv-cache-dtype fp8`, MTP 5 tokens, `--tool-call-parser glm47`, `--reasoning-parser glm47`; "Hopper does not support FP8 KV cache for this model and must run BF16 KV"; ROCm MTP needs PR #55239 - [vLLM recipe](https://recipes.vllm.ai/zai-org/GLM-5.3-Flash)
- `Glm5Next` is not in the vLLM supported-models table as of the read - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- HF card: `pip install vllm` then `vllm serve "zai-org/GLM-5.3-Flash"`; SGLang `python3 -m sglang.launch_server --model-path "zai-org/GLM-5.3-Flash"` or `lmsysorg/sglang:latest` - [HF model card](https://huggingface.co/zai-org/GLM-5.3-Flash)

**5. OpenRouter pricing and hosts**
- 34 endpoints. Lowest OpenInference and Relace $0.0052 / $0.1985. Z.AI $0.15 / $0.50 (fp8). Many at $0.15 / $0.50: PrimeIntellect, Modal (nvfp4), BaseTen (fp8), Crusoe (fp4), CoreWeave (nvfp4), AtlasCloud, Fireworks, Friendli, SiliconFlow, Together, Parasail (fp4), Venice, DeepInfra (fp4). Highest Fireworks/us $0.225 / $0.75 - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints)
- Z.ai list price: "GLM-5.3-Flash | $0.15 | $0.03 | Limited-time Free | $0.50" - [Z.ai pricing](https://docs.z.ai/guides/overview/pricing)
- Mistral and Inceptron also host GLM-5.3 (not Flash) for EU in-region routing; Inceptron hosts Flash for EU at $0.18 / $0.69 - [OpenRouter page](https://openrouter.ai/z-ai/glm-5.3-flash)

**6. Preview status**
- Not a preview. It was previewed anonymously as "Ox Alpha" on OpenRouter before launch (not read directly) - [DeepLearning.AI](https://www.deeplearning.ai/the-batch/ox-alpha-revealed-as-glm-5-3-flash)

### Inferences
- The 657 GB `usedStorage` is about double the 306 GiB FP8 footprint; the repo likely holds more than one revision. Use about 330 GB for sizing.
- Smallest listed node: about 330 GB fits 8x H100 (640 GB); the recipe shows 4x H200 suffices.
- Wide price dispersion and listed quantizations show self-hosting.

### Gaps
- Exact release date of the weights is not stated on the HF card.

---

## 8. deepseek/deepseek-v4.1-flash (DeepSeek V4.1 Flash)

### Takeaway
MIT-licensed, 552B backbone with 8B active on prefill and 16B on decode, Causal Encoder-Decoder, mixed FP8/FP4 weights of about 511 GB. vLLM 0.31.0+ serves it (no Jinja template; needs `--tokenizer-mode deepseek_v41`). DeepSeek itself does not sell it on OpenRouter; 38 third-party hosts price it from $0.07 to $0.60 input, with many at DeepSeek's $0.30 / $1.20 peak list price.

### Cited Findings

**1. Weights**
- Repo `deepseek-ai/DeepSeek-V4.1-Flash`, `gated: false`, created 2026-09-10T02:17:58Z, about 510 GB, safetensors I8 557.2B + F8_E4M3 204.0B + BF16 2.0B (total 763.2B), license `mit`, 1,488,213 downloads - [HF API](https://huggingface.co/api/models/deepseek-ai/DeepSeek-V4.1-Flash)
- Later checkpoint `deepseek-ai/DeepSeek-V4.1-Flash-1017` created 2026-10-17, `license:mit` - [HF API search](https://huggingface.co/api/models?author=deepseek-ai&search=V4&limit=30)
- TNW: released Thursday September 10, 2026, weights on Hugging Face - [TNW](https://thenextweb.com/news/deepseek-v4-1-flash-launch-v4-pro-retired-price-cut)
- OpenRouter created 1789021285 (2026-09-10); endpoint tag `20260910` - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints)

**2. License**
- "This repository and the model weights are licensed under the MIT License." - [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

**3. Architecture and size**
- "552B backbone parameters"; "8B parameters per token during prefill" and "16B during decode"; "Causal Encoder-Decoder (CED)"; 40 layers ("a 20-layer causal encoder followed by a 20-layer decoder"); 1 shared + 384 routed experts, 6 routed active; context "up to one million tokens"; input images and text - [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- config.json: `model_type "deepseek_v41"`, `DeepseekV41ForCausalLM`, `num_hidden_layers 40`, `hidden_size 5120`, `n_routed_experts 384`, `num_experts_per_tok 6`, `n_shared_experts 1`, `max_position_embeddings 1048576`, `sliding_window 128`, `quantization_config` `quant_method "fp8"`, `weight_block_size [32,32]`, `expert_dtype "fp4"`; DSpark fields (`dspark_block_size 5`, `num_nextn_predict_layers 3`) - [config.json](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/raw/main/config.json)
- vLLM recipe: "About 511 GB on disk"; `vram_minimum_gb` 614, "which fits one GB200 NVL4 tray (768 GB) at TP4 or one 8×H200 node (1128 GB)"; H200 TP4 with Engram CPU offload; MI300X (192 GB) TP4 with offload, "TP2 does not fit on this SKU" - [vLLM recipe](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash)

**4. Serving**
- vLLM recipe: "Requires vLLM 0.31.0+" (architecture shipped in 0.30.0); defaults to the 1017 checkpoint; `--reasoning-parser deepseek_v41`, `--tool-call-parser deepseek_v41`; "no Jinja template ships with the model. `--tokenizer-mode deepseek_v41` covers this"; "V4.1 dropped MTP. DSpark is the only speculative method" (5-token block, drafter adds about 14B params); the model "does not support `torch.compile`" on AMD; first load slow (`VLLM_ENGINE_READY_TIMEOUT_S=3600`); some B300 latency work depends on PRs #61868 and #61869 "not yet on main" - [vLLM recipe](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash)
- vLLM supported-models table lists `DeepseekV4ForCausalLM`; `DeepseekV41` is not yet in the table - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- HF card: "This release does not include a Jinja-format chat template"; prompt encoding via `encoding.py`; SGLang `python3 -m sglang.launch_server --model-path "deepseek-ai/DeepSeek-V4.1-Flash"` or `lmsysorg/sglang:latest` - [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

**5. OpenRouter pricing and hosts**
- 38 endpoints; no DeepSeek-operated endpoint. Lowest OpenInference $0.07 / $0.50 (fp4), Relace $0.07 / $0.50, Baidu $0.075 / $0.30 (fp8). Many at $0.30 / $1.20: Google Vertex, Nebius (fp8), PrimeIntellect, BaseTen, Together, SiliconFlow (fp8), Modal, Parasail (fp8), Fireworks, Venice (fp8). Highest BaseTen fast $0.60 / $2.40 - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints)
- DeepSeek list price: `deepseek-flash` (DeepSeek-V4.1-Flash-1017) cache hit $0.003 / $0.006, cache miss $0.15 / $0.30, output $0.60 / $1.20 (off-peak / peak); "Peak hours are 01:00 - 04:00 and 06:00 - 10:00 UTC" weekdays - [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)

**6. Preview status**
- Not a preview. The OpenRouter endpoints are tagged with the 2026-09-10 checkpoint while DeepSeek's API now serves the 1017 revision - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints), [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)

### Inferences
- Since DeepSeek has no endpoint on OpenRouter, every host is a self-hoster (or a reseller of another host); the $0.30 / $1.20 cluster equals DeepSeek's peak-hour price.
- Smallest listed node: the recipe's 614 GB minimum VRAM leaves no headroom on 8x H100 (640 GB) and H100 is not a listed config, so 8x H200 (1,128 GB) is the smallest listed node that the recipe supports.
- The HF total of 763B "parameters" counts packed I8 elements and should not be read as a parameter count; the card's 552B backbone is the right figure.

### Gaps
- No SGLang cookbook page for V4.1-Flash was located.

---

## 9. deepseek/deepseek-v4-pro (DeepSeek V4 Pro)

### Takeaway
MIT-licensed, 1.6T total / 49B active, mixed FP4/FP8 weights of about 865 GB (preview) or about 893 GB (0813 release). The HF card calls the April checkpoint "a preview version of DeepSeek-V4 series", and a 0813 version followed. OpenRouter hosts serve the April checkpoint at widely varying prices with no DeepSeek endpoint, so they self-host.

### Cited Findings

**1. Weights**
- Repo `deepseek-ai/DeepSeek-V4-Pro`, `gated: false`, created 2026-04-22T06:04:45Z, about 865 GB, safetensors I8 1,572.8B + F8_E4M3 23.2B + BF16 2.8B (total 1,598.8B), license `mit`, 354,943 downloads - [HF API](https://huggingface.co/api/models/deepseek-ai/DeepSeek-V4-Pro)
- Later repos: `DeepSeek-V4-Pro-0813` (created 2026-08-13, `license:mit`), `DeepSeek-V4-Pro-DSpark` (2026-06-27), `DeepSeek-V4-Pro-Base` - [HF API search](https://huggingface.co/api/models?author=deepseek-ai&search=V4&limit=30)
- OpenRouter created 1777000679 (2026-04-24); all 16 endpoints tagged `20260423`; display name "DeepSeek V4 Pro 0423" - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro/endpoints)

**2. License**
- "This repository and the model weights are licensed under the MIT License." - [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

**3. Architecture and size**
- 1.6T total, 49B active, 1M context; precision "FP4 + FP8 Mixed*" with "MoE expert parameters use FP4 precision; most other parameters use FP8"; hybrid Compressed Sparse Attention and Heavily Compressed Attention; no Jinja chat template (Python `encoding` scripts instead); Think Max needs a context of at least 384K - [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- vLLM recipe: "about 893 GB for the fused 0813 checkpoints and about 865 GB for the preview"; single node on 8x B300 (DP + EP), 8x H200 (DP + EP, "Context is capped at 800K tokens"), 8x MI355X (TP8); "the ~960 GB mixed-precision checkpoint does not fit on one tray" of GB200 NVL4 - [vLLM recipe](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro)

**4. Serving**
- vLLM supported-models table: "`DeepseekV4ForCausalLM` | DeepSeek-V4 | `deepseek-ai/DeepSeek-V4-Flash`, `deepseek-ai/DeepSeek-V4-Pro`, etc." - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- vLLM recipe: baseline "vLLM 0.20.0+"; 0813 and DSpark "require **vLLM 0.25.0**"; `--tokenizer-mode deepseek_v4`, `--reasoning-parser deepseek_v4`, `--tool-call-parser deepseek_v4`; preview uses MTP, 0813 uses DSpark with 7 tokens; "requires `--max-model-len >= 393216` (384K tokens) to avoid truncation" in Think Max; "the 0813 release ships no Jinja chat template" - [vLLM recipe](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro)
- HF card: `vllm serve "deepseek-ai/DeepSeek-V4-Pro"`; SGLang launch_server or `lmsysorg/sglang:latest` - [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

**5. OpenRouter pricing and hosts**
- 16 endpoints, no DeepSeek endpoint: Baidu $0.441 / $0.882 (fp8), StreamLake $0.443 / $0.885 (fp8), Parasail $0.45 / $3.48 (fp8), Relace $0.90 / $1.50 (fp4), GMICloud $0.957 / $1.914 (fp8), DigitalOcean $1.044 / $2.088, Reka $1.05 / $2.10, Cloudflare $1.15 / $2.55, DeepInfra $1.30 / $2.60 (fp8, 16,384 max output), Alibaba $1.416 / $2.832 (fp8), SiliconFlow $1.50 / $3.135 (fp8), Alibaba us-east-1 $1.56 / $3.12, Novita $1.60 / $3.20 (fp8), Venice $1.65 / $3.30, AtlasCloud $1.68 / $3.38 (fp4), Azure $1.91 / $3.83 - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro/endpoints)
- DeepSeek list price for `deepseek-v4-pro` (DeepSeek-V4-Pro-0813): cache hit $0.022 / $0.044, cache miss $0.66 / $1.32, output $1.98 / $3.96 (off-peak / peak) - [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)
- TNW (Sept 2026): "From 04:00 UTC on September 14, every V4-Pro request goes to V4.1-Flash and is billed at Flash rates" until a V4.1-Pro arrives - [TNW](https://thenextweb.com/news/deepseek-v4-1-flash-launch-v4-pro-retired-price-cut); this conflicts with DeepSeek's pricing page read on 2026-10-22, which still lists `deepseek-v4-pro` with its own price and no routing note - [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)

**6. Preview status**
- HF card: the April checkpoint is "a preview version of **DeepSeek-V4** series" - [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- OpenRouter hosts serve the `20260423` preview checkpoint, not the 0813 release - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro/endpoints)

### Inferences
- With no DeepSeek endpoint and prices spanning $0.44 to $1.91 input, all hosts self-host.
- Smallest listed node: 865 GB fits 8x H200 (1,128 GB), as the recipe confirms (with the 800K context cap); 8x H100 (640 GB) does not hold it.

### Gaps
- Whether DeepSeek's first-party V4-Pro endpoint is actually live or redirected to Flash could not be resolved from the two conflicting sources.

---

## 10. moonshotai/kimi-k3 (Moonshot Kimi K3)

### Takeaway
Open weights under the custom "Kimi K3 License" (MIT-style, but model-as-a-service providers with over US$20M revenue in 12 months need a separate agreement, and large products must display "Kimi K3"). Native MXFP4 weights total 1,561 GB, which fits only 8x MI355X among the listed nodes (vendor recipes name 8x GB300 or 8x B300 / MI355X). vLLM support is labeled "Pre-release" and needs a dedicated image. 28 OpenRouter hosts price from $0.24 to $4.50 input; Moonshot's endpoint is at its $3 / $15 list price.

### Cited Findings

**1. Weights**
- Repo `moonshotai/Kimi-K3`, `gated: false`, created 2026-06-13T06:42:57Z, last modified 2026-09-02, about 1,561 GB, safetensors U8 2,722.7B + BF16 57.2B (total 2,779.9B), `license: other`, `license_name: kimi-k3`, 954,778 downloads - [HF API](https://huggingface.co/api/models/moonshotai/Kimi-K3)
- Weights published around July 26 to 27, 2026 as a 1.56 TB download - [RITS](https://rits.shanghai.nyu.edu/ai/kimi-k3-open-weights-ship-2-8t-parameters-1-4-tb-to-run/), [Simon Willison](https://simonwillison.net/2026/Jul/27/kimi-k3/) (not read directly)
- SGLang cookbook: full weights "scheduled to release by July 27, 2026" - [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3)
- OpenRouter created 1784215858 (2026-07-16) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints)

**2. License (Kimi K3 License)**
- Card: "Both the code repository and the model weights are released under the Kimi K3 License." - [HF model card](https://huggingface.co/moonshotai/Kimi-K3)
- Grant: "Permission is hereby granted, free of charge, to any person" ... "to run, deploy, fine-tune, or otherwise modify the Software and create derivative works" - [LICENSE](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE)
- MaaS: "\"Model as a Service\" means giving a third party access to language model" inference or fine-tuning; excludes "(b) mere relaying of requests to models hosted by others" - [LICENSE](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE)
- Threshold: where "the aggregate revenue of the Licensee and its affiliates exceeds 20 million" "US dollars (or the equivalent in other currencies) in total over any consecutive 12 months", "the Licensee must enter into a separate agreement with Moonshot AI" "before using the Software or its derivative works for any commercial purpose." - [LICENSE](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE)
- Attribution: for products with "more than 100 million monthly active users, or more than 20 million US dollars" monthly revenue, "\"Kimi K3\" must be prominently displayed on the user interface of such product or service." - [LICENSE](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE)
- Exemptions: "(a) internal use of the Software" and "any use of the Software accessed through Moonshot AI's official products or certified inference partners." No competing-model clause, no termination clause, no governing law - [LICENSE](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE)
- OpenRouter's own blog notes the license has no SPDX identifier and is not OSI-approved (not read directly) - [OpenRouter blog](https://openrouter.ai/blog/insights/kimi-k3-open-source/)

**3. Architecture and size**
- 2.8T total, 104B activated; 93 layers (1 dense); 896 experts, 16 selected per token, 2 shared; 1,048,576 context; vocab 160K; native weights MXFP4 with MXFP8 activations via quantization-aware training "from the SFT stage onward"; modalities text and image (video in features) - [HF model card](https://huggingface.co/moonshotai/Kimi-K3)
- config.json: `KimiK3ForConditionalGeneration` / `KimiLinearForCausalLM`, `num_hidden_layers 93`, `hidden_size 7168`, `num_experts 896`, `num_experts_per_token 16`, `num_shared_experts 2`, `max_position_embeddings 1048576`, `num_nextn_predict_layers 0`; `quantization_config` `compressed-tensors`, `format "mxfp4-pack-quantized"`, `num_bits 4`, `group_size 32`, attention / shared experts / dense MLP / lm_head / vision excluded - [config.json](https://huggingface.co/moonshotai/Kimi-K3/raw/main/config.json)
- vLLM recipe hardware: "At least 8x GB300. Multi-node for real production traffic."; AMD at least 8x MI355X or MI350X; "1.56 TB of weights from shared storage" - [vLLM recipe](https://recipes.vllm.ai/moonshotai/Kimi-K3)
- SGLang cookbook layouts: B300 1x8 (TP8/DCP8), GB300 2x4, MI350X/MI355X 1x8, B200 2x8, H200 2x8, H100 4x8 (32 GPUs); "H100 has the least post-weight memory headroom (80 GB)" - [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3)

**4. Serving**
- vLLM supported-models table: "`KimiK3ForConditionalGeneration` | Kimi-K3 | T + I<sup>+</sup> | `moonshotai/Kimi-K3` | | ✅︎" - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- vLLM recipe: "vLLM 0.29.0+"; image `vllm/vllm-openai:kimi-k3` ("ships as a CUDA 13 (cu130) build only", needs r580+ driver); profiles labeled "Pre-release"; `--reasoning-parser kimi_k3`, `--tool-call-parser kimi_k3`; DSpark drafter `Inferact/Kimi-K3-DSpark` (4 to 7 tokens); known issue: K3 "occasionally emit a tool-call format its own parser doesn't expect"; DeepGEMM MegaMoE "not compatible with cross-node RDMA"; InferenceX performance figures "have not been reproduced for this recipe" - [vLLM recipe](https://recipes.vllm.ai/moonshotai/Kimi-K3)
- SGLang cookbook: `uv pip install --prerelease=allow sglang` or `lmsysorg/sglang:latest` (NVFP4 needs `lmsysorg/sglang:dev-dev-kimi-k3-nvfp4`); parsers `kimi_k3`; `--speculative-algorithm DSPARK` (7 draft tokens, needs `pp_size == 1`); only the B300 1x8 cells are verified, all others "Final Verification In Progress"; "Accuracy has not been re-measured on any cell"; "VLM input is image-only; video and audio are rejected"; Ascend has no tool calling - [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3)
- Usage: "Kimi K3 always has thinking enabled, and will return `reasoning_content`"; full assistant messages including `reasoning_content` and `tool_calls` must be passed back - [HF model card](https://huggingface.co/moonshotai/Kimi-K3)

**5. OpenRouter pricing and hosts**
- 28 endpoints. Lowest Wafer $0.238 / $16.00 (mxfp4), InferenceNet $0.239 / $11.94 (fp4), Relace $0.30 / $12.00 (fp4). Moonshot AI $3.00 / $15.00 (mxfp4). Others at $3.00 / $15.00: Amazon Bedrock, Parasail (fp4), Modal (mxfp4), Together, Fireworks, BaseTen (fp8). Highest Fireworks us/fast $4.50 / $22.50. Chutes $1.85 / $9.50 (mxfp4), DeepInfra $2.85 / $14.25 (mxfp4) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints)
- Moonshot list price: "kimi-k3 | 1M tokens | $3.00 (cache write 5min) | $6.00 (cache write 1h) | $0.30 (cached input) | $3.00 (input) | $15.00 (output) | 1,048,576 tokens" - [Kimi API pricing](https://platform.kimi.ai/docs/pricing/chat)

**6. Preview status**
- Not a preview.

### Inferences
- Price dispersion and the fp4 / mxfp4 / fp8 listings show self-hosting; Moonshot's endpoint is the lab at list price.
- Smallest listed node: 1,561 GB exceeds 8x B200 (1,440 GB) and 8x MI300X (1,536 GB); only 8x MI355X (2,304 GB) holds it among the listed nodes, consistent with the recipes naming 8x MI355X and 8x B300 / GB300.
- A small US company under $20M in 12-month revenue can sell a paid API without an agreement; above that, a separate agreement with Moonshot is required. The "certified inference partners" exemption suggests Moonshot runs a partner program, but no public terms were found.

### Gaps
- No public list of Moonshot "certified inference partners" was found.

---

## 11. minimax/minimax-m3.1-flash (MiniMax M3.1 Flash)

### Takeaway
Closed as of 2026-10-22. MiniMax said on October 19 that "Model weights will arrive on Oct 23" with no license, size, or format given. There is no Hugging Face repo yet. OpenRouter has a single endpoint, operated by MiniMax, at MiniMax's own $0.15 / $0.60 list price, so OpenRouter is purely a proxy for this model today.

### Cited Findings

**1. Weights**
- The MiniMaxAI Hugging Face org has no M3.1 repo; the newest repos are `MiniMaxAI/MiniMax-Music3` (2026-08-07), `MiniMaxAI/MiniMax-H3` (2026-07-28), `MiniMaxAI/MiniMax-M3` and `MiniMax-M3-MXFP8` (2026-06-02, `license:other`) - [HF API, MiniMaxAI](https://huggingface.co/api/models?author=MiniMaxAI&sort=createdAt&direction=-1&limit=30)
- MiniMax official X post, October 19, 2026: "API pricing (flat rate): $0.15 / $0.60 per 1M input/output tokens, with cache reads at $0.015 / 1M tokens. Model weights will arrive on Oct 23." (quoted in the article) - [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/25582/minimax-m3-1-flash-announced-space-bunny), [X post](https://x.com/MiniMax_AI/status/2112150867868541221)
- The article: "The post gives no license, size or format." - [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/25582/minimax-m3-1-flash-announced-space-bunny)
- OpenRouter created 1792379569 (2026-10-19) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/minimax/minimax-m3.1-flash/endpoints)

**2. License**
- Not found. No license has been published. Precedent: MiniMax-M3 carries a custom `other` license tag - [HF API, MiniMaxAI](https://huggingface.co/api/models?author=MiniMaxAI&sort=createdAt&direction=-1&limit=30)

**3. Architecture and size**
- Not found. MiniMax has not disclosed parameter counts. Context 1,000,000 tokens; input text, image, video; `effort` levels low to max with max default and thinking that cannot be switched off - [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/25582/minimax-m3-1-flash-announced-space-bunny)
- OpenRouter: modality "text+image+video->text", context 1,000,000, max output 524,288, quantization "unknown" - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/minimax/minimax-m3.1-flash/endpoints)

**4. Serving**
- Not applicable until weights exist. For context, vLLM already lists `MiniMaxM3SparseForCausalLM` and `MiniMaxM3SparseForConditionalGeneration` for MiniMax-M3 - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)

**5. OpenRouter pricing and hosts**
- One endpoint: "Minimax | minimax/minimax-m3.1-flash-20261019", prompt $0.15 / completion $0.60 / cache read $0.015 - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/minimax/minimax-m3.1-flash/endpoints)
- MiniMax list price: $0.15 / $0.60, cache reads $0.015, flat rate with no context tiers (per MiniMax's post and pricing page as quoted) - [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/25582/minimax-m3-1-flash-announced-space-bunny)

**6. Preview status**
- Previewed as "Space Bunny Alpha" on OpenRouter from September 23; MiniMax's docs "now lists it without the Preview label"; weights promised for October 23 - [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/25582/minimax-m3-1-flash-announced-space-bunny)
- An aggregator lists open weights as "none" and the model as closed (not read directly) - [eesel](https://www.eesel.ai/de/blog/minimax-m3-1-flash-daten-preise-preview-testen)

### Inferences
- The OpenRouter price equals the lab's price because the only host is the lab; OpenRouter resells MiniMax's API.
- If weights ship on Oct 23 under terms like MiniMax-M3's custom license, serving terms will need a fresh read; nothing can be concluded today.

### Gaps
- No primary MiniMax page (blog or pricing) was fetched; the quotes come from an article reproducing MiniMax's X posts.
- Parameter count, precision, and license are unknown.

---

## 12. nvidia/nemotron-3-ultra-550b-a55b (NVIDIA Nemotron 3 Ultra)

### Takeaway
Open weights under OpenMDW-1.1, a permissive license with no commercial, hosting, or attribution-in-UI conditions ("permission is hereby granted, free of charge, to deal in the Model Materials without restriction"). BF16 checkpoint of about 1.1 TB (NVFP4 about 352 GB). vLLM v0.22.0+ and SGLang v0.5.12.post1 are documented on 8x B200. OpenRouter hosts (DeepInfra, BaseTen, Venice) set their own prices; NVIDIA sells no first-party endpoint there.

### Cited Findings

**1. Weights**
- Repo `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16`, `gated: false`, created 2026-06-03T14:50:04Z, `usedStorage` about 2,242 GB, safetensors BF16 560.5B params, `license: other`, 1,058,710 downloads - [HF API](https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- Card: release date June 4, 2026; NVFP4 variant `NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4` linked - [HF model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- NVFP4 repo safetensors total 352,308,689,576 bytes (about 352 GB) across 113 files - [HF tree API](https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4/tree/main)
- OpenRouter created 1780551208 (2026-06-07); endpoint tag `20260604` - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/nvidia/nemotron-3-ultra-550b-a55b/endpoints)

**2. License (OpenMDW-1.1)**
- Card: "use of this model is governed by the OpenMDW License Agreement, version 1.1 (OpenMDW-1.1)"; "This model is ready for commercial and non-commercial use." - [HF model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- Grant: "permission is hereby granted, free of charge, to deal in the Model Materials without restriction", "including under all copyright, patent, database, and trade secret rights included or embodied therein" - [OpenMDW-1.1 text](https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1)
- Notice: "you shall retain in your distribution (1) a copy of this agreement, and (2) all copyright notices"; outputs: "does not impose any restrictions or obligations with respect to any use, modification, or sharing of any outputs"; termination on patent or copyright litigation ("all rights and grants made to you hereunder are terminated"). No revenue, MAU, UI-attribution, or competing-model clauses - [OpenMDW-1.1 text](https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1)
- The NGC NIM container is separately governed by the NVIDIA Software License Agreement (not read directly) - [NGC](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemotron-3-ultra-550b-a55b)

**3. Architecture and size**
- 550B total, 55B active (Safetensors 561B); "LatentMoE - Mamba-2 + MoE + Attention" with MTP layers; context "Up to 1M tokens"; checkpoint BF16; "pre-trained with an NVFP4 recipe" - [HF model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- vLLM recipe index figures: "BF16 1320G" and "NVFP4 330G" - [vLLM recipes, nvidia](https://recipes.vllm.ai/nvidia)
- Card single-node config: 8x B200, TP8 with expert parallel - [HF model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)

**4. Serving**
- vLLM: recommended container `vllm/vllm-openai:v0.22.0`; recipe "vLLM 0.22.0+"; `--reasoning-parser nemotron_v3`, `--tool-call-parser qwen3_coder`, MTP `{"method":"mtp","num_speculative_tokens":5}`, `--mamba-backend triton`, `--mamba-ssm-cache-dtype float32`, `--kv-cache-dtype fp8`; multi-node via Ray (`ray[cgraph]`); 1M context needs `VLLM_ALLOW_LONG_MAX_MODEL_LEN=1` - [HF model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16), [vLLM recipe](https://recipes.vllm.ai/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- SGLang: tested container `lmsysorg/sglang:v0.5.12.post1` on 8x B200, TP and EP 8, EAGLE 5 steps; tool calls require `"chat_template_kwargs": {"enable_thinking": true, "force_nonempty_content": true}`; 1M context needs `SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1` - [HF model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- TensorRT-LLM: "While support for NVIDIA Hopper systems is planned, it is not currently available." - [HF model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- The vLLM supported-models table lists the `NemotronHForCausalLM` family but does not name Nemotron 3 Ultra - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)

**5. OpenRouter pricing and hosts**
- Five endpoints: DeepInfra flex $0.40 / $1.76 (fp4, 16,384 max output), DeepInfra $0.50 / $2.20 (fp4), BaseTen us $0.60 / $2.40 (fp4, 202,800 ctx), BaseTen $0.60 / $2.40 (fp4), Venice $0.625 / $3.125 (fp8, 256,000 ctx) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/nvidia/nemotron-3-ultra-550b-a55b/endpoints)
- No NVIDIA-operated endpoint appears on OpenRouter - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/nvidia/nemotron-3-ultra-550b-a55b/endpoints)

**6. Preview status**
- Not a preview.

### Inferences
- BF16 size by dtype math is 561B x 2 bytes = about 1,121 GB; the HF `usedStorage` of 2,242 GB is exactly double, so the repo likely stores duplicate shards or revisions. The recipe's 1320G figure includes runtime overhead. Use about 1.1 TB for BF16 (estimate).
- Smallest listed node: BF16 (about 1,121 GB) is 99 percent of 8x H200 (1,128 GB), so 8x B200 (1,440 GB) is the smallest practical listed node, matching the vendor's 8x B200 configs. NVFP4 (352 GB) fits 8x H100 by memory but NVFP4 kernels need Blackwell and the recipe targets B200.
- All three hosts are self-hosters (fp4 and fp8 listed, different prices).

### Gaps
- NVIDIA's own paid API pricing (build.nvidia.com) was not checked.
- Expert and layer counts are not in the visible part of the card.

---

## 13. qwen/qwen3.8-2.4t-a95b (Qwen3.8 2.4T A95B)

### Takeaway
Open weights (BF16, 4,892 GB) under the custom "Qwen3.8-Max License", MIT-style but requiring a separate license for model-as-a-service providers above US$50M revenue in 12 months and UI attribution above 100M MAU or $20M monthly revenue. It is the open-weight, text-only variant of the hosted Qwen3.8-Max. vLLM support requires a nightly build; only 4-bit variants fit on 8 GPUs. All five OpenRouter hosts charge Alibaba's $2 / $6 list price.

### Cited Findings

**1. Weights**
- Repo `Qwen/Qwen3.8-2.4T-A95B`, `gated: false`, created 2026-08-08T01:50:52Z, last modified 2026-08-12, `usedStorage` 4,892,378,458,656 bytes (about 4,892 GB), safetensors BF16 2,446.2B params, `license: other`, `license_name: qwen3.8-max`, 25,398 downloads - [HF API](https://huggingface.co/api/models/Qwen/Qwen3.8-2.4T-A95B)
- OpenRouter description: "the open-weight variant of Qwen3.8 Max, with 95 billion active parameters out of 2.4 trillion total"; created 1786551702 (2026-08-12) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/qwen/qwen3.8-2.4t-a95b/endpoints)

**2. License (Qwen3.8-Max License)**
- Grant: "Permission is hereby granted, free of charge, to any person obtaining a copy of this software" with rights to "use, copy, modify, merge" and to "sell, deploy, host, fine-tune, and create derivative works" - [LICENSE](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE)
- Clause 1 (attribution): products with "more than 100,000,000 monthly active users or US$ 20,000,000 (or equivalent in other currencies) monthly revenue" must ensure the "respective model name must be prominently displayed on the user interface" - [LICENSE](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE)
- Clause 2 (MaaS): "Model as a Service" means "giving a third party access to language model inference or fine-tuning"; providers whose "aggregate revenue of the licensee and its affiliates exceeds US$50,000,000" in any consecutive twelve months "shall obtain a separate license from Qwen before Using the Software" - [LICENSE](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE)
- Notice retention required; no competing-model clause; no termination clause; no governing law stated - [LICENSE](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE)

**3. Architecture and size**
- 2.4T total, 95B active; 92 layers in a hybrid Gated DeltaNet + Gated Attention layout, each followed by MoE; 512 experts with 10 routed + 1 shared active; hidden 8192; context "262,144 natively and extensible up to 1,010,000 tokens"; tensor type BF16; text-only ("Multimodal inputs are not supported, and thinking cannot be disabled"); MTP "trained with multiple steps" - [HF model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- vLLM recipe sizes and GPU counts: BF16 4.45 TiB (24x B300 or 48x H200), FP8 2.27 TiB (16x B300 / 16x MI355X / 32x H200), MXFP4 1.45 TiB (8x MI355X, 16x H200), NVFP4 W4A4 1.32 TiB (8x B300, 16x H200), NVFP4-REAP-25 1.04 TiB (8x B300); "Only NVFP4 (W4A4 or REAP-25) fits on a single 8-GPU node (8×B300). MXFP4 fits one 8×MI355X node."; TP must divide 64 attention heads - [vLLM recipe](https://recipes.vllm.ai/Qwen/Qwen3.8-2.4T-A95B)

**4. Serving**
- vLLM recipe: "vLLM: nightly" ("vnightly+" in the index), "transformers >= 5.4.0"; `--reasoning-parser qwen3`, `--tool-call-parser qwen3_coder`; MTP `{"method":"mtp","num_speculative_tokens":3}` (depth 1 "was measured at 64.8% acceptance" and not worth it); linear backend "is Docker only until FlashInfer version upgrade in the vllm build"; `VLLM_ENGINE_READY_TIMEOUT_S` 3600; 1M context via `--max-model-len 1010000` with `--hf-overrides` - [vLLM recipe](https://recipes.vllm.ai/Qwen/Qwen3.8-2.4T-A95B), [vLLM recipes, Qwen](https://recipes.vllm.ai/Qwen)
- Not in the vLLM supported-models table by name (only `Qwen3NextForCausalLM`) - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- HF card: `vllm serve "Qwen/Qwen3.8-2.4T-A95B"`; SGLang `launch_server` or `lmsysorg/sglang:latest`; compatible with "vLLM, SGLang, and TokenSpeed" - [HF model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

**5. OpenRouter pricing and hosts**
- Five endpoints, all $2.00 / $6.00 with cache read $0.25: Novita (unknown, 1,000,000 ctx), Alibaba (unknown, 1,000,000 ctx, cache write $2.50), SiliconFlow (fp8, 1,048,576 ctx), Venice (unknown, 262,144 ctx, discount 0.2), Together (unknown, 1,010,000 ctx, 909,000 max output) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/qwen/qwen3.8-2.4t-a95b/endpoints)
- Alibaba list price for `qwen3.8-max`: US scope (Virginia) and International (Singapore) $2 input / $0.25 cached / $6 output; Global regions (Frankfurt, Virginia, Tokyo, Hong Kong) and China $1.65 / $0.206 / $4.951; context 1,000,000, max output 131,072; "This page only shows the original pricing for model API calls, excluding any limited-time promotions." The page does not mention the open-weight checkpoint - [Alibaba Cloud Model Studio](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- Secondary: the hosted Qwen3.8-Max is multimodal while the open checkpoint is text-only (not read directly) - [Runtime Wire](https://runtimewire.com/article/alibaba-qwen38-24t-open-weights-enterprise-license)

**6. Preview status**
- Not a preview.

### Inferences
- The uniform $2 / $6 equals Alibaba's US-scope list price for qwen3.8-max. SiliconFlow's fp8 listing (which needs 16 GPUs per the recipe) and Together's 1,010,000 context (the open checkpoint's extended maximum) indicate those two self-host; Novita and Venice cannot be classified from OpenRouter data; Alibaba is the lab.
- Smallest listed node: none of the five listed nodes holds FP8 (about 2,496 GB). NVFP4 (about 1,451 GB) slightly exceeds 8x B200 (1,440 GB) and the recipe names 8x B300. MXFP4 (about 1,594 GB) fits 8x MI355X (2,304 GB). So 8x MI355X with MXFP4 is the only listed node that fits (estimate from recipe sizes).
- A small US company below $50M revenue can sell a paid API without a separate license.

### Gaps
- The hosted qwen3.8-max and the open checkpoint may differ (modality, possibly post-training); Alibaba does not state they are identical.

---

## 14. meta/muse-spark-open (Meta Muse Spark Open)

### Takeaway
Weights are gated ("manual" approval with name, date of birth, and organization) under the custom "Muse Model License", which requires a "Built with Muse Spark Open" notice and a separate agreement for model-as-a-service providers above $20M gross revenue in any 12 months. 816B total / 42B active, BF16 1,644 GB, NVFP4 about 533 GB. vLLM support is via a dedicated image until PR #61879 merges. Meta sells no first-party API; all six OpenRouter hosts self-host and charge an identical $1.25 / $4.25, which equals the price reported for Meta's closed Muse Spark 1.1 API.

### Cited Findings

**1. Weights**
- Repo `meta-models/Muse-Spark-Open-816B-A42B`, `gated: "manual"`, author `meta-models`, created 2026-09-15T19:23:19Z, last modified 2026-10-15, about 1,644 GB, safetensors BF16 821.9B (total 822.0B), `license: other`, `license_name: muse-model-license`, `license_link: LICENSE.md`, tags include `facebook`, `meta` - [HF API](https://huggingface.co/api/models/meta-models/Muse-Spark-Open-816B-A42B)
- NVFP4 repo `meta-models/Muse-Spark-Open-816B-A42B-NVFP4` (created 2026-09-15); third-party quantizations from unsloth, amd, intel-ai, ggml-org, mlx-community, nvidia (DFlash2) - [HF API search](https://huggingface.co/api/models?search=Muse-Spark&limit=30)
- Card: access requires logging in "to review the conditions and access this model content"; form asks for full legal name, date of birth, organization; model attributed to "Meta Superintelligence Labs", "Copyright (c) 2026 Meta Platforms, Inc.", contact museoss@meta.com; release "October 2026" - [HF model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- The raw LICENSE.md returns HTTP 401 without accepting the gate - [LICENSE.md](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B/raw/main/LICENSE)
- OpenRouter created 1792087069 (2026-10-15) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/meta/muse-spark-open/endpoints)

**2. License (Muse Model License, as summarized on the card)**
- Section 2: licensee must "prominently display 'Built with Muse Spark Open'" in the product UI, documentation, website, or settings - [HF model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- Section 3: if a licensee or affiliate offers third parties access to model outputs as a service and aggregate gross revenue exceeds $20 million in any 12-month period, the licensee must notify Meta and sign a separate written agreement before offering it; internal use, research, and features within the licensee's own product are excluded - [HF model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- Section 4: "Meta claims no ownership of outputs generated by the Software" - [HF model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- Secondary coverage agrees: "Built with Muse Spark Open" label required; API hosts above $20M revenue "must notify Meta and sign a separate agreement"; free use, fine-tuning, distillation permitted (not read directly) - [FourWeekMBA](https://fourweekmba.com/ai-meta-opens-816b-muse-spark-but-20m-api-hosts-need-a-deal/)
- One commentator (Nathan Lambert) described the threshold as $20M per month, which conflicts with the 12-month wording on the card (not read directly) - [FourWeekMBA](https://fourweekmba.com/ai-meta-opens-816b-muse-spark-but-20m-api-hosts-need-a-deal/)

**3. Architecture and size**
- 816B total, 42B active; MoE Transformer with a Perception Encoder; 62 layers; 256 experts, 8 active; GQA with 128 Q / 16 KV heads, head dim 64, QK-norm, gated attention; 1M context; vocab 202,048; input text, image, video, audio; "requires a GPU with at least 700GB of VRAM for NVFP4 and 2TB for BF16" - [HF model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- vLLM recipe: NVFP4 "fits one 8-GPU node" at about 533 GB; BF16 about 1.64 TB; Quark MXFP4 about 509 GB, all before KV cache; NVIDIA Blackwell; AMD MI350X / MI355X - [vLLM recipe](https://recipes.vllm.ai/meta-models/Muse-Spark-Open-816B-A42B)

**4. Serving**
- vLLM recipe: "vLLM 0.33.0" or later; "Use Docker image for now until the code is in vLLM main repo"; `--tensor-parallel-size 8 --enable-expert-parallel --max-model-len 1048576 --reasoning-parser muse --tool-call-parser muse --enable-auto-tool-choice`, DSpark drafter `Inferact/Muse-Spark-Open-DSpark` (7 tokens); "The audio track of a video is not processed"; AMD serves text only - [vLLM recipe](https://recipes.vllm.ai/meta-models/Muse-Spark-Open-816B-A42B)
- vLLM blog: model code in PR #61879; images `vllm/vllm-openai:muse-spark-open` and `vllm/vllm-openai-rocm:muse-spark-open`; the model "will only be available at nightly PyPI wheel after the code" is merged, which "usually takes about a week" - [vLLM blog](https://vllm.ai/blog/2026-10-15-muse-spark-open), [PR #61879](https://github.com/vllm-project/vllm/pull/61879)
- Not in the vLLM supported-models table (only `MuseGlimmer` is listed) - [vLLM supported models](https://docs.vllm.ai/en/latest/models/supported_models/)
- HF card: `pip install vllm` then `vllm serve`; SGLang `launch_server` or `lmsysorg/sglang:latest`; `reasoning_effort` low / medium / high / xhigh (default) - [HF model card](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- Secondary: Meta says it runs on SGLang, vLLM, TensorRT-LLM, Transformers, MLX, llama.cpp, Unsloth (not read directly) - [Latenode](https://latenode.com/news/meta-releases-muse-spark-open-weights-with-hosted-api-options)

**5. OpenRouter pricing and hosts**
- Six endpoints, all $1.25 / $4.25 with cache read $0.15: Makora (fp4; `supports_tool_choice` all false), Modal (unknown), Together (unknown), Nebius (fp4), Fireworks (unknown), BaseTen (fp4) - [OpenRouter endpoints](https://openrouter.ai/api/v1/models/meta/muse-spark-open/endpoints)
- Secondary: Meta does not serve Muse Spark Open on its own API; partners host it (not read directly) - [eesel](https://www.eesel.ai/es/blog/meta-muse-spark-open-que-incluye-cuanto-cuesta-y-quien-debe-usarlo)
- Secondary: Meta priced its closed Muse Spark API at $4.25 per million output tokens (not read directly) - [Implicator](https://www.implicator.ai/meta-prices-its-first-paid-ai-model-api-at-4-25-per-million-output-tokens/); Fireworks and Together list $1.25 / $4.25 / $0.15 (not read directly) - [LLM Reference](https://www.llmreference.com/model/muse-spark-open/fireworks-ai)

**6. Preview status**
- Not a preview. Released October 15, 2026; "detailed evaluation report is to follow" per coverage (not read directly) - [aiweekly](https://aiweekly.co/alerts/meta-launches-816b-muse-spark-open-and-closed-wonder-models)

### Inferences
- Because Meta has no API to proxy, all six hosts self-host. The identical $1.25 / $4.25 across hosts is not explained by any source; it equals the reported price of Meta's closed Muse Spark 1.1 API, which suggests launch-partner price alignment (inference).
- Smallest listed node: NVFP4 (533 GB) fits 8x B200 (1,440 GB) and would fit 8x H100 (640 GB) by memory only, but NVFP4 requires Blackwell; BF16 (1,644 GB) fits only 8x MI355X (2,304 GB) among the listed nodes.
- A small US company below $20M gross revenue can sell a paid API without an agreement, but must accept the gate terms and show "Built with Muse Spark Open".

### Gaps
- The full LICENSE.md text is behind the gate; clause quotes above are from the model card's summary and secondary coverage.
- Meta's own blog post was not found (ai.meta.com URL returned 404).

---

## Summary table

Prices are USD per million tokens (input / output). "Paid API OK" is for a small US company below any stated threshold. "GB native" is repo size at the lab's native precision; "est." marks dtype-math estimates. "Smallest node" uses the coordinator's node list; vendor-named nodes are cited in the sections above.

| Model | Weights public | License | Paid API OK | Params total / active | GB at native precision | Smallest 8-GPU node that fits | vLLM / SGLang | OpenRouter hosts self-host or proxy | Caveat |
|---|---|---|---|---|---|---|---|---|---|
| tencent/hy4-preview | Yes (not gated), 2026-08-27 | Apache 2.0 | Yes | 770B / 49B | BF16 1,560; FP8 814 | FP8: 8x H200. BF16: 8x MI355X only | vLLM 0.29+ via `hy4-preview` image, in supported list; SGLang `hy4-preview` image | 4 hosts, all at Tencent's list price $0.834 / $2.501; 3 list own quantization (likely self-host, price-pegged); Tencent endpoint is the lab | "early version", "shipping with known issues" |
| tencent/hy3 | Yes (not gated), 2026-07 | Apache 2.0 | Yes | 295B / 21B | BF16 598; FP8 about 300 (est.) | FP8: 8x H100. BF16: 8x H200 | vLLM 0.28+ stable, supported list; SGLang (transformers>=5.6) | 5 hosts, varied prices, bf16/fp8 mix: self-host | None material |
| stepfun/step-5-preview | Yes (not gated), weights 2026-10-15 | StepFun Model License 1.0 | Conditional (MaaS >$20M / 12 mo needs license; "Powered by StepFun AI" above 100M MAU or $20M/mo) | 600B / 27B | FP8 650; BF16 about 1,210 (est.) | FP8: 8x H200 (card: 8x H200 or 4x B300) | vLLM `step-5-preview` image (in supported list; PR #61727 draft); SGLang "has not shipped in an SGLang release yet", `step-5-preview` image | 5 hosts, all at StepFun's $1.00 / $2.70; two serve fp4 (self-host, price-pegged); StepFun endpoint is the lab | Preview name; no time-limit statement found |
| xiaomi/mimo-v2.6-flash | Yes (not gated), 2026-09-21 | MIT | Yes | 309B / 15B | 178 (MXFP4-stored experts) | 8x H100 (4x H200 suffices) | vLLM 0.31.0+ stable (first release to load mxfp4 store); SGLang per card | 9 hosts, $0.10 to $0.175 input: self-host; Xiaomi endpoint at list $0.14 / $0.28 | RL checkpoint can loop tool calls; MOPD recommended |
| xiaomi/mimo-v2.6-pro | Yes (not gated), 2026-09-21 | MIT | Yes | 1.02T / 42B | 573 (MXFP4-stored experts) | 8x H200 | vLLM 0.31.0+; SGLang per card | 5 hosts, $0.387 to $0.522 input: self-host; Xiaomi at list $0.435 / $0.87 | Pro recipe page not read |
| z-ai/glm-5.3 | Yes (not gated), 2026-08-25 | GLM-5.3 License (MIT-style) | Yes (security review only above $10B revenue) | 753B / about 40B (secondary) | FP8 756; BF16 about 1,500 (separate repo) | FP8: 8x H200 (recipe) | vLLM 0.28/0.29+ stable (`glm_moe_dsa`); SGLang cookbook | 48 hosts, $0.079 to $2.80 input: self-host; Z.AI at list $1.40 / $4.40 | Active count not on card |
| z-ai/glm-5.3-flash | Yes (not gated), 2026-08-25 | MIT | Yes | 320B / 18B | FP8 about 330 (recipe 306 GiB; HF reports 657) | 8x H100 (4x H200 suffices) | vLLM 0.29+ "use docker before the integration is included in the public repo"; SGLang per card | 34 hosts, $0.0052 to $0.225 input: self-host; Z.AI at list $0.15 / $0.50 | Hopper cannot use FP8 KV cache |
| deepseek/deepseek-v4.1-flash | Yes (not gated), 2026-09-10; 1017 revision 2026-10-17 | MIT | Yes | 552B / 8B prefill, 16B decode | FP8+FP4 mixed 510 | 8x H200 (recipe min VRAM 614 GB) | vLLM 0.31.0+ (arch in 0.30.0), no Jinja template, DSpark only; SGLang per card | 38 hosts, no DeepSeek endpoint, $0.07 to $0.60 input: self-host; DeepSeek list $0.15 / $0.60 off-peak, $0.30 / $1.20 peak | OpenRouter serves 0910 checkpoint; lab serves 1017 |
| deepseek/deepseek-v4-pro | Yes (not gated), 2026-04-22 preview; 0813 release | MIT | Yes | 1.6T / 49B | FP4+FP8 mixed 865 (0813 about 893) | 8x H200 (recipe, 800K context cap) | vLLM 0.20+ (0813 needs 0.25+), supported list; SGLang per card | 16 hosts, no DeepSeek endpoint, $0.44 to $1.91 input: self-host; DeepSeek list $0.66 / $1.98 off-peak | Card calls April checkpoint "a preview version"; hosts serve it; TNW says lab routes V4-Pro to Flash (conflicts with pricing page) |
| moonshotai/kimi-k3 | Yes (not gated), weights ~2026-07-27 | Kimi K3 License (MIT-style) | Conditional (MaaS >$20M / 12 mo needs agreement; "Kimi K3" display above 100M MAU or $20M/mo) | 2.8T / 104B | MXFP4 1,561 | 8x MI355X only (recipes: 8x GB300/B300 or 8x MI355X) | vLLM 0.29+ via `kimi-k3` image, "Pre-release"; SGLang only B300 1x8 verified | 28 hosts, $0.24 to $4.50 input: self-host; Moonshot at list $3 / $15 | Tool-call format sometimes breaks own parser |
| minimax/minimax-m3.1-flash | No (closed); weights promised 2026-10-23 | Not found | No (closed) | Not found | Not found | Not applicable | Not applicable | 1 host (MiniMax) at MiniMax's list $0.15 / $0.60: proxy | License, size, format undisclosed |
| nvidia/nemotron-3-ultra-550b-a55b | Yes (not gated), 2026-06-04 | OpenMDW-1.1 | Yes | 550B / 55B | BF16 about 1,121 (est.; HF reports 2,242); NVFP4 352 | BF16: 8x B200 (card). NVFP4: Blackwell required | vLLM 0.22.0+ (v0.22.0 container); SGLang v0.5.12.post1 on 8x B200 | 3 hosts (DeepInfra fp4, BaseTen fp4, Venice fp8), varied prices: self-host; no NVIDIA endpoint | TRT-LLM Hopper support "not currently available" |
| qwen/qwen3.8-2.4t-a95b | Yes (not gated), 2026-08-12 | Qwen3.8-Max License (MIT-style) | Conditional (MaaS >$50M / 12 mo needs license; name display above 100M MAU or $20M/mo) | 2.4T / 95B | BF16 4,892; FP8 about 2,496; NVFP4 about 1,451; MXFP4 about 1,594 | 8x MI355X with MXFP4 only (NVFP4 needs 8x B300 per recipe) | vLLM nightly only; SGLang per card | 5 hosts, all at Alibaba's US list $2 / $6; SiliconFlow (fp8) and Together (1.01M ctx) look self-hosted; Alibaba is the lab | Text-only; thinking cannot be disabled; hosted Max may differ |
| meta/muse-spark-open | Yes but gated (manual approval), 2026-10-15 | Muse Model License | Conditional (MaaS >$20M gross / 12 mo needs agreement; "Built with Muse Spark Open" required) | 816B / 42B | BF16 1,644; NVFP4 about 533 | NVFP4: 8x B200 (Blackwell). BF16: 8x MI355X only | vLLM 0.33+ via `muse-spark-open` image until PR #61879 merges; SGLang per card | 6 hosts, all $1.25 / $4.25 (= Meta's closed API price); Meta has no API, so all self-host | Full license text behind gate; video audio track not processed |
