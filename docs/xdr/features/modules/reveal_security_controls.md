# Security controls

The Security controls tab in the asset context panel shows which detection and protection technologies are actively covering an asset. Use it to confirm that the right tools are in place, identify visibility gaps, and understand which response actions are available before taking containment steps.

## How Security controls works

Reveal aggregates coverage information from two sources:

- **Asset connectors** that have created or enriched the asset record.
- **Intakes and technologies** that have observed the asset in recent event data.

This produces a unified view of what Sekoia knows about the protection and observability of the asset.

## Security controls sections

### Asset connectors

Lists the connectors that have contributed to the asset record, such as an EDR tool (CrowdStrike, HarfangLab), a vulnerability scanner (Tenable), or an identity provider (Microsoft Entra).

Each connector entry indicates:

- Which technology provides coverage.
- Whether contextual or remediation actions are available from that connector, such as isolating a host or triggering a patch scan.

Use this section to confirm that the expected tools are linked to the asset and to identify which response options are available during an active investigation.

### Seen by

Lists the intakes and technologies that have observed the asset recently, such as a proxy, the Sekoia Endpoint Agent, or an identity provider log.

Presence in the **Seen by** list confirms that event data from that source is reaching Sekoia and has been associated with this asset. Absence may indicate a visibility gap or a data ingestion issue.

> 📸 [SCREENSHOT SUGGESTION: Security controls tab showing an asset connectors section listing CrowdStrike and Tenable, and a seen by section listing the Sekoia Endpoint Agent and a proxy intake. | ALT TEXT: Security controls tab with two asset connectors and two observed sources listed.]

## How to use Security controls during an investigation

**Before containment:** confirm that the EDR connector linked to the asset supports host isolation. If the expected connector is absent, containment may need to follow a manual process.

**During triage:** check whether the asset is covered by both endpoint and network telemetry. An asset visible only in network logs but not in endpoint logs may have limited forensic data available.

**For proactive review:** identify assets that are missing expected connectors or have not been observed by key intakes recently.

??? example "Detecting a visibility gap on a domain controller"
    A high-value domain controller appears in network telemetry and vulnerability management scans but is absent from the **Seen by** list for endpoint and identity logs. This explains why credential-access activity on the host was not detected. The recommended action is to deploy the Sekoia Endpoint Agent or configure an identity provider intake for the asset.

## Related links

- [Asset context panel: Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md): Full reference for all Reveal-specific sections of the asset context panel, including the Security controls tab.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to add a connector that contributes to asset coverage.
- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md): How to diagnose connector errors if an expected connector does not appear.
- [Endpoint Hygiene](/xdr/features/modules/reveal_hygiene.md): How hygiene signals complement coverage data during posture assessment.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md): Data source requirements for Security controls and other Reveal capabilities.
