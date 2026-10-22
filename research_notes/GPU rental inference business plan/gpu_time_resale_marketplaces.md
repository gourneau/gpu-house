# GPU time resale marketplaces: host side, re-listing rented GPUs, and the rent-vs-resell spread

All numbers below were read live on 2026-10-22 unless a different date is stated next to the number. "Estimate" marks my own arithmetic or reasoning. "Not found" marks items I could not source. The WebSearch budget ran out near the end of this research, so a few gaps (listed in each section) could not be closed.

## Key question 1: Vast.ai host side (requirements, verification, fee, payouts, terms, live prices)

### Takeaway
Vast is open to anyone with a dedicated Ubuntu Server machine, a public IPv4, open ports and 500 Mbps, but the Standard Hosting Agreement makes the provider warrant that it is "the sole owner of the Hardware" and that the hardware "shall at all times be located at the Provider." Vast does not publish a host fee percentage; its own blog says renter-facing prices are "about 25% above what hosts earn." Live renter-facing medians today: H100 SXM $2.53, RTX 4090 $0.67, RTX 5090 $0.87 per GPU-hour.

### Cited Findings

**Live renter-facing prices on Vast (vast.ai/pricing, checked 2026-10-22, "Prices reflect currently available offers and update hourly")** — [Vast.ai Pricing](https://vast.ai/pricing)

| GPU | From (min) $/hr | Median $/hr |
|---|---|---|
| H100 SXM | $1.73 | $2.53 |
| H100 PCIE | $2.00 | $2.40 |
| H100 NVL | $2.32 | $3.00 |
| H200 | $4.34 | $4.71 |
| H200 NVL | $3.20 | $3.99 |
| B200 | $6.25 | $10.00 |
| A100 SXM4 80GB | $0.40 | $0.91 |
| A100 PCIE 80GB | $0.35 | $0.73 |
| L40S | $0.47 | $0.64 |
| RTX 4090 | $0.14 | $0.67 |
| RTX 5090 | $0.39 | $0.87 |
| RTX PRO 6000 WS | $1.00 | $1.60 |

- Host earnings calculator (vast.ai/hosting/calculator, checked 2026-10-22, two loads a few minutes apart) pre-fills the RTX 5090 listing price "from the current market median". Listed-market stats shown: first load Min $0.31, P10 $0.48, Median $0.69; second load Min $0.31, P10 $0.42, Median $0.65. It reported "476 RTX 5090 GPUs are currently listed and available to rent" on the first load and "443" on the second. — [Vast Host Earnings Calculator](https://vast.ai/hosting/calculator)
- Calculator output for 1x RTX 5090 at $0.65/hr: Conservative $251/mo at 42% util, Expected $386/mo at 65% util, Optimistic $456/mo at 77% util; breakdown GPU $304 + storage $79 + bandwidth $3. The page states: "Utilization varies with demand and your price — this is your assumption, not a marketplace measurement." and "Vast does not guarantee any level of utilization or earnings." — [Vast Host Earnings Calculator](https://vast.ai/hosting/calculator)
- Calculator fee wording: "Keep What You List. Your asking price is the basis for GPU earnings. Customer-facing prices may also reflect marketplace operations and support." and "Automatic Payouts... No minimum threshold to cash out." The FAQ titles "How does Vast pay hosts?", "How does customer-facing pricing work?", "Does storage revenue go through the platform fee?" exist, but their answer text is not in the rendered HTML (checked with JS rendering). — [Vast Host Earnings Calculator](https://vast.ai/hosting/calculator)
- Vast blog (May 18, 2026): "Consumer GPUs like the RTX 5090 typically earn $0.30-$0.60 per GPU-hour... A four-GPU 5090 rig running at 80% utilization can generate $700-$1,400 per month." "H100s and H200s bring in $2.15-$4.00+ per GPU-hour." "Live GPU prices are typically about 25% above what hosts earn." "Once you log in and register at least one machine with Vast.ai, your host dashboard will show detailed market stats with occupancy rates and more." — [How Much Money Can You Earn Renting Out Your GPU on Vast.ai?](https://vast.ai/article/how-much-money-can-you-earn-renting-out-your-gpu-on-vast-ai)
- Vast does not publish a numeric host fee anywhere I could read: not in the Terms of Use, the Hosting Agreement, the payout docs, the tax guide, the hosting page, or the calculator (all checked 2026-10-22). Third-party sites conflict: one review says Vast's lowest platform fee is "10–15%" ([GPUnex, Feb 7 2026](https://www.gpunex.com/blog/vast-ai-review-2026/), fee figure appeared only in search snippet, not in the fetched article), another says hosts keep "roughly 85%" ([MiningBoard](https://miningboard.com/rental-markets/vast-ai), via search snippet), and a comparison page claims "there is no fee or commission deducted from your earnings" ([getdeploying](https://getdeploying.com/hetzner-vs-vast-ai), via search snippet). None of these is primary.
- Market stats for hosts: "To get an understanding of prices, check our Market Stats page. You'll need to be signed in as a host with at least one registered machine to view it." — [Hosting Overview](https://docs.vast.ai/host/hosting-overview.md). The host-only dashboards show "Historical supply/demand counts and P10/median/P90 pricing over time" and "Current supply/demand counts, pricing, and stats for each GPU type"; CLI `vastai metrics gpu`, `gpu-trends`, `gpu-locations` return supply, demand and pricing; market data refreshes every 5 minutes. No public utilization percentage is published. — [GPU Market Metrics](https://docs.vast.ai/host/market-metrics.md)

**Hardware, OS, software and network requirements (verification baseline)** — [Verification Stages](https://docs.vast.ai/host/verification-stages.md)
- GPU: NVIDIA, Maxwell or newer, more than 7 GB VRAM per GPU, CUDA 11.8 or newer, all GPUs in a machine the same model, more than 2.85 GiB/s PCIe bandwidth per GPU.
- CPU: x86_64 or ARM64 with AVX, at least 2 physical cores per GPU. System RAM at least 95% of total GPU VRAM.
- Storage: SSD, a dedicated 200 GB drive for Docker storage, 20 GB free on root.
- Network: at least 500 Mbps download and 500 Mbps upload, wired Ethernet, "A public IPv4 address. CGNAT or shared ISP IPs are unsupported." At least 5 forwarded ports per GPU, 100 per GPU recommended.
- OS: "Ubuntu Server 22.04 LTS minimum, with 24.04 LTS recommended. Desktop editions aren't supported." Secure Boot disabled. SSH key-only. Currently supported NVIDIA driver.
- "Machines must be dedicated to hosting. Mining, gaming, personal jobs, or desktop use cause failure." Reliability score over 90%.
- Self-test: "Even with --ignore-requirements, your machine must have at least three direct open ports, otherwise, the self-test will fail." — [How to Self-Test](https://docs.vast.ai/host/how-to-self-test.md)
- Hosts are responsible for "installing Ubuntu, creating disk partitions, installing NVIDIA drivers, opening network ports on the router and installing the Vast hosting software." "Vast does not offer support for getting your machine working." "You must create a new account for hosting." — [Hosting Overview](https://docs.vast.ai/host/hosting-overview.md)
- IPMI: not mentioned anywhere in Vast host docs (not found). Static IP: "a static IP helps" (favored, not required). — [Understanding Verification](https://docs.vast.ai/host/understanding-verification.md)
- Verification is "fully automated"; criteria are reliability ("Sustained ≥99.99% (up to 99.9999%+) uptime is typically favored"), infrastructure (newer datacenter GPUs prioritized "B200 > H200 >> 5090 > 4070"; "8×5090 >> 2×5090 > 1×5090"), DLPerf, and supply/demand. "Enabling VM support significantly improves verification likelihood." — [Understanding Verification](https://docs.vast.ai/host/understanding-verification.md)
- Community guide (single host's log, not official): Ubuntu 22.04/24.04, NVIDIA Driver 535, Docker + NVIDIA runtime, NVIDIA Container Toolkit, port forwarding range 16384–32768. — [AG-Sec4 VastAI GPU Host Guide](https://github.com/AG-Sec4/VastAI-GPU-Host-Guide)

**What the Vast install script does (read via the public script URL)** — [Vast install script](https://s3.amazonaws.com/vast.ai/install)
- No hypervisor or bare-metal check: "It does not run systemd-detect-virt or dmidecode, and it has no hypervisor or bare-metal check." The only hardware test is an IOMMU check used to decide whether to install `qemu-kvm`, `libvirt-daemon-system` for VM support.
- It removes `docker`, `docker-engine`, `docker.io`, installs `nvidia-docker2`, edits `/etc/docker/daemon.json` (adds Vast registry mirrors, sets `native.cgroupdriver=cgroupfs` on 22.04), and moves `/var/lib/docker` onto a dedicated XFS partition with project quotas, creating the partition with `parted mkpart` or a loop file fallback.
- It creates a system user `vastai_kaalia` with `vastai_kaalia ALL=(ALL) NOPASSWD:ALL` in sudoers, blacklists nouveau, and can install the NVIDIA `.run` driver.
- So the daemon needs full root, control of the Docker daemon and the ability to repartition or create a loop file. It does not technically refuse to run inside a VM.

**VM support for hosts** — [VMs](https://docs.vast.ai/host/vms.md)
- "Vast now supports VM instances running on Kernel Virtual Machine (KVM) in addition to Docker container based instances. VM support is currently an optional feature for hosts." "You will require a CPU and a chipset that support Intel VT-d or AMD-Vi." Requires `intel_iommu=on`/`amd_iommu=on` kernel args and no display manager. "VMs cannot earn revenue from bandwidth."

**Datacenter (verified, blue label, Secure Cloud) status**
- Docs requirements: "ONE of the following third party certificates must be active: ISO/IEC 27001"; "The equipment must be owned by a business"; "The company must sign the Datacenter Hosting Agreement"; "The owner must undergo identity verification"; "at least 5 GPU servers listed on Vast.ai". Required documents include "A contract or invoice from the datacenter linking the business". — [Datacenter Status](https://docs.vast.ai/host/datacenter-status.md)
- Marketing page (conflicts on certification): "Run 40+ data center GPUs or 80+ consumer GPUs racked in an ISO-certified facility?"; "Minimum 5 GPU Servers"; "Equipment owned by a registered business. Owners must complete identity verification and sign the Data Center Hosting Agreement."; "Certifications like ISO 27001, SOC 2, or equivalent are encouraged and will strengthen your application, but are not strictly required." Applications reviewed "within 2 business days." — [Data Center Application](https://vast.ai/data-center-application)

**Host payouts** — [Host Payouts](https://docs.vast.ai/host/payment.md)
- "Vast.ai currently supports payouts through: Wise, PayPal, Stripe." "Direct bank transfers, ACH payments, wire transfers, and SWIFT payments are not available." Crypto: not offered (not listed).
- "Your account must accumulate at least $20 USD before an invoice can be generated." "Invoices are generated weekly on Fridays." "Invoices generated on Friday are generally scheduled to be paid on the following Friday." "It typically takes up to two weeks to receive your first payout." (This conflicts with the calculator's "No minimum threshold to cash out.")
- Hosting Agreement payment clause: "Vast.ai agrees to pay Provider in installments based on a weekly billing period, the payments set forth payable within 14 days of a completed billing period". "Vast.ai may withhold payments for: lost user data, excessive outages, extensive downtime or any other occurrences which result in harm to the Vast.ai brand." — [Standard Hosting Agreement](https://cloud.vast.ai/host/agreement)
- Tax guide: "As an independent contractor, you are solely responsible for tracking your earnings"; "Vast.ai does not automatically withhold taxes." — [Tax Guide for Hosts](https://docs.vast.ai/host/guide-to-taxes.md)

**Host terms (Standard Hosting Agreement, read 2026-10-22 at cloud.vast.ai/host/agreement; it "supersedes any and all other agreements, including Vast.ai's Terms of Use")** — [Standard Hosting Agreement](https://cloud.vast.ai/host/agreement)
- Recital: "WHEREAS, Provider is the owner of certain hardware".
- Representations: "Provider represents and warrants that: (i) it is the sole owner of the Hardware and Provider has the unrestricted right to lease the Hardware to Vast.ai as provided herein".
- Ownership: "The Hardware shall, at all times, be the sole and exclusive property of Provider. Vast.ai shall have no rights or property interest therein, except for the right to use the Hardware in the normal operation of its business".
- Location: "The Hardware shall at all times be located at the Provider and shall be used by Vast.ai in furtherance of Vast.ai's business."
- Software license: "Provider may not directly or indirectly, grant sublicenses, leases, or other rights under the License to third parties."
- Non-exclusive: "nothing in this Agreement shall in any way be deemed or construed to prohibit Provider from participating in similar business arrangements as those described herein."
- Subcontractors: "The use of subcontractors is permissible under this Agreement provided that: the subcontractor must agree to the same terms and conditions".
- Term: one week, auto-renewing weekly; either party may terminate at end of term; 30-day cure for material breach.
- Non-circumvention of Vast customers for one year after termination, with "$5,000.00 AS LIQUIDATED DAMAGES FOR EACH VIOLATION".
- Physical security: "Provider shall implement reasonable physical and environmental security around the Hardware to restrict unauthorized persons' physical access to the machine." Audit right: "Provider and its subcontractors shall provide the right of audit to its facilities to Vast.ai".
- Verification timing: "The Hardware specifications shall be verified by Vast.ai within two to three weeks of initial Provider onboarding."
- Docs restatement of host commitments: "the hardware can not be used for any other purposes"; "the advertised services must be provided until each rental contract's rental end date". — [Hosting Overview](https://docs.vast.ai/host/hosting-overview.md)
- Vast Terms of Use (Version Date: September 1, 2026) define "Rental by users of hosting services ('User') from independent providers ('Provider')" and state "All Providers are independent contractors". — [Vast Terms of Use](https://vast.ai/terms)

### Inferences
- Estimate: if renter-facing prices run "about 25% above what hosts earn", a host receives roughly 80% of the listed price (1/1.25). The calculator's listed-market RTX 5090 median ($0.65 to $0.69) versus the pricing page's renter-facing 5090 median ($0.87) gives a ratio of 1.26 to 1.34, consistent with that statement.
- Estimate: implied host take at today's medians: H100 SXM about $2.02/hr, RTX 4090 about $0.54/hr, RTX 5090 about $0.65 to $0.70/hr.
- The agreement's "sole owner" and "located at the Provider" clauses make a rented cloud instance a breach of warranty, regardless of whether the daemon runs.

### Gaps
- Vast's exact platform fee percentage: not published; FAQ answers on the hosting and calculator pages are JS-only and did not render.
- Vast does not publish marketplace utilization or occupancy numbers publicly; they are behind the host-only Market Stats login.
- No official statement on whether the host daemon is rejected inside a VM. The install script has no such check, but verification requirements (PCIe bandwidth, dedicated machine, open ports, VT-d for VM support) are the practical constraint.

## Key question 2: RunPod Community Cloud host program

### Takeaway
RunPod closed its Community Cloud host program to new hosts on Feb 24, 2026; existing hosts continue. RunPod does not publish host revenue share or host hardware terms, and its Pods are containers where "you cannot spin up your own Docker instance", so a RunPod Pod cannot run the Vast host daemon.

### Cited Findings
- Runpod blog "An update on the Community Cloud hosting application process" (Feb 24, 2026, original URL now redirects to the Clusters product page): the company "has decided to stop accepting new hosts for its Community Cloud"; driven by "the expansion of Runpod's Secure Cloud, which now provides the necessary GPU variety and availability"; "existing Community Cloud hosts can continue to operate as usual." — [Plushcap summary of Runpod blog, Feb 2026](https://www.plushcap.com/companies/runpod/blog/summaries/2026/2); original: [Runpod blog](https://www.runpod.io/blog/an-update-on-the-community-cloud-hosting-application-process)
- Runpod docs hosting page: "the hosting form is no longer active"; all hosts "are required to complete KYC (Know Your Customer) verification"; "Larger providers must complete a Provider Agreement and Service Level Agreement"; hosts "can also define a minimum bid price for spot rental" (search snippet; the page itself returned 404 to my fetchers). — [Runpod docs: hosting](https://docs.runpod.io/hosting)
- Runpod Terms of Service (Last Updated March 24, 2026): Section 4.2.1 "peer-to-peer GPU computing that connects individual compute providers"; "Runpod is only the venue to connect Hosts with consumers"; "Runpod has no responsibility for the actions of Hosts". Section 9 prohibits "Resell any credits purchased through the Service without the prior written consent of Runpod" and "Use the Service as part of any effort to compete with us." No clause on host hardware ownership or subleasing. — [Runpod Terms of Service](https://www.runpod.io/legal/terms-of-service)
- Pods: "Runpod runs Docker for you, so you cannot spin up your own Docker instance or use Docker Compose on Pods." — [Runpod Pods overview](https://docs.runpod.io/pods/overview)
- Runpod prices (runpod.io/pricing, checked 2026-10-22), Community / Secure per GPU-hour: H100 SXM $2.69 / $3.99; H100 PCIe $1.99 / $2.89; H100 NVL $2.59 / $3.19; H200 $3.59 / $5.29; B200 $5.98 / $7.99; A100 80GB PCIe $1.19 / $1.79; A100 80GB SXM $1.39 / $1.79; L40S $0.79 / $1.09; RTX 4090 $0.34 / $0.89; RTX 5090 $0.69 / $1.19; RTX PRO 6000 $1.69 / $2.49. — [Runpod Pricing](https://www.runpod.io/pricing)
- Host revenue share: a third-party comparison claims hosts keep "93% after the 7% fee" (unverified, not in any Runpod document I could read). — [MiningBoard Vast/Runpod/io.net comparison](https://miningboard.com/guides/vast-runpod-io-net-comparison)

### Inferences
- Since the program is closed, the only path onto RunPod supply is the Secure Cloud provider route, which the blog describes as a "much higher" bar with HIPAA/SOC-type certification (requirements page not found).

### Gaps
- Official RunPod host revenue share, payout cadence, and the historical host hardware requirements (GPU counts, bandwidth, uptime, burn test) could not be read; the docs pages 404.
- Whether a RunPod host machine could be a cloud VM: not stated anywhere I could read; moot for new hosts.

## Key question 3: TensorDock host marketplace

### Takeaway
TensorDock takes a 25% revenue share (its agreement text says "twenty percent (25%)"), pays via Stripe with a $250 withdrawal threshold and $1,000 per 24 hours limit, and requires that "all new hardware added to our platform must be hosted in a data center" with 1 Gbps, a static IP and a Libvirt hypervisor on the host, which rules out running on a rented VM.

### Cited Findings
- Host page: "Apply, install our software on Ubuntu 22.04 LTS, set your pricing"; "we'll send you a script to install our Libvirt-based hypervisor software"; "marketplace users will be able to deploy virtual machines on your hardware"; "All hosts go through our strict vetting process." Requirements: "1 Gigabit Internet Connection... shared amongst multiple servers, up to 40 GPUs"; "A static IP address"; "all new hardware added to our platform must be hosted in a data center"; "PCIe Bandwidth: 16 GB/s (4.0 x8 or 3.0 x16)"; "RAM: 16 GB+ of RAM per GPU"; "CPU: 8+ vCPUs with 3+ GHz boost per GPU"; "Storage: 1 TB NVMe SSD per GPU"; "Network: 100 forwarded ports or dedicated IP"; a separate display device is needed "for the NVIDIA GPU to be fully passed through". "25% revenue-share fee". "Get paid whenever you want through Stripe. We'll cover the fees for all withdrawals above $10K." "excessive downtime will be penalized"; "you're not allowed to cirvument TensorDock and contact customers directly." — [TensorDock host page](https://www.tensordock.com/host.html)
- Supplier Hosting Agreement (Last updated March 26, 2024): "TensorDock will take a twenty percent (25%) fee from Supplier's earnings." "Once Supplier's account surpasses $250 of account balance, Supplier will be able to withdraw their balance." Max "one-thousand US dollars ($1,000)" per 24 hours via Stripe Connect. "Supplier represents and warrants that they have the right to grant TensorDock.com, Inc the rights to use the Cloud Services." "Supplier may not assign, transfer, sub-license or deal in any other manner with any or all of its rights" without consent. Downtime penalty "5 hours multiplied by the hourly earnings of the server"; data loss penalty "up to but not exceeding Supplier's previous month's earnings". TensorDock may terminate "with one (1) week of notice". No explicit hardware-ownership or prohibited-source clause. — [TensorDock Supplier Hosting Agreement](https://docs.tensordock.com/legal-information/supplier-hosting-agreement)
- Renter Terms of Service (Last updated September 24, 2024): 3.2 "you are procuring the Compute Services on your own behalf and not for resale or use by another entity." 5.1 access rights are "non-assignable, non-sublicensable, non-transferrable, and non-exclusive." — [TensorDock Terms of Service](https://docs.tensordock.com/legal-information/terms-of-service-tos)
- Renter prices on the homepage (checked 2026-10-22): "H100 SXM5 from $2.25/hr", "A100 SXM4 from $1.80/hr", "RTX 4090 from $0.35/hr", consumer GPUs "from $0.12/hr"; KVM section promises root access, "Docker is included on all VM templates". — [TensorDock](https://www.tensordock.com/)
- Ownership: TensorDock was acquired by Voltage Park in March 2025 (search snippet; not verified on TensorDock's site).

### Inferences
- Hosts must own the hypervisor layer (Libvirt on bare metal with GPU passthrough), so a TensorDock host cannot be a rented VM without nested virtualization, and the "hosted in a data center" rule excludes home and cloud-VM hosts.

### Gaps
- TensorDock 5090 and H100 PCIe renter prices: not shown on the pages I could read (gpu-4090.html and gpu-h100.html returned 404).

## Key question 4: SF Compute resale of reserved contracts

### Takeaway
SF Compute lets a buyer sell any part of owned reserved time back on its orderbook; the platform fee is a fixed per node-hour amount plus a percentage, both unpublished and variable; fills are whole minutes with a minimum of 1 node (8 GPUs) for 1 minute; a sell order "earns nothing until it fills" and is "not guaranteed to fill".

### Cited Findings
- "Sell unused compute time through the SF Compute orderbook... You receive credits only when a buyer buys the time." "You can sell any part of the time you own, including a period in the middle." "Fills use whole minutes, with a minimum of 1 node for 1 minute." "The same rules apply to time bought through a spot deployment or a firm reservation." — [SF Compute: Sell unused compute time](https://docs.sfcompute.com/preview/guides/reselling.md)
- Fee: "SF Compute subtracts a platform fee when your sale fills. The fee has two parts: Fixed amount: Fee per node-hour × node-hours sold; Percentage: Fee percentage × sale value." "SF Compute sets both fee parts, and your fees can change. Fees can also differ between organizations. Check the fee estimate in the CLI before you confirm an order." — [SF Compute: Sell unused compute time](https://docs.sfcompute.com/preview/guides/reselling.md)
- Orders: "Buy orders have no fees." Buy orders fill immediately if there is availability, otherwise "SF Compute cancels the order by default (immediate-or-cancel)"; `--allow-standing` keeps an order on the book. Sell orders "are not guaranteed to fill." Interruptible buy orders list purchased compute for resale at a multiple "above 1.0 and at most 1.5" of your max rate. API example: an order created at 1742402883 filled at 1742402889 (about six seconds, one example). Examples use "1 node (8 GPUs)" and 1h durations. — [SF Compute: Orders](https://docs.sfcompute.com/preview/orders.md)
- CEO article (Sept 9, 2026): customers "receive an average 25% realized discount off their compute price, via resale"; example "$100k purchase returns about $25k, lowering a $4.50/GPU/hr price to $3.375/GPU/hr"; "Each node has eight GPUs"; "The treasury limits each order to 24 hours"; "Resale fees reduce the credit received" (no rate given). — [SF Compute: The average customer now saves 25%](https://sfcompute.com/news/realized-discount)
- Reselling is "in public preview" (search snippet). — [SF Compute reselling introduction](https://docs.sfcompute.com/preview/guides/reselling-introduction)

### Inferences
- SF Compute is the only venue found where resale of rented capacity is explicitly sanctioned by the seller's own contract. The 25% average realized discount is a recovery on unused time, not a profit margin.

### Gaps
- Exact fee rate (fixed and percentage): not published; shown only in the CLI at order time.
- Allocation-schedule grid granularity: the platform-constants page redirects to a login ("blueprint") page.

## Key question 5: Crypto-paid marketplaces (FLAG: crypto, low priority)

### Takeaway
Akash, io.net, Clore, Nosana, Render and Lium pay hosts in tokens (axlUSDC is available on Akash and Clore accepts USDT/USDC with a 15% surcharge); Salad pays in "Salad Balance" redeemable for PayPal cash. Measured Salad host earnings for Oct 15 to 21, 2026 were $0.289/hr average for an RTX 4090 and $0.279/hr for an RTX 5090.

### Cited Findings

| Marketplace | Host payment currency | Host requirements (as published) | Live prices seen (renter-facing unless stated) |
|---|---|---|---|
| Akash Network (CRYPTO) | AKT or axlUSDC; take rate 1% uAKT, 2% axlUSDC (Prop 267, passed 2024-09-19) — [Akash gov proposal 267](https://akash.valopers.com/proposals/267) | "Kubernetes cluster deployed and verified"; "Base domain that you control"; "Provider bid deposit is in AKT (0.5 AKT); keep AKT for gas" — [Akash provider installation prep](https://akash.network/docs/providers/setup-and-installation/kubespray/provider-installation-prep/); 5 AKT wallet minimum in the build guide (search snippet) — [Build a Cloud Provider](https://akash.network/docs/deployments/praetor-app/akash-provider/build-cloud-provider) | H100 SXM $2.73/hr (computeprices, updated 2026-10-22) — [Akash H100](https://computeprices.com/providers/akash/gpus/h100); RTX 4090 $0.34, RTX 5090 $0.57 (computeprices, 2026-10-22) — [computeprices 4090](https://computeprices.com/gpus/rtx4090), [computeprices 5090](https://computeprices.com/gpus/rtx5090). Akash's own pricing page says "Prices are per GPU-hour in USD, derived from recent provider bids" but its table did not render — [Akash GPU pricing](https://akash.network/pricing/gpus/) |
| io.net (CRYPTO) | $IO coin for block rewards and jobs; "Your must stake to your device to make it eligible for block rewards and to be hired for jobs" — [io.net device onboarding](https://io.net/docs/guides/workers/device-onboarding) | 12 GB RAM, 256 GB SSD; Windows RTX 30xx+, macOS M3/M4, Ubuntu, HiveOS; 12-hour wait before hire; Proof of Work verification (search snippet of docs) — [io.net docs](https://docs.io.net/docs/workers-page) | io.net FAQ, "Pricing as of April 2026": H100 SXM $2.20/hr, H100 PCIe $1.49/hr, RTX 4090 $0.18/hr; 5090 not listed — [io.net FAQ](https://io.net/p/faq-what-gpus-are-available-on-io-net) |
| Clore.ai (CRYPTO) | Settled in CLORE; base fee "split 50/50 between you and the renter": on-demand 10% total (host 5%), spot 2.5% (host 1.25%); BTC/USDT/USDC payments add a 15% extra hoster fee; Proof-of-Holding reduces base fee up to 50% at 2,000,000+ CLORE — [Clore host fees](https://docs.clore.ai/for-hosts/host-fees) | Not read (search budget exhausted); Clore Partners program pays "tied to the US dollar" (search snippet) — [Clore Partners](https://docs.clore.ai/for-hosts/advanced/clore-partners-high-volume-rental-system-for-major-clients) | MiningBoard lists RTX 4090 on Clore at $0.750/hr (58 offers, "Updated 8 minutes ago" on 2026-10-22), no H100 row — [MiningBoard Clore](https://miningboard.com/rental-markets/clore-ai); a search snippet from the same site gave $0.139/h for 4090 and $1.99/h for H100 (conflict, treat as unreliable) |
| Nosana (CRYPTO) | $NOS earnings shown on host.nosana.com — [Nosana hosts](https://learn.nosana.com/hosts/grid.html) | "only native Linux installations are officially supported" (Ubuntu 20.04+); 12 GB+ RAM; 256 GB+ NVMe; 100/50 Mbps minimum; RTX 30/40/50, RTX A, A100, H100; "1 private key per GPU, 1 GPU per PC" — [Nosana hosts](https://learn.nosana.com/hosts/grid.html) | nosana.com: "NVIDIA 4090" $0.400/h (0 of 94 hosts available), "NVIDIA 5090" $0.500/h (0 of 38), "NVIDIA H100" $1.500/h (0 hosts) — [Nosana](https://nosana.com/) |
| Render Network (CRYPTO) | RENDER token (search snippet; not on the fetched page) | "A CUDA-enabled NVIDIA GPU and a minimum of CUDA 10.1 drivers"; driver "566.36"; "minimum 6GB of VRAM, and 8+GB VRAM is preferred"; 32+ GB RAM recommended; join via "Render Network Interest Form" and an onboarding queue — [Render node operator start](https://know.rendernetwork.com/general-render-network/what-role-am-i/how-to-get-started-1) | Not found |
| Spheron (CRYPTO/fiat unclear) | Not found | Provider docs not found (docs.spheron.ai landing only) — [Spheron docs](https://docs.spheron.ai/) | "starting at $0.72/hour" across H100/A100/B200/B300 — [Spheron docs](https://docs.spheron.ai/); 5090 $0.68, H100 SXM $2.20 (computeprices, 2026-10-22) |
| Lium (Bittensor SN51) (CRYPTO) | Not stated on the page read; provider "incentive" set by score — [Lium provider overview](https://docs.lium.io/bittensor-subnet/miner/overview) | Accepted NVIDIA list (Hopper/Blackwell/Ampere, RTX 50/40/30/20, GTX 10/16); "A node without Sysbox is never listed"; confidential VMs need Hopper or Blackwell — [Lium provider overview](https://docs.lium.io/bittensor-subnet/miner/overview) | H100 SXM $1.31/hr (computeprices, updated 2026-10-21, cheapest H100 SXM tracked) — [computeprices H100](https://computeprices.com/gpus/h100) |
| Salad (pays in Salad Balance) | "Redeem your balance for PayPal cash, RENDER and other crypto rewards, prepaid cards, gift cards, games, and more." — [Why Salad](https://salad.com/why-salad) | "Windows 10 or 11, 64-bit"; "NVIDIA RTX 3060 or later currently has the best access to high-earning GPU workloads"; 4+ cores, 12 GB+ RAM; workloads run in "an isolated Linux VM, separate from Windows" — [Why Salad](https://salad.com/why-salad) | Host earnings, measured Oct 15–21, 2026: RTX 4090 average $0.289/hr (most machines $0.285–$0.302, top 1% $0.481, job running 97% of time); RTX 5090 average $0.279/hr ($0.261–$0.311, top $0.413, 97%); RTX 3090 $0.081/hr — [Salad GPU earning rates](https://salad.com/earning-rates/). Renter price RTX 4090 $0.160 (Lowest) to $0.330 (High), RTX 5090 $0.250 (Lowest) (computeprices, 2026-10-22) |

### Inferences
- Salad is the only platform in this group that publishes measured host earnings including idle hours; its 4090 figure ($0.289/hr) is close to the implied Vast host take on a 4090 at roughly 54% utilization (estimate: $0.54 × 0.54).
- Every crypto venue except Salad settles in a token; USD-equivalent earnings depend on token price at withdrawal.

### Gaps
- Akash official provider hardware and bare-metal/VM policy pages returned 404 at /docs/providers/ and /docs/providers/intro.
- io.net payout currency and schedule are not on the docs pages read; Clore host requirements not read; Spheron provider docs not found; Lium payment token not confirmed.

## Key question 6: Other hosts/aggregators that pay in USD

### Takeaway
Among USD-paying venues, only Vast and TensorDock accept small independent hosts. Shadeform works only with Tier 3/4 datacenter machines, Cudo requires 5 bare-metal hosts in a renewable-powered datacenter, Hyperbolic takes supply by email, Prime Intellect lists direct GPU contribution as a future feature, and Thunder, Fluidstack, GMI, Hot Aisle and Massed Compute have no supplier program I could find.

### Cited Findings
- Hyperbolic: homepage "Compute Providers" section with a "List Your GPU Capacity" button linking to `mailto:christopher@hyperbolic.ai`; no requirements published. Terms (Last Updated March 24, 2025): 1.1 "Hyperbolic does not offer, supply, or provide the Supplier Services"; 9.3 prohibits arranging "the sale of Supplier Services from, or the payment of fees to, Suppliers outside the Services". — [Hyperbolic](https://www.hyperbolic.ai/), [Hyperbolic Terms](https://www.hyperbolic.ai/terms)
- Shadeform: "We currently only work with machines that located in Tier 3 and Tier 4 datacenters"; contact support@shadeform.ai; "We guarantee all GPUs are in Tier 3 or Tier 4 datacenters." — [Shadeform FAQ](https://docs.shadeform.ai/getting-started/faq)
- Prime Intellect: "We've already integrated 12 clouds, with many more coming"; "Allow users to contribute their GPUs directly" is listed under upcoming features (blog undated). — [Prime Intellect compute blog](https://primeintellect.ai/blog/compute)
- Cudo Compute supplier requirements: "the infrastructure must be hosted in a data center powered by renewable energy"; "it is required to commit a minimum of 5 bare-metal hosts"; per host "16 cores or greater, with VT-x or AMD-V enabled", "64 GB or greater" RAM, "At least 1 x 2 TB SSD", "1 x 10GbE for public traffic", "iDRAC/iLO/IPMI out-of-band management interface", "A minimum block of 32 (/27) publicly routable IPv4 addresses". Revenue share not stated. — [Cudo supplier requirements](https://docs.cudocompute.com/suppliers/requirements)
- Thunder Compute: no host program found (search); Fluidstack: homepage has no partner or supply section; GMI Cloud: partner program is for resellers and alliances, not hardware suppliers (search snippet) — [GMI partnership](https://www.gmicloud.ai/en/company/partnership); Hot Aisle: AMD MI300X provider, no supply program found; Massed Compute: "We own the hardware, so you skip the middleman", only an affiliate program — [Massed Compute](https://massedcompute.com/).
- Cheap resellers/aggregators that appear in price trackers today: "Compute Cheap" H100 SXM $1.38 (2026-10-22), "OpenRelay" RTX 5090 $0.50, "QuickPod" 5090 $0.57, "gpu.ai (community)" 4090 $0.34, "Hexgrid Cloud" 5090 $0.55 (business models not researched). — [computeprices H100](https://computeprices.com/gpus/h100), [computeprices 5090](https://computeprices.com/gpus/rtx5090)

### Inferences
- White-label or reseller programs exist on the demand side (GMI resellers, SF Compute resale), not as host-onboarding programs for individuals.

### Gaps
- Hyperbolic supply-side requirements and revenue share: not published.
- Massed Compute partner page (/partners/) 404; Fluidstack partner requirements not found.

## Key question 7 (TECHNICAL): Can a GPU instance rented from Lambda, RunPod, TensorDock, Hyperbolic, Nebius, Crusoe or Voltage Park run the Vast host daemon or RunPod host software?

### Takeaway
The Vast daemon needs root on an Ubuntu Server box, control of the Docker daemon, a dedicated Docker partition, a public IPv4 with 5+ forwarded ports per GPU, 500 Mbps up and down, and (for VM support) VT-d/IOMMU. It does not check for a hypervisor, so a root VM from Lambda, Nebius, Crusoe or Voltage Park could in principle run Docker-only hosting; RunPod Pods cannot (no Docker daemon). RunPod host software is closed to new hosts, and TensorDock's host software is itself a hypervisor, so it needs bare metal.

### Cited Findings
- Vast daemon needs: Ubuntu Server 22.04/24.04 (desktop unsupported), public IPv4 (no CGNAT), ≥5 forwarded ports per GPU, 500/500 Mbps, dedicated 200 GB Docker SSD, Secure Boot off, machine "dedicated to hosting". — [Verification Stages](https://docs.vast.ai/host/verification-stages.md)
- Vast install script: no hypervisor check; installs nvidia-docker2; rewrites daemon.json; moves /var/lib/docker to an XFS partition created with parted or a loop file; creates a NOPASSWD sudo user; installs qemu-kvm/libvirt only if IOMMU passes. — [Vast install script](https://s3.amazonaws.com/vast.ai/install)
- Vast VM support requires "a CPU and a chipset that support Intel VT-d or AMD-Vi" and IOMMU kernel args; hosts without it are "hidden in the search page for clients who have VM-based templates selected." — [VMs](https://docs.vast.ai/host/vms.md)
- RunPod Pods: "Runpod runs Docker for you, so you cannot spin up your own Docker instance or use Docker Compose on Pods." — [Runpod Pods overview](https://docs.runpod.io/pods/overview)
- Lambda On-Demand: "on-demand access to Linux-based, GPU-backed virtual machine instances"; GPU Base image includes "NVIDIA driver, CUDA toolkit, OFED, cuDNN, NCCL, Docker"; the page references running `sudo apt full-upgrade`. Nested virtualization not mentioned. — [Lambda On-Demand docs](https://docs.lambda.ai/public-cloud/on-demand/)
- TensorDock renter instances: "KVM Virtualization" with root access, "Docker is included on all VM templates". — [TensorDock](https://www.tensordock.com/)
- Nebius Compute: "virtual machines" that "function similarly to your local machine but are hosted in the cloud". — [Nebius Compute docs](https://docs.nebius.com/compute)
- Crusoe: docs list a "Creating a VM" quickstart; bare metal not mentioned. — [Crusoe Cloud docs](https://docs.crusoecloud.com/)
- Voltage Park: navigation lists "Bare-Metal Access" and "Virtual Machines"; "You can rent one H100 GPU for 1 hour starting at $1.99 without a contract." — [Voltage Park pricing](https://www.voltagepark.com/pricing)
- TensorDock host software is "Libvirt-based hypervisor software" with GPU passthrough. — [TensorDock host page](https://www.tensordock.com/host.html)

**Feasibility matrix (estimate, based on the findings above)**

| Source instance | What you get | Run Vast daemon (Docker-only)? | Run Vast with VM support? | Run TensorDock host software? | Run RunPod host software? |
|---|---|---|---|---|---|
| RunPod Pod | Container, no Docker daemon | No | No | No | n/a (program closed) |
| Lambda | Linux VM, sudo, Docker preinstalled, public IP | Technically plausible (unverified: port forwarding count, PCIe bandwidth, repartitioning inside a VM) | Only with nested virt + IOMMU (not documented) | No (needs hypervisor on host) | n/a |
| TensorDock | KVM VM, root, Docker | Technically plausible (unverified) | Only with nested virt | No | n/a |
| Hyperbolic | Not verified (supplier-provided machines) | Unknown | Unknown | No | n/a |
| Nebius / Crusoe | VM | Technically plausible (unverified) | Only with nested virt | No | n/a |
| Voltage Park bare metal | Bare metal | Yes in principle (daemon has no ownership check) | Yes if VT-d enabled | Yes in principle | n/a |

### Inferences
- Nothing in Vast's software blocks a rented VM; the blockers are (a) verification criteria such as >2.85 GiB/s PCIe per GPU, 500 Mbps symmetric, 5 ports per GPU, and (b) the contract (see question 8). Unverified machines rank low and most renters filter for verified hosts (third-party claim: [AI Tool Discovery review](https://www.aitooldiscovery.com/ai-infra/vast-ai-review)).
- Bare metal from Voltage Park is the only configuration in the list that satisfies all of Vast's technical requirements including VM support, but Voltage Park's contract forbids it (question 8).

### Gaps
- No published test of the Vast daemon inside a cloud VM was found. Whether Lambda/Nebius/Crusoe expose enough forwarded ports and allow repartitioning is not documented on the pages read.

## Key question 8 (CONTRACTUAL): Do renter-side terms forbid resale, and do host-side terms forbid listing hardware you do not own?

### Takeaway
Every renter-side contract read (Lambda, Nebius, Crusoe, Voltage Park, Hyperbolic, TensorDock, and Vast's own Terms) prohibits reselling, renting or leasing the service to third parties. On the host side, Vast's Standard Hosting Agreement requires the provider to be "the sole owner of the Hardware" with the hardware "located at the Provider"; TensorDock requires the supplier to warrant it has "the right to grant" use and to host in a data center; RunPod's terms are silent but the program is closed.

### Cited Findings (renter side, with URLs)
- Lambda Cloud Terms (Last updated August 2025): Section 2(i) prohibits "sell, resell, rent, lease, or otherwise distribute any portion of the Services"; 2(iv) "access any portion of the Services for the purpose of building a similar or competitive product or service"; "Customer may not access the Services if it is a direct competitor of Lambda, except with Lambda's prior written consent." Access is "non-sublicensable, non-transferable, non-exclusive". — [Lambda Terms of Service](https://lambda.ai/legal/terms-of-service)
- Nebius AI Platform Terms of Use (published March 31, 2025), 2.8: "When using the Platform User shall not: ... (ii) sell, resell, sublicense, transfer, or distribute any or all of the services and Platform". — [Nebius Terms of Use](https://docs.nebius.com/legal/terms-of-use)
- Crusoe Cloud Platform Terms of Service (Version 1.10, effective August 10, 2026), Customer Obligations > Restrictions: "Customer will not, and will not allow End Users to, ... (c) sell, resell, sublicense, transfer, or distribute any or all of the Services" and "(iii) in a manner intended to avoid incurring Fees". — [Crusoe legal](https://legal.crusoe.ai/)
- Voltage Park Compute Services Agreement (Last Revised May 28, 2026), Exhibit A item 1: "sell, resell, rent, lease or otherwise distribute any portion of the Services" and "use the Services to provide a service bureau"; item 5: "building a similar or competitive product or service"; item 14: "allow any person who is not an employee or independent contractor of the Customer to access or use the Services." — [Voltage Park Compute Services Agreement](https://voltagepark.com/computer-services-agreement)
- Hyperbolic Terms (Last Updated March 24, 2025), Section 7(i): users may not "license, sell, rent, lease, transfer, assign, reproduce, distribute, host or otherwise commercially exploit the Services"; 2.1 bars "redistribution or use on a service bureau basis". — [Hyperbolic Terms](https://www.hyperbolic.ai/terms)
- TensorDock Terms (Sept 24, 2024), 3.2: "you are procuring the Compute Services on your own behalf and not for resale or use by another entity." — [TensorDock Terms](https://docs.tensordock.com/legal-information/terms-of-service-tos)
- RunPod Terms (March 24, 2026), Section 9: "Resell any credits purchased through the Service without the prior written consent of Runpod"; "Use the Service as part of any effort to compete with us." — [Runpod Terms of Service](https://www.runpod.io/legal/terms-of-service)
- Vast Terms of Use (Sept 1, 2026), Prohibited Activities item 10: using the Services "(i) as part of any effort to compete with Company or to provide services as a service bureau"; item 17: "Access or use the Services to develop, train, or improve any competing or similar product or service." (Relevant if someone rents from Vast and resells elsewhere.) — [Vast Terms of Use](https://vast.ai/terms)

### Cited Findings (host side, with URLs)
- Vast Standard Hosting Agreement: "Provider represents and warrants that: (i) it is the sole owner of the Hardware and Provider has the unrestricted right to lease the Hardware to Vast.ai"; "The Hardware shall at all times be located at the Provider"; "The Hardware shall, at all times, be the sole and exclusive property of Provider." Subcontractors are allowed if they "agree to the same terms"; the relationship is "nonexclusive". — [Standard Hosting Agreement](https://cloud.vast.ai/host/agreement)
- Vast datacenter status: "The equipment must be owned by a business"; application needs "A contract or invoice from the datacenter linking the business". — [Datacenter Status](https://docs.vast.ai/host/datacenter-status.md)
- TensorDock Supplier Hosting Agreement: "Supplier represents and warrants that they have the right to grant TensorDock.com, Inc the rights to use the Cloud Services"; no explicit ownership clause; "all new hardware added to our platform must be hosted in a data center" (host page). — [TensorDock Supplier Hosting Agreement](https://docs.tensordock.com/legal-information/supplier-hosting-agreement), [TensorDock host page](https://www.tensordock.com/host.html)
- RunPod Terms: "No clause addresses Hosts owning hardware or prohibited hardware sources." — [Runpod Terms of Service](https://www.runpod.io/legal/terms-of-service)

### Inferences
- Re-listing a Lambda, Nebius, Crusoe, Voltage Park, Hyperbolic or TensorDock instance on Vast would breach the source cloud's resale clause and Vast's "sole owner" and "located at the Provider" warranties at the same time. A colocated or leased-to-own server that you control and that sits at your premises or your colo is the closest compliant structure; Vast's subcontractor clause and the datacenter "contract or invoice from the datacenter" requirement suggest colo is accepted.
- Only SF Compute resale (question 4) is a contractually sanctioned secondary market.

### Gaps
- Nebius's current Customer Agreement PDF (agreement-20260311.pdf) could not be parsed; the Terms of Use clause above is the readable source.
- Lambda's "Platform Guidelines" referenced in Cloud Terms 2(c) were not readable.

## Key question 9 (NUMBERS): H100 SXM, RTX 4090, RTX 5090 spread

### Takeaway
At today's Vast medians and an assumed ~80% host share, the gross spread between the cheapest VM-capable cloud rental and Vast host take is about $0.34/hr on an H100 SXM (needs ~83% utilization to break even), about $0.19/hr on a 4090 (~65% break-even), and about $0.15 to $0.20/hr on a 5090 (~71 to 79% break-even). Every figure after column (b) is an estimate because Vast does not publish its fee or utilization.

### Cited Findings

| Item | H100 SXM | RTX 4090 | RTX 5090 |
|---|---|---|---|
| (a) Cheapest rental cost per GPU-hour from a cloud today (any model) | Lium.io $1.31 (updated 2026-10-21), Compute Cheap $1.38 (2026-10-22), Latitude.sh $1.68, Gcore $1.72, Cudo $1.79, Voltage Park $1.99, Runpod Community $2.69, TensorDock from $2.25, Lambda $3.99 to $4.29, Nebius $4.50 — [computeprices H100](https://computeprices.com/gpus/h100), [Runpod pricing](https://www.runpod.io/pricing), [TensorDock](https://www.tensordock.com/), [Lambda pricing](https://lambda.ai/pricing), [Nebius prices](https://nebius.com/prices) | Salad $0.160 (container, Lowest priority), Akash $0.34, Runpod Community $0.34 (out of stock), TensorDock VM from $0.35, io.net $0.18 (April 2026), Vast itself from $0.14 — [computeprices 4090](https://computeprices.com/gpus/rtx4090), [TensorDock](https://www.tensordock.com/), [io.net FAQ](https://io.net/p/faq-what-gpus-are-available-on-io-net) | Salad $0.25 (container), OpenRelay $0.50, Hexgrid $0.55, Akash $0.57, QuickPod $0.57, Runpod Community $0.69, Vast itself from $0.39 — [computeprices 5090](https://computeprices.com/gpus/rtx5090), [Runpod pricing](https://www.runpod.io/pricing) |
| (a') Cheapest rental on a root VM or bare metal (needed to run a host daemon) | Latitude.sh $1.68 (bare metal provider; VM/BM not verified today), Voltage Park $1.99 (bare metal offered) | TensorDock KVM VM from $0.35 | Not found at a VM/bare-metal provider with a stated price |
| (b) Median renter-facing price on Vast today | $2.53 — [Vast pricing](https://vast.ai/pricing) | $0.67 — [Vast pricing](https://vast.ai/pricing) | $0.87 (pricing page); listed-market median in host calculator $0.65 to $0.69 — [Vast pricing](https://vast.ai/pricing), [Vast calculator](https://vast.ai/hosting/calculator) |
| (c) Vast host fee | Not published. Vast: "Live GPU prices are typically about 25% above what hosts earn." — [Vast blog](https://vast.ai/article/how-much-money-can-you-earn-renting-out-your-gpu-on-vast-ai) | same | same |
| (c') Implied host take at median (estimate = b / 1.25) | $2.02 | $0.54 | $0.70 (or $0.65 to $0.69 per calculator) |
| (d) Net spread per hour at 100% utilization (estimate = c' minus a') | $0.34 vs Latitude $1.68; $0.03 vs Voltage Park $1.99; negative vs Runpod Community $2.69 | $0.19 vs TensorDock $0.35 | $0.15 to $0.20 vs $0.50 to $0.55 (OpenRelay/Hexgrid, instance type unverified) |
| (d') Break-even utilization (estimate = a' / c') | 83% (Latitude), 99% (Voltage Park) | 65% | 71% to 79% |
| (e) Typical host utilization | Not published by Vast. Calculator default assumption 65%; Vast blog example 80%. Third-party: "60–85%" (MiningBoard guide, via search) vs "nearer 30%" for residential boxes (GPUnex review, via search). Salad measured 97% job time on 4090/5090 (Salad only). All non-Vast figures are estimates. — [Vast calculator](https://vast.ai/hosting/calculator), [Salad earning rates](https://salad.com/earning-rates/) | same | same |

- Vast's own listing for 1x RTX 5090 at $0.65 and 65% utilization yields $386/mo expected host earnings, of which $304 is GPU revenue (= $0.65 × 24 × 30 × 0.65, estimate check: $304). — [Vast calculator](https://vast.ai/hosting/calculator)
- Vast's blog: a 4x 5090 rig at 80% utilization "can generate $700-$1,400 per month", i.e. $175 to $350 per GPU per month (estimate: $0.30 to $0.61 per rented hour). — [Vast blog](https://vast.ai/article/how-much-money-can-you-earn-renting-out-your-gpu-on-vast-ai)

### Inferences
- Estimate: at the calculator's default 65% utilization the H100 SXM resale loses money against every cloud source except Lium ($1.31) and Compute Cheap ($1.38), whose instance types and contract terms were not verified; the 4090 nets about $0.00/hr (0.54 × 0.65 = $0.35 vs $0.35 cost); the 5090 nets about -$0.05 to $0.00/hr.
- Estimate: storage and bandwidth revenue (calculator shows $79 + $3 per month on a 5090 listing) can exceed the GPU spread itself, but a rented VM usually pays its provider for disk too.
- The cheapest Vast offers (H100 SXM from $1.73, 4090 from $0.14, 5090 from $0.39) show that a reseller must undercut existing verified hosts, which pushes the achievable price below the median used above.

### Gaps
- Vast host fee percentage: not published (see question 1).
- No Vast-published utilization figure exists; everything in row (e) other than Vast's own "assumption" wording is third-party.
- Whether Lium, Compute Cheap, Latitude, OpenRelay, Hexgrid instances are VMs or bare metal, and their resale clauses: not checked (search budget exhausted).

## Key question 10: Does anyone publicly describe renting from a cloud and re-listing on Vast, and what happened?

### Takeaway
I found no public account (Reddit, Hacker News, X, or blogs) of anyone renting a cloud GPU and re-listing it on Vast, RunPod or TensorDock, across eight targeted searches before the search budget ran out. The only sanctioned, documented resale practice is SF Compute's orderbook, where the company reports a 25% average realized discount for sellers.

### Cited Findings
- Searches for "rent GPU cloud relist on vast.ai arbitrage", "vast.ai host rented cloud server relist resell GPU reddit", "GPU rental arbitrage rent cloud instance resell marketplace hacker news", "hetzner GPU server vast.ai host earnings", "runpod OR vast.ai host hetzner OR ovh GPU dedicated server relist", and "arbitrage GPU vast.ai rent resell margin" returned only vendor blogs, reviews and comparison pages; none described the practice. (Search results, 2026-10-22.)
- SF Compute (Sept 9, 2026): customers "receive an average 25% realized discount off their compute price, via resale"; a listing "earns nothing until it fills". — [SF Compute realized discount](https://sfcompute.com/news/realized-discount)
- A 2018-era Hacker News thread quotes Vast's founders describing it as "airbnb for compute" (background only). — [Hacker News: Vast.ai](https://news.ycombinator.com/item?id=30736459)
- Third-party reviews on host economics (not arbitrage): one claims a realistic single 4090 nets "near +$30/month" after fees, 30% utilization and electricity (GPUnex, via search snippet) — [GPUnex review](https://www.gpunex.com/blog/vast-ai-review-2026/); another says RTX 4090s on Vast clear "around $0.169/h" (MiningBoard bid guide, via search snippet) — [MiningBoard bid pricing](https://miningboard.com/guides/vast-ai-bid-pricing).

### Inferences
- The absence of public write-ups is consistent with the contractual bars in question 8 and with the thin or negative spreads in question 9.

### Gaps
- r/vastai, r/LocalLLaMA and X were not directly searchable with the remaining budget; a follow-up search session is needed to confirm there are no first-hand accounts.
