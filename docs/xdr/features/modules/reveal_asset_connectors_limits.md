# Asset connector limits

_**[Reveal module](/xdr/features/modules/reveal_index.md)** — This feature requires the Reveal add-on module._ 

Sekoia limits what asset connectors can push, to keep asset collection fast for every community. This article lists these limits, explains what a connector receives when it reaches one, and how it gets back under it.

Some limits apply to every asset connector. Others apply to custom asset connectors only: the asset connectors of the custom integrations your community imports.

!!! note "Default values"
    The values below are the defaults of the platform. They can change.

## Limits on every asset connector

| Limit | Value | Applies to | What the connector receives |
|---|---|---|---|
| Pushes | 60 per minute | Asset connector configuration | 429 `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED` |
| Items pushed, counted before validation | 200,000 per day | Asset connector configuration | 429 `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED`, with `details.limit` set to `items per day` |
| Size of one item | 900 KB | Item | 413 `ASSET_CONNECTOR_PUSH_TOO_LARGE` |
| Hostname validation | - | Item | 200 with a `rejected` field listing at most 50 of the rejected items, or 422 when every item of the push is rejected |
| Vulnerabilities per application | 1,000 | Application | Nothing: the vulnerabilities over the limit are dropped |
| Vulnerability rows per asset | 20,000 | Asset | Nothing: the new rows over the limit are dropped |

- **Hostname validation.** An item whose `device.hostname` is not a usable hostname is rejected, and so is a fully-qualified name: send the short hostname in `hostname` and the other labels in `domain`. The other items of the push are accepted.
- **Vulnerabilities per application.** Vulnerabilities known to be exploited are always kept. The others are kept by highest CVSS score.
- **Vulnerability rows per asset.** Once an asset reaches the limit, the rows it already has are still updated and closed.

Assets also have limits on their detection properties: see [Limits on detection properties](/xdr/features/collect/assets.md#detection-properties).

## Limits on custom asset connectors

The limits in this section never apply to the asset connectors Sekoia provides.

### Import

A community can own up to 10 custom integrations that contain an asset connector. Over this limit, the import fails at the **Validating integration** step.

- An integration with several asset connectors counts once.
- Updating an integration that already contains an asset connector is never limited.

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

The connector does not save its progress on a refused push. It waits, for an hour by default, then fetches again from where it stopped: no data is lost while it is blocked.

### Get back under a limit

| Limit | Way out |
|---|---|
| Active assets, active applications | By itself. Nothing is reported while the configuration is blocked, so its assets and applications leave the 30-day window. The configuration can alternate between blocked and free. |
| Open vulnerability findings | Open vulnerability findings never age, and the connector cannot close them while it is blocked. Only changing the status of findings, to remediated, accepted risk or false positive, lowers the count. |
| Lifetime limits | Never by itself. Contact Sekoia support. |

## Tell a limit from a rate limit

Every 429 pauses the connector, for an hour by default, whether it comes from a limit or from a rate limit. To know which one the connector reached, [open its logs](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#step-2-open-the-connector-logs) in the asset connectors panel:

- `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED`: the connector pushed too often or too many items. It resumes by itself.
- `ASSET_CONNECTOR_LIMIT_REACHED`: a custom asset connector reached a limit. The log names the reached limits.

The logs show the error code and the reached limits from version TBD of `sekoia-automation-sdk`. A custom asset connector built with an older version logs the 429 without its code.

## Related links

- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md) — How to configure a new asset connector from the integration catalog.
- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md) — How to identify a defective connector and read its logs.
- [Integrations](/xdr/features/collect/integrations_hub.md#create-your-own-integration) — How to create and import a custom integration.
