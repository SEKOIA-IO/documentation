---
title: "Quick start: Reveal"
description: "Get started with Sekoia Reveal, the asset intelligence add-on module that brings asset context, vulnerability data, and attack path visualization into your investigation workflows."
keywords: [reveal, asset intelligence, quick start, asset context, vulnerability, points of interest, hygiene, attack path]
audience: analyst
module: reveal
type: tutorial
---

# Quick start: Reveal

Sekoia Reveal is an add-on module that adds an asset intelligence layer to your Sekoia Defend environment. It continuously discovers and contextualizes assets from your event data, endpoint agents, and connected tools, and surfaces this context directly inside your alert and case investigation workflows. This article explains what Reveal enables and how to get started.

## What Reveal adds to your workflow

Without Reveal, an alert tells you that an event matched a detection rule. With Reveal, the same alert immediately answers:

- What is this asset, and how critical is it to my organization?
- Is it vulnerable to known CVEs?
- What unusual activity has occurred on it recently?
- Which other assets could it reach or put at risk?

Reveal surfaces this context through the **asset context panel**, which is accessible from any alert, case, event, or asset view.

## Key capabilities

| Capability | What it does |
|---|---|
| **Asset context panel** | Shows asset identity, vulnerabilities, hygiene signals, and behavioral history in one place during triage |
| **Points of Interest** | Surfaces behavioral anomalies on assets (unusual authentication, rare locations) without requiring a separate alert |
| **Attack Path Visualization** | Maps relationships between assets to identify lateral movement paths during an active investigation |
| **Endpoint Hygiene** | Shows posture signals for endpoints (firewall status, disk encryption) when the Sekoia Endpoint Agent or a supported connector is deployed |
| **Vulnerability enrichment** | Shows which CVEs affect an asset, drawn from connected vulnerability scanners |

## Prerequisites

Before you can start using Reveal:

- The **Reveal module** must be enabled for your community. Contact your account manager if it is not active.
- At least one supported telemetry source must be sending events to Sekoia. Passive asset discovery starts automatically as soon as events arrive.

You do not need all data sources to begin. Each source you add unlocks additional Reveal capabilities.

## How to set up Reveal

The full setup guide is available in the Sekoia Defend documentation. It walks you through four steps:

1. Onboard telemetry to start passive asset discovery
2. Validate event data coverage for activity-based features
3. Configure asset connectors to enrich assets with structured data
4. Deploy the Sekoia Endpoint Agent for direct endpoint visibility

Follow the complete guide here: [Getting started with Reveal](https://docs.sekoia.com/xdr/features/modules/reveal_index/)

## What to do after setup

Once Reveal is configured, open any alert and click on an affected asset to open the asset context panel. Review the asset's identity, recent activity timeline, hygiene signals, and vulnerability list directly within your investigation.

> 📸 [SCREENSHOT SUGGESTION: The asset context panel open within an alert, showing asset identity, vulnerability list, and recent activity timeline. | ALT TEXT: Asset context panel showing asset details, vulnerabilities, and activity history during alert investigation.]

## Related links

- [Getting started with Reveal](https://docs.sekoia.com/xdr/features/modules/reveal_index/) — Full setup guide with step-by-step instructions for all data source types.
- [Workspace setup overview](/getting_started/workspace_setup_overview.md) — Admin checklist for enabling modules and preparing your workspace.
- [Glossary](/getting_started/glossary.md) — Definitions of asset, atom, point of interest, and vulnerability enrichment.
