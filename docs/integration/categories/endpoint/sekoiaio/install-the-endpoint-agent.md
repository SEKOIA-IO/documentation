---
description: Install the Sekoia.io Endpoint Agent and enable installation-time options.
---

# Install the endpoint agent

Sekoia.io Endpoint Agent collects endpoint telemetry with minimal setup. You install it from a dedicated intake and send events directly to Sekoia.io.

### Prerequisites

You need the following items before you start:

* Access to **Operations > Intakes**
* Administrator or root privileges on the target host
* Outbound access to the required regional endpoints

{% hint style="warning" %}
If you install the agent on a host that already runs an EDR, you may generate false positives. EDR actions produce events that the agent collects. Fine-tune effort level 3 and 4 rules if needed.
{% endhint %}

### Installation steps

{% stepper %}
{% step %}
### Create an intake

To generate a unique identifier for your logs, navigate to **Operations > Intakes** and create a [new intake associated with the Sekoia.io Agent](https://app.sekoia.io/operations/intakes/new?match\[name]=Sekoia.io%20Endpoint%20Agent).
{% endstep %}

{% step %}
### Download the installer

To obtain the binary, use the download link provided in the intake description.
{% endstep %}

{% step %}
### Install the agent

Run the installation command for your operating system.

{% tabs %}
{% tab title="Windows" %}
Run the following command as an administrator:

```powershell
.\agent-latest.exe install --intake-key <INTAKE_KEY>
```
{% endtab %}

{% tab title="Linux" %}
If `auditd` is running, stop it before you install the agent:

```shell
sudo systemctl stop auditd
# In case of error "Failed to stop auditd.service: Operation refused"
# try to set "RefuseManualStop" to "no" inside "/usr/lib/systemd/system/auditd.service"
# reload the systemctl daemon "sudo systemctl daemon-reload"
# and retry "sudo systemctl stop auditd"
sudo systemctl disable auditd
```

{% hint style="info" %}
Stop `auditd` so the agent can work correctly. Disable it to keep this setting after reboot.
{% endhint %}

Install the agent:

```shell
chmod +x ./agent-latest
sudo ./agent-latest install --intake-key <INTAKE_KEY>
```
{% endtab %}

{% tab title="MacOS" %}
Move `SekoiaEndpointAgent.app` from the download folder to `/Applications`.

Grant full disk access:

1. Open **Apple menu > System Settings**.
2. Select **Privacy & Security**.
3. Select **Full Disk Access**.
4. Enable **SekoiaEndpointAgent**.

If the app is not listed:

1. Select **+**.
2. Open **Applications**.
3. Select **SekoiaEndpointAgent**.

Run the following command:

```shell
sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY>
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
### Verify the installation

Check that the agent is installed and running.

{% tabs %}
{% tab title="Windows" %}
```powershell
Get-Service SEKOIAEndpointAgent
```
{% endtab %}

{% tab title="Linux" %}
```shell
sudo systemctl status SEKOIAEndpointAgent.service
```
{% endtab %}

{% tab title="MacOS" %}
```shell
sudo launchctl print system/SEKOIAEndpointAgent
```
{% endtab %}
{% endtabs %}
{% endstep %}
{% endstepper %}

### Linux journald configuration

To ensure the agent captures audit events correctly, prevent **journald** from listening to the audit socket.

```shell
# Stop listening to audit events
systemctl stop systemd-journald-audit.socket

# Disable it to avoid future start
systemctl disable systemd-journald-audit.socket

# Mask it to block restarts from other services
systemctl mask systemd-journald-audit.socket

# Restart journald
systemctl restart systemd-journald
```

{% hint style="info" %}
If audit events still appear after these steps, reboot the host.
{% endhint %}

### Configuration options

#### Set a specific region

To target a specific region during installation, append `--region <region_name>` to the install command.

For example, to use `fra2`:

{% tabs %}
{% tab title="Windows" %}
```shell
.\agent-latest.exe install --intake-key <INTAKE_KEY> --region fra2
```
{% endtab %}

{% tab title="Linux" %}
```shell
./agent-latest install --intake-key <INTAKE_KEY> --region fra2
```
{% endtab %}

{% tab title="MacOS" %}
```shell
sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY> --region fra2
```
{% endtab %}
{% endtabs %}

#### Enable host hygiene collection

Host hygiene collection is part of the Reveal module. You can enable it during installation or later in the configuration file.

**Enable host hygiene during installation**

Append `--compliance-collector` to the install command.

{% tabs %}
{% tab title="Windows" %}
```shell
.\agent-latest.exe install --intake-key <INTAKE_KEY> --compliance-collector
```
{% endtab %}

{% tab title="Linux" %}
```shell
./agent-latest install --intake-key <INTAKE_KEY> --compliance-collector
```
{% endtab %}

{% tab title="MacOS" %}
```shell
sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY> --compliance-collector
```
{% endtab %}
{% endtabs %}

**Enable host hygiene in the configuration file**

1. Edit the configuration file:

{% include "../../../.gitbook/includes/endpoint-agent-configuration-file-paths.md" %}

2. Add the following configuration:

```yaml
roles:
- event-collector
- compliance-collector
```

3. Restart the agent:

{% include "../../../.gitbook/includes/restart-the-endpoint-agent.md" %}

### Related articles

* [Sekoia.io endpoint agent](./) Review supported platforms, prerequisites, and the article map.
* [Manage the endpoint agent](manage-the-endpoint-agent.md) Update or uninstall the agent after deployment.
* [Troubleshoot](troubleshoot.md) Diagnose installation or startup issues.
