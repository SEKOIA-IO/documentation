---
title: "Step 2: Verify event reception"
description: "Confirm that your Sekoia Defend intake is receiving logs correctly by reviewing the events graph and checking for parsing issues."
keywords: [events, intake, verify, event reception, valid events, warning, invalid, graph, monitoring]
audience: analyst
module: defend
type: task
---

# Step 2: Verify event reception

After creating an intake and deploying the intake key or starting a pull connector, you need to confirm that logs are arriving and being parsed correctly. This step helps you catch configuration problems early, before they affect your detection coverage.

## Before you begin

- You have completed [Step 1: Connect a data source](/getting_started/defend_step1_connect_data_source).
- For push intakes: your data source has been configured to forward logs to the Sekoia intake endpoint using the intake key.
- For pull intakes: you have toggled the intake to **On**.

## Check the intakes listing

1. In the navigation menu, select **Collect > Intakes**.
2. Locate your intake in the list.

Each intake card shows three event counters for the selected time period:

| Counter | What it means |
|---|---|
| **Valid events** | Events successfully received and parsed |
| **Events in warning** | Events received but only partially parsed, or where some field values did not match the expected format |
| **Invalid events** | Events received but not parseable at all, usually due to a format mismatch |

!!! tip "Change the time range"
    Use the date range selector on the intakes page to view event counts for the last 24 hours, 7 days, or 30 days. For a new intake, start with the 24-hour view.

> 📸 [SCREENSHOT SUGGESTION: An intake card showing valid event count, warning count, and invalid event count, with the date selector visible. | ALT TEXT: Intake card displaying event reception metrics including valid, warning, and invalid event counts.]

## Inspect the intake detail page

To see more detail about your intake's health:

1. Click the intake name to open its detail page.
2. Review the **events graph**, which shows event volume over time.
3. Check for spikes in warning or invalid events.

### Understand event delivery lag

The **event delivery** metric shows the average time between when an event was created at the source and when Sekoia received it. A high or negative value can indicate:

- A timezone misconfiguration on the data source
- Network latency or bandwidth issues
- An abnormal burst of events causing ingestion delay

For a healthy intake, event delivery lag should be close to zero.

## What to do if no events appear

If your intake shows zero valid events after 30 minutes:

| Intake type | Check |
|---|---|
| **Push** | Confirm the intake key is deployed correctly on your data source. Verify that firewall or network rules allow outbound connections to the Sekoia intake endpoint. |
| **Pull** | Open the **Connector log** tab on the intake detail page. Look for error messages that indicate an authentication failure or a connectivity issue with the source API. |

For region-specific intake endpoint URLs, refer to [Log in for the first time](/getting_started/log_in_for_the_first_time).

## Set up an intake monitoring notification

To receive an alert when your intake stops sending events:

1. On the intake card, click **...** and select **Notifications**.
2. Choose how long the intake must be inactive before a notification is triggered (from 15 minutes to 24 hours).
3. Select your preferred delivery channel (in-app, email, Slack, or Teams).
4. Save the notification rule.

This ensures you are informed immediately if a critical data source goes silent.

See: [Create a notification](/getting_started/create_a_notification) for the full procedure.

## Acceptable thresholds

| Metric | Target |
|---|---|
| Warning events | Less than 3% of total events per intake |
| Invalid events | Less than 1% of total events per intake |

If warning or invalid rates exceed these thresholds, review the technology-specific setup guide for your intake in the [integration catalog](/integration/categories/).

## Related links

- [Step 3: Activate detection rules](/getting_started/defend_step3_activate_detection_rules) — Start enabling rules once your events are flowing correctly.
- [Create a notification](/getting_started/create_a_notification) — Set up alerts for intake monitoring and other triggers.
- [Troubleshooting common issues](/getting_started/troubleshooting_common_issues) — Solutions for connectivity and ingestion problems.
