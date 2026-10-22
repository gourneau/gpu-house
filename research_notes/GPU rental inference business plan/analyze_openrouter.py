"""Compute per-model provider counts and price stats from OpenRouter endpoint JSON.
Run:  python -I analyze_openrouter.py "<dir with raw_openrouter_*.json>" weekly_tokens.json > openrouter_tables_generated.md
Prices are converted from $/token (API) to $/M tokens. Checked 2026-10-22.
"""
import json, glob, os, statistics, sys
from collections import defaultdict

D = sys.argv[1]
weekly = {}
if len(sys.argv) > 2 and os.path.exists(sys.argv[2]):
    weekly = json.load(open(sys.argv[2], encoding="utf-8"))

models = {m["id"]: m for m in json.load(open(os.path.join(D, "raw_openrouter_models.json"), encoding="utf-8"))["data"]}

def pm(x):
    return float(x) * 1_000_000 if x not in (None, "") else None

def fmt(x, nd=3):
    if x is None:
        return "n/a"
    return f"{x:.{nd}f}".rstrip("0").rstrip(".") if nd else str(x)

def tok(n):
    if n is None: return "n/a"
    for u, v in (("T", 1e12), ("B", 1e9), ("M", 1e6)):
        if n >= v: return f"{n/v:.3g}{u}"
    return str(n)

rows = []
details = []
prov_models = defaultdict(set)
prov_ratio_out = defaultdict(list)
prov_ratio_in = defaultdict(list)
prov_floor = defaultdict(int)
prov_quant = defaultdict(list)

for f in sorted(glob.glob(os.path.join(D, "raw_openrouter_endpoints_*.json"))):
    d = json.load(open(f, encoding="utf-8"))["data"]
    mid = d["id"]
    eps = d.get("endpoints", [])
    if not eps:
        rows.append(dict(id=mid, n_prov=0, n_ep=0, ctx=models.get(mid, {}).get("context_length"), min_in=None, med_in=None, min_out=None, med_out=None, max_out=None, floor_prov="none"))
        continue
    # cheapest endpoint per distinct provider (by output price, then input price); skip $0 endpoints
    best = {}
    for e in eps:
        pi, po = pm(e["pricing"]["prompt"]), pm(e["pricing"]["completion"])
        if pi is None or po is None or (pi == 0 and po == 0):
            continue
        p = e["provider_name"]
        if p not in best or (po, pi) < (pm(best[p]["pricing"]["completion"]), pm(best[p]["pricing"]["prompt"])):
            best[p] = e
    ins = [pm(e["pricing"]["prompt"]) for e in best.values()]
    outs = [pm(e["pricing"]["completion"]) for e in best.values()]
    ctx = models.get(mid, {}).get("context_length") or max(e["context_length"] for e in eps)
    min_out = min(outs) if outs else None
    min_in = min(ins) if ins else None
    floor = [p for p, e in best.items() if pm(e["pricing"]["completion"]) == min_out]
    rows.append(dict(id=mid, n_prov=len(best), n_ep=len(eps), ctx=ctx,
                     min_in=min_in, med_in=statistics.median(ins) if ins else None,
                     min_out=min_out, med_out=statistics.median(outs) if outs else None,
                     max_out=max(outs) if outs else None, floor_prov=", ".join(sorted(floor))))
    for p, e in best.items():
        prov_models[p].add(mid)
        if min_out: prov_ratio_out[p].append(pm(e["pricing"]["completion"]) / min_out)
        if min_in: prov_ratio_in[p].append(pm(e["pricing"]["prompt"]) / min_in)
        if pm(e["pricing"]["completion"]) == min_out: prov_floor[p] += 1
        prov_quant[p].append(e.get("quantization") or "unknown")
    # detail table: every endpoint
    lines = [f"### {mid}", "",
             f"Source: https://openrouter.ai/api/v1/models/{mid}/endpoints (checked 2026-10-22). Distinct providers: {len(best)}. Endpoints: {len(eps)}. Model context: {ctx}.", "",
             "| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for e in sorted(eps, key=lambda e: (pm(e["pricing"]["completion"]), pm(e["pricing"]["prompt"]))):
        pr = e["pricing"]
        up = e.get("uptime_last_1d")
        lines.append(f"| {e['provider_name']} | {e.get('tag','')} | {e.get('quantization') or 'unknown'} | {e['context_length']} | {e.get('max_completion_tokens') or ''} | {fmt(pm(pr['prompt']),4)} | {fmt(pm(pr['completion']),4)} | {fmt(pm(pr.get('input_cache_read')),4)} | {fmt(up,1) if up is not None else 'n/a'} | {e.get('status')} |")
    details.append("\n".join(lines))

# summary table sorted by weekly tokens (if known) then provider count
def wk(mid):
    w = weekly.get(mid)
    return w["tokens"] if w else None
rows.sort(key=lambda r: (-(wk(r["id"]) or 0), r["n_prov"]))

out = []
out.append("## Summary table across models")
out.append("")
out.append("Sources: https://openrouter.ai/api/v1/models and https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints for prices, counts, context; https://openrouter.ai/rankings and https://openrouter.ai/models?order=top-weekly for weekly tokens and rank. All checked 2026-10-22. Prices in USD per million tokens. Min and median are computed over distinct providers, using each provider's cheapest endpoint. Endpoints priced at $0 are ignored. 'Price to beat' is the current minimum minus 5 percent.")
out.append("")
out.append("| Model | Providers | Endpoints | Context | Min in | Median in | Min out | Median out | Max out | Cheapest provider(s) | Price to beat (in / out) | Weekly tokens | Weekly rank | Tokens per provider |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    w = weekly.get(r["id"], {})
    t = w.get("tokens"); rk = w.get("rank", "")
    tpp = tok(t / r["n_prov"]) if (t and r["n_prov"]) else "n/a"
    beat = f"{fmt(r['min_in']*0.95,4)} / {fmt(r['min_out']*0.95,4)}" if r["min_out"] else "n/a"
    out.append(f"| {r['id']} | {r['n_prov']} | {r['n_ep']} | {r['ctx']} | {fmt(r['min_in'],4)} | {fmt(r['med_in'],4)} | {fmt(r['min_out'],4)} | {fmt(r['med_out'],4)} | {fmt(r['max_out'],4)} | {r['floor_prov']} | {beat} | {tok(t) if t else 'not in top list'} | {rk if rk else 'n/a'} | {tpp} |")
out.append("")
out.append("## Provider frequency across the models above")
out.append("")
out.append("Source: the endpoints files listed above (checked 2026-10-22). 'Out price vs floor' is the median of (provider output price / cheapest output price for that model). 'Times cheapest' counts models where the provider posts the lowest output price (ties count).")
out.append("")
out.append("| Provider | Models served (of {}) | Times cheapest | Out price vs floor (median x) | In price vs floor (median x) | Quantizations offered |".format(len([r for r in rows if r['n_prov']])))
out.append("|---|---|---|---|---|---|")
for p in sorted(prov_models, key=lambda p: -len(prov_models[p])):
    q = sorted(set(prov_quant[p]))
    out.append(f"| {p} | {len(prov_models[p])} | {prov_floor[p]} | {fmt(statistics.median(prov_ratio_out[p]),2) if prov_ratio_out[p] else 'n/a'} | {fmt(statistics.median(prov_ratio_in[p]),2) if prov_ratio_in[p] else 'n/a'} | {', '.join(q)} |")
out.append("")
out.append("## Detail tables, one per model (every endpoint)")
out.append("")
out.append("\n\n".join(details))
print("\n".join(out))
