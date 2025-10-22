# Asset context panel

The **asset context panel** is the analyst’s command window for understanding an asset’s full context — its identity, posture, vulnerabilities, and recent behavior — directly within your investigation workflow.

It appears as a slide-out panel accessible from any **alert**, **event**, or **case** where an asset is mentioned, or via the **asset listing** table.

Instead of switching between inventory pages, a configuration management database (CMDB), vulnerability management (VM), or endpoint detection and response (EDR) tools, analysts can instantly see **who or what the asset is**, **how it’s behaving** — now and historically — and **how well it’s protected** in one place.

**Availability**

- **All clients:** core sections — overview, asset details, recent activity, related alerts/cases/events, timeline.
- **(Reveal specific capability):** extended sections — hygiene, vulnerabilities, security controls, points of interest (PoIs), applications *(coming soon)*.

!!! Note
    To learn how assets are **configured and discovered**, see [Collect → Assets](https://docs.sekoia.io/xdr/features/collect/assets/).

---

<img width="431" height="684" alt="Asset context panel example" src="https://github.com/user-attachments/assets/7559b5b2-a838-4e53-a416-071d6b8c2fef" />

---

## Accessing the asset context panel

The panel is designed for **contextual investigation**, letting you open it from where you work:

- **From alerts:** click the affected host, user, or IP asset.  
  → Instantly view posture, vulnerabilities, and related alerts.  
  *Typical usage:* during triage, verify whether the asset is critical or recently compromised.
- **From events:** click any field linked to an asset (e.g., hostname, username, IP).  
  → See who or what generated the event and whether it is part of a larger pattern.
- **From cases:** click any listed **Affected asset**.  
  → Correlate incidents affecting the same asset.
- **From asset listing (Configure → Assets):** click the **asset context panel** icon on the right side of the listed asset.  
  → Instantly view all contextual information known about that asset, including identifiers, posture, vulnerabilities, and recent activity.

**Why it matters**  

During an active investigation, analysts need to pivot fast. Every external click — to a CMDB, EDR console, or VM dashboard — adds friction and increases the risk of misattribution.  
The **asset context panel** eliminates this by bringing **context, coverage, and posture** directly into the investigation view — helping analysts move from *alert to understanding* in a single step.

## Asset context panel content

### 1. Overview tab

The **overview** tab summarizes the asset’s identity, business relevance, and current review status — helping analysts assess **how critical it is to the organization** before acting and navigate known details.

#### Header card

**Displayed fields**

- **Asset risk score (ARS)** — *coming soon*  
- **Name & type:** host, account, or network  
- **Criticality:** configured asset criticality (0–100)  
- **Verified by:** user who verified the asset  
- **Status:** reviewed or unreviewed  
- **Communities:** communities the asset is part of  
- **First seen:** when the asset was first seen by a discovery source  
- **Last seen:** when the asset was last seen by a discovery source  
- *Note: fields differ by asset type and discovery source.*

**Why it matters during investigations**

- **Prioritization:** analysts must respond faster to alerts on high-impact systems (e.g., domain controllers or production databases).  
- **Attribution:** identifies the business unit or owner to contact for containment, access suspension, or post-incident communication.

**Example**  

When a ransomware alert hits *FIN-SRV01*, the overview shows it is a finance system tagged **critical** and owned by the CFO’s department. This routes containment to the right team immediately — reducing dwell time.

<img width="538,3" height="172,2" alt="image" src="https://github.com/user-attachments/assets/11a8deca-efc1-4758-a218-c951703e284a" />


#### Details card

The **details** section provides the technical identifiers used to recognize and correlate this asset across multiple data sources.

**Displayed fields**

- **All asset types:** description, tags, identified by  
- **Hosts:** hostname, IP addresses, Sekoia agent, operating system, domain/FQDN  
- **Users:** username, full name, role, email, department, account state, last password change, key privileges  
- **Networks(Coming soon):** IP/CIDR ranges, VLAN/segment 

**Why it matters during investigations**

- **Correlation:** analysts can pivot across EDR, identity, network, and vulnerability logs using consistent identifiers.

**Example**  

A host appears in a lateral-movement alert with IP `10.10.2.45`. In the panel, you see the same IP belongs to *HR-LAPTOP07*, last seen by CrowdStrike and identified as Windows 11. You have confirmed identity and scope in seconds.

<img width="743" height="320" alt="Details card example" src="https://github.com/user-attachments/assets/9319c956-126d-4640-a382-f3b09f4ff7b8" />

#### Health check card *(Reveal specific capability)*

**Availability:** host assets

The **health check** card provides a high-level overview of known **vulnerabilities** and **misconfigurations** on the viewed asset.  
It helps analysts quickly assess overall security posture and determine whether an asset is well protected or needs remediation.

**Purpose**

- Offer a **snapshot of asset health** by summarizing active vulnerabilities and hygiene issues.  
- Display the **security controls** currently in place to protect the asset.  
- Help analysts identify **pivot** and **remediation** opportunities during investigations.

**Security controls**  

Lists the active **asset connectors** and **intakes** contributing telemetry or protection for the asset, indicating:  
- Which defensive technologies are in place (e.g., EDR, vulnerability scanner, CMDB).  
- What contextual or remediation actions are available (e.g., isolate host, trigger patch scan).

**Open vulnerabilities**  

Shows the number of open vulnerabilities affecting the asset. Items can be set to:  
- **Accepted risk** — justified exception  
- **False positive** — invalid/irrelevant  
- **Remediated** — no longer present on the asset

**Misconfigurations**  

Displays the number of configuration or posture issues identified (e.g., disabled firewall, missing encryption).

**Why it matters**

- **At-a-glance posture:** aggregates multiple data sources into a single, interpretable summary.  
- **Faster triage:** prioritize assets with both critical vulnerabilities and poor hygiene.  
- **Context for action:** seeing which connectors protect an asset clarifies available playbooks and containment paths.  
- **Visibility gaps:** absence of certain controls (e.g., no VM data) highlights where additional integration may be required.

<img width="671" height="233" alt="Health check card example" src="https://github.com/user-attachments/assets/2e4cfcff-758a-4902-8b49-21676382336a" />

#### Seen in (last 30 days) card

The **seen in (last 30 days)** card shows how frequently the asset has appeared in recent security activity, aggregating counts across **alerts**, **cases**, **PoIs**, and **events** related to the asset.

**What it shows**

- **Alerts:** number of detections that referenced this asset  
- **Cases:** number of investigations involving this asset  
- **PoIs:** number of behavioral anomalies observed for this asset  
- **Events:** total raw telemetry events linked to this asset

Each counter links to its respective view (filtered to the asset and time range) for rapid drill-down.

<img width="670" height="114" alt="Seen in 30 days card example" src="https://github.com/user-attachments/assets/1545c3b2-a748-4d0f-bbcc-8b62644b105c" />

#### Last 5 severe alerts and cases (last 30 days) card

A compact card listing the **five most severe** items (by severity, then recency) involving the asset over the last 30 days. Use it to spot high-impact activity at a glance and jump straight into the most urgent investigations.

**Displayed fields**

- alert or case name, severity, and age

**Why it matters**

- **Campaign correlation:** several alerts on the same host (failed logins, unusual tools, privilege escalation) often indicate an active compromise chain.  
- **Case enrichment:** attach new findings to an existing incident instead of opening a duplicate case.

**Example**  

*ADMIN-LAPTOP01* triggered a *suspicious PsExec* alert and a *credential dumping* case. Linking both identifies lateral movement tied to a stolen admin account.

<img width="671" height="545" alt="Severe items card example" src="https://github.com/user-attachments/assets/073e1702-d1e3-4d7e-a994-96e7b93a9e9b" />

---

### 2. Timeline tab *(all clients; enriched with Reveal specific capability)*

The **timeline** provides a unified, chronological record of relevant activity for a specific asset, bringing together **alerts**, **points of interest (PoIs)**, **vulnerabilities**, and **case associations** into a single stream.

**Displayed items**

- Alerts (rule/analytics detections)  
- Case associations (when the asset is seen in a case)  
- PoIs (UEBA anomalies and notable activities) (coming soon)  
- Hygiene (Changes to asset hygiene posture) (coming soon)  
- Vulnerabilities (identified exposures related to the asset) (coming soon)

#### How the timeline works

Each entry represents a significant observation tied to the asset.  
Entries are automatically timestamped and iconized by category (alert, case, PoI, vulnerability) and color-coded by severity.

Clicking an item triggers available pivots (e.g., clicking an alert opens the **alert details** view).

!!! Note
    With the *(Reveal specific capability)*, the timeline includes PoIs vulnerability enrichments and hygiene changes.

#### Using PoIs in the timeline

**PoIs** capture anomalies and behavioral deviations that may **precede** or **follow** alerts — filling gaps between rule-based detections.

**Example PoIs**

- anomalous login time (user/host)  
- rare login location (user/host)  
- anomalous login failure ratio (user/host)

**Why PoIs matter**

1) **Connect subtle signals** into a coherent narrative.  
2) **Correlate with detections** before/after alerts (e.g., failed logons → successful RDP → SYSTEM process creation).

