---
title: "Manage notifications"
description: "View, edit, disable, and delete your personal notification rules in Sekoia."
keywords: [notifications, manage, edit, disable, delete, notification rules, personal]
audience: all
module: all
type: task
---

# Manage notifications

After you create notification rules, you can update them at any time to reflect changes in your workflow or monitoring priorities. This article explains how to view, edit, disable, re-enable, and delete your personal notification rules.

## Before you begin

- You must be logged in to Sekoia with any role.
- You must have at least one existing notification rule. See [Create a notification](/getting_started/create_a_notification.md) if you have not set one up yet.

!!! note "Personal visibility"
    Notification rules are personal. You can only view and manage the rules you created. Rules created by other users in your community are not visible to you.

## View your notification rules

1. Navigate to the bottom of the left-hand navigation menu and click **Settings**.
2. Select the **Notifications** tab.

The listing page displays all your notification rules for the current community, with their name, trigger type, delivery channel, and current status (enabled or disabled).

> 📸 [SCREENSHOT SUGGESTION: The Notifications settings page showing a list of notification rules with their names, trigger types, delivery channels, and enabled/disabled status toggles. | ALT TEXT: Notifications listing page showing personal notification rules with status toggles.]

## Edit a notification rule

To change the trigger, conditions, or delivery action of an existing rule:

1. On the **Notifications** settings page, locate the rule you want to update.
2. Click the rule line.
3. Update the fields you want to change:
    - **Name** — Update the rule name to reflect its new purpose.
    - **Trigger** — Change the event type that activates the rule.
    - **Conditions** — Add, remove, or modify filters.
    - **Action** — Change or add a delivery channel.
4. Click **Save**.

The updated rule takes effect immediately.

## Disable a notification rule

Disabling a rule pauses it without deleting it. Use this option when you want to temporarily stop receiving notifications without losing your configuration.

To disable a rule:

1. On the **Notifications** settings page, locate the rule you want to pause.
2. Click the toggle to switch it from enabled to disabled.

The rule remains visible in the listing with a disabled status and stops firing until you re-enable it.

## Re-enable a notification rule

To re-enable a disabled rule:

1. On the **Notifications** settings page, locate the disabled rule.
2. Click the toggle to switch it back to enabled.

The rule resumes firing immediately for matching events.

## Delete a notification rule

Deleting a rule permanently removes it. This action cannot be undone.

!!! warning "Permanent action"
    Deleted notification rules cannot be recovered. If you only need to pause a rule temporarily, disable it instead.

To delete a rule:

1. On the **Notifications** settings page, locate the rule you want to remove.
2. Click the **...** button to the right of the rule.
3. Select **Delete**.
4. Confirm the deletion.

The rule is removed immediately from your listing and stops firing.

## Related links

- [Notification system overview](/getting_started/notification_system_overview.md) — How the notification system works and what triggers and delivery channels are available.
- [Create a notification](/getting_started/create_a_notification.md) — Step-by-step procedure to set up a new notification rule.
- [Notification examples](/getting_started/notification_examples.md) — Ready-to-use templates for common monitoring scenarios.
