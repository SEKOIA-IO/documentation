# Sekoia Defend (XDR) - Sales Engineer Technical Summary and RFP Guide

Version: 2026-03-02  
Audience: Sales Engineers (primary), technical evaluators, RFP responders  
Purpose: Give Sales Engineers a complete technical and positioning foundation for Sekoia Defend before hands-on product work.

---

## 1. How to use this guide

This document is intentionally detailed. It is written for SEs who may be strong in security but new to Sekoia Defend.

Use it in three layers:

1. **Foundation reading**: read Sections 2 to 5 to understand the platform end-to-end.
2. **Conversation prep**: use Sections 6 and 7 before customer calls and demos.
3. **Execution support**: use Sections 8 and 9 for objection handling and RFP responses.

A practical way to consume it:

1. Start with the product story in Section 2.
2. Read the architecture and workflow in Section 3.
3. Study each capability section in Section 4.
4. Use the talk track and RFP language later as reusable assets.

---

## 2. Executive positioning for Sales Engineers

Sekoia Defend is an XDR platform built to help SOC teams move from fragmented visibility to coordinated detection and response operations.

In practical terms, Sekoia Defend gives security teams one operational layer to:

- ingest and normalize telemetry,
- detect suspicious and malicious behavior in real time,
- investigate alerts with enriched context,
- manage incidents through cases,
- report posture and performance to operational and business stakeholders.

For Sales Engineers, the core positioning message is:

- **Business value first**: faster SOC operations, lower triage friction, better prioritization, better reporting discipline.
- **Technical credibility second**: real-time multi-engine detection, mature rule operations, contextual enrichment, analyst-centric investigation tooling, and extensibility.

When this is explained well, customers usually understand that Sekoia Defend is not just “another log repository” and not just “another alerting tool.” It is an operating environment for detection and response.

---

## 3. Platform architecture and operating model

### 3.1 End-to-end flow

A simple way to explain Sekoia Defend technically is to walk through the lifecycle of a security signal:

1. **Collection**: logs and security events are brought in through intakes (push or pull).
2. **Normalization and enrichment**: events are standardized and enriched with contextual data.
3. **Detection**: rules and models evaluate events in real time across multiple detection engines.
4. **Alerting and prioritization**: alerts are created, scored, grouped, and routed into analyst workflows.
5. **Investigation and case management**: analysts pivot across events, alerts, assets, and CTI context.
6. **Analytics and reporting**: SOC and management views are generated with dashboards and queries.
7. **Automation and ecosystem actions**: playbooks and integrations connect detection outputs to response actions and external systems.

This lifecycle framing helps SEs structure discovery, demo flow, and RFP narratives consistently.

### 3.2 What is distinctive in practice

For customer conversations, these are the practical differentiators to emphasize:

- **Real-time detection posture** rather than delayed or purely batch-oriented workflows.
- **Multi-engine strategy** (Sigma, CTI/IoC, anomaly) rather than a single detection pattern style.
- **Strong rule operations model** (catalog management, effort levels, filters, lifecycle, testing).
- **Context-rich investigation experience** (assets, observables, cases, graph, query tools).
- **AI support at workflow level** (Roy assistant and AI Cases) with analyst-in-the-loop control.

---

## 4. Technical deep dive (detailed)

## 4.1 Collection and onboarding telemetry

### What this capability is

Collection in Sekoia Defend is built around **intakes**, which represent data sources sending or exposing telemetry to the platform. Each intake is associated with an intake format, an entity, and an intake key, giving the SOC a structured way to onboard heterogeneous technologies.

### How it works in practice

Sekoia Defend supports two primary collection modes:

- **Push intake**: the customer forwards logs toward Sekoia intake points.
- **Pull intake**: Sekoia connectors actively fetch data from source systems (commonly API-based patterns).

This dual model is important for SE work because enterprise environments are rarely homogeneous. Some sources can push, others must be polled.

### Operational controls and health visibility

The intake experience is not only about initial setup. It includes health visibility that matters during production operations:

