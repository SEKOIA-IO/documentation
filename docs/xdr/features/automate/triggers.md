# Triggers

To create a playbook, you need a `Trigger` to launch its execution.

## Types of Triggers

To access triggers:

1. Go to a `Playbook` graph
2. In the `Actions Library`, right under the search bar are two checkboxes: Actions and Triggers
3. Select `Triggers`

The `Triggers` collect data that will be used by the Operators and Actions to answer a specific need.

### Alerts

The `Security alerts` triggers are made by Sekoia.io and allow users to collect information about alerts. To find them in the listing, filter by `Triggers` and click on Sekoia.io.

There you can find the following triggers:

- Alert comment created
- Alert created
- Alert status changed
- Alert updated

The trigger named `Any Alert Update` regroups all of the triggers cited above.

By using these triggers, you can get:

- An alert UUID `alert_uuid`
- Its date of creation (`created_at`),
- Its category (`alert_type`),
- Its `urgency`
- The action that triggered the alert notification (`event_type`)

!!! note
    This trigger is only applicable in the Operations Center.


### Manual trigger (webhook)

The `Manual trigger` can be found in the Triggers listing by clicking on Sekoia.io. It allows users to automatically trigger actions once a human has raised and removed a doubt on an alert.

### Cron

The `Cron` trigger allows users to periodically launch an automatic action that should be defined and created by a user.

## Logs and errors in triggers

Some configuration errors in triggers can be hard to understand. We display all logs so it's easier to understand what can be improved and why the playbook is not working properly.

### Logs

In the playbooks listing page, you can identify a playbook with configuration errors via an error message in the playbook card.

In a playbook page with configuration errors in a trigger node, you can see if the state of the node is in error.

Click on this node and go to the tab `Errors` or `Logs` to see all messages.

### Levels and retention

There are five possible types of log messages :

* `Debug` : used to find the reason in case your program is not working as expected or an exception has occurred
* `Info` : used to log the information your program is working as expected
* `Warning` : will not stop anything, but is there to tell you that something happened that is not expected (or there may be a potential issue) and it's not critical enough to terminate or stop the app/process
* `Error` : informs you that you actually did something wrong, describes the problem, and stops the process/app
* `Critical error` : a serious error that forces the program to stop and it becomes impossible for the running program, operating system or software to continue working normally

Each error message has details that you can display by clicking on the log line.

The logs of a trigger have a retention period that depends on the severity of the log. The following retention periods are currently applied:

| Severity | Retention period |
| --- | --- |
| Debug | 1 hour |
| Info | 1 day |
| Warning | 7 days |
| Error | 7 days |
| Critical | 1 month |
