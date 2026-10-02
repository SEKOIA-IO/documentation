# Application discovery

_**[Reveal module](/xdr/features/modules/reveal_index.md)** — This feature requires the Reveal add-on module._

!!! note "Beta"

    The Applications tab is currently in **Beta**. Fields and behavior may change as the feature evolves.

Application discovery lists the software installed on an asset and maps each application to the known CVE exposures that affect it. Analysts can review what is installed on a host, identify which applications are vulnerable, and pivot directly from an application to its associated vulnerabilities, all from the asset context panel.

Application data is available in the asset context panel under the **Applications** tab for host assets.

## How application discovery works

Reveal collects installed-software inventory from connected asset connectors (such as EDR tools and vulnerability scanners) and from endpoint telemetry. Each application is normalized to a Common Platform Enumeration (CPE) and, when available, a Package URL (PURL), which lets Sekoia match the application and its version against known CVEs.

When an installed application matches one or more known CVEs, it is flagged as vulnerable and the number of matching CVEs is shown in the **CVE Count** column.

!!! note "Data source"

    Application discovery requires a connected asset connector or endpoint agent that reports installed-software inventory. Without this source, the Applications tab does not display data. See [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md).

## Summary counters

At the top of the tab, two counters summarize the asset's software footprint:

| Counter | Description |
|---|---|
| Vulnerable Applications | Number of installed applications that have at least one matching CVE |
| Installed Applications | Total number of applications discovered on the asset |

## Filter and search

| Control | Description |
|---|---|
| **All / vulnerable** toggle | Switch between all discovered applications and only those with at least one CVE |
| **Filters** | Narrow the list by **Publisher**, **Application**, **Architecture**, or **Signed** status |
| **Search applications** | Free-text search across the application list |

## Application fields

The application list shows the following columns:

| Column | Description |
|---|---|
| Publisher | Vendor or author of the application (for example, Apache, Google, OpenSSL) |
| Application | Application name |
| CVE Count | Number of known CVEs affecting the installed version. Select the badge to view the matching vulnerabilities |
| Architecture | Target architecture of the installed binary, when reported |
| Version | Installed version of the application |
| Signed | Whether the binary is digitally signed (`True` / `False`) |
| Signed by | Signing authority, when the binary is signed |
| Filename | File name of the application binary, when reported |

Select an application row to expand it and view additional detail:

| Field | Description |
|---|---|
| Install path | Location where the application is installed on the asset |
| Installation date | When the application was installed |
| First seen | First time Sekoia observed the application on the asset |
| Last seen | Most recent time Sekoia observed the application on the asset |
| Last username | User associated with the most recent observation, when available |
| Source | Connector or intake that reported the application |
| SHA-256 | SHA-256 hash of the application binary, when available |
| MD5 | MD5 hash of the application binary, when available |
| CPE | Common Platform Enumeration identifier used to match the application to known CVEs |
| PURL | Package URL identifier, when available |

## Pivot from an application to its vulnerabilities

The **CVE Count** badge is a shortcut into the [Vulnerabilities tab](/xdr/features/modules/reveal_vulnerabilities.md). Select the badge (the **Click to see vulnerabilities** tooltip appears on hover) to open the filtered list of CVEs affecting that application.

This pivot lets analysts move from "what is installed and vulnerable on this host" to "exactly which CVEs apply and how severe they are" without leaving the asset context panel.

> 📸 [SCREENSHOT SUGGESTION: Applications tab (Beta) showing the Vulnerable Applications / Installed Applications counters, the All / vulnerable toggle, and the application list with Publisher, Application, CVE Count, Version, and Signed columns. One row is expanded to show Install path, CPE, and hashes. | ALT TEXT: Applications tab listing installed applications with CVE counts and one expanded row showing CPE and hash detail.]

## How to use application discovery during an investigation

**During alert triage:** check whether the alerted host runs a vulnerable application that aligns with the observed attack technique, then pivot to the CVEs to confirm severity and exploitability.

**During root cause analysis:** identify outdated or unsigned software that may have been the entry point or enabler of a compromise.

**For proactive review:** use the **vulnerable** filter to surface hosts running applications with high CVE counts (for example, an end-of-life browser or a legacy web server) and prioritize remediation before an incident occurs.

??? example "Vulnerable application triage"

    A host asset shows **Apache Tomcat 9.0.30** with a CVE Count of 38 and **Apache Log4j 2.14.1** with a CVE Count of 10. Selecting the Tomcat CVE badge opens the Vulnerabilities tab filtered to that application, where the analyst confirms several high-severity CVEs. The recommended action is to prioritize upgrading Tomcat and Log4j and document the exposure in the case.

## Related links

- [Vulnerability enrichment](/xdr/features/modules/reveal_vulnerabilities.md): How CVE exposures are aggregated and scored, and the detail available for each vulnerability.
- [Asset context panel: Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md): Full reference for the Reveal tabs in the asset context panel.
- [Asset risk scoring](/xdr/features/modules/asset_risk_scoring.md): How vulnerability exposure contributes to the host-level Asset Risk Score.
- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): How to configure the data sources required for application discovery.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md): Data source requirements for application discovery and other Reveal capabilities.
