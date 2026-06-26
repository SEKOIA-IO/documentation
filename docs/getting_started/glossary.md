---
title: "Glossary"
description: "Definitions of key platform and cybersecurity terms used across Sekoia documentation."
keywords: [glossary, definitions, terms, concepts, xdr, cti, alert, intake, playbook, stix, ioc, ttp]
audience: all
module: all
type: reference
---

# Glossary

This glossary defines key terms used across Sekoia documentation and the broader cybersecurity field. Terms are organized alphabetically. Click any linked term to read the full documentation on that topic.

## A

**Alert**
A security notification generated when an incoming event matches an active detection rule. Alerts have an urgency score, a lifecycle (from Pending to Closed), and contain the events that triggered them. Alerts are the primary unit of work for SOC analysts in Sekoia Defend.
See: [Triage your first alert](/getting_started/defend_step4_triage_first_alert)

**API key**
An authentication token that grants programmatic access to the Sekoia platform. API keys are permissions-based (not role-based) and are used to connect external tools, run integrations, and operate playbooks. A key is only displayed once at creation and must be stored securely.
See: [Manage API keys](/getting_started/manage_api_keys)

**Asset**
Any device, user account, or network element that is part of your monitored infrastructure. Assets in Sekoia have a criticality score that influences alert urgency. They are discovered automatically from event data or added manually.

**Atom**
A unique identifier observed in event data that maps to a specific asset at a given point in time, such as an IP address, hostname, username, or email address. Atoms allow Sekoia to automatically associate events with assets even before a formal asset record exists.

## C

**C2 (Command and Control)**
Infrastructure used by a threat actor to communicate with and control compromised systems. C2 indicators (IP addresses, domains) are tracked in the Sekoia Intelligence database and used in CTI-based detection rules.

**Case**
A container used to group related alerts and document an ongoing investigation. Cases allow analysts to collaborate, track timelines, and record findings across multiple alerts that belong to the same incident.

**Community**
An operational subdivision within a workspace. Communities allow separate configurations, intakes, detection rules, alerts, and user access for different teams or clients. Most day-to-day security operations happen at the community level.
See: [Workspace and communities](/getting_started/workspace_and_communities)

**CVE (Common Vulnerabilities and Exposures)**
A standardized identifier for a publicly known software vulnerability. CVEs are tracked in the Sekoia Intelligence database and can be surfaced in the Reveal module when a vulnerable asset is involved in an alert.

## D

**Detection rule**
A logic pattern that Sekoia applies to your event stream in real time to identify suspicious activity. Detection rules can be Sigma-based (pattern matching), CTI-based (indicator matching), or anomaly-based (statistical deviation). Sekoia provides over 1,000 verified rules mapped to the MITRE ATT&CK framework.
See: [Activate detection rules](/getting_started/defend_step3_activate_detection_rules)

## E

**EDR (Endpoint Detection and Response)**
A security tool that monitors and collects activity data from endpoints (workstations, servers). EDR data is a common intake source in Sekoia Defend.

**Effort level**
A label assigned to each detection rule that indicates how much effort is required to enable it and how likely it is to generate false positives. Levels range from Elementary (low effort, low noise) to Master (requires tuning, high detection specificity).

**Entity**
An organizational grouping for intakes within a community. Entities help you structure your data sources and scope detection rules to specific parts of your infrastructure (for example, a geographic site or a business unit).

**Event**
A normalized log entry ingested from one of your data sources via an intake. Events are the raw material on which detection rules operate. Sekoia normalizes events to the Elastic Common Schema (ECS) to enable technology-agnostic detection.
See: [Verify event reception](/getting_started/defend_step2_verify_event_reception)

## F

**Feed**
A filtered view of the Sekoia Intelligence database, configured by the user to surface only the intelligence relevant to a specific sector, geography, or threat type. Feeds can trigger notifications when new matching content is published.

**FLINT (Flash Intelligence)**
A category of threat report published by Sekoia analysts. FLINT reports are rapid-response analyses published when a significant threat event occurs, such as a new active campaign or a major vulnerability being exploited in the wild. They include indicators of compromise, technical analysis, and recommended actions.

## I

**Indicator**
A threat intelligence object that represents a specific pattern known to be associated with malicious activity. Indicators in Sekoia are always linked to a threat, carry an expiration date, and can automatically trigger alerts in Sekoia Defend when matched against your event stream. Indicators are always derived from one or more observables.

**Intake**
A configured data source connection in Sekoia Defend. An intake defines how logs from a specific technology (firewall, EDR, cloud service, etc.) are collected and normalized. Each intake has a unique intake key used to route incoming data. Intakes can be push-based (you forward logs to Sekoia) or pull-based (Sekoia fetches logs from a source API).
See: [Connect a data source](/getting_started/defend_step1_connect_data_source)

