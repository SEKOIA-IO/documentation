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

Periodically pulls the Valhalla Sigma feed and pushes each rule into the Sekoia Rules Catalog so it runs in the detection engine. New rules are created, known rules are updated in place, and a rule the user has disabled in the catalog stays disabled across syncs.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Pull frequency in seconds. Default `86400` (24h), minimum `3600`. |
| `enabled` | `boolean` | If `false` (default), newly-imported rules are disabled on first import. Existing rules keep their current catalog state. |
| `min_sigma_level` | `string` | Minimum Sigma `level`: `informational`, `low`, `medium`, `high`, `critical`. Default `medium`. Rules missing `level` are always skipped. |
| `min_sigma_status` | `string` | Minimum Sigma `status`: `experimental`, `test`, `stable`. Default `stable`. Rules with status `deprecated`/`unsupported` are never imported. |
| `disable_removed` | `boolean` | When `true`, disables rules that Nextron removed from the Valhalla feed, or that newly fell below your minimum level/status. The rule stays in the catalog (not deleted); if Nextron re-publishes it later, the sync resumes updating it. Default `false` runs a dry-run — candidates are counted under `to_disable` on the summary event. |
| `preserve_rule_names` | `array` | List of exact rule names copied from the Sekoia Rules Catalog UI whose contents are no longer overwritten by future syncs (counted under `preserved` on the summary event). Match is case-sensitive; surrounding whitespace is tolerated. Default `[]` disables the check. The `disable_removed` pass still runs on preserved rules — only the content is protected. To delete entries from the list, create a new trigger configuration. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `created` | `integer` | Number of rules created in this run. |
| `updated` | `integer` | Number of rules updated in this run. |
| `preserved` | `integer` | Number of rules whose name matched `preserve_rule_names` and were therefore not overwritten. |
| `failed` | `integer` | Number of rules the sync failed to create or update. |
| `skipped_unmapped` | `integer` | Number of rules skipped because one or more Sigma fields could not be mapped to ECS. |
| `skipped_filter` | `integer` | Number of rules skipped because they did not meet the configured `min_sigma_level` / `min_sigma_status`. |
| `total_rules` | `integer` | Total number of rules received from the Valhalla feed. |
| `top_unmapped` | `object` | Up to the five most common unmapped Sigma field names and their occurrence counts (diagnostic). |
| `server_marker_count` | `integer` | Number of catalog rules recognised by the start-of-sync catalog scan via their `uuid-*` marker tag. |
| `duplicate_markers` | `integer` | Number of catalog rules sharing the same `uuid-*` marker tag — delete the duplicates in the Sekoia UI. |
| `local_overridden` | `integer` | Number of local id-map entries overridden by the catalog scan because the server pointed somewhere else. |
| `to_disable` | `integer` | Number of candidates the `disable_removed` dry-run identified. Set `disable_removed=true` to actually disable them. |
| `newly_disabled` | `integer` | Number of rules just disabled by this run (when `disable_removed=true`). |
| `already_disabled` | `integer` | Number of candidates that were already disabled server-side. |
| `already_gone` | `integer` | Number of candidates whose server-side rule no longer exists — the id-map entry is pruned. |
| `disable_failed` | `integer` | Number of candidates the disable pass failed to update. |


## Extra

Module **`Nextron Valhalla Sigma Rules` v1.1.0**
