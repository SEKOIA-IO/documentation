---
title: "Quick start: Intelligence"
description: "A three-step guide to start using Sekoia Intelligence and Digital Risk Protection: explore the threat knowledge base, investigate and disseminate threat reports, and monitor external exposures."
keywords: [quick start, intelligence, cti, threat intelligence, digital risk protection, drp, getting started, tutorial, reports, database, dissemination]
audience: analyst
module: intelligence
type: tutorial
---

# Quick start: Intelligence

Sekoia Intelligence is a continuously updated cyber threat intelligence (CTI) knowledge base maintained by Sekoia analysts. This quick start covers three complementary paths: exploring the intelligence database, investigating and disseminating threat reports, and monitoring external exposures with Digital Risk Protection (DRP). By the end of this guide, you will know where to start for both intelligence consumption and exposure monitoring.

The intelligence is produced by a team of over 25 analysts with backgrounds in military, national cyber agencies, and private industry, and is built on open standards such as STIX 2.1 and MITRE ATT&CK. Sekoia's team collaborates with organizations including Europol, NATO, and the FBI. Over half of the indicators of compromise in the database come from Sekoia's own research; the rest are curated from open-source intelligence (OSINT) and validated before publication. All threat objects are connected in a single knowledge graph, which is what the [threat context](/getting_started/intelligence_step1_explore_threat_database.md#use-the-threat-context) feature lets you explore.

## What Sekoia Intelligence is used for

Sekoia Intelligence and Digital Risk Protection support the following use cases:

| Use case | What it means |
|---|---|
| **Detect threats** | Operationalize and disseminate Sekoia indicators of compromise (IOCs), and their context, into detection layers such as SIEM, XDR, SOC platforms, EDR, or firewalls |
| **Understand threats** | Access a knowledge base that links indicators of compromise to the tactical and strategic elements of the threat behind them: threat actors, campaigns, malware |
| **Investigate strategically** | Pivot across related threat objects to understand the broader context of a campaign, actor, or malware family |
| **Enrich incident response** | Disseminate Sekoia's threat context into incident response tools such as SOAR platforms |
| **Stay informed** | Follow and understand the evolution of the threat landscape relevant to your organization |
| **Monitor external exposure** | Track data from clear, deep, and dark web sources that matches identifiers configured for your organization |

## Learning goal

After completing this guide, you will be able to:

- Search the intelligence database for a threat actor, malware family, or indicator
- Understand how intelligence objects are structured and related
- Investigate a FLINT threat report and cross-reference it with your environment
- Disseminate intelligence to your detection and response tools
- Set up a feed and notification to stay informed about new relevant intelligence
- Configure Digital Risk Protection monitoring and investigate an exposure event in Flare

## Prerequisites

- You have an active Sekoia Intelligence subscription.
- You have logged in and your account is active.

## The three paths

| Step | What you do | Time estimate |
|---|---|---|
| [Step 1](/getting_started/intelligence_step1_explore_threat_database.md) | Explore the threat intelligence database | 15-20 min |
| [Step 2](/getting_started/intelligence_step2_read_threat_reports.md) | Investigate and disseminate threat intelligence | 15-20 min |
| [Step 3](/getting_started/quick_start_flare.md) | Monitor digital risk exposures with Flare | 20-30 min |

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

## What you will find in Digital Risk Protection

Digital Risk Protection helps you monitor external exposures that match identifiers configured in Flare. These events complement the broader threat knowledge available in Sekoia Intelligence.

| Capability | What it contains |
|---|---|
| **Identifiers** | Domains, names, keywords, IP addresses, and other values that define what Flare monitors |
| **Policies** | Matching, ignored-term, discovery, and duplication settings that control which events appear |
| **Flare events** | Exposures observed across clear, deep, and dark web sources |
| **Sekoia events** | Normalized Flare events collected through the Flare Events intake |
| **Sekoia alerts** | Alerts generated when activated detection rules match Flare events |

## How Intelligence integrates with Defend and Digital Risk Protection

If your organization also uses Sekoia Defend, the products can work together across collection, detection, and investigation:

- Indicators from the Intelligence database can power CTI-based detection rules in Defend, raising alerts when a known malicious indicator appears in your event stream.
- Alerts in Defend can be enriched with Intelligence context, showing the threat actor, campaign, and related objects associated with an alert's observables.
- FLINT reports often include indicators of compromise that you can cross-reference with your Defend alerts.
- Flare events collected through the Flare Events intake become Sekoia events that you can search and evaluate with detection rules.
- When a Flare event includes a source URL, use `event.url` to pivot from the Sekoia event to the corresponding event in Flare.

Intelligence, Defend, and Digital Risk Protection are separate capabilities that you can use together when your subscription includes them.

## Prefer to learn with video?

Visit the [Sekoia Academy](https://academy.sekoia.io) for video tutorials on using Sekoia Intelligence.

## Related links

- [Step 1: Explore the threat intelligence database](/getting_started/intelligence_step1_explore_threat_database.md): Search for threat objects and understand the data model.
- [Step 2: Investigate and disseminate threat intelligence](/getting_started/intelligence_step2_read_threat_reports.md): Read reports, disseminate intelligence, and set up feeds.
- [Step 3: Monitor digital risk exposures](/getting_started/quick_start_flare.md): Configure Flare, collect exposure events, activate detections, and investigate alerts.
- [Flare events in Sekoia Digital Risk](/cti/features/flare_events_overview.md): Overview of the Flare event flow, normalized fields, and investigation pivot.
- [Glossary](/getting_started/glossary.md): Definitions of CTI terms including indicator, observable, IOC, STIX, TLP, and FLINT.