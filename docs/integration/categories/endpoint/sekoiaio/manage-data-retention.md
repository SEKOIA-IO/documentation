---
description: Configure the local event buffer used when connectivity is unavailable.
---

# Manage data retention

The agent stores events locally when it cannot reach Sekoia.io. Use this page to adjust the local buffer size used for temporary retention.

### Default retention behavior

The agent saves logs locally on disk if the network connection is lost. When the buffer is full, the oldest logs are replaced by newer ones.

By default, the local buffer size is `100` MB.

### Change the local buffer size

{% stepper %}
{% step %}
### Open the configuration file

Edit the agent configuration file:

{% include "../../../.gitbook/includes/endpoint-agent-configuration-file-paths.md" %}
{% endstep %}

{% step %}
### Set the buffer size

Add or modify the following setting:

```yaml
EventBufferCacheSize: 200
```

This value is the on-disk cache size in MB.
{% endstep %}

{% step %}
### Restart the agent

Restart the agent to apply the new setting:

{% include "../../../.gitbook/includes/restart-the-endpoint-agent.md" %}
{% endstep %}
{% endstepper %}

### Related articles

* [Collect logs in files](collect-logs-in-files.md) Configure additional local file sources.
* [Resource footprint](resource-footprint.md) Review average CPU, memory, and disk usage.
* [Troubleshoot](troubleshoot.md) Investigate buffer or disk-related issues.
