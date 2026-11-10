# LocateRisk

LocateRisk is a specialist for automated IT risk analysis and monitoring. This module integrates Sekoia.io with the LocateRisk platform to ingest vulnerability findings from LocateRisk scan report exports.

## Configuration

| Name       | Type     | Description                                                                         |
| ---------- | -------- | ----------------------------------------------------------------------------------- |
| `api_key`  | `string` | LocateRisk API key used to authenticate to the LocateRisk API                      |
| `base_url` | `string` | Base URL of the LocateRisk platform. Default: `https://app.locaterisk.com/` (HTTPS required) |

## Connectors

### LocateRisk Scan Report

Collect findings from a LocateRisk scan report export.

The connector polls the CSV report at `<report_url>/<scan_id>/csv`, parses semicolon-delimited rows (including quoted multi-line values such as CVE lists), enriches each event with `source=locaterisk`, and forwards the result to Sekoia.io.

To reduce duplicates, the connector stores row hashes from the previous successful poll and only forwards new or changed rows on the next cycle.

**Arguments**

Required arguments: `intake_key`, `scan_id`

| Name               | Type      | Description                                                                                   |
| ------------------ | --------- | --------------------------------------------------------------------------------------------- |
| `intake_server`    | `string`  | Server of the intake server (e.g. `https://intake.sekoia.io`). Default: `https://intake.sekoia.io` |
| `intake_key`       | `string`  | Intake key used to send events to Sekoia.io                                                   |
| `scan_id`          | `string`  | Identifier of the LocateRisk scan to export                                                   |
| `report_url`       | `string`  | LocateRisk report export endpoint base URL. Default: `https://app.locaterisk.com/api/rest/report/export` |
| `polling_interval` | `integer` | Polling interval in minutes. Default: `5`                                                     |

## Extra

Module **`LocateRisk` v0.6.0**
