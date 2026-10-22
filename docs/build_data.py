"""Bundle model output and curated tables into site/data.js so the page works
from file:// and GitHub Pages without fetch. Run: python -I docs/build_data.py"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        return None
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def slim_params(P):
    """Keep what the page needs: rates with sources, models with OpenRouter stats and throughput."""
    if P is None:
        return None
    out = {"start_date": P.get("start_date"), "test_start_date": P.get("test_start_date"),
           "decide_date": P.get("decide_date"), "tax": P.get("tax"), "vast": P.get("vast"),
           "assumptions": P.get("assumptions"), "plans": P.get("plans"), "owned": P.get("owned"),
           "gpus": P.get("gpus"), "models": P.get("models")}
    return out


data = {
    "generated": "2026-10-22",
    "results": load("data/results.json"),
    "results_typical": load("data/results_typical.json"),
    "params": slim_params(load("data/params.json")),
    "tables": load("docs/tables.json") or {},
}
js = "window.DATA = " + json.dumps(data, separators=(",", ":"), ensure_ascii=False) + ";\n"
with open(os.path.join(ROOT, "docs", "data.js"), "w", encoding="utf-8") as f:
    f.write(js)
print("wrote docs/data.js", len(js), "bytes; tables:", list((data["tables"] or {}).keys()))