- valid event counts,
- invalid event counts,
- warning-level events,
- event delivery lag indicators,
- pull connector status and connector logs,
- inactivity notifications.

SE note: this is often where customer trust is won or lost. Detection quality always depends on ingestion quality. Demonstrating these controls helps position Sekoia Defend as operationally mature.

### Why it matters for business outcomes

- Faster source onboarding reduces time-to-value.
- Better collection observability reduces blind spots caused by silent failures.
- Better troubleshooting reduces analyst and engineering time spent on pipeline uncertainty.

### Demo guidance for new SEs

Show:

1. Intake listing and health metrics.
2. Pull connector status states and error handling flow.
3. Lag interpretation and root-cause examples.
4. Inactivity notification configuration.

---

## 4.2 Parsing, normalization, and event quality

### What this capability is

Sekoia Defend applies parsing and normalization so events from different products become analyzable in a consistent model. In both the current product narrative and the baseline technical summary, the normalization strategy is presented as a foundational enabler of cross-source detection engineering.

### Why normalization is critical

Without normalization, every rule and investigation query becomes source-specific. With normalization, SOC teams can:

- build reusable detection logic,
- correlate across technologies,
- reduce parsing ambiguity in investigations,
- maintain consistent reporting metrics.

### What to explain clearly to customers

- The SOC does not only need data volume; it needs **usable** data.
- Parsing quality directly affects false positives and missed detections.
- Intake validation states (valid/warning/invalid) are practical indicators of rule reliability downstream.

### SE note for RFP language

When asked about interoperability and scalability, tie normalization to long-term maintainability of detections and hunt queries.

---

## 4.3 Enrichment and context generation

### What this capability is

Sekoia Defend enriches normalized events with context so analysts can interpret significance faster. This context combines platform intelligence and customer environment context.

### Core enrichment dimensions

- **Threat-intelligence-derived context**: observables and threat knowledge mapped to event artifacts.
- **Asset-derived context**: organization-specific context (criticality, ownership cues, scope relevance, etc.).

In the investigation workflow, this turns raw telemetry into prioritized, explainable security context.

### Why this matters operationally

Analysts do not triage raw strings; they triage risk and impact. Enrichment improves:

- speed of qualification,
- confidence in prioritization,
- consistency in analyst decisions,
- communication quality toward incident stakeholders.

### What to show in demos

- Event detail with enrichment enabled.
- A practical before/after explanation of triage quality with and without context.
- How enriched values support investigation pivots and case evidence.

---

## 4.4 Entities and segmentation model

### What this capability is

Entities are logical organizational units used to group data sources and alerts. They can represent a site, business unit, network zone, or another customer-defined boundary.

### Why this matters

Entities enable:

- cleaner operational segmentation,
- easier reporting and governance,
- differentiated alert workflow behavior through alert generation mode defaults.

### Alert generation mode

Entity configuration includes alert generation mode:

- `automatic`: alerts proceed to operational status directly,
- `manual`: alerts remain pending until analyst action.

This is particularly useful for phased rollouts and customer maturity adaptation.

### SE conversation angle

When customers worry about “turning on too much too fast,” use entities and generation modes to show controlled rollout patterns.

---

## 4.5 Asset model and asset-driven operations

### Why assets deserve extra attention

For new SEs, this is one of the most important sections: Sekoia Defend is not only event-centric, it is also strongly asset-aware. That is essential for credible SOC prioritization.

### What the asset model is

Assets in Sekoia Defend represent core IT resources (accounts, hosts, networks) and include contextual and detection-related properties. Criticality values (0-100) are part of this model and feed prioritization logic in investigations.

### Asset lifecycle and discovery

Asset inventory can include:

- manually created assets,
- imported assets,
- automatically discovered assets from event telemetry.

Automatic discovery uses event-derived identifiers (atoms) and tracks relationships over time. This historical mapping is useful in investigations where identifiers shift (for example IP/hostname associations over time).

### Why this matters in real SOC operations

