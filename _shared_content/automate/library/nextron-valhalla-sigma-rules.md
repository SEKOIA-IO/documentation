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
| `sekoia_api_key` | `string` | Sekoia bearer token from Settings → Workspace → API Keys. Needs the following permissions: Manage rules and alert filters, View Rules Catalog. Optional: View intelligence or View intelligence with limited access, to link rules to their ATT&CK techniques. |
| `sekoia_base_url` | `string` | Region-specific Sekoia API base URL (must use `https://`). Default `https://api.sekoia.io` (FRA1). For FRA2/MCO1/UAE1 use `https://app.<region>.sekoia.io/api`. |
| `community_uuid` | `string` | Optional. Only needed when the API key has access to several communities (e.g. MSSP keys): the sync then only reads and writes rules of this community. To find the UUID, open the community in Sekoia, go to **Settings → General** and copy the part of the URL between `/communities/` and `/community-details`. |

## Triggers

### Sync Valhalla Sigma rules into Sekoia Rules Catalog

Periodically pulls the Valhalla Sigma feed and pushes each rule into the Sekoia Rules Catalog so it runs in the detection engine. New rules are created, known rules are updated in place, and a rule the user has disabled in the catalog stays disabled across syncs. Updates replace the Valhalla content (name, description, detection, severity, tags, alert type, false positives) and keep the settings made in Sekoia: entities, assets, parameters, event fields, similarity strategy, effort, validity, deprecation message, threats linked by the user and alert filters. Rules that are already up to date are not sent again.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Pull frequency in seconds. Default `86400` (24h), minimum `3600`. After a failed sync, the trigger retries after 15 and then 30 minutes (at most 2 such retries per 24h). |
| `enabled` | `boolean` | If `false` (default), newly-imported rules are disabled on first import. Existing rules keep their current catalog state. |
| `min_sigma_level` | `string` | Minimum Sigma `level`: `informational`, `low`, `medium`, `high`, `critical`. Default `medium`. Rules missing `level` are always skipped. |
| `min_sigma_status` | `string` | Minimum Sigma `status`: `experimental`, `test`, `stable`. Default `experimental`. Rules with status `deprecated`/`unsupported` are never imported; rules missing `status` are always skipped. |
| `disable_removed` | `boolean` | When `true`, disables rules that Nextron removed from the Valhalla feed, or that newly fell below your minimum level/status. The rule stays in the catalog (not deleted) and gets the tag `valhalla-auto-disabled`; if it returns to the feed later, any trigger configuration updates and re-enables it and removes the tag. Rules you disabled yourself (no tag) are left alone. Default `false` runs a dry-run — candidates are counted under `to_disable` on the summary event. The pass is skipped when the feed is empty or shrank by more than 20% (see `disable_skipped_reason`). Enable it on only one trigger per community. |
| `preserve_rule_names` | `string` | Rules listed here keep their current content: future syncs don't update them (counted under `preserved` on the summary event). One entry per line, or separate entries with `;`. An entry matches the rule's name as shown in the Sekoia Rules Catalog, or one of its tags (e.g. `uuid-<valhalla_id>`, which is unique). Match is case-sensitive; surrounding whitespace is tolerated. Default empty disables the check. Settings made in Sekoia are kept on every rule anyway; list a rule here only to keep changes to its content. The `disable_removed` pass still runs on preserved rules. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `created` | `integer` | Number of rules created in this run. |
| `updated` | `integer` | Number of rules updated in this run. |
| `unchanged` | `integer` | Number of known rules that were already up to date, so no update was sent. |
| `preserved` | `integer` | Number of rules that matched `preserve_rule_names` and were therefore not overwritten. |
| `failed` | `integer` | Number of rules the sync failed to create or update. |
| `skipped_unmapped` | `integer` | Number of rules skipped because they could not be parsed, or one or more Sigma fields could not be mapped to ECS. |
| `stale` | `integer` | Number of imported rules kept at their catalog version because the new version could not be converted. The first five names are logged. |
| `skipped_filter` | `integer` | Number of rules skipped because they did not meet the configured `min_sigma_level` / `min_sigma_status`. |
| `skipped_no_id` | `integer` | Number of feed rules skipped because they have no Valhalla `id`. |
| `total_rules` | `integer` | Total number of rules received from the Valhalla feed. |
| `top_unmapped` | `object` | Up to the five most common unmapped Sigma field names and their occurrence counts (diagnostic). |
| `server_marker_count` | `integer` | Number of catalog rules recognised by the start-of-sync catalog scan via their `uuid-*` marker tag. |
| `duplicate_markers` | `integer` | Number of catalog rules sharing the same `uuid-*` marker tag — delete the duplicates in the Sekoia UI. |
| `local_overridden` | `integer` | Number of local id-map entries overridden by the catalog scan because the server pointed somewhere else. |
| `re_enabled` | `integer` | Number of rules switched off by an earlier disable pass that came back and were enabled again. |
| `reenable_failed` | `integer` | Number of such rules the sync failed to enable again. |
| `reenable_conflicts` | `integer` | Number of rules this configuration re-enabled in its previous sync that another trigger disabled again. Run one sync trigger per community. |
| `to_disable` | `integer` | Number of still-enabled rules the disable pass identified. Set `disable_removed=true` to actually disable them. |
| `newly_disabled` | `integer` | Number of rules just disabled by this run (when `disable_removed=true`). |
| `already_disabled` | `integer` | Number of candidates that were already disabled server-side. |
| `already_gone` | `integer` | Number of candidates whose server-side rule no longer exists — the id-map entry is pruned. |
| `disable_failed` | `integer` | Number of candidates the disable pass failed to update. |
| `disable_skipped_reason` | `string` | Empty, or why the disable pass did not run: `empty_feed`, `feed_shrank`, `interrupted`. |


Each synced rule carries the tags `nextron-valhalla`, `uuid-<valhalla_id>` and `status-<sigma status>`. If you remove the `nextron-valhalla` tag, the sync still finds the rule and puts the tag back on its next update. Its payload contains the Sigma `logsource` block and the detection converted to ECS fields. The `logsource` block is informational: the detection engine only evaluates the detection, so it doesn't restrict which events a rule runs on.

Re-enabling only covers rules carrying the `valhalla-auto-disabled` tag, which the disable pass adds. If you re-enable such a rule yourself, the tag is removed, so a later manual disable stays yours.

## Extra

Module **`Nextron Valhalla Sigma Rules` v1.0.0**
