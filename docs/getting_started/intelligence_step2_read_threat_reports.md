---
title: "Step 2: Read and act on threat reports"
description: "Navigate FLINT threat reports in Sekoia Intelligence, understand their structure, and set up feeds to receive relevant intelligence automatically."
keywords: [flint, threat report, report, feed, notification, intelligence, cti, indicators, sector]
audience: analyst
module: intelligence
type: task
---

# Step 2: Read and act on threat reports

Sekoia analysts publish regular threat reports, including FLINT (Flash Intelligence) reports, that provide rapid, actionable intelligence on emerging threats. This step shows you how to find and read reports, understand their structure, and set up a feed to receive future reports automatically.

## Before you begin

- You have completed [Step 1: Explore the threat intelligence database](/getting_started/intelligence_step1_explore_threat_database.md).

## Find threat reports

### Search for reports

1. In the navigation menu, select **Observe** > **Intelligence**.
2. Enter a topic in the search bar (for example, a threat actor name, a malware family, or a sector).
3. In the results, open the **Objects** tab.
4. Filter by **Type > Report** to display only reports.

### Browse all reports

To see all available reports:

1. Open the filter panel on the Intelligence page.
2. Set **Type** to **Report**.
3. By default the table is sorted by **Last edited** to see the most recent reports firt.

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

## Set up a feed for your sector

A feed is a filtered, personalized view of the Intelligence database that shows only the content relevant to you.

To create a feed:

1. In the navigation menu, select **Observe > Feeds**.
2. Click **+ New Feed**.
3. Enter a name for the feed (for example, `Finance sector threats`).
4. Set filters based on your interests: sector, geography, threat type, or TLP level.
5. Save the feed.

Your feed appears in the Feeds section and updates automatically as new matching content is published.

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

- [Quick start: Intelligence](/getting_started/quick_start_intelligence.md) — Return to the overview of the Intelligence quick start.
- [Create a notification](/getting_started/create_a_notification.md) — Full procedure for setting up notification rules.
- [Glossary](/getting_started/glossary.md) — Definitions of FLINT, IOC, TLP, indicator, and feed.
