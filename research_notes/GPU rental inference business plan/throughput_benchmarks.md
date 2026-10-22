# LLM inference throughput benchmarks: H100, H200, B200 (vLLM, SGLang, TensorRT-LLM)

Scope: measured and vendor-claimed output tokens/s per GPU for popular open-weight models on NVIDIA H100 SXM, H200 and B200, for a tokens-per-GPU-hour revenue model. Every row in every table was checked on 2026-10-22. "Vendor" means NVIDIA, a serving-engine team, or a cloud selling the hardware. "Independent" means a third party that does not sell the GPU. Derived numbers are marked "estimate" with the arithmetic.

Conversion used throughout: output tokens per GPU-hour = output tok/s per GPU x 3,600. Example: 5,000 tok/s per GPU = 18.0M output tokens per GPU-hour.

A critical unit note about InferenceX (SemiAnalysis). See Key Question 5. The arithmetic strongly indicates that the "tokens/s per GPU" on InferenceX run pages counts input plus output tokens on its 8k-input/1k-output workload. Output-only is about one ninth of the listed figure on that workload. I mark every such conversion as an estimate.

## Key Question 1: Per-model, per-GPU throughput table (realistic production and best-case vendor)

### Takeaway
Across models, the strongest independent datapoints come from InferenceX (SemiAnalysis), GPUStack's performance lab, LMSYS deployments and MLPerf; the strongest vendor datapoints come from NVIDIA's TensorRT-LLM perf table (offline max-throughput, 1k/1k). Realistic production output throughput at 50 to 100 tok/s per user is typically 30 to 60 percent of the TensorRT-LLM offline figure, and prefill-heavy shapes (8k/1k) cut output throughput per GPU by 4 to 6x versus 1k/1k.

### Cited Findings

#### gpt-oss-120b (117B total, 5.1B active, MXFP4 MoE weights)

