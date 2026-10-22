# Newer accelerators versus B200 for a small inference provider, plus Kimi K3 serving economics

Checked 2026-10-22. Read-only web check. Every number carries its source URL. "Estimate" marks my own arithmetic or a third-party aggregator figure. Prices are USD per GPU-hour unless stated.

## Verdict in six lines

1. B300 is rentable today with a card (RunPod $8.99, Nebius $9.50, DigitalOcean spot $6.17). It costs 12 to 14 percent more than B200 at the same provider and delivers 5 to 25 percent more output tokens per GPU on gpt-oss-120b and DeepSeek R1 at max throughput. Tokens per dollar lands at roughly 0.9 to 1.1 times B200. That is parity, not a win. (Estimate, arithmetic in section 3.)
2. What B300 really buys is memory: 288 GB (268 GB usable) per GPU, so one 8-GPU node holds Kimi K3 (about 1.5 TB MXFP4). B200 needs two nodes (16 GPUs) for the same model.
3. MI355X is the cheapest 288 GB part if you can get the low prices. Vultr lists "starting at $2.65" and Daytona $5.99 in stock. InferenceX measures MI355X at 9,217 tok/s per GPU on Kimi K3 at 50 tok/s per user, 52 percent above B300. Tokens per dollar on Kimi K3 is 1.6 to 4.5 times B200 depending on which MI355X price you can get. (Estimate.)
4. GB200 NVL72 is rentable in 4-GPU units at CoreWeave ($10.50 per GPU). GB300 NVL72 is quote-only almost everywhere (Oracle lists $18 per GPU). Vera Rubin NVL72 is live only at CoreWeave in limited availability with no public price. MI400 series (MI450 / MI455X) is waitlist only with no public price. TPU7x is GA at $12.00 per chip-hour on demand and needs GCP quota.
5. Kimi K3 serving economics look very good on paper. At OpenRouter's $5.50 per million output floor, an 8x B300 node at $7.94 per GPU-hour breaks even at about 7 percent utilization and an 8x MI355X node at $2.59 breaks even at about 1.4 percent. (Estimate.) The catch is that those throughput figures assume high concurrency on a benchmark workload; at low concurrency and 64K context the same node makes about 63 tok/s per GPU and loses money.
6. The Kimi K3 license is open for a small provider. The only hard gate is a separate agreement with Moonshot once Model-as-a-Service revenue passes $20 million in any 12 months.

## 1. Summary table

| Accelerator | Rentable now | Cheapest public $/GPU-hr | Min unit | Memory per GPU | Tokens per $ vs B200, gpt-oss-120b | Tokens per $ vs B200, DeepSeek-class | Big open models that fit one 8-GPU node | Verdict |
|---|---|---|---|---|---|---|---|---|
| B200 (baseline) | Yes, card | $6.69 Lambda 8x on demand; $5.50 Koyeb serverless; $8.50 Nebius | 1 GPU | 180 GB | 1.00 | 1.00 | GLM 5.3 FP8 (756 GB), Hy4 FP8 (814 GB), DeepSeek V4.1 Flash (510 GB), gpt-oss-120b. Kimi K3 no (needs 16 GPUs). | Baseline |
| B300 (Blackwell Ultra) | Yes, card | $6.17 DigitalOcean spot (8x); $7.10 Daytona GPU-only 1x; $7.94 DigitalOcean 12-month; $8.99 RunPod 1x; $9.50 Nebius | 1 GPU (RunPod, Nebius, Daytona); 8 GPUs (DigitalOcean) | 288 GB (268 GB usable) | 0.9 to 1.1 (estimate) | 0.8 to 1.3 (estimate; InferenceX 50 tok/s point shows 0.36, flagged) | All of the above plus Kimi K3 MXFP4 (about 1.5 TB) and 4-bit Qwen3.8 (about 1.2 TB, secondary source). Qwen3.8 FP8 (about 2.4 TB) does not fit. | Buy for memory, not for tokens per dollar |
| GB200 NVL72 | Yes, sales-led, 4-GPU instances | $10.50 CoreWeave on demand (4x = $42.00/hr); AWS Capacity Block $10.582 per accelerator at 36 or 72 GPUs | 4 GPUs (CoreWeave); 36 (AWS) | 186 GB (CoreWeave listing) | 0.8 (estimate, TRT-LLM parity on throughput, 22 percent price premium) | 0.5 (estimate, InferenceX 50 tok/s point) | Same as B200 per node; Kimi K3 needs 16 GPUs (4 trays) | Not for a small provider |
| GB300 NVL72 | Mostly quote-only | $18.00 Oracle BM.GPU.GB300.4 (4x) listed; Verda $12.16 (out of stock); CoreWeave, Nebius, Crusoe, Together: contact sales; Azure ND GB300 v6: quote | 4 GPUs | 288 GB | 0.6 (estimate, TRT-LLM +33 percent throughput, 2.1x price) | 0.25 to 0.6 (estimate) | Same as B300 per 8 GPUs | Not rentable at a usable price |
| Vera Rubin NVL72 (VR200) | Limited availability at CoreWeave only, no public price | None published | Rack-scale | Not verified here | n/a | n/a | n/a | Not rentable for a small provider in 2026 |
| RTX PRO 6000 Blackwell (96 GB) | Yes, card, widely | $1.39 CoreWeave spot (8x); $1.80 Nebius; $2.20 Koyeb; $2.49 RunPod; $2.50 CoreWeave on demand (8x = $20/hr) | 1 GPU | 96 GB GDDR7 | No matched benchmark. Llama 3.3 70B proxy: about 1.2 (estimate, TRT-LLM 1k/1k, Nebius prices) | n/a (DeepSeek R1 FP4 needs 8 GPUs with pipeline parallel; no published run) | gpt-oss-120b, DeepSeek V4.1 Flash FP8 (510 GB, tight), GLM 5.3 and Hy4 only at 4-bit; Kimi K3 no | Good for small models; irrelevant for 1T-class |
| AMD MI355X (288 GB) | Yes, thin supply | $2.65 Vultr "starting at" (8x reserve page); $2.95 TensorWave (sales); $3.44 Daytona spot 1x; $5.50 DigitalOcean spot 8x; $5.99 Daytona on demand 1x in stock; $8.60 Oracle 8x | 1 GPU (Daytona); 8 GPUs (Vultr, DO, Oracle) | 288 GB | 1.0 to 2.8 (estimate; 0.87x throughput, price 0.31x to 0.90x of B200) | 0.4 to 1.1 (estimate; 0.35x throughput at 50 tok/s) | Same as B300: Kimi K3 1x8 is the vLLM and SGLang reference recipe | Best tokens per dollar on Kimi K3 if you can get the sub-$3 price; ROCm risk |
| AMD MI400 / MI450 / MI455X (432 GB HBM4) | No. Waitlist at TensorWave, Vultr (pre-orders for 2027 to 2028), Cirrascale, Azure, Oracle | None published | 72-GPU Helios rack | 432 GB | n/a | n/a | Kimi K3 MXFP4 on 4 GPUs (estimate, getdeploying) | Not rentable in 2026 |
| Google TPU7x (Ironwood) | Yes, GA since 2026-03-31, needs GCP quota | $12.00 per chip-hour on demand (us-central1); $6.00 flex-start; $8.40 1-year; $5.40 3-year | 4-chip VM (tpu7x-standard-4t) | 192 GiB HBM | n/a (no public InferenceX or MLPerf per-chip gpt-oss run found) | n/a | n/a; only JAX and PyTorch stacks, no CUDA | List price 41 percent above Nebius B200; not a fit for a vLLM shop |

