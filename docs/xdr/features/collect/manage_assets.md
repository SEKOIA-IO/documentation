# Manage assets

The **Assets** page lists the hosts, accounts, and networks in your inventory and lets you update them individually or in bulk. This article explains how to review and filter the inventory, apply bulk actions, and create an asset manually.

## Review the asset inventory

![Asset list](/assets/operation_center/assets_v2/assets-list.png){align="center", style="max-width:100%"}

To open the inventory, go to **Assets** in the main menu. Each row of the table represents one asset.

To narrow the list, click **Filters** and select one or more of the following criteria:

| Filter | Selects assets by |
| --- | --- |
| Criticality | Assigned criticality level. |
| Tags | Tags applied to the asset. |
| Types | Asset type: host, account, or network. |
| Source | How the asset was added to the inventory, such as manual creation or, with Reveal, automatic discovery. |
| Status | Review status: reviewed or not reviewed. |

You can combine filters. The number next to **Filters** shows how many assets match the current selection.

!!! note "Tag limits"
    An asset can have up to 100 tags. Tag values must be strings.

## Apply bulk actions

To update several assets at once, select them in the table and choose one of the following actions:

| Action | Effect |
| --- | --- |
| Add tags | Applies one or more tags to the selected assets. |
| Revoke assets | Removes the selected assets from the inventory. |
| Change criticality | Sets the same criticality on the selected assets. |
| Change status | Sets the selected assets to reviewed or not reviewed. |

!!! note
    An action on a large number of assets, such as 10,000, runs in the background. The changes appear progressively while the operation runs.

## Create an asset manually

To create an asset:

1. Go to **Assets** in the main menu.
2. Click **+ New Asset** and select the asset type.
3. Enter a name for the asset.
4. Mark the asset as reviewed if you consider it qualified.
5. For a host or an account, select a category. The category is optional.
6. Add tags to group the asset with others.
7. Add a description and the contextual properties you need.
8. Set the criticality.
9. Add the detection properties that identify the asset in your events.

The following table summarizes the fields of the asset form:

| Field | Description |
| --- | --- |
| Type | Host, account, or network. You cannot change the type after creation. |
| Name | The name displayed in the inventory and in investigations. |
| Reviewed | Marks the asset as qualified by your team. It has no impact on detection. |
| Category | The kind of host or account. Optional. Network assets have no category. See [Asset categories](/xdr/features/collect/assets.md#asset-categories). |
| Tags | Labels that group assets, for example to target them in [detection rules](/xdr/features/investigate/investigate_assets.md#use-assets-in-detections). |
| Description and contextual properties | Information that describes the asset. See [Contextual properties](/xdr/features/collect/assets.md#contextual-properties). |
| Criticality | A value from 0 to 100. See [Criticality](/xdr/features/collect/assets.md#criticality). |
| Detection properties | Values that identify the asset in events. Events are matched to the asset through these values. See [Detection properties](/xdr/features/collect/assets.md#detection-properties). |

!!! tip "Create assets automatically with Reveal"
    With the Reveal add-on module, assets can also be created from telemetry and from external systems. See [Understand passive asset discovery](/xdr/features/modules/reveal_asset_discovery.md) and [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md).

## Related articles

- [Assets](/xdr/features/collect/assets.md): Overview of asset types, categories, criticality, and asset properties.
- [Investigate assets](/xdr/features/investigate/investigate_assets.md): How to use assets in detection rules, alert filters, and investigations.
- [Synchronize assets with an Active Directory](/xdr/usecases/playbook/synchronize_asset_with_ad.md): How to create and update assets from Active Directory with a playbook.
- [Assets FAQ](/xdr/FAQ/Assets_qa.md): Reference for frequently asked questions about assets.
- [Understand passive asset discovery](/xdr/features/modules/reveal_asset_discovery.md): Overview of how Reveal creates and enriches assets from telemetry.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to configure a Reveal asset connector.
