---
title: "Quick start: Intelligence"
description: "A two-step guide to start using Sekoia Intelligence: explore the threat knowledge base and read threat reports."
keywords: [quick start, intelligence, cti, threat intelligence, getting started, tutorial, reports, database]
audience: analyst
module: intelligence
type: tutorial
---

# Quick start: Intelligence

Sekoia Intelligence is a continuously updated cyber threat intelligence (CTI) knowledge base maintained by Sekoia analysts. In two steps, you will learn how to search the intelligence database and read threat reports that are relevant to your organization. By the end of this guide, you will be able to use Sekoia Intelligence as a daily operational resource.

## Learning goal

After completing this guide, you will be able to:

- Search the intelligence database for a threat actor, malware family, or indicator
- Understand how intelligence objects are structured and related
- Read and act on a FLINT threat report
- Set up a feed and notification to stay informed about new relevant intelligence

## Prerequisites

- You have an active Sekoia Intelligence subscription.
- You have logged in and your account is active.

## The two steps

| Step | What you do | Time estimate |
|---|---|---|
| [Step 1](/getting_started/intelligence_step1_explore_threat_database) | Explore the threat intelligence database | 15-20 min |
| [Step 2](/getting_started/intelligence_step2_read_threat_reports) | Read and act on threat reports | 15-20 min |

## How Intelligence integrates with Defend

If your organization also uses Sekoia Defend, the two products work together automatically:

- Indicators from the Intelligence database power CTI-based detection rules in Defend, raising alerts when a known malicious indicator appears in your event stream.
- Alerts in Defend are enriched with Intelligence context, showing you the threat actor, campaign, and related objects associated with an alert's observables.
- FLINT reports often include indicators of compromise that you can cross-reference with your Defend alerts.

## Prefer to learn with video?

Visit the [Sekoia Academy](https://academy.sekoia.io) for video tutorials on using Sekoia Intelligence.

## Related links

- [Step 1: Explore the threat intelligence database](/getting_started/intelligence_step1_explore_threat_database) — Search for threat objects and understand the data model.
- [Step 2: Read and act on threat reports](/getting_started/intelligence_step2_read_threat_reports) — Navigate reports, understand their structure, and set up feeds.
- [Glossary](/getting_started/glossary) — Definitions of CTI terms including indicator, observable, IOC, STIX, TLP, and FLINT.
