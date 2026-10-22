#!/usr/bin/env bash
# Serve zai-org/GLM-5.3 (743B MoE, 39B active, native FP8) with vLLM 0.28+.
# Source: https://recipes.vllm.ai/zai-org/GLM-5.3 (updated 2026-10-15, read 2026-10-22).
# FP8 fits one 8x H200 node; with FP8 KV cache it reaches the full 1M context on 8x B200.
# Inferact/GLM-5.3-NVFP4 (about 465 GB) is the comfortable Blackwell-only option.
#
# Usage:  HW=b200 ./glm-5.3.sh           (FP8, 8x B200 or 8x H200)
#         HW=nvfp4 ./glm-5.3.sh          (NVFP4 on B200/B300)
#         HW=mi355x ./glm-5.3.sh         (ROCm)
set -euo pipefail
HW="${HW:-b200}"
PORT="${PORT:-8002}"
SERVED="${SERVED:-glm-5.3}"
MAX_MODEL_LEN="${MAX_MODEL_LEN:-262144}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-64}"
HF_CACHE="${HF_CACHE:-$HOME/.cache/huggingface}"
IMAGE="${IMAGE:-vllm/vllm-openai:v0.29.0}"
EXTRA="${EXTRA:-}"

case "$HW" in
  b200|b300|h200)
    docker run -d --name vllm-glm --restart unless-stopped \
      --gpus all --ipc=host -p "${PORT}:8000" \
      -e HF_TOKEN="${HF_TOKEN:-}" \
      -v "${HF_CACHE}:/root/.cache/huggingface" \
      "${IMAGE}" zai-org/GLM-5.3 \
        --kv-cache-dtype fp8_e4m3 \
        --tensor-parallel-size 8 \
        --speculative-config.method mtp \
        --speculative-config.num_speculative_tokens 5 \
        --max-model-len "${MAX_MODEL_LEN}" \
        --max-num-seqs "${MAX_NUM_SEQS}" \
        --tool-call-parser glm47 \
        --reasoning-parser glm47 \
        --enable-auto-tool-choice \
        --port 8000 \
        --served-model-name "${SERVED}" ${EXTRA}
    ;;
  nvfp4)
    docker run -d --name vllm-glm --restart unless-stopped \
      --gpus all --ipc=host -p "${PORT}:8000" \
      -e HF_TOKEN="${HF_TOKEN:-}" \
      -v "${HF_CACHE}:/root/.cache/huggingface" \
      "${IMAGE}" Inferact/GLM-5.3-NVFP4 \
        --tensor-parallel-size 8 \
        --enable-expert-parallel \
        --kv-cache-dtype fp8_e4m3 \
        --max-model-len "${MAX_MODEL_LEN}" \
        --max-num-seqs "${MAX_NUM_SEQS}" \
        --reasoning-parser glm47 \
        --tool-call-parser glm47 \
        --enable-auto-tool-choice \
        --port 8000 \
        --served-model-name "${SERVED}" ${EXTRA}
    ;;
  mi355x|mi300x)
    docker run -d --name vllm-glm --restart unless-stopped \
      --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host -p "${PORT}:8000" \
      -e VLLM_ROCM_USE_AITER=1 -e VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS=1 \
      -e HF_TOKEN="${HF_TOKEN:-}" \
      -v "${HF_CACHE}:/root/.cache/huggingface" \
      vllm/vllm-openai-rocm:v0.29.0 zai-org/GLM-5.3 \
        --kv-cache-dtype fp8_e4m3 \
        --tensor-parallel-size 8 \
        --speculative-config.method mtp \
        --speculative-config.num_speculative_tokens 5 \
        --tool-call-parser glm47 \
        --reasoning-parser glm47 \
        --enable-auto-tool-choice \
        --gpu-memory-utilization 0.80 \
        --max-model-len "${MAX_MODEL_LEN}" \
        --max-num-seqs "${MAX_NUM_SEQS}" \
        --linear-backend aiter --moe-backend aiter \
        --port 8000 \
        --served-model-name "${SERVED}" ${EXTRA}
    ;;
  *) echo "unknown HW=$HW (b200|b300|h200|nvfp4|mi355x|mi300x)"; exit 1;;
esac
echo "started vllm-glm on :${PORT}; follow with: docker logs -f vllm-glm"
