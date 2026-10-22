# Model results (start 2026-12-01, 744 GPU-hours left in 2026 per GPU)

## Unit economics: revenue per GPU-hour at 100% utilization

| Model | GPU | Price point | Rev/GPU-hr @100% | @20% | @40% | @70% | On-demand cost | 12-mo cost |
|---|---|---|---:|---:|---:|---:|---:|---:|
| deepseek/deepseek-r1-0528 | B200 | median | 31.80 | 6.36 | 12.72 | 22.26 | 3.50 | 3.50 |
| deepseek/deepseek-r1-0528 | B200 | min | 29.96 | 5.99 | 11.98 | 20.97 | 3.50 | 3.50 |
| deepseek/deepseek-r1-0528 | H200 | median | 8.48 | 1.70 | 3.39 | 5.94 | 3.00 | 3.00 |
| deepseek/deepseek-r1-0528 | H200 | min | 7.99 | 1.60 | 3.20 | 5.59 | 3.00 | 3.00 |
| deepseek/deepseek-r1-0528 | MI300X | median | 2.12 | 0.42 | 0.85 | 1.48 | 1.85 | 1.75 |
| deepseek/deepseek-r1-0528 | MI300X | min | 2.00 | 0.40 | 0.80 | 1.40 | 1.85 | 1.75 |
| deepseek/deepseek-r1-0528 | MI355X | median | 28.62 | 5.72 | 11.45 | 20.03 | 2.59 | 2.59 |
| deepseek/deepseek-r1-0528 | MI355X | min | 26.96 | 5.39 | 10.79 | 18.87 | 2.59 | 2.59 |
| deepseek/deepseek-v4.1-flash | B200 | median | 11.79 | 2.36 | 4.72 | 8.26 | 3.50 | 3.50 |
| deepseek/deepseek-v4.1-flash | B200 | min | 3.20 | 0.64 | 1.28 | 2.24 | 3.50 | 3.50 |
| deepseek/deepseek-v4.1-flash | H200 | median | 3.14 | 0.63 | 1.26 | 2.20 | 3.00 | 3.00 |
| deepseek/deepseek-v4.1-flash | H200 | min | 0.85 | 0.17 | 0.34 | 0.60 | 3.00 | 3.00 |
| deepseek/deepseek-v4.1-flash | MI300X | median | 0.79 | 0.16 | 0.31 | 0.55 | 1.85 | 1.75 |
| deepseek/deepseek-v4.1-flash | MI300X | min | 0.21 | 0.04 | 0.09 | 0.15 | 1.85 | 1.75 |
| deepseek/deepseek-v4.1-flash | MI355X | median | 10.61 | 2.12 | 4.25 | 7.43 | 2.59 | 2.59 |
| deepseek/deepseek-v4.1-flash | MI355X | min | 2.88 | 0.58 | 1.15 | 2.02 | 2.59 | 2.59 |
| meta-llama/llama-3.3-70b-instruct | B200 | median | 23.71 | 4.74 | 9.48 | 16.60 | 3.50 | 3.50 |
| meta-llama/llama-3.3-70b-instruct | B200 | min | 7.63 | 1.53 | 3.05 | 5.34 | 3.50 | 3.50 |
| meta-llama/llama-3.3-70b-instruct | H100 | median | 6.32 | 1.26 | 2.53 | 4.43 | 2.30 | 2.30 |
| meta-llama/llama-3.3-70b-instruct | H100 | min | 2.04 | 0.41 | 0.81 | 1.42 | 2.30 | 2.30 |
| meta-llama/llama-3.3-70b-instruct | H200 | median | 8.43 | 1.69 | 3.37 | 5.90 | 3.00 | 3.00 |
| meta-llama/llama-3.3-70b-instruct | H200 | min | 2.71 | 0.54 | 1.09 | 1.90 | 3.00 | 3.00 |
| meta-llama/llama-3.3-70b-instruct | MI300X | median | 6.32 | 1.26 | 2.53 | 4.43 | 1.85 | 1.75 |
| meta-llama/llama-3.3-70b-instruct | MI300X | min | 2.04 | 0.41 | 0.81 | 1.42 | 1.85 | 1.75 |
| meta-llama/llama-3.3-70b-instruct | MI355X | median | 11.06 | 2.21 | 4.43 | 7.75 | 2.59 | 2.59 |
| meta-llama/llama-3.3-70b-instruct | MI355X | min | 3.56 | 0.71 | 1.42 | 2.49 | 2.59 | 2.59 |
| meta-llama/llama-3.3-70b-instruct | RTXPRO6000 | median | 4.90 | 0.98 | 1.96 | 3.43 | 2.20 | 2.20 |
| meta-llama/llama-3.3-70b-instruct | RTXPRO6000 | min | 1.58 | 0.32 | 0.63 | 1.10 | 2.20 | 2.20 |
| meta-llama/llama-4-maverick | B200 | median | 41.33 | 8.27 | 16.53 | 28.93 | 3.50 | 3.50 |
| meta-llama/llama-4-maverick | B200 | min | 23.27 | 4.65 | 9.31 | 16.29 | 3.50 | 3.50 |
| meta-llama/llama-4-maverick | H100 | median | 10.63 | 2.13 | 4.25 | 7.44 | 2.30 | 2.30 |
| meta-llama/llama-4-maverick | H100 | min | 5.98 | 1.20 | 2.39 | 4.19 | 2.30 | 2.30 |
| meta-llama/llama-4-maverick | H200 | median | 14.76 | 2.95 | 5.90 | 10.33 | 3.00 | 3.00 |
| meta-llama/llama-4-maverick | H200 | min | 8.31 | 1.66 | 3.32 | 5.82 | 3.00 | 3.00 |
| meta-llama/llama-4-maverick | MI300X | median | 12.69 | 2.54 | 5.08 | 8.89 | 1.85 | 1.75 |
| meta-llama/llama-4-maverick | MI300X | min | 7.15 | 1.43 | 2.86 | 5.00 | 1.85 | 1.75 |
| meta-llama/llama-4-maverick | MI355X | median | 35.42 | 7.08 | 14.17 | 24.80 | 2.59 | 2.59 |
| meta-llama/llama-4-maverick | MI355X | min | 19.95 | 3.99 | 7.98 | 13.96 | 2.59 | 2.59 |
| mistralai/mistral-small-2603 | B200 | median | 8.01 | 1.60 | 3.21 | 5.61 | 3.50 | 3.50 |
| mistralai/mistral-small-2603 | B200 | min | 7.61 | 1.52 | 3.05 | 5.33 | 3.50 | 3.50 |
| mistralai/mistral-small-2603 | H100 | median | 2.12 | 0.42 | 0.85 | 1.48 | 2.30 | 2.30 |
| mistralai/mistral-small-2603 | H100 | min | 2.01 | 0.40 | 0.80 | 1.41 | 2.30 | 2.30 |
| mistralai/mistral-small-2603 | H200 | median | 2.84 | 0.57 | 1.14 | 1.99 | 3.00 | 3.00 |
| mistralai/mistral-small-2603 | H200 | min | 2.70 | 0.54 | 1.08 | 1.89 | 3.00 | 3.00 |
| mistralai/mistral-small-2603 | MI300X | median | 2.12 | 0.42 | 0.85 | 1.48 | 1.85 | 1.75 |
| mistralai/mistral-small-2603 | MI300X | min | 2.01 | 0.40 | 0.80 | 1.41 | 1.85 | 1.75 |
| mistralai/mistral-small-2603 | MI355X | median | 3.78 | 0.76 | 1.51 | 2.65 | 2.59 | 2.59 |
| mistralai/mistral-small-2603 | MI355X | min | 3.59 | 0.72 | 1.44 | 2.51 | 2.59 | 2.59 |
| moonshotai/kimi-k2-0905 | B200 | median | 30.96 | 6.19 | 12.38 | 21.67 | 3.50 | 3.50 |
| moonshotai/kimi-k2-0905 | B200 | min | 29.41 | 5.88 | 11.76 | 20.59 | 3.50 | 3.50 |
| moonshotai/kimi-k2-0905 | H200 | median | 8.67 | 1.73 | 3.47 | 6.07 | 3.00 | 3.00 |
| moonshotai/kimi-k2-0905 | H200 | min | 8.24 | 1.65 | 3.29 | 5.76 | 3.00 | 3.00 |
| moonshotai/kimi-k2-0905 | MI300X | median | 2.23 | 0.45 | 0.89 | 1.56 | 1.85 | 1.75 |
| moonshotai/kimi-k2-0905 | MI300X | min | 2.12 | 0.42 | 0.85 | 1.48 | 1.85 | 1.75 |
| moonshotai/kimi-k2-0905 | MI355X | median | 27.86 | 5.57 | 11.15 | 19.50 | 2.59 | 2.59 |
| moonshotai/kimi-k2-0905 | MI355X | min | 26.47 | 5.29 | 10.59 | 18.53 | 2.59 | 2.59 |
| openai/gpt-oss-120b | B200 | median | 34.56 | 6.91 | 13.82 | 24.19 | 3.50 | 3.50 |
| openai/gpt-oss-120b | B200 | min | 9.85 | 1.97 | 3.94 | 6.89 | 3.50 | 3.50 |
| openai/gpt-oss-120b | H100 | median | 6.91 | 1.38 | 2.76 | 4.84 | 2.30 | 2.30 |
| openai/gpt-oss-120b | H100 | min | 1.97 | 0.39 | 0.79 | 1.38 | 2.30 | 2.30 |
| openai/gpt-oss-120b | H200 | median | 9.22 | 1.84 | 3.69 | 6.45 | 3.00 | 3.00 |
| openai/gpt-oss-120b | H200 | min | 2.63 | 0.53 | 1.05 | 1.84 | 3.00 | 3.00 |
| openai/gpt-oss-120b | MI300X | median | 6.22 | 1.24 | 2.49 | 4.35 | 1.85 | 1.75 |
| openai/gpt-oss-120b | MI300X | min | 1.77 | 0.35 | 0.71 | 1.24 | 1.85 | 1.75 |
| openai/gpt-oss-120b | MI355X | median | 29.95 | 5.99 | 11.98 | 20.97 | 2.59 | 2.59 |
| openai/gpt-oss-120b | MI355X | min | 8.54 | 1.71 | 3.41 | 5.98 | 2.59 | 2.59 |
| openai/gpt-oss-120b | RTXPRO6000 | median | 3.46 | 0.69 | 1.38 | 2.42 | 2.20 | 2.20 |
| openai/gpt-oss-120b | RTXPRO6000 | min | 0.98 | 0.20 | 0.39 | 0.69 | 2.20 | 2.20 |
| openai/gpt-oss-20b | B200 | median | 23.18 | 4.64 | 9.27 | 16.23 | 3.50 | 3.50 |
| openai/gpt-oss-20b | B200 | min | 13.79 | 2.76 | 5.52 | 9.65 | 3.50 | 3.50 |
| openai/gpt-oss-20b | H100 | median | 4.97 | 0.99 | 1.99 | 3.48 | 2.30 | 2.30 |
| openai/gpt-oss-20b | H100 | min | 2.95 | 0.59 | 1.18 | 2.07 | 2.30 | 2.30 |
| openai/gpt-oss-20b | H200 | median | 5.96 | 1.19 | 2.38 | 4.17 | 3.00 | 3.00 |
| openai/gpt-oss-20b | H200 | min | 3.55 | 0.71 | 1.42 | 2.48 | 3.00 | 3.00 |
| openai/gpt-oss-20b | MI300X | median | 4.50 | 0.90 | 1.80 | 3.15 | 1.85 | 1.75 |
| openai/gpt-oss-20b | MI300X | min | 2.68 | 0.54 | 1.07 | 1.88 | 1.85 | 1.75 |
| openai/gpt-oss-20b | MI355X | median | 19.87 | 3.97 | 7.95 | 13.91 | 2.59 | 2.59 |
| openai/gpt-oss-20b | MI355X | min | 11.82 | 2.36 | 4.73 | 8.27 | 2.59 | 2.59 |
| qwen/qwen3-235b-a22b-2507 | B200 | median | 8.60 | 1.72 | 3.44 | 6.02 | 3.50 | 3.50 |
| qwen/qwen3-235b-a22b-2507 | B200 | min | 5.03 | 1.01 | 2.01 | 3.52 | 3.50 | 3.50 |
| qwen/qwen3-235b-a22b-2507 | H100 | median | 2.87 | 0.57 | 1.15 | 2.01 | 2.30 | 2.30 |
| qwen/qwen3-235b-a22b-2507 | H100 | min | 1.68 | 0.34 | 0.67 | 1.17 | 2.30 | 2.30 |
| qwen/qwen3-235b-a22b-2507 | H200 | median | 4.87 | 0.97 | 1.95 | 3.41 | 3.00 | 3.00 |
| qwen/qwen3-235b-a22b-2507 | H200 | min | 2.85 | 0.57 | 1.14 | 1.99 | 3.00 | 3.00 |
| qwen/qwen3-235b-a22b-2507 | MI300X | median | 4.30 | 0.86 | 1.72 | 3.01 | 1.85 | 1.75 |
| qwen/qwen3-235b-a22b-2507 | MI300X | min | 2.51 | 0.50 | 1.01 | 1.76 | 1.85 | 1.75 |
| qwen/qwen3-235b-a22b-2507 | MI355X | median | 7.45 | 1.49 | 2.98 | 5.22 | 2.59 | 2.59 |
| qwen/qwen3-235b-a22b-2507 | MI355X | min | 4.36 | 0.87 | 1.74 | 3.05 | 2.59 | 2.59 |
| qwen/qwen3-235b-a22b-2507 | RTXPRO6000 | median | 2.29 | 0.46 | 0.92 | 1.60 | 2.20 | 2.20 |
| qwen/qwen3-235b-a22b-2507 | RTXPRO6000 | min | 1.34 | 0.27 | 0.54 | 0.94 | 2.20 | 2.20 |
| qwen/qwen3-32b | B200 | median | 8.27 | 1.65 | 3.31 | 5.79 | 3.50 | 3.50 |
| qwen/qwen3-32b | B200 | min | 4.98 | 1.00 | 1.99 | 3.49 | 3.50 | 3.50 |
| qwen/qwen3-32b | H100 | median | 2.36 | 0.47 | 0.94 | 1.65 | 2.30 | 2.30 |
| qwen/qwen3-32b | H100 | min | 1.42 | 0.28 | 0.57 | 1.00 | 2.30 | 2.30 |
| qwen/qwen3-32b | H200 | median | 3.07 | 0.61 | 1.23 | 2.15 | 3.00 | 3.00 |
| qwen/qwen3-32b | H200 | min | 1.85 | 0.37 | 0.74 | 1.29 | 3.00 | 3.00 |
| qwen/qwen3-32b | MI300X | median | 2.36 | 0.47 | 0.94 | 1.65 | 1.85 | 1.75 |
| qwen/qwen3-32b | MI300X | min | 1.42 | 0.28 | 0.57 | 1.00 | 1.85 | 1.75 |
| qwen/qwen3-32b | MI355X | median | 3.90 | 0.78 | 1.56 | 2.73 | 2.59 | 2.59 |
| qwen/qwen3-32b | MI355X | min | 2.35 | 0.47 | 0.94 | 1.64 | 2.59 | 2.59 |
| stepfun/step-5-preview | B200 | median | 49.25 | 9.85 | 19.70 | 34.47 | 3.50 | 3.50 |
| stepfun/step-5-preview | B200 | min | 46.79 | 9.36 | 18.71 | 32.75 | 3.50 | 3.50 |
| stepfun/step-5-preview | H200 | median | 13.13 | 2.63 | 5.25 | 9.19 | 3.00 | 3.00 |
| stepfun/step-5-preview | H200 | min | 12.48 | 2.50 | 4.99 | 8.73 | 3.00 | 3.00 |
| stepfun/step-5-preview | MI300X | median | 3.28 | 0.66 | 1.31 | 2.30 | 1.85 | 1.75 |
| stepfun/step-5-preview | MI300X | min | 3.12 | 0.62 | 1.25 | 2.18 | 1.85 | 1.75 |
| stepfun/step-5-preview | MI355X | median | 44.32 | 8.86 | 17.73 | 31.03 | 2.59 | 2.59 |
| stepfun/step-5-preview | MI355X | min | 42.11 | 8.42 | 16.84 | 29.47 | 2.59 | 2.59 |
| tencent/hy3 | B200 | median | 8.64 | 1.73 | 3.46 | 6.05 | 3.50 | 3.50 |
| tencent/hy3 | B200 | min | 7.58 | 1.52 | 3.03 | 5.31 | 3.50 | 3.50 |
| tencent/hy3 | H100 | median | 1.15 | 0.23 | 0.46 | 0.81 | 2.30 | 2.30 |
| tencent/hy3 | H100 | min | 1.01 | 0.20 | 0.40 | 0.71 | 2.30 | 2.30 |
| tencent/hy3 | H200 | median | 2.59 | 0.52 | 1.04 | 1.81 | 3.00 | 3.00 |
| tencent/hy3 | H200 | min | 2.28 | 0.46 | 0.91 | 1.59 | 3.00 | 3.00 |
| tencent/hy3 | MI300X | median | 2.25 | 0.45 | 0.90 | 1.57 | 1.85 | 1.75 |
| tencent/hy3 | MI300X | min | 1.97 | 0.39 | 0.79 | 1.38 | 1.85 | 1.75 |
| tencent/hy3 | MI355X | median | 7.49 | 1.50 | 3.00 | 5.24 | 2.59 | 2.59 |
| tencent/hy3 | MI355X | min | 6.57 | 1.31 | 2.63 | 4.60 | 2.59 | 2.59 |
| tencent/hy4-preview | B200 | median | 43.23 | 8.65 | 17.29 | 30.26 | 3.50 | 3.50 |
| tencent/hy4-preview | B200 | min | 41.06 | 8.21 | 16.43 | 28.75 | 3.50 | 3.50 |
| tencent/hy4-preview | H200 | median | 11.53 | 2.31 | 4.61 | 8.07 | 3.00 | 3.00 |
| tencent/hy4-preview | H200 | min | 10.95 | 2.19 | 4.38 | 7.67 | 3.00 | 3.00 |
| tencent/hy4-preview | MI300X | median | 2.88 | 0.58 | 1.15 | 2.02 | 1.85 | 1.75 |
| tencent/hy4-preview | MI300X | min | 2.74 | 0.55 | 1.10 | 1.92 | 1.85 | 1.75 |
| tencent/hy4-preview | MI355X | median | 38.90 | 7.78 | 15.56 | 27.23 | 2.59 | 2.59 |
| tencent/hy4-preview | MI355X | min | 36.96 | 7.39 | 14.78 | 25.87 | 2.59 | 2.59 |
| xiaomi/mimo-v2.6-flash | B200 | median | 5.96 | 1.19 | 2.38 | 4.17 | 3.50 | 3.50 |
| xiaomi/mimo-v2.6-flash | B200 | min | 4.65 | 0.93 | 1.86 | 3.25 | 3.50 | 3.50 |
| xiaomi/mimo-v2.6-flash | H100 | median | 0.79 | 0.16 | 0.32 | 0.56 | 2.30 | 2.30 |
| xiaomi/mimo-v2.6-flash | H100 | min | 0.62 | 0.12 | 0.25 | 0.43 | 2.30 | 2.30 |
| xiaomi/mimo-v2.6-flash | H200 | median | 1.79 | 0.36 | 0.71 | 1.25 | 3.00 | 3.00 |
| xiaomi/mimo-v2.6-flash | H200 | min | 1.39 | 0.28 | 0.56 | 0.98 | 3.00 | 3.00 |
| xiaomi/mimo-v2.6-flash | MI300X | median | 1.55 | 0.31 | 0.62 | 1.08 | 1.85 | 1.75 |
| xiaomi/mimo-v2.6-flash | MI300X | min | 1.21 | 0.24 | 0.48 | 0.85 | 1.85 | 1.75 |
| xiaomi/mimo-v2.6-flash | MI355X | median | 5.16 | 1.03 | 2.07 | 3.61 | 2.59 | 2.59 |
| xiaomi/mimo-v2.6-flash | MI355X | min | 4.03 | 0.81 | 1.61 | 2.82 | 2.59 | 2.59 |
| z-ai/glm-4.6 | B200 | median | 33.26 | 6.65 | 13.31 | 23.28 | 3.50 | 3.50 |
| z-ai/glm-4.6 | B200 | min | 22.98 | 4.60 | 9.19 | 16.09 | 3.50 | 3.50 |
| z-ai/glm-4.6 | H100 | median | 4.44 | 0.89 | 1.77 | 3.10 | 2.30 | 2.30 |
| z-ai/glm-4.6 | H100 | min | 3.06 | 0.61 | 1.23 | 2.15 | 2.30 | 2.30 |
| z-ai/glm-4.6 | H200 | median | 9.98 | 2.00 | 3.99 | 6.99 | 3.00 | 3.00 |
| z-ai/glm-4.6 | H200 | min | 6.89 | 1.38 | 2.76 | 4.83 | 3.00 | 3.00 |
| z-ai/glm-4.6 | MI300X | median | 8.65 | 1.73 | 3.46 | 6.05 | 1.85 | 1.75 |
| z-ai/glm-4.6 | MI300X | min | 5.98 | 1.20 | 2.39 | 4.18 | 1.85 | 1.75 |
| z-ai/glm-4.6 | MI355X | median | 28.83 | 5.77 | 11.53 | 20.18 | 2.59 | 2.59 |
| z-ai/glm-4.6 | MI355X | min | 19.92 | 3.98 | 7.97 | 13.94 | 2.59 | 2.59 |
| z-ai/glm-5.3 | B200 | median | 61.63 | 12.33 | 24.65 | 43.14 | 3.50 | 3.50 |
| z-ai/glm-5.3 | B200 | min | 13.44 | 2.69 | 5.37 | 9.41 | 3.50 | 3.50 |
| z-ai/glm-5.3 | H200 | median | 16.43 | 3.29 | 6.57 | 11.50 | 3.00 | 3.00 |
| z-ai/glm-5.3 | H200 | min | 3.58 | 0.72 | 1.43 | 2.51 | 3.00 | 3.00 |
| z-ai/glm-5.3 | MI300X | median | 4.11 | 0.82 | 1.64 | 2.88 | 1.85 | 1.75 |
| z-ai/glm-5.3 | MI300X | min | 0.90 | 0.18 | 0.36 | 0.63 | 1.85 | 1.75 |
| z-ai/glm-5.3 | MI355X | median | 55.46 | 11.09 | 22.19 | 38.83 | 2.59 | 2.59 |
| z-ai/glm-5.3 | MI355X | min | 12.09 | 2.42 | 4.84 | 8.46 | 2.59 | 2.59 |
| z-ai/glm-5.3-flash | B200 | median | 8.21 | 1.64 | 3.28 | 5.75 | 3.50 | 3.50 |
| z-ai/glm-5.3-flash | B200 | min | 1.76 | 0.35 | 0.70 | 1.23 | 3.50 | 3.50 |
| z-ai/glm-5.3-flash | H100 | median | 1.09 | 0.22 | 0.44 | 0.77 | 2.30 | 2.30 |
| z-ai/glm-5.3-flash | H100 | min | 0.23 | 0.05 | 0.09 | 0.16 | 2.30 | 2.30 |
| z-ai/glm-5.3-flash | H200 | median | 2.46 | 0.49 | 0.98 | 1.72 | 3.00 | 3.00 |
| z-ai/glm-5.3-flash | H200 | min | 0.53 | 0.11 | 0.21 | 0.37 | 3.00 | 3.00 |
| z-ai/glm-5.3-flash | MI300X | median | 2.13 | 0.43 | 0.85 | 1.49 | 1.85 | 1.75 |
| z-ai/glm-5.3-flash | MI300X | min | 0.46 | 0.09 | 0.18 | 0.32 | 1.85 | 1.75 |
| z-ai/glm-5.3-flash | MI355X | median | 7.11 | 1.42 | 2.85 | 4.98 | 2.59 | 2.59 |
| z-ai/glm-5.3-flash | MI355X | min | 1.52 | 0.30 | 0.61 | 1.07 | 2.59 | 2.59 |

