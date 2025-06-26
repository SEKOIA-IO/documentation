uuid: 250e4095-fa08-4101-bb02-e72f870fcbd1
name: Sekoia.io Endpoint Agent
type: intake

# Sekoia.io Endpoint Agent

Sekoia.io provides its agent for collecting security-related events with a minimal configuration overhead. This agent sends events directly to Sekoia.io.

### Disclaimer

!!! INFO
    The Sekoia.io Endpoint Detection Agent preserves the integrity of logs collected from the operating system event log; it does NOT modify or rewrite logs.

## Supported OS versions

The Endpoint Detection Agent supports the following operating systems, **on 64-bit versions only**:

=== "Windows"

    * Windows 8
    * Windows 10
    * Windows 11
    * Windows Server 2016
    * Windows Server 2019
    * Windows Server 2022
    * Windows Server 2025

=== "Linux"

    The agent should support Linux distributions based on a kernel version of **3.10** or newer.

    Here's a non-exhaustive list of supported distributions:

    * Ubuntu 14.04 and newer
    * Debian 8 and newer
    * CentOS 7 and newer
    * Redhat 7 and newer

=== "MacOs"

    * macOS 13 Ventura and newer

## New features

To find out about the changes between each version please check the [agent's changelog](https://changelog.sekoia.io/changelog?type=t6527b1484d556)

## Prerequisites
The Sekoia.io Endpoint Agent uses the HTTPS protocol to send its events and has an automatic update mechanism. As a prerequisite, it's necessary to open the following streams:

=== "FRA1"

    * <https://intake.sekoia.io/>
    * <https://api.sekoia.io/>

=== "FRA2"
    * <https://fra2.app.sekoia.io/>

=== "MCO1"
    * <https://mco1.app.sekoia.io/>

=== "UAE1"
    * <https://app.uae1.sekoia.io/>

=== "USA1"
    * <https://app.usa1.sekoia.io/>


## Installation

### Disclaimer

!!! Warning
        If you want to install this agent on a machine with an EDR in place, please keep in mind that most EDRs perform actions to detect malware or other types of threats. Those actions generate events that our agent collects. This may result in raising false positive alerts from our detection rules of effort levels 3 and 4. Customers need to fine-tune these rules to reduce the occurrence of false positives.

### Step 1: Create an intake

The first step to use the agent is to create a [new intake associated with the Sekoia.io Agent](https://app.sekoia.io/operations/intakes/new?match[name]=Sekoia.io%20Endpoint%20Agent){:target="_blank"}.

### Step 2: Download executable

Use the download link provided in the description of the intake in the application.

### Installation

The Endpoint Detection Agent is easy to install on Windows or Linux systems once you create a dedicated intake key on Sekoia.io XDR.

=== "Windows"

    Execute the following commands **as an administrator**:

    ```shell
    .\agent-latest.exe install --intake-key <INTAKE_KEY>
    ```

    To make sure the agent is successfully installed as a service, run the following command:

    ```shell
    Get-Service SEKOIAEndpointAgent
    ```

=== "Linux"

    If `auditd` is running on the machine, you must deactivate it before installing the Linux agent:

    ```shell
    sudo systemctl stop auditd
    # In case of error "Failed to stop auditd.service: Operation refused"
    # try to set "RefuseManualStop" to "no" inside "/usr/lib/systemd/system/auditd.service"
    # reload the systemctl daemon "sudo systemctl daemon-reload"
    # and retry "sudo systemctl stop auditd"
    sudo systemctl disable auditd
    ```

    !!! note
        Stop the auditd service to enable the agent to work properly. The disable command is used to allow persistence of the configuration.  

    Now that `auditd` is disabled, you can install the agent:

    ```shell
    chmod +x ./agent-latest
    sudo ./agent-latest install --intake-key <INTAKE_KEY>
    ```

    To make sure the agent is successfully installed as a service, run the following command:

    ```shell
    sudo systemctl status SEKOIAEndpointAgent.service
    ```

    #### journald configuration

    To get events, the agent pushes rules to the audit framework. By default, **journald**  might listen to the audit socket for events.

    To disable audit logging, do the following as root:


        # Stop listening to audit events
        systemctl stop systemd-journald-audit.socket 

        # Disable it to avoid future start
        systemctl disable systemd-journald-audit.socket

        # Masking will prevent starting by other services
        systemctl mask systemd-journald-audit.socket

        # Restart journald
        systemctl restart systemd-journald


    A reboot may be necessary if the audit events are still appearing in the logs.

=== "MacOs"

    **Unzipping SekoiaEndpointAgent.zip Archive**

    1.  Open the Archive: Double-click the file. macOS will automatically open it using the Archive Utility.

    2.  Extracting Files: Once the Archive Utility opens, the files will be extracted to the same location as the original archive. You can also specify a different location if needed.

    **Move the application from its download folder to the `/Applications` directory.**

    **Grant full disk access to SekoiaEndpointAgent by following these steps:**

    1.  Click on the Apple icon on the top left corner of your screen.

    2.  Select System Preferences.

    3.  Go to Security & Privacy Preferences > Privacy and click Full Disk Access from the left panel.

    4.  Tick the checkbox for SekoiaEndpointAgent. If the lock at the bottom left is locked, click it to unlock the Privacy pane.

        If you can't find SekoiaEndpointAgent in step 4, do the following:

        1.  Click the plus (+) icon (at the bottom left corner of the window) and navigate to Applications.

        2.  In the left panel, find SekoiaEndpointAgent and click Open. Make sure SekoiaEndpointAgent is ticked and then close the window.

    **Now that `Full Disk Access` is enable, you can install the agent:**

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY>
    ```

    To make sure the agent is successfully installed as a service, run the following command:

    ```shell
    sudo launchctl print system/SEKOIAEndpointAgent
    ```

Once installed, the agent collects, normalizes, and sends event logs to Sekoia.io. The protocol used to send events is HTTPS (443).

#### Setting the region

It's possible to specify the region the agent will communicate with during the installation.
To do it, append `--region <region_name>` at the end of the command.

For example, if the agent must communicate with `fra2`, run the following command:

=== "Windows"

    ```shell
    .\agent-latest.exe install --intake-key <INTAKE_KEY> --region fra2
    ```

=== "Linux"

    ```shell
    ./agent-latest install --intake-key <INTAKE_KEY> --region fra2
    ```

=== "MacOs"

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY> --region fra2
    ```
#### Enabling Host Hygiene Collection
**Note:** Collection of Hygiene telemetry are a feature of the Reveal module.

Host Hygiene collection can be enabled during the initial installation of the Sekoia Agent or by modifying the agent's configuration file.

##### Method 1: During Agent Installation

To enable Host Hygiene collection during the agent installation, append the `--compliance-collector` flag to your installation command.

For example,

=== "Windows"

    ```shell
    .\agent-latest.exe install --intake-key <INTAKE_KEY> --compliance-collector
    ```

=== "Linux"

    ```shell
    ./agent-latest install --intake-key <INTAKE_KEY> ---compliance-collector
    ```

=== "MacOs"

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY> --compliance-collector
    ```

##### Method 2: Editing the Configuration File

If the Sekoia Agent is already installed, you can enable Host Hygiene collection by editing its configuration file. Locate the configuration file and add `compliance-collector` to the `roles` section.

=== "Windows"

        ```
        C:\Windows\System32\config\systemprofile\AppData\Local\Sekoia.io\EndpointAgent\config.yaml
        ```

    === "Linux"

        ```
        /etc/endpoint-agent/config.yaml
        ```

    === "MacOs"
    
        ```
        /etc/endpoint-agent/config.yaml
        ```

2. Add the following configuration:

        ```
        roles:
        - event-collector
        - compliance-collector
        ```

### Update

#### Disable automatic update

By default, the agent will be updated automatically. To disable this feature, specify the `--disable-auto-update` flag during the installation.

#### Manual update

To update the agent manually, follow the instructions specific to your OS.

=== "Windows"

    Execute the following command **as an administrator**:

    ```shell
    $ProgramFiles\EndpointAgent\agent-latest.exe update
    ```

    Where `$ProgramFiles` refers to the path to the `Program Files` folder, usually `c:\Program Files`.

=== "Linux"

    The following command must be executed:

    ```shell
    sudo /opt/endpoint-agent/agent update
    ```

=== "MacOs"

    The following command must be executed:

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent update
    ```


### Uninstall

To uninstall the agent, follow the instructions specific to your OS.

#### Since version 0.3.0

=== "Windows"

    To completely uninstall the agent on Windows, you must execute the command using a copy of the running executable.
    You can either:

    * Download the latest version of the agent and use this binary to perform the uninstall
    * Copy the running agent located at `$ProgramFiles\EndpointAgent\agent.exe` 
      * `$ProgramFiles` refers to the path to the `Program Files` folder, usually `c:\Program Files`

    Execute the following command **as an administrator**:

    ```shell
    .\agent-latest.exe uninstall
    ```
=== "Linux"

    Execute the following command:

    ```shell
    sudo /opt/endpoint-agent/agent uninstall
    ```

=== "MacOs"

    !!! WARNING
        It is not possible to uninstall the agent by dragging the application into the trash.

    Execute the following command:

    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent uninstall
    ```

#### For versions prior to 0.3.0

=== "Windows"

    To remove the service, execute the following commands **as an administrator**:

    ```shell
    .\agent-latest.exe -service stop
    .\agent-latest.exe -service uninstall
    ```

    Then, remove the folders created by the agent:

      * `$ProgramFiles\EndpointAgent`
        * Where `$ProgramFiles` refers to the path to the `Program Files` folder, usually `c:\Program Files`
      * `$ProgramData\EndpointAgent`
        * Where `$ProgramData` refers to the path to the `ProgramData` folder, usually `c:\ProgramData` 

=== "Linux"

    Execute the following commands to remove the service:

    ```shell
    sudo /opt/endpoint-agent/agent -service stop
    sudo /opt/endpoint-agent/agent -service uninstall
    ```

    Then, remove the folders created by the agent:

    ```shell
    sudo rm -rf /opt/endpoint-agent
    sudo rm -rf /etc/endpoint-agent
    ```

## Collect logs in files

!!! INFO
    This feature allows you to monitor and collect logs from applications like NGINX. The agent automatically collects logs for all system-related events.

The agent offers to send logs contained in files to Sekoia.io.

If you want to enable this feature, follow these steps:

1. Edit the configuration file at:

    === "Windows"

        ```
        C:\Windows\System32\config\systemprofile\AppData\Local\Sekoia.io\EndpointAgent\config.yaml
        ```

    === "Linux"

        ```
        /etc/endpoint-agent/config.yaml
        ```

    === "MacOs"
    
        ```
        /etc/endpoint-agent/config.yaml
        ```

2. Add the following configuration:
	
	```yaml
	logfiles:
	    - filepath: /var/log/nginx/access.log  # Path to the file to watch
	      intakekey: {intake key}  # Intake key to use to send the events
	```

!!! WARNING
    It's important to use an intake key from a format that matches the content of the log file.

    For example, an intake key from the NGINX format is required for watching NGINX access logs.

If you want to collect multiple source files on the host, just add a new entry in the configuration. 
For instance:
	
	```yaml
	logfiles:
	    - filepath: /var/log/nginx/access.log  # Path to the file to watch
	      intakekey: {intake key}  # Intake key to use to send the events
	    - filepath: /var/log/mysql/mysql.log
	      intakekey: {intake key}
	```

!!! WARNING
    Your configuration file must be a valid YAML. An invalid file can prevent the agent from starting.

Once the configuration file is modified, restart the agent:

=== "Windows"

    Execute the following command **as an administrator**:

    ```
    Restart-Service SEKOIAEndpointAgent
    ```

=== "Linux"

    Execute the following command:

    ```
    sudo systemctl restart SEKOIAEndpointAgent.service
    ```

=== "MacOs"

    Execute the following command:

    ```
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent service restart
    ```

### Using file patterns

It is possible to specify patterns in the `filepath` attribute to match multiple files. 
For example `/var/log/nginx/*.log` will match all the log files located under `/var/log/nginx/`.

It is also possible to restrict the allowed matching characters by specifying a range between brackets.
For example, the pattern `/var/log/nginx/*[a-z].log` will match `/var/log/nginx/access.log` but not `/var/log/nginx/access.2023-02-14.log`.
This kind of pattern is particularly useful when log rotation is enabled. 

!!! note
	The recursive globstart pattern `**` is currently not supported

## Retention

The agent sends the host logs through the Internet. The agent saves logs locally on disk in a non-customizable 100 MB memory space if the Internet connection is lost. Once the logs exceed the buffer size, the older logs are replaced by newer ones. When the Internet connection is restored, the older logs are sent to Sekoia.io first.

{!_shared_content/operations_center/integrations/generated/250e4095-fa08-4101-bb02-e72f870fcbd1.md!}

## Events examples

Here's a non-exhaustive list of events the agent can detect:

=== "Windows"

    * Files creation/deletion/rename
    * Process lifecycle
    * Remote thread execution
    * DNS Resolution
    * TCP connection
    * Powershell commands
    * WMI Activity
    * NTLM
    * Windows Defender events
    * Sysmon events if configured
    * ...

=== "Linux"

    * Root commands executions
    * Files creation/deletion/rename/change
    * Process lifecycle
    * TCP connection
    * Python/Perl commands
    * PIP/APT installs
    * Cron configuration & scheduled jobs
    * Sudoers file changes
    * Passwd operations
    * Suspicious activity (curl, wireshark, …)
    * ...

=== "MacOs"

    * Root commands executions
    * Files creation/deletion/rename/change
    * DNS Resolution
    * TCP connection
    * PIP/APT installs
    * Sudoers file changes
    * Passwd operations
    * Suspicious activity (curl, wireshark, …)
    * ...

## Proxy Support

The Sekoia.io agent can use a proxy server for its HTTPS requests if needed.
If you want to enable this feature, follow these steps:

1. Edit the configuration file at:

    === "Windows"

        ```
        C:\Windows\System32\config\systemprofile\AppData\Local\Sekoia.io\EndpointAgent\config.yaml
        ```

    === "Linux"

        ```
        /etc/endpoint-agent/config.yaml
        ```

    === "MacOs"

        ```
        /etc/endpoint-agent/config.yaml
        ```

2. Add the following line:

    ```
    HTTPProxyURL: "<PROXY_URL>"
    ```

If you want to automate the agent installation with this configuration option, ensure that a `config.yaml` file with this line is present in the working directory before launching the install command.

The proxy URL should follow the format `http://user:pass@host:port`.

## Optional steps

=== "Windows"

    #### Install Sysmon

    You can collect additional events using Sysmon. When installed, the Sekoia.io Agent will automatically collect Sysmon logs if it hasn't already done so.

    !!! warning
        Installing this tool will generate more logs, consuming more CPU resources. Install it on correctly dimensioned equipment or try it on low-risk assets at first.

    Sysmon is a Microsoft tool downloadable from [microsoft.com](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
    A common installation instruction and configuration file is available on [Florian Roth's GitHub](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml). This configuration is an updated (and maintained) version of the [SwiftOnSecurity's configuration](https://github.com/SwiftOnSecurity/sysmon-config.md), which can also be used.

    #### Configure Security log auditing

    A proper security log auditing configuration will allow the agent to collect different security-related events.
    
    This document can be followed for an optimal configuration: [Configuring Security Log Audit Settings](https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/main/ConfiguringSecurityLogAuditPolicies.md).

=== "Linux"

    #### Collect DNS resolution events

    You can collect DNS resolutions events by enabling it in the agent configuration file:

    1. Edit the configuration file at:
	
	    ```
	    /etc/endpoint-agent/config.yaml
	    ```

    2. Add the following configuration:
        
        ```yaml
        EnableDNSResolutions: true
        ```

    Once the configuration file is modified, restart the agent:

       ```
       sudo systemctl restart SEKOIAEndpointAgent.service
       ```

#### Don't compute hashes for files under a specific directory

To avoid having the agent computing hashes for files located under a specific directory the `HashesExcludedPaths` option can be added to the agent configuration.

If you want to enable this feature, follow these steps: 

1. Edit the configuration file at:
	
	=== "Windows"
	
	    ```
	    C:\Windows\System32\config\systemprofile\AppData\Local\Sekoia.io\EndpointAgent\config.yaml
	    ```
	
	=== "Linux"
	
	    ```
	    /etc/endpoint-agent/config.yaml
	    ```

	=== "MacOs"
	
	    ```
	    /etc/endpoint-agent/config.yaml
	    ```

2. Add the following configuration:

```yaml
HashesExcludedPaths:
  - C:\path\to\ignore`
```

Once the configuration file is modified, restart the agent:

=== "Windows"

    Execute the following command **as an administrator**:

    ```
    Restart-Service SEKOIAEndpointAgent
    ```

=== "Linux"

    Execute the following command:

    ```
    sudo systemctl restart SEKOIAEndpointAgent.service
    ```


## Additionnal information
Please find options and arguments available for Sekoia Agent by typing

=== "Windows"

    ````
    .\agent-latest.exe -h
    ````

=== "Linux"

    ````
    agent -h
    ````

=== "MacOs"

    ````
    /Applications/SekoiaEndpointAgent.app/Contents/MacOS/SekoiaEndpointAgent -h
    ````

**Usage**:

=== "Windows"

    ````
    .\agent-latest.exe <command> [<args>]
    ````

=== "Linux"

    ````
    agent-latest <command> [<args>]
    ````

=== "MacOs"

    ````
    /Applications/SekoiaEndpointAgent.app/Contents/MacOS/SekoiaEndpointAgent  <command> [<args>]
    ````



**Options**:

| Options | Meaning |
| -- | -- |
| --help, -h | display this help and exit |
| --version | display version and exit |

**Commands**:

| Commands | Meaning|
| -- | -- |
| install | install the agent |
| update | update the agent |
| uninstall |uninstall the agent |

## Resources footprint

We monitor the agent metrics and try to keep its footprint as small as possible.
Our agent uses, on average, less than 1% of CPU and around 36MB of RAM.

## Troubleshoot
The first step to troubleshooting your Sekoia agent installation is to check the logs.

Here are the paths where to find the logs:

=== "Windows"

    ```
    C:\Windows\System32\config\systemprofile\AppData\Local\SEKOIA.IO\EndpointAgent\logs\agent.log
    ```

=== "Linux"

    ```
    /var/log/endpoint-agent/agent.log
    ```

=== "MacOs"

    ```
    /var/log/endpoint-agent/agent.log
    ```

!!! note
	Please always use the latest Sekoia.io agent version. We recommend activating the update option.

If you need further assistance, provide our team with the following information:

1- Results of the setup request in case of failure (stack trace) + machine configuration

2- Logs of the agent

{!_shared_content/operations_center/detection/generated/suggested_rules_250e4095-fa08-4101-bb02-e72f870fcbd1_do_not_edit_manually.md!} 
