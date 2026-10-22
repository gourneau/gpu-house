"""Scenario model for the GPU rental / inference business.

Reads data/params.json (every number there carries a source URL and a
"checked" date) and writes data/results.json plus data/results.md.

Run:  python -I model/model.py

All money is USD. All rates are per GPU-hour. The planning horizon is the
12 months starting on params["start_date"] (default 2026-12-01).
"""
import json
import math
import os
import sys
from datetime import date, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS = os.path.join(ROOT, "data", "params.json")
_SUFFIX = "" if os.environ.get("CASE", "conservative") == "conservative" else "_" + os.environ.get("CASE")
OUT_JSON = os.path.join(ROOT, "data", f"results{_SUFFIX}.json")
OUT_MD = os.path.join(ROOT, "data", f"results{_SUFFIX}.md")

HOURS_PER_MONTH = 730.0  # 8760 / 12
CASE = os.environ.get("CASE", "conservative")  # or "typical"


def tps_cell(tp):
    """Pick the throughput cell for the active case."""
    if CASE == "typical" and tp.get("tps_out_per_gpu_typical", {}).get("value") is not None:
        return tp["tps_out_per_gpu_typical"]
    return tp.get("tps_out_per_gpu", {})
UTILS = [0.20, 0.40, 0.70]
SPEND_LEVELS = [50_000, 100_000, 250_000]


def load_params():
    with open(PARAMS, "r", encoding="utf-8") as f:
        return json.load(f)


def hours_in_2026(start: date) -> float:
    end = date(2027, 1, 1)
    return max(0.0, (end - start).days * 24.0)


def v(x, name):
    """Pull the numeric value out of a {"value":..,"source":..} cell."""
    if isinstance(x, dict):
        if x.get("value") is None:
            raise ValueError(f"params: {name} has no value")
        return float(x["value"])
    if x is None:
        raise ValueError(f"params: {name} is null")
    return float(x)


# ---------------------------------------------------------------- revenue
def inference_rev_per_gpu_hour(model, gpu_key, price_point, util, P):
    """Revenue per GPU-hour from selling tokens.

    tps = output tokens/sec per GPU at the benchmark shape.
    ratio_in = input tokens per output token at that shape.
    price_point = "min" (undercut floor) or "median".
    """
    tp = model["throughput"].get(gpu_key)
    if tp is None or tps_cell(tp).get("value") is None:
        return None
    tps = v(tps_cell(tp), f"{model['slug']}.{gpu_key}.tps")
    ratio_bench = v(tp.get("ratio_in", {"value": 1.0}), "ratio_in")
    ratio_demand = v(model.get("ratio_in_demand", {"value": ratio_bench}), "ratio_in_demand")
    # Real traffic carries more prompt tokens than the benchmark shape. Bill
    # input at the demand mix and take a prefill haircut on decode throughput
    # for the extra prompt work (estimate, see params.assumptions).
    A = P.get("assumptions", {})
    haircut = float(A.get("prefill_haircut", {}).get("value", 0.8)) if ratio_demand > ratio_bench else 1.0
    undercut = float(A.get("undercut", {}).get("value", 0.05)) if price_point == "min" else 0.0
    p_in = v(model["openrouter"][f"{price_point}_in"], "p_in") * (1.0 - undercut)
    p_out = v(model["openrouter"][f"{price_point}_out"], "p_out") * (1.0 - undercut)
    tokens_out_per_hour = tps * haircut * 3600.0 * util
    rev = tokens_out_per_hour / 1e6 * (p_out + ratio_demand * p_in)
    return rev


def vast_rev_per_gpu_hour(gpu, util, P):
    """Revenue per GPU-hour from re-renting on Vast.ai at the median price."""
    price = v(gpu["vast_median_rent"], f"{gpu['key']}.vast_median_rent")
    fee = v(P["vast"]["host_fee"], "vast.host_fee")
    return price * (1.0 - fee) * util