## Scenarios

### 1. Month-to-month, inference | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $674 | $-3,493 | $687 | $4,247 | $1,755 | $8,086 | $-41,914 | $-40,159 |
| 40% | 0.74 | $1,348 | $-2,819 | $1,374 | $4,247 | $1,416 | $16,172 | $-33,828 | $-32,411 |
| 70% | 1.30 | $2,358 | $-1,808 | $2,404 | $4,247 | $909 | $28,301 | $-21,699 | $-20,790 |

### 2a. 3-month prepaid, inference | H100 | spend $50,000

GPUs: 3.22 (about 3). Monthly cost: $4,167. Cash at risk: $12,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $876 | $-3,291 | $892 | $12,500 | $5,723 | $10,507 | $-39,493 | $-33,770 |
| 40% | 0.74 | $1,751 | $-2,415 | $1,785 | $12,500 | $5,283 | $21,015 | $-28,985 | $-23,703 |
| 70% | 1.30 | $3,065 | $-1,102 | $3,123 | $12,500 | $4,623 | $36,776 | $-13,224 | $-8,602 |

### 2b. 12-month prepaid, inference | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $674 | $-3,493 | $687 | $50,000 | $24,311 | $8,086 | $-41,914 | $-17,603 |
| 40% | 0.74 | $1,348 | $-2,819 | $1,374 | $50,000 | $23,973 | $16,172 | $-33,828 | $-9,855 |
| 70% | 1.30 | $2,358 | $-1,808 | $2,404 | $50,000 | $23,465 | $28,301 | $-21,699 | $1,766 |

### 3a. Month-to-month, resell on Vast | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $733 | $-3,433 | $747 | $4,247 | $1,725 | $8,800 | $-41,200 | $-39,475 |
| 40% | 0.81 | $1,467 | $-2,700 | $1,495 | $4,247 | $1,357 | $17,600 | $-32,400 | $-31,043 |
| 70% | 1.42 | $2,567 | $-1,600 | $2,616 | $4,247 | $804 | $30,800 | $-19,200 | $-18,396 |

### 3b. 12-month prepaid, resell on Vast | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $733 | $-3,433 | $747 | $50,000 | $24,282 | $8,800 | $-41,200 | $-16,918 |
| 40% | 0.81 | $1,467 | $-2,700 | $1,495 | $50,000 | $23,913 | $17,600 | $-32,400 | $-8,487 |
| 70% | 1.42 | $2,567 | $-1,600 | $2,616 | $50,000 | $23,360 | $30,800 | $-19,200 | $4,160 |

### 4. Own used servers in colocation | H100 | spend $50,000

GPUs: 2.17 (about 2). Monthly cost: $786. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $589 | $-197 | $600 | $50,801 | $21,828 | $7,064 | $-52,367 | $-30,539 |
| 40% | 0.74 | $1,177 | $391 | $1,200 | $50,801 | $21,532 | $14,128 | $-45,302 | $-23,770 |
| 70% | 1.30 | $2,060 | $1,274 | $2,100 | $50,801 | $21,088 | $24,725 | $-34,706 | $-13,618 |

### 4b. Own servers in colocation, resell time on Vast | H100 | spend $50,000

GPUs: 2.17 (about 2). Monthly cost: $786. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $641 | $-145 | $653 | $50,801 | $21,802 | $7,688 | $-51,743 | $-29,941 |
| 40% | 0.81 | $1,281 | $495 | $1,306 | $50,801 | $21,480 | $15,376 | $-44,055 | $-22,575 |
| 70% | 1.42 | $2,242 | $1,456 | $2,285 | $50,801 | $20,997 | $26,908 | $-32,523 | $-11,526 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.18 | $2,141 | $-2,026 | $2,182 | $50,000 | $23,574 | $25,686 | $-24,314 | $-739 |
| 40% | 1.35 | $2,448 | $-1,719 | $2,495 | $50,000 | $23,420 | $29,372 | $-20,628 | $2,792 |
| 70% | 1.61 | $2,908 | $-1,258 | $2,964 | $50,000 | $23,189 | $34,901 | $-15,099 | $8,090 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H100 | spend $59,094

GPUs: 3.22 (about 3). Monthly cost: $4,167. Cash at risk: $21,594. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $876 | $-3,291 | $1,353 | $21,594 | $9,979 | $11,860 | $-47,233 | $-37,255 |
| 40% | 0.74 | $1,751 | $-2,415 | $2,706 | $21,594 | $9,312 | $23,721 | $-35,373 | $-26,061 |
| 70% | 1.30 | $3,065 | $-1,102 | $4,735 | $21,594 | $8,311 | $41,511 | $-17,583 | $-9,271 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H100 | spend $56,998

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $56,998. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $674 | $-3,493 | $1,041 | $56,998 | $27,587 | $9,127 | $-47,871 | $-20,284 |
| 40% | 0.74 | $1,348 | $-2,819 | $2,082 | $56,998 | $27,073 | $18,255 | $-38,744 | $-11,670 |
| 70% | 1.30 | $2,358 | $-1,808 | $3,644 | $56,998 | $26,303 | $31,946 | $-25,053 | $1,251 |

### 1. Month-to-month, inference | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $1,348 | $-6,986 | $1,374 | $8,493 | $3,510 | $16,172 | $-83,828 | $-80,318 |
| 40% | 0.74 | $2,695 | $-5,638 | $2,747 | $8,493 | $2,833 | $32,344 | $-67,656 | $-64,823 |
| 70% | 1.30 | $4,717 | $-3,616 | $4,807 | $8,493 | $1,817 | $56,602 | $-43,398 | $-41,580 |

### 2a. 3-month prepaid, inference | H100 | spend $100,000

GPUs: 6.45 (about 6). Monthly cost: $8,333. Cash at risk: $25,000. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $1,751 | $-6,582 | $1,785 | $25,000 | $11,445 | $21,015 | $-78,985 | $-67,540 |
| 40% | 0.74 | $3,502 | $-4,831 | $3,570 | $25,000 | $10,565 | $42,029 | $-57,971 | $-47,406 |
| 70% | 1.30 | $6,129 | $-2,204 | $6,247 | $25,000 | $9,245 | $73,551 | $-26,449 | $-17,203 |

### 2b. 12-month prepaid, inference | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $1,348 | $-6,986 | $1,374 | $100,000 | $48,623 | $16,172 | $-83,828 | $-35,205 |
| 40% | 0.74 | $2,695 | $-5,638 | $2,747 | $100,000 | $47,946 | $32,344 | $-67,656 | $-19,710 |
| 70% | 1.30 | $4,717 | $-3,616 | $4,807 | $100,000 | $46,930 | $56,602 | $-43,398 | $3,532 |

