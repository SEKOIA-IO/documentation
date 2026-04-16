---
description: Find logs, collect diagnostics, and review common installation issues.
---

# Troubleshoot

Use this page to diagnose installation or runtime issues with the Sekoia.io Endpoint Agent. Start with the local agent logs, then gather the details needed for escalation.

### Find the agent logs

{% tabs %}
{% tab title="Windows" %}
```shell
C:\Windows\System32\config\systemprofile\AppData\Local\SEKOIA.IO\EndpointAgent\logs\agent.log
```
{% endtab %}

{% tab title="Linux" %}
```shell
/var/log/endpoint-agent/agent.log
```
{% endtab %}

{% tab title="MacOS" %}
```shell
/var/log/endpoint-agent/agent.log
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Use the latest Sekoia.io agent version. Enable automatic updates when possible.
{% endhint %}

### Gather troubleshooting data

If you need assistance, collect the following information:

* The setup request result or stack trace
* The machine configuration
* The agent logs

### Common errors

#### `ERR HTTP request to send logs to SEKOIA.IO failed StatusCode=422`

If this error appears in the agent logs, check the following items:

* The intake key is still valid
* The related community subscription is still valid

### Related articles

* [Install the endpoint agent](install-the-endpoint-agent.md) Revisit the installation flow and validation commands.
* [Manage the endpoint agent](manage-the-endpoint-agent.md) Review update and uninstall procedures when maintenance fails.
* [Proxy support](proxy-support.md) Validate proxy settings when connectivity errors occur.
