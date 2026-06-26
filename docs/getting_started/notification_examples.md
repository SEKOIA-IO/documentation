---
title: "Notification examples"
description: "Ready-to-use notification rule templates for the most common monitoring scenarios in Sekoia."
keywords: [notification, examples, templates, intake monitoring, alerts, playbook error, rules catalog, reports]
audience: all
module: all
type: reference
---

# Notification examples

This article provides ready-to-use templates for the most common notification scenarios in Sekoia. For each example, the trigger, recommended conditions, and suggested delivery action are listed. Use these as a starting point and adjust the conditions to match your environment.

For setup instructions, see [Create a notification](/getting_started/create_a_notification).

## Intake monitoring

Receive an alert when one of your data sources stops sending events.

| Setting | Value |
|---|---|
| **Trigger** | No events are received |
| **Conditions** | Select the specific intake to monitor. Set the inactivity duration (15 minutes to 24 hours). |
| **Action** | Email or Slack |

!!! tip "Recommended threshold"
    Set the inactivity duration to 1 hour for most intakes. For critical data sources such as an EDR or Active Directory, use 15 or 30 minutes.

## New detection rule in the catalog

Receive an alert when Sekoia publishes a new detection rule that matches your criteria.

| Setting | Value |
|---|---|
| **Trigger** | A new rule is added to the Rules Catalog |
| **Conditions** | Filter by severity, name keyword, or pattern (optional) |
| **Action** | In-app or email |

## New threat report

Receive an alert when Sekoia publishes a new report relevant to your sector or threat focus.

| Setting | Value |
|---|---|
| **Trigger** | A report is available |
| **Conditions** | Filter by sector, TLP level, country, or report type (FLINT or standard). Combine multiple conditions for precision. |
| **Action** | Email or Slack |

??? example "FLINT reports for the finance sector"
    **Trigger:** A report is available

    **Conditions:**
    - Report type is FLINT
    - Sector contains Finance

    **Action:** Send an email

    **Result:** You receive an email each time Sekoia publishes a FLINT report targeting the finance sector.

## High-urgency alert raised

Receive an alert when a critical threat is detected in your environment.

| Setting | Value |
|---|---|
| **Trigger** | A new alert is raised |
| **Conditions** | Urgency is greater than 75. Optionally filter by specific assets, entities, or triggering rules. |
| **Action** | Email, Slack, or Teams |

## Alert updated

Receive an alert when an existing alert changes status or is updated by another analyst.

| Setting | Value |
|---|---|
| **Trigger** | An alert is updated |
| **Conditions** | Filter by urgency, asset, entity, or new status (optional) |
| **Action** | In-app or email |

## Playbook error

Receive an alert when a playbook encounters an error during execution.

| Setting | Value |
|---|---|
| **Trigger** | A playbook has encountered an error |
| **Conditions** | To receive notifications only for errors that crash the playbook, add the condition **And it crashed**. Without this condition, all errors are reported, including non-fatal ones. |
| **Action** | Email or Slack |

## Related links

- [Notification system overview](/getting_started/notification_system_overview) — Full list of available triggers and delivery channels.
- [Create a notification](/getting_started/create_a_notification) — Step-by-step procedure to set up a notification rule.
- [Manage notifications](/getting_started/manage_notifications) — How to edit, disable, or delete existing rules.
