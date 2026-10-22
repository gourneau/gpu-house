## Summary table across models

Sources: https://openrouter.ai/api/v1/models and https://openrouter.ai/api/v1/models/{author}/{slug}/endpoints for prices, counts, context; https://openrouter.ai/rankings and https://openrouter.ai/models?order=top-weekly for weekly tokens and rank. All checked 2026-10-22. Prices in USD per million tokens. Min and median are computed over distinct providers, using each provider's cheapest endpoint. Endpoints priced at $0 are ignored. 'Price to beat' is the current minimum minus 5 percent.

| Model | Providers | Endpoints | Context | Min in | Median in | Min out | Median out | Max out | Cheapest provider(s) | Price to beat (in / out) | Weekly tokens | Weekly rank | Tokens per provider |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepseek/deepseek-v4.1-flash | 30 | 38 | 1048576 | 0.07 | 0.2025 | 0.18 | 0.81 | 1.2 | Decart | 0.0665 / 0.171 | 27.5T | 1 | 917B |
| deepseek/deepseek-v4.1-flash-1017 | 26 | 30 | 1048576 | 0.07 | 0.2075 | 0.15 | 0.69 | 1.2 | Sail Research | 0.0665 / 0.1425 | 20T | 2 | 769B |
| z-ai/glm-5.3-flash | 30 | 34 | 1048576 | 0.0052 | 0.15 | 0.145 | 0.5 | 1.6 | StreamLake | 0.0049 / 0.1377 | 12.4T | 3 | 413B |
| tencent/hy4-preview | 4 | 4 | 1048576 | 0.834 | 0.834 | 2.501 | 2.501 | 2.501 | DeepInfra, Novita, SiliconFlow, Tencent | 0.7923 / 2.3759 | 9.7T | 6 | 2.42T |
| xiaomi/mimo-v2.6-flash | 9 | 9 | 1050000 | 0.1 | 0.14 | 0.266 | 0.28 | 0.35 | DeepInfra | 0.095 / 0.2527 | 9.12T | 5 | 1.01T |
| z-ai/glm-5.3 | 37 | 48 | 1048576 | 0.079 | 0.98 | 1.4 | 4.2 | 6.6 | Wafer | 0.075 / 1.33 | 5.73T | 9 | 155B |
| deepseek/deepseek-v4-flash-0731 | 23 | 26 | 1048576 | 0.0422 | 0.14 | 0.1333 | 0.28 | 1.32 | Baidu | 0.0401 / 0.1267 | 4.63T | 11 | 201B |
| tencent/hy3 | 5 | 5 | 262144 | 0.132 | 0.14 | 0.528 | 0.58 | 0.8 | Tencent | 0.1254 / 0.5016 | 3.49T | 13 | 698B |
| meta/muse-spark-1.3-contributor | 1 | 1 | 1048576 | 0.1 | 0.1 | 0.2 | 0.2 | 0.2 | Meta | 0.095 / 0.19 | 3.41T | 12 | 3.41T |
| deepseek/deepseek-v4-flash | 15 | 15 | 1048576 | 0.05 | 0.13 | 0.14 | 0.28 | 1.32 | StreamLake | 0.0475 / 0.133 | 3.02T | 15 | 201B |
| stepfun/step-5-preview | 4 | 5 | 1048576 | 1 | 1 | 2.7 | 2.7 | 2.7 | DeepInfra, Featherless, InferenceNet, StepFun | 0.95 / 2.565 | 2.96T | 17 | 740B |
| moonshotai/kimi-k3 | 20 | 28 | 1048576 | 0.239 | 2.325 | 5.5 | 14.125 | 17.25 | Sail Research | 0.2271 / 5.225 | 1.96T | 20 | 98B |
| xiaomi/mimo-v2.6-pro | 5 | 5 | 1050000 | 0.387 | 0.435 | 0.783 | 0.87 | 1.044 | DeepInfra | 0.3676 / 0.7438 | 1.73T | >20 | 346B |
| minimax/minimax-m3 | 13 | 14 | 1048576 | 0.224 | 0.3 | 0.88 | 1.2 | 2.4 | DeepInfra | 0.2128 / 0.836 | 1.47T | >20 | 113B |
| deepseek/deepseek-v4-pro-0813 | 21 | 23 | 1048576 | 0.1461 | 0.99 | 0.4871 | 3.8 | 8 | Baidu | 0.1388 / 0.4627 | 1.09T | >20 | 51.9B |
| qwen/qwen3.6-35b-a3b | 10 | 10 | 262144 | 0.05 | 0.1 | 0.7 | 1 | 1.8 | Darkbloom | 0.0475 / 0.665 | 785B | >20 | 78.5B |
| qwen/qwen3.8-flash | 1 | 2 | 1000000 | 0.15 | 0.15 | 0.47 | 0.47 | 0.47 | Alibaba | 0.1425 / 0.4465 | 717B | >20 | 717B |
| deepseek/deepseek-v4-pro | 15 | 16 | 1048576 | 0.4411 | 1.15 | 0.8822 | 2.6 | 3.83 | Baidu | 0.419 / 0.8381 | 685B | >20 | 45.7B |
| google/gemma-4-31b-it | 12 | 15 | 262144 | 0.1 | 0.145 | 0.32 | 0.4 | 1.15 | DeepInfra | 0.095 / 0.304 | 613B | >20 | 51.1B |
| openai/gpt-oss-120b | 22 | 24 | 131072 | 0.03 | 0.095 | 0.15 | 0.46 | 0.95 | Near AI, Venice | 0.0285 / 0.1425 | 568B | >20 | 25.8B |
| qwen/qwen3.8-27b | 20 | 20 | 1000000 | 0.035 | 0.2 | 1.25 | 2.3 | 3.2 | Chutes | 0.0333 / 1.1875 | 485B | >20 | 24.2B |
| deepseek/deepseek-v3.2 | 12 | 12 | 163840 | 0.07 | 0.2841 | 0.105 | 0.88 | 4.5 | Baidu | 0.0665 / 0.0997 | 303B | >20 | 25.2B |
| openai/gpt-oss-20b | 10 | 11 | 131072 | 0.018 | 0.03 | 0.09 | 0.145 | 0.3 | Darkbloom | 0.0171 / 0.0855 | 217B | >20 | 21.7B |
| z-ai/glm-5.3-flashx | 1 | 1 | 1048576 | 0.37 | 0.37 | 1.25 | 1.25 | 1.25 | Z.AI | 0.3515 / 1.1875 | 158B | >20 | 158B |
| moonshotai/kimi-k2.6 | 17 | 17 | 262144 | 0.4493 | 0.75 | 1.892 | 3.5 | 4.6 | Baidu | 0.4269 / 1.7974 | 144B | >20 | 8.47B |
| meta/muse-spark-open | 6 | 6 | 1048576 | 1.25 | 1.25 | 4.25 | 4.25 | 4.25 | BaseTen, Fireworks, Makora, Modal, Nebius, Together | 1.1875 / 4.0375 | 118B | >20 | 19.7B |
| qwen/qwen3-235b-a22b-2507 | 5 | 6 | 262144 | 0.0875 | 0.14 | 0.35 | 0.75 | 0.88 | GMICloud | 0.0831 / 0.3325 | 63.7B | >20 | 12.7B |
| deepseek/deepseek-chat-v3.1 | 5 | 5 | 163840 | 0.25 | 0.55 | 0.95 | 1.5 | 1.7 | DeepInfra | 0.2375 / 0.9025 | 54.3B | >20 | 10.9B |
| z-ai/glm-5 | 8 | 8 | 204800 | 0.6 | 0.975 | 1.92 | 2.875 | 3.2 | GMICloud, StreamLake | 0.57 / 1.824 | 41.7B | >20 | 5.21B |
| meta-llama/llama-3.3-70b-instruct | 10 | 11 | 131072 | 0.1 | 0.3715 | 0.32 | 0.715 | 2.253 | DeepInfra | 0.095 / 0.304 | 39.1B | >20 | 3.91B |
| z-ai/glm-4.7 | 6 | 7 | 204800 | 0.32 | 0.57 | 1.4 | 2.09 | 2.5 | DeepInfra | 0.304 / 1.33 | 36.2B | >20 | 6.03B |
| moonshotai/kimi-k2.5 | 5 | 5 | 262144 | 0.49 | 0.532 | 2.5 | 2.85 | 3.325 | AtlasCloud, SiliconFlow | 0.4655 / 2.375 | 35.4B | >20 | 7.08B |
| nvidia/nemotron-3-ultra-550b-a55b | 3 | 5 | 262144 | 0.4 | 0.6 | 1.76 | 2.4 | 3.125 | DeepInfra | 0.38 / 1.672 | 35.2B | paid slug >20; :free variant is rank 10 (4.46T) | 11.7B |
| minimax/minimax-m2.7 | 5 | 6 | 204800 | 0.21 | 0.3 | 0.84 | 1.2 | 1.8 | GMICloud | 0.1995 / 0.798 | 33.3B | >20 | 6.66B |
| mistralai/mistral-small-3.2-24b-instruct | 4 | 4 | 256000 | 0.075 | 0.0919 | 0.2 | 0.275 | 0.3 | DeepInfra | 0.0712 / 0.19 | 32.8B | >20 | 8.2B |
| qwen/qwen3-coder-next | 1 | 1 | 262144 | 0.12 | 0.12 | 0.8 | 0.8 | 0.8 | Parasail | 0.114 / 0.76 | 27.9B | >20 | 27.9B |
| meta-llama/llama-4-scout | 2 | 4 | 1310720 | 0.08 | 0.165 | 0.24 | 0.47 | 0.7 | DeepInfra | 0.076 / 0.228 | 22.9B | >20 | 11.4B |
| z-ai/glm-4.6 | 4 | 5 | 204800 | 0.4 | 0.49 | 1.6 | 1.975 | 2.2 | DeepInfra | 0.38 / 1.52 | 20.3B | >20 | 5.08B |
| deepseek/deepseek-chat | 2 | 3 | 163840 | 0.256 | 0.2567 | 0.712 | 0.8703 | 1.0287 | DeepInfra | 0.2432 / 0.6764 | 19.3B | >20 | 9.65B |
| meta-llama/llama-4-maverick | 3 | 3 | 524288 | 0.1875 | 0.35 | 0.6525 | 1 | 1.15 | DigitalOcean | 0.1781 / 0.6199 | 19.3B | >20 | 6.43B |
| qwen/qwen3-coder | 3 | 3 | 262144 | 0.22 | 0.3 | 1 | 1.5 | 1.8 | DeepInfra | 0.209 / 0.95 | 18B | >20 | 6B |
| deepseek/deepseek-r1-0528 | 3 | 3 | 163840 | 0.5 | 0.5 | 2.15 | 2.18 | 2.286 | DeepInfra | 0.475 / 2.0425 | 13.8B | >20 | 4.6B |
| qwen/qwen3-32b | 3 | 3 | 131072 | 0.08 | 0.14 | 0.28 | 0.4 | 0.57 | DeepInfra | 0.076 / 0.266 | 13.3B | >20 | 4.43B |
| minimax/minimax-m2.5 | 7 | 8 | 204800 | 0.27 | 0.3 | 0.95 | 1.2 | 1.2 | Venice | 0.2565 / 0.9025 | 12.2B | >20 | 1.74B |
| nvidia/nemotron-3-super-120b-a12b | 3 | 3 | 262144 | 0.08 | 0.085 | 0.4 | 0.45 | 2.4 | DeepInfra | 0.076 / 0.38 | 11.7B | >20 (free variant 514B) | 3.9B |
| minimax/minimax-m3.1-flash | 1 | 1 | 1000000 | 0.15 | 0.15 | 0.6 | 0.6 | 0.6 | Minimax | 0.1425 / 0.57 | 8.32B | 4 is the :free variant (10.3T); paid slug not in top 20 | 8.32B |
| mistralai/mistral-medium-3.1 | 1 | 3 | 131072 | 0.4 | 0.4 | 2 | 2 | 2 | Mistral | 0.38 / 1.9 | 5.08B | >20 | 5.08B |
| mistralai/mistral-small-2603 | 1 | 4 | 262144 | 0.15 | 0.15 | 0.6 | 0.6 | 0.6 | Mistral | 0.1425 / 0.57 | 5.03B | >20 | 5.03B |
| moonshotai/kimi-k2-thinking | 2 | 2 | 262144 | 0.6 | 0.6 | 2.5 | 2.5 | 2.5 | Google, Novita | 0.57 / 2.375 | 3.44B | >20 | 1.72B |
| mistralai/mistral-medium-3-5 | 1 | 3 | 262144 | 1.5 | 1.5 | 7.5 | 7.5 | 7.5 | Mistral | 1.425 / 7.125 | 3.19B | >20 | 3.19B |
| moonshotai/kimi-k2-0905 | 1 | 1 | 262144 | 0.6 | 0.6 | 2.5 | 2.5 | 2.5 | Novita | 0.57 / 2.375 | 3.09B | >20 | 3.09B |
| moonshotai/kimi-k2 | 1 | 1 | 131072 | 0.57 | 0.57 | 2.3 | 2.3 | 2.3 | Novita | 0.5415 / 2.185 | 1.86B | >20 | 1.86B |
| qwen/qwen3-coder-flash | 1 | 1 | 1000000 | 0.195 | 0.195 | 0.975 | 0.975 | 0.975 | Alibaba | 0.1852 / 0.9262 | 1.65B | >20 | 1.65B |
| z-ai/glm-4.5 | 1 | 1 | 131072 | 0.6 | 0.6 | 2.2 | 2.2 | 2.2 | Z.AI | 0.57 / 2.09 | 1.4B | >20 | 1.4B |
| qwen/qwen3-235b-a22b-thinking-2507 | 1 | 1 | 128000 | 0.45 | 0.45 | 3.5 | 3.5 | 3.5 | Venice | 0.4275 / 3.325 | 670M | >20 | 670M |
| deepseek/deepseek-r1 | 0 | 0 | None | n/a | n/a | n/a | n/a | n/a | none | n/a | not in top list | n/a | n/a |
| qwen/qwen3-235b-a22b | 0 | 0 | None | n/a | n/a | n/a | n/a | n/a | none | n/a | not in top list | n/a | n/a |
| qwen/qwen3.8-2.4t-a95b | 5 | 5 | 1048576 | 2 | 2 | 6 | 6 | 6 | Alibaba, Novita, SiliconFlow, Together, Venice | 1.9 / 5.7 | not in top list | n/a | n/a |

