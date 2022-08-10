# Triggers

To start creating a playbook, a `Trigger` is needed in order to launch the start of the playbook execution.

## Types of Triggers

In the Operations Center, section Playbooks, once you have selected a created playbook, you will be able to filter the `Blocks` into one of the three categories: `Triggers, Operators and Actions`. Here we want to filter on `Triggers` only.

![SEKOIA.IO Operations Center Filter on Triggers](/assets/operation_center/playbooks/filter_triggers.png){: style="max-width:60%"}

The `Triggers` collects data that will be used by the Operators and Actions to answer a specific need.

### Alerts

The `Security alerts` trigger allows a user to collect information of an alert, such as the `alert_uuid`, its date of creation (`created_at`), its category (`alert_type`), its `urgency` or the action that triggered THIS alert notification (`event_type`) for example "alert-created", "alert-status-changed", "alert-comment-created" etc.

### Webhook

The `Alert webhook` trigger allows a user to automatically trigger actions once a human has raised and removed a doubt on an alert.
This is a `Block` button, such as the one you will find hereunder, for the example of adding an standardised commentary on the alert commentary section.

![SEKOIA.IO Operations Center Webhook Trigger](/assets/operation_center/playbooks/web_hook.gif){: style="max-width:60%"}

### Cron

The `Cron` trigger allows a user to periodically launch an automatic action, that should be defined and created by a user.

## Logs and errors in triggers

Some configuration errors in triggers can be hard to understand. We display all logs so it's easier to understand what can be improved and why the playbook is not working properly.

### Logs

In the playbooks listing page, you can identify a playbook with configuration errors via an error message in the playbook card.
In a playbook page with configuration errors in a trigger node, you can see if the state of the node is in error.
Click on this node and go to the tab “Errors” or “Logs” to see all messages.

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
| Warning | 7 days |
