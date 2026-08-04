---
title: "Quick start: Elevate"
description: "Get oriented with Sekoia Elevate, the AI-powered agentic triage module that autonomously investigates alerts and generates verdicts so analysts can focus on confirmed threats."
keywords: [elevate, agentic triage, ai agents, alert investigation, verdict, runbook, findings, quick start]
audience: analyst
module: elevate
type: tutorial
---

# Quick start: Elevate

Sekoia Elevate is the AI layer of the Sekoia platform. When a new alert arrives, the Elevate investigation agent (Roy) runs a full investigation autonomously without waiting for an analyst to open the alert. It produces a verdict, a confidence score, and a complete audit trail, so analysts can focus on confirmed threats rather than repetitive triage.

## What Elevate does

For each incoming alert, the Elevate agent:

- Assesses whether the alert is a true positive or a false positive.
- Collects and correlates evidence across all your ingested data sources.
- Enriches findings with threat intelligence and contextual signals.
- Produces a verdict with a confidence score and a plain-language explanation.
- Logs every action and reasoning step so analysts can review and override at any time.

Elevate also investigates cases. Assign a case to Roy and it produces a verdict, findings, and reasoning questions at the case level.

!!! note "Private by architecture"
    All AI computation runs on Sekoia infrastructure. No data is sent to external LLM providers, which makes Elevate suitable for regulated environments.

## Key concepts

| Concept | Definition |
|---|---|
| **Verdict** | The outcome of the investigation: True Positive or False Positive, with a confidence score and explanation. Analysts can override any verdict. |
| **Findings** | Individual evidence items the agent collected. Each finding links to the exact query or search the agent ran to reach it. |
| **Runbook** | The investigation guide tied to a detection rule. It defines what the detection catches, likely false positive scenarios, and the reasoning questions the agent works through. Sekoia generates one runbook per detection rule automatically. |
| **Runs** | Each investigation consumes one run from your monthly run pack. Runs reset at the start of each month. |

## Before you start

- The **Elevate module** must be included in your Sekoia subscription. Verify in **Settings > Subscriptions**.
- You must have administrator access to activate the agent.
- At least one intake must be configured and sending events to Sekoia.

## Activate Elevate

The Elevate agent is disabled by default. Enabling it starts automatic analysis of all new incoming alerts.

!!! warning "Run consumption starts immediately"
    Enabling auto-analyze triggers analysis of all new incoming alerts across all communities. Each analysis consumes one run from your monthly run pack. Review your run pack before activating.

For step-by-step activation, see [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate/).

## Go further

Once Elevate is active, explore these guides to tune and get the most out of it:

- [Elevate overview](/xdr/features/modules/elevate_overview/): Full concept guide covering the investigation method, runbooks, verdicts, and key concepts.
- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert/): How to read a verdict, findings, and reasoning questions.
- [Add custom instructions](/xdr/features/modules/elevate_custom_instructions/): Teach the agent about your environment to improve verdict accuracy.
- [Manage your Elevate runs](/xdr/features/modules/elevate_quota/): Monitor consumption and optimize your monthly run pack.

## Related links

- [Workspace setup overview](/getting_started/workspace_setup_overview): Admin checklist for enabling modules and preparing your workspace.
- [Quick start: Defend](/getting_started/quick_start_defend): Complete the Defend quick start before setting up Elevate.
- [Glossary](/getting_started/glossary): Definitions for alert, verdict, runbook, and agentic triage.