## Provider frequency across the models above

Source: the endpoints files listed above (checked 2026-10-22). 'Out price vs floor' is the median of (provider output price / cheapest output price for that model). 'Times cheapest' counts models where the provider posts the lowest output price (ties count).

| Provider | Models served (of 56) | Times cheapest | Out price vs floor (median x) | In price vs floor (median x) | Quantizations offered |
|---|---|---|---|---|---|
| DeepInfra | 34 | 18 | 1 | 1.18 | bf16, fp4, fp8, mxfp4 |
| Novita | 27 | 5 | 1.36 | 1.4 | bf16, fp4, fp8, unknown |
| Venice | 26 | 4 | 1.46 | 1.67 | fp4, fp8, int4, unknown |
| SiliconFlow | 21 | 3 | 2.04 | 3.4 | fp8, int4 |
| Parasail | 21 | 1 | 2 | 2.2 | bf16, fp4, fp8, int4 |
| GMICloud | 18 | 3 | 1.44 | 1.86 | bf16, fp8 |
| AtlasCloud | 16 | 1 | 2.56 | 2.79 | fp4, fp8, int4 |
| CoreWeave | 14 | 0 | 1.95 | 2.64 | fp16, fp4, fp8, nvfp4 |
| StreamLake | 13 | 3 | 1.33 | 1.34 | fp8, unknown |
| DigitalOcean | 13 | 1 | 2.35 | 2.82 | unknown |
| Phala | 13 | 0 | 2.93 | 5.71 | nvfp4, unknown |
| Together | 12 | 2 | 3.2 | 4.64 | unknown |
| Alibaba | 12 | 3 | 2.9 | 3.11 | fp8, unknown |
| Google | 11 | 1 | 2.4 | 3 | unknown |
| Baidu | 10 | 5 | 1.08 | 1.14 | fp4, fp8 |
| Relace | 10 | 0 | 1.95 | 1 | fp4, mxfp4, unknown |
| BaseTen | 9 | 1 | 3.14 | 4.29 | fp4, fp8, unknown |
| Wafer | 9 | 1 | 1.84 | 2.29 | fp4, fp8, mxfp4, nvfp4 |
| Cloudflare | 9 | 0 | 4 | 8.8 | fp8, unknown |
| Crusoe | 8 | 0 | 3.3 | 3.95 | bf16, fp4, fp8 |
| Reka | 7 | 0 | 3.96 | 1.77 | fp8, unknown |
| Sail Research | 7 | 2 | 1.39 | 3.55 | fp4, fp8 |
| DekaLLM | 7 | 0 | 1.56 | 1.61 | bf16, fp8, unknown |
| Makora | 7 | 1 | 3.14 | 2.72 | fp4, fp8, unknown |
| AkashML | 7 | 0 | 1.58 | 2 | bf16, fp4, fp8 |
| Z.AI | 7 | 2 | 1.57 | 1.67 | fp4, fp8 |
| SambaNova | 6 | 0 | 3.2 | 4.15 | fp8, unknown |
| InferenceNet | 6 | 1 | 2.77 | 1.08 | fp4, fp8 |
| Fireworks | 6 | 1 | 2.82 | 6.54 | unknown |
| Modal | 6 | 1 | 2.94 | 8.42 | mxfp4, nvfp4, unknown |
| Amazon Bedrock | 6 | 0 | 2.2 | 4.44 | unknown |
| Mancer 2 | 5 | 0 | 2 | 3.8 | fp4, fp8 |
| Morph | 5 | 0 | 3.33 | 3.61 | fp8 |
| Mistral | 5 | 3 | 1 | 1 | nvfp4, unknown |
| Mara | 4 | 0 | 3.86 | 3.84 | unknown |
| Friendli | 4 | 0 | 3.14 | 11.55 | unknown |
| Inceptron | 4 | 0 | 2.22 | 4.15 | fp4, fp8, int4 |
| Decart | 4 | 1 | 1.72 | 4.44 | fp4, mxfp4 |
| PrimeIntellect | 4 | 0 | 5.06 | 11 | unknown |
| Nebius | 4 | 1 | 3.57 | 4.64 | fp4, fp8 |
| Chutes | 4 | 1 | 1.09 | 1.16 | fp4, fp8, int4, mxfp4 |
| ModelRun | 4 | 0 | 2.56 | 6.61 | fp4, fp8 |
| Groq | 4 | 0 | 2.9 | 4.58 | unknown |
| Minimax | 4 | 1 | 1.31 | 1.23 | fp8, unknown |
| Darkbloom | 4 | 2 | 1.03 | 1 | fp4, fp8 |
| Ionstream | 3 | 0 | 4 | 2.53 | fp8, unknown |
| OpenInference | 3 | 0 | 2.78 | 1 | fp4 |
| Io Net | 3 | 0 | 2.29 | 3.61 | fp8, unknown |
| Near AI | 3 | 1 | 1.08 | 1.14 | fp4, fp8 |
| Azure | 2 | 0 | 4.17 | 4.27 | unknown |
| DeepSeek | 2 | 0 | 4.03 | 3.33 | unknown |
| Moonshot AI | 2 | 0 | 2.42 | 7.33 | int4, mxfp4 |
| Cerebras | 2 | 0 | 3.1 | 19.98 | fp16 |
| Tencent | 2 | 2 | 1 | 1 | fp8 |
| Xiaomi | 2 | 0 | 1.08 | 1.26 | fp8 |
| Cohere | 1 | 0 | 2.1 | 3.32 | unknown |
| Meta | 1 | 1 | 1 | 1 | unknown |
| Tenstorrent | 1 | 0 | 1.43 | 1.75 | fp8 |
| Featherless | 1 | 1 | 1 | 1 | fp4 |
| StepFun | 1 | 1 | 1 | 1 | fp8 |
| NextBit | 1 | 0 | 5.17 | 28.85 | fp4 |

## Detail tables, one per model (every endpoint)

### deepseek/deepseek-chat-v3.1

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-chat-v3.1/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 163840.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4 | fp4 | 163840 | 32768 | 0.25 | 0.95 | 0.13 | 99.8 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 163840 | 147456 | 0.27 | 1 | n/a | 96.7 | 0 |
| SambaNova | sambanova/fp8 | fp8 | 131072 | 7168 | 0.65 | 1.5 | n/a | 97.2 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 161000 | 144900 | 0.55 | 1.65 | 0.55 | 100 | 0 |
| Mara | mara | unknown | 131072 | 117964 | 0.6 | 1.7 | n/a | 0 | -5 |

### deepseek/deepseek-chat

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-chat/endpoints (checked 2026-10-22). Distinct providers: 2. Endpoints: 3. Model context: 163840.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4/flex | fp4 | 163840 | 147456 | 0.256 | 0.712 | n/a | 100 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 163840 | 16384 | 0.32 | 0.89 | n/a | 95.3 | 0 |
| StreamLake | streamlake | unknown | 128000 | 16000 | 0.2574 | 1.0287 | n/a | 99.8 | 0 |

### deepseek/deepseek-r1-0528

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-r1-0528/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 163840.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4 | fp4 | 163840 | 32768 | 0.5 | 2.15 | 0.35 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 163840 | 147456 | 0.5 | 2.18 | n/a | 100 | 0 |
| StreamLake | streamlake | unknown | 128000 | 32000 | 0.571 | 2.286 | n/a | 99.9 | 0 |

### deepseek/deepseek-v3.2

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v3.2/endpoints (checked 2026-10-22). Distinct providers: 12. Endpoints: 12. Model context: 163840.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp8 | fp8 | 131072 | 65536 | 0.07 | 0.105 | 0.007 | 96.7 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 163840 | 147456 | 0.2088 | 0.3096 | 0.0216 | 99.7 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 163840 | 16384 | 0.26 | 0.38 | 0.13 | 99.7 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 163840 | 147456 | 0.26 | 0.38 | 0.13 | 99.6 | 0 |
| Venice | venice | unknown | 160000 | 32768 | 0.2683 | 0.3902 | 0.1301 | 99.5 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 163840 | 147456 | 0.259 | 0.8 | 0.14 | 99.4 | 0 |
| DigitalOcean | digitalocean | unknown | 163840 | 147456 | 0.3 | 0.96 | 0.09 | 99.7 | 0 |
| Phala | phala | unknown | 163840 | 64000 | 1 | 1 | 0.5 | 100 | 0 |
| Friendli | friendli | unknown | 163840 | 147456 | 0.5 | 1.5 | 0.25 | 100 | 0 |
| Google | google-vertex | unknown | 163840 | 65536 | 0.56 | 1.68 | n/a | 25.8 | -5 |
| Mara | mara | unknown | 32768 | 7168 | 3 | 4.5 | n/a | 0 | 0 |
| SambaNova | sambanova | unknown | 32768 | 7168 | 3 | 4.5 | n/a | 97 | 0 |