# ------------------------------------------------------------------ taxes
def _ca_cap(P):
    c = P["tax"].get("ca_excess_business_loss_cap", {}).get("value")
    return float(c) if c is not None else v(P["tax"]["excess_business_loss_cap"], "cap")


def tax_saved_on_expense(net_loss, P):
    """Tax saved by a net business loss against W-2 income.
    Federal cap: IRC 461(l) 2026 single threshold. CA: its own threshold."""
    if net_loss <= 0:
        return 0.0
    fed_cap = v(P["tax"]["excess_business_loss_cap"], "cap")
    fed = min(net_loss, fed_cap) * v(P["tax"]["fed_rate"], "fed")
    ca = min(net_loss, _ca_cap(P)) * v(P["tax"]["ca_rate"], "ca")
    return fed + ca


def equipment_year1_deduction(capex, P):
    """Federal: 100% bonus. CA: Sec 179 ($25k, phased out dollar for dollar
    above $200k placed in service, R&TC 17255) + MACRS 5-yr mid-quarter Q4."""
    fed = capex
    limit = v(P["tax"]["ca_179_limit"], "ca179")
    phase = P["tax"].get("ca_179_phaseout_start", {}).get("value", 200000)
    limit = max(0.0, limit - max(0.0, capex - float(phase)))
    ca179 = min(capex, limit)
    ca_macrs_q4 = v(P["tax"]["ca_macrs_year1_q4_rate"], "macrs")  # 0.05
    ca = ca179 + (capex - ca179) * ca_macrs_q4
    return fed, ca


def tax_saved_equipment(capex, revenue_2026, opex_2026, P):
    fed_ded, ca_ded = equipment_year1_deduction(capex, P)
    fed_loss = max(0.0, fed_ded + opex_2026 - revenue_2026)
    ca_loss = max(0.0, ca_ded + opex_2026 - revenue_2026)
    fed_cap = v(P["tax"]["excess_business_loss_cap"], "cap")
    fed = min(fed_loss, fed_cap) * v(P["tax"]["fed_rate"], "fed")
    ca = min(ca_loss, _ca_cap(P)) * v(P["tax"]["ca_rate"], "ca")
    return fed + ca, fed_ded, ca_ded


# ---------------------------------------------------------- opportunities
def routing_share(model, price_point, undercut, P):
    """Estimated share of a model's OpenRouter traffic for a new provider.

    OpenRouter's default routing weights providers by the inverse square of
    price (see provider-routing docs). We price at (1 - undercut) x the current
    floor and compare against the sum of 1/p^2 over existing providers.
    sum_inv_sq_price is precomputed from the raw endpoints JSON (blended
    price per M tokens = out + 3 x in). This is an estimate; observed shares
    for floor-priced endpoints are much lower, so a cap is applied downstream.
    """
    orr = model["openrouter"]
    ratio_in = v(model.get("ratio_in_demand", {"value": 1.0}), "ratio_in_demand")
    p_new = (v(orr["min_out"], "min_out") + ratio_in * v(orr["min_in"], "min_in")) * (1.0 - undercut)
    if p_new <= 0:
        return 1.0
    w_new = 1.0 / (p_new ** 2)
    sis = orr.get("sum_inv_sq_price", {}).get("value")
    if sis is None:
        k = v(orr["providers"], "providers")
        p_med = v(orr["median_out"], "median_out") + ratio_in * v(orr["median_in"], "median_in")
        sis = k / (p_med ** 2) if p_med > 0 else 0.0
    return w_new / (w_new + sis)


