# Asset context panel — Reveal capabilities

The Reveal add-on module extends the asset context panel with vulnerability data, endpoint hygiene, security controls, points of interest, and attack path visualization. These capabilities give analysts a complete picture of an asset's exposure and protection directly in the investigation workflow.

This article covers the Reveal-specific sections of the asset context panel. For core capabilities available to all clients, see [Asset context panel](/xdr/features/investigate/asset_context_panel.md).

!!! note "Requirements"
    The capabilities described on this page require the Reveal add-on module. To set up the required data sources, see [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md).

## Health check card

The **Health check** card appears in the **Overview** tab for host assets. It provides a summary of open vulnerabilities, misconfigurations, and active security controls in one place.

| Section | Description |
|---|---|
| Security controls | Lists the active asset connectors and intakes contributing telemetry or protection for the asset |
| Open vulnerabilities | Total count of open CVE exposures. Individual items can be marked as accepted risk, false positive, or remediated |
| Misconfigurations | Count of configuration or posture issues identified, such as a disabled firewall or missing disk encryption |

This card gives analysts an at-a-glance posture summary before they open the dedicated tabs. It also shows which connectors are active, which clarifies available response actions such as host isolation or patch scan.

<img width="671" height="233" alt="Health check card example" src="https://github.com/user-attachments/assets/2e4cfcff-758a-4902-8b49-21676382336a" />

## Timeline enrichment

With Reveal enabled, the asset timeline includes additional entry types beyond alerts and cases.

| Entry type | Description |
|---|---|
| Points of Interest | Behavioral anomalies detected on the asset, such as unusual login times or rare locations |
| Hygiene changes *(coming soon)* | Changes to the asset's hygiene posture, such as firewall being disabled |
| Vulnerability changes *(coming soon)* | New CVE exposures identified on the asset |

Points of Interest fill the gaps between rule-based detections. They capture behavioral deviations that may precede or follow an alert, helping analysts build a coherent narrative from subtle signals.

!!! example "Points of Interest in context"
    A user account triggers a *credential dumping* alert. The timeline also shows a PoI for an anomalous login time two hours earlier and a second PoI for a rare login location the previous day. Together, these signals suggest the account was compromised before the alert fired.

## Hygiene tab

The **Hygiene** tab shows the security posture and configuration health of a host asset, based on data from the Sekoia Endpoint Agent and connected integrations.

| Control | Description |
|---|---|
| Firewall | Current state: enabled or disabled |
| Disk encryption | Global state and per-volume details |

Use this tab to validate that protections are in place during triage, identify weaknesses that may have enabled a compromise, and confirm that controls were restored after remediation.

!!! note "Data source"
    Hygiene data requires the Sekoia Endpoint Agent or a connector that provides endpoint posture data. See [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md).

<img width="389" height="465" alt="Hygiene tab example" src="https://github.com/user-attachments/assets/8e476aa6-2bb5-4284-8f71-374042bd936f" />

## Vulnerabilities tab

The **Vulnerabilities** tab lists known CVE exposures affecting the asset, aggregated from connected vulnerability scanners and cloud or IaaS APIs.

### Vulnerability list

| Column | Description |
|---|---|
| Status | Open, Closed: Accepted risk, Closed: False positive, or Closed: Remediated |
| CVE ID | Linked to Sekoia CTI |
| Severity | CVSS score (v3 or v4 when available) |
| CWE | Weakness category |
| Unified risk score | Normalized score from 1 to 100 (see below) |
| Software / Version | Affected product and version |

Select a row to expand it and view the full description, the connector that identified the vulnerability, the user or process that closed it if applicable, and first and last seen dates.

### Unified risk score

Different vulnerability scanners use different scoring scales. The unified risk score translates each source into a single comparable value from 1 to 100.

The score is calculated as follows:

1. Normalize the vendor score to a 0–100 range.
2. Invert the direction if the source scores safety rather than risk, so that 100 always represents the highest risk.
3. Clamp and round to the 1–100 range. Missing or invalid scores display as N/A.

The unified risk score reflects contextual risk and is not the same as CVSS.

!!! example "Exploit alignment during a web server incident"
    A *remote file inclusion* alert (ATT&CK T1190) targets a web server. The vulnerabilities tab shows **CVE-2023-28432** on the same application version with a high unified risk score. The recommended action is to isolate the host, patch urgently, and document exploit alignment in the case.

<img width="515" height="396" alt="Vulnerabilities tab example" src="https://github.com/user-attachments/assets/300d5842-379d-4c09-9827-331217ac4357" />

## Security controls tab

The **Security controls** tab shows which detection and protection technologies are actively covering the asset.

### Asset connectors

Lists the connectors that discovered or enriched the asset, such as an EDR tool (CrowdStrike, HarfangLab) or a vulnerability scanner (Tenable). Use this section to identify which technologies provide visibility or protection, and where gaps exist.

### Seen by

Lists the intakes and technologies that have observed the asset recently, such as a proxy, the Sekoia Endpoint Agent, or an identity provider. Presence in this list confirms that data from that source is reaching Sekoia.

!!! example "Detecting a visibility gap on a domain controller"
    A high-value domain controller appears in network telemetry and vulnerability management scans but not in endpoint or identity logs. This explains why credential-access activity was not detected. The recommended action is to deploy endpoint monitoring on the asset.

<img width="463,4" height="390,6" alt="Security controls tab example" src="https://github.com/user-attachments/assets/279e1288-53c6-490e-8f30-0498c3484d3e"/>

## Attack Path Visualization tab

The **Attack Path Visualization** tab displays a graph of hosts and users connected to the current asset through observed authentication relationships. Use it to assess whether a compromised or exposed asset provides a path to a more sensitive target.

**What the graph shows**

- Hosts, users, and accounts connected through observed authentication activity.
- Node color reflecting configured asset criticality.
- Satellite indicators per node summarizing active alerts, cases, vulnerabilities, and hygiene issues.

A single exposure is not always critical on its own. Its impact depends on what it connects to. This tab lets analysts assess blast radius and identify where remediation would have the greatest effect before escalating or containing.

For full guidance on navigating the graph, interpreting node types, and prioritizing remediation, see [Attack Path Visualization](/xdr/features/investigate/attack_path_visualization.md).

<img width="463,4" height="390,6" alt="Attack path visualization tab showing a node graph of connected assets within the asset context panel." src="/assets/attack_path_visualization"/>

## Related links

- [Asset context panel](/xdr/features/investigate/asset_context_panel.md): Core capabilities available to all clients, including the overview, timeline, and related events tabs.
- [Attack Path Visualization](/xdr/features/investigate/attack_path_visualization.md): Full reference for the attack path graph, node types, navigation, and remediation workflow.
- [Points of Interest](/xdr/features/detect/points_of_interest.md): How Reveal surfaces behavioral anomalies on assets during triage and investigation.
- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): How to enable Reveal and configure the required data sources.
- [Asset connector health status and logs](/xdr/features/collect/asset_connector_health.md): How to monitor connector synchronization and troubleshoot errors.
