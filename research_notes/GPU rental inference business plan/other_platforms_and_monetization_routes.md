# Other platforms and monetization routes for a solo US GPU/inference operator (beyond OpenRouter, HF Inference Providers, Vast.ai)

All numbers below were read live on 2026-10-22 unless a row says otherwise. "checked 2026-10-22" marks a live read. "estimate" marks my own arithmetic or judgment. "not found" means I looked and found nothing. Crypto-paid options are flagged "CRYPTO". The WebSearch budget ran out near the end, so a few items are listed as gaps rather than guesses.

## Key question 1: What channels exist in each category (A through F), and what are their terms?

### Takeaway
Only a handful of channels are self-serve, pay in USD or a stablecoin, and accept a small operator: Lium (95% revenue share, USDT payout option), Salad (consumer GPUs, PayPal cash-out, tiny per-GPU rates), Sogni (crypto), Chutes mining (crypto, explicitly allows rented bare metal), and cheaperinference.com (resells cloud API quota, not GPUs). Everything else is either sales-gated at datacenter scale (Lepton, Shadeform, Hydra Host, Hyperbolic, Parasail), credit-only (SF Compute resale, most referral programs), or token-paid with no reliable USD earnings data.

### Cited Findings

#### A. Legitimate compute resale and capacity markets

| Option | What it is / who pays whom | How to join | Requirements | Payment | Fees / rev share | Earnings or traffic evidence | Time to first dollar | Rented-cloud compatible? |
|---|---|---|---|---|---|---|---|---|
| SF Compute (resale on orderbook) | Customers who bought reserved time on SF Compute resell unused time to other SF Compute buyers; buyer pays SF Compute, seller gets credits | Self-serve via `sf` CLI; "Reselling" is a public-preview feature | "You need compute time that you own and access to the sf CLI"; sell from a pool/SKU you already bought | Platform credits, not cash: "SF Compute subtracts the fee from your sale value and adds the remaining amount to your credits" | Two-part fee: "Fee per node-hour × node-hours sold" plus "Fee percentage × sale value"; "SF Compute sets both fee parts, and your fees can change. Fees can also differ between organizations"; exact rates not published (not found) | Sep 9, 2026 post: on-platform customers get "average 25% realized discount" via resale; example $4.50/GPU-hr purchase realized at $3.375/GPU-hr (checked 2026-10-22) | Only after you buy compute; credits arrive on fill | N/A; it only resells SF Compute's own time. Pricing page redirects to a login wall (checked 2026-10-22) |
| SF Compute (hardware supply side) | Datacenter operators supply clusters to SFC under negotiated contracts | Sales only; job posts for "Compute Partnerships Manager" and "Account Manager, Compute Providers" | Long-term supply agreements, uptime KPIs, SLAs | not found | not found | not found | not found | No public supplier page (not found) |
| cheaperinference.com (Keak AI, Inc.) | Keak routes customer requests through a seller's cloud API account using the seller's API key; Keak pays the seller per routed request | Web form: "Tell us where you have available capacity and its approximate dollar value. Our team will review the fit and contact you directly." Fields: Email, Provider (dropdown), "Available capacity in USD" | Seller must be a company ("the company named at acceptance"); "Cloud Provider" means "the company that provides a Seller Account, for example Amazon Web Services, Microsoft, Google or Venice"; Seller gives Keak a "Credential" (API key) | Earnings "shown for each Routed Request, at the rate in effect when the request was sent"; paid "by the method and on the schedule that your seller dashboard shows" (currency not stated; buyer side uses Stripe, wallet from $5) | Rates set per request in dashboard; buyer sees discounts of 33% to 50% off list (e.g., deepseek-v4.1-flash $0.15 to $0.08 per M input) (checked 2026-10-22) | 360 models in catalog; no seller traffic data (not found) | Sales review first; no SLA on timing | Yes by design, but the seller carries the risk: "YOU ARE SOLELY RESPONSIBLE FOR COMPLIANCE WITH YOUR CLOUD TERMS. KEAK HAS NOT REVIEWED YOUR CLOUD TERMS" and "A CLOUD PROVIDER CAN ... SUSPEND OR CLOSE YOUR SELLER ACCOUNT" |
| Shadeform (supply side) | Asset-light broker reselling 23 to 30+ clouds | No public supplier page; /providers returns 404 (checked 2026-10-22). Supply is sourced by a "Sourcing Manager" who vets "GPU and data center operators" | Datacenter or bare-metal operator | not found | not found | SemiAnalysis: "offered GPUs from 23 providers", rated ClusterMAX Bronze | not found | Not applicable to a renter |
| Prime Intellect (compute supply) | B2B marketplace aggregating clouds; "generates revenue by taking a margin on GPU rentals" | No public program. 2024 blog listed "Allow users to contribute their GPUs directly" as an upcoming feature; 2026 hiring "Head of Compute" and partnerships leads | not found | not found | not found | 2024: "integrated 12 clouds"; H100 from $1.65/hr then | not found | not found |
| NVIDIA DGX Cloud Lepton | Marketplace where "NVIDIA Cloud Partners (NCPs), GPU marketplaces, cloud providers" list capacity | Partner early-access application; no public criteria. Docs expose "Bring Your Own Compute" for a workspace to attach its own nodes (consumption, not selling) | Named providers: CoreWeave, Lambda, Yotta, AWS, Azure, Nebius, Nscale, Firebird, Fluidstack, Hydra Host, Scaleway, Together, GMI | not found | not found | not found | not found | No; NCP-scale only |
| Compute Exchange | Auction marketplace launched Jan 28, 2025; claimed "$1 billion in compute supply" by Apr 2, 2025 and "80k GPUs" | computeexchange.com renders as a parked/placeholder page (checked 2026-10-22); no 2026 news found | not found | not found | not found | Self-reported press only | not found | Unknown |
| Hydra Host (Brokkr partner program) | Partners resell or supply bare-metal GPU capacity; "competitive revenue-sharing models" | Apply on site; "we'll respond within one business day" | Partner types: "resellers and neoclouds", "data center operators", "AI platforms", "Managed Service Provider", OEMs/VARs | not found (revenue share) | not found | Bitzero pilot: 64 B300 GPUs leased via Brokkr (Jan 2026); Hydra joined Lepton as NCP (Jun 11, 2025) | Sales cycle; not found | Not stated |
| Lium (Bittensor SN51; CRYPTO-adjacent with USDT option) | GPU rental marketplace; renters pay USD/hr; provider keeps 95% | Self-serve "Path A": sign up with Google or email, "No fee and nothing to buy"; install Sysbox, run one command; "listed for rent about 5 minutes after" | Supported NVIDIA list spans H100/H200/B200/B300, L40S, RTX PRO 6000, and consumer RTX 30/40/50 series; 100 Mbit/s download; disk at least 1.5x GPU memory; Sysbox on host | "95% of every rental payment"; "Paid daily to your coldkey in alpha, or in USDT if you choose a stablecoin payout"; Path A: "Earnings are paid in USDT once you add a payout address" | 5% platform fee on rentals; idle pay comes from subnet emission in alpha | Aggregator listed an H100 80GB at $1.39/GPU-hr on Lium; marketplace reported 1,329 GPUs across 470 nodes as of Sep 11, 2026 | Rental fees paid daily with a 2-day delay (estimate: first USDT within about a week if rented) | Not explicitly stated; needs root/Sysbox on the host, so a bare-metal or VM rental could work, a RunPod-style pod cannot (inference) |
| Hyperbolic (supply) | Aggregates capacity "from third-party data centers and operators" and resells; launched Forge (Jun 2026) for provisioning | No self-serve page found; job posts for "Supply Specialist" and "Head of Supply" negotiate "reserved capacity, and SLAs" | NeoCloud/datacenter scale | not found | not found | not found | not found | not found |
| Novita AI (supply) | GPU cloud and inference | No supplier program found | not found | not found | not found | not found | not found | not found |
| Parasail (capacity partners) | Inference/deployment network sourcing from "HydraHost, Shadeform, and Voltage Park" (job post) | No partner program page found | Neocloud scale | not found | not found | 2025: H200/H100/A100/4090 at $0.65 to $3.25/hr (dated) | not found | not found |
| Massed Compute | Own-infrastructure GPU cloud; supplies Shadeform | No reseller program found | not found | not found | not found | not found | not found | not found |
| Thunder Compute | GPU cloud; referral only (see E) | n/a | n/a | credits | 3% | n/a | n/a | n/a |
| Exabits | Compute base layer; "contributed over 65,000 GPUs" (2024 claim) | No provider page found | not found | not found | not found | $10M ARR claim (Dec 2024, press); no 2025-2026 updates | not found | not found |
| Fluence (CRYPTO-adjacent) | Hosts "earn USDC / FLT when renters use it"; GPU onboarding on Q3 2025 roadmap | Provider sign-up form (not read) | Datacenter partners named: Spheron, Kabat, Piknik | USDC plus FLT token | Third-party estimate: provider keeps roughly 80% (unofficial) | CPU marketplace "over $1 million in ARR" (company claim) | not found | not found |
| Hivenet | Consumer/contributor compute; "first certified GPU supplier" blog | not found | not found | not found | not found | not found | not found | not found |
| Foundry (mlfoundry), GPUdeploy, Cloud-GPUs, Lambda/CoreWeave/Nebius/Crusoe/Voltage Park partner tracks, Together "GPU partner", Nebius Token Factory partners, Azure/AWS bring-your-own-capacity | not researched or not found (search budget exhausted) | | | | | | | |