A SOC does not only need to know that "an event happened." It needs to know:

- which business-relevant asset is affected,
- how critical that asset is,
- how to prioritize containment and escalation.

Sekoia Defend’s asset model helps move from technical signal to operational priority.

### Asset-driven detection tuning

Detection and filtering can use asset properties, tags, and criticality dimensions to:

- focus on high-value targets,
- suppress known low-value noise,
- tailor detections to environment realities.

This is frequently a deciding factor for mature buyers that have already experienced “generic SIEM noise.”

### SE demo guidance

Show:

1. Asset listing and filters.
2. Criticality use in urgency calculations.
3. A simple rule or filter pattern scoped with asset context.
4. A case where asset context changes investigation priority.

---

## 4.6 Storage, retention, and historical investigations

### Storage architecture

Sekoia Defend uses a tiered model:

- **Hot storage** for immediate operational search.
- **Cold storage** (optional) for archived retention.

Hot storage is the operational investigation layer; cold storage supports longer-term retention strategy with rehydration workflows.

### Retention ranges and constraints

Documented baseline values include:

- hot storage default: 30 days,
- extendable up to 365 days,
- contractual limits govern recoverability.

Archived data can be rehydrated for investigations, but this process is controlled and temporary.

### Why this matters to customers

- Balances search performance and retention economics.
- Supports compliance and historical IR needs without over-indexing all data.
- Creates clear governance boundaries for what is recoverable.

### SE framing tip

Be explicit with customers: retention beyond contractual thresholds is not recoverable. This clarity improves trust during technical due diligence.

---

## 4.7 Detection strategy and rule operations

### Detection strategy overview

Sekoia Defend combines three primary detection approaches:

- **Sigma** for signature and behavioral logic,
- **CTI/IoC** for intelligence-driven matching,
- **Anomaly** for time-series deviation detection.

This combination is key to explain because customers rarely succeed with one approach alone.

### Rules catalog and operational structure

The Rules Catalog is not only a list; it is an operational control plane:

- verified rules maintained by Sekoia teams,
- customer custom rules,
- integration-related rules,
- filtering and bulk activation controls,
- effort-level classification,
- lifecycle states and deprecation handling.

Documented rule coverage includes more than 1000 verified rules.

### Effort levels and practical rollout

Effort levels (from elementary to master) provide a pragmatic adoption path:

- low-friction baseline enablement first,
- gradually add higher-effort, higher-noise-potential detections as maturity grows.

This model is very useful for customers with limited analyst capacity.

### Rule quality and tuning controls

Sekoia Defend provides several mechanisms for maintaining signal quality:

- alert filters with auditable impact,
- entity/asset scoping,
- Sigma pattern testing (with documented scope limits),
- lifecycle transparency and changelog visibility.

### MITRE ATT&CK and coverage conversation

Rules map to ATT&CK-oriented security profile views, enabling coverage discussions in customer language that aligns with threat-informed defense practices.

### SE narrative tip

When buyers ask “How do we avoid noise?”, connect this whole section as a system:

- staged activation + scope tuning + filter governance + testing.

---

## 4.8 Sigma and correlation logic

### Why this matters for SE credibility

Even non-detection-engineer SEs should understand the Sigma model well enough to explain how simple detections scale into multi-event logic.

### Sigma basics in Sekoia Defend

Sigma rules evaluate normalized event fields in real time. Rules are expressed as YAML patterns and support:

- mapped field matching,
- list/wildcard logic,
- modifiers,
- condition composition.

### Correlation support

Sekoia Defend supports Sigma correlation patterns for multi-event use cases, including:

- event count logic,
- value count logic,
- temporal proximity logic,
- chaining patterns for more complex behavior sequences.

This is useful when customers ask for higher-fidelity attack chain detections rather than single-event triggers.

### SE demo suggestion

Show one simple Sigma rule first, then show a correlation example to illustrate maturity progression.

---

## 4.9 CTI/IoC detection and retrohunt

### Operational concept

