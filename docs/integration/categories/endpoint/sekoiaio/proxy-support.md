---
description: Configure the agent to use an HTTP proxy.
---

# Proxy support

The Sekoia.io agent can send HTTPS requests through a proxy server. Use this page to configure the proxy URL in the agent configuration.

### Configure proxy support

{% stepper %}
{% step %}
### Open the configuration file

Edit the agent configuration file:

{% include "../../../.gitbook/includes/endpoint-agent-configuration-file-paths.md" %}
{% endstep %}

{% step %}
### Add the proxy URL

Add the following setting:

```yaml
HTTPProxyURL: "<PROXY_URL>"
```
{% endstep %}

{% step %}
### Restart the agent

Restart the agent to apply the new setting:

{% include "../../../.gitbook/includes/restart-the-endpoint-agent.md" %}
{% endstep %}
{% endstepper %}

### Proxy URL format

Use the following format for the proxy URL:

```
http://user:pass@host:port
```

If you automate the installation, make sure a `config.yaml` file that contains this setting is present in the working directory before you run the install command.

### Related articles

* [Install the endpoint agent](install-the-endpoint-agent.md) Install the agent and set installation-time options.
* [Manage events and fields](manage-events-and-fields.md) Review event handling and optimization rules.
* [Troubleshoot](troubleshoot.md) Debug connectivity and proxy-related issues.
