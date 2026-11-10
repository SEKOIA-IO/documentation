# Asset connectors: good practices and limits

_**[Reveal module](/xdr/features/modules/reveal_index.md)** — This feature requires the Reveal add-on module._ 

A custom asset connector is code your community writes and runs. A bug in it, such as a new asset created at every run or findings that are never closed, would fill your inventory with duplicate and stale assets, and slow down the asset pages, searches and risk scores your analysts rely on. To protect your inventory from such a connector, Sekoia limits what custom asset connectors can store. The asset connectors Sekoia provides are not subject to these limits. Every asset connector, custom or provided by Sekoia, has rate limits on how often and how much it pushes, and caps on the size of an item and on the vulnerabilities of an asset.

This article gives good practices to build a custom asset connector, lists these limits and rate limits, explains what a connector receives when it reaches one, and how it gets back under it. It also explains how a push merges with the assets your community already has, which explains duplicate or missing assets as often as the limits do.

!!! note "Default values"
    The values below are the defaults of the platform. They can change.

## Good practices

- **Build items with the models.** Build every item with the OCSF models of `sekoia-automation-models` (`DeviceOCSFModel`, `UserOCSFModel`, `SoftwareOCSFModel`, `VulnerabilityOCSFModel`, sent in an `AssetList`). The platform validates a push against the same models.
- **Normalize hostnames.** Build `hostname` and `domain` with `split_hostname()` from `sekoia-automation-models` 1.5.0 or later. It applies the same rule as the platform and returns no hostname for a value the platform would reject, so the connector can skip that device instead of pushing it.
- **Push the findings that matter.** Filter findings in the connector's code before pushing them, for instance by severity or by known exploitation, so that your inventory and the risk score of your assets reflect the vulnerabilities your analysts act on.
- **Know how a push merges.** An asset connector updates the assets your community already has: see [How a push merges with existing assets](#how-a-push-merges-with-existing-assets), which explains most duplicate or missing assets.

### How a push merges with existing assets

An asset connector does not own the assets it pushes: it updates the assets your community already has, whatever source created them.

- **Device.** A device is matched to the host asset of the community that has the same `hostname` [detection property](/xdr/features/collect/assets.md#detection-properties), regardless of letter casing. Revoked assets are never matched. A new host asset is created only when none matches, so a device merges with the asset that the Sekoia Endpoint Agent or your events already created for the same host.
- **User.** A user is matched on its email when its username is an email address, and on its username otherwise.
- **Properties.** When an item matches an asset, each property the push carries overwrites the stored value. The core properties of a device, such as its OS, IP address or MAC address, are cleared when the push leaves them empty. The interfaces, groups, partitions and accounts the push carries replace the stored ones; when the push carries none, the stored ones are kept.
- **Vulnerability finding.** A vulnerability finding is matched to a finding of the same asset whose CVEs include all the CVEs it carries. A finding without a CVE is matched on its `finding_info.uid`. Otherwise, a new finding is created.

## Rate limits on every asset connector

| Rate limit or cap | Value | Applies to | What the connector receives |
|---|---|---|---|
| Pushes | 60 per minute | Asset connector configuration | 429 `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED` |
| Items pushed, counted before validation | 200,000 per day | Asset connector configuration | 429 `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED`, with `details.limit` set to `items per day` |
| Size of one item | 900 KB | Item | 413 `ASSET_CONNECTOR_PUSH_TOO_LARGE` |
| Hostname validation | - | Item | 200 with a `rejected` field listing at most 50 of the rejected items, or 422 when every item of the push is rejected |
| Vulnerabilities per application | 1,000 | Application | Nothing: the vulnerabilities over the cap are dropped |
| Vulnerability rows per asset | 20,000 | Asset | Nothing: the new rows over the cap are dropped |

- **Hostname validation.** An item whose `device.hostname` is not a usable hostname is rejected, and so is a fully-qualified name: send the short hostname in `hostname` and the other labels in `domain`. The other items of the push are accepted.
- **Vulnerabilities per application.** This cap applies to the CVEs Sekoia matches to an application from the NVD, not to the vulnerability findings a connector pushes. Vulnerabilities known to be exploited are always kept. The others are kept by highest CVSS score.
- **Vulnerability rows per asset.** This cap applies to every vulnerability of an asset, pushed by a connector or matched from the NVD. Once an asset reaches the cap, the rows it already has are still updated and closed.

The vulnerabilities these two caps leave out are not stored, so they do not appear on the asset in Sekoia, and nothing warns that some were left out. They are still available in the tool the connector reads, or in the NVD for the CVEs of an application.

## Limits on custom asset connectors

The limits in this section apply to custom asset connectors only. The asset connectors Sekoia provides only have the rate limits and caps of the section above.

### Import

A community can own up to 10 custom integrations that contain an asset connector. Over this limit, the import fails at the **Validating integration** step.

- The limit counts integrations, not asset connectors or their configurations: an integration with several asset connectors counts once, and a community can create any number of asset connector configurations from its integrations. What these configurations store counts in the Active and Lifetime limits of the community.
- Updating an integration counts only when the update adds its first asset connector: the integration then takes a slot, and the update fails at the **Validating integration** step when the community has none left.

### Active limits

Active limits apply to what an asset connector configuration and its community have now. An asset or an application is active while an asset connector configuration has reported it within the last 30 days.

| Figure | Per asset connector configuration | Per community |
|---|---|---|
| Active assets | 25,000 | 50,000 |
| Active applications | 2,000 | 4,000 |
| Open vulnerability findings | 25,000 | 50,000 |

### Lifetime limits

Lifetime limits apply to everything the custom asset connectors of a community have stored, active or not, including the data of deleted asset connector configurations.

| Figure | Per community |
|---|---|
| Assets | 500,000 |
| Applications | 2,000,000 |
| Vulnerability findings, of any status | 1,000,000 |

### When a limit is reached

Usage is computed every 15 minutes. A push accepted before the next computation is processed in full, even if it takes the usage over a limit.

While an asset connector configuration or its community has reached any of these limits, every push of the configuration is refused with a 429 `ASSET_CONNECTOR_LIMIT_REACHED`, whatever it carries, closures included.

The `details.limits` field of the response names each reached limit by:

- `figure`: `active_assets`, `active_applications`, `open_vulnerability_findings`, `lifetime_assets`, `lifetime_applications` or `lifetime_vulnerability_findings`
- `scope`: `configuration` or `community`

The response gives neither the usage nor the remaining count.

The connector does not move its checkpoint forward on a refused push. It waits, for an hour by default, then fetches again from its last checkpoint. Once the configuration is free again, the connector pushes what the source still holds: data the source deleted while the configuration was blocked is not recovered.

### Get back under a limit

| Limit | Way out |
|---|---|
| Active assets, active applications | By itself. Nothing is reported while the configuration is blocked, so its assets and applications leave the 30-day window. The configuration can alternate between blocked and free. |
| Open vulnerability findings | Open vulnerability findings never age, and the connector cannot close them while it is blocked. Only changing the status of findings, to remediated, accepted risk or false positive, lowers the count. |
| Lifetime limits | Never by itself. Contact Sekoia support. |

## Tell a limit from a rate limit

Every 429 pauses the connector, for an hour by default, whether it comes from a limit of custom asset connectors or from a rate limit. To know which one the connector reached, [open its logs](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#step-2-open-the-connector-logs) in the asset connectors panel:

- `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED`: the connector pushed too often or too many items. It resumes by itself.
- `ASSET_CONNECTOR_LIMIT_REACHED`: a custom asset connector reached a limit. The log names the reached limits.

The logs show the error code and the reached limits from version TBD of `sekoia-automation-sdk`. A custom asset connector built with an older version logs the 429 without its code.

## Related links

- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md) — How to configure a new asset connector from the integration catalog.
- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md) — How to identify a defective connector and read its logs.
- [Integrations](/xdr/features/collect/integrations_hub.md#create-your-own-integration) — How to create and import a custom integration.
