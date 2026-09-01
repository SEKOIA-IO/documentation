uuid: a81edea4-3259-4c20-b68d-0bdc923349d7
name: Nextron Valhalla Sigma Rules
type: playbook

# Nextron Valhalla Sigma Rules

![Nextron Valhalla Sigma Rules](/assets/playbooks/library/nextron-valhalla-sigma-rules.svg){ align=right width=150 }

Syncs the [Nextron Valhalla](https://valhalla.nextron-systems.com) Sigma feed into the Sekoia Rules Catalog so the rules can be used in Sekoia's detection engine.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `valhalla_api_key` | `string` | API key from valhalla.nextron-systems.com. The default is the public demo key (community feed only); a paid key unlocks the full ruleset. |
| `sekoia_api_key` | `string` | Sekoia bearer token from Settings → Workspace → API Keys. Needs the following permissions: Manage rules and alert filters, View Rules Catalog, Manage rule settings. |
| `sekoia_base_url` | `string` | Region-specific Sekoia API base URL. Default `https://api.sekoia.io` (FRA1). For FRA2/MCO1/UAE1 use `https://app.<region>.sekoia.io/api`. |

## Triggers

### Sync Valhalla Sigma rules into Sekoia Rules Catalog

Periodically pulls the Valhalla Sigma feed and POSTs each rule to the Sekoia Rules Catalog so it executes in the detection engine. POST on first seen, PUT on subsequent pulls.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Pull frequency in seconds. Default `86400` (24h), minimum `3600`. |
| `enabled` | `boolean` | When `true`, rules are pushed enabled. When `false` (default), rules land disabled and operators opt in per rule. |
| `min_sigma_level` | `string` | Minimum Sigma `level`: `informational`, `low`, `medium`, `high`, `critical`. Default `informational`. Rules missing `level` are always skipped. |
| `min_sigma_status` | `string` | Minimum Sigma `status`: `experimental`, `test`, `stable`. Default `experimental`. Rules with status `deprecated`/`unsupported` are never imported. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `created` | `integer` | Number of rules created in this run. |
| `updated` | `integer` | Number of rules updated in this run. |


## Extra

Module **`Nextron Valhalla Sigma Rules` v1.0.2**