### 3a. Month-to-month, resell on Vast | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $1,467 | $-6,867 | $1,495 | $8,493 | $3,450 | $17,600 | $-82,400 | $-78,950 |
| 40% | 0.81 | $2,933 | $-5,400 | $2,990 | $8,493 | $2,713 | $35,200 | $-64,800 | $-62,087 |
| 70% | 1.42 | $5,133 | $-3,200 | $5,232 | $8,493 | $1,608 | $61,600 | $-38,400 | $-36,792 |

### 3b. 12-month prepaid, resell on Vast | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $1,467 | $-6,867 | $1,495 | $100,000 | $48,563 | $17,600 | $-82,400 | $-33,837 |
| 40% | 0.81 | $2,933 | $-5,400 | $2,990 | $100,000 | $47,826 | $35,200 | $-64,800 | $-16,974 |
| 70% | 1.42 | $5,133 | $-3,200 | $5,232 | $100,000 | $46,721 | $61,600 | $-38,400 | $8,321 |

### 4. Own used servers in colocation | H100 | spend $100,000

GPUs: 4.34 (about 4). Monthly cost: $1,572. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $1,177 | $-394 | $1,200 | $101,602 | $40,734 | $14,128 | $-104,733 | $-63,999 |
| 40% | 0.74 | $2,355 | $783 | $2,400 | $101,602 | $40,143 | $28,257 | $-90,605 | $-50,462 |
| 70% | 1.30 | $4,121 | $2,549 | $4,200 | $101,602 | $39,256 | $49,449 | $-69,412 | $-30,157 |

### 4b. Own servers in colocation, resell time on Vast | H100 | spend $100,000

GPUs: 4.34 (about 4). Monthly cost: $1,572. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $1,281 | $-290 | $1,306 | $101,602 | $40,682 | $15,376 | $-103,486 | $-62,804 |
| 40% | 0.81 | $2,563 | $991 | $2,612 | $101,602 | $40,038 | $30,752 | $-88,110 | $-48,072 |
| 70% | 1.42 | $4,485 | $2,913 | $4,571 | $101,602 | $39,073 | $53,815 | $-65,046 | $-25,974 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.18 | $4,281 | $-4,052 | $4,363 | $100,000 | $47,149 | $51,372 | $-48,628 | $-1,479 |
| 40% | 1.35 | $4,895 | $-3,438 | $4,989 | $100,000 | $46,840 | $58,744 | $-41,256 | $5,585 |
| 70% | 1.61 | $5,817 | $-2,516 | $5,928 | $100,000 | $46,377 | $69,802 | $-30,198 | $16,180 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H100 | spend $118,187

GPUs: 6.45 (about 6). Monthly cost: $8,333. Cash at risk: $43,187. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $1,751 | $-6,582 | $2,706 | $43,187 | $19,957 | $23,721 | $-94,467 | $-74,509 |
| 40% | 0.74 | $3,502 | $-4,831 | $5,412 | $43,187 | $18,623 | $47,441 | $-70,746 | $-52,123 |
| 70% | 1.30 | $6,129 | $-2,204 | $9,471 | $43,187 | $16,622 | $83,022 | $-35,165 | $-18,543 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H100 | spend $113,996

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $113,996. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $1,348 | $-6,986 | $2,082 | $113,996 | $55,174 | $18,255 | $-95,742 | $-40,568 |
| 40% | 0.74 | $2,695 | $-5,638 | $4,165 | $113,996 | $54,147 | $36,509 | $-77,487 | $-23,340 |
| 70% | 1.30 | $4,717 | $-3,616 | $7,289 | $113,996 | $52,607 | $63,891 | $-50,105 | $2,502 |

### 1. Month-to-month, inference | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $3,369 | $-17,464 | $3,434 | $21,233 | $8,775 | $40,430 | $-209,570 | $-200,795 |
| 40% | 0.74 | $6,738 | $-14,095 | $6,868 | $21,233 | $7,082 | $80,861 | $-169,139 | $-162,057 |
| 70% | 1.30 | $11,792 | $-9,041 | $12,018 | $21,233 | $4,543 | $141,506 | $-108,494 | $-103,951 |

### 2a. 3-month prepaid, inference | H100 | spend $250,000

GPUs: 16.12 (about 16). Monthly cost: $20,833. Cash at risk: $62,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $4,378 | $-16,455 | $4,462 | $62,500 | $28,613 | $52,537 | $-197,463 | $-168,851 |
| 40% | 0.74 | $8,756 | $-12,077 | $8,924 | $62,500 | $26,413 | $105,073 | $-144,927 | $-118,514 |
| 70% | 1.30 | $15,323 | $-5,510 | $15,617 | $62,500 | $23,113 | $183,878 | $-66,122 | $-43,009 |

### 2b. 12-month prepaid, inference | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $3,369 | $-17,464 | $3,434 | $250,000 | $121,557 | $40,430 | $-209,570 | $-88,013 |
| 40% | 0.74 | $6,738 | $-14,095 | $6,868 | $250,000 | $119,864 | $80,861 | $-169,139 | $-49,275 |
| 70% | 1.30 | $11,792 | $-9,041 | $12,018 | $250,000 | $117,325 | $141,506 | $-108,494 | $8,831 |

### 3a. Month-to-month, resell on Vast | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $3,667 | $-17,167 | $3,737 | $21,233 | $8,625 | $44,000 | $-206,000 | $-197,375 |
| 40% | 0.81 | $7,333 | $-13,500 | $7,474 | $21,233 | $6,783 | $88,000 | $-162,000 | $-155,217 |
| 70% | 1.42 | $12,833 | $-8,000 | $13,079 | $21,233 | $4,020 | $154,000 | $-96,000 | $-91,980 |

### 3b. 12-month prepaid, resell on Vast | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $3,667 | $-17,167 | $3,737 | $250,000 | $121,408 | $44,000 | $-206,000 | $-84,592 |
| 40% | 0.81 | $7,333 | $-13,500 | $7,474 | $250,000 | $119,565 | $88,000 | $-162,000 | $-42,435 |
| 70% | 1.42 | $12,833 | $-8,000 | $13,079 | $250,000 | $116,802 | $154,000 | $-96,000 | $20,802 |

### 4. Own used servers in colocation | H100 | spend $250,000

GPUs: 10.84 (about 11). Monthly cost: $3,930. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $2,943 | $-986 | $3,000 | $254,005 | $94,533 | $35,321 | $-261,833 | $-167,300 |
| 40% | 0.74 | $5,887 | $1,957 | $6,000 | $254,005 | $93,054 | $70,642 | $-226,512 | $-133,458 |
| 70% | 1.30 | $10,302 | $6,372 | $10,500 | $254,005 | $90,836 | $123,624 | $-173,531 | $-82,695 |

### 4b. Own servers in colocation, resell time on Vast | H100 | spend $250,000

GPUs: 10.84 (about 11). Monthly cost: $3,930. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $3,203 | $-726 | $3,265 | $254,005 | $94,402 | $38,440 | $-258,715 | $-164,313 |
| 40% | 0.81 | $6,407 | $2,477 | $6,529 | $254,005 | $92,793 | $76,879 | $-220,275 | $-127,482 |
| 70% | 1.42 | $11,212 | $7,282 | $11,427 | $254,005 | $90,379 | $134,538 | $-162,616 | $-72,237 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.18 | $10,703 | $-10,131 | $10,908 | $250,000 | $117,872 | $128,430 | $-121,570 | $-3,697 |
| 40% | 1.35 | $12,238 | $-8,595 | $12,473 | $250,000 | $117,101 | $146,861 | $-103,139 | $13,961 |
| 70% | 1.61 | $14,542 | $-6,291 | $14,821 | $250,000 | $115,943 | $174,506 | $-75,494 | $40,449 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H100 | spend $295,469

GPUs: 16.12 (about 16). Monthly cost: $20,833. Cash at risk: $107,969. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $4,378 | $-16,455 | $6,765 | $107,969 | $49,893 | $59,302 | $-236,167 | $-186,274 |
| 40% | 0.74 | $8,756 | $-12,077 | $13,530 | $107,969 | $46,558 | $118,603 | $-176,865 | $-130,307 |
| 70% | 1.30 | $15,323 | $-5,510 | $23,677 | $107,969 | $41,556 | $207,556 | $-87,913 | $-46,357 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H100 | spend $284,991

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $284,991. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.37 | $3,369 | $-17,464 | $5,206 | $284,991 | $129,134 | $45,636 | $-239,355 | $-110,221 |
| 40% | 0.74 | $6,738 | $-14,095 | $10,412 | $284,991 | $128,493 | $91,273 | $-193,718 | $-65,225 |
| 70% | 1.30 | $11,792 | $-9,041 | $18,221 | $284,991 | $127,533 | $159,728 | $-125,264 | $2,269 |

### 1. Month-to-month, inference | H200 | spend $50,000

GPUs: 1.90 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $1,425 | $-2,742 | $1,452 | $4,247 | $1,378 | $17,097 | $-32,903 | $-31,525 |
| 40% | 2.05 | $2,849 | $-1,317 | $2,904 | $4,247 | $662 | $34,194 | $-15,806 | $-15,144 |
| 70% | 3.59 | $4,987 | $820 | $5,082 | $4,247 | $0 | $59,839 | $9,839 | $9,839 |

### 2a. 3-month prepaid, inference | H200 | spend $50,000

GPUs: 2.00 (about 2). Monthly cost: $4,167. Cash at risk: $12,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $1,500 | $-2,667 | $1,528 | $12,500 | $5,409 | $17,997 | $-32,003 | $-26,594 |
| 40% | 2.05 | $2,999 | $-1,167 | $3,057 | $12,500 | $4,655 | $35,994 | $-14,006 | $-9,351 |
| 70% | 3.59 | $5,249 | $1,082 | $5,350 | $12,500 | $3,525 | $62,989 | $12,989 | $16,514 |

### 2b. 12-month prepaid, inference | H200 | spend $50,000

GPUs: 1.90 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $1,425 | $-2,742 | $1,452 | $50,000 | $23,934 | $17,097 | $-32,903 | $-8,969 |
| 40% | 2.05 | $2,849 | $-1,317 | $2,904 | $50,000 | $23,218 | $34,194 | $-15,806 | $7,412 |
| 70% | 3.59 | $4,987 | $820 | $5,082 | $50,000 | $22,144 | $59,839 | $9,839 | $31,984 |

### 3a. Month-to-month, resell on Vast | H200 | spend $50,000

GPUs: 1.90 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $1,047 | $-3,120 | $1,067 | $4,247 | $1,568 | $12,560 | $-37,440 | $-35,872 |
| 40% | 1.51 | $2,093 | $-2,073 | $2,133 | $4,247 | $1,042 | $25,120 | $-24,880 | $-23,838 |
| 70% | 2.64 | $3,663 | $-503 | $3,734 | $4,247 | $253 | $43,960 | $-6,040 | $-5,787 |

### 3b. 12-month prepaid, resell on Vast | H200 | spend $50,000

GPUs: 1.90 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $1,047 | $-3,120 | $1,067 | $50,000 | $24,124 | $12,560 | $-37,440 | $-13,316 |
| 40% | 1.51 | $2,093 | $-2,073 | $2,133 | $50,000 | $23,598 | $25,120 | $-24,880 | $-1,282 |
| 70% | 2.64 | $3,663 | $-503 | $3,734 | $50,000 | $22,809 | $43,960 | $-6,040 | $16,769 |

### 4. Own used servers in colocation | H200 | spend $50,000

GPUs: 1.06 (about 1). Monthly cost: $386. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $797 | $411 | $812 | $50,393 | $21,522 | $9,560 | $-45,068 | $-23,546 |
| 40% | 2.05 | $1,593 | $1,208 | $1,624 | $50,393 | $21,122 | $19,119 | $-35,508 | $-14,386 |
| 70% | 3.59 | $2,788 | $2,403 | $2,842 | $50,393 | $20,522 | $33,459 | $-21,169 | $-647 |

### 4b. Own servers in colocation, resell time on Vast | H200 | spend $50,000

GPUs: 1.06 (about 1). Monthly cost: $386. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $585 | $200 | $596 | $50,393 | $21,628 | $7,023 | $-47,605 | $-25,976 |
| 40% | 1.51 | $1,170 | $785 | $1,193 | $50,393 | $21,334 | $14,046 | $-40,582 | $-19,247 |
| 70% | 2.64 | $2,048 | $1,663 | $2,088 | $50,393 | $20,893 | $24,580 | $-30,047 | $-9,154 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H200 | spend $50,000

GPUs: 1.90 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 2.53 | $3,518 | $-649 | $3,586 | $50,000 | $22,882 | $42,217 | $-7,783 | $15,099 |
| 40% | 3.18 | $4,419 | $253 | $4,504 | $50,000 | $22,429 | $53,034 | $3,034 | $25,463 |
| 70% | 4.16 | $5,772 | $1,605 | $5,882 | $50,000 | $21,750 | $69,259 | $19,259 | $41,009 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H200 | spend $56,777

GPUs: 2.00 (about 2). Monthly cost: $4,167. Cash at risk: $19,277. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $1,500 | $-2,667 | $2,317 | $19,277 | $8,361 | $20,314 | $-36,463 | $-28,102 |
| 40% | 2.05 | $2,999 | $-1,167 | $4,635 | $19,277 | $7,219 | $40,628 | $-16,149 | $-8,930 |
| 70% | 3.59 | $5,249 | $1,082 | $8,111 | $19,277 | $5,505 | $71,100 | $14,322 | $19,827 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H200 | spend $56,438

GPUs: 1.90 (about 2). Monthly cost: $4,167. Cash at risk: $56,438. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $1,425 | $-2,742 | $2,202 | $56,438 | $26,739 | $19,298 | $-37,140 | $-10,401 |
| 40% | 2.05 | $2,849 | $-1,317 | $4,403 | $56,438 | $25,653 | $38,597 | $-17,841 | $7,812 |
| 70% | 3.59 | $4,987 | $820 | $7,705 | $56,438 | $24,025 | $67,545 | $11,106 | $35,132 |

### 1. Month-to-month, inference | H200 | spend $100,000

GPUs: 3.81 (about 4). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $2,849 | $-5,484 | $2,904 | $8,493 | $2,755 | $34,194 | $-65,806 | $-63,051 |
| 40% | 2.05 | $5,699 | $-2,634 | $5,808 | $8,493 | $1,324 | $68,388 | $-31,612 | $-30,289 |
| 70% | 3.59 | $9,973 | $1,640 | $10,164 | $8,493 | $0 | $119,679 | $19,679 | $19,679 |

### 2a. 3-month prepaid, inference | H200 | spend $100,000

GPUs: 4.01 (about 4). Monthly cost: $8,333. Cash at risk: $25,000. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $2,999 | $-5,334 | $3,057 | $25,000 | $10,818 | $35,994 | $-64,006 | $-53,188 |
| 40% | 2.05 | $5,999 | $-2,334 | $6,114 | $25,000 | $9,311 | $71,987 | $-28,013 | $-18,702 |
| 70% | 3.59 | $10,498 | $2,165 | $10,699 | $25,000 | $7,050 | $125,978 | $25,978 | $33,028 |

### 2b. 12-month prepaid, inference | H200 | spend $100,000

GPUs: 3.81 (about 4). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $2,849 | $-5,484 | $2,904 | $100,000 | $47,868 | $34,194 | $-65,806 | $-17,938 |
| 40% | 2.05 | $5,699 | $-2,634 | $5,808 | $100,000 | $46,437 | $68,388 | $-31,612 | $14,824 |
| 70% | 3.59 | $9,973 | $1,640 | $10,164 | $100,000 | $44,289 | $119,679 | $19,679 | $63,968 |