Sources for this table are in sections 2 through 5.

## 2. Rentable today, by accelerator

### B300 (HGX B300, Blackwell Ultra, 288 GB)

Self-serve with a card:
- RunPod: B300 Secure Cloud $8.99/hr per GPU, 1x in stock; 2x $8.99; Community Cloud $6.94 listed but out of stock. Serverless B300 $10.65/hr. https://www.runpod.io/pricing and https://getdeploying.com/gpus/nvidia-b300 (checked 2026-10-22).
- Nebius: HGX B300 on demand $9.50, preemptible from $0.99. Bank card via Stripe, $25 minimum first payment. B200 on the same page is $8.50. https://nebius.com/prices (checked 2026-10-22).
- DigitalOcean: B300 spot $6.17/GPU/hr, self-serve, 8-GPU droplet (size gpu-b300x8-2304gb-spot). 12-month reserved $7.94/GPU/hr via contact sales. No on-demand B300 tier listed. Cards accepted, billed per second with a 5-minute minimum. https://www.digitalocean.com/pricing/gpu-droplets (checked 2026-10-22).
- Crusoe: HGX B300 on demand $9.90/GPU-hr; managed inference self-serve dedicated B300 $13.80/GPU-hr. https://www.crusoe.ai/cloud/pricing (checked 2026-10-22).
- Daytona: 1x B300 GPU-only on demand $7.10, with 8 vCPU and 100 GB RAM $9.15; spot $4.08 GPU-only; 8x $9.15 on demand, all in stock. https://getdeploying.com/gpus/nvidia-b300 (checked 2026-10-22).
- Lium: 1x B300 SXM $8.00 in stock; 8x spot $6.85. https://getdeploying.com/gpus/nvidia-b300 (checked 2026-10-22).
- Vast.ai: HGX B300 from $8.38/GPU-hr (1x and 2x), 4x $11.33. https://computeprices.com/providers/vast/gpus/hgx-b300 (checked 2026-10-22).
- CoreWeave: HGX B300 8x spot $35.84/hr ($4.48 per GPU, estimate); on demand contact sales. https://www.coreweave.com/pricing (checked 2026-10-22).
- AWS: p6-b300.48xlarge (8x B300) Capacity Blocks $129.168/hr per instance, $16.146 per accelerator, us-east-1, us-west-2, Seoul, London and others. https://aws.amazon.com/ec2/capacityblocks/pricing/ (checked 2026-10-22). Third-party trackers put on-demand near $142.42/hr ($17.80 per GPU, estimate). https://aws-pricing.com/p6-b300.48xlarge.html (checked 2026-10-22).
- Term deals seen on getdeploying: Impossible Cloud 60-month $4.53, TheAI Cloud 36-month $4.70 and 24-month $5.00, GPUaaS custom $5.00, all 8x, pre-order. https://getdeploying.com/gpus/nvidia-b300 (checked 2026-10-22).
- getdeploying aggregate: 36 providers, median on-demand $8.99, cheapest listed $6.50 (Bentaus, not verified in stock), 90-day trend +12 percent. https://getdeploying.com/gpus/nvidia-b300 (checked 2026-10-22).
- Lambda, Voltage Park, Hyperbolic, Koyeb, Hot Aisle, Together: no B300 price on their public pages. Lambda's top on-demand part is B200 at $6.69 (8x) to $6.99 (1x). https://lambda.ai/pricing (checked 2026-10-22). Koyeb B200 serverless $5.50/hr. https://www.koyeb.com/pricing (checked 2026-10-22).
- shadeform tracker: DNS failed and the GPU page returned 404 on 2026-10-22, so it is not cited.

Minimum unit: 1 GPU at RunPod, Nebius, Daytona, Lium, Vast.ai. 8 GPUs at DigitalOcean, Crusoe, CoreWeave, AWS. Card: yes at RunPod, Nebius, DigitalOcean, Vast.ai. CoreWeave and AWS Capacity Blocks are account-approval or reservation flows.

### GB200 NVL72

- CoreWeave: 4-GPU instance (2 GB200 superchips) $42.00/hr on demand = $10.50 per GPU (estimate). Inference-platform single-GPU rate $10.50 for eligible customers. https://www.coreweave.com/pricing (checked 2026-10-22).
- AWS: P6e UltraServer Capacity Blocks, 72 x B200 at $761.904/hr and 36 x B200 at $380.952/hr, both $10.582 per accelerator, Dallas Local Zone only. https://aws.amazon.com/ec2/capacityblocks/pricing/ (checked 2026-10-22).
- Nebius, Crusoe, Together: contact sales. https://nebius.com/prices, https://www.crusoe.ai/cloud/pricing, https://www.together.ai/pricing (checked 2026-10-22).
- Minimum unit: 4 GPUs at CoreWeave, 36 at AWS. Not a card purchase.

### GB300 NVL72

