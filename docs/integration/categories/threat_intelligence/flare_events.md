uuid: 75153d22-df06-4d8e-b18e-c5f5f287d3ac
name: Flare Events
type: intake

## Overview

Flare Events provides exposure intelligence from clear, deep and dark web sources, including chat channels, forums, marketplaces, leaks, stealer logs, and lookalike domains. The intake normalizes Flare tenant feed events into ECS for correlation and detection in SEKOIA.io.

## Architecture

- **Vendor**: Flare
- **Product URL**: [https://flare.io/](https://flare.io/)
- **Technology type**: Cloud (SaaS only)
- **On-prem version**: N/A
- **Detection approach in Sekoia.io**: Threat-oriented detections from ingested events

Flare exposes a unified tenant event feed where each event is identified by `header.type`. The connector consumes this single feed and forwards all supported subtypes to the Flare Events intake.

## Event coverage

The integration covers the full tenant feed and supports multiple subtypes, including:

- `chat_message`, `attachment`
- `forum_post`, `forum_topic`
- `listing`, `seller`
- `paste`
- `leaked_credential`, `stealer_log`
- `source_code`, `docker_image`
- `driller_profile`
- `domain`
- `blog_post`
- `bucket`, `bucket_object`
- `document` (ransomleak)
- `google`
- `service`, `social_media`
- `experimental`

Reference:

- [Flare tenant feed endpoint](https://api.docs.flare.io/api-reference/v4/endpoints/current-tenant-feed)
- [Flare event types catalog](https://api.docs.flare.io/event-types/overview)

### Focus on leaked credentials

For `leaked_credential` events, Flare data can originate from several source families (for example `stealer_logs`, `url_login_pass`, `phishing_kits_credentials`, named leaks, and `combolists`). This source context is exposed in the payload through `source_id` and `data.leak_source.*` fields.

Operationally:

- `stealer_logs` and phishing-kit credentials can include richer event linkage (`event_uid`) in Flare datasets
- named leaks include breach context (`breached_at`, `leaked_at`, `pii_tags`)
- combolists and ULP-style data are generally lower-context but still actionable for account exposure detection

## Configure

### Prerequisites

Before configuring the integration, ensure you have:

- An active Flare tenant
- A Flare API key with read access to tenant events
- Permissions in SEKOIA.io to create and manage intakes
- Outbound HTTPS access to `https://api.flare.io`

### Create Flare credentials

1. Sign in to the [Flare console](https://app.flare.io/).
2. Go to `Settings` > `API Keys`.
3. Create an API key with read scope on tenant events.
4. Copy and store the API key securely.

For details on Flare authentication and token lifecycle, see the [Flare Python SDK authentication guide](https://api.docs.flare.io/sdk/python).

### Get the optional tenant ID

If your API key is scoped to multiple tenants, you can set `tenant_id` in the connector configuration.

- In the Flare web console URL, the tenant identifier appears in the tenant context (for example in tenant-scoped paths after selecting a tenant).
- Use that numeric value as `tenant_id` in SEKOIA.io.

### How collection works

The connector uses a scheduled **PULL** model with the official `flareio` SDK.

1. It calls `POST /firework/v4/events/tenant/_search` to read event pages.
2. For each returned `items[].uid`, it fetches the full activity payload via `GET /firework/v2/activities/{uid}` (handled by `FlareApiClient.scroll_events`).
3. It forwards normalized events to the configured Sekoia.io intake.

Pagination and checkpoint behavior:

- Paging uses Flare `from` / `next` cursor semantics.
- The connector persists the latest non-null `next` cursor in checkpoint storage.
- On first run, it uses an initial lookback window (`estimated_created_at.gte`) before switching to cursor-based incremental collection.
- Empty `items` pages do not stop polling; collection ends only when `next` is null or absent.

The connector also applies client-side throttling and relies on SDK retry logic for transient API errors (including HTTP 429).

### Create your intake in SEKOIA.io

1. Go to the [Intakes page](https://app.sekoia.io/operations/intakes).
2. Click `+ Intake`.
3. Choose `Flare Events`.
4. Give the intake a name and select the target entity.
5. Configure the trigger account with:
   - `api_key` (required)
   - `tenant_id` (optional)
6. Start the trigger `Fetch new events from Flare`.

### Instruction on Sekoia

{!_shared_content/operations_center/integrations/generated/75153d22-df06-4d8e-b18e-c5f5f287d3ac_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_75153d22-df06-4d8e-b18e-c5f5f287d3ac_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/75153d22-df06-4d8e-b18e-c5f5f287d3ac.md!}
