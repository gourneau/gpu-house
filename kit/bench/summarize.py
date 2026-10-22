"""Turn `vllm bench serve` JSON results into revenue per GPU-hour and breakeven utilization.

Usage:
  python summarize.py --dir results --gpus 8 --rent 3.50 --prompt-usd 0.075 --completion-usd 1.33
  (rent = USD per GPU-hour; prices = USD per million tokens you will post)

Reads every *.json in --dir. vllm bench serve writes fields such as
output_throughput (output tokens/s), total_token_throughput, request_throughput,
mean_ttft_ms, median_ttft_ms, p99_ttft_ms, mean_tpot_ms, median_itl_ms, duration,
total_input_tokens, total_output_tokens, max_concurrency.
"""
import argparse
import glob
import json
import os


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="results")
    ap.add_argument("--gpus", type=int, default=8)
    ap.add_argument("--rent", type=float, required=True, help="USD per GPU-hour")
    ap.add_argument("--prompt-usd", type=float, required=True, help="USD per million prompt tokens")
    ap.add_argument("--completion-usd", type=float, required=True, help="USD per million completion tokens")
    ap.add_argument("--ttft-cap-ms", type=float, default=3000, help="flag rows whose median TTFT exceeds this")
    ap.add_argument("--csv", default=None, help="optional CSV output path")
    a = ap.parse_args()

    rows = []
    for p in sorted(glob.glob(os.path.join(a.dir, "*.json"))):
        with open(p, "r", encoding="utf-8") as f:
            r = json.load(f)
        dur = float(r.get("duration") or 0)
        tin = float(r.get("total_input_tokens") or 0)
        tout = float(r.get("total_output_tokens") or 0)
        out_tps = float(r.get("output_throughput") or (tout / dur if dur else 0))
        in_tps = (tin / dur) if dur else 0.0
        per_gpu_out = out_tps / a.gpus
        per_gpu_in = in_tps / a.gpus
        rev_hr = (per_gpu_in * a.prompt_usd + per_gpu_out * a.completion_usd) * 3600 / 1e6
        be = (a.rent / rev_hr) if rev_hr > 0 else float("inf")
        rows.append({
            "file": os.path.basename(p),
            "concurrency": r.get("max_concurrency") or (r.get("metadata") or {}).get("concurrency"),
            "in_tok": int(tin / max(1, r.get("completed", 1))) if r.get("completed") else None,
            "out_tps_per_gpu": per_gpu_out,
            "in_tps_per_gpu": per_gpu_in,
            "ttft_median_ms": r.get("median_ttft_ms"),
            "ttft_p99_ms": r.get("p99_ttft_ms"),
            "tpot_median_ms": r.get("median_tpot_ms"),
            "per_user_tps": (1000.0 / r["median_tpot_ms"]) if r.get("median_tpot_ms") else None,
            "rev_per_gpu_hr_100": rev_hr,
            "breakeven_util": be,
            "ttft_ok": (r.get("median_ttft_ms") or 0) <= a.ttft_cap_ms,
        })
    if not rows:
        print("no results found in", a.dir); return
    hdr = ["file", "concurrency", "out_tps_per_gpu", "in_tps_per_gpu", "ttft_median_ms", "ttft_p99_ms", "per_user_tps", "rev_per_gpu_hr_100", "breakeven_util", "ttft_ok"]
    print(" | ".join(hdr))
    for r in rows:
        print(" | ".join(f"{r[k]:.2f}" if isinstance(r[k], float) else str(r[k]) for k in hdr))
    best = max((r for r in rows if r["ttft_ok"]), key=lambda r: r["rev_per_gpu_hr_100"], default=None)
    if best:
        print(f"\nBest row with acceptable TTFT: {best['file']}: {best['out_tps_per_gpu']:.0f} output tok/s per GPU, "
              f"${best['rev_per_gpu_hr_100']:.2f} per GPU-hour at 100%, breakeven utilization {best['breakeven_util']:.0%} at ${a.rent:.2f}/GPU-hr rent.")
        print("Compare with the model's planning number in data/params.json and update tps_out_per_gpu with this measurement.")
    if a.csv:
        import csv
        with open(a.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
        print("wrote", a.csv)


if __name__ == "__main__":
    main()