**IOC (Indicator of Compromise)**
A technical artifact, such as a file hash, IP address, domain name, or URL, that provides evidence that a system has been compromised or is in contact with a known threat. In Sekoia Intelligence, an observable becomes an IOC when it is clearly associated with malicious activity and linked to a threat.

**Intrusion set**
A grouped set of adversarial behaviors and resources believed to be orchestrated by a single threat actor or organization. Intrusion sets in the Sekoia Intelligence database group related campaigns, tools, and techniques attributed to a known or suspected threat group.

## M

**MITRE ATT&CK**
A publicly available knowledge base of adversary tactics and techniques observed in real-world cyberattacks. Sekoia maps all verified detection rules to MITRE ATT&CK techniques. The Rules Catalog includes a visual matrix view showing your detection coverage across tactics and techniques.

**Malware**
Software designed to disrupt, damage, or gain unauthorized access to a system. Malware types tracked in Sekoia Intelligence include ransomware, trojans, spyware, rootkits, and more.

## O

**Observable**
A technical artifact extracted from threat intelligence sources, such as an IP address, domain, URL, file hash, or email address. Observables are data points that may indicate a potential threat. An observable becomes an indicator (and potentially an IOC) when it is contextualized, linked to a threat, and given a validity period.

## P

**Playbook**
An automated workflow in Sekoia Defend that executes a sequence of actions in response to a trigger, such as a new alert. Playbooks are used to enrich alerts with external data, change alert statuses automatically, send notifications, or interact with third-party tools.
See: [Automate with playbooks](/getting_started/defend_step5_automate_with_playbooks)

**Point of Interest (PoI)**
A behavioral signal surfaced by the Reveal module that highlights anomalous activity on an asset, such as unusual authentication patterns or access from unexpected locations. Points of Interest appear during triage and investigation without requiring a separate alert.

## R

**Report**
An analytical document published in the Sekoia Intelligence database by Sekoia analysts. Reports cover threat actors, campaigns, malware, and industry-specific threats. They include context, technical indicators, and recommended defensive actions.

**Role**
A set of permissions assigned to a user that determines what they can view and do within a workspace or community. Sekoia has three built-in roles (Guest, Analyst, Admin) and supports custom and restricted roles.
See: [Roles and permissions](/getting_started/roles_and_permissions)

## S

**Sigma rule**
A text-based detection rule written in YAML that describes a pattern of suspicious activity in log data. Sekoia uses Sigma as its primary detection rule format. Analysts can create custom Sigma rules directly in the Rules Catalog.

**SIEM (Security Information and Event Management)**
A traditional security tool that collects and organizes log data and detects threats using static rules. Unlike a SIEM, Sekoia Defend adds native automation, threat intelligence integration, and AI-assisted triage.

**SOC (Security Operations Center)**
The team, tools, and processes responsible for monitoring, detecting, and responding to security threats within an organization. Sekoia is designed to power and augment SOC operations.

**SOAR (Security Orchestration, Automation and Response)**
A category of security technology that automates incident response workflows and integrates multiple security tools. In Sekoia, SOAR capabilities are provided by the Playbooks feature.

**STIX (Structured Threat Information Expression)**
An international standard format for representing and sharing cyber threat intelligence. Sekoia Intelligence stores and exposes all threat objects in STIX 2.1 format, enabling interoperability with other CTI platforms and tools.

## T

**TLP (Traffic Light Protocol)**
A color-coded classification system that defines how threat intelligence can be shared. TLP values used in Sekoia Intelligence:

| TLP | Meaning |
|---|---|
| **White** | No sharing restrictions |
| **Green** | Can be shared within the security community |
| **Amber** | Restricted to the recipient's organization |
| **Red** | Not to be shared outside the direct recipients |

**TTP (Tactics, Techniques, and Procedures)**
A description of how a threat actor operates: their goals (tactics), the methods they use to achieve them (techniques), and the specific tools or behaviors they employ (procedures). TTPs are the basis for the MITRE ATT&CK framework and for Sekoia's detection rule coverage.

## U

**Urgency**
A score between 0 and 100 assigned to each alert in Sekoia Defend. Urgency is calculated from the severity of the triggering detection rule and the criticality of the affected asset. High urgency (75-100) indicates an alert that requires immediate attention.

## W

**Workspace**
The top-level environment in Sekoia that contains all communities, users, and configuration for your organization. Each workspace is isolated and has its own subscription and security settings.
See: [Workspace and communities](/getting_started/workspace_and_communities)

**XDR (Extended Detection and Response)**
A security platform that unifies log collection, threat detection, investigation, and automated response across all layers of an organization's environment (endpoints, networks, cloud, applications). Sekoia Defend is an XDR platform.

## Related links

- [What is Sekoia](/getting_started/what_is_sekoia) — Overview of the Sekoia platform and its product suite.
- [Workspace and communities](/getting_started/workspace_and_communities) — How Sekoia organizes your environment.
- [Roles and permissions](/getting_started/roles_and_permissions) — How user access is structured in Sekoia.
