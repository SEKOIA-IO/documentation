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
    * <https://app.fra2.sekoia.io/>

=== "MCO1"
    * <https://app.mco1.sekoia.io/>

=== "UAE1"
    * <https://app.uae1.sekoia.io/>

=== "USA1"
    * <https://app.usa1.sekoia.io/>


## Installation

!!! warning "Coexistence with EDR"

        If you want to install this agent on a machine with an EDR in place, please keep in mind that most EDRs perform actions to detect malware or other types of threats. 
		Those actions generate events that our agent collects. This may result in raising false positive alerts from our detection rules of effort levels 3 and 4. Customers need to fine-tune these rules to reduce the occurrence of false positives.

### Step 1: Create an intake

To generate a unique identifier for your logs, navigate to the Operations > Intakes page and create a [new intake associated with the Sekoia.io Agent](https://app.sekoia.io/operations/intakes/new?match[name]=Sekoia.io%20Endpoint%20Agent){:target="_blank"}.

### Step 2: Download executable

To obtain the binary, use the download link provided in the description of your newly created intake.

### Step 3: Installation

To install the agent, use the command specific to your operating system. Replace <INTAKE_KEY> with the key generated in Step 1.

=== "Windows"
1. Download the executable using the link provided in the intake description.
2. Open a terminal as an administrator.
3. To install the agent, run the following command:
   
	 ```shell
    .\agent-latest.exe install --intake-key <INTAKE_KEY>
    ```
4. To verify the service status, run:
    ```shell
    Get-Service SEKOIAEndpointAgent
    ```


=== "Linux"

!!! note "Auditd Conflict"

    You must stop the `auditd` service to enable the agent to work properly.
	
1. To disable `auditd`, run:
    ```shell
    sudo systemctl stop auditd
    # In case of error "Failed to stop auditd.service: Operation refused"
    # try to set "RefuseManualStop" to "no" inside "/usr/lib/systemd/system/auditd.service"
    # reload the systemctl daemon "sudo systemctl daemon-reload"
    # and retry "sudo systemctl stop auditd"
    sudo systemctl disable auditd
    ```
2. To make the binary executable, run:
    `chmod +x ./agent-latest`
3. To install the agent, run:
     ```shell
    chmod +x ./agent-latest
    sudo ./agent-latest install --intake-key <INTAKE_KEY>
    ```
4. To verify the service status, run:
    ```shell
    sudo systemctl status SEKOIAEndpointAgent.service
    ```


#### Configure journald for the Linux Agent

To ensure the Sekoia.io Endpoint Agent correctly captures events via the audit framework, you must prevent **journald** from listening to the audit socket. This configuration avoids event competition between the two services.

**Prerequisites**
* Access to the Linux machine with **root** or **sudo** privileges.
* The Sekoia.io Endpoint Agent must be installed on the host.

**Disable audit logging in journald**

Perform the following steps to disable the audit socket in **journald**:

1. To stop the service from listening to audit events, run:
    `systemctl stop systemd-journald-audit.socket`
2. To prevent the socket from starting automatically in the future, run:
    `systemctl disable systemd-journald-audit.socket`
3. To ensure other services cannot trigger the socket, run:
    `systemctl mask systemd-journald-audit.socket`
4. To apply the new configuration, restart the journald daemon:
    `systemctl restart systemd-journald`

!!! note

    If audit events continue to appear in your logs after these steps, you must reboot the machine to fully clear the socket state.

Once configured, the agent successfully collects, normalizes, and sends event logs to Sekoia.io via HTTPS on port 443. 


=== "MacOs"
1. Open the Archive: double-click the **SekoiaEndpointAgent.zip** archive to extract it.
2. Move the application to the `/Applications` directory.
3. Grant full disk access to SekoiaEndpointAgent: Navigate to **System Preferences > Security & Privacy > Privacy**.
4. Select **Full Disk Access**.
5. Click the **+** icon and select **SekoiaEndpointAgent** from the Applications folder.
 !!! note

 If you can't find SekoiaEndpointAgent in step 4, do the following:

        1.  Click the plus (+) icon (at the bottom left corner of the window) and navigate to Applications.
        2.  In the left panel, find SekoiaEndpointAgent and click Open. Make sure SekoiaEndpointAgent is ticked and then close the window.

6. Tick the checkbox for **SekoiaEndpointAgent**.

!!! note

    If the lock at the bottom left is locked, click it to unlock the Privacy pane.

7. To install the agent, run the following command in a terminal:
   
    ```shell
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent install --intake-key <INTAKE_KEY>
    ```

    To make sure the agent is successfully installed as a service, run the following command:

    ```shell
    sudo launchctl print system/SEKOIAEndpointAgent
    ```

Once installed, the agent collects, normalizes, and sends event logs to Sekoia.io. The protocol used to send events is HTTPS (443).

## Configuration options

### Set a specific region

To point the agent to a specific data region, append the append the `--region <region_name>` at the end of the command during installation.

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
### Enable host hygiene collection
!!! note

    Collection of Hygiene telemetry are a feature of the Reveal module.

Host Hygiene collection can be enabled during the initial installation of the Sekoia Agent or by modifying the agent's configuration file.

#### Method 1: During Agent Installation

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

#### Method 2: Editing the Configuration File

If the Sekoia Agent is already installed, you can enable Host Hygiene collection by editing its configuration file. Locate the configuration file and add `compliance-collector` to the `roles` section.

=== "Windows"

    ```shell
    C:\Windows\System32\config\systemprofile\AppData\Local\Sekoia.io\EndpointAgent\config.yaml
    ```

=== "Linux"

    ```shell
    /etc/endpoint-agent/config.yaml
    ```

=== "MacOs"

    ```shell
    /etc/endpoint-agent/config.yaml
    ```

Add the following configuration:

    ```yaml
    roles:
    - event-collector
    - compliance-collector
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

=== "MacOs"

    Execute the following command:

    ```
    sudo /Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent service restart

## Manage the endpoint agent 

### Update

#### Disable automatic update

By default, the agent will be updated automatically. To disable this feature, specify the `--disable-auto-update` flag during the installation.

#### Manual update

The agent updates automatically by default. To update the agent manually, follow the instructions specific to your OS.

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

	1. Open a terminal as an administrator.
	2. Execute the following command:

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

	1. Open a terminal as an administrator.
	2. Execute the following command:

    ```shell
    .\agent-latest.exe -service stop
    .\agent-latest.exe -service uninstall
    ```

    3. Remove the folders created by the agent:

      * `$ProgramFiles\EndpointAgent`
        * Where `$ProgramFiles` refers to the path to the `Program Files` folder, usually `c:\Program Files`
      * `$ProgramData\EndpointAgent`
        * Where `$ProgramData` refers to the path to the `ProgramData` folder, usually `c:\ProgramData`

=== "Linux"

	1. To remove the service, execute the following command:

    ```shell
    sudo /opt/endpoint-agent/agent -service stop
    sudo /opt/endpoint-agent/agent -service uninstall
    ```

	2. Remove the folders created by the agent:

    ```shell
    sudo rm -rf /opt/endpoint-agent
    sudo rm -rf /etc/endpoint-agent
    ```

## Collect logs in files

!!! INFO
    This feature allows you to monitor and collect logs from applications like NGINX. The agent automatically collects logs for all system-related events.

The agent offers to send logs contained in files to Sekoia.io.

If you want to enable this feature, follow these steps:

### Step 1. Edit the configuration file

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

### Step 2. Configure 
Add the following configuration:**

	```yaml
	logfiles:
	    - filepath: /var/log/nginx/access.log  # Path to the file to watch
	      intakekey: {intake key}  # Intake key to use to send the events
	```

!!! WARNING
    It's important to use an intake key from a format that matches the content of the log file.

    For example, an intake key from the NGINX format is required for watching NGINX access logs.

To monitor multiple files, add a new entry for each path as shown below:

```yaml
logfiles:
    - filepath: /var/log/nginx/access.log  # Path to the file to watch
      intakekey: {intake key}  # Intake key to use to send the events
    - filepath: /var/log/mysql/mysql.log
      intakekey: {intake key}
```

!!! WARNING
    Your configuration file must be a valid YAML. An invalid file can prevent the agent from starting.

### Step 3. Use file patterns (optional):
It is possible to specify patterns in the `filepath` attribute to match multiple files.

!!! example

    `/var/log/nginx/*.log` will match all the log files located under `/var/log/nginx/`.

It is also possible to restrict the allowed matching characters by specifying a range between brackets.

!!! example

    For example, the pattern `/var/log/nginx/*[a-z].log` will match `/var/log/nginx/access.log` but not `/var/log/nginx/access.2023-02-14.log`.
    This kind of pattern is particularly useful when log rotation is enabled.

!!! note

	The recursive globstart pattern `**` is currently not supported

### Step 4. Once the configuration file is modified, restart the agent:**

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

## Manage data retention

The agent sends the host logs through the Internet. The agent saves logs locally on disk in a local buffer if the Internet connection is lost. Once the logs exceed the buffer size, the older logs are replaced by newer ones. When the Internet connection is restored, the older logs are sent to Sekoia.io first.

### Increase the local buffer size
By default the local buffer size is set to 100 MB. 

You can change this value by editing the `EventBufferCacheSize` option in the configuration file.
To change the value:

1. Open the configuration file at:

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


2. Add or modify the following configuration:
    ```yaml
    EventBufferCacheSize: 200  # Size in MB of the on-disk cache for events when no network connection is available
    ```

3. Once the configuration file is modified, restart the agent:

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

## Manage events and fields

The Sekoia.io Endpoint Agent allows you to filter and categorize telemetry data to focus on relevant security events and optimize resource consumption.

### Ignore events with optimization rules

!!! INFO
    This feature is currently in beta

Optimization rules enable the agent to discard specific events locally based on field values before they are sent to the platform. 

An optimization rule can be created:

- Locally on the agent by editing its configuration file
- Centrally from the Sekoia.io platform

#### Optimization rule structure

Each optimization rule is composed of:

- An** UUID** defining the unique identifier of the rule.
- An **action code** defining the action to apply. The agent currently only supports the action to ignore (`action: 1`).
- A **list of filters** defining the conditions to match an event. All filters must match for the rule to match.
  Each filter is composed of:
    - A field name: `field`
    - An operator: `operator`
    - A value: `value`

!!! note
    String comparisons are case-sensitive.

The supported operators are:

| Operator code | Description                                           | Field type |
|---------------|-------------------------------------------------------|------------|
| ==            | The field value is equal to the value                 | all        |
| !=            | The field value is not equal to the value             | all        |
| contains      | The field value contains the value                    | string     |
| not contains  | The field value does not contain the value            | string     |
| >             | The field value is greater than the value             | number     |
| >=            | The field value is greater than or equal to the value | number     |
| <             | The field value is less than the value                | number     |
| <=            | The field value is less than or equal to the value    | number     |


!!! info
	
    - If multiple optimization rules match the same event, they are applied sequentially following their order of creation.
    - Ignored events are reported in the agent’s health events.
    - Each rule’s properties include a counter for the number of ignored events.

??? example "Example Rule: Ignore Notepad text files"

	This rule ignores events where the process name is notepad.exe AND the file extension is txt.
    ```yaml
    - uuid: 30bb044d-f7ba-448a-81c2-7f3c41a1fbf9
       action: 1
       filters:
         - field: process.name
          operator: ==
         value: "notepad.exe"
        - field: file.extension
          operator: ==
          value: "txt"
    ```

!!! note
    The performance impact of optimization rules is negligible.
    The agent is optimized to apply them efficiently with minimal CPU and memory overhead.

#### Configure local optimization rules

To define optimization rules locally on the agent, they must be defined in the agent's configuration file.

!!! WARNING
    If the YAML configuration file is invalid:

    - If it is valid YAML but contains invalid optimization rules: the agent logs an error and ignores the rules.
    - If it is not valid YAML, the agent logs an error and exits.


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
    OptimizationRules:
      - uuid: "30bb044d-f7ba-448a-81c2-7f3c41a1fbf9"
        action: 1
        filters:
          - field: process.name
            operator: ==
            value: "notepad.exe"
          - field: file.extension
            operator: ==
            value: "txt"
    ```

3. Once the configuration file is modified, restart the agent:

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

#### Manage remote optimization rules

Remote optimization rules can be defined centrally from the Sekoia.io platform.

!!! INFO
    To manage optimization rules in the platform the user must have the permission to manage intakes.

##### Allow the agent to fetch optimization rules

The first step to use remote optimization rules is to allow the agent to fetch them from the platform.
To do so the `RemoteOptimizationRules` option must be set to `true` in the agent's configuration file.

1. Open the configuration file at:

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

2. To allow the agent to fetch platform rules, set the following option:
    ```yaml
    RemoteOptimizationRules: true
    ```

3. Once the configuration file is modified, restart the agent:
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

Once enabled:

- The agent fetches remote rules at startup and then every hour.
- If the agent is offline, it retries when connectivity is restored using cached rules.
- Local and remote rules are merged — both are applied.

The agent logs which optimization rules it applies.
These logs are sent to Sekoia.io, allowing analysts to audit rule versions and deployments across agents.



##### Create optimization rules in the platform

It is possible to create an optimization rule that will be applied to:

- All the agents from the community:  When creating the rule `format_uuid` must be set to the agent's format UUID: `250e4095-fa08-4101-bb02-e72f870fcbd1`
- A specific agent intake: When creating the rule `intake_uuid` must be set to the intake UUID and the format UUID to the agent's format UUID: `250e4095-fa08-4101-bb02-e72f870fcbd1`
- A specific agent:  When creating the rule `agent_id` must be set to the agent's ID and the format UUID to the agent's format UUID: `250e4095-fa08-4101-bb02-e72f870fcbd1`

Currently, you must use the Sekoia.io API to create remote optimization rules. 
Refer to the [API documentation](/developer/api.md#/Configuration/Intakes/post_optimization_rules_resource) for full details.

??? example "Example Rule of an optimization rule created from the platform:" 

   Send a `POST` to `https://api.sekoia.io/v1/sic/conf/intakes/optimization_rules/` with the following payload:

    === "For all agents from the community"

        ```json
        {
           "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
          "description": "Ignore notepad txt files",
          "action": 1,
          "filters": [
            {
              "field": "process.name",
              "operator": "==",
              "value": "notepad.exe"
            },
            {
              "field": "file.extension",
              "operator": "==",
              "value": "txt"
            }
          ]
        }
        ```
    === "For a specific intake"

        ```json
        {
          "intake_uuid": "your_intake_uuid",
          "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
          "description": "Ignore notepad txt files",
          "action": 1,
          "filters": [
            {
              "field": "process.name",
              "operator": "==",
              "value": "notepad.exe"
            },
             {
              "field": "file.extension",
              "operator": "==",
              "value": "txt"
            }
          ]
       }
        ```
    === "For a specific agent"
         ```json
        {
           "agent_id": "your_agent_id",
           "format_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1",
           "description": "Ignore notepad txt files",
           "action": 1,
           "filters": [
             {
               "field": "process.name",
              "operator": "==",
              "value": "notepad.exe"
             },
            {
              "field": "file.extension",
              "operator": "==",
              "value": "txt"
             }
           ]
        }
        ```


{!_shared_content/operations_center/integrations/generated/250e4095-fa08-4101-bb02-e72f870fcbd1.md!}

### Events examples

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

!!! tip "Automated Installation"
    If you want to automate the agent installation with this configuration option, ensure that a `config.yaml` file with this line is present in the working directory before launching the install command.
    The proxy URL should follow the format `http://user:pass@host:port`.

## Optional steps

### Enrich your telemetry or optimize agent behavior

Follow these steps to enrich your telemetry or optimize agent behavior based on your specific environment.

=== "Windows"

   **Install Sysmon**

    The Sekoia.io Agent automatically collects Sysmon logs if the service is present on the host.

    !!! warning
	    Sysmon generates a high volume of logs. Test this tool on low-risk assets first to ensure the hardware is correctly dimensioned.
	

    1. Download Sysmon from [the official microsoft website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
    2. Apply a maintain configuration such as [Florian Roth's configuration](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml).

   **Configure Security log auditing**

    A proper security log auditing configuration will allow the agent to collect different security-related events.

    For an optimal setup, follow [Yamato Security guide](https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/main/ConfiguringSecurityLogAuditPolicies.md).

=== "Linux"

    **Collect DNS resolution events**

    You can collect DNS resolutions events by enabling it in the agent configuration file:

    1. Edit the configuration file at:

	    ```
	    /etc/endpoint-agent/config.yaml
	    ```

    2. Add the following configuration:

        ```yaml
        EnableDNSResolutions: true
        ```

    3. Once the configuration file is modified, restart the agent:

       ```
       sudo systemctl restart SEKOIAEndpointAgent.service
       ```
### Manage performance and log management

#### Exclude directories from file hashing

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

3. Once the configuration file is modified, restart the agent:

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

#### Customize agent's log file rotation

By default, the agent's log files are rotated when they reach 100 MB in size, and up to 5 rotated log files are kept.

You can customize these thresholds in the config.yaml file.

  | Parameter      | Description                                   | Default |
| -------------- | --------------------------------------------- | ------- |
| LogMaxSize     | Maximum size in MB before rotation.           | 100     |
| LogMaxBackups  | Number of old log files to retain.            | 5       |
| LogCompress    | Whether to compress rotated logs (true/false).| true    |
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
LogMaxSize: 50          # Maximum size in MB of the log file before rotating it
LogMaxBackups: 10       # Maximum number of old log files to keep
LogCompress: false      # Whether to compress old log files
```

3. Once the configuration file is modified, restart the agent:

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

## Find available arguments and options
Please find options and arguments available for Sekoia Agent by executing:

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

### Common errors

- `ERR HTTP request to send logs to SEKOIA.IO failed StatusCode=422`

If this error appears in the agent's logs, check: is the intake key still valid? is the related community's subscription valid?
  

{!_shared_content/operations_center/detection/generated/suggested_rules_250e4095-fa08-4101-bb02-e72f870fcbd1_do_not_edit_manually.md!}