### deepseek/deepseek-v4-flash-0731

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-flash-0731/endpoints (checked 2026-10-22). Distinct providers: 23. Endpoints: 26. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp8 | fp8 | 1048576 | 131072 | 0.0444 | 0.1333 | 0.0014 | 100 | 0 |
| Sail Research | sail-research/us | fp4 | 1048576 | 943718 | 0.15 | 0.15 | 0.042 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 943718 | 0.15 | 0.15 | 0.042 | 100 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 943718 | 0.0422 | 0.1729 | 0.0275 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 384000 | 0.06 | 0.18 | 0.015 | 100 | 0 |
| Wafer | wafer/fast | nvfp4 | 1048576 | 943718 | 0.14 | 0.23 | 0.135 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 943718 | 0.119 | 0.238 | 0.0238 | 100 | 0 |
| BaseTen | baseten/fp8 | fp8 | 1048576 | 384000 | 0.13 | 0.26 | 0.028 | 94.4 | 0 |
| BaseTen | baseten/fp32 | fp32 | 1048576 | 384000 | 0.13 | 0.26 | 0.028 | 93.9 | 0 |
| Venice | venice | unknown | 1000000 | 32768 | 0.13 | 0.26 | 0.028 | 97.8 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 262144 | 235929 | 0.13 | 0.28 | 0.07 | 100 | 0 |
| Cohere | cohere | unknown | 1048576 | 384000 | 0.14 | 0.28 | 0.07 | 99.7 | 0 |
| Together | together | unknown | 1048576 | 943718 | 0.14 | 0.28 | 0.03 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.14 | 0.28 | 0.05 | 100 | 0 |
| Inceptron | inceptron/fp4 | fp4 | 1048576 | 943718 | 0.11 | 0.3666 | 0.027 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 384000 | 0.132 | 0.396 | 0.0042 | 99.9 | 0 |
| Reka | reka | unknown | 262144 | 131072 | 0.05 | 0.528 | 0.02 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 393216 | 0.176 | 0.528 | 0.0176 | 99.7 | 0 |
| Alibaba | alibaba/us-east-1 | unknown | 1000000 | 393216 | 0.187 | 0.561 | 0.0187 | 99.8 | -2 |
| Mancer 2 | mancer/fp8 | fp8 | 1048576 | 943718 | 0.2 | 0.6 | n/a | 99.8 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 0.22 | 0.66 | 0.028 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 0.286 | 0.858 | 0.0091 | 100 | 0 |
| Phala | phala | unknown | 1048576 | 393216 | 0.308 | 0.924 | 0.0196 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 0.4092 | 1.2276 | 0.026 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp4 | fp4 | 1048576 | 393216 | 0.44 | 1.32 | 0.028 | 100 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 0.44 | 1.32 | 0.014 | 100 | 0 |

### deepseek/deepseek-v4-flash

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-flash/endpoints (checked 2026-10-22). Distinct providers: 15. Endpoints: 15. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 384000 | 0.07 | 0.14 | 0.014 | 100 | 0 |
| Wafer | wafer/mxfp4 | mxfp4 | 1048576 | 943718 | 0.7 | 0.17 | 0.013 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 65536 | 0.09 | 0.18 | 0.018 | 97.2 | 0 |
| Baidu | baidu/fp8 | fp8 | 1048576 | 131072 | 0.0909 | 0.1817 | 0.0182 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 0.091 | 0.182 | 0.0182 | 99.9 | 0 |
| Venice | venice | unknown | 1000000 | 32768 | 0.0966 | 0.1925 | 0.0196 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 384000 | 0.098 | 0.196 | 0.0196 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 0.13 | 0.28 | 0.028 | 99.4 | 0 |
| AtlasCloud | atlas-cloud/fp4 | fp4 | 1048576 | 393216 | 0.14 | 0.28 | 0.028 | 99.9 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.14 | 0.28 | 0.07 | 100 | 0 |
| Alibaba | alibaba/fp8/us-east-1 | fp8 | 1000000 | 393216 | 0.15 | 0.3 | 0.03 | 99.8 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 943718 | 0.05 | 0.45 | 0.05 | 100 | 0 |
| Mancer 2 | mancer/fp8 | fp8 | 1048576 | 943718 | 0.19 | 0.5 | n/a | 97.6 | 0 |
| Azure | azure/us | unknown | 1048576 | 384000 | 0.21 | 0.56 | 0.031 | 86.6 | 0 |
| Cloudflare | cloudflare | unknown | 384000 | 345600 | 0.44 | 1.32 | 0.014 | 99 | 0 |

### deepseek/deepseek-v4-pro-0813

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro-0813/endpoints (checked 2026-10-22). Distinct providers: 21. Endpoints: 23. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp8 | fp8 | 1048576 | 393216 | 0.1624 | 0.4871 | 0.0052 | 100 | 0 |
| Sail Research | sail-research/us | fp4 | 1048576 | 384000 | 0.45 | 0.8 | 0.065 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 384000 | 0.45 | 0.8 | 0.065 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 393216 | 0.5808 | 1.7424 | 0.0581 | 99.8 | 0 |
| Alibaba | alibaba/us-east-1 | unknown | 1000000 | 393216 | 0.66 | 1.98 | 0.066 | 99.6 | -2 |
| StreamLake | streamlake | unknown | 1024000 | 384000 | 0.66 | 1.98 | 0.022 | 100 | 0 |
| DeepSeek | deepseek | unknown | 1048576 | 393216 | 0.66 | 1.98 | 0.022 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 16384 | 1.3 | 2.6 | 0.1 | 99.9 | 0 |
| Phala | phala | unknown | 1048576 | 393216 | 0.957 | 2.8776 | 0.099 | 100 | 0 |
| Ionstream | ionstream | unknown | 1048576 | 943718 | 0.37 | 2.93 | 0.088 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 0.99 | 2.97 | 0.033 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 1.056 | 3.168 | 0.0352 | 100 | 0 |
| DekaLLM | dekallm | unknown | 1048576 | 943718 | 0.88 | 3.8 | 0.15 | 99.4 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 1048576 | 943718 | 1.31 | 3.96 | 0.044 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 393216 | 1.32 | 3.96 | 0.132 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 1.32 | 3.96 | 0.044 | 98.9 | 0 |
| Together | together | unknown | 1048576 | 943718 | 1.32 | 3.96 | 0.13 | 98.8 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 943718 | 1.32 | 3.96 | 0.044 | 94.8 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 1.32 | 3.96 | 0.044 | 100 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 1.32 | 3.96 | 0.044 | 99.5 | 0 |
| Venice | venice | unknown | 1000000 | 32768 | 1.65 | 4.95 | 0.165 | 98.4 | 0 |
| Wafer | wafer/mxfp4 | mxfp4 | 1048576 | 943718 | 0.25 | 5 | 0.249 | 99.4 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 393216 | 0.1461 | 8 | 0.15 | 99.8 | 0 |

### deepseek/deepseek-v4-pro

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4-pro/endpoints (checked 2026-10-22). Distinct providers: 15. Endpoints: 16. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp8 | fp8 | 1048576 | 393216 | 0.4411 | 0.8822 | 0.0365 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 384000 | 0.4427 | 0.8853 | 0.0369 | 100 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 393216 | 0.9 | 1.5 | 0.25 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048576 | 943718 | 0.957 | 1.914 | 0.0798 | 99.8 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 384000 | 1.044 | 2.088 | 0.2088 | 100 | 0 |
| Reka | reka | unknown | 1048576 | 393216 | 1.05 | 2.1 | 0.21 | 98.7 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 1.15 | 2.55 | 0.2 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 16384 | 1.3 | 2.6 | 0.1 | 99.9 | 0 |
| Alibaba | alibaba/fp8 | fp8 | 1000000 | 393216 | 1.416 | 2.832 | 0.118 | 97.7 | 0 |
| Alibaba | alibaba/fp8/us-east-1 | fp8 | 1000000 | 393216 | 1.56 | 3.12 | 0.13 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 1.5016 | 3.135 | 0.135 | 96.2 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 1.6 | 3.2 | 0.135 | 100 | 0 |
| Venice | venice | unknown | 1000000 | 32768 | 1.65 | 3.301 | 0.33 | 98.4 | 0 |
| AtlasCloud | atlas-cloud/fp4 | fp4 | 1048576 | 393216 | 1.68 | 3.38 | 0.13 | 99.4 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.45 | 3.48 | 0.1 | 72.6 | -2 |
| Azure | azure/us | unknown | 1048576 | 384000 | 1.91 | 3.83 | 0.16 | 100 | 0 |

### deepseek/deepseek-v4.1-flash-1017

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash-1017/endpoints (checked 2026-10-22). Distinct providers: 26. Endpoints: 30. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Sail Research | sail-research/fp4/us | fp4 | 1048576 | 384000 | 0.101 | 0.15 | 0.0067 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 384000 | 0.101 | 0.15 | 0.0067 | 99.9 | 0 |
| DeepInfra | deepinfra/fp8/flex | fp8 | 1048576 | 131072 | 0.0784 | 0.2352 | 0.0024 | 88.7 | -2 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 131072 | 0.098 | 0.294 | 0.0029 | 100 | 0 |
| DeepInfra | deepinfra/fp8/priority | fp8 | 1048576 | 131072 | 0.147 | 0.441 | 0.0044 | 99.9 | 0 |
| OpenInference | open-inference/fp4 | fp4 | 1048576 | 943718 | 0.07 | 0.5 | 0.008 | 99 | 0 |
| Relace | relace | unknown | 1048576 | 943718 | 0.07 | 0.5 | 0.008 | 100 | 0 |
| InferenceNet | inference-net/us | fp8 | 1040000 | 393216 | 0.08 | 0.5 | 0.008 | 100 | 0 |
| InferenceNet | inference-net/fp8 | fp8 | 1040000 | 393216 | 0.08 | 0.5 | 0.008 | 100 | 0 |
| Wafer | wafer/mxfp4 | mxfp4 | 1048576 | 943718 | 0.16 | 0.5 | 0.008 | 100 | 0 |
| Decart | decart/fp4 | fp4 | 1048576 | 262144 | 0.138 | 0.552 | 0.0028 | 99.9 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 0.1 | 0.6 | 0.003 | 100 | 0 |
| Reka | reka | unknown | 1048576 | 393216 | 0.15 | 0.6 | 0.003 | 98.3 | 0 |
| DeepSeek | deepseek | unknown | 1048576 | 393216 | 0.15 | 0.6 | 0.003 | 100 | 0 |
| Ionstream | ionstream | unknown | 1048576 | 943718 | 0.22 | 0.6 | 0.019 | 100 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.253 | 0.6 | 0.022 | 99.9 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 393216 | 0.165 | 0.66 | 0.0165 | 98.3 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 0.18 | 0.72 | 0.0036 | 99.6 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 393216 | 0.195 | 0.78 | 0.0039 | 99.7 | 0 |
| Baidu | baidu/fp8 | fp8 | 1048576 | 393216 | 0.28 | 1.13 | 0.006 | 100 | 0 |
| Crusoe | crusoe/fp8 | fp8 | 1048576 | 943718 | 0.29 | 1.2 | 0.007 | 100 | 0 |
| Makora | makora/fp8 | fp8 | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 99.5 | 0 |
| Phala | phala | unknown | 1048576 | 393216 | 0.3 | 1.2 | 0.006 | 99.4 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 0.3 | 1.2 | 0.006 | 98.4 | -2 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 0.3 | 1.2 | 0.006 | 99.9 | 0 |
| Together | together | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| PrimeIntellect | primeintellect | unknown | 1048576 | 131072 | 0.3 | 1.2 | 0.006 | 99.9 | 0 |
| BaseTen | baseten | unknown | 1048576 | 262144 | 0.3 | 1.2 | 0.007 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |

### deepseek/deepseek-v4.1-flash

Source: https://openrouter.ai/api/v1/models/deepseek/deepseek-v4.1-flash/endpoints (checked 2026-10-22). Distinct providers: 30. Endpoints: 38. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Decart | decart/fp4 | fp4 | 1048576 | 262144 | 0.09 | 0.18 | 0.018 | 100 | 0 |
| Sail Research | sail-research/fp4/us | fp4 | 1048576 | 384000 | 0.09 | 0.25 | 0.006 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 384000 | 0.09 | 0.25 | 0.006 | 100 | 0 |
| DeepInfra | deepinfra/fp8/flex | fp8 | 1048576 | 131072 | 0.112 | 0.336 | 0.0034 | 90.8 | -2 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 131072 | 0.14 | 0.42 | 0.0042 | 100 | 0 |
| OpenInference | open-inference/fp4 | fp4 | 1048576 | 943718 | 0.07 | 0.5 | 0.008 | 99.9 | 0 |
| Relace | relace | unknown | 1048576 | 943718 | 0.07 | 0.5 | 0.008 | 99.8 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 393216 | 0.135 | 0.54 | 0.0135 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 384000 | 0.147 | 0.588 | 0.0029 | 100 | 0 |
| Baidu | baidu/fp8 | fp8 | 1048576 | 393216 | 0.15 | 0.6 | 0.003 | 100 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.253 | 0.6 | 0.022 | 98.8 | 0 |
| DeepInfra | deepinfra/fp8/priority | fp8 | 1048576 | 131072 | 0.21 | 0.63 | 0.0063 | 73.5 | -5 |
| CoreWeave | coreweave/fp8 | fp8 | 1048576 | 943718 | 0.15 | 0.65 | 0.002 | 100 | 0 |
| Wafer | wafer/mxfp4 | mxfp4 | 1048576 | 943718 | 0.19 | 0.65 | 0.012 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 393216 | 0.165 | 0.66 | 0.0165 | 100 | 0 |
| InferenceNet | inference-net/us | fp8 | 1040000 | 393216 | 0.103 | 0.715 | 0.008 | 100 | 0 |
| InferenceNet | inference-net/fp8 | fp8 | 1040000 | 393216 | 0.103 | 0.715 | 0.008 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048575 | 943717 | 0.18 | 0.72 | 0.0036 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 393216 | 0.195 | 0.78 | 0.0039 | 100 | 0 |
| Reka | reka | unknown | 1048576 | 393216 | 0.105 | 0.84 | 0.007 | 94.3 | 0 |
| Fireworks | fireworks/spot | unknown | 1048576 | 943718 | 0.21 | 0.84 | 0.0042 | 100 | 0 |
| Phala | phala | unknown | 1048576 | 943718 | 0.21 | 0.84 | 0.0042 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 943718 | 0.225 | 0.9 | 0.006 | 100 | 0 |
| Makora | makora/fp8 | fp8 | 1048576 | 943718 | 0.26 | 1.17 | 0.0058 | 99.9 | 0 |
| Crusoe | crusoe/fp8 | fp8 | 1048576 | 943718 | 0.29 | 1.2 | 0.007 | 100 | 0 |
| Google | google-vertex/global | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.03 | 98.5 | -2 |
| Nebius | nebius/fp8 | fp8 | 1048000 | 943200 | 0.3 | 1.2 | 0.01 | 100 | 0 |
| PrimeIntellect | primeintellect | unknown | 1048576 | 131072 | 0.3 | 1.2 | 0.03 | 100 | 0 |
| BaseTen | baseten/us | unknown | 1048576 | 262144 | 0.3 | 1.2 | 0.007 | 100 | 0 |
| Together | together | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 393216 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| Modal | modal | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.03 | 100 | 0 |
| BaseTen | baseten | unknown | 1048576 | 262144 | 0.3 | 1.2 | 0.007 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 100 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 0.3 | 1.2 | 0.006 | 98 | -2 |
| Venice | venice/fp8 | fp8 | 1000000 | 131072 | 0.3 | 1.2 | 0.0075 | 100 | 0 |
| Fireworks | fireworks/us | unknown | 1048576 | 943718 | 0.45 | 1.8 | 0.009 | 100 | 0 |
| BaseTen | baseten/fast | unknown | 1048576 | 131072 | 0.6 | 2.4 | 0.014 | 99.8 | 0 |

### google/gemma-4-31b-it

Source: https://openrouter.ai/api/v1/models/google/gemma-4-31b-it/endpoints (checked 2026-10-22). Distinct providers: 12. Endpoints: 15. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8/flex | fp8 | 262144 | 235929 | 0.16 | 0.32 | n/a | 99.6 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 262144 | 235929 | 0.1 | 0.34 | 0.1 | 100 | 0 |
| Venice | venice/fp4 | fp4 | 256000 | 8192 | 0.12 | 0.36 | 0.09 | 98.1 | 0 |
| Chutes | chutes/fp4 | fp4 | 131072 | 65536 | 0.12 | 0.37 | 0.012 | 95.2 | 0 |
| Crusoe | crusoe/bf16 | bf16 | 262144 | 262141 | 0.14 | 0.4 | 0.14 | 98.8 | 0 |
| Friendli | friendli | unknown | 262144 | 8192 | 0.14 | 0.4 | n/a | 100 | 0 |
| Novita | novita/bf16 | bf16 | 262144 | 131072 | 0.14 | 0.4 | n/a | 84.2 | 0 |
| Parasail | parasail/fp8 | fp8 | 262144 | 235929 | 0.15 | 0.4 | 0.06 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 262144 | 16384 | 0.2 | 0.4 | n/a | 98.4 | 0 |
| DeepInfra | deepinfra/turbo | fp4 | 262144 | 16384 | 0.135 | 0.51 | 0.075 | 99.9 | 0 |
| DeepInfra | deepinfra/fp8/priority | fp8 | 262144 | 235929 | 0.3 | 0.6 | n/a | 93.2 | 0 |
| ModelRun | modelrun/fp4 | fp4 | 262144 | 235929 | 0.75 | 1 | 0.2 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 262144 | 235929 | 0.75 | 1 | 0.25 | 95.3 | 0 |
| Io Net | io-net | unknown | 262144 | 16384 | 0.361 | 1.0925 | 0.1805 | 93.4 | 0 |
| SambaNova | sambanova | unknown | 131072 | 117964 | 0.38 | 1.15 | n/a | 99.5 | -2 |

### meta-llama/llama-3.3-70b-instruct

Source: https://openrouter.ai/api/v1/models/meta-llama/llama-3.3-70b-instruct/endpoints (checked 2026-10-22). Distinct providers: 10. Endpoints: 11. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/turbo | fp8 | 131072 | 16384 | 0.1 | 0.32 | n/a | 99.4 | 0 |
| Novita | novita/bf16 | bf16 | 12288 | 11059 | 0.135 | 0.4 | n/a | 99.9 | 0 |
| Parasail | parasail/fp8 | fp8 | 131072 | 16384 | 0.22 | 0.5 | 0.11 | 99.5 | 0 |
| AkashML | akashml/fp8 | fp8 | 131072 | 128000 | 0.2 | 0.52 | 0.1 | 99.9 | 0 |
| CoreWeave | coreweave/fp16 | fp16 | 128000 | 115200 | 0.71 | 0.71 | 0.71 | 100 | 0 |
| Google | google-vertex/us-central1 | unknown | 128000 | 8192 | 0.72 | 0.72 | n/a | n/a | 0 |
| Google | google-vertex | unknown | 128000 | 115200 | 0.72 | 0.72 | n/a | n/a | 0 |
| Groq | groq | unknown | 131072 | 32768 | 0.59 | 0.79 | 0.295 | 100 | 0 |
| SambaNova | sambanova-turbo | unknown | 131072 | 3072 | 0.45 | 0.9 | n/a | 99.9 | 0 |
| Together | together | unknown | 131072 | 2048 | 1.04 | 1.04 | n/a | 97.9 | 0 |
| Cloudflare | cloudflare/fp8 | fp8 | 24000 | 21600 | 0.293 | 2.253 | n/a | 100 | 0 |

### meta-llama/llama-4-maverick

Source: https://openrouter.ai/api/v1/models/meta-llama/llama-4-maverick/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 524288.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DigitalOcean | digitalocean | unknown | 128000 | 16384 | 0.1875 | 0.6525 | 0.05 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 524288 | 32768 | 0.35 | 1 | 0.17 | 99.9 | 0 |
| Google | google-vertex/us-east5 | unknown | 524288 | 8192 | 0.35 | 1.15 | n/a | n/a | 0 |

### meta-llama/llama-4-scout

Source: https://openrouter.ai/api/v1/models/meta-llama/llama-4-scout/endpoints (checked 2026-10-22). Distinct providers: 2. Endpoints: 4. Model context: 1310720.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8/flex | fp8 | 327680 | 294912 | 0.08 | 0.24 | n/a | 67.2 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 327680 | 16384 | 0.1 | 0.3 | n/a | 99.6 | 0 |
| DeepInfra | deepinfra/fp8/priority | fp8 | 327680 | 294912 | 0.15 | 0.45 | n/a | 95.2 | 0 |
| Google | google-vertex/us-east5 | unknown | 1310720 | 8192 | 0.25 | 0.7 | n/a | n/a | 0 |

### meta/muse-spark-1.3-contributor

Source: https://openrouter.ai/api/v1/models/meta/muse-spark-1.3-contributor/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Meta | meta | unknown | 1048576 | 943718 | 0.1 | 0.2 | 0.002 | 100 | 0 |

### meta/muse-spark-open

Source: https://openrouter.ai/api/v1/models/meta/muse-spark-open/endpoints (checked 2026-10-22). Distinct providers: 6. Endpoints: 6. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Makora | makora/fp4 | fp4 | 1048576 | 131072 | 1.25 | 4.25 | 0.15 | 100 | 0 |
| Modal | modal | unknown | 1000000 | 262144 | 1.25 | 4.25 | 0.15 | 100 | 0 |
| Together | together | unknown | 1048576 | 943718 | 1.25 | 4.25 | 0.15 | 100 | 0 |
| Nebius | nebius/fp4 | fp4 | 1048576 | 943718 | 1.25 | 4.25 | 0.15 | 90 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 1.25 | 4.25 | 0.15 | 98.5 | 0 |
| BaseTen | baseten/fp4 | fp4 | 1048576 | 943718 | 1.25 | 4.25 | 0.15 | 100 | 0 |

### minimax/minimax-m2.5

Source: https://openrouter.ai/api/v1/models/minimax/minimax-m2.5/endpoints (checked 2026-10-22). Distinct providers: 7. Endpoints: 8. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Venice | venice | unknown | 198000 | 32768 | 0.27 | 0.95 | 0.03 | 94.5 | -2 |
| StreamLake | streamlake | unknown | 200000 | 128000 | 0.27 | 1.08 | 0.027 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 196608 | 176947 | 0.295 | 1.2 | 0.06 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 196608 | 176947 | 0.3 | 1.2 | 0.03 | 95 | 0 |
| DigitalOcean | digitalocean | unknown | 65536 | 58982 | 0.3 | 1.2 | 0.06 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 204800 | 131100 | 0.3 | 1.2 | 0.03 | 98.8 | 0 |
| Minimax | minimax/fp8 | fp8 | 204800 | 131072 | 0.3 | 1.2 | 0.03 | 100 | 0 |
| Minimax | minimax/highspeed | fp8 | 204800 | 131072 | 0.6 | 2.4 | 0.06 | 100 | 0 |