- Oracle: BM.GPU.GB300.4 at $18.00 per GPU on demand, 4 GPUs, stock not verified. https://getdeploying.com/gpus/nvidia-gb300 (checked 2026-10-22). Oracle's own price page is JS-rendered and showed blank prices on my fetch, so the Oracle figure is as reported by getdeploying.
- Verda: 2x GB300 on demand $12.16, 24-month $9.12, 4x spot $6.08, all out of stock. https://getdeploying.com/gpus/nvidia-gb300 (checked 2026-10-22).
- CoreWeave, Nebius, Crusoe, Together, Gcore: contact sales. AWS u-p6e-gb300x72: reserved, custom. Azure ND GB300 v6 (Standard_ND128isr_GB300_v6): no self-serve price, quote only. https://www.coreweave.com/pricing, https://nebius.com/prices, https://www.crusoe.ai/cloud/pricing, https://getdeploying.com/gpus/nvidia-gb300, https://www.spheron.network/blog/azure-gb300-pricing-2026/ (checked 2026-10-22).
- getdeploying: 8 providers, 28 price points, no on-demand median because fewer than 3 providers list one. https://getdeploying.com/gpus/nvidia-gb300 (checked 2026-10-22).

### Vera Rubin NVL72 (VR200 / Rubin)

- CoreWeave announced Vera Rubin NVL72 availability at its Fully Connected conference; first customer Cognition began using it in early September 2026; Cognition claims up to 4.8x total token throughput on its SWE-2 workload versus GB200 NVL72 (vendor claim). No price or capacity figure. https://datacenterdynamics.com/en/news/coreweave-makes-nvidia-vera-rubin-nvl72-available-cognition-is-early-customer (checked 2026-10-22).
- Crusoe lists "NVIDIA Vera Rubin NVL72" as contact sales. https://www.crusoe.ai/cloud/pricing (checked 2026-10-22).
- SemiAnalysis models VR200 hyperscaler TCO at $3.61 per chip-hour, 60 percent above B300's $2.26. https://inferencex.semianalysis.com/compare/deepseek-r1-b200-vs-b300 (checked 2026-10-22).
- Verdict: not rentable by a small provider. No card path, no public price.

### RTX PRO 6000 Blackwell Server Edition (96 GB)

- Nebius on demand $1.80, preemptible from $0.79. https://nebius.com/prices (checked 2026-10-22).
- Koyeb $2.20/hr serverless. https://www.koyeb.com/pricing (checked 2026-10-22).
- RunPod $2.49/hr; MIG slices 48 GB $1.29 and 24 GB $0.69. https://www.runpod.io/pricing (checked 2026-10-22).
- CoreWeave High Memory 8x $20.00/hr on demand ($2.50 per GPU, estimate), spot $11.09/hr ($1.39 per GPU, estimate), inference-customer single-GPU rate $2.50. https://www.coreweave.com/pricing (checked 2026-10-22).
- Minimum unit 1 GPU almost everywhere; card accepted.

### AMD MI355X (288 GB)

- Vultr product page: "Starting at $2.650 / Per hour", 8-GPU plans, "Reserve now" and "Deploy now" buttons. https://www.vultr.com/products/cloud-gpu/amd-mi355x/ (checked 2026-10-22). getdeploying shows the Vultr 8x MI355X plan (vbm-256c-3072gb-8-mi355x-gpu) at $2.59 as spot and out of stock as of 2026-10-22T17:15Z. https://getdeploying.com/gpus/amd-mi355x (checked 2026-10-22). Your $2.59 figure is the older Vultr list price; the live page says $2.65.
- Daytona: 1x MI355X GPU-only on demand $5.99 in stock, spot $3.44, 8x on demand $8.04. https://getdeploying.com/gpus/amd-mi355x (checked 2026-10-22).
- DigitalOcean: MI355X spot $5.50/GPU/hr, 8-GPU droplet, self-serve with card. https://www.digitalocean.com/pricing/gpu-droplets (checked 2026-10-22).
- Oracle BM.GPU.MI355X.8 $8.60 per GPU, 8 GPUs. https://getdeploying.com/gpus/amd-mi355x (checked 2026-10-22).
- TensorWave: "Starting at $2.95/GPU HR", bare metal 8x, sales-led. https://tensorwave.com/products/accelerators/amd-mi355x (checked 2026-10-22).
- Crusoe: on demand contact sales; managed inference dedicated MI355X $7.40/GPU-hr. https://www.crusoe.ai/cloud/pricing (checked 2026-10-22).
- Hot Aisle: MI300X only ($2.99 VM, $3.39 bare metal); no MI355X on the price page. https://hotaisle.xyz/pricing/ (checked 2026-10-22).
- Minimum unit: 1 GPU at Daytona; 8 at Vultr, DigitalOcean, Oracle, TensorWave. Card: yes at Daytona, DigitalOcean, Vultr.

### AMD MI400 series (MI450 / MI455X, 432 GB HBM4)

- getdeploying tracks 5 providers (TensorWave, Vultr, Cirrascale, Azure, Oracle), all waitlist, all custom pricing, none published. Released Q3 2026 per the spec sheet; "shipments ramping from late 2026 into the first half of 2027". https://getdeploying.com/gpus/amd-mi455x (checked 2026-10-22).
- Vultr: "Vultr is currently taking pre-orders for reserved capacity from 2027 through 2028." Deployed as full 72-GPU Helios racks. https://www.vultr.com/products/cloud-gpu/amd-mi455x/ (checked 2026-10-22).
- Oracle announced in October 2025 that OCI would deploy 50,000 MI450 starting Q3 2026; no public per-GPU price found. https://datacentrenews.uk/story/oracle-to-launch-ai-supercluster-with-amd-mi450-gpus-in-2026 (checked 2026-10-22).
- Verdict: not rentable in 2026.

### Google TPU7x (Ironwood)

- Cloud TPU pricing page: Ironwood us-central1 on demand $12.00 per chip-hour, DWS flex-start $6.00, calendar mode $8.40, 1-year $8.40, 3-year $5.40; europe-west2 on demand $13.20. https://cloud.google.com/tpu/pricing (checked 2026-10-22).
- GA on 2026-03-31 per the Cloud TPU release notes. https://docs.cloud.google.com/tpu/docs/release-notes (checked 2026-10-22).
- Smallest slice is 2x2x1 = 4 chips, one tpu7x-standard-4t VM with 224 vCPU and 960 GB RAM; 192 GiB HBM per chip at about 7.37 TB/s. https://docs.cloud.google.com/tpu/docs/tpu7x (checked 2026-10-22).
- Card: GCP accepts cards, but TPU7x capacity needs a quota request. vLLM and SGLang run through JAX or TorchTPU backends, not CUDA.