CTI detection in Sekoia Defend matches telemetry against curated indicator sets and can retroactively search historical data when new indicators become available.

### What to explain clearly

- The built-in Sekoia Intelligence Feed rule offers immediate CTI detection baseline.
- CTI matching runs on ingested events and creates alerts when indicators are found.
- Retrohunt extends value by re-checking relevant historical windows when threat intelligence evolves.
- Customers can use their own IoC collections for custom CTI strategies.

### Why customers care

This directly addresses a common SOC pain: the threat is identified after the initial event window. Retrohunt reduces that timing gap.

### SE tip

If a customer asks “Do we miss attacks discovered late?”, this section is your direct answer.

---

## 4.10 Anomaly detection and behavior monitoring

### Role in the detection stack

Anomaly detection is complementary. It does not replace deterministic detections; it helps surface unusual behavior changes that may not map cleanly to known signatures.

### Documented scope

Sekoia Defend anomaly rules support univariate time-series analysis with configurable:

- query scope,
- aggregation method,
- bucket interval,
- directionality (high/low/both),
- thresholding and severity.

Documented alert timing behavior includes a delay formula tied to interval selection.

### Why this matters to SE positioning

This is useful for customers trying to detect:

- account abuse pattern shifts,
- traffic volume anomalies,
- unusual operational drift that indicates attack preparation or active compromise.

### Implementation expectation setting

Set expectations that anomaly tuning is iterative and benefits from stable telemetry baselines.

---

## 4.11 Alert operations and prioritization model

### Alert object fundamentals

Alerts are generated when events match active detection logic. In Sekoia Defend, alert handling includes lifecycle controls, urgency scoring, and similarity logic.

### Urgency model

Documented urgency computation combines:

- detection rule severity,
- asset criticality.

This keeps prioritization tied to both threat signal and business impact.

### Similarity and occurrences

Alert similarity strategies group repeated matching events into occurrences. This helps avoid unnecessary alert sprawl and makes analyst workloads more manageable.

### Workflow customization

Custom statuses and verdicts can be used to align platform workflow with SOC process language, including shared vocabulary across alerts and cases.

### SE demo guidance

Show:

1. Alert urgency details.
2. Occurrence behavior.
3. Status and verdict configuration concept.
4. How these choices affect operational reporting.

---

## 4.12 Cases, collaboration, and investigation depth

### Why cases are central

In real incidents, analysts rarely deal with a single alert in isolation. Cases are the mechanism for consolidating findings, decisions, tasks, and evidence.

### Case model

Cases in Sekoia Defend support:

- alert grouping,
- assignees and priorities,
- comments/timeline,
- tasks/subtasks,
- associated event evidence,
- graph investigation.

### Graph investigation value

Graph investigation provides a visual correlation layer across:

- observables,
- relationships,
- CTI objects,
- linked event context.

Layer controls allow analysts to keep complex incidents understandable and navigable.

### Why this matters to buyers

- Improves multi-analyst collaboration quality.
- Improves traceability for post-incident review and governance.
- Reduces context loss between triage and deeper analysis.

---

## 4.13 Events exploration and hunt workflows

### Events experience purpose

Events are the raw investigative substrate. Sekoia Defend gives analysts structured search, filtering, column control, history, export, and case pivot capabilities.

### Key analyst benefits

- Quick value-based pivots from smart descriptions and details.
- Reusable search patterns through history and saved workflows.
- Direct event-to-case association for evidence capture.
- Context enrichment overlays to improve interpretation.

### Why this matters for new SEs

Many customer technical evaluators benchmark XDR/SIEM platforms by event investigation usability. Demonstrating this flow clearly is often more persuasive than discussing abstract architecture.

---

## 4.14 Query Builder, SOL, and reporting analytics

### Query model

Sekoia Defend supports two query modes:

- **Form mode** for guided construction.
- **Code mode** with **SOL** for advanced analysts.

SOL is a pipe-based language with SQL/KQL-style familiarity and supports multiple data sources across events, alerts, cases, intakes, entities, assets, and telemetry datasets.