def opportunities(P, undercut=None):
    gpus = {g["key"]: g for g in P["gpus"]}
    A = P.get("assumptions", {})
    undercut = float(A.get("undercut", {}).get("value", 0.05)) if undercut is None else undercut
    share_cap = A.get("new_provider_share_cap", {}).get("value")
    rows = []
    for m in P["models"]:
        orr = m["openrouter"]
        wt = orr.get("weekly_tokens", {}).get("value")
        k = orr.get("providers", {}).get("value")
        ratio_demand = v(m.get("ratio_in_demand", {"value": 1.0}), "ratio_in_demand")
        for gk, tp in m["throughput"].items():
            if gk not in gpus or tps_cell(tp).get("value") is None:
                continue
            g = gpus[gk]
            tps = v(tps_cell(tp), "tps")
            rev100 = inference_rev_per_gpu_hour(m, gk, "min", 1.0, P)
            p_in = v(orr["min_in"], "min_in") * (1.0 - undercut)
            p_out = v(orr["min_out"], "min_out") * (1.0 - undercut)
            ratio_bench = v(tp.get("ratio_in", {"value": 1.0}), "ratio_in")
            haircut = float(A.get("prefill_haircut", {}).get("value", 0.8)) if ratio_demand > ratio_bench else 1.0
            out_tokens_per_gpu_hour = tps * haircut * 3600.0
            cost_m1 = v(g["rates"]["m1"], "m1") if g["rates"]["m1"].get("value") is not None else None
            cost_m12 = v(g["rates"]["m12"], "m12") if g["rates"]["m12"].get("value") is not None else None
            share_model = routing_share(m, "min", undercut, P) if k else None
            share = share_model
            if share is not None and share_cap is not None:
                share = min(share, float(share_cap))
            cap_tokens_week = wt * share if (wt and share is not None) else None
            cap_out_tokens_week = cap_tokens_week / (1.0 + ratio_demand) if cap_tokens_week else None
            gpus_70 = cap_out_tokens_week / (168.0 * 0.7 * out_tokens_per_gpu_hour) if cap_out_tokens_week else None
            rev_week_cap = cap_out_tokens_week / 1e6 * (p_out + ratio_demand * p_in) if cap_out_tokens_week else None
            breakeven_util_m12 = (cost_m12 / rev100) if (cost_m12 and rev100 > 0) else None
            breakeven_util_m1 = (cost_m1 / rev100) if (cost_m1 and rev100 > 0) else None
            rows.append({
                "model": m["slug"], "gpu": gk, "gpus_per_replica": tp.get("gpus_per_replica"),
                "tps_out_per_gpu": tps, "ratio_in_demand": ratio_demand, "prefill_haircut": haircut,
                "price_in_new": p_in, "price_out_new": p_out,
                "rev_per_gpu_hour_100": rev100,
                "cost_m1": cost_m1, "cost_m12": cost_m12,
                "margin_100_m12": (rev100 - cost_m12) if cost_m12 else None,
                "margin_100_m1": (rev100 - cost_m1) if cost_m1 else None,
                "breakeven_util_m1": breakeven_util_m1,
                "breakeven_util_m12": breakeven_util_m12,
                "providers": k, "weekly_tokens": wt,
                "share_model": share_model, "share_est": share,
                "capturable_tokens_week": cap_tokens_week,
                "capturable_rev_week": rev_week_cap,
                "gpus_supported_at_70pct": gpus_70,
                "revenue_per_week_per_gpu_at_70pct": rev100 * 0.7 * 168.0,
            })
    rows.sort(key=lambda r: (-(r["margin_100_m12"] or -1e9)))
    return rows


