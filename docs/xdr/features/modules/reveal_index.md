# Reveal

Reveal is a Sekoia add-on module that adds asset intelligence to your investigation workflows. It enriches the [asset context panel](https://docs.sekoia.io/xdr/features/investigate/asset_context_panel/) with vulnerability data, endpoint hygiene, behavioral signals, and attack path analysis.

Use Reveal to answer questions that alerts alone cannot answer:

- What is this asset, and is it vulnerable or poorly protected?
- What activity has occurred around it recently?
- Which other assets could it put at risk?

<div>
  <script async src="https://js.storylane.io/js/v2/storylane.js"></script>
  <div class="sl-embed" style="position:relative;padding-bottom:calc(51.02% + 25px);width:100%;height:0;transform:scale(1)">
    <iframe loading="lazy" class="sl-demo" src="https://sekoia.storylane.io/demo/1moepcy7xrq5?embed=popup" name="sl-embed" allow="fullscreen" allowfullscreen style="position:absolute;top:0;left:0;width:100%!important;height:100%!important;border:1px solid rgba(63,95,172,0.35);box-shadow: 0px 0px 18px rgba(26, 19, 72, 0.15);border-radius:10px;box-sizing:border-box;"></iframe>
  </div>
</div>


## How Reveal works

Reveal builds asset context from multiple sources and surfaces it where analysts already work.

| Source | What it provides |
|---|---|
| Passive Asset Discovery | Creates and lightly enriches assets from identifiers observed in supported telemetry. Starts automatically when telemetry is ingested. |
| Event data | Powers timelines, Points of Interest, Attack Path Visualization, and alert and case context. |
| Asset Connectors | Creates and deeply enriches assets with structured data from identity providers, endpoint tools, vulnerability scanners, and asset inventories. |
| Sekoia Endpoint Agent | Creates and enriches endpoint assets with direct endpoint visibility and hygiene signals. |

You do not need all four sources to start. Each source unlocks additional capabilities.


## Key capabilities
### Asset context panel

The asset context panel is the primary investigation surface. Reveal extends it with vulnerability data, hygiene status, and behavioral signals.

→ [Asset context panel](/xdr/features/modules/reveal_asset_context_panel.md)

### Attack Path Visualization

Attack Path Visualization maps relationships between assets. Use it to identify lateral movement paths, intermediary assets, and connected security activity.

→ [Attack Path Visualization](/xdr/features/investigate/attack_path_visualization.md)

### Points of Interest

Points of Interest surface behavioral anomalies on assets, such as unusual authentication patterns or rare locations. They appear during triage and investigation without requiring a separate alert.

→ [Points of Interest](/xdr/features/detect/points_of_interest.md)

### Endpoint Hygiene

Endpoint Hygiene shows posture signals for endpoints, such as whether the firewall or disk encryption is enabled. It requires the Sekoia Endpoint Agent or a supported connector.

→ [Asset connector health status and logs](/xdr/features/collect/asset_connector_health.md) 

### Vulnerability enrichment

Vulnerability enrichment shows whether an asset is affected by known CVEs. It requires a connected vulnerability scanner.

## When to use Reveal

Use Reveal when you need asset context that your alerts do not provide. Typical situations include:

- Triaging an alert on an asset you do not recognize.
- Assessing whether a compromised asset can reach sensitive systems.
- Identifying assets that are vulnerable or poorly protected before an incident occurs.
- Investigating lateral movement during an active case.

## Get started

To enable and configure Reveal, follow the [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md) guide. It describes the required data sources, the recommended setup order, and how to validate each capability.


## Related links

- [Collect — Assets](/xdr/features/collect/assets.md): Documentation on how assets are configured, discovered, and managed in Sekoia.
- [Detection — IOC detection](/xdr/features/detect/iocdetection.md): Overview of detection capabilities in Sekoia, including rule-based and analytics-driven approaches.
- [Integration — Asset categories](/integration/assets_categories/overview.md): Reference for asset connector categories and integration setup.