### Reporting layer

Dashboards combine:

- built-in widgets for immediate operational visibility,
- query-based widgets for custom metrics and narratives.

Built-in risk-level and activity widgets help customers track both SOC posture and operational workload.

### Why this matters commercially

- Supports technical depth for analysts.
- Supports communication depth for managers and executives.
- Supports measurable SOC value storytelling.

### SE demo guidance

Show one incident investigation query and one management KPI query in the same session to demonstrate cross-audience value.

---

## 4.15 Automation and ecosystem extensibility

### Integration posture

Sekoia Defend includes an integrations catalog and documented automation patterns for connecting with external security and IT systems.

### What this enables

- ingestion integration breadth,
- action/trigger integration for playbook workflows,
- synchronization and notification use cases,
- enrichment actions and response-adjacent workflows,
- custom integration development/import paths.

### Why this matters in enterprise deals

Most customers require coexistence with existing controls. Extensibility and integration maturity are often mandatory, not optional.

### SE positioning tip

Position Sekoia Defend as an operating layer that can orchestrate with the current stack, then evolve with the customer’s architecture over time.

---

## 4.16 AI capabilities (deep workflow coverage)

### AI model in Sekoia Defend

Sekoia Defend uses AI in two complementary layers:

- **Roy Assistant** for analyst-assist workflows.
- **AI Cases** for automated case correlation and summarization.

The key SE message: AI is positioned as acceleration for human analysts, not autonomous replacement.

### Roy Assistant - what it supports

Documented Roy capabilities include assistance across multiple daily SOC workflows:

- conversational guidance from the platform interface,
- support for Sigma rule drafting,
- support for query construction in natural language,
- support for explaining selected event attributes,
- support for navigating product documentation context,
- awareness of current threat-intelligence context.

This is important for customer teams with mixed maturity. Junior analysts gain faster guidance; senior analysts gain speed on repetitive drafting tasks.

### Roy Assistant - security and trust framing

Documented trust points include:

- privacy-oriented handling posture in assistant interactions,
- explicit recommendation to validate critical AI outputs,
- secured model hosting description for data-processing AI scenarios.

SE note: always frame AI outputs as “assistive draft + analyst validation.”

### AI Cases - what it supports

AI Cases is designed to reduce case management overhead by:

- correlating related alerts into incident-level cases,
- generating and updating case descriptions,
- updating priority based on incoming alert context,
- keeping case context current during active windows.

### AI conversation framework for customer calls

When discussing AI with customers, structure it as:

1. **Workflow support**: where exactly AI saves time.
2. **Control model**: analysts remain decision-makers.
3. **Reliability model**: validate outputs before action.
4. **Outcome model**: reduced manual overhead and faster orientation.

### Optional baseline-PDF narrative

The baseline PDF also describes broader AI assistant positioning and use examples. Treat those points as package/tenant-validated commitments during active pre-sales cycles.

---

## 5. A complete SE demo storyline (for teams new to Sekoia)

Use this sequence if you need one reliable, repeatable technical story:

1. **Start with entity + intake onboarding** to anchor data foundation.
2. **Show ingestion health** (valid/invalid/warning and lag) to establish operational credibility.
3. **Activate and inspect detections** in rules catalog with effort-level framing.
4. **Trigger or inspect a representative alert** and explain urgency + similarity.
5. **Pivot into events and case workflow** to show investigation depth.
6. **Open graph investigation** to illustrate context correlation.
7. **Use Query Builder/SOL** to produce an analyst and management view.
8. **Show dashboards** and tie to executive communication.
9. **Show AI workflow assist** (Roy prompt + AI Cases behavior).
10. **Close with integration/automation path** for coexistence with current tools.

This progression works well for both technical evaluators and mixed business-technical buying groups.

---

## 6. Key technical concepts every SE should master

