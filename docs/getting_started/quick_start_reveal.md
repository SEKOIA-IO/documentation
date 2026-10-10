---
title: "Quick start: Reveal"
description: "Get oriented with Sekoia Reveal, the asset intelligence add-on module that adds asset context, vulnerability data, and attack path visualization to your investigation workflows."
keywords: [reveal, asset intelligence, quick start, asset context, vulnerability, points of interest, attack path]
audience: analyst
module: reveal
type: tutorial
---

# Quick start: Reveal

Sekoia Reveal is an add-on module that adds an asset intelligence layer to your Sekoia Defend environment. It enriches your alerts with asset context so you can triage faster and investigate with more precision.

## What Reveal adds to your workflow

Without Reveal, an alert tells you what happened. Reveal helps you understand what it means for your organization, how urgently it should be investigated, and what to prioritize next.

From any alert, you can quickly determine:

- What asset is involved, who it belongs to, and how critical it is to the organization.
- Which applications, vulnerabilities, and known CVEs increase its exposure.
- What risk signals, unusual behaviors, or Points of Interest have recently been observed.
- Why the asset is considered risky and which factors contribute to its risk score.
- Which connected assets or systems could also be exposed.

This context is surfaced through the **asset context panel**, available within alerts, cases, events, and asset views. Analysts get the information they need without leaving their investigation workflow.

## Before you start

- The **Reveal module** must be enabled for your community. Contact your account manager if it is not already active.
- Connect at least one data source:
    - **Telemetry sources** enable passive asset discovery as events are ingested.
    - **Asset connectors** synchronize asset data from supported third-party platforms for richer context.

You do not need every source to start. Reveal becomes more capable as you add sources over time.

## Set up Reveal

The full setup guide covers telemetry onboarding, asset connector configuration, and Sekoia Endpoint Agent deployment.

Follow the complete guide: [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md)

## Related links

- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md): Full step-by-step setup guide for all data source types.
- [Workspace setup overview](/getting_started/workspace_setup_overview.md): Admin checklist for enabling modules and preparing your workspace.
- [Glossary](/getting_started/glossary.md): Definitions for asset, point of interest, and vulnerability enrichment.