### minimax/minimax-m2.7

Source: https://openrouter.ai/api/v1/models/minimax/minimax-m2.7/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 6. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| GMICloud | gmicloud/fp8 | fp8 | 196608 | 176947 | 0.21 | 0.84 | 0.042 | 99.2 | 0 |
| Novita | novita/fp8 | fp8 | 204800 | 131072 | 0.27 | 1.08 | 0.054 | 99.3 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 196608 | 176947 | 0.3 | 1.2 | 0.06 | 98.4 | 0 |
| Minimax | minimax/fp8 | fp8 | 204800 | 131072 | 0.3 | 1.2 | 0.06 | 99.9 | 0 |
| Groq | groq | unknown | 196608 | 131072 | 0.6 | 1.8 | n/a | 98.5 | 0 |
| Minimax | minimax/highspeed | fp8 | 204800 | 131072 | 0.6 | 2.4 | 0.06 | 98.3 | 0 |

### minimax/minimax-m3.1-flash

Source: https://openrouter.ai/api/v1/models/minimax/minimax-m3.1-flash/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 1000000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Minimax | minimax | unknown | 1000000 | 524288 | 0.15 | 0.6 | 0.015 | 100 | 0 |

### minimax/minimax-m3

Source: https://openrouter.ai/api/v1/models/minimax/minimax-m3/endpoints (checked 2026-10-22). Distinct providers: 13. Endpoints: 14. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8/flex | fp8 | 524288 | 131072 | 0.224 | 0.88 | 0.0448 | 100 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 262144 | 235929 | 0.23 | 0.96 | 0.05 | 99.7 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048576 | 524288 | 0.24 | 0.96 | 0.048 | 99.7 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 524288 | 131072 | 0.28 | 1.1 | 0.056 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 1000000 | 512000 | 0.3 | 1.2 | 0.06 | 98.6 | 0 |
| Venice | venice/fp8 | fp8 | 524288 | 65536 | 0.3 | 1.2 | 0.06 | 97.5 | 0 |
| Together | together | unknown | 524288 | 471859 | 0.3 | 1.2 | 0.06 | 99.4 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 524288 | 0.3 | 1.2 | 0.06 | 99.9 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 524300 | 524288 | 0.3 | 1.2 | 0.06 | 98.7 | 0 |
| Novita | novita/fp8 | fp8 | 1000000 | 131072 | 0.3 | 1.2 | 0.06 | 100 | 0 |
| Minimax | minimax/fp8 | fp8 | 524288 | 512000 | 0.3 | 1.2 | 0.06 | 99.9 | 0 |
| ModelRun | modelrun/fp8 | fp8 | 1048576 | 943718 | 0.3 | 1.3 | 0.05 | 99.8 | 0 |
| Mara | mara | unknown | 1048576 | 943718 | 0.6 | 2.4 | n/a | 85.7 | 0 |
| SambaNova | sambanova | unknown | 1048576 | 943718 | 0.6 | 2.4 | 0.06 | 95.5 | 0 |

### mistralai/mistral-medium-3-5

Source: https://openrouter.ai/api/v1/models/mistralai/mistral-medium-3-5/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 3. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Mistral | mistral/zdr | unknown | 262144 | 209715 | 1.5 | 7.5 | n/a | 100 | 0 |
| Mistral | mistral | unknown | 262144 | 209715 | 1.5 | 7.5 | n/a | 100 | 0 |
| Mistral | mistral/eu | unknown | 262144 | 209715 | 1.65 | 8.25 | n/a | 100 | 0 |

### mistralai/mistral-medium-3.1

Source: https://openrouter.ai/api/v1/models/mistralai/mistral-medium-3.1/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 3. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Mistral | mistral/zdr | unknown | 131072 | 104857 | 0.4 | 2 | 0.04 | 99.9 | 0 |
| Mistral | mistral | unknown | 131072 | 104857 | 0.4 | 2 | 0.04 | 99.9 | 0 |
| Mistral | mistral/eu | unknown | 131072 | 104857 | 0.44 | 2.2 | 0.044 | 100 | 0 |

### mistralai/mistral-small-2603

Source: https://openrouter.ai/api/v1/models/mistralai/mistral-small-2603/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 4. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Mistral | mistral/zdr | unknown | 262144 | 209715 | 0.15 | 0.6 | 0.015 | 99.8 | 0 |
| Mistral | mistral | unknown | 262144 | 209715 | 0.15 | 0.6 | 0.015 | 99.9 | 0 |
| Mistral | mistral/eu | unknown | 262144 | 209715 | 0.165 | 0.66 | 0.0165 | 100 | 0 |
| Mistral | mistral/us | unknown | 262144 | 209715 | 0.165 | 0.66 | 0.0165 | 100 | 0 |

### mistralai/mistral-small-3.2-24b-instruct

Source: https://openrouter.ai/api/v1/models/mistralai/mistral-small-3.2-24b-instruct/endpoints (checked 2026-10-22). Distinct providers: 4. Endpoints: 4. Model context: 256000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8 | fp8 | 128000 | 16384 | 0.075 | 0.2 | n/a | 99.9 | 0 |
| Venice | venice/fp8 | fp8 | 256000 | 16384 | 0.0938 | 0.25 | n/a | 99.2 | 0 |
| Parasail | parasail/bf16 | bf16 | 131072 | 32768 | 0.09 | 0.3 | 0.05 | 100 | 0 |
| Mistral | mistral/eu | unknown | 32768 | 26214 | 0.1 | 0.3 | 0.01 | 100 | 0 |

### moonshotai/kimi-k2-0905

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2-0905/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Novita | novita/fp8 | fp8 | 262144 | 98304 | 0.6 | 2.5 | n/a | 100 | 0 |

### moonshotai/kimi-k2-thinking

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2-thinking/endpoints (checked 2026-10-22). Distinct providers: 2. Endpoints: 2. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Google | google-vertex | unknown | 262144 | 235929 | 0.6 | 2.5 | n/a | 85.2 | -5 |
| Novita | novita/bf16 | bf16 | 262144 | 98304 | 0.6 | 2.5 | 0.15 | 100 | 0 |

### moonshotai/kimi-k2.5

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2.5/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| AtlasCloud | atlas-cloud/int4 | int4 | 262144 | 235929 | 0.49 | 2.5 | 0.2 | 99.4 | 0 |
| SiliconFlow | siliconflow/int4 | int4 | 262144 | 235929 | 0.5 | 2.5 | 0.15 | 100 | 0 |
| Novita | novita | unknown | 262144 | 235929 | 0.57 | 2.85 | 0.095 | 99.9 | 0 |
| Amazon Bedrock | amazon-bedrock/us-east-2 | unknown | 262144 | 131072 | 0.6 | 3 | n/a | 100 | 0 |
| Venice | venice | unknown | 256000 | 65536 | 0.532 | 3.325 | 0.209 | 100 | 0 |

### moonshotai/kimi-k2.6

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2.6/endpoints (checked 2026-10-22). Distinct providers: 17. Endpoints: 17. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Baidu | baidu/fp4 | fp4 | 262144 | 235929 | 0.4493 | 1.892 | 0.0757 | 99.5 | 0 |
| Chutes | chutes/int4 | int4 | 262144 | 65535 | 0.45 | 1.95 | 0.045 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 262144 | 235929 | 0.57 | 2.4 | 0.114 | 100 | 0 |
| StreamLake | streamlake/fp8 | fp8 | 256000 | 230400 | 0.5985 | 2.52 | 0.1008 | 97.3 | 0 |
| Inceptron | inceptron/int4 | int4 | 262144 | 235929 | 0.5621 | 3.2 | 0.169 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 262144 | 235929 | 0.77 | 3.4 | 0.14 | 99.8 | 0 |
| Novita | novita | unknown | 262144 | 235929 | 0.8 | 3.4 | 0.16 | 100 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 262144 | 235929 | 0.65 | 3.41 | 0.15 | 99.7 | 0 |
| Crusoe | crusoe/bf16 | bf16 | 262144 | 235929 | 0.7 | 3.5 | 0.35 | 99.6 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 262144 | 16384 | 0.75 | 3.5 | 0.15 | 99.6 | 0 |
| Venice | venice/int4 | int4 | 256000 | 65536 | 0.75 | 3.5 | 0.16 | 97.1 | 0 |
| Parasail | parasail/int4 | int4 | 262144 | 235929 | 0.75 | 3.5 | 0.16 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 262144 | 235929 | 0.855 | 3.6 | 0.144 | n/a | 0 |
| AtlasCloud | atlas-cloud/int4 | int4 | 262144 | 235929 | 0.95 | 4 | 0.16 | 100 | 0 |
| Cloudflare | cloudflare | unknown | 262144 | 235929 | 0.95 | 4 | 0.16 | 100 | 0 |
| Moonshot AI | moonshotai/int4 | int4 | 262144 | 235929 | 0.95 | 4 | 0.16 | 100 | 0 |
| Phala | phala | unknown | 262144 | 235929 | 1.09 | 4.6 | 0.37 | 100 | 0 |

### moonshotai/kimi-k2

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k2/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Novita | novita/fp8 | fp8 | 131072 | 98304 | 0.57 | 2.3 | n/a | 100 | 0 |

### moonshotai/kimi-k3

Source: https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints (checked 2026-10-22). Distinct providers: 20. Endpoints: 28. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Sail Research | sail-research/fp4/us | fp4 | 1048576 | 943718 | 1.2 | 5.5 | 0.2 | n/a | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 943718 | 1.2 | 5.5 | 0.2 | n/a | 0 |
| Decart | decart/mxfp4 | mxfp4 | 1048576 | 943718 | 1.65 | 8.25 | 0.165 | 99.8 | 0 |
| Chutes | chutes/mxfp4 | mxfp4 | 1048576 | 65535 | 1.85 | 9.5 | 0.185 | 96.3 | 0 |
| Fireworks | fireworks/spot | unknown | 1048576 | 943718 | 2.1 | 10.5 | 0.21 | 77.6 | 0 |
| Wafer | wafer/us | mxfp4 | 1048576 | 943718 | 0.36 | 11.9 | 0.359 | 100 | 0 |
| InferenceNet | inference-net/us | fp4 | 1048576 | 943718 | 0.239 | 11.936 | 0.21 | 100 | 0 |
| InferenceNet | inference-net/fp4 | fp4 | 1048576 | 943718 | 0.239 | 11.936 | 0.21 | 100 | 0 |
| Relace | relace/fp4 | fp4 | 1048576 | 943718 | 0.3 | 12 | 0.25 | 99.4 | 0 |
| Phala | phala | unknown | 1048576 | 943718 | 2.55 | 12.75 | 0.255 | 99.9 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 943718 | 2.55 | 12.95 | 0.255 | 100 | 0 |
| InferenceNet | inference-net/fast | fp4 | 1048576 | 943718 | 2.04 | 13.2 | 0.35 | 99.4 | 0 |
| AkashML | akashml/fp4 | fp4 | 1048576 | 943718 | 1.2 | 14 | 1.2 | 99.7 | 0 |
| DeepInfra | deepinfra/mxfp4 | mxfp4 | 1048576 | 943718 | 2.85 | 14.25 | 0.285 | 99.9 | 0 |
| InferenceNet | inference-net/us/fast | fp4 | 1048576 | 943718 | 2.24 | 14.519 | 0.35 | 99.7 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.892 | 14.9 | 0.427 | 98.9 | 0 |
| Makora | makora/fp4 | fp4 | 1048576 | 943718 | 0.65 | 15 | 0.23 | 99.4 | 0 |
| Amazon Bedrock | amazon-bedrock/us-east-2 | unknown | 1048576 | 128000 | 3 | 15 | 0.3 | 94.2 | 0 |
| Parasail | parasail/fp4 | fp4 | 1048576 | 943718 | 3 | 15 | 0.3 | 97.4 | 0 |
| Modal | modal/mxfp4 | mxfp4 | 1048576 | 943718 | 3 | 15 | 0.3 | 100 | 0 |
| Together | together | unknown | 1048576 | 943718 | 3 | 15 | 0.3 | 99.9 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 3 | 15 | 0.3 | 97.9 | 0 |
| BaseTen | baseten/fp8 | fp8 | 1048576 | 262144 | 3 | 15 | 0.3 | 99.7 | 0 |
| Moonshot AI | moonshotai/mxfp4 | mxfp4 | 1048576 | 943718 | 3 | 15 | 0.3 | 100 | 0 |
| Wafer | wafer | mxfp4 | 1048576 | 943718 | 0.238 | 16 | 0.228 | 100 | 0 |
| Alibaba | alibaba | unknown | 1048576 | 131072 | 3.45 | 17.25 | 0.345 | 98.8 | 0 |
| Fireworks | fireworks/us | unknown | 1048576 | 943718 | 4.5 | 22.5 | 0.45 | 97.6 | 0 |
| Fireworks | fireworks/fast | unknown | 1048576 | 943718 | 4.5 | 22.5 | 0.45 | 98.5 | 0 |

