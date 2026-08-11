---
title: "Quick start: Intelligence"
description: "A two-step guide to start using Sekoia Intelligence: explore the threat knowledge base and investigate and disseminate threat reports."
keywords: [quick start, intelligence, cti, threat intelligence, getting started, tutorial, reports, database, dissemination]
audience: analyst
module: intelligence
type: tutorial
---

# Quick start: Intelligence

Sekoia Intelligence is a continuously updated cyber threat intelligence (CTI) knowledge base maintained by Sekoia analysts. In two steps, you will learn how to search the intelligence database and investigate and disseminate threat reports that are relevant to your organization. By the end of this guide, you will be able to use Sekoia Intelligence as a daily operational resource.

## What Sekoia Intelligence is used for

Sekoia Intelligence supports five main use cases:

| Use case | What it means |
|---|---|
| **Detect threats** | Operationalize and disseminate Sekoia indicators of compromise (IOCs), and their context, into detection layers such as SIEM, XDR, SOC platforms, EDR, or firewalls |
| **Understand threats** | Access a knowledge base that links indicators of compromise to the tactical and strategic elements of the threat behind them: threat actors, campaigns, malware |
| **Investigate strategically** | Pivot across related threat objects to understand the broader context of a campaign, actor, or malware family |
| **Enrich incident response** | Disseminate Sekoia's threat context into incident response tools such as SOAR platforms |
| **Stay informed** | Follow and understand the evolution of the threat landscape relevant to your organization |

## Learning goal

After completing this guide, you will be able to:

- Search the intelligence database for a threat actor, malware family, or indicator
- Understand how intelligence objects are structured and related
- Investigate a FLINT threat report and cross-reference it with your environment
- Disseminate intelligence to your detection and response tools
- Set up a feed and notification to stay informed about new relevant intelligence

## Prerequisites

- You have an active Sekoia Intelligence subscription.
- You have logged in and your account is active.

## The two steps

| Step | What you do | Time estimate |
|---|---|---|
| [Step 1](/getting_started/intelligence_step1_explore_threat_database.md) | Explore the threat intelligence database | 15-20 min |
| [Step 2](/getting_started/intelligence_step2_read_threat_reports.md) | Investigate and disseminate threat intelligence | 15-20 min |

## What you will find in the Intelligence product

| Section | What it contains |
|---|---|
| **Dashboard** | An overview of the volume of objects consolidated in the database and the latest published reports |
| **Threat Landscape** | A view curated weekly by Sekoia's TDR analysts, highlighting recent FLINT reports and malware, campaigns, and threat actors of interest |
| **Intelligence** | The core of Sekoia Intelligence: the full database of CTI objects |
| **Feeds** | Filtered subsets of the Intelligence database, built for consumption via API or TAXII 2.1 |
| **Reports** | Threat intelligence reports published in the database, including FLINT and third-party reports |
| **IoC Collections** | Third-party indicators consolidated in Sekoia, for detection in Sekoia Defend or dissemination to a third-party detection tool |
| **Graph Explorations** | Visual explorations built around threat objects, for example the threat actors active in a specific country |

## How Intelligence integrates with Defend

If your organization also uses Sekoia Defend, the two products work together automatically:

- Indicators from the Intelligence database power CTI-based detection rules in Defend, raising alerts when a known malicious indicator appears in your event stream.
- Alerts in Defend are enriched with Intelligence context, showing you the threat actor, campaign, and related objects associated with an alert's observables.
- FLINT reports often include indicators of compromise that you can cross-reference with your Defend alerts.

## Prefer to learn with video?

Visit the [Sekoia Academy](https://academy.sekoia.io) for video tutorials on using Sekoia Intelligence.

## Related links

- [Step 1: Explore the threat intelligence database](/getting_started/intelligence_step1_explore_threat_database.md): Search for threat objects and understand the data model.
- [Step 2: Investigate and disseminate threat intelligence](/getting_started/intelligence_step2_read_threat_reports.md): Read reports, disseminate intelligence, and set up feeds.
- [Glossary](/getting_started/glossary.md): Definitions of CTI terms including indicator, observable, IOC, STIX, TLP, and FLINT.