### 3a. Month-to-month, resell on Vast | H200 | spend $100,000

GPUs: 3.81 (about 4). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $2,093 | $-6,240 | $2,133 | $8,493 | $3,135 | $25,120 | $-74,880 | $-71,745 |
| 40% | 1.51 | $4,187 | $-4,147 | $4,267 | $8,493 | $2,084 | $50,240 | $-49,760 | $-47,676 |
| 70% | 2.64 | $7,327 | $-1,007 | $7,467 | $8,493 | $506 | $87,920 | $-12,080 | $-11,574 |

### 3b. 12-month prepaid, resell on Vast | H200 | spend $100,000

GPUs: 3.81 (about 4). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $2,093 | $-6,240 | $2,133 | $100,000 | $48,248 | $25,120 | $-74,880 | $-26,632 |
| 40% | 1.51 | $4,187 | $-4,147 | $4,267 | $100,000 | $47,196 | $50,240 | $-49,760 | $-2,564 |
| 70% | 2.64 | $7,327 | $-1,007 | $7,467 | $100,000 | $45,619 | $87,920 | $-12,080 | $33,539 |

### 4. Own used servers in colocation | H200 | spend $100,000

GPUs: 2.13 (about 2). Monthly cost: $771. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $1,593 | $822 | $1,624 | $100,786 | $40,123 | $19,119 | $-90,136 | $-50,013 |
| 40% | 2.05 | $3,187 | $2,415 | $3,248 | $100,786 | $39,323 | $38,239 | $-71,016 | $-31,694 |
| 70% | 3.59 | $5,577 | $4,805 | $5,683 | $100,786 | $38,122 | $66,918 | $-42,337 | $-4,215 |

### 4b. Own servers in colocation, resell time on Vast | H200 | spend $100,000

GPUs: 2.13 (about 2). Monthly cost: $771. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $1,170 | $399 | $1,193 | $100,786 | $40,336 | $14,046 | $-95,209 | $-54,874 |
| 40% | 1.51 | $2,341 | $1,570 | $2,386 | $100,786 | $39,748 | $28,092 | $-81,164 | $-41,416 |
| 70% | 2.64 | $4,097 | $3,325 | $4,175 | $100,786 | $38,865 | $49,160 | $-60,095 | $-21,230 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H200 | spend $100,000

GPUs: 3.81 (about 4). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 2.53 | $7,036 | $-1,297 | $7,171 | $100,000 | $45,765 | $84,434 | $-15,566 | $30,199 |
| 40% | 3.18 | $8,839 | $506 | $9,009 | $100,000 | $44,859 | $106,068 | $6,068 | $50,927 |
| 70% | 4.16 | $11,543 | $3,210 | $11,765 | $100,000 | $43,500 | $138,519 | $38,519 | $82,019 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H200 | spend $113,554

GPUs: 4.01 (about 4). Monthly cost: $8,333. Cash at risk: $38,554. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $2,999 | $-5,334 | $4,635 | $38,554 | $16,722 | $40,628 | $-72,926 | $-56,204 |
| 40% | 2.05 | $5,999 | $-2,334 | $9,270 | $38,554 | $14,437 | $81,257 | $-32,298 | $-17,860 |
| 70% | 3.59 | $10,498 | $2,165 | $16,222 | $38,554 | $11,010 | $142,199 | $28,645 | $39,655 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H200 | spend $112,877

GPUs: 3.81 (about 4). Monthly cost: $8,333. Cash at risk: $112,877. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $2,849 | $-5,484 | $4,403 | $112,877 | $53,478 | $38,597 | $-74,280 | $-20,802 |
| 40% | 2.05 | $5,699 | $-2,634 | $8,806 | $112,877 | $51,307 | $77,194 | $-35,683 | $15,624 |
| 70% | 3.59 | $9,973 | $1,640 | $15,411 | $112,877 | $48,051 | $135,089 | $22,213 | $70,263 |

### 1. Month-to-month, inference | H200 | spend $250,000

GPUs: 9.51 (about 10). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $7,124 | $-13,710 | $7,260 | $21,233 | $6,888 | $85,485 | $-164,515 | $-157,627 |
| 40% | 2.05 | $14,247 | $-6,586 | $14,521 | $21,233 | $3,309 | $170,970 | $-79,030 | $-75,721 |
| 70% | 3.59 | $24,933 | $4,100 | $25,411 | $21,233 | $0 | $299,197 | $49,197 | $49,197 |

### 2a. 3-month prepaid, inference | H200 | spend $250,000

GPUs: 10.01 (about 10). Monthly cost: $20,833. Cash at risk: $62,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $7,499 | $-13,335 | $7,642 | $62,500 | $27,045 | $89,984 | $-160,016 | $-132,971 |
| 40% | 2.05 | $14,997 | $-5,836 | $15,285 | $62,500 | $23,277 | $179,968 | $-70,032 | $-46,755 |
| 70% | 3.59 | $26,245 | $5,412 | $26,749 | $62,500 | $17,625 | $314,944 | $64,944 | $82,569 |

### 2b. 12-month prepaid, inference | H200 | spend $250,000

GPUs: 9.51 (about 10). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $7,124 | $-13,710 | $7,260 | $250,000 | $119,671 | $85,485 | $-164,515 | $-44,845 |
| 40% | 2.05 | $14,247 | $-6,586 | $14,521 | $250,000 | $116,091 | $170,970 | $-79,030 | $37,061 |
| 70% | 3.59 | $24,933 | $4,100 | $25,411 | $250,000 | $110,722 | $299,197 | $49,197 | $159,919 |

### 3a. Month-to-month, resell on Vast | H200 | spend $250,000

GPUs: 9.51 (about 10). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $5,233 | $-15,600 | $5,334 | $21,233 | $7,838 | $62,800 | $-187,200 | $-179,362 |
| 40% | 1.51 | $10,467 | $-10,367 | $10,667 | $21,233 | $5,209 | $125,600 | $-124,400 | $-119,191 |
| 70% | 2.64 | $18,317 | $-2,517 | $18,668 | $21,233 | $1,265 | $219,800 | $-30,200 | $-28,935 |

### 3b. 12-month prepaid, resell on Vast | H200 | spend $250,000

GPUs: 9.51 (about 10). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $5,233 | $-15,600 | $5,334 | $250,000 | $120,620 | $62,800 | $-187,200 | $-66,580 |
| 40% | 1.51 | $10,467 | $-10,367 | $10,667 | $250,000 | $117,991 | $125,600 | $-124,400 | $-6,409 |
| 70% | 2.64 | $18,317 | $-2,517 | $18,668 | $250,000 | $114,047 | $219,800 | $-30,200 | $83,847 |

### 4. Own used servers in colocation | H200 | spend $250,000

GPUs: 5.32 (about 5). Monthly cost: $1,928. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $3,983 | $2,055 | $4,060 | $251,965 | $93,005 | $47,799 | $-225,340 | $-132,335 |
| 40% | 2.05 | $7,966 | $6,038 | $8,119 | $251,965 | $91,004 | $95,597 | $-177,541 | $-86,537 |
| 70% | 3.59 | $13,941 | $12,013 | $14,209 | $251,965 | $88,001 | $167,296 | $-105,843 | $-17,841 |

### 4b. Own servers in colocation, resell time on Vast | H200 | spend $250,000

GPUs: 5.32 (about 5). Monthly cost: $1,928. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.75 | $2,926 | $998 | $2,982 | $251,965 | $93,536 | $35,115 | $-238,024 | $-144,488 |
| 40% | 1.51 | $5,852 | $3,924 | $5,965 | $251,965 | $92,066 | $70,229 | $-202,909 | $-110,843 |
| 70% | 2.64 | $10,242 | $8,314 | $10,438 | $251,965 | $89,860 | $122,901 | $-150,237 | $-60,377 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H200 | spend $250,000

GPUs: 9.51 (about 10). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 2.53 | $17,590 | $-3,243 | $17,928 | $250,000 | $114,412 | $211,085 | $-38,915 | $75,496 |
| 40% | 3.18 | $22,097 | $1,264 | $22,521 | $250,000 | $112,147 | $265,170 | $15,170 | $127,317 |
| 70% | 4.16 | $28,858 | $8,025 | $29,412 | $250,000 | $108,750 | $346,297 | $96,297 | $205,047 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H200 | spend $283,886

GPUs: 10.01 (about 10). Monthly cost: $20,833. Cash at risk: $96,386. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $7,499 | $-13,335 | $11,587 | $96,386 | $41,806 | $101,571 | $-182,315 | $-140,509 |
| 40% | 2.05 | $14,997 | $-5,836 | $23,174 | $96,386 | $36,094 | $203,142 | $-80,744 | $-44,651 |
| 70% | 3.59 | $26,245 | $5,412 | $40,554 | $96,386 | $27,525 | $355,498 | $71,612 | $99,137 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H200 | spend $282,192

GPUs: 9.51 (about 10). Monthly cost: $20,833. Cash at risk: $282,192. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.03 | $7,124 | $-13,710 | $11,008 | $282,192 | $128,076 | $96,492 | $-185,699 | $-57,624 |
| 40% | 2.05 | $14,247 | $-6,586 | $22,015 | $282,192 | $126,722 | $192,985 | $-89,207 | $37,515 |
| 70% | 3.59 | $24,933 | $4,100 | $38,527 | $282,192 | $120,127 | $337,724 | $55,532 | $175,659 |

### 1. Month-to-month, inference | B200 | spend $50,000

GPUs: 1.63 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $4,580 | $413 | $4,667 | $4,247 | $0 | $54,955 | $4,955 | $4,955 |
| 40% | 7.69 | $9,159 | $4,992 | $9,335 | $4,247 | $0 | $109,909 | $59,909 | $59,909 |
| 70% | 13.46 | $16,028 | $11,862 | $16,336 | $4,247 | $0 | $192,341 | $142,341 | $142,341 |

### 2a. 3-month prepaid, inference | B200 | spend $50,000

GPUs: 1.71 (about 2). Monthly cost: $4,167. Cash at risk: $12,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $4,813 | $647 | $4,906 | $12,500 | $3,744 | $57,760 | $7,760 | $11,504 |
| 40% | 7.69 | $9,627 | $5,460 | $9,811 | $12,500 | $1,326 | $115,520 | $65,520 | $66,846 |
| 70% | 13.46 | $16,847 | $12,680 | $17,170 | $12,500 | $0 | $202,160 | $152,160 | $152,160 |

### 2b. 12-month prepaid, inference | B200 | spend $50,000

GPUs: 1.63 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $4,580 | $413 | $4,667 | $50,000 | $22,349 | $54,955 | $4,955 | $27,304 |
| 40% | 7.69 | $9,159 | $4,992 | $9,335 | $50,000 | $20,048 | $109,909 | $59,909 | $79,957 |
| 70% | 13.46 | $16,028 | $11,862 | $16,336 | $50,000 | $16,596 | $192,341 | $142,341 | $158,937 |

### 3a. Month-to-month, resell on Vast | B200 | spend $50,000

GPUs: 1.63 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $1,905 | $-2,262 | $1,941 | $4,247 | $1,137 | $22,857 | $-27,143 | $-26,006 |
| 40% | 3.20 | $3,810 | $-357 | $3,883 | $4,247 | $179 | $45,714 | $-4,286 | $-4,106 |
| 70% | 5.60 | $6,667 | $2,500 | $6,795 | $4,247 | $0 | $80,000 | $30,000 | $30,000 |

### 3b. 12-month prepaid, resell on Vast | B200 | spend $50,000

GPUs: 1.63 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $1,905 | $-2,262 | $1,941 | $50,000 | $23,693 | $22,857 | $-27,143 | $-3,450 |
| 40% | 3.20 | $3,810 | $-357 | $3,883 | $50,000 | $22,736 | $45,714 | $-4,286 | $18,450 |
| 70% | 5.60 | $6,667 | $2,500 | $6,795 | $50,000 | $21,300 | $80,000 | $30,000 | $51,300 |

### 4. Own used servers in colocation | B200 | spend $50,000

GPUs: 0.88 (about 1). Monthly cost: $359. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $2,458 | $2,099 | $2,505 | $50,366 | $20,674 | $29,495 | $-24,811 | $-4,137 |
| 40% | 7.69 | $4,916 | $4,557 | $5,010 | $50,366 | $19,439 | $58,990 | $4,684 | $24,123 |
| 70% | 13.46 | $8,603 | $8,244 | $8,768 | $50,366 | $17,587 | $103,233 | $48,926 | $66,513 |

### 4b. Own servers in colocation, resell time on Vast | B200 | spend $50,000

GPUs: 0.88 (about 1). Monthly cost: $359. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $1,022 | $663 | $1,042 | $50,366 | $21,395 | $12,268 | $-42,039 | $-20,643 |
| 40% | 3.20 | $2,045 | $1,686 | $2,084 | $50,366 | $20,882 | $24,536 | $-29,771 | $-8,889 |
| 70% | 5.60 | $3,578 | $3,219 | $3,647 | $50,366 | $20,111 | $42,937 | $-11,369 | $8,742 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | B200 | spend $50,000

GPUs: 1.63 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 7.05 | $8,389 | $4,222 | $8,550 | $50,000 | $20,435 | $100,669 | $50,669 | $71,104 |
| 40% | 10.09 | $12,016 | $7,850 | $12,247 | $50,000 | $18,612 | $144,195 | $94,195 | $112,807 |
| 70% | 14.66 | $17,457 | $13,290 | $17,792 | $50,000 | $15,879 | $209,484 | $159,484 | $175,362 |

### 6a. Staged: test month-to-month, then 3-month prepaid | B200 | spend $60,634

GPUs: 1.71 (about 2). Monthly cost: $4,167. Cash at risk: $23,134. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $4,813 | $647 | $7,438 | $23,134 | $7,738 | $65,198 | $4,564 | $12,302 |
| 40% | 7.69 | $9,627 | $5,460 | $14,875 | $23,134 | $4,072 | $130,395 | $69,761 | $73,833 |
| 70% | 13.46 | $16,847 | $12,680 | $26,032 | $23,134 | $0 | $228,192 | $167,558 | $167,558 |

### 6b. Staged: test month-to-month, then 12-month prepaid | B200 | spend $60,117

GPUs: 1.63 (about 2). Monthly cost: $4,167. Cash at risk: $60,117. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $4,580 | $413 | $7,076 | $60,117 | $26,149 | $62,031 | $1,913 | $28,063 |
| 40% | 7.69 | $9,159 | $4,992 | $14,153 | $60,117 | $22,661 | $124,062 | $63,944 | $86,605 |
| 70% | 13.46 | $16,028 | $11,862 | $24,767 | $60,117 | $17,428 | $217,108 | $156,991 | $174,418 |

### 1. Month-to-month, inference | B200 | spend $100,000

GPUs: 3.26 (about 3). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $9,159 | $826 | $9,335 | $8,493 | $0 | $109,909 | $9,909 | $9,909 |
| 40% | 7.69 | $18,318 | $9,985 | $18,669 | $8,493 | $0 | $219,818 | $119,818 | $119,818 |
| 70% | 13.46 | $32,057 | $23,723 | $32,672 | $8,493 | $0 | $384,682 | $284,682 | $284,682 |

### 2a. 3-month prepaid, inference | B200 | spend $100,000

