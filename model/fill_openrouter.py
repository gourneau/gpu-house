"""Fill the OpenRouter cells of data/params.json from the raw endpoints JSON.

For every model slug in params["models"] it reads
  research_notes/GPU rental inference business plan/raw_openrouter_endpoints_{author}_{slug}.json
and weekly_tokens.json from the same folder, and writes:
  providers        distinct providers with at least one paid, active endpoint
  min_in/min_out   minimum over distinct providers (each provider's cheapest endpoint by output price, then input)
  median_in/median_out  median over the same per-provider prices
  weekly_tokens    'Tokens processed in the last 7 days' from weekly_tokens.json (rounded page value), else null
  sum_inv_sq_price sum over paid, active endpoints of 1 / (blended price)^2, blended = out + 3 x in, USD per million tokens

Exclusions: endpoints priced at $0 (free variants) and endpoints whose status is not 0
(the API marks degraded or disabled endpoints with negative status codes such as -2 and -5).

Run from the repo root:  python -I model/fill_openrouter.py
"""
import json
import os
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS = os.path.join(ROOT, "data", "params.json")
NOTES = os.path.join(ROOT, "research_notes", "GPU rental inference business plan")
CHECKED = "2026-10-22"
RATIO_IN_DEMAND = 3.0


def per_million(x):
    """API prices are USD per token as strings; convert to USD per million and drop float noise."""
    return round(float(x) * 1_000_000, 6) if x not in (None, "") else None


def load_endpoints(slug):
    author, name = slug.split("/", 1)
    path = os.path.join(NOTES, f"raw_openrouter_endpoints_{author}_{name}.json")
    if not os.path.exists(path):
        return None, path
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["data"].get("endpoints", []), path


def main():
    with open(PARAMS, "r", encoding="utf-8") as f:
        P = json.load(f)
    with open(os.path.join(NOTES, "weekly_tokens.json"), "r", encoding="utf-8") as f:
        weekly = json.load(f)
    api = "https://openrouter.ai/api/v1/models/{slug}/endpoints"
    for m in P["models"]:
        slug = m["slug"]
        eps, path = load_endpoints(slug)
        orr = m["openrouter"]
        src = api.format(slug=slug) + f" (raw copy {os.path.relpath(path, ROOT)}, checked {CHECKED})"
        if eps is None:
            print(f"{slug}: no raw endpoints file, left null")
            continue
        paid = []
        excluded = []
        for e in eps:
            pi, po = per_million(e["pricing"]["prompt"]), per_million(e["pricing"]["completion"])
            if pi is None or po is None or (pi == 0 and po == 0):
                excluded.append(f"{e['provider_name']} free")
                continue
            if e.get("status", 0) != 0:
                excluded.append(f"{e['provider_name']} status {e.get('status')}")
                continue
            paid.append((e["provider_name"], pi, po))
        best = {}
        for prov, pi, po in paid:
            if prov not in best or (po, pi) < (best[prov][1], best[prov][0]):
                best[prov] = (pi, po)
        ins = [v[0] for v in best.values()]
        outs = [v[1] for v in best.values()]
        n = len(best)
        sis = round(sum(1.0 / (po + RATIO_IN_DEMAND * pi) ** 2 for _, pi, po in paid), 6)
        wt = weekly.get(slug, {}).get("tokens")
        excl_note = ("; excluded: " + ", ".join(excluded)) if excluded else ""
        orr["providers"] = {"value": n, "source": src, "checked": CHECKED,
                            "note": f"distinct providers with a paid endpoint of status 0; {len(paid)} such endpoints{excl_note}"}
        med = lambda xs: round(statistics.median(xs), 6) if xs else None
        orr["min_in"] = {"value": min(ins) if ins else None, "source": src, "checked": CHECKED,
                         "note": "USD per million prompt tokens; minimum over providers using each provider's cheapest endpoint"}
        orr["median_in"] = {"value": med(ins), "source": src, "checked": CHECKED,
                            "note": "median over providers of the per-provider cheapest endpoint"}
        orr["min_out"] = {"value": min(outs) if outs else None, "source": src, "checked": CHECKED,
                          "note": "USD per million completion tokens; minimum over providers"}
        orr["median_out"] = {"value": med(outs), "source": src, "checked": CHECKED,
                             "note": "median over providers of the per-provider cheapest endpoint"}
        orr["weekly_tokens"] = {"value": wt,
                                "source": "https://openrouter.ai/models?order=top-weekly card label 'Tokens processed in the last 7 days' (3 significant figures, includes the in-progress day), via weekly_tokens.json beside the notes; rank from https://openrouter.ai/rankings",
                                "checked": CHECKED,
                                "note": f"rank {weekly.get(slug, {}).get('rank', 'n/a')}; " + ("rounded page value" if wt else "not found on the page")}
        orr["sum_inv_sq_price"] = {"value": sis, "source": src, "checked": CHECKED,
                                   "note": f"sum over {len(paid)} paid, status-0 endpoints of 1/(out + 3 x in)^2 with prices in USD per million tokens; used by model.routing_share"}
        print(f"{slug}: providers {n}, endpoints {len(paid)}, min {min(ins) if ins else None}/{min(outs) if outs else None}, "
              f"median {med(ins)}/{med(outs)}, weekly {wt}, sis {sis:.4g}{excl_note}")
    with open(PARAMS, "w", encoding="utf-8") as f:
        json.dump(P, f, indent=1)
    print("wrote", PARAMS)


if __name__ == "__main__":
    main()
