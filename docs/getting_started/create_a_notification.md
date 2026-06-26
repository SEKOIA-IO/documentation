---
title: "Create a notification"
description: "Set up a notification rule in Sekoia to receive alerts through your preferred channel when a specific event occurs."
keywords: [notification, create, rule, trigger, condition, email, slack, teams, webhook, alert]
audience: all
module: all
type: task
---

# Create a notification

Notification rules let you receive alerts through your preferred channel when a specific event occurs in your workspace, such as a new high-urgency alert, an intake going silent, or a new threat report being published. This article walks you through creating a notification rule from scratch.

## Before you begin

- You must be logged in to Sekoia with any role (Guest, Analyst, or Admin).
- If you plan to deliver notifications to Slack, Teams, or Mattermost, have your incoming webhook URL ready before starting.

## Create a notification rule

1. Navigate to the bottom of the left-hand navigation menu and click **Settings**.
2. Select the **Notifications** tab.
3. Click **+ New notification rule**.

!!! note "First notification"
    If you have no existing rules, the listing page appears empty with a **+ Notification** button instead. Click it to start.

4. Enter a descriptive name in the **Notification name** field (for example, `High-urgency alerts on production assets`).
5. Select the event type from the **Trigger** dropdown. See [Notification system overview](/getting_started/notification_system_overview) for the full list of available triggers.
6. In the **Conditions** section, define filters to narrow down which events qualify. Conditions are optional but strongly recommended to avoid noise.
7. In the **Action to perform** section, select your delivery method:
    - **In-app notification** — Displays in the Sekoia notification panel.
    - **Email** — Enter the recipient email address. Enable **Enrich email with contextual info** to include event details in the message body.
    - **Slack**, **Teams**, or **Mattermost** — Paste your incoming webhook URL.
    - **Webhook** — Enter the URL of your HTTP endpoint to receive a JSON payload.
8. Click **Save**.

Your rule is now active and appears in your personal notification list.

> 📸 [SCREENSHOT SUGGESTION: The notification creation form showing the Trigger dropdown selected, a Conditions section with urgency filter, and the Action section with email delivery selected. | ALT TEXT: Notification creation form with trigger, conditions, and email delivery options configured.]
>

!!! info "Find your incoming webhook URL"
   If you have not set up an incoming webhook for your messaging platform yet:

   - **Slack:** [Sending messages using Incoming Webhooks](https://api.slack.com/messaging/webhooks)
   - **Microsoft Teams:** [Create incoming webhooks](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)
   - **Mattermost:** [Mattermost incoming webhooks](https://developers.mattermost.com/integrate/webhooks/incoming/)

## Example: High-urgency alert on a production asset

This example shows how to set up a notification that fires when a critical asset is involved in a high-urgency alert.

??? example "High-urgency alert notification"
    **Trigger:** A new alert is raised

    **Conditions:**
    - Urgency is greater than 80
    - Asset name contains `Production`

    **Action:** Send an email and a Slack message

    **Result:** Whenever an alert matching these criteria is raised, you receive an email and a Slack message with a direct link to the alert.

## Related links

- [Notification system overview](/getting_started/notification_system_overview) — Full list of available triggers and delivery channels.
- [Manage notifications](/getting_started/manage_notifications) — How to edit, disable, or delete an existing notification rule.
- [Notification examples](/getting_started/notification_examples) — Ready-to-use templates for intake monitoring, alerts, playbooks, and reports.
