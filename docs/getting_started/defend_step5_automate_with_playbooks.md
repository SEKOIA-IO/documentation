---
title: "Step 5: Automate with playbooks"
description: "Activate a playbook template in Sekoia Defend to automate alert enrichment or response actions."
keywords: [playbook, automation, template, trigger, response, alert, automate, workflow]
audience: analyst
module: defend
type: task
---

# Step 5: Automate with playbooks

Playbooks are automated workflows that execute a sequence of actions when a trigger fires, such as when a new alert is created. They reduce manual effort by handling repetitive triage steps, enriching alerts with external data, or sending notifications to your team. This step shows you how to activate your first playbook using a ready-made template.

## Before you begin

- You have completed [Step 4: Triage your first alert](/getting_started/defend_step4_triage_first_alert).
- You have the **Analyst** or **Admin** role.

## Understand playbook triggers

Every playbook starts with a trigger that defines when it runs.

| Trigger type | When it fires |
|---|---|
| **Alert created** | Fires automatically each time a new alert is raised |
| **Alert updated** | Fires when an alert's status or properties change |
| **Manual** | Fires on demand when an analyst clicks **Run playbook** from an alert |
| **Scheduled** | Fires at a defined time interval |

For your first playbook, use the **Alert created** trigger with a condition to limit it to specific alert types or urgency levels.

## Activate a playbook from a template

Sekoia provides a library of ready-made playbook templates for common use cases.

1. In the navigation menu, select **Automate > Playbooks**.
2. Click **+ Playbook**.
3. Select **Use a template**.
4. Browse the template library or search by keyword.
5. Select a template that matches your use case (for example, **Enrich alert with VirusTotal** or **Send Slack notification on new alert**).
6. Click **Use this template**.
7. Review the template configuration. Update any credentials or parameters required by the template (for example, an API key for a third-party service).
8. Set a condition on the trigger to limit when the playbook runs (for example, only for alerts with urgency above 70).
9. Click **Save**.
10. Toggle the playbook to **Active**.

> 📸 [SCREENSHOT SUGGESTION: The playbook template library showing a grid of available templates with names and descriptions. | ALT TEXT: Playbook template library with available automation templates listed as cards.]

## Verify a playbook run

After activating the playbook, wait for a new alert that matches the trigger condition. Then verify the playbook ran correctly.

1. Navigate to **Automate > Playbooks**.
2. Click the playbook name to open its detail page.
3. Select the **Runs** tab.
4. Check the most recent run. A **Success** status confirms the playbook executed without errors.

If the run shows an error, click the run to inspect the step where it failed and review the error message.

!!! tip "Monitor playbook health"
    Set up a notification to alert you when a playbook encounters an error. Navigate to **Settings > Notifications**, create a new rule, and select **A playbook has encountered an error** as the trigger.

## Keep your playbooks efficient

As your library of playbooks grows, keep these principles in mind:

- Each playbook should have a single, clear objective.
- Use a trigger condition to avoid running a playbook on every alert, even irrelevant ones.
- Aim for playbooks that complete in under one minute.
- Limit each playbook to fewer than 15 modules (trigger + operators + actions).

For detailed guidance on designing and optimizing your playbook library, see the [best practices guide](/xdr/operations/best-practices).

## Related links

- [Quick start: Defend](/getting_started/quick_start_defend) — Return to the overview of all five steps.
- [Notification system overview](/getting_started/notification_system_overview) — Configure alerts for playbook errors and other operational events.