### nvidia/nemotron-3-super-120b-a12b

Source: https://openrouter.ai/api/v1/models/nvidia/nemotron-3-super-120b-a12b/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/bf16 | bf16 | 262144 | 16384 | 0.085 | 0.4 | n/a | 100 | 0 |
| DekaLLM | dekallm/fp8 | fp8 | 262144 | 235929 | 0.08 | 0.45 | n/a | 99.9 | 0 |
| Crusoe | crusoe/fp8 | fp8 | 262144 | 235929 | 0.3 | 2.4 | 0.15 | 100 | 0 |

### nvidia/nemotron-3-ultra-550b-a55b

Source: https://openrouter.ai/api/v1/models/nvidia/nemotron-3-ultra-550b-a55b/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 5. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4/flex | fp4 | 262144 | 16384 | 0.4 | 1.76 | 0.08 | 100 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 262144 | 16384 | 0.5 | 2.2 | 0.1 | 100 | 0 |
| BaseTen | baseten/fp4/us | fp4 | 202800 | 182520 | 0.6 | 2.4 | 0.12 | 99.3 | 0 |
| BaseTen | baseten/fp4 | fp4 | 202800 | 182520 | 0.6 | 2.4 | 0.12 | 98.9 | 0 |
| Venice | venice/fp8 | fp8 | 256000 | 32768 | 0.625 | 3.125 | 0.1875 | 100 | 0 |

### openai/gpt-oss-120b

Source: https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints (checked 2026-10-22). Distinct providers: 22. Endpoints: 24. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Near AI | near-ai/fp4 | fp4 | 131072 | 117964 | 0.03 | 0.15 | 0.015 | 97.5 | 0 |
| Venice | venice/int4 | int4 | 128000 | 32768 | 0.03 | 0.15 | 0.03 | 99.5 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 131072 | 117964 | 0.03 | 0.17 | 0.03 | 99.7 | 0 |
| DeepInfra | deepinfra/bf16 | bf16 | 131072 | 117964 | 0.037 | 0.17 | n/a | 100 | 0 |
| DekaLLM | dekallm/bf16 | bf16 | 131072 | 117964 | 0.03 | 0.18 | 0.03 | 100 | 0 |
| AkashML | akashml/bf16 | bf16 | 131072 | 117964 | 0.03 | 0.187 | 0.03 | 99.9 | 0 |
| Crusoe | crusoe/bf16 | bf16 | 131072 | 117964 | 0.05 | 0.25 | 0.05 | 99.7 | 0 |
| Mancer 2 | mancer/fp8 | fp8 | 131072 | 117964 | 0.05 | 0.25 | n/a | 99.8 | 0 |
| Novita | novita/fp4 | fp4 | 131072 | 32768 | 0.05 | 0.25 | n/a | 100 | 0 |
| Google | google-vertex/global | unknown | 131072 | 117964 | 0.09 | 0.36 | n/a | 80 | -5 |
| DigitalOcean | digitalocean | unknown | 128000 | 4096 | 0.06 | 0.42 | 0.012 | 100 | 0 |
| BaseTen | baseten/fp4/us | fp4 | 128072 | 115264 | 0.1 | 0.5 | 0.1 | 99.8 | 0 |
| BaseTen | baseten/fp4 | fp4 | 128072 | 115264 | 0.1 | 0.5 | 0.1 | 99.5 | 0 |
| Amazon Bedrock | amazon-bedrock/eu-west-1 | unknown | 131072 | 117964 | 0.15 | 0.6 | n/a | 100 | 0 |
| Nebius | nebius/fp4 | fp4 | 131072 | 117964 | 0.15 | 0.6 | n/a | 100 | 0 |
| Amazon Bedrock | amazon-bedrock | unknown | 131072 | 117964 | 0.15 | 0.6 | n/a | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 131072 | 8192 | 0.15 | 0.6 | 0.075 | 97 | 0 |
| Phala | phala | unknown | 131072 | 32768 | 0.15 | 0.6 | n/a | 99.8 | 0 |
| Together | together | unknown | 131072 | 117964 | 0.15 | 0.6 | n/a | 97.8 | 0 |
| Groq | groq | unknown | 131072 | 65536 | 0.15 | 0.6 | 0.075 | 100 | 0 |
| Parasail | parasail/fp4 | fp4 | 131072 | 117964 | 0.1 | 0.75 | 0.055 | 100 | 0 |
| Mara | mara | unknown | 131072 | 117964 | 0.15 | 0.75 | n/a | 89.5 | 0 |
| Cerebras | cerebras/fp16 | fp16 | 131072 | 40960 | 0.35 | 0.75 | 0.35 | 100 | 0 |
| SambaNova | sambanova | unknown | 131072 | 117964 | 0.14 | 0.95 | n/a | 100 | 0 |

### openai/gpt-oss-20b

Source: https://openrouter.ai/api/v1/models/openai/gpt-oss-20b/endpoints (checked 2026-10-22). Distinct providers: 10. Endpoints: 11. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Darkbloom | darkbloom/fp8 | fp8 | 131072 | 32768 | 0.018 | 0.09 | 0.009 | 100 | 0 |
| AkashML | akashml/fp4 | fp4 | 131072 | 117964 | 0.02 | 0.1 | n/a | 100 | 0 |
| CoreWeave | coreweave/fp4 | fp4 | 131072 | 117964 | 0.03 | 0.13 | 0.03 | 100 | 0 |
| DekaLLM | dekallm/bf16 | bf16 | 131072 | 117964 | 0.029 | 0.14 | 0.029 | 100 | 0 |
| DeepInfra | deepinfra/bf16 | bf16 | 131072 | 117964 | 0.03 | 0.14 | n/a | 99.3 | 0 |
| Parasail | parasail/fp4 | fp4 | 131072 | 117964 | 0.03 | 0.15 | 0.02 | 99.9 | 0 |
| Amazon Bedrock | amazon-bedrock/eu-west-1 | unknown | 131072 | 117964 | 0.07 | 0.15 | n/a | 100 | 0 |
| Amazon Bedrock | amazon-bedrock | unknown | 131072 | 117964 | 0.07 | 0.15 | n/a | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 131072 | 8192 | 0.04 | 0.18 | n/a | 92.1 | -2 |
| Google | google-vertex/us-central1 | unknown | 131072 | 32768 | 0.07 | 0.25 | n/a | 46.2 | -5 |
| Groq | groq | unknown | 131072 | 65536 | 0.075 | 0.3 | 0.0375 | 97.2 | 0 |

### qwen/qwen3-235b-a22b-2507

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-235b-a22b-2507/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 6. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| GMICloud | gmicloud/fp8 | fp8 | 262144 | 235929 | 0.0875 | 0.35 | 0.0175 | 0 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 262144 | 16384 | 0.09 | 0.55 | n/a | 81.8 | 0 |
| Venice | venice/fp8 | fp8 | 128000 | 16384 | 0.15 | 0.75 | n/a | 91.4 | 0 |
| Parasail | parasail/fp8 | fp8 | 131072 | 117964 | 0.14 | 0.8 | 0.05 | 100 | 0 |
| Google | google-vertex/us-south1 | unknown | 262144 | 16384 | 0.22 | 0.88 | n/a | 26 | -5 |
| Google | google-vertex/us-south1 | unknown | 262144 | 16384 | 0.25 | 1 | n/a | 27.1 | -5 |

### qwen/qwen3-235b-a22b-thinking-2507

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-235b-a22b-thinking-2507/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 128000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Venice | venice/fp8 | fp8 | 128000 | 16384 | 0.45 | 3.5 | n/a | 100 | 0 |

### qwen/qwen3-32b

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-32b/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8 | fp8 | 40960 | 16384 | 0.08 | 0.28 | n/a | 96 | 0 |
| Tenstorrent | tenstorrent/fp8 | fp8 | 20000 | 16400 | 0.14 | 0.4 | 0.09 | 99.7 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 131072 | 117964 | 0.14 | 0.57 | n/a | 99.4 | 0 |

### qwen/qwen3-coder-flash

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-coder-flash/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 1000000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Alibaba | alibaba | unknown | 1000000 | 65536 | 0.195 | 0.975 | 0.039 | 100 | 0 |

### qwen/qwen3-coder-next

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-coder-next/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Parasail | parasail/bf16 | bf16 | 262144 | 235929 | 0.12 | 0.8 | 0.07 | 100 | 0 |

### qwen/qwen3-coder

Source: https://openrouter.ai/api/v1/models/qwen/qwen3-coder/endpoints (checked 2026-10-22). Distinct providers: 3. Endpoints: 3. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/turbo | fp4 | 262144 | 65536 | 0.3 | 1 | 0.1 | 94.7 | -2 |
| Venice | venice/fp8 | fp8 | 256000 | 65536 | 0.35 | 1.5 | 0.04 | 80.3 | -2 |
| Google | google-vertex/us-south1 | unknown | 262144 | 65536 | 0.22 | 1.8 | n/a | 62 | -5 |

### qwen/qwen3.6-35b-a3b

Source: https://openrouter.ai/api/v1/models/qwen/qwen3.6-35b-a3b/endpoints (checked 2026-10-22). Distinct providers: 10. Endpoints: 10. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Darkbloom | darkbloom/fp4 | fp4 | 262144 | 32768 | 0.05 | 0.7 | 0.025 | 100 | 0 |
| AkashML | akashml/fp8 | fp8 | 262144 | 235929 | 0.1 | 0.9 | 0.05 | 100 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 262144 | 65536 | 0.1 | 0.95 | 0.1 | 99 | 0 |
| Parasail | parasail/fp8 | fp8 | 262144 | 235929 | 0.1 | 0.95 | 0.05 | 100 | 0 |
| DekaLLM | dekallm | unknown | 262144 | 235929 | 0.1 | 1 | 0.05 | 99.6 | 0 |
| Venice | venice/fp8 | fp8 | 256000 | 65536 | 0.1 | 1 | n/a | 100 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 262144 | 235929 | 0.25 | 1.25 | 0.25 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 262144 | 65536 | 0.25 | 1.25 | 0.25 | 99.3 | 0 |
| Phala | phala | unknown | 262144 | 235929 | 0.2 | 1.27 | 0.056 | 96.8 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 262144 | 235929 | 0.24 | 1.8 | 0.15 | 96.6 | 0 |

