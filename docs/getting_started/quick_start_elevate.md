---
title: "Quick start: Elevate"
description: "Get started with Sekoia Elevate, the AI-powered agentic triage module that autonomously analyzes alerts and generates verdicts."
keywords: [elevate, ai triage, agentic, quick start, alert triage, verdict, runbook, automation]
audience: analyst
module: elevate
type: tutorial
---

# Quick start: Elevate

Sekoia Elevate is an AI-powered add-on module that autonomously triages security alerts. For each alert it processes, Elevate analyzes the available context, executes a runbook, and produces a verdict with supporting evidence, reducing the volume of repetitive manual triage work for your analysts.

!!! note "Documentation in progress"
    The Elevate module is currently being finalized. This quick start guide will be updated with full setup instructions when the module becomes generally available. Check the [changelog](https://changelog.sekoia.com) for release announcements.

## What Elevate does

Elevate acts as an autonomous analyst that works alongside your team. For each alert it handles, Elevate:

1. Collects relevant context from the alert, the associated asset, and threat intelligence
2. Executes a runbook that defines the investigation logic for that alert type
3. Produces a verdict (true positive or false positive) with a written explanation
4. Surfaces the result in the alert for human review

Analysts review Elevate's output and either accept the verdict or override it based on their judgment.

## Prerequisites

- The **Elevate module** must be enabled for your community.
- You have an active Sekoia Defend subscription.

## What comes next

Full setup instructions, runbook configuration guidance, and analyst workflow documentation will be available here once Elevate is released.

In the meantime, you can:

- Read the [Elevate overview article](https://docs.sekoia.com/xdr/features/modules/elevate_overview/) for an early look at the module's capabilities.
- Set up your [workspace](/getting_started/workspace_setup_overview.md) and ensure Defend is fully operational using the [Defend quick start](/getting_started/quick_start_defend.md).

## Related links

- [Quick start: Defend](/getting_started/quick_start_defend.md) — Prerequisite for Elevate: ensure Defend is set up and generating alerts.
- [Support and resources](/getting_started/support_and_resources.md) — Contact support or check the Academy for early access materials.
