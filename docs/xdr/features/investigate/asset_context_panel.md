# Asset context panel

The asset context panel is the central investigation surface in Sekoia. It gives analysts immediate access to an asset's identity, recent activity, and related security events without leaving the investigation workflow.

The panel is available to all clients from any alert, event, case, or the asset listing table. It eliminates the need to pivot between a CMDB, EDR console, or identity provider to answer basic questions about an asset.

!!! note "Reveal add-on module"
    The Reveal add-on module extends this panel with vulnerability data, endpoint hygiene, security controls, points of interest, and attack path visualization. See [Asset context panel — Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md).

<img width="431" height="684" alt="Asset context panel example" src="https://github.com/user-attachments/assets/7559b5b2-a838-4e53-a416-071d6b8c2fef" />

## Access the asset context panel

You can open the panel from several entry points depending on where you are working.

- **From an alert:** click the affected host, user, or IP. Use this to verify whether the asset is critical or recently involved in other detections during triage.
- **From an event:** click any field linked to an asset such as a hostname, username, or IP. Use this to identify who or what generated the event.
- **From a case:** click any listed affected asset. Use this to correlate incidents affecting the same asset.
- **From the asset listing:** navigate to **Configure > Assets**, then click the asset context panel icon on the right side of the asset row. Use this to review all known context for an asset outside of an active investigation.

## Overview tab

The **Overview** tab summarizes the asset's identity and recent security activity. Use it to assess how critical the asset is and whether it has been involved in recent detections before taking action.

### Header card

The header card displays the asset's name, type, and organizational context.

| Field | Description |
|---|---|
| Name and type | Host, account, or network |
| Criticality | Configured criticality score (0–100) |
| Verified by | User who verified the asset |
| Status | Reviewed or unreviewed |
| Communities | Communities the asset belongs to |
| First seen | When the asset was first observed by a discovery source |
| Last seen | When the asset was last observed by a discovery source |

!!! note "Field availability"
    Displayed fields differ by asset type and discovery source.

??? example "Ransomware triage scenario"
    A ransomware alert targets *FIN-SRV01*. The header card shows it is a finance system tagged as critical and owned by the CFO's department. This routes containment to the right team immediately, reducing dwell time.

<img width="538,3" height="172,2" alt="image" src="https://github.com/user-attachments/assets/11a8deca-efc1-4758-a218-c951703e284a" />

### Details card

The details card lists the technical identifiers used to recognize and correlate the asset across data sources.

| Asset type | Displayed fields |
|---|---|
| All types | Description, tags, identified by |
| Hosts | Hostname, IP addresses, Sekoia agent, operating system, domain/FQDN |
| Users | Username, full name, role, email, department, account state, last password change, key privileges |
| Networks *(coming soon)* | IP/CIDR ranges, VLAN/segment |

Select **View more details** to open the full list of known fields for the asset. You can mark any field as a favorite from this view. Favorites are personal and persist on a per-asset-type basis.
Select **Your favorite details:** to open all fields you have marked as Favorites. Favorites are personal and persist on a per–asset-type bas

??? example "Lateral movement identification"
    A host appears in a lateral movement alert with IP `10.10.2.45`. The details card shows the same IP belongs to *HR-LAPTOP07*, last seen by CrowdStrike and identified as Windows 11. Identity and scope are confirmed in seconds.

<img width="743" height="320" alt="Details card example" src="https://github.com/user-attachments/assets/9319c956-126d-4640-a382-f3b09f4ff7b8" />

### Seen in (last 30 days) card

The **Seen in** card shows how frequently the asset has appeared in recent security activity across alerts, cases, points of interest, and events over the last 30 days.

Each counter links to its respective filtered view for direct drill-down.

<img width="670" height="114" alt="Seen in 30 days card example" src="https://github.com/user-attachments/assets/1545c3b2-a748-4d0f-bbcc-8b62644b105c" />

### Last 5 severe alerts and cases card

This card lists the five most severe alerts and cases involving the asset over the last 30 days, ordered by severity then recency.

| Field | Description |
|---|---|
| Name | Alert or case title |
| Severity | Configured severity level |
| Age | Time since the item was created |

??? example "Lateral movement correlation"
    *ADMIN-LAPTOP01* triggered a *suspicious PsExec* alert and a *credential dumping* case. Linking both identifies lateral movement tied to a stolen admin account.

<img width="671" height="545" alt="Severe items card example" src="https://github.com/user-attachments/assets/073e1702-d1e3-4d7e-a994-96e7b93a9e9b" />

## Timeline tab

The **Timeline** tab provides a unified chronological record of significant activity for the asset. It brings together alerts, case associations, and raw events into a single stream.

Each entry is timestamped and categorized by type (alert, case, event) and color-coded by severity. Clicking an entry opens the corresponding detail view.

!!! note "Reveal enrichment"
    With the Reveal add-on module, the timeline also includes points of interest, vulnerability changes, and hygiene state changes. See [Asset context panel — Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md).

## Related events tab

The **Related events** tab provides direct access to all events associated with the asset. Use it to visualize activity volume and examine underlying telemetry without leaving the asset context.

**Top of the view**

- **Event histogram:** shows event distribution over time to help identify unusual activity windows.
- **Filter bar:** adjust the time range, connector, or field filters.
- **Totals:** displays event count and the number of events linked to alerts.

**Event list**

Each row includes the timestamp, event type and action, a short description, linked assets, and quick actions to expand the raw event or assign it to a case.

<img width="378" height="447" alt="Related events tab example" src="https://github.com/user-attachments/assets/536911ca-7745-49c9-b83e-a7b403f2d55d" />


## What Reveal adds to this panel

The Reveal add-on module extends the asset context panel with capabilities that go beyond identity and activity:

- **Endpoint Hygiene** — firewall and disk encryption status for host assets.
- **Vulnerabilities** — known CVE exposures from connected vulnerability scanners, with unified risk scoring.
- **Security controls** — a view of which detection and protection technologies cover the asset, and where gaps exist.
- **Points of Interest** — behavioral anomalies surfaced on the asset timeline, such as unusual authentication patterns or rare login locations.
- **Attack Path Visualization** — a graph of connected hosts and users that may form a lateral movement path from the asset.

To learn more, see [Asset context panel — Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md).

## Related links

- [Asset context panel — Reveal capabilities](/xdr/features/modules/reveal_asset_context_panel.md): Vulnerability data, endpoint hygiene, security controls, points of interest, and attack path visualization.
- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): How to enable Reveal and configure the required data sources.
- [Collect — Assets](/xdr/features/collect/assets.md): How assets are configured, discovered, and managed in Sekoia.
- [Points of Interest](/xdr/features/detect/points_of_interest.md): How Reveal surfaces behavioral anomalies on assets during triage and investigation.
