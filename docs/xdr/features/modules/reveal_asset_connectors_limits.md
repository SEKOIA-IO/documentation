# Custom asset connectors

_**[Reveal module](/xdr/features/modules/reveal_index.md)** — This feature requires the Reveal add-on module._ 

A custom asset connector is code your community writes and runs. A connector built well keeps your inventory accurate: one asset per machine or account, findings closed when they are fixed, and asset pages, searches and risk scores your analysts can rely on. This article gives the good practices to build such a connector, explains each error a push can receive and what to do about it, and how much a custom asset connector can store.

!!! note "Default values"
    The values on this page are the defaults of the platform. They can change.

## Good practices

- **Build items with the models.** Build every item with the OCSF models of `sekoia-automation-models` (`DeviceOCSFModel`, `UserOCSFModel`, `SoftwareOCSFModel`, `VulnerabilityOCSFModel`, sent in an `AssetList`). The platform validates a push against the same models.
- **Normalize hostnames.** Build `hostname` and `domain` with `split_hostname()` from `sekoia-automation-models` 1.5.0 or later. It applies the same rule as the platform and returns no hostname for a value the platform would reject, so the connector can skip that device instead of pushing it.
- **Push in batches.** Each asset connector configuration can push up to 60 times per minute and 200,000 items per day. Send items in batches rather than one by one, and keep each item under 900 KB.
- **Push the findings that matter.** Filter findings in the connector's code before pushing them, for instance by severity or by known exploitation, so that your inventory and the risk score of your assets reflect the vulnerabilities your analysts act on.
- **Close the findings that are fixed.** Push a finding with the Close activity once the source reports it fixed: its status becomes remediated. Pushing it again without Close reopens it. A status a user set, accepted risk or false positive, is never changed by a push.
- **Know how a push merges.** An asset connector updates the assets your community already has: see [How a push merges with existing assets](#how-a-push-merges-with-existing-assets), which explains most duplicate or missing assets.

### How a push merges with existing assets

An asset connector does not own the assets it pushes: it updates the assets your community already has, whatever source created them.

- **Device.** A device is matched to the host asset of the community that has the same `hostname` [detection property](/xdr/features/collect/assets.md#detection-properties), regardless of letter casing. Revoked assets are never matched. A new host asset is created only when none matches, so a device merges with the asset that the Sekoia Endpoint Agent or your events already created for the same host.
- **User.** A user is matched on its email when its username is an email address, and on its username otherwise.
- **Properties.** When an item matches an asset, each property the push carries overwrites the stored value. The core properties of a device, such as its OS, IP address or MAC address, are cleared when the push leaves them empty. The interfaces, groups, partitions and accounts the push carries replace the stored ones; when the push carries none, the stored ones are kept.
- **Vulnerability finding.** A vulnerability finding is matched to a finding of the same asset whose CVEs include all the CVEs it carries. A finding without a CVE is matched on its `finding_info.uid`. Otherwise, a new finding is created.

## Push errors

To see the errors of a connector, [open its logs](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#step-2-open-the-connector-logs) in the asset connectors panel. Each error shows its code.

| Response | Code | Cause | What to do |
|---|---|---|---|
| 200, with a `rejected` field | - | Some items have a `device.hostname` that is not a usable hostname, or that is a fully-qualified name. The other items are accepted. The `rejected` field lists at most 50 of the rejected items, with their index, field, value and reason. | Build `hostname` and `domain` with `split_hostname()`, and skip the devices it returns no hostname for. |
| 422 | - | Every item of the push was rejected, for the reasons above. | Same as above. |
| 403 | `INSUFFICIENT_PERMISSIONS` | The API key of the connector is not allowed to push assets to the community of the asset connector configuration. | Use an API key of that community with the permission to push assets. |
| 404 | `ASSET_CONNECTOR_NOT_FOUND` | The asset connector configuration was deleted, or the connector pushes with the UUID of a configuration that does not exist. | Check the configuration the connector runs for. |
| 413 | `ASSET_CONNECTOR_PUSH_TOO_LARGE` | An item is larger than 900 KB. | Make the item smaller, for instance by sending fewer interfaces, groups or accounts. |
| 429 | `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED` | The asset connector configuration pushed more than 60 times in a minute, or more than 200,000 items in a day. In the second case, `details.limit` is set to `items per day`. Items are counted before validation. | Push larger batches less often. The connector resumes by itself. |
| 429 | `ASSET_CONNECTOR_LIMIT_REACHED` | The custom asset connector configuration, or its community, stores as much as your subscription allows. `details.limits` names each reached figure. | See [How much a custom asset connector can store](#how-much-a-custom-asset-connector-can-store). |
| 503 | `ASSET_CONNECTOR_PUSH_UNAVAILABLE` | Sekoia could not confirm the delivery of the push. Some of its items may have been accepted. | Push the items again: they are matched to the assets already created, as [a push merges](#how-a-push-merges-with-existing-assets). |

After a 429, the connector does not move its checkpoint forward. It waits, for an hour by default, then fetches again from its last checkpoint. Once it can push again, it pushes what the source still holds: data the source deleted in the meantime is not recovered. After any other error, the connector logs it and goes on with the next batch.

The logs show the code of a 429, and the figures reached, from version TBD of `sekoia-automation-sdk`. A custom asset connector built with an older version logs a 429 without its code.

The asset connectors Sekoia provides can receive the same errors, except `ASSET_CONNECTOR_LIMIT_REACHED`.

## How much a custom asset connector can store

A custom asset connector with a bug, such as a new asset created at every run or findings never closed, would fill your inventory with duplicate and stale assets. To protect your inventory, what custom asset connectors can store follows your subscription: each figure is the number of assets your community subscribed, times a ratio. A community whose number of assets Sekoia does not know counts as 1,000 assets. The asset connectors Sekoia provides are not concerned.

### Integrations with an asset connector

A community can own up to 10 custom integrations that contain an asset connector. Over this number, the import fails at the **Validating integration** step.

- The number counts integrations, not asset connectors or their configurations: an integration with several asset connectors counts once, and a community can create any number of asset connector configurations from its integrations. What these configurations store counts in the active and lifetime figures of the community.
- Updating an integration counts only when the update adds its first asset connector: the integration then takes a slot, and the update fails at the **Validating integration** step when the community has none left.

### Active figures

An asset or an application is active while an asset connector configuration has reported it within the last 30 days.

| Figure | Per asset connector configuration | Per community |
|---|---|---|
| Active assets | 5 × subscribed assets | 10 × subscribed assets |
| Active applications | 25 × subscribed assets | 50 × subscribed assets |
| Open vulnerability findings | 50 × subscribed assets | 100 × subscribed assets |

For instance, a community subscribed to 2,000 assets can have 10,000 active assets per asset connector configuration, and 20,000 in the community.

### Lifetime figures

Lifetime figures count everything the custom asset connectors of a community have stored, active or not, including the data of deleted asset connector configurations.

| Figure | Per community |
|---|---|
| Assets | 15 × subscribed assets |
| Applications | 300 × subscribed assets |
| Vulnerability findings, of any status | 200 × subscribed assets |

### When a figure is reached

Usage is computed every 15 minutes. A push accepted before the next computation is processed in full, even if it takes the usage over a figure.

While an asset connector configuration or its community has reached any of these figures, every push of the configuration receives a 429 `ASSET_CONNECTOR_LIMIT_REACHED`, whatever it carries, closures included. The `details.limits` field of the response names each reached figure by:

- `figure`: `active_assets`, `active_applications`, `open_vulnerability_findings`, `lifetime_assets`, `lifetime_applications` or `lifetime_vulnerability_findings`
- `scope`: `configuration` or `community`

The response gives neither the usage nor the remaining count.

| Figure reached | How the configuration pushes again |
|---|---|
| Active assets, active applications | By itself. Nothing is reported while the configuration is blocked, so its assets and applications leave the 30-day window. The configuration can alternate between blocked and free. |
| Open vulnerability findings | Open vulnerability findings never age, and the connector cannot close them while it is blocked. Only changing the status of findings, to remediated, accepted risk or false positive, lowers the count. |
| Lifetime figures | Lifetime figures do not decrease. |

## Vulnerabilities kept on an asset

These caps apply to every asset connector. Nothing is returned to the connector when they apply.

- **Vulnerabilities per application: 1,000.** This cap applies to the CVEs Sekoia matches to an application from the NVD, not to the vulnerability findings a connector pushes. Vulnerabilities known to be exploited are always kept. The others are kept by highest CVSS score.
- **Vulnerabilities per asset: 20,000.** This cap applies to every vulnerability of an asset, pushed by a connector or matched from the NVD. Once an asset reaches the cap, the vulnerabilities it already has are still updated and closed.

The vulnerabilities these two caps leave out are not stored, so they do not appear on the asset in Sekoia, and nothing warns that some were left out. They are still available in the tool the connector reads, or in the NVD for the CVEs of an application.

## Related links

- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md) — How to configure a new asset connector from the integration catalog.
- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md) — How to identify a defective connector and read its logs.
- [Integrations](/xdr/features/collect/integrations_hub.md#create-your-own-integration) — How to create and import a custom integration.
