---
title: "Step 4: Triage your first alert"
description: "Learn how to read, investigate, and close a security alert in Sekoia Defend using the alert detail page."
keywords: [alert, triage, urgency, status, investigate, alert filter, false positive, events, close, reject]
audience: analyst
module: defend
type: task
---

# Step 4: Triage your first alert

An alert is raised when an incoming event matches an active detection rule. Triaging an alert means reviewing its context, deciding whether it represents a real threat or a false positive, and updating its status accordingly. This step walks you through your first full triage cycle in Sekoia Defend.

## Before you begin

- You have completed [Step 3: Activate detection rules](/getting_started/defend_step3_activate_detection_rules.md) and rules are active.
- At least one alert has been raised in your community.

!!! note "No alerts yet?"
    If no alerts have appeared after your rules are active, your intakes may need more time to generate matching events. Check that your intake is receiving events (see [Step 2](/getting_started/defend_step2_verify_event_reception.md)) and that the corresponding rules are enabled. You can also lower the effort level filter to see if Elementary rules are active.

## Open the alerts page

In the navigation menu, select **Investigate > Alerts**.

The alerts page displays all alerts raised in your community, ordered by most recent by default. Each row shows:

- The alert creation date and last update
- The urgency score (0-100)
- The status (Pending, Acknowledged, Ongoing, Closed, or Rejected)
- The entity and asset involved
- The rule that triggered the alert
- The associated threat

## Understand alert urgency

Urgency measures the risk level of an alert on a scale from 0 to 100.

| Urgency range | Display | What it means |
|---|---|---|
| 75-100 | High | Requires immediate attention |
| 50-74 | Medium | Investigate when capacity allows |
| 0-49 | Low | Review during regular operations |

Urgency is calculated from the **severity of the detection rule** and the **criticality of the affected asset**. An Elementary rule triggered on a critical server produces a higher urgency than the same rule triggered on an unclassified endpoint.

## Read the alert detail page

To open an alert:

1. Click the alert name or row in the alerts listing.

The alert detail page is organized into tabs.

### Details tab

The Details tab shows:

- The urgency score and rule that triggered the alert
- The affected assets and entity
- Related threat intelligence from the Sekoia Intelligence database
- The alert timeline (status changes, comments, and events)

### Events tab

The Events tab lists the raw events that triggered the alert. Use it to understand exactly what activity caused the rule to fire.

You can interact with individual field values to:

- Filter for or filter out that value within the alert's events
- Search across all events in the platform for that value

> 📸 [SCREENSHOT SUGGESTION: The alert detail page showing the Details tab with urgency score, affected asset, and timeline on the right, and the Events tab visible in the navigation. | ALT TEXT: Alert detail page with urgency score, asset information, and event timeline.]

## Change the alert status

After reviewing the alert, update its status to reflect your analysis.

1. Click the **Alert Status** button at the top of the alert detail page.
2. Select the appropriate status.

| Status | When to use it |
|---|---|
| **Acknowledged** | You have started analysis but have not yet determined the outcome |
| **Ongoing** | The alert is confirmed as a true positive and a response is in progress |
| **Closed** | The alert has been fully investigated and all necessary actions have been taken |
| **Rejected** | The alert is a false positive |

!!! tip "Leave a comment"
    Add a comment when you change status to document your reasoning. This is especially useful when multiple analysts work on the same community.

## Create an alert filter for a false positive

If the alert is a false positive and you expect the same rule to trigger repeatedly on the same benign activity, create an alert filter to suppress future occurrences.

1. In the **Events** tab, click **Toggle value selection** icon in the top right of the events list.
2. Select the field values that identify this specific false positive pattern.
3. Click **New alert filter** icon.
4. Enter a name for the filter (required) and an optional description.
5. The filter pattern is pre-filled from your selected values. Review it.
6. To reject the current alert (optional), select the "Reject current alert" option, and select a status and verdict to apply.
7. Click **Create alert filter**.

The filter takes effect immediately for future matching events. 



## Related links

- [Step 5: Automate with playbooks](/getting_started/defend_step5_automate_with_playbooks.md) — Set up automated enrichment and response workflows for your alerts.
- [Notification system overview](/getting_started/notification_system_overview.md) — Receive an email or Slack message when a high-urgency alert is raised.
