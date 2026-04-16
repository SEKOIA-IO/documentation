---
description: Configure the agent to collect logs from local files.
---

# Collect logs in files

The agent can collect logs from files in addition to system telemetry. Use this page to configure file-based collection for supported log sources.

### Prerequisites

You need an intake key that matches the log format you want to collect.

{% hint style="warning" %}
Use an intake key from a format that matches the content of the target log file.
{% endhint %}

### Configure file collection

{% stepper %}
{% step %}
### Open the configuration file

Edit the agent configuration file:

{% include "../../../.gitbook/includes/endpoint-agent-configuration-file-paths.md" %}
{% endstep %}

{% step %}
### Add a logfile entry

Add a `logfiles` section to the configuration file:

```yaml
logfiles:
  - filepath: /var/log/nginx/access.log
    intakekey: {intake key}
```

The `filepath` value is the file to watch. The `intakekey` value is the intake key used to send the events.
{% endstep %}

{% step %}
### Restart the agent

Restart the agent to apply the new configuration:

{% include "../../../.gitbook/includes/restart-the-endpoint-agent.md" %}
{% endstep %}
{% endstepper %}

### Collect multiple files

Add another entry under `logfiles` to collect more than one source file.

```yaml
logfiles:
  - filepath: /var/log/nginx/access.log
    intakekey: {intake key}
  - filepath: /var/log/mysql/mysql.log
    intakekey: {intake key}
```

{% hint style="warning" %}
Your configuration file must be valid YAML. An invalid file can prevent the agent from starting.
{% endhint %}

### Use file patterns

You can use patterns in the `filepath` attribute to match several files.

* `/var/log/nginx/*.log` matches all log files under `/var/log/nginx/`
* `/var/log/nginx/*[a-z].log` matches `/var/log/nginx/access.log`
* `/var/log/nginx/*[a-z].log` does not match `/var/log/nginx/access.2023-02-14.log`

{% hint style="info" %}
The recursive globstart pattern `**` is currently not supported.
{% endhint %}

### Related articles

* [Manage data retention](manage-data-retention.md) Adjust the local buffer used for temporary storage.
* [Manage events and fields](manage-events-and-fields.md) Review optimization rules and event-related reference data.
* [Troubleshoot](troubleshoot.md) Debug file collection issues from the local logs.
