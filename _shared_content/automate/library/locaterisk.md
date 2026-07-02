# LocateRisk

LocateRisk is a specialist for automated IT risk analysis and monitoring. This module integrates Sekoia.io with the LocateRisk platform to ingest vulnerability findings from a LocateRisk scan report.

## Configuration

| Name         | Type     | Description                                                                                                        |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------ |
| `api_key`    | `string` | LocateRisk API key used to authenticate against the report export endpoint                                         |
| `scan_id`    | `string` | Identifier of the LocateRisk scan whose findings should be exported                                                |
| `report_url` | `string` | Base URL of the LocateRisk report export endpoint. Defaults to `https://app.locaterisk.com/api/rest/report/export` |

## Connectors

### LocateRisk Scan Report

Collect findings from a LocateRisk scan report export.

The connector periodically pulls the CSV report at `<report_url>/<scan_id>/csv`, parses the rows (including multi-line fields such as CVE lists) and pushes each finding to Sekoia.io as a structured event.

**Arguments**

| Name               | Type      | Description                                                                                   |
| ------------------ | --------- | --------------------------------------------------------------------------------------------- |
| `intake_server`    | `string`  | Sekoia.io intake server URL (e.g. `https://intake.sekoia.io`). Defaults to the platform value |
| `intake_key`       | `string`  | Intake key to use when sending events                                                         |
| `polling_interval` | `integer` | Polling interval in minutes. Defaults to `5`                                                  |

## Extra

Module **`LocateRisk` v0.1.9**
