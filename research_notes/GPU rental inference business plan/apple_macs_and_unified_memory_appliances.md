# Apple Macs and unified-memory appliances as a cheap way to serve open-weight LLMs as a paid API (late 2026)

All URLs below were read live on 2026-10-22 ("checked 2026-10-22"). Source dates are the dates printed on the page. Numbers labelled "estimate" are my arithmetic and are shown with the inputs. "Not found" means I looked and did not find a sourced number. Web search budget ran out near the end; a few items are marked "not found (search budget exhausted)".

Key facts up front:

- Apple no longer sells the M3 Ultra or M4 Max Mac Studio. The current lineup is M5 Max ($2,499 start) and M5 Ultra ($5,499 start, up to 512 GB, 1.2 TB/s). The 512 GB M5 Ultra config was due "late October" and its price was still unannounced in every source I could read.
- Best measured batched numbers on a 512 GB M3 Ultra (oMLX community benchmarks, March to April 2026): gpt-oss-120b 68 tok/s single, 187 tok/s aggregate at batch 8; DeepSeek V3.2 4-bit 19.3 tok/s single, 26.4 tok/s at batch 2; Kimi K2.6 3.3-bit 21 tok/s single, 41 tok/s at batch 4; Qwen3 235B 4-bit 28 tok/s single, 61 tok/s at batch 4. Nobody has published batch 16 or 32 numbers for these models on a Mac Studio.
- Prefill is the weak point: 85 to 690 tok/s on M3 Ultra depending on model, so an 8k-token prompt to DeepSeek takes about 48 s to first token on one M3 Ultra. Apple says M5 Ultra prefill is up to 4.6x faster.
- An H100 at $2.50/hr serving gpt-oss-120b with vLLM produces about 9,000 tok/s per GPU (SemiAnalysis InferenceX), which is roughly $0.08 per million output tokens. A 512 GB M3 Ultra owned over 3 years lands near $0.86 per million for the same model (estimate). The Mac loses by about 10x on gpt-oss-120b. On DeepSeek-class MoE at low per-user speed the gap narrows (Mac about $4.6 to $6.1 per million vs H100 about $6 to $9 per million at 30 to 50 tok/s per user), but the Mac cannot meet an 8k-prompt TTFT target.
- Cheapest hosted big-memory Mac with no contract: MacWeb (Silicon Valley) lists M3 Ultra 256 GB at $799/mo and M5 Ultra 256 GB at $1,500/mo, "No contract required", but both were out of stock or "coming soon" and I could not find its acceptable-use policy. No host offers a 512 GB Mac Studio. AWS mac-m3ultra.metal (256 GB) is $12.50/hr with a 24-hour minimum.

## 1. Hardware and prices today (Apple lineup as of 2026-10-22, memory, bandwidth)

### Takeaway
Apple's current Mac Studio is M5 Max (36 to 128 GB, 460 or 614 GB/s) and M5 Ultra (96, 256, 512 GB, 1.2 TB/s). M3 Ultra and M4 Max are discontinued; the 512 GB M3 Ultra is only available used or from resellers at about $9.7k and up. The 512 GB M5 Ultra price is not yet published.

