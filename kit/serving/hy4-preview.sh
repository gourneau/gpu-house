#!/usr/bin/env bash
# Serve tencent/Hy4-preview (770B MoE, 49B active) with vLLM.
# Source: https://recipes.vllm.ai/tencent/Hy4-preview (updated 2026-09-28, read 2026-10-22).
# The recipe's reference nodes are 16x B200, 8x B300 and 8x MI355X. The 8x B200 command
# below is the recipe's own docker example; the MXFP8 checkpoint is about 924 GB, so on
# 8x B200 (1,440 GB) KV cache is limited. Measure before pricing.
#
# Usage:  HW=b200 ./hy4-preview.sh        (default)
#         HW=mi355x ./hy4-preview.sh
#         PORT=8001 MAX_MODEL_LEN=131072 ./hy4-preview.sh
set -euo pipefail
HW="${HW:-b200}"
PORT="${PORT:-8001}"
MODEL="${MODEL:-tencent/Hy4-preview-FP8}"
SERVED="${SERVED:-hy4-preview}"
MAX_MODEL_LEN="${MAX_MODEL_LEN:-262144}"
HF_CACHE="${HF_CACHE:-$HOME/.cache/huggingface}"
EXTRA="${EXTRA:-}"   # e.g. "--no-enable-prefix-caching" for clean benchmarks

case "$HW" in
  b200|b300|h200)
    docker run -d --name vllm-hy4 --restart unless-stopped \
      --gpus all --ipc=host -p "${PORT}:8000" \
      -e VLLM_ENABLE_HPC_OPS=1 \
      -e HF_TOKEN="${HF_TOKEN:-}" \
      -v "${HF_CACHE}:/root/.cache/huggingface" \
      vllm/vllm-openai:hy4-preview "${MODEL}" \
        --tensor-parallel-size 8 \
        --speculative-config '{"num_speculative_tokens":3,"method":"mtp"}' \
        --attention-backend FLASHMLA_SPARSE \
        --tool-call-parser hy_v4 \
        --reasoning-parser hy_v4 \
        --enable-auto-tool-choice \
        --max-model-len "${MAX_MODEL_LEN}" \
        --port 8000 \
        --served-model-name "${SERVED}" ${EXTRA}
    ;;
  mi355x)
    # ROCm image; MTP is opt-in on gfx950 per the recipe (omitted here for stability)
    docker run -d --name vllm-hy4 --restart unless-stopped \
      --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host -p "${PORT}:8000" \
      -e VLLM_ROCM_USE_AITER=1 \
      -e HF_TOKEN="${HF_TOKEN:-}" \
      -v "${HF_CACHE}:/root/.cache/huggingface" \
      vllm/vllm-openai-rocm:v0.29.0 "${MODEL}" \
        --tensor-parallel-size 8 \
        --max-model-len "${MAX_MODEL_LEN}" \
        --gpu-memory-utilization 0.85 \
        --max-num-batched-tokens 8192 \
        --tool-call-parser hy_v4 \
        --reasoning-parser hy_v4 \
        --enable-auto-tool-choice \
        --port 8000 \
        --served-model-name "${SERVED}" ${EXTRA}
    ;;
  *) echo "unknown HW=$HW (b200|b300|h200|mi355x)"; exit 1;;
esac
echo "started vllm-hy4 on :${PORT}; follow with: docker logs -f vllm-hy4"
echo "ready when: curl -s localhost:${PORT}/health returns 200"