## 3. Throughput: B300 versus B200

### Price ratio, B300 divided by B200, same provider

| Source | B300 | B200 | Ratio |
|---|---|---|---|
| Nebius on demand https://nebius.com/prices (checked 2026-10-22) | $9.50 | $8.50 | 1.12 |
| RunPod 1x secure https://www.runpod.io/pricing (checked 2026-10-22) | $8.99 | $7.99 | 1.13 |
| AWS Capacity Blocks per accelerator https://aws.amazon.com/ec2/capacityblocks/pricing/ (checked 2026-10-22) | $16.146 | $14.208 | 1.14 |
| SemiAnalysis hyperscaler-ownership TCO https://inferencex.semianalysis.com/chips/b300 (checked 2026-10-22) | $2.26 | $1.73 | 1.31 |
| SemiAnalysis retail rental tier https://inferencex.semianalysis.com/run/deepseek-r1-on-b300 and /run/deepseek-r1-on-b200 (checked 2026-10-22) | $4.25 | $3.70 | 1.15 |

I use 1.12 (Nebius, a card-rentable pair) as the primary ratio and 1.31 (TCO) as the pessimistic one.

### Output tokens per second per GPU, max-throughput benchmarks

TensorRT-LLM 1.2.1 perf overview. B300 and GB300 are marked beta. Unit is output tokens per second per GPU. https://nvidia.github.io/TensorRT-LLM/1.2.1/developer-guide/perf-overview.html (checked 2026-10-22).

| Model, ISL/OSL | B200 | B300 | B300/B200 | GB200 | GB300 |
|---|---|---|---|---|---|
| gpt-oss-120b 1024/1024 | 29,061 | 34,737 | 1.20 | 29,056 | 38,702 |
| gpt-oss-120b 8192/1024 | 6,938 | 8,361 | 1.21 | 7,874 | 9,407 |
| gpt-oss-120b 1024/8192 | 16,434 | 18,338 | 1.12 | 17,079 | 19,866 |
| DeepSeek R1 0528 1024/1024 (FP4, DEP4) | 5,757 | 6,046 | 1.05 | 4,989 | 4,981 |
| DeepSeek R1 8192/1024 | 1,176 | 1,489 | 1.27 | 1,276 | 1,599 |
| DeepSeek R1 1024/8192 | 4,228 | 6,235 | 1.47 | 4,474 | 6,842 |

MLPerf Inference v6.0 closed division, Nebius submissions, total tokens per second for 8 GPUs, server and offline. https://nebius.com/blog/posts/mlperf-inference-v6-0-results (checked 2026-10-22).

| Model, scenario | HGX B200 (8) | HGX B300 (8) | B300/B200 | GB300 NVL72 (8) |
|---|---|---|---|---|
| DeepSeek R1 server | 51,693 | 60,413 | 1.17 | 64,510 |
| DeepSeek R1 offline | 58,582 | 69,319 | 1.18 | 76,347 |
| gpt-oss-120b server | 87,444 | 100,437 | 1.15 | n/a |
| gpt-oss-120b offline | 85,921 | 106,885 | 1.24 | n/a |

NVIDIA's own MLPerf v6.0 post gives GB300 NVL72 at 8,064 tokens/s per GPU on DeepSeek R1 server and 9,821 offline, up from 2,907 and 5,842 in v5.1 on the same hardware. https://developer.nvidia.com/blog/nvidia-extreme-co-design-delivers-new-mlperf-inference-records/ (checked 2026-10-22).

### InferenceX (SemiAnalysis), measured at matched interactivity

gpt-oss-120b: B300 has no published run. B200 leads at 44,489 tokens/s per GPU at 50 tok/s per user, 8k/1k, FP4 vLLM; MI355X 38,497. https://inferencex.semianalysis.com/rankings/fastest-gpu-for-gptoss-120b and https://inferencex.semianalysis.com/run/gptoss-120b-on-b300 (checked 2026-10-22).

DeepSeek R1, 8k/1k, best engine at each point, tokens/s per GPU. https://inferencex.semianalysis.com/run/deepseek-r1-on-b200 and https://inferencex.semianalysis.com/run/deepseek-r1-on-b300 (checked 2026-10-22).

| Per-user target | B200 (SGLang fp4) | B300 (SGLang fp8) | B300/B200 |
|---|---|---|---|
| 30 tok/s | 6,799 | 2,166 | 0.32 |
| 50 tok/s | 4,610 | 1,845 | 0.40 |
| 100 tok/s | 2,685 | 1,286 | 0.48 |
| 200 tok/s | 1,598 | 690 | 0.43 |

Flag: this ladder compares B200 FP4 to B300 FP8. The InferenceX B200-vs-B300 compare page, filtered to FP4 8K/1K, shows B300 ahead at two of three interpolated points (3,887 vs 2,804; 1,016 vs 1,008; 649 vs 373 tokens/s per chip) and its summary line says "B300 delivers 1% more tok/s/chip than B200 on DeepSeek R1; B200 is 30% more cost-efficient." https://inferencex.semianalysis.com/compare/deepseek-r1-b200-vs-b300 (checked 2026-10-22). The per-dollar page at 1k/1k fp8 gives B200 $0.57 vs B300 $0.95 per million at 78 tok/s per user and $1.91 vs $2.29 at 143 tok/s. https://inferencex.semianalysis.com/compare-per-dollar/deepseek-r1-b200-vs-b300 (checked 2026-10-22). The B300 FP4 SGLang configuration is clearly not mature in the live data. Treat the 0.40 as a software snapshot, not a hardware ceiling.

Kimi K3 (AgentX agentic coding workload, 50 tok/s per user): B300 6,083 (vLLM fp4, single 8-GPU node); B200 6,505 (Dynamo vLLM fp4, multi-node, 16 GPUs); GB200 NVL72 8,488; MI355X 9,217. https://inferencex.semianalysis.com/rankings/fastest-gpu-for-kimi-k3 (checked 2026-10-22).

### Tokens per dollar versus B200 = 1.0 (estimate)

Formula: (B300 throughput / B200 throughput) divided by (B300 price / B200 price).

gpt-oss-120b:
- TRT-LLM 1k/1k: 1.20 / 1.12 = 1.07. At TCO ratio 1.31: 0.92.
- TRT-LLM 8k/1k: 1.21 / 1.12 = 1.08. At 1.31: 0.92.
- MLPerf server: 1.15 / 1.12 = 1.03. At 1.31: 0.88.
- MLPerf offline: 1.24 / 1.12 = 1.11. At 1.31: 0.95.
- Range: 0.9 to 1.1. Parity.

