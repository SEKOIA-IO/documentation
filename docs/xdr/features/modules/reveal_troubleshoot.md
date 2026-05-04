# Troubleshoot Reveal

This reference lists common Reveal issues and the checks you can perform to resolve them.

## Asset context panel is empty or limited

Check whether:

- Reveal is enabled for your workspace or community.
- Supported telemetry is onboarded so Passive Asset Discovery can create and enrich asset records.
- Relevant event data is ingested.
- Asset Connectors are configured and synchronizing.
- The Sekoia Endpoint Agent is deployed and reporting where endpoint data is expected.

## Points of Interest are not visible

Check whether:

- The required behavioral event data is ingested.
- The relevant Points of Interest logic is available for your telemetry type.
- The asset has had enough time to establish a behavioral baseline.
- The asset has sufficient recent activity to evaluate.

## Attack Path Visualization shows no relationships

Check whether:

- Authentication event data is ingested.
- Events describe interactions between assets, users, hosts, or IPs.
- The involved assets are discovered or enriched.
- The selected asset has relevant relationship activity.

## Endpoint Hygiene is missing

Check whether:

- The Sekoia Endpoint Agent is deployed and reporting.
- A supported connector provides endpoint posture data.
- The endpoint is correctly associated with the asset record.
- The hygiene signal is supported for the endpoint or connector source.

## Vulnerability context is missing

Check whether:

- A vulnerability source is configured.
- The connector has synchronized successfully.
- The asset exists in the vulnerability source.
- The vulnerability data can be matched to the asset record in Reveal.

## Asset merging issues

Reveal merges assets from different sources when it finds matching identifiers. It merges host assets by hostname and user assets by username.

If the identifier format differs between sources, merging does not occur.

| Source A | Source B | Result |
|---|---|---|
| `laptop-123` | `laptop-123` | Assets merge. |
| `jane.doe` | `jane.doe` | Assets merge. |
| `laptop-123` | `laptop-123.company.local` | Assets may not merge. Short hostname and FQDN are not recognized as identical. |
| `jane.doe` | `jane.doe@company.com` | Assets may not merge. Username and email address are not recognized as identical. |
| `company\jane.doe` | `jane.doe` | Assets may not merge. Domain-prefixed username and plain username are not recognized as identical. |

!!! tip "Improve merge accuracy"
    Review how each source formats hostnames and usernames. Normalizing identifier formats across sources reduces duplicate asset records.

## Related links

- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md)
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md)
- [Asset context panel - Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md)
- [Attack Path Visualization](/xdr/features/investigate/attack_path_visualization.md)
- [Points of Interest](/xdr/features/detect/points_of_interest.md)