# -------------------------------------------------------------- scenarios
def rented_scenario(name, term, gpu, rev_fn, S, P, start, prepay_fraction, deductible_2026_fn, exit_text, lockin_text, node_size=1):
    """Generic rented-GPU scenario.

    term: "ondemand" | "m1" | "m3" | "m12"  (rate key on the gpu record)
    S: 12-month total spend. N GPUs = S / (rate * 8760).
    prepay_fraction: fraction of S that is paid up front in 2026.
    deductible_2026_fn(S, N, rate, h2026) -> 2026 deductible dollars.
    """
    rate = v(gpu["rates"][term], f"{gpu['key']}.{term}")
    N = S / (rate * 8760.0)
    h2026 = hours_in_2026(start)
    monthly_cost = N * rate * HOURS_PER_MONTH
    ded_2026 = deductible_2026_fn(S, N, rate, h2026)
    rows = []
    for u in UTILS:
        rph = rev_fn(u)
        rev_month = N * rph * HOURS_PER_MONTH
        rev_2026 = N * rph * h2026
        rev_12mo = N * rph * 8760.0
        cost_12mo = S
        net_loss_2026 = ded_2026 - rev_2026
        tax = tax_saved_on_expense(net_loss_2026, P)
        rows.append({
            "util": u,
            "rev_per_gpu_hour": rph,
            "rev_month": rev_month,
            "profit_month": rev_month - monthly_cost,
            "rev_2026": rev_2026,
            "deductible_2026": ded_2026,
            "net_loss_2026": net_loss_2026,
            "tax_saved_2026": tax,
            "rev_12mo": rev_12mo,
            "profit_12mo_pretax": rev_12mo - cost_12mo,
            "after_tax_12mo": rev_12mo - cost_12mo + tax,
        })
    node_month_cost = node_size * rate * HOURS_PER_MONTH
    return {
        "scenario": name,
        "gpu": gpu["key"],
        "term": term,
        "rate_per_gpu_hour": rate,
        "spend_12mo": S,
        "gpus": N,
        "gpus_rounded": max(1, round(N)),
        "node_size": node_size,
        "node_month_cost": node_month_cost,
        "node_months_affordable": S / node_month_cost,
        "whole_nodes_12mo": math.floor(N / node_size),
        "monthly_cost": monthly_cost,
        "cash_at_risk": S * prepay_fraction,
        "hours_2026": h2026,
        "exit": exit_text,
        "lock_in": lockin_text,
        "by_util": rows,
    }


def staged_scenario(name, prepay_term, gpu, rev_fn, S, P, start, test_start, node_size, decide_date):
    """Test month-to-month from test_start to Dec 31, then on decide_date prepay
    a 3-month or 12-month term that starts Jan 1, 2027. S = the 12-month budget
    at the prepaid rate; the test weeks are paid on top at the month-to-month rate.
    The December prepayment is deductible in 2026 under the 12-month rule when it
    is non-refundable and the term ends within 12 months (CPA to confirm)."""
    rate_pre = v(gpu["rates"][prepay_term], f"{gpu['key']}.{prepay_term}")
    tr = gpu["rates"].get("test_rate", {})
    rate_m1 = v(tr, "test_rate") if tr.get("value") is not None else v(gpu["rates"]["m1"], f"{gpu['key']}.m1")
    N = S / (rate_pre * 8760.0)
    h_test = hours_in_2026(test_start)
    test_cost = N * rate_m1 * h_test
    prepay = S * (0.25 if prepay_term == "m3" else 1.0)
    ded_2026 = test_cost + prepay
    monthly_cost = N * rate_pre * HOURS_PER_MONTH
    rows = []
    for u in UTILS:
        rph = rev_fn(u)
        rev_2026 = N * rph * h_test
        rev_month = N * rph * HOURS_PER_MONTH
        rev_12mo = N * rph * 8760.0
        net_loss_2026 = ded_2026 - rev_2026
        tax = tax_saved_on_expense(net_loss_2026, P)
        rows.append({
            "util": u,
            "rev_per_gpu_hour": rph,
            "rev_month": rev_month,
            "profit_month": rev_month - monthly_cost,
            "rev_2026": rev_2026,
            "deductible_2026": ded_2026,
            "net_loss_2026": net_loss_2026,
            "tax_saved_2026": tax,
            "rev_12mo": rev_12mo + rev_2026,
            "profit_12mo_pretax": rev_12mo + rev_2026 - S - test_cost,
            "after_tax_12mo": rev_12mo + rev_2026 - S - test_cost + tax,
        })
    node_month_cost = node_size * rate_pre * HOURS_PER_MONTH
    return {
        "scenario": name,
        "gpu": gpu["key"],
        "term": prepay_term,
        "rate_per_gpu_hour": rate_pre,
        "test_rate_per_gpu_hour": rate_m1,
        "test_start": test_start.isoformat(),
        "decide_date": decide_date,
        "test_cost_2026": test_cost,
        "prepay_dec_2026": prepay,
        "spend_12mo": S + test_cost,
        "gpus": N,
        "gpus_rounded": max(1, round(N)),
        "node_size": node_size,
        "node_month_cost": node_month_cost,
        "node_months_affordable": S / node_month_cost,
        "whole_nodes_12mo": math.floor(N / node_size),
        "monthly_cost": monthly_cost,
        "cash_at_risk": prepay + test_cost,
        "hours_2026": h_test,
        "exit": "Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end." if prepay_term == "m3" else "Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.",
        "lock_in": "None during the test; then 3 months." if prepay_term == "m3" else "None during the test; then 12 months.",
        "by_util": rows,
    }


