---
title: What is Sekoia
keywords:
  - sekoia
  - soc platform
  - xdr
  - cti
  - defend
  - intelligence
  - reveal
  - elevate
  - ai soc
  - detection
  - response
audience: all
module: all
type: concept
description: >-
  Sekoia is the European agentic cybersecurity company building autonomous cyber
  defense for the AI era.
---

# What is Sekoia

gloIts security platform connects threat intelligence, customer context, investigation memory, AI models, security capabilities, and response actions. This enables machines to investigate and act at scale while security teams set objectives, policies, and controls.

Sekoia brings threat detection, investigation, response, cyber threat intelligence, asset context, and agentic AI together in one security operations platform. It helps security teams reduce noise, understand threats with more context, and respond with greater speed and confidence.

<div data-with-frame="true"><figure><img src=".gitbook/assets/Sekoia_stack.png" alt="Overview of the Sekoia security operations platform stack, connecting threat intelligence, customer context, investigation memory, AI agents, and response action"><figcaption><p>The Sekoia platform connects intelligence, context, investigation, and action so security teams can govern operations with clarity and control.</p></figcaption></figure></div>

### What can Sekoia help you do?

Security teams use Sekoia to:

* Collect security data from endpoints, networks, cloud services, applications, and other sources
* Detect threats using detection rules, behavioral analytics, threat intelligence, and AI reasoning
* Investigate alerts and incidents with historical data, asset context, and attacker knowledge
* Hunt for threats across their environment
* Automate repetitive triage and response workflows
* Understand their threat landscape through cyber threat intelligence
* Govern security operations while AI agents handle investigations at scale

Sekoia consolidates capabilities that are often spread across multiple tools, including SIEM, XDR, SOAR, cyber threat intelligence, asset intelligence, and AI-assisted security operations.

### Sekoia capabilities

Sekoia is built around a unified security operations platform and a set of integrated products and modules. Depending on your subscription and role, you may have access to some or all of the following capabilities.

#### Sekoia Defend

Sekoia Defend provides the detection and response foundation of the platform. It collects security data from across your environment, applies continuously updated detection content, and gives analysts the tools they need to investigate alerts and automate response actions.

Defend supports the main stages of security operations:

| Capability      | What it does                                                                                               |
| --------------- | ---------------------------------------------------------------------------------------------------------- |
| **Collect**     | Ingests logs and security events from endpoints, cloud services, networks, applications, and other sources |
| **Detect**      | Applies detection rules and analytics to identify suspicious activity and generate alerts                  |
| **Investigate** | Provides alert triage, event history search, case management, and investigation workflows                  |
| **Respond**     | Helps analysts contain threats and execute response actions                                                |
| **Automate**    | Runs playbooks to enrich alerts, trigger actions, and connect with external tools                          |
| **Report**      | Provides dashboards and metrics to monitor security coverage and operational performance                   |

Start with the Quick start: [Defend guide](defend.md).

#### Sekoia Intelligence

Sekoia Intelligence provides cyber threat intelligence maintained by Sekoia's Threat Detection and Research team.

The knowledge base includes threat actors, malware families, attack campaigns, indicators of compromise, tactics, techniques, procedures, and analytical reports.

Sekoia Intelligence helps security teams:

* Search and explore threat intelligence
* Enrich alerts and investigations with attacker context
* Identify relationships between threat actors, malware, campaigns, and indicators
* Create intelligence feeds for a specific sector, geography, or threat type
* Use threat intelligence to improve detection and threat hunting

Threat intelligence integrates directly with Sekoia Defend, allowing analysts to connect external attacker knowledge with activity observed in their own environment.

Start with the Quick start: Intelligence guide.

#### Sekoia Reveal

Sekoia Reveal provides asset and exposure intelligence for security operations.

It gives analysts a unified view of assets, identities, vulnerabilities, endpoint hygiene signals, behavioral anomalies, and potential attack paths. This context is surfaced directly in alert and case investigation workflows.

Reveal helps security teams understand:

* Which assets are affected by an alert
* Who owns or uses an asset
* Whether an asset is exposed or vulnerable
* How suspicious activity relates to the organization's environment
* Which assets may be connected through an attack path

Start with the Quick start: Reveal guide.

#### Sekoia Elevate

Sekoia Elevate is the agentic SOC analyst layer of the platform.

Elevate autonomously analyzes security alerts, correlates relevant evidence, investigates activity, and provides an explainable verdict. It can also execute configured runbook steps, allowing analysts to spend less time on repetitive triage and more time on decisions that require human judgment.

Sekoia Elevate is designed around a clear division of responsibilities:

* **Machines investigate and act at scale**
* **Security teams set intent, policy, and control**

Start with the Quick start: Elevate guide.

### How Sekoia differs from traditional security tools

Security teams often rely on several tools that have limited context about one another. Sekoia connects these capabilities in one platform.