DeepSeek R1:
- TRT-LLM 1k/1k: 1.05 / 1.12 = 0.94. At 1.31: 0.80.
- TRT-LLM 8k/1k: 1.27 / 1.12 = 1.13. At 1.31: 0.97.
- TRT-LLM 1k/8k: 1.47 / 1.12 = 1.31. At 1.31: 1.12.
- MLPerf server: 1.17 / 1.12 = 1.04. At 1.31: 0.89.
- MLPerf offline: 1.18 / 1.12 = 1.05. At 1.31: 0.90.
- InferenceX compare page FP4 points: 1.39 / 1.12 = 1.24; 1.01 / 1.12 = 0.90; 1.74 / 1.12 = 1.55.
- InferenceX ranking at 50 tok/s per user: 0.40 / 1.12 = 0.36 (flagged above).
- Range excluding the flagged point: 0.8 to 1.3. Long-output and long-context shapes favor B300; short chat shapes do not.

Kimi K3: B300 6,083 vs B200 6,505 gives 0.935 / 1.12 = 0.83 tokens per dollar, but the B200 number needs two 8-GPU nodes with Dynamo. The practical point is that B300 is the smallest single node that runs Kimi K3.

Other accelerators versus B200 (estimate, InferenceX or TRT-LLM throughput, cheapest card-rentable B200 price $6.69 Lambda or same-provider pairs):
- GB200 NVL72: gpt-oss-120b TRT-LLM 1k/1k 29,056 vs 29,061 = 1.00; CoreWeave $10.50 vs CoreWeave B200 $8.60 = 1.22; tokens per dollar 0.82. DeepSeek R1 at 50 tok/s: 2,697 vs 4,610 = 0.585; / 1.22 = 0.48. Kimi K3: 8,488 vs 6,505 = 1.30; / 1.22 = 1.07.
- GB300 NVL72: gpt-oss-120b TRT-LLM 1k/1k 38,702 vs 29,061 = 1.33; Oracle $18.00 vs CoreWeave B200 $8.60 = 2.09; tokens per dollar 0.64. DeepSeek R1 at 50 tok/s: 2,438 vs 4,610 = 0.53; / 2.09 = 0.25. MLPerf server 8-GPU: 64,510 vs 51,693 = 1.25; / 2.09 = 0.60.
- MI355X: gpt-oss-120b InferenceX 38,497 vs 44,489 = 0.865. Price ratio 0.31 (Vultr $2.65 vs Nebius B200 $8.50) to 0.90 (Daytona $5.99 vs Lambda $6.69). Tokens per dollar 2.8 to 1.0. DeepSeek R1 at 50 tok/s: 1,608 vs 4,610 = 0.35; tokens per dollar 1.1 to 0.4. Kimi K3: 9,217 vs 6,505 = 1.42; tokens per dollar 4.5 to 1.6.
- RTX PRO 6000: no matched gpt-oss-120b run. Proxy from TRT-LLM Llama 3.3 70B 1k/1k: RTX 6000 Pro single GPU 1,724 vs B200 6,943 = 0.25; Nebius $1.80 vs $8.50 = 0.21; tokens per dollar 1.17. https://nvidia.github.io/TensorRT-LLM/1.2.1/developer-guide/perf-overview.html and https://nebius.com/prices (checked 2026-10-22). A vendor test of gpt-oss-120b on one RTX PRO 6000 with vLLM at 50 concurrent prompts, 100 in and 600 out, reports about 1,780 tokens/s aggregate; not comparable to InferenceX's matched-interactivity figures. https://www.databasemart.com/blog/vllm-gpu-benchmark-pro6000 (checked 2026-10-22, figure from the page summary; the table was truncated in my fetch).
- TPU7x: no public per-chip gpt-oss or DeepSeek run found. List price $12.00 is 1.41x Nebius B200. n/a.

## 4. Kimi K3 economics

### Model facts

Kimi K3: 2.8T total parameters, 104B active, 16 of 896 experts, MXFP4 weights with MXFP8 activations from quantization-aware training, 1,048,576-token context, released 2026-07-16 with open weights by 2026-07-27. https://huggingface.co/moonshotai/Kimi-K3 (checked 2026-10-22). Weights are about 1.5 TB; AMD's recipe says "at ~1.5 TB a per-node copy is usually not an option." https://rocm.docs.amd.com/projects/infera/en/latest/_sources/recipes/kimi-k3.md (checked 2026-10-22). getdeploying's model-fit estimate is 1,544 GB at 4-bit including FP8 KV cache at 32K context. https://getdeploying.com/gpus/amd-mi355x (checked 2026-10-22). Your 1,561 GB figure is consistent.

Reference recipes and node counts:
- vLLM: "The easiest way to run Kimi K3 is to use 8 NVIDIA B300 GPUs or 8 AMD MI355X GPUs." The recipe page lists hardware "at least 8x GB300" for NVIDIA with multi-node for production, and "at least 8x MI355X/MI350X" for ROCm, with TP8, TEP16, TP8xPP2 and disaggregated profiles. https://vllm.ai/blog/2026-07-27-k3 and https://recipes.vllm.ai/moonshotai/Kimi-K3 (checked 2026-10-22).
- SGLang cookbook node counts: B300 1x8, GB300 2x4, MI350X/MI355X 1x8, B200 2x8, GB200 4x4, H200 2x8, H100 4x8. B300 1x8 Unified Low-Latency and Balanced cells are "Verified"; the MI35x TP8/DCP8 recipe is "Final Verification In Progress". https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3 (checked 2026-10-22).
- Speculative decoding: vLLM reports 118 tok/s per user without and 370 tok/s with DSpark on 16 GB300 NVL72 GPUs, single user. https://vllm.ai/blog/2026-07-27-k3 (checked 2026-10-22).

### Measured output tokens per second per GPU at high concurrency

InferenceX, AgentX agentic coding workload, vLLM FP4, tokens/s per GPU. https://inferencex.semianalysis.com/run/kimi-k3-on-b300, https://inferencex.semianalysis.com/run/kimi-k3-on-mi355x, https://inferencex.semianalysis.com/run/kimi-k3-on-b200, https://inferencex.semianalysis.com/run/kimi-k3-on-gb200-nvl72 (checked 2026-10-22).