def owned_scenario(S, gpu_key, rev_fn, P, start):
    """Owned servers in colocation. S = capex budget."""
    hw = P["owned"][gpu_key]
    capex_per_gpu = v(hw["capex_per_gpu"], "capex_per_gpu")
    colo_per_gpu_month = v(hw["colo_per_gpu_month"], "colo")
    N = S / capex_per_gpu
    h2026 = hours_in_2026(start)
    months_2026 = h2026 / HOURS_PER_MONTH
    opex_month = N * colo_per_gpu_month
    opex_2026 = opex_month * months_2026
    rows = []
    for u in UTILS:
        rph = rev_fn(u)
        rev_month = N * rph * HOURS_PER_MONTH
        rev_2026 = N * rph * h2026
        tax, fed_ded, ca_ded = tax_saved_equipment(S, rev_2026, opex_2026, P)
        rev_12mo = N * rph * 8760.0
        rows.append({
            "util": u,
            "rev_per_gpu_hour": rph,
            "rev_month": rev_month,
            "profit_month": rev_month - opex_month,
            "rev_2026": rev_2026,
            "deductible_2026_fed": fed_ded + opex_2026,
            "deductible_2026_ca": ca_ded + opex_2026,
            "tax_saved_2026": tax,
            "rev_12mo": rev_12mo,
            "profit_12mo_pretax_cash": rev_12mo - opex_month * 12 - S,
            "after_tax_12mo_cash": rev_12mo - opex_month * 12 - S + tax,
        })
    return {
        "scenario": "4. Own used servers in colocation",
        "gpu": gpu_key,
        "term": "own",
        "capex": S,
        "gpus": N,
        "gpus_rounded": max(1, round(N)),
        "monthly_cost": opex_month,
        "cash_at_risk": S,
        "hours_2026": h2026,
        "exit": "Sell used hardware on the secondary market (weeks to months); cancel colo per contract.",
        "lock_in": "Capital is sunk; resale value falls every quarter.",
        "by_util": rows,
    }


