uuid: 9466f885-adf6-496a-b971-ed4bf1006fc8
name: Palo Alto Cortex XDR Issues (API v5)
type: intake

## Overview

Palo Alto Cortex XDR Issues (API v5) collects Cortex issues/cases and forwards them to Sekoia.io.

This integration is dedicated to the issues model and does not replace the historical alerts connector.

- Historical alerts connector: [Palo Alto Cortex XDR (EDR)](/integration/categories/endpoint/paloalto_cortex_edr.md) (`/public_api/v1/alerts/get_alerts_multi_events`)
- This connector: issues/cases (`/public_api/v1/issue/search`)

- **Vendor**: Palo Alto
- **Supported environment**: Cloud
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: Cortex XDR Issues APIs

## Before you begin

From Palo Alto Cortex XDR documentation:

- The issues APIs require a **Cortex XDR** license.
- API calls use the headers:
    - `Authorization: <api_key>`
    - `x-xdr-auth-id: <api_key_id>`
- API keys are created with a selected security level (**Standard** or **Advanced**) and an assigned role.

Use an API key role that can read issues in your tenant. If the role is too restrictive, the connector can receive `403` responses.

## Create API key credentials

1. In Cortex XDR, navigate to **Settings** > **Configurations** > **Integrations** > **API Keys** > **New Key**.
2. Under **Security Level**, select the API key type (**Standard** or **Advanced**).
3. Under **Role**, select a role that can read issues/cases data.
4. Generate the key and copy:
    - the API key value (`api_key`)
    - the API key ID (`api_key_id`)
5. Copy your tenant API URL/FQDN from the API Keys page (**Copy API URL**).

## Configure in Sekoia.io

### Create the intake

1. Go to the [Intake page](https://app.sekoia.io/operations/intakes) and create a `Palo Alto Cortex XDR Issues (API v5)` intake.
2. Create or select a Palo Alto account with:
    - `api_key` (required, secret)
    - `api_key_id` (required, secret)
    - `fqdn` (required)
3. Select the connector `Fetch Issues from Cortex [API v5]` (`cortex_query_issues`).
4. Configure connector arguments:
    - `frequency` (required, default `60` seconds)
    - `chunk_size` (default `100`)
    - `intake_key` (required)
    - `intake_server` (default `https://intake.sekoia.io`)

!!! warning
    `chunk_size` is not a strict upper bound for one fetch cycle.
    The runtime pagination uses `max(chunk_size, 100)`.

## Collection behavior

The connector uses:

- `POST /public_api/v1/issue/search` (Cortex Issues API)

Even though this integration is named “API v5”, the request path is `/public_api/v1/issue/search` (not `/public_api/v5`).

### FQDN normalization

The connector accepts and normalizes:

- `example.com`
- `api-example.com`
- an HTTPS URL
- an URL already ending with `/public_api/v1/issue/search`

It also rewrites the historical alerts path (`/public_api/v1/alerts/get_alerts_multi_events`) to the issues path.

### Query strategy and pagination

Each polling cycle:

- filters on `modification_time` with operator `gte`
- sorts by `modification_time` in descending order
- paginates with `search_from` / `search_to`
- reads issues from `reply.issues`
- forwards each issue as raw JSON

### Cursor, deduplication, and retransmission

- Initial cursor starts **5 minutes before** the first run.
- A saved cursor older than **7 days** is clamped to the 7-day limit.
- Deduplication key is `issue_id + modification_time`.
- `modification_time` is a Unix timestamp in milliseconds.
- Issues without `issue_id` are ignored.
- Issues with `is_excluded=true` are **not** filtered out by the connector.

!!! info
    This behavior helps continuity but does not guarantee full historical backfill.
    A same issue can be retransmitted when its `modification_time` changes.

## Error handling

- `401 Unauthorized`: invalid `api_key` or `api_key_id`.
- `403 Forbidden`: API key role/permissions are insufficient for the issues API.
- Temporary connectivity/API errors: the connector retries on the next scheduled polling cycle.

## Minimal test sample

The following fixture is a minimal test example used for connector validation:

```json
{
  "issue_id": "5930923",
  "severity": "MEDIUM",
  "modification_time": 1705912900118,
  "is_excluded": false
}
```

## Format and generated references

The Cortex XDR Issues intake format reference is not yet available in this repository as a dedicated generated page/identifier.
Until it is published, this page intentionally does not add generated sample/event-reference includes for that format.

## Further readings

- [Get started with Cortex XDR 5.x APIs](https://cortex-docs.paloaltonetworks.com/xdr-5-api/readme.md)
- [Create a new API key](https://cortex-docs.paloaltonetworks.com/xdr-5-api/create-a-new-api-key.md)
- [Get your Cortex XDR API key ID](https://cortex-docs.paloaltonetworks.com/xdr-5-api/get-your-cortex-api-key-id.md)
- [Get your FQDN](https://cortex-docs.paloaltonetworks.com/xdr-5-api/get-your-fqdn.md)
- [Cortex XDR Issues API](https://cortex-docs.paloaltonetworks.com/xdr-5-api/issues-apis/issues.md)
