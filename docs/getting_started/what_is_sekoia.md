---
title: "What is Sekoia"
description: "Sekoia is an AI-powered SOC platform that combines extended detection and response, threat intelligence, and automated triage in a single solution."
keywords: [sekoia, soc platform, xdr, cti, defend, intelligence, reveal, elevate, ai soc, detection, response]
audience: all
module: all
type: concept
---

# What is Sekoia

Sekoia is an AI-powered Security Operations Center (SOC) platform that brings together detection, threat intelligence, and automated response in a single, integrated solution. It is designed to help security teams of all sizes detect threats faster, investigate with more context, and respond with less manual effort.

## The Sekoia platform

Sekoia is built around two core products and a set of AI-powered add-on modules that extend its capabilities.

### Sekoia Defend

Sekoia Defend is the extended detection and response (XDR) product. It collects logs from your entire environment, applies a continuously updated catalog of over 1,000 detection rules mapped to the MITRE ATT&CK framework, and gives you the tools to investigate alerts and automate responses.

Defend operates across five areas:

| Area | What it does |
|---|---|
| **Collect** | Ingests logs from endpoints, cloud services, networks, and applications via intakes |
| **Detect** | Applies detection rules to your event stream in real time to raise security alerts |
| **Investigate** | Provides alert triage, event history search, and case management |
| **Automate** | Runs playbooks to enrich alerts, trigger responses, and connect with external tools |
| **Report** | Surfaces dashboards to monitor security coverage and team performance |

Defend is the foundation of Sekoia. All other products and modules integrate with it.

### Sekoia Intelligence

Sekoia Intelligence is the cyber threat intelligence (CTI) product. It gives you access to a continuously updated knowledge base maintained by Sekoia's expert analysts. The database contains threat actors, malware families, attack campaigns, indicators of compromise, and analytical reports.

Intelligence integrates directly with Defend: threat intelligence enriches your alerts, and indicators from the database power CTI-based detection rules.

Intelligence operates across three areas:

| Area | What it does |
|---|---|
| **Consume** | Search and browse the threat intelligence database, read reports, and explore relationships between threat objects |
| **Customize** | Create feeds to filter intelligence by sector, geography, or threat type |
| **Report** | Build dashboards to track threat trends relevant to your organization |

### Add-on modules

Add-on modules are purchased separately and extend Defend with specialized capabilities.

| Module | What it adds |
|---|---|
| **Reveal** | Adds an asset intelligence layer: a unified asset inventory enriched with vulnerability data, endpoint hygiene signals, behavioral anomalies, and attack path visualization, surfaced directly inside alert and case investigation workflows |
| **Elevate** | Adds AI-powered agentic triage: Elevate autonomously analyzes alerts, generates a verdict, and executes runbook steps, reducing the volume of repetitive triage work for your analysts |

## How Sekoia differs from traditional tools

Security teams often operate multiple tools that do not communicate well with each other. Sekoia consolidates these into a single platform:

| Traditional tool | What it does | How Sekoia covers it |
|---|---|---|
| SIEM | Collects and organizes logs, detects threats using static rules | Sekoia Defend (Collect + Detect) |
| SOAR | Automates incident response workflows | Sekoia Defend (Automate — Playbooks) |
| CTI platform | Provides threat intelligence feeds and analysis | Sekoia Intelligence |
| Asset inventory | Tracks and categorizes infrastructure assets | Sekoia Reveal (add-on) |

By consolidating these capabilities, Sekoia reduces the time between detecting a threat and responding to it, and eliminates the overhead of maintaining separate integrations.

## Roy, the AI assistant

Roy is Sekoia's built-in AI assistant. Roy is available across the platform and helps analysts:

- Explain complex event fields in natural language
- Generate Sigma detection rules from a description
- Build search queries using plain language
- Access platform documentation without leaving the current page

Roy does not retain query history or personal data between sessions.

## What you can do in your first session

Depending on your role and subscription, here is what you can achieve right away:

- **Defend analyst** — Connect a data source, activate detection rules, and receive your first security alert within hours.
- **Intelligence analyst** — Search the threat database, read the latest threat reports, and set up a feed for your sector.
- **Admin** — Configure your workspace, invite your team, assign roles, and create API keys for integrations.

## Related links

- [Workspace and communities](/getting_started/workspace_and_communities.md) — How Sekoia organizes your environment and what each level controls.
- [Glossary](/getting_started/glossary.md) — Definitions of key platform and cybersecurity terms.
- [Quick start: Defend](/getting_started/quick_start_defend.md) — Five-step guide to start using Sekoia Defend.
- [Quick start: Intelligence](/getting_started/quick_start_intelligence.md) — Two-step guide to start using Sekoia Intelligence.
- [Quick start: Reveal](/getting_started/quick_start_reveal.md) — Setup guide for the Reveal asset intelligence module.
