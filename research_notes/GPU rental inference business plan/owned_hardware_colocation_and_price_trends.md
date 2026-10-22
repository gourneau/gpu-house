# Owning GPU inference hardware in cheap-power colocation, and GPU rental price trends (US sole proprietor, October 2026)

All numbers below were read live on 2026-10-22 ("checked 2026-10-22" applies to every row). "Source date" is the date the source page states, or "undated" if the page gives none. Every estimate is marked "estimate" and shows the arithmetic. "Not found" means I could not find a public figure.

Method note: the crw scraper was unreachable (connection closed on every call), so pages were read with WebFetch. Several pages blocked the fetch (eBay listing 403, DatacenterDynamics 403, Benzinga 403, bestvaluegpu 429, rackrate.ai DNS failure); where that happened the figure comes from the search-result snippet and is marked "snippet only".

## Key question 1: What does it cost today to buy the hardware (used 8x H100 SXM, 8x H200, new 8x B200, single cards)?

### Takeaway
A refurbished 8x H100 SXM server (Dell XE9680 class, about 2.5 to 3 years old) is listed by US resellers at $180,000 to $215,000, and a broker fair-market index puts a used HGX H100 node at about $195,000 (August 2026 data). A new 8x H200 server runs about $320,000 to $420,000 (typical $370,000) and refurbished H200 systems barely exist; a new 8x B200 server runs about $400,000 to $550,000 with 8 to 20 week lead times. Single used H100 SXM modules trade around $17,500 to $24,000 on eBay in September and October 2026, used H100 PCIe cards around $28,000 to $32,000 (asks), and sources disagree widely on A100 80GB.

### Cited Findings

#### Used and refurbished 8x H100 SXM servers (checked 2026-10-22)