| Per-user target | 8x B300 (TP8, single node) | 8x MI355X (single node) | B200 (16 GPUs) | GB200 NVL72 |
|---|---|---|---|---|
| 30 tok/s | 7,855 | 14,141 | 9,324 | 10,638 |
| 50 tok/s | 6,083 | 9,217 | 6,505 | 8,488 |
| 75 tok/s | 4,650 | 6,569 | 3,830 | 6,543 |
| 100 tok/s | 4,051 | 4,526 | 2,958 | 4,288 |
| 150 tok/s | 2,075 | 2,224 | 1,663 | 2,183 |
| Peak measured, any config | 12,566 | 17,482 | 10,585 | 10,950 |
| InferenceX $/M tokens at retail rental tier, 50 tok/s | $0.19 at $4.25/hr | $0.087 at $2.90/hr | $0.16 at $3.70/hr | $0.13 at $4.00/hr |

Note on units: InferenceX labels these "tokens/s per GPU" and prices them as "$ per million total tokens"; the TRT-LLM and MLPerf per-GPU numbers above are explicitly output tokens. I treat the InferenceX figure as output tokens for the revenue math below. If it is total tokens on the AgentX trace, output revenue is lower than shown, but input and cache-read revenue (not counted below) would offset part of it.

Low-concurrency, long-context reality check: GPUStack ran 8x B300 with vLLM and the DSpark draft at 64K input, 3K output, concurrency 10, and saw about 501 tok/s aggregate stable decode (about 63 tok/s per GPU, estimate); at 200K input vLLM fell to about 163 tok/s and SGLang with DCP=8 held about 268 tok/s. https://dev.to/gpustack/gpustack-day-0-support-for-kimi-k3-vllm-vs-sglang-inference-benchmark-on-8xb300-gpus-2g0g (checked 2026-10-22).

### OpenRouter Kimi K3 prices (checked 2026-10-22)

- Model page headline: $0.238 in / $16.00 out per million; 28 endpoints. https://openrouter.ai/moonshotai/kimi-k3/pricing (checked 2026-10-22).
- Endpoint API lists 28 endpoints from 20 distinct providers: Wafer, InferenceNet, Relace, Makora, Morph, Sail Research, AkashML, Decart, Chutes, Fireworks, Phala, DigitalOcean, DeepInfra, Amazon Bedrock, Parasail, Modal, Together, BaseTen, Moonshot AI, Alibaba. https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints (checked 2026-10-22).
- Cheapest input: Wafer $0.238. Cheapest output: Sail Research $5.50 at $1.20 input. Your "floor" of $0.239 in / $5.50 out combines two different providers. Moonshot first-party: $3.00 / $15.00.
- My snapshot medians across the 28 endpoints (estimate): $2.17 in, $14.38 out. Your $2.325 / $14.125 is a slightly older snapshot. I use your floor and median figures below as instructed.
- Self-host or proxy: 14 of 20 providers declare a quantization (mxfp4, fp4 or fp8), which means they run the weights themselves: Wafer, InferenceNet, Relace, Makora, Morph, Sail Research, AkashML, Decart, Chutes, DeepInfra, Parasail, Modal, BaseTen, Moonshot AI. The 6 with "unknown" quantization (Fireworks, Phala, DigitalOcean, Amazon Bedrock, Together, Alibaba) are all infrastructure operators with their own fleets and distinct prices, latencies and throughputs, so I infer they also self-host (inference, not confirmed). I found no evidence of a pure Moonshot proxy among the 20. The license treats "mere relaying of requests to models hosted by others" as outside Model-as-a-Service anyway.

### Revenue per GPU-hour and breakeven utilization (estimate)

Assumptions: output tokens only (input and cache-read revenue ignored, which is conservative); 100 percent utilization at the InferenceX operating point; node price as given. Revenue per GPU-hour = tokens/s per GPU x 3,600 / 1e6 x price per million.

