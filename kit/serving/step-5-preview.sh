#!/usr/bin/env bash
# Serve stepfun-ai/Step-5-Preview (604B multimodal MoE, 1M context, MTP) with the vendor vLLM image.
# Source: https://recipes.vllm.ai/stepfun-ai/Step-5-Preview (updated 2026-10-15, read 2026-10-22).
# Recipe reference: FP8 on 4x B300 (TP4), or 8x H200 (TP8, omit the MegaMoE flag on Hopper).
# Not yet in a stable vLLM or SGLang release; the step-5-preview image is required.
set -euo pipefail
HW="${HW:-h200}"
PORT="${PORT:-8003}"
SERVED="${SERVED:-step-5-preview}"
MAX_MODEL_LEN="${MAX_MODEL_LEN:-262144}"
HF_CACHE="${HF_CACHE:-$HOME/.cache/huggingface}"
EXTRA="${EXTRA:-}"
MODEL="${MODEL:-stepfun-ai/Step-5-Preview}"

case "$HW" in
  h200|b200)
    PAR="--tensor-parallel-size 8"
    ;;
  b300)
    PAR="--tensor-parallel-size 4 --enable-expert-parallel --moe-backend deep_gemm_mega_moe"
    ;;
  *) echo "unknown HW=$HW (h200|b200|b300)"; exit 1;;
esac
docker run -d --name vllm-step5 --restart unless-stopped \
  --gpus all --ipc=host -p "${PORT}:8000" \
  -e HF_TOKEN="${HF_TOKEN:-}" \
  -v "${HF_CACHE}:/root/.cache/huggingface" \
  vllm/vllm-openai:step-5-preview "${MODEL}" \
    ${PAR} \
    --max-model-len "${MAX_MODEL_LEN}" \
    --reasoning-parser step5 \
    --tool-call-parser step5 \
    --enable-auto-tool-choice \
    --port 8000 \
    --served-model-name "${SERVED}" ${EXTRA}
echo "started vllm-step5 on :${PORT}"
