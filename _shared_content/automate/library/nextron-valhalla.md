uuid: a81edea4-3259-4c20-b68d-0bdc923349d7
name: Nextron Valhalla
type: playbook

# Nextron Valhalla

![Nextron Valhalla](/assets/playbooks/library/nextron-valhalla.svg){ align=right width=150 }

Nextron Valhalla integration for Sekoia

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `valhalla_api_key` | `string` | API key from valhalla.nextron-systems.com. The default is the public demo key, which only grants the community feed. Stored as a secret: masked once the account is saved. |
| `sekoia_api_key` | `string` | Bearer token from Sekoia (Settings → Workspace → API Keys). Used to push rules into the Sekoia Rules Catalog. Stored as a secret: masked once the account is saved. |
| `sekoia_base_url` | `string` | Region-specific base URL. Default https://api.sekoia.io covers FRA1. For FRA2/MCO1/UAE1 use https://app.<region>.sekoia.io/api. |
| `community_uuid` | `string` | Optional. Only needed when the API key has access to several communities (e.g. MSSP keys): the sync then only reads and writes rules of this community. To find the UUID, open the community in Sekoia, go to Settings > General and copy the part of the URL between /communities/ and /community-details. |

## Triggers

### Sync Valhalla Sigma rules into Sekoia Rules Catalog

Periodically pulls the Valhalla Sigma feed and pushes each rule into the Sekoia Rules Catalog so it runs in the detection engine. New rules are created, known rules are updated in place, and a rule the user has disabled in the catalog stays disabled across syncs.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` |  |
| `enabled` | `boolean` | If false (default), newly-imported rules are disabled on first import. Existing rules keep their current catalog state. |
| `min_sigma_level` | `string` | Only rules with a Sigma `level` at least this severe are imported. Rules missing the `level` field are always skipped. |
| `min_sigma_status` | `string` | Only rules with a Sigma `status` at least this mature are imported (ordering: experimental < test < stable). Rules with status `deprecated` or `unsupported` are never imported. Rules missing the `status` field are always skipped. |
| `disable_removed` | `boolean` | Disables rules that Nextron removed from the Valhalla feed, or that newly fell below your minimum level/status. The rule stays in the catalog (not deleted) and gets the tag `valhalla-auto-disabled`; if it returns to the feed later, any trigger configuration of this integration updates and re-enables it and removes the tag. Rules you disabled yourself (no tag) are left alone. Default false runs a dry-run — candidates are counted under `to_disable` on the summary event. Set true to actually disable. The pass is skipped when the feed is empty or shrank by more than 20% (see `disable_skipped_reason`). Enable it on only one trigger per community. |
| `preserve_rule_names` | `string` | Rules listed here keep their current content: future syncs don't update them (counted under `preserved` on the summary event). One entry per line, or separate entries with `;`. An entry matches the rule's name as shown in the Sekoia Rules Catalog, or one of its tags (e.g. `uuid-<valhalla_id>`, which is unique). Match is case-sensitive; surrounding whitespace is tolerated. Leave empty (default) to disable. Settings such as entities, assets, parameters, event fields and similarity strategy are kept on every rule anyway; list a rule here only to keep changes to its content (name, description, detection, severity, tags). The `disable_removed` pass still runs on preserved rules. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `created` | `integer` |  |
| `updated` | `integer` |  |
| `unchanged` | `integer` |  |
| `preserved` | `integer` |  |
| `failed` | `integer` |  |
| `skipped_unmapped` | `integer` |  |
| `stale` | `integer` |  |
| `skipped_filter` | `integer` |  |
| `skipped_no_id` | `integer` |  |
| `total_rules` | `integer` |  |
| `top_unmapped` | `object` |  |
| `server_marker_count` | `integer` |  |
| `duplicate_markers` | `integer` |  |
| `local_overridden` | `integer` |  |
| `re_enabled` | `integer` |  |
| `reenable_failed` | `integer` |  |
| `reenable_conflicts` | `integer` |  |
| `to_disable` | `integer` |  |
| `newly_disabled` | `integer` |  |
| `already_disabled` | `integer` |  |
| `already_gone` | `integer` |  |
| `disable_failed` | `integer` |  |
| `disable_skipped_reason` | `string` |  |


## Extra

Module **`Nextron Valhalla` v1.0.0**