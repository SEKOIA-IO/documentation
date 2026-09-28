---
title: "Notification system overview"
description: "The Sekoia notification system monitors your workspace for specific events and sends alerts through your preferred channels when defined conditions are met."
keywords: [notifications, triggers, alerts, email, slack, teams, webhook, in-app, monitoring, notification system]
audience: all
module: all
type: concept
---

# Notification system overview

The Sekoia notification system lets you define rules that watch for specific events in your workspace and deliver alerts to your preferred channel when those events occur. Notification rules are personal: each user creates and manages their own rules, and rules are only visible to the user who created them.

This article explains how the notification system works, which events you can monitor, and which delivery channels are available.

## How notifications work

A notification rule has three components:

| Component | What it defines |
|---|---|
| **Trigger** | The type of event that starts the notification |
| **Conditions** | Optional filters that narrow down which specific events qualify |
| **Action** | Where and how to deliver the notification (email, Slack, in-app, etc.) |

When an event in your workspace matches a rule's trigger and conditions, the system executes the defined action immediately.

## Available triggers

You can create notification rules for the following event categories:

### Alerts

| Trigger | When it fires |
|---|---|
| A new alert is raised | A detection rule generates a new alert |
| An alert is updated | An existing alert's status or properties change |
| An automated case is created | A new case is generated automatically |
| An automated case is edited | An automated case is modified |
| A detection rule entered rate-limited state | A rule is generating too many alerts and has been throttled |

### Intelligence

| Trigger | When it fires |
|---|---|
| A new rule is added to the Rules Catalog | Sekoia publishes a new detection rule |
| A rule is scheduled for deprecation | A rule approaches its end-of-life date |
| A rule is deprecated | A rule's validity date has passed |
| A report is available | A new CTI report is published |

### Operations

| Trigger | When it fires |
|---|---|
| No events are received | An intake stops sending data for a defined period |
| A playbook encountered an error | A playbook run fails |
| A connector encountered an error | A pull intake connector reports an issue |

## Delivery channels

Each notification rule can send alerts through one or more channels simultaneously.

| Channel | Description |
|---|---|
| **In-app** | Notification appears in the Sekoia notification panel, accessible from the navigation menu |
| **Email** | Message sent to a specified email address. An enriched option includes contextual details about the triggering event |
| **Slack** | Message posted to a Slack channel using an incoming webhook URL |
| **Microsoft Teams** | Message posted to a Teams channel using an incoming webhook URL |
| **Mattermost** | Message posted to a Mattermost channel using an incoming webhook URL |
| **Custom webhook** | JSON payload sent to a custom HTTP endpoint for integration with other systems |

!!! note "Email rate limit"
    Each email recipient can receive a maximum of 10 emails per hour for a single notification rule.

## Notification scope

When you create a notification rule, the **it concerns** field lets you choose which communities the rule monitors:

- **All communities**: the rule monitors the trigger across every community you have access to.
- **A specific community**: the rule only monitors the community you select.

!!! note "Exception: intake monitoring"
    The **No events are received** trigger must be configured for one specific community. This trigger requires selecting the intake to monitor, and an intake always belongs to a single community.

## Personal visibility

Notification rules are personal: only the user who created a rule can see or manage it. Other users, including in the same community, cannot see your rules.

## Related links

- [Create a notification](/getting_started/create_a_notification.md): Step-by-step procedure to set up your first notification rule.
- [Manage notifications](/getting_started/manage_notifications.md): How to edit, disable, or delete existing rules.
- [Notification examples](/getting_started/notification_examples.md): Ready-to-use templates for common notification scenarios.