GPUs: 3.43 (about 3). Monthly cost: $8,333. Cash at risk: $25,000. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $9,627 | $1,293 | $9,811 | $25,000 | $7,488 | $115,520 | $15,520 | $23,008 |
| 40% | 7.69 | $19,253 | $10,920 | $19,623 | $25,000 | $2,651 | $231,040 | $131,040 | $133,691 |
| 70% | 13.46 | $33,693 | $25,360 | $34,340 | $25,000 | $0 | $404,320 | $304,320 | $304,320 |

### 2b. 12-month prepaid, inference | B200 | spend $100,000

GPUs: 3.26 (about 3). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $9,159 | $826 | $9,335 | $100,000 | $44,698 | $109,909 | $9,909 | $54,607 |
| 40% | 7.69 | $18,318 | $9,985 | $18,669 | $100,000 | $40,096 | $219,818 | $119,818 | $159,914 |
| 70% | 13.46 | $32,057 | $23,723 | $32,672 | $100,000 | $33,193 | $384,682 | $284,682 | $317,875 |

### 3a. Month-to-month, resell on Vast | B200 | spend $100,000

GPUs: 3.26 (about 3). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $3,810 | $-4,524 | $3,883 | $8,493 | $2,273 | $45,714 | $-54,286 | $-52,013 |
| 40% | 3.20 | $7,619 | $-714 | $7,765 | $8,493 | $359 | $91,429 | $-8,571 | $-8,213 |
| 70% | 5.60 | $13,333 | $5,000 | $13,589 | $8,493 | $0 | $160,000 | $60,000 | $60,000 |

### 3b. 12-month prepaid, resell on Vast | B200 | spend $100,000

GPUs: 3.26 (about 3). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $3,810 | $-4,524 | $3,883 | $100,000 | $47,386 | $45,714 | $-54,286 | $-6,900 |
| 40% | 3.20 | $7,619 | $-714 | $7,765 | $100,000 | $45,472 | $91,429 | $-8,571 | $36,900 |
| 70% | 5.60 | $13,333 | $5,000 | $13,589 | $100,000 | $42,601 | $160,000 | $60,000 | $102,601 |

### 4. Own used servers in colocation | B200 | spend $100,000

GPUs: 1.75 (about 2). Monthly cost: $718. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $4,916 | $4,198 | $5,010 | $100,731 | $38,427 | $58,990 | $-49,623 | $-11,196 |
| 40% | 7.69 | $9,832 | $9,114 | $10,020 | $100,731 | $35,957 | $117,980 | $9,368 | $45,324 |
| 70% | 13.46 | $17,205 | $16,488 | $17,535 | $100,731 | $32,252 | $206,465 | $97,853 | $130,105 |

### 4b. Own servers in colocation, resell time on Vast | B200 | spend $100,000

GPUs: 1.75 (about 2). Monthly cost: $718. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $2,045 | $1,327 | $2,084 | $100,731 | $39,870 | $24,536 | $-84,077 | $-44,207 |
| 40% | 3.20 | $4,089 | $3,372 | $4,168 | $100,731 | $38,842 | $49,071 | $-59,541 | $-20,699 |
| 70% | 5.60 | $7,156 | $6,439 | $7,293 | $100,731 | $37,301 | $85,875 | $-22,738 | $14,563 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | B200 | spend $100,000

GPUs: 3.26 (about 3). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 7.05 | $16,778 | $8,445 | $17,100 | $100,000 | $40,870 | $201,338 | $101,338 | $142,207 |
| 40% | 10.09 | $24,032 | $15,699 | $24,493 | $100,000 | $37,225 | $288,389 | $188,389 | $225,614 |
| 70% | 14.66 | $34,914 | $26,581 | $35,584 | $100,000 | $31,757 | $418,967 | $318,967 | $350,725 |

### 6a. Staged: test month-to-month, then 3-month prepaid | B200 | spend $121,268

GPUs: 3.43 (about 3). Monthly cost: $8,333. Cash at risk: $46,268. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $9,627 | $1,293 | $14,875 | $46,268 | $15,477 | $130,395 | $9,127 | $24,604 |
| 40% | 7.69 | $19,253 | $10,920 | $29,750 | $46,268 | $8,143 | $260,790 | $139,523 | $147,666 |
| 70% | 13.46 | $33,693 | $25,360 | $52,063 | $46,268 | $0 | $456,383 | $335,115 | $335,115 |

### 6b. Staged: test month-to-month, then 12-month prepaid | B200 | spend $120,235

GPUs: 3.26 (about 3). Monthly cost: $8,333. Cash at risk: $120,235. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $9,159 | $826 | $14,153 | $120,235 | $52,299 | $124,062 | $3,827 | $56,125 |
| 40% | 7.69 | $18,318 | $9,985 | $28,305 | $120,235 | $45,321 | $248,123 | $127,889 | $173,210 |
| 70% | 13.46 | $32,057 | $23,723 | $49,534 | $120,235 | $34,855 | $434,216 | $313,981 | $348,836 |

### 1. Month-to-month, inference | B200 | spend $250,000

GPUs: 8.15 (about 8). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $22,898 | $2,064 | $23,337 | $21,233 | $0 | $274,773 | $24,773 | $24,773 |
| 40% | 7.69 | $45,795 | $24,962 | $46,674 | $21,233 | $0 | $549,545 | $299,545 | $299,545 |
| 70% | 13.46 | $80,142 | $59,309 | $81,679 | $21,233 | $0 | $961,704 | $711,704 | $711,704 |

### 2a. 3-month prepaid, inference | B200 | spend $250,000

GPUs: 8.57 (about 9). Monthly cost: $20,833. Cash at risk: $62,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $24,067 | $3,233 | $24,528 | $62,500 | $18,720 | $288,800 | $38,800 | $57,520 |
| 40% | 7.69 | $48,133 | $27,300 | $49,056 | $62,500 | $6,628 | $577,600 | $327,600 | $334,228 |
| 70% | 13.46 | $84,233 | $63,400 | $85,849 | $62,500 | $0 | $1,010,800 | $760,800 | $760,800 |

### 2b. 12-month prepaid, inference | B200 | spend $250,000

GPUs: 8.15 (about 8). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $22,898 | $2,064 | $23,337 | $250,000 | $111,745 | $274,773 | $24,773 | $136,518 |
| 40% | 7.69 | $45,795 | $24,962 | $46,674 | $250,000 | $100,240 | $549,545 | $299,545 | $399,785 |
| 70% | 13.46 | $80,142 | $59,309 | $81,679 | $250,000 | $82,982 | $961,704 | $711,704 | $794,686 |

### 3a. Month-to-month, resell on Vast | B200 | spend $250,000

GPUs: 8.15 (about 8). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $9,524 | $-11,310 | $9,706 | $21,233 | $5,683 | $114,286 | $-135,714 | $-130,032 |
| 40% | 3.20 | $19,048 | $-1,786 | $19,413 | $21,233 | $897 | $228,571 | $-21,429 | $-20,531 |
| 70% | 5.60 | $33,333 | $12,500 | $33,973 | $21,233 | $0 | $400,000 | $150,000 | $150,000 |

### 3b. 12-month prepaid, resell on Vast | B200 | spend $250,000

GPUs: 8.15 (about 8). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $9,524 | $-11,310 | $9,706 | $250,000 | $118,465 | $114,286 | $-135,714 | $-17,250 |
| 40% | 3.20 | $19,048 | $-1,786 | $19,413 | $250,000 | $113,679 | $228,571 | $-21,429 | $92,251 |
| 70% | 5.60 | $33,333 | $12,500 | $33,973 | $250,000 | $106,502 | $400,000 | $150,000 | $256,502 |

### 4. Own used servers in colocation | B200 | spend $250,000

GPUs: 4.38 (about 4). Monthly cost: $1,794. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $12,290 | $10,495 | $12,525 | $251,829 | $88,764 | $147,475 | $-124,056 | $-35,292 |
| 40% | 7.69 | $24,579 | $22,785 | $25,051 | $251,829 | $83,908 | $294,951 | $23,419 | $107,327 |
| 70% | 13.46 | $43,014 | $41,219 | $43,839 | $251,829 | $76,956 | $516,164 | $244,632 | $321,588 |

### 4b. Own servers in colocation, resell time on Vast | B200 | spend $250,000

GPUs: 4.38 (about 4). Monthly cost: $1,794. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 1.60 | $5,112 | $3,317 | $5,210 | $251,829 | $92,371 | $61,339 | $-210,193 | $-117,822 |
| 40% | 3.20 | $10,223 | $8,429 | $10,419 | $251,829 | $89,802 | $122,678 | $-148,853 | $-59,051 |
| 70% | 5.60 | $17,891 | $16,096 | $18,234 | $251,829 | $86,430 | $214,687 | $-56,845 | $29,586 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | B200 | spend $250,000

GPUs: 8.15 (about 8). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 7.05 | $41,945 | $21,112 | $42,750 | $250,000 | $102,174 | $503,344 | $253,344 | $355,518 |
| 40% | 10.09 | $60,081 | $39,248 | $61,233 | $250,000 | $93,062 | $720,974 | $470,974 | $564,036 |
| 70% | 14.66 | $87,285 | $66,452 | $88,959 | $250,000 | $79,393 | $1,047,418 | $797,418 | $876,812 |

### 6a. Staged: test month-to-month, then 3-month prepaid | B200 | spend $303,170

GPUs: 8.57 (about 9). Monthly cost: $20,833. Cash at risk: $115,670. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $24,067 | $3,233 | $37,188 | $115,670 | $38,691 | $325,988 | $22,818 | $61,510 |
| 40% | 7.69 | $48,133 | $27,300 | $74,376 | $115,670 | $20,358 | $651,976 | $348,806 | $369,164 |
| 70% | 13.46 | $84,233 | $63,400 | $130,158 | $115,670 | $0 | $1,140,958 | $837,788 | $837,788 |

### 6b. Staged: test month-to-month, then 12-month prepaid | B200 | spend $300,587

GPUs: 8.15 (about 8). Monthly cost: $20,833. Cash at risk: $300,587. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.85 | $22,898 | $2,064 | $35,382 | $300,587 | $127,340 | $310,154 | $9,567 | $136,907 |
| 40% | 7.69 | $45,795 | $24,962 | $70,763 | $300,587 | $113,303 | $620,308 | $319,721 | $433,025 |
| 70% | 13.46 | $80,142 | $59,309 | $123,836 | $300,587 | $87,138 | $1,085,540 | $784,953 | $872,091 |

### 1. Month-to-month, inference | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $321 | $-3,846 | $327 | $4,247 | $1,932 | $3,849 | $-46,151 | $-44,219 |
| 40% | 0.35 | $641 | $-3,525 | $654 | $4,247 | $1,771 | $7,697 | $-42,303 | $-40,531 |
| 70% | 0.62 | $1,123 | $-3,044 | $1,144 | $4,247 | $1,530 | $13,470 | $-36,530 | $-35,000 |

### 2a. 3-month prepaid, inference | H100 | spend $50,000

GPUs: 3.22 (about 3). Monthly cost: $4,167. Cash at risk: $12,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $417 | $-3,750 | $425 | $12,500 | $5,953 | $5,001 | $-44,999 | $-39,046 |
| 40% | 0.35 | $834 | $-3,333 | $849 | $12,500 | $5,744 | $10,002 | $-39,998 | $-34,254 |
| 70% | 0.62 | $1,459 | $-2,708 | $1,487 | $12,500 | $5,430 | $17,504 | $-32,496 | $-27,067 |

### 2b. 12-month prepaid, inference | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $321 | $-3,846 | $327 | $50,000 | $24,489 | $3,849 | $-46,151 | $-21,662 |
| 40% | 0.35 | $641 | $-3,525 | $654 | $50,000 | $24,328 | $7,697 | $-42,303 | $-17,975 |
| 70% | 0.62 | $1,123 | $-3,044 | $1,144 | $50,000 | $24,086 | $13,470 | $-36,530 | $-12,444 |

### 3a. Month-to-month, resell on Vast | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $733 | $-3,433 | $747 | $4,247 | $1,725 | $8,800 | $-41,200 | $-39,475 |
| 40% | 0.81 | $1,467 | $-2,700 | $1,495 | $4,247 | $1,357 | $17,600 | $-32,400 | $-31,043 |
| 70% | 1.42 | $2,567 | $-1,600 | $2,616 | $4,247 | $804 | $30,800 | $-19,200 | $-18,396 |

### 3b. 12-month prepaid, resell on Vast | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $733 | $-3,433 | $747 | $50,000 | $24,282 | $8,800 | $-41,200 | $-16,918 |
| 40% | 0.81 | $1,467 | $-2,700 | $1,495 | $50,000 | $23,913 | $17,600 | $-32,400 | $-8,487 |
| 70% | 1.42 | $2,567 | $-1,600 | $2,616 | $50,000 | $23,360 | $30,800 | $-19,200 | $4,160 |

### 4. Own used servers in colocation | H100 | spend $50,000

GPUs: 2.17 (about 2). Monthly cost: $786. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $280 | $-506 | $286 | $50,801 | $21,983 | $3,362 | $-56,069 | $-34,086 |
| 40% | 0.35 | $560 | $-226 | $571 | $50,801 | $21,842 | $6,725 | $-52,706 | $-30,864 |
| 70% | 0.62 | $981 | $195 | $999 | $50,801 | $21,631 | $11,768 | $-47,663 | $-26,032 |

### 4b. Own servers in colocation, resell time on Vast | H100 | spend $50,000

GPUs: 2.17 (about 2). Monthly cost: $786. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $641 | $-145 | $653 | $50,801 | $21,802 | $7,688 | $-51,743 | $-29,941 |
| 40% | 0.81 | $1,281 | $495 | $1,306 | $50,801 | $21,480 | $15,376 | $-44,055 | $-22,575 |
| 70% | 1.42 | $2,242 | $1,456 | $2,285 | $50,801 | $20,997 | $26,908 | $-32,523 | $-11,526 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H100 | spend $50,000

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.99 | $1,787 | $-2,379 | $1,822 | $50,000 | $23,752 | $21,449 | $-28,551 | $-4,799 |
| 40% | 0.96 | $1,741 | $-2,425 | $1,775 | $50,000 | $23,775 | $20,897 | $-29,103 | $-5,328 |
| 70% | 0.92 | $1,673 | $-2,494 | $1,705 | $50,000 | $23,810 | $20,070 | $-29,930 | $-6,120 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H100 | spend $59,094

GPUs: 3.22 (about 3). Monthly cost: $4,167. Cash at risk: $21,594. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $417 | $-3,750 | $644 | $21,594 | $10,328 | $5,645 | $-53,449 | $-43,120 |
| 40% | 0.35 | $834 | $-3,333 | $1,288 | $21,594 | $10,011 | $11,290 | $-47,804 | $-37,793 |
| 70% | 0.62 | $1,459 | $-2,708 | $2,254 | $21,594 | $9,535 | $19,758 | $-39,336 | $-29,801 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H100 | spend $56,998

GPUs: 2.48 (about 2). Monthly cost: $4,167. Cash at risk: $56,998. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $321 | $-3,846 | $496 | $56,998 | $27,856 | $4,344 | $-52,654 | $-24,798 |
| 40% | 0.35 | $641 | $-3,525 | $991 | $56,998 | $27,611 | $8,688 | $-48,310 | $-20,698 |
| 70% | 0.62 | $1,123 | $-3,044 | $1,735 | $56,998 | $27,245 | $15,205 | $-41,793 | $-14,548 |

