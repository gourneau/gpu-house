# Alternative accelerators for open-weight LLM inference: AMD Instinct, Google TPU, AWS Trainium/Inferentia, Intel Gaudi, ASIC startups, and NVIDIA value tier

Research date: 2026-10-22. Every price and throughput below was read live on 2026-10-22 unless the row says otherwise. "InferenceX" is the SemiAnalysis InferenceMAX dashboard (inferencemax.ai now redirects to inferencex.semianalysis.com). All InferenceX throughput is output tokens per second per chip on a single-turn chat workload with 8K input / 1K output, at a fixed per-user speed. InferenceX cost figures use SemiAnalysis TCO assumptions, not rental prices. I recompute tokens per dollar with live rental prices and mark every such number "estimate".

Tool note: the web search budget ran out near the end. Everything after that point came from direct page fetches. Items I could not reach are listed under Gaps.

## Key Question 0: Per-accelerator fact sheet (where to rent, price by term, memory, devices per replica, measured throughput, software maturity)

### Takeaway
Only AMD Instinct (MI300X, MI325X, MI355X), Google TPU, AWS Trainium2/Inferentia2, and the NVIDIA value tier are rentable today by a solo operator with public prices. Intel Gaudi 3 has no on-demand listing I could find. Qualcomm AI 100 Ultra is monthly-contract only. Tenstorrent is "request access" with no price. Groq, Cerebras, SambaNova, d-Matrix, Positron, Etched, Furiosa, Rebellions, and Taalas do not rent raw hardware to small customers.

### Cited Findings

#### A. AMD Instinct MI300X (192 GB HBM3, 8 per node = 1.5 TB)

Rental prices per GPU-hour (checked 2026-10-22):