def build(P):
    start = datetime.strptime(P["start_date"], "%Y-%m-%d").date()
    gpus = {g["key"]: g for g in P["gpus"]}
    out = {"case": CASE, "start_date": P["start_date"], "hours_2026": hours_in_2026(start),
           "unit_economics": [], "scenarios": [], "opportunities": opportunities(P)}

    # ---- D. unit economics table: every model x gpu at min and median price
    for m in P["models"]:
        for gk in m["throughput"]:
            if gk not in gpus:
                continue
            g = gpus[gk]
            for pp in ("min", "median"):
                for u in [1.0] + UTILS:
                    rph = inference_rev_per_gpu_hour(m, gk, pp, u, P)
                    if rph is None:
                        continue
                    out["unit_economics"].append({
                        "model": m["slug"], "gpu": gk, "price_point": pp, "util": u,
                        "rev_per_gpu_hour": rph,
                        "cost_ondemand": v(g["rates"]["ondemand"], "od"),
                        "cost_m12": v(g["rates"]["m12"], "m12"),
                        "gpus_per_replica": m["throughput"][gk].get("gpus_per_replica"),
                    })

    # ---- plans: each plan = one GPU type, node size and model mix
    for plan in P["plans"]:
        gk = plan["gpu"]
        g = gpus[gk]
        node_size = int(plan.get("node_size", 1))
        chosen = [m for m in P["models"] if m["slug"] in plan["models"] and gk in m["throughput"]
                  and tps_cell(m["throughput"][gk]).get("value") is not None]
        if not chosen:
            continue
        pp = plan.get("price_point", "min")

        def blend_rev(u, chosen=chosen, gk=gk, pp=pp):
            vals = [inference_rev_per_gpu_hour(m, gk, pp, u, P) for m in chosen]
            vals = [x for x in vals if x is not None]
            return sum(vals) / len(vals)

        def vast_rev(u, g=g):
            return vast_rev_per_gpu_hour(g, u, P)

        def hybrid_rev(u, g=g, blend_rev=blend_rev):
            # inference on sold hours; idle hours re-rented on Vast at a fill rate
            fill = v(P["vast"]["idle_fill_rate"], "fill")
            return blend_rev(u) + vast_rev_per_gpu_hour(g, (1.0 - u) * fill, P)

        has_vast = g.get("vast_median_rent", {}).get("value") is not None
        for S in SPEND_LEVELS:
            rows = []
            # 1. month-to-month, deduct only hours used in 2026
            rows.append(rented_scenario(
                "1. Month-to-month, inference", "m1", g, blend_rev, S, P, start,
                prepay_fraction=1.0 / 12.0,
                deductible_2026_fn=lambda S, N, r, h: N * r * h,
                exit_text="Cancel at the end of any month.",
                lockin_text="None.", node_size=node_size))
            # 2a. 3-month prepaid, renewed 4x. First term prepaid in 2026.
            rows.append(rented_scenario(
                "2a. 3-month prepaid, inference", "m3", g, blend_rev, S, P, start,
                prepay_fraction=0.25,
                deductible_2026_fn=lambda S, N, r, h: S * 0.25,
                exit_text="Walk away at the end of a 3-month term.",
                lockin_text="3 months at a time.", node_size=node_size))
            # 2b. 12-month prepaid in Dec 2026 (12-month rule)
            rows.append(rented_scenario(
                "2b. 12-month prepaid, inference", "m12", g, blend_rev, S, P, start,
                prepay_fraction=1.0,
                deductible_2026_fn=lambda S, N, r, h: S,
                exit_text="Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.",
                lockin_text="12 months, non-refundable.", node_size=node_size))
            # 3. backup: resell GPU time on Vast (month-to-month and 12-month)
            if has_vast:
                rows.append(rented_scenario(
                    "3a. Month-to-month, resell on Vast", "m1", g, vast_rev, S, P, start,
                    prepay_fraction=1.0 / 12.0,
                    deductible_2026_fn=lambda S, N, r, h: N * r * h,
                    exit_text="Cancel at the end of any month.",
                    lockin_text="None.", node_size=node_size))
                rows.append(rented_scenario(
                    "3b. 12-month prepaid, resell on Vast", "m12", g, vast_rev, S, P, start,
                    prepay_fraction=1.0,
                    deductible_2026_fn=lambda S, N, r, h: S,
                    exit_text="Resell reserved time or ride it out.",
                    lockin_text="12 months, non-refundable.", node_size=node_size))
            # 4. owned (inference), 4b. owned, resell on Vast (the only legal Vast route)
            if gk in P["owned"] and P["owned"][gk]["capex_per_gpu"].get("value") is not None:
                rows.append(owned_scenario(S, gk, blend_rev, P, start))
                if has_vast:
                    o = owned_scenario(S, gk, vast_rev, P, start)
                    o["scenario"] = "4b. Own servers in colocation, resell time on Vast"
                    rows.append(o)
            # 5. hybrid: 12-month prepaid, inference first, idle hours on Vast
            if has_vast:
                rows.append(rented_scenario(
                    "5. Hybrid: 12-month prepaid, inference + Vast on idle hours", "m12", g, hybrid_rev, S, P, start,
                    prepay_fraction=1.0,
                    deductible_2026_fn=lambda S, N, r, h: S,
                    exit_text="Resell reserved time; Vast listing can stop any time.",
                    lockin_text="12 months, non-refundable.", node_size=node_size))
            # 6. staged: test month-to-month in Nov/Dec, prepay in late Dec for a term starting Jan 1
            test_start = datetime.strptime(P.get("test_start_date", "2026-11-15"), "%Y-%m-%d").date()
            decide = P.get("decide_date", "2026-12-28")
            rows.append(staged_scenario("6a. Staged: test month-to-month, then 3-month prepaid", "m3", g, blend_rev, S, P, start, test_start, node_size, decide))
            rows.append(staged_scenario("6b. Staged: test month-to-month, then 12-month prepaid", "m12", g, blend_rev, S, P, start, test_start, node_size, decide))
            for r in rows:
                r["budget"] = S
                if r["scenario"].startswith(("3a", "3b", "5.")):
                    r["blocked_for_rented"] = True
                    r["block_reason"] = "Vast hosts must own the hardware and keep it on their premises; rental contracts ban resale. Comparison only."
                r["plan"] = plan["key"]
                r["plan_label"] = plan["label"]
                r["models"] = [m["slug"] for m in chosen]
                r["price_point"] = pp
            out["scenarios"].extend(rows)
    return out


