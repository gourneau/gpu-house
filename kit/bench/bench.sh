#!/usr/bin/env bash
# Throughput sweep with `vllm bench serve` against a running vLLM server.
# Produces one JSON result per (shape, concurrency) in results/, then summarize.py turns
# them into tokens/s per GPU, revenue per GPU-hour and breakeven utilization.
#
# Usage:  MODEL=zai-org/GLM-5.3 SERVED=glm-5.3 PORT=8002 GPUS=8 ./bench.sh
# Start the server with EXTRA="--no-enable-prefix-caching" for a clean measurement
# (the GLM recipe recommends it). Runs inside the vLLM container or any env with vllm installed.
set -euo pipefail
MODEL="${MODEL:?set MODEL to the HF id used by the server}"
SERVED="${SERVED:-$MODEL}"
HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8000}"
GPUS="${GPUS:-8}"
OUT="${OUT:-results}"
SHAPES="${SHAPES:-1024:1024 3072:1024 8000:1024}"     # input:output token lengths
CONC="${CONC:-32 64 128 256}"                         # max concurrency levels
MULT="${MULT:-4}"                                     # prompts per run = MULT x concurrency
mkdir -p "$OUT"
for shape in $SHAPES; do
  IN="${shape%%:*}"; OUTLEN="${shape##*:}"
  for c in $CONC; do
    n=$(( c * MULT ))
    tag="in${IN}_out${OUTLEN}_c${c}"
    echo "== $tag ($n prompts)"
    vllm bench serve \
      --backend openai-chat --endpoint /v1/chat/completions \
      --host "$HOST" --port "$PORT" \
      --model "$MODEL" --served-model-name "$SERVED" \
      --dataset-name random --random-input-len "$IN" --random-output-len "$OUTLEN" \
      --num-prompts "$n" --max-concurrency "$c" --request-rate inf \
      --ignore-eos --percentile-metrics ttft,tpot,itl,e2el \
      --save-result --result-dir "$OUT" --result-filename "$tag.json" \
      --metadata gpus="$GPUS" shape="$shape" concurrency="$c" served="$SERVED"
  done
done
echo "done. summarize: python summarize.py --dir $OUT --gpus $GPUS --rent 3.50 --prompt-usd 0.075 --completion-usd 1.33"