### qwen/qwen3.8-2.4t-a95b

Source: https://openrouter.ai/api/v1/models/qwen/qwen3.8-2.4t-a95b/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Novita | novita | unknown | 1000000 | 131072 | 2 | 6 | 0.25 | 99.8 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 131072 | 2 | 6 | 0.25 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 131072 | 2 | 6 | 0.25 | 100 | 0 |
| Venice | venice | unknown | 262144 | 65536 | 2 | 6 | 0.25 | 100 | 0 |
| Together | together | unknown | 1010000 | 909000 | 2 | 6 | 0.25 | 99.8 | 0 |

### qwen/qwen3.8-27b

Source: https://openrouter.ai/api/v1/models/qwen/qwen3.8-27b/endpoints (checked 2026-10-22). Distinct providers: 20. Endpoints: 20. Model context: 1000000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Chutes | chutes/fp8 | fp8 | 262144 | 65536 | 0.039 | 1.25 | 0.0039 | 100 | 0 |
| Near AI | near-ai/fp8 | fp8 | 262144 | 65536 | 0.04 | 1.35 | 0.018 | 96.5 | 0 |
| Cerebras | cerebras/fp16 | fp16 | 65536 | 32768 | 0.99 | 1.49 | 0.99 | 100 | 0 |
| DeepInfra | deepinfra/bf16 | bf16 | 262144 | 235929 | 0.15 | 1.875 | 0.0375 | 100 | 0 |
| Ionstream | ionstream/fp8 | fp8 | 262144 | 65536 | 0.04 | 1.95 | 0.02 | 98.4 | 0 |
| AkashML | akashml/fp8 | fp8 | 262144 | 131072 | 0.225 | 1.98 | 0.05 | 100 | 0 |
| Darkbloom | darkbloom/fp4 | fp4 | 262144 | 32768 | 0.035 | 2.2 | 0.0175 | 73.4 | 0 |
| Reka | reka/fp8 | fp8 | 262144 | 235929 | 0.04 | 2.2 | 0.02 | 99.8 | 0 |
| Parasail | parasail/fp8 | fp8 | 262144 | 235929 | 0.24 | 2.2 | 0.05 | 99.6 | 0 |
| Modal | modal | unknown | 262144 | 235929 | 0.04 | 2.3 | 0.02 | 99.9 | 0 |
| Wafer | wafer/fp8 | fp8 | 262144 | 235929 | 0.06 | 2.3 | 0.059 | 98.3 | 0 |
| DekaLLM | dekallm | unknown | 262144 | 235929 | 0.04 | 2.5 | 0.02 | 100 | 0 |
| ModelRun | modelrun/fp4 | fp4 | 262144 | 235929 | 0.2 | 2.5 | 0.09 | 100 | 0 |
| Mancer 2 | mancer/fp8 | fp8 | 262144 | 235929 | 0.2 | 2.5 | n/a | 99.4 | 0 |
| Phala | phala | unknown | 1000000 | 262144 | 0.2 | 2.5 | 0.05 | 99.6 | -2 |
| Alibaba | alibaba | unknown | 1000000 | 131072 | 0.425 | 2.55 | 0.085 | 99.8 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 262144 | 235929 | 0.4 | 3 | 0.15 | 100 | 0 |
| Novita | novita | unknown | 1000000 | 131072 | 0.42 | 3 | 0.085 | 99.8 | 0 |
| Cloudflare | cloudflare | unknown | 262144 | 235929 | 0.45 | 3.2 | 0.05 | 100 | 0 |
| Venice | venice/fp8 | fp8 | 262144 | 65536 | 0.45 | 3.2 | n/a | 100 | 0 |

### qwen/qwen3.8-flash

Source: https://openrouter.ai/api/v1/models/qwen/qwen3.8-flash/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 2. Model context: 1000000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Alibaba | alibaba/us-east-1 | unknown | 1000000 | 131072 | 0.15 | 0.47 | 0.016 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 131072 | 0.15 | 0.47 | 0.016 | 100 | 0 |

### stepfun/step-5-preview

Source: https://openrouter.ai/api/v1/models/stepfun/step-5-preview/endpoints (checked 2026-10-22). Distinct providers: 4. Endpoints: 5. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| InferenceNet | inference-net/us | fp4 | 1048576 | 131072 | 1 | 2.7 | 0.05 | 100 | 0 |
| InferenceNet | inference-net/fp4 | fp4 | 1048576 | 131072 | 1 | 2.7 | 0.05 | 100 | 0 |
| Featherless | featherless/fp4 | fp4 | 262144 | 32768 | 1 | 2.7 | 0.1 | 0 | 0 |
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 65536 | 1 | 2.7 | 0.1 | 100 | 0 |
| StepFun | stepfun/fp8 | fp8 | 1000000 | 64000 | 1 | 2.7 | 0.1 | 100 | 0 |

### tencent/hy3

Source: https://openrouter.ai/api/v1/models/tencent/hy3/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 262144.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Tencent | tencent/fp8 | fp8 | 262144 | 128000 | 0.132 | 0.528 | 0.033 | 100 | 0 |
| Novita | novita | unknown | 262144 | 235929 | 0.14 | 0.58 | 0.035 | 100 | 0 |
| GMICloud | gmicloud/bf16 | bf16 | 262144 | 235929 | 0.14 | 0.58 | 0.035 | 99.9 | 0 |
| Phala | phala | unknown | 262144 | 235929 | 0.15 | 0.64 | 0.04 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 262144 | 131072 | 0.2 | 0.8 | 0.05 | 100 | 0 |

### tencent/hy4-preview

Source: https://openrouter.ai/api/v1/models/tencent/hy4-preview/endpoints (checked 2026-10-22). Distinct providers: 4. Endpoints: 4. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4 | fp4 | 1048576 | 131072 | 0.834 | 2.501 | 0.042 | 99.7 | 0 |
| Novita | novita/fp8 | fp8 | 1000000 | 64000 | 0.834 | 2.501 | 0.042 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 262144 | 0.834 | 2.501 | 0.042 | 100 | 0 |
| Tencent | tencent/fp8 | fp8 | 1048576 | 64000 | 0.834 | 2.501 | 0.042 | 100 | 0 |

### xiaomi/mimo-v2.6-flash

Source: https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-flash/endpoints (checked 2026-10-22). Distinct providers: 9. Endpoints: 9. Model context: 1050000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 943718 | 0.133 | 0.266 | 0.0027 | 98.5 | 0 |
| Darkbloom | darkbloom/fp4 | fp4 | 1048576 | 131072 | 0.1 | 0.28 | 0.05 | 99.5 | 0 |
| Makora | makora/fp8 | fp8 | 1048576 | 131072 | 0.13 | 0.28 | 0.002 | 96.5 | 0 |
| Relace | relace/mxfp4 | mxfp4 | 1048576 | 131072 | 0.13 | 0.28 | 0.003 | 99.9 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 131072 | 0.14 | 0.28 | 0.0028 | 99.6 | 0 |
| GMICloud | gmicloud/bf16 | bf16 | 1050000 | 945000 | 0.14 | 0.28 | 0.003 | 94.3 | -2 |
| Xiaomi | xiaomi/fp8 | fp8 | 1048576 | 131072 | 0.14 | 0.28 | 0.0028 | 100 | 0 |
| Io Net | io-net/fp8 | fp8 | 1048320 | 131072 | 0.15 | 0.29 | 0.025 | 99.2 | 0 |
| Venice | venice/fp8 | fp8 | 1000000 | 131072 | 0.175 | 0.35 | 0.0037 | 99.3 | 0 |

### xiaomi/mimo-v2.6-pro

Source: https://openrouter.ai/api/v1/models/xiaomi/mimo-v2.6-pro/endpoints (checked 2026-10-22). Distinct providers: 5. Endpoints: 5. Model context: 1050000.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp8 | fp8 | 1048576 | 943718 | 0.387 | 0.783 | 0.0032 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 131072 | 0.435 | 0.87 | 0.0036 | 98.9 | -2 |
| GMICloud | gmicloud/bf16 | bf16 | 1050000 | 945000 | 0.435 | 0.87 | 0.004 | 99.4 | 0 |
| Xiaomi | xiaomi/fp8 | fp8 | 1048576 | 131072 | 0.435 | 0.87 | 0.0036 | 99.4 | 0 |
| StreamLake | streamlake | unknown | 1000000 | 128000 | 0.522 | 1.044 | 0.0043 | 30.8 | 0 |

### z-ai/glm-4.5

Source: https://openrouter.ai/api/v1/models/z-ai/glm-4.5/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 131072.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Z.AI | z-ai/fp8 | fp8 | 131072 | 98304 | 0.6 | 2.2 | 0.11 | 100 | 0 |

### z-ai/glm-4.6

Source: https://openrouter.ai/api/v1/models/z-ai/glm-4.6/endpoints (checked 2026-10-22). Distinct providers: 4. Endpoints: 5. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4/flex | fp4 | 202752 | 131072 | 0.4 | 1.6 | 0.08 | n/a | 0 |
| Venice | venice/fp4 | fp4 | 198000 | 16384 | 0.43 | 1.75 | 0.08 | 80 | -5 |
| DeepInfra | deepinfra/fp4 | fp4 | 202752 | 131072 | 0.5 | 2 | 0.1 | 99.6 | 0 |
| Novita | novita/bf16 | bf16 | 204800 | 131072 | 0.55 | 2.2 | 0.11 | 99.8 | 0 |
| Z.AI | z-ai/fp4 | fp4 | 202752 | 131072 | 0.6 | 2.2 | 0.11 | 99.9 | 0 |

### z-ai/glm-4.7

Source: https://openrouter.ai/api/v1/models/z-ai/glm-4.7/endpoints (checked 2026-10-22). Distinct providers: 6. Endpoints: 7. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| DeepInfra | deepinfra/fp4/flex | fp4 | 202752 | 131072 | 0.32 | 1.4 | 0.064 | 100 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 202752 | 131072 | 0.4 | 1.75 | 0.08 | 94.7 | 0 |
| Venice | venice/fp4 | fp4 | 198000 | 16384 | 0.4004 | 1.9292 | 0.0801 | 60.3 | 0 |
| Novita | novita/fp8 | fp8 | 204800 | 131072 | 0.54 | 1.98 | 0.099 | 99.6 | 0 |
| Google | google-vertex | unknown | 200000 | 128000 | 0.6 | 2.2 | n/a | 45.2 | -5 |
| Z.AI | z-ai/fp4 | fp4 | 202752 | 131072 | 0.6 | 2.2 | 0.11 | 99.7 | 0 |
| Mancer 2 | mancer/fp4 | fp4 | 131072 | 117964 | 0.7 | 2.5 | n/a | 64.5 | 0 |

### z-ai/glm-5.3-flash