### 1. Month-to-month, inference | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $641 | $-7,692 | $654 | $8,493 | $3,865 | $7,697 | $-92,303 | $-88,438 |
| 40% | 0.35 | $1,283 | $-7,050 | $1,307 | $8,493 | $3,543 | $15,395 | $-84,605 | $-81,063 |
| 70% | 0.62 | $2,245 | $-6,088 | $2,288 | $8,493 | $3,059 | $26,941 | $-73,059 | $-70,000 |

### 2a. 3-month prepaid, inference | H100 | spend $100,000

GPUs: 6.45 (about 6). Monthly cost: $8,333. Cash at risk: $25,000. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $834 | $-7,500 | $849 | $25,000 | $11,906 | $10,002 | $-89,998 | $-78,092 |
| 40% | 0.35 | $1,667 | $-6,666 | $1,699 | $25,000 | $11,487 | $20,004 | $-79,996 | $-68,508 |
| 70% | 0.62 | $2,917 | $-5,416 | $2,973 | $25,000 | $10,859 | $35,008 | $-64,992 | $-54,133 |

### 2b. 12-month prepaid, inference | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $641 | $-7,692 | $654 | $100,000 | $48,978 | $7,697 | $-92,303 | $-43,325 |
| 40% | 0.35 | $1,283 | $-7,050 | $1,307 | $100,000 | $48,655 | $15,395 | $-84,605 | $-35,950 |
| 70% | 0.62 | $2,245 | $-6,088 | $2,288 | $100,000 | $48,172 | $26,941 | $-73,059 | $-24,887 |

### 3a. Month-to-month, resell on Vast | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $1,467 | $-6,867 | $1,495 | $8,493 | $3,450 | $17,600 | $-82,400 | $-78,950 |
| 40% | 0.81 | $2,933 | $-5,400 | $2,990 | $8,493 | $2,713 | $35,200 | $-64,800 | $-62,087 |
| 70% | 1.42 | $5,133 | $-3,200 | $5,232 | $8,493 | $1,608 | $61,600 | $-38,400 | $-36,792 |

### 3b. 12-month prepaid, resell on Vast | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $1,467 | $-6,867 | $1,495 | $100,000 | $48,563 | $17,600 | $-82,400 | $-33,837 |
| 40% | 0.81 | $2,933 | $-5,400 | $2,990 | $100,000 | $47,826 | $35,200 | $-64,800 | $-16,974 |
| 70% | 1.42 | $5,133 | $-3,200 | $5,232 | $100,000 | $46,721 | $61,600 | $-38,400 | $8,321 |

### 4. Own used servers in colocation | H100 | spend $100,000

GPUs: 4.34 (about 4). Monthly cost: $1,572. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $560 | $-1,011 | $571 | $101,602 | $41,044 | $6,725 | $-112,137 | $-71,093 |
| 40% | 0.35 | $1,121 | $-451 | $1,142 | $101,602 | $40,763 | $13,449 | $-105,413 | $-64,650 |
| 70% | 0.62 | $1,961 | $390 | $1,999 | $101,602 | $40,341 | $23,536 | $-95,326 | $-54,985 |

### 4b. Own servers in colocation, resell time on Vast | H100 | spend $100,000

GPUs: 4.34 (about 4). Monthly cost: $1,572. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $1,281 | $-290 | $1,306 | $101,602 | $40,682 | $15,376 | $-103,486 | $-62,804 |
| 40% | 0.81 | $2,563 | $991 | $2,612 | $101,602 | $40,038 | $30,752 | $-88,110 | $-48,072 |
| 70% | 1.42 | $4,485 | $2,913 | $4,571 | $101,602 | $39,073 | $53,815 | $-65,046 | $-25,974 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H100 | spend $100,000

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.99 | $3,575 | $-4,759 | $3,643 | $100,000 | $47,504 | $42,897 | $-57,103 | $-9,599 |
| 40% | 0.96 | $3,483 | $-4,850 | $3,550 | $100,000 | $47,550 | $41,795 | $-58,205 | $-10,655 |
| 70% | 0.92 | $3,345 | $-4,988 | $3,409 | $100,000 | $47,619 | $40,141 | $-59,859 | $-12,240 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H100 | spend $118,187

GPUs: 6.45 (about 6). Monthly cost: $8,333. Cash at risk: $43,187. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $834 | $-7,500 | $1,288 | $43,187 | $20,656 | $11,290 | $-106,897 | $-86,241 |
| 40% | 0.35 | $1,667 | $-6,666 | $2,576 | $43,187 | $20,021 | $22,580 | $-95,607 | $-75,586 |
| 70% | 0.62 | $2,917 | $-5,416 | $4,508 | $43,187 | $19,069 | $39,515 | $-78,672 | $-59,603 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H100 | spend $113,996

GPUs: 4.96 (about 5). Monthly cost: $8,333. Cash at risk: $113,996. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $641 | $-7,692 | $991 | $113,996 | $55,712 | $8,688 | $-105,308 | $-49,596 |
| 40% | 0.35 | $1,283 | $-7,050 | $1,982 | $113,996 | $55,223 | $17,377 | $-96,619 | $-41,397 |
| 70% | 0.62 | $2,245 | $-6,088 | $3,469 | $113,996 | $54,490 | $30,410 | $-83,587 | $-29,097 |

### 1. Month-to-month, inference | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $1,604 | $-19,230 | $1,634 | $21,233 | $9,662 | $19,243 | $-230,757 | $-221,095 |
| 40% | 0.35 | $3,207 | $-17,626 | $3,269 | $21,233 | $8,856 | $38,487 | $-211,513 | $-202,657 |
| 70% | 0.62 | $5,613 | $-15,221 | $5,720 | $21,233 | $7,648 | $67,352 | $-182,648 | $-175,001 |

### 2a. 3-month prepaid, inference | H100 | spend $250,000

GPUs: 16.12 (about 16). Monthly cost: $20,833. Cash at risk: $62,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $2,084 | $-18,750 | $2,124 | $62,500 | $29,765 | $25,005 | $-224,995 | $-195,229 |
| 40% | 0.35 | $4,168 | $-16,666 | $4,247 | $62,500 | $28,718 | $50,011 | $-199,989 | $-171,271 |
| 70% | 0.62 | $7,293 | $-13,540 | $7,433 | $62,500 | $27,148 | $87,519 | $-162,481 | $-135,333 |

### 2b. 12-month prepaid, inference | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $1,604 | $-19,230 | $1,634 | $250,000 | $122,444 | $19,243 | $-230,757 | $-108,312 |
| 40% | 0.35 | $3,207 | $-17,626 | $3,269 | $250,000 | $121,639 | $38,487 | $-211,513 | $-89,875 |
| 70% | 0.62 | $5,613 | $-15,221 | $5,720 | $250,000 | $120,430 | $67,352 | $-182,648 | $-62,219 |

### 3a. Month-to-month, resell on Vast | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $3,667 | $-17,167 | $3,737 | $21,233 | $8,625 | $44,000 | $-206,000 | $-197,375 |
| 40% | 0.81 | $7,333 | $-13,500 | $7,474 | $21,233 | $6,783 | $88,000 | $-162,000 | $-155,217 |
| 70% | 1.42 | $12,833 | $-8,000 | $13,079 | $21,233 | $4,020 | $154,000 | $-96,000 | $-91,980 |

### 3b. 12-month prepaid, resell on Vast | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $3,667 | $-17,167 | $3,737 | $250,000 | $121,408 | $44,000 | $-206,000 | $-84,592 |
| 40% | 0.81 | $7,333 | $-13,500 | $7,474 | $250,000 | $119,565 | $88,000 | $-162,000 | $-42,435 |
| 70% | 1.42 | $12,833 | $-8,000 | $13,079 | $250,000 | $116,802 | $154,000 | $-96,000 | $20,802 |

### 4. Own used servers in colocation | H100 | spend $250,000

GPUs: 10.84 (about 11). Monthly cost: $3,930. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $1,401 | $-2,529 | $1,428 | $254,005 | $95,308 | $16,811 | $-280,343 | $-185,035 |
| 40% | 0.35 | $2,802 | $-1,128 | $2,856 | $254,005 | $94,604 | $33,623 | $-263,532 | $-168,927 |
| 70% | 0.62 | $4,903 | $974 | $4,997 | $254,005 | $93,548 | $58,840 | $-238,314 | $-144,766 |

### 4b. Own servers in colocation, resell time on Vast | H100 | spend $250,000

GPUs: 10.84 (about 11). Monthly cost: $3,930. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.40 | $3,203 | $-726 | $3,265 | $254,005 | $94,402 | $38,440 | $-258,715 | $-164,313 |
| 40% | 0.81 | $6,407 | $2,477 | $6,529 | $254,005 | $92,793 | $76,879 | $-220,275 | $-127,482 |
| 70% | 1.42 | $11,212 | $7,282 | $11,427 | $254,005 | $90,379 | $134,538 | $-162,616 | $-72,237 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | H100 | spend $250,000

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.99 | $8,937 | $-11,896 | $9,108 | $250,000 | $118,760 | $107,243 | $-142,757 | $-23,997 |
| 40% | 0.96 | $8,707 | $-12,126 | $8,874 | $250,000 | $118,875 | $104,487 | $-145,513 | $-26,638 |
| 70% | 0.92 | $8,363 | $-12,471 | $8,523 | $250,000 | $119,048 | $100,352 | $-149,648 | $-30,600 |

### 6a. Staged: test month-to-month, then 3-month prepaid | H100 | spend $295,469

GPUs: 16.12 (about 16). Monthly cost: $20,833. Cash at risk: $107,969. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $2,084 | $-18,750 | $3,220 | $107,969 | $51,641 | $28,225 | $-267,243 | $-215,602 |
| 40% | 0.35 | $4,168 | $-16,666 | $6,440 | $107,969 | $50,054 | $56,451 | $-239,018 | $-188,964 |
| 70% | 0.62 | $7,293 | $-13,540 | $11,270 | $107,969 | $47,673 | $98,789 | $-196,680 | $-149,007 |

### 6b. Staged: test month-to-month, then 12-month prepaid | H100 | spend $284,991

GPUs: 12.41 (about 12). Monthly cost: $20,833. Cash at risk: $284,991. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.18 | $1,604 | $-19,230 | $2,478 | $284,991 | $129,469 | $21,721 | $-263,270 | $-133,801 |
| 40% | 0.35 | $3,207 | $-17,626 | $4,956 | $284,991 | $129,164 | $43,442 | $-241,549 | $-112,384 |
| 70% | 0.62 | $5,613 | $-15,221 | $8,673 | $284,991 | $128,707 | $76,024 | $-208,967 | $-80,260 |

### 1. Month-to-month, inference | MI355X | spend $50,000

GPUs: 2.20 (about 2). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $5,570 | $1,403 | $5,677 | $4,247 | $0 | $66,837 | $16,837 | $16,837 |
| 40% | 6.92 | $11,139 | $6,973 | $11,353 | $4,247 | $0 | $133,673 | $83,673 | $83,673 |
| 70% | 12.12 | $19,494 | $15,327 | $19,868 | $4,247 | $0 | $233,928 | $183,928 | $183,928 |

### 2a. 3-month prepaid, inference | MI355X | spend $50,000

GPUs: 2.32 (about 2). Monthly cost: $4,167. Cash at risk: $12,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $5,864 | $1,697 | $5,977 | $12,500 | $3,216 | $70,369 | $20,369 | $23,585 |
| 40% | 6.92 | $11,728 | $7,561 | $11,953 | $12,500 | $270 | $140,737 | $90,737 | $91,007 |
| 70% | 12.12 | $20,524 | $16,358 | $20,918 | $12,500 | $0 | $246,290 | $196,290 | $196,290 |

### 2b. 12-month prepaid, inference | MI355X | spend $50,000

GPUs: 2.20 (about 2). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $5,570 | $1,403 | $5,677 | $50,000 | $21,851 | $66,837 | $16,837 | $38,688 |
| 40% | 6.92 | $11,139 | $6,973 | $11,353 | $50,000 | $19,053 | $133,673 | $83,673 | $102,726 |
| 70% | 12.12 | $19,494 | $15,327 | $19,868 | $50,000 | $14,855 | $233,928 | $183,928 | $198,783 |

### 6a. Staged: test month-to-month, then 3-month prepaid | MI355X | spend $56,779

GPUs: 2.32 (about 2). Monthly cost: $4,167. Cash at risk: $19,279. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $5,864 | $1,697 | $9,061 | $19,279 | $5,037 | $79,430 | $22,651 | $27,688 |
| 40% | 6.92 | $11,728 | $7,561 | $18,122 | $19,279 | $570 | $158,859 | $102,081 | $102,651 |
| 70% | 12.12 | $20,524 | $16,358 | $31,714 | $19,279 | $0 | $278,004 | $221,226 | $221,226 |

### 6b. Staged: test month-to-month, then 12-month prepaid | MI355X | spend $56,438

GPUs: 2.20 (about 2). Monthly cost: $4,167. Cash at risk: $56,438. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $5,570 | $1,403 | $8,606 | $56,438 | $23,581 | $75,443 | $19,005 | $42,586 |
| 40% | 6.92 | $11,139 | $6,973 | $17,213 | $56,438 | $19,338 | $150,886 | $94,447 | $113,786 |
| 70% | 12.12 | $19,494 | $15,327 | $30,122 | $56,438 | $12,974 | $264,050 | $207,612 | $220,586 |

### 1. Month-to-month, inference | MI355X | spend $100,000

GPUs: 4.41 (about 4). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $11,139 | $2,806 | $11,353 | $8,493 | $0 | $133,673 | $33,673 | $33,673 |
| 40% | 6.92 | $22,279 | $13,946 | $22,706 | $8,493 | $0 | $267,346 | $167,346 | $167,346 |
| 70% | 12.12 | $38,988 | $30,655 | $39,736 | $8,493 | $0 | $467,856 | $367,856 | $367,856 |

### 2a. 3-month prepaid, inference | MI355X | spend $100,000

GPUs: 4.64 (about 5). Monthly cost: $8,333. Cash at risk: $25,000. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $11,728 | $3,395 | $11,953 | $25,000 | $6,432 | $140,737 | $40,737 | $47,169 |
| 40% | 6.92 | $23,456 | $15,123 | $23,906 | $25,000 | $539 | $281,474 | $181,474 | $182,014 |
| 70% | 12.12 | $41,048 | $32,715 | $41,836 | $25,000 | $0 | $492,580 | $392,580 | $392,580 |

### 2b. 12-month prepaid, inference | MI355X | spend $100,000

GPUs: 4.41 (about 4). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $11,139 | $2,806 | $11,353 | $100,000 | $43,703 | $133,673 | $33,673 | $77,376 |
| 40% | 6.92 | $22,279 | $13,946 | $22,706 | $100,000 | $38,106 | $267,346 | $167,346 | $205,452 |
| 70% | 12.12 | $38,988 | $30,655 | $39,736 | $100,000 | $29,710 | $467,856 | $367,856 | $397,566 |

### 6a. Staged: test month-to-month, then 3-month prepaid | MI355X | spend $113,557

GPUs: 4.64 (about 5). Monthly cost: $8,333. Cash at risk: $38,557. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $11,728 | $3,395 | $18,122 | $38,557 | $10,074 | $158,859 | $45,302 | $55,377 |
| 40% | 6.92 | $23,456 | $15,123 | $36,245 | $38,557 | $1,140 | $317,719 | $204,162 | $205,302 |
| 70% | 12.12 | $41,048 | $32,715 | $63,428 | $38,557 | $0 | $556,008 | $442,451 | $442,451 |