| GPU | Source (date) | Engine / version | Precision | GPUs per replica | ISL/OSL | Concurrency | Total output tok/s (replica) | Output tok/s per GPU | Per-user tok/s | TTFT | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H100 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) (docs v1.4.0rc1, 2026) | trtllm-bench, PyTorch backend | FP8 | 4 (DEP4) | 1000/1000 | offline max load | 18,740 (estimate: 4,685 x 4) | 4,685 | not stated | not stated | Vendor |
| H100 | same | same | FP8 | 4 (DEP4) | 8192/1024 | offline | 4,676 (estimate) | 1,169 | not stated | not stated | Vendor |
| H100 | [InferenceX run page](https://inferencex.semianalysis.com/run/gptoss-120b-on-h100) (runs 2026-03-27 to 2026-05-17) | vLLM | FP4 | per-GPU normalized | 8k/1k | swept | n/a | 8,973 listed at 50 tok/s/user; ~997 output (estimate: 8,973 / 9); peak 10,284 listed | 50 | not stated | Independent |
| H100 | same | vLLM | FP4 | per-GPU | 8k/1k | swept | n/a | 5,863 listed at 100 tok/s/user; 2,558 at 200 | 100 / 200 | not stated | Independent |
| H100 | [InferenceX compare H100 vs H200](https://inferencex.semianalysis.com/compare/gptoss-120b-h100-vs-h200) (2026) | best engine | FP4 | per-GPU | 8k/1k | ~32 | n/a | 6,362 listed at 90 tok/s/user; 4,148 at 143 | 90 / 143 | not stated | Independent |
| H100 x2 | [GPUStack performance lab](https://docs.gpustack.ai/latest/performance-lab/gpt-oss-120b/h100/) (GPUStack 2.2 docs, late 2025) | vLLM v0.10.2, `--async-scheduling -tp 2` | MXFP4 | 2 (TP2) | ShareGPT (avg ~215 in / ~196 out) | 1000 queued requests | 7,649 | 3,824 (estimate: 7,649 / 2) | ~12 (mean TPOT 86.5 ms) | mean 4.6 s | Independent |
| H100 x2 | same | same | MXFP4 | 2 | 4000/200 | 500 queued | 1,135 | 568 (estimate) | ~6 (TPOT 165 ms) | mean 29.5 s | Independent |
| H100 x1 | same, baseline | vLLM v0.10.2 default | MXFP4 | 1 | ShareGPT | 1000 queued | 2,901 | 2,901 | ~18 (TPOT 54 ms) | mean 24.8 s | Independent |
| H100 x1 | same, engine comparison | SGLang v0.5.3rc0 default | MXFP4 | 1 | ShareGPT | 1000 queued | 866 | 866 | ~17 | mean 133 s | Independent |
| H100 x1 | same | TensorRT-LLM v1.0.0 default | MXFP4 | 1 | ShareGPT | 1000 queued | 1,014 | 1,014 | ~4 (TPOT 233 ms) | mean 56 s | Independent |
| H100 x2 | [Simplismart](https://www.simplismart.ai/blog/deploy-gpt-oss-120b-h100-vllm) (2025-10-10) | vLLM 0.10.1.1, TP2, defaults | MXFP4 | 2 | 1024/512 | 32 | 1,467 | 734 (estimate: 1,467 / 2) | ~39 (TPOT 25.8 ms) | mean 261 ms | Independent |
| H100 x1 | same | vLLM 0.10.1.1, `--max-model-len 4096 --max-num-seqs 8` | MXFP4 | 1 | 1024/512 | 32 requested, 8 active | 552 | 552 | ~60 (TPOT 16.7 ms) | mean 4.4 s | Independent (memory-limited config) |
| H200 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) | trtllm-bench | FP8 | 1 (TP1) | 1000/1000 | offline | 6,868 | 6,868 | not stated | not stated | Vendor |
| H200 | same | same | FP8 | 1 | 8192/1024 | offline | 1,828 | 1,828 | not stated | not stated | Vendor |
| H200 | [InferenceX run page](https://inferencex.semianalysis.com/run/gptoss-120b-on-h200) (runs 2025-12-15 to 2026-05-30) | vLLM (TRT-LLM also run) | FP4 | per-GPU | 8k/1k | swept | n/a | 12,300 listed at 30 tok/s/user; 9,319 at 50 (~1,035 output, estimate /9); 6,346 at 100; 2,845 at 200; peak 13,091 listed | 30 to 200 | not stated | Independent |
| B200 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) | trtllm-bench | FP4 (NVFP4) | 2 (DEP2) | 1000/1000 | offline | 51,886 (estimate: 25,943 x 2) | 25,943 | not stated | not stated | Vendor |
| B200 | same | same | FP4 | 2 | 8192/1024 | offline | 12,222 (estimate) | 6,111 | not stated | not stated | Vendor |
| B200 | [TRT-LLM gpt-oss deployment guide](https://nvidia.github.io/TensorRT-LLM/1.3.0rc18/blogs/tech_blog/blog09_Deploying_GPT_OSS_on_TRTLLM.html) (container 1.1.0rc1, Aug 2025, page updated 2026-06-08) | TRT-LLM, DP4EP4, max_batch_size 640 per rank | not stated (MXFP4 weights) | 4 | 1k/2k | 2,560 (640 x 4) | 78,000 (estimate: 19,500 x 4) | 19,500 | not stated | not stated | Vendor |
| B200 x8 | same | TRT-LLM, TP8, batch 1 | not stated | 8 | not stated | 1 | 420 | 52.5 (estimate: 420 / 8) | 420 | not stated | Vendor |
| B200 | [NVIDIA blog on InferenceMAX v1](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/) (2025-10-13) | TRT-LLM | NVFP4 | not stated | 1k/1k | InferenceMAX tested 4 to 64 | n/a | ~10,000 per GPU at 100 tok/s/user (InferenceMAX v1 published); ~30,000 with Eagle3 speculative decoding; 60,000 max | 100 | not stated | Vendor claim citing InferenceMAX |
| B200 | [InferenceX run page](https://inferencex.semianalysis.com/run/gptoss-120b-on-b200) (runs 2026-02-05 to 2026-05-31) | vLLM (TRT-LLM also run) | FP4 | per-GPU | 8k/1k | swept | n/a | 44,489 listed at 50 tok/s/user (~4,943 output, estimate /9); 29,548 at 100; 15,470 at 200; peak 65,459 listed | 50 to 200 | not stated | Independent |
| B200 | [InferenceX compare B200 vs H100](https://inferencex.semianalysis.com/compare/gptoss-120b-b200-vs-h100) (2026) | best engine | FP4 | per-GPU | 8k/1k | swept | n/a | 36,090 listed at 90 tok/s/user; 24,876 at 143 | 90 / 143 | not stated | Independent |

#### gpt-oss-20b (21B total, 3.6B active)

| GPU | Source (date) | Engine | Precision | GPUs | ISL/OSL | Concurrency | Output tok/s per GPU | Type |
|---|---|---|---|---|---|---|---|---|
| H100 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) (2026) | trtllm-bench | FP8 | 1 | 1000/1000 | offline | 11,557 | Vendor |
| H100 | same | same | FP8 | 1 | 8192/1024 | offline | 3,366 | Vendor |
| H200 | same | same | FP8 | 1 | 1000/1000 | offline | 13,858 | Vendor |
| H200 | same | same | FP8 | 1 | 8192/1024 | offline | 4,015 | Vendor |
| B200 | same | same | FP4 | 1 | 1000/1000 | offline | 53,812 | Vendor |
| B200 | same | same | FP4 | 1 | 8192/1024 | offline | 11,904 | Vendor |

I found no independent serving benchmark for gpt-oss-20b on these GPUs at production concurrency.

#### Llama 3.3 70B (dense)

| GPU | Source (date) | Engine / version | Precision | GPUs per replica | ISL/OSL | Concurrency | Total output tok/s (replica) | Output tok/s per GPU | Per-user tok/s | TTFT | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H100 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) (2026) | trtllm-bench | FP8 | 2 (TP2) | 1000/1000 | offline | 4,418 (estimate: 2,209 x 2) | 2,209 | not stated | not stated | Vendor |
| H100 | same | same | FP8 | 2 | 8192/1024 | offline | 796 (estimate) | 398 | not stated | not stated | Vendor |
| H100 | [InferenceX run page](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h100) (run 2025-10-29) | vLLM | FP8 | per-GPU | 8k/1k | swept | n/a | 2,056 listed at 30 tok/s/user; 1,496 at 50 (~166 output, estimate /9); 923 at 75; no point at 100; peak 2,568 listed | 30 to 75 | not stated | Independent |
| H100 x4 | [GeneralCompute](https://www.generalcompute.com/blog/generalcompute-vs-vllm-throughput-latency-and-cost-benchmarks) (2026-06-11) | vLLM 0.8.x, TP4, prefix caching on | FP8 | 4 | 1024/256 | 256 | ~3,400 | ~850 (estimate: 3,400 / 4) | 22 at concurrency 64 | p50 310 ms, p99 2.4 s | Independent (Llama 3.1 70B, a sibling model) |
| H200 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) | trtllm-bench | FP8 | 2 (TP2) | 1000/1000 | offline | 5,174 (estimate) | 2,587 | not stated | not stated | Vendor |
| H200 | same | same | FP8 | 2 | 8192/1024 | offline | 1,074 (estimate) | 537 | not stated | not stated | Vendor |
| H200 | [InferenceX run page](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h200) (run 2025-10-29) | vLLM (TRT-LLM also run) | FP8 | per-GPU | 8k/1k | swept | n/a | 2,581 listed at 30; 2,099 at 50 (~233 output, estimate /9); 1,263 at 75; 798 at 100; peak 5,312 listed | 30 to 100 | not stated | Independent |
| B200 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) | trtllm-bench | FP4 | 1 (TP1) | 1000/1000 | offline | 6,920 | 6,920 | not stated | not stated | Vendor |
| B200 | same | same | FP4 | 1 | 8192/1024 | offline | 1,362 | 1,362 | not stated | not stated | Vendor |
| B200 | [NVIDIA blog on InferenceMAX v1](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/) (2025-10-13) | InferenceMAX config | NVFP4 | 1 | 1k/1k | 4 to 64 | n/a | "10,000 tokens per second at 50 TPS/user", "more than 4x" H200 | 50 | not stated | Vendor claim citing InferenceMAX |
| B200 | [InferenceX run page](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-b200) (run 2025-10-29) | vLLM (TRT-LLM also run) | FP4 (FP8 also run) | per-GPU | 8k/1k | swept | n/a | 8,935 listed at 30; 6,127 at 50 (~681 output, estimate /9); 3,989 at 75; 2,500 at 100; peak 12,981 listed | 30 to 100 | not stated | Independent |
| B200 | [vLLM blog on InferenceMAX](https://vllm.ai/blog/2025-10-09-blackwell-inferencemax) (2025-10-09) | vLLM | FP4 | not stated | 1k/8k | swept | n/a | "up to 3.7x more throughput" vs Hopper (chart only) | swept | not stated | Vendor (engine team) |

#### Qwen3-235B-A22B (MoE, 22B active)

| GPU | Source (date) | Engine / version | Precision | GPUs per replica | ISL/OSL | Concurrency | Total output tok/s (replica) | Output tok/s per GPU | Per-user tok/s | TTFT | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H100 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) (2026) | trtllm-bench | FP8 | 8 (DEP8) | 1000/1000 | offline | 15,456 (estimate: 1,932 x 8) | 1,932 | not stated | not stated | Vendor |
| H100 | same | same | FP8 | 8 | 1024/8192 | offline | 6,984 (estimate) | 873 | not stated | not stated | Vendor |
| H200 | same | same | FP8 | 4 (DEP4) | 1000/1000 | offline | 13,152 (estimate) | 3,288 | not stated | not stated | Vendor |
| H200 | same | same | FP8 | 4 | 8192/1024 | offline | 2,508 (estimate) | 627 | not stated | not stated | Vendor |
| H200 | [Baseten day-zero benchmark](https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/) (2025-04-29, updated 2025-05-19) | SGLang (day-zero build) | FP8 (TP4 on Hopper per the post) | not stated for the H200 run; FP8 is "served in TP4" | 1000/1000 | 32 | ~1,400 total tok/s "including prefill" (~700 output, estimate: half, since ISL = OSL) | ~175 if 4 GPUs (estimate: 700 / 4) | ~45 | ~250 ms median | Vendor (inference cloud) |
| H200 | same | same | FP8 | same | 1000/1000 | 384 | ~4,600 total tok/s (~2,300 output, estimate) | ~575 if 4 GPUs (estimate) | lower, not stated | not stated | Vendor |
| H100 x8 | [GPUStack performance lab, Qwen3-235B-A22B on H100](https://docs.gpustack.ai/2.2/performance-lab/qwen3-235b-a22b/h100/) (GPUStack 2.2 docs, late 2025) | vLLM v0.11.0, `-tp 8`, Qwen3-235B-A22B-Instruct-2507 | BF16 | 8 (TP8) | ShareGPT | 984 queued | 4,015 | 502 (estimate: 4,015 / 8) | ~7 (mean TPOT 148 ms) | mean 8.7 s | Independent |
| H100 x8 | same | SGLang v0.5.5.post1 default | BF16 | 8 | ShareGPT | 984 queued | 3,645 | 456 (estimate) | not stated | not stated | Independent |
| H100 x4 | same, recommended config | vLLM v0.11.0, Qwen3-235B-A22B-Instruct-2507-FP8, `-tp 4 --max-num-batched-tokens 16384` | FP8 | 4 (TP4) | ShareGPT | 984 queued | 3,701 | 925 (estimate: 3,701 / 4) | ~5 (mean TPOT 186 ms) | mean 9.6 s | Independent |
| H100 x4 | same | same | FP8 | 4 | 4000/200 | 500 queued | 718 | 180 (estimate) | ~11 (TPOT 90 ms) | mean 60.5 s | Independent |
| H100 x4 | same | same | FP8 | 4 | 2000/100 | 500 queued | 895 | 224 (estimate) | ~8 (TPOT 126 ms) | mean 26.9 s | Independent |
| H100 x8 | same | vLLM v0.11.0 BF16 TP8 | BF16 | 8 | 4000/200 | 500 queued | 931 | 116 (estimate) | ~14.5 (TPOT 69 ms) | mean 47.8 s | Independent |
| B200 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) | trtllm-bench | FP4 | 4 (DEP4) | 1000/1000 | offline | 23,056 (estimate) | 5,764 | not stated | not stated | Vendor |
| B200 | same | same | FP4 | 4 | 8192/1024 | offline | 5,640 (estimate) | 1,410 | not stated | not stated | Vendor |

#### Qwen3-32B (dense)

| GPU | Source (date) | Engine / version | Precision | GPUs | ISL/OSL | Concurrency | Output tok/s per GPU | Per-user tok/s | TTFT | Type |
|---|---|---|---|---|---|---|---|---|---|---|
| H100 | [GPUStack performance lab](https://docs.gpustack.ai/2.0/performance-lab/qwen3-32b/h100/) (GPUStack 2.0 docs, late 2025) | vLLM v0.11.0 default | BF16 | 1 | ShareGPT | 1000 queued | 1,132 (peak 2,360) | ~11 (TPOT 88 ms) | mean 78 s | Independent |
| H100 | same | TensorRT-LLM v1.2.0rc1 default | BF16 | 1 | ShareGPT | 1000 queued | 1,280 | ~16 (TPOT 62 ms) | mean 65 s | Independent |
| H100 | same | SGLang v0.5.5.post1 default | BF16 | 1 | ShareGPT | 1000 queued | 814 | ~17 | mean 116 s | Independent |
| H100 | same, recommended config | TensorRT-LLM, Qwen3-32B-FP8, chunked prefill | FP8 | 1 | ShareGPT | 1000 queued | 2,060 (peak 4,371) | ~6 (mean TPOT 159 ms, median 116 ms) | mean 31 s | Independent |
| H100 | same | same | FP8 | 1 | 2000/100 | 500 queued | 282 (5,902 total tok/s incl. input) | ~4.5 (TPOT 223 ms) | mean 87 s | Independent |
| H100 | same | same | FP8 | 1 | 4000/200 | 500 queued | 235 (4,929 total) | ~7 | mean 208 s | Independent |

I found no H200 or B200 serving benchmark for Qwen3-32B.

#### Qwen3-Coder-480B-A35B

| GPU | Source (date) | Engine | Precision | GPUs | ISL/OSL | Concurrency | Total output tok/s | Output tok/s per GPU | Per-user tok/s | TTFT | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H200 (hardware not stated in the result block; the recipe targets 8x H200) | [vLLM recipe](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Coder-480B-A35B.html) (2025 to 2026) | vLLM, FP8 via `--data-parallel-size 8 --enable-expert-parallel` | FP8 | 8 | 2048/1024 random | 10 | 131.9 | 16.5 (estimate: 131.9 / 8) | ~14.6 (TPOT 68 ms) | mean 7.6 s | Vendor (engine recipe, untuned) |

No throughput-tuned benchmark exists for this model on H100, H200 or B200 that I could find.

#### DeepSeek R1 / V3 (671B, 37B active)

| GPU | Source (date) | Engine / version | Precision | GPUs per replica | ISL/OSL | Concurrency | Total output tok/s (replica) | Output tok/s per GPU | Per-user tok/s | TTFT | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H100 (multi-node) | [InferenceX run page](https://inferencex.semianalysis.com/run/deepseek-r1-on-h100) (runs 2026-02-08 to 2026-02-13) | Dynamo SGLang, disaggregated, multi-node | FP8 | per-GPU | 8k/1k | swept | n/a | 116 listed at 30 tok/s/user; 74.2 at 50 (~8 output, estimate /9); 25.7 at 100; peak 1,376 listed | 30 to 100 | not stated | Independent |
| H100 | [InferenceX compare B200 vs H100](https://inferencex.semianalysis.com/compare/deepseek-r1-b200-vs-h100) (2026) | best engine | FP8 | per-GPU | 8k/1k | ~132 | n/a | 739.5 listed at 45 tok/s/user; 280.6 at 71; 154.3 at 97 | 45 to 97 | not stated | Independent (conflicts with run page above) |
| H100 x96 | [LMSYS, SGLang PD disaggregation](https://lmsys.org/blog/2025-05-05-large-scale-ep/) (2025-05-05) | SGLang, PD disaggregation, EP72 decode | FP8 (model native) | 9 decode nodes (72 GPUs) | 2000 in / 100 out, batch 256 per node | 256 per node | 22,282 per node | 2,785 per decode GPU (estimate: 22,282 / 8) | ~10.9 (estimate: 2,785 / 256) | not stated | Vendor (engine team) |
| H100 x96 | same | same, prefill EP32 | FP8 | 4 prefill nodes | 2k prompt | n/a | 54,543 prefill tok/s per node | 6,818 prefill tok/s per GPU (estimate) | n/a | n/a | Vendor (engine team) |
| H200 x8 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) (2026) | trtllm-bench | FP8 | 8 (DEP8) | 1000/1000 | offline | 13,016 (estimate: 1,627 x 8) | 1,627 | not stated | not stated | Vendor |
| H200 x8 | same | same | FP8 | 8 | 1024/8192 | offline | 9,744 (estimate) | 1,218 | not stated | not stated | Vendor |
| H200 | [InferenceX run page](https://inferencex.semianalysis.com/run/deepseek-r1-on-h200) (runs 2025-12-15 to 2026-10-22) | SGLang (Dynamo and TRT-LLM also run) | FP8 | per-GPU | 8k/1k | swept | n/a | 1,540 listed at 30 tok/s/user; 1,196 at 50 (~133 output, estimate /9); 909 at 75; 709 at 100; peak 3,370 listed | 30 to 100 | not stated | Independent |
| H200 (multi-node) | [vLLM blog, wide-EP](https://vllm.ai/blog/2025-12-17-large-scale-serving) (2025-12-17) | vLLM wide-EP, DBO, EPLB, llm-d on CoreWeave H200 + InfiniBand | FP8 | multi-node | not stated | not stated | n/a | 2,200 "sustained"; earlier 1,500 | not stated | not stated | Vendor (engine team) |
| H200 x8 | [GPUStack performance lab](https://docs.gpustack.ai/2.2/performance-lab/deepseek-r1/h200/) (GPUStack 2.2 docs, late 2025) | SGLang v0.5.3, TP8 + DP attention | FP8 | 8 | ShareGPT | 1000 queued | 3,415 | 427 (estimate: 3,415 / 8) | ~3 (mean TPOT 305 ms) | mean 6.0 s | Independent |
| H200 x8 | same | vLLM v0.11.0 TP8 default | FP8 | 8 | ShareGPT | 1000 queued | 2,621 | 328 | ~4 | mean 17.7 s | Independent |
| H200 x8 | same | TensorRT-LLM v1.0.0 TP8 EP8 | FP8 | 8 | ShareGPT | 1000 queued | 1,619 | 202 | ~5 | mean 20.3 s | Independent |
| H200 x8 | same | SGLang optimized | FP8 | 8 | 4000/200 | 500 queued | 767 | 96 | ~9 (TPOT 108 ms) | mean 63 s | Independent |
| H200 x8 | [dstack](https://dstack.ai/blog/h200-mi300x-deepskeek-benchmark/) (2025-03-18) | TensorRT-LLM (online) | not stated | 8 | 3200/800 | 4 to 128 | 4,176 (best online) | 522 (estimate) | not stated | chart only | Independent |
| H200 x8 | same | SGLang (offline) | not stated | 8 | 3200/800 to 3200 | batch 32 to 1024 | 6,311 (best offline) | 789 (estimate) | n/a | n/a | Independent |
| H200 x8 | [NVIDIA MLPerf v5.1 blog](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut) (2025-09-09) | TRT-LLM, MLPerf DeepSeek-R1 | FP8 | 8 | MLPerf R1 dataset | server: 12.5 tok/s/user p99, TTFT 2 s | n/a | 1,253 offline; 556 server | 12.5 (server) | 2 s cap | Vendor (unverified by MLCommons) |
| B200 x8 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) | trtllm-bench | FP4 (NVFP4 v2) | 4 (DEP4) | 1000/1000 | offline | 25,852 (estimate: 6,463 x 4) | 6,463 | not stated | not stated | Vendor |
| B200 | same | same | FP4 | 4 | 8192/1024 | offline | 4,672 (estimate) | 1,168 | not stated | not stated | Vendor |
| B200 | same | same | FP4 | 4 | 1024/8192 | offline | 15,448 (estimate) | 3,862 | not stated | not stated | Vendor |
| B200 | [InferenceX run page](https://inferencex.semianalysis.com/run/deepseek-r1-on-b200) (runs 2026-01-29 to 2026-09-16) | SGLang (Dynamo and TRT-LLM also run) | FP4 (FP8 also run) | per-GPU | 8k/1k | swept | n/a | 6,799 listed at 30; 4,610 at 50 (~512 output, estimate /9); 3,172 at 75; 2,685 at 100; 1,598 at 200; peak 13,430 listed | 30 to 200 | not stated | Independent |
| B200 x16 pool, TP4/EP4 | [InferenceX blog, SGLang 0.5.6](https://inferencex.semianalysis.com/blog/sglang-0-5-6-b200-deepseek-r1-fp4-up-to-1-8x) (run 2025-12-31, post 2026-05-02) | SGLang v0.5.6 | NVFP4 | 4 | 8192/1024 | 32 | n/a | 3,063 listed (~340 output, estimate /9) | 45.6 (TPOT 22.0 ms) | not stated | Independent |
| B200 same | same | same | NVFP4 | 4 | 8192/1024 | 64 | n/a | 3,419 listed (~380 output, estimate) | 30.4 | not stated | Independent |
| B200 same | same | same | NVFP4 | 4 | 8192/1024 | 128 | n/a | 5,145 listed (~572 output, estimate) | 18.6 (TPOT 53.7 ms) | not stated | Independent |
| B200 x8 | [TRT-LLM DeepSeek-V3.2 blog](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog15_Optimizing_DeepSeek_V32_on_NVIDIA_Blackwell_GPUs) (page updated 2026-10-19) | TRT-LLM, TP8 EP8, attention DP, MTP-1 | FP8 KV, weights not stated | 8 | 8K/1K | 256 | 8,618 | 1,077 | 11.3 (TPOT 98.5 ms) | mean 19.5 s | Vendor (DeepSeek-V3.2) |
| B200 x4 | same | TRT-LLM, TP4, MTP-3, min-latency | same | 4 | 8K/1K | 1 | 274 | 68.5 | 312 (TPOT 3.2 ms) | 426 ms | Vendor (DeepSeek-V3.2) |
| GB200 NVL72 (for reference) | [LMSYS SGLang on GB200 part II](https://www.lmsys.org/blog/2025-09-25-gb200-part-2/) via [LMSYS InferenceMAX post](https://www.lmsys.org/blog/2025-10-14-sa-inference-max/) (2025-10-14) | SGLang, PD disaggregation, large EP | FP8 attention, NVFP4 MoE | 72 | 2000-token input | large | n/a | 26,156 prefill per GPU; 13,386 decode per GPU | not stated | not stated | Vendor (engine team) |

#### DeepSeek-V3.2 (DSA sparse attention)

| GPU | Source (date) | Engine / version | Precision | GPUs | ISL/OSL | Concurrency | Total output tok/s | Output tok/s per GPU | Per-user tok/s | Type |
|---|---|---|---|---|---|---|---|---|---|---|
| H200 x8 | [GPUStack performance lab](https://docs.gpustack.ai/2.1/performance-lab/deepseek-v3.2/h200/) (GPUStack 2.1 docs, Dec 2025 to early 2026) | vLLM v0.13.0 TP8 baseline | FP8 | 8 | ShareGPT | 1000 queued | 2,702 | 338 (estimate) | ~4 (TPOT 275 ms) | Independent |
| H200 x8 | same | SGLang v0.5.6.post2, TP8 DP8 DP-attention, tool parser | FP8 | 8 | ShareGPT | 1000 queued | 3,968 | 496 (estimate) | ~5 | Independent |
| H200 x8 | same, recommended config | SGLang | FP8 | 8 | 1K/2K "generation heavy" | not stated | 3,704 total tok/s (~2,470 output, estimate: x2/3) | ~309 (estimate) | ~25 (TPOT 39 ms) | Independent |
| B200 x8 | TRT-LLM V3.2 blog (see R1 table) | TRT-LLM TP8 EP8 MTP-1 | FP8 KV | 8 | 8K/1K | 256 | 8,618 | 1,077 | 11.3 | Vendor |

#### GLM-4.5 / GLM-4.6 (355B-A32B MoE)

| GPU | Source (date) | Engine | Precision | GPUs | ISL/OSL | Concurrency | Total output tok/s | Output tok/s per GPU | Per-user tok/s | Type |
|---|---|---|---|---|---|---|---|---|---|---|
| not stated | [vLLM GLM recipe](https://docs.vllm.ai/projects/recipes/en/stable/GLM/GLM.html) (2025 to 2026) | vLLM, GLM-4.5-FP8 | FP8 | not stated (TP8 in examples) | 8000/1000 | 16 prompts, request rate 10000 | 651.6 (5,864 total incl. input) | 81 if 8 GPUs (estimate: 651.6 / 8) | ~45 (TPOT 22.4 ms) | Vendor (engine recipe, "expected output") |
| H200 (proxy: GLM-5, a newer and different model) | [InferenceX GLM-5 on H200](https://inferencex.semianalysis.com/run/glm-5-1-on-h200) (runs 2026-03-19 to 2026-05-19) | SGLang | FP8 | per-GPU | 8k/1k | swept | n/a | 788 listed at 30 tok/s/user; 572 at 50 (~64 output, estimate /9); 395 at 75; peak 852 listed | 30 to 75 | Independent (different model) |
| B200 (proxy: GLM-5) | [InferenceX GLM-5 on B200](https://inferencex.semianalysis.com/run/glm-5-1-on-b200) (runs 2026-03-20 to 2026-09-14) | SGLang (Dynamo, TileRT also run) | FP4 (FP8 also run) | per-GPU | 8k/1k | swept | n/a | 3,641 listed at 30; 2,792 at 50 (~310 output, estimate /9); 2,054 at 75; 1,527 at 100; peak 4,134 listed | 30 to 100 | Independent (different model) |
| H100 x8 | [GPUStack performance lab, GLM-4.x on H100](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h100/) (GPUStack 2.2 docs, late 2025) | vLLM v0.11.0 `-tp 8`, GLM-4.6-FP8 | FP8 (BF16 "cannot be served on a single server with NVIDIA H100 GPUs due to memory limitations") | 8 (TP8) | ShareGPT | 1000 queued | 1,528 | 191 (estimate: 1,528 / 8) | ~2 (mean TPOT 509 ms) | Independent |
| H100 x8 | same, recommended config | SGLang v0.5.3 `--tp-size 8 --ep-size 8`, GLM-4.6-FP8 | FP8 | 8 | ShareGPT | 1000 queued | 1,861 | 233 (estimate) | ~1.5 (mean TPOT 677 ms) | Independent |
| H200 x8 | [GPUStack performance lab, GLM-4.x on H200](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h200/) (GPUStack 2.2 docs, late 2025; page says the recommendation applies to GLM-4.5, 4.6 and 4.7) | vLLM v0.11.0 `-tp 8`, GLM-4.6 | BF16 (not stated explicitly) | 8 (TP8) | ShareGPT | 1000 queued | 2,908 | 363 (estimate) | ~5 (mean TPOT 198 ms) | Independent |
| H200 x8 | same | SGLang v0.5.3 `--tp-size 8`, GLM-4.6 | BF16 | 8 | ShareGPT | 1000 queued | 3,367 | 421 (estimate) | not stated | Independent |
| H200 x4 | same, recommended config | SGLang v0.5.3 `--tp 4`, GLM-4.6-FP8 | FP8 | 4 (TP4) | ShareGPT | 1000 queued | 3,416 (page normalizes to 8 GPUs as "7,081 x2" total TPS) | 854 (estimate: 3,416 / 4) | ~4 (mean TPOT 256 ms) | Independent |
| H200 x4 | same | same | FP8 | 4 | 4000/200 | 500 queued | 712 | 178 (estimate) | ~10 (TPOT 98 ms) | Independent |
| H200 x4 | same | same | FP8 | 4 | 2000/100 | 500 queued | 827 | 207 (estimate) | ~7 (TPOT 145 ms) | Independent |
| H200 x8 | same | vLLM v0.11.0 `-tp 8` baseline | BF16 | 8 | 4000/200 | 500 queued | 795 | 99 (estimate) | ~5 (TPOT 206 ms) | Independent |

I found no throughput benchmark for GLM-4.5 or GLM-4.6 on B200.

#### Kimi K2 (1T total, 32B active)

| GPU | Source (date) | Engine | Precision | GPUs per replica | ISL/OSL | Concurrency | Total output tok/s | Output tok/s per GPU | Per-user tok/s | TTFT | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H200 x128 | [LMSYS, Kimi K2 on 128 H200](https://www.lmsys.org/blog/2025-07-20-k2-large-scale-ep/) (2025-07-20) | SGLang, PD disaggregation (4 prefill nodes, 12 decode nodes), large EP, EPLB | FP8 (native) | 128 (96 decode GPUs) | 2000 in / 100 out, decode batch 480 | 480 per decode group | 288,000 decode | 3,000 per decode GPU (estimate: 288,000 / 96); 2,250 per GPU over all 128 (estimate) | ~6 (estimate: 3,000 / 480) | not stated | Vendor (engine team) |
| H200 x128 | same | same, prefill side | FP8 | 32 prefill GPUs | 2000 in | n/a | 224,000 prefill | 7,000 prefill tok/s per prefill GPU (estimate: 224,000 / 32) | n/a | n/a | Vendor (engine team) |
| H200 x128 | same | same | FP8 | 128 | same | same | cost "~$0.21 per 1M output tokens" at "$2.3/hour" H200 | n/a | n/a | n/a | Vendor (engine team) |
| H200 (proxy: Kimi K2.6, same 1T class) | [InferenceX compare B300 vs H200](https://inferencex.semianalysis.com/compare/kimi-k26-b300-vs-h200) (2026) | best engine | not stated | per-GPU | 8k/1k | swept | n/a | 867 listed at 40 tok/s/user, $0.39 per M tokens (~96 output, estimate /9) | 40 | not stated | Independent (K2.6) |
| H200 (proxy: K2.6) | [InferenceX K2.6 on H200](https://inferencex.semianalysis.com/run/kimi-k26-on-h200) (runs 2026-03-27 to 2026-05-30) | vLLM | INT4 | per-GPU | 8k/1k | swept | n/a | no interactivity tier reached (15 configs) | none | not stated | Independent (K2.6) |
| H200 x16 | [vLLM Kimi-K2 recipe](https://docs.vllm.ai/projects/recipes/en/latest/moonshotai/Kimi-K2.html) (2025 to 2026) | vLLM, TP8 x PP2, `-dcp 8`, FP8 KV cache | FP8 (native) | 16 (two nodes) | 8000/1000 | 16 prompts, request rate 10000 | 339.4 (peak 384) | 21.2 (estimate: 339.4 / 16) | ~22 (TPOT 45 ms) | mean 2.0 s | Vendor (engine recipe), low concurrency |
| H200 x16 | same | same without `-dcp` | FP8 | 16 | 8000/1000 | 16 | 255.0 | 15.9 (estimate) | ~17 (TPOT 58 ms) | mean 4.3 s | Vendor (engine recipe) |
| H800 x16 | same | vLLM TP8 x PP2 | FP8 | 16 | 1000/512 | 8 prompts at 1 req/s | 30.8 | 1.9 (estimate) | ~32 (TPOT 31 ms) | mean 58 s | Vendor (engine recipe), queue-bound |
| B200 x8 | [Lambda, Kimi-K2-Instruct with vLLM](https://lambda.ai/blog/how-to-serve-kimi-k2-instruct-on-lambda-with-vllm) (2025) | vLLM, TP8, `--num-prompts 10` ShareGPT | native (959 GB weights on disk) | 8 | ShareGPT | ~10 | 219.6 | 27.5 (estimate: 219.6 / 8) | ~57 (TPOT 17.6 ms) | 149 ms mean | Vendor (cloud), untuned |
| B200 (proxy: K2.6) | [InferenceX K2.6 on B200](https://inferencex.semianalysis.com/run/kimi-k26-on-b200) (runs 2026-03-24 to 2026-08-07) | Dynamo vLLM / vLLM | FP4 | per-GPU | 8k/1k | swept | n/a | 4,732 listed at 30; 3,449 at 50 (~383 output, estimate /9); 2,265 at 75; 1,510 at 100; 485 at 150; peak 16,602 listed | 30 to 150 | not stated | Independent (K2.6) |
| B300 (proxy: K2.6) | [InferenceX compare B300 vs H200](https://inferencex.semianalysis.com/compare/kimi-k26-b300-vs-h200) | best engine | not stated | per-GPU | 8k/1k | swept | n/a | 2,181 listed at 40 tok/s/user, $0.29 per M | 40 | not stated | Independent (K2.6) |

#### Mistral Small 3.1 / 3.2 (24B dense)

| GPU | Source (date) | Engine | Precision | GPUs | Shape | Concurrency | Output tok/s | Type |
|---|---|---|---|---|---|---|---|---|
| H100 x2 | [Spheron blog](https://www.spheron.network/blog/gpu-cost-per-token-benchmark-llm-inference-2026/) (2026) | not stated | FP16 | 2 | not stated | not stated | ~3,400 aggregate (~1,700 per GPU, estimate) | Vendor (GPU marketplace), low quality |
| H100 x1 | [Spheron Devstral post](https://www.spheron.network/blog/deploy-devstral-gpu-cloud/) (2026) | vLLM | BF16 | 1 | batch 8 | 8 | ~2,800 to 3,200 (Devstral, same 24B base) | Vendor (GPU marketplace), low quality |
| any | [Mistral announcement](https://mistral.ai/news/mistral-small-3-1/) (2025-03) | not stated | not stated | not stated | single stream | 1 | "150 tokens per second" | Vendor (model lab) |

No rigorous H100, H200 or B200 serving benchmark exists for Mistral Small 3.x that I could find.

#### Llama 4 Scout (109B-A17B) and Maverick (400B-A17B)

| Model | GPU | Source (date) | Engine | Precision | GPUs | ISL/OSL | Output tok/s per GPU | Type |
|---|---|---|---|---|---|---|---|---|
| Maverick | H200 | [NVIDIA TRT-LLM perf overview](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) (2026) | trtllm-bench | FP8 | 8 (DEP8) | 1000/1000 | 4,146 | Vendor |
| Maverick | H200 | same | same | FP8 | 8 | 8192/1024 | 1,276 | Vendor |
| Maverick | B200 | same | same | FP4 | 4 (DEP4) | 1000/1000 | 11,337 | Vendor |
| Maverick | B200 | same | same | FP4 | 4 | 8192/1024 | 3,279 | Vendor |
| Maverick | B200 | [NVIDIA Llama 4 blog](https://developer.nvidia.com/blog/nvidia-accelerates-inference-on-meta-llama-4-scout-and-maverick/) (2025-04-05) | TRT-LLM | FP8 | not stated | not stated | "over 30K tokens per second" (system, GPU count not stated); "3.4x faster throughput" than H200 | Vendor |
| Scout | B200 | same | TRT-LLM | FP8 | not stated | not stated | "over 40K output tokens per second" (system, GPU count not stated); 5,000 per GPU if 8 GPUs (estimate) | Vendor |
| Scout | H100 | same | TRT-LLM | INT4 | 1 | n/a | no throughput given; "optimized and quantized to int4 for a single NVIDIA H100 GPU" | Vendor |

No H100 throughput number exists for either Llama 4 model in the TRT-LLM table, and I found no independent benchmark.

### Inferences
- Output share by shape: at 1k/1k half of all tokens are output; at 8k/1k one ninth are output. Any "total tokens/s" figure must be split before it is used as output tokens per GPU-hour.
- Realistic production at 50 tok/s per user on 1k/1k lands at roughly 30 to 60 percent of the TRT-LLM offline figure, based on the gpt-oss-120b H100 data: TRT-LLM 4,685 offline versus GPUStack 3,824 at ~12 tok/s per user and Simplismart 734 at ~39 tok/s per user with an untuned vLLM.
- MoE models with very large total weights (DeepSeek, Kimi K2, GLM) are KV-cache limited on 8x H200, so their per-GPU output throughput at 50 tok/s per user (about 130 to 500 tok/s) is far below their 1k/1k offline peak (1,600 tok/s on H200).

### Gaps
- No independent H200 or B200 benchmark for Qwen3-32B, Mistral Small 24B, gpt-oss-20b, or Llama 4 Scout.
- No throughput-tuned benchmark for Qwen3-Coder-480B on any NVIDIA GPU.
- No throughput benchmark for GLM-4.5 or GLM-4.6 on H100/H200/B200 beyond an untuned vLLM recipe block with unstated hardware.
- InferenceX reports TTFT as "0.0 ms" or "0.1 ms" best-case on its run pages, which is not usable; its per-run TTFT lives in the interactive dashboard only.
- InferenceX H100 DeepSeek R1 numbers conflict between the run page (74 at 50 tok/s/user, multi-node Dynamo) and the compare page (739 at 45 tok/s/user). I could not resolve which configuration the compare page interpolates from.

## Key Question 2: Realistic production versus best-case vendor output tok/s per GPU

### Takeaway
For each model the best-case vendor number is the TensorRT-LLM offline 1k/1k figure (or NVIDIA's InferenceMAX-derived claims); realistic production at 50 tok/s per user with a general-purpose engine is 3 to 10x lower on prefill-heavy traffic and 1.5 to 3x lower on 1k/1k chat traffic.

### Cited Findings
- gpt-oss-120b B200: vendor best is 25,943 output tok/s per GPU offline at 1k/1k ([TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)) and "60,000 TPS/GPU max throughput" with Eagle3 ([NVIDIA blog](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/)); NVIDIA states the InferenceMAX v1 published figure at 100 tok/s per user was about 10,000 per GPU, and that InferenceMAX "only tests concurrencies 4-64" while the 30,000 figure relies on higher concurrency and DEP.
- gpt-oss-120b H100: vendor best 4,685 offline at 1k/1k ([TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)); independent vLLM TP2 on ShareGPT reached 3,824 per GPU at ~12 tok/s per user ([GPUStack](https://docs.gpustack.ai/latest/performance-lab/gpt-oss-120b/h100/)); untuned vLLM TP2 at 32 concurrent users and 1024/512 reached 734 per GPU at ~39 tok/s per user ([Simplismart](https://www.simplismart.ai/blog/deploy-gpt-oss-120b-h100-vllm)).
- Llama 3.3 70B H100: vendor best 2,209 offline at 1k/1k ([TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)); independent vLLM FP8 TP4 at 1024/256 and 256 concurrent reached ~850 per GPU, with 22 tok/s per user at 64 concurrent ([GeneralCompute](https://www.generalcompute.com/blog/generalcompute-vs-vllm-throughput-latency-and-cost-benchmarks)).
- DeepSeek R1 H200: vendor best 1,627 offline at 1k/1k ([TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)); vLLM multi-node wide-EP claims 2,200 sustained ([vLLM blog](https://vllm.ai/blog/2025-12-17-large-scale-serving)); independent single-node SGLang on ShareGPT reached 427 per GPU at ~3 tok/s per user ([GPUStack](https://docs.gpustack.ai/2.2/performance-lab/deepseek-r1/h200/)); TRT-LLM online at 3200/800 reached 522 per GPU ([dstack](https://dstack.ai/blog/h200-mi300x-deepskeek-benchmark/)); MLPerf server (12.5 tok/s per user) is 556 per GPU ([NVIDIA MLPerf blog](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut)).
- DeepSeek R1 B200: vendor best 6,463 offline at 1k/1k ([TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)); independent SGLang 0.5.6 at 8k/1k, 32 concurrent per 4-GPU replica, 45.6 tok/s per user: 3,063 listed per GPU, about 340 output (estimate) ([InferenceX blog](https://inferencex.semianalysis.com/blog/sglang-0-5-6-b200-deepseek-r1-fp4-up-to-1-8x)); TRT-LLM V3.2 at 8K/1K and 256 concurrent on 8 GPUs: 1,077 output per GPU at 11 tok/s per user ([TRT-LLM V3.2 blog](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog15_Optimizing_DeepSeek_V32_on_NVIDIA_Blackwell_GPUs)).
- Qwen3-235B H200: vendor best 3,288 offline at 1k/1k ([TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)); day-zero SGLang at batch 32 and 1k/1k gave ~1,400 total tok/s per replica at 45 tok/s per user ([Baseten](https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/)).
- Kimi K2 H200: 3,000 output per decode GPU at 2000/100 with decode batch 480 and about 6 tok/s per user ([LMSYS](https://www.lmsys.org/blog/2025-07-20-k2-large-scale-ep/)); at 40 tok/s per user the K2.6-class listed figure is 867 per H200 on 8k/1k ([InferenceX compare](https://inferencex.semianalysis.com/compare/kimi-k26-b300-vs-h200)).

### Inferences
- The gap between vendor offline and realistic serving grows with model size: for gpt-oss-120b on H100 the ratio is about 1.2x to 6x depending on per-user speed; for DeepSeek R1 on H200 it is about 3x to 12x.
- Engine choice swings results by 2 to 3x at the same hardware (GPUStack: vLLM 6,095 vs TRT-LLM 2,140 vs SGLang 1,814 total tok/s for gpt-oss-120b on H100; SGLang 6,636 vs vLLM 5,483 vs TRT-LLM 3,386 for R1 on H200).

### Gaps
- No source reports a per-user-speed-controlled 1k/1k sweep for H100 on any of these models with the engine version stated, except GeneralCompute (Llama 3.1 70B) and Simplismart (gpt-oss-120b).

## Key Question 3: H200 versus H100, and B200 versus H200, in measured benchmarks

### Takeaway
H200 beats H100 by about 1.0x to 1.7x (most gain on models that are KV-cache bound), while B200 beats H200 by about 2.7x to 4.9x (most gain on MoE at FP4 and on dense models at FP4); the B200 gain is largest at the interactive end of the curve.

### Cited Findings

| Model | Metric | H100 | H200 | B200 | H200/H100 | B200/H200 | Source |
|---|---|---|---|---|---|---|---|
| gpt-oss-120b | InferenceX listed tok/s per GPU at 50 tok/s/user, 8k/1k | 8,973 | 9,319 | 44,489 | 1.04x | 4.77x | [H100](https://inferencex.semianalysis.com/run/gptoss-120b-on-h100), [H200](https://inferencex.semianalysis.com/run/gptoss-120b-on-h200), [B200](https://inferencex.semianalysis.com/run/gptoss-120b-on-b200) |
| gpt-oss-120b | InferenceX at 90 tok/s/user | 6,362 | 6,798 | 36,090 | 1.07x ("11% more" per page summary) | 5.3x | [compare H100 vs H200](https://inferencex.semianalysis.com/compare/gptoss-120b-h100-vs-h200), [compare B200 vs H100](https://inferencex.semianalysis.com/compare/gptoss-120b-b200-vs-h100) |
| gpt-oss-120b | TRT-LLM offline output tok/s per GPU, 1k/1k | 4,685 (DEP4 FP8) | 6,868 (TP1 FP8) | 25,943 (DEP2 FP4) | 1.47x | 3.78x | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| gpt-oss-20b | TRT-LLM offline, 1k/1k | 11,557 | 13,858 | 53,812 | 1.20x | 3.88x | same |
| Llama 3.3 70B | InferenceX listed at 50 tok/s/user, 8k/1k | 1,496 | 2,099 | 6,127 | 1.40x | 2.92x | [H100](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h100), [H200](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-h200), [B200](https://inferencex.semianalysis.com/run/llama-3-3-70b-on-b200) |
| Llama 3.3 70B | TRT-LLM offline, 1k/1k | 2,209 (TP2 FP8) | 2,587 (TP2 FP8) | 6,920 (TP1 FP4) | 1.17x | 2.67x | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| Llama 3.3 70B | NVIDIA claim, InferenceMAX 1k/1k at 50 tok/s/user | n/a | n/a | 10,000 | n/a | "more than 4x" | [NVIDIA blog](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/) |
| Llama 2 70B (MLPerf) | MLPerf v5.0 server tokens/s, 8 GPUs | n/a | 33,072 | 98,443 | n/a | 2.98x | [NVIDIA MLPerf v5.0 blog](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/) |
| Llama 2 70B (MLPerf) | MLPerf v5.1 server, 8 GPUs | H200 is "11% performance increase" over best H100 v5.0 | 33,385 (VMware vGPU) | 101,611 (Nebius) | 1.11x | 3.0x | [Nebius](https://nebius.com/blog/posts/bare-metal-class-performance-mlperf-inference), [VMware](https://blogs.vmware.com/cloud-foundation/2025/12/15/mlperf-5-1-confirms-vcf-future-of-ai-ml-performance/) |
| DeepSeek R1 | InferenceX listed at 50 tok/s/user, 8k/1k | 74 (multi-node) | 1,196 | 4,610 | n/a | 3.85x | [H200](https://inferencex.semianalysis.com/run/deepseek-r1-on-h200), [B200](https://inferencex.semianalysis.com/run/deepseek-r1-on-b200) |
| DeepSeek R1 | TRT-LLM offline, 1k/1k | not listed | 1,627 (DEP8 FP8) | 6,463 (DEP4 FP4) | n/a | 3.97x | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| DeepSeek R1 | MLPerf v5.1 per GPU | n/a | 1,253 offline / 556 server | GB200: 4,024 / 2,327; GB300: 5,842 / 2,907 | n/a | GB200/H200 3.2x offline, 4.2x server | [NVIDIA MLPerf v5.1 blog](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut) |
| DeepSeek R1 | NVIDIA claim, cost per M tokens at ~75 tok/s/user | n/a | $1.56 | GB200 NVL72: "just over $0.10" | n/a | 15x (GB200) | [NVIDIA blog](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/) |
| DeepSeek R1 | SGLang claim | n/a | n/a | "up to a 4x performance gain compared to previous generation Hopper GPUs (H100/H200)" | n/a | up to 4x | [LMSYS](https://www.lmsys.org/blog/2025-10-14-sa-inference-max/) |
| Qwen3-235B | TRT-LLM offline, 1k/1k | 1,932 (DEP8 FP8) | 3,288 (DEP4 FP8) | 5,764 (DEP4 FP4) | 1.70x | 1.75x | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| Llama 4 Maverick | TRT-LLM offline, 1k/1k | not listed | 4,146 (DEP8 FP8) | 11,337 (DEP4 FP4) | n/a | 2.73x | same |
| Llama 4 (both) | NVIDIA claim | n/a | baseline | "3.4x faster throughput and 2.6x better cost per token" | n/a | 3.4x | [NVIDIA Llama 4 blog](https://developer.nvidia.com/blog/nvidia-accelerates-inference-on-meta-llama-4-scout-and-maverick/) |
| GLM-5 (proxy for GLM) | InferenceX listed at 50 tok/s/user, 8k/1k | n/a | 572 | 2,792 | n/a | 4.88x | [H200](https://inferencex.semianalysis.com/run/glm-5-1-on-h200), [B200](https://inferencex.semianalysis.com/run/glm-5-1-on-b200) |
| Kimi K2.6 (proxy) | InferenceX listed at 40 tok/s/user | n/a | 867 | B300: 2,181 | n/a | 2.5x (B300) | [compare](https://inferencex.semianalysis.com/compare/kimi-k26-b300-vs-h200) |
| Llama 3.1 405B (MLPerf) | MLPerf v5.1, 8 GPUs | n/a | 277 server / 547 offline (VMware vGPU) | 1,247 to 1,280 server / 1,649 to 1,660 offline | n/a | 4.5x server, 3.0x offline | [Lambda](https://lambda.ai/blog/lambda-mlperf-inference-v5.1), [Nebius](https://nebius.com/blog/posts/bare-metal-class-performance-mlperf-inference), [VMware](https://blogs.vmware.com/cloud-foundation/2025/12/15/mlperf-5-1-confirms-vcf-future-of-ai-ml-performance/) |
| gpt-oss-120b and Llama 3.3 70B | vLLM claim | Hopper baseline | n/a | "up to 4x higher throughput at similar latency" (4.3x on gpt-oss 1k/1k, 3.7x on Llama 70B 1k/8k) | n/a | up to 4.3x | [vLLM blog](https://vllm.ai/blog/2025-10-09-blackwell-inferencemax) |

### Inferences
- A planning rule of thumb: H200 = 1.1x H100 for small models that fit in 80 GB, 1.4x to 1.7x for models where H100 is KV-cache starved (70B FP8, 235B MoE). B200 = 2.7x to 3x H200 for dense models at FP4 and 3.8x to 4.9x for large MoE at FP4.
- The InferenceX H100 vs H200 gap on gpt-oss-120b (1.04x) is small because the model's 5.1B active parameters and 60 GB weights leave H100 compute-bound rather than memory-bound at 8k/1k.

### Gaps
- No measured H100 vs H200 comparison for DeepSeek R1 on a like-for-like single-node configuration, since R1 FP8 does not fit on 8x H100.

## Key Question 4: GPU memory per model and GPUs per replica

### Takeaway
At FP8 the rule is 1 byte per parameter plus KV cache; at BF16 2 bytes. That puts gpt-oss-120b and Mistral 24B on one GPU, Llama 70B FP8 on one to two, Qwen3-235B FP8 on four H100 or two to four H200, and DeepSeek, GLM-4.5 BF16 and Kimi K2 on eight H200 or B200 (or 16 H100).

### Cited Findings

| Model | Params (total / active) | Weights at stated precision | GPUs per replica, cited | Source |
|---|---|---|---|---|
| gpt-oss-120b | 117B / 5.1B | MXFP4 MoE weights; "run on a single 80GB GPU" (H100 named) | 1x H100/H200/B200; TRT-LLM table uses DEP4 on H100, TP1 on H200/GB200, DEP2 on B200 | [HF model card](https://huggingface.co/openai/gpt-oss-120b); [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html); [Simplismart](https://www.simplismart.ai/blog/deploy-gpt-oss-120b-h100-vllm) notes a single H100 needed `--max-model-len 4096 --max-num-seqs 8` to avoid OOM with vLLM 0.10.1 |
| gpt-oss-20b | 21B / 3.6B | MXFP4; "run within 16GB of memory" | 1 GPU | [HF model card](https://huggingface.co/openai/gpt-oss-120b) |
| Llama 3.3 70B | 70.6B dense | BF16 about 141 GB (estimate: 70.6B x 2 bytes); FP8 about 71 GB (estimate: x1 byte) | TRT-LLM uses TP2 FP8 on H100 and H200, TP1 FP4 on B200; InferenceX runs vLLM FP8 (TP not stated) | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| Qwen3-235B-A22B | 235B / 22B | FP8 "well over 200 gigabytes of files"; BF16 about 470 GB (estimate: x2) | FP8 TP4 on four H100; BF16 TP8 on eight H100; TRT-LLM uses DEP8 FP8 on H100, DEP4 FP8 on H200, DEP4 FP4 on B200 | [Baseten](https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/); [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| Qwen3-32B | 32B dense | BF16 about 65 GB (estimate); FP8 about 33 GB (estimate) | 1x H100 in GPUStack (BF16 and FP8) | [GPUStack](https://docs.gpustack.ai/2.0/performance-lab/qwen3-32b/h100/) |
| Qwen3-Coder-480B-A35B | 480B / 35B | FP8 about 480 GB (estimate) | 8x H200 (141 GB x 8), FP8 via DP8 + EP; TP8 "fails for the FP8 model" | [vLLM recipe](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Coder-480B-A35B.html) |
| DeepSeek V3 / R1 / V3.2 | 671B / 37B | FP8 native, about 671 GB (estimate: x1 byte) | SGLang official matrix: FP8 on "8x H200, 8x B200, 8x MI300X, 2x8x H100/H800/H20"; BF16 on "2x8x H200, 4x8x H100/H800"; W4A8/AWQ/MXFP4/NVFP4 on "8x H20/H100, 4x H200; 8x H100/A100; 8/4x B200". Measured: 8x H200 TP8 (GPUStack, dstack, TRT-LLM DEP8); 4x B200 at FP4 (TRT-LLM DEP4); 96x H100 multi-node (LMSYS); 2-node H100 appears on InferenceX as "multi-node" | [SGLang DeepSeek docs](https://docs.sglang.io/basic_usage/deepseek_v3.html); [GPUStack](https://docs.gpustack.ai/2.2/performance-lab/deepseek-r1/h200/); [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html); [LMSYS](https://lmsys.org/blog/2025-05-05-large-scale-ep/); [InferenceX H100](https://inferencex.semianalysis.com/run/deepseek-r1-on-h100) |
| DeepSeek V3 (TP vs EP memory) | same | "TP strategy shows 34GB free device memory per H200" | 8x H200 | [vLLM blog](https://vllm.ai/blog/2025-12-17-large-scale-serving) |
| GLM-4.5 / 4.6 | 355B / 32B (HF lists 358B params) | BF16 about 716 GB (estimate: 358B x 2); FP8 about 358 GB (estimate) | Official: BF16 "H100 x 16 / H200 x 8"; FP8 "H100 x 8 / H200 x 4" (batch up to 8, MTP on); full 128K context needs double; vLLM on 8x H100 "need `--cpu-offload-gb 16`". GPUStack: GLM-4.6 BF16 "cannot be served on a single server with NVIDIA H100 GPUs"; GLM-4.6-FP8 runs on 8x H100 TP8 and on 4x H200 TP4 | [HF GLM-4.5](https://huggingface.co/zai-org/GLM-4.5); [GPUStack H100](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h100/); [GPUStack H200](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h200/) |
| Kimi K2 | 1T / 32B | "Weights-on-disk: 959GB"; "Idle vRAM usage: 1,347GB" on 8x B200 TP8 | 8x B200; Lambda also recommends 16x H100; vLLM recipe: native FP8 needs "a cluster with 16 GPUs" and benchmarks on 16x H200 (TP8 x PP2) and 16x H800; LMSYS used 128x H200 | [Lambda](https://lambda.ai/blog/how-to-serve-kimi-k2-instruct-on-lambda-with-vllm); [vLLM Kimi-K2 recipe](https://docs.vllm.ai/projects/recipes/en/latest/moonshotai/Kimi-K2.html); [LMSYS](https://www.lmsys.org/blog/2025-07-20-k2-large-scale-ep/) |
| Mistral Small 3.1 24B | 24B dense | BF16 about 48 GB (estimate); FP8 about 24 GB (estimate) | 1x H100 (FP8) or 2x H100 (FP16) per a low-quality source | [Spheron](https://www.spheron.network/blog/gpu-cost-per-token-benchmark-llm-inference-2026/) |
| Llama 4 Scout | 109B / 17B | INT4 "for a single NVIDIA H100 GPU"; BF16 about 218 GB (estimate); FP8 about 109 GB (estimate) | 1x H100 INT4; 2x H100 FP8 (estimate) | [NVIDIA Llama 4 blog](https://developer.nvidia.com/blog/nvidia-accelerates-inference-on-meta-llama-4-scout-and-maverick/) |
| Llama 4 Maverick | 400B / 17B | BF16 about 800 GB (estimate); FP8 about 400 GB (estimate) | TRT-LLM uses DEP8 FP8 on H200 and DEP4 FP4 on B200 | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| Llama 3.1 405B | 405B dense | FP4 on B200 in MLPerf | 8x B200 (FP4), 8x H200, 4x GB200 | [Lambda](https://lambda.ai/blog/lambda-mlperf-inference-v5.1); [Nebius](https://nebius.com/blog/posts/bare-metal-class-performance-mlperf-inference) |

Memory capacities used: H100 SXM 80 GB, H200 SXM 141 GB, B200 180 GB (DGX B200) per the [TRT-LLM hardware list](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html); vLLM cites "192 GB of HBM3e at 8 TB/s per B200" ([vLLM blog](https://vllm.ai/blog/2025-10-09-blackwell-inferencemax)).

### Inferences
- Weight-to-capacity ratio drives the H100 penalty. A 671 GB FP8 DeepSeek on 8x H100 (640 GB) does not fit, so H100 serving of DeepSeek, Kimi K2 and GLM-4.5 BF16 needs two nodes, which is why InferenceX's H100 R1 numbers are 10x below H200.
- For a rental business, the models that fit one GPU (gpt-oss-120b, gpt-oss-20b, Qwen3-32B FP8, Mistral 24B, Llama 70B FP8 on H200) give the simplest capacity planning and the least interconnect sensitivity.

### Gaps
- No source states the exact KV-cache budget left per GPU for each model and precision; the vLLM blog's 34 GB free per H200 figure for DeepSeek TP8 is the only one.

## Key Question 5: InferenceMAX / InferenceX figures, cost per million tokens and assumed GPU hourly cost

### Takeaway
InferenceX (the renamed, continuously updated InferenceMAX) publishes a per-GPU throughput ladder at fixed per-user speeds on an 8k/1k workload, with cost per million tokens computed from a July 2026 SemiAnalysis TCO of $1.17 (H100), $1.22 (H200) and $1.73 (B200) per GPU-hour at hyperscaler volume, and $2.00, $2.90 and $3.70 at retail. The ladder's "tokens/s per GPU" reconciles with TRT-LLM output-only figures only if it counts input plus output tokens.

### Cited Findings

Assumed GPU cost (SemiAnalysis "Market July 2026 Pricing Surveys & AI Cloud TCO Model", as shown on every InferenceX page, e.g. [compare page](https://inferencex.semianalysis.com/compare/deepseek-r1-b200-vs-h100)):

| Chip | Owning at large hyperscaler volume, $/GPU/hr | Retail, $/GPU/hr |
|---|---|---|
| H100 | $1.17 | $2.00 |
| H200 | $1.22 | $2.90 |
| B200 | $1.73 | $3.70 |
| B300 | $2.26 | not shown |
| GB200 | $1.86 | not shown |
| GB300 | $2.31 | not shown |
| MI300X | $0.95 | not shown |
| MI325X | $1.10 | not shown |
| MI355X | $1.50 | not shown |
| RTX 6000 Pro | $0.68 | not shown |
| VR200 | $3.61 | not shown |

InferenceX throughput ladder and cost (8k input / 1k output, best engine at each point, "$ per million total tokens", hyperscaler tier). Sources: run pages linked in Key Question 1.

| Model | GPU | 30 tok/s/user | 50 tok/s/user | 75 | 100 | 150 | 200 | Peak listed | $/M tokens at 50 (hyperscaler / retail) | Engine, precision | Run dates |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gpt-oss-120b | H100 | none | 8,973 | 7,136 | 5,863 | 3,931 | 2,558 | 10,284 | $0.036 / $0.062 | vLLM, FP4 | 2026-03-27 to 2026-05-17 |
| gpt-oss-120b | H200 | 12,300 | 9,319 | 7,422 | 6,346 | 4,384 | 2,845 | 13,091 | $0.036 / $0.086 | vLLM, FP4 | 2025-12-15 to 2026-05-30 |
| gpt-oss-120b | B200 | none | 44,489 | 34,672 | 29,548 | 20,866 | 15,470 | 65,459 | $0.011 / $0.023 | vLLM, FP4 | 2026-02-05 to 2026-05-31 |
| Llama 3.3 70B | H100 | 2,056 | 1,496 | 923 | none | none | none | 2,568 | $0.22 / $0.37 | vLLM, FP8 | 2025-10-29 |
| Llama 3.3 70B | H200 | 2,581 | 2,099 | 1,263 | 798 | none | none | 5,312 | $0.16 / $0.38 | vLLM, FP8 | 2025-10-29 |
| Llama 3.3 70B | B200 | 8,935 | 6,127 | 3,989 | 2,500 | none | none | 12,981 | $0.078 / $0.17 | vLLM, FP4 | 2025-10-29 |
| DeepSeek R1 | H100 | 116 | 74.2 | 49.5 | 25.7 | none | none | 1,376 | $4.38 / $7.49 | Dynamo SGLang, FP8, multi-node | 2026-02-08 to 2026-02-13 |
| DeepSeek R1 | H200 | 1,540 | 1,196 | 909 | 709 | none | none | 3,370 | $0.28 / $0.67 | SGLang, FP8 | 2025-12-15 to 2026-10-22 |
| DeepSeek R1 | B200 | 6,799 | 4,610 | 3,172 | 2,685 | 2,146 | 1,598 | 13,430 | $0.10 / $0.22 | SGLang, FP4 | 2026-01-29 to 2026-09-16 |
| GLM-5 | H200 | 788 | 572 | 395 | none | none | none | 852 | $0.59 / $1.41 | SGLang, FP8 | 2026-03-19 to 2026-05-19 |
| GLM-5 | B200 | 3,641 | 2,792 | 2,054 | 1,527 | none | none | 4,134 | $0.17 / $0.37 | SGLang, FP4 | 2026-03-20 to 2026-09-14 |
| Kimi K2.6 | B200 | 4,732 | 3,449 | 2,265 | 1,510 | 485 | none | 16,602 | $0.14 / $0.30 | Dynamo vLLM / vLLM, FP4 | 2026-03-24 to 2026-08-07 |

Additional InferenceX compare-page points (interpolated), with concurrency:
- gpt-oss-120b at 90 tok/s/user: H100 6,362 at ~32 concurrency, H200 6,798 at ~19; cost $0.051 vs $0.050 per M; at 143 tok/s/user H100 4,148 and H200 4,618 ([compare](https://inferencex.semianalysis.com/compare/gptoss-120b-h100-vs-h200)).
- DeepSeek R1 at 45 tok/s/user: B200 5,215 at ~365 concurrency ($0.092 per M), H100 739.5 at ~132 ($0.439); at 71: B200 2,846.5 ($0.169), H100 280.6 ($1.158); at 97: B200 1,429 ($0.336), H100 154 ($2.106) ([compare](https://inferencex.semianalysis.com/compare/deepseek-r1-b200-vs-h100)).
- Kimi K2.6 at 40 tok/s/user: H200 867 ($0.39 per M), B300 2,181 ($0.29) ([compare](https://inferencex.semianalysis.com/compare/kimi-k26-b300-vs-h200)).

Methodology statements:
- The ladder "reads the measured frontier at each per-user speed target on a single-turn chat workload (8k input / 1k output), using the best engine and precision at that point" and sweeps concurrency on real hardware ([run page](https://inferencex.semianalysis.com/run/gptoss-120b-on-h100)).
- The InferenceMAX v1 launch (2025-10-09) tested 1k/1k, 8k/1k and 1k/8k with input lengths randomized to 80 to 100 percent of nominal, concurrency "4, 8, 16, 32, 64, etc.", no warmup, random sequences to defeat prefix caching; the TCO section is paywalled and the per-GPU charts are images ([SemiAnalysis launch article](https://newsletter.semianalysis.com/p/inferencemax-open-source-inference)).
- NVIDIA states InferenceMAX v1 "currently only tests concurrencies 4-64" ([NVIDIA blog](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/)).
- Disaggregated configs are costed "per decode chip or per prefill chip, rather than per total chip count", which the site says is not apples-to-apples ([compare page note](https://inferencex.semianalysis.com/compare/gptoss-120b-h100-vs-h200)).
- The SGLang 0.5.6 post gives TPOT and tok/s per user beside tok/s per GPU for a 16-GPU B200 pool at TP4/EP4, e.g. concurrency 128: 5,145 tok/s/GPU, TPOT 53.7 ms, 18.6 tok/s/user ([InferenceX blog](https://inferencex.semianalysis.com/blog/sglang-0-5-6-b200-deepseek-r1-fp4-up-to-1-8x)).
- From the launch article: per-MW figures for gpt-oss-120b, e.g. H100 900,000 and B200 2.8M tokens/s per MW; "DeepSeek R1 at 30 tok/s/user: GB200 NVL72 FP4 gives ~8x" tokens per MW versus single-node H200 FP8 ([SemiAnalysis](https://newsletter.semianalysis.com/p/inferencemax-open-source-inference)).

### Inferences
- Unit check (estimate, my arithmetic). Cost per M on each run page equals $/hr divided by (listed tok/s x 3,600): H100 gpt-oss-120b $1.17 / (8,973 x 3,600) = $0.0362 per M, matching the page's $0.036. The page labels this "$ per million total tokens", so the listed tok/s is the same token count the cost uses.
- Unit check 2 (estimate). On 8k/1k, total tokens are 9x output tokens. Listed peak / 9 versus TRT-LLM's output-only 8192/1024 figure: gpt-oss-120b H100 10,284/9 = 1,143 vs 1,169; H200 13,091/9 = 1,455 vs 1,828; B200 65,459/9 = 7,273 vs 6,111; Llama 3.3 70B H200 5,312/9 = 590 vs 537; B200 12,981/9 = 1,442 vs 1,362; DeepSeek R1 B200 13,430/9 = 1,492 vs 1,168. All six land within about 25 percent, where an output-only reading would be 4 to 9x off.
- Unit check 3 (estimate). SGLang 0.5.6 row at concurrency 128 and 18.6 tok/s/user on a 4-GPU replica gives 128 x 18.6 = 2,381 output tok/s per replica, or 595 per GPU; 595 x 9 = 5,357 total, matching the listed 5,145. At concurrency 4: 4 x 108.5 / 4 GPUs = 108.5 output per GPU, x9 = 977 versus listed 907.
- Conclusion: treat InferenceX ladder values as total tokens per GPU-second on 8k/1k. Output tokens per GPU-second is about the listed value divided by 9 on that workload, and the "$ per million tokens" is per million total tokens. For a revenue model priced on output tokens, multiply the InferenceX cost by about 9 or use the output estimates in Key Question 1.
- The InferenceMAX v1 numbers NVIDIA quotes for 1k/1k (B200 ~10,000 per GPU at 100 tok/s/user for gpt-oss-120b; 10,000 at 50 tok/s/user for Llama 3.3 70B) would be about 5,000 output per GPU if they are also total tokens, which sits between TRT-LLM's offline 1k/1k figures and the InferenceX 8k/1k output estimates and is plausible either way; I could not confirm the unit for those October 2025 charts.

### Gaps
- InferenceX does not publish the 1k/1k ladder on its static run pages; only the 8k/1k frontier is in text. The 1k/1k and 1k/8k data are in the interactive dashboard and in images.
- The launch article's TCO assumptions and absolute per-GPU charts are paywalled or image-only; the hourly figures above come from the live pages' July 2026 survey, not the October 2025 launch.
- I could not find InferenceX text stating explicitly whether "tokens/s per GPU" is total or output; the conclusion above rests on the three arithmetic checks.

## Key Question 6: MLPerf Inference v5.0 and v5.1 (Llama 3.1 405B, Llama 2 70B, DeepSeek R1)

### Takeaway
Per GPU, MLPerf v5.1 shows B200 at about 12,500 to 12,700 tokens/s on Llama 2 70B server, about 156 to 160 on Llama 3.1 405B server, and H200 at about 4,170 and 35 respectively; DeepSeek R1 reaches 556 server / 1,253 offline per H200 (unverified) and 2,327 / 4,024 per GB200 GPU. Per-GPU is not a primary MLPerf metric; all per-GPU values are total divided by accelerator count.

### Cited Findings

| Benchmark | System | Scenario | Tokens/s (system) | Tokens/s per GPU | Entry | Source |
|---|---|---|---|---|---|---|
| Llama 2 70B 99 | 8x B200 (Lambda, TensorRT 10.11, CUDA 12.9, FP4) | Offline | 102,725 | 12,841 (estimate: /8) | v5.1 | [Lambda](https://lambda.ai/blog/lambda-mlperf-inference-v5.1) (2025-09-09) |
| Llama 2 70B 99 | 8x B200 (Lambda) | Server | 99,994 | 12,499 (estimate) | v5.1 | same |
| Llama 2 70B | 8x B200 (Nebius) | Server / Offline | 101,611 / 101,246 | 12,701 / 12,656 (estimate) | 5.1-0077 | [Nebius](https://nebius.com/blog/posts/bare-metal-class-performance-mlperf-inference) (2025-09-10) |
| Llama 2 70B 99.9 | NVIDIA platform record | Offline / Server / Interactive | n/a | 12,934 / 12,701 / 7,856 | v5.0 and v5.1 | [NVIDIA MLPerf v5.1 blog](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut) |
| Llama 2 70B | 8x B200 (NVIDIA) | Server / Offline | 98,443 / 98,858 | 12,305 / 12,357 (estimate) | 5.0-0060 | [NVIDIA MLPerf v5.0 blog](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/) (2025-04-02) |
| Llama 2 70B | 8x H200 (NVIDIA) | Server / Offline | 33,072 / 34,988 | 4,134 / 4,374 (estimate) | 5.0-0056 | same |
| Llama 2 70B | 8x H200 (VMware VCF vGPU, Dell XE9680) | Server / Offline | 33,385 / 34,301 | 4,173 / 4,288 (estimate) | v5.1 | [VMware](https://blogs.vmware.com/cloud-foundation/2025/12/15/mlperf-5-1-confirms-vcf-future-of-ai-ml-performance/) (2025-12-15); "only 1% or 2% different" from bare metal |
| Llama 2 70B | 8x H100 | Server | H200 shows "11% performance increase compared to the best results achieved on H100-powered systems" in v5.0; so about 3,720 per GPU (estimate: 4,134 / 1.11) | ~3,720 (estimate) | 5.0-0057 | [Nebius](https://nebius.com/blog/posts/bare-metal-class-performance-mlperf-inference) |
| Llama 2 70B Interactive (450 ms TTFT, 40 ms TPOT) | 8x B200 vs 8x H200 | Server | "3.1x higher throughput" | n/a | 5.0-0056, 5.0-0060 | [NVIDIA MLPerf v5.0 blog](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/) |
| Llama 3.1 405B | 8x B200 (Lambda, FP4) | Offline / Server | 1,648.6 / 1,246.8 | 206 / 156 (estimate) | v5.1 | [Lambda](https://lambda.ai/blog/lambda-mlperf-inference-v5.1) |
| Llama 3.1 405B | 8x B200 (Nebius) | Offline / Server | 1,660 / 1,280 | 208 / 160 (estimate) | 5.1-0077 | [Nebius](https://nebius.com/blog/posts/bare-metal-class-performance-mlperf-inference) |
| Llama 3.1 405B | 8x B200 (NVIDIA) | Offline / Server | 1,538.2 / 1,080.3 | 192 / 135 (estimate) | v5.0 best | [Lambda](https://lambda.ai/blog/lambda-mlperf-inference-v5.1) (as "v5.0 Best") |
| Llama 3.1 405B | 8x H200 (VMware vGPU) | Server / Offline | 277 / 547 | 35 / 68 (estimate) | v5.1 | [VMware](https://blogs.vmware.com/cloud-foundation/2025/12/15/mlperf-5-1-confirms-vcf-future-of-ai-ml-performance/) |
| Llama 3.1 405B | 8x H200 (Nebius) | Offline / Server | B200 is "3x and 4.3x" higher, so about 553 / 298 (estimate: 1,660/3 and 1,280/4.3) | ~69 / ~37 (estimate) | 5.1-0079 | [Nebius](https://nebius.com/blog/posts/bare-metal-class-performance-mlperf-inference) |
| Llama 3.1 405B | 4x GB200 (Nebius) | Offline / Server | 855.8 / 596.1 | 214 / 149 (estimate) | 5.1-0078 | same |
| Llama 3.1 405B | NVIDIA platform record | Offline / Server / Interactive | n/a | 224 / 170 / 138 | v5.1 | [NVIDIA MLPerf v5.1 blog](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut) |
| Llama 3.1 405B | GB200 NVL72 vs 8x H200 | Offline / Server | "2.8x faster offline and 3.4x faster in server mode" per GPU | n/a | 5.0-0058, 5.0-0060 | [NVIDIA MLPerf v5.0 blog](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/) |
| DeepSeek R1 | 8x H200 (DGX H200, NVIDIA, unverified) | Offline / Server | n/a | 1,253 / 556 | not verified | [NVIDIA MLPerf v5.1 blog](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut) |
| DeepSeek R1 | GB200 NVL72 (72 GPUs) | Offline / Server | n/a | 4,024 / 2,327 | 5.1-0071 | same |
| DeepSeek R1 | GB300 NVL72 (72 GPUs) | Offline / Server | n/a | 5,842 / 2,907 | 5.1-0072 | same |
| Mixtral 8x7B | 8x B200 vs 8x H200 | Server / Offline | 126,845 / 128,148 vs 61,802 / 62,630 | 15,856 / 16,019 vs 7,725 / 7,829 (estimate) | 5.0-0056, 5.0-0060 | [NVIDIA MLPerf v5.0 blog](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/) |

Latency constraints: Llama 3.1 405B server has 6 s TTFT and 175 ms TPOT (v5.0); Llama 2 70B Interactive has 450 ms TTFT and 40 ms TPOT (25 tok/s per user) ([v5.0 blog](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/)); DeepSeek-R1 server has 2 s TTFT and 12.5 tok/s per user at p99; 405B interactive has 4.5 s TTFT and 12.5 tok/s per user ([v5.1 blog](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut)). NVIDIA did not submit DeepSeek R1 on 8x B200 or 8x H100; no B200 R1 MLPerf number exists in these sources.

### Inferences
- MLPerf 70B server numbers (about 12,500 per B200, 4,170 per H200, ~3,700 per H100) are upper bounds for chat serving because the server TPOT target is loose (5 to 25 tok/s per user) and the dataset has short outputs; they are 2x to 5x above the 50 tok/s per user InferenceX output estimates.
- MLPerf 405B numbers scale to a dense 70B as roughly 1/6 per GPU, consistent with parameter count.

### Gaps
- I could not retrieve the MLCommons results table directly, so H100 v5.1 and bare-metal H200 405B entries are inferred from vendor blogs with stated ratios.
- No MLPerf B200 (8-GPU) DeepSeek R1 submission was found.

## Key Question 7: Whole-node serving of the big MoE models (8x H100, 8x H200, 8x B200)

### Takeaway
Of the six big MoE models, only GLM-4.5/4.6 (FP8), Qwen3-235B (FP8 or BF16) and, marginally, Qwen3-Coder-480B (FP8) fit one 8x H100 node; DeepSeek V3/R1/V3.2 (FP8, about 671 GB) and Kimi K2 (959 GB) do not, and need 8x H200 (or two H100 nodes) at minimum, with Kimi K2 tight even on 8x H200. Measured node aggregates at high concurrency run from about 1,900 output tok/s (GLM-4.6 on 8x H100) to about 8,600 (DeepSeek V3.2 on 8x B200 with TRT-LLM), far below vendor offline tables.

### Cited Findings

Fit on one 8-GPU node. HBM per node: 8x H100 = 640 GB, 8x H200 = 1,128 GB, 8x B200 = 1,440 GB (180 GB each per the [TRT-LLM hardware list](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)). vLLM "conservatively uses 90% of GPU memory" by default ([vLLM GLM recipe](https://docs.vllm.ai/projects/recipes/en/stable/GLM/GLM.html)), so usable is about 576, 1,015 and 1,296 GB (estimate: x0.9).

| Model | Weights (FP8 unless noted) | 8x H100 FP8 | 8x H200 | 8x B200 | Source |
|---|---|---|---|---|---|
| DeepSeek V3 / R1 / V3.2 | about 671 GB (estimate: 671B x 1 byte) | Does not fit. SGLang lists FP8 on "2x8x H100/H800/H20" only; 8x H100 appears only under "W4A8 / AWQ / MXFP4 / NVFP4" | Fits: "8x H200" listed for FP8; "34GB free device memory per H200" under TP8 | Fits: "8x B200" for FP8; "8/4x B200" for NVFP4 | [SGLang DeepSeek docs](https://docs.sglang.io/basic_usage/deepseek_v3.html); [vLLM blog](https://vllm.ai/blog/2025-12-17-large-scale-serving) |
| Kimi K2 | "Weights-on-disk: 959GB" | Does not fit (959 GB > 640 GB); Lambda recommends 16x H100 | Marginal: 959 GB of 1,128 GB leaves about 169 GB for KV (estimate); vLLM recipe says native FP8 needs "a cluster with 16 GPUs" and benchmarks on 16x H200; no single-node 8x H200 benchmark found | Fits: "Idle vRAM usage: 1,347GB" on 8x B200 TP8 (about 93 GB free, estimate: 1,440 minus 1,347) | [Lambda](https://lambda.ai/blog/how-to-serve-kimi-k2-instruct-on-lambda-with-vllm); [vLLM Kimi-K2 recipe](https://docs.vllm.ai/projects/recipes/en/latest/moonshotai/Kimi-K2.html) |
| GLM-4.5 / 4.6 | about 358 GB (estimate: 358B x 1 byte); BF16 about 716 GB | Fits at FP8: official "H100 x 8" for FP8; BF16 "cannot be served on a single server with NVIDIA H100 GPUs" | Fits; FP8 fits 4x H200 ("H200 x 4"), so an 8x H200 node can run two replicas | Fits (no benchmark found) | [HF GLM-4.5](https://huggingface.co/zai-org/GLM-4.5); [GPUStack H100](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h100/) |
| Qwen3-235B-A22B | FP8 "well over 200 gigabytes"; BF16 about 470 GB (estimate) | Fits: FP8 on 4x H100 (TP4), BF16 on 8x H100 (TP8) | Fits; TRT-LLM uses DEP4 (two replicas per node) | Fits; TRT-LLM uses DEP4 FP4 | [Baseten](https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/); [GPUStack H100](https://docs.gpustack.ai/2.2/performance-lab/qwen3-235b-a22b/h100/); [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| Qwen3-Coder-480B-A35B | about 480 GB (estimate: 480B x 1 byte) | Marginal: 480 GB of 576 GB usable leaves about 96 GB for KV across 8 GPUs (estimate); the vLLM recipe targets "8xH200 (or H20) GPUs (141GB x 8)" and notes TP8 "fails for the FP8 model", so DP8 + EP is required; not benchmarked on H100 | Fits (recipe target) | Fits (no benchmark found) | [vLLM Qwen3-Coder recipe](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Coder-480B-A35B.html) |

Measured node aggregates at high concurrency (output tokens/s for the whole 8-GPU node, and per GPU). "Queued N" means N requests submitted at once with no concurrency cap, the GPUStack method; it is the highest-concurrency regime available.

| Model | Node | Engine, precision, parallelism | Workload, concurrency | Node output tok/s | Per GPU | Per-user tok/s | Type | Source |
|---|---|---|---|---|---|---|---|---|
| DeepSeek R1 0528 | 8x H100 | none at FP8 (does not fit) | n/a | n/a | n/a | n/a | n/a | [SGLang docs](https://docs.sglang.io/basic_usage/deepseek_v3.html) |
| DeepSeek R1 0528 | 16x H100 (two nodes) | Dynamo SGLang FP8, disaggregated | 8k/1k, InferenceX frontier | peak 1,376 listed per GPU, about 153 output per GPU, about 2,450 per 16 GPUs (estimates: /9, x16) | ~153 | peak point, not stated | Independent | [InferenceX](https://inferencex.semianalysis.com/run/deepseek-r1-on-h100) |
| DeepSeek V3 | 72x H100 decode (9 nodes) | SGLang EP72, PD disaggregation | 2000 in / 100 out, batch 256 per node | 22,282 per node | 2,785 (estimate) | ~10.9 (estimate) | Vendor (engine team) | [LMSYS](https://lmsys.org/blog/2025-05-05-large-scale-ep/) |
| DeepSeek R1 0528 | 8x H200 | SGLang v0.5.3 FP8, TP8 + DP attention | ShareGPT, queued 1000 | 3,415 | 427 | ~3 (TPOT 305 ms) | Independent | [GPUStack](https://docs.gpustack.ai/2.2/performance-lab/deepseek-r1/h200/) |
| DeepSeek R1 0528 | 8x H200 | vLLM v0.11.0 FP8 TP8 | ShareGPT, queued 1000 | 2,621 | 328 | ~4 | Independent | same |
| DeepSeek R1 0528 | 8x H200 | SGLang optimized | 4000/200, queued 500 | 767 | 96 | ~9 | Independent | same |
| DeepSeek R1 | 8x H200 | TensorRT-LLM (online) | 3200/800, concurrency up to 128 | 4,176 | 522 | not stated | Independent | [dstack](https://dstack.ai/blog/h200-mi300x-deepskeek-benchmark/) |
| DeepSeek R1 | 8x H200 | SGLang (offline) | 3200/800 to 3200, batch up to 1024 | 6,311 | 789 | n/a | Independent | same |
| DeepSeek R1 | 8x H200 | TRT-LLM, MLPerf server (12.5 tok/s/user p99, TTFT 2 s) | MLPerf R1 | 4,448 (estimate: 556 x 8); offline 10,024 (estimate: 1,253 x 8) | 556 / 1,253 | 12.5 | Vendor (unverified by MLCommons) | [NVIDIA MLPerf v5.1 blog](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut) |
| DeepSeek R1 0528 | 8x H200 | trtllm-bench DEP8 FP8, offline max load | 1000/1000 | 13,016 (estimate: 1,627 x 8) | 1,627 | not stated | Vendor | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| DeepSeek V3.2 | 8x H200 | SGLang v0.5.6.post2 FP8, TP8 DP8 DP-attention | ShareGPT, queued 1000 | 3,968 | 496 | ~5 | Independent | [GPUStack](https://docs.gpustack.ai/2.1/performance-lab/deepseek-v3.2/h200/) |
| DeepSeek V3.2 | 8x H200 | vLLM v0.13.0 FP8 TP8 | ShareGPT, queued 1000 | 2,702 | 338 | ~4 | Independent | same |
| DeepSeek V3.2 | 8x B200 | TRT-LLM TP8 EP8, attention DP, MTP-1, FP8 KV | 8K/1K, concurrency 256 | 8,618 | 1,077 | 11.3 | Vendor | [TRT-LLM V3.2 blog](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog15_Optimizing_DeepSeek_V32_on_NVIDIA_Blackwell_GPUs) |
| DeepSeek R1 0528 | 8x B200 (two DEP4 replicas) | trtllm-bench DEP4 NVFP4, offline | 1000/1000 | 51,704 (estimate: 6,463 x 8) | 6,463 | not stated | Vendor | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| DeepSeek R1 0528 | 8x B200 (two DEP4 replicas) | same | 8192/1024 | 9,344 (estimate: 1,168 x 8) | 1,168 | not stated | Vendor | same |
| DeepSeek R1 | 8x B200 (two TP4/EP4 replicas) | SGLang v0.5.6 NVFP4 | 8k/1k, concurrency 128 per replica | about 4,580 output (estimate: 5,145 listed / 9 x 8) | ~572 (estimate) | 18.6 | Independent | [InferenceX blog](https://inferencex.semianalysis.com/blog/sglang-0-5-6-b200-deepseek-r1-fp4-up-to-1-8x) |
| DeepSeek R1 | 8x B200 | best SGLang / Dynamo / TRT-LLM config, FP4 | 8k/1k frontier peak | about 11,940 output (estimate: 13,430 listed / 9 x 8) | ~1,492 (estimate) | peak point | Independent | [InferenceX](https://inferencex.semianalysis.com/run/deepseek-r1-on-b200) |
| Kimi K2 | 8x H100 | none (does not fit) | n/a | n/a | n/a | n/a | n/a | [Lambda](https://lambda.ai/blog/how-to-serve-kimi-k2-instruct-on-lambda-with-vllm) |
| Kimi K2 | 8x H200 | none found single-node | n/a | n/a | n/a | n/a | n/a | gap |
| Kimi K2 | 16x H200 (two nodes) | vLLM TP8 x PP2, DCP8, FP8 | 8000/1000, 16 prompts | 339 (peak 384) | 21 (estimate) | ~22 | Vendor (engine recipe), low concurrency | [vLLM Kimi-K2 recipe](https://docs.vllm.ai/projects/recipes/en/latest/moonshotai/Kimi-K2.html) |
| Kimi K2 | 96x H200 decode (12 nodes) + 32x H200 prefill | SGLang PD disaggregation, large EP, FP8 | 2000 in / 100 out, decode batch 480 | 288,000 decode total; 24,000 per 8-GPU decode node (estimate) | 3,000 per decode GPU (estimate) | ~6 (estimate) | Vendor (engine team) | [LMSYS](https://www.lmsys.org/blog/2025-07-20-k2-large-scale-ep/) |
| Kimi K2.6 (proxy) | H200 | best engine | 8k/1k at 40 tok/s/user | about 770 output per 8 GPUs (estimate: 867 listed / 9 x 8) | ~96 (estimate) | 40 | Independent (K2.6) | [InferenceX compare](https://inferencex.semianalysis.com/compare/kimi-k26-b300-vs-h200) |
| Kimi K2 | 8x B200 | vLLM TP8, defaults | ShareGPT, 10 prompts | 220 | 27.5 (estimate) | ~57 | Vendor (cloud), untuned | [Lambda](https://lambda.ai/blog/how-to-serve-kimi-k2-instruct-on-lambda-with-vllm) |
| Kimi K2.6 (proxy) | 8x B200 | Dynamo vLLM / vLLM FP4 | 8k/1k at 50 tok/s/user; at 30; peak | about 3,070; 4,210; 14,760 output per 8 GPUs (estimates: listed 3,449; 4,732; 16,602 / 9 x 8) | ~383; ~526; ~1,845 (estimates) | 50; 30; peak | Independent (K2.6) | [InferenceX](https://inferencex.semianalysis.com/run/kimi-k26-on-b200) |
| GLM-4.6-FP8 | 8x H100 | SGLang v0.5.3 TP8 EP8 | ShareGPT, queued 1000 | 1,861 | 233 (estimate) | ~1.5 (TPOT 677 ms) | Independent | [GPUStack H100](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h100/) |
| GLM-4.6-FP8 | 8x H100 | vLLM v0.11.0 TP8 | ShareGPT, queued 1000 | 1,528 | 191 (estimate) | ~2 (TPOT 509 ms) | Independent | same |
| GLM-4.6 (BF16) | 8x H200 | SGLang v0.5.3 TP8 | ShareGPT, queued 1000 | 3,367 | 421 (estimate) | not stated | Independent | [GPUStack H200](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h200/) |
| GLM-4.6 (BF16) | 8x H200 | vLLM v0.11.0 TP8 | ShareGPT, queued 1000 | 2,908 | 363 (estimate) | ~5 (TPOT 198 ms) | Independent | same |
| GLM-4.6-FP8 | 8x H200 (as two TP4 replicas) | SGLang v0.5.3 TP4 | ShareGPT, queued 1000 per replica | 6,832 (estimate: 3,416 x 2; the page itself normalizes with "x2") | 854 (estimate) | ~4 (TPOT 256 ms) | Independent | same |
| GLM-4.6-FP8 | 8x H200 (two TP4 replicas) | same | 4000/200, queued 500 per replica | 1,424 (estimate: 712 x 2) | 178 (estimate) | ~10 | Independent | same |
| GLM-4.5-FP8 | unstated (TP8 in examples) | vLLM | 8000/1000, 16 prompts | 652 | 81 if 8 GPUs (estimate) | ~45 | Vendor (engine recipe) | [vLLM GLM recipe](https://docs.vllm.ai/projects/recipes/en/stable/GLM/GLM.html) |
| GLM-4.5 / 4.6 | 8x B200 | none found | n/a | n/a | n/a | n/a | gap | GLM-5 proxy only: about 2,480 output per 8 GPUs at 50 tok/s/user on 8k/1k (estimate: 2,792 / 9 x 8) per [InferenceX](https://inferencex.semianalysis.com/run/glm-5-1-on-b200) |
| Qwen3-235B-A22B-Instruct-2507 (BF16) | 8x H100 | vLLM v0.11.0 TP8 | ShareGPT, queued 984 | 4,015 | 502 (estimate) | ~7 (TPOT 148 ms) | Independent | [GPUStack H100](https://docs.gpustack.ai/2.2/performance-lab/qwen3-235b-a22b/h100/) |
| same (BF16) | 8x H100 | SGLang v0.5.5.post1 TP8 | ShareGPT, queued 984 | 3,645 | 456 (estimate) | not stated | Independent | same |
| same (BF16) | 8x H100 | vLLM TP8 | 4000/200, queued 500 | 931 | 116 (estimate) | ~14.5 | Independent | same |
| Qwen3-235B-A22B-Instruct-2507-FP8 | 8x H100 (as two TP4 replicas) | vLLM v0.11.0 TP4, max-num-batched-tokens 16384 | ShareGPT, queued 984 per replica | 7,402 (estimate: 3,701 x 2) | 925 (estimate) | ~5 (TPOT 186 ms) | Independent | same |
| same FP8 | 8x H100 (two TP4 replicas) | same | 4000/200, queued 500 per replica | 1,436 (estimate: 718 x 2) | 180 (estimate) | ~11 | Independent | same |
| Qwen3-235B-A22B | 8x H100 | trtllm-bench DEP8 FP8, offline | 1000/1000 | 15,456 (estimate: 1,932 x 8) | 1,932 | not stated | Vendor | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| Qwen3-235B-A22B | 8x H200 (two DEP4 replicas) | trtllm-bench DEP4 FP8, offline | 1000/1000 | 26,304 (estimate: 3,288 x 8) | 3,288 | not stated | Vendor | same |
| Qwen3-235B | H200, replica GPU count not stated (FP8 TP4 on Hopper per the post) | SGLang day-zero, FP8 | 1000/1000, batch 384 | ~4,600 total tok/s per replica, about 2,300 output (estimate: half); about 4,600 output per 8 GPUs if TP4 replicas (estimate) | ~575 (estimate) | not stated | Vendor (inference cloud), dated 2025-04 | [Baseten](https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/) |
| Qwen3-235B-A22B | 8x B200 (two DEP4 replicas) | trtllm-bench DEP4 FP4, offline | 1000/1000 | 46,112 (estimate: 5,764 x 8) | 5,764 | not stated | Vendor | [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html) |
| Qwen3-Coder-480B-A35B-FP8 | 8x H100 | none (marginal fit, not benchmarked) | n/a | n/a | n/a | n/a | gap | [vLLM recipe](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Coder-480B-A35B.html) |
| Qwen3-Coder-480B-A35B-FP8 | 8x H200 (recipe target; result block does not restate hardware) | vLLM DP8 + EP | 2048/1024, concurrency 10 | 132 | 16.5 (estimate) | ~14.6 (TPOT 68 ms) | Vendor (engine recipe), low concurrency | same |
| Qwen3-Coder-480B-A35B | 8x B200 | none found | n/a | n/a | n/a | n/a | gap | gap |

### Inferences
- Models that need the full 8x H200 node for weights (DeepSeek, Kimi K2) deliver about 300 to 800 output tok/s per GPU at high concurrency with a single-node engine, because KV cache, not compute, is the limit; splitting the node into two 4-GPU replicas is impossible for them but roughly doubles per-GPU throughput for GLM-4.6-FP8 and Qwen3-235B-FP8 (GPUStack H200 and H100 data).
- Estimate for GLM-4.5/4.6 on 8x B200: 6,832 (8x H200 two-replica measured) x 3.5 (midpoint of the measured B200/H200 ratios 2.7 to 4.9) = about 24,000 output tok/s per node, or 3,000 per GPU, at ShareGPT-style high concurrency. Low confidence.
- Estimate for Kimi K2 on 8x H200 single node: KV headroom of about 169 GB (estimate) is about one fifth of the 8x B200 free memory; InferenceX K2.6 reached no interactivity tier on H200 with INT4 vLLM across 15 configs, so plan on at most the 770-per-node figure at 40 tok/s per user, or run two nodes.
- The GPUStack "queued 1000" regime drives per-user speed down to 2 to 7 tok/s, so these node aggregates are the throughput-maximizing ceiling for a general-purpose engine, not a 50 tok/s per user operating point.

### Gaps
- No single-node 8x H200 benchmark for Kimi K2 and no 8x B200 benchmark for GLM-4.5/4.6, Qwen3-Coder-480B or (tuned) Kimi K2.
- No 8x H100 benchmark for Qwen3-Coder-480B.
- No W4A8 or INT4 DeepSeek benchmark on 8x H100, although the SGLang matrix lists that as supported.

## Recommended planning numbers

### Takeaway
For a revenue model, plan on the "conservative" output tok/s per GPU below for mixed real traffic at about 50 tok/s per user, and the "typical" figure for a well-tuned deployment at 30 to 50 tok/s per user on 1k/1k-like traffic; the "vendor best" column is the offline ceiling and should not be used for revenue.

### Cited Findings
All figures are output tokens/s per GPU. "Vendor best" cites the TRT-LLM 1k/1k offline table unless noted. Conservative and typical are my estimates; the reasoning column shows the inputs. Output tokens per GPU-hour = typical x 3,600.

| Model | GPU | GPUs per replica (precision) | Conservative output tok/s/GPU | Typical output tok/s/GPU | Typical output tokens per GPU-hour | Vendor best (offline, 1k/1k) | Reasoning and sources |
|---|---|---|---|---|---|---|---|
| gpt-oss-120b | H100 | 1 (MXFP4; TP2 improves per-GPU) | 1,500 | 3,000 | 10.8M | 4,685 | GPUStack vLLM TP2 ShareGPT 3,824 at ~12 tok/s/user; Simplismart untuned TP2 734 at 39 tok/s/user; InferenceX 8k/1k ~1,000 output at 50 tok/s/user (estimate). Typical = 65% of vendor; conservative = 1/3 of vendor. |
| gpt-oss-120b | H200 | 1 (MXFP4) | 2,000 | 4,000 | 14.4M | 6,868 | TRT-LLM 1.47x H100 offline; InferenceX only 1.04x at 50 tok/s/user. Scaled H100 planning by 1.3x. |
| gpt-oss-120b | B200 | 1 to 2 (FP4) | 8,000 | 15,000 | 54.0M | 25,943 (60,000 with Eagle3 claim) | NVIDIA InferenceMAX 1k/1k ~10,000 at 100 tok/s/user (unit uncertain); InferenceX 8k/1k ~4,900 output at 50 tok/s/user (estimate). Typical = 58% of vendor table. |
| gpt-oss-20b | H100 | 1 (MXFP4) | 4,500 | 7,500 | 27.0M | 11,557 | Vendor only. Conservative = 40%, typical = 65% of vendor (same ratios as gpt-oss-120b H100). |
| gpt-oss-20b | H200 | 1 | 5,500 | 9,000 | 32.4M | 13,858 | Same ratios. |
| gpt-oss-20b | B200 | 1 (FP4) | 20,000 | 35,000 | 126M | 53,812 | Same ratios. |
| Llama 3.3 70B | H100 | 2 (FP8 TP2) or 1 (FP8, small KV) | 600 | 1,200 | 4.3M | 2,209 | GeneralCompute vLLM FP8 TP4: 850/GPU at 256 concurrent, 22 tok/s/user at 64; InferenceX 8k/1k ~166 output at 50 tok/s/user (estimate). Typical = 54% of vendor. |
| Llama 3.3 70B | H200 | 1 to 2 (FP8) | 800 | 1,600 | 5.8M | 2,587 | InferenceX H200/H100 = 1.40x at 50 tok/s/user; MLPerf 70B server 4,170/GPU is an upper bound. |
| Llama 3.3 70B | B200 | 1 (FP4) | 2,500 | 4,500 | 16.2M | 6,920 (NVIDIA claims 10,000 at 50 tok/s/user on 1k/1k) | InferenceX B200/H200 = 2.9x; MLPerf 70B server 12,500/GPU upper bound. |
| Qwen3-235B-A22B | H100 | 4 (FP8 TP4) or 8 (DEP8) | 500 | 1,000 | 3.6M | 1,932 | Vendor 1k/1k only; Baseten day-zero ~175/GPU at 45 tok/s/user on H200 (estimate, dated). Typical = 52% of vendor. |
| Qwen3-235B-A22B | H200 | 4 (FP8 DEP4) | 800 | 1,700 | 6.1M | 3,288 | Same ratio; TRT-LLM H200/H100 = 1.70x. |
| Qwen3-235B-A22B | B200 | 4 (FP4 DEP4) | 1,500 | 3,000 | 10.8M | 5,764 | Same ratio; TRT-LLM B200/H200 = 1.75x. |
| Qwen3-32B | H100 | 1 (FP8) | 500 | 1,000 | 3.6M | 2,060 (GPUStack TRT-LLM FP8, ShareGPT, ~6 tok/s/user) | Independent only; 2k/100 gave 282/GPU. Typical = 50% of the high-concurrency ShareGPT figure. |
| Qwen3-32B | H200 | 1 (FP8) | 650 | 1,300 | 4.7M | none found | Estimate: H100 x 1.3 (Llama 70B InferenceX H200/H100 1.4x, TRT-LLM 1.17x). |
| Qwen3-32B | B200 | 1 (FP4) | 1,800 | 3,500 | 12.6M | none found | Estimate: H200 x 2.7 (Llama 70B TRT-LLM B200/H200 2.67x). |
| Qwen3-Coder-480B-A35B | H100 | 16 (FP8 2-node) | 250 | 500 | 1.8M | none | Estimate: Qwen3-235B x 0.5 (35B vs 22B active, 2x weights, 2-node penalty). Low confidence. |
| Qwen3-Coder-480B-A35B | H200 | 8 (FP8 DP8 EP) | 500 | 1,000 | 3.6M | none; vLLM recipe shows 16.5/GPU at concurrency 10 untuned | Estimate: Qwen3-235B H200 x 0.6. Low confidence. |
| Qwen3-Coder-480B-A35B | B200 | 8 (FP4 or FP8) | 1,000 | 2,000 | 7.2M | none | Estimate: Qwen3-235B B200 x 0.65. Low confidence. |
| DeepSeek V3 / R1 / V3.2 | H100 | 16 (FP8, 2 nodes) | 100 | 250 | 0.9M | none (LMSYS 96-GPU decode: 2,785/decode GPU at ~11 tok/s/user, 2k/100) | InferenceX multi-node H100: ~8 to 13 output at 30 to 50 tok/s/user, peak ~153 output (estimates); compare page 739 total at 45. Very low and interconnect-bound. |
| DeepSeek V3 / R1 / V3.2 | H200 | 8 (FP8) | 400 | 800 | 2.9M | 1,627 (2,200 vLLM wide-EP multi-node claim) | GPUStack SGLang 427/GPU at ~3 tok/s/user; dstack TRT-LLM online 522/GPU at 3200/800; MLPerf server 556 at 12.5 tok/s/user; InferenceX ~133 output at 50 tok/s/user (estimate); V3.2 SGLang 1K/2K ~309/GPU at 25 tok/s/user. |
| DeepSeek V3 / R1 / V3.2 | B200 | 8 (FP4; 4 possible) | 1,500 | 3,000 | 10.8M | 6,463 | TRT-LLM V3.2 TP8/EP8 8K/1K: 1,077/GPU at 11 tok/s/user; InferenceX ~512 output at 50 tok/s/user and ~1,490 peak on 8k/1k (estimates); 1k/1k output share is 4.5x higher than 8k/1k. Typical = 46% of vendor. |
| GLM-4.5 / 4.6 | H100 | 8 (FP8) | 200 | 400 | 1.4M | none | Estimate: 0.5x DeepSeek H200 planning since FP8 fits 8x H100 but with little KV; 32B active vs 37B. Low confidence. |
| GLM-4.5 / 4.6 | H200 | 4 to 8 (FP8) | 400 | 900 | 3.2M | none; vLLM recipe 651 output on unstated GPUs at 8k/1k, 45 tok/s/user | Estimate: DeepSeek H200 x 1.1 (fewer active params, half the weights); InferenceX GLM-5 (different model) ~64 output at 50 tok/s/user on 8k/1k. Low confidence. |
| GLM-4.5 / 4.6 | B200 | 4 to 8 (FP4 or FP8) | 1,500 | 3,000 | 10.8M | none | Estimate: same as DeepSeek B200; InferenceX GLM-5 B200/H200 = 4.9x. Low confidence. |
| Kimi K2 | H100 | 16 (FP8, 2 nodes) | 80 | 200 | 0.7M | none | Estimate: 0.8x DeepSeek H100 (959 GB weights). Very low confidence. |
| Kimi K2 | H200 | 8 to 16 (FP8) | 300 | 700 | 2.5M | none (LMSYS 128-GPU PD: 3,000/decode GPU at ~6 tok/s/user, 2k/100) | InferenceX K2.6 H200 867 total at 40 tok/s/user, ~96 output (estimate); single-node 8x H200 leaves ~170 GB for KV. |
| Kimi K2 | B200 | 8 (FP4 or native) | 1,200 | 2,500 | 9.0M | none (InferenceX K2.6 peak 16,602 total, ~1,845 output estimate) | InferenceX K2.6 ~383 output at 50 tok/s/user on 8k/1k (estimate); Lambda untuned vLLM TP8 27.5/GPU at ~10 concurrent. |
| Mistral Small 3.x 24B | H100 | 1 (FP8 or BF16) | 700 | 1,400 | 5.0M | none | Estimate: Qwen3-32B H100 x 1.33 (24B vs 32B dense); Spheron ~1,700/GPU unspecified shape. Low confidence. |
| Mistral Small 3.x 24B | H200 | 1 | 900 | 1,800 | 6.5M | none | Estimate: H100 x 1.3. Low confidence. |
| Mistral Small 3.x 24B | B200 | 1 (FP4) | 2,300 | 4,500 | 16.2M | none | Estimate: H200 x 2.5. Low confidence. |
| Llama 4 Scout | H100 | 2 (FP8) or 1 (INT4) | 500 | 1,000 | 3.6M | none | Estimate: H200 / 1.4. Low confidence. |
| Llama 4 Scout | H200 | 1 to 2 (FP8) | 700 | 1,300 | 4.7M | none ("3.4x" below B200 per NVIDIA) | Estimate: B200 planning / 3.4. Low confidence. |
| Llama 4 Scout | B200 | 8 (FP8) or 1 to 2 (FP4) | 2,000 | 4,000 | 14.4M | ~5,000 per GPU if NVIDIA's ">40K" is 8 GPUs (estimate) | Vendor claim only. Typical = 80% of the per-GPU estimate because the claim's GPU count is unstated. |
| Llama 4 Maverick | H100 | 8 (FP8, 400 GB weights) | 900 | 1,800 | 6.5M | none | Estimate: 0.7x H200 (KV-starved on 640 GB). Low confidence. |
| Llama 4 Maverick | H200 | 8 (FP8 DEP8) | 1,200 | 2,500 | 9.0M | 4,146 | Typical = 60% of vendor 1k/1k; 8k/1k vendor is 1,276. |
| Llama 4 Maverick | B200 | 4 (FP4 DEP4) | 3,500 | 7,000 | 25.2M | 11,337 | Typical = 62% of vendor; 8k/1k vendor is 3,279. |

Reference ceilings for other models in the brief: Llama 3.1 405B at MLPerf server is 156 to 160 per B200 and about 35 per H200 ([Lambda](https://lambda.ai/blog/lambda-mlperf-inference-v5.1), [VMware](https://blogs.vmware.com/cloud-foundation/2025/12/15/mlperf-5-1-confirms-vcf-future-of-ai-ml-performance/)).

Whole-node planning numbers for the big MoE models (one 8-GPU node; output tokens/s for the node, with per GPU in parentheses; "typical" is for a tuned engine at high concurrency, about 30 to 50 tok/s per user; "conservative" is for mixed traffic with long prompts). Fit status is from Key Question 7.

| Model | 8x H100 node (FP8) | 8x H200 node | 8x B200 node | Reasoning and sources |
|---|---|---|---|---|
| DeepSeek V3 / R1 / V3.2 | Does not fit at FP8 (671 GB vs 640 GB). Two H100 nodes: conservative 1,600 (100), typical 4,000 (250) for 16 GPUs. W4A8/INT4 single node is listed as supported but unbenchmarked. | Fits (FP8). Conservative 3,200 (400); typical 6,400 (800). Measured: GPUStack SGLang 3,415 at 3 tok/s/user, dstack TRT-LLM 4,176 at up to 128 concurrent, MLPerf server 4,448 at 12.5 tok/s/user, SGLang offline 6,311; vendor offline 13,016. | Fits (FP4 or FP8). Conservative 12,000 (1,500); typical 24,000 (3,000). Measured: TRT-LLM V3.2 8,618 at 8K/1K and 11 tok/s/user; InferenceX 8k/1k peak about 11,940 output (estimate); vendor offline 1k/1k 51,704. Typical = 46% of vendor. | [SGLang docs](https://docs.sglang.io/basic_usage/deepseek_v3.html), [GPUStack](https://docs.gpustack.ai/2.2/performance-lab/deepseek-r1/h200/), [dstack](https://dstack.ai/blog/h200-mi300x-deepskeek-benchmark/), [NVIDIA MLPerf](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut), [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html), [TRT-LLM V3.2](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog15_Optimizing_DeepSeek_V32_on_NVIDIA_Blackwell_GPUs), [InferenceX](https://inferencex.semianalysis.com/run/deepseek-r1-on-b200) |
| Kimi K2 (1T) | Does not fit (959 GB). Needs 16x H100 or H200/B200. Two H100 nodes: conservative 1,300 (80), typical 3,200 (200) for 16 GPUs. Very low confidence. | Marginal fit (959 GB of 1,128 GB; about 169 GB KV, estimate). Conservative 2,400 (300); typical 5,600 (700). Measured proxies: InferenceX K2.6 about 770 output per 8 GPUs at 40 tok/s/user on 8k/1k (estimate); LMSYS PD cluster 24,000 per 8-GPU decode node at 2k/100 and ~6 tok/s/user (decode nodes only). Prefer 16x H200 (vLLM recipe) or B200. | Fits (1,347 GB idle VRAM on TP8). Conservative 9,600 (1,200); typical 20,000 (2,500). Measured proxies: InferenceX K2.6 about 3,070 output at 50 tok/s/user and about 14,760 peak on 8k/1k (estimates); Lambda untuned vLLM 220 at ~10 concurrent. | [Lambda](https://lambda.ai/blog/how-to-serve-kimi-k2-instruct-on-lambda-with-vllm), [vLLM recipe](https://docs.vllm.ai/projects/recipes/en/latest/moonshotai/Kimi-K2.html), [LMSYS](https://www.lmsys.org/blog/2025-07-20-k2-large-scale-ep/), [InferenceX K2.6 B200](https://inferencex.semianalysis.com/run/kimi-k26-on-b200), [InferenceX compare](https://inferencex.semianalysis.com/compare/kimi-k26-b300-vs-h200) |
| GLM-4.5 / 4.6 (355B-A32B) | Fits at FP8 (358 GB); BF16 does not. Conservative 1,600 (200); typical 3,200 (400). Measured: GPUStack SGLang TP8 EP8 1,861 and vLLM 1,528 at ShareGPT queued 1000. Typical is 1.7x the measured ceiling to allow for newer engines, since GPUStack ran SGLang v0.5.3; treat as optimistic. | Fits; FP8 runs as two TP4 replicas. Conservative 3,200 (400); typical 7,200 (900). Measured: GPUStack SGLang FP8 TP4 3,416 per replica, 6,832 per node (estimate x2); BF16 TP8 3,367. | Fits. Conservative 12,000 (1,500); typical 24,000 (3,000). Estimate: 6,832 x 3.5 (midpoint of measured B200/H200 ratios); InferenceX GLM-5 proxy gives only about 2,480 output per 8 GPUs at 50 tok/s/user on 8k/1k. Low confidence. | [HF GLM-4.5](https://huggingface.co/zai-org/GLM-4.5), [GPUStack H100](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h100/), [GPUStack H200](https://docs.gpustack.ai/2.2/performance-lab/glm-4.x/h200/), [InferenceX GLM-5](https://inferencex.semianalysis.com/run/glm-5-1-on-b200) |
| Qwen3-235B-A22B | Fits (FP8 on 4 GPUs, BF16 on 8). Conservative 4,000 (500); typical 8,000 (1,000). Measured: GPUStack vLLM FP8 TP4 3,701 per replica, 7,402 per node (estimate x2); BF16 TP8 4,015; vendor offline DEP8 15,456. Typical = 52% of vendor. | Fits (two DEP4 or TP4 replicas). Conservative 6,400 (800); typical 13,600 (1,700). Vendor offline DEP4 26,304; Baseten day-zero about 4,600 output per 8 GPUs at batch 384 (estimate, dated). Typical = 52% of vendor. | Fits (two DEP4 FP4 replicas). Conservative 12,000 (1,500); typical 24,000 (3,000). Vendor offline 46,112. Typical = 52% of vendor. | [GPUStack H100](https://docs.gpustack.ai/2.2/performance-lab/qwen3-235b-a22b/h100/), [TRT-LLM table](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html), [Baseten](https://www.baseten.co/blog/day-zero-benchmarks-for-qwen-3-with-sglang-on-baseten/) |
| Qwen3-Coder-480B-A35B | Marginal fit at FP8 (480 GB of 576 GB usable, estimate); recipe targets H200; not benchmarked. Conservative 2,000 (250); typical 4,000 (500). Low confidence. | Fits (FP8, DP8 + EP). Conservative 4,000 (500); typical 8,000 (1,000). Only datapoint: vLLM recipe 132 output at concurrency 10 (untuned). Estimate: Qwen3-235B H200 x 0.6 (35B vs 22B active, 2x weights). Low confidence. | Fits. Conservative 8,000 (1,000); typical 16,000 (2,000). Estimate: Qwen3-235B B200 x 0.65. Low confidence. | [vLLM recipe](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Coder-480B-A35B.html) |

Models that cannot fit one 8x H100 node at FP8 and need H200 or B200 (or two H100 nodes): DeepSeek V3 / R1 / V3.2 (FP8 needs "2x8x H100" per [SGLang](https://docs.sglang.io/basic_usage/deepseek_v3.html)), Kimi K2 (959 GB per [Lambda](https://lambda.ai/blog/how-to-serve-kimi-k2-instruct-on-lambda-with-vllm)), GLM-4.5 / 4.6 at BF16 (FP8 fits per [HF](https://huggingface.co/zai-org/GLM-4.5)), and Qwen3-Coder-480B is marginal (estimate). Qwen3-235B fits in either precision.

### Inferences
- The conservative column assumes a general-purpose engine (vLLM or SGLang), default-ish tuning, mixed prompt lengths with some long-context traffic, and a 50 tok/s per user target; it is about one third of the vendor offline figure for single-GPU models and about one quarter for 8-GPU MoE models.
- The typical column assumes an engine tuned per the GPUStack or TRT-LLM recipes, DP/EP for MoE, FP8 or FP4 weights and KV cache, and 30 to 50 tok/s per user; it is about half to two thirds of the vendor offline figure.
- Revenue sensitivity: at the InferenceX hyperscaler TCO of $1.17 per H100-hour, a typical gpt-oss-120b H100 (10.8M output tokens per hour) costs about $0.11 per million output tokens before margin, versus $0.036 per million total tokens on the InferenceX page; the difference is the input-token share of the 8k/1k workload.

### Gaps
- Rows marked low confidence rest on scaling from a neighbouring model because no benchmark exists; they should be replaced with a `vllm bench serve` or `trtllm-bench` run on the target hardware before pricing is finalized.
- No source gives prefill tokens/s per GPU on H100/H200/B200 for most models; the only prefill figures are LMSYS DeepSeek (6,818 per H100 at 2k) and Kimi K2 (7,000 per H200 at 2k), and GB200 (26,156 per GPU). Prefill throughput per GPU for input-token revenue needs separate measurement.