| Traditional capability              | Typical purpose                                  | How Sekoia addresses it                                                                |
| ----------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------- |
| **SIEM**                            | Collects and analyzes security logs              | Sekoia Defend collects security data and detects suspicious activity                   |
| **XDR**                             | Correlates signals across security domains       | Sekoia connects detections, telemetry, threat intelligence, and response context       |
| **SOAR**                            | Automates security workflows                     | Sekoia playbooks and response actions automate enrichment and remediation workflows    |
| **Cyber threat intelligence**       | Provides knowledge about attackers and campaigns | Sekoia Intelligence enriches detections and investigations with external context       |
| **Asset intelligence**              | Provides visibility into assets and exposure     | Sekoia Reveal connects alerts to assets, identities, vulnerabilities, and attack paths |
| **AI-assisted security operations** | Helps analysts process security data             | Sekoia Elevate investigates alerts and provides explainable verdicts                   |

The goal is not only to generate more alerts. Sekoia connects data, intelligence, context, investigation, and action so security teams can make better decisions with less manual effort.

### The Autonomous SOC approach

Sekoia's approach to security operations is based on collaboration between machines and humans.

Machines can process large amounts of security data, correlate evidence, investigate alerts, and recommend or execute actions. Security teams remain responsible for setting objectives, defining policies, validating decisions, and governing operations.

This approach helps organizations move from manual alert processing to supervised autonomous defense.

### Roy, the Sekoia AI assistant

Roy is Sekoia's built-in AI assistant. Roy is available across the platform and helps analysts:

* Explain complex event fields in natural language
* Generate Sigma detection rules from a description
* Build search queries using plain language
* Find relevant information in the Sekoia documentation

Roy supports analysts during their daily work. It does not replace the investigation workflows, controls, and governance provided by the Sekoia platform.

### Choose your getting started path

Your next step depends on your role and the products available in your workspace.

| Role                        | Start here                                              | What you will do                                                                     |
| --------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Defend analyst**          | Quick start: [Defend](defend.md)                        | Connect a data source, activate detection content, and investigate your first alerts |
| **Intelligence analyst**    | Quick start: [Intelligence](intelligence.md)            | Search threat intelligence, explore reports, and create a feed                       |
| **Reveal user**             | Quick start: [Reveal](reveal.md)                        | Explore assets, exposure, vulnerabilities, and attack paths                          |
| **Elevate user**            | Quick start: [Elevate](elevate.md)                      | Configure agentic triage and review investigation verdicts                           |
| **Workspace administrator** | [Workspace setup overview](workspace_setup_overview.md) | Configure your workspace, invite users, assign roles, and connect integrations       |

If you are new to Sekoia, start with the Workspace setup overview, then follow the quick start guide for the products available in your workspace.

### Frequently asked questions

#### Is Sekoia a SIEM?

Sekoia provides SIEM capabilities through Sekoia Defend, including security data collection, detection, alert management, investigation, dashboards, and response workflows.

Sekoia also connects these capabilities with threat intelligence, asset context, and agentic AI.

#### Is Sekoia an XDR platform?

Sekoia Defend provides extended detection and response capabilities. It correlates security signals across your environment and connects detection, investigation, threat intelligence, and response workflows in one platform.

#### What is an Autonomous SOC?

An Autonomous SOC uses automation and AI agents to investigate security activity, reduce repetitive manual work, and support response actions.

Human analysts remain responsible for objectives, policies, approvals, and operational governance.

#### What is agentic AI in cybersecurity?

Agentic AI refers to AI systems that can perform multi-step tasks, such as gathering evidence, correlating events, investigating an alert, explaining a verdict, and recommending or executing an action.

In Sekoia, agentic AI operates within the context and controls of the security platform.

#### Does Sekoia include cyber threat intelligence?

Yes. Sekoia Intelligence provides continuously updated cyber threat intelligence, including information about threat actors, malware, campaigns, indicators, and attacker techniques.

This intelligence can enrich detections, investigations, and threat hunting in Sekoia Defend.

#### What products are available in Sekoia?

Sekoia provides several integrated capabilities, including Sekoia Defend for detection and response, Sekoia Intelligence for cyber threat intelligence, Sekoia Reveal for asset and exposure intelligence, and Sekoia Elevate for agentic alert investigation.

The products available to you depend on your subscription and workspace configuration.

### Related links

* [Workspace and communities](workspace_and_communities.md): Learn how Sekoia organizes your environment and what each level controls.
* [Workspace setup overview:](workspace_setup_overview.md) Configure your workspace, invite users, assign roles, and prepare your integrations.
* [Glossary](glossary.md): Find definitions for key Sekoia, security operations, and cybersecurity terms.
* [Quick start: Defend](defend.md): Connect a data source, activate detection content, and investigate your first alerts.
* [Quick start: Intelligence](intelligence.md): Search threat intelligence, explore reports, and create a feed for your organization.
* [Quick start: Reveal](reveal.md): Configure asset intelligence and explore asset, exposure, and vulnerability context.
* [Quick start: Elevate](elevate.md): Configure agentic triage and review investigation verdicts, evidence, and reasoning.