def fmt_money(x):
    return f"${x:,.0f}"


def write_md(out):
    L = []
    L.append(f"# Model results (start {out['start_date']}, {out['hours_2026']:.0f} GPU-hours left in 2026 per GPU)\n")
    L.append("## Unit economics: revenue per GPU-hour at 100% utilization\n")
    L.append("| Model | GPU | Price point | Rev/GPU-hr @100% | @20% | @40% | @70% | On-demand cost | 12-mo cost |")
    L.append("|---|---|---|---:|---:|---:|---:|---:|---:|")
    ue = out["unit_economics"]
    keys = sorted({(r["model"], r["gpu"], r["price_point"]) for r in ue})
    for (m, g, pp) in keys:
        rows = {r["util"]: r for r in ue if (r["model"], r["gpu"], r["price_point"]) == (m, g, pp)}
        r1 = rows[1.0]
        L.append(f"| {m} | {g} | {pp} | {r1['rev_per_gpu_hour']:.2f} | {rows[0.2]['rev_per_gpu_hour']:.2f} | {rows[0.4]['rev_per_gpu_hour']:.2f} | {rows[0.7]['rev_per_gpu_hour']:.2f} | {r1['cost_ondemand']:.2f} | {r1['cost_m12']:.2f} |")
    L.append("\n## Scenarios\n")
    for s in out["scenarios"]:
        L.append(f"### {s['scenario']} | {s['gpu']} | spend {fmt_money(s.get('spend_12mo', s.get('capex', 0)))}\n")
        L.append(f"GPUs: {s['gpus']:.2f} (about {s['gpus_rounded']}). Monthly cost: {fmt_money(s['monthly_cost'])}. Cash at risk: {fmt_money(s['cash_at_risk'])}. Lock-in: {s['lock_in']} Exit: {s['exit']}\n")
        L.append("| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |")
        L.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for r in s["by_util"]:
            ded = r.get("deductible_2026", r.get("deductible_2026_fed"))
            pre = r.get("profit_12mo_pretax", r.get("profit_12mo_pretax_cash"))
            aft = r.get("after_tax_12mo", r.get("after_tax_12mo_cash"))
            L.append(f"| {r['util']:.0%} | {r['rev_per_gpu_hour']:.2f} | {fmt_money(r['rev_month'])} | {fmt_money(r['profit_month'])} | {fmt_money(r['rev_2026'])} | {fmt_money(ded)} | {fmt_money(r['tax_saved_2026'])} | {fmt_money(r['rev_12mo'])} | {fmt_money(pre)} | {fmt_money(aft)} |")
        L.append("")
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


def main():
    P = load_params()
    out = build(P)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    write_md(out)
    print(f"wrote {OUT_JSON} and {OUT_MD}: {len(out['scenarios'])} scenario rows, {len(out['unit_economics'])} unit-econ rows")


if __name__ == "__main__":
    main()