---

### 3. Related events tab

The **related events** tab provides an investigative view of all events associated with the asset. It enables analysts to **visualize activity volume** and **drill into telemetry** without leaving asset context, bridging summarized context (overview, timeline) and underlying evidence.

<img width="378" height="447" alt="Related events tab example" src="https://github.com/user-attachments/assets/536911ca-7745-49c9-b83e-a7b403f2d55d" />

#### Purpose

- investigate directly from the asset view (host, IP, user)  
- correlate behaviors over time (spikes/quiet periods)  
- assign events to cases for evidence tracking

#### What you see

**Top of the view**

- **event histogram:** distribution over time to spot patterns  
- **filter bar:** adjust time range, connectors, or field filtering  
- **totals:** event count and number linked to alerts

**Event list**

- **timestamp**  
- **event type and action**  
- **short description** (process execution, logon, network connection, etc.)  
- **linked asset(s)**  
- **quick actions** (expand raw event, assign to case)

**Why it matters**

- **Efficient triage:** spot abnormal activity windows quickly  
- **Evidence-driven analysis:** access exact telemetry  
- **Forensic traceability:** assigned events become case evidence  
- **Cross-source correlation:** endpoint, identity, and network in one place

---

### 4. Hygiene tab *(Reveal specific capability)*

The **hygiene** tab provides visibility into the asset’s **security posture** and **configuration health** based on the Sekoia endpoint agent and connected integrations.  
It highlights **disabled encryption** or **disabled firewall** and other missing protections that increase exposure and impact.