### 6b. Staged: test month-to-month, then 12-month prepaid | MI355X | spend $112,877

GPUs: 4.41 (about 4). Monthly cost: $8,333. Cash at risk: $112,877. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $11,139 | $2,806 | $17,213 | $112,877 | $47,162 | $150,886 | $38,009 | $85,171 |
| 40% | 6.92 | $22,279 | $13,946 | $34,425 | $112,877 | $38,676 | $301,772 | $188,895 | $227,571 |
| 70% | 12.12 | $38,988 | $30,655 | $60,244 | $112,877 | $25,948 | $528,100 | $415,224 | $441,171 |

### 1. Month-to-month, inference | MI355X | spend $250,000

GPUs: 11.02 (about 11). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $27,849 | $7,015 | $28,383 | $21,233 | $0 | $334,183 | $84,183 | $84,183 |
| 40% | 6.92 | $55,697 | $34,864 | $56,765 | $21,233 | $0 | $668,366 | $418,366 | $418,366 |
| 70% | 12.12 | $97,470 | $76,637 | $99,339 | $21,233 | $0 | $1,169,640 | $919,640 | $919,640 |

### 2a. 3-month prepaid, inference | MI355X | spend $250,000

GPUs: 11.60 (about 12). Monthly cost: $20,833. Cash at risk: $62,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $29,320 | $8,487 | $29,883 | $62,500 | $16,080 | $351,843 | $101,843 | $117,923 |
| 40% | 6.92 | $58,640 | $37,807 | $59,765 | $62,500 | $1,348 | $703,686 | $453,686 | $455,034 |
| 70% | 12.12 | $102,621 | $81,788 | $104,589 | $62,500 | $0 | $1,231,450 | $981,450 | $981,450 |

### 2b. 12-month prepaid, inference | MI355X | spend $250,000

GPUs: 11.02 (about 11). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $27,849 | $7,015 | $28,383 | $250,000 | $109,257 | $334,183 | $84,183 | $193,440 |
| 40% | 6.92 | $55,697 | $34,864 | $56,765 | $250,000 | $95,265 | $668,366 | $418,366 | $513,630 |
| 70% | 12.12 | $97,470 | $76,637 | $99,339 | $250,000 | $74,276 | $1,169,640 | $919,640 | $993,916 |

### 6a. Staged: test month-to-month, then 3-month prepaid | MI355X | spend $283,893

GPUs: 11.60 (about 12). Monthly cost: $20,833. Cash at risk: $96,393. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $29,320 | $8,487 | $45,306 | $96,393 | $25,186 | $397,149 | $113,256 | $138,442 |
| 40% | 6.92 | $58,640 | $37,807 | $90,612 | $96,393 | $2,850 | $794,297 | $510,404 | $513,255 |
| 70% | 12.12 | $102,621 | $81,788 | $158,570 | $96,393 | $0 | $1,390,021 | $1,106,128 | $1,106,128 |

### 6b. Staged: test month-to-month, then 12-month prepaid | MI355X | spend $282,192

GPUs: 11.02 (about 11). Monthly cost: $20,833. Cash at risk: $282,192. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 3.46 | $27,849 | $7,015 | $43,032 | $282,192 | $117,906 | $377,215 | $95,023 | $212,929 |
| 40% | 6.92 | $55,697 | $34,864 | $86,064 | $282,192 | $96,691 | $754,429 | $472,237 | $568,929 |
| 70% | 12.12 | $97,470 | $76,637 | $150,611 | $282,192 | $64,869 | $1,320,251 | $1,038,059 | $1,102,929 |

### 1. Month-to-month, inference | MI300X | spend $50,000

GPUs: 3.09 (about 3). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $693 | $-3,474 | $706 | $4,247 | $1,746 | $8,311 | $-41,689 | $-39,943 |
| 40% | 0.62 | $1,385 | $-2,781 | $1,412 | $4,247 | $1,398 | $16,623 | $-33,377 | $-31,980 |
| 70% | 1.08 | $2,424 | $-1,743 | $2,471 | $4,247 | $876 | $29,090 | $-20,910 | $-20,035 |

### 2a. 3-month prepaid, inference | MI300X | spend $50,000

GPUs: 3.24 (about 3). Monthly cost: $4,167. Cash at risk: $12,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $728 | $-3,439 | $742 | $12,500 | $5,797 | $8,736 | $-41,264 | $-35,467 |
| 40% | 0.62 | $1,456 | $-2,711 | $1,484 | $12,500 | $5,431 | $17,473 | $-32,527 | $-27,096 |
| 70% | 1.08 | $2,548 | $-1,619 | $2,597 | $12,500 | $4,882 | $30,577 | $-19,423 | $-14,541 |

### 2b. 12-month prepaid, inference | MI300X | spend $50,000

GPUs: 3.26 (about 3). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $732 | $-3,434 | $746 | $50,000 | $24,282 | $8,786 | $-41,214 | $-16,932 |
| 40% | 0.62 | $1,464 | $-2,702 | $1,492 | $50,000 | $23,914 | $17,573 | $-32,427 | $-8,513 |
| 70% | 1.08 | $2,563 | $-1,604 | $2,612 | $50,000 | $23,362 | $30,752 | $-19,248 | $4,114 |

### 6a. Staged: test month-to-month, then 3-month prepaid | MI300X | spend $59,475

GPUs: 3.24 (about 3). Monthly cost: $4,167. Cash at risk: $21,975. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $728 | $-3,439 | $1,125 | $21,975 | $10,279 | $9,861 | $-49,613 | $-39,334 |
| 40% | 0.62 | $1,456 | $-2,711 | $2,250 | $21,975 | $9,724 | $19,723 | $-39,752 | $-30,028 |
| 70% | 1.08 | $2,548 | $-1,619 | $3,937 | $21,975 | $8,892 | $34,515 | $-24,960 | $-16,068 |

### 6b. Staged: test month-to-month, then 12-month prepaid | MI300X | spend $59,529

GPUs: 3.26 (about 3). Monthly cost: $4,167. Cash at risk: $59,529. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $732 | $-3,434 | $1,131 | $59,529 | $28,790 | $9,918 | $-49,611 | $-20,821 |
| 40% | 0.62 | $1,464 | $-2,702 | $2,263 | $59,529 | $28,232 | $19,835 | $-39,693 | $-11,461 |
| 70% | 1.08 | $2,563 | $-1,604 | $3,960 | $59,529 | $27,395 | $34,712 | $-24,817 | $2,578 |

### 1. Month-to-month, inference | MI300X | spend $100,000

GPUs: 6.17 (about 6). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $1,385 | $-6,948 | $1,412 | $8,493 | $3,491 | $16,623 | $-83,377 | $-79,886 |
| 40% | 0.62 | $2,770 | $-5,563 | $2,824 | $8,493 | $2,795 | $33,245 | $-66,755 | $-63,960 |
| 70% | 1.08 | $4,848 | $-3,485 | $4,941 | $8,493 | $1,751 | $58,179 | $-41,821 | $-40,070 |

### 2a. 3-month prepaid, inference | MI300X | spend $100,000

GPUs: 6.49 (about 6). Monthly cost: $8,333. Cash at risk: $25,000. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $1,456 | $-6,877 | $1,484 | $25,000 | $11,593 | $17,473 | $-82,527 | $-70,934 |
| 40% | 0.62 | $2,912 | $-5,421 | $2,968 | $25,000 | $10,862 | $34,945 | $-65,055 | $-54,193 |
| 70% | 1.08 | $5,096 | $-3,237 | $5,194 | $25,000 | $9,764 | $61,154 | $-38,846 | $-29,081 |

### 2b. 12-month prepaid, inference | MI300X | spend $100,000

GPUs: 6.52 (about 7). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $1,464 | $-6,869 | $1,492 | $100,000 | $48,564 | $17,573 | $-82,427 | $-33,863 |
| 40% | 0.62 | $2,929 | $-5,405 | $2,985 | $100,000 | $47,828 | $35,145 | $-64,855 | $-17,027 |
| 70% | 1.08 | $5,125 | $-3,208 | $5,224 | $100,000 | $46,725 | $61,504 | $-38,496 | $8,229 |

### 6a. Staged: test month-to-month, then 3-month prepaid | MI300X | spend $118,949

GPUs: 6.49 (about 6). Monthly cost: $8,333. Cash at risk: $43,949. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $1,456 | $-6,877 | $2,250 | $43,949 | $20,558 | $19,723 | $-99,227 | $-78,669 |
| 40% | 0.62 | $2,912 | $-5,421 | $4,500 | $43,949 | $19,449 | $39,445 | $-79,504 | $-60,055 |
| 70% | 1.08 | $5,096 | $-3,237 | $7,875 | $43,949 | $17,785 | $69,029 | $-49,920 | $-32,135 |

### 6b. Staged: test month-to-month, then 12-month prepaid | MI300X | spend $119,058

GPUs: 6.52 (about 7). Monthly cost: $8,333. Cash at risk: $119,058. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $1,464 | $-6,869 | $2,263 | $119,058 | $57,580 | $19,835 | $-99,222 | $-41,642 |
| 40% | 0.62 | $2,929 | $-5,405 | $4,526 | $119,058 | $56,464 | $39,671 | $-79,387 | $-22,923 |
| 70% | 1.08 | $5,125 | $-3,208 | $7,920 | $119,058 | $54,791 | $69,424 | $-49,634 | $5,157 |

### 1. Month-to-month, inference | MI300X | spend $250,000

GPUs: 15.43 (about 15). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $3,463 | $-17,370 | $3,529 | $21,233 | $8,728 | $41,557 | $-208,443 | $-199,716 |
| 40% | 0.62 | $6,926 | $-13,907 | $7,059 | $21,233 | $6,988 | $83,113 | $-166,887 | $-159,899 |
| 70% | 1.08 | $12,121 | $-8,713 | $12,353 | $21,233 | $4,378 | $145,448 | $-104,552 | $-100,174 |

### 2a. 3-month prepaid, inference | MI300X | spend $250,000

GPUs: 16.22 (about 16). Monthly cost: $20,833. Cash at risk: $62,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $3,640 | $-17,193 | $3,710 | $62,500 | $28,983 | $43,682 | $-206,318 | $-177,335 |
| 40% | 0.62 | $7,280 | $-13,553 | $7,420 | $62,500 | $27,154 | $87,363 | $-162,637 | $-135,482 |
| 70% | 1.08 | $12,741 | $-8,093 | $12,985 | $62,500 | $24,411 | $152,886 | $-97,114 | $-72,703 |

### 2b. 12-month prepaid, inference | MI300X | spend $250,000

GPUs: 16.31 (about 16). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $3,661 | $-17,172 | $3,731 | $250,000 | $121,411 | $43,931 | $-206,069 | $-84,658 |
| 40% | 0.62 | $7,322 | $-13,511 | $7,462 | $250,000 | $119,571 | $87,863 | $-162,137 | $-42,566 |
| 70% | 1.08 | $12,813 | $-8,020 | $13,059 | $250,000 | $116,812 | $153,760 | $-96,240 | $20,572 |

### 6a. Staged: test month-to-month, then 3-month prepaid | MI300X | spend $297,373

GPUs: 16.22 (about 16). Monthly cost: $20,833. Cash at risk: $109,873. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $3,640 | $-17,193 | $5,625 | $109,873 | $51,394 | $49,306 | $-248,067 | $-196,672 |
| 40% | 0.62 | $7,280 | $-13,553 | $11,250 | $109,873 | $48,621 | $98,613 | $-198,760 | $-150,139 |
| 70% | 1.08 | $12,741 | $-8,093 | $19,687 | $109,873 | $44,462 | $172,573 | $-124,800 | $-80,339 |

### 6b. Staged: test month-to-month, then 12-month prepaid | MI300X | spend $297,644

GPUs: 16.31 (about 16). Monthly cost: $20,833. Cash at risk: $297,644. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.31 | $3,661 | $-17,172 | $5,657 | $297,644 | $130,634 | $49,588 | $-248,056 | $-117,421 |
| 40% | 0.62 | $7,322 | $-13,511 | $11,314 | $297,644 | $129,939 | $99,176 | $-198,467 | $-68,529 |
| 70% | 1.08 | $12,813 | $-8,020 | $19,799 | $297,644 | $128,895 | $173,559 | $-124,085 | $4,810 |

### 1. Month-to-month, inference | RTXPRO6000 | spend $50,000

GPUs: 2.59 (about 3). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $493 | $-3,674 | $502 | $4,247 | $1,846 | $5,914 | $-44,086 | $-42,240 |
| 40% | 0.52 | $986 | $-3,181 | $1,005 | $4,247 | $1,598 | $11,828 | $-38,172 | $-36,574 |
| 70% | 0.91 | $1,725 | $-2,442 | $1,758 | $4,247 | $1,227 | $20,699 | $-29,301 | $-28,074 |

### 2a. 3-month prepaid, inference | RTXPRO6000 | spend $50,000

GPUs: 2.73 (about 3). Monthly cost: $4,167. Cash at risk: $12,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $519 | $-3,648 | $529 | $12,500 | $5,902 | $6,225 | $-43,775 | $-37,873 |
| 40% | 0.52 | $1,038 | $-3,129 | $1,057 | $12,500 | $5,641 | $12,450 | $-37,550 | $-31,908 |
| 70% | 0.91 | $1,816 | $-2,351 | $1,850 | $12,500 | $5,250 | $21,788 | $-28,212 | $-22,962 |

### 2b. 12-month prepaid, inference | RTXPRO6000 | spend $50,000

GPUs: 2.59 (about 3). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $493 | $-3,674 | $502 | $50,000 | $24,402 | $5,914 | $-44,086 | $-19,684 |
| 40% | 0.52 | $986 | $-3,181 | $1,005 | $50,000 | $24,155 | $11,828 | $-38,172 | $-14,017 |
| 70% | 0.91 | $1,725 | $-2,442 | $1,758 | $50,000 | $23,783 | $20,699 | $-29,301 | $-5,518 |

### 3a. Month-to-month, resell on Vast | RTXPRO6000 | spend $50,000

GPUs: 2.59 (about 3). Monthly cost: $4,167. Cash at risk: $4,167. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $485 | $-3,682 | $494 | $4,247 | $1,850 | $5,818 | $-44,182 | $-42,332 |
| 40% | 0.51 | $970 | $-3,197 | $988 | $4,247 | $1,606 | $11,636 | $-38,364 | $-36,757 |
| 70% | 0.90 | $1,697 | $-2,470 | $1,730 | $4,247 | $1,241 | $20,364 | $-29,636 | $-28,395 |

### 3b. 12-month prepaid, resell on Vast | RTXPRO6000 | spend $50,000

GPUs: 2.59 (about 3). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $485 | $-3,682 | $494 | $50,000 | $24,406 | $5,818 | $-44,182 | $-19,775 |
| 40% | 0.51 | $970 | $-3,197 | $988 | $50,000 | $24,163 | $11,636 | $-38,364 | $-14,201 |
| 70% | 0.90 | $1,697 | $-2,470 | $1,730 | $50,000 | $23,797 | $20,364 | $-29,636 | $-5,839 |

### 4. Own used servers in colocation | RTXPRO6000 | spend $50,000

GPUs: 2.35 (about 2). Monthly cost: $414. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $446 | $32 | $455 | $50,422 | $21,713 | $5,353 | $-49,616 | $-27,903 |
| 40% | 0.52 | $892 | $478 | $909 | $50,422 | $21,489 | $10,706 | $-44,263 | $-22,775 |
| 70% | 0.91 | $1,561 | $1,147 | $1,591 | $50,422 | $21,152 | $18,735 | $-36,234 | $-15,082 |

