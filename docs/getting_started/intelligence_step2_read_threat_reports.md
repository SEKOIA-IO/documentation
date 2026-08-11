---
title: "Step 2: Investigate and disseminate threat intelligence"
description: "Find and interpret FLINT threat reports in Sekoia Intelligence, and disseminate intelligence to your detection and response tools through native connectors, TAXII, or the API."
keywords: [flint, threat report, report, feed, notification, intelligence, cti, indicators, dissemination, taxii, connector, api, firewall]
audience: analyst
module: intelligence
type: task
---

# Step 2: Investigate and disseminate threat intelligence

The Sekoia CTI team verifies, consolidates, and enriches thousands of reports in STIX 2.1 format, coming from third-party sources. In addition, the team writes and publishes its own research, under the name FLINT (Flash Intelligence). This step shows you how to find and read these reports, cross-reference their indicators with your environment, and disseminate intelligence to your detection and response tools.

## Before you begin

- You have completed [Step 1: Explore the threat intelligence database](/getting_started/intelligence_step1_explore_threat_database.md).

## Find threat reports

### Search for reports

1. In the navigation menu, select **Observe > Intelligence**.
2. Enter a topic in the search bar (for example, a threat actor name, a malware family, or a sector).
3. In the results, open the **Objects** tab.
4. Filter by **Type > Report** to display only reports.

!!! tip "Find all FLINT reports"
    Add the filter **Source = Sekoia** to your search to display only the reports written by Sekoia's own analysts, including all FLINT reports.

### Browse all reports

To see all available reports:

1. Open the filter panel on the Intelligence page.
2. Set **Type** to **Report**.
3. Sort by **Last edited** to see the most recent reports first.

## Understand FLINT reports

FLINT (Flash Intelligence) reports are rapid-response publications released when a significant threat event occurs, such as a new ransomware campaign or an actively exploited vulnerability. They are designed to be actionable within hours of publication.

A FLINT report typically contains:

| Section | What it provides |
|---|---|
| **Executive summary** | A plain-language overview of the threat for non-technical stakeholders |
| **Technical analysis** | Detailed breakdown of the attack chain, tools, and techniques |
| **MITRE ATT&CK mapping** | The tactics and techniques used by the threat actor |
| **Indicators of compromise** | File hashes, IP addresses, domains, and other artifacts for detection |
| **Recommended actions** | Steps to detect, contain, or remediate the threat |

> 📸 [SCREENSHOT SUGGESTION: A FLINT report detail page showing the executive summary section, MITRE ATT&CK mapping, and a list of indicators of compromise. | ALT TEXT: FLINT report page with executive summary, MITRE mapping, and IOC list.]

## Act on report indicators

When a FLINT report includes indicators of compromise, you can cross-reference them with your Sekoia Defend environment.

If you have Sekoia Defend, the CTI-based detection rule **SEKOIA Intelligence Feed** is active by default. This rule automatically triggers alerts in Defend when a valid Sekoia Intelligence indicator appears in your event stream. You do not need to manually import indicators from reports.

To check whether any indicator from a report has already appeared in your environment:

1. Copy an IP address, domain, or file hash from the report.
2. Paste it into the search bar on the Intelligence page.
3. Switch to the **Observables** tab to see if it is known.
4. Navigate to **Investigate > Events** and search for the value in your event history.

## Disseminate intelligence to your tools

Beyond Sekoia Defend, you can operationalize Sekoia Intelligence in your own detection and response stack. There are three main ways to do this.

| Method | When to use it |
|---|---|
| **Native connector** | For technologies with a dedicated Sekoia connector (SIEM, SOAR, firewall). Always prefer this option when available: native connectors support dynamic updates and revocation, and follow Sekoia's STIX taxonomy correctly. |
| **TAXII 2.1 connector** | For technologies that natively support ingesting STIX 2.1 data through the TAXII 2.1 protocol. |
| **API** | For custom consumption needs, with the ability to run precise, segmented queries against the database. See the [Intelligence API reference](https://docs.sekoia.com/developer/api/#/intelligence). To consume the full feed reliably over time, including revoked objects, build your integration following the [API consumption guide](/cti/features/integrations/api.md). |

!!! note "Model Context Protocol (MCP)"
    Sekoia is also developing an MCP-based way to consume Intelligence. This capability is still in progress. Check the [changelog](https://changelog.sekoia.io) for updates.

## Set up a feed for your firewall

A feed is a filtered, personalized subset of the Intelligence database that contains only the content you select.

Sekoia Intelligence customers commonly use feeds to create dynamic blocklists for their firewalls. Because these blocklists only support network artifacts, a dedicated feed limited to network indicators is the most efficient way to build them.

To create the feed:

1. In the navigation menu, select **Observe > Feeds**.
2. Click **+ New Feed**.
3. Enter a name for the feed (for example, `Firewall blocklist`).
4. Set filters based on your firewall's requirements, for example: object type is **Indicator**, indicator type is **IPv4**.
5. Optionally, filter to include only indicators from Sekoia sources (C2 tracker, honeypots, etc.).
6. Save the feed.

Your feed appears in the Feeds section and updates automatically as new matching content is published. The feed has an API URL that your firewall can use to fetch its indicator list.

!!! note "Feeds support API and TAXII consumption"
    A feed lets you build a filtered subset of the Intelligence database for consumption through the API or TAXII 2.1, independently of the dissemination method you use for your main detection stack.

## Receive notifications for new reports

To be notified whenever a new report matching your criteria is published:

1. Navigate to **Settings > Notifications**.
2. Click **+ New notification rule**.
3. Set the trigger to **A report is available**.
4. Add conditions to match your feed criteria (for example, sector, TLP level, or specific threat names).
5. Select your delivery channel (in-app, email, Slack, or Teams).
6. Save the rule.

You now receive an alert each time Sekoia publishes a relevant new report.

See: [Create a notification](/getting_started/create_a_notification.md) for the full procedure.

## Related links

- [Quick start: Intelligence](/getting_started/quick_start_intelligence.md): Return to the overview of the Intelligence quick start.
- [Data model](/cti/features/data_model.md): Full reference on STIX objects, observables, confidence, and reliability.
- [Create a notification](/getting_started/create_a_notification.md): Full procedure for setting up notification rules.
- [Glossary](/getting_started/glossary.md): Definitions of FLINT, IOC, TLP, indicator, and feed.