### Cited Findings
- Apple's Mac Studio store page shows three stock configs: M5 Max 18c CPU/40c GPU 64 GB 1 TB; M5 Max 18c/32c 36 GB 512 GB SSD; M5 Ultra 30c/64c 96 GB 1 TB. No M3 Ultra or M4 Max listed. Prices did not render (JS). Page meta: "Get a new Mac Studio desktop with M5 Max or M5 Ultra from only $208.25 per month." (page template dated Oct 14 2026; checked 2026-10-22) [Apple Store](https://www.apple.com/shop/buy-mac/mac-studio)
- Apple spec page: M5 Max memory 36 GB base, configurable 48/64/128 GB; bandwidth "460GB/s" base and "614GB/s" with the 40-core GPU. M5 Ultra memory 96 GB base, configurable 256 or 512 GB; bandwidth "1.2TB/s"; GPU 64-core base, 80-core option; Thunderbolt 5 "up to 120Gb/s"; "Maximum continuous power 480W" (system). (checked 2026-10-22) [Apple Mac Studio specs](https://www.apple.com/mac-studio/specs/)
- Apple press release (reprinted): "Mac Studio with M5 Max starts at $2,499, or $2,299 with education pricing." "Mac Studio with M5 Ultra starts at $5,499, or $5,099 for education." "Preorders are open today in 30 countries and regions, with deliveries and retail availability beginning September 22." "The 512GB configuration will become available in late October." M5 Ultra "provides 1.2TB/s of memory bandwidth, 50% more than M3 Ultra" and "4.3 times the peak AI compute performance of Mac Studio with M3 Ultra." (Aug 25 2026; checked 2026-10-22) [iClarified](https://www.iclarified.com/101883/apple-launches-mac-studio-with-m5-max-and-m5-ultra-starting-at-2499)
- Macworld: M5 Ultra starts $5,499; "the most expensive M5 Ultra you can get now, with 256GB of RAM and 16TB of storage, costs $18,299"; a fully loaded model "won't be available until October" and will cost "well over 20 grand"; the new models replace the M4 Max and M3 Ultra options; M5 Ultra costs $1,500 more than the M3 Ultra did at its March 2025 launch. (Aug 25 2026; checked 2026-10-22) [Macworld](https://macworld.com/article/3220024/apple-announces-the-m5-ultra-mac-studio-with-up-to-512gb-of-ram.html)
- Pinggy (secondary): M5 Ultra "Starting price: $5,499 (96GB). The 256GB build is $9,499." 512 GB "unpriced and ships in late October 2026." M3 Ultra bandwidth 819 GB/s; M5 Ultra 1.2 TB/s ("about 1.46x"). (Sep 1 2026; checked 2026-10-22) [Pinggy](https://pinggy.io/blog/self_hosting_llms_on_512gb_m5_ultra_mac_studio/)
- Implicator (secondary): M5 Ultra "$200 above the M3 Ultra's most recent price and $1,500 above its March 2025 launch", implying M3 Ultra base was about $5,299 just before discontinuation and $3,999 at launch. (Aug 2026; checked 2026-10-22) [Implicator](https://www.implicator.ai/apple-mac-studio-m5-ultra-prompt-processing.md)
- M3 Ultra 512 GB street price: Small Dog listed a new, factory-sealed M3 Ultra 32c CPU, 512 GB, 4 TB SSD at $9,689.99 (sale, regular $10,499.99), sold out; eBay sealed 512 GB/8 TB unit at about $27,999.99. (checked 2026-10-22, via search snippets) [Small Dog](https://smalldog.com/collections/mac-studio-1), [eBay](https://www.ebay.com/shop/mac-studio-m3-ultra-512-gb-ram)
- Jeff Geerling's cluster bill of materials gives Apple's pre-discontinuation prices: M3 Ultra 512 GB / 8 TB at $11,699 each; 256 GB / 4 TB at $8,099 each. (Dec 18 2025; checked 2026-10-22) [Jeff Geerling](https://jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5)
- An Australian reseller states "512GB unified memory is no longer available from Apple, likely due to recent increases in memory costs." (checked 2026-10-22) [Macfixit AU](https://www.macfixit.com.au/products/brand-new-open-box-mac-studio-m3-ultra-32c-cpu-80c-gpu-512gb-ram-2tb-ssd)
- Apple refurbished store listed no Mac Studio units at all on 2026-10-22. [Apple Refurbished](https://www.apple.com/shop/refurbished/mac/mac-studio)
- Mac mini: Apple's spec page now lists only M6 (16 to 32 GB, 153 or 170 GB/s) and M5 Pro (24 to 64 GB, 307 GB/s). The M4 Pro mini is discontinued. (checked 2026-10-22) [Apple Mac mini specs](https://www.apple.com/mac-mini/specs/). "Mac mini with M6 starts at $899 in the U.S., while the M5 Pro version starts at $1,699"; available September 22. (updated Sep 3 2026; checked 2026-10-22) [iGeeksBlog](https://www.igeeksblog.com/mac-mini-m6-m5-pro-price-specs-release-date/). Third-party price trackers list M5 Pro 15c/16c 64 GB 512 GB at $2,699 and 18c/20c 64 GB 1 TB at $3,199 (secondary, via search snippets; checked 2026-10-22) [refurb.me](https://www.refurb.me/stats/mac-mini/mac-mini-m5-pro-late-2026)
- Memory bandwidth per chip from the llama.cpp Apple-silicon table: M2 Ultra 800 GB/s; M3 Ultra 800 (Apple says 819); M4 Pro 273; M4 Max 410 (32-core GPU) or 546 (40-core); M5 Pro 307; M5 Max 614; M5 Ultra 1,228 GB/s. (table updated Aug 25 2026; checked 2026-10-22) [llama.cpp discussion #4167](https://github.com/ggml-org/llama.cpp/discussions/4167)
- Power (Apple support, "Published Date: September 21, 2026"): Mac Studio M5 Ultra idle 9 W, max 385 W; M5 Max idle 7 W, max 200 W; M3 Ultra (2025) idle 9 W, max 270 W; M4 Max (2025) idle 6 W, max 145 W; M2 Ultra idle 10 W, max 295 W. (checked 2026-10-22) [Apple support 102027](https://support.apple.com/en-us/102027)
- Apple MLX blog: "peak power consumption is about 200W for the Mac Studio with M3 Ultra, and 300W for the Mac Studio with M5 Ultra" during LLM inference at 65,536-token context. (Oct 15 2026; checked 2026-10-22) [Apple ML Research](https://machinelearning.apple.com/research/mlx-distributed-inference)

### Inferences
- The user's 0.3 kW planning figure is close to Apple's measured 300 W peak for M5 Ultra and generous for M3 Ultra (about 200 W peak under inference).
- Planning placeholder for M5 Ultra 512 GB (estimate): $13,499 = $9,499 (256 GB build) + $4,000, assuming the 256 to 512 GB step costs the same as the 96 to 256 GB step ($5,499 to $9,499). This is an assumption, not a price.

### Gaps
- M5 Ultra 512 GB price: not found (unannounced in every source read; Apple's configurator did not render prices).
- M5 Max 128 GB Mac Studio retail price: not found (only base $2,499; search budget exhausted before I could price the 128 GB tier).
- Mac Studio M4 Max 128 GB new price today: not found (discontinued; no live retail listing read).
- Mac mini M4 Pro 64 GB: discontinued; no live price. Successor M5 Pro 64 GB price ($2,699) is from third-party trackers, not apple.com.

## 2. Measured LLM throughput on Macs (batch 1, batch 8+, prefill)

### Takeaway
On a 512 GB M3 Ultra the measured numbers are: gpt-oss-120b 68 tok/s single and 187 tok/s aggregate at batch 8 (2.7x); DeepSeek V3.2 4-bit 19.3 tok/s single and 26.4 at batch 2; Kimi K2.6 3.3-bit 21 single and 41 at batch 4; Qwen3 235B 4-bit 28 single and 61 at batch 4. Prefill is 85 to 690 tok/s. No one has published batch 16 or 32 results for these models on a Mac Studio, and no independent M5 Ultra numbers exist for these models yet.

### Cited Findings
gpt-oss-120b
- oMLX community benchmark, M3 Ultra 80-core, 512 GB, gpt-oss-120b-MXFP4-Q8, oMLX v0.2.6, macOS 15.5, dated 2026-03-08: PP/TG by context: 1k 613.2 / 68.4 tok/s; 4k 685.5 / 64.1; 8k 687.8 / 57.8; 16k 663.6 / 47.5 (TTFT 24,691 ms); 32k 600.7 / 35.2. Peak memory 59.2 to 60.4 GB. Batching: 1x 68.4; 2x 105.7 (1.55x); 4x 145.9 (2.13x); 8x 187.1 (2.74x) aggregate tok/s. (checked 2026-10-22) [oMLX wjn65xp9](https://omlx.ai/benchmarks/wjn65xp9)
- A second oMLX run (v0.2.7) reached 187.6 tok/s at 8x (search snippet; checked 2026-10-22) [oMLX benchmarks](https://omlx.ai/benchmarks?page=5140)

DeepSeek V3 / V3.2 / R1
- oMLX, M3 Ultra 80c 512 GB, DeepSeek-V3.2 4-bit, oMLX v0.2.9, macOS 26.3.1, dated 2026-03-12: 1k ctx PP 209.8 / TG 19.3 tok/s, TTFT 4,880 ms; 4k 201.0 / 15.8; 8k 169.7 / 15.1; 16k 128.0 / 14.1; 32k 84.0 / 12.8 (TTFT 390,223 ms). Peak memory 354 to 382 GB. Batching: 1x 19.3; 2x 26.4 (1.37x). No larger batch listed. (checked 2026-10-22) [oMLX 47hp35d3](https://omlx.ai/benchmarks/47hp35d3), [oMLX pw2zbs9w](https://omlx.ai/benchmarks/pw2zbs9w)
- DeepSeek-V3-0324 4-bit, MLX, M3 Ultra (r/LocalLLaMA, Mar 25 2025): 69-token prompt 58.1 tok/s prompt, 21.05 tok/s generation, peak memory 380 GB; 15,777-token prompt: 69.45 tok/s prompt (227 s), generation 5.79 tok/s, peak memory 466 GB. (checked 2026-10-22, via Implicator summary and search snippets; the Reddit mirror refused the connection) [Implicator](https://www.implicator.ai/apple-mac-studio-m5-ultra-prompt-processing.md), [r/LocalLLaMA mirror](https://cal1.lr.ggtyler.dev/r/LocalLLaMA/comments/1jj6i4m/deepseek_v3)
- DeepSeek R1 671B Q4 MLX on M3 Ultra 512 GB (r/LocalLLaMA, Mar 2025): 18.43 tok/s short prompt; 13,140-token prompt at 59.56 tok/s prompt, 6.39 tok/s generation, peak memory 491 GB; 16k context went out of memory; "70 second wait to first token." (checked 2026-10-22, search snippet) [r/LocalLLaMA mirror](https://redlib.ssps.io/r/LocalLLaMA/s/kj0MKbLnAJ)
- "In July 2026, a rented 512GB M3 Ultra held a 351.7GiB four-bit DeepSeek R1 build entirely in memory and generated 20.3 tokens per second." (secondary; checked 2026-10-22) [Pinggy](https://pinggy.io/blog/self_hosting_llms_on_512gb_m5_ultra_mac_studio/)
- kunalganglani benchmark table: M3 Ultra 512 GB, DeepSeek-V3 671B Q4_K_M, MLX, 17 tok/s generation, marked measured; Llama 3.1 405B Q4_K_M 4 tok/s. No batch or prefill data. (undated; checked 2026-10-22) [kunalganglani](https://kunalganglani.com/llm-benchmarks)
- Hugging Face model card for a DeepSeek V3.1 5.5-bit MLX quant: expect "~13-19 tokens/s on a 512GB M3 Ultra" (search snippet; checked 2026-10-22) [inferencerlabs](https://huggingface.co/inferencerlabs/deepseek-v3.1-MLX-5.5bit/blob/ec2d08509e6f5053ca3b04099381f7bd3e03ef1d/README.md)

Kimi K2
- oMLX, M3 Ultra 80c 512 GB, "Kimi-K2.6 3.3bit", oMLX v0.3.7rc1, macOS 15.7.4, dated 2026-04-25: 1k ctx PP 213.1 / TG 21.2 tok/s, TTFT 4,805 ms, peak memory 399.3 GB; 4k PP 243.6 / TG 20.5. Batching: 1x 21.2; 2x 30.1 (1.42x); 4x 40.9 (1.93x). (checked 2026-10-22) [oMLX mb6beh2t](https://omlx.ai/benchmarks/mb6beh2t)
- Other oMLX Kimi runs on M3 Ultra 512 GB (DQ3_K_M-q8): about 20 to 22 tok/s short context, 13.6 tok/s at 32k; peak memory about 400 to 460 GB (search snippet; checked 2026-10-22) [oMLX yj9s0ome](https://omlx.ai/benchmarks/yj9s0ome)
- Kimi K2 Thinking at native int4 is "600+ GB" and does not fit one 512 GB Mac; it ran at "around 30 tokens per second" on four M3 Ultra Studios (Geerling, Dec 18 2025; checked 2026-10-22) [Jeff Geerling](https://jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5). Hardware Corner lists it as "Kimi K2 Thinking 1T A32B (4-bit MLX, 658 GB)" and "Cannot run on one node" (Dec 19 2025; checked 2026-10-22) [Hardware Corner](https://www.hardware-corner.net/mac-rdma-over-thunderbolt-llm/)

Qwen3 235B
- oMLX, M3 Ultra 80c 512 GB, Qwen3-235B-A22B 4-bit, oMLX v0.2.9, macOS 26.2, dated 2026-03-13: 1k ctx PP 372.7 / TG 28.1 tok/s, TTFT 2,748 ms, peak memory 124.0 GB; 4k PP 390.3 / TG 24.3. Batching: 1x 28.1; 2x 45.4 (1.62x); 4x 61.4 (2.19x). (checked 2026-10-22) [oMLX dn0dqucy](https://omlx.ai/benchmarks/dn0dqucy)
- Qwen3 235B 8-bit MLX is 242 GB (Hardware Corner, Dec 19 2025; checked 2026-10-22) [Hardware Corner](https://www.hardware-corner.net/mac-rdma-over-thunderbolt-llm/). 8-bit tok/s on one M3 Ultra: not found.

Llama 3.3 70B and Qwen3 32B (dense)
- kunalganglani: M3 Ultra 256 GB, Llama 3.1 70B Q8_0, MLX, 11 tok/s (measured); M4 Max 128 GB Llama 3.3 70B Q4_K_M MLX 11 tok/s (measured); M5 Max 128 GB Llama 3.3 70B Q4_K_M 13 tok/s (reference, not measured); H100 80GB Llama 3.3 70B fp16 vLLM 55 tok/s single. (checked 2026-10-22) [kunalganglani](https://kunalganglani.com/llm-benchmarks)
- Pinggy summary of an MLX benchmark set on M3 Ultra 512 GB: Llama 3.3 70B 4-bit prefill 103 to 150 tok/s, generation 6.5 to 15.5 tok/s; Qwen 32B 4-bit at 1K context prefill about 345 tok/s, generation 31.2 tok/s; at 128K context prefill about 154 tok/s, generation 8.5 tok/s; Mixtral 8x7B 4-bit 68.4 tok/s; GLM-5.2 (743B MoE) 4-bit prefill 213.6 / generation 17.7 tok/s (from oMLX). (Sep 1 2026; secondary; checked 2026-10-22) [Pinggy](https://pinggy.io/blog/self_hosting_llms_on_512gb_m5_ultra_mac_studio/)
- llama.cpp Apple-silicon table (Llama 2 7B, PP batch 512, TG batch 1): M3 Ultra 80-core Q4_0 PP 1,471 / TG 92.1 tok/s; M4 Max 40-core Q4_0 PP 886 / TG 83.1; M5 Max 40-core Q4_0 PP 3,220 / TG 119.9; M5 Ultra 80-core Q4_0 PP 4,945 / TG 179.1, F16 PP 5,207 / TG 73.6; M5 Pro 20-core Q4_0 PP 1,621 / TG 66.3. (updated Aug 25 2026; checked 2026-10-22) [llama.cpp discussion #4167](https://github.com/ggml-org/llama.cpp/discussions/4167)

M5 Ultra (Apple's own measurements, batch 1, mlx_lm.benchmark)
- Apple, Oct 15 2026: M5 Ultra decode is "1.6x faster tokens/s" than M3 Ultra and TTFT "up to 4.6x faster". Table 3 decode (tok/s, 128 generated tokens; the page shows one tab of values, which by the TTFT arithmetic is the 8,192-token context): Qwen 3.8 27B BF16: M3 Ultra 12.46, M5 Ultra 19.69, 2x M5 pipeline 19.44, 2x M5 tensor 33.27, 4x M5 tensor 50.89. Mistral Medium 3.5 128B FP8: M3 Ultra 4.95, M5 Ultra 7.70, 2x pipeline 7.70, 2x tensor 13.69, 4x tensor 23.37. Muse Spark Open 816B-A42B NVFP4 (about 493 GB, does not fit one machine): 2x pipeline 15.74, 2x tensor 24.99, 4x tensor 36.73. Table 2 TTFT (s): Qwen 3.8: M3 Ultra 18.2, M5 Ultra 4.1, 2x tensor 3.1, 4x tensor 1.7; Mistral 128B: M3 Ultra 95.9, M5 Ultra 24.6, 2x tensor 14.4, 4x tensor 7.5; Muse Spark Open: 2x pipeline 8.4, 2x tensor 8.2, 4x tensor 4.8. At 65,536 context on four M5 Ultras, two Thunderbolt cables per link cut Muse Spark TTFT from about 50.5 s to 40.6 s. (checked 2026-10-22) [Apple ML Research](https://machinelearning.apple.com/research/mlx-distributed-inference)
- Apple press release: M5 Ultra has "4.3 times the peak AI compute performance" of M3 Ultra (Aug 25 2026; checked 2026-10-22) [iClarified](https://www.iclarified.com/101883/apple-launches-mac-studio-with-m5-max-and-m5-ultra-starting-at-2499)

Batching software on Apple silicon
- vllm-mlx paper (arXiv 2601.19139, Jan 27 2026, M4 Max): "21% to 87% higher throughput than llama.cpp", "continuous batching that scales to 4.3x aggregate throughput at 16 concurrent requests", peak "up to 525 tokens per second on text models". Qwen3-0.6B scaled from 441 tok/s single to 1,642 tok/s at 16 concurrent (3.7x); "larger models show diminishing returns due to memory bandwidth saturation." (checked 2026-10-22) [arXiv](https://arxiv.org/abs/2601.19139v1)
- vLLM project announced vllm-metal ("Concurrent Serving on Apple Silicon") on Sep 22 2026, tested on M5 Pro 64 GB and older chips with 4-bit Qwen3.8-27B, Gemma 4 E4B, Qwen3.6-35B-A3B. It reports relative gains and batch wall times (8 requests, Qwen3.6-35B-A3B: vllm-metal 3.87 s vs mlx_lm 4.52 s vs llama.cpp 5.29 s vs oMLX 7.32 s) but no absolute aggregate tok/s and no Mac Studio run. (checked 2026-10-22) [vLLM blog](https://vllm.ai/blog/2026-09-22-vllm-metal-v0-28-0)
- A Level1Techs thread (Aug to Sep 2026) asking for real multi-user M3 Ultra measurements got none; one poster's bandwidth-formula estimate was 296 tok/s aggregate for a 120B-class MoE (not measured). (checked 2026-10-22) [Level1Techs](https://forum.level1techs.com/t/sanity-check-on-my-math-dgx-spark-vs-2x-radeon-pro-r9700-vs-mac-studio-m3-ultra-for-multi-user-office-llm-serving-does-reality-match-the-numbers/253436)

Power under inference
- TechRadar headline: M3 Ultra ran DeepSeek R1 671B "entirely in memory using less than 200W" (article body did not load; headline only; checked 2026-10-22) [TechRadar](https://www.techradar.com/pro/apple-mac-studio-m3-ultra-workstation-can-run-deepseek-r1-671b-ai-model-entirely-in-memory-using-less-than-200w-reviewer-finds)

### Inferences
- Batch scaling on M3 Ultra flattens fast: gpt-oss-120b gains 2.74x at batch 8; the big MoE models gain 1.4x at batch 2 and about 2x at batch 4. Extrapolating to batch 16 or 32 is unsupported by any published measurement; I would not plan above about 3x single-stream for MoE on one Mac.
- Estimate for M5 Ultra on the same models (Apple's 1.6x decode multiplier applied to the oMLX M3 Ultra numbers): gpt-oss-120b about 109 tok/s single and about 300 tok/s at batch 8; DeepSeek V3.2 4-bit about 31 tok/s single and about 42 at batch 2; Kimi K2.6 3.3-bit about 34 single, 65 at batch 4; Qwen3 235B 4-bit about 45 single, 98 at batch 4. These are estimates.
- Prefill TTFT estimates (single request, from oMLX PP rates): gpt-oss-120b on M3 Ultra: 1k prompt about 1.6 s, 8k about 11.6 s (8,192 / 688). DeepSeek V3.2: 1k about 4.9 s (measured TTFT 4,880 ms), 8k about 48 s (8,192 / 170). Kimi K2.6: 8k about 34 s. Qwen3 235B: 8k about 21 s. With Apple's "up to 4.6x" M5 Ultra prefill claim, DeepSeek 8k would be about 10 s and gpt-oss-120b 8k about 2.5 s (estimates).

### Gaps
- Aggregate tok/s at 16 or 32 concurrent requests for any of the target models on any Mac Studio: not found. The largest published batch is 8 (gpt-oss-120b) and 4 (Kimi, Qwen3 235B), 2 (DeepSeek).
- DeepSeek V3/R1 batch 4 or 8 on M3 Ultra: not found.
- Independent M5 Ultra measurements of DeepSeek, Kimi, GLM, Qwen3 235B, gpt-oss-120b: not found (Apple's blog covers Qwen 3.8 27B, Mistral Medium 3.5 128B, Muse Spark Open 816B only).
- Llama 3.3 70B 8-bit and Qwen3 32B on M3 Ultra with batching: not found. The 70B 4-bit figures come from a secondary summary.
- GLM-4.6 / GLM-5 on Mac: only the secondary GLM-5.2 figure (17.7 tok/s, 213.6 PP) via Pinggy; primary oMLX page not read (search budget exhausted).

## 3. Clustering Mac Studios (exo, MLX distributed, llama.cpp RPC over Thunderbolt 5)

### Takeaway
RDMA over Thunderbolt 5 (macOS 26.2, MLX jaccl backend, exo) makes tensor-parallel clustering scale: four M3 Ultras ran DeepSeek V3.1 at 32.5 tok/s (vs 21.1 on one), Kimi K2 Thinking at 25 to 30 tok/s, and Apple's four M5 Ultras ran an 816B MoE at 36.7 tok/s. llama.cpp RPC over TCP gets slower as nodes are added. Clustering buys capacity and about 1.5x to 2.6x decode, not throughput per dollar.

### Cited Findings
- Jeff Geerling, four M3 Ultra Studios (2x 512 GB at $11,699, 2x 256 GB at $8,099; "just shy of $40,000"; 1.5 TB total), Thunderbolt 5, macOS 26.2 RDMA: Qwen3 235B on exo "hitting 32 tokens per second on the full cluster"; Kimi K2 Thinking "around 30 tokens per second"; llama.cpp RPC "scales but is inefficient, with performance decreasing as nodes are added"; exo is the only tool with RDMA; only four Macs supported so far; "under 250 watts"; RDMA must be enabled from recovery (rdma_ctl enable); prerelease software; HPL without RDMA crashed the Macs. (Dec 18 2025; checked 2026-10-22) [Jeff Geerling](https://jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5)
- Per-node figures from Geerling's charts as reported by IT之家: DeepSeek V3.1 exo RDMA 21.1 tok/s on 1 node to 32.5 on 4 nodes (+54%); llama.cpp without RDMA 14.6 tok/s on 4 nodes (exo +122.6%); Qwen3 235B exo RDMA 31.9 on 4 nodes vs llama.cpp 15.2; Kimi K2 Thinking 28.3 tok/s on 4 nodes. (Dec 23 2025; checked 2026-10-22) [IT之家](https://www.ithome.com/0/907/113.htm). A search snippet attributed 27.8 tok/s to the 2-node DeepSeek V3.1 run (secondary, not verified on a page).
- Hardware Corner (Dec 19 2025): Qwen3 235B A22B 8-bit MLX is 242 GB; DeepSeek V3.1 4-bit MLX 378 GB; Kimi K2 Thinking 4-bit MLX 658 GB "Cannot run on one node"; at 4 nodes exo RDMA is "roughly double the throughput of the TCP setup"; tests "done by Jeff Geerling". (checked 2026-10-22) [Hardware Corner](https://www.hardware-corner.net/mac-rdma-over-thunderbolt-llm/)
- Creative Strategies (Max Weinbach), same 4-node M3 Ultra setup, exo, Kimi K2 Thinking native int4: "about 25 tok/s with RDMA", author estimate "about 5 tok/s" over plain Thunderbolt networking, TTFT "roughly 2000ms", "under 450W peak", cluster "$39,596 before tax"; author estimates a B200 node would deliver about 50x the throughput at about 50x the power; no batch numbers. (Dec 18 2025; checked 2026-10-22) [Creative Strategies](https://creativestrategies.com/research/running-a-1t-parameter-model-on-a-40k-mac-studio-cluster/)
- Apple MLX distributed (Oct 15 2026): MLX v0.30.1+ jaccl backend on the macOS 26.2 RDMA driver; two cables per link; four M5 Ultras in a Thunderbolt mesh. Muse Spark Open 816B NVFP4: 2x pipeline 15.74 tok/s, 2x tensor 24.99, 4x tensor 36.73 ("over 36 tokens per second"); TTFT at 8k context 8.4 / 8.2 / 4.8 s. Dense Qwen 3.8 27B: 1 M5 Ultra 19.69, 2x tensor 33.27, 4x tensor 50.89 tok/s. Pipeline parallel "leaves decode speed essentially unchanged" and gives up to about 1.8x prefill at 65k context. "Dense architectures scale better across multiple computers." All at batch size 1. (checked 2026-10-22) [Apple ML Research](https://machinelearning.apple.com/research/mlx-distributed-inference)
- exo + DGX Spark + M3 Ultra heterogeneous split (prefill on Spark, decode on Mac), Llama 3.1 8B FP16, 8,192-token prompt: Spark prefill 1.47 s / decode 2.87 s; M3 Ultra prefill 5.57 s / decode 0.85 s; combined 2.32 s total, 2.8x vs Mac alone. (undated; checked 2026-10-22) [EXO Labs](https://blog.exolabs.net/nvidia-dgx-spark/)

### Inferences
- Four M3 Ultras (about $40k) give about 1.5x the DeepSeek decode of one 512 GB Mac (32.5 vs 21.1 tok/s) for about 4x the money, so clustering only makes sense when the model does not fit (Kimi K2 at 4-bit, Muse Spark Open).
- Apple's four-M5-Ultra tensor-parallel scaling on a dense 27B model (2.6x on 4 nodes) is better than on MoE (Muse Spark 2.3x over the 2-node pipeline baseline). Communication is still the limit at 65k contexts (40 s TTFT on four M5 Ultras).
- For an API operator, N independent Macs each serving a model that fits (DeepSeek 4-bit on a 512 GB box) will beat one N-node cluster on aggregate throughput, because cluster scaling is sub-linear and all measurements are batch 1.

### Gaps
- Batched (multi-request) throughput on any Mac cluster: not found (all cluster numbers are batch 1).
- 2-node and 3-node numbers for Kimi K2 and Qwen3 235B on M3 Ultra: only in Geerling's charts (not in text); IT之家 reports only 1 and 4 nodes.
- Official exo documentation page with benchmark tables: not read (search budget exhausted).

## 4. Hosted or colocated Macs (price, minimum term, inference-API terms)

### Takeaway
No hosting provider offers a 512 GB Mac Studio. The biggest hosted Macs are 256 GB M3 Ultra / M5 Ultra at MacWeb ($799 and $1,500 per month, no contract, out of stock or coming soon) and AWS mac-m3ultra.metal (256 GB, $12.50/hr, 24-hour minimum). MacStadium's AUP bars making the service "available to any third party" except "as part of a SaaS offering to your Users", which an inference API plausibly qualifies for but is not explicitly addressed. Hetzner lists no Macs.

### Cited Findings
- MacStadium pricing page (USD, monthly, "monthly or annual pricing options", prepaid first of month): Mac mini M4.S M4 16 GB $149; M4.M M4 24 GB $249; M4.L M4 Pro 12-core 48 GB 1 TB $349; Mac Studio S1.M M1 Max 64 GB $249; S2.M M2 Ultra 64 GB $369; S2.L M2 Ultra 128 GB 2 TB $449. No M3 Ultra, M4 Max or M5 plans; no colocation pricing; no setup fee or minimum term stated; mentions upcoming M5/M6 minis. (checked 2026-10-22) [MacStadium pricing](https://www.macstadium.com/pricing)
- MacStadium Acceptable Use Policy (undated; "may be revised at any time"): prohibited to "License, sell, rent, lease, transfer, assign, distribute, display, host, disclose," "permit timesharing, or otherwise commercially exploit or make the Services, or related materials, available to any third party" "other than as part of a SaaS offering to your Users". Also prohibits "Mine bitcoins and other cryptocurrencies", "Managing a proxy server on MacStadium's network", and "deliberate attempts to overload the MacStadium network". (checked 2026-10-22) [MacStadium AUP](https://docs.macstadium.com/macstadium/legal-and-compliance/acceptable-use-policy). The Master Subscription Services Agreement is v.2.0, Sept 26 2025. [MacStadium MSSA](https://docs.macstadium.com/macstadium/legal-and-compliance/master-services-agreement)
- MacStadium colocation page describes cloud "Mac Cloud Compute" with Mac minis ("MacStadium has minis available today"); no colocation price, term, or Mac Studio support stated. (checked 2026-10-22) [MacStadium colocation](https://www.macstadium.com/colocation)
- MacWeb (Silicon Valley), Cloud Mac Studio, all with 10 Gbps port, "No contract required", "Cancel at any time": Power M5 Max 128 GB (614 GB/s) 2 TB $800/mo (Coming Soon); Ultimate M5 Ultra 256 GB (1.2 TB/s) 4 TB $1,500/mo (Coming Soon); Ultimate M4 Max 128 GB 2 TB $599/mo (Out of Stock); Power M3 Ultra 256 GB (819 GB/s) 2 TB $799/mo (Out of Stock); Power M2 Ultra 64 GB $399; Ultimate M2 Ultra 128 GB $499. No 512 GB option. No AUP language on the page. (checked 2026-10-22) [MacWeb Mac Studio](https://macweb.com/macstudio). MacWeb colocation: customers ship "Apple systems" to its "Prime Silicon Valley location", "10 G and 100 G connections"; price by quote only. (checked 2026-10-22) [MacWeb colocation](https://macweb.com/colocation). MacWeb terms pages returned 404 at /terms and /terms-of-service. (checked 2026-10-22)
- Scaleway Apple silicon (EUR, before tax, per month / per hour): M4-S Mac mini M4 16 GB €149 / €0.22; M4-M M4 32 GB 1 TB €199 / €0.29; M4-XL Mac mini M4 Pro 64 GB 2 TB €335 / €0.49; M2-L M2 Pro 16 GB €139 / €0.21; private network 10 Gbps add-on €19.99/mo. No Mac Studio. (checked 2026-10-22) [Scaleway pricing](https://www.scaleway.com/en/pricing/apple-silicon/). "Due to license constraints, the minimum lease for Apple silicon-as-a-Service is 24 hours." Linux and Windows not supported on the M4 mini. (checked 2026-10-22) [Scaleway Mac mini M4](https://www.scaleway.com/en/mac-mini-m4/)
- AWS EC2 Mac: instance types mac-m3ultra.metal (M3 Ultra, 256 GB), mac-m4max.metal (M4 Max, 128 GB), mac-m4pro.metal (48 GB), mac-m4.metal (24 GB), mac2-m2pro.metal (32 GB), mac2-m1ultra.metal (128 GB). Sold as Dedicated Hosts; billed "per second with a 24-hour minimum allocation period to comply with the Apple macOS Software License Agreement"; up to 44% off with a 3-year commitment. No prices on the page. (checked 2026-10-22) [AWS EC2 Mac](https://aws.amazon.com/ec2/instance-types/mac/). Vantage lists mac-m3ultra.metal on-demand at $12.500/hr (28 vCPU, 256 GiB) and mac-m4max.metal at $6.250/hr (16 vCPU, 128 GiB); no reserved prices shown. (checked 2026-10-22) [Vantage mac-m3ultra](https://instances.vantage.sh/aws/ec2/mac-m3ultra.metal), [Vantage mac-m4max](https://instances.vantage.sh/aws/ec2/mac-m4max.metal). aws-pricing.com shows N/A for mac-m3ultra in us-east-1 and us-west-2. [aws-pricing.com](https://aws-pricing.com/mac-m3ultra.metal.html)
- Flow Swiss Mac bare metal (CHF, excl. VAT; "24-hour minimum allocation period"; billing continues while switched off): studio.m4-max 16-core 128 GB 2 TB CHF 1.34/hr, CHF 979/mo; macmini.m5-pro 18-core 64 GB 2 TB CHF 1.02/hr, CHF 749/mo; macmini.m4-pro 14-core 48 GB CHF 0.82/hr, CHF 599/mo. No M3 Ultra or M5 Ultra. (checked 2026-10-22) [Flow Swiss pricing](https://doc.flow.swiss/platform/pricing/mac-bare-metal)
- OakHost (hosted in Germany, HQ Estonia; EUR excl. VAT per month): Mac M4Pro.L M4 Pro 64 GB 1 TB €260 (Out of Stock); Mac M5Pro.L M5 Pro 64 GB 1 TB €340 (Coming Soon); Mac M6.S 16 GB €120; no Mac Studio; minimum term and setup fee not stated; 14-day money-back. (checked 2026-10-22) [OakHost](https://www.oakhost.com/mac-mini-hosting)
- HostMyApple: "Mac VPS Cloud Hosting" from $24.99/mo; dedicated M6 Mac minis 16/32 GB "now in stock"; no prices for dedicated plans; no Mac Studio. (checked 2026-10-22) [HostMyApple](https://www.hostmyapple.com/)
- Hetzner: the dedicated-server page lists AX, EX, GPU, SX and DX lines only; no Apple hardware. (checked 2026-10-22) [Hetzner](https://www.hetzner.com/dedicated-rootserver/matrix-apple/)
- Mac Mini Vault (CyberLynk, US): colocation "from $29/mo", "purchase or rent a mini from us, or send yours in"; Enterprise plan $49.99/mo with 1 Gbps port (dated promo pages). Mac mini M4 Pro 64 GB 1 TB rental $274.99/mo. (search snippets; checked 2026-10-22) [Mac Mini Vault colo](https://www.cyberlynk.net/datacenter-services/speciality-services/mac-mini-colocation), [Mac Mini Vault dedicated](https://www.macminivault.com/dedicated-mac-mini/)
- Macfixit Australia rents an M3 Ultra 256 GB 2 TB Mac Studio at $1,000/month with a 3-month minimum (currency not stated, AU site). (checked 2026-10-22) [Macfixit AU](https://www.macfixit.com.au/products/brand-new-mac-studio-m3-ultra-28c-cpu-60c-gpu-256gb-ram-2tb-storage)

### Inferences
- Cheapest hosted Mac that can hold gpt-oss-120b (63 GB) or Qwen3 235B 4-bit (124 GB): MacWeb M4 Max 128 GB at $599/mo ($0.82/hr) or Flow Swiss M4 Max 128 GB at CHF 979/mo; both show 546 GB/s. For DeepSeek 4-bit (354 to 382 GB peak) no hosted Mac exists; you must own.
- MacWeb's M5 Ultra 256 GB at $1,500/mo is $2.05/hr (1,500 / 730), under the H100 rental rate, but it serves a 256 GB ceiling and the throughput in section 5.
- MacStadium's "SaaS offering to your Users" carve-out is the only explicit permission language found; an OpenRouter-style public API is a SaaS offering to your own paying users, but a written confirmation from the host would be prudent. AWS and Scaleway state no inference-specific restriction, only the 24-hour minimum from Apple's macOS license.

### Gaps
- MacWeb acceptable-use / terms text: not found (404 on two URLs; search budget exhausted).
- Scaleway and AWS terms clauses on resale/public APIs: not found on the pages read.
- Any host offering a 512 GB Mac Studio: not found.
- Current MacStadium colocation price for customer-owned Mac Studios: not found (quote only).

## 5. Economics: cost per hour and cost per million output tokens, Mac vs H100 (estimates with arithmetic)

### Takeaway
At 100% utilisation a 512 GB M3 Ultra owned for 3 years costs about $0.58/hr and produces gpt-oss-120b at about $0.86 per million output tokens (batch 8), versus about $0.08 per million on a $2.50/hr H100 running vLLM. For DeepSeek-class MoE the Mac is about $4.6 to $6.1 per million versus $6 to $9 per million for an H100 held to 30 to 50 tok/s per user, so the Mac is competitive only in that narrow low-concurrency regime, and only if the buyer tolerates 5 to 48 s time to first token. Macs do not compete at scale.

### Cited Findings (inputs)
- H100 gpt-oss-120b (InferenceX, vLLM, fp4, 8k in / 1k out, runs Mar 27 to May 17 2026): per-user target 50 tok/s gives 8,973 tok/s per GPU ($0.036 per 1M at $1.17/GPU-hr; $0.062 at $2.00/GPU-hr retail); 75 tok/s 7,136; 100 tok/s 5,863; 150 tok/s 3,931; 200 tok/s 2,558; peak 10,284 tok/s per GPU. (checked 2026-10-22) [InferenceX gpt-oss-120b H100](https://inferencex.semianalysis.com/run/gptoss-120b-on-h100)
- H100 DeepSeek R1 (InferenceX, Dynamo SGLang, fp8, 8k in / 1k out, runs Feb 8 to 13 2026): 30 tok/s per user gives 116 tok/s per GPU ($2.81 per 1M at $1.17/hr); 50 tok/s 74.2 ($4.38; $7.49 at $2.00/hr); 75 tok/s 49.5 ($6.57); 100 tok/s 25.7 ($12.64); peak 1,376 tok/s per GPU. (checked 2026-10-22) [InferenceX DeepSeek R1 H100](https://inferencex.semianalysis.com/run/deepseek-r1-on-h100)
- H100 Llama 3.3 70B (InferenceX, vLLM, FP8, 8k in / 1k out, Oct 29 2025): 30 tok/s per user 2,056 tok/s per GPU ($0.16 per 1M at $1.17/hr); 50 tok/s 1,496 ($0.22; $0.37 at $2.00/hr); 75 tok/s 923; peak 2,568. (checked 2026-10-22) [InferenceX Llama 3.3 70B H100](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h100)
- H100 rental, "last checked on October 10, 2026": Vast.ai about $1.68 (marketplace); RunPod H100 PCIe Community $1.99, Secure $2.89; Lambda 8x H100 SXM $3.99, 1x SXM $4.29, 1x PCIe $3.29; Nebius $4.50 (from Oct 1 2026); AWS p5.48xlarge $6.88 per H100-hr ($8.60 N. California); Azure $6.98 (1 GPU). (checked 2026-10-22) [IntuitionLabs](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison). Hivenet (Oct 13 2026): Lambda H100 PCIe $3.29/hr, SXM $4.29/hr; Modal H100 SXM5 about $3.95/hr. (checked 2026-10-22) [Hivenet](https://www.hivenet.com/post/nvidia-h100-pricing)
- OpenRouter lists DeepSeek V3 ("deepseek-chat") endpoints; page not read for price (budget). [OpenRouter](https://openrouter.ai/models/deepseek/deepseek-chat)
- Mac inputs: see sections 1, 2 and 4. Power and internet assumptions are the user's ($0.25/kWh, 0.3 kW) plus an internet assumption of $100/mo (Comcast Business gigabit was listed at $229.99/mo undated and plans "starting at $60 per month" in March 2026; not Bay Area specific). (checked 2026-10-22) [business.com](https://www.business.com/reviews/xfinity), [ThePricer](https://www.thepricer.org/how-much-does-business-internet-cost/)

### Inferences (all estimates; arithmetic shown; 8,760 hr/yr; 100% utilisation; power 0.3 kW x $0.25 = $0.075/hr; internet $1,200/yr = $0.137/hr)

Cost per hour, owned:

| Machine | Price used | 3-yr hardware/hr | 3-yr total/hr | 5-yr hardware/hr | 5-yr total/hr |
|---|---|---|---|---|---|
| M3 Ultra 512 GB (sealed reseller) | $9,690 | 9,690 / 26,280 = $0.369 | $0.581 | 9,690 / 43,800 = $0.221 | $0.433 |
| M5 Ultra 256 GB | $9,499 | $0.361 | $0.573 | $0.217 | $0.429 |
| M5 Ultra 512 GB (placeholder, estimate) | $13,499 | $0.514 | $0.726 | $0.308 | $0.520 |
| DGX Spark 128 GB | $4,699 | $0.179 | $0.391 | $0.107 | $0.319 |
| Framework Desktop 128 GB | $3,449 | $0.131 | $0.343 | $0.079 | $0.291 |
| H100 rented | $2.50/hr | n/a | $2.50 | n/a | $2.50 |

Cost per million output tokens (owned, 3-yr / 5-yr), using the highest published aggregate batch result for each:

| Machine, model, batch | Aggregate tok/s | M tok/hr | 3-yr $/M | 5-yr $/M |
|---|---|---|---|---|
| M3 Ultra 512 GB, gpt-oss-120b, batch 8 | 187.1 (measured) | 0.674 | 0.581 / 0.674 = $0.86 | $0.64 |
| M3 Ultra 512 GB, DeepSeek V3.2 4-bit, batch 2 | 26.4 (measured) | 0.095 | $6.11 | $4.56 |
| M3 Ultra 512 GB, Kimi K2.6 3.3-bit, batch 4 | 40.9 (measured) | 0.147 | $3.95 | $2.94 |
| M3 Ultra 512 GB, Qwen3 235B 4-bit, batch 4 | 61.4 (measured) | 0.221 | $2.63 | $1.96 |
| M3 Ultra 256 GB, Llama 70B Q8, batch 1 | 11 (measured) | 0.040 | $14.7 | $10.9 |
| M5 Ultra 256 GB, gpt-oss-120b, batch 8 | 299 (estimate = 187.1 x 1.6) | 1.077 | $0.53 | $0.40 |
| M5 Ultra 512 GB, gpt-oss-120b, batch 8 | 299 (estimate) | 1.077 | $0.67 | $0.48 |
| M5 Ultra 512 GB, DeepSeek 4-bit, batch 2 | 42 (estimate = 26.4 x 1.6) | 0.152 | $4.80 | $3.44 |
| DGX Spark, gpt-oss-120b, vLLM 8 concurrent | 153 (measured, upper of 116 to 153) | 0.551 | $0.71 | $0.58 |
| Framework Desktop, gpt-oss-120b, single stream | 53.4 (measured) | 0.192 | $1.79 | $1.51 |
| H100 $2.50/hr, gpt-oss-120b, 50 tok/s per user | 8,973 (measured) | 32.3 | $0.077 | same |
| H100 $2.50/hr, gpt-oss-120b, 200 tok/s per user | 2,558 (measured) | 9.21 | $0.27 | same |
| H100 $2.50/hr, DeepSeek R1 fp8, 30 tok/s per user | 116 per GPU (measured) | 0.418 | $5.99 | same |
| H100 $2.50/hr, DeepSeek R1 fp8, 50 tok/s per user | 74.2 per GPU (measured) | 0.267 | $9.36 | same |
| H100 $2.50/hr, Llama 3.3 70B FP8, 50 tok/s per user | 1,496 (measured) | 5.39 | $0.46 | same |

Hosted Mac cost per million (estimate): MacWeb M3 Ultra 256 GB $799/mo = $1.09/hr; gpt-oss-120b at 187 tok/s = $1.62/M. MacWeb M5 Ultra 256 GB $1,500/mo = $2.05/hr; at the estimated 299 tok/s = $1.90/M. AWS mac-m3ultra.metal $12.50/hr at 187 tok/s = $18.6/M.

- Where the Mac loses: any mid-size model (gpt-oss-120b, Llama 70B, Qwen3 32B) at scale. The H100 is 8 to 30x cheaper per token on gpt-oss-120b and about 25x cheaper on Llama 70B, because vLLM batches to thousands of tok/s per GPU and the Mac flattens at 2 to 3x single-stream.
- Where the Mac is close: DeepSeek-class 671B MoE at low per-user speeds. An owned 512 GB M3 Ultra at $4.6 to $6.1/M is in the same band as an H100 at $6 to $9/M at 30 to 50 tok/s per user, because the H100 InferenceX run is 8-GPU tensor-parallel fp8 with 8k inputs (prefill-heavy). But the Mac's own prefill is 85 to 210 tok/s, so the same 8k-input workload would take 40 to 100 s to first token on the Mac and the comparison is not like-for-like. H200/B200 nodes move the GPU numbers down further (not researched here).
- Where the Mac wins outright: power (200 to 300 W peak vs an 8-GPU node), silence, and the ability to serve a 400 GB model in one $10k box with no GPU rental commitment. These are capacity and convenience wins, not cost-per-token wins.
- Utilisation sensitivity: every figure above assumes 24x7 load. At 50% average utilisation all owned-Mac $/M figures double; the rented H100 can be released, so its $/M holds (subject to minimums).
- Depreciation: 100% federal bonus depreciation (section 7) improves after-tax cash flow in year one but does not change the pre-tax $/M comparison.

### Gaps
- M5 Ultra 512 GB price (used a placeholder) and any measured batched throughput on M5 Ultra for the target models: not found.
- Batched throughput beyond batch 8 on any Mac: not found, so the Mac side of the table may understate what vllm-metal or oMLX at batch 16 could reach; no evidence either way.
- H100 numbers for DeepSeek V3/V4 specifically (used R1, same architecture) and for Qwen3 235B / Kimi K2 / GLM on H100: not found in the pages read.
- A current Bay Area business internet quote: not found; $100/mo is an assumption.

## 6. Other unified-memory or appliance options (DGX Spark, DGX Station GB300, Ryzen AI Max+ 395, Tenstorrent)

### Takeaway
DGX Spark ($4,699 since Feb 2026, 128 GB, 273 GB/s) decodes gpt-oss-120b at 50 to 60 tok/s single-stream and about 115 to 175 tok/s aggregate with vLLM; its prefill (1,700 to 6,000 tok/s) is far better than any Mac. Ryzen AI Max+ 395 boxes (Framework Desktop 128 GB $3,449) do about 53 tok/s on gpt-oss-120b and 17 tok/s on Qwen3 235B Q3. DGX Station GB300 (748 GB coherent) is about $99k to $188k. Tenstorrent QuietBox 2 is $9,999 with 128 GB GDDR6 and a vendor claim of about 476 to 500 tok/s on Llama 70B (aggregate, conditions unstated).

### Cited Findings
DGX Spark
- NVIDIA forum "2/23/2026 Price Change Announcement": Founders Edition price moved from $3,999 to $4,699 "due to worldwide constraints in memory supply". (posted Feb 25 2026; checked 2026-10-22) [NVIDIA forums](https://forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713). Street prices have been reported above $6,000 (secondary search snippets; checked 2026-10-22) [borecraft](https://borecraft.com/2026/02/27/nvidia-dgx-spark-gets-700-price-hike-as-memory-shortages-bite-founders-edition-price-jumps-18-to-4699-up-from-3999/)
- NVIDIA technical blog (Oct 24 2025): 128 GB unified memory, 273 GB/s, 1 PFLOP FP4; GPT-OSS-120B MXFP4 llama.cpp prefill 1,725.47 tok/s, decode 55.37 tok/s (ISL 2048 / OSL 128, batch 1); GPT-OSS-20B 3,670 / 82.74; Qwen3 235B NVFP4 on two Sparks via ConnectX-7: prefill 23,477 tok/s, decode 11.73 tok/s. (checked 2026-10-22) [NVIDIA blog](https://developer.nvidia.com/blog/?p=107650)
- LMSYS (Nov 3 2025): SGLang on DGX Spark "around 70 tokens/s on GPT-OSS 20B and 50 tokens/s on GPT-OSS 120B". (checked 2026-10-22) [LMSYS](https://lmsys.org/blog/2025-11-03-gpt-oss-on-nvidia-dgx-spark)
- NVIDIA forum measured benchmarks on one Spark (Aug 10 2026): GPT-OSS-120B Ollama 42.1 tok/s single, 42.5 at 8 concurrent ("does not batch"); vLLM 60.7 tok/s single, 116 to 153 tok/s aggregate at 8 concurrent, TTFT 131 ms; "~6,000 tok/s prefill"; a 27,000-token prompt prefills in 3.6 s; concurrent figures varied about +-30% between runs. (checked 2026-10-22) [NVIDIA forums](https://forums.developer.nvidia.com/t/measured-inference-benchmarks-on-a-single-dgx-spark-same-harness-across-ollama-llama-cpp-and-vllm-notes-data-published/379766)
- NVIDIA forum "Dgx spark benchmark performance" (Dec 16 2025), gpt-oss-120b: vLLM 1 prompt 34.94 output tok/s (TTFT 103 ms); 10 prompts 74.90 tok/s (TTFT 677 ms); 100 prompts 175.14 tok/s (TTFT 4,890 ms); SGLang 1 prompt 52.37, 10 prompts 80.29 tok/s. (checked 2026-10-22) [NVIDIA forums](https://forums.developer.nvidia.com/t/dgx-spark-benchmark-performance/343318)
- Two DGX Sparks, vLLM 0.17.0 MXFP4 patches, gpt-oss-120b TP=2, single request, 1024 in / 128 out: 51.82 tok/s vanilla, 80.88 tok/s patched; llama-benchy tg32 81.48 tok/s; pp2048 6,069 tok/s. (Mar 9 to 11 2026; checked 2026-10-22) [NVIDIA forums](https://forums.developer.nvidia.com/t/vllm-0-17-0-mxfp4-patches-for-dgx-spark-qwen3-5-35b-a3b-70-tok-s-gpt-oss-120b-80-tok-s-tp-2/362824)
- A 64 GB DGX Spark variant is sold from $4,999 through OEM partners only (secondary; checked 2026-10-22) [Petronella](https://petronellatech.com/blog/dgx-spark-64gb-specs-price-and-the-cable-to-pair-two/)

DGX Station GB300
- pi3g price tracker (published Jun 17 2026, prices updated Oct 13 2026): indicative $100,000 excl. VAT and shipping; vendor range $99,000 (Supermicro, 12 to 16 weeks) to $188,500 (Dell); Exxact $105,000; MSI $104,500; Gigabyte $112,000; ASUS $123,500; HP $148,500. Specs: 252 GB HBM3e at 7.1 TB/s GPU memory, 496 GB LPDDR5X at 396 GB/s CPU memory, 748 GB total coherent, 1,600 W PSU, Grace 72-core CPU. (checked 2026-10-22) [pi3g](https://pi3g.com/?p=31780)
- Tom's Hardware: an Exxact listing at $94,930 for a single-GB300 unit (headline only read; search snippet for price; checked 2026-10-22) [Tom's Hardware](https://www.tomshardware.com/desktops/nvidias-gb300-powered-dgx-station-desktop-tower-listed-for-nearly-usd100-000-online-enterprise-ai-powerhouse-now-available-to-buy-for-mere-mortals-with-lots-of-cash). Spheron (Oct 2026) cites MSI XpertStation WS300 at $85,000 as the only public list price (search snippet; checked 2026-10-22) [Spheron](https://www.spheron.network/blog/dgx-station-gb300-vs-renting-gb300-nvl72-break-even-guide-20/)
- DGX Station GB300 measured LLM throughput: not found.

AMD Ryzen AI Max+ 395 (Strix Halo), 128 GB, about 256 GB/s
- Framework Desktop DIY live prices: Ryzen AI Max 385 32 GB $1,269; Max+ 395 64 GB $1,959; Max+ 395 128 GB $3,449; all "Out of stock"; "Ships within 5 business days". (checked 2026-10-22) [Framework](https://frame.work/products/desktop-diy-amd-aimax300/configuration/new). Launch price was $1,999 (2025). AMD's Jan 2026 blog footnote used "USD $2566 for the Framework Desktop 128GB and USD $4000 for the NVIDIA DGX Spark as of December 2025". (checked 2026-10-22) [AMD blog](https://www.amd.com/en/blogs/2026/amd-ryzen-ai-max-ai-pcs-deliver-exceptional-intelligence.html)
- visorcraft/strix-halo-llm-perf (GMKtec EVO-X2 and Beelink GTR9 Pro, 128 GB each, llama.cpp ROCm 7.0, Fedora 43, latest finding Mar 3 2026): GPT-OSS 120B Q4_K_M pp512 120 / tg128 53.4 tok/s (llama-server); Qwen3-235B-A22B Q3_K_M (104.7 GiB) pp 101 / tg 17.2; Llama 3.1 70B Q4_K_M pp 81.6 / tg 5.1; Qwen3 30B-A3B pp 1,142 / tg 86.1. Two-host RPC over a direct USB4 cable ("~9.4 Gbps measured"): Qwen3.5-397B-A17B UD-Q4_K_XL pp 147.55 / tg 11.76; MiniMax-M2.5 139B Q8_0 pp 332 / tg 15.35. No two-host result for gpt-oss-120b or Qwen3 235B. (checked 2026-10-22) [GitHub visorcraft](https://github.com/visorcraft/strix-halo-llm-perf)
- AMD (Jan 5 2026): gpt-oss-120b on Ryzen AI Max+ 395 runs "about 10 times faster than Meta Llama 3 70B"; "average 1.7 times more tokens per dollar" than DGX Spark in LM Studio (Vulkan llama.cpp) across GPT-OSS 20B/120B, GLM 4.5 Air, DeepSeek R1 Distill 70B; no absolute tok/s in text. (checked 2026-10-22) [AMD blog](https://www.amd.com/en/blogs/2026/amd-ryzen-ai-max-ai-pcs-deliver-exceptional-intelligence.html). AMD's 2025 LM Studio post: gpt-oss-120b "up to 30 tokens per second", MXFP4 weights about 61 GB (search snippet; checked 2026-10-22) [AMD 2025](https://www.amd.com/en/blogs/2025/how-to-run-openai-gpt-oss-20b-120b-models-on-amd-ryzen-ai-radeon.html)
- HP Z2 Mini G1a 128 GB: Swiss retail CHF 5,555 (1 TB), UK sale £2,197.51; a 2025 forum post cited $3,300 US preorder. GMKtec EVO-X2 128 GB: CHF 3,299 (2 TB); EUR 3,749 to 3,799 (German retail); maker's site 1,999 euros at review time. (search snippets; dates mixed; checked 2026-10-22) [Galaxus comparison](https://www.galaxus.ch/en/s1/producttype/pc-18/compare/gmktec-evo-x2-vs-hp-z2-mini-g1a-2501), [Level1Techs Z2 Mini](https://forum.level1techs.com/t/hp-z2-mini-g1a/225762), [Notebookcheck](https://www.notebookcheck.net/GMKtec-releases-cheaper-AMD-Strix-Halo-desktop-with-128-GB-RAM-and-96-GB-VRAM.1345433.0.html)
- Batched/concurrent throughput on Strix Halo for gpt-oss-120b: not found.

Tenstorrent
- IEEE Spectrum / Tenstorrent newsroom (Mar 24 2026): QuietBox 2 "expected retail price of US $9,999", four Blackhole accelerators, "each card has 120 Tensix AI accelerators and 32 GB of GDDR6 memory" (128 GB GDDR6 total), 256 GB DDR5, runs Llama 3.1 70B "at speeds of nearly 500 tokens per second" (aggregate vs per-user not stated), launch "second quarter of 2026". (checked 2026-10-22) [Tenstorrent newsroom](https://tenstorrent.com/newsroom/these-ai-workstations-look-like-pcs-but-pack-a-stronger-punch). Press release figure: 476.5 tokens per second for Llama 3.1 70B (search snippet; checked 2026-10-22) [Kyodo PR](https://kyodonewsprwire.jp/release/202603135606). A third-party write-up says the 476.5 figure is "aggregate throughput across concurrent requests" (search snippet; checked 2026-10-22) [runaihome](https://runaihome.com/blog/qualcomm-tenstorrent-risc-v-ai-accelerator-home-lab-2026/)
- Tenstorrent docs: TT-QuietBox 2 $9,999; 4x Blackhole chips on 2x p300c cards; 480 Tensix cores; 128 GB GDDR6; "1,024 GB/s per card"; 720 MB SRAM; 256 GB DDR5-5600; 1,600 W PSU, peak about 1,500 W; liquid cooled; ships with Qwen3-32B preloaded; Llama 3.3 70B listed as supported; no throughput numbers on the page. (checked 2026-10-22) [Tenstorrent docs](https://docs.tenstorrent.com/tt-quietbox2-guide)
- Blackhole p150a card $1,399 (up from $1,299 at 2025 launch), 4 to 6 week shipping; p100a $999. (search snippets; checked 2026-10-22) [Tenstorrent cards](https://www.tenstorrent.com/cards). Galaxy Blackhole server from $110,000, claims "over 350 tokens per second per user on DeepSeek-R1-0528 671B" (search snippet; vendor claim; checked 2026-10-22) [Munich Startup](https://insights.munich-startup.de/news/feed/tenstorrent-launches-galaxy-blackhole-ai-system-with-10x-faster-video-generation-and-350-tokens-second-llm-inference)

### Inferences
- DGX Spark is the better appliance for an API: similar single-stream decode to a Mac on gpt-oss-120b, 3 to 9x faster prefill (1,725 to 6,000 vs 690 tok/s), real continuous batching (vLLM, SGLang), CUDA. Its 128 GB cap rules out DeepSeek-class models; two Sparks run Qwen3 235B NVFP4 at only 11.7 tok/s.
- Strix Halo at $3,449 (Framework) is the cheapest box that runs gpt-oss-120b at about 53 tok/s, but there is no published batching data and its prefill (120 tok/s on gpt-oss-120b) is worse than the Mac's.
- Tenstorrent's $9,999 QuietBox 2 vendor claim of about 476 tok/s aggregate on Llama 70B, if real, would be about 15x a Mac Studio on that dense model and would put it near an H100's per-token cost (estimate: 3-yr hardware 9,999 / 26,280 = $0.38/hr, power at its 1.5 kW peak $0.375/hr, internet $0.137/hr, total $0.89/hr; 476 tok/s = 1.714 M tok/hr; about $0.52 per million). No independent benchmark found; power draw is 5x a Mac.
- DGX Station GB300 at about $100k buys 748 GB coherent memory and 7.1 TB/s HBM; no public LLM throughput was found, so no $/M can be estimated.

### Gaps
- DGX Spark gpt-oss-120b vLLM aggregate at exactly 16 and 32 concurrent: not found (have 8 and 100 concurrent).
- Strix Halo batched throughput and two-box RPC for gpt-oss-120b / Qwen3 235B: not found.
- Independent QuietBox 2 benchmarks: not found.
- Current US retail price for HP Z2 Mini G1a 128 GB and GMKtec EVO-X2 128 GB: not found (search budget exhausted; only mixed-date, mixed-currency listings).

## 7. Tax angle (federal bonus depreciation, California, home office vs colo)

### Takeaway
A Mac bought and placed in service in 2026 qualifies for permanent 100% federal bonus depreciation (OBBBA; property acquired and placed in service after January 19, 2025; IRS Notice 2026-11). California does not conform to bonus depreciation and caps Section 179 at $25,000 (reduced above $200,000 of purchases), so the state deduction is $25,000 plus regular depreciation. Computers stopped being "listed property" after 2017, so a Mac in a Redwood Shores home office versus a colo does not change the federal deduction; only the business-use percentage does.

### Cited Findings
- Thomson Reuters (Jan 15 2026): IRS Notice 2026-11 (issued Jan 14 2026, IR 2026-06); the OBBB "permanently reinstated 100% bonus depreciation for qualified property acquired and placed in service after January 19, 2025"; taxpayers "may elect to apply the 40% rate" (60% for long-production-period property) for the first tax year ending after January 19, 2025, on a timely filed return; eligibility follows Reg. 1.168(k)-2 with date substitutions. (checked 2026-10-22) [Thomson Reuters](https://tax.thomsonreuters.com/news/irs-provides-guidance-on-post-obbb-bonus-depreciation/). The notice PDF is at [IRS n-26-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) (fetched as binary; not text-readable here). BDO: property must be both acquired and placed in service after January 19, 2025; a written binding contract on or before that date makes it "acquired" before the cutoff (search snippets; checked 2026-10-22) [BDO](https://www.bdo.com/insights/tax/irs-issues-interim-guidance-on-bonus-depreciation-rules), [NATP](https://www.natptax.com/news-insights/blog/irs-releases-guidance-on-permanent-100-bonus-depreciation/)
- Federal Section 179 for 2026: $2,560,000 limit, phase-out from $4,090,000 (secondary, citing IRS Pub 946 "What's New for 2026"; checked 2026-10-22) [Harness](https://www.harness.co/articles/section-179-vs-bonus-depreciation-2026)
- California FTB, 2025 Instructions for Form FTB 3885: "California law does not conform to the federal limitation amounts under IRC Section 179(b)(1) and (2). For California purposes, the maximum IRC Section 179 expense deduction allowed is $25,000. This amount is reduced if the cost of all IRC Section 179 property placed in service during the taxable year is more than $200,000." California does not conform to "IRC Section 168(k) relating to the depreciation deduction for certain assets" (bonus depreciation) nor to the "100% depreciation election for qualified production property (IRC Section 168(n))". Useful life guide: "Computers and peripheral equipment (printers, etc.): 6 yrs." (2025 tax year; checked 2026-10-22) [FTB 3885 instructions](https://www.ftb.ca.gov/forms/2025/2025-3885-instructions.html)
- KDA (Mar 28 2026): "California partially conforms to Section 179 expensing, allowing up to $25,000 per year"; "California does not conform and requires standard MACRS depreciation over the asset's useful life"; cites R&TC 17250 and 24356; federal 100% bonus "placed in service after December 31, 2024" (this date conflicts with the IRS guidance above; the Jan 19, 2025 date is the statutory one). (checked 2026-10-22) [KDA](https://kdainc.com/bonus-depreciation-income-limitation-2025-california-the-22000-state-tax-trap-bu/)
- Computers as 5-year MACRS property ("qualified technological equipment"); half-year schedule 20 / 32 / 19.2 / 11.52 / 11.52 / 5.76 percent (secondary; checked 2026-10-22) [TaxGPT](https://www.taxgpt.com/answer/what-is-the-depreciation-schedule-for-computers-used-for-business)
- Listed property: the TCJA removed "computers and peripheral equipment placed in service after 2017" from the definition of listed property, so the more-than-50% business-use test and heightened substantiation no longer apply to them; depreciation is still limited to the business-use percentage of cost. (search snippets; checked 2026-10-22) [ThisMatter](https://thismatter.com/money/tax/listed-property.htm), [Keeper](https://keepertax.com/posts/self-employed-computer-tax-deduction)

### Inferences
- A $9,690 to $13,499 Mac Studio placed in service by Dec 31 2026 and used 100% for the business is fully deductible federally in 2026. For California, deduct $25,000 under Section 179 (enough to cover one Mac) and depreciate the rest; two or more Macs exceed the $25,000 cap and the excess follows California MACRS. Because the California cap is $25,000 per year, spreading purchases across tax years increases the state first-year deduction.
- Home office vs colo: federal bonus depreciation and Section 179 do not depend on where the machine sits. A colo arguably simplifies proving 100% business use (no personal use possible) and the colo fee is an ordinary expense; a home-office Mac needs business-use substantiation but is no longer "listed property". The "no physical work" preference favours colo or hosted because hardware swaps, reboots after kernel panics (Geerling: RDMA testing crashed Macs) and macOS upgrades ("cannot be run over SSH") require hands-on access.
- Tax treatment of a leased or hosted Mac: the rental is an ordinary expense, no depreciation; this forfeits the bonus-depreciation timing benefit.

### Gaps
- IRS Notice 2026-11 primary text: not quoted (PDF not text-extractable in this session); relied on Thomson Reuters, BDO, NATP summaries.
- Whether California's $25,000 Section 179 cap applies per taxpayer for an individual (R&TC 17255) exactly as for corporations (24356): the FTB corporate form was read; the personal-income form 3885A was not (403).
- Any authority on home office vs colo affecting the deduction: none found; the inference above is reasoning, not a cited rule.

## Key question: Can a Mac-based provider meet OpenRouter-style expectations (TTFT under a few seconds at 1k to 8k prompts, 95% uptime)?

### Takeaway
Uptime (95%+) is achievable with a redundant pair of Macs and a load balancer, since the requirement is request success rate, not hardware availability. TTFT is the problem: on an M3 Ultra a 1k prompt is 1.6 to 5 s and an 8k prompt is 12 to 48 s depending on model; only gpt-oss-120b on an M5 Ultra (estimated about 2.5 s at 8k) plausibly meets "a few seconds". DeepSeek-class models on a Mac cannot.

### Cited Findings
- OpenRouter provider guide: uptime "successful requests / total requests" excluding user errors; "95%+ uptime" normal routing, "80-94% uptime" lower priority, "<80% uptime" fallback only; needs "100+ requests" before calculation; OpenRouter "publicly tracks TTFT (time to first token) and throughput (tokens/second)"; throughput is "output tokens / generation time" and "any queueing on your side appears in your throughput numbers"; "Return early 429s if under load, rather than queueing requests"; "send SSE comments as keep-alives". (checked 2026-10-22) [OpenRouter for providers](https://openrouter.ai/docs/guides/community/for-providers.md)
- Measured TTFT on M3 Ultra 512 GB: gpt-oss-120b 16k context TTFT 24,691 ms (oMLX); DeepSeek V3.2 1k TTFT 4,880 ms, 32k TTFT 390 s (oMLX); Kimi K2.6 1k TTFT 4,805 ms (oMLX); Qwen3 235B 1k TTFT 2,748 ms (oMLX); DeepSeek V3 15,777-token prompt 227 s (r/LocalLLaMA Mar 2025). See section 2 for URLs.
- Apple M5 Ultra TTFT at 8,192 context: Qwen 3.8 27B BF16 4.1 s (M3 Ultra 18.2 s); Mistral Medium 3.5 128B FP8 24.6 s (M3 Ultra 95.9 s). (Oct 15 2026; checked 2026-10-22) [Apple ML Research](https://machinelearning.apple.com/research/mlx-distributed-inference)
- DGX Spark gpt-oss-120b TTFT 131 ms single (vLLM) and 4,890 ms at 100 concurrent; H100 numbers in section 5 are at 8k input with per-user interactivity targets of 30 to 200 tok/s. See sections 5 and 6 for URLs.

### Inferences
- Per-model TTFT estimate at 8k prompt, single request: M3 Ultra gpt-oss-120b about 12 s; M5 Ultra gpt-oss-120b about 2.5 s (4.6x); M3 Ultra DeepSeek 48 s; M5 Ultra DeepSeek about 10 s; M3 Ultra Qwen3 235B 21 s; M3 Ultra Kimi 34 s. Under concurrency, prefill of one request blocks or slows others, so these are best cases.
- Verdict: a Mac can list gpt-oss-120b, Qwen3 32B or 70B-class dense models on OpenRouter with acceptable TTFT at 1k prompts, and only an M5 Ultra at 8k; it cannot list DeepSeek/Kimi/GLM-class models with competitive TTFT. Its throughput column on OpenRouter would show 20 to 70 tok/s per request, at the low end of the market.
- Uptime: Apple's and Geerling's notes on reboots, recovery-mode RDMA enablement, and SSH-blocked OS upgrades mean a single Mac will fall below 95% over a year unless a second machine takes traffic during maintenance.

### Gaps
- Measured TTFT under concurrent load on a Mac Studio: not found.
- Typical OpenRouter provider TTFT and throughput percentiles per model: not read (model pages not fetched; search budget exhausted).

## Recommended planning numbers

### Takeaway
Use these for the plan. Measured values are cited above; "est." values are my arithmetic (M5 Ultra = M3 Ultra x 1.6 for decode; cost per hour = price / (3 x 8,760) + $0.075 power + $0.137 internet; $/M = cost per hour / (aggregate tok/s x 3,600 / 1e6)).

### Cited Findings (table)

| Machine | Price (checked 2026-10-22) | Memory | Bandwidth | gpt-oss-120b aggregate tok/s | DeepSeek-class MoE aggregate tok/s | Cost/hr owned 3-yr (est.) | $/M output tokens gpt-oss-120b (est.) | $/M output tokens DeepSeek-class (est.) |
|---|---|---|---|---|---|---|---|---|
| Mac Studio M3 Ultra 512 GB (discontinued; reseller) | $9,690 (Small Dog sealed, sold out) | 512 GB | 819 GB/s | 187 at batch 8 (measured, oMLX 2026-03-08) | 26.4 at batch 2 (measured, V3.2 4-bit, oMLX 2026-03-12); Kimi K2.6 3.3-bit 40.9 at batch 4 | $0.58 | $0.86 | $6.11 (V3.2), $3.95 (Kimi) |
| Mac Studio M5 Ultra 256 GB | $9,499 (Pinggy, Sep 2026) | 256 GB | 1.2 TB/s | about 300 at batch 8 (est.) | does not fit DeepSeek 4-bit (354 to 382 GB peak) | $0.57 | $0.53 | n/a |
| Mac Studio M5 Ultra 512 GB | not found; placeholder $13,499 (est.) | 512 GB | 1.2 TB/s | about 300 at batch 8 (est.) | about 42 at batch 2 (est.) | $0.73 | $0.67 | $4.80 |
| Mac Studio M5 Max 128 GB | 128 GB tier price not found (base $2,499) | 128 GB | 614 GB/s | not found | does not fit | n/a | n/a | n/a |
| Mac mini M5 Pro 64 GB | $2,699 (third-party tracker) | 64 GB | 307 GB/s | does not fit (63 GB weights) | does not fit | n/a | n/a | n/a |
| 4x M3 Ultra cluster (2x512 + 2x256) | $39,596 (Creative Strategies, Dec 2025) | 1.5 TB | 819 GB/s each | not measured | Kimi K2 Thinking 25 to 30; DeepSeek V3.1 32.5 (batch 1) | $1.94 (est.: 39,596 / 26,280 = 1.507 + 4 x 0.075 + 0.137) | n/a | $16.6 (est.: 1.94 / (32.5 x 3,600 / 1e6 = 0.117)) |
| DGX Spark 128 GB | $4,699 MSRP (NVIDIA, Feb 2026) | 128 GB | 273 GB/s | 116 to 153 at 8 concurrent, 175 at 100 (measured, vLLM) | does not fit | $0.39 | $0.71 | n/a |
| Framework Desktop Ryzen AI Max+ 395 128 GB | $3,449 (frame.work, out of stock) | 128 GB | about 256 GB/s | 53.4 single (measured); batched not found | does not fit (Qwen3 235B Q3 17.2 tok/s) | $0.34 | $1.79 (single stream) | n/a |
| Tenstorrent QuietBox 2 | $9,999 (vendor) | 128 GB GDDR6 + 256 GB DDR5 | 1,024 GB/s per card | not found | does not fit | $0.89 (est.: 9,999 / 26,280 = 0.38 hw + 0.375 power at 1.5 kW + 0.137 internet) | n/a (Llama 70B vendor claim 476 tok/s aggregate, about $0.52/M est.) | n/a |
| DGX Station GB300 | about $99k to $188k (pi3g, Oct 13 2026) | 748 GB coherent | 7.1 TB/s HBM | not found | not found | $3.8 to $7.2 hw only (est.: 99,000 / 26,280 to 188,500 / 26,280) | n/a | n/a |
| H100 rented (reference) | $2.50/hr (user); market $1.99 to $4.50 on Oct 10 2026 | 80 GB HBM | 3.35 TB/s | 8,973 per GPU at 50 tok/s per user (measured, InferenceX) | DeepSeek R1 fp8 116 per GPU at 30 tok/s per user (8-GPU TP) | $2.50 | $0.077 | $5.99 |
| Hosted: MacWeb M3 Ultra 256 GB | $799/mo, no contract (out of stock) | 256 GB | 819 GB/s | 187 at batch 8 | does not fit | $1.09 | $1.62 | n/a |
| Hosted: MacWeb M5 Ultra 256 GB | $1,500/mo, no contract (coming soon) | 256 GB | 1.2 TB/s | about 300 (est.) | does not fit | $2.05 | $1.90 | n/a |
| Hosted: AWS mac-m3ultra.metal | $12.50/hr, 24-hr minimum (Vantage) | 256 GB | 819 GB/s | 187 at batch 8 | does not fit | $12.50 | $18.6 | n/a |

### Inferences
- Plain answer: a Mac cannot compete with a rented H100 on cost per token at scale for any model that fits an H100 node with vLLM. The gap is about 10x on gpt-oss-120b and about 25x on Llama 70B. The one regime where an owned 512 GB Mac is in the same price band is DeepSeek-class MoE served at 30 to 50 tok/s per user and short prompts, and even there the Mac's 5 to 48 s TTFT would be the slowest provider on OpenRouter.
- Where Macs win: a 400 GB model in a single $10k box with 200 to 300 W draw, no rental minimums, full-expensing tax treatment in 2026, and a resale market. That suits a private or low-concurrency deployment, not a public paid API.
- If the operator still wants a Mac, the M5 Ultra (1.6x decode, up to 4.6x prefill) is the only sensible choice, and only gpt-oss-120b / Qwen3 235B-class models should be exposed publicly; wait for the 512 GB price and for a vllm-metal or oMLX batch-16 measurement before buying more than one.

### Gaps
- No published batch 16 or 32 measurement on any Mac Studio for the target models; this is the single biggest unknown in the table.
- M5 Ultra 512 GB price and independent M5 Ultra benchmarks on DeepSeek / Kimi / gpt-oss-120b: not found.
- H100 figures for DeepSeek V3/V4, Kimi K2, GLM-5, Qwen3 235B: not found in pages read (used DeepSeek R1 as proxy).
- Search budget was exhausted before confirming: MacWeb AUP, Mac Studio M5 Max 128 GB price, HP/GMKtec current US prices, OpenRouter per-model latency pages.