### 4b. Own servers in colocation, resell time on Vast | RTXPRO6000 | spend $50,000

GPUs: 2.35 (about 2). Monthly cost: $414. Cash at risk: $50,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $439 | $25 | $447 | $50,422 | $21,716 | $5,266 | $-49,703 | $-27,986 |
| 40% | 0.51 | $878 | $464 | $895 | $50,422 | $21,496 | $10,532 | $-44,437 | $-22,941 |
| 70% | 0.90 | $1,536 | $1,122 | $1,565 | $50,422 | $21,165 | $18,432 | $-36,537 | $-15,372 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | RTXPRO6000 | spend $50,000

GPUs: 2.59 (about 3). Monthly cost: $4,167. Cash at risk: $50,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.77 | $1,463 | $-2,704 | $1,491 | $50,000 | $23,915 | $17,550 | $-32,450 | $-8,535 |
| 40% | 0.90 | $1,713 | $-2,454 | $1,746 | $50,000 | $23,789 | $20,555 | $-29,445 | $-5,656 |
| 70% | 1.10 | $2,089 | $-2,078 | $2,129 | $50,000 | $23,601 | $25,062 | $-24,938 | $-1,337 |

### 6a. Staged: test month-to-month, then 3-month prepaid | RTXPRO6000 | spend $56,777

GPUs: 2.73 (about 3). Monthly cost: $4,167. Cash at risk: $19,277. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $519 | $-3,648 | $802 | $19,277 | $9,108 | $7,027 | $-49,750 | $-40,642 |
| 40% | 0.52 | $1,038 | $-3,129 | $1,603 | $19,277 | $8,713 | $14,054 | $-42,724 | $-34,010 |
| 70% | 0.91 | $1,816 | $-2,351 | $2,806 | $19,277 | $8,121 | $24,594 | $-32,184 | $-24,063 |

### 6b. Staged: test month-to-month, then 12-month prepaid | RTXPRO6000 | spend $56,438

GPUs: 2.59 (about 3). Monthly cost: $4,167. Cash at risk: $56,438. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $493 | $-3,674 | $762 | $56,438 | $27,449 | $6,675 | $-49,763 | $-22,314 |
| 40% | 0.52 | $986 | $-3,181 | $1,523 | $56,438 | $27,073 | $13,351 | $-43,088 | $-16,014 |
| 70% | 0.91 | $1,725 | $-2,442 | $2,665 | $56,438 | $26,510 | $23,364 | $-33,074 | $-6,564 |

### 1. Month-to-month, inference | RTXPRO6000 | spend $100,000

GPUs: 5.19 (about 5). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $986 | $-7,348 | $1,005 | $8,493 | $3,692 | $11,828 | $-88,172 | $-84,480 |
| 40% | 0.52 | $1,971 | $-6,362 | $2,009 | $8,493 | $3,197 | $23,656 | $-76,344 | $-73,148 |
| 70% | 0.91 | $3,450 | $-4,884 | $3,516 | $8,493 | $2,454 | $41,397 | $-58,603 | $-56,149 |

### 2a. 3-month prepaid, inference | RTXPRO6000 | spend $100,000

GPUs: 5.46 (about 5). Monthly cost: $8,333. Cash at risk: $25,000. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $1,038 | $-7,296 | $1,057 | $25,000 | $11,804 | $12,450 | $-87,550 | $-75,746 |
| 40% | 0.52 | $2,075 | $-6,258 | $2,115 | $25,000 | $11,282 | $24,901 | $-75,099 | $-63,817 |
| 70% | 0.91 | $3,631 | $-4,702 | $3,701 | $25,000 | $10,500 | $43,576 | $-56,424 | $-45,923 |

### 2b. 12-month prepaid, inference | RTXPRO6000 | spend $100,000

GPUs: 5.19 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $986 | $-7,348 | $1,005 | $100,000 | $48,805 | $11,828 | $-88,172 | $-39,367 |
| 40% | 0.52 | $1,971 | $-6,362 | $2,009 | $100,000 | $48,310 | $23,656 | $-76,344 | $-28,035 |
| 70% | 0.91 | $3,450 | $-4,884 | $3,516 | $100,000 | $47,567 | $41,397 | $-58,603 | $-11,036 |

### 3a. Month-to-month, resell on Vast | RTXPRO6000 | spend $100,000

GPUs: 5.19 (about 5). Monthly cost: $8,333. Cash at risk: $8,333. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $970 | $-7,364 | $988 | $8,493 | $3,700 | $11,636 | $-88,364 | $-84,664 |
| 40% | 0.51 | $1,939 | $-6,394 | $1,977 | $8,493 | $3,213 | $23,273 | $-76,727 | $-73,515 |
| 70% | 0.90 | $3,394 | $-4,939 | $3,459 | $8,493 | $2,482 | $40,727 | $-59,273 | $-56,791 |

### 3b. 12-month prepaid, resell on Vast | RTXPRO6000 | spend $100,000

GPUs: 5.19 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $970 | $-7,364 | $988 | $100,000 | $48,813 | $11,636 | $-88,364 | $-39,551 |
| 40% | 0.51 | $1,939 | $-6,394 | $1,977 | $100,000 | $48,326 | $23,273 | $-76,727 | $-28,402 |
| 70% | 0.90 | $3,394 | $-4,939 | $3,459 | $100,000 | $47,595 | $40,727 | $-59,273 | $-11,678 |

### 4. Own used servers in colocation | RTXPRO6000 | spend $100,000

GPUs: 4.70 (about 5). Monthly cost: $828. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $892 | $64 | $909 | $100,844 | $40,504 | $10,706 | $-99,232 | $-58,728 |
| 40% | 0.52 | $1,784 | $956 | $1,818 | $100,844 | $40,056 | $21,411 | $-88,527 | $-48,471 |
| 70% | 0.91 | $3,122 | $2,294 | $3,182 | $100,844 | $39,383 | $37,470 | $-72,468 | $-33,085 |

### 4b. Own servers in colocation, resell time on Vast | RTXPRO6000 | spend $100,000

GPUs: 4.70 (about 5). Monthly cost: $828. Cash at risk: $100,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $878 | $50 | $895 | $100,844 | $40,511 | $10,532 | $-99,405 | $-58,894 |
| 40% | 0.51 | $1,755 | $927 | $1,789 | $100,844 | $40,070 | $21,065 | $-88,873 | $-48,803 |
| 70% | 0.90 | $3,072 | $2,244 | $3,131 | $100,844 | $39,409 | $36,863 | $-73,075 | $-33,666 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | RTXPRO6000 | spend $100,000

GPUs: 5.19 (about 5). Monthly cost: $8,333. Cash at risk: $100,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.77 | $2,925 | $-5,408 | $2,981 | $100,000 | $47,830 | $35,101 | $-64,899 | $-17,069 |
| 40% | 0.90 | $3,426 | $-4,907 | $3,492 | $100,000 | $47,579 | $41,110 | $-58,890 | $-11,311 |
| 70% | 1.10 | $4,177 | $-4,156 | $4,257 | $100,000 | $47,201 | $50,125 | $-49,875 | $-2,674 |

### 6a. Staged: test month-to-month, then 3-month prepaid | RTXPRO6000 | spend $113,554

GPUs: 5.46 (about 5). Monthly cost: $8,333. Cash at risk: $38,554. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $1,038 | $-7,296 | $1,603 | $38,554 | $18,217 | $14,054 | $-99,501 | $-81,284 |
| 40% | 0.52 | $2,075 | $-6,258 | $3,206 | $38,554 | $17,427 | $28,107 | $-85,447 | $-68,021 |
| 70% | 0.91 | $3,631 | $-4,702 | $5,611 | $38,554 | $16,241 | $49,187 | $-64,367 | $-48,126 |

### 6b. Staged: test month-to-month, then 12-month prepaid | RTXPRO6000 | spend $112,877

GPUs: 5.19 (about 5). Monthly cost: $8,333. Cash at risk: $112,877. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $986 | $-7,348 | $1,523 | $112,877 | $54,897 | $13,351 | $-99,526 | $-44,629 |
| 40% | 0.52 | $1,971 | $-6,362 | $3,046 | $112,877 | $54,147 | $26,702 | $-86,175 | $-32,029 |
| 70% | 0.91 | $3,450 | $-4,884 | $5,331 | $112,877 | $53,020 | $46,728 | $-66,149 | $-13,129 |

### 1. Month-to-month, inference | RTXPRO6000 | spend $250,000

GPUs: 12.97 (about 13). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,464 | $-18,369 | $2,511 | $21,233 | $9,230 | $29,570 | $-220,430 | $-211,201 |
| 40% | 0.52 | $4,928 | $-15,905 | $5,023 | $21,233 | $7,992 | $59,139 | $-190,861 | $-182,869 |
| 70% | 0.91 | $8,624 | $-12,209 | $8,790 | $21,233 | $6,134 | $103,493 | $-146,507 | $-140,372 |

### 2a. 3-month prepaid, inference | RTXPRO6000 | spend $250,000

GPUs: 13.65 (about 14). Monthly cost: $20,833. Cash at risk: $62,500. Lock-in: 3 months at a time. Exit: Walk away at the end of a 3-month term.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,594 | $-18,240 | $2,644 | $62,500 | $29,509 | $31,126 | $-218,874 | $-189,365 |
| 40% | 0.52 | $5,188 | $-15,646 | $5,287 | $62,500 | $28,206 | $62,252 | $-187,748 | $-159,542 |
| 70% | 0.91 | $9,078 | $-11,755 | $9,252 | $62,500 | $26,251 | $108,940 | $-141,060 | $-114,809 |

### 2b. 12-month prepaid, inference | RTXPRO6000 | spend $250,000

GPUs: 12.97 (about 13). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell unused reserved time (SF Compute style market) or sublease if the provider allows; otherwise no exit.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,464 | $-18,369 | $2,511 | $250,000 | $122,012 | $29,570 | $-220,430 | $-98,419 |
| 40% | 0.52 | $4,928 | $-15,905 | $5,023 | $250,000 | $120,774 | $59,139 | $-190,861 | $-70,087 |
| 70% | 0.91 | $8,624 | $-12,209 | $8,790 | $250,000 | $118,917 | $103,493 | $-146,507 | $-27,590 |

### 3a. Month-to-month, resell on Vast | RTXPRO6000 | spend $250,000

GPUs: 12.97 (about 13). Monthly cost: $20,833. Cash at risk: $20,833. Lock-in: None. Exit: Cancel at the end of any month.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,424 | $-18,409 | $2,471 | $21,233 | $9,250 | $29,091 | $-220,909 | $-211,659 |
| 40% | 0.51 | $4,848 | $-15,985 | $4,941 | $21,233 | $8,032 | $58,182 | $-191,818 | $-183,787 |
| 70% | 0.90 | $8,485 | $-12,348 | $8,648 | $21,233 | $6,205 | $101,818 | $-148,182 | $-141,977 |

### 3b. 12-month prepaid, resell on Vast | RTXPRO6000 | spend $250,000

GPUs: 12.97 (about 13). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time or ride it out.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,424 | $-18,409 | $2,471 | $250,000 | $122,032 | $29,091 | $-220,909 | $-98,877 |
| 40% | 0.51 | $4,848 | $-15,985 | $4,941 | $250,000 | $120,814 | $58,182 | $-191,818 | $-71,004 |
| 70% | 0.90 | $8,485 | $-12,348 | $8,648 | $250,000 | $118,987 | $101,818 | $-148,182 | $-29,195 |

### 4. Own used servers in colocation | RTXPRO6000 | spend $250,000

GPUs: 11.74 (about 12). Monthly cost: $2,070. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,230 | $160 | $2,273 | $252,110 | $93,957 | $26,764 | $-248,080 | $-154,123 |
| 40% | 0.52 | $4,461 | $2,390 | $4,546 | $252,110 | $92,836 | $53,528 | $-221,316 | $-128,480 |
| 70% | 0.91 | $7,806 | $5,736 | $7,956 | $252,110 | $91,156 | $93,674 | $-181,170 | $-90,015 |

### 4b. Own servers in colocation, resell time on Vast | RTXPRO6000 | spend $250,000

GPUs: 11.74 (about 12). Monthly cost: $2,070. Cash at risk: $250,000. Lock-in: Capital is sunk; resale value falls every quarter. Exit: Sell used hardware on the secondary market (weeks to months); cancel colo per contract.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,194 | $124 | $2,236 | $252,110 | $93,975 | $26,331 | $-248,514 | $-154,538 |
| 40% | 0.51 | $4,388 | $2,318 | $4,473 | $252,110 | $92,873 | $52,662 | $-222,183 | $-129,310 |
| 70% | 0.90 | $7,680 | $5,609 | $7,827 | $252,110 | $91,219 | $92,158 | $-182,687 | $-91,468 |

### 5. Hybrid: 12-month prepaid, inference + Vast on idle hours | RTXPRO6000 | spend $250,000

GPUs: 12.97 (about 13). Monthly cost: $20,833. Cash at risk: $250,000. Lock-in: 12 months, non-refundable. Exit: Resell reserved time; Vast listing can stop any time.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.77 | $7,313 | $-13,521 | $7,453 | $250,000 | $119,576 | $87,751 | $-162,249 | $-42,673 |
| 40% | 0.90 | $8,565 | $-12,269 | $8,729 | $250,000 | $118,947 | $102,775 | $-147,225 | $-28,278 |
| 70% | 1.10 | $10,443 | $-10,391 | $10,643 | $250,000 | $118,003 | $125,312 | $-124,688 | $-6,685 |

### 6a. Staged: test month-to-month, then 3-month prepaid | RTXPRO6000 | spend $283,886

GPUs: 13.65 (about 14). Monthly cost: $20,833. Cash at risk: $96,386. Lock-in: None during the test; then 3 months. Exit: Stop after the test if it fails (lose only the test weeks). After prepaying, walk away at term end.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,594 | $-18,240 | $4,008 | $96,386 | $45,542 | $35,134 | $-248,752 | $-203,210 |
| 40% | 0.52 | $5,188 | $-15,646 | $8,016 | $96,386 | $43,566 | $70,268 | $-213,618 | $-170,052 |
| 70% | 0.91 | $9,078 | $-11,755 | $14,028 | $96,386 | $40,603 | $122,968 | $-160,918 | $-120,315 |

### 6b. Staged: test month-to-month, then 12-month prepaid | RTXPRO6000 | spend $282,192

GPUs: 12.97 (about 13). Monthly cost: $20,833. Cash at risk: $282,192. Lock-in: None during the test; then 12 months. Exit: Stop after the test if it fails. After a 12-month prepay, resell unused time if the provider allows.

| Util | Rev/GPU-hr | Rev/month | Profit/month | Rev 2026 | Deductible 2026 | Tax saved 2026 | Rev 12 mo | Pre-tax 12 mo | After-tax 12 mo |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20% | 0.26 | $2,464 | $-18,369 | $3,808 | $282,192 | $128,961 | $33,377 | $-248,815 | $-119,853 |
| 40% | 0.52 | $4,928 | $-15,905 | $7,615 | $282,192 | $128,493 | $66,754 | $-215,438 | $-86,945 |
| 70% | 0.91 | $8,624 | $-12,209 | $13,327 | $282,192 | $127,790 | $116,820 | $-165,372 | $-37,581 |