| Item | Price | Condition and terms | Source date | Source |
|---|---|---|---|---|
| Dell PowerEdge XE9680, 8x H100 80GB SXM5, 2x Xeon 8462Y+, 2 TB DDR5, no drives, 6x 2800 W PSU | $180,000 | Seller refurbished, Dell ProSupport to Nov 4, 2028, 30-day returns, free 2-day shipping, out of stock, orders over $50K go through sales | undated (warranty end Nov 4, 2028) | [ServerPartDeals](https://serverpartdeals.com/products/dell-poweredge-xe9680-xeon-platinum-8462y-8x-nvidia-hgx-h100-80gb-sxm5-nvlink-ai-powered-refurbished-gpu-server) |
| Dell XE9680 8x H100 SXM5 (eBay) | $185,000 | Refurbished, 1-year warranty (snippet only; listing page returned 403) | undated | [eBay item 306859468669](https://www.ebay.com/itm/306859468669) |
| Dell XE9680 8x H100 SXM5 (eBay, second listing) | $215,000 or best offer | Used (snippet only) | undated | [eBay item 117157513315](https://www.ebay.com/itm/117157513315) |
| Dell XE9680 8x H100 | $199,999 | Used dealer listing (snippet only) | undated | [The Server Store](https://www.theserverstore.com/search.asp?catid=&keyword=dell+Poweredge&page=8&sortby=0) |
| Dell XE9680 8x H100 | $249,000 | Dealer listing (snippet only) | undated | [Network Outlet](https://networkoutlet.com/products/dell-poweredge-xe9680-ai-gpu-server-8-nvidia-hgx-h100-80gb-sxm) |
| Dell XE9680 8x H100 | $275,000 | Dealer listing (snippet only) | undated | [Viperatech](https://viperatech.com/product/dell-poweredge-xe9680-rack-server-210-bfxh-bundle-with-8-x-h100-gpus) |
| Used HGX H100 8-GPU node, fair market value (observed whole-node listings adjusted to a reference config; excludes fabric, racks, install, support) | about $195,000 per node ($24,400 per GPU); orderly liquidation about $173,000 (89%); forced liquidation about $126,000 (65%) | Index, not realized sales; up 0.8% on prior issue | Data through August 2026; page updated Oct 17, 2026 | [American Compute HGX H100 server value](https://www.amcompute.com/gpu-server-values/h100) |
| Used 8-GPU H100 server | roughly $150,000 to $180,000 | Article estimate, no date on the figure | Apr 8, 2026 | [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/) |
| Used HGX H100 system, median | $250,000 (indicative, July 2026) | Snippet only; site did not resolve | July 2026 | [RackRate](https://rackrate.ai/hardware/hgx-h100) |
| Buyback offer for used XE9680 8x H100 | EUR 80,000 to 120,000 per system | What a European buyer says it pays sellers (marketing page) | undated | [server-parts.eu](https://www.server-parts.eu/post/selling-used-dell-xe9680-nvidia-h100-gpu-servers) |
| Used/refurbished H100 cards | $18,000 to $22,000 each; used servers price "meaningfully below new" (no figure) | Analyst blog | Jul 14, 2026 | [Mercatus H100 server price](https://www.mercatus-ai.com/blog/h100-server-price) |

#### New 8x H100 SXM servers (reference for depreciation; checked 2026-10-22)

| Item | Price | Notes | Source date | Source |
|---|---|---|---|---|
| Supermicro SYS-821GE-TNHR 8U, eStore "system starting price" | $323,684.64 | Page lists an "HGX 8x H200 141GB" baseboard in the configuration and says "contact us before purchasing"; 6x 3000 W Titanium PSUs (4+2); in stock | undated | [Supermicro eStore](https://store.supermicro.com/us_en/8u-gpu-superserver-sys-821ge-tnhr.html) |
| Supermicro SYS-821GE-TNHR with 8x H100, 2x Xeon 8558 | $298,999 | Reseller bundle (snippet only) | undated | [Router-Switch](https://www.router-switch.com/ai-server-promotion-bundle-7.html) |
| Supermicro SYS-821GE-TNHR with 8x H100 | $298,888 and $310,140 (two configs) | Reseller (snippet only) | undated | [Network Outlet](https://networkoutlet.com/products/supermicro-sys-821ge-tnhr-ai-gpu-server-nvidia-h100) |
| Supermicro SYS-821GE-TNHR with 8x H100 | $289,000 | Reseller (snippet only) | undated | [GPUVendor](https://gpuvendor.com/server/supermicro-sys-821ge-tnhr-h100-sxm5-8-gpu-ai-server) |
| Supermicro SYS-821GE-TNHR barebone (no GPUs) | $23,487.60 | Structured-data price on the page (snippet only) | undated | [Exxact](https://www.exxactcorp.com/Supermicro-SYS-821GE-TNHR-E133318654) |
| New 8-GPU HGX H100 from Supermicro, Dell, HPE, integrators | $250,000 to $320,000; typical $285,000 ($31,000 to $40,000 per GPU); cost stack: 8 GPUs $200K to $240K, server $25K to $30K, NVLink/NVSwitch about $15K, networking and storage $20K to $30K, integration $10K to $15K | Analyst blog, "public OEM quotes" | Jul 14, 2026 | [Mercatus H100 server price](https://www.mercatus-ai.com/blog/h100-server-price) |

#### 8x H200 servers (checked 2026-10-22)

| Item | Price | Notes | Source date | Source |
|---|---|---|---|---|
| New 8-GPU HGX H200 (OEM integrated) | $320,000 to $420,000; typical $370,000 ($40,000 to $52,500 per GPU); 8 to 12% off for multi-system orders | "Refurbished H200 systems barely exist in 2026"; H200 SXM card $32,000 to $40,000 | Jul 8, 2026 | [Mercatus H200 server price](https://www.mercatus-ai.com/blog/h200-server-price) |
| 8-GPU HGX H200 | List $400,000 to $500,000; street and resale $350,000 to $420,000; single H200 SXM list $40,000 to $55,000, street $30,000 to $40,000 | Cloud vendor blog | Published Jan 8, 2026; updated Oct 20, 2026 | [Jarvislabs H200 price](https://jarvislabs.ai/blog/h200-price) |
| 8x H200 141GB SXM server, 96 cores, 2,304 GB DDR5 (eBay) | $513,540 or best offer | Listed as used with 1-year warranty (snippet only) | undated | [eBay item 167882999886](https://www.ebay.com/itm/167882999886) |
| HGX H200 8-GPU server; DGX H200 | $528,000; $880,000 | Reseller list (snippet only) | undated | [ITCT Shop](https://itctshop.com/nvidia-h100-h200-b200-price/) |
| Gigabyte G593-SD2 HGX H200 at Newegg | about $293,000 | Out of stock when checked by the source (snippet only) | Oct 2026 | [Thunder Compute H200 pricing](https://www.thundercompute.com/blog/nvidia-h200-pricing) |
| Bizon X9000 HGX H200 | "starts at $172,643" | Configuration unclear; far below other sources (snippet only) | undated | [Bizon](https://bizon-tech.com/bizon-x9000.html) |
| Used H200 SXM 141GB card | $24,000 to $28,000 (68 to 74% of $34,000 to $38,000 list) | "Q2 2026" figures in a February-dated article; no named data source | Feb 2026 | [ClusterBid secondary market 2026](https://clusterbid.com/blog/secondary-gpu-market-2026-used-h100-prices-resale-value-trading-volume) |

#### New 8x B200 servers (checked 2026-10-22)

| Item | Price | Notes | Source date | Source |
|---|---|---|---|---|
| 8-GPU HGX B200 (integrated) | $400,000 to $500,000; typical $450,000 (about $56,000 per GPU deployed); DGX B200 about $515,000; B200 card list (8+ volume) $30,000 to $40,000; street $45,000 to $50,000; 1,000 W per GPU, about 8 kW GPU load, "budget 12 kW or more of billed colocation capacity" | Analyst blog | Jul 16, 2026 | [Mercatus B200 server price](https://www.mercatus-ai.com/blog/b200-server-price) |
| 8-GPU HGX B200 | $450,000 to $550,000 incl. NVLink fabric, NICs, CPUs; single B200 street $45,000 to $55,000 "under 2026 supply constraints"; list $30,000 to $40,000 per Epoch AI | Cloud vendor blog | Published Apr 2, 2026; reviewed Oct 16, 2026 | [Thunder Compute B200 pricing](https://www.thundercompute.com/blog/nvidia-b200-pricing) |
| Supermicro SYS-A22GA-NBRT-G1 10U, 2x Xeon 6960P, HGX B200 | $422,704, "estimated delivery 4 weeks" | Reseller (snippet only) | undated | [Uvation marketplace](https://marketplace-admin.uvation.com/supermicro-sys-a22ga-nbrt-g1-10u-b200-gold-series-gpu-servers.html) |
| Supermicro SYS-822GS-NBRT 8U HGX B200 | special $198,500 (regular $234,451.12) | Listing text is internally inconsistent (Intel vs AMD); likely not a fully loaded system (snippet only) | undated | [Uvation marketplace](https://marketplace-admin.uvation.com/supermicro-sys-822gs-nbrt-gpu-superserver-intel-8u-nvidia-hgx-b200.html) |
| HGX B200 lead times | 8 to 20 weeks for "Golden SKU"; custom BOMs over 26 weeks | Reseller (snippet only) | undated | [Uvation marketplace](https://marketplace-admin.uvation.com/supermicro-sys-a22ga-nbrt-gpu-superserver-intel-10u-nvidia-hgx-b200.html) |
| Supermicro eStore B200 starting price | Not found (no eStore result surfaced) | | | |

#### Single cards (checked 2026-10-22)

| Card | Price | Basis | Source date | Source |
|---|---|---|---|---|
| H100 PCIe 80GB, eBay | $27,999.99 on each weekly snapshot Aug 21 to Sep 11, 2026; "no fresh used offer today, recently $28,000" | Tracker, condition not always recorded; excludes shipping | Oct 9, 2026 latest table row | [GPU Dojo H100 PCIe](https://gpudojo.com/h100-pcie) |
| H100 PCIe 80GB, Newegg (new) | $29,500 (Oct 9, 2026); $34,989 (Oct 2); $29,500 (Sep 25); $34,879 (Sep 11); $32,879 (Aug 21 to Sep 4) | Tracker | Oct 9, 2026 | [GPU Dojo H100 PCIe](https://gpudojo.com/h100-pcie) |
| H100 PCIe 80GB, US eBay asks | $28,000 to $32,399, median $32,000, 3 listings; six new-in-box overseas listings $27,884 to $52,950 | Asks, not sold | Sep 9, 2026 | [Caladan Semi buying guide](https://caladansemi.com/blog/used-nvidia-h100-a100-gpu-buying-guide-2026) |
| H100 PCIe 80GB, used | $13,000 to $16,500 (52 to 57% of $25,000 to $29,000 list) | No named data source | Feb 2026 ("Q2 2026" figures) | [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-2026-used-h100-prices-resale-value-trading-volume) |
| H100 PCIe 80GB | used $14,000 to $25,000; new $25,000 to $34,000 | Buyback index | Jun 27, 2026 | [ServerBuyback index](https://serverbuyback.com/resources/gpu-resale-value-index/) |
| H100 PCIe 80GB, used | $16,000 to $20,000 (Compute Exchange "Q3 2026 indicative") | Indicative, not sales | Sep 5, 2026 | [IntuitionLabs used AI GPU prices](https://intuitionlabs.ai/articles/used-ai-gpu-prices-resale-trends) |
| H100 SXM5 80GB module, eBay | $19,999.99 (Oct 22 and Oct 9, 2026); $23,999 (Oct 2); $37,998.99 (Sep 25); $17,549.99 (Sep 11 and 18) | Tracker; page updated 2026-10-22 02:14 UTC | Oct 22, 2026 | [GPU Dojo H100 SXM](https://gpudojo.com/h100-sxm) |
| H100 SXM5 80GB, US eBay asks | $14,000 to $22,550, median $19,550, 3 listings; eight modules at median = $156,400 | Asks, not sold | Sep 9, 2026 | [Caladan Semi](https://caladansemi.com/blog/used-nvidia-h100-a100-gpu-buying-guide-2026) |
| H100 SXM 80GB, used | $15,000 to $19,000 (54 to 58% of $28,000 to $32,000 list) | | Feb 2026 | [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-2026-used-h100-prices-resale-value-trading-volume) |
| H100 SXM5 80GB | used $15,000 to $28,000; new $27,000 to $40,000 | Buyback index | Jun 27, 2026 | [ServerBuyback](https://serverbuyback.com/resources/gpu-resale-value-index/) |
| H100 SXM, used | $22,000 to $27,000 (Compute Exchange "Q3 2026 indicative"); 3 new-in-box units at $18,000 each on r/homelabsales in Dec 2025 | Indicative | Sep 5, 2026 | [IntuitionLabs](https://intuitionlabs.ai/articles/used-ai-gpu-prices-resale-trends) |
| H100 SXM5, new list | $25,000 to $30,000 | | Jul 14, 2026 | [Mercatus](https://www.mercatus-ai.com/blog/h100-server-price) |
| A100 80GB PCIe, US eBay asks | $14,950 to $24,999, median $18,500, 15 listings; one US card with "ECC Error" at $12,500 | Asks | Sep 9, 2026 | [Caladan Semi](https://caladansemi.com/blog/used-nvidia-h100-a100-gpu-buying-guide-2026) |
| A100 80GB SXM4, US eBay asks | $8,300 to $12,200, median $9,925, 4 listings | Asks | Sep 9, 2026 | [Caladan Semi](https://caladansemi.com/blog/used-nvidia-h100-a100-gpu-buying-guide-2026) |
| A100 80GB (compare widget) | $12,500 | Tracker | Oct 2026 | [GPU Dojo H100 PCIe page](https://gpudojo.com/h100-pcie) |
| A100 80GB, used | $7,000 to $9,500 (Compute Exchange Q3 2026 indicative) | | Sep 5, 2026 | [IntuitionLabs](https://intuitionlabs.ai/articles/used-ai-gpu-prices-resale-trends) |
| A100 80GB SXM, used | $5,000 to $7,000 | | Feb 2026 | [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-2026-used-h100-prices-resale-value-trading-volume) |
| A100 SXM 80GB, used | $15,000 to $17,000 | Buyback index | Jun 27, 2026 | [ServerBuyback](https://serverbuyback.com/resources/gpu-resale-value-index/) |
| A100 80GB, used | $4,000 to $9,000 (new $7,000 to $15,000) | Vendor blog | Mar 2026 | [Jarvislabs A100 price](https://jarvislabs.ai/blog/a100-price) |
| A100 used/refurbished | about $7,800 (40GB) to $18,900 (80GB PCIe) "as of early 2026" | | Apr 8, 2026 | [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/) |
| RTX 5090 (MSRP $1,999) | new $7,443.99 Amazon (ASUS TUF OC); used eBay $6,750; tracked low $4,199.99 (Jul 30, 2026), high $7,449 (Sep 30, 2026); +74.3% Jun 10 to Oct 11 | Tracker | Oct 11, 2026 | [VideoCardPrices RTX 5090](https://videocardprices.com/card/nvidia-rtx-5090/) |
| RTX 5090, used eBay Buy-It-Now median | $6,900 (91 samples), lowest $4,400; history: $4,700 (Jul 28), $5,000 (Aug 15), $5,500 (Sep 1), $6,800 (Sep 30) | Asks; filter change on Oct 4 breaks comparability | Oct 11, 2026 | [SiliconComps RTX 5090](https://siliconcomps.com/gpu/rtx-5090/price-history/) |
| RTX 5090 | $4,999 new (B&H), $3,822 used (eBay) | Snippet only; page returned 429 | Oct 2026 | [BestValueGPU RTX 5090](https://bestvaluegpu.com/history/new-and-used-rtx-5090-price-history-and-specs/) |
| RTX 4090 (MSRP $1,599, discontinued), used | October 2026 "lowest average" (mean of 3 cheapest eBay listings per day) $3,147, daily range $2,997 to $3,300; prior 3 months $2,611; current $3,266 | Asks | Oct 2026 | [GPUPoet RTX 4090 Oct 2026](https://gpupoet.com/gpu/learn/price/october-2026/nvidia-geforce-rtx-4090) |
| RTX 4090, used | about $2,800 (eBay, via BestValueGPU) | | Oct 1, 2026 | [AI Indigo RTX 4090](https://aiindigo.com/hardware/nvidia-rtx-4090-24gb) |
| L40S 48GB, used | $6,750 to $8,750 | Dealer and marketplace observations, refreshed monthly | Oct 1, 2026 | [ClusterMelt L40S](https://clustermelt.com/gpus/l40s/price) |
| L40S 48GB | new Amazon $5,999, Newegg $8,495; used from $7,300 | Snippet only | Sep 2026 | [GPU Dojo L40S](https://gpudojo.com/l40s) |
| L40S 48GB | used $5,000 to $8,000; new $8,000 to $11,000 | Buyback index | Jun 27, 2026 | [ServerBuyback](https://serverbuyback.com/resources/gpu-resale-value-index/) |
| L40S (PNY) | $10,497.99 | Retail list (snippet only) | undated | [CDW](https://www.cdw.com/product/pny-nvidia-quadro-l40s-graphic-card-48-gb-gddr6/7582191) |

#### Server power, weight, and size (for colo sizing)

- NVIDIA DGX H100: "10.2 kW max" input, six 3.3 kW PSUs in 4+2 redundancy, 287.6 lb (130.45 kg) max, 8U, operating 5 to 30 C — [NVIDIA DGX H100 user guide](https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html) (undated doc, checked 2026-10-22)
- Supermicro SYS-821GE-TNHR: six 3000 W Titanium PSUs (4+2), optional eight (4+4) — [Supermicro eStore](https://store.supermicro.com/us_en/8u-gpu-superserver-sys-821ge-tnhr.html)
- Dell XE9680 (refurb listing): 6U, six 2800 W PSUs, H100 700 W TDP each — [ServerPartDeals](https://serverpartdeals.com/products/dell-poweredge-xe9680-xeon-platinum-8462y-8x-nvidia-hgx-h100-80gb-sxm5-nvlink-ai-powered-refurbished-gpu-server)
- Mercatus sizing rule: H100/H200 GPU load 5.6 kW (8 x 700 W); its worked example bills 8 kW of colo capacity at PUE 1.4; B200 systems about 8 kW GPU load, budget 12 kW+ billed — [Mercatus H100](https://www.mercatus-ai.com/blog/h100-server-price), [Mercatus B200](https://www.mercatus-ai.com/blog/b200-server-price) (Jul 2026)

#### Shipping and setup inputs (checked 2026-10-22)

- LTL per-pallet live rates on one broker's ticker: $88 (LA metro) to $447 (LA to NYC); populated server racks are freight class 70, single pieces over about 150 lb need two-person delivery — [Warp server racks page](https://www.wearewarp.com/tools/how-to-ship/server-racks) (undated)
- Dense servers are freight class 85 to 100; carrier liability is only $0.10 to $2.00 per lb; cargo insurance "typically costs 1 to 3% of the declared value" — [Warp electronics shipping guide](https://www.wearewarp.com/tools/how-to-ship/electronics) (snippet only, undated)
- Colo one-time fees: setup/installation $500 to $3,000+; pallet receiving $250 to $600; rack and stack $1,000 to $2,500 — [QuoteColo single-rack AI colocation](https://www.quotecolo.com/single-rack-ai-colocation/) (undated, 2026)
- GR1D (South Houston) charges no setup fee on 12+ month terms — [GR1D host page](https://gr1d.us/host) (undated, cites March 2026 market data)

### Inferences
- All-in capex for one used 8x H100 SXM server (estimate): $180,000 server (ServerPartDeals XE9680 refurb) + about $2,500 freight and cargo insurance (one pallet $100 to $450 plus 1% of $180,000 = $1,800) + about $2,000 setup (pallet receiving $250 to $600 and rack-and-stack $1,000 to $2,500, QuoteColo) = about $184,500. Using the American Compute fair-market value of $195,000 instead gives about $199,500. Range: roughly $185,000 to $200,000 before spares, drives (the ServerPartDeals unit ships with no drives), or an extra NIC.
- All-in capex for one 8x H200 server (estimate): no credible used market exists ("barely exist", Mercatus), so use new typical $370,000 (Mercatus) to $420,000 (Jarvislabs street high) + about $6,000 freight, cargo insurance (1% of $370,000 = $3,700) and setup = about $376,000 to $426,000.
- Used H100 SXM modules are cheaper per GPU than used PCIe cards (eBay asks: SXM median $19,550 vs PCIe median $32,000 on Sep 9, 2026, Caladan Semi) because SXM modules need an HGX baseboard host; this is why whole used HGX nodes at $180,000 to $195,000 ($22,500 to $24,400 per GPU) are the practical route for a small buyer.
- Sources conflict by 2x or more on used A100 80GB and on used H100 SXM. The best-dated primary observations (eBay asks on Sep 9 and GPU Dojo weekly eBay snapshots through Oct 22, 2026) sit above the "Q2 2026" ClusterBid estimates, which suggests the ClusterBid article is stale or modeled rather than observed.

### Gaps
- No eBay "sold listings" data could be read directly (eBay pages returned 403). All eBay figures are asks or tracker snapshots.
- No Thinkmate, Puget Systems, Lambda hardware, or Exxact full-system price for an 8x H100 or 8x H200 was found; Exxact shows only a barebone.
- No published Supermicro eStore starting price for an HGX B200 system was found.
- No used 8x H200 server price other than one eBay ask ($513,540) was found.
- Tom's Hardware and SemiAnalysis articles on secondary-market H100 prices were not surfaced by search.

## Key question 2: What is the monthly cost to run one 8-GPU server (10 to 12 kW) or a quarter or full rack in a Texas, Tennessee, or Reno colo, and what is the Bay Area reference?

### Takeaway
Public broker ranges for GPU-density racks (12 to 20 kW) are $140 to $285 per kW per month in Dallas, Houston, Nashville, and Reno, with wholesale (1 to 5 MW) asking rates of $125 to $195 per kW in those metros and $180 to $275 per kW in Silicon Valley; most named providers (TRG, Evocative, Switch, Hivelocity, Databank, Flexential) do not publish rate cards and require a quote. Industrial power in July 2026 was 7.07 cents/kWh in Texas, 7.13 in Tennessee, 10.04 in Nevada, and 25.11 in California (EIA), and Switch advertises 4.9 cents/kWh at its Reno campus.

### Cited Findings

#### Per-kW and per-rack colocation pricing by market (checked 2026-10-22)

| Market | Price | What it covers | Source date | Source |
|---|---|---|---|---|
| Dallas / Texas, single rack AI | $140 to $240 per kW; typical 10 to 25 kW racks; "best single-rack availability" | Broker ballpark | undated (2026) | [QuoteColo single-rack AI](https://www.quotecolo.com/single-rack-ai-colocation/) |
| Dallas-Fort Worth, 2026 benchmark | $96 per kW (standard 10 to 20 kW/rack, air); $120 per kW (40 to 60 kW/rack, rear-door HX); $150 per kW (80 to 120 kW/rack, direct-to-chip liquid); power cost basis $0.05/kWh; vacancy 3.2%; average lead time 18 months | Benchmark page; does not state whether rates are monthly | undated (2026) | [GPU Lease Index DFW](https://gpuleaseindex.com/ai-colocation/dallas-fort-worth-tx) |
| Dallas-Fort Worth, wholesale 1 to 5 MW | $130 to $170 per kW per month (JLL midyear 2025; CBRE Q1 2026 flat YoY) | Wholesale asking | Sep 7, 2026 | [GoDataCenters pricing by market](https://godatacenters.com/blog/colocation-pricing-by-market-2026) |
| Dallas rack tiers | high-density 48U 10 to 17 kW: $712 to $4,465 per month; 4-rack 20 kW/rack cage: $13,300 to $17,100 per month | Broker table (unit not stated; monthly implied) | undated (2026) | [QuoteColo Nashville page comparison table](https://www.quotecolo.com/colocation-hosting/tennessee/nashville/) |
| Houston, GPU inference rack 12 to 20 kW | $155 to $275 per kW per month; 8 to 12 kW cabinet $135 to $235; 20 to 30+ kW hot rack $195 to $335+; worked example 20 kW x $220 = $4,400 + network $800 to $2,300 = $5,800 to $8,700 per month | Broker ballpark | undated (2026; images dated 2026/09) | [QuoteColo Houston](https://www.quotecolo.com/colocation-hosting/texas/houston/) |
| Houston, Logix 42U cabinet, 36-month term | 30A 208V (4.99 kW A/B): $450 cabinet + $540 power + 1 Gbps DIA included = $990 per month; 20A 120V (1.92 kW): $675 per month | Published provider offer (low density only) | undated (2026) | [QuoteColo Houston](https://www.quotecolo.com/colocation-hosting/texas/houston/) |
| Houston, wholesale 1 to 5 MW | $130 to $160 per kW per month (JLL midyear 2025) | | Sep 7, 2026 | [GoDataCenters](https://godatacenters.com/blog/colocation-pricing-by-market-2026) |
| South Houston, GR1D liquid-cooled | from $180 per kW per month (20 kW rack = $3,600); 10 to 100+ kW per rack; N+1; no setup fee on 12+ month terms; bandwidth price not stated | Provider "from" price | undated (market table dated March 2026) | [GR1D host](https://gr1d.us/host) |
| Austin, rack tiers | high-density 48U 10 to 17 kW: $2,134 to $4,940 per month; 4-rack 20 kW cage $15,200 to $21,375 | Broker table | undated (2026) | [QuoteColo Houston comparison table](https://www.quotecolo.com/colocation-hosting/texas/houston/) |
| Austin and San Antonio, wholesale | $125 to $165 per kW per month (JLL midyear 2025) | | Sep 7, 2026 | [GoDataCenters](https://godatacenters.com/blog/colocation-pricing-by-market-2026) |
| Texas (anecdote) | $200 to $400 per kW per month, power $0.08 to $0.12/kWh, setup $1,000 to $5,000 | Reddit comment (low reliability) | Dec 2025 | [Reddit snapshot](https://reddit.sentinel-team.org/posts/1pputkr/snapshots/2025-12-20T05%3A00%3A23.111356Z) |
| TRG Datacenters (Houston HOU1 6 MW, HOU2 24 MW Q4 2026) | Quote only; "cross-connects are free, forever"; Colo+ includes 24/7 remote hands; up to 50 kW per cabinet | Provider | undated | [TRG Houston pricing resource](https://www.trgdatacenters.com/resource/houston-colocation-pricing-what-does-it-really-cost/) |
| Evocative Dallas | Not found (no published pricing) | | | |
| Nashville, GPU inference rack 12 to 20 kW | $165 to $275 per kW per month; 8 to 12 kW $145 to $235; 20 to 30+ kW $205 to $335+ | Broker ballpark; the rack-tier table on the same page is labeled "Atlanta" so it is not reliable for Nashville | undated (2026) | [QuoteColo Nashville](https://www.quotecolo.com/colocation-hosting/tennessee/nashville/) |
| Tennessee statewide | same per-kW ranges as Nashville | Broker | undated (2026) | [QuoteColo Tennessee](https://www.quotecolo.com/colocation-hosting/tennessee/) |
| Murfreesboro TN (MyDataSuites, 30 min from BNA) | No prices; up to 50 kW per rack; N+1; managed services billed hourly | Provider | undated | [MyDataSuites colocation](https://mydatasuites.com/colocation/) |
| Chattanooga | Not found (QuoteColo Chattanooga URL redirects to the statewide page; BroadbandLocators page is a placeholder) | | | [QuoteColo](https://www.quotecolo.com/colocation/us/tennessee/chattanooga/), [BroadbandLocators](https://www.broadbandlocators.com/colocation_tennessee_chattanooga.php) |
| Memphis | Not found (page lists pricing factors with no dollar figures) | | undated | [Broadband Trader Memphis](https://www.broadbandtrader.com/server-colocation-tennessee-memphis.php) |
| Reno, GPU inference rack 12 to 20 kW | $165 to $285 per kW per month; 8 to 12 kW $145 to $235; 20 to 30+ kW $200 to $335+; worked example 20 kW x $235 = $4,700 + network $900 to $2,400 = $6,100 to $9,100 per month; installs take 2 to 6 weeks | Broker ballpark; rack-tier table on the page is labeled "Las Vegas" (high-density 48U 10 to 17 kW $2,375 to $4,940) | undated (2026; images dated 2026/09) | [QuoteColo Reno](https://www.quotecolo.com/colocation-hosting/nevada/reno/) |
| Las Vegas and Reno, wholesale 1 to 5 MW | $145 to $195 per kW per month (JLL midyear 2025) | | Sep 7, 2026 | [GoDataCenters](https://godatacenters.com/blog/colocation-pricing-by-market-2026) |
| Nevada (Las Vegas vs Reno) | about $110 to $175 per kW per month | Broker (snippet only) | undated | [QuoteColo Nevada](https://www.quotecolo.com/colocation-hosting/nevada/) |
| Switch Tahoe Reno (Citadel) | Power "4.9 cents per kWh, 100% green"; "we can beat any colocation price guaranteed"; Nevada 4.6% sales and use tax (page) vs 2% (snippet; conflict); 75% reduction in business personal property tax; no state income tax; cabinets up to 55 kW (Baxtel) | Provider marketing; no per-kW colo rate published | undated | [Switch](https://switch.com/?p=29026), [Baxtel Switch Reno](https://baxtel.com/data-center/switch-tahoe-reno-the-citadel-campus) |
| Reno market overview | Providers: Switch (55 kW cabinets), NOVVA (deployments from 250 kW), EdgeCore (216 MW), Vantage NV1 (224 MW); Nevada industrial power June 2026 10.16 cents/kWh (EIA); TRIC about 4.9 cents/kWh with 100% renewables (unsourced FAQ) | Broker overview, no pricing | Sep 19, 2026 | [Brightlio Reno](https://brightlio.com/reno-colocation-data-center/) |
| Roller Network (Reno) | Cannot host GPU/AI density; design 5 kW average, 8.6 kW max per rack; full rack includes 2.1 kW and 1 Gbps (price on separate page not read) | Provider | undated (2026) | [Roller Network](https://roller.network/) |
| Silicon Valley / Bay Area | CBRE asking $180 to $275 per kW per month (H2 2025, unchanged in H1 2026); QuoteColo $200 to $350 per kW ("most expensive market"); Santa Clara broker $145 to $255 (8 to 12 kW) and $165 to $295 (GPU rack); vacancy 4.2% (CBRE H1 2026) | | Sep 7, 2026 and undated | [GoDataCenters](https://godatacenters.com/blog/colocation-pricing-by-market-2026), [QuoteColo single-rack AI](https://www.quotecolo.com/single-rack-ai-colocation/), [QuoteColo Santa Clara](https://www.quotecolo.com/colocation-hosting/california/santa-clara/) |
| National average, 250 to 500 kW, 8 primary NA markets | $196.25 per kW per month (H2 2025); CBRE expects above $200 in 2026 | | Sep 7, 2026 | [GoDataCenters](https://godatacenters.com/blog/colocation-pricing-by-market-2026) |
| Hivelocity (Dallas 1 and 8 other US sites) | No published pricing; "request a quote" | Provider | undated | [Hivelocity colocation](https://www.hivelocity.net/colocation/) |
| Databank, Flexential, TierPoint, Colocation America, Volico, Core Scientific, Applied Digital | Not found (no public GPU-density rate cards surfaced) | | | |

#### Add-on fees and terms (checked 2026-10-22)

| Item | Figure | Source date | Source |
|---|---|---|---|
| Committed power | $130 to $225 per kW allocated per month; metered overage $0.07 to $0.11/kWh | undated (2026) | [QuoteColo single-rack AI](https://www.quotecolo.com/single-rack-ai-colocation/) |
| Cross-connects | $100 to $400 per month each; $250 to $500 for 25 to 100G links | undated (2026) | [QuoteColo single-rack AI](https://www.quotecolo.com/single-rack-ai-colocation/) |
| Cross-connects (other guides) | install $500 to $1,500 one-time plus $100 to $300 per month; or $200 to $500 per month | undated (2026) | [IPTP colocation pricing](https://www.iptp.net/blog/colocation-pricing-breakdown/), [ClusterBid colo pricing guide](https://clusterbid.com/blog/gpu-colocation-pricing-guide-2026-power-space-interconnect) (snippets) |
| Remote hands | $150 to $300 per hour (main text) vs $3 to $5 per minute or $75 to $150 per hour (FAQ); page is inconsistent | undated (2026) | [QuoteColo single-rack AI](https://www.quotecolo.com/single-rack-ai-colocation/) |
| Remote hands (Tier III/IV) | $150 to $350 per hour, one-hour minimum; Equinix basic $150 to $250, smart hands $200 to $350 | undated (2026) | [IPTP](https://www.iptp.net/blog/colocation-pricing-breakdown/) (snippet) |
| Bandwidth | 1 to 10 Gbps "typically included"; 25 to 100G ports $400 to $1,800 per month; overage $0.01 to $0.03 per GB; IP transit 1 Gbps $300 to $800 per month | undated (2026) | [QuoteColo single-rack AI](https://www.quotecolo.com/single-rack-ai-colocation/), [IPTP](https://www.iptp.net/blog/colocation-pricing-breakdown/) |
| Minimum term | 12 to 24 months (flexible) or 12 to 36 months (locked); Logix Houston offer 36 months; GR1D waives setup at 12+ months | undated (2026) | [QuoteColo single-rack AI](https://www.quotecolo.com/single-rack-ai-colocation/), [QuoteColo Houston](https://www.quotecolo.com/colocation-hosting/texas/houston/), [GR1D](https://gr1d.us/host) |
| Hidden fees | "20 to 50% above quoted base rate" in year one; "25 to 30%" per another broker | undated (2026) | [IPTP](https://www.iptp.net/blog/colocation-pricing-breakdown/), [QuoteColo AI colo cost blog](https://www.quotecolo.com/blog/colocation-2/ai-colocation-pricing-cost/) (snippets) |

#### Electricity price floor (EIA Electric Power Monthly Table 5.6.A, July 2026, cents per kWh; checked 2026-10-22)

| State | Industrial | Commercial | Source |
|---|---|---|---|
| Texas | 7.07 | 8.47 | [EIA Table 5.6.A](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a) |
| Tennessee | 7.13 | 13.43 | same |
| Nevada | 10.04 | 9.72 | same |
| California | 25.11 | 30.56 | same |
| US total | 9.77 | 14.53 | same |

- Switch Reno advertises 4.9 cents/kWh (below the Nevada state industrial average) — [Switch](https://switch.com/?p=29026)
- GPU Lease Index DFW benchmark uses $0.05/kWh as its power cost basis — [GPU Lease Index DFW](https://gpuleaseindex.com/ai-colocation/dallas-fort-worth-tx)

### Inferences
- Monthly opex for one 8x H100 server in a Texas, Tennessee, or Reno retail colo (estimate): committed power 10 kW (the DGX H100 maximum is 10.2 kW; a 10 kW commit covers full load) x $140 to $285 per kW (broker GPU-rack ranges above) = $1,400 to $2,850; cross-connect $100 to $400; bandwidth $0 (1 to 10 Gbps included) to $500; remote hands 2 hours x $150 to $300 = $300 to $600; insurance about $165 (see KQ6). Total about $2,000 to $4,500 per month; midpoint used below: $2,900 per month.
- A raw-power floor at 10 kW x 24 x 30.4 = 7,300 kWh per month x 7.07 cents (Texas industrial) = $516 per month, or x 4.9 cents (Switch Reno claim) = $358. The colo per-kW charge ($1,400 to $2,850 for 10 kW) therefore embeds about 3 to 5x the bare energy cost (covering cooling PUE, space, redundancy, margin).
- For a quarter rack with high density (about 10 to 17 kW), broker rack-tier tables put Dallas at $712 to $4,465 per month, Austin and Reno at $2,134 to $4,940, and Nashville at $2,375 to $4,940 (labels on those tables are inconsistent; treat as ballpark). A full high-density rack is not sold as a unit; it is priced as 20 to 30+ kW at $195 to $335+ per kW, i.e., about $4,000 to $10,000 per month before network.
- Reno's per-kW colo rates are not lower than Texas in the public broker data, even though Switch's power is cheap; Nevada's state industrial rate (10.04 cents) is above Texas (7.07) and Tennessee (7.13).

### Gaps
- No named Texas, Tennessee, or Reno provider publishes a per-kW price for 10 to 20 kW GPU racks; all per-kW figures are broker ballparks or wholesale (1 to 5 MW) surveys. Quotes are required from TRG, Evocative, Databank, Flexential, Switch, Hivelocity, and others.
- No Chattanooga or Memphis pricing was found at all.
- Patmos (Dallas) full cabinet $1,200 per month plus $600 per month for 4 kW appeared in a search snippet, but the fetched page showed no prices, so it is unverified.
- No public figure for Core Scientific or Applied Digital style GPU hosting for a single server.

## Key question 3: What is the implied cost per GPU-hour of owning, at 100% and 50% utilization, over 3 and 5 years? (estimate)

### Takeaway
Estimate: owning a used 8x H100 SXM server in a Texas-class colo implies about $1.30 per GPU-hour at 100% utilization over 3 years ($2.60 at 50%) and about $1.00 at 100% over 5 years ($2.00 at 50%), before cost of capital, taxes, failures, and downtime. A new 8x H200 server implies about $1.85 (100%, 3-year) to $3.70 (50%, 3-year) and $1.35 to $2.70 over 5 years. Current rental indices are $2.88 to $3.75 per H100-hour and $4.59 to $5.88 per H200-hour, so ownership only clears rental at sustained utilization well above 50%.

### Cited Findings
Inputs used (all cited in KQ1, KQ2, KQ5, KQ6):
- Used 8x H100 server all-in capex about $184,500 (ServerPartDeals $180,000 plus freight, cargo insurance, setup) — [ServerPartDeals](https://serverpartdeals.com/products/dell-poweredge-xe9680-xeon-platinum-8462y-8x-nvidia-hgx-h100-80gb-sxm5-nvlink-ai-powered-refurbished-gpu-server), [QuoteColo](https://www.quotecolo.com/single-rack-ai-colocation/), [Warp](https://www.wearewarp.com/tools/how-to-ship/electronics)
- New 8x H200 server all-in capex about $376,000 (Mercatus typical $370,000 plus freight, insurance, setup) — [Mercatus H200](https://www.mercatus-ai.com/blog/h200-server-price)
- Monthly opex about $2,900 (10 kW x about $190 per kW midpoint, plus cross-connect, remote hands, insurance; see KQ2 inference)
- Residual value: American Compute forecasts a used HGX H100 node bought in 2026 retains 3 to 6% of original price (moderate) or 2 to 3% (conservative) after 36 months, 1 to 3% after 48 months — [American Compute](https://www.amcompute.com/gpu-server-values/h100); Mercatus assumes a $370,000 H200 system resells for $92,500 (25%) at 36 months — [Mercatus H200](https://www.mercatus-ai.com/blog/h200-server-price); ClusterBid puts H100 salvage at 60 months at $3,000 to $5,000 per GPU — [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-2026-used-h100-prices-resale-value-trading-volume)
- Hours: 8,760 per year per GPU; 8 GPUs = 70,080 GPU-hours per year
- Rental comparators (Oct 2026): Silicon Data neo-cloud H100 $2.88 (Oct 22), Ornn OCPI H100 $3.09 (Oct 21), GetDeploying median $3.75 (week of Oct 19); H200: Jarvislabs $4.59 on-demand, Ornn OCPI-H200 $5.88 (Oct 21) — see KQ4
- Latent Space (Oct 11, 2024) breakeven framing: at $50,000 per H100 all-in and a 5-year life, on-demand above $2.85/hr beats the stock market IRR and below $1.65/hr is an expected loss; the model assumed 100% allocation, which the author called unreasonable — [Latent Space, "$2 H100s"](https://www.latent.space/p/gpu-bubble)

### Inferences (all estimates; arithmetic shown)

Scenario A: used 8x H100 SXM server, Texas-class colo

| Line | 3-year | 5-year |
|---|---|---|
| Capex all-in | $184,500 | $184,500 |
| Residual at end (assume $20,000, within American Compute's 36-month moderate band of 3 to 6% of a roughly $285,000 original, and above its 48-month band) | -$20,000 | -$10,000 |
| Net capex | $164,500 | $174,500 |
| Opex at $2,900 per month | 36 x $2,900 = $104,400 | 60 x $2,900 = $174,000 |
| Total cost | $268,900 | $348,500 |
| GPU-hours at 100% | 3 x 70,080 = 210,240 | 5 x 70,080 = 350,400 |
| Cost per GPU-hour at 100% | $268,900 / 210,240 = $1.28 | $348,500 / 350,400 = $0.99 |
| GPU-hours at 50% | 105,120 | 175,200 |
| Cost per GPU-hour at 50% | $268,900 / 105,120 = $2.56 | $348,500 / 175,200 = $1.99 |

Scenario B: new 8x H200 server, same colo

| Line | 3-year | 5-year |
|---|---|---|
| Capex all-in | $376,000 | $376,000 |
| Residual at end (Mercatus 25% at 36 months = $92,500; assume 15% = $55,500 at 60 months, between the Mercatus 36-month figure and the Mercatus/Spheron ">60 month 25 to 35% floor" for H100, which looks optimistic against American Compute) | -$92,500 | -$55,500 |
| Net capex | $283,500 | $320,500 |
| Opex at $2,900 per month | $104,400 | $174,000 |
| Total cost | $387,900 | $494,500 |
| Cost per GPU-hour at 100% | $387,900 / 210,240 = $1.85 | $494,500 / 350,400 = $1.41 |
| Cost per GPU-hour at 50% | $387,900 / 105,120 = $3.69 | $494,500 / 175,200 = $2.82 |

Sensitivities (estimate):
- Cost of capital: 10% per year on $184,500 = $18,450 per year = $18,450 / 70,080 = +$0.26 per GPU-hour at 100% utilization, +$0.53 at 50%. On $376,000: +$0.54 at 100%, +$1.07 at 50%.
- Colo at the low end ($2,000 per month) lowers Scenario A 3-year 100% cost to ($164,500 + $72,000) / 210,240 = $1.12; at the high end ($4,500 per month) it rises to ($164,500 + $162,000) / 210,240 = $1.55.
- Zero residual on the H100 server changes the 3-year 100% figure to $288,900 / 210,240 = $1.37.
- These figures exclude GPU failures and replacement (see KQ6), downtime, software and engineering time, income tax, and the price the owner can actually sell compute for (marketplace floors were $1.33 to $1.73 per H100-hour in July 2026 per GPU Finder and AI Compute Tracker, see KQ4).

### Gaps
- No source gives a realized utilization rate for a single owner-operated 8-GPU node sold on a marketplace, so the 50% and 100% cases are assumptions, not observations.
- No source gives an observed resale price for a 5.5 to 6 year old H100 server (none exist yet; the H100 shipped in late 2022/2023).

## Key question 4: How fast are H100 and H200 rental prices falling, and what do analysts expect for 2027?

### Takeaway
H100 on-demand rates fell from above $8 per GPU-hour in 2023 to about $2 on marketplaces and $1.70 for 1-year contracts by late 2025, but have risen through 2026: the SemiAnalysis 1-year contract index gained about 40% from October 2025 to March 2026, and October 2026 indices show +10 to +26% over one month to one year (Ornn $3.09, Silicon Data $2.88, GetDeploying median $3.75). H200 indices also rose in autumn 2026 (Ornn $4.42 at end-August to $5.88 on Oct 21). The only 2027 forecasts found are from market blogs and point back down ($1 to $1.50 per H100-hour by 2027 to 2028) as Blackwell saturates; no SemiAnalysis or bank 2027 rental forecast was found.

### Cited Findings

#### H100 rental price timeline (per GPU-hour; checked 2026-10-22)

| Date | Price | Segment | Source date | Source |
|---|---|---|---|---|
| Mar 2023 | about $4.70 at launch, rising to over $8 | On-demand, shortage peak | Oct 11, 2024 | [Latent Space, Eugene Cheah](https://www.latent.space/p/gpu-bubble) |
| 2H 2023 | $6.62 | SemiAnalysis composite (hyperscaler-weighted, blended with contract survey) | undated page | [SemiAnalysis H100 index](https://gpu-index.semianalysis.com/) |
| Aug to Dec 2023 | $7.76 median | Hyperscaler | Dec 21, 2025 | [Silicon Data H100 price over time](https://www.silicondata.com/blog/h100-rental-price-over-time) |
| Start of 2024 | about $2.85 across multiple providers | On-demand | Oct 11, 2024 | [Latent Space](https://www.latent.space/p/gpu-bubble) |
| 1Q, 2Q, 3Q, 4Q 2024 | $5.78, $4.77, $4.44, $3.91 | SemiAnalysis composite | undated | [SemiAnalysis](https://gpu-index.semianalysis.com/) |
| Jun to Dec 2024 | hyperscaler $9.34; marketplace $2.58; neocloud $2.99 (medians) | | Dec 21, 2025 | [Silicon Data](https://www.silicondata.com/blog/h100-rental-price-over-time) |
| Aug 2024 | $1 to $2 | Auctioned short slices | Oct 11, 2024 | [Latent Space](https://www.latent.space/p/gpu-bubble) |
| 1Q 2025, 2Q 2025 | $3.60, $3.34 | SemiAnalysis composite | undated | [SemiAnalysis](https://gpu-index.semianalysis.com/) |
| Jan to May 2025 | hyperscaler $8.96; marketplace $2.29; neocloud $3.50 | | Dec 21, 2025 | [Silicon Data](https://www.silicondata.com/blog/h100-rental-price-over-time) |
| Jun 2025 | AWS cut on-demand P5 (H100) prices 44% and P5en (H200) 25% | Hyperscaler | Oct 14, 2026 | [GPUSmith H100 rental history](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| Jul to Dec 2025 | hyperscaler $6.26; marketplace $1.95; neocloud $3.33 | | Dec 21, 2025 | [Silicon Data](https://www.silicondata.com/blog/h100-rental-price-over-time) |
| Jul 2025 to Dec 2025 | $2.79, $2.90, $2.90, $2.84, $2.80, $2.81 (monthly) | SemiAnalysis composite | undated | [SemiAnalysis](https://gpu-index.semianalysis.com/) |
| Oct 2025 | $1.70 (low) | SemiAnalysis 1-year contract index | Aug 2, 2026 | [ColoPrice H100 rental guide](https://coloprice.com/guides/h100-rental-prices/) |
| Dec 9, 2025 to Jan 6, 2026 | $2.00 to $2.20 (+10% in four weeks) | Silicon Data on-demand index | Oct 14, 2026 | [GPUSmith](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| Jan, Feb, Mar 2026 | $2.82, $2.83, $2.80 | SemiAnalysis composite ("current" shown as $2.82) | undated | [SemiAnalysis](https://gpu-index.semianalysis.com/) |
| Mar 2026 | $2.35 (+40% from Oct 2025 low) | SemiAnalysis 1-year contract index | Aug 2, 2026 | [ColoPrice](https://coloprice.com/guides/h100-rental-prices/) |
| May 2026 | $2.95 median; neocloud $2.69 to $2.95 | Cross-provider | Oct 14, 2026 | [GPUSmith](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| Jun 21, 2026 | $2.16 median (normalized index) | | snippet | [fabryka.ai index](https://gpu-price-index.vercel.app/) |
| Jun 2026 | about $2.99 cohort median (AIMultiple); $4.29 five-provider median (ComputeTape) | | Oct 14, 2026 | [GPUSmith](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| Jul 2026 | $3.46 average (GetDeploying); $1.33 cheapest confirmed in stock (GPU Finder) | | Oct 14, 2026 | [GPUSmith](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| Jul 2026 | specialist on-demand median $3.88; marketplace floor $1.73 | Survey | Jul 2026 | [AI Compute Tracker](https://aicomputetracker.com/gpu-cloud/h100/) (snippet) |
| Aug 12, 2026 | about $2.80 spot (Bank of America, Vivek Arya) | | Oct 20, 2026 | [Shattered.io](https://shattered.io/h100-h200-b200-cloud-gpu-pricing-2026/) |
| Aug 18, 2026 | $2.77, +2% month over month, +33% year over year (Bank of America) | | Oct 20, 2026 | [Shattered.io](https://shattered.io/h100-h200-b200-cloud-gpu-pricing-2026/) |
| Aug 25, 2026 | about $3.38 median (AIMultiple) | | Oct 20, 2026 | [Shattered.io](https://shattered.io/h100-h200-b200-cloud-gpu-pricing-2026/) |
| Sep 13, 2026 | $3.84 average across 27 providers; "not falling over the last 90 days" | Mercatus GPU Index | snippet | [Mercatus GPU rental prices](https://www.mercatus-ai.com/blog/gpu-rental-prices) |
| Oct 4, 2026 | $2.59 | Ornn OCPI H100 SXM (volume-weighted transacted) | snippet | [Ornn OCPI](https://data.ornn.com/) |
| Oct 7, 2026 | $4.20 median across 16 providers, range $3.20 to $12.29 | List prices | snippet | [Uvik GPU price index](https://uvik.net/blog/gpu-price-index/) |
| Oct 20, 2026 | $3.12, +4.7% day, +17.7% month | Ornn OCPI H100 SXM | snippet | [Ornn OCPI](https://data.ornn.com/) |
| Oct 21, 2026 | $3.09, -1.0% day, +10.8% month | Ornn OCPI H100 SXM | Oct 21, 2026 20:00 UTC | [Ornn OCPI](https://data.ornn.com/) |
| Week of Oct 19, 2026 | $3.75 median on-demand across 40 providers; +11% over 4 weeks; +26% over 1 year | GetDeploying tracker | Oct 19, 2026 | [GetDeploying price trends](https://getdeploying.com/gpu-price-trends) |
| Oct 22, 2026 | $2.88 (neo-cloud), +10.3% over 7 days (page FAQ separately says $2.53) | Silicon Data SDH100RT | Oct 22, 2026 | [Silicon Data H100 index](https://www.silicondata.com/products/silicon-index/h100) |
| Oct 2026 provider list prices | Lambda H100 SXM $3.99 (8x), $4.29 (1x), PCIe $3.29 (1x); RunPod H100 SXM $3.99 secure / $2.69 community, PCIe $2.89 / $1.99; Vast.ai from $1.49; Google Cloud $10.98 | Rate cards | Lambda undated (2026); RunPod updated Oct 8, 2026 | [Lambda pricing](https://lambda.ai/pricing), [RunPod pricing](https://www.runpod.io/pricing), [Shattered.io](https://shattered.io/h100-h200-b200-cloud-gpu-pricing-2026/) |

#### H200 rental price points (per GPU-hour; checked 2026-10-22)

| Date | Price | Segment | Source date | Source |
|---|---|---|---|---|
| Apr 2026 | median H200 on-demand up about 28% year over year (Barrack AI) | | Oct 14, 2026 | [GPUSmith](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| May 2026 | $3.39 to $3.50 (Alatirok medians) | | Oct 14, 2026 | [GPUSmith](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| Jul 2026 | range $2.30 to $13.78, median about $4.00 (AIMultiple) | | Oct 14, 2026 | [GPUSmith](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| Aug 5, 2026 to Oct 16, 2026 | mean on-demand across 11 providers $5.95 to $6.20 (+4.2%); range Hyperbolic $3.99, Vast $4.24, RunPod $5.29, CoreWeave $6.31, AWS $7.91, Oracle $10.00, Azure $10.60, Google $10.85 | Tracker | Oct 16, 2026 | [Thunder Compute H200 pricing](https://www.thundercompute.com/blog/nvidia-h200-pricing) |
| Aug, Sep, Oct 2026 | month-end $4.42 (Aug, -21.4%), $5.58 (Sep, +26.2%), $5.88 (Oct 21, +5.4% MTD); Oct 21 daily $5.88, -4.5% day, +16.0% 30-day; since Jul 22 range $4.24 to $6.51 | Ornn OCPI-H200 | Oct 21, 2026 | [Ornn H200 market](https://data.ornn.com/markets/h200) |
| Sep 13, 2026 | $4.43 average across 20 providers, -0.8% over 30 days | Mercatus | snippet | [Mercatus GPU rental prices](https://www.mercatus-ai.com/blog/gpu-rental-prices) |
| Oct 2026 | Jarvislabs $4.59 on-demand, $2.29 spot; Nebius $4.50 / $2.45 spot; Vast.ai from $3.82; RunPod $5.29 secure / $3.59 community; AWS and Azure about $10.60; Oracle about $10.00; Google spot $3.72 | Rate cards | Oct 20, 2026; RunPod Oct 8, 2026 | [Jarvislabs H200 price](https://jarvislabs.ai/blog/h200-price), [RunPod pricing](https://www.runpod.io/pricing) |
| undated (2026) | GPU clouds median $5.40; hyperscalers $10.85; spot about 58% of on-demand | GetDeploying tables | Oct 19, 2026 page | [GetDeploying](https://getdeploying.com/gpu-price-trends) |

#### Forecasts for 2027 (checked 2026-10-22)

| Forecast | Who | Source date | Source |
|---|---|---|---|
| H100 holds $2 to $3 through 2026, then falls toward $1 to $1.50 "as Blackwell saturates in 2027 to 28", toward "power-plus-margin economics"; upward pressure from inference demand and fixed H100 supply; CME (Silicon Data) and ICE (Ornn) compute futures to give market-based outlook | ColoPrice (broker blog, "working base case, not a consensus") | Aug 2, 2026 | [ColoPrice](https://coloprice.com/guides/h100-rental-prices/) |
| "H100 marketplace rates likely keep drifting toward $1 an hour by mid-2027" as B200 absorbs premium demand; memory costs set the price floor for new chips through fiscal 2028 | Shattered.io (blog) | Oct 20, 2026 | [Shattered.io](https://shattered.io/h100-h200-b200-cloud-gpu-pricing-2026/) |
| H100 stays the cost-optimal choice through mid-2027, after which Blackwell pricing normalizes | emma.ms (vendor blog) | snippet | [emma.ms](https://www.emma.ms/blog/nvidia-h100-cloud-gpu) |
| H100 and H200 drift toward a "value tier" through 2026 and 2027; Bernstein projects a 2 to 2.5x increase in HBM contract prices for 2027, pushing GPU purchase prices up with a lag to rentals; committed capacity largely booked through Aug to Sep 2026; "lock in pricing sooner rather than later" | GPUSmith (blog) | Oct 14, 2026 | [GPUSmith](https://gpusmith.com/articles/en/h100-rental-price-history-trends) |
| "Analysts expect relatively stable H100 prices with minor adjustments" (no 2027 figure); historical peaks near $8 | Thunder Compute (vendor) | Oct 1, 2026 | [Thunder Compute market trends](https://www.thundercompute.com/blog/ai-gpu-rental-market-trends) |
| Prices falling "at least 40% per year", especially for small clusters; "don't buy new H100s" | Latent Space (2024 view) | Oct 11, 2024 | [Latent Space](https://www.latent.space/p/gpu-bubble) |
| SF Compute index | Not found. The site shows only a "Resell" widget with "Reserved price $3.00/gpu/hr" and "Realized price $4.29/gpu/hr" (GPU model not named, undated), no index or history | Oct 22, 2026 | [SF Compute](https://sfcompute.com/) |

### Inferences
- Decline rate 2023 to late 2025: SemiAnalysis composite fell from $6.62 (2H 2023) to $2.81 (Dec 2025), a 58% drop over about 2.25 years, roughly 32% per year; marketplace medians fell from $2.58 (2H 2024) to $1.95 (2H 2025), about 24% in a year (Silicon Data).
- 2026 reversed the trend: composite indices are flat to up (SemiAnalysis flat at $2.80 to $2.83 Jan to Mar 2026; Ornn +10.8% in the month to Oct 21; GetDeploying +26% year over year; Bank of America +33% year over year in August). The dip to about $2.00 to $2.16 (Dec 2025, Jun 2026 fabryka) now looks like the trough.
- Indices measure different things (transacted volume-weighted Ornn $3.09; neo-cloud Silicon Data $2.88; list-price medians $3.75 to $4.20), so the spread between a marketplace seller's achievable price (about $1.50 to $2.90) and list prices is wide. A solo owner selling on a marketplace should model realized revenue near the lower indices, not the list-price medians.
- H200 commands about a 35 to 90% premium over H100 depending on index (Ornn $5.88 vs $3.09; RunPod $5.29 vs $3.99).

### Gaps
- No SemiAnalysis, Barclays, or bank forecast for 2027 rental prices was found; the SemiAnalysis index page's 1-year contract column could not be read (it showed "loading").
- No dated 2025 H200 rental history was found; H200 history starts in April 2026 in the sources read.
- No Lambda or RunPod price-cut announcement was found; one tracker says RunPod's September 2026 repricing raised, not lowered, H100 serverless rates (snippet only, [usagepricing.com](https://www.usagepricing.com/blueprint/runpod)).
- SF Compute publishes no H100 index that I could find.

## Key question 5: How much does a used H100 lose per year, and what do buyers pay for 2 to 3 year old H100 servers?

### Takeaway
Observed asks put 2.5 to 3 year old 8x H100 servers at $180,000 to $215,000, about 63 to 75% of a new $285,000 system, while single used H100 SXM modules trade at about $17,500 to $24,000, roughly 60 to 80% of a $25,000 to $30,000 list card; published depreciation curves range from 18 to 27% per year (ClusterBid) to 75 to 85% retained at 24 months (ServerBuyback, Mercatus). Accounting lives are 5.5 to 6 years at CoreWeave, Microsoft, Alphabet, and Meta, while Michael Burry argues the economic life is 2 to 3 years and that hyperscalers understate depreciation by $176 billion over 2026 to 2028; a broker residual forecast for a used HGX H100 node bought in 2026 is only 3 to 6% of original price after 36 months.

### Cited Findings

#### Published depreciation and retention curves (checked 2026-10-22)

| Claim | Who | Source date | Source |
|---|---|---|---|
| H100 retained value by age (Mercatus tracker): 0 to 12 months 95 to 100%; 12 to 18 months 85 to 95%; 18 to 24 months 75 to 85%; 24 to 36 months 60 to 75%; 36 to 48 months 45 to 60%; past 60 months 25 to 35% floor; no H200 multi-year tracker exists yet | Spheron citing Mercatus | Oct 9, 2026 (modified Oct 19) | [Spheron GPU depreciation 2026](https://www.spheron.network/blog/gpu-depreciation-in-2026-how-fast-h100s-and-h200s-lose-value/) |
| 36-month resale of a $285,000 new H100 system (GPU resale only): conservative 30% about $62,000; mid 50 to 60% about $115,000; optimistic 70% about $146,000 | Mercatus | Jul 14, 2026 | [Mercatus H100 server price](https://www.mercatus-ai.com/blog/h100-server-price) |
| H200 system: 3-year resale $92,500 (25% of $370,000); H200 system pricing to decline about 10% per year, driven by B200 supply | Mercatus | Jul 8, 2026 | [Mercatus H200 server price](https://www.mercatus-ai.com/blog/h200-server-price) |
| 24-month retention: H100 SXM5 75 to 85%; H100 PCIe 70 to 82%; A100 SXM 80GB 60 to 80%; A100 PCIe 40GB 55 to 70%; L40S 60 to 75% | ServerBuyback (buyback dealer) | Jun 27, 2026 | [ServerBuyback index](https://serverbuyback.com/resources/gpu-resale-value-index/) |
| Annual depreciation: H100 SXM 22 to 25%; H100 PCIe 24 to 27%; H200 18 to 21%; A100 SXM 28 to 32%; A100 PCIe 40GB 35 to 38%; H100 SXM fell 35% in first 18 months (to about $18,500) then another 23% by month 30; residual 54 to 58% (table) vs 42% at 24 to 30 months (text; internal conflict); salvage at 60 months $3,000 to $5,000 per GPU (10 to 16%); projected 2029 H100 SXM value $3,500 to $5,500; refurbishers buy used clusters at 55 to 70% of original cost; lenders advance 55 to 65% LTV on new H100s, down from 75 to 80% in 2024; 245,000 units traded in Q1 2026; x86 servers retain 55 to 65% at 24 months | ClusterBid (no named data source) | Feb 2026 (cites "Q2 2026") | [ClusterBid secondary market 2026](https://clusterbid.com/blog/secondary-gpu-market-2026-used-h100-prices-resale-value-trading-volume) |
| Used HGX H100 node residual forecast for a deal signed in 2026 (share of original price, conservative / moderate): 12 months 11 to 19% / 19 to 42%; 24 months 5 to 7% / 7 to 14%; 36 months 2 to 3% / 3 to 6%; 48 months 1% / 1 to 3%; today's node value ($195,000) "sits above the 2026 band" | American Compute (June 2026 residual report) | page updated Oct 17, 2026 | [American Compute H100 server value](https://www.amcompute.com/gpu-server-values/h100) |
| Used H100 peaked at up to $50,000 per GPU in mid-2024 scarcity while retail held $25,000 to $40,000 from mid-2024 into early 2026; A100 purchase prices may fall another 10 to 15% through 2026; Azure retired V100 VMs about 7.5 years after launch and K80/P100/P40 implied 7 to 9 year lives; conclusion: GPUs retain value for roughly 5 to 7+ years; Gavin Baker argues 8 to 10 years; Meta reported about 9% annualized H100 failure rate in Llama 3 training | Hashrate Index (Luxor) | Apr 8, 2026 | [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/) |
| Used non-refurbished H100s sell at 60 to 70% of new (Compute Exchange, unverified); a 2018 T4 still rents at about $0.15/hr on Vast.ai | IntuitionLabs | Sep 5, 2026 | [IntuitionLabs](https://intuitionlabs.ai/articles/used-ai-gpu-prices-resale-trends) |
| Used H100 (18 to 30 months) sells at $22,500 to $25,500 | Mercatus | snippet | [Mercatus H100 resale value](https://www.mercatus-ai.com/blog/h100-resale-value) |

#### Accounting useful lives and the Burry debate (checked 2026-10-22)

| Claim | Source date | Source |
|---|---|---|
| CoreWeave raised the useful life of "technology equipment" from 5 to 6 years effective Jan 1, 2023, citing "continuous advancements in hardware performance, software optimization, and data center design improvements"; category covers CPUs, GPUs, SSDs, networking, memory; just over $13 billion of such assets at end of June 2025 | Nov 11, 2025 | [Motley Fool](https://www.fool.com/investing/2025/11/11/michael-burrys-latest-warning-could-be-bad-news-fo/), [Adiram's Substack](https://adirams.substack.com/p/a-look-at-coreweave) (snippet) |
| CoreWeave (March 2026 conference): six years "remains the appropriate depreciation assumption" with empirical support that usage could extend beyond it | Mar 8, 2026 | [MarketBeat](https://www.marketbeat.com/instant-alerts/coreweave-conference-insatiable-ai-demand-leaves-2026-compute-capacity-broadly-sold-out-2026-03-08/) (snippet) |
| CoreWeave CEO: 2020 A100s "remain fully booked" and 2022 H100s "command 95% of original rental prices" (company-supplied) | 2026 | [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/coreweave-proves-nvidias-aging-ai-154147477.html) (snippet) |
| Michael Burry: hyperscalers will understate depreciation by a cumulative $176 billion over 2026 to 2028 by stretching GPU useful lives; economic life closer to 2 to 3 years | Nov 11, 2025 | [Motley Fool](https://www.fool.com/investing/2025/11/11/michael-burrys-latest-warning-could-be-bad-news-fo/), [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/) |
| Burry later argued Nvidia's depreciation chart is built on modeled forward rental income over an assumed 8-year chip life, not secondary-market prices | 2026 | [BigGo Finance](https://finance.biggo.com/news/b8ae08f8-fdc6-4186-9e37-bbda41fe2188) (snippet) |
| Microsoft: server and network life 4 to 6 years (FY2023, about $3.7 billion less depreciation); Alphabet: servers 4 to 6 years (2023, about $3.9 billion); Meta: 5.5 years effective Jan 29, 2025 (about $2.92 billion); Amazon cut a subset from 6 to 5 years in 2025 ($677 million net income hit over nine months); Lambda 5 years; Nebius 4 years; CoreWeave 6 years | Oct 9, 2026 and Apr 8, 2026 | [Spheron](https://www.spheron.network/blog/gpu-depreciation-in-2026-how-fast-h100s-and-h200s-lose-value/), [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/) |

### Inferences
- Observed 2.5 to 3 year old XE9680 8x H100 asks ($180,000 to $215,000) against Mercatus's $285,000 typical new price imply 63 to 75% retention, which matches the Mercatus/Spheron "24 to 36 months: 60 to 75%" band and the ServerBuyback 24-month band, and is far above American Compute's forward residual bands (which project collapse to 3 to 6% by 2029). The two views are consistent only if most of the remaining value evaporates in the next 2 to 3 years as Blackwell volume lands.
- Implied straight-line loss on a used server bought today at $184,500 and sold in 3 years at $20,000 (American Compute moderate band) is about $55,000 per year, or about 30% of purchase price per year; sold at $60,000 (Mercatus conservative 30% of new) it is about $41,500 per year, or 22.5%.
- The accounting-life debate matters less to a sole proprietor than cash resale: every source agrees resale prices are far below book value on a 6-year straight line.

### Gaps
- No Barclays, SemiAnalysis, or lender-published depreciation curve was found; the lender LTV figures (55 to 65%) come from an unsourced ClusterBid article.
- No completed-sale (not ask) data for 2 to 3 year old H100 servers was found.
- The Mercatus H100 resale value page could not be fetched directly (figure from snippet).

## Key question 6: What does a solo owner need to run a colocated server remotely (IPMI, remote hands, spares, warranty, insurance), and what are failure rates?

### Takeaway
Meta's Llama 3 run on 16,384 H100s logged 419 unexpected interruptions in 54 days, with faulty GPUs (30.1%) and HBM3 memory (17.2%) the top causes, which Hashrate Index converts to about a 9% annualized per-GPU failure rate; a refurbisher-sourced dataset reports 4.2% year-one annualized failure for refurbished H100s versus 1.8% new and 5 to 7% by year three. Colo providers require the customer to insure the equipment; equipment-floater rates in 2026 run about $0.89 to $1.35 per $100 of value per year, and remote hands cost $150 to $350 per hour. No public price for a 3-year onsite warranty on an HGX H100 was found.

### Cited Findings

| Item | Figure | Source date | Source |
|---|---|---|---|
| Meta Llama 3 405B training: 16,384 H100 80GB GPUs, 54 days, 419 unexpected interruptions; faulty GPU 148 (30.1%); GPU HBM3 72 (17.2%); GPU SRAM 19 (4.5%); GPU system processor 17 (4.1%); network switch and cable 35 (8.4%); CPU 2; effective training time above 90%; only 3 incidents needed significant manual intervention | Jul 29, 2024 | [SDxCentral on Meta report](https://www.sdxcentral.com/news/meta-report-details-hundreds-of-gpu-and-hbm3-related-interruptions-to-llama-3-training-run/) |
| Same run: 466 total interruptions, 419 unexpected, 47 planned; about one unexpected failure every three hours | Jul 2024 | [3DTested](https://www.3dtested.com/tech-industry/artificial-intelligence/faulty-nvidia-h100-gpus-and-hbm3-memory-caused-half-of-the-failures-during-llama-3-training-one-failure-every-three-hours-for-metas-16384-gpu-training-cluster) (snippet) |
| Meta's data implies about 9% annualized H100 failure rate | Apr 8, 2026 | [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/) |
| Refurbished vs new H100 (2,000 refurbished units from three refurbishers): DOA 1.8% vs 0.3%; year-1 annualized failure 4.2% vs 1.8%; year-3 5 to 7% both; 22% of H100s need fan replacement at 24 months, $45 to $85 per fan; refurbished units run at 97 to 99% of new performance | Feb 2026 | [ClusterBid](https://clusterbid.com/blog/secondary-gpu-market-2026-used-h100-prices-resale-value-trading-volume) |
| Supermicro standard warranty: 3 years labor, 1 year parts on SuperServer products; special terms noted on invoice | undated | [Supermicro warranty](https://supermicro.com/support/warranty) (snippet) |
| Reseller 3-year NBD onsite extended warranty SKUs for Supermicro servers exist, tiered by server value (Australian resellers, $271.82 to $659.80 for low-value tiers); no HGX-class price found | undated | [Area9 store](https://store.area9.com.au/products/computergate-supermicro-server-extended-warranty-6000-3-year-nbd-on-site-response-time-parts-labour-remote-site-charges-apply-50km-of-cbd-1326013) (snippet) |
| Refurbished XE9680 at $180,000 includes Dell ProSupport through Nov 4, 2028 and a 30-day return window | undated | [ServerPartDeals](https://serverpartdeals.com/products/dell-poweredge-xe9680-xeon-platinum-8462y-8x-nvidia-hgx-h100-80gb-sxm5-nvlink-ai-powered-refurbished-gpu-server) |
| Colo insurance: "Colocation agreements, leases, and loans require you to insure your own equipment"; facility policy does not cover customer gear; all-risk property cover at replacement cost; certificates in 2 to 4 weeks; no premium published | undated | [American Compute GPU property insurance](https://www.amcompute.com/gpu-property-insurance) |
| Equipment floater rates: $1.35 per $100 of value per year (Stony Brook Research Foundation, effective Jul 1, 2026); $0.8923 per $100 base (Mississippi State specialty equipment); $1 per $100 (University of Illinois computer plan) | Jul 1, 2026 and undated | [Stony Brook equipment insurance](https://linguistics.stonybrook.edu/commcms/osp-ogm/post_award_management/Post_Award_Management_Financial_OGM/equipment_insurance), [Mississippi State](https://www.ocrm.msstate.edu/insurance/specialty-equipment), [UIUC](https://treasury.uillinois.edu/risk_management/property_insurance/computer_and_special_equipment_insurance) (snippets) |
| Generic small-business inland marine averages: $48 per month (TechInsurance), $29 per month (Insureon); items over $2,500 may need separate scheduling | undated | [TechInsurance](https://www.techinsurance.com/inland-marine-insurance/cost), [Insureon](https://www.insureon.com/small-business-insurance/inland-marine/cost) (snippets) |
| Remote hands: $150 to $300 per hour (QuoteColo); $150 to $350 per hour, one-hour minimum, higher after hours (IPTP); TRG Colo+ bundles 24/7 remote hands; TRG cross-connects free | undated (2026) | [QuoteColo](https://www.quotecolo.com/single-rack-ai-colocation/), [IPTP](https://www.iptp.net/blog/colocation-pricing-breakdown/), [TRG](https://www.trgdatacenters.com/resource/houston-colocation-pricing-what-does-it-really-cost/) |
| Cargo insurance for shipping: 1 to 3% of declared value; carrier liability $0.10 to $2.00 per lb | undated | [Warp](https://www.wearewarp.com/tools/how-to-ship/electronics) (snippet) |
| DGX H100 weight 287.6 lb, 8U; pieces over about 150 lb need two-person delivery | undated | [NVIDIA DGX H100 guide](https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html), [Warp](https://www.wearewarp.com/tools/how-to-ship/server-racks) |

### Inferences
- Insurance estimate: $180,000 insured value x 1.1% per year (midpoint of the $0.89 to $1.35 per $100 academic floater rates) = about $1,980 per year, about $165 per month. Commercial quotes for a sole proprietor in a colo may differ.
- Expected GPU failures (estimate): at a 4.2% to 9% annualized per-GPU rate, an 8-GPU server sees 0.34 to 0.72 GPU failures per year, i.e., about one GPU failure every 1.4 to 3 years. Without a transferable warranty, one SXM replacement costs about $17,500 to $24,000 at current eBay asks (KQ1), plus remote hands and downtime. That makes a unit with remaining OEM support (such as the ServerPartDeals XE9680 with ProSupport to Nov 2028) worth a premium.
- Remote operation needs: Dell XE9680 ships with iDRAC and Supermicro with IPMI/BMC as standard out-of-band management (general product knowledge; no page fetched in this session states it, so verify with the vendor spec sheet). Budget 1 to 3 remote-hands hours per month ($150 to $900) for reboots, drive swaps, and fan replacements, and hold spares for the parts the data says fail (fans at 24 months, $45 to $85 each).

### Gaps
- No public price for a 3-year onsite warranty on an HGX H100 or H200 system from Supermicro, Dell, or a reseller was found; quotes are required.
- No insurer publishes a premium for colocated GPU servers; the only rates found are university equipment floaters.
- No source gives failure rates for inference (versus training) workloads on H100 servers; Meta's data is from a 54-day training run.
- No source was fetched that confirms IPMI/iDRAC inclusion on the specific used units listed.
