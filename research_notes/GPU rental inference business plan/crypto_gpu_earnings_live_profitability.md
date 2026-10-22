# Crypto and token-paid GPU earnings: live profitability on 2026-10-22

All numbers below were read on 2026-10-22 unless a source shows its own date. "Estimate" marks my arithmetic. "Not found" marks data no fetched page provided. WebSearch quota ran out mid-task, so some pages were reached by direct URL only; items I could not reach are listed under Gaps.

Reference prices used in arithmetic (all checked 2026-10-22):

| Asset | Price | Source |
|---|---|---|
| BTC | $81,498.50 | [CoinGecko](https://www.coingecko.com/en/coins/bitcoin) |
| TAO | $257.97 (taostats) / $255.93 (CoinGecko, 24h -7.6%) | [taostats](https://taostats.io/subnets), [CoinGecko](https://www.coingecko.com/en/coins/bittensor) |
| IO | $0.1549 | [CoinGecko](https://www.coingecko.com/en/coins/io-net) |
| NOS | $0.5187 | [CoinGecko](https://www.coingecko.com/en/coins/nosana) |
| ATH | $0.005798 | [CoinGecko](https://www.coingecko.com/en/coins/aethir) |
| GNK | $0.1998 (FDV $86.79M, no circulating supply reported) | [CoinGecko](https://www.coingecko.com/en/coins/gonka) |
| LPT | $1.57 | [CoinGecko](https://www.coingecko.com/en/coins/livepeer) |
| AKT | $0.703 | [Akash provider calculator](https://akash.network/pricing/provider-calculator/) |
| PRL (Pearl) | 0.00002561 BTC on SafeTrade = $2.09 (estimate: 0.00002561 x 81,498.50) | [WhatToMine PRL](https://whattomine.com/coins/469-prl-pearl) |

Rental benchmarks used for the "rented GPU" cost side (all checked 2026-10-22):

| GPU | Low rental | High rental | Sources |
|---|---|---|---|
| RTX 4090 | $0.34/hr (Akash) = $8.16/day | $0.89/hr (RunPod) = $21.36/day | [Akash GPU pricing](https://akash.network/pricing/gpus/), [RunPod pricing, updated Oct 8, 2026](https://www.runpod.io/pricing) |
| RTX 5090 | $0.57/hr (Akash) = $13.68/day | $1.19/hr (RunPod) = $28.56/day | same |
| RTX 3090 | $0.15/hr (Akash) = $3.60/day | $0.50/hr (RunPod) = $12.00/day | same |
| H100 80GB | $1.93/hr avg (lium.io 30-day) or $2.00/hr spot 8x Helsinki = $46.32 to $48/day | $2.73/hr Akash, $2.89 RunPod PCIe, $3.99 RunPod SXM = $65.52 to $95.76/day | [lium.io provider page](https://lium.io/rent-out-your-gpu), [lium.io](https://lium.io/), Akash, RunPod |
| H200 141GB | $5.29/hr (RunPod pod) = $126.96/day; 8x = $1,015.68/day | $6.35/hr (RunPod cluster) = $152.40/day | [RunPod pricing](https://www.runpod.io/pricing) |

Vast.ai's pricing page did not render prices in the fetch ([vast.ai/pricing](https://vast.ai/pricing), checked 2026-10-22), so the Akash and RunPod figures stand in for the ranges the owner gave ($0.34 to $0.89 for the 4090, $0.69 to $1.19 for the 5090, $2 to $4 for the H100). Those ranges are consistent with what Akash, RunPod and lium show.

## Key question 1: What does classic GPU proof-of-work mining earn today?

### Takeaway
Only two brand-new coins (Pearl, Quantus) show meaningful revenue: a 4090 shows $9.84/day and a 5090 $11.75/day on WhatToMine at $0.10/kWh. Every legacy coin the owner remembers (RVN, ERG, FIRO, NEXA, CFX, ETC) pays under $1.10/day gross on a 4090 and most are negative after power. No calculator lists an H100.

### Cited Findings
- WhatToMine GPU ranking at $0.10/kWh, checked 2026-10-22: RTX 5090 (marked "Limited, unverified results") 370.00 Th/s Pearl at 520 W, revenue $11.75/day, profit $10.50/day; RTX 4090 310.00 Th/s Pearl at 400 W, revenue $9.84/day, profit $8.88/day; RTX 3090 130.00 Th/s Pearl at 320 W, revenue $4.13/day, profit $3.36/day. Second and third coins: 5090 Quantus (QPoW) $7.73 revenue / $6.53 profit, Qubitcoin (Qhash) $1.61 profit; 4090 Quantus $5.24 / $4.59, QTC $2.37 / $1.65; 3090 Quantus $2.74 / $2.21, ZCL $1.59 / $1.01. The page states electricity at $0.10/kWh. No H100 row exists. [WhatToMine GPUs](https://whattomine.com/gpus)
- Pearl (PRL) on WhatToMine: "Fresh coin, early version miners. Input pool reported hashrate, not miner hashrate." Exchange: SafeTrade only. Rate 0.00002561 BTC per PRL. 24h volume 73.392 BTC. Market cap shown as $0. Network hashrate 74,666.27 Ph/s, block reward 2,232.28 PRL. Checked 2026-10-22. [WhatToMine PRL](https://whattomine.com/coins/469-prl-pearl)
- Quantus (QUANTUS, QPoW) on WhatToMine: SafeTrade only, 24h volume 1.758 BTC, market cap shown as $0, network hashrate 25.60 Th/s, block reward 0.30. Checked 2026-10-22. [WhatToMine Quantus](https://whattomine.com/coins/473-quantus-qpow)
- hashrate.no RTX 4090 at $0.10/kWh, checked 2026-10-22 (revenue / profit per day): Pearl $10.29 / $9.62 (308.21 Th/s, 280 W); Quantus $8.09 / $7.38; Parano1d NOID $3.76 / $3.06; Qubitcoin $2.51 / $1.89; Epic Cash $1.68 / $0.96; Aeternity $1.52 / $0.88; Conflux $1.06 / $0.39; Iron Fish $0.75 / $0.18; Firo $0.84 / $0.12; Xelis $0.46 / $0.10; Karlsen $0.56 / -$0.02; Ergo $0.33 / -$0.11; Neurai $0.32 / -$0.39; Ravencoin $0.26 / -$0.45; Nexa $0.37 / -$0.46; ETC $0.06 / -$0.54; OctaSpace $0.06 / -$0.54. Flux, Neoxa, Clore, Zephyr, Alephium and Kaspa are not on the 4090 list. [hashrate.no 4090](https://www.hashrate.no/gpus/4090)
- hashrate.no RTX 5090 at $0.10/kWh, checked 2026-10-22: Pearl $13.95 / $12.71 (417.89 Th/s, 519 W); Quantus $8.28 / $7.31; Qubitcoin $2.76 / $2.15; Epic Cash $2.53 / $1.43; Conflux $1.85 / $0.70; Iron Fish $1.22 / $0.41; Karlsen $0.91 / $0.10; Ergo $0.69 / $0.04; Ravencoin $0.39 / -$0.72; Nexa $0.50 / -$0.68; ETC $0.10 / -$0.87. [hashrate.no 5090](https://www.hashrate.no/gpus/5090)
- hashrate.no RTX 3090 at $0.10/kWh, checked 2026-10-22: Pearl $4.18 / $3.39 (326 W); Epic Cash $1.48 / $0.65; Conflux $0.95 / $0.13; Iron Fish $0.73 / $0.08; Firo $0.78 / -$0.05; Ergo $0.32 / -$0.24; Ravencoin $0.20 / -$0.57; ETC $0.06 / -$0.71. [hashrate.no 3090](https://www.hashrate.no/gpus/3090)
- minerstat RTX 4090 (does not list Pearl): top coin XTM (Tari) revenue "about $1.75 per day" and $1.29 profit at $0.08/kWh; break-even power price $0.307/kWh; profit $1.18 at $0.10/kWh and $1.07 at $0.12/kWh. Measured hashrates: KawPow 65 MH/s at 299 W, Autolykos2 265.8 MH/s at 183 W, Octopus 123.1 MH/s at 279 W, Ethash 124.7 MH/s at 249 W (benchmarks dated 2026-09-30 to 2026-10-01). [minerstat 4090](https://minerstat.com/hardware/nvidia-rtx-4090)
- Kaspa: KHeavyHash, network hashrate 365.61 Ph/s, est. revenue $0.188/day per Th/s. No GPU row. Checked 2026-10-22. [hashrate.no Kaspa](https://www.hashrate.no/coins/kaspa)
- Alephium: Blake3, network hashrate 5.97 Ph/s, est. revenue $0.000256/day per Gh/s. No GPU row. Checked 2026-10-22. [hashrate.no Alephium](https://www.hashrate.no/coins/alephium)
- Flux: "This coin is currently disabled and not receiving updates" on hashrate.no. The Flux site says a soft fork "eliminated wasteful GPU mining" and PoUW v2 "removes mining pools". [hashrate.no Flux](https://www.hashrate.no/coins/flux); [runonflux.com/fluxnodes](https://runonflux.com/fluxnodes)
- Clore (KawPow): "currently disabled and not receiving updates" on hashrate.no. Clore now operates as a GPU rental marketplace (see Key question 4). [hashrate.no Clore](https://www.hashrate.no/coins/clore)
- Neoxa (KawPow): "currently disabled and not receiving updates". [hashrate.no Neoxa](https://www.hashrate.no/coins/neoxa)
- Zephyr: RandomX (a CPU algorithm), est. revenue $0.0180/day per Kh/s. Not on any GPU list. [hashrate.no Zephyr](https://www.hashrate.no/coins/zephyr)
- H100 mining revenue: not found on WhatToMine, hashrate.no or minerstat.

### Inferences
- Power sensitivity (estimate, using WhatToMine revenue and wattage): RTX 4090 mining Pearl uses 400 W x 24 h = 9.6 kWh/day. Net = $9.84 minus power: $8.88 at $0.10, $7.44 at $0.25, $6.96 at $0.30, $9.07 at $0.08, $8.69 at $0.12. RTX 5090: 520 W = 12.48 kWh/day. Net = $11.75 minus power: $10.50 at $0.10, $8.63 at $0.25, $8.01 at $0.30, $10.75 at $0.08, $10.25 at $0.12. RTX 3090: 320 W = 7.68 kWh/day. Net = $4.13 minus power: $3.36 at $0.10, $2.21 at $0.25, $1.83 at $0.30.
- Rented GPU arithmetic (estimate): 4090 at $0.34/hr costs $8.16/day; mining Pearl at $9.84/day nets +$1.68/day only at that floor price and only on an unverified fresh coin. At $0.89/hr ($21.36/day) the net is -$11.52/day. 5090 at $0.57/hr ($13.68/day) nets -$1.93/day; at $1.19/hr ($28.56/day) nets -$16.81/day. H100 at $1.93 to $3.99/hr costs $46.32 to $95.76/day with no listed mining revenue; even if it matched a 5090 ($11.75) it would lose $34 to $84/day.
- Without Pearl and Quantus, the best 4090 coin is NOID at $3.76/day gross, and the classic coins the owner knows pay $0.26 to $1.06/day gross. Classic GPU mining as the owner remembers it is dead; what remains is launch-sniping of fresh coins with single-exchange liquidity.
- Pearl's $0 market cap on WhatToMine and single SafeTrade listing mean the dollar figures depend on being able to sell PRL at the quoted BTC rate. A 73 BTC daily volume figure for a "fresh coin" is unusual and should be treated as unverified.

### Gaps
- No H100 or H200 hashrate data exists on the calculators; nobody benchmarks datacenter cards for PoW.
- I could not verify Pearl's exchange liquidity or whether the quoted volume is real; SafeTrade was not fetched.
- 2cryptocalc was not fetched (search quota exhausted); WhatToMine, hashrate.no and minerstat agree closely so the gap is minor.

## Key question 2: What do cloud providers' terms say about mining?

### Takeaway
Lambda, Nebius, Voltage Park and TensorDock ban or gate crypto mining in writing; Vast.ai bans it for anyone who buys credits by credit card; RunPod, Hyperbolic and Crusoe have no mining clause in the documents fetched. Separately, the networks themselves (Chutes, Targon, Aethir, Salad, Nosana) require bare metal, TEE or owned consumer PCs, which excludes rented pods regardless of cloud terms.

### Cited Findings
- RunPod Terms of Service, "Last Updated: March 24, 2026": no clause mentions cryptocurrency, mining, blockchain or proof of work. Section 9 "Prohibited Activities" says "You may not access or use the Site for any purpose other than that for which we make the Site available." Section 8 names Crypto.com as a payment provider. The RunPod legal page links only the Trust Center and contact page, no AUP. [RunPod ToS](https://www.runpod.io/legal/terms-of-service); [RunPod legal](https://www.runpod.io/legal)
- Lambda Acceptable Use Policy, Section 3 "Certain High Risk Activities": "You shall not use the Services in support of mining of cryptocurrency including but not limited to BitCoin" "or any similar currency." Terms page last updated August 2025. [Lambda ToS](https://lambda.ai/legal/terms-of-service)
- Vast.ai Terms, "Version Date: September 1, 2026", Prohibited Activities item 22: "If you purchase credits for use of services on or through the Website using a credit card," "you may not engage in any cryptocurrency mining, including but not limited to Bitcoin mining," "Ethereum mining, or any other form of digital currency mining." Definition: "cryptocurrency mining refers to the process of using computer processing power to validate and record transactions in a public ledger for a cryptocurrency network. This includes any operation that involves the use of Company or Provider resources to solve complex mathematical problems or algorithms associated with the generation or transaction of cryptocurrencies." [Vast.ai terms](https://vast.ai/terms)
- TensorDock Acceptable Use Policy, "Last updated: June 27, 2024", Section 4 "Spam and Inauthentic Activity" lists "cryptocurrency mining, without our express written permission;" as disallowed. [TensorDock AUP](https://docs.tensordock.com/legal-information/acceptable-use-policy-aup)
- Hyperbolic Terms, "Last Updated Date: March 24, 2025": no reference to crypto mining, mining, blockchain or proof of work in the visible text; Section 9.3 only says Points "cannot be redeemed for cash or cash equivalent, including any cryptocurrency." [Hyperbolic terms](https://www.hyperbolic.ai/terms)
- Nebius Acceptable Use Policy, effective June 26, 2026, Section 14: "Mining means using the resources of Nebius Platform to create cryptocurrency." Section 4 "Prohibition of Mining": 4.1 "Nebius may suspend Customer's right to access the Services immediately without prior notice to Customer, if Customer uses Services for Mining." 4.2 "Nebius may undertake any technical and organizational measures for limiting the possibility of using Services for Mining." [Nebius AUP](https://docs.nebius.com/legal/aup)
- Crusoe Acceptable Use Policy Version 1.1, effective August 7th 2026 (Version 1.0 ran August 1st 2023 to August 7th 2026): no clause mentions cryptocurrency, crypto mining, blockchain or proof of work. The closest clause prohibits operating "abusive network infrastructure" (open mail relays, open proxies, open recursive DNS resolvers, Tor exit nodes). [Crusoe legal hub](https://legal.crusoe.ai/)
- Voltage Park Compute Services Agreement, Exhibit A Acceptable Use Policy, "Last Revised on May 28, 2026", item 9: "use the Services for crypto-mining;" is prohibited. The AI Factory Usage Policy (revised October 20, 2025) has no crypto clause. [Voltage Park CSA](https://voltagepark.com/computer-services-agreement); [AI Factory Usage Policy](https://voltagepark.com/ai-factory/usage-policy)
- Salad Terms of Service for Chefs, "Last Updated: September 28, 2026": Section 2 says the app "utilizes a portion of the computation power, internet bandwidth, or other resources of your personal computer or laptop"; Section 6 item 16 prohibits running the App "on a virtual machine or emulator" or "on any computer you do not own or control, without the Company's written permission"; Section 3 "Reward Points have no cash value." [Salad Chefs terms](https://salad.com/terms/chefs/)
- Chutes miner README: "ALL servers must be bare metal/VM, meaning it will not work on Runpod, Vast, etc." and "The chutes network is now TEE-exclusive" (Intel TDX confidential VMs). [chutes-miner](https://github.com/rayonlabs/chutes-miner)
- Targon miner docs: TargonOS wipes every eligible disk, requires "The TEE must be enabled in BIOS for the installer to proceed", and GPU profiles require "exactly 8 GPUs of the listed SKU". [Targon miner.md](https://github.com/manifold-inc/targon/blob/main/docs/miner/miner.md)
- Aethir Cloud Host operational requirements: "The infrastructure must consist of bare-metal servers"; "Only enterprise-grade GPUs that meet our benchmarked performance metrics"; 99% Monthly Uptime Rate; daily offline time under 30 minutes. [Aethir requirements](https://docs.aethir.com/aethir-cloud/aethir-cloud-host/operational-requirements-for-cloud-hosts)
- Nosana host guide: "Native Linux only. Windows, including WSL2, is being deprecated"; "Nosana supports 1 private key per GPU, 1 GPU per PC". [Nosana host guide](https://learn.nosana.com/hosts/grid.html)
- io.net docs: "Devices available for hire on io.net should remain idle and not perform any computationally intensive tasks." No datacenter, cloud or VM rule found. [io.net docs index](https://io.net/docs/llms.txt)

### Inferences
- A renter who wants to run PoW on RunPod, Crusoe or Hyperbolic would not breach a written mining clause, but RunPod's "any purpose other than that for which we make the Site available" language gives it discretion. Lambda, Nebius, Voltage Park and TensorDock are explicit bans. Vast.ai bans it for card-funded accounts, which is most retail accounts.
- The "AI mining" networks are a harder wall than the cloud terms: Chutes and Targon need TEE-capable bare metal with BIOS access; Aethir needs bare metal; Salad needs an owned Windows PC and forbids VMs; Nosana needs native Linux with one GPU per machine. None of these can run inside a rented container pod.

### Gaps
- RunPod: no AUP or host (Community Cloud) agreement was found on its legal page; a host-side mining rule may exist in the console and was not fetched.
- Lambda's "Platform Guidelines" (incorporated by reference) were beyond the fetched 100,000 characters.
- Akash and Hyperbolic supply-side host terms were not fetched.

## Key question 3: Bittensor "AI mining": what do the compute and inference subnets pay, and who can mine?

### Takeaway
Bittensor emits 3,600 TAO/day network-wide; each subnet also emits 7,200 alpha/day with 41% to miners. The three compute subnets that matter are SN51 lium.io ($85.6k/day to 74 miners), SN64 Chutes ($51.7k/day to 18 miners, TEE-only) and SN4 Targon ($40.1k/day to 5 miners, 8-GPU TEE nodes, auction capped at about $2.90 to $3.50 per H200-hour). SN27 (formerly NI Compute, now "Orion") pays miners zero. SN19 Nineteen and SN3 Templar no longer exist under those names.

### Cited Findings
- TAO price $257.97 (-6.10%), market cap $3.01B, 24h volume $202.72M, new-subnet registration cost 593.7 TAO, 128 subnets, total daily TAO emission 3,599.9995 (table total row). Checked 2026-10-22. [taostats subnets](https://taostats.io/subnets)
- Per-subnet rows (taostats, checked 2026-10-22; "Total Emission" is TAO/day flowing to the subnet; price is alpha in TAO):
  - SN51 lium.io: price 0.112388 tau, market cap 558.06K tau, Total Emission 515.5485 tau/day (14.32%), Injected 110.6874, Chain Buys 404.8611, Root Prop 13.68%.
  - SN64 Chutes: price 0.067863, MCap 422.61K, Total Emission 311.0327 (8.64%).
  - SN4 Targon: price 0.052651, MCap 313.63K, Total Emission 242.2753 (6.73%).
  - SN120 Affine: 0.041541, 180.48K, 173.7717 (4.83%), Incentive Burn 10.00%.
  - SN8 Vanta (formerly proprietary trading): 0.031254, 172.75K, 141.796 (3.94%). Excluded per brief.
  - SN3 Teutonic (netuid 3): 0.022755, 131.16K, 101.2502 (2.81%).
  - SN9 iota (Macrocosmos): 0.023707, 122.53K, 105.3687 (2.93%).
  - SN56 Gradients: 0.014977, 81.85K, 60.5517 (1.68%).
  - SN110 Green Compute: 0.025348, 80.95K, 113.7153 (3.16%).
  - SN19 blockmachine: 0.009089, 47.84K, 26.5869 (0.74%).
  - SN95 Actual and SN39 deprecated: 0% emission, Root Prop 100%.
  - Top-10 emission legend: lium.io 14.31%, Chutes 8.61%, Targon 6.72%, Affine 4.86%, Minos 4.04%, REAX 3.93%, OpenRoboto 2.92%, SOMA 2.62%, ORO 2.46%, KubeTEE 2.37%. [taostats subnets](https://taostats.io/subnets)
- SN64 Chutes detail page, checked 2026-10-22: price 0.067864 tau = $17.394199; market cap $108.32M; FDV $365.28M; circulating 6.23M alpha; TAO in pool 200.60K; eTao split Owner 18%, Vali/Root 5.38%, Vali/Alpha 35.62%, Miner 41%; Tao Injected 64.14 (1.78%); Tao Chain Buys 246.91 (6.86%); Tao Emission Total 311.05 (8.64%); Incentive Burn 0.00%; "Emissions / Day 488.62"; "Miner / Day 200.34 //41%"; "Validator / Day 200.34"; "Owner / Day 87.95"; "Reg Cost 0.00"; Holders 12,606. Metagraph: 256 UIDs, Active Validators 14, Active Miners 18, Maximum Validators 64. [taostats SN64](https://taostats.io/subnets/64); [SN64 metagraph](https://taostats.io/subnets/64/metagraph)
- SN4 Targon detail, checked 2026-10-22: price 0.052651 tau = $13.494964; market cap $80.39M; Tao Emission Total 242.27 (6.73%); Emissions / Day 379.09; Miner / Day 155.42; Owner / Day 68.23; Reg Cost 0.00; Holders 7,419. Metagraph: 256 UIDs, Active Validators 9, Active Miners 5, Active Dual UIDs 1. [taostats SN4](https://taostats.io/subnets/4); [SN4 metagraph](https://taostats.io/subnets/4/metagraph)
- SN51 lium.io detail, checked 2026-10-22: price 0.112401 tau = $28.757903; market cap $142.80M; Tao Emission Total 515.55 (14.32%); Emissions / Day 809.29; Miner / Day 331.81; Owner / Day 145.67; Reg Cost 0.50; Holders 7,061. Metagraph: 256 UIDs, Active Validators 9, Active Miners 74. [taostats SN51](https://taostats.io/subnets/51); [SN51 metagraph](https://taostats.io/subnets/51/metagraph)
- SN27 (now "Orion", SILX Labs; this is the netuid formerly branded NI Compute), checked 2026-10-22: price 0.002219 tau = $0.568773; market cap $2.79M; Tao Emission Total 0.00 (0.00%); Incentive Burn 100.00%; Emissions / Day 15.97; "Miner / Day 0.00 //41%"; Validator / Day 6.55. [taostats SN27](https://taostats.io/subnets/27)
- Chutes miner requirements (README, checked 2026-10-22): "The chutes network is now TEE-exclusive"; GPU workers must be "Intel TDX confidential VMs"; "ALL servers must be bare metal/VM, meaning it will not work on Runpod, Vast, etc."; IPs "unique, static, and provide a 1:1 port mapping"; "as much RAM (or very close to it) per GPU as VRAM"; a non-GPU control server "4 cores, 32gb ram minimum"; "The entirety of the chutes miner must run within a kubernetes" (k3s recommended); GPUs "from very cheap (a10, a5000, t4, etc.) to very powerful (8x h100 nodes)"; "Incentives are based on total compute time" plus bounties; "Incentives/weights are calculated from 7 day sum of compute"; register with btcli on netuid 64; "Never register more than one UID". No earnings figure. [chutes-miner](https://github.com/rayonlabs/chutes-miner)
- Chutes public site: "Powering Trillions of Tokens per Month"; per-model prices such as DeepSeek V3.2 $1.00 in / $1.00 out per M tokens, Kimi K3 $1.85 / $9.50. No GPU or miner counts. [chutes.ai](https://chutes.ai/)
- Targon miner docs (checked 2026-10-22): GPU profiles Intel TDX: H100 SXM, H200, B200, B300, RTX PRO 6000 Blackwell; AMD SEV-SNP: B300, RTX PRO 6000; "exactly 8 GPUs of the listed SKU"; "The TEE must be enabled in BIOS for the installer to proceed"; installer wipes eligible disks; "Miner emissions are paid per card based on each auction's target price"; "Emissions not allocated to auctions are burned"; example auction: H200 target_cards 96, target_price 290, max_price 350; B200 target_cards 16, target_price 420, max_price 650 (USD cents per hour per card); min_stake 1000 alpha for validators; live data at tower.targon.com/api/v2/auctions. [Targon miner.md](https://github.com/manifold-inc/targon/blob/main/docs/miner/miner.md)
- Targon live auction API returned HTTP 502 on two attempts on 2026-10-22. [tower.targon.com](https://tower.targon.com/api/v2/auctions)
- lium.io (SN51) provider page, checked 2026-10-22: "An NVIDIA GPU, RTX 30, 40 or 50 series up to H100, H200, B200 and B300; one model per node"; Ubuntu 24.04, Docker, Sysbox, public IP, 100 Mbit/s, ports 8080 and 2200; providers keep "95% of every rental"; paid daily at 17:00 UTC; payout in USDT on Ethereum (minimum $5, 5% conversion fee) or Subnet 51 alpha; idle pay every tempo (about 72 minutes). Measured 30 days to 2026-10-22, averaged across all providers: RTX 4090 $315 per GPU-month at $0.45/hr average rental; RTX 5090 $414 per GPU-month at $0.57/hr; H100 80GB HBM3 $1,292 per GPU-month at $1.93/hr; an 8-GPU H100 server earned $10,333 per month. [lium.io provider page](https://lium.io/rent-out-your-gpu)
- lium.io marketplace: 8x H100 Helsinki SPOT $16/hour ($2/GPU), 8x H100 Dallas $30/hour ($3.75/GPU), B200 1x $6/hour, 8x B300 $55 to $80/hour. "Spot nodes are cheaper but a provider can reclaim them." [lium.io](https://lium.io/)
- SN56 Gradients (G.O.D README): tournaments with minimum miners 5 (Environment, paused), 4 (Text), 4 (Image); participation fees 0.6 TAO, 0.7 TAO, 0.4 TAO; "trainers run those repositories on validator-controlled GPU infrastructure". [G.O.D](https://github.com/rayonlabs/G.O.D)
- SN3: "Subnet 3 is now running Crusades", an MFU optimization competition; Templar is dormant. [templar README](https://github.com/one-covenant/templar)
- SN9 iota miner hardware: "Cuda GPU with >= 16GB VRAM (RTX 4090, for example)", Ubuntu 22.04; "token incentivized"; no earnings figure. [macrocosm-os/iota](https://github.com/macrocosm-os/iota)
- SN110 Green Compute: "Bittensor Subnet 110"; RTX 4090 (24 GB) and RTX 5090 (32 GB) nodes; requires proof of clean power (biogas, solar, hydro, wind, geothermal) and location proofs; "Payouts every epoch, no proof no payout"; "Includes 1.5x Green Multiplier"; calculator example 5.7 tau per month for a 2x RTX 4090 profile. [green-compute.com](https://www.green-compute.com/)
- SN90 KubeTEE: miner onboarding listed as "Coming"; nodes "confidential-computing capable". [kubetee.ai](https://kubetee.ai/)
- Bittensor emission share is determined by net TAO staking inflows under TaoFlow; subnets with negative flows receive zero emissions. Daily issuance about 3,600 TAO after the December 2025 halving. [search summary, Tokenomist and others](https://tokenomist.ai/research/bittensor-and-subnets-how-the-emission-engine-works)

### Inferences
- Alpha emission rate (estimate, derived): taostats "Emissions / Day" equals 7,200 x alpha price for every subnet checked (SN64: 7,200 x 0.067864 = 488.6; SN4: 7,200 x 0.052651 = 379.1; SN51: 7,200 x 0.112401 = 809.3; SN27: 7,200 x 0.002219 = 15.98). That matches 1 alpha per 12-second block, valued in TAO. So each subnet emits 7,200 alpha/day and miners get 41% = 2,952 alpha/day, which taostats shows as "Miner / Day" in TAO value.
- USD to miners per day (estimate = Miner/Day tau x $257.97): SN51 331.81 tau = $85,598; SN64 200.34 tau = $51,682; SN4 155.42 tau = $40,094; SN110 2,952 x 0.025348 = 74.83 tau = $19,304; SN9 69.98 tau = $18,053; SN3 67.17 tau = $17,328; SN56 44.21 tau = $11,405; SN27 $0.
- Per active miner (estimate, equal split, which is not how weights work): SN51 $85,598 / 74 = $1,157/day; SN64 $51,682 / 18 = $2,871/day; SN4 $40,094 / 5 = $8,019/day. Real splits follow compute share; the 18 Chutes miners and 5 Targon miners are multi-node operators.
- Targon per-GPU (estimate): the auction pays up to the target of 290 cents/hour per H200 card while the auction is below target cards, capped at 350 cents. An 8x H200 node therefore earns at most 8 x $2.90 x 24 = $556.80/day at target, or 8 x $3.50 x 24 = $672/day at cap, paid in SN4 alpha. The target_cards of 96 means about 12 such nodes fill the H200 auction; Targon has 5 active miners today. The miner doc says per-card rate "moves toward the target price" as more cards come online and unallocated emissions are burned.
- Lium is the only subnet with a published, measured per-GPU figure: $315/month on a 4090 is $10.50/day, 97% of the $0.45/hr x 24 x 30 = $324 that full-time rental would pay, so it likely includes idle pay or near-full utilization. Note that lium does not require TEE and accepts RTX 30/40/50 cards, so it is the only Bittensor path for consumer GPUs.
- Green Compute's calculator figure (5.7 tau/month for 2x 4090 = $1,470/month = about $24.50 per GPU-day at $257.97) is a marketing estimate, not measured; it also requires green-power attestation that a home miner in California cannot easily supply.
- Chutes USD per GPU per day cannot be computed because Chutes does not publish miner GPU counts (gap). Given 18 miners sharing $51.7k/day and a stated fleet from T4s to 8x H100 nodes, a new miner would need TDX-capable hosts (Sapphire Rapids or newer) plus H100/H200-class cards to earn a compute share.

### Gaps
- Live Targon auction (current cards online, current price): API returned 502 twice.
- Chutes: no public count of GPUs or per-GPU payout; chutes.ai shows no network stats.
- Per-subnet registration burn today: taostats shows "Reg Cost 0.00" for SN64 and SN4 and 0.50 tau for SN51; I could not confirm whether 0.00 means free or unloaded.
- Miner counts for SN9, SN56, SN110, SN3 were not fetched.
- The Bittensor emission docs page returned 404 (docs.learnbittensor.org redirect to bittensor.com/docs), so the 1-alpha-per-block derivation rests on taostats arithmetic rather than a primary doc.

## Key question 4: DePIN compute providers: what do they pay per GPU today?

### Takeaway
Marketplaces with real rental demand (Akash, lium, Nosana, io.net hire) price a 4090 at $0.25 to $0.45/hr and an H100 at $1.19 to $2.73/hr; token block rewards on top are small (io.net about $2.17/day for a 4090, $17/day for an H100, estimate) and concentrated among a few suppliers. Aethir, Gonka and Targon only take enterprise bare metal. Spheron Fizz, Gensyn mainnet, Lilypad mainnet, Cuckoo, Hyperspace and Heurist mining do not exist as paying GPU programs today.

### Cited Findings
- Akash GPU pricing (per GPU-hour, from recent provider bids, checked 2026-10-22): B300 $6.00 (fixed), B200 $5.00 (fixed), RTX Pro 6000 WE $1.44, Pro 6000 SE $2.02, A100 80GB $1.67, H100 80GB SXM5 $2.73, V100 32GB $0.21, RTX 5090 $0.57, RTX 3090 $0.15, RTX 4090 $0.34, A10g $0.18, RTX 4080 $0.15, T4 $0.16, RTX 3060 $0.08. [Akash GPU pricing](https://akash.network/pricing/gpus/)
- Akash provider calculator default, checked 2026-10-22: 1x H100 at $2.73/hr and 100% utilization = $1,994.00/month for the GPU, $2,281/month total with CPU, memory, storage and IPs (about 3,243 AKT at $0.703). "Estimates only, before operating costs. Actual earnings depend on the leases you win and your uptime." [Akash provider calculator](https://akash.network/pricing/provider-calculator/)
- Akash network stats page did not render ("Loading..."). [stats.akash.network](https://stats.akash.network/)
- io.net block rewards (explorer, checked 2026-10-22): "Epoch rewards emission: 10,204.41" IO per closed 3-hour epoch (every epoch listed from 2026-10-21-00 through 2026-10-22-12); "Nominated" 1,300 to 1,321 devices per epoch; "Today's Coins Distributed 51,022.071"; "Total Coins Distributed 12,127,911.114"; "Total Unique Suppliers Paid 8"; "Today's Unique Suppliers Paid 8"; device-class share of the 12.1M IO total: GeForce RTX 4090 37.3% (105 devices, 4 suppliers), H100 80GB HBM3 32.5% (95 devices, 5 suppliers), RTX A6000 6.1%, L40 4.7%, RTX PRO 6000 4.6%, RTX 6000 Ada 4.4%, Others 10.3%. Banner: "Co-staking is being discontinued." [io.net block rewards](https://explorer.io.net/explorer/epoch-rewards)
- io.net explorer home, checked 2026-10-22: 1,313 "Total Cluster Ready and Fully Collateralized GPUs/CPUs", Hired 1,301, Idle 12; top nodes H100 80GB HBM3 640, GeForce RTX 4090 616, B300 8, GAUDI2 8, L40S 8; hire prices: RTX 4090 Ray $0.25/hr, Container $0.30/hr, Baremetal $0.37/hr, VM $0.30/hr; H100 80GB HBM3 Ray $1.19, Container $2.09, Baremetal $1.79, VM $1.99; H100 PCIe $0.89 to $1.59; B300 $4.48 to $6.73. [io.net explorer](https://explorer.io.net/)
- io.net staking: base "$IO 200" per card; "minimum_stake_required = base_requirement_per_card * max(1, earning_multiplier)"; examples 8 H100 at multiplier 10 = 16,000 IO, 4 RTX 4070 = 800 IO; 14-day unstake cooldown; slashing for spoofing or inadequate service. Multipliers (current to new, June 2025 doc): RTX 4090 0.75 to 1.25 (Enterprise Pool), RTX 3090 0.5 to 1.75 (Community), H100 10 to 10, H200 15 to 12; Community Pool 5% of block rewards, Enterprise Pool 95%. Block rewards page: 95% to GPUs, 5% to CPUs; eligibility needs green uptime for the past 5 hours, minimum stake, a Solana wallet, hardware multiplier and connectivity tier above 0. Onboarding: 12 GB RAM, 256 GB SSD, "Windows: NVIDIA GeForce RTX 30xx and above series", 100/75 Mb/s, 12-hour readiness wait, proof-of-work check. Supported list includes GeForce RTX 4090, RTX 5090, RTX 3090, H100 80GB HBM3, H100 PCIe, H200. VM or cloud rules: not stated. [io staking](https://io.net/docs/guides/staking/io-staking.md); [multiplier page](https://io.net/docs/guides/block-rewards/proposed-device-block-reward-multiplier); [block rewards](https://io.net/docs/guides/block-rewards/block-rewards.md); [onboarding](https://io.net/docs/guides/workers/device-onboarding.md); [supported devices](https://io.net/docs/guides/workers/supported-devices.md)
- Aethir Cloud Host staking parameters (checked 2026-10-22): staking coefficient 267.258716936387 (updated December 22nd, 2025, recalculated weekly); ATH staking requirement per spec: GeForce RTX 4090 (BM-L3) 6,324 ATH; H100 (BM-L5) 45,095 ATH; H100x8 (BM-L17) 360,763 ATH; B200x8 368,384 ATH; A10 2,772 ATH. Rewards: PoC and PoD "even 50/50 split"; "5% protocol fee"; vesting "30% of the rewards are released immediately, 30% after 90 days, and the remaining 40% after 180 days"; distributed daily 00:00 UTC. Requirements: bare metal, enterprise-grade GPUs meeting benchmarks, same model per server, 99% monthly uptime, under 30 minutes daily offline, public IP, SSH, no GPUs sourced from China or sanctioned regions. No per-GPU reward figure published. [staking parameters](https://docs.aethir.com/aethir-cloud/aethir-cloud-host/operational-requirements-for-cloud-hosts/staking-as-cloud-host/staking-parameters); [rewards](https://docs.aethir.com/aethir-cloud/aethir-cloud-host/rewards-and-service-fees-for-cloud-hosts/rewards-for-cloud-host); [requirements](https://docs.aethir.com/aethir-cloud/aethir-cloud-host/operational-requirements-for-cloud-hosts)
- Render node operators: CUDA GPU compute capability 3.0+, driver 566.36+, "At least 6GB" VRAM (8+ preferred), "32+ GB System Memory", 100 GB free disk, onboarding via interest form and queue; Tier 2 nodes need 32 GB minimum VRAM for 50-series. Paid in RENDER. No earnings figure. [Render getting started](https://know.rendernetwork.com/general-render-network/what-role-am-i/how-to-get-started-1.md); [Render docs index](https://know.rendernetwork.com/llms.txt)
- Nosana markets (explore.nosana.com, checked 2026-10-22): "10 / 1012 hosts available"; NVIDIA 4090 $0.400/h, 0 / 90 hosts free, 5 deployments queued; 5090 $0.500/h, 0 / 39 hosts; 3090 $0.192/h, 6 / 37 hosts; H100 $1.500/h, 0 / 0 hosts, 8 deployments queued; A100 80GB $0.900/h; Pro 6000 (SOC2) $1.000/h; Pro 6000 Server (CC) $1.100/h; 3080 $0.096/h; 5080 $0.200/h. Host requirements: native Linux (Ubuntu 20.04+), 12 GB RAM, 256 GB NVMe, 100/50 Mb/s, "1 private key per GPU, 1 GPU per PC", NVIDIA RTX 30/40/50, A-series, A100/H100. Earnings in NOS at host.nosana.com. Staking amount and fee: not stated on fetched pages. [Nosana markets](https://explore.nosana.com/markets); [Nosana host guide](https://learn.nosana.com/hosts/grid.html)
- Clore marketplace, checked 2026-10-22: "1266 servers"; 4x RTX 4090 at 3.50 USD/hour (Ukraine, reliability 46.3%); 4x RTX 5090 at 4.38 USD/hour (Ukraine, reliability 50.0%); 1x RTX 5080 0.48 USD/hour; "Hold CLORE tokens for up to -50% marketplace fees"; pay per minute in BTC or CLORE. Host fee schedule: not found. [Clore marketplace](https://clore.ai/marketplace)
- Spheron Fizz Node: "We're phasing out Fizz Node" and "will no longer be maintaining it." Spheron now rents H100/A100/B200/B300 from $0.72/hour. [Fizz sunset](https://fizz.spheron.network/); [Spheron docs](https://docs.spheron.ai/)
- Golem stats, checked 2026-10-22: Network earnings 24h 694.27 GLM, 7d 5,224.05 GLM, total 324,199.61 GLM; 587 providers online (CPU runtime), 7,943 cores; 136 providers computing right now, 7-day peak 244. GPU provider docs page returned 404. [Golem stats](https://stats.golem.network/)
- Lilypad: RP-Beta runs "on Testnet"; rewards in Lilybits; "Currently, a RTX 4090 earns approximately 2,200 Lilybits per day (as of March 2025)". [Lilypad blog](https://blog.lilypad.tech/resource-provider-beta-program)
- Gensyn docs: testnet products "ran on the Gensyn Testnet and are no longer actively maintained"; "No official swarms are running at this time". No token rewards mentioned. [Gensyn docs](https://docs.gensyn.ai/)
- Hyperspace (hyper.space): landing page reads "where agents work" with no node, hardware or reward content. [hyper.space](https://hyper.space/)
- Inference.net (formerly Kuzco): site and docs describe renting B200 at $9.98/hr and deploying models; no worker or GPU-supply program found. [inference.net](https://inference.net/); [docs](https://docs.inference.net/)
- Gonka: mainnet ("gonka-mainnet"); "Host models, serve inference, and earn GNK"; each MLNode needs "at least 320 GB total GPU VRAM" (example 4x H100 or 2x H200), at least 2 ML Nodes per model, 16-core network node; without collateral a host "receives only the base weight (20% by default)"; PoC roughly every 24 hours; no earnings figure. [gonka.ai](https://gonka.ai/); [hardware](https://gonka.ai/docs/host/hardware-specifications/); [quickstart](https://gonka.ai/docs/host/quickstart/)
- Exabits: sells "GB200s, H100s, H200s and RTX5090s"; no supplier program on landing page. [exabits.ai](https://www.exabits.ai/)
- Cuckoo Network: cuckoo.network now 301-redirects to bex.co. [cuckoo.network](https://cuckoo.network/)
- Heurist: site and docs describe Heurist Mesh agents and a ZK L2; no GPU mining program content found. [heurist.ai](https://www.heurist.ai/); [docs](https://docs.heurist.ai/)
- Ritual: landing page has no node or GPU supply program. [ritual.net](https://ritual.net/)
- Morpheus (mor.org) and Cudos (cudos.org) returned HTTP 429 on all attempts.

### Inferences
- io.net block reward per GPU (estimate): daily emission = 10,204.41 x 8 epochs = 81,635 IO = $12,645/day at $0.1549. Weighting the 1,313 collateralized GPUs by current multipliers (616 x 1.25 for 4090 = 770; 640 x 10 for H100 = 6,400; about 57 others x 2 = 114; total about 7,284 units) gives 11.2 IO per unit per day. RTX 4090: 1.25 x 11.2 = 14.0 IO = $2.17/day. H100: 10 x 11.2 = 112 IO = $17.36/day. A cross-check using the historical class share (37.3% to 4090s) gives 30,450 IO/day across 616 cards = 49 IO = $7.66/day, so the 4090 figure sits somewhere between $2 and $8/day. Only 8 suppliers were paid today, so a new entrant has no demonstrated path to that share.
- io.net hire income (estimate, 100% hired, before any io.net fee): 4090 at $0.30/hr = $7.20/day; H100 at $1.79 bare metal = $42.96/day. Stake needed: 4090 250 IO = $38.73; H100 2,000 IO = $309.80; H200 2,400 IO = $371.76.
- Nosana at 100% hired (estimate, before any fee): 4090 $9.60/day; 5090 $12.00/day; 3090 $4.61/day; H100 $36.00/day. Zero of 90 4090 hosts free and 5 jobs queued shows demand currently exceeds supply for that card.
- Akash at 100% utilization (estimate, before take rate, which was not found): 4090 $8.16/day; 5090 $13.68/day; H100 $65.52/day. Utilization is unknown because the stats page did not load.
- Aethir stake in USD (estimate at $0.005798): RTX 4090 $36.67; H100 $261.46; H100x8 $2,091.70. Reward per GPU is unpublished and 70% of it vests over 180 days.
- Clore listings show 4090s asking $0.875/GPU-hour and 5090s $1.095/GPU-hour, but 43 to 50% reliability scores and unknown utilization make a per-day figure impossible.

### Gaps
- Akash take rate and provider utilization: not found on fetched pages.
- io.net: no official per-device block reward formula or published multiplier for the 5090; no rule on VMs or cloud hosts.
- Nosana staking amount and marketplace fee: not on fetched docs pages.
- Aethir: no per-GPU reward amount; compute-rewards tokenomics page gives no numbers.
- Render: no earnings data anywhere in fetched docs.
- Fluence: not fetched. Morpheus, Cudos: rate-limited. Golem GPU runtime: docs 404.

## Key question 5: Salad measured host earnings, and does it exclude rented GPUs?

### Takeaway
Salad's own measured table for Oct 15 to 21, 2026 shows an RTX 4090 averaging $0.289/hr ($6.94/day) and an RTX 5090 $0.279/hr ($6.70/day); the Chefs terms forbid VMs, emulators and any computer you do not own or control, which excludes rented datacenter GPUs.

### Cited Findings
- Salad earning rates, "Oct 15–21, 2026", "Updated 7 h ago" (checked 2026-10-22): RTX 4090 average $0.289/hr, most machines $0.285 to $0.302/hr, top chefs $0.481/hr, has a job running 97% of the time; RTX 5090 $0.279/hr average, $0.261 to $0.311, top $0.413, 97%; RTX 5080 $0.154; RTX 4080 $0.131; RTX 3090 Ti $0.102; RTX 3090 $0.081 ($0.076 to $0.091, top $0.150, 94%); RTX 3080 $0.082; RTX 3060 $0.036. "Includes container jobs, bandwidth sharing and mining." Based on single-GPU machines that averaged four hours a day or more; "Machines with two or more cards are counted separately." Recommends 32 GB RAM and 500 GB free storage for top-chef numbers. [Salad earning rates](https://salad.com/earning-rates/)
- Salad system requirements: "Windows 10 or 11, 64-bit"; NVIDIA RTX 3060 or later for best access; 12 GB RAM and 4 cores recommended; stable broadband. [Salad download page](https://salad.com/download-high-end)
- Salad Chefs terms (Sept 28, 2026): app uses "your personal computer or laptop"; may not "run the App on a virtual machine or emulator" or "on any computer you do not own or control, without the Company's written permission"; "Reward Points have no cash value"; redemption via PayPal, prepaid cards, gift cards; points appear within five business days; may expire after twelve months with no earning. [Salad Chefs terms](https://salad.com/terms/chefs/)
- Salad charges renters RTX 4090 High priority $0.330/hr and Lowest $0.160/hr; RTX 5090 High $0.500/hr, Lowest $0.250/hr, as of 12 Sep 2026 (third-party summary of Salad's September price change). [Spheron blog](https://www.spheron.network/blog/saladcloud-pricing-2026-gpu-cost-vs-spheron/)

### Inferences
- Daily gross (estimate): 4090 $0.289 x 24 = $6.94; 5090 $0.279 x 24 = $6.70; 3090 $0.081 x 24 = $1.94. Net at $0.30/kWh assuming about 300 W average draw on a 4090 (7.2 kWh = $2.16): $4.78/day; at $0.10/kWh ($0.72): $6.22/day. For the 5090 assuming 400 W (9.6 kWh = $2.88 at $0.30): $3.82/day. Power draw under Salad workloads is my assumption, not measured.
- Salad's 4090 host rate ($0.289/hr) is 88% of what it charges renters at High priority ($0.330/hr), so the platform is passing most of the rental price through; the ceiling is the renter price.
- Rented datacenter GPUs are excluded three ways: Windows-only, no VMs, and the "own or control" clause.

### Gaps
- Salad does not publish average power draw, so net-of-power figures rest on my wattage assumptions.

## Key question 6: Other token-paid "do something with a GPU" networks

### Takeaway
Livepeer is the only one of this group with live, public earnings data, and it is small: $6,319 in fees across the whole network in 7 days plus LPT inflation that mostly flows to delegators. Flux ended GPU mining, Grass is bandwidth only, Theta Elite Edge needs a 10,000 to 500,000 TFUEL stake with no published yield, and Nillion, Vana and Cudos have no GPU-paying role I could find.

### Cited Findings
- Livepeer explorer, checked 2026-10-22: "Fees Paid (7d) $6,319"; Orchestrators 100; Delegators 2,335; inflation rate 0.04985%; round #4379 rewards "26,008 / 29,069 LPT"; total supply 58.34M LPT; top orchestrators by forecasted yield about 39.5% (LPT plus ETH, on 150 LPT delegation); trailing 90-day fees per orchestrator mostly 0.01 to 1.02 ETH, with fastagents.eth at 13.7 ETH. [Livepeer explorer](https://explorer.livepeer.org/)
- Livepeer orchestrator tutorial: NVIDIA GPU with NVENC, "GTX 1060+ for transcoding"; Linux recommended; port 8935; active set requires total stake "in the top 100"; suggested Reward Cut 10 (orchestrator keeps 10% of LPT inflation, delegators 90%) and Fee Cut 95 (orchestrator keeps 95% of ETH fees); a missed reward call forfeits that round's LPT; at least 0.05 ETH on Arbitrum for gas. No earnings figure. [Livepeer tutorial](https://docs.livepeer.org/network/tutorials/run-your-first-orchestrator)
- Theta Elite Edge Node: "a minimum of 10,000 TFuel and maximum of 500,000 TFuel that can be staked to each Edge Node"; about 60-hour unstaking; rewards work like Guardian Node staking; no yield figure. [Theta docs](https://docs.thetatoken.org/docs/elite-edge-node-staking-process.md)
- Flux: GPU mining eliminated by soft fork; PoUW v2; Nimbus tier collateral 12,500 FLUX with 4 cores, 32 GB RAM, 440 GB SSD; from block 3,071,200 (late October 2026) "every block pays 12.6 FLUX" split 8.1 Stratus, 3.15 Nimbus, 0.9 Cumulus, 0.45 Foundation; reward drops 10% every 1,051,200 blocks; 6,623 nodes as of May 2026. [runonflux.com/fluxnodes](https://runonflux.com/fluxnodes); [runonflux.com](https://runonflux.com/)
- Grass: "Grass only uses bandwidth you are not using"; rewards in Grass Points, possibly Grass Tokens or USDC; no GPU involvement; no earnings stated. [grass.io](https://www.grass.io/)
- Nillion docs homepage: Blacklight L1 and Blind Computer; no node hardware, GPU or reward content found. [Nillion docs](https://docs.nillion.com/)
- OctaSpace: "Total nodes: 657"; supports Nvidia, Intel, AMD and CPU-only nodes; no earnings figure. OCTA Ethash on a 4090 shows $0.06/day revenue, -$0.54 profit on hashrate.no. [octa.space](https://octa.space/); [hashrate.no 4090](https://www.hashrate.no/gpus/4090)
- Vana docs: "Bring your own compute" is marked "(future)"; pooled confidential compute is a roadmap item; no GPU provider role. [Vana docs](https://docs.vana.org/)
- Golem: see Key question 4 (694.27 GLM/day network-wide, CPU runtime only).
- Cudos: cudos.org returned HTTP 429 twice.

### Inferences
- Livepeer fee income per orchestrator (estimate): $6,319 / 7 days / 100 orchestrators = $9.03/day average, and the distribution is skewed to a few AI-focused orchestrators. LPT inflation of 26,008 LPT/round x $1.57 = $40,833/day network-wide, but it is split by stake, so a new orchestrator with little LPT receives almost none, and entry requires enough stake to rank in the top 100.
- None of the networks in this section pays a GPU-day rate competitive with Salad or lium.

### Gaps
- Livepeer active-set stake threshold: not fetched.
- Theta Edge Node yield and GPU requirement: not found.
- Cudos and Morpheus status: rate-limited.

## Key question 7: Tax note

### Takeaway
Mined and staked tokens are ordinary income at fair market value when received, so they add to taxable income rather than offsetting W-2 wages; only subsequent price moves are capital gains or losses.

### Cited Findings
- IRS Notice 2014-21, Q-8/A-8: when a taxpayer successfully "mines" virtual currency, "the fair market value of the virtual currency as of the date of receipt is includible in gross income." Q-9/A-9: if mining "constitutes a trade or business" and the taxpayer is not an employee, net earnings "constitute self-employment income and are subject to the self-employment tax." [IRB 2014-16](https://www.irs.gov/irb/2014-16_IRB)
- Rev. Rul. 2023-14: for a cash-method taxpayer staking on a proof-of-stake chain, "the fair market value of the validation rewards received is included in the taxpayer's gross income" "in the taxable year in which the taxpayer gains dominion and control over the validation rewards," valued at that date and time. [IRB 2023-33](https://www.irs.gov/irb/2023-33_IRB)
- IRS virtual currency FAQ Q9: receiving virtual currency "in exchange for performing services, whether or not you perform the services as an employee," is ordinary income; Q12: "The amount of income you must recognize is the fair market value of the virtual currency, in U.S. dollars, when received." [IRS FAQ](https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-virtual-currency-transactions)

### Inferences
- Bittensor alpha, IO, NOS, ATH, GLM and Salad reward points received for compute are income at receipt under the services and mining rules above; a later drop in the alpha price before sale is a capital loss, not a reduction of that income.

### Gaps
- None material; the rulings are primary sources.

## Key question 8: Is any token-paid GPU activity profitable today on rented GPUs at market rental rates?

### Takeaway
Only at the very bottom of the rental market, and only by a dollar or two per GPU-day: a 4090 rented at $0.34/hr can clear about $1.68/day mining Pearl or about $2.34/day re-rented through lium, both before fees and risk. At $0.89/hr every option loses $10 or more per day, and the H100 and 8x H200 cases lose at every rental price. Most networks also refuse rented pods.

### Cited Findings
- See rental benchmarks above (Akash $0.34 and $0.57, RunPod $0.89, $1.19, $2.89 to $3.99, $5.29; lium $1.93 to $2.00) and revenue figures in Key questions 1, 3, 4 and 5.

### Inferences
Per GPU-day arithmetic (all estimates; revenue minus rental; no electricity because the renter does not pay it):

| GPU | Activity | Revenue/day | Rental/day (low / high) | Net/day (low / high) | Allowed on rented pods? |
|---|---|---|---|---|---|
| RTX 4090 | Mine Pearl (WhatToMine) | $9.84 | $8.16 / $21.36 | +$1.68 / -$11.52 | Not at Lambda, Nebius, Voltage Park, TensorDock, Vast (card accounts); no clause at RunPod, Crusoe, Hyperbolic |
| RTX 4090 | lium.io re-rent (measured $315/mo) | $10.50 | $8.16 / $21.36 | +$2.34 / -$10.86 | Needs Ubuntu 24.04 root + Sysbox; a container pod cannot run it, a rented VM might |
| RTX 4090 | Nosana (100% hired) | $9.60 | $8.16 / $21.36 | +$1.44 / -$11.76 | Needs native Linux, 1 GPU per PC; 0/90 hosts free today |
| RTX 4090 | io.net block reward + hire | $2.17 + $7.20 = $9.37 | $8.16 / $21.36 | +$1.21 / -$11.99 | Requires 250 IO stake; 8 suppliers paid today |
| RTX 4090 | Salad | $6.94 | $8.16 / $21.36 | -$1.22 / -$14.42 | No: VM and ownership clauses |
| RTX 5090 | Mine Pearl | $11.75 | $13.68 / $28.56 | -$1.93 / -$16.81 | as above |
| RTX 5090 | lium.io ($414/mo) | $13.80 | $13.68 / $28.56 | +$0.12 / -$14.76 | as above |
| RTX 5090 | Nosana (100% hired) | $12.00 | $13.68 / $28.56 | -$1.68 / -$16.56 | as above |
| H100 | Mine | not found (assume at most 5090-class $11.75) | $46.32 / $95.76 | -$34.57 / -$84.01 | n/a |
| H100 | lium.io ($1,292/mo) | $43.07 | $46.32 / $95.76 | -$3.25 / -$52.69 | VM needed |
| H100 | Akash provider (100% util) | $65.52 | $46.32 / $95.76 | +$19.20 / -$30.24 before take rate; circular (renting Akash supply to resell on Akash) | needs k8s on a VM |
| H100 | io.net block reward + hire | $17.36 + $42.96 = $60.32 | $46.32 / $95.76 | +$14.00 / -$35.44 | 2,000 IO stake; unverified share |
| 8x H200 | Targon auction (cap) | $556.80 to $672 | $1,015.68 (RunPod $5.29/hr) | -$458.88 to -$343.68 | No: TEE in BIOS, TargonOS wipes disks |
| 8x H200 | Chutes | not computable | $1,015.68 | n/a | No: "will not work on Runpod, Vast, etc." |

- The only positive cells are at the Akash floor price, which is itself a DePIN marketplace price, so "renting at $0.34 to resell at $0.45" is an arbitrage between two thin marketplaces, not a mining margin. Any fee (lium keeps 5%, Nosana and io.net fees unknown) or a few hours of downtime erases it.
- At the rental rates the owner quoted as typical (4090 $0.69 to $0.89, 5090 $0.99 to $1.19, H100 $2 to $4) every token-paid activity loses money.

### Gaps
- Real utilization on Akash, Nosana and io.net hire is unknown; the 100% figures are ceilings.

## Key question 9: Is any of it profitable on owned GPUs at $0.30/kWh (California) or $0.08 to $0.12 (colo)?

### Takeaway
Yes, modestly: an owned 4090 nets roughly $5 to $8 per day and a 5090 roughly $8 to $10 per day at California power, and about $1 more per day at colo rates. An owned H100 nets about $38 to $60 per day and an owned 8x H200 TEE node could net $500 to $625 per day on Targon if it wins auction share. The 4090 and 5090 figures are below what the same cards earn in plain rental ($0.45 to $0.89/hr).

### Cited Findings
- Power figures from WhatToMine (4090 400 W, 5090 520 W, 3090 320 W mining Pearl). H100 and H200 wattage are my assumptions (700 W per SXM card, about 6.5 kW for an 8x node with CPUs, fans and PSU loss).

### Inferences
Daily electricity (estimate): 4090 9.6 kWh = $2.88 at $0.30, $0.96 at $0.10, $0.77 at $0.08, $1.15 at $0.12; 5090 12.48 kWh = $3.74 / $1.25 / $1.00 / $1.50; 3090 7.68 kWh = $2.30 / $0.77; H100 16.8 kWh = $5.04 / $1.68; 8x H200 156 kWh = $46.80 / $15.60. Salad draws less than mining; I used 300 W (4090) and 400 W (5090).

| GPU (owned) | Activity | Gross/day | Net at $0.30/kWh | Net at $0.10/kWh | Notes |
|---|---|---|---|---|---|
| RTX 4090 | lium.io (measured) | $10.50 | $7.62 | $9.54 | paid USDT or alpha, 95% to provider |
| RTX 4090 | Nosana (100% hired) | $9.60 | $6.72 | $8.64 | fee unknown; 1 GPU per PC |
| RTX 4090 | Mine Pearl | $9.84 | $6.96 | $8.88 | single-exchange fresh coin |
| RTX 4090 | Salad (measured) | $6.94 | $4.78 | $6.22 | Windows PC, points not cash |
| RTX 4090 | Akash (100% util) | $8.16 | $5.28 | $7.20 | take rate unknown |
| RTX 4090 | io.net reward + hire | $9.37 | $6.49 | $8.41 | reward share unverified |
| RTX 5090 | lium.io (measured) | $13.80 | $10.06 | $12.55 | |
| RTX 5090 | Nosana (100% hired) | $12.00 | $8.26 | $10.75 | |
| RTX 5090 | Mine Pearl | $11.75 | $8.01 | $10.50 | unverified 5090 benchmark |
| RTX 5090 | Salad (measured) | $6.70 | $3.82 | $5.45 | |
| RTX 3090 | Mine Pearl | $4.13 | $1.83 | $3.36 | |
| RTX 3090 | Salad | $1.94 | $0.02 (at 256 W assumption) | $1.30 | |
| H100 | Akash (100% util) | $65.52 | $60.48 | $63.84 | before take rate |
| H100 | lium.io (measured) | $43.07 | $38.03 | $41.39 | |
| H100 | Nosana (100% hired) | $36.00 | $30.96 | $34.32 | 0 hosts, 8 jobs queued |
| H100 | io.net reward + hire | $60.32 | $55.28 | $58.64 | |
| 8x H200 | Targon auction target / cap | $556.80 / $672.00 | $510.00 / $625.20 | $541.20 / $656.40 | TEE bare metal, 5 miners today, alpha payout |
| 8x H200 | lium.io (H100 proxy $10,333/mo) | $344.43 | $297.63 | $328.83 | H200 not in lium's published table |

- Mining Pearl at $0.30/kWh keeps 71% of gross on a 4090 ($6.96 of $9.84), so California power is not the binding constraint; the binding constraint is that gross is only $10/day on a $1,600 to $2,000 card. Rental at the owner's own quoted $0.69 to $0.89/hr ($16.56 to $21.36/day) beats every token option for a 4090.
- For an owned H100, Akash at full utilization ($65.52/day) matches direct rental ($2.73/hr) because it is direct rental; the token element is only the payment rail.

### Gaps
- H100 and H200 power draw and node overhead are assumptions.
- No measured utilization for Akash, Nosana, io.net hire or Clore.

## Key question 10: Which networks pay enough to justify an 8x H100 or H200 node, and what is the projected net for Nov 1 to Dec 31, 2026 (61 days)?

### Takeaway
Only Targon (SN4) publishes a per-card rate that approaches cloud rental ($2.90 to $3.50 per H200-hour, alpha-denominated, TEE bare metal only); Chutes pays more in aggregate but requires TDX hosts and publishes no per-GPU rate; lium's measured 8x H100 figure is $10,333/month. On owned hardware a Targon 8x H200 node projects to roughly $31k to $38k net over 61 days at California power; on rented hardware every option loses.

### Cited Findings
- Targon auction example: H200 target 290 cents/hr, max 350, target_cards 96; B200 target 420, max 650, target_cards 16; "Emissions not allocated to auctions are burned". [Targon miner.md](https://github.com/manifold-inc/targon/blob/main/docs/miner/miner.md)
- Targon SN4 Miner/Day 155.42 tau; 5 active miners. [taostats SN4](https://taostats.io/subnets/4)
- Chutes SN64 Miner/Day 200.34 tau; 18 active miners; TDX-only. [taostats SN64](https://taostats.io/subnets/64); [chutes-miner](https://github.com/rayonlabs/chutes-miner)
- lium 8-GPU H100 server $10,333/month measured. [lium.io provider page](https://lium.io/rent-out-your-gpu)
- Gonka minimum about 8x H100 (2 MLNodes x 320 GB VRAM), GNK $0.1998, no published earnings. [gonka hardware](https://gonka.ai/docs/host/hardware-specifications/)
- Aethir H100x8 stake 360,763 ATH ($2,092 at $0.005798), earnings unpublished. [Aethir staking](https://docs.aethir.com/aethir-cloud/aethir-cloud-host/operational-requirements-for-cloud-hosts/staking-as-cloud-host/staking-parameters)

### Inferences
- Targon cap check (estimate): the whole SN4 miner pool is $40,094/day. At the $3.50/hr cap an 8x H200 node takes $672/day, so about 60 such nodes would exhaust the pool; the 96-card H200 target implies the auction is sized for about 12 nodes. With 5 active miners today the auction is likely under target, which is when the per-card rate is at or near the cap. All of this is paid in SN4 alpha (price 0.0527 tau, down 2.6% on the month) and must be sold into a pool holding 135.51K TAO.
- 61-day projection, 8x H200 (estimate): owned at $0.30/kWh, Targon $510.00 to $625.20/day x 61 = $31,110 to $38,137; at $0.10/kWh $541.20 to $656.40 x 61 = $33,013 to $40,040. Rented at RunPod $5.29/hr: -$458.88 to -$343.68/day x 61 = -$27,992 to -$20,964, and the node is ineligible anyway.
- 61-day projection, 8x H100 on lium (estimate): $344.43/day gross; owned CA $297.63 x 61 = $18,155; colo $328.83 x 61 = $20,059; rented at $2.00/hr spot ($384/day) -$39.57 x 61 = -$2,414.
- Chutes: cannot be projected per node (no per-GPU data). Gonka and Aethir: no earnings data, so no projection.

### Gaps
- Live Targon fill rate (API 502).
- Chutes GPU fleet size.
- H200 wattage assumption.

## Key question 11: Which of these are allowed on rented cloud GPUs?

### Takeaway
Classic PoW mining is contractually barred at Lambda, Nebius, Voltage Park, TensorDock and (for card-funded accounts) Vast.ai, and merely unaddressed at RunPod, Crusoe and Hyperbolic. The AI-mining and DePIN networks mostly exclude rented pods by their own hardware rules: Chutes (TDX bare metal, "will not work on Runpod, Vast"), Targon (BIOS TEE, disk wipe), Aethir (bare metal), Salad (no VM, must own), Nosana (native Linux, one GPU per PC). Lium, io.net, Akash and Render do not state a rented-hardware ban in the pages fetched, but each needs a root-level Linux host (Sysbox, Docker, Kubernetes), which a container pod cannot provide.

### Cited Findings
- See Key question 2 for verbatim clauses and sources.

### Inferences
- A rented bare-metal or VM instance (not a container pod) with root could technically run lium, io.net, Akash or Render clients, subject to the host's terms; a rented RunPod or Vast container cannot.

### Gaps
- No provider page states whether reselling rented capacity on another marketplace is permitted.

## Ranked: net USD per GPU-day today (checked 2026-10-22, estimates)

Owned hardware at $0.30/kWh (California), best measured or published option per card first:

| Rank | Option | 4090 | 5090 | H100 | 8x H200 node |
|---|---|---|---|---|---|
| 1 | Targon SN4 auction (TEE 8-GPU node only) | n/a | n/a | n/a | $510 to $625 |
| 2 | Akash provider at 100% utilization (take rate unknown) | $5.28 | $9.94 | $60.48 | not listed |
| 3 | io.net block reward + hire (reward share unverified) | $6.49 | not found (5090 multiplier unpublished) | $55.28 | not listed |
| 4 | lium.io SN51 (measured 30-day) | $7.62 | $10.06 | $38.03 | $297.63 (8x H100 proxy) |
| 5 | Nosana at 100% hired (fee unknown) | $6.72 | $8.26 | $30.96 | no H200 market |
| 6 | PoW mining Pearl (fresh coin, one exchange) | $6.96 | $8.01 | not found | not found |
| 7 | Salad (measured week, Windows PC only) | $4.78 | $3.82 | not eligible | not eligible |
| 8 | PoW mining best legacy coin (Conflux) | $0.39 at $0.10/kWh, negative at $0.30 | $0.70 at $0.10/kWh | not found | not found |
| 9 | Livepeer orchestrator (new, low stake) | about $0 to $9 per orchestrator, not per GPU | same | same | same |
| 10 | Aethir, Render, Gonka, Golem, Lilypad, Theta | no public per-GPU number | | | |
| 11 | Chutes SN64 | no per-GPU number; $51,682/day across 18 TDX miners | | | |
| 12 | SN27 Orion, Flux PoW, Clore PoW, Neoxa, Spheron Fizz, Gensyn, Cuckoo, Hyperspace | $0 (ended, burned or discontinued) | | | |

Rented hardware (revenue minus rental, no power), best case at the lowest rental seen and at the owner's typical rate:

| Option | 4090 at $0.34 / $0.89 | 5090 at $0.57 / $1.19 | H100 at $1.93 / $3.99 | 8x H200 at $5.29 |
|---|---|---|---|---|
| lium.io re-rent | +$2.34 / -$10.86 | +$0.12 / -$14.76 | -$3.25 / -$52.69 | n/a |
| Mine Pearl | +$1.68 / -$11.52 | -$1.93 / -$16.81 | not found | not found |
| Nosana (100% hired) | +$1.44 / -$11.76 | -$1.68 / -$16.56 | -$10.32 / -$59.76 | n/a |
| io.net reward + hire | +$1.21 / -$11.99 | not found | +$14.00 / -$35.44 | n/a |
| Salad | not allowed | not allowed | not allowed | not allowed |
| Targon | not allowed | not allowed | not allowed | -$459 to -$344 and not allowed |
| Chutes | not allowed | not allowed | not allowed | not allowed |

## Projected net, Nov 1 to Dec 31, 2026 (61 days; estimates; today's rates held flat; token prices held flat)

| Hardware | Rented, best case (lowest rental) | Rented at typical rental | Owned, $0.30/kWh, best option | Owned, $0.10/kWh, best option |
|---|---|---|---|---|
| 1x RTX 4090 | +$143 (lium at $0.34/hr: $2.34 x 61) or +$102 (Pearl: $1.68 x 61) | -$662 (lium at $0.89/hr: -$10.86 x 61) or -$703 (Pearl) | +$465 (lium: $7.62 x 61); Pearl +$425; Salad +$292 | +$582 (lium: $9.54 x 61); Pearl +$542 |
| 1x RTX 5090 | +$7 (lium at $0.57/hr: $0.12 x 61) | -$900 (lium at $1.19/hr: -$14.76 x 61) or -$1,025 (Pearl) | +$614 (lium: $10.06 x 61); Pearl +$489 | +$766 (lium: $12.55 x 61); Pearl +$641 |
| 1x H100 | -$198 (lium at $1.93/hr: -$3.25 x 61) | -$3,214 (lium at $3.99/hr: -$52.69 x 61) | +$3,689 (Akash at 100% util, before take rate: $60.48 x 61) or +$2,320 (lium measured: $38.03 x 61) | +$3,894 (Akash) or +$2,525 (lium) |
| 8x H200 node | not eligible; -$20,964 to -$27,992 if forced through RunPod at $5.29/hr | same | +$31,110 to +$38,137 (Targon at $2.90 to $3.50 per card-hour: $510.00 to $625.20 x 61); lium 8x H100 proxy +$18,155 | +$33,013 to +$40,040 (Targon); lium proxy +$20,059 |

Arithmetic basis: daily nets from the tables above multiplied by 61. The Targon figure assumes the H200 auction stays below its 96-card target so each card earns the target-to-cap rate, that the node wins allocation, and that SN4 alpha can be sold at today's 0.0527 tau; a 7.6% one-day TAO move (CoinGecko, 2026-10-22) shows the price risk. The lium figures are 30-day measured averages across all providers and include the 5% platform cut; the Pearl figures depend on a coin WhatToMine labels "Fresh coin, early version miners" with a $0 market cap entry and one exchange. Nothing here reduces W-2 income; every token received is ordinary income at receipt (Key question 7).

### Overall gaps
- WebSearch quota was exhausted after about 12 searches; everything after that came from direct URLs. Not fetched: Fluence, 2cryptocalc, SafeTrade (Pearl liquidity), Vast.ai live prices and host fee, Akash take rate and stats, Chutes fleet size, live Targon auction, Nosana fee and stake, Morpheus (429), Cudos (429), Golem GPU runtime (404), Lambda Platform Guidelines, RunPod host agreement.