1. Intakes, formats, entities, and ingestion health.
2. Parsing quality and normalized data quality impact.
3. Rule types and where each detection engine is strongest.
4. Effort levels, activation strategy, and filter governance.
5. Urgency scoring and asset criticality influence.
6. Case workflows, graph investigation, and evidence linking.
7. Query Builder vs SOL usage patterns.
8. Hot/cold retention and rehydration boundaries.
9. Roy and AI Cases scope with analyst-in-the-loop guardrails.

---

## 7. Objection handling (expanded)

### Objection 1: "We already have SIEM and SOAR."

Response:
Sekoia Defend can be positioned either as a primary XDR operating layer or as a complementary layer integrated with existing tooling. The value is not just "more alerts"; it is better signal operations and investigation coherence.

Technical anchors:

- multi-engine real-time detection,
- rule operations maturity,
- case-centric investigation flows,
- integration and playbook extensibility.

### Objection 2: "We are worried about alert noise."

Response:
Sekoia Defend includes staged enablement and tuning controls designed for noise governance: effort-level strategy, scope controls by entity/asset, alert filters, and pattern testing.

Technical anchors:

- effort levels,
- active filter auditing,
- Sigma testing,
- lifecycle controls.

### Objection 3: "How do detections stay current?"

Response:
Verified rule maintenance, changelog visibility, lifecycle states, and auto-enable options support continuous detection posture updates with governance controls.

### Objection 4: "Analysts lose too much time in investigations and case writing."

Response:
Sekoia Defend addresses this through workflow AI and structured case operations. Roy assists analysts in query/rule/investigation tasks; AI Cases reduces manual case correlation and summary overhead.

### Objection 5: "Retention and historical search are hard in our environment."

Response:
The hot/cold architecture with rehydration workflows supports operational speed plus longer-horizon access, with clear contractual boundaries for data permanence.

### Objection 6: "We have too many tools already."

Response:
Sekoia Defend is designed to connect with heterogeneous ecosystems through integrations and automation patterns, enabling phased adoption rather than disruptive replacement.

---

## 8. RFP-ready answer bank (expanded language)

Note: Replace organization-specific placeholders before submission.

### 8.1 Platform architecture

Q: Describe the architecture of your detection and response platform.

Answer:
Sekoia Defend is an XDR platform that unifies telemetry collection, event normalization, real-time detection, incident investigation, and security reporting. Data is ingested through configurable intakes (push and pull), processed into a consistent operational model, and continuously evaluated by multiple detection engines including Sigma, CTI/IoC, and anomaly detection. Analysts work through alert and case workflows that provide contextual enrichment, collaboration features, and investigation pivots. Reporting is supported through dashboards and query tooling (Query Builder and SOL) for both operational and managerial audiences.

### 8.2 Data ingestion and telemetry operations

Q: What ingestion methods and data quality controls are available?

Answer:
Sekoia Defend supports both push and pull intake models to accommodate diverse source constraints. The platform includes operational telemetry and controls for ingestion quality, including valid/invalid/warning event visibility, connector status and logs for pull intakes, event delivery lag indicators, and inactivity notification options. These controls support reliable onboarding and production monitoring of collection pipelines.

### 8.3 Detection coverage and lifecycle

Q: Describe detection coverage and rule lifecycle management.

Answer:
Sekoia Defend provides a Rules Catalog with verified rules, integration rules, and custom customer rules. The platform supports Sigma (including correlation), CTI/IoC, and anomaly rule types. Rule operations include effort-level classification, filtering, scope controls, lifecycle states (active/scheduled for deprecation/deprecated), and associated notifications. This model supports both broad baseline coverage and organization-specific tuning.

### 8.4 False positive and noise reduction

Q: How does your platform reduce false positives?

Answer:
Sekoia Defend supports multiple signal quality controls: alert filters with auditability, entity and asset scoping, duplication/customization of rules where required, and Sigma pattern testing against historical data for supported scenarios. Together, these controls enable staged tuning without losing governance visibility.

### 8.5 Threat intelligence operations

Q: How is threat intelligence operationalized?