B300 node at $7.94 per GPU-hour (DigitalOcean 12-month, https://www.digitalocean.com/pricing/gpu-droplets, checked 2026-10-22):
- 50 tok/s per user: 6,083 x 3,600 = 21.9M output tokens per GPU-hour.
  - Floor $5.50/M: 21.9 x 5.50 = $120.4 revenue per GPU-hour. Breakeven utilization = 7.94 / 120.4 = 6.6 percent.
  - Median $14.125/M: 21.9 x 14.125 = $309.3. Breakeven = 7.94 / 309.3 = 2.6 percent.
  - Cost per million output tokens at 100 percent utilization: 7.94 / 21.9 = $0.36.
- 100 tok/s per user: 4,051 x 3,600 = 14.6M tokens per GPU-hour.
  - Floor: $80.2; breakeven 9.9 percent. Median: $206.0; breakeven 3.9 percent. Cost per million: $0.54.
- Whole 8-GPU node at 50 tok/s: cost $63.52/hr; revenue $963/hr at floor, $2,474/hr at median.
- At Nebius on demand $9.50 instead: breakeven 7.9 percent at floor, 3.1 percent at median.
- Low-concurrency long-context case (GPUStack, 63 tok/s per GPU): 0.227M tokens per GPU-hour; floor $1.25/hr, median $3.20/hr; both below the $7.94 cost. Breakeven is impossible at floor and 248 percent at median. Concurrency is the whole business.

MI355X node at $2.59 per GPU-hour (your Vultr figure; live Vultr page says $2.65, https://www.vultr.com/products/cloud-gpu/amd-mi355x/, checked 2026-10-22):
- 50 tok/s per user: 9,217 x 3,600 = 33.2M output tokens per GPU-hour.
  - Floor $5.50/M: 33.2 x 5.50 = $182.5. Breakeven = 2.59 / 182.5 = 1.4 percent (1.45 percent at $2.65).
  - Median $14.125/M: 33.2 x 14.125 = $468.7. Breakeven = 2.59 / 468.7 = 0.55 percent.
  - Cost per million output tokens: 2.59 / 33.2 = $0.078.
- 100 tok/s per user: 4,526 x 3,600 = 16.3M tokens per GPU-hour. Floor $89.6, breakeven 2.9 percent. Median $230.1, breakeven 1.1 percent. Cost per million $0.16.
- Whole 8-GPU node at 50 tok/s: cost $20.72/hr; revenue $1,460/hr at floor, $3,750/hr at median.
- At Daytona on demand $5.99 (the only verified in-stock 1x price): breakeven 3.3 percent at floor, 1.3 percent at median.

| Node | $/GPU-hr | Tok/s per GPU (50 tok/s per user) | M output tokens per GPU-hr | Revenue per GPU-hr at floor $5.50 | Revenue at median $14.125 | Breakeven util at floor | Breakeven util at median | Cost per M output tokens |
|---|---|---|---|---|---|---|---|---|
| 8x B300, DigitalOcean 12-mo | $7.94 | 6,083 | 21.9 | $120 | $309 | 6.6 percent | 2.6 percent | $0.36 |
| 8x B300, Nebius on demand | $9.50 | 6,083 | 21.9 | $120 | $309 | 7.9 percent | 3.1 percent | $0.43 |
| 8x B300, 100 tok/s per user | $7.94 | 4,051 | 14.6 | $80 | $206 | 9.9 percent | 3.9 percent | $0.54 |
| 8x B300, 64K ctx, concurrency 10 (GPUStack) | $7.94 | 63 | 0.23 | $1.25 | $3.20 | never | 248 percent | $35 |
| 8x MI355X, Vultr | $2.59 | 9,217 | 33.2 | $183 | $469 | 1.4 percent | 0.55 percent | $0.078 |
| 8x MI355X, Daytona on demand | $5.99 | 9,217 | 33.2 | $183 | $469 | 3.3 percent | 1.3 percent | $0.18 |
| 8x MI355X, 100 tok/s per user | $2.59 | 4,526 | 16.3 | $90 | $230 | 2.9 percent | 1.1 percent | $0.16 |

All rows are estimates. Reading: the gap between serving cost ($0.08 to $0.54 per million output tokens at full load) and the market's lowest output price ($5.50) is 10x to 70x. That is why 20 hosts are on OpenRouter. The risk is not margin per token. It is filling the node: a small provider on OpenRouter with no brand gets routed traffic only when it is cheapest or fastest, and the output-price floor has already fallen from $15 (Moonshot list) to $5.50 (Sail Research) in three months.

### License

Kimi K3 License, full text. https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE (checked 2026-10-22).
- Grant: use, copy, modify, distribute, sublicense, sell, deploy, fine-tune, without restriction, subject to the conditions below.
- Clause 2 (Model as a Service): if the licensee or its affiliates operate a MaaS business and aggregate revenue exceeds $20 million in total over any consecutive 12 months, they must enter a separate agreement with Moonshot before commercial use. MaaS means giving third parties API-style access with meaningful control over inputs, parameters or training data. It excludes end-user products with embedded model features and "mere relaying of requests to models hosted by others."
- Clause 3 (branding): products with more than 100 million monthly active users or more than $20 million in monthly revenue must display "Kimi K3" prominently in the UI.
- Clause 4 (exemptions): internal use, and access through Moonshot's official products or certified inference partners.
- For a small provider: no fee, no attribution, no agreement until MaaS revenue crosses $20 million in 12 months. Note the clause reads "aggregate revenue of the Licensee and its affiliates", which a conservative reading applies to the whole company, not only Kimi K3 revenue.

## 5. What "newer" buys, one line each

Memory per GPU and per 8-GPU node:
- B200 180 GB, node 1,440 GB. https://www.coreweave.com/pricing (checked 2026-10-22).
- B300 288 GB, 268 GB usable per InferenceX, node 2,304 GB (2,144 GB usable). https://inferencex.semianalysis.com/chips/b300 (checked 2026-10-22).
- MI355X 288 GB HBM3e, 8 TB/s, node 2,304 GB. https://www.vultr.com/products/cloud-gpu/amd-mi355x/ (checked 2026-10-22).
- GB300 288 GB per GPU, 18 nodes of 4 per rack. https://getdeploying.com/gpus/nvidia-gb300 (checked 2026-10-22).
- MI455X 432 GB HBM4, 23.3 TB/s, 31 TB per 72-GPU Helios rack. https://www.vultr.com/products/cloud-gpu/amd-mi455x/ (checked 2026-10-22).
- RTX PRO 6000 96 GB GDDR7, node 768 GB. https://www.coreweave.com/pricing (checked 2026-10-22).
- TPU7x 192 GiB HBM per chip, 7.37 TB/s, 4 chips per VM. https://docs.cloud.google.com/tpu/docs/tpu7x (checked 2026-10-22).

FP4 dense compute:
- B300 13,500 TFLOPS dense FP4, a 1.5x uplift over B200 while FP8 and BF16 stay at B200 levels (so B200 is about 9,000 TFLOPS FP4, estimate). https://inferencex.semianalysis.com/chips/b300 (checked 2026-10-22).
- GB300 15,000 TFLOPS FP4 dense per getdeploying's datasheet summary. https://getdeploying.com/gpus/nvidia-gb300 (checked 2026-10-22).
- MI355X 10,066 TFLOPS MXFP4 (80.5 PFLOPS per 8-GPU platform). https://www.vultr.com/products/cloud-gpu/amd-mi355x/ (checked 2026-10-22).
- MI455X listed at 40,265 TFLOPS FP4 by getdeploying (likely a sparsity figure; not verified against AMD). https://getdeploying.com/gpus/amd-mi455x (checked 2026-10-22).
- Why it matters less than it sounds: on gpt-oss-120b and DeepSeek R1 the 1.5x FP4 uplift turns into 5 to 25 percent more tokens at max throughput, because decode is memory-bound and B300 has the same 8 TB/s bandwidth as B200 (section 3).

Which big open models fit one 8-GPU node (weights only; add KV cache; all estimates unless a recipe confirms):
- Kimi K3, MXFP4, about 1.5 TB (your 1,561 GB): fits 8x B300 and 8x MI355X (both are the 1x8 reference recipes in vLLM and SGLang); does not fit 8x B200 (SGLang recipe is 2x8); MI455X would need 4 GPUs per getdeploying's estimate. https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3 and https://getdeploying.com/gpus/amd-mi455x (checked 2026-10-22).
- Qwen3.8-2.4T-A95B: 2.4T total, 95B active, open weights under a custom "qwen3.8-max" license. https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B (checked 2026-10-22). At FP8 that is about 2.4 TB, which does not fit any 8-GPU node here (estimate). A 4-bit build of about 1.2 TB (secondary source) would fit 8x B300 or 8x MI355X but not 8x B200. https://techsy.io/en/blog/qwen-3-8 (checked 2026-10-22, secondary).
- GLM 5.3: about 753B total, 39 to 40B active; FP8 about 744 GB (your 756 GB). Fits 8x B200 (1,440 GB) with about 680 GB left for KV, and all 288 GB nodes. https://www.yottalabs.ai/post/glm-5-3-hardware-requirements-gpu-memory-2026 (checked 2026-10-22, secondary).
- Hy4 (Tencent, preview): 770B total, 49B active, Apache 2.0, FP8 variant published; one review cites an MXFP8 build of about 924 GB and Tencent's minimum of 16x B200 or 8x B300 for weights plus KV at full context. Your 814 GB FP8 figure fits 8x B200 on weights alone with about 626 GB headroom; 8x B300 is the comfortable fit. https://www.eesel.ai/blog/tencent-hy4-review (checked 2026-10-22, secondary).
- DeepSeek V4.1 Flash: 552B total, 16B active; FP8 about 554 GB including 32K KV per getdeploying (your 510 GB). Fits every node here including 8x RTX PRO 6000 (768 GB), tightly. https://getdeploying.com/gpus/amd-mi355x (checked 2026-10-22).
- gpt-oss-120b: 67 GB at 4-bit. Fits one GPU on anything in this note. https://getdeploying.com/gpus/nvidia-gb300 (checked 2026-10-22).

## 6. Caveats

- Aggregator prices (getdeploying, computeprices) are scraped and can lag a provider's own page by hours. Where I had the provider page I cited it.
- InferenceX re-runs continuously; the B300 DeepSeek R1 FP4 SGLang lane was clearly behind the B200 lane on 2026-10-22, and the Kimi K3 B300 run is dated 2026-08-16 versus MI355X 2026-10-19. Expect B300 numbers to move up.
- TensorRT-LLM B300 and GB300 numbers are marked beta by NVIDIA.
- The breakeven math ignores input-token revenue, cache-read revenue, egress, storage, idle reload time and the fact that OpenRouter routes by price and speed. It also assumes you can sustain the InferenceX concurrency, which the GPUStack row shows is not a given at long context.
- Oracle's price page did not render prices in my fetch; Oracle GB300 and MI355X figures come from getdeploying's scrape of it.
- I did not log in anywhere or submit any form.

## Source list

- https://www.digitalocean.com/pricing/gpu-droplets
- https://nebius.com/prices
- https://lambda.ai/pricing
- https://www.coreweave.com/pricing
- https://www.runpod.io/pricing
- https://www.crusoe.ai/cloud/pricing
- https://www.together.ai/pricing
- https://www.koyeb.com/pricing
- https://hotaisle.xyz/pricing/
- https://tensorwave.com/products/accelerators/amd-mi355x
- https://www.vultr.com/products/cloud-gpu/amd-mi355x/
- https://www.vultr.com/products/cloud-gpu/amd-mi455x/
- https://aws.amazon.com/ec2/capacityblocks/pricing/
- https://aws-pricing.com/p6-b300.48xlarge.html
- https://cloud.google.com/tpu/pricing
- https://docs.cloud.google.com/tpu/docs/tpu7x
- https://docs.cloud.google.com/tpu/docs/release-notes
- https://getdeploying.com/gpus/nvidia-b300
- https://getdeploying.com/gpus/nvidia-gb300
- https://getdeploying.com/gpus/amd-mi355x
- https://getdeploying.com/gpus/amd-mi455x
- https://computeprices.com/providers/vast/gpus/hgx-b300
- https://www.spheron.network/blog/azure-gb300-pricing-2026/
- https://datacenterdynamics.com/en/news/coreweave-makes-nvidia-vera-rubin-nvl72-available-cognition-is-early-customer
- https://datacentrenews.uk/story/oracle-to-launch-ai-supercluster-with-amd-mi450-gpus-in-2026
- https://nvidia.github.io/TensorRT-LLM/1.2.1/developer-guide/perf-overview.html
- https://nebius.com/blog/posts/mlperf-inference-v6-0-results
- https://developer.nvidia.com/blog/nvidia-extreme-co-design-delivers-new-mlperf-inference-records/
- https://inferencex.semianalysis.com/compare/deepseek-r1-b200-vs-b300
- https://inferencex.semianalysis.com/compare-per-dollar/deepseek-r1-b200-vs-b300
- https://inferencex.semianalysis.com/rankings/fastest-gpu-for-gptoss-120b
- https://inferencex.semianalysis.com/rankings/fastest-gpu-for-deepseek-r1
- https://inferencex.semianalysis.com/rankings/fastest-gpu-for-kimi-k3
- https://inferencex.semianalysis.com/run/kimi-k3-on-b300
- https://inferencex.semianalysis.com/run/kimi-k3-on-mi355x
- https://inferencex.semianalysis.com/run/kimi-k3-on-b200
- https://inferencex.semianalysis.com/run/kimi-k3-on-gb200-nvl72
- https://inferencex.semianalysis.com/run/deepseek-r1-on-b200
- https://inferencex.semianalysis.com/run/deepseek-r1-on-b300
- https://inferencex.semianalysis.com/run/deepseek-r1-on-gb300-nvl72
- https://inferencex.semianalysis.com/run/gptoss-120b-on-mi355x
- https://inferencex.semianalysis.com/run/gptoss-120b-on-b300
- https://inferencex.semianalysis.com/chips/b300
- https://inferencex.semianalysis.com/model/kimi-k3
- https://dev.to/gpustack/gpustack-day-0-support-for-kimi-k3-vllm-vs-sglang-inference-benchmark-on-8xb300-gpus-2g0g
- https://vllm.ai/blog/2026-07-27-k3
- https://recipes.vllm.ai/moonshotai/Kimi-K3
- https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3
- https://rocm.docs.amd.com/projects/infera/en/latest/_sources/recipes/kimi-k3.md
- https://huggingface.co/moonshotai/Kimi-K3
- https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE
- https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
- https://openrouter.ai/moonshotai/kimi-k3/pricing
- https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints
- https://www.yottalabs.ai/post/glm-5-3-hardware-requirements-gpu-memory-2026
- https://www.eesel.ai/blog/tencent-hy4-review
- https://techsy.io/en/blog/qwen-3-8
- https://www.databasemart.com/blog/vllm-gpu-benchmark-pro6000