| Provider | On-demand | Term pricing | Min unit | Source and source date |
|---|---|---|---|---|
| Vultr | $1.85 | "Contact us for additional contract duration" | 8x bare metal | [vultr.com/pricing](https://www.vultr.com/pricing/) (live page, 2026-10-22) |
| AMD Developer Cloud (runs on DigitalOcean) | $1.99 (1x), $15.92/hr for 8x | none | 1x | [Phoronix review](https://phoronix.com/review/amd-developer-cloud) (2025); a Sept 30 2026 third-party snapshot calls $1.99 historical, see Gaps |
| DigitalOcean | $2.59 | $1.91 at 12-month reserved | 1x or 8x | [digitalocean.com/pricing/gpu-droplets](https://www.digitalocean.com/pricing/gpu-droplets) (page says new pricing effective 2026-08-01) |
| RunPod Secure Cloud | $2.39 | reserved "contact sales" | 1x | [computeprices.com RunPod MI300X](https://computeprices.com/providers/runpod/gpus/mi300x) (updated 2026-10-22); not on the main RunPod pricing page |
| Hot Aisle | $2.99 (1x, 2x, 4x VM), $3.39 (8x bare metal) | none listed | 1x VM | [hotaisle.xyz/pricing](https://hotaisle.xyz/pricing/) (live) |
| Cirrascale | not hourly; 8x server $22,499/mo monthly ($3.85/GPU-hr equiv) | $21,379/mo 3-month ($3.66), $20,249/mo 6-month ($3.47), $17,999/mo annual ($3.08) | 8x server | [cirrascale.com/pricing](https://www.cirrascale.com/pricing) (live) |
| Crusoe | $3.45 | contact sales | not stated | [crusoe.ai/cloud/pricing](https://www.crusoe.ai/cloud/pricing) (live) |
| Oracle BM.GPU.MI300X.8 | $6.00 ($48.00/node) | $32.16/node 1-year (-33%), $24.00/node 3-year (-50%), $24.00/node preemptible | 8x bare metal | [economize.cloud OCI tracker](https://www.economize.cloud/resources/oci/pricing/compute/BM_GPU_MI300X_8/) (updated 2026-10-08); launch price confirmed at $6.00/GPU-hr by [Oracle blog](https://blogs.oracle.com/cloud-infrastructure/post/announcing-ga-oci-compute-amd-mi300x-gpus) |
| Azure Standard_ND96isr_MI300X_v5 | $48.00/hr (East US 2, West US 3) = $6.00/GPU | not shown | 8x VM | [azurespeed.com](https://www.azurespeed.com/AzureVmPricing/Standard_ND96isr_MI300X_v5) (live); Spheron July 2026 snapshot reports spot $1.11 to $2.22/GPU-hr, see [spheron](https://www.spheron.network/blog/azure-mi300x-pricing-2026/) |
| TensorWave | no public price page (tensorwave.com/pricing is a 404) | custom | 8x | [getdeploying MI355X page](https://getdeploying.com/gpus/amd-mi355x) lists TensorWave as custom; gpus.io TensorWave page returned 403 |
| Nebius, Fluidstack, Scaleway, Vast.ai | no MI300X listed | | | [nebius.com/prices](https://nebius.com/prices); Fluidstack pricing page 404; [scaleway GPU pricing](https://www.scaleway.com/en/pricing/gpu/); vast.ai/pricing/gpu/MI300X is 404 |

Measured throughput (InferenceX, tok/s per GPU, 8K/1K):
- gpt-oss-120b, vLLM, FP4 (MXFP4 weights): 8,067 at 50 tok/s/user; 4,659 at 100 tok/s/user; peak 11,449. Runs 2026-03-09 to 2026-04-21. [InferenceX run page](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi300x)
- Llama 3.3 70B, vLLM, FP8: 1,482 at 50; 457 at 100; peak 3,520. Run 2025-10-29. [InferenceX](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-mi300x)
- DeepSeek R1 671B, SGLang, FP8: 608 at 30; 306 at 50; no data at 75 to 200; peak 873. Runs 2026-02-27 to 2026-10-22. [InferenceX](https://inferencex.semianalysis.com/run/deepseek-r1-on-mi300x)
- Head to head with H100 on gpt-oss-120b: H100 6,413 vs MI300X 5,144 at 89 tok/s/user; 4,180 vs 3,406 at 142; 2,714 vs 1,102 at 194. [InferenceX compare](https://inferencex.semianalysis.com/compare/gptoss-120b-h100-vs-mi300x)
- Head to head on DeepSeek R1: H100 850 vs MI300X 632 at 28 tok/s/user; 718 vs 375 at 46. [InferenceX compare](https://inferencex.semianalysis.com/compare/deepseek-r1-h100-vs-mi300x)
- AMD's own March 2025 claim that MI300X beats H200 by 2x to 5x on DeepSeek R1 with SGLang ("2X–5X higher throughput at the same latency") used a pre-upstream SGLang image and an older H200 SGLang 0.4.4.post1. [AMD ROCm blog, 2025-03-21](https://rocm.blogs.amd.com/artificial-intelligence/DeepSeekR1-Part2/README.html). InferenceX today shows H200 at 1,196 tok/s/GPU at 50 tok/s/user vs MI300X 306, so the AMD claim is stale.
- dstack independent test (2025): MI300X with vLLM reached 4,574 tok/s online for DeepSeek R1, and vLLM beat SGLang on MI300X. [dstack blog](https://dstack.ai/blog/h200-mi300x-deepskeek-benchmark/)

Software notes:
- vLLM gpt-oss recipe supports MI300X, MI325X, MI355X. The AMD launch requires env vars HSA_NO_SCRATCH_RECLAIM=1, AMDGCN_USE_BUFFER_OPS=0, VLLM_ROCM_USE_AITER=1, VLLM_ROCM_QUICK_REDUCE_QUANTIZATION=INT4, plus --attention-backend ROCM_AITER_UNIFIED_ATTN and --block-size 64. No MI355X launch command is given. [vLLM recipe](https://recipes.vllm.ai/openai/gpt-oss-120b)
- SGLang Kimi K2 cookbook marks MI300X as verified and requires SGLANG_ROCM_FUSED_DECODE_MLA=0 on AMD. It lists the model requirement as "8 GPUs with ≥140GB each (H200/B200)". [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K2)
- MLPerf Inference v5.1 (Sept 2025): MI300X appears only in a MangoBoost heterogeneous submission (4 MI300X + 2 MI325X nodes, about 94 percent efficiency). [AMD ROCm blog](https://rocm.blogs.amd.com/artificial-intelligence/mlperf-inference-v5.1/README.html)

#### B. AMD Instinct MI325X (256 GB HBM3e, 8 per node = 2 TB)

| Provider | On-demand | Term | Min unit | Source |
|---|---|---|---|---|
| Vultr | $2.00 | contact | 8x | [vultr.com/pricing](https://www.vultr.com/pricing/) (live) |
| DigitalOcean | $3.80 | $2.88 at 12-month | 1x or 8x | [DigitalOcean](https://www.digitalocean.com/pricing/gpu-droplets) |
| TensorWave | about $2.25 ($18.00/hr for 8x, custom terms) | custom | 8x | [getdeploying MI325X vs MI355X](https://getdeploying.com/gpus/amd-mi325x-vs-amd-mi355x) (secondary) |

Throughput (InferenceX, interpolated compare pages):
- gpt-oss-120b vs H200: MI325X 5,346 tok/s/GPU at 44 tok/s/user, 3,875 at 65, 1,856 at 86; H200 10,029 / 8,019 / 6,958. [InferenceX](https://inferencex.semianalysis.com/compare/gptoss-120b-h200-vs-mi325x)
- DeepSeek R1 vs H200: MI325X 966 at 35, 747 at 57, 607 at 78; H200 1,928 / 1,338 / 885. [InferenceX](https://inferencex.semianalysis.com/compare/deepseek-r1-h200-vs-mi325x)
- gpt-oss-120b per dollar vs MI355X (SemiAnalysis TCO $1.10 vs $1.50): MI325X $0.243/M vs MI355X $0.027/M at 81 tok/s/user. [InferenceX per-dollar](https://inferencex.semianalysis.com/compare-per-dollar/gptoss-120b-mi325x-vs-mi355x)
- MLPerf v5.1: MI325X Llama 2 70B FP8 closed division, about 2 percent (offline) and 4 percent (server) over v5.0; partner MI325X submissions from Vultr and others. [AMD blog](https://rocm.blogs.amd.com/artificial-intelligence/mlperf-inference-v5.1/README.html). Cross-round partner numbers: MI325X FP8 Llama 2 70B 31,889 to 32,028 tok/s per 8-GPU node. [Principled Technologies](https://www.principledtechnologies.com/AMD/Instinct-GPU-MLPerf-0726.pdf)

#### C. AMD Instinct MI350X and MI355X (288 GB HBM3e, 8 per node = 2.3 TB)

| Provider | On-demand | Term / spot | Min unit | Stock | Source |
|---|---|---|---|---|---|
| Vultr MI355X | $2.59 | contact | 8x | getdeploying marks Vultr MI355X out of stock on 2026-10-22 | [vultr.com/pricing](https://www.vultr.com/pricing/) (live); [getdeploying](https://getdeploying.com/gpus/amd-mi355x) |
| Daytona MI355X | $5.99 | spot $3.44 | 1x | in stock 2026-10-22 | [getdeploying](https://getdeploying.com/gpus/amd-mi355x) |
| DigitalOcean MI355X | not listed | spot $5.50 | 8x | | [DigitalOcean](https://www.digitalocean.com/pricing/gpu-droplets) |
| DigitalOcean MI350X | not listed | $4.76 12-month reserved; spot $3.50 | not stated | | [DigitalOcean](https://www.digitalocean.com/pricing/gpu-droplets) |
| Oracle MI355X | $8.60 ($68.80/hr 8x) | not found | 8x | | [getdeploying](https://getdeploying.com/gpus/amd-mi355x) (checked 2026-10-22; Oracle's own pricing pages returned 403/404) |
| TensorWave MI355X | $2.95 custom (8x = $23.60/hr) | custom | 8x | | [getdeploying](https://getdeploying.com/gpus/amd-mi355x) (last checked 2026-08-31) |
| Crusoe MI355X | on request | | 8x | | [Crusoe pricing](https://www.crusoe.ai/cloud/pricing) |
| Vultr MI455X (next gen, 72-GPU Helios rack) | contact sales to reserve | | 4-GPU node of a 72-GPU rack | | [vultr.com/pricing](https://www.vultr.com/pricing/) |

Throughput (InferenceX):
- gpt-oss-120b, vLLM, FP4: 38,497 at 50 tok/s/user; 30,982 at 75; 23,792 at 100; 14,133 at 150; 8,871 at 200; peak 44,999. Runs 2026-01-14 to 2026-06-05. Engines listed: ATOM and vLLM; footnote says "The ATOM engine is promising, however it has yet to serve production tokens." [InferenceX](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi355x)
- gpt-oss-120b vs B200: B200 32,860 vs MI355X 23,358 at 104 tok/s/user; 20,448 vs 13,182 at 171; 13,725 vs 3,911 at 238. [InferenceX compare](https://inferencex.semianalysis.com/compare/gptoss-120b-b200-vs-mi355x)
- Llama 3.3 70B, vLLM, FP4: 5,337 at 30; 2,878 at 50; 1,034 at 75; 618 at 100; peak 8,749. Run 2025-10-29. [InferenceX](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-mi355x). B200 on the same page family: 6,127 at 50, 2,500 at 100. [InferenceX](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-b200)
- DeepSeek R1: 1,134 at 30 (MoRI SGLang fp8); 1,608 at 50 (SGLang fp8); 4,027 at 75 (MoRI SGLang fp4); 3,616 at 100 (fp4); 1,568 at 150; 1,014 at 200; peak 8,175. Runs 2026-01-14 to 2026-10-22, 307 configs. [InferenceX](https://inferencex.semianalysis.com/run/deepseek-r1-on-mi355x). The frontier is non-monotonic (the 75 tok/s point is higher than 50), which means the fp4 MoRI config was not run at the lower interactivity points.
- DeepSeek R1 per dollar vs B200 (TCO $1.50 vs $1.73): MI355X $0.053/M vs B200 $0.060/M at 87 tok/s/user; $0.195 vs $0.234 at 158; $0.534 vs $0.377 at 230. [InferenceX per-dollar](https://inferencex.semianalysis.com/compare-per-dollar/deepseek-r1-b200-vs-mi355x)
- MLPerf v5.1 (Sept 2025): first MI355X results, Llama 2 70B open division MXFP4 with vLLM, 2.7x over MI325X FP8 single node; 8-node 7.9x over single node. [AMD blog](https://rocm.blogs.amd.com/artificial-intelligence/mlperf-inference-v5.1/README.html). Partner cross-round figures: MI355X FP4 Llama 2 70B 96,734 to 100,282 tok/s per 8-GPU node. [Principled Technologies](https://www.principledtechnologies.com/AMD/Instinct-GPU-MLPerf-0726.pdf)
- MLPerf v6.0: AMD says MI355X passed 1M tok/s multi-node; search snippet cites about 10,300 tok/s per GPU for gpt-oss-120b server mode (AMD blog fetch timed out, number unverified). [AMD blog](https://amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-inference-6-0-results.html)
- AMD's ROCm 7.0 preview gpt-oss-120b benchmark doc targets MI355X and MI350X only, TP=1, vLLM 0.10.1, image rocm/7.0-preview:rocm7.0_preview_ubuntu_22.04_vllm_0.10.1_instinct_rc1; it gives the recipe but no numbers. [ROCm docs](https://rocm.docs.amd.com/en/docs-7.0-rc1/preview/benchmark-docker/inference-vllm-gpt-oss-120b.html)

#### D. Google Cloud TPU v5e, v6e (Trillium), v7 (Ironwood)

Prices per chip-hour from the live Google page [cloud.google.com/tpu/pricing](https://cloud.google.com/tpu/pricing) (read 2026-10-22):

| TPU | HBM per chip | Region | On-demand | DWS Flex-start | 1-year CUD | 3-year CUD |
|---|---|---|---|---|---|---|
| v5e | 16 GB | us-central1, us-east5, us-west1, us-west4 | $1.20 | $0.60 | $0.84 | $0.54 |
| v6e Trillium | 32 GB | us-east1, us-east5 | $2.70 | $1.35 | $1.89 | $1.22 |
| v5p | 95 GB | us-east5, us-east1 | $4.20 | $2.10 | $2.94 | $1.89 |
| v7 Ironwood | 192 GB (206 GB per InferenceX) | us-central1 | $12.00 | $6.00 | $8.40 | $5.40 |

HBM per chip for v5e/v6e/v7 is from InferenceX ("HBM: 192 GiB (206 GB) for TPU v7") and common spec sheets; the Google pricing page does not list memory. [InferenceX TPU v7 page](https://inferencex.semianalysis.com/hardware/tpu-v7-ironwood-vs-gb300-nvl72-agentx-results)

Quota for a new customer (live page [docs.cloud.google.com/tpu/docs/quota](https://docs.cloud.google.com/tpu/docs/quota)):
- Default on-demand quota per project per zone: v6e 512 cores, v5e 512 cores, v5p 128 cores. Preemptible: v6e 1,536, v5e 1,536.
- v5e on-demand requests up to 64 cores are auto-approved in all zones. v6e auto-approve threshold is 0 cores, so every v6e increase is a manual request. Ironwood is not mentioned on the quota page. The pricing page says to "Contact our sales team to purchase quota" and offers a "custom quote" link.

Throughput:
- vLLM gpt-oss-120b recipe lists "TPU v7 (Ironwood)" as verified, with a TP 2, DP 4 example. [vLLM recipe](https://recipes.vllm.ai/openai/gpt-oss-120b)
- InferenceX (results dated 2026-10-19), vLLM on Google's TPU backend, Ironwood has no native FP4 compute: Qwen3.5-397B-A17B FP8 peaks at 40,363 tok/s/chip at 81 tok/s/user; GB300 NVL72 FP8 peaks at 101,367 tok/s/GPU at 68 tok/s/user. Kimi K3 2.8T FP4-weights: TPU v7 6,567 tok/s/chip vs GB300 20,143 tok/s/GPU at 56 tok/s/user. Tokens per $1 TCO at 100 tok/s/user on Kimi K3: TPU v7 13.87M (external TCO $1.21/chip-hr) vs GB300 14.23M ($2.31/GPU-hr). On Qwen3.5 at 200 tok/s/user TPU v7 gives 1.85x the tokens per dollar of GB300 FP8 but 0.54x of GB300 FP4. The page notes "$2.00 rental from Google Cloud, 3-year commit" for TPU v7, which conflicts with the $5.40 3-year list price above. [InferenceX TPU v7](https://inferencex.semianalysis.com/hardware/tpu-v7-ironwood-vs-gb300-nvl72-agentx-results)
- v6e: Google claims "nearly 2x higher relative inference throughput" for Llama 2 70B vs v5e, no absolute number. [Google Cloud blog](https://cloud.google.com/blog/products/compute/trillium-tpu-is-ga?hl=en). The vLLM TPU profiling doc runs Llama 3.1 70B on v6e at TP 8 but gives no tok/s. [vLLM docs](https://docs.vllm.ai/en/v0.10.2/examples/offline_inference/profiling_tpu.html)

#### E. AWS Trainium2 (Trn2) and Inferentia2 (Inf2)

- trn2.48xlarge: 16 Trainium2 chips, 1.5 TB accelerator memory total (96 GB per chip by division), 192 vCPU, 2 TB RAM, 3.2 Tbps EFA. [AWS Trn2 page](https://aws.amazon.com/ec2/instance-types/trn2/)
- Capacity Blocks for ML price: trn2.48xlarge $35.7608 per instance-hour = $2.235 per chip-hour, US East (Ohio) and Asia Pacific (Hyderabad). For comparison on the same page: p5.48xlarge (8x H100) $47.757 ($5.970/GPU), p5e.48xlarge (8x H200) $54.924 ($6.866/GPU), p6-b200.48xlarge $113.666 ($14.208/GPU), u-p6e-gb200x72 $761.904 per UltraServer-hour ($10.582/GPU). [AWS Capacity Blocks pricing](https://aws.amazon.com/ec2/capacityblocks/pricing/) (live)
- trn2.48xlarge on-demand: conflicting third-party values ($103.157 "starting at" on [instances.vantage.sh](https://instances.vantage.sh/aws/ec2/trn2.48xlarge); about $8.60 on sparecores for Ohio, which looks like a spot price). Not verified against AWS. Treat as not found.
- inf2.48xlarge: 12 Inferentia2 chips x 32 GB = 384 GB; on-demand $12.981/hr ($1.08 per chip-hour), 1-year reserved $8.178, 3-year $5.608, spot $4.336. [AWS Inf2 page](https://aws.amazon.com/ec2/instance-types/inf2/); [instances.vantage.sh](https://instances.vantage.sh/aws/ec2/inf2.48xlarge). inf2.xlarge (1 chip) $0.76/hr.
- Throughput: the only published Llama 3.3 70B number on Trn2 is the AWS NxD tutorial at concurrency 1, TP=64 across the whole 16-chip instance, BF16, 10,000 input / 1,500 output: 36.56 output tok/s baseline, 144.17 tok/s with fused speculative decoding (Llama 3.2 1B draft). [AWS Neuron tutorial, SDK 2.32](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/libraries/nxd-inference/tutorials/trn2-llama3.3-70b-tutorial.html). No high-concurrency throughput for Trn2 or Inf2 was found.
- vLLM Neuron for Llama 3: continuous batching, prefix caching, static per-tensor FP8 (ModelOpt) plus FP8 KV cache, EAGLE3 and DFlash speculation, disaggregated prefill; no pipeline parallelism; data parallel "throughput does not scale as expected" due to a vLLM DP load-balancing issue. Accuracy on Neuron 2.32: Llama 3.3 70B GSM8K 0.95 BF16 and FP8. [vLLM Neuron recipe](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/vllm-neuron/docs/model-recipes/llama-3.html)

#### F. Intel Gaudi 2 and Gaudi 3 (Gaudi 3: 128 GB HBM2e; Gaudi 2: 96 GB)

- Getdeploying lists one Gaudi 3 provider, Denvr, "on request, custom, waitlist," 8x only (checked 2026-10-22). No on-demand Gaudi 3 listing. [getdeploying Gaudi 3](https://getdeploying.com/gpus/intel-gaudi3)
- IBM Cloud gx3d-160x1792x8gaudi3 (8x Gaudi 3): $60/hr ($7.50 per card-hour) vs $85/hr for the matching 8x H100 and 8x H200 profiles, prices accessed 2025-03-21 in an Intel-commissioned report. [Signal65](https://signal65.com/research/ai/intel-gaudi-3-accelerates-ai-at-scale-on-ibm-cloud/). IBM's live docs page returned HTTP 500 today.
- Intel Tiber AI Cloud: both intel.com URLs redirect to a 404 and ai.cloud.intel.com does not resolve. No live price found.
- Denvr: pricing page lists Gaudi 2 in the menu, per-minute billing, "Save up to 20% with multi-month or annual commitments," but the fetched text was truncated before the rates. [denvr.com/pricing](https://www.denvr.com/pricing)
- Throughput (Intel's own table, Gaudi software 1.24.0, Optimum-Habana v1.21.0, not vLLM, FP8): Llama 3.3 70B on 8 HPU, 2048 in / 2048 out, batch 600: 10,747 tok/s (1,343 per card); 128 in / 2048 out, batch 768: 20,980 tok/s. Llama 3.1 70B on 2 HPU, 2048/2048, batch 175: 3,115 tok/s. [Intel Gaudi performance page](https://www.intel.com/content/www/us/en/developer/platform/gaudi/model-performance.html)
- Signal65 (vLLM 0.6.6.post1, March 2025): Gaudi 3 within 10 percent of H200 and 107 percent above H100 on Llama 3.1 405B FP8 at batch 128; 8.5 to 21 percent above H200 on Mixtral 8x7B. [Signal65](https://signal65.com/research/ai/intel-gaudi-3-accelerates-ai-at-scale-on-ibm-cloud/)

#### G. Qualcomm Cloud AI 100 Ultra

- Cirrascale: 8x AI 100 Ultra server $4,699 per month (monthly term) or $3,759 per month (annual). Single AI 100 Pro cards from $329 to $549 per month. Cirrascale prices per server per month, not hourly; the page says hourly equivalents are comparison values only. [Cirrascale pricing](https://www.cirrascale.com/pricing)
- Estimate: $3,759 / 730 hr / 8 cards = $0.64 per card-hour on an annual contract.
- No vLLM or vendor tok/s for gpt-oss-120b or Llama 70B was found. Cirrascale also runs an "Inference Cloud powered by Qualcomm" as an API. [Cirrascale Qualcomm page](https://www.cirrascale.com/solutions-qualcomm-cloud-ai100.php)

#### H. Tenstorrent

- Koyeb lists N300s (24 GB) and 4x N300s (96 GB) as "Request access" with no price. Blackhole and Galaxy are not on the Koyeb page. [Koyeb pricing](https://www.koyeb.com/pricing)
- Buy option: Blackhole p150a and p150b $1,399 (32 GB GDDR6, 300 W, four 800G QSFP-DD ports), p100a $999 (28 GB); "Ships in 2 weeks." [Tenstorrent Blackhole page](https://tenstorrent.com/hardware/blackhole)
- No measured LLM serving throughput for the models in scope was found. Mark "not rentable with a public price."

#### I. Groq, Cerebras, SambaNova, d-Matrix, Positron, Etched, Furiosa, Rebellions, Taalas

| Vendor | Raw hardware rentable by a small customer? | Evidence (fetched 2026-10-22) |
|---|---|---|
| Groq | No. API only via developer console; no dedicated or GroqRack pricing on site. | [groq.com](https://groq.com/) |
| Cerebras | No hourly hardware. API tiers; "Available by agreement" for an unnamed enterprise item; partner channels AWS Marketplace, OpenRouter, Hugging Face, Vercel. | [cerebras.ai/pricing](https://www.cerebras.ai/pricing) |
| SambaNova | No public rental. SambaCloud API; SambaRack sold for datacenters; no prices. | [sambanova.ai](https://sambanova.ai/) |
| d-Matrix Corsair / Squadron | No self-serve. "Request Early Access" and "Contact Sales"; a "Demo Cloud" is announced. Third-party: early access via Gimlet Cloud 2H 2026; Squadron GA "for select customers." | [d-matrix.ai](https://www.d-matrix.ai/); [Spheron](https://www.spheron.network/blog/d-matrix-corsair-vs-nvidia-gpus-new-inference-chip-2026/); [Autobound press reprint](https://www.autobound.ai/companies/d-matrix/news/d-matrix-announces-squadron-compute-clusters-for-ai-ab719ed0) |
| Positron | No price. Atlas appliance "Shipping now," up to 500B parameter models; Asimov chip and Titan rack due 2027; only CTA is "CONTACT US." | [positron.ai](https://www.positron.ai/) |
| Etched | No. "Our first racks ship this summer"; "Get Access" form; $1B in contracts. | [etched.com](https://www.etched.com/) |
| FuriosaAI RNGD | Evaluation only. "Request access" to bare-metal or an API endpoint; partners Equinix and DCP AI Cloud Center; no price. | [furiosa.ai](https://furiosa.ai/) |
| Rebellions | No. RebelPOD and RebelRack via "Let's Talk" sales contact; no price. | [rebellions.ai](https://rebellions.ai/) |
| Taalas | No product page content; contact info@taalas.com. | [taalas.com](https://taalas.com/) |

#### J. NVIDIA value tier and reference prices (per GPU-hour, checked 2026-10-22)

| GPU | Memory | RunPod Secure / Community | Lambda | Vultr (8x) | DigitalOcean OD / 12-mo | Nebius | Crusoe | Koyeb | Cirrascale 8x annual / monthly equiv | Vast.ai "from" | Other |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RTX PRO 6000 Blackwell | 96 GB GDDR7 | $2.49 / $1.69 | not listed | not listed | not listed | $1.80 (getdeploying) | not listed | $2.20 | $1.37 / $1.71 | $1.00 (WS edition, availability "Med") | CoreWeave $2.50 (8x), Hyperstack $1.85, Packet.ai $0.66, Database Mart $0.90 (24-mo), AWS $3.36, GCP $4.50, Azure $5.50, Oracle $4.50 (8x) |
| RTX 5090 | 32 GB GDDR7 | $1.19 / $0.69 | | | | | | | | $0.39 (availability "High") | Salad $0.50, HyperAI $0.35, Nova $0.72, TensorDock listing $0.56 |
| RTX 4090 | 24 GB | $0.89 / $0.34 | | | | | | | | not fetched | TensorDock $0.35 (page dated 2024-07-24), Hyperbolic cap $0.50 |
| L40S | 48 GB | $1.09 / $0.79 | | $1.671 (1x to 8x) | $1.57 | $1.55 | $1.50 | $1.20 | | | |
| A100 80 GB | 80 GB | $1.79 / $1.39 | $2.79 (8x SXM) | | | | $2.30 SXM / $2.00 PCIe | $1.60 PCIe / $2.15 SXM | $2.60 / $3.25 | | TensorDock $1.80 |
| GH200 | 96 GB HBM3 + 480 GB LPDDR | | $2.29 (1x) | $1.99 (1x) | | | | | | | |
| H100 SXM | 80 GB | $3.99 / $2.69 | $3.99 (8x), $4.29 (1x) | $2.30 | $4.41 / $3.26 | $4.50 | $3.90 | $2.50 | $3.43 / $4.28 | | TensorDock $2.25, Hyperbolic $3.19, GMI $2.60, AWS CB $5.97 |
| H200 | 141 GB | $5.29 / $3.59 | not listed | not listed | $4.47 / $3.40 | $5.40 | $4.29 | $3.00 | $3.63 / $4.54 | | GMI $3.20, AWS CB $6.87 to $7.90 |
| B200 | 180 GB | $7.99 / $5.98 | $6.69 (8x) | $3.50 | not listed | $8.50 | contact | $5.50 | $4.79 / $5.99 | | GMI $5.00, AWS CB $14.21 |
| B300 | 288 GB | $8.99 | | contact | $7.94 12-mo / $6.17 spot | $9.50 | $9.90 | | | | |
| GB200 NVL72 | 72x 186 GB | | | | | contact | contact | | | | GMI "from $8.00/GPU-hour, available now"; AWS CB $10.582/GPU ($761.90 per 72-GPU UltraServer-hour) |

Sources: [RunPod pricing (updated 2026-10-08)](https://www.runpod.io/pricing); [Lambda pricing](https://lambda.ai/pricing); [Vultr pricing](https://www.vultr.com/pricing/); [DigitalOcean](https://www.digitalocean.com/pricing/gpu-droplets); [Nebius](https://nebius.com/prices); [Crusoe](https://www.crusoe.ai/cloud/pricing); [Koyeb](https://www.koyeb.com/pricing); [Cirrascale](https://www.cirrascale.com/pricing); [Vast.ai RTX 5090](https://vast.ai/pricing/gpu/RTX-5090); [Vast.ai RTX PRO 6000 WS](https://vast.ai/pricing/gpu/RTX-PRO-6000-WS); [getdeploying RTX PRO 6000](https://getdeploying.com/gpus/nvidia-rtx-pro-6000); [getdeploying RTX 5090](https://getdeploying.com/gpus/nvidia-rtx5090); [TensorDock](https://tensordock.com/cloud-gpus.html); [Hyperbolic docs](https://docs.hyperbolic.xyz/docs/gpu-marketplace-pricing); [GMI Cloud](https://www.gmicloud.ai/pricing); [AWS Capacity Blocks](https://aws.amazon.com/ec2/capacityblocks/pricing/). Lambda 1-Click Clusters (2 weeks to 1 year): B200 $9.86 (16 GPUs) to $8.87 (256+); H100 $6.16 to $5.54. Lambda lists no H200 and no reserved prices. RunPod reserved clusters are "contact sales" for every GPU.

NVIDIA reference throughput (InferenceX, tok/s per GPU, 8K/1K):
- gpt-oss-120b FP4, vLLM: H100 8,973 at 50 and 5,863 at 100 (peak 10,284); H200 9,319 at 50 and 6,346 at 100 (peak 13,091); B200 44,489 at 50 and 29,548 at 100 (peak 65,459). [H100](https://inferencex.semianalysis.com/run/gptoss-120b-on-h100), [H200](https://inferencex.semianalysis.com/run/gptoss-120b-on-h200), [B200](https://inferencex.semianalysis.com/run/gptoss-120b-on-b200)
- Llama 3.3 70B: H100 FP8 1,496 at 50 (peak 2,568); B200 FP4 6,127 at 50, 2,500 at 100 (peak 12,981). [H100](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h100), [B200](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-b200)
- DeepSeek R1: H200 SGLang FP8 1,196 at 50, 709 at 100 (peak 3,370); B200 SGLang FP4 4,610 at 50, 2,685 at 100 (peak 13,430). [H200](https://inferencex.semianalysis.com/run/deepseek-r1-on-h200), [B200](https://inferencex.semianalysis.com/run/deepseek-r1-on-b200)
- RTX PRO 6000: InferenceX has a compare page but "No measured data at any of these interactivity points" and assigns it $0.68/chip-hr TCO. [InferenceX](https://inferencex.semianalysis.com/compare/gptoss-120b-h100-vs-rtx6000pro)
- RTX PRO 6000 Server Edition, vLLM, 1 GPU, 50 concurrent prompts, 100 in / 600 out: gpt-oss-120b 1,524.66 output tok/s, median ITL 32.5 ms, TTFT 342 ms. Page footer "Last Updated: 10/22/2026". [Database Mart](https://www.databasemart.com/blog/vllm-gpu-benchmark-pro6000)
- RTX PRO 6000 vs 5090 vs 4090, vLLM, 4-bit AWQ, 1,000 in / 1,000 out, 400 concurrent (CloudRift, 2025-10-09): Llama 3.3 70B INT4: 1x PRO 6000 1,031 output tok/s; 2x RTX 5090 (pipeline parallel) 1,230; 2x RTX 4090 467. GLM-4.5-Air 4-bit: 1x PRO 6000 3,169; 4x 5090 4,622; 4x 4090 1,731. Qwen3-Coder-30B: 1x 5090 4,570; 1x PRO 6000 8,425; 4x 5090 12,744. [CloudRift](https://www.cloudrift.ai/blog/benchmarking-rtx-gpus-for-llm-inference)
- StorageReview via eurokommerz: 2x RTX PRO 6000 Server, vLLM TP=2, batch 1, gpt-oss-120b NVFP4 about 176 tok/s per user. Millstone: 2x PRO 6000 MXFP4 peak system 664 tok/s at 6 concurrent. These are low-concurrency numbers. [eurokommerz](https://eurokommerz.at/blog/nvidia-rtx-pro-6000-real-benchmarks/); [Millstone](https://www.millstoneai.com/inference-benchmark/gpt-oss-120b-mxfp4-2x-rtx-pro-6000-blackwell)
- vLLM gpt-oss recipe: "ongoing work for Ampere/Ada/RTX 5090"; supported list is H100, H200, B200, A100 (single card, Marlin MXFP4), MI300X/MI325X/MI355X, Radeon AI PRO R9700, Intel Arc Pro B70, TPU v7. Blackwell uses FlashInfer MXFP4 with MXFP8 MoE. [vLLM recipe](https://recipes.vllm.ai/openai/gpt-oss-120b)

#### K. Memory per device and devices per replica (model fits)

| Model | Weights at serving precision | Devices per replica (minimum, with KV headroom) | Source |
|---|---|---|---|
| gpt-oss-120b | about 61 GB MXFP4 | 1x H100/H200/B200/MI300X/MI325X/MI355X/RTX PRO 6000; 1x A100 80 GB (Marlin); 2x to 4x RTX 5090 is unsupported in vLLM today; TPU v7 verified (TP 2 x DP 4 example) | [GitLab deploy guide](https://docs.gitlab.com/administration/gitlab_duo_self_hosted/vllm_gpt_oss_120b/); [vLLM recipe](https://recipes.vllm.ai/openai/gpt-oss-120b) |
| Llama 3.3 70B | about 70 GB FP8; about 48 GB INT4 AWQ; about 35 GB NVFP4 | 1x H200/B200/MI300X/MI325X/MI355X at FP8; 1x H100 FP8 is tight (InferenceX did run it); 1x RTX PRO 6000 at INT4 (CloudRift); 2x RTX 5090 INT4 pipeline parallel; Gaudi 3: 2 or 8 cards (Intel table); Trn2: whole 16-chip instance at TP 64 (AWS tutorial); TPU v6e: 8 chips at TP 8 (vLLM profiling doc) | [CloudRift](https://www.cloudrift.ai/blog/benchmarking-rtx-gpus-for-llm-inference); [Intel](https://www.intel.com/content/www/us/en/developer/platform/gaudi/model-performance.html); [AWS](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/libraries/nxd-inference/tutorials/trn2-llama3.3-70b-tutorial.html) |
| DeepSeek V3 / R1 671B | about 671 GB FP8; about 340 GB FP4 | 8x H200 (1,128 GB), 8x MI300X (1,536 GB), 8x MI325X (2,048 GB), 8x B200 FP4 or FP8 (1,440 GB), 8x MI355X (2,304 GB); 16x H100 at FP8 | InferenceX run pages above show single-node configs for H200, B200, MI300X, MI325X, MI355X |
| Kimi K2 / K2-Thinking (1T total, 32B active) | native INT4 about 594 GB (K2-Thinking); FP8 about 1 TB | SGLang: "8 GPUs with ≥140GB each (H200/B200)"; 8x MI300X at FP8 fits in 1.5 TB (AMD guide, secondary); MI300X verified in SGLang | [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K2); [WebProNews on AMD guide](https://www.webpronews.com/amds-audacious-bet-running-a-one-trillion-parameter-ai-model-on-a-single-desktop-workstation/) |
| Qwen3 235B-A22B | about 235 GB FP8 | 2x MI300X/H200/B200; 4x H100 (estimate from weight size) | estimate |
| GLM-4.6 (355B) / GLM-5.x (744B) | about 355 GB / 744 GB FP8 | 4x / 8x of any 141 GB+ device (estimate) | estimate; InferenceX lists GLM 5.3 744B runs on Vera Rubin NVL72 only |

### Inferences
- The only non-NVIDIA accelerator with mature vLLM and SGLang support, single-device fit for gpt-oss-120b and 70B, single-node fit for DeepSeek V3 and Kimi K2, and public self-serve pricing is the AMD Instinct line. TPU v7 is close on software (verified in the vLLM gpt-oss recipe) but costs $12.00 per chip-hour on demand.
- MI325X is the weakest AMD part per dollar in every InferenceX comparison. MI300X at $1.85 to $2.59 is a credible H100 substitute. MI355X at $2.59 (Vultr, when in stock) is the AMD part that competes with B200.
- Trainium2 and Gaudi 3 lack any published high-concurrency vLLM throughput for the models in scope, so their tokens per dollar cannot be computed from public data.

### Gaps
- AMD Developer Cloud current price: the DigitalOcean live page shows $2.59 on-demand; a 2026-09-30 third-party note says the $1.99 figure is historical. The AMD page itself returned 403.
- TensorWave has no public price page; all TensorWave prices are secondary.
- Oracle's own pricing pages returned 403 and 404; Oracle numbers are from trackers and the 2024 launch blog.
- Intel Tiber AI Cloud and IBM Cloud live Gaudi 3 prices: not found (404, DNS failure, HTTP 500).
- Fluidstack: no public rate card; pricing page 404.
- trn2.48xlarge on-demand price: conflicting third-party values; not verified.
- No vLLM or SGLang throughput for Trn2, Inf2, Gaudi 3, TPU v5e, TPU v6e, Qualcomm AI 100 Ultra, or Tenstorrent on gpt-oss-120b, Llama 3.3 70B, or DeepSeek-class models.
- No Kimi K2 high-concurrency throughput on any rentable hardware; the SGLang cookbook's 8x B200 number (1,113 output tok/s at concurrency 100, ShareGPT) is not a saturated run.
- GB200 NVL72 per-GPU throughput for gpt-oss-120b or DeepSeek was not fetched.
- InferenceX Kimi K3 and DeepSeek V4.1 Flash dashboards load data dynamically; no numbers extracted.
- Vast.ai live prices for RTX 4090, H100, H200, B200, A100, L40S were not fetched (the 500.farm stats page returned "TEST").

## Key Question 1: Which accelerator gives the most output tokens per dollar for (a) gpt-oss-120b, (b) Llama 3.3 70B, (c) DeepSeek V3-class MoE, (d) Kimi K2-class 1T MoE?

### Takeaway
On live rental prices, Vultr's 8x MI355X node at $2.59 per GPU-hour gives the most output tokens per dollar for gpt-oss-120b (about 53.5M tokens per dollar, estimate), ahead of Vultr's B200 at $3.50 (45.8M). For Llama 3.3 70B and DeepSeek-class MoE the B200 at $3.50 wins (6.3M and 4.7M tokens per dollar), with MI355X second. For Kimi K2-class 1T models no high-concurrency measurement exists on rentable hardware. At typical (non-Vultr) prices the ranking is B200 first, MI355X second, MI300X about equal to H100, H200 behind H100, MI325X last.

### Cited Findings

Reference on-demand prices used (cheapest public price page checked 2026-10-22, minimum unit in parentheses): H100 $2.30 Vultr (8x) [source](https://www.vultr.com/pricing/); H200 $3.00 Koyeb (1x) [source](https://www.koyeb.com/pricing); B200 $3.50 Vultr (8x) [source](https://www.vultr.com/pricing/); MI300X $1.85 Vultr (8x) [source](https://www.vultr.com/pricing/); MI325X $2.00 Vultr (8x); MI355X $2.59 Vultr (8x, out of stock today per getdeploying) and $5.99 Daytona (1x, in stock) [source](https://getdeploying.com/gpus/amd-mi355x); RTX PRO 6000 $1.00 Vast.ai WS edition and $1.69 RunPod Community [source](https://vast.ai/pricing/gpu/RTX-PRO-6000-WS), [source](https://www.runpod.io/pricing); RTX 5090 $0.39 Vast.ai and $0.69 RunPod Community.

Throughput sources are the InferenceX run pages cited in Key Question 0. Formula: tokens per dollar = (tok/s per GPU at 50 tok/s per user) x 3,600 / ($ per GPU-hour). All values are estimates.

(a) gpt-oss-120b at 50 tok/s per user:

| GPU | tok/s per GPU | $/GPU-hr | Tokens per $ (estimate) | vs H100 |
|---|---|---|---|---|
| H100 | 8,973 | $2.30 | 8,973 x 3,600 / 2.30 = 14.0M | 1.00 |
| H200 | 9,319 | $3.00 | 33.5M / 3.00 = 11.2M | 0.80 |
| B200 | 44,489 | $3.50 | 160.2M / 3.50 = 45.8M | 3.26 |
| MI300X | 8,067 | $1.85 | 29.0M / 1.85 = 15.7M | 1.12 |
| MI325X | 5,346 (at 44 tok/s/user, nearest point) | $2.00 | 19.2M / 2.00 = 9.6M | 0.69 |
| MI355X | 38,497 | $2.59 | 138.6M / 2.59 = 53.5M | 3.81 |
| MI355X | 38,497 | $5.99 (Daytona 1x) | 138.6M / 5.99 = 23.1M | 1.65 |
| RTX PRO 6000 | 1,525 (Database Mart, 50 concurrent, 100/600, not the same workload) | $1.69 | 5.5M / 1.69 = 3.2M | 0.23 (not comparable) |
| RTX PRO 6000 | 1,525 | $1.00 | 5.5M | 0.39 (not comparable) |

InferenceX's own retail-tier $/M at 50 tok/s per user (their retail $/hr in parentheses): H100 $0.062 ($2.00), H200 $0.086 ($2.90), B200 $0.023 ($3.70), MI300X $0.045 ($1.30), MI355X $0.021 ($2.90). Inverting: H100 16.1M, H200 11.6M, B200 43.5M, MI300X 22.2M, MI355X 47.6M tokens per dollar; ratios vs H100: 0.72, 2.70, 1.38, 2.95. [H100](https://inferencex.semianalysis.com/run/gptoss-120b-on-h100), [H200](https://inferencex.semianalysis.com/run/gptoss-120b-on-h200), [B200](https://inferencex.semianalysis.com/run/gptoss-120b-on-b200), [MI300X](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi300x), [MI355X](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi355x)

(b) Llama 3.3 70B at 50 tok/s per user:

| GPU | tok/s per GPU | $/GPU-hr | Tokens per $ (estimate) | vs H100 |
|---|---|---|---|---|
| H100 (FP8) | 1,496 | $2.30 | 5.39M / 2.30 = 2.34M | 1.00 |
| B200 (FP4) | 6,127 | $3.50 | 22.06M / 3.50 = 6.30M | 2.69 |
| MI300X (FP8) | 1,482 | $1.85 | 5.34M / 1.85 = 2.88M | 1.23 |
| MI355X (FP4) | 2,878 | $2.59 | 10.36M / 2.59 = 4.00M | 1.71 |
| RTX PRO 6000 (INT4 AWQ, 1K/1K, 400 concurrent, CloudRift) | 1,031 | $1.69 | 3.71M / 1.69 = 2.20M | 0.94 (estimate, different workload and precision) |
| RTX PRO 6000 | 1,031 | $1.00 | 3.71M | 1.59 (estimate) |
| 2x RTX 5090 (INT4, pipeline parallel, CloudRift) | 1,230 per pair | 2 x $0.69 = $1.38 | 4.43M / 1.38 = 3.21M | 1.37 (estimate) |
| 2x RTX 5090 | 1,230 | 2 x $0.39 = $0.78 | 5.68M | 2.43 (estimate) |
| Gaudi 3 (8 cards, Optimum-Habana FP8, 2048/2048, batch 600, Intel table) | 1,343 per card | $7.50 (IBM, March 2025) | 4.84M / 7.50 = 0.64M | 0.28 (estimate, stale price, not vLLM) |
| Trn2 (16 chips, batch 1, AWS tutorial) | 36.6 per instance | $35.76 per instance | 131,760 / 35.76 = 3,685 | about 0.002 (not comparable, concurrency 1) |

(c) DeepSeek R1 671B (V3-class) at 50 tok/s per user:

| GPU | tok/s per GPU | $/GPU-hr | Tokens per $ (estimate) | vs H100 |
|---|---|---|---|---|
| H100 | 718 (at 46 tok/s/user, compare page; no 50 point) | $2.30 | 2.58M / 2.30 = 1.12M | 1.00 |
| H200 (SGLang FP8) | 1,196 | $3.00 | 4.31M / 3.00 = 1.44M | 1.28 |
| B200 (SGLang FP4) | 4,610 | $3.50 | 16.60M / 3.50 = 4.74M | 4.23 |
| MI300X (SGLang FP8) | 306 | $1.85 | 1.10M / 1.85 = 0.60M | 0.53 |
| MI325X | 747 (at 57 tok/s/user) | $2.00 | 2.69M / 2.00 = 1.34M | 1.20 |
| MI355X (SGLang FP8 at 50) | 1,608 | $2.59 | 5.79M / 2.59 = 2.24M | 2.00 |
| MI355X (MoRI SGLang FP4 at 75 tok/s/user, higher interactivity) | 4,027 | $2.59 | 14.50M / 2.59 = 5.60M | 5.00 |

(d) Kimi K2-class 1T MoE: no InferenceX data for Kimi K2 on any chip. Available anchors:
- Kimi K3 2.8T (FP4 weights) on GB300 NVL72: 20,143 tok/s per GPU at 56 tok/s/user, 31.4M tokens per $1 TCO; TPU v7 6,567 tok/s per chip, 19.5M tokens per $1 external TCO. At 100 tok/s/user TPU v7 13.87M vs GB300 14.23M tokens per $1 TCO. [InferenceX](https://inferencex.semianalysis.com/hardware/tpu-v7-ironwood-vs-gb300-nvl72-agentx-results)
- Kimi K2-Instruct on 8x B200, SGLang 0.5.6.post1, TP 8, attn-dp 4, EP 4, 100 concurrent, ShareGPT: 1,113 output tok/s per node (139 per GPU). This is not a saturated run. [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K2)
- Estimate from that number: 1,113 x 3,600 / (8 x $3.50) = 143,000 tokens per dollar on Vultr B200; the true saturated figure should be several times higher.

### Inferences
- The MI355X lead on gpt-oss-120b exists only because Vultr lists it at $2.59; at Daytona's $5.99 the MI355X falls to 1.65x H100 and behind B200. Vultr's MI355X stock is the single most important variable.
- Vultr's B200 at $3.50 is far below the market ($5.50 to $8.50 elsewhere). At Lambda's $6.69 the B200 gives 23.9M tokens per dollar on gpt-oss-120b (1.70x H100 at $2.30), still above MI300X.
- MI300X is a cheap and adequate H100 substitute for gpt-oss-120b and 70B dense models (1.1x to 1.2x H100 tokens per dollar) but a poor choice for DeepSeek-class MoE at 50 tok/s per user (0.53x H100), because its SGLang MLA path lags.
- For 70B at INT4, a single RTX PRO 6000 at $1.00 to $1.69 and a pair of RTX 5090s at $0.78 to $1.38 are competitive with or better than an H100 node per token, but with lower per-user speed and quality loss from INT4. Treat as a hypothesis to benchmark, not a result.

### Gaps
- No Llama 3.3 70B InferenceX run page for H200, MI325X, or RTX PRO 6000.
- No DeepSeek R1 InferenceX run page for H100 (compare page only, interpolated).
- No apples-to-apples RTX PRO 6000 number at 8K/1K and 50 tok/s per user; InferenceX has none at any operating point.
- No Kimi K2 saturated throughput on any rentable node.
- GLM-5.2 InferenceX pages exist for MI325X vs MI355X (search result) but the run page I guessed returned 404.

## Key Question 2: Which accelerators can a solo operator start on this week with a credit card, and which need sales calls or quota requests?

### Takeaway
MI300X (Hot Aisle, RunPod, DigitalOcean, Vultr), MI325X and MI355X (Vultr 8x, Daytona 1x), every NVIDIA value-tier part (RunPod, Vast.ai, Koyeb, Lambda, TensorDock), TPU v5e (auto-approved up to 64 cores), and Trn2 via Capacity Blocks are credit-card starts. TPU v6e and v7, Oracle and Azure MI300X, TensorWave, Cirrascale, Gaudi 3 anywhere, Tenstorrent on Koyeb, GB200 NVL72, and every ASIC startup need a quota request or a sales conversation.

### Cited Findings
- Hot Aisle: "Credit card to running compute in under a minute," provision "without contacting sales first," Stripe billing metered to the minute. [hotaisle.xyz](https://hotaisle.xyz/)
- DigitalOcean GPU Droplets: billed per second with a 5-minute minimum; reserved pricing "available through sales." [DigitalOcean](https://www.digitalocean.com/pricing/gpu-droplets)
- Vultr: "provision VMs or bare metal servers on demand ... with no need for special requests or reservations"; MI455X, GB300 NVL72, and HGX B300 are "Contact sales." [Vultr](https://www.vultr.com/pricing/)
- RunPod: on-demand pods self-serve; reserved clusters "Contact sales" for every GPU; MI300X available but not on the main pricing page. [RunPod](https://www.runpod.io/pricing); [computeprices](https://computeprices.com/providers/runpod/gpus/mi300x)
- Lambda: on-demand 1x to 8x self-serve; "Contact us for reserved capacity." [Lambda](https://lambda.ai/pricing)
- Koyeb: NVIDIA instances self-serve; Tenstorrent N300s "Request access." [Koyeb](https://www.koyeb.com/pricing)
- Google TPU: v5e on-demand up to 64 cores auto-approved; v6e auto-approve threshold 0 cores (manual request); v7 not on the quota page; pricing page says "Contact our sales team to purchase quota." [TPU quota](https://docs.cloud.google.com/tpu/docs/quota); [TPU pricing](https://cloud.google.com/tpu/pricing)
- AWS Trn2: Capacity Blocks are purchasable from the console in US East (Ohio) at $35.76 per instance-hour. [AWS](https://aws.amazon.com/ec2/capacityblocks/pricing/). New-account quota for trn2 or inf2 vCPUs was not verified (gap).
- Oracle BM.GPU.MI300X.8 and Azure ND96isr_MI300X_v5 are 8-GPU-only shapes at $48/hr; both hyperscalers gate large GPU shapes behind quota (not verified on their pages today).
- TensorWave: no public price; "Book A Call." [TensorWave 404 page](https://tensorwave.com/pricing)
- Cirrascale: monthly contracts per server, not hourly. [Cirrascale](https://www.cirrascale.com/pricing)
- Gaudi 3: Denvr waitlist; IBM live page errored; Intel Tiber pages 404. [getdeploying](https://getdeploying.com/gpus/intel-gaudi3)
- GB200 NVL72: GMI "from $8.00/GPU-hour, available now" with committed pricing via sales; Nebius and Crusoe "contact." [GMI](https://www.gmicloud.ai/pricing); [Nebius](https://nebius.com/prices); [Crusoe](https://www.crusoe.ai/cloud/pricing)
- ASIC vendors: all "contact sales," "request access," or "early access" (see Key Question 0, table I).

### Inferences
- The fastest MI300X start is Hot Aisle (1x VM, by the minute) or RunPod; the cheapest is Vultr 8x bare metal at $14.80 per node-hour.
- The fastest MI355X start is Daytona at 1x $5.99 (in stock); the cheapest is Vultr at $20.72 per node-hour when in stock.
- A new GCP project can test on v5e immediately but must file a request for any v6e or v7 capacity.

### Gaps
- Vultr, Oracle, Azure, and AWS new-account quota limits for GPU and accelerator shapes were not read today.
- Whether Daytona and the smaller RTX PRO 6000 hosts on getdeploying (Packet.ai, HyperAI) accept instant credit-card signup was not verified.

## Key Question 3: Are MI300X or MI355X nodes cheaper per hour than H200 or B200 nodes at 1, 3, and 12 month terms, and by how much?

### Takeaway
Yes at every term I could price. On-demand, a Vultr 8x MI300X node ($14.80/hr) is 38 to 57 percent cheaper than the cheapest 8x H200 nodes ($24.00 Koyeb, $34.32 Crusoe), and a Vultr 8x MI355X node ($20.72/hr) is 26 percent cheaper than Vultr's 8x B200 ($28.00) and 61 percent cheaper than Lambda's ($53.52). On Cirrascale's published 1, 3, 6, and 12 month terms the MI300X node is 15 percent cheaper than H200 and 36 percent cheaper than B200 at every term. No public 1, 3, or 12 month MI355X price exists.

### Cited Findings

8-GPU node price per hour (GPU price x 8):

| Term | MI300X node | MI355X node | H200 node | B200 node | Sources |
|---|---|---|---|---|---|
| On-demand | Vultr $14.80; Hot Aisle $27.12; DigitalOcean $20.72; Oracle $48.00; Azure $48.00 | Vultr $20.72; Oracle $68.80; DigitalOcean spot $44.00 | Koyeb $24.00; Crusoe $34.32; DigitalOcean $35.76; Nebius $43.20; RunPod cluster $50.80 | Vultr $28.00; Koyeb $44.00; Lambda $53.52; RunPod $63.92; Nebius $68.00 | [Vultr](https://www.vultr.com/pricing/), [Hot Aisle](https://hotaisle.xyz/pricing/), [DigitalOcean](https://www.digitalocean.com/pricing/gpu-droplets), [Oracle tracker](https://www.economize.cloud/resources/oci/pricing/compute/BM_GPU_MI300X_8/), [Azure](https://www.azurespeed.com/AzureVmPricing/Standard_ND96isr_MI300X_v5), [getdeploying MI355X](https://getdeploying.com/gpus/amd-mi355x), [Koyeb](https://www.koyeb.com/pricing), [Crusoe](https://www.crusoe.ai/cloud/pricing), [Nebius](https://nebius.com/prices), [RunPod](https://www.runpod.io/pricing), [Lambda](https://lambda.ai/pricing) |
| 1 month | Cirrascale $22,499/mo = $30.82/hr | not found | Cirrascale $26,499/mo = $36.30/hr | Cirrascale $34,999/mo = $47.94/hr | [Cirrascale](https://www.cirrascale.com/pricing) (730 hr/mo) |
| 3 month | Cirrascale $21,379/mo = $29.29/hr | not found | Cirrascale $25,179/mo = $34.49/hr | Cirrascale $33,249/mo = $45.55/hr | [Cirrascale](https://www.cirrascale.com/pricing) |
| 6 month | Cirrascale $20,249/mo = $27.74/hr | not found | Cirrascale $23,849/mo = $32.67/hr | Cirrascale $31,499/mo = $43.15/hr | [Cirrascale](https://www.cirrascale.com/pricing) |
| 12 month | Cirrascale $17,999/mo = $24.66/hr; DigitalOcean $1.91 x 8 = $15.28/hr; Oracle $32.16/hr | DigitalOcean MI350X $4.76 x 8 = $38.08/hr (MI350X, not MI355X) | Cirrascale $21,199/mo = $29.04/hr; DigitalOcean $3.40 x 8 = $27.20/hr | Cirrascale $27,999/mo = $38.36/hr; DigitalOcean B300 $7.94 x 8 = $63.52/hr (B300, not B200) | [Cirrascale](https://www.cirrascale.com/pricing), [DigitalOcean](https://www.digitalocean.com/pricing/gpu-droplets), [Oracle tracker](https://www.economize.cloud/resources/oci/pricing/compute/BM_GPU_MI300X_8/) |
| 36 month | Oracle MI300X $24.00/hr | getdeploying cites a $2.29/GPU 36-month MI355X offer = $18.32/hr (provider unnamed) | not found | not found | [Oracle tracker](https://www.economize.cloud/resources/oci/pricing/compute/BM_GPU_MI300X_8/); [getdeploying](https://getdeploying.com/gpus/amd-mi355x) |

Percent differences (estimates):
- On-demand MI300X vs H200: Vultr $14.80 vs Koyeb $24.00 = 38 percent cheaper; vs Crusoe $34.32 = 57 percent cheaper. Same-provider: DigitalOcean $20.72 vs $35.76 = 42 percent cheaper.
- On-demand MI355X vs B200: Vultr $20.72 vs Vultr $28.00 = 26 percent cheaper; vs Lambda $53.52 = 61 percent cheaper; Oracle MI355X $68.80 is more expensive than every B200 listing found.
- 1 month: Cirrascale MI300X $30.82 vs H200 $36.30 = 15 percent cheaper; vs B200 $47.94 = 36 percent cheaper.
- 3 month: $29.29 vs $34.49 = 15 percent; vs $45.55 = 36 percent.
- 12 month: Cirrascale $24.66 vs $29.04 = 15 percent; DigitalOcean $15.28 vs $27.20 = 44 percent; Cirrascale MI300X vs B200 $38.36 = 36 percent.

### Inferences
- The MI300X discount vs H200 is largest at hyperscaler-style and marketplace providers (38 to 57 percent) and smallest at Cirrascale (15 percent). For the InferenceX workloads, the MI300X throughput deficit vs H200 is 13 percent on gpt-oss-120b at 50 tok/s per user and 74 percent on DeepSeek R1, so a 15 percent node discount only pays on dense and gpt-oss style models.
- MI355X vs B200 at 26 percent cheaper (Vultr) roughly matches the 13 percent throughput deficit on gpt-oss-120b at 50 tok/s per user, giving the MI355X a slight edge; on Llama 70B (53 percent deficit) and DeepSeek R1 FP8 (65 percent deficit) B200 wins.

### Gaps
- No public 1, 3, or 12 month MI355X or MI325X price from any provider.
- No same-provider B200 term price with an MI355X term price for a clean comparison.
- Oracle B200 and H200 prices were not read (Oracle pages blocked).

## Key Question 4: What does InferenceMAX say today about cost per million tokens for each accelerator at 50 to 100 tokens/s per user?

### Takeaway
At SemiAnalysis hyperscaler-ownership TCO, gpt-oss-120b costs $0.011 per million tokens on B200 and MI355X, $0.033 on MI300X, $0.036 on H100 and H200 at 50 tok/s per user; at 100 tok/s per user B200 $0.016, MI355X $0.018, H200 $0.053, H100 $0.055, MI300X $0.057. DeepSeek R1 at 50 tok/s per user costs $0.10 on B200, $0.26 on MI355X, $0.28 on H200, $0.86 on MI300X. These use $/GPU-hr of H100 $1.17, H200 $1.22, B200 $1.73, MI300X $0.95, MI325X $1.10, MI355X $1.50, RTX PRO 6000 $0.68, TPU v7 $1.03, GB200 $1.86, GB300 $2.31, from SemiAnalysis July 2026 pricing surveys.

### Cited Findings

$/M output tokens, InferenceX, 8K/1K, hyperscaler-ownership TCO (retail tier at 50 tok/s per user in parentheses):

| Model | Chip | 50 tok/s/user | 75 | 100 | Engine, precision | Source |
|---|---|---|---|---|---|---|
| gpt-oss-120b | H100 | $0.036 (retail $0.062 at $2.00/hr) | $0.046 | $0.055 | vLLM FP4 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-h100) |
| gpt-oss-120b | H200 | $0.036 (retail $0.086 at $2.90/hr) | $0.046 | $0.053 | vLLM FP4 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-h200) |
| gpt-oss-120b | B200 | $0.011 (retail $0.023 at $3.70/hr) | $0.014 | $0.016 | vLLM FP4 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-b200) |
| gpt-oss-120b | MI300X | $0.033 (retail $0.045 at $1.30/hr) | $0.044 | $0.057 | vLLM FP4 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi300x) |
| gpt-oss-120b | MI325X | $0.057 at 44 tok/s/user | $0.079 at 65 | $0.165 at 86 | vLLM FP4 | [link](https://inferencex.semianalysis.com/compare/gptoss-120b-h200-vs-mi325x) |
| gpt-oss-120b | MI355X | $0.011 (retail $0.021 at $2.90/hr) | $0.013 | $0.018 | vLLM FP4 | [link](https://inferencex.semianalysis.com/run/gptoss-120b-on-mi355x) |
| Llama 3.3 70B | H100 | $0.22 (retail $0.37) | $0.35 | no data | vLLM FP8 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h100) |
| Llama 3.3 70B | B200 | $0.078 (retail $0.17) | $0.12 | $0.19 | vLLM FP4 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-b200) |
| Llama 3.3 70B | MI300X | $0.18 (retail $0.24) | $0.37 | $0.58 | vLLM FP8 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-mi300x) |
| Llama 3.3 70B | MI355X | $0.14 (retail $0.28) | $0.40 | $0.67 | vLLM FP4 | [link](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-mi355x) |
| DeepSeek R1 | H200 | $0.28 (retail $0.67) | $0.37 | $0.48 | SGLang FP8 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-h200) |
| DeepSeek R1 | B200 | $0.10 (retail $0.22) | $0.15 | $0.18 | SGLang FP4 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-b200) |
| DeepSeek R1 | MI300X | $0.86 (retail $1.18) | no data | no data | SGLang FP8 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-mi300x) |
| DeepSeek R1 | MI325X | $0.409 at 57 tok/s/user | $0.504 at 78 | no data | not stated | [link](https://inferencex.semianalysis.com/compare/deepseek-r1-h200-vs-mi325x) |
| DeepSeek R1 | MI355X | $0.26 (retail $0.50) | $0.10 (fp4) | $0.12 (fp4) | SGLang FP8 at 50, MoRI SGLang FP4 at 75 and 100 | [link](https://inferencex.semianalysis.com/run/deepseek-r1-on-mi355x) |
| Kimi K3 2.8T | GB300 NVL72 | 31.4M tokens per $1 TCO at 56 tok/s/user peak; 14.23M at 100 | | | Dynamo vLLM FP4 | [link](https://inferencex.semianalysis.com/hardware/tpu-v7-ironwood-vs-gb300-nvl72-agentx-results) |
| Kimi K3 2.8T | TPU v7 | 19.15M tokens per $1 at 50; 13.87M at 100 (external TCO) | | | vLLM TPU | same |

- Several InferenceX compare pages carry prose percentages that do not match their own tables (for example "H100 is 100% cheaper per token" where the table shows $0.12 vs $0.24). Use the table values. [example](https://inferencex.semianalysis.com/compare/gptoss-120b-h100-vs-mi300x)
- Some compare pages show "FP4" in the control and "fp8" in the text for Hopper and MI300X Llama 70B and DeepSeek runs; the run pages resolve this as FP8 for H100/H200/MI300X and FP4 for B200/MI355X on Llama 70B.

### Inferences
- InferenceX TCO prices favor AMD more than rental prices do: the $0.95 MI300X vs $1.17 H100 ratio (0.81) is close to the Vultr rental ratio ($1.85 vs $2.30 = 0.80), but the $1.50 MI355X vs $1.73 B200 ratio (0.87) is above Vultr's ($2.59 vs $3.50 = 0.74), so Vultr rental pricing makes MI355X look better than InferenceX does.

### Gaps
- No InferenceX cost data for TPU v5e, v6e, Trn2, Inf2, Gaudi 3, or RTX PRO 6000 at any operating point.
- No InferenceX data at 50 to 100 tok/s per user for MI325X on gpt-oss-120b (page tops out at 86).

## Key Question 5: Do provider terms allow running a public paid inference API on the rented hardware?

### Takeaway
DigitalOcean, Google Cloud, AWS, and Lambda terms expressly or implicitly permit building a paid service for your own end users on rented capacity, while prohibiting resale of the raw cloud service. Vast.ai's terms contain a "service bureau" and "make available to any third party" prohibition that could be read against a public API; RunPod's main Terms of Use contain website-scoped commercial-use language and point to separate Compute Services Supplemental Terms I could not fetch. Hot Aisle publishes no terms page. Treat Vast.ai and RunPod as "ask before relying on it."

### Cited Findings
- DigitalOcean TOS (last updated 2026-08-22), section 4.4, contemplates customer products built on the service: "including via resale, your own products and services, or public-facing websites, applications, interfaces" and "You are responsible for your End Users' compliance with this TOS." Section 2.5 grants a "non-exclusive, non-transferable, non-sublicensable, revocable license." [DigitalOcean TOS](https://www.digitalocean.com/legal/terms-of-service-agreement)
- Google Cloud Platform Terms, section 1.1: "Customer may use the Services, and integrate the GCP Services and Looker (original) Services into any Customer Application that has material value independent of the Services." Section 3.3 prohibits "(c) sell, resell, sublicense, transfer, or distribute any or all of the Services." [Google Cloud terms](https://cloud.google.com/terms)
- AWS Customer Agreement (last updated 2026-08-14), section 6.4 prohibits "(c) resell the Services or AWS Content"; section 2.5: "You are responsible for End Users' use of Your Content and the Services," and "End User" is defined as any individual or entity that directly or indirectly uses the Services through you. [AWS agreement](https://aws.amazon.com/agreement/)
- Lambda Cloud Terms (last updated August 2025), section 2(a): "non-sublicensable, non-transferable, non-exclusive right to access and use the Services." The Acceptable Use Policy bans "operating network services such as: open proxies; open mail relays," cryptocurrency mining, and use "beyond commercially reasonable limits." No clause bars hosting a commercial API. [Lambda terms](https://lambda.ai/legal/terms-of-service)
- Vast.ai Terms (version date 2026-09-01), Prohibited Activities section 10: "to redistribute, resell, sublicense, publish or otherwise make available to any third party" and "as part of any effort to compete with Company or to provide services as a service bureau"; licence grant is "solely for your internal business purposes." [Vast.ai terms](https://vast.ai/terms)
- RunPod Terms of Use (last updated 2026-03-24), section 9: "Resell any credits purchased through the Service without the prior written consent of Runpod," "License, sell, transfer or commercially exploit the Site," "The Site may not be used in connection with any commercial endeavors." Section 4 says Compute Services "may be subject to the Compute Services Supplemental Terms," which were not on the page; my guessed URL for the supplemental terms returned 404. [RunPod terms](https://www.runpod.io/legal/terms-of-service)
- Hot Aisle: homepage says the platform is for "building and deploying products on the platform" and lists no terms, acceptable use, or privacy links; /terms/ returned 404. [Hot Aisle](https://hotaisle.xyz/)

### Inferences
- The RunPod "commercial endeavors" language is scoped to "the Site" (the website), not to pods, and RunPod markets Serverless for production APIs; the binding text is in the Compute Services Supplemental Terms, which must be read before launch.
- Vast.ai's "service bureau" wording is the only explicit language found that could prohibit a multi-tenant paid API on rented machines.

### Gaps
- Terms for Vultr, Oracle, Azure, Nebius, Crusoe, Koyeb, TensorWave, Cirrascale, Daytona, Hot Aisle, and Google's AUP (page truncated) were not read.
- RunPod Compute Services Supplemental Terms not found.

## Recommended planning numbers

All tokens per dollar figures are estimates computed as (InferenceX tok/s per GPU at 50 tok/s per user) x 3,600 / (listed $ per device-hour), with H100 at Vultr $2.30 = 1.0 (14.0M tokens per dollar on gpt-oss-120b; 1.12M on DeepSeek R1). "DS" = DeepSeek R1 671B as the DeepSeek-class MoE proxy. Prices checked 2026-10-22.

| Accelerator | Best rental source (min unit) | $/device-hr on-demand | $/device-hr 1 mo | 3 mo | 12 mo | Memory | tok/s per device gpt-oss-120b at 50 tok/s/user | tok/s per device DS at 50 tok/s/user | Tokens per $ vs H100=1.0, gpt-oss-120b | Tokens per $ vs H100=1.0, DS |
|---|---|---|---|---|---|---|---|---|---|---|
| NVIDIA H100 SXM | Vultr (8x); Lambda (1x $4.29) | $2.30 | Cirrascale $4.28 | $4.07 | $3.43; DO $3.26 | 80 GB | 8,973 | about 718 (at 46) | 1.00 | 1.00 |
| NVIDIA H200 | Koyeb (1x); Crusoe $4.29 | $3.00 | Cirrascale $4.54 | $4.31 | $3.63; DO $3.40 | 141 GB | 9,319 | 1,196 | 0.80 | 1.28 |
| NVIDIA B200 | Vultr (8x); Lambda $6.69 (8x) | $3.50 | Cirrascale $5.99 | $5.69 | $4.79 | 180 GB | 44,489 | 4,610 | 3.26 | 4.23 |
| AMD MI300X | Vultr (8x); Hot Aisle $2.99 (1x, by the minute) | $1.85 | Cirrascale $3.85 | $3.66 | $3.08; DO $1.91 | 192 GB | 8,067 | 306 | 1.12 | 0.53 |
| AMD MI325X | Vultr (8x); DO $3.80 (1x) | $2.00 | not found | not found | DO $2.88 | 256 GB | 5,346 (at 44) | 747 (at 57) | 0.69 | 1.20 |
| AMD MI355X | Vultr (8x, stock varies); Daytona $5.99 (1x) | $2.59 | not found | not found | not found (DO MI350X $4.76) | 288 GB | 38,497 | 1,608 FP8 (4,027 FP4 at 75) | 3.81 (1.65 at $5.99) | 2.00 (5.0 with FP4 at 75) |
| NVIDIA RTX PRO 6000 Blackwell | Vast.ai WS $1.00; RunPod Community $1.69; Cirrascale 8x $1.37 annual | $1.00 to $2.49 | Cirrascale $1.71 | $1.63 | $1.37; Database Mart $0.90 (24 mo) | 96 GB GDDR7 | 1,525 (Database Mart, 50 concurrent, 100/600; not comparable) | not found | 0.23 to 0.39 (not comparable) | not found |
| NVIDIA RTX 5090 | Vast.ai $0.39; RunPod $0.69 to $1.19 | $0.39 to $1.19 | not found | not found | not found | 32 GB | not supported in vLLM gpt-oss recipe | not applicable (no fit) | not found | not applicable |
| NVIDIA GB200 NVL72 | GMI Cloud (per GPU, rack terms unstated) | $8.00 (AWS CB $10.58) | contact | contact | contact | 186 GB per GPU | not fetched | not fetched | not found | not found |
| Google TPU v7 Ironwood | Google Cloud (quota request) | $12.00 | flex $6.00 | not applicable | $8.40 1-yr; $5.40 3-yr | 192 GB | not found (verified in vLLM recipe); Qwen3.5-397B 40,363 at 81 tok/s/user | Kimi K3 6,567 per chip at peak | not found | not found |
| Google TPU v6e Trillium | Google Cloud (manual quota) | $2.70 | flex $1.35 | not applicable | $1.89 1-yr; $1.22 3-yr | 32 GB | not found | not applicable (no single-host fit) | not found | not found |
| Google TPU v5e | Google Cloud (auto quota up to 64 cores) | $1.20 | flex $0.60 | not applicable | $0.84 1-yr; $0.54 3-yr | 16 GB | not found | not applicable | not found | not found |
| AWS Trainium2 (trn2.48xlarge, 16 chips) | AWS Capacity Blocks, US East (Ohio) | $2.235 per chip (block) | same | same | not found | 96 GB per chip | not found (Llama 70B 36.6 tok/s per instance at concurrency 1) | not found | not found | not found |
| AWS Inferentia2 (inf2.48xlarge, 12 chips) | AWS on-demand | $1.08 per chip | not applicable | not applicable | $0.68 1-yr; $0.47 3-yr | 32 GB per chip | not found | not applicable | not found | not found |
| Intel Gaudi 3 | IBM Cloud 8x (price from March 2025); Denvr waitlist | $7.50 (stale) | not found | not found | not found | 128 GB | not found (Llama 3.3 70B 1,343 per card, Optimum-Habana) | not found | not found | not found |
| Qualcomm AI 100 Ultra | Cirrascale 8x server, monthly only | not hourly ($0.64 equiv on annual, estimate) | $4,699/mo per 8x | not found | $3,759/mo per 8x | 128 GB | not found | not found | not found | not found |
| Tenstorrent Wormhole n300 / Blackhole p150 | Koyeb "request access"; buy p150a $1,399 | not found | not found | not found | not found | 24 GB / 32 GB | not found | not applicable | not found | not found |
| Groq, Cerebras, SambaNova, d-Matrix, Positron, Etched, Furiosa, Rebellions, Taalas | not rentable as raw hardware | not applicable | | | | | | | | |