Answer:
Sekoia Defend supports CTI/IoC detections through indicator matching on ingested events, including support for the built-in Sekoia Intelligence Feed rule and customer-managed IoC collections. The platform includes retrohunt workflows to re-evaluate relevant historical windows when new indicators become available.

### 8.6 Anomaly and behavioral detection

Q: Do you support behavioral/anomaly detection?

Answer:
Yes. Sekoia Defend includes anomaly detection for univariate time-series analysis with configurable query scope, aggregation methods, intervals, anomaly direction, thresholding, and severity controls. This capability complements signature and IoC detections by identifying unusual behavioral deviations from established baselines.

### 8.7 Incident investigation and case management

Q: Describe incident triage and case handling capabilities.

Answer:
Sekoia Defend supports configurable alert workflows with urgency scoring and similarity-based occurrence grouping. Analysts can escalate or consolidate findings in cases with assignees, priorities, comments/timeline, tasks/subtasks, and linked event evidence. Investigation tooling includes events pivots, graph-based analysis, and contextual enrichment tied to assets and threat intelligence.

### 8.8 AI support across workflows

Q: What AI capabilities are available and how are they used?

Answer:
Sekoia Defend provides AI at two levels. Roy Assistant supports analyst workflows through natural-language assistance for platform navigation, query building, Sigma drafting, and event context interpretation. AI Cases supports incident workflows by correlating related alerts into case objects, generating and updating case descriptions, and dynamically adjusting case priority as incident context evolves. These capabilities are designed for analyst-in-the-loop usage, with human validation of critical decisions.

### 8.9 Reporting and SOC metrics

Q: How does the platform support operational and executive reporting?

Answer:
Sekoia Defend provides built-in and custom dashboards with widget-based visualization. Query Builder and SOL support advanced analytics across events, alerts, cases, assets, intakes, entities, and telemetry datasets. This enables SOC teams to report on activity, detection performance, risk indicators, and investigation outcomes for both technical and non-technical stakeholders.

### 8.10 Retention and historical access

Q: Describe your retention and historical investigation model.

Answer:
Sekoia Defend uses a tiered retention architecture with hot storage for immediate search and optional cold storage for archival purposes. Archived data can be rehydrated for investigation workflows under subscription and contractual constraints. This model balances operational performance with longer-term retention requirements.

### 8.11 Multi-scope operations

Q: How does the platform support segmented or multi-tenant operations?

Answer:
Sekoia Defend supports segmentation using entities and community constructs, enabling scoped collection, alerting, and reporting practices. Alert and case workflows can share status/verdict models to improve consistency. Query and reporting layers support cross-scope operational oversight where applicable.

### 8.12 Integration and extensibility

Q: Can the platform integrate with third-party systems and custom workflows?

Answer:
Yes. Sekoia Defend includes an integrations catalog and automation-oriented components (including triggers/actions and playbook use cases), and supports custom integration development/import workflows for organizations requiring tailored ecosystem connectivity.

---

## 9. Discovery checklist for SEs before first deep demo

1. Which telemetry domains are in scope now vs later (endpoint, identity, cloud, network, SaaS)?
2. Which pain is most urgent: ingestion reliability, detection quality, triage speed, reporting, or integration?
3. Is the customer seeking replacement, coexistence, or phased migration?
4. What retention and audit constraints apply?
5. Which KPIs are decision-critical (MTTD, MTTR, alert backlog, risk trend, coverage)?
6. What is their AI posture (assistive only, governance requirements, validation expectations)?

---

## 10. Glossary for new SEs

- **Intake**: A configured data source connection for event ingestion.
- **Entity**: A logical operational grouping for data sources and alerts.
- **Asset**: A host/account/network object with contextual and prioritization attributes.
- **Occurrence**: Repeated matching events grouped under an alert by similarity strategy.
- **Urgency**: Risk prioritization score derived from rule severity and asset criticality.
- **Retrohunt**: Retroactive detection process triggered when new IoCs become available.
- **SOL**: Sekoia Operating Language for advanced query and analytics workflows.