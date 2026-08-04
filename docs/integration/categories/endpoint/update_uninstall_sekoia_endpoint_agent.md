# Update and uninstall the Sekoia Endpoint Agent

This article explains how to update the Sekoia Endpoint Agent and how to remove it from Windows, Linux, and macOS hosts.

## Update the agent

### Automatic update

By default, the agent updates itself automatically. To disable this behavior, append the `--disable-auto-update` flag to the install command during the initial installation.

### Manual update

=== "Windows"

    Execute the following command as an administrator:

    ```shell
    $ProgramFiles\EndpointAgent\agent-latest.exe update
    ```

    `$ProgramFiles` refers to the path of your `Program Files` folder, typically `C:\Program Files`.

=== "Linux"

    ```shell
    sudo /opt/endpoint-agent/agent update
    ```

=== "macOS"

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent update
    ```

## Uninstall the agent

### Version 0.3.0 and later

=== "Windows"

    To uninstall on Windows, you must run the uninstall command using a copy of the agent binary that is not currently running as a service. Use one of the following approaches:

    * Download the latest version of the agent and use that binary.
    * Copy the running binary from `$ProgramFiles\EndpointAgent\agent.exe`, where `$ProgramFiles` is typically `C:\Program Files`.

    Execute the following command as an administrator:

    ```shell
    .\agent-latest.exe uninstall
    ```

=== "Linux"

    ```shell
    sudo /opt/endpoint-agent/agent uninstall
    ```

=== "macOS"

    !!! warning "Do not use the trash"
        Dragging the application to the trash does not fully remove the agent. Use the command below.

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent uninstall
    ```

### Versions prior to 0.3.0

=== "Windows"

    Execute the following commands as an administrator to stop and remove the service:

    ```shell
    .\agent-latest.exe -service stop
    .\agent-latest.exe -service uninstall
    ```

    Then, remove the following folders manually:

    * `$ProgramFiles\EndpointAgent` (where `$ProgramFiles` is typically `C:\Program Files`)
    * `$ProgramData\EndpointAgent` (where `$ProgramData` is typically `C:\ProgramData`)

=== "Linux"

    Stop and remove the service:

    ```shell
    sudo /opt/endpoint-agent/agent -service stop
    sudo /opt/endpoint-agent/agent -service uninstall
    ```

    Then, remove the agent folders:

    ```shell
    sudo rm -rf /opt/endpoint-agent
    sudo rm -rf /etc/endpoint-agent
    ```

## Related articles

[Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md): How to create an intake, download, and install the agent on Windows, Linux, and macOS.

[Sekoia Endpoint Agent](/integration/categories/endpoint/sekoia_endpoint_agent.md): Overview of the agent, supported OS versions, prerequisites, and resource footprint.

[Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md): How to read agent logs and resolve common errors.
