# Install the Sekoia Endpoint Agent

This article explains how to install the Sekoia Endpoint Agent on Windows, Linux, and macOS. The agent installs as a system service and starts collecting events automatically once installed.

## Prerequisites

Before installing the agent, make sure the required network streams are open for your region. See [Sekoia Endpoint Agent](/integration/categories/endpoint/sekoiaio.md#prerequisites) for the full list.

!!! warning "Hosts with an EDR installed"
    If the target host already runs an EDR, the EDR's threat detection actions generate events that the Sekoia Endpoint Agent collects. This may trigger false positive alerts from detection rules at effort levels 3 and 4. Fine-tune those rules to reduce false positives after deployment.

## Step 1: Create an intake

Create a [new intake associated with the Sekoia Endpoint Agent](https://app.sekoia.io/operations/intakes/new?match[name]=Sekoia.io%20Endpoint%20Agent){:target="_blank"}. The intake key generated here is required during installation.

## Step 2: Download the agent

Use the download link provided in the intake description in the Sekoia interface.

## Step 3: Install the agent

=== "Windows"

    Execute the following command as an administrator:

    ```shell
    .\agent-latest.exe install --intake-key <INTAKE_KEY>
    ```

    To verify the agent is running as a service:

    ```shell
    Get-Service SEKOIAEndpointAgent
    ```

=== "Linux"

    If `auditd` is running on the host, stop and disable it before installing the agent.

    !!! note "Why auditd must be stopped"
        The agent pushes rules to the Linux audit framework. If `auditd` is running simultaneously, the two processes conflict and the agent cannot function correctly. The disable command ensures this configuration persists after a reboot.

    ```shell
    sudo systemctl stop auditd
    sudo systemctl disable auditd
    ```

    If the stop command returns `Failed to stop auditd.service: Operation refused`, set `RefuseManualStop` to `no` inside `/usr/lib/systemd/system/auditd.service`, run `sudo systemctl daemon-reload`, then retry.

    Install the agent:

    ```shell
    chmod +x ./agent-latest
    sudo ./agent-latest install --intake-key <INTAKE_KEY>
    ```

    To verify the agent is running as a service:

    ```shell
    sudo systemctl status SEKOIAEndpointAgent.service
    ```

    **Disable journald audit logging**

    By default, `journald` listens to the audit socket. To prevent it from interfering with the agent, disable audit logging in journald:

    ```shell
    systemctl stop systemd-journald-audit.socket
    systemctl disable systemd-journald-audit.socket
    systemctl mask systemd-journald-audit.socket
    systemctl restart systemd-journald
    ```

    A reboot may be necessary if audit events continue to appear in the logs after this change.

=== "macOS"

    **Unzip the archive**

    Double-click `SekoiaEndpointAgent.zip`. macOS Archive Utility extracts the files to the same directory as the archive.

    **Move the application to the Applications directory**

    Move `SekoiaEndpointAgent.app` from its download folder to `/Applications`.

    **Grant full disk access**

    1. Open **System Preferences**.
    2. Go to **Security & Privacy > Privacy** and select **Full Disk Access** in the left panel.
    3. Select the checkbox next to **SekoiaEndpointAgent**. If the panel is locked, click the lock icon to unlock it first.

    If **SekoiaEndpointAgent** does not appear in the list:

    1. Click the **+** button, then navigate to **Applications**.
    2. Select **SekoiaEndpointAgent** and click **Open**.
    3. Confirm the checkbox next to **SekoiaEndpointAgent** is selected, then close the window.

    **Run the install command:**

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY>
    ```

    To verify the agent is running as a service:

    ```shell
    sudo launchctl print system/SEKOIAEndpointAgent
    ```

Once installed, the agent collects, normalizes, and sends event logs to Sekoia over HTTPS (port 443).

## Set the region

By default, the agent communicates with the FRA1 region. To specify a different region, append `--region <region_name>` to the install command.

For example, to use the `fra2` region:

=== "Windows"

    ```shell
    .\agent-latest.exe install --intake-key <INTAKE_KEY> --region fra2
    ```

=== "Linux"

    ```shell
    ./agent-latest install --intake-key <INTAKE_KEY> --region fra2
    ```

=== "macOS"

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY> --region fra2
    ```

## Enable Host Hygiene collection

!!! note "Reveal module required"
    Host Hygiene telemetry collection is a feature of the Sekoia Reveal module.

You can enable Host Hygiene collection during installation or by editing the configuration file after installation.

### During installation

Append the `--compliance-collector` flag to the install command:

=== "Windows"

    ```shell
    .\agent-latest.exe install --intake-key <INTAKE_KEY> --compliance-collector
    ```

=== "Linux"

    ```shell
    ./agent-latest install --intake-key <INTAKE_KEY> --compliance-collector
    ```

=== "macOS"

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY> --compliance-collector
    ```

### After installation

1. Open the configuration file:

    === "Windows"

        ```
        C:\Windows\System32\config\systemprofile\AppData\Local\Sekoia.io\EndpointAgent\config.yaml
        ```

    === "Linux"

        ```
        /etc/endpoint-agent/config.yaml
        ```

    === "macOS"

        ```
        /etc/endpoint-agent/config.yaml
        ```

2. Add the following configuration:

    ```yaml
    roles:
      - event-collector
      - compliance-collector
    ```

3. Restart the agent:

    === "Windows"

        Execute the following command as an administrator:

        ```shell
        Restart-Service SEKOIAEndpointAgent
        ```

    === "Linux"

        ```shell
        sudo systemctl restart SEKOIAEndpointAgent.service
        ```

    === "macOS"

        ```shell
        sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent service restart
        ```

## Related articles

[Sekoia Endpoint Agent](/integration/categories/endpoint/sekoiaio.md): Overview of the agent, supported OS versions, prerequisites, and resource footprint.

[Configure the Sekoia Endpoint Agent](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md): How to set up log file collection, proxy, retention, and optional features.

[Update and uninstall the Sekoia Endpoint Agent](/integration/categories/endpoint/update_uninstall_sekoia_endpoint_agent.md): How to update the agent manually and remove it from a host.

[Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md): How to read agent logs and resolve common errors.