<img width="389" height="465" alt="Hygiene tab example" src="https://github.com/user-attachments/assets/8e476aa6-2bb5-4284-8f71-374042bd936f" />

#### Purpose

- assess hardening (are firewall and encryption enabled?)  
- identify exposure (weak points attackers can exploit)  
- support remediation (actionable insights for IT and SOC)

#### What you see

**Summary cards**

- **firewall:** enabled/disabled  
- **disk encryption:** global state and per-volume details

**Why it matters**

- **Root-cause validation:** hygiene exposes weaknesses that enabled compromise.  
- **Containment prioritization:** poor posture on high-value assets warrants immediate action.  
- **Post-incident remediation:** validate protections were restored.

---

### 5. Vulnerabilities tab *(Reveal specific capability)*

The **vulnerabilities** tab lists known CVE exposures affecting the asset, aggregated from vulnerability scanners and cloud/IaaS APIs.  
Use it to understand **exposure**, validate **exploit alignment**, and prioritize **remediation**.

#### What you see

**List columns**

- **status:** `Open`, `Closed: Accepted risk`, `Closed: False positive`, `Closed: Remediated`  
- **CVE ID:** linked to **Sekoia cyber threat intelligence (CTI)**  
- **severity:** CVSS (v3/v4 when available)  
- **CWE:** weakness category  
- **unified risk score (1–100):** normalized across vendor-specific scoring systems (see *Normalization* below)  
- **software / version:** affected product and version

**Expanded row**

- **description** (source/CTI)  
- **identified by** (scanner/connector/job)  
- **closed by** (user/process, if available)  
- **first seen / last seen**

#### Normalization (unified risk score)

Different sources score severity/risk differently. The **unified risk score (1–100)** translates each source into a comparable “risk level”. It is **not the same as CVSS** — it reflects *contextual risk*, aligning disparate vendor scales.

**How it works**

1) **Normalize** any vendor range (e.g., 0–10, 0–5) to a **0–100** percentage.  
2) **Adjust direction:** if a score means *higher = safer*, invert so **100 = highest risk**.  
3) **Clamp & round:** keep within 1–100; missing/invalid → **N/A**.

**Why it matters**

- **Threat alignment:** if an alert technique exploits a listed CVE, prioritize containment/patching.  
- **Attack-surface clarity:** explains plausible entry points and lateral paths.  
- **Operational prioritization:** escalate high-risk items to vulnerability ops; link to the active case.

**Example**  

A *remote file inclusion* alert (ATT&CK T1190) hits a web server. The tab shows **CVE-2023-28432** on the same application version with high unified risk → isolate host, patch urgently, and document exploit alignment.

<img width="515" height="396" alt="Vulnerabilities tab example" src="https://github.com/user-attachments/assets/300d5842-379d-4c09-9827-331217ac4357" />

---

### 6. Software tab *(coming soon)*

---

### 7. Security controls tab *(Reveal specific capability)*

The **security controls** tab visualizes which detection and protection technologies are actively securing the asset — a clear view of **telemetry posture** (how the asset was discovered and which controls observe/protect it).

#### Asset connectors
Connectors that discovered or enriched the asset (e.g., **EDR** such as CrowdStrike/HarfangLab; **VM** such as Tenable). Use this to identify which technologies provide **visibility/protection**, where to **pivot**, and whether gaps exist (e.g., only logs, no active monitoring).

#### Seen by
**Intakes and technologies** that have observed the asset recently (e.g., proxy, endpoint agent, identity provider). Presence indicates data visibility from that source.

**Why it matters**

- **Coverage validation:** quickly spot endpoint/identity/network blind spots.  
- **Response planning:** confirm protective agents/integrations before containment.  
- **SOC maturity:** continuously improve visibility and control coverage.

**Example**  

A high-value domain controller appears in network telemetry and VM scans but not in endpoint or identity logs — explaining why credential-access activity was not detected. Task: deploy endpoint monitoring.

<img width="463,4" height="390,6" alt="Security controls tab example" src="https://github.com/user-attachments/assets/279e1288-53c6-490e-8f30-0498c3484d3e" />

## Summary

The **asset context panel** combines **asset intelligence**, **behavior analytics**, and **security posture** in one view.

It turns investigation into **risk-aware decision-making**, helping analysts:

- understand **what** the asset is  
- evaluate **how well** it is protected  
- assess **whether** it is behaving abnormally  
- **act decisively** with traceable context

The panel bridges the gap between *data visibility* and *investigative understanding* — making every analyst faster, more confident, and more effective.
