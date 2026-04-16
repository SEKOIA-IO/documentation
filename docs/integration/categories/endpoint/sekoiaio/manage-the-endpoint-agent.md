---
description: Update or uninstall the Sekoia.io Endpoint Agent.
---

# Manage the endpoint agent

Use this page to keep the Sekoia.io Endpoint Agent up to date or remove it from a host. The procedures cover supported update and uninstall paths by operating system.

### Update the agent

#### Disable automatic updates

The agent updates automatically by default. To disable this behavior, add `--disable-auto-update` during installation.

#### Update the agent manually

Use the following command for your operating system.

{% tabs %}
{% tab title="Windows" %}
Run the following command as an administrator:

```shell
$ProgramFiles\EndpointAgent\agent-latest.exe update
```

`$ProgramFiles` usually points to `C:\Program Files`.
{% endtab %}

{% tab title="Linux" %}
Run the following command:

```shell
sudo /opt/endpoint-agent/agent update
```
{% endtab %}

{% tab title="MacOS" %}
Run the following command:

```shell
sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent update
```
{% endtab %}
{% endtabs %}

### Uninstall the agent

#### Uninstall version 0.3.0 and later

{% tabs %}
{% tab title="Windows" %}
To uninstall the agent on Windows, use a copy of the running executable.

You can either:

* Download the latest agent version and use that binary
* Copy the running agent from `$ProgramFiles\EndpointAgent\agent.exe`

Run the following command as an administrator:

```shell
.\agent-latest.exe uninstall
```
{% endtab %}

{% tab title="Linux" %}
Run the following command:

```shell
sudo /opt/endpoint-agent/agent uninstall
```
{% endtab %}

{% tab title="MacOS" %}
{% hint style="info" %}
You cannot uninstall the agent by dragging the application to the trash.
{% endhint %}

Run the following command:

```shell
sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent uninstall
```
{% endtab %}
{% endtabs %}

#### Uninstall versions earlier than 0.3.0

{% tabs %}
{% tab title="Windows" %}
Remove the service:

```shell
.\agent-latest.exe -service stop
.\agent-latest.exe -service uninstall
```

Then remove the following folders:

* `$ProgramFiles\EndpointAgent`
* `$ProgramData\EndpointAgent`
{% endtab %}

{% tab title="Linux" %}
Remove the service:

```shell
sudo /opt/endpoint-agent/agent -service stop
sudo /opt/endpoint-agent/agent -service uninstall
```

Then remove the following folders:

```shell
sudo rm -rf /opt/endpoint-agent
sudo rm -rf /etc/endpoint-agent
```
{% endtab %}
{% endtabs %}

### Related articles

* [Install the endpoint agent](install-the-endpoint-agent.md) Install the agent and enable installation-time options.
* [Troubleshoot](troubleshoot.md) Find logs and common errors during update or uninstall.
* [Available arguments and options](available-arguments-and-options.md) Review supported commands and flags.
