# Vulnerability enrichment

_**[Reveal module](/xdr/features/modules/reveal_index.md)** — This feature requires the Reveal add-on module._

Vulnerability enrichment aggregates known CVE exposures from connected vulnerability scanners and cloud or IaaS APIs and surfaces them on asset records in Sekoia. Reveal also enriches each CVE with data collected from the [NIST National Vulnerability Database (NVD)](https://nvd.nist.gov/), so analysts can review an asset's exposure and the technical characteristics of each vulnerability directly in the asset context panel, without switching to a separate vulnerability management tool.

Vulnerability data is available in the asset context panel under the **Vulnerabilities** tab and summarized in the **Health check** card on the **Overview** tab.

!!! note "Different from Asset Risk Score"

    The Unified risk score helps compare individual vulnerabilities from different sources. It is not the same as the host-level Asset Risk Score, which prioritizes the asset using multiple signal types.

## How vulnerability enrichment works

Reveal collects vulnerability data from connected asset connectors that support vulnerability scanning. Each connector synchronizes its findings and maps them to the relevant asset record in Sekoia.

When an asset is affected by a known CVE, that vulnerability appears in the **Vulnerabilities** tab with its status, severity, weakness category, and a unified risk score. Sekoia then enriches the CVE with reference data from NIST NVD, including the full CVSS vector, exploitability characteristics, and external references.

!!! note "Data source"

    Vulnerability enrichment requires a connected vulnerability scanner or a cloud or IaaS API that provides CVE data. Without this source, the Vulnerabilities tab does not display data. See [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md).

## Filter and search

| Control | Description |
|---|---|
| **Filters** | Narrow the vulnerability list by its available attributes |
| **Search vulnerabilities** | Free-text search across the vulnerability list (for example, by CVE ID or title) |
| **Status** dropdown | Change a vulnerability's status inline — see [Vulnerability statuses](#vulnerability-statuses) |

## Vulnerability list fields

The vulnerability list shows the following columns:

| Field | Description |
|---|---|
| Status | Open, Closed: Accepted risk, Closed: False positive, or Closed: Remediated |
| CVE ID | Common Vulnerabilities and Exposures identifier — the unique identifier assigned to a publicly known vulnerability. Linked to Sekoia CTI for additional threat intelligence context |
| Title | Short title of the vulnerability |
| Severity (CVSS) | Common Vulnerability Scoring System score, which rates the technical severity of the vulnerability (CVSS v4) |
| Exploitation | Known exploitation status for the vulnerability, when available |
| CWE | Common Weakness Enumeration — the underlying software flaw behind the vulnerability |
| Unified risk score | Normalized score from 1 to 100 (see [Unified risk score](#unified-risk-score)) |

### Severity (CVSS) bands

CVSS rates the technical severity of a vulnerability on a 0–10 scale:

| CVSS score | Severity |
|---|---|
| 9.0–10.0 | Critical |
| 7.0–8.9 | High |
| 4.0–6.9 | Medium |
| 0.1–3.9 | Low |
| 0.0 | None |

## Vulnerability detail

Select a vulnerability row to expand it and view the full detail. Reveal combines Sekoia detection metadata with the NIST NVD record for the CVE.

| Field | Description |
|---|---|
| Closed by | Who or what closed the vulnerability, or `Not remediated yet` when it is still open |
| Description | Full CVE description |
| CVSS version | CVSS version used to score the vulnerability (for example, `3.1`) |
| CVSS assessment source | Identifier of the source that provided the CVSS assessment |
| CVSS vector | Full CVSS vector string (for example, `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`), with a copy action |
| Attack vector | Context in which exploitation is possible (for example, `Network`) |
| Attack complexity | Conditions beyond the attacker's control required to exploit (for example, `High`) |
| Privileges required | Privileges an attacker needs before exploitation (for example, `None`) |
| User interaction | Whether a separate user must participate for exploitation (for example, `Required`) |
| Source | Authority that published the CVE record (for example, the vendor CNA) |
| References | External links categorized with tags such as `Release Notes`, `Vendor Advisory`, `Exploit`, `Issue Tracking`, and `Third Party Advisory` |
| Detection source | Connector or capability that detected the vulnerability on the asset (for example, Sekoia Asset Discovery) |
| Confirmed by | Source that confirmed the vulnerability on the asset |
| First seen | First time the vulnerability was observed on the asset |
| Last seen | Most recent time the vulnerability was observed on the asset |
| UUID | Unique identifier of the vulnerability record, with a copy action |
| External reference ID | Identifier of the vulnerability in the external source, when available |

!!! note "NIST NVD enrichment"

    The CVSS vector, attack vector, attack complexity, privileges required, user interaction, references, and description are sourced from the NIST National Vulnerability Database. This context helps analysts assess exploitability without leaving Sekoia.

> 📸 [SCREENSHOT SUGGESTION: Vulnerabilities tab with one CVE row expanded, showing the description, CVSS vector, attack vector, privileges required, references, and detection source fields. | ALT TEXT: Expanded vulnerability row showing NIST NVD enrichment fields including CVSS vector and references.]

## Unified risk score

!!! note "Asset score and vulnerability score"

    The Unified risk score applies to an individual vulnerability. The Asset Risk Score applies to the host asset and combines exposure, recent activity, and criticality.

Different vulnerability scanners use different scoring scales. The unified risk score translates each source into a single comparable value from 1 to 100, so analysts can prioritize across connectors without converting scores manually.

**Calculation method:**

1. Normalize the vendor score to a 0–100 range.
2. Invert the direction if the source scores safety rather than risk, so that 100 always represents the highest risk.
3. Clamp and round to the 1–100 range. Missing or invalid scores display as N/A.

The unified risk score is normalized for consistency across vendors and maps to the following bands:

| Unified risk score | Band |
|---|---|
| 76–100 | Critical |
| 51–75 | High |
| 26–50 | Medium |
| 1–25 | Low |

The unified risk score reflects contextual risk. It is not the same as CVSS.

## Vulnerability statuses

Analysts can update the status of a vulnerability from the **Status** dropdown to reflect its current state.

| Status | When to use |
|---|---|
| Open | The vulnerability is active and unresolved |
| Closed: Accepted risk | The risk is acknowledged and accepted as a justified exception |
| Closed: False positive | The finding is invalid or irrelevant for this asset |
| Closed: Remediated | The vulnerability has been patched or mitigated |

!!! note

    The inline dropdown on a row offers **Accepted risk** and **False positive**. A vulnerability moves to a remediated state when the connected scanner no longer reports it.

## How to use vulnerability enrichment during an investigation

**During alert triage:** check whether the alerted asset is affected by CVEs that align with the attack technique observed. Use the CVSS vector and exploitability fields to judge how easily the vulnerability can be exploited.

**During root cause analysis:** identify whether a known vulnerability was the likely entry point or enabler of the compromise, using the references and detection source for corroboration.

**For proactive review:** use the Vulnerabilities tab to identify assets with high unified risk scores or open critical CVEs before an incident occurs.

??? example "Exploit alignment during a web server incident"

    A *remote file inclusion* alert (ATT&CK T1190) targets a web server. The Vulnerabilities tab shows a CVE on the same application version with a high unified risk score. The expanded detail shows an `Attack vector: Network` with `Privileges required: None`, and a reference tagged `Exploit`, confirming it is readily exploitable. The recommended action is to isolate the host, patch urgently, and document the exploit alignment in the case before closing.

## Related links

- [Application discovery](/xdr/features/modules/reveal_applications.md): Review installed software and pivot from an application to its CVEs.
- [Asset context panel: Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md): Full reference for the Vulnerabilities tab and Health check card.
- [Asset risk scoring](/xdr/features/modules/asset_risk_scoring.md): How vulnerability exposure contributes to the host-level Asset Risk Score.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to connect a vulnerability scanner or cloud API to Sekoia.
- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): How to configure the data sources required for vulnerability enrichment.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md): Data source requirements for vulnerability enrichment and other Reveal capabilities.
