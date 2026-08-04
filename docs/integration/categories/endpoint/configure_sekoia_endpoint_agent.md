# Configure the Sekoia Endpoint Agent

This article covers the configuration options available for the Sekoia Endpoint Agent after installation: collecting logs from files, configuring a proxy, adjusting the local event buffer, and enabling optional telemetry features.

## Edit the configuration file

Most configuration options require editing the agent configuration file and restarting the agent.

The configuration file is located at:

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

!!! warning "YAML validity"
    The configuration file must be valid YAML. An invalid file prevents the agent from starting. If the file is valid YAML but contains invalid optimization rules, the agent logs an error and ignores those rules.

After editing the file, restart the agent:

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

## Collect logs from files

!!! note
    Use this feature to monitor application logs such as NGINX access logs. The agent collects all system-related events automatically without extra configuration.

The agent can forward logs from specific files to Sekoia. This is useful for applications that write their output to disk.

1. Open the configuration file (see [Edit the configuration file](#edit-the-configuration-file)).

2. Add a `logfiles` entry for each file to monitor:

    ```yaml
    logfiles:
      - filepath: /var/log/nginx/access.log  # Path to the file to watch
        intakekey: <INTAKE_KEY>               # Intake key matching the log format
    ```

!!! warning "Use a matching intake key"
    The intake key must correspond to the format of the log file. For example, use an intake key from the NGINX format to collect NGINX access logs.

To monitor multiple files, add an entry for each:

```yaml
logfiles:
  - filepath: /var/log/nginx/access.log
    intakekey: <INTAKE_KEY>
  - filepath: /var/log/mysql/mysql.log
    intakekey: <INTAKE_KEY>
```

3. Restart the agent (see [Edit the configuration file](#edit-the-configuration-file)).

### Use file patterns

The `filepath` attribute supports glob patterns to match multiple files. For example, `/var/log/nginx/*.log` matches all log files in `/var/log/nginx/`.

To restrict matching, use character ranges. For example, `/var/log/nginx/*[a-z].log` matches `/var/log/nginx/access.log` but not `/var/log/nginx/access.2023-02-14.log`. This is useful when log rotation is enabled.

!!! note
    The recursive glob pattern `**` is not supported.

## Configure proxy support

The agent can route its HTTPS requests through a proxy server.

1. Open the configuration file (see [Edit the configuration file](#edit-the-configuration-file)).

2. Add the following line:

    ```yaml
    HTTPProxyURL: "<PROXY_URL>"
    ```

    The URL must follow the format `http://user:pass@host:port`.

    To automate installation with a proxy, place a `config.yaml` file containing this line in the working directory before running the install command.

3. Restart the agent (see [Edit the configuration file](#edit-the-configuration-file)).

## Configure the local event buffer

The agent saves events to a local buffer on disk when the internet connection is unavailable. Once connectivity is restored, buffered events are sent to Sekoia first. When the buffer is full, older events are replaced by newer ones.

The default buffer size is 100 MB.

1. Open the configuration file (see [Edit the configuration file](#edit-the-configuration-file)).

2. Add or update the following option:

    ```yaml
    EventBufferCacheSize: 200  # Size in MB of the on-disk buffer
    ```

3. Restart the agent (see [Edit the configuration file](#edit-the-configuration-file)).

## Optional features

### Install Sysmon (Windows only)

Sysmon provides additional telemetry on Windows. When Sysmon is installed, the Sekoia Endpoint Agent automatically collects Sysmon logs.

!!! warning
    Sysmon increases the volume of events generated and raises CPU usage. Test it on low-risk assets before deploying broadly.

Download Sysmon from [microsoft.com](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon). A widely used configuration file is available on [Florian Roth's GitHub](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml), which is an updated version of the [SwiftOnSecurity configuration](https://github.com/SwiftOnSecurity/sysmon-config.md).

### Configure Security log auditing (Windows only)

A well-configured security log auditing policy allows the agent to collect a broader range of security events on Windows. Follow this guide for an optimal setup: [Configuring Security Log Audit Settings](https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/main/ConfiguringSecurityLogAuditPolicies.md).

### Collect DNS resolution events (Linux only)

DNS resolution events are not collected by default on Linux.

1. Open the configuration file (see [Edit the configuration file](#edit-the-configuration-file)).

2. Add the following option:

    ```yaml
    EnableDNSResolutions: true
    ```

3. Restart the agent:

    ```shell
    sudo systemctl restart SEKOIAEndpointAgent.service
    ```

### Exclude directories from hash computation

To prevent the agent from computing file hashes for files in a specific directory, add the `HashesExcludedPaths` option to the configuration file.

1. Open the configuration file (see [Edit the configuration file](#edit-the-configuration-file)).

2. Add the following configuration:

    ```yaml
    HashesExcludedPaths:
      - C:\path\to\ignore
    ```

3. Restart the agent (see [Edit the configuration file](#edit-the-configuration-file)).

### Customize agent log file rotation {#customize-agents-log-file-rotation}

By default, agent log files are rotated when they reach 100 MB, and up to 5 rotated files are kept in compressed form.

The following options control this behavior:

| Option | Description | Default |
|---|---|---|
| `LogMaxSize` | Maximum size in MB before rotation | `100` |
| `LogMaxBackups` | Maximum number of rotated files to keep | `5` |
| `LogCompress` | Whether to compress rotated files | `true` |

1. Open the configuration file (see [Edit the configuration file](#edit-the-configuration-file)).

2. Add the options you want to customize:

    ```yaml
    LogMaxSize: 50
    LogMaxBackups: 10
    LogCompress: false
    ```

3. Restart the agent (see [Edit the configuration file](#edit-the-configuration-file)).

## Related articles

[Sekoia Endpoint Agent](/integration/categories/endpoint/sekoia_endpoint_agent.md): Overview of the agent, supported OS versions, prerequisites, and resource footprint.

[Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md): How to create an intake, download, and install the agent on Windows, Linux, and macOS.

[Reduce event volume from the Sekoia Endpoint Agent](/integration/categories/endpoint/reduce_event_volume_endpoint_agent.md): How to filter events at the agent level using optimization rules.

[Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md): How to read agent logs and resolve common errors.
