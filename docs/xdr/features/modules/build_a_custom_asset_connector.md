# Build a custom asset connector

_**[Reveal module](/xdr/features/modules/reveal_index.md)** — This feature requires the Reveal add-on module._ 

This article explains how to build a custom asset connector that sends valid data and keeps your inventory free of duplicate assets. It applies to custom asset connectors only: connectors your community creates and runs.

## Before you begin

- Create the connector in a custom integration. See [Create your own integration](/xdr/features/collect/integrations_hub.md#create-your-own-integration).
- Use `sekoia-automation-models` 1.5.0 or later.
- A community can own up to 10 custom integrations with an asset connector. See [Storage limits for custom asset connectors](/xdr/features/modules/reveal_asset_connectors_limits.md#storage-limits-for-custom-asset-connectors).

## Build valid connector items

- Build every item with the OCSF models of `sekoia-automation-models`: `DeviceOCSFModel`, `UserOCSFModel`, `SoftwareOCSFModel` or `VulnerabilityOCSFModel`.
- Send the items in an `AssetList`. Sekoia validates each push against the same models.
- Build `hostname` and `domain` with `split_hostname()`. It applies the hostname rule of Sekoia.
- Skip a device when `split_hostname()` returns no hostname. Sekoia would reject it.

## Send data efficiently

- Send items in batches, not one by one. Each configuration has a rate limit on pushes per minute and a daily item quota.
- Keep each item under the item-size limit.
- Filter findings in the connector code before sending them, for instance by severity or known exploitation.

The values are in [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md).

## Keep findings up to date

- Send a finding with the Close activity when the source reports it fixed. Its status becomes remediated.
- Send it again without Close if it comes back. Its status becomes open.

A push never changes a status a user set, such as accepted risk or false positive.

## Understand how pushed data is matched

A custom asset connector updates the assets your community already has, whatever source created them.

| Item | Matched to | When nothing matches |
|---|---|---|
| Device | The host asset with the same `hostname` [detection property](/xdr/features/collect/assets.md#detection-properties), regardless of case. Revoked assets are excluded. | A new host asset is created. |
| User | The account asset with the same email when the username is an email address, or the same username otherwise. | A new account asset is created. |
| Vulnerability finding | The finding of the same asset whose CVEs include all the CVEs it carries, or with the same `finding_info.uid` when it has no CVE. | A new finding is created. |

When an item matches an asset:

- Each property the item carries overwrites the stored value.
- Empty core properties of a device, such as OS, IP address or MAC address, clear the stored value.
- Interfaces, groups, partitions and accounts the item carries replace the stored ones. When the item carries none, the stored ones are kept.

## Plan for custom connector storage limits

Each configuration and each community can store a limited number of active assets, active applications and open findings. The limits follow the number of assets your community subscribed.

- Close fixed findings, so that open findings stay under their limit.
- Send each machine and account with the same hostname or username at every run, so that it updates one asset instead of creating new ones.

When a configuration reaches a storage limit, every push of the configuration receives a 429 `ASSET_CONNECTOR_LIMIT_REACHED`. See [Storage limits for custom asset connectors](/xdr/features/modules/reveal_asset_connectors_limits.md#storage-limits-for-custom-asset-connectors).

## Related articles

- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#diagnose-push-errors): Push errors and the action for each.
- [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md): Rate limits, caps and storage limits.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to configure an asset connector from the integration catalog.
