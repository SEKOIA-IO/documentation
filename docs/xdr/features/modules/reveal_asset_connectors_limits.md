# Asset connector limits

_**[Reveal module](/xdr/features/modules/reveal_index.md)** — This feature requires the Reveal add-on module._ 

This article lists the limits that apply to asset connectors and what happens when a connector reaches one. Use it to check which limits apply to your connector.

!!! note "Scope"
    Rate limits, item-size limits and vulnerability caps apply to built-in and custom asset connectors. Active and lifetime storage limits apply only to custom asset connectors.

Rate limits and vulnerability caps use the current platform defaults. Custom storage limits depend on the number of assets included in the community subscription. These values may change.

## Rate limits and caps for every asset connector

| Limit | Value | Applies to | When reached |
|---|---|---|---|
| Pushes | 60 per minute | Asset connector configuration | 429 `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED` |
| Daily item quota | 200,000 items per day, counted before validation | Asset connector configuration | 429 `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED`, with `details.limit` set to `items per day` |
| Item size | 900 KB | Item | 413 `ASSET_CONNECTOR_PUSH_TOO_LARGE` |
| Vulnerabilities per application | 1,000 | Application | Nothing is returned. Extra vulnerabilities are not stored. |
| Vulnerabilities per asset | 20,000 | Asset | Nothing is returned. New vulnerabilities are not stored. |

- The daily item quota is not a rolling window and does not reset at a fixed time. It resets 24 hours after the first counted push.
- After a 429, the connector pauses for an hour by default. Then it fetches again from its last checkpoint.
- The vulnerabilities-per-application cap applies only to CVEs that Sekoia matches from the NVD. It keeps known exploited CVEs first, then the highest CVSS scores.
- The vulnerabilities-per-asset cap applies to pushed findings and to CVEs matched from the NVD. Stored vulnerabilities are still updated and closed.
- Nothing warns when a cap leaves vulnerabilities out. They remain in the source tool, or in the NVD.

## Storage limits for custom asset connectors

!!! note "Custom asset connectors only"
    The limits in this section apply only to custom asset connectors. Built-in asset connectors are subject to the rate limits and vulnerability caps described above.

### Custom integrations

A community can own up to 10 custom integrations that contain an asset connector.

- The count is per integration. An integration with several asset connectors counts once.
- The number of asset connector configurations is not limited.
- An update counts only when it adds the first asset connector of the integration.
- Over the limit, the import or the update fails at the **Validating integration** step.

### How storage limits are calculated

Each storage limit is the number of assets your community subscribed, multiplied by a ratio. A community with no known number of assets counts as 1,000 assets.

| Limit | Counts | Per configuration | Per community |
|---|---|---|---|
| Active assets | Assets reported in the last 30 days | 5 × subscribed assets | 10 × subscribed assets |
| Active applications | Applications reported in the last 30 days | 25 × subscribed assets | 50 × subscribed assets |
| Open vulnerability findings | Findings with the open status | 50 × subscribed assets | 100 × subscribed assets |
| Lifetime assets | All assets stored, including those of deleted configurations | - | 15 × subscribed assets |
| Lifetime applications | All applications stored, including those of deleted configurations | - | 300 × subscribed assets |
| Lifetime vulnerability findings | All findings stored, of any status, including those of deleted configurations | - | 200 × subscribed assets |

For example, a community subscribed to 2,000 assets can have 10,000 active assets per configuration and 20,000 in the community.

### When a storage limit is reached

- Usage is computed every 15 minutes. A push accepted before the next computation is processed in full.
- While a configuration or its community has reached a limit, every push of the configuration receives a 429 `ASSET_CONNECTOR_LIMIT_REACHED`. Closures are refused too.
- When the community reaches a limit, every custom asset connector configuration of the community is blocked, not only the one that sent the most data. All of them push again once the community is back under the limit.
- `details.limits` lists each reached limit by `figure` and `scope` (`configuration` or `community`). It gives no usage or remaining count.
- The connector pauses for an hour by default, then fetches again from its last checkpoint. Data the source deleted in the meantime is not recovered.

### Which usage decreases

| Limit | How usage decreases |
|---|---|
| Active assets, active applications | By itself. While blocked, the configurations report nothing, so their assets and applications leave the 30-day window. |
| Open vulnerability findings | Only when users change finding statuses to remediated, accepted risk or false positive. The blocked connector cannot close findings. |
| Lifetime limits | Never. |

## Related articles

- [Build a custom asset connector](/xdr/features/modules/build_a_custom_asset_connector.md): How to send valid data and avoid duplicate assets.
- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md#diagnose-push-errors): Push errors and the action for each.