Sources for section A: [SF Compute reselling guide](https://docs.sfcompute.com/preview/guides/reselling-introduction); [SF Compute roadmap (public preview)](https://docs.sfcompute.com/preview/roadmap); [SF Compute realized discount post](https://sfcompute.com/news/realized-discount); [SFC Compute Partnerships Manager posting](https://jobs.electriccapital.com/companies/san-francisco-compute-company-2/jobs/59319875-compute-partnerships-manager); [cheaperinference.com home](https://cheaperinference.com); [Cheaper Inference Seller Agreement](https://platform.cheaperinference.com/legal/seller-agreement); [Cheaper Inference Terms](https://platform.cheaperinference.com/legal/terms); [Shadeform sourcing job](https://dailyremote.com/remote-job/sourcing-manager-sourcing-associate-5394704); [SemiAnalysis ClusterMAX on Shadeform](https://clustermax.semianalysis.com/cloudreview/shadeform); [Prime Intellect compute blog](https://primeintellect.ai/blog/compute); [Sacra on Prime Intellect](https://sacra.com/research/prime-intellect); [NVIDIA Lepton page](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/); [Lepton docs intro](https://docs.nvidia.com/dgx-cloud/lepton/get-started/index.html); [Constellation on Lepton partners](https://www.constellationr.com/index%2Ephp/insights/news/nvidia-adds-aws-microsoft-azure-dgx-cloud-lepton-marketplace); [Compute Exchange launch PR](https://www.businesswire.com/news/home/20250128536805/en/Compute-Exchange-Launches-to-Transform-How-AI-Compute-is-Bought-and-Sold); [Compute Exchange $1B PR](https://www.businesswire.com/news/home/20250402039147/en/Compute-Exchange-Auction-Model-Broadens-AI-Compute-Access-With-%241B-Supply); [Hydra Host partners](https://hydrahost.com/partners/); [Hydra Host Lepton post](https://hydrahost.com/post/hydra-host-named-nvidia-dgx-cloud-partner/); [Bitzero/Hydra B300 pilot](https://www.nasdaq.com/press-release/bitzero-holdings-inc-acquires-nvidia-blackwell-b300-gpu-servers-launch-ai-compute); [Lium rewards](https://docs.lium.io/providers/rewards); [Lium rental fees](https://docs.lium.io/providers/rewards/rental-fees); [Lium quickstart](https://docs.lium.io/providers/quickstart); [Lium architecture / supported GPUs](https://docs.lium.io/providers/architecture); [Lium H100 price on aggregator](https://getdeploying.com/lium); [Lium scale (Sep 2026)](https://pctechmag.com/?p=97853); [Hyperbolic Forge](https://principalvc.substack.com/p/hyperbolic-launches-forge-an-infrastructure); [Hyperbolic supply job](https://www.builtinchicago.org/job/supply-specialist/10560930); [Parasail capacity job](https://job-boards.greenhouse.io/parasail/jobs/5115827008); [Parasail pricing 2025](https://www.nextplatform.com/ai/2025/04/03/parasail-brokers-between-ai-compute-demand-and-supply/1661866); [Massed Compute on Shadeform](https://www.shadeform.ai/clouds/massedcompute); [Exabits seed round](https://pulse2.com/exabits-compute-base-layer-company-raises-15-million-seed); [Fluence GPU launch](https://decrypt.co/342785/fluence-launches-global-and-affordable-gpu-compute-for-ai); [Fluence on MiningBoard](https://miningboard.com/rental-markets/fluence); [Hivenet supplier blog](https://www.hivenet.com/post/from-mining-to-ai-powerhouse-meet-hivenets-first-certified-gpu-supplier).

#### B. Decentralized and token-paid networks (all CRYPTO unless noted)

| Network | Role and payment | Join / requirements | USD economics (public) | Rented cloud GPU allowed? |
|---|---|---|---|---|
| Bittensor overall | TAO price $257.61, market cap $3.01B (taostats, checked 2026-10-22). Top-10 emission shares shown on taostats: SN51 14.31%, SN64 8.61%, SN4 6.72% (checked 2026-10-22). Registration cost shown as 593.7 (units not labeled on page) | Miners register a hotkey per subnet in TAO | Per-miner USD earnings not published by taostats page I could read | Varies by subnet |
| SN64 Chutes (serverless inference) | Miners run "chutes" (inference apps) in a k3s cluster; "Incentives are based on total compute time"; paid in subnet alpha | Requirements: "ALL servers must be bare metal/VM, meaning it will not work on Runpod, Vast, etc., and we do not currently support shared or dynamic IPs"; "as much RAM per GPU as VRAM"; one non-GPU control server "8 cores, 64gb ram minimum"; ports 30000-32767 public; "Never register more than one UID"; "weights are calculated from 7 day sum of compute" | One 2026 table listed SN64 market cap at $80.2M (date unverified) ; per-miner earnings not found | Yes, explicitly: docs assume "CPU instances on one provider (AWS, Google, etc.), and GPU instances on another (Latitude, Massed Compute, etc.)" |
| SN4 Targon (confidential inference) | Miners run TargonOS; paid in alpha | "UEFI machine with Intel TDX enabled in BIOS, a TPM 2.0, and GPUs"; installer "refuses to proceed if TEE is disabled" | Revenue "unaudited projection of about $10.4M" (analyst) | Needs TDX bare metal; standard cloud VMs will not pass (inference) |
| SN51 Lium | See section A (USDT option) | See A | See A | See A |
| SN56 Gradients (G.O.D) | Miners submit training code; "trainers run those repositories on validator-controlled GPU infrastructure"; tournament fees 0.7 TAO (text), 0.4 TAO (image) | Not a GPU-supply role | n/a | n/a; you do not supply GPUs |
| SN19 Nineteen, SN27 NI Compute, SN3 Templar | not found (reference READMEs returned 404; search budget exhausted) | | | |
| Akash | Providers run Kubernetes clusters; tenants pay in AKT or axlUSDC | Ubuntu 24.04, x86_64, min 8 cores/16GB/150GB SSD; "You must own a domain name"; static public IP or DDNS; ports 80/443/8443/8444/30000-32767; "NVIDIA GPUs only"; "One GPU Type Per Node"; 100 Mbps symmetrical min (checked 2026-10-22). Bids need a refundable 5 AKT deposit | Third-party: take rate ~20% on USDC, ~4% on AKT; another source says take rate changed Mar 23, 2026 (Proposal #318). Tutorial claims H100 rents at $1.20 to $1.80/hr (secondary). 2024 annual network spend $1.62M (secondary) | Not stated; architecture is k8s on servers you control (gap) |
| io.net | Suppliers run IO Worker; paid in IO tokens hourly | docs.io.net/docs/io-worker redirects to overview (checked 2026-10-22) | Claims 100,000+ GPUs vs an independent count of ~6,720 verified active devices (mid-2026); per-GPU USD earnings not found | not found |
| Aethir | Cloud Hosts earn fees plus ATH | Enterprise-grade hosts; "Cloud Host for enterprise providers" | 2025 revenue "more than $127.8 million" and "$166 million" ARR (secondary citing Aethir); per-host earnings not found | not found |
| Render Network | Node operators render jobs; paid in RENDER | Operator onboarding not read | Protocol revenue about $409K (Q1 2026), $409K (Q2 2026), $467K (Q3 2026 partial) per DeFiLlama; "ROI ... not measurable yet" | not found |
| Nosana | Hosts paid in NOS | Consumer GPUs | Customer prices: RTX 4090 ~$0.40/hr, H100 ~$1.50/hr (aggregator); job demand "fell month over month in early 2026"; passive staking winds down Nov 28, 2026 | not found |
| Clore.ai | Hosts set price; paid CLORE/BTC (one aggregator also says USD) | Install hosting software | Renter fee 10% (5% with PoH); aggregator says host share 85%; 20,000+ GPUs (Apr 2026) | not found |
| Spheron Fizz | Liveness rewards in Spheron Points every 24h; lease fees mostly to operator | At least 50% uptime per 24h | Spheron lists H100 SXM at $3.92/hr (vendor blog, Jul 2026); operator earnings not found | not found |
| Gensyn | Testnet rewards fed a $AI token sale multiplier (Dec 2025); 2% reward pool unlocked Apr 29, 2026 | RTX 3090/4090/5090/A100/H100, 24GB+ VRAM (third-party guide) | Current reward rules not found | not found |
| Kuzco / Inference.net | Paid in KZO points/tokens | Min 16GB VRAM, 16GB RAM, 30GB disk | 8,500 active nodes (profile); per-GPU USD not found | not found |
| Gonka | Hosts earn GNK; "initially 323,000" GNK per epoch split by Proof of Compute weight | Hosts "post collateral" | ~11,000 H100-equivalents; "no secondary market trading" as of Jul 2026 profile, so USD value unrealizable | not found |
| Morpheus | Providers host open models, earn MOR | Stake MOR | Aug 2026 review: 63.2B tokens served, "users paid for 48,138 of them"; "a provider can earn no more MOR than it has staked"; MOR ~$2.14 | not found |
| Golem | Providers set GLM hourly rate | Nvidia 30xx+ with 8GB+ VRAM | ~732 active providers; Modelserve paused; GLM $0.136 (Feb 26, 2026) or ~$0.20 (conflicting) | not found |
| Lilypad | IncentiveNet (2024) paid Lilybit credits | not found for 2026 | not found | not found |
| Nous Psyche | Compute contributors to get crypto rewards | "testnet is closed to new nodes"; "data-center-grade GPUs" (low-authority source) | No token announced | not found |
| Livepeer | Orchestrators earn ETH fees plus LPT | GPU plus staking | AI fees ~$154,700 in Q1 2026 (~60% of protocol revenue); docs example: RTX 4090 at £800 earning £30/month; LIP-89 sends 10% of new LPT to treasury | not found |
| Sogni (Supernet) | Workers render images/video; "worker's 51% share"; paid in Spark/SOGNI tokens, claimable same day over a threshold | Fast Worker NFT for subscription pool | Sept 2026 full-month forecasts before costs: RTX 5090 $413 to $594; RTX PRO 6000 $813 to $1,102; RTX 4090 $259 to $357; RTX 5080 $174 to $242; worker pool "closed at $64,693"; one account's 133 workers did 57.6% of pool work (checked 2026-10-22) | not found |
| Salad (see D; moving on-chain) | Chefs paid in Salad balance, "Cash out for gift cards, games and subscriptions, or PayPal"; RNP-023 moves "payments and rewards to on-chain RENDER transactions" | Consumer single-GPU PCs | See D | Not designed for cloud |
| Hyperspace, Ritual, Pluralis, Prime Intellect protocol, "Ionet" (same as io.net) | not researched (search budget exhausted) | | | |

Sources for section B: [taostats subnets](https://taostats.io/subnets); [Chutes miner docs](https://chutes.ai/docs/miner-resources/overview); [SN64 market table](https://www.altcoinbuzz.io/6-top-subnets-on-bittensor); [TargonOS install](https://docs.targon.com/providers/miner/installing-targonos); [Targon revenue projection critique](https://pineanalytics.substack.com/p/the-bear-case-for-bittensor-tao); [G.O.D README](https://raw.githubusercontent.com/rayonlabs/G.O.D/main/README.md); [Akash hardware requirements](https://akash.network/docs/providers/getting-started/hardware-requirements/); [Akash stable payments](https://akash.network/docs/deployments/stable-payment-deployments/); [Akash take rate (secondary)](https://coinstancy.com/article/what-is-akash-network); [Akash 2026 fundamentals (FR)](https://journalducoin.com/defi/akash-network-akt-veteran-cloud-decentralise-gpu-ia-analyse-fondamentale/); [Akash H100 pricing claim](https://www.dextools.io/tutorials/what-is-akash-network-depin-cloud-compute-akt-guide-2026-pt); [io.net worker blog](https://blog.io.net/posts/unlock-the-potential-of-your-underutilized-hardware-rent-your-gpus-cpus-with-io-worker); [io.net active device analysis](https://yellow.com/zh/research/ai-计算需求已超越供给，加密网络正填补缺口); [Aethir 2025 revenue](https://yespress.io/aethir); [Render revenue (DeFiLlama)](https://defillama.com/token/RENDER); [Render operator ROI](https://gamefi-roi-web.onrender.com/opportunities/render-node-operator); [Nosana profile](https://solanacompass.com/projects/Nosana); [Nosana ROI page](https://gamefi-roi-web.onrender.com/opportunities/nosana-gpu-host); [Clore docs](https://docs.clore.ai/readme.md); [Clore host share (aggregator)](https://miningboard.com/rental-markets); [Spheron Fizz rewards](https://docs.spheron.network/fizz/reward-details); [Spheron H100 price post](https://spheron.network/blog/coreweave-h100-h200-pricing-2026); [Gensyn token sale](https://www.aap.com.au/aapreleases/cision20251215en47107); [Gensyn hardware guide](https://docs.spheron.network/guide-to-deploy/nodes/gensyn-ai); [Kuzco profile](https://solanacompass.com/projects/kuzco); [Kuzco requirements](https://docs.octa.space/inference-kuzco); [Gonka tokenomics](https://gonka.ai/tokenomics.pdf); [Gonka profile](https://www.fxempire.com/crypto/wrapped-gonka/profile); [Morpheus review](https://buttondown.com/ownyourmind/archive/we-built-morpheus-a-balance-sheet/); [MOR on DeFiLlama](https://defillama.com/token/mor); [Golem GPU guide](https://docs.golem.network/docs/providers/gpu/gpu-golem-live); [Golem usage critique](https://onekey.so/blog/ecosystem/glm-deep-research-report-token-utility-roadmap-and-price-outlook); [Lilypad IncentiveNet](https://lilypadnetwork.notion.site/Leap-into-Lilypad-s-IncentiveNet-9e9b12936d4340ad9417d92dab8bd9d1); [Psyche airdrop guide (low authority)](https://airdrops.io/?p=2019742); [Livepeer earning model](https://docs.livepeer.org/v2/orchestrators/guides/staking-and-rewards/earning-model.md); [Livepeer operator rationale](https://docs.livepeer.org/v2/orchestrators/guides/operator-considerations/operator-rationale); [Livepeer Q1 2026 fees](https://www.tokenpost.kr/research/1209); [Sogni Sept 2026 earnings](https://blog.sogni.ai/blogs/what-a-gpu-earns-on-sogni/); [Salad joins Render](https://blog.salad.com/salad-joins-render-network); [Salad on-chain payment rails](https://blog.salad.com/salad-payment-rails-onchain-milestone-3-architecture-rnp-023).

#### C. Direct customer channels and price references

Dedicated-endpoint and serverless-GPU list prices (all checked 2026-10-22):

| Vendor | H100 80GB | H200 | B200 | B300 | Other | Billing | Source |
|---|---|---|---|---|---|---|---|
| Together AI (Dedicated Model Inference) | $5.49/hr | contact sales | $8.99/hr | contact sales | GB300 contact sales | per minute, only ready replicas; reserved tier by contact | [Together DMI pricing](https://docs.together.ai/docs/dedicated-endpoints/pricing) |
| Fireworks (on-demand deployments) | $8.00/hr ($0.134/min) | $8.00/hr | $13.00/hr | $15.00/hr | GB300 $20.00/hr; region-restricted 1.5x | per GPU second | [Fireworks pricing](https://fireworks.ai/pricing) |
| Baseten (dedicated deployments) | $0.10833 listed (per minute; $6.50/hr estimate) | not listed | $0.16633 (per minute; $9.98/hr estimate) | not listed | A100 $0.06667 ($4.00/hr est.), H100 MIG $0.0625 ($3.75/hr est.), A10G $0.02012 ($1.21/hr est.), L4 $0.01414 ($0.85/hr est.), T4 $0.01052 ($0.63/hr est.) | per minute; "Volume discounts available" | [Baseten pricing](https://www.baseten.co/pricing/) |
| Modal (serverless) | $0.001097/sec ($3.95/hr; Modal's own example uses $3.95/GPU-hr) | $0.001261/sec ($4.54/hr est.) | $0.001736/sec ($6.25/hr est.) | $0.001972/sec ($7.10/hr est.) | RTX PRO 6000 $0.000842/sec ($3.03/hr est.), A100 80GB $0.000694/sec ($2.50/hr est.), L40S $0.000542/sec ($1.95/hr est.), A10 $0.000306/sec ($1.10/hr est.), L4 $0.000222/sec ($0.80/hr est.), T4 $0.000164/sec ($0.59/hr est.) | per second; Starter plan $30/month free credits | [Modal pricing](https://modal.com/pricing) |
| fal (serverless GPU) | list $4.50/hr, "as low as" $2.49/hr | $6.00 / $2.99 | $7.99 / $5.49 | $12.99 / $5.99 | GB200 $9.99 / $5.89; RTX PRO 6000 $4.00 / $1.99 | per second while runners alive | [fal pricing](https://fal.ai/pricing) |

A third-party tracker said Together's H100 endpoint fell to $3.99 on Sep 1, 2026 as a promotion through Sep 30, 2026, list $5.49; Together's docs showed $5.49 on 2026-10-22 ([morphllm tracker](https://www.morphllm.com/together-ai-pricing)).

Low-price GPU rental references a small provider competes against: Lium H100 $1.39/GPU-hr ([getdeploying](https://getdeploying.com/lium)); Akash H100 $1.20 to $1.80/hr (secondary, [dextools](https://www.dextools.io/tutorials/what-is-akash-network-depin-cloud-compute-akt-guide-2026-pt)); Spheron H100 SXM $3.92/hr (vendor, [Spheron blog](https://spheron.network/blog/coreweave-h100-h200-pricing-2026)); Nosana H100 ~$1.50/hr (aggregator).

Direct-demand evidence:
- An Upwork listing seeks an "Open WebUI Engineer, Self-Hosted LLM Platform, Deployment & Production Support" who can debug "model connections to vLLM, Ollama, and other OpenAI-compatible backends", with Docker/Kubernetes experience, for "real-world self-hosted LLM environments running Open WebUI in production" ([Upwork listing](https://www.upwork.com/freelance-jobs/apply/Open-WebUI-Engineer-Self-Hosted-LLM-Platform-Deployment-Production-Support_~022069931536353701997/)).
- A LocalLLaMA thread (2024) shows a consultant seeking private remote inference because client code cannot go to an uncontrolled provider ([thread mirror](https://lr.in.psf.lt/r/LocalLLaMA/comments/1fgxuon/private_remote_inference)). A community post names ArliAI as a small provider with "no rate-limits ... No-logging policy and ... OpenAI compatible API" ([lemmy post](https://old.lemmy.dbzer0.com/comment/13525360)).
- immers.cloud sells private endpoints "with hourly billing or long-term monthly subscriptions" ([immers.cloud FAQ](https://en.immers.cloud/faq/view/?id=179)).
- Modal offers academics "up to $10k free compute credits" and startups free credits, which is direct competition for academic and startup customers ([Modal pricing](https://modal.com/pricing)).
- Batch/offline inference buyers (Scale, Surge, Mercor, Turing), evaluation firms, Kaggle teams, Discord buyers, Toptal/Contra listings: not researched (search budget exhausted).

#### D. Adjacent GPU uses that pay in USD

| Option | What pays | Numbers (checked 2026-10-22) | Notes |
|---|---|---|---|
| Salad (SaladCloud "Chefs") | Container jobs, bandwidth sharing, mining on consumer GPUs; cash out via PayPal or gift cards | Oct 15 to 21, 2026 measured rates: RTX 4090 average $0.289/hr, "most machines" $0.285 to $0.302/hr, top 1% $0.481/hr, job running 97% of time; RTX 5090 $0.279/hr avg; RTX 5080 $0.154; RTX 3090 $0.081; RTX 3060 $0.036 | Single-GPU consumer machines; Salad recommends 32GB RAM and 500GB free storage. Salad is joining Render Network (RNP-023) and designing on-chain RENDER rewards (Aug 11, 2026 post), so the USD rail may change |
| Sogni | See B (crypto) | RTX 5090 $413 to $594/month forecast | Image/video generation marketplace |
| Livepeer (video transcoding, AI) | ETH fees + LPT | See B | Crypto |
| Render Network | RENDER tokens | See B | Crypto |
| Render farm marketplaces (Blender/Octane), scientific compute marketplaces, game streaming, speech/transcription resale, VFX "GPU for hire", Civitai/Runware provider programs | not researched (search budget exhausted) | | Folding@home and Stable Horde are unpaid (prior knowledge, not re-verified) |

Sources: [Salad earning rates](https://salad.com/earning-rates); [Salad blog index with RNP-023 posts](https://blog.salad.com/); [Sogni](https://blog.sogni.ai/blogs/what-a-gpu-earns-on-sogni/).

#### E. Reseller, affiliate and managed-service routes

| Program | Payout | Terms (checked 2026-10-22) | Source |
|---|---|---|---|
| Runpod referral | Credits: "5% commission on all Serverless spend for the first 6 months", "3% commission on all Pod spend for the first 6 months"; bonus $5 to $500 after referral loads $10 (about 96% get $10 or less) | Referral must sign up via Google SSO, be new, after Jun 15, 2025 | [Runpod referrals](https://docs.runpod.io/accounts-billing/referrals.md) |
| Runpod affiliate (PartnerStack) | "10% cash commission on all referral spend for the first 6 months" | Requires "at least 25 paying users" referred first; opting in is permanent | same |
| Runpod creator (templates) | "1% in Runpod Credits for every dollar spent using their templates" | Template needs 1 day total runtime | same |
| Thunder Compute referral | "3% of every dollar" as credits, lifetime, "cannot be converted to cash"; beta | Card payments only qualify | [Thunder referral](https://www.thundercompute.com/docs/guides/referral-program.md) |
| DigitalOcean referral | $25 credit after referee pays $25; credit cannot be cashed out | 30 invites/day | [DO referrals](https://docs.digitalocean.com/products/accounts/referrals/) |
| DigitalOcean affiliate | 10% commission; duration conflicts (12 months vs lifetime) across third parties | Application-based | [DO affiliates](https://try.digitalocean.com/affiliates); [RevShare listing](https://www.revshare.so/programs/advertiser/digitalocean-digitalocean-com) |
| Hydra Host partners | "Revenue Sharing"; rate not published | Includes "Managed Service Provider" partner type | [Hydra partners](https://hydrahost.com/partners/) |
| CoreWeave partners | No reseller/referral program on page; curated technology partner network, "Contact us" only | | [CoreWeave partners](https://www.coreweave.com/partners) |
| Lambda referral/affiliate | not found; only a third-party site says it has an affiliate relationship with Lambda | | [GPUPerHour disclosure](https://gpuperhour.com/affiliate-disclosure) |
| Nebius partners page | 404 (checked 2026-10-22) | | |
| Vultr referral page | HTTP 403 to fetcher (checked 2026-10-22) | | |
| Voltage Park, Crusoe, Massed Compute partner programs | not found | | |

Terms of service on resale and agency use (checked 2026-10-22):
- Runpod ToS (Last Updated March 24, 2026) prohibits: "Resell any credits purchased through the Service without the prior written consent of Runpod"; "Use a buying agent or purchasing agent to make purchases on the Site"; and Section 7 says "If the Account is a Runpod reseller account, the Account will be suspended" in a listed circumstance, which implies reseller accounts exist under consent. No managed-service-provider clause found ([Runpod ToS](https://www.runpod.io/legal/terms-of-service)).
- Lambda Cloud ToS grants "a non-sublicensable, non-transferable, non-exclusive right to access and use the Services"; no explicit resale or MSP clause in the first 100,000 characters; Platform Guidelines were truncated ([Lambda ToS](https://lambda.ai/legal/terms-of-service)).
- Cheaper Inference's Seller Agreement makes the seller warrant that "your Cloud Terms permit Keak to use the Credential and to send Routed Requests from Customers through the Seller Account" ([Seller Agreement](https://platform.cheaperinference.com/legal/seller-agreement)).
- Chutes miner docs explicitly expect rented bare metal: "GPU instances on another (Latitude, Massed Compute, etc.)" and exclude "Runpod, Vast, etc." ([Chutes](https://chutes.ai/docs/miner-resources/overview)).

#### F. Credits and subsidies (cost reducers, not revenue)

| Program | Amount | Eligibility (checked 2026-10-22) | Sole proprietor? | Source |
|---|---|---|---|---|
| AWS Activate Founders | "Start with $1,000 USD in Activate Credits. Select participants may qualify for additional credits up to $5,000" | Self-funded; "founded in the last 10 years"; "AWS Account on Paid Tier Plan" | Page does not mention incorporation or sole proprietors (not found) | [AWS Activate](https://aws.amazon.com/startups/credits) |
| AWS Activate Portfolio | "Up to $200,000 USD" | "Pre-Series B"; needs an Org ID from an Activate Provider (accelerator, angel, VC) | Needs an investor sponsor | same |
| Google for Startups Cloud | Base up to $2,000 (search summary); page fetch truncated | "not yet funded by an institutional investor"; founded within 5 years (other cached versions say 24 months or 3 years); excludes "dev shops, consultancies, or agencies"; "at the discretion of Google Cloud" | Unclear; a consultancy is excluded | [Google benefits page](https://cloud.google.com/startup/benefits) |
| Microsoft for Startups | "up to $150,000 in credits" | Tiers via usage or investor referral (third parties: ~$5K entry with business verification; $25K/$150K higher); not more than $10,000 prior free Azure | Third party says "privately held company building a software product you own" | [Microsoft for Startups](https://www.microsoft.com/en-us/startups); [aggregator](https://guptadeepak.com/startup-offers/guides/microsoft-for-startups) |
| NVIDIA Inception | Free membership; "free cloud credits from NVIDIA and partners"; preferred hardware pricing | "apply ... regardless of your company's current funding stage"; "no application fees, deadlines, or cohorts". Third parties list: incorporated, under 10 years, at least one developer, working website. A forum thread reports a solo founder told solo founders are ineligible (anecdotal) | Unincorporated likely fails "official incorporation" (third-party criteria) | [NVIDIA Inception](https://www.nvidia.com/en-us/startups/); [Thunder guide](https://www.thundercompute.com/blog/nvidia-inception-program-guide); [forum thread](https://forums.developer.nvidia.com/t/request-for-eligibility-review-inception-application-declined-without-a-stated-reason/376901) |
| Nebius | AI Explorer $5,000; AI Builder up to $100,000 (partner affiliation); AI Scaler up to $150,000 plus $10,000 inference; conflicting page versions. Inception route "temporarily confined to startups with $5M+ in venture backing" | Explorer: pre-seed, solo founder or team under 8, AI-first product, founded within 5 years (one version) | Solo founder explicitly allowed in one version | [Nebius startup program](https://nebius.com/startup-program); [Nebius Inception offer](https://nebius.com/nebius-nvidia-inception-credit-offering) |
| Runpod Startup Program | Starter $1,000; Growth: "Load $50,000 and get $25,000 in bonus credits", 12-month agreement | "Selective program for venture-backed AI startups"; Starter "Pre-Series A startups with working products" | Venture-backed expected | [Runpod startup program](https://runpod.io/startup-program) |
| Together AI Startup Accelerator | Build up to $15K (up to $5M raised); Scale up to $30K; Grow up to $50K; "Credits do not apply to Reserved GPU Clusters" | Form requires "Which VCs are you affiliated with?" | VC affiliation required field | [Together accelerator](https://together.ai/startup-accelerator) |
| Modal for Startups | "thousands of free GPU credits"; Starter plan gives everyone $30/month free credits; academics up to $10K | "Raised any amount of VC funding from our VC partner network" or ">$1m from any fund" | No (VC required), except the $30/month Starter credit | [Modal startups](https://modal.com/startups); [Modal pricing](https://modal.com/pricing) |
| Lambda | Up to $7,500 (aggregators, unverified; expire 12 months) | not found on Lambda site | not found | [aggregator](https://xraise.ai/blog/lambda-startup-credits/) |

### Inferences
- The cheaperinference.com seller path is a quota-arbitrage program for cloud API accounts (AWS, Microsoft, Google, Venice), not a GPU-hosting program. A solo operator would only fit if the "Provider" dropdown accepts a custom OpenAI-compatible endpoint, which I could not verify.
- SF Compute resale cannot create revenue for a party that owns no SF Compute allocation. It is a hedge for buyers. The fee has a fixed per-node-hour part, so very cheap short sales may net little.
- Lium is the only self-serve marketplace I found that pays a stablecoin (USDT) with a published 95% share and lists a node in minutes. It is still Bittensor-based and requires Discord connection for idle pay.
- Chutes is the only network that states in writing that rented bare-metal cloud servers are expected. Rewards are a token, so USD income depends on alpha price and on winning compute share against large miners.
- Most referral programs pay credits, not cash. Only Runpod's PartnerStack tier (after 25 paying referrals) and DigitalOcean's affiliate pay cash.
- Credit programs mostly require VC backing or an incorporated entity. A sole proprietorship realistically qualifies for AWS Activate Founders ($1,000 to $5,000), Modal's $30/month, and possibly Nebius AI Explorer ($5,000) if a solo founder with an AI product.

### Gaps
- Exact SF Compute fee rates, SF Compute hardware supplier terms, Shadeform supplier terms, Prime Intellect provider terms, Lepton partner criteria, Hydra Host revenue-share rate, Hyperbolic/Novita/Parasail/Massed/Foundry/GPUdeploy supply terms: not found.
- Compute Exchange 2026 status: site renders as a parked page; no 2026 coverage found.
- Per-GPU USD earnings for io.net, Aethir, Render, Nosana, Clore, Spheron, Gensyn, Kuzco, Gonka, Golem, Lilypad, Morpheus, Livepeer: not found.
- SN19, SN27, SN3, Hyperspace, Ritual, Pluralis, Nous Psyche current rules: not found (READMEs 404; search budget exhausted).
- Render-farm marketplaces, scientific compute marketplaces, game streaming, transcription resale, VFX GPU-for-hire, Civitai/Runware provider programs, Scale/Surge/Mercor/Turing as inference buyers, Toptal/Contra listings: not researched.
- Vultr, Nebius, Voltage Park, Crusoe, CoreWeave reseller commissions: not found.

## Key question 2: Which 5 options could realistically produce a first paying customer within 4 weeks for a solo operator, with evidence?

### Takeaway
The five with the best evidence are: (1) direct managed-inference consulting where the client pays the cloud and you bill a fee, (2) Lium Path A, (3) Chutes mining on rented bare metal (crypto), (4) Salad on owned consumer GPUs (small USD), and (5) Sogni on owned consumer or workstation GPUs (crypto). Everything else is sales-gated, credit-only, or lacks earnings evidence.

### Cited Findings
- Direct consulting demand exists: an Upwork posting seeks a senior engineer for "self-hosted LLM environments running Open WebUI in production" with vLLM/Ollama backends ([Upwork](https://www.upwork.com/freelance-jobs/apply/Open-WebUI-Engineer-Self-Hosted-LLM-Platform-Deployment-Production-Support_~022069931536353701997/)); privacy-driven buyers ask for private remote inference ([LocalLLaMA](https://lr.in.psf.lt/r/LocalLLaMA/comments/1fgxuon/private_remote_inference)). Runpod's ToS bars buying agents and credit resale, so the client must hold the cloud account ([Runpod ToS](https://www.runpod.io/legal/terms-of-service)).
- Lium: "No fee and nothing to buy"; node "usually listed for rent about 5 minutes after the command finishes"; "Earnings are paid in USDT once you add a payout address"; 95% share paid daily with a 2-day delay; 1,329 GPUs on the marketplace as of Sep 11, 2026 ([Lium quickstart](https://docs.lium.io/providers/quickstart); [Lium rewards](https://docs.lium.io/providers/rewards); [scale](https://pctechmag.com/?p=97853)).
- Chutes: explicit support for rented bare metal from "Latitude, Massed Compute, etc."; rewards accrue on a "7 day sum of compute", so first measurable income needs about a week of uptime; SN64 carries 8.61% of top-10 emissions on taostats (checked 2026-10-22) ([Chutes](https://chutes.ai/docs/miner-resources/overview); [taostats](https://taostats.io/subnets)).
- Salad: measured RTX 4090 average $0.289/hr with a job running 97% of the time for Oct 15 to 21, 2026; cash-out via PayPal ([Salad](https://salad.com/earning-rates)).
- Sogni: Sept 2026 forecast $413 to $594/month per RTX 5090 at 24/7 uptime before costs; "Pay-as-you-go earnings can be claimed the same day once the applicable earnings threshold is met" ([Sogni](https://blog.sogni.ai/blogs/what-a-gpu-earns-on-sogni/)).
- cheaperinference.com requires a team review before any routing: "We review provider fit" then "Discuss supply and settlement" ([home](https://cheaperinference.com)).
- Hydra Host promises a reply "within one business day" but publishes no rates ([Hydra](https://hydrahost.com/partners/)).

### Inferences
- Estimate: Lium and Chutes can show first revenue within 1 to 2 weeks of listing if hardware is rented at or below the soft limit, but Lium's 48-hour-of-rental penalty for a dropped rental (about $730 on an 8x H100 at $2.00/GPU-hr) makes rented, pre-emptible cloud capacity risky.
- Estimate: Salad and Sogni produce dollars in days but only on owned consumer GPUs; a rented H100 cannot earn there.
- Estimate: a consulting engagement is the only route likely to produce a four-figure USD invoice within 4 weeks, and it needs no platform approval.

### Gaps
- No public data on Lium or Chutes fill rates for a brand-new small provider.
- No evidence that cheaperinference.com or Hydra Host onboard sellers in under 4 weeks.

## Key question 3: Which options explicitly allow running on rented cloud GPUs?

### Takeaway
Only Chutes (SN64) says in writing that rented bare-metal or VM servers are the expected setup, while naming Runpod and Vast as unsupported. Cheaper Inference is built on cloud API accounts but shifts all cloud-terms risk to the seller. Others are silent.

### Cited Findings
- Chutes: "ALL servers must be bare metal/VM, meaning it will not work on Runpod, Vast, etc., and we do not currently support shared or dynamic IPs"; docs assume "GPU instances on another (Latitude, Massed Compute, etc.)" ([Chutes](https://chutes.ai/docs/miner-resources/overview)).
- Cheaper Inference: seller warrants "your Cloud Terms permit Keak to use the Credential"; "KEAK IS NOT LIABLE FOR ANY ACTION THAT A CLOUD PROVIDER TAKES ON YOUR SELLER ACCOUNT" ([Seller Agreement](https://platform.cheaperinference.com/legal/seller-agreement)).
- SF Compute resale only covers time bought on SF Compute ([SFC reselling](https://docs.sfcompute.com/preview/guides/reselling-introduction)).
- Lium requires Sysbox on the host and a static listing; it does not mention cloud rentals ([Lium quickstart](https://docs.lium.io/providers/quickstart)).
- Targon requires Intel TDX in BIOS and TPM 2.0 ([TargonOS](https://docs.targon.com/providers/miner/installing-targonos)).
- Akash requires a domain you own and a static public IP or DDNS, with Kubernetes on your servers ([Akash](https://akash.network/docs/providers/getting-started/hardware-requirements/)).
- Runpod ToS bans credit resale without consent and buying agents ([Runpod ToS](https://www.runpod.io/legal/terms-of-service)); Lambda grants a "non-sublicensable, non-transferable" right ([Lambda ToS](https://lambda.ai/legal/terms-of-service)).

### Inferences
- Lium and Akash will likely work on a rented bare-metal server or a VM with root and a static IP (inference), but not on container-style pods.
- Reselling a Runpod or Lambda pod through any of these marketplaces would conflict with "non-sublicensable" or anti-resale wording (inference); a managed-service model where the client holds the account avoids this.

### Gaps
- No marketplace besides Chutes publishes a list of permitted or banned upstream clouds.
- Vast.ai host terms were out of scope (covered elsewhere) and the search budget was exhausted before re-checking them.

## Key question 4: What do dedicated-endpoint customers pay per GPU-hour today, and what would a small provider have to charge to win?

### Takeaway
List prices for a dedicated H100 run from $3.95/hr (Modal) to $8.00/hr (Fireworks), with fal advertising "as low as" $2.49/hr; a small provider would need to land near or below $2.49/hr for H100 and show reliability to win on price alone.

### Cited Findings
- Together DMI: H100 $5.49/hr, B200 $8.99/hr; "A single H100 replica at $5.49/hour costs about $132/day, or roughly $3,950 over a 30-day month" ([Together](https://docs.together.ai/docs/dedicated-endpoints/pricing)).
- Fireworks: H100 and H200 $8.00/hr, B200 $13.00/hr, B300 $15.00/hr, GB300 $20.00/hr ([Fireworks](https://fireworks.ai/pricing)).
- Baseten: H100 $0.10833 per listed unit (per minute, $6.50/hr estimate), B200 $0.16633 ($9.98/hr estimate), A100 $0.06667 ($4.00/hr estimate) ([Baseten](https://www.baseten.co/pricing/)).
- Modal: H100 $0.001097/sec ($3.95/hr), H200 $0.001261/sec, B200 $0.001736/sec, B300 $0.001972/sec, A100 80GB $0.000694/sec, L40S $0.000542/sec ([Modal](https://modal.com/pricing)).
- fal: H100 list $4.50/hr, "as low as $2.49/hr"; H200 $6.00/$2.99; B200 $7.99/$5.49; RTX PRO 6000 $4.00/$1.99 ([fal](https://fal.ai/pricing)).
- Low-end rental benchmarks: Lium H100 $1.39/GPU-hr ([getdeploying](https://getdeploying.com/lium)); Akash H100 $1.20 to $1.80 (secondary); SF Compute example buy order at $18/node-hour = $2.25/GPU-hr ([SFC post](https://sfcompute.com/news/realized-discount)).

### Inferences
- Estimate: the winning price band for a small provider's managed dedicated H100 endpoint is about $2.00 to $3.50/hr, which sits between raw-rental benchmarks ($1.20 to $2.25) and the cheapest managed offers ($2.49 to $3.95). Margin on a rented $1.39 to $2.25 H100 is thin; a $2.99 price leaves roughly $0.75 to $1.60/hr before overhead (estimate).
- Per-token serverless competition (cheaperinference.com shows 33% to 50% discounts off list) undercuts dedicated endpoints for low-volume customers, so dedicated sales should target steady high-utilization or privacy-bound workloads (inference from Together's own guidance that DMI wins when "a replica would stay busy most of the day").

### Gaps
- Reserved-term discounts at Together, Fireworks and Baseten are quote-only (not found).
- The Together $3.99 H100 promo status after Sep 30, 2026 is unverified.

## Key question 5: Are there programs that let a small operator sell reserved GPU blocks legally (SF Compute, Compute Exchange, Lepton)?

### Takeaway
SF Compute lets any customer resell reserved blocks it bought on SF Compute, for credits, under a published fee structure without published rates; Compute Exchange's site is parked and Lepton's supply side is limited to NVIDIA Cloud Partners, so neither is open to a small operator today.

### Cited Findings
- SF Compute: "Sell unused compute time through the SF Compute orderbook"; "You receive credits only when a buyer buys the time"; "Fills use whole minutes, with a minimum of 1 node for 1 minute"; sell orders can stand until filled; fee has fixed and percentage parts set by SFC; "The fee cannot exceed the sale value" ([SFC reselling](https://docs.sfcompute.com/preview/guides/reselling-introduction); [public preview status](https://docs.sfcompute.com/preview/roadmap)).
- SF Compute reports a 25% average realized discount for customers reselling idle capacity (Sep 9, 2026) ([SFC](https://sfcompute.com/news/realized-discount)).
- Compute Exchange: launch PR Jan 28, 2025; "$1 billion in compute supply" claim Apr 2, 2025; domain shows a placeholder page on 2026-10-22 ([PR](https://www.businesswire.com/news/home/20250402039147/en/Compute-Exchange-Auction-Model-Broadens-AI-Compute-Access-With-%241B-Supply)).
- Lepton: supply comes from "NVIDIA Cloud Partners (NCPs), GPU marketplaces, cloud providers"; Hydra Host joined as an NCP ([NVIDIA](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/); [Hydra](https://hydrahost.com/post/hydra-host-named-nvidia-dgx-cloud-partner/)).
- Hydra Host's Brokkr accepts "resellers and neoclouds reselling capacity" and "Managed Service Provider" partners with revenue sharing ([Hydra partners](https://hydrahost.com/partners/)).

### Inferences
- SF Compute resale is a legal way to shed risk on a reserved block, but it returns credits, so it only helps an operator who already buys on SFC and wants to sell idle hours.
- Hydra Host is the most plausible "small reseller" door among the block markets because its partner page names resellers and MSPs explicitly, but terms are undisclosed.

### Gaps
- SF Compute fee rates, minimum purchase sizes, and KYC requirements are behind a login (pricing page redirects to WorkOS auth).
- Compute Exchange operating status in 2026 is unknown.

## Key question 6: Realism ranking for a solo operator by Dec 31, 2026

### Takeaway
Realistic revenue by year-end comes from selling labor plus hosting (managed inference), then Lium, then crypto-paid networks that accept rented bare metal; block markets, partner programs and credits are either closed to small operators or are cost reducers.

### Cited Findings

| Rank | Option | Currency | Realism by Dec 31, 2026 | One-line reason |
|---|---|---|---|---|
| 1 | Managed inference consulting (client pays the cloud; you bill a fee) | USD | High | Demand visible on Upwork for self-hosted LLM deployment; avoids Runpod/Lambda resale clauses because the client holds the account ([Upwork](https://www.upwork.com/freelance-jobs/apply/Open-WebUI-Engineer-Self-Hosted-LLM-Platform-Deployment-Production-Support_~022069931536353701997/); [Runpod ToS](https://www.runpod.io/legal/terms-of-service)) |
| 2 | Lium Path A provider | USDT (or alpha) | High | Self-serve, no fee, listed in ~5 minutes, 95% share, daily payouts ([Lium](https://docs.lium.io/providers/quickstart)) |
| 3 | Chutes SN64 miner on rented bare metal | CRYPTO (alpha) | Medium | Only network that explicitly allows rented bare metal; 7-day compute window; needs k3s cluster and static IPs ([Chutes](https://chutes.ai/docs/miner-resources/overview)) |
| 4 | Salad on owned consumer GPUs | USD via PayPal (moving on-chain) | Medium (low dollars) | Measured $0.289/hr for an RTX 4090 with 97% job time ([Salad](https://salad.com/earning-rates)) |
| 5 | Sogni worker on owned 5090/RTX PRO 6000 | CRYPTO | Medium (low dollars) | Published monthly forecasts $413 to $1,102 per card, one account dominates the pool ([Sogni](https://blog.sogni.ai/blogs/what-a-gpu-earns-on-sogni/)) |
| 6 | Direct dedicated endpoints priced under fal/Modal | USD (Stripe) | Medium | Price ceiling $2.49 to $3.95/hr for H100 set by fal and Modal ([fal](https://fal.ai/pricing); [Modal](https://modal.com/pricing)) |
| 7 | cheaperinference.com capacity seller | Unstated (dashboard) | Low-Medium | Needs cloud API quota, not GPUs; sales review; seller bears cloud-terms risk ([Seller Agreement](https://platform.cheaperinference.com/legal/seller-agreement)) |
| 8 | Hydra Host partner (reseller/MSP) | USD (rev share) | Low-Medium | Open application, 1-day reply, but no rates and bare-metal focus ([Hydra](https://hydrahost.com/partners/)) |
| 9 | Akash provider | AKT or axlUSDC | Low-Medium | Needs domain, static IP, k8s; thin demand data; take rate up to ~20% on USDC (secondary) ([Akash](https://akash.network/docs/providers/getting-started/hardware-requirements/)) |
| 10 | Runpod/DigitalOcean affiliate cash tiers | USD | Low | Runpod cash only after 25 paying referrals; DO 10% unverified ([Runpod](https://docs.runpod.io/accounts-billing/referrals.md)) |
| 11 | SF Compute resale | Credits | Low (not revenue) | Only resells SFC-bought time; fee rates unpublished ([SFC](https://docs.sfcompute.com/preview/guides/reselling-introduction)) |
| 12 | Clore, Fluence, Nosana, io.net, Render, Aethir, Livepeer, Golem, Morpheus, Gonka, Kuzco | CRYPTO | Low | No per-GPU USD earnings found; several show falling demand or no liquid token ([Gonka](https://www.fxempire.com/crypto/wrapped-gonka/profile); [Morpheus](https://buttondown.com/ownyourmind/archive/we-built-morpheus-a-balance-sheet/)) |
| 13 | Lepton, Shadeform, Prime Intellect, Hyperbolic, Parasail, Novita, Massed supply | USD | Very low | NCP or datacenter scale, sales-gated, no self-serve ([NVIDIA](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/)) |
| 14 | Compute Exchange | USD | Very low | Site parked on 2026-10-22; no 2026 activity found |
| 15 | Targon SN4 | CRYPTO | Very low | Requires Intel TDX bare metal ([TargonOS](https://docs.targon.com/providers/miner/installing-targonos)) |
| 16 | Gradients SN56, Gensyn, Nous Psyche, Lilypad | CRYPTO | Very low | No GPU-supply role, closed testnet, or stale program ([G.O.D](https://raw.githubusercontent.com/rayonlabs/G.O.D/main/README.md)) |
| n/a | Credits (AWS Founders $1K to $5K, Nebius Explorer $5K, Modal $30/mo) | Cost offset | Useful | Reduce cost; most other credit programs need VC or an incorporated entity ([AWS](https://aws.amazon.com/startups/credits); [Nebius](https://nebius.com/startup-program); [Modal](https://modal.com/pricing)) |

### Inferences
- A sole proprietorship should expect to be excluded from NVIDIA Inception, Runpod Growth, Together, and Modal startup credits, and should budget only for AWS Founders, Nebius Explorer, and Modal Starter credits.
- Crypto options can still matter as filler for idle rented hours, but every dollar figure above for them is a forecast or a token price, not settled cash.

### Gaps
- No public fill-rate or customer-count data for Lium or Chutes small providers.
- Render farms, scientific marketplaces, transcription resale, VFX hire, Civitai/Runware, Scale/Surge/Mercor buyers, Kaggle/academic channels, and Hyperspace/Ritual/Pluralis were not researched because the search budget ran out.
