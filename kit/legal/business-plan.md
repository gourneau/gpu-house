# Radiant Machines: business plan

**Prepared October 22, 2026. Owner: Joshua Gourneau, sole proprietor, Redwood City, California.**
This plan is written before the first dollar is spent so that the tax file shows the profit motive, the expected pre-tax return, and the decision rules that were set in advance (IRC 183 factors 1 and 2; IRC 7701(o)(2)). Every number comes from the research and model in the gpu-house repository (github.com/gourneau/gpu-house), read live on October 22, 2026. Numbers marked "measured" will be filled in from the November benchmark and replace the estimates.

## 1. What the business sells

Radiant Machines sells AI inference as a service: it rents GPU servers from cloud providers, runs open-weight language models on them with vLLM, and sells completions per token through (a) its own OpenAI-compatible API billed by Stripe and (b) the OpenRouter marketplace, which pays providers monthly in US dollars at the provider's posted price. Customers are developers and companies that want the newest open models at the lowest reliable price.

## 2. Why it can make money

Most open models on OpenRouter are commodities: 10 to 36 providers at a price floor that cannot pay for the hardware. A few large new models are not: on October 22, 2026, Tencent Hy4-preview (9.7 trillion tokens a week) had four providers, all at the lab's list price of $0.834 in / $2.501 out per million tokens; Step 5 Preview (3.0T tokens a week) had four at $1.00 / $2.70; GLM 5.3 (5.7T a week) had 36 with a median output price of $4.30 against a floor of $1.40. These models need an 8-GPU Blackwell-class node, which keeps the provider count low. Radiant Machines serves exactly these models, prices 5% under the floor, and competes on uptime and throughput, which OpenRouter measures and rewards with traffic.

## 3. Unit economics (estimates, to be replaced by the November measurement)

| Item | Value | Source |
|---|---|---|
| Hardware | one 8x NVIDIA B200 node | Vultr HGX B200, $3.50 per GPU-hour, $28.00 per node-hour, about $20,400 per month (vultr.com, checked 2026-10-22) |
| Throughput, Hy4-preview, conservative | 1,500 output tokens/s per GPU (12,000 per node) | mapped from DeepSeek-class benchmarks on 8x B200 (TRT-LLM, InferenceX); measured value: ______ |
| Revenue per GPU-hour at 100% utilization | Hy4 $20.53; Step 5 $23.39; GLM 5.3 $6.72 | model output, 5% under floor, 3 prompt tokens per completion token |
| Breakeven utilization against $3.50 rent | Hy4 17%; Step 5 15%; GLM 5.3 52% | model output |
| Demand available | at a 7% share of Hy4's OpenRouter tokens, about 330 B200s could be kept 70% busy; one node needs 0.3% | OpenRouter rankings and endpoints API, 2026-10-22 |
| Blended plan at 40% utilization, $100k/yr budget | revenue $9,159/month, cost $8,333/month, profit $826/month pre-tax | model output, conservative throughput |
| Same at 70% | profit $7,695/month | model output |
| Typical throughput case at 40% | profit $9,985/month | model output |

Expected pre-tax profit, 12 months from launch, $100k budget: +$10k at 40% utilization conservative, +$92k at 70%, +$120k at 40% typical. The business is expected to be profitable before tax at any utilization above about 36%.

## 4. How it starts: a staged commitment

| Date | Step | Spend | Decision rule |
|---|---|---|---|
| Oct 27 to Oct 31, 2026 | Business license and FBN, bank account, Stripe, cloud accounts, privacy policy and terms published, OpenRouter provider application submitted | under $500 | none |
| Nov 3 to Nov 7 | Gateway and serving stack live on one rented GPU; end-to-end test with a small model | about $500 | none |
| Nov 10 to Nov 14 | Rent an 8-GPU node for 2 to 3 days; benchmark Hy4-preview and GLM 5.3 with vllm bench serve | about $2,000 | record output tokens/s per GPU and time to first token; recompute revenue per GPU-hour |
| Nov 17 to Nov 21 | Public launch: API open to the public, pricing posted, first unrelated paying customer invoiced through Stripe; OpenRouter listing if approved | node month-to-month, about $20,400/month | launch only if measured revenue per GPU-hour at 100% exceeds $7.00 (2x rent) |
| Nov 24 to Dec 12 | Operate; weekly review of revenue per GPU-hour, utilization, uptime (target above 95%), error rate | month-to-month | re-price weekly; add Step 5 or Hy3 if capacity allows |
| Dec 15 to Dec 28 | Term decision | $25k (3 months) to $245k (12 months) prepaid | prepay only if measured revenue per GPU-hour at measured utilization exceeds $3.50; otherwise stop and record the result |
| Dec 29 to Dec 31 | Close the books; package records for the CPA | none | none |

Cash at risk before the term decision: about $23,000 (test weeks, setup, licenses). The prepaid term, if signed, buys guaranteed capacity on a GPU class that was gated and whose prices rose 10% to 40% during 2026; its deductibility in 2026 under the 12-month rule is a timing benefit on a real expense, not the reason for the business.

## 5. Milestones and what success looks like

| By | Milestone |
|---|---|
| Nov 21, 2026 | First paying customer invoiced; API public; OpenRouter feed live |
| Dec 15, 2026 | Four weeks of revenue; measured revenue per GPU-hour; OpenRouter decision received |
| Mar 31, 2027 | Monthly revenue above monthly rent for two consecutive months |
| Jun 30, 2027 | Second node or second model family; cumulative revenue above cumulative cost since launch |
| Dec 31, 2027 | Profitable year; evaluate owned hardware only if a measured configuration beats rental |

## 6. Risks and the planned responses

1. **Not listed on OpenRouter.** Sell direct through the Stripe API; apply again with a gap model; keep the node month-to-month until listed.
2. **Preview models change price or disappear.** Serve three models; re-price weekly; never prepay on one model's economics.
3. **Throughput below estimate.** The launch rule (2x rent at 100%) and the prepay rule (rent at measured utilization) stop the plan before money is committed.
4. **Node outage.** Health checks and auto-restart; accept a lower traffic share rather than overload.
5. **Rental prices change.** Rising prices justify the prepaid term; falling prices favor staying month-to-month. The decision is made in late December with current quotes.

## 7. Records kept from day one

Separate business bank account and card; Stripe and OpenRouter revenue exports; cloud invoices; the gateway's usage database (token counts and revenue per request); a weekly time log; monthly unit-economics review notes; this plan with dated revisions; signed contracts. The owner performs all of the work (material participation: "substantially all" test, Reg. 1.469-5T(a)(2)).

Signed: ______________________  Date: ______________
