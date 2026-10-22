# Privacy Policy

**DRAFT for attorney review. Not yet in force.**
Radiant Machines ("we", "us"), a sole proprietorship in Redwood City, California.
Effective date: [DATE]. Contact: privacy@[DOMAIN].

This policy covers the Radiant Machines inference API (the "Service") at api.[DOMAIN], including requests routed to us by marketplaces such as OpenRouter. It is written to satisfy OpenRouter's provider requirements (a published policy that states whether prompts are logged and whether data is used for training), the California Online Privacy Protection Act, and the disclosures a business customer needs to run its own privacy program.

## 1. What we do with your prompts and outputs

- **We do not store prompt content or model output.** Requests are processed in memory on our GPU servers and discarded when the response is complete. We keep no copies, no samples and no backups of request or response bodies.
- **We do not train on your data.** We never use prompts, outputs or embeddings to train, fine-tune, evaluate or improve any model.
- **Zero data retention is the default** for every request, not an option you must select.
- Model weights we serve are published open-weight models; their outputs are generated on our infrastructure and are not sent to the model's original developer.

## 2. What we do record

For billing, abuse prevention and service health we keep per-request metadata only:

| Field | Why | Retention |
|---|---|---|
| API key identifier (never the key itself; keys are stored as hashes) | billing, abuse | 13 months after the key is revoked |
| Timestamp, model name, request id | billing, debugging | 13 months |
| Prompt token count, cached token count, completion token count, reasoning token count | billing | 13 months |
| Latency, HTTP status, whether the response was streamed | service health | 13 months |
| Source IP address and user agent in web server access logs | abuse prevention, security | 30 days |

We do not record message text, system prompts, tool definitions, tool outputs, images or files.

## 3. Account data

If you buy access directly from us we collect the data needed to bill you: name, email, company, and the billing details you give to our payment processor, Stripe. Stripe stores card details; we never see full card numbers. If you reach us through a marketplace (for example OpenRouter), the marketplace holds your account data and we receive only the request.

## 4. Sub-processors

| Sub-processor | Purpose | Location |
|---|---|---|
| GPU cloud provider(s) named on our status page (for example Vultr, Koyeb) | hosting the inference servers | United States |
| Stripe | payments and invoicing | United States |
| OpenRouter (when you reach us through it) | routing and billing of marketplace requests | United States |

GPU providers can see traffic at the network level but not decrypted request bodies; traffic to our gateway is encrypted with TLS and traffic between the gateway and the model servers stays inside a private network on the same host or node.

## 5. Security

TLS for all external connections; API keys stored only as SHA-256 hashes; least-privilege access to servers; no persistent storage of request bodies, so a breach of our systems would expose metadata only. We will notify affected customers without undue delay if we learn of a breach involving their data.

## 6. Your rights

California residents have rights under the CCPA/CPRA to know, delete and correct personal information and to opt out of sale or sharing. We do not sell or share personal information, and we hold no prompt content to delete. To exercise rights or ask questions, email privacy@[DOMAIN]. We respond within 45 days. We do not discriminate against anyone who exercises these rights.

Note for the attorney: the business is currently below the CCPA applicability thresholds ($26.6 million annual revenue, 100,000 consumers, or 50% of revenue from selling data); this section is included so that it is already in place if that changes and because CalOPPA requires a posted policy regardless.

## 7. Children

The Service is for businesses and adult developers. We do not knowingly process data from children under 13 and do not offer consumer accounts.

## 8. Law enforcement

We disclose data only when legally required. Because we hold no prompt content, we cannot produce it.

## 9. Changes

We will post changes here with a new effective date and notify direct customers by email at least 14 days before material changes take effect.