Source: https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flash/endpoints (checked 2026-10-22). Distinct providers: 30. Endpoints: 34. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| StreamLake | streamlake/fp8 | fp8 | 1024000 | 128000 | 0.0435 | 0.145 | 0.0087 | 98.8 | -5 |
| OpenInference | open-inference/fp4 | fp4 | 1048576 | 943718 | 0.0052 | 0.1985 | 0.0052 | 99.9 | 0 |
| Relace | relace | unknown | 1048576 | 131072 | 0.0052 | 0.1985 | 0.0052 | 100 | 0 |
| Wafer | wafer/nvfp4 | nvfp4 | 1048576 | 131072 | 0.074 | 0.2 | 0.073 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048576 | 943718 | 0.075 | 0.25 | 0.015 | 97.1 | 0 |
| Sail Research | sail-research/us | fp4 | 1048576 | 131072 | 0.0784 | 0.25 | 0.0261 | 100 | 0 |
| Sail Research | sail-research/fp4 | fp4 | 1048576 | 131072 | 0.0784 | 0.25 | 0.0261 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 131072 | 0.084 | 0.28 | 0.0168 | 99.9 | 0 |
| InferenceNet | inference-net/us | fp4 | 1048576 | 262144 | 0.12 | 0.388 | 0.032 | 100 | 0 |
| InferenceNet | inference-net/fp4 | fp4 | 1048576 | 262144 | 0.12 | 0.388 | 0.032 | 100 | 0 |
| Phala | phala/nvfp4 | nvfp4 | 1048576 | 131072 | 0.1275 | 0.425 | 0.0255 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 131072 | 0.1312 | 0.4375 | 0.03 | 100 | 0 |
| Makora | makora | unknown | 1048576 | 131072 | 0.14 | 0.47 | 0.024 | 99.4 | 0 |
| Near AI | near-ai/fp8 | fp8 | 1048576 | 943718 | 0.08 | 0.5 | 0.012 | 92.8 | -5 |
| PrimeIntellect | primeintellect | unknown | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | 97.3 | 0 |
| Modal | modal/nvfp4 | nvfp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | n/a | 0 |
| BaseTen | baseten/fp8/us | fp8 | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | n/a | 0 |
| Crusoe | crusoe/fp4 | fp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 94.5 | 0 |
| CoreWeave | coreweave/nvfp4 | nvfp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.02 | 99.9 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | 96.1 | 0 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 99 | 0 |
| Friendli | friendli | unknown | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 262144 | 0.15 | 0.5 | 0.03 | 99.7 | -5 |
| Together | together | unknown | 1048575 | 943717 | 0.15 | 0.5 | 0.03 | 99 | -2 |
| Parasail | parasail/fp4 | fp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 99.9 | 0 |
| BaseTen | baseten/fp8 | fp8 | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | n/a | 0 |
| Venice | venice | unknown | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | 99.9 | -2 |
| DeepInfra | deepinfra/fp4 | fp4 | 1048576 | 943718 | 0.15 | 0.5 | 0.03 | 99.9 | 0 |
| Z.AI | z-ai/fp8 | fp8 | 1048576 | 131072 | 0.15 | 0.5 | 0.03 | 100 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.143 | 0.65 | 0.04 | 99.4 | 0 |
| Inceptron | inceptron/fp8 | fp8 | 1048576 | 943718 | 0.18 | 0.69 | 0.075 | 100 | 0 |
| NextBit | nextbit/fp4 | fp4 | 1048576 | 128000 | 0.15 | 0.75 | 0.05 | 96.9 | 0 |
| Fireworks | fireworks/us | unknown | 1048576 | 943718 | 0.225 | 0.75 | 0.045 | 100 | 0 |
| Reka | reka | unknown | 1048576 | 943718 | 0.08 | 1.6 | 0.04 | 99.9 | 0 |

### z-ai/glm-5.3-flashx

Source: https://openrouter.ai/api/v1/models/z-ai/glm-5.3-flashx/endpoints (checked 2026-10-22). Distinct providers: 1. Endpoints: 1. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Z.AI | z-ai/fp8 | fp8 | 1048576 | 131072 | 0.37 | 1.25 | 0.09 | 100 | 0 |

### z-ai/glm-5.3

Source: https://openrouter.ai/api/v1/models/z-ai/glm-5.3/endpoints (checked 2026-10-22). Distinct providers: 37. Endpoints: 48. Model context: 1048576.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| Wafer | wafer/us | fp4 | 1048576 | 943718 | 0.079 | 1.4 | 0.078 | 100 | 0 |
| Wafer | wafer/fp4 | fp4 | 1048576 | 943718 | 0.179 | 1.4 | 0.178 | 100 | 0 |
| Inceptron | inceptron/fp4 | fp4 | 1048576 | 943718 | 0.45 | 1.96 | 0.145 | 100 | 0 |
| Novita | novita/fp8 | fp8 | 1048576 | 131072 | 0.63 | 1.98 | 0.117 | 100 | 0 |
| Sail Research | sail-research/us | fp8 | 1048576 | 943718 | 0.5 | 2 | 0.08 | 100 | 0 |
| Sail Research | sail-research/fp8 | fp8 | 1048576 | 943718 | 0.5 | 2 | 0.08 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 1048576 | 262144 | 0.7 | 2.2 | 0.13 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 1048576 | 943718 | 0.7 | 2.2 | 0.13 | 100 | 0 |
| Relace | relace | unknown | 1048576 | 131072 | 0.75 | 2.4 | 0.075 | 100 | 0 |
| DeepInfra | deepinfra/fp4 | fp4 | 1048576 | 131072 | 0.5625 | 2.5 | 0.125 | 98.1 | 0 |
| Phala | phala | unknown | 1048576 | 943718 | 0.84 | 2.64 | 0.156 | 97.5 | 0 |
| Decart | decart/fp4 | fp4 | 1048576 | 943718 | 0.84 | 2.71 | 0.19 | 100 | 0 |
| DigitalOcean | digitalocean | unknown | 1048576 | 128000 | 0.91 | 2.86 | 0.169 | 99 | 0 |
| DekaLLM | dekallm | unknown | 1048576 | 943718 | 0.18 | 2.95 | 0.15 | 99.7 | 0 |
| Fireworks | fireworks/spot | unknown | 1048576 | 943718 | 0.98 | 3.08 | 0.182 | 100 | 0 |
| Io Net | io-net/fp8 | fp8 | 262124 | 131072 | 0.49 | 3.2 | 0.15 | 100 | 0 |
| Alibaba | alibaba | unknown | 1000000 | 131072 | 1.19 | 3.74 | 0.238 | 100 | 0 |
| Friendli | friendli | unknown | 1048576 | 943718 | 1.26 | 3.96 | 0.234 | 100 | 0 |
| InferenceNet | inference-net/fp4 | fp4 | 1048576 | 943718 | 0.08 | 4 | 0.076 | 100 | 0 |
| CoreWeave | coreweave/fp8 | fp8 | 1048576 | 943718 | 1.2 | 4 | 0.19 | 95.6 | -5 |
| Reka | reka | unknown | 1048576 | 262144 | 0.14 | 4.2 | 0.105 | 100 | 0 |
| InferenceNet | inference-net/us | fp4 | 1048576 | 943718 | 0.08 | 4.381 | 0.076 | 100 | 0 |
| Baidu | baidu/fp8 | fp8 | 1048576 | 131072 | 1.3986 | 4.3956 | 0.2597 | 99.8 | 0 |
| Makora | makora/fp4 | fp4 | 1048576 | 128000 | 0.14 | 4.4 | 0.1 | 89.4 | 0 |
| AkashML | akashml/fp8 | fp8 | 1048576 | 131072 | 0.19 | 4.4 | 0.19 | 100 | 0 |
| Morph | morph/fp8 | fp8 | 1048576 | 943718 | 0.232 | 4.4 | 0.058 | 100 | 0 |
| Mistral | mistral/zdr | nvfp4 | 1048576 | 131072 | 1.4 | 4.4 | 0.14 | 99 | 0 |
| BaseTen | baseten/fp4/us | fp4 | 1048576 | 262144 | 1.4 | 4.4 | 0.14 | 99.7 | -5 |
| Mistral | mistral/nvfp4 | nvfp4 | 1048576 | 131072 | 1.4 | 4.4 | 0.14 | 99.4 | 0 |
| Nebius | nebius/fp4 | fp4 | 1024000 | 921600 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Crusoe | crusoe/fp4 | fp4 | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 99.9 | 0 |
| PrimeIntellect | primeintellect | unknown | 1048576 | 131072 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Venice | venice | unknown | 1000000 | 131072 | 1.4 | 4.4 | 0.26 | 96.2 | 0 |
| Together | together | unknown | 1048575 | 943717 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Parasail | parasail/fp8 | fp8 | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 99.7 | 0 |
| Modal | modal | unknown | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 99.7 | 0 |
| BaseTen | baseten/fp4 | fp4 | 1048576 | 262144 | 1.4 | 4.4 | 0.14 | 95.8 | -5 |
| Fireworks | fireworks | unknown | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Cloudflare | cloudflare | unknown | 1048576 | 943718 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| AtlasCloud | atlas-cloud/fp8 | fp8 | 1048576 | 131072 | 1.4 | 4.4 | 0.26 | 99.7 | 0 |
| Z.AI | z-ai/fp8 | fp8 | 1048576 | 131072 | 1.4 | 4.4 | 0.26 | 100 | 0 |
| Mistral | mistral/nvfp4/eu | nvfp4 | 1048576 | 131072 | 1.54 | 4.84 | 0.154 | 100 | 0 |
| Amazon Bedrock | amazon-bedrock/us-east-1 | unknown | 1048576 | 131072 | 1.68 | 5.28 | 0.312 | 99 | 0 |
| ModelRun | modelrun/fp4 | fp4 | 1048576 | 524288 | 2.1 | 6.6 | 0.4 | 100 | 0 |
| Fireworks | fireworks/fast | unknown | 1048576 | 943718 | 2.1 | 6.6 | 0.39 | 98.6 | 0 |
| BaseTen | baseten/us/fast | fp8 | 1048576 | 262144 | 2.1 | 6.6 | 0.21 | 99.9 | 0 |
| BaseTen | baseten/fast | fp8 | 1048576 | 262144 | 2.1 | 6.6 | 0.21 | 100 | 0 |
| Alibaba | alibaba/prime | unknown | 1000000 | 131072 | 2.8 | 8.8 | 0.56 | 100 | 0 |

### z-ai/glm-5

Source: https://openrouter.ai/api/v1/models/z-ai/glm-5/endpoints (checked 2026-10-22). Distinct providers: 8. Endpoints: 8. Model context: 204800.

| Provider | Endpoint tag | Quant | Context | Max out | In $/M | Out $/M | Cache read $/M | Uptime 1d % | Status |
|---|---|---|---|---|---|---|---|---|---|
| StreamLake | streamlake/fp8 | fp8 | 198000 | 128000 | 0.6 | 1.92 | 0.12 | 100 | 0 |
| GMICloud | gmicloud/fp8 | fp8 | 202752 | 182476 | 0.6 | 1.92 | 0.12 | 99.9 | 0 |
| Baidu | baidu/fp8 | fp8 | 202752 | 131072 | 0.7 | 2.24 | 0.14 | 100 | 0 |
| SiliconFlow | siliconflow/fp8 | fp8 | 204800 | 131072 | 0.95 | 2.55 | 0.2 | 99.8 | 0 |
| Amazon Bedrock | amazon-bedrock | unknown | 202752 | 131072 | 1 | 3.2 | n/a | 100 | 0 |
| Venice | venice/fp8 | fp8 | 198000 | 32000 | 1 | 3.2 | 0.2 | 98.9 | 0 |
| Novita | novita/fp8 | fp8 | 202800 | 131072 | 1 | 3.2 | 0.2 | 100 | 0 |
| Z.AI | z-ai/fp8 | fp8 | 202752 | 131072 | 1 | 3.2 | 0.2 | 99.7 | 0 |
