# In-stock AI inference hardware (Oct/Nov 2026 delivery), tinybox, and ship-to-colo options

All prices and stock text were read on 2026-10-22 unless a line says otherwise. Every "estimate" shows its arithmetic. "not found" means I could not reach or find the item today. Web search quota ran out partway through; several retailer pages (B&H, CDW, Newegg, Provantage, Connection, Insight, eBay, Micro Center, TheServerStore, UnixSurplus, ServerMonkey, HostDime) returned HTTP 403/404 to the fetcher and are listed as gaps.

## Key question 1: tinygrad tinybox. What is listed, what does it cost, is it in stock, and is it competitive?

### Takeaway
tinygrad.org now sells a configurable "new tinybox" in three platforms (G4, G5, pro) with AMD R9700, AMD 9070XT, or NVIDIA RTX 6000 Blackwell GPUs. Nothing is in stock. Every unit is "Made to order. Ships in 1–8 weeks," wire transfer only, and the configurator shows "Checkout not connected." The old tinybox red, green, and green v2 are no longer on the site. tinygrad publishes no LLM throughput numbers and offers no hosting or rental.

### Cited Findings
- Three preset configs on tinygrad.org (checked 2026-10-22): "tinybox red flash G4 · 32 GB DDR4, 6× AMD R9700, 192 GB GPU RAM · 3,840 GB/s, $19,000"; "tinybox green workstation G5 · 192 GB DDR5 · 4 TB RAID, 2× NVIDIA RTX 6000 Blackwell, 192 GB GPU RAM · 3,584 GB/s, $60,000"; "tinybox pro · 384 GB DDR5, 8x NVIDIA RTX 6000 Blackwell, 768 GB GPU RAM · 14,336 GB/s, $200,000" — [tinygrad.org](https://tinygrad.org/)
- Configurator base prices: "G4 DDR4 EPYC PCIe 4 $7,000 base", "G5 DDR5 GENOA PCIe 5 $12,000 base", "pro 5U rack Dual GENOA PCIe 5 $32,000 base". GPU add-ons: "4× AMD 9070XT +$4,000", "6× AMD R9700 +$12,000", "1× NVIDIA RTX 6000 +$19,000", "2× NVIDIA RTX 6000 +$38,000", "8x NVIDIA RTX 6000 +$152,000". Memory "128 GB +$3,000". Storage "4 TB RAID +$2,000", "16 TB RAID +$6,000" — [tinygrad.org](https://tinygrad.org/)
- Stock and lead time, verbatim: "**Made to order.** Ships in 1–8 weeks." and "**Bank transfer / wire only.** Complete payment within 5 days of order confirmation to guarantee your order." The checkout button is followed by "Checkout not connected." — [tinygrad.org](https://tinygrad.org/)
- Returns: "Within 30 days of receipt, with a 20% restocking fee." Shipping: "Fully insured UPS shipping worldwide... Allow 3–10 days for delivery after dispatch." — [tinygrad.org](https://tinygrad.org/)
- G4 red flash system spec: "32 core EPYC, water cooled", "1700W PSU, 100V~240V", "2× 1GbE + OCP3.0", "< 60 dB, GPU blowers are audible", "6× AMD R9700 (limited to 225W)", "Up to 6 GPUs, full-fabric PCIe", "42 lbs, 12″W × 19¼″H × 18″D" (a tower, not a rack unit) — [tinygrad.org](https://tinygrad.org/)
- The tinybox pro is a "5U rack" platform; G4 and G5 are towers — [tinygrad.org](https://tinygrad.org/)
- The docs still describe the older lineup: "The red box includes six 7900XTX GPUs, the green box includes six 4090 GPUs, and the green v2 box includes four 5090 GPUs," with "two 1600W PSUs" and 12U rack mounting; those models no longer appear on the store page — [docs.tinygrad.org/tinybox](https://docs.tinygrad.org/tinybox/)
- No cloud or rental: "We don't have a stupid cloud service, you don't have to create a tiny account to set it up" — [docs.tinygrad.org/tinybox](https://docs.tinygrad.org/tinybox/)
- A third-party green v2 owner wrote up home-server use with Ollama but published no tokens-per-second numbers — [owain.bearblog.dev](https://owain.bearblog.dev/turning-a-tinybox-green-v2-into-a-private-ai-home-server/)
- Warranty: not found on tinygrad.org or docs.tinygrad.org (checked 2026-10-22).
- Published tinybox LLM throughput: not found. No tinybox-specific tokens/s numbers exist on tinygrad.org, docs.tinygrad.org, or in search results.
- Third parties renting tinyboxes or selling tinybox time: not found. The only hits were an unofficial iPad client app and aggregator pages — [search summary](https://www.stork.ai/ko/tinybox)

### Inferences
- The G5 "green workstation" is a 2x RTX PRO 6000 Blackwell box at $60,000. Two cards at Saitech's special-order price cost 2 × $16,956 = $33,912 (estimate from [Saitech](https://esaitech.com/products/nvidia-vcnrtxpro6000b-pb-rtx-pro-96gb-graphic-card)). A Bizon G7000 G4 4U server base ($17,731, in stock) plus two cards is about $17,731 + $33,912 = $51,643 (estimate). So the tinybox G5 costs about $8,400 more than a comparable in-stock rackmount build and ships in 1 to 8 weeks versus 1 to 4 days.
- Throughput for the G5 should track two RTX PRO 6000 cards. Using TensorRT-LLM's FP4 Llama 3.3 70B figure of 1,724 output tok/s per GPU at 1 GPU (PP1) and 1,881 at PP2, a 2-card box is about 2 × 1,881 = 3,762 tok/s aggregate (estimate; aggregate = per-GPU rate × GPU count) — [TensorRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/1.2.0/developer-guide/perf-overview.html). A 4x RTX PRO 6000 box at PP4 is about 4 × 1,798 = 7,192 tok/s (estimate). The 4x box roughly doubles throughput for about 1.5x the price, so the tinybox G5 is not competitive on tokens per dollar with a 4x RTX PRO 6000 box.
- The "red flash G4" (6x R9700, 192 GB, $19,000) is the cheapest 192 GB box found. No 6-card R9700 throughput data exists. Two R9700 cards hit about 3,057 tok/s aggregate on gpt-oss-20b with vLLM (ASRock vendor test, see Key question 6). gpt-oss-120b (about 63 GB MXFP4) needs at least 3 of the 32 GB cards, and no measured 120B number on R9700 was found.
- "Checkout not connected" plus "wire only" and "1–8 weeks" make a tinybox a poor fit for a hard December 15 in-service date.

### Gaps
- tinybox warranty terms: not found.
- Any measured tokens/s on any tinybox model: not found.
- Whether "Checkout not connected" means orders are closed today or the configurator is simply a preview: not stated on the page.

## Key question 2: RTX PRO 6000 Blackwell (96 GB) systems and cards: price, stock, and measured throughput

### Takeaway
Bizon is the only vendor found with explicit "In Stock" text and ship dates for RTX PRO 6000 Blackwell multi-GPU systems (X5500 G2 tower up to 4x, X7000 G3 and G7000 G4 4U servers up to 8x), but Bizon shows only base prices. Lambda has discontinued its on-premise hardware line. Single cards cost about $17,000 to $17,850 at Saitech (special order) and $24,450 refurbished with "ETA 3-4 days" at IT Creations; NVIDIA's own store listed the card at $16,000 and out of stock in August. Single-card throughput is well measured (about 1,500 output tok/s on gpt-oss-120b in vLLM at 50 concurrent prompts; 1,724 tok/s per GPU on Llama 3.3 70B FP4 in TensorRT-LLM). Multi-GPU vLLM numbers are thin; TensorRT-LLM per-GPU tables for PP4 and PP8 are the best evidence.

### Cited Findings
Systems:
- Lambda: "Lambda has discontinued its on-premise hardware line, including Vector Pro... Warranties will still be fully supported." Lambda points buyers to partners — [lambda.ai/gpu-workstations/vector-pro](https://lambda.ai/gpu-workstations/vector-pro) (checked 2026-10-22). The Scalar server page returned 404 — [lambda.ai/gpu-servers/scalar](https://lambda.ai/gpu-servers/scalar)
- Bizon X5500 G2 (tower, "22.8 x 9.5 x 22.0 inches"): "Up to 2× NVIDIA RTX 5090 or 4x RTX PRO 6000 Blackwell GPUs", "Starting at $9,076", PSU "4 GPU: 3000W", stock text "In Stock", "Lead time: 2–3 days", "Ship date: Oct 24 – Oct 25, 2026", "Ships within 1-3 days." 4-GPU price not shown — [bizon-tech.com/bizon-x5500.html](https://bizon-tech.com/bizon-x5500.html)
- Bizon X7000 G3 (dual EPYC, "Rackmountable; 4U"): "Up to 8 Nvidia graphics cards", options "RTX PRO 6000 Blackwell 96GB (600W)" and "Max-Q 96GB (300W)", "Starting at $20,653", PSU "2+2 2600W" or "3+1 3200W", "In Stock", "Lead time: 5–7 days", "Ship date: Oct 27 – Oct 29, 2026" — [bizon-tech.com/bizon-x7000.html](https://bizon-tech.com/bizon-x7000.html)
- Bizon G7000 G4 (dual Xeon, 4U): up to 8 GPUs incl. "RTX PRO 6000 Blackwell 96Gb Server (600W)" and Max-Q, "Starting at $17,731", PSU 2+2 2600W (5200W max), "In Stock", "Lead time: 1–4 days", "Ship date: Oct 23 – Oct 26, 2026" — [bizon-tech.com/bizon-g7000.html](https://bizon-tech.com/bizon-g7000.html)
- Exxact Valence 4x Max-Q Workstation (platform VWS-135223847): "4x NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition", Threadripper PRO 9995WX, 1TB DDR5, 2500W PSU; "each of our GPUs pulled the maximum 300W TDP". No price, no lead time, no tokens/s — [exxactcorp.com blog](https://www.exxactcorp.com/blog/news/exxact-validates-4x-nvidia-rtx-pro-6000-blackwell-max-q-in-a-workstation)
- Puget Systems: category pages show no model prices; the only shipping text is "Most orders ship in 2 weeks." Rackstations offer "Options with up to four NVIDIA RTX GPUs" — [pugetsystems.com/products/workstations](https://www.pugetsystems.com/products/workstations/), [rackmount](https://www.pugetsystems.com/products/rackmount-workstations/)
- System76 Thelio Mega: "Up to 3 x NVIDIA or AMD Pro Graphics", options "96 GB NVIDIA RTX PRO 6000 (non-refundable)" and Max-Q, price shown "Now: $8,999.00" (base), "Current Stock:" field blank, no lead time — [system76.com/desktops/thelio-mega](https://system76.com/desktops/thelio-mega)
- Thinkmate GPX server category shows "RTX PRO 6000 (7)" systems in the filter but no lead times in the page text — [thinkmate.com/systems/servers/gpx](https://www.thinkmate.com/systems/servers/gpx)
- Supermicro AS-5126GS-TNRT 5U with 8x RTX PRO 6000 Server Edition offered by an EU reseller as "Special cancelled-order pricing – quotation on request", "Limited cancelled-order allocation", "No standard production lead time; dispatch subject to confirmation" — [server-parts.eu](https://www.server-parts.eu/post/supermicro-as-5126gs-tnrt-8-gpu-rtx-pro-6000-blackwell-server)
- Dell Pro Max T2, HP Z8 Fury, Boxx, Velocity Micro, Maingear, ASUS ESC, Gigabyte: not reachable or no price/stock text found today (Dell and HP pages returned navigation only or timed out).

Single cards:
- Saitech (US): NVIDIA VCNRTXPRO6000B-PB (PNY Workstation Edition) "Sale price$16,956.00", "In stock: No", "This product is available for special order and may take longer to ship." — [esaitech.com](https://esaitech.com/products/nvidia-vcnrtxpro6000b-pb-rtx-pro-96gb-graphic-card)
- Saitech: Server Edition 900-2G153-0000-000 "Sale price$17,850.00", "In stock: No", special order — [esaitech.com](https://esaitech.com/products/nvidia-rtx-pro-6000-900-2g153-0000-000-96gb-graphic-card). Saitech's H100 search page also lists "NVIDIA VCNRTXPRO6000BQ-PB RTX PRO 6000 Blackwell Max-Q... $16,956.00, Get a Quote" and "PNY VCG509032TFXPB1 GeForce RTX 5090 32GB $9,063.00" — [esaitech.com search](https://esaitech.com/search?q=H100)
- IT Creations: "NVIDIA RTX PRO 6000 BLACKWELL SERVER EDITION PASSIVE GPU 96GB", part "RTX PRO 6000 SERVER-CISCO", "Refurbished", structured-data price 24450 USD (visible field "Request Pricing"), "ETA 3-4 days" "as of 10/22/2026 07:32:00 AM PDT" — [itcreations.com/product/160264](https://www.itcreations.com/product/160264)
- Supermicro eStore GPU-NVRTXPRO-6K-B-SE: "Out of stock", "This item is out of stock but we may still be able to fulfill your order." No price — [store.supermicro.com](https://store.supermicro.com/us_en/supermicro-rtx-pro-6000-gpu-nvrtxpro-6k-b-se.html)
- NVIDIA Marketplace: reports say the Workstation Edition rose to $13,250 in June 2026 and $16,000 in August 2026 and showed out of stock — [letsdatascience](https://letsdatascience.com/news/nvidia-raises-rtx-pro-6000-blackwell-price-again-6d1ae9ff). The marketplace page timed out twice today, so the live price is not verified.
- Hardware Corner lists "$8,800" as "Current Price in US / Avg. Market Value" for the card; this conflicts with the $16,000 to $17,850 figures above and its date is not shown — [hardware-corner.net](https://www.hardware-corner.net/gpu-llm-benchmarks/rtx-pro-6000-blackwell/)
- B&H, CDW, Newegg, Provantage, Connection, Insight: HTTP 403 to the fetcher today. A cached Newegg page showed a PNY Workstation Edition at $9,999.00 and an NVIDIA OEM version out of stock at $8,995.99, undated — [newegg.com cached](https://www.newegg.com/p/pl?d=6000680)

Measured throughput:
- 1x RTX PRO 6000 Server Edition, vLLM, 50 prompts with request-rate inf, input 100 / output 600 tokens, max-model-len 4096: gpt-oss-120b "Total 1778.77 tok/s, Output 1524.66 tok/s, 2.54 req/s"; Qwen3-14B 1,743.76 output tok/s; DeepSeek-R1-Distill-Qwen-32B 829.02 output tok/s. 300-concurrent stress test: DeepSeek-R1-Distill-Qwen-32B 1,654.67 tok/s on PRO 6000 vs 1,481.62 on H100 vs 720.75 on A100 — [DatabaseMart](https://www.databasemart.com/blog/vllm-gpu-benchmark-pro6000)
- 1x RTX PRO 6000, vLLM docker, 400 concurrent requests, 1000 in / 1000 out, kv-cache fp8: Qwen3-Coder-30B-A3B AWQ 8,425 output tok/s; Llama-3.3-70B-Instruct-AWQ-INT4 1,031 output tok/s; GLM-4.5-Air-AWQ-4bit 3,169 output tok/s — [CloudRift](https://www.cloudrift.ai/blog/benchmarking-rtx-gpus-for-llm-inference)
- 1x RTX PRO 6000, llama.cpp single stream: gpt-oss 120B Q8_0 221.3 t/s at 4k context, 123.3 at 128k; MXFP4 210.1 at 4k; Llama 3.3 70B Q4_K 32.0 t/s at 4k; GLM 4.5 Air 106B Q4_K 101.1 t/s at 4k — [Hardware Corner](https://www.hardware-corner.net/gpu-llm-benchmarks/rtx-pro-6000-blackwell/). Earlier guide (llama.cpp 6112): gpt-oss-120b 148.17 t/s at 12k context with flash attention, 83.03 at 131k — [Hardware Corner guide](https://www.hardware-corner.net/guides/rtx-pro-6000-gpt-oss-120b-performance/)
- 1x RTX PRO 6000, Ollama single stream: gpt-oss-120b about 134 tok/s — [DatabaseMart Ollama](https://www.databasemart.com/blog/ollama-gpu-benchmark-pro6000)
- TensorRT-LLM 1.2.0 official tables, "RTX 6000 Pro Blackwell Server Edition", unit "output tokens per second per GPU", FP4 ModelOpt checkpoints, throughput mode with "--concurrency -1" (all requests queued): Llama 3.3 70B FP4 at 1024/1024: 1 GPU 1,724; 2 GPU (PP2) 1,881; 4 GPU (PP4) 1,798; 8 GPU (PP8) 1,545. At 8192/1024: 306 / 329 / 323 / 307. Qwen3 235B A22B FP4 at 1024/1024: 4 GPU (PP4) 1,529; 8 GPU (PP8) 1,185. At 8192/1024: 343 / 337 — [TensorRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/1.2.0/developer-guide/perf-overview.html)
- Packet.ai, 1x RTX PRO 6000, vLLM, Llama 3.1 70B Q4_K_M: batch 1 = 18 tok/s, batch 8 = 62, batch 32 = 118, batch 64 = 142 (TTFT 1,240 ms at 64). Page does not say aggregate or per-stream — [packet.ai](https://packet.ai/blog/blackwell-rtx-pro-6000-inference)
- Petronella's 4x/8x RTX PRO 6000 vLLM page has no measured numbers; it lists system prices "4x: $20K to $28K" and "8x: $40K to $56K", which do not match today's card prices — [petronellatech.com](https://petronellatech.com/hardware/rtx-6000-pro-blackwell-multi-gpu-vllm/)
- GLM-4.6 FP8 on RTX PRO 6000 (any count): not found. Qwen3 235B on vLLM: not found (only the TensorRT-LLM table above).

### Inferences
- 4x RTX PRO 6000 aggregate estimates from the TensorRT-LLM per-GPU table: Llama 3.3 70B FP4 at 1024/1024 = 4 × 1,798 = 7,192 output tok/s; Qwen3 235B FP4 = 4 × 1,529 = 6,116 output tok/s. 8x: Llama 70B = 8 × 1,545 = 12,360; Qwen3 235B = 8 × 1,185 = 9,480 (estimates: aggregate = per-GPU × count; PP configs are pipeline parallel, so real single-model scaling is sub-linear and these tables already reflect that).
- gpt-oss-120b on 4x: the model fits one card. Running 4 independent replicas behind a load balancer gives about 4 × 1,525 = 6,100 output tok/s at 50 prompts each (estimate; assumes linear replica scaling, which CloudRift saw for 1x to 4x 5090 on a 30B model).
- Price of a 4x RTX PRO 6000 build today (estimate): Bizon X7000 G3 base $20,653 + 4 × $16,956 (Max-Q, Saitech) = $88,477; with Server Edition 600W cards 4 × $17,850 = $92,053. Using the tower X5500 G2 base $9,076 + 4 × $16,956 = $76,900. Bizon's own configured prices were not visible.
- 8x RTX PRO 6000 (estimate): $20,653 + 8 × $17,850 = $163,453 (over $150,000). 6x: $20,653 + 6 × $17,850 = $127,753.
- Power: Server Edition 600W × 4 = 2,400W GPUs plus roughly 500W to 700W for dual EPYC, RAM, fans = about 2.9 to 3.1 kW peak (estimate). Max-Q 300W × 4 = 1,200W plus ~500W = about 1.7 kW (estimate). Exxact measured each Max-Q card at the full 300W.

### Gaps
- No live, in-stock, priced listing for a complete 4x or 8x RTX PRO 6000 system was found. Bizon shows "In Stock" and ship dates but hides configured prices.
- B&H, CDW, Newegg, Provantage, Insight, Connection card prices: blocked (HTTP 403).
- No vLLM or SGLang multi-GPU (4x/8x) measurement on RTX PRO 6000 for gpt-oss-120b, Llama 70B FP8/NVFP4, Qwen3 235B, or GLM-4.6 FP8 was found. Only TensorRT-LLM FP4 tables exist.

## Key question 3: 4x RTX 5090 boxes: price, stock, measured 70B throughput

### Takeaway
AVADirect sells a configurable 5U 4x RTX 5090 liquid-cooled rackmount at $56,149 as configured, but the page shows no stock text and the configurator warned the item "can not be added to the cart" until issues are resolved. Bizon's in-stock X5500 G2 tops out at 2x 5090. CloudRift measured 4x 5090 at 4,622 output tok/s on GLM-4.5-Air AWQ and 2x 5090 at 1,230 output tok/s on Llama 3.3 70B AWQ-INT4, and found 4x scaled only about 40 percent over 2x on 70B.

### Cited Findings
- AVADirect "AMD WRX90 4x RTX 5090 Liquid Cooled Rackmount Workstation": "Configured price $56149", "4 x GIGABYTE GeForce RTX 5090 WINDFORCE OC 32G", PSUs "Super Flower Leadex Titanium 2800W" plus "SILVERSTONE Extreme 1200R 1200W", chassis "SILVERSTONE RM52 ... 5U Chassis", warranty "AVA Basic (2-Year Labor / 1-Year Parts)". No stock or availability text; the configurator shows the item "can not be added to the cart" until listed issues are resolved — [avadirect.com](https://www.avadirect.com/AMD-WRX90-4x-RTX-5090-Liquid-Cooled-Rackmount-Workstation/Configure/19763558)
- Bizon X5500 G2: "Up to 2× NVIDIA RTX 5090", "In Stock", "Ships within 1-3 days" — [bizon-tech.com](https://bizon-tech.com/bizon-x5500.html)
- System76 Thelio Mega offers "32 GB NVIDIA Geforce RTX 5090" with up to 3 GPUs total — [system76.com](https://system76.com/desktops/thelio-mega)
- Single RTX 5090 at Saitech: PNY VCG509032TFXPB1 "$9,063.00", "Get a Quote" — [esaitech.com](https://esaitech.com/search?q=H100)
- Comino Grando page (reported 4x/7x 5090 "in stock" by TechRadar) returned 404 today — [comino.com/grando](https://www.comino.com/grando)
- CloudRift, vLLM, 400 concurrent, 1000/1000 tokens, fp8 KV cache: Qwen3-Coder-30B-A3B AWQ 1x 5090 = 4,570 output tok/s, 4x 5090 = 12,744; Llama-3.3-70B-AWQ-INT4 2x 5090 = 1,230; GLM-4.5-Air-AWQ-4bit 4x 5090 = 4,622. The 4x config was "only about 40% faster than 2x" on 70B, attributed to PCIe bottlenecks — [CloudRift](https://www.cloudrift.ai/blog/benchmarking-rtx-gpus-for-llm-inference)
- 2x RTX 5090, Ollama single stream, Llama 3.3 70B 4-bit: about 26.85 tok/s — [DatabaseMart](https://databasemart.com/blog/ollama-gpu-benchmark-rtx5090-2)
- Llama 70B FP8 on 4x 5090 with vLLM: not found. Only AWQ INT4 results exist.

### Inferences
- Tokens per dollar on GLM-4.5-Air AWQ: 4x 5090 at $56,149 gives 4,622 tok/s, or $12.15 per tok/s. One RTX PRO 6000 card at $16,956 gives 3,169 tok/s, or $5.35 per tok/s (card only, no chassis). The single 96 GB card beats the 4x 5090 box on tokens per dollar and on memory for 70B-class models.
- Llama 70B AWQ: 2x 5090 = 1,230 tok/s; 4x 5090 estimate = 1,230 × 1.4 = 1,722 tok/s (CloudRift's "about 40%" uplift). One RTX PRO 6000 = 1,031 tok/s. So 4x 5090 is about 1.7x one PRO 6000 at 3.3x the card cost.

### Gaps
- No vendor page showed "In stock" text for a complete 4x 5090 system today.
- No FP8 Llama 70B result on 4x 5090 was found.

## Key question 4: DGX Spark, DGX Station GB300, and GB10 clones: price, stock, throughput

### Takeaway
DGX Spark is sold through partners; NVIDIA's page shows "Sign up To Be Notified on Availability" and no price. Saitech lists the NVIDIA Founders Edition at $4,825 and the PNY version at $5,835, quote-only. DGX Station GB300 is orderable from Exxact at "Starting Price: $96,250.00" (Valence) or $98,893.30 (TensorEX) with no lead time shown; an EU reseller tracker updated 2026-10-13 lists US-dollar prices from $99,000 (Supermicro, 12 to 16 weeks) to $188,500 (Dell, 2 weeks) and says NVIDIA must approve each purchase, which takes 14 to 30 days. A single Spark decodes gpt-oss-120b at about 50 tok/s; two linked Sparks reach about 290 to 323 output tok/s at concurrency 32.

### Cited Findings
- NVIDIA DGX Spark page: "Up to 128 GB Unified Memory", 240 W power supply, GB10 TDP 140 W, buttons "Buy Now" and "Sign up To Be Notified on Availability", retail partners Amazon, Micro Center, PNY, TD SYNNEX, Best Buy; OEM systems Acer Veriton GN100, ASUS Ascent GX10, Dell Pro Max, Gigabyte AI TOP ATOM, HP ZGX Nano, Lenovo, MSI. No price on the page — [nvidia.com DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
- Saitech: "NVIDIA 940-54242-0000-000 DGX Spark Founders Edition... Sale price $4,825.00, Get a Quote"; "PNY NVDGXSPARK-PB... Sale price $5,835.00, Get a Quote" — [esaitech.com](https://esaitech.com/search?q=DGX)
- Cached Newegg listings (undated): ASUS Ascent GX10 1TB at $2,999 and $3,999.99 in different results; NVIDIA DGX Spark 4TB $4,199.99; one listing out of stock — [newegg.com](https://www.newegg.com/p/pl?d=spark). NVIDIA's reservation price was reported at $3,999 — [TechRadar](https://www.techradar.com/pro/project-digits-is-now-dgx-spark-nvidia-raises-its-price-by-33-percent-as-hpe-dell-jump-on-petaflop-mini-ai-bandwagon)
- ASUS Ascent GX10 US page shows no price or stock, only "Shop on ASUS Store" — [asus.com](https://www.asus.com/us/displays-desktops/desktops/ascent/asus-ascent-gx10/). Dell Pro Max GB10 and HP ZGX Nano pages returned navigation only or 404 today.
- NVIDIA Marketplace page timed out twice; Micro Center returned 403.
- DGX Station GB300 (NVIDIA): "748 GB of coherent memory", "252 GB HBM3e ECC | 7.1 TB/s", "496 GB LPDDR5X ECC | 396 GB/s", "Total System Power: 1,600 W | 20A circuit required", "Sign up to be notified when DGX Station becomes available", "Order Now... Contact a partner" — [nvidia.com DGX Station](https://www.nvidia.com/en-us/products/workstations/dgx-station/)
- Exxact Valence VWS-158270643 DGX Station: "Starting Price: $96,250.00", buttons "Customize" and "Get a quote", no lead time text — [exxactcorp.com](https://www.exxactcorp.com/Exxact-VWS-158270643-E158270643). Exxact TensorEX TWS-188490844: "Starting Price: $98,893.30", no lead time — [exxactcorp.com](https://www.exxactcorp.com/Exxact-TWS-188490844-E188490844)
- pi3g reseller tracker, "last updated on 13.10.2026": Supermicro Super AI Station GB300 $99,000, 12-16 weeks; MSI WS300 $104,500, 8-12 weeks; Exxact Valence $105,000, 8 weeks; Gigabyte W775 $112,000, 8-10 weeks; ASUS ET900N G3 $123,500, 6-12 weeks; HP ZGX Fury $148,500, 4-5 weeks; Dell Pro Max GB300 $188,500, 2 weeks. "Final pricing is set after NVIDIA approves your purchase." Prices "may rise 10-20% or more in the coming weeks because of memory costs." — [pi3g.com](https://pi3g.com/?p=31780). NVIDIA approval "can take 14 to 30 days" — [pi3g FAQ](https://pi3g.com/?p=31903)
- DGX Spark throughput, single unit: gpt-oss-120b "50 tokens/s" and gpt-oss-20b "around 70 tokens/s" with SGLang — [LMSYS](https://lmsys.org/blog/2025-11-03-gpt-oss-on-nvidia-dgx-spark); vLLM about 59 tok/s, dropping to about 26 with --enforce-eager — [ai-muninn.com](https://ai-muninn.com/en/blog/part2-gpt-oss-120b-serve-script); llama.cpp MXFP4 about 55 tok/s — [NVIDIA blog](https://developer.nvidia.com/blog/?p=107650)
- Two linked DGX Sparks, gpt-oss-120b, 100 ShareGPT prompts, concurrency 32: vLLM 292.46 output tok/s (TTFT 100.56 ms); SGLang 323.21 output tok/s with CUDA graphs; TensorRT-LLM 62.13 output tok/s. Single request SGLang two nodes 75.12 tok/s, one node 52 tok/s; vLLM one node 36, two nodes 55 — [NVIDIA forums](https://forums.developer.nvidia.com/t/setting-up-vllm-sglang-or-tensorrt-on-two-dgx-sparks/353338)
- DGX Station GB300 measured LLM throughput: not found.

### Inferences
- Tokens per dollar for Spark on gpt-oss-120b: two Sparks at 2 × $4,825 = $9,650 give about 300 output tok/s at c=32, or about $32 per tok/s (estimate). A single RTX PRO 6000 card at $16,956 gives 1,525 output tok/s at 50 prompts, or about $11 per tok/s. Sparks lose by about 3x on tokens per dollar for batched serving.
- DGX Station timing risk: NVIDIA approval (14 to 30 days) plus 2 to 16 weeks vendor lead time from an order placed 2026-10-22 lands between mid-November and late February 2027. Only the Dell (2 weeks) and HP (4 to 5 weeks) entries on the EU tracker clearly fit a December 15 target, and those are EU-reseller quotes. Exxact's US page shows no lead time.

### Gaps
- Live US retail stock text for DGX Spark (Micro Center, NVIDIA Marketplace, Amazon): blocked or timed out.
- Dell Pro Max GB10, HP ZGX Nano prices: not found today.
- Any DGX Station GB300 throughput measurement: not found.

## Key question 5: Used and refurbished datacenter servers in stock (8x H100 SXM, 8x A100, H100 PCIe/NVL cards)

### Takeaway
No in-stock, priced 8x H100 or 8x A100 server was found at any US reseller today. Cloud Ninjas lists a refurbished Dell XE9680 and a Supermicro SYS-821GE at $375,000 each with "Availability: 0 in stock", and ServerPartDeals lists a refurbished XE9680 at $180,000 marked "Out of stock". DGX A100 sellers (Procurri, Viperatech) are quote-only. H100 NVL cards show $29,799 quote-only at Saitech. All of these sit above the $150,000 cap anyway, except single cards.

### Cited Findings
- Cloud Ninjas Dell PowerEdge XE9680, 8x HGX H100 80GB SXM, 2048GB RAM, "Used/Refurbished": "$375,000.00", "Availability: 0 in stock.", button "Sold out" — [cloudninjas.com](https://cloudninjas.com/products/dell-poweredge-xe9680-gpu-server). A search snippet showed the same listing at $170,000 in another version; the live page today says $375,000.
- Cloud Ninjas Supermicro SYS-821GE-TNHR, 8x HGX H100 80GB SXM5, 1024GB RAM, "18 Month" warranty, "Refurbished Condition": "$375,000.00", "Availability: 0 in stock", "Sold out", "Customer is required to sign GTC paperwork at the time of purchase." — [cloudninjas.com](https://cloudninjas.com/products/used-supermicro-sys-821ge-tnhr-server)
- ServerPartDeals: "Dell PowerEdge XE9680 Xeon Platinum 8462Y+ 8x NVIDIA HGX H100 80GB SXM5 NVLink AI-Powered Refurbished GPU Server", "$180,000.00", "Out of stock", "Sold out" — [serverpartdeals.com](https://serverpartdeals.com/search?q=H100)
- Enterasource Supermicro AS-8125GS-TNHR refurbished: "Availability: Available by Quote", "Price on Request" — [search summary](https://www.enterasource.com/servers/shopby/sata)
- Procurri DGX A100 (8x A100 80GB, 2TB RAM, 30TB NVMe): no price; "NVIDIA DGX A100 Servers available!" and "Limited stock—don't miss out!"; purchase via form; UK contact details — [procurri.com](https://www.procurri.com/?p=150919)
- Viperatech "NVIDIA DGX A100 Units In Stock and Primed for Immediate Dispatch!" post is dated 2023-08-15 and gives no price — [viperatech.com](https://viperatech.com/news-details/viperatech-exclusive-nvidia-dgx-a100-units-in-stock-and-primed-for-immediate-dispatch)
- Saitech new H100 servers, quote-only: "ASUS ESC N8-E11... HGX H100 8GPU... $283,293.00, Get a Quote"; "ASRock 6U8X-EGS2 H100... $292,915.00, Get a Quote" — [esaitech.com](https://esaitech.com/search?q=H100)
- Saitech H100 NVL card: "NVIDIA H100 NVL NVH100NVLTCGPU-KIT... Sale price$29,799.00", "Get a Quote" — [esaitech.com](https://esaitech.com/search?q=H100)
- CDW PNY H100 80GB PCIe: $32,411.99 as of 2026-09-21 but "Discontinued" per a tracker — [gpuperhour.com](https://gpuperhour.com/blog/nvidia-h100-price)
- eBay, TheServerStore, UnixSurplus, ServerMonkey, PCServerAndParts, Micro Center: HTTP 403 or 404 to the fetcher today. Cloud Ninjas and ServerPartDeals GPU collection pages: 404.
- Used A100 80GB card price estimates conflict: $4,000 to $9,000 in one guide versus $12,000 to $18,000 in another — [directmacro.com](https://directmacro.com/blog/post/nvidia-a100-in-2025)

### Inferences
- The used 8x H100 SXM market is both out of stock at the two US resellers checked and priced at $180,000 to $375,000, so it fails the budget and the stock test.
- Used DGX A100 at "a fraction of new" is quote-only; no number can be recorded.

### Gaps
- A firm in-stock price for any 8x H100 or 8x A100 server: not found.
- 4x or 8x H100 PCIe servers in stock: not found.
- H100 PCIe / NVL stock text at Newegg, Provantage, CDW, Insight: blocked.

## Key question 6: AMD options (MI300X/MI325X servers, Radeon AI PRO R9700, Ryzen AI Max+ 395 mini PCs)

### Takeaway
MI300X servers are quote-only at the resellers checked, with no stock text. The R9700 (32 GB, about $1,880 at Puget) is the only AMD part with multi-card vLLM data; tinybox's $19,000 6x R9700 box is the cheapest 192 GB machine found but is made to order. Every 128 GB Ryzen AI Max+ 395 mini PC checked is out of stock or pre-order, and the Framework Desktop 128 GB now lists at $3,449.

### Cited Findings
MI300X / MI325X:
- Saitech lists ASRock 6U8M-GENOA2 MI300X, Gigabyte G593-ZX1-LAX1 MI300X, ASRock 6U8M-TURIN2 MI300X servers with no price and only "Get a Quote" — [esaitech.com](https://esaitech.com/search?q=MI300X)
- Supermicro AS-8125GS-TNMR2 (8x MI300X, 8U, "6x 3000W Redundant (3 + 3)") product page shows no price or lead time; buy via "eStore" or "Buy from Our Partners" — [supermicro.com](https://www.supermicro.com/en/products/system/gpu/8u/as-8125gs-tnmr2). The eStore search returned only filter counts.
- TensorWave appears only as a cloud provider at "$1.71" per GPU-hour, "Quote-only"; the page does not say where to buy MI300X servers outright — [thundercompute.com](https://www.thundercompute.com/blog/amd-mi300x-pricing)
- MI300X purchase price: only a 2024 Citi-based report of about $10,000 to $15,000 per GPU — [techpowerup forum](https://techpowerup.com/forums/goto/post?id=5191220)

Radeon AI PRO R9700:
- Puget: R9700 is 32 GB GDDR6, 640 GB/s, 300 W; "About $1,880 at Puget Systems pricing as of July 2026. AMD's MSRP is $1,299." — [pugetsystems.com](https://www.pugetsystems.com/labs/articles/amd-radeon-ai-pro-r9700-dual-gpu-ai-inference-performance/)
- Puget vLLM ROCm v0.20.2, 2x R9700 TP=2, Qwen3.6-27B FP8: stock vLLM 15.88 tok/s at c=1, 156.21 at c=8; tuned build 198.78 at c=8; tuned plus MTP speculative decoding 62.75 at c=1 and 320.23 at c=8. 1x R9700 Llama 3.1 8B FP16: 29.1 / 102 / 153 tok/s at c=1/4/8 — [pugetsystems.com](https://www.pugetsystems.com/labs/articles/amd-radeon-ai-pro-r9700-dual-gpu-ai-inference-performance/)
- ASRock vendor test, vLLM ROCm, gpt-oss-20b: one card about 60 tok/s single request, about 1,494 tok/s peak under continuous batching; two cards (TP) about 117 tok/s single request and about 3,057 tok/s batched — [asrock.com blog](https://asrock.com/blog/blog-details.asp?id=6) (page fetch returned empty today; numbers come from the search index summary of that page)
- Multi-card R9700 boxes: tinybox red flash G4, 6x R9700, $19,000, made to order (see Key question 1). Velocity Micro's R9700 page returned 307 today. Exxact and Bizon R9700 configs: not found.
- US R9700 card stock: BuildCores snapshots showed PowerColor at Amazon $1,550 "in stock" and Newegg $1,599.99 out of stock; ASRock Creator $1,699.99 in stock; undated — [buildcores.com](https://www.buildcores.com/products/GPU/780usqig9/ASRock-AMD-Radeon-AI-PRO-R9700-Creator-32GB-GDDR6)

Ryzen AI Max+ 395 128 GB:
- Framework Desktop "Max+ 395 - 128GB": "$3,449", "(Out of stock)"; general text "Ships within 5 business days"; a separate "AI Max PRO 400 Series" is "Pre-order" from "$6,799.00" — [frame.work configurator](https://frame.work/products/desktop-diy-amd-aimax300/configuration/new)
- GMKtec EVO-X2: 64GB/1TB "Sale price $2,199.99"; both 128GB variants "Variant sold out or unavailable"; vendor benchmark "GPT-OSS: 120B 19.25 tokens/s", "Qwen3: 235B 11 tokens/s" — [gmktec.com](https://www.gmktec.com/products/amd-ryzen™-ai-max-395-evo-x2-ai-mini-pc)
- Beelink GTR9 Pro 128GB/2TB: "$4,349.00" (reference $4,699.00), "Pre-order Shipping time is approximately 35 days." — [bee-link.com](https://www.bee-link.com/products/beelink-gtr9-pro-amd-ryzen-ai-max-395)
- HP Z2 Mini G1a: page timed out; not found.

### Inferences
- A 6x R9700 tinybox has 192 GB, enough for gpt-oss-120b MXFP4 (about 65 GB file per Hardware Corner) or Llama 70B FP8 (about 70 GB). Throughput is unknown. Scaling ASRock's 2-card gpt-oss-20b figure to three 2-card pairs gives about 3 × 3,057 = 9,171 tok/s on the 20B model (estimate; a 20B MoE, not comparable to 120B).
- Ryzen AI Max+ 395 boxes serve gpt-oss-120b at about 19 tok/s single stream (vendor). They are not viable as a paid-API backbone at that rate, and none are in stock.

### Gaps
- Any in-stock, priced MI300X or MI325X server: not found.
- R9700 throughput on gpt-oss-120b or Llama 70B across 4 or 6 cards: not found.
- HP Z2 Mini G1a price and stock: not found.

## Key question 7: Where to put it with no physical work (ship-to-colo with remote hands), with prices and power limits

### Takeaway
Published, fetchable prices exist at Psychz (Ashburn/Dallas; full 42U cabinet 4.99 kW at $2,332/month month-to-month or $1,058/month on a 1-year term), ColoCrossing (full cabinet 3.84 kW $1,399), Cyber Wurx Atlanta (42U 2 to 5 kW from $1,299), Hurricane Electric Fremont (42U cabinet with power and 1 Gbps for $600/month, power amount not stated), and MillionMiner (Nebraska/Missouri/Mississippi, "$0.075 per kWh, all-inclusive" for a single node up to 20 kW, month-to-month, remote hands included, explicitly accepts shipped H100/RTX servers). Cheap 1U plans (ColoCrossing $59, Colocation America $75, Cyber Wurx $99) include only 1 to 2 amps and cannot power a GPU box. TRG Houston advertises free best-effort remote hands and immediate availability but prints no price. Bay Area and Nevada options (Evocative, Colovore, Switch, Flexential) are quote-only; Colovore now starts at 1 MW.

### Cited Findings
- Hurricane Electric (Fremont 1 and 2, San Jose): "$600/month Cabinet + Gige", "Includes 42U Cabinet, Power, 1 Gbps Internet bandwidth", "Limit one per customer", "24 x 7 x 365 Remote Hands" listed as a feature. No per-U pricing, no power amount, no setup fee, no term stated — [he.net/colocation.html](https://www.he.net/colocation.html). A 2015 forum post described the same deal at $400 with 15A/120V — [lowendtalk](https://lowendtalk.com/discussion/comment/1317671/) (dated, anecdotal)
- Psychz Networks (tabs "Ashburn Data Center" and "Dallas Data Center"; Los Angeles listed as a location): Half Cabinet 20U "approximately 2kW (8A/120V or 4A/208V)", "$0" setup, "$599/month", "Based on availability". Full Cabinet 42U, setup "$2,250": 1.92kW 20A/120V $907; 2.88kW 30A/120V $1,344; 3.33kW 20A/208V $1,563; 4.99kW 30A/208V $2,332. On a 1-year agreement: half cabinet 1.92kW $454 ($0 setup); locking full cabinet 1.92kW $608 and 4.99kW $1,058 (setup $500). Includes 1Gbps uplink, DDoS protection, 24/7 staff. "most commitments are month-to-month". Accepts shipped equipment (lists what to ship; "Shipping costs can vary widely, so we pass these costs on to our customer"). "Ask about our power-based (per-kW) options" for single AI/GPU servers, no rate printed. Tower hardware not mentioned — [psychz.net/colocation.html](https://www.psychz.net/colocation.html)
- ColoCrossing: "Single Server $59/mo 1U 1A/120V"; "Half Cabinet $699/mo 20U 1.92 kW of 20A/120V"; "Full Cabinet $1,399/mo 42U 3.84 kW of 20A/120V"; "Cage Space $2,499/mo 2 x 42U 7.68 kW"; 100 Mbps transfer, 1 Gbps port, /29. Remote hands is an add-on with no price. Setup, term, tower acceptance not stated — [colocrossing.com](https://www.colocrossing.com/colocation/)
- Cyber Wurx (CoreSite AT2, Atlanta): "Node 1U shared $99" (up to 1.0A); "Core 10U $459" (8–10A shared 30A/120V); "Edge 20U $695" (dedicated 20A/120V; 30A/120V $949); "Apex 42U $1,299" (2kW to 5kW); fixed list 42U 30A/208V $1,699 single feed; remote hands "first 5 minutes are free", further pricing not listed; "ship or bring your equipment" — [cyberwurx.com](https://www.cyberwurx.com/colocation/)
- Colocation America: 1U "$75/month", "2 Amps at 120V AC", 10 Mbps; 4U "$199/month"; "basic remote hands and reboots included at no additional cost" (third-party plan listing; the provider's own pages returned 403/404 today) — [whtop.com](https://www.whtop.com/plans/colocationamerica.com/5888)
- Sectorlink tower colocation: "Tower Server Colocation from $65/month", full tower "$75/mo", "2 Amp 120V AC POWER", 1Gbps unmetered, "No setup fees", "Ship your server to us, and our team will place it, connect it, and help get it online." Location not stated — [sectorlink.com](https://www.sectorlink.com/data-center-colocation/tower-server-colocation)
- LinkSecured Networks (Los Angeles, also Phoenix and Dallas): "1U going for only $69/month" with "100W of UPS Power"; "2KW Colocation – LAX – $699/mo"; "Free Rack and Stack"; post dated 2025-03-13 — [lowendbox.com](https://lowendbox.com/?p=47734). The provider's own site returned 403 today.
- TRG Datacenters (Houston HOU1/HOU2-3; Dallas "Available from Q2 2027"): rack prices print as "from $ /month" with the number missing; "Immediate availability in Houston"; "5c/kWh metered power options"; "non-emergency, non-SLA'd 'best effort' free remote hands-on tier that is entirely free"; "Simply send us your gear or we'll come and pick it up"; half racks "provide the full 20Amp, 120V power supply" — [trgdatacenters.com H100 colo](https://www.trgdatacenters.com/colocation/nvidia-h100/), [trgdatacenters.com colocation](https://www.trgdatacenters.com/colocation/). A search snippet of the same page showed "half racks from $499/m in Houston" and "$399/m in Dallas"; the live fetch did not show those numbers.
- MillionMiner (Nebraska 25 MW, Missouri A and B 25 MW each, Mississippi 20 MW): "Tier 1 (single node to 20 kW) $0.075 per kWh, all-inclusive"; "Tier 2 (20–200 kW) $0.07 per kWh + metered rack space"; "No setup fee, no maintenance surcharge, no egress bill"; "All bands include power, cooling, physical security, network transit and remote hands"; "24/7 on-site remote hands"; Tier 1 "Month-to-month available"; FAQ: "Yes. Ship us the H100, H200, A100, L40S or RTX servers you already own" — [millionminer.com/gpu-hosting](https://millionminer.com/gpu-hosting)
- Hivelocity (Tampa, Dallas, LA, NY, Chicago and more): no colocation prices on the page; "Request a Quote"; TurnKey Internet's colocation URL now redirects to hivelocity.net — [hivelocity.net/colocation](https://www.hivelocity.net/colocation/), [turnkeyinternet.net redirect](https://turnkeyinternet.net/colocation/)
- Evocative (San Jose, Santa Clara x3, Los Angeles, Phoenix, Seattle, Plano and others): no prices, "Remote Hands" shown as included feature, "You can supply us with your racks, or we can provide them" — [evocative.com](https://evocative.com/colocation/)
- Colovore (Silicon Valley): "5-600+ kW per rack", deployments "start at 1 MW"; no pricing — [colovore.com](https://www.colovore.com/)
- Wowrack (Seattle Tukwila and Westin): no prices; "High Density Power Racks support 20-100kW"; remote hands lists "Shipping & Receiving / Equipment RMA" — [wowrack.com](https://www.wowrack.com/en-us/x/colocation/)
- Joe's Datacenter (Kansas City): colocation page shows "This Account has been suspended." — [joesdatacenter.com](https://www.joesdatacenter.com/colocation/)
- QuadraNet: a LowEndBox post says QuadraNet's Los Angeles operation shut down and referred customers to LinkSecured — [lowendbox.com](https://lowendbox.com/?p=47734)
- HostDime, Psychz LA, Flexential, Data Foundry, Switch Reno, Hydra Host, Applied Digital, Core Scientific, Hut 8, Soluna: no published per-U or per-kW colocation prices found; HostDime pages returned 404; the others are quote-only or operate their own clouds — [Hydra Host](https://hydrahost.com/data-center/), [Applied Digital](https://applieddigital.com/applied-digital-cloud)
- Market per-kW benchmark: CloudRift's January 2026 model uses "$185/kW per month" within "$170–200/kW/month" for Tier 3 markets, "$150 per month" remote hands, 8x RTX PRO 6000 SE server "6.8 kW" (Max-Q about 4 kW), 8x H100 "10.2 kW"; resulting colocation cost "$1,258/month" (RTX PRO 6000 SE) and "$1,887/month" (H100) — [cloudrift.ai](https://www.cloudrift.ai/blog/the-true-cost-of-gpu-ownership)

### Inferences
- A 4x RTX PRO 6000 Server Edition box (about 3 kW peak, estimate above) needs at least a 20A/208V circuit (3.33 kW license; 80 percent continuous rating = 2.66 kW, so it is tight) or 30A/208V (4.99 kW). Psychz's 42U 4.99 kW plan at $2,332 month-to-month ($2,250 setup) or $1,058 on 1 year ($500 setup) fits. A 4x Max-Q box (about 1.7 kW) fits a 20A/120V half cabinet (1.92 kW license; 1.54 kW at 80 percent continuous, marginal) such as Psychz $454 to $599, ColoCrossing $699, Cyber Wurx $695, or TRG's half rack.
- MillionMiner cost for a 4x box: 2.5 kW × 730 h = 1,825 kWh × $0.075 = $137/month (estimate) and for an 8x H100 class box: 10 kW × 730 = 7,300 kWh × $0.075 = $548/month (estimate). This is the cheapest published rate found but it is in Nebraska, Missouri, or Mississippi, not California.
- Nearest published-price option to Redwood Shores: Hurricane Electric Fremont at $600/month for a 42U cabinet with power and 1 Gbps. The page does not state the power cap; a GPU box at 3 kW likely exceeds the bundled circuit, so the real price needs a quote.
- Tower acceptance: only Sectorlink says it accepts towers, but at 2A/120V (240 W) it cannot run a GPU workstation. A 4U rackmount (Bizon X7000 G3 or G7000 G4) avoids the tower problem.
- Remote hands for the initial install: TRG (free, best effort) and MillionMiner (included) are the only providers that print "free" or "included" for remote hands; Cyber Wurx gives the first 5 minutes free. All others are unpriced.

### Gaps
- Per-U pricing at Hurricane Electric, Hivelocity, Evocative, Flexential, Switch, Data Foundry, HostDime, Wowrack, Psychz LA: not published.
- Hourly remote-hands rates at every provider except MillionMiner and TRG: not found.
- Whether any provider other than Sectorlink accepts tower workstations: not stated.
- TRG's actual half-rack and full-rack prices: the live page prints blanks.

## Key question 8: Hosted bare metal with the same GPUs plus buy-to-own or lease, and the tax treatment

### Takeaway
No public rent-to-own, lease-to-own, or buy-later program was found at Lambda, Hot Aisle, Hivenet, Exxact, or Supermicro. Dell Financial Services offers $1-buyout and FMV leases of 24 to 60 months and a Dell Pay Pro installment plan where "Customer owns the equipment after a contract is entered into." IRS Publication 946 says a lessee can depreciate leased property "only if you retain the incidents of ownership," and it confirms the One Big Beautiful Bill Act "reinstated the 100% special depreciation allowance" for property acquired and placed in service after January 19, 2025.

### Cited Findings
- Lambda: search results covered only Lambda's own $917M loan and NVIDIA lease-back deals, not a customer lease program — [tomshardware.com](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-signs-usd1-5-billion-deal-with-cloud-startup-lambda-to-rent-back-its-own-ai-chips-18-000-gpus-will-be-leased-over-4-years-as-lambda-gears-up-for-its-ipo). Lambda's on-prem line is discontinued — [lambda.ai](https://lambda.ai/gpu-workstations/vector-pro)
- Hot Aisle: on-demand MI300X "all without contracts, sales calls, or long-term commitments"; no ownership path — [amd.com blog](https://www.amd.com/en/blogs/2025/neocloud-hot-aisle-brings-the-heat.html). Hivenet: rentals from about €0.40/hour, no buyout option — [hivenet.com](https://www.hivenet.com/fr/post/best-solutions-to-rent-gpu-online-for-deep-learning-ai)
- Exxact: homepage shows no financing or leasing text; /financing returns 404 — [exxactcorp.com](https://www.exxactcorp.com/)
- Dell Financial Services: described as offering "installment agreements, $1-buyout and fair-market-value leases over 24 to 60 months" for servers and AI infrastructure — [amcompute.com](https://www.amcompute.com/lenders/dell-financial-services). Dell's own page: Dell Pay Pro "Customer owns the equipment after a contract is entered into and customer makes equal monthly installments"; "Offers not available for personal, family or household use." — [dell.com DFS](https://www.dell.com/en-us/lp/dell-financial-services). A Dell promotional "technology ownership offer" was 3.99% on 36-month finance leases, $25,000 to $1,000,000 — [delltechnologies.com PDF](https://www.delltechnologies.com/asset/no-no/solutions/financing-and-payment-solutions/briefs-summaries/technology-ownership-offer.pdf)
- RTX PRO 6000 hourly rental reference (to compare against owning): Lium lists "$1.19 per GPU-hour" reference price with "Available now: 0 pods" — [lium.io](https://lium.io/gpu/rtx-pro-6000-blackwell-workstation-edition). H100 on-demand "cheapest... $2.50 per GPU-hour" as of 2026-09-14 — [gpuperhour.com](https://gpuperhour.com/blog/nvidia-h100-price)
- Tax, leased property: "You can depreciate leased property only if you retain the incidents of ownership in the property." Incidents of ownership include legal title, a legal obligation to pay for the property, responsibility for maintenance and operating expenses, the duty to pay taxes on it, and the risk of loss — [IRS Publication 946](https://www.irs.gov/publications/p946)
- Tax, bonus depreciation: the One Big Beautiful Bill Act "reinstated the 100% special depreciation allowance" for "certain qualified property acquired and placed in service after January 19, 2025"; a 40% election is available instead. "You place property in service when it is ready and available for a specific use." — [IRS Publication 946](https://www.irs.gov/publications/p946)
- Secondary sources agree the 100% rate is permanent with no phase-down and that IRS Notice 2026-11 (2026-01-14) gave initial guidance — [instead.com](https://instead.com/resources/blog/how-bonus-depreciation-works-in-2026-under-the-obbba). Section 179 limit reported at $2.5 million with phase-out from $4 million — [xero.com](https://www.xero.com/us/guides/bonus-depreciation-2026/)
- The IRS has discontinued Publication 535, which held the "conditional sales contract" factors; the current page links only to the 2022 PDF — [IRS Publication 535](https://www.irs.gov/publications/p535)

### Inferences
- A $1-buyout (finance/capital) lease from DFS or a bank lessor transfers the incidents of ownership (obligation to pay, risk of loss, maintenance) to the lessee, so the lessee depreciates the equipment and can claim 100% bonus depreciation once it is placed in service. A fair-market-value (operating) lease does not. This is an inference from Publication 946's test; confirm with a CPA.
- Hosted bare metal with the same GPUs does not create a depreciable asset for the renter unless the contract is a conditional sale. No vendor found offers such a contract publicly.

### Gaps
- A published rent-to-own or lease-to-own GPU program: not found at any vendor checked.
- DFS applicability to non-Dell hardware (for example a Bizon or Exxact server): not confirmed.
- IRS Notice 2026-11 text: not read directly.

## Key question 9: Best tokens per dollar in stock today under $50,000 and under $150,000

### Takeaway
Under both caps the best evidenced option is RTX PRO 6000 Blackwell cards in a Bizon 4U server that Bizon marks "In Stock" with October ship dates. Under $50,000 that is two cards (about $52,000 estimate, slightly over); under $150,000 it is six cards (about $128,000 estimate). The 4x RTX 5090 box, DGX Spark pairs, and tinybox G5 all cost more per token per second.

### Cited Findings
- Per-card and system prices and the throughput figures are cited in Key questions 2, 3, 4, and 1.

### Inferences (all arithmetic shown; all are estimates)
| Machine | Price basis | Throughput basis | $ per output tok/s |
|---|---|---|---|
| 1x RTX PRO 6000 card only ($16,956 Saitech) | $16,956 | Llama 3.3 70B FP4 TRT-LLM 1,724 tok/s/GPU | $16,956 / 1,724 = $9.84 |
| 1x RTX PRO 6000 card only | $16,956 | GLM-4.5-Air AWQ vLLM 3,169 tok/s | $5.35 |
| 1x RTX PRO 6000 card only | $16,956 | gpt-oss-120b vLLM 1,525 output tok/s | $11.12 |
| Bizon G7000 G4 + 2x RTX PRO 6000 Max-Q | $17,731 + 2 × $16,956 = $51,643 | 2 × 1,881 (PP2) = 3,762 tok/s Llama 70B FP4 | $13.73 |
| Bizon X7000 G3 + 4x RTX PRO 6000 SE | $20,653 + 4 × $17,850 = $92,053 | 4 × 1,798 (PP4) = 7,192 tok/s Llama 70B FP4 | $12.80 |
| Bizon X7000 G3 + 6x RTX PRO 6000 SE | $20,653 + 6 × $17,850 = $127,753 | 6 × 1,798 = 10,788 tok/s (uses PP4 per-GPU rate; no PP6 data) | $11.84 |
| AVADirect 4x RTX 5090 | $56,149 | GLM-4.5-Air AWQ 4,622 tok/s | $12.15 |
| AVADirect 4x RTX 5090 | $56,149 | Llama 70B AWQ 2x = 1,230; 4x est 1,230 × 1.4 = 1,722 | $32.61 |
| tinybox green G5 (2x RTX 6000) | $60,000 | 3,762 tok/s Llama 70B FP4 | $15.95 |
| 2x DGX Spark | 2 × $4,825 = $9,650 | gpt-oss-120b ~300 output tok/s at c=32 | $32.17 |
| tinybox red flash G4 (6x R9700) | $19,000 | no 70B or 120B data | not computable |

- Under $50,000: a Bizon X5500 G2 tower with 2x RTX PRO 6000 Max-Q ($9,076 + $33,912 = $42,988 estimate) is the cheapest in-stock path, but a tower is hard to colocate. The 4U G7000 G4 with two cards is about $51,643 (estimate), just over the cap.
- Under $150,000: Bizon X7000 G3 with 6x RTX PRO 6000 (about $127,753 estimate) gives the most throughput per dollar with "In Stock" text. 8x breaks the cap at about $163,453.
- The tinybox is not in stock, is wire-only, and shows "Checkout not connected." Its G5 is about 16 percent worse on $ per tok/s than a Bizon 2-card build and about 25 percent worse than a 4-card build.

### Gaps
- Bizon's configured prices for 2x, 4x, and 6x RTX PRO 6000 builds are not visible without using the configurator (not done; read-only constraint). All system totals above are card price plus base price estimates.

## Key question 10: Three "buy today, ship to colo, remote hands install, serve by December 15" packages

### Takeaway
All three packages use Bizon 4U servers (the only vendor showing "In Stock" and October ship dates for RTX PRO 6000 systems) and a colocation plan with a printed price and shipped-equipment acceptance. Each should arrive at the colo by mid-November, leaving four weeks for install and testing before December 15, and all three qualify for 100% bonus depreciation if placed in service by December 31, 2026 (Publication 946 cited above).

### Cited Findings
- Bizon ship dates: G7000 G4 "Ship date: Oct 23 – Oct 26, 2026"; X7000 G3 "Ship date: Oct 27 – Oct 29, 2026" — [bizon-tech.com](https://bizon-tech.com/bizon-x7000.html)
- Colo prices and remote hands terms: Key question 7.
- Bonus depreciation rule: [IRS Publication 946](https://www.irs.gov/publications/p946).

### Inferences
Buy-now packages (every dollar figure below is an estimate built from the cited component prices; monthly colo is the printed plan price; "total 2026 cash" = machine + setup fee + 2 months of colo; shipping to colo not included; federal deduction = machine price at 100% bonus depreciation, which reduces taxable income by that amount, not tax owed):

| # | Machine | Seller | Price (est.) | Stock text | Throughput (est.) | Colo | Monthly cost | Total 2026 cash | Federal deduction |
|---|---|---|---|---|---|---|---|---|---|
| A | Bizon G7000 G4 4U + 2x RTX PRO 6000 Max-Q (192 GB, ~1.2 kW GPUs) | bizon-tech.com + cards sourced by Bizon (Saitech reference $16,956/card) | $17,731 + $33,912 = $51,643 | "In Stock", "Lead time: 1–4 days", "Ship date: Oct 23 – Oct 26, 2026" | Llama 70B FP4 ~3,762 tok/s; gpt-oss-120b 2 replicas ~3,050 output tok/s | Psychz half cabinet 20U, 1.92 kW, 1-year | $454 | $51,643 + $0 + 2 × $454 = $52,551 | $51,643 |
| B | Bizon X7000 G3 4U + 4x RTX PRO 6000 Server Edition (384 GB, ~3 kW) | bizon-tech.com (Saitech reference $17,850/card) | $20,653 + $71,400 = $92,053 | "In Stock", "Lead time: 5–7 days", "Ship date: Oct 27 – Oct 29, 2026" | Llama 70B FP4 ~7,192 tok/s; Qwen3 235B FP4 ~6,116 tok/s; gpt-oss-120b 4 replicas ~6,100 output tok/s | Psychz locking full cabinet 42U, 4.99 kW, 1-year ($500 setup) | $1,058 | $92,053 + $500 + 2 × $1,058 = $94,669 | $92,053 |
| C | Bizon X7000 G3 4U + 6x RTX PRO 6000 Server Edition (576 GB, ~4.3 kW) | bizon-tech.com (Saitech reference $17,850/card) | $20,653 + $107,100 = $127,753 | same as B | Llama 70B FP4 ~10,788 tok/s; Qwen3 235B ~9,174 tok/s (6 × 1,529) | MillionMiner Tier 1, $0.075/kWh all-inclusive, month-to-month, remote hands included (4.3 kW × 730 h × $0.075 = $235) | $235 | $127,753 + $0 + 2 × $235 = $128,223 | $127,753 |

- Alternative colo for A or B near Redwood Shores: Hurricane Electric Fremont 42U cabinet at $600/month with power and 1 Gbps; the power cap is unstated and must be confirmed by quote before shipping a 3 kW box. Alternative cheap-power option for B: TRG Houston with free best-effort remote hands and "Immediate availability", price by quote.
- Timeline (estimate): order Oct 22 to 23; Bizon ships Oct 23 to 29; ground freight 5 to 7 business days; colo receiving and rack-and-stack 3 to 10 business days; machine online by about November 14 to 21; four weeks of burn-in and vLLM tuning before December 15.
- Power for package C at 6 × 600 W = 3.6 kW GPUs plus ~0.7 kW host = 4.3 kW exceeds a 30A/208V cabinet's 80 percent continuous rating (3.99 kW), so C needs MillionMiner's per-kWh plan, a per-kW quote (Psychz, TRG, Evocative), or Max-Q cards (6 × 300 W = 1.8 kW GPUs, ~2.5 kW total).

Not available today (checked 2026-10-22):
- Lambda Vector Pro and Scalar: discontinued — [lambda.ai](https://lambda.ai/gpu-workstations/vector-pro)
- tinybox (all models): "Made to order. Ships in 1–8 weeks", "Checkout not connected", wire only — [tinygrad.org](https://tinygrad.org/)
- tinybox red (6x 7900XTX), green (6x 4090), green v2 (4x 5090), 8xV2: no longer listed on tinygrad.org
- NVIDIA Marketplace RTX PRO 6000 Workstation Edition: $16,000 and out of stock as of August 2026 reports; live page unreachable today — [letsdatascience](https://letsdatascience.com/news/nvidia-raises-rtx-pro-6000-blackwell-price-again-6d1ae9ff)
- Supermicro eStore RTX PRO 6000 Server Edition card: "Out of stock" — [store.supermicro.com](https://store.supermicro.com/us_en/supermicro-rtx-pro-6000-gpu-nvrtxpro-6k-b-se.html)
- Saitech RTX PRO 6000 (all editions): "In stock: No", special order — [esaitech.com](https://esaitech.com/products/nvidia-vcnrtxpro6000b-pb-rtx-pro-96gb-graphic-card)
- Cloud Ninjas XE9680 and SYS-821GE 8x H100: "0 in stock", $375,000 — [cloudninjas.com](https://cloudninjas.com/products/dell-poweredge-xe9680-gpu-server)
- ServerPartDeals XE9680 8x H100: "Out of stock", $180,000 — [serverpartdeals.com](https://serverpartdeals.com/search?q=H100)
- DGX A100 used: quote-only (Procurri, Viperatech), no price
- MI300X / MI325X servers: quote-only, no stock text (Saitech, Supermicro)
- DGX Station GB300: Exxact from $96,250, no lead time printed; NVIDIA approval 14 to 30 days plus 2 to 16 weeks per EU tracker — [pi3g.com](https://pi3g.com/?p=31780)
- DGX Spark: NVIDIA page "Sign up To Be Notified on Availability"; Saitech quote-only at $4,825 — [nvidia.com](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
- Framework Desktop 128 GB: "$3,449", "(Out of stock)" — [frame.work](https://frame.work/products/desktop-diy-amd-aimax300/configuration/new)
- GMKtec EVO-X2 128 GB: "Variant sold out or unavailable" — [gmktec.com](https://www.gmktec.com/products/amd-ryzen™-ai-max-395-evo-x2-ai-mini-pc)
- Beelink GTR9 Pro 128 GB: "Pre-order Shipping time is approximately 35 days." — [bee-link.com](https://www.bee-link.com/products/beelink-gtr9-pro-amd-ryzen-ai-max-395)
- AVADirect 4x RTX 5090: $56,149 configured, no stock text, cart blocked by configurator warnings — [avadirect.com](https://www.avadirect.com/AMD-WRX90-4x-RTX-5090-Liquid-Cooled-Rackmount-Workstation/Configure/19763558)
- Comino Grando: page 404
- Colovore: "start at 1 MW" — [colovore.com](https://www.colovore.com/)
- Joe's Datacenter: site "This Account has been suspended." — [joesdatacenter.com](https://www.joesdatacenter.com/colocation/)
- QuadraNet Los Angeles: shut down per LowEndBox — [lowendbox.com](https://lowendbox.com/?p=47734)
- TurnKey Internet: redirects to Hivelocity
- Rent-to-own / lease-to-own GPU server programs: none found at Lambda, Hot Aisle, Hivenet, Exxact, Supermicro

### Gaps
- Bizon configured totals, freight quotes, and colo quotes for a specific cabinet were not obtained (read-only constraint; no forms submitted).
- Hurricane Electric's power allowance for the $600 cabinet: not published.
- Retailer pages that blocked the fetcher (B&H, CDW, Newegg, Provantage, Connection, Insight, eBay, Micro Center, TheServerStore, UnixSurplus, ServerMonkey) could not be read today; a browser session would be needed.
