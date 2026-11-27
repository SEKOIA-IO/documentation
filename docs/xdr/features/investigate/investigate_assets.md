# Investigate assets

Asset fields let you scope detection rules and alert filters to groups of assets, and the asset investigation view shows the activity around an asset. This article explains how to use asset fields in detection patterns and how to review an asset's authentications and pivot to related assets.

## Use assets in detections

You can write detection rules and alert filters that apply only to specific assets, such as critical servers, or that exclude some assets, such as administrator accounts. To do so, reference the asset fields that Sekoia adds to events that match an asset.

| Field | Type | Example |
| --- | --- | --- |
| `sekoiaio.any_asset.tags` | Set of strings | `{"VIP", "critical", "internal"}` |
| `sekoiaio.any_asset.uuid` | Set of strings | `{NETWORK_UUID, ENTITYLESS_HOST, USER_UUID, ENTITYSPECIFIC_HOST}` |
| `sekoiaio.any_asset.name` | Set of strings | `"My asset"` |
| `sekoiaio.any_asset.criticality_display` | Set of strings | `{"high", "low"}` |
| `sekoiaio.any_asset.criticality_value` | Set of integers | `{80, 0}` |

!!! warning "Fields available in event search"
    Sekoia removes some asset fields from events before indexing them. All the fields above work in detection rules and alert filters, but indexed events only contain `sekoiaio.any_asset.uuid`, `sekoiaio.any_asset.name`, `sekoiaio.any_asset.criticality_value`, and `sekoiaio.assets.*.uuid`.

    You cannot search `sekoiaio.any_asset.tags` in events. To work on tagged assets, use a detection rule, an alert filter, or a [SOL query](/xdr/features/investigate/sol_query_examples.md#search-the-events-of-assets-with-a-specific-tag) that reads tags from the `assets` data source.

Tags are the most flexible way to group assets. You can add them manually, with a [bulk action](/xdr/features/collect/manage_assets.md#apply-bulk-actions), or through the API.

### Target assets with a detection rule

The following Sigma pattern matches event code 4720 only on assets tagged `my_custom_tag_for_critical_servers`:

```yaml
detection:
  selection:
    event.code: 4720
    sekoiaio.any_asset.tags: "my_custom_tag_for_critical_servers"

  condition: selection
```

### Exclude assets with an alert filter

The following Sigma pattern matches events on assets tagged `my_custom_tag_for_admin_assets`. Use it in an alert filter to stop raising alerts for those assets:

```yaml
detection:
  selection:
    sekoiaio.any_asset.tags: "my_custom_tag_for_admin_assets"

  condition: selection
```

!!! tip
    You do not need the `contains` modifier for tags. Because `sekoiaio.any_asset.tags` is a list, `sekoiaio.any_asset.tags: mytag` already matches when any of the asset's tags is `mytag`.

## Investigate asset activity

The asset investigation view shows an asset's history and a selection of past activities. Use it to spot unusual behavior and to follow the relationships between hosts and accounts.

### Review authentications

The authentication view lists the authentications that involve the asset.

![Asset authentications](/assets/operation_center/assets_v2/asset_authentications.png){: style="max-width:100%"}

Each authentication shows the following properties:

| Property | Description |
| --- | --- |
| Time of first occurrence | When the authentication was first recorded. |
| Number of occurrences | How many times the authentication occurred. |
| Source host | The host that the attempt came from. |
| Target host | The host that the attempt targeted. |
| Source account | The account that initiated the attempt. |
| Target account | The account that the attempt targeted. |
| Service/Process | The service or process involved. |
| Authentication status | The result of the attempt, such as success or failure. |

The view also shows the trend of the top 10 target accounts and the top 5 source hosts for the asset.

### Pivot to related assets

Click a source host, target host, source account, or target account in the authentication view to open the details of that asset.

![Asset authentication pivot](/assets/operation_center/assets_v2/asset_auth_pivot.png){: style="max-width:100%"}

| Pivot | What you can review |
| --- | --- |
| Source host | The host's activity history and the other assets or accounts it interacted with. |
| Target host | The activities involving the host, its past incidents, and its relationships with other assets or accounts. |
| Source account | The account's activity across assets, its authentication attempts, and the incidents involving it. |
| Target account | The account's interaction history, the incidents involving it, and its access permissions and recent changes. |

## Related articles

- [Assets](/xdr/features/collect/assets.md): Overview of asset types, categories, criticality, and asset properties.
- [Manage assets](/xdr/features/collect/manage_assets.md): How to review the asset inventory, apply bulk actions, and create assets manually.
- [Asset context panel](/xdr/features/investigate/asset_context_panel.md): How to open and use the asset context panel during an investigation.
- [SOL query examples](/xdr/features/investigate/sol_query_examples.md): Reference for SOL queries, including queries on assets and their events.
- [Sigma](/xdr/features/detect/sigma.md): Overview of Sigma detection patterns in the Sekoia SOC platform.
