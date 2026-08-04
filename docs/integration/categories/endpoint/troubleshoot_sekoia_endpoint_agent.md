# Troubleshoot the Sekoia Endpoint Agent

This article helps you diagnose and resolve issues with the Sekoia Endpoint Agent by checking logs, using the CLI, and identifying common errors.

## Check the agent logs

The first step in troubleshooting is to check the agent log file.

=== "Windows"

    ```
    C:\Windows\System32\config\systemprofile\AppData\Local\SEKOIA.IO\EndpointAgent\logs\agent.log
    ```

=== "Linux"

    ```
    /var/log/endpoint-agent/agent.log
    ```

=== "macOS"

    ```
    /var/log/endpoint-agent/agent.log
    ```

!!! note
    Always use the latest version of the Sekoia Endpoint Agent. Enabling automatic updates is recommended.

If you contact Sekoia support, include the following information:

1. The full stack trace from the failed setup request, along with your machine configuration.
2. The agent log file.

## CLI reference

To list all available options and commands, run:

=== "Windows"

    ```shell
    .\agent-latest.exe -h
    ```

=== "Linux"

    ```shell
    agent -h
    ```

=== "macOS"

    ```shell
    /Applications/SekoiaEndpointAgent.app/Contents/MacOS/SekoiaEndpointAgent -h
    ```

**Usage:**

=== "Windows"

    ```shell
    .\agent-latest.exe <command> [<args>]
    ```

=== "Linux"

    ```shell
    agent-latest <command> [<args>]
    ```

=== "macOS"

    ```shell
    /Applications/SekoiaEndpointAgent.app/Contents/MacOS/SekoiaEndpointAgent <command> [<args>]
    ```

**Options:**

| Option | Description |
|---|---|
| `--help`, `-h` | Display help and exit |
| `--version` | Display version and exit |

**Commands:**

| Command | Description |
|---|---|
| `install` | Install the agent |
| `update` | Update the agent |
| `uninstall` | Uninstall the agent |

## Common errors

### ERR HTTP request to send logs to SEKOIA.IO failed StatusCode=422

This error indicates a problem with the intake key or the community subscription. Check:

* Whether the intake key is still valid.
* Whether the community's subscription is still active.

## Related articles

[Sekoia Endpoint Agent](/integration/categories/endpoint/sekoia_endpoint_agent.md): Overview of the agent, supported OS versions, prerequisites, and resource footprint.

[Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md): How to create an intake, download, and install the agent on Windows, Linux, and macOS.

[Configure the Sekoia Endpoint Agent](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md): How to set up log file collection, proxy, retention, and optional features.

[Update and uninstall the Sekoia Endpoint Agent](/integration/categories/endpoint/update_uninstall_sekoia_endpoint_agent.md): How to update the agent manually and remove it from a host.
