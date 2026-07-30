# Triggers

A trigger is the entry node of a playbook: it starts the execution and passes data to the operators and actions that follow. Every playbook requires exactly one trigger.

## Access triggers

To find available triggers in the Actions library:

1. Open a playbook graph.
2. In the **Actions library**, locate the two checkboxes below the search bar: **Actions** and **Triggers**.
3. Select **Triggers**.

## Trigger types

### Alert triggers

Alert triggers are provided by Sekoia and collect information about security alerts. To find them, filter by **Triggers** and select **Sekoia** as the provider.

The following alert triggers are available:

- **Alert comment created**
- **Alert created**
- **Alert status changed**
- **Alert updated**

The **Any alert update** trigger combines all four triggers listed above.

Each alert trigger passes the following fields to subsequent actions:

| Field | Description |
|---|---|
| `alert_uuid` | Unique identifier of the alert |
| `created_at` | Date the alert was created |
| `alert_type` | Category of the alert |
| `urgency` | Urgency level of the alert |
| `event_type` | Action that triggered the alert notification |

!!! note "Operations Center only"
    Alert triggers are only available in the Operations Center.

### Manual trigger (webhook)

The **Manual trigger** is provided by Sekoia. It starts a playbook automatically once an analyst has reviewed an alert and cleared a doubt.

### Manual trigger for case

The **Manual trigger for case** lets analysts start a playbook directly from a case without leaving their investigation.

Once a playbook uses this trigger as its entry node and is set to **On**, it appears in the **Available playbooks for this case** panel of every case in the community. The playbook receives the case as its triggering event, and the run is identified as **Sekoia Case: \<case ID\>** in the **Runs** tab.

Chain this trigger with the **Get case** action to retrieve the case content.

To start a playbook from a case and read its results, see [Run a playbook from a case](/xdr/features/investigate/run_playbook_case.md).

### Cron trigger

The **Cron** trigger starts a playbook on a recurring schedule. You define and configure the schedule when setting up the trigger.

## Logs and errors

Sekoia displays all trigger logs to help you understand configuration errors and diagnose playbooks that are not running as expected.

### View logs

To view logs for a trigger node:

1. On the playbooks listing page, locate a playbook that shows an error message on its card.
2. Open the playbook and click the trigger node that is in an error state.
3. Select the **Errors** or **Logs** tab to view all messages.

Click a log line to expand its details.

### Log levels

Each log message has one of five severity levels:

| Level | Description |
|---|---|
| `Debug` | Detailed diagnostic information for troubleshooting unexpected behavior or exceptions |
| `Info` | Confirmation that the playbook is running as expected |
| `Warning` | An unexpected condition occurred that is not critical and does not stop the process |
| `Error` | A configuration or runtime error that stopped the current process |
| `Critical` | A serious error that forced the program to stop entirely |

### Log retention

Logs are retained for different durations depending on their severity:

| Severity | Retention period |
|---|---|
| Debug | 1 hour |
| Info | 1 day |
| Warning | 7 days |
| Error | 7 days |
| Critical | 1 month |

## Related articles

[Run a playbook from a case](/xdr/features/investigate/run_playbook_case.md): How to start a playbook directly from a case and read the run results.

[Playbooks](/xdr/features/automate/playbooks.md): Overview of the playbook builder, including operators and actions.

[Cases](/xdr/features/investigate/cases.md): Overview of the case management workflow in Sekoia.
