# Vulnerability enrichment

Vulnerability enrichment aggregates known CVE exposures from connected vulnerability scanners and cloud or IaaS APIs and surfaces them on asset records in Sekoia. Analysts can review an asset's exposure directly in the asset context panel without switching to a separate vulnerability management tool.

Vulnerability data is available in the asset context panel under the **Vulnerabilities** tab and summarized in the **Health check** card on the **Overview** tab.

## How vulnerability enrichment works

Reveal collects vulnerability data from connected asset connectors that support vulnerability scanning. Each connector synchronizes its findings and maps them to the relevant asset record in Sekoia.

When an asset is affected by a known CVE, that vulnerability appears in the **Vulnerabilities** tab with its status, severity, and a unified risk score.

!!! note "Data source"
    Vulnerability enrichment requires a connected vulnerability scanner or a cloud or IaaS API that provides CVE data. Without this source, the Vulnerabilities tab does not display data. See [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md).

## Vulnerability fields

| Field | Description |
|---|---|
| Status | Open, Closed: Accepted risk, Closed: False positive, or Closed: Remediated |
| CVE ID | Linked to Sekoia CTI for additional threat intelligence context |
| Severity | CVSS score (v3 or v4 when available) |
| CWE | Weakness category |
| Unified risk score | Normalized score from 1 to 100 (see below) |
| Software / Version | Affected product and version |

Select a vulnerability row to expand it and view the full description, the connector that identified it, who or what closed it if applicable, and first and last seen dates.

> 📸 [SCREENSHOT SUGGESTION: Vulnerabilities tab listing three CVEs with status badges, CVSS scores, and unified risk scores visible. One row is expanded showing the description and connector fields. | ALT TEXT: Vulnerabilities tab with CVE list and one expanded row showing additional detail.]

## Unified risk score

Different vulnerability scanners use different scoring scales. The unified risk score translates each source into a single comparable value from 1 to 100, so analysts can prioritize across connectors without converting scores manually.

**Calculation method:**

1. Normalize the vendor score to a 0–100 range.
2. Invert the direction if the source scores safety rather than risk, so that 100 always represents the highest risk.
3. Clamp and round to the 1–100 range. Missing or invalid scores display as N/A.

The unified risk score reflects contextual risk. It is not the same as CVSS.

## Vulnerability statuses

Analysts can update the status of a vulnerability to reflect its current state.

| Status | When to use |
|---|---|
| Open | The vulnerability is active and unresolved |
| Closed: Accepted risk | The risk is acknowledged and accepted as a justified exception |
| Closed: False positive | The finding is invalid or irrelevant for this asset |
| Closed: Remediated | The vulnerability has been patched or mitigated |

## How to use vulnerability enrichment during an investigation

**During alert triage:** check whether the alerted asset is affected by CVEs that align with the attack technique observed. If the alert technique matches a vulnerability on the asset, prioritize containment and patching.

**During root cause analysis:** identify whether a known vulnerability was the likely entry point or enabler of the compromise.

**For proactive review:** use the Vulnerabilities tab to identify assets with high unified risk scores or open critical CVEs before an incident occurs.

??? example "Exploit alignment during a web server incident"
    A *remote file inclusion* alert (ATT&CK T1190) targets a web server. The Vulnerabilities tab shows **CVE-2023-28432** on the same application version with a high unified risk score. The CVE is linked to Sekoia CTI, which confirms active exploitation in the wild. The recommended action is to isolate the host, patch urgently, and document the exploit alignment in the case before closing.

## Related links

- [Asset context panel: Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md): Full reference for the Vulnerabilities tab and Health check card in the asset context panel.
- [Endpoint Hygiene](/xdr/features/modules/reveal_hygiene.md): How hygiene signals complement vulnerability data during posture assessment.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to connect a vulnerability scanner or cloud API to Sekoia.
- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): How to configure the data sources required for vulnerability enrichment.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md): Data source requirements for vulnerability enrichment and other Reveal capabilities.
