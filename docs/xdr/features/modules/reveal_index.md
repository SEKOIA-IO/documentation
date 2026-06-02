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

Security teams investigate in two directions. Reactive investigations start from an alert, case, or detection. Proactive investigations start from a risk or exposure question. Reveal supports both by giving analysts the context they need to understand what an asset is, how it is protected, and what it connects to.


### What Reveal provides
 
| Capability | Description |
|---|---|
| [Asset context panel](/xdr/features/modules/reveal_asset_context_panel.md)| Extends the core panel with hygiene, vulnerabilities, security controls, points of interest, and attack path visualization |
| [Asset Connectors](/xdr/features/modules/reveal_asset_connectors_create.md) | Connects external systems such as EDR tools, vulnerability scanners, and identity providers to create and enrich asset records |
| [Points of Interest](/xdr/features/detect/points_of_interest.md) | Surfaces behavioral anomalies on assets that may not trigger alerts, such as unusual authentication patterns or rare locations |
| [Endpoint Hygiene](/xdr/features/modules/reveal_hygiene.md) | Shows firewall and disk encryption status for host assets |
| [Vulnerability enrichment](/xdr/features/modules/reveal_vulnerabilities.md) | Lists known CVE exposures affecting an asset, aggregated from connected scanners |
| [Security controls](/xdr/features/modules/reveal_security_controls.md) | Shows which detection and protection technologies cover an asset and where gaps exist |
| [Attack Path Visualization](/xdr/features/investigate/attack_path_visualization.md) | Maps relationships between assets to help analysts assess lateral movement risk and blast radius |
 
## How Reveal fits into your workflows
 
Reveal is designed to enrich the workflows analysts already use.
 
During a **reactive investigation**, an analyst starts from an alert or case. Reveal adds context about the involved asset: its identity, posture, exposure, recent activity, and relationships, so the analyst can assess priority, scope, and impact without pivoting to external tools.
 
During a **proactive investigation**, an analyst looks for assets that may require attention before an incident occurs. Reveal surfaces vulnerable, poorly protected, or unusually active assets so teams can prioritize remediation early.

## Get started

To enable and configure Reveal, follow the [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md) guide. It describes the required data sources, the recommended setup order, and how to validate each capability.


## Related links

- [Collect — Assets](/xdr/features/collect/assets.md): Documentation on how assets are configured, discovered, and managed in Sekoia.
- [Detection — IOC detection](/xdr/features/detect/iocdetection.md): Overview of detection capabilities in Sekoia, including rule-based and analytics-driven approaches.
- [Integration — Asset categories](/integration/assets_categories/overview.md): Reference for asset connector categories and integration setup.
