uuid: 250e4095-fa08-4101-bb02-e72f870fcbd1
name: SEKOIA.IO Endpoint Agent
type: intake

# SEKOIA.IO Endpoint Agent

SEKOIA.IO provides its own agent allowing to collect interresting events with a minimal configuration overhead. This agent sends events directly to SEKOIA.IO.
	
{!_shared_content/operations_center/detection/generated/suggested_rules_250e4095-fa08-4101-bb02-e72f870fcbd1_do_not_edit_manually.md!}	

## Supported OS versions

The Endpoint Detection Agent supports the following operating systems, **on 64 bits version only**:

=== "Windows"

    * Windows 8
    * Windows 10
    * Windows 11
    * Windows server 2016
    * Windows server 2019
    * Windows server 2022

=== "Linux"

    Linux distributions based on a kernel version of **3.10** or newer should be supported by the agent.

    Here's a non-exhaustive list of supported distributions:

    * Ubuntu 14.04 and newer
    * Debian 8 and newer
    * CentOS 7 and newer
    * Redhat 7 and newer


## Installation

### Disclamer

!!! Warning
	If you want to install this agent on a machine that already has an EDR in place, be aware that most EDR perform actions on the machines to detect malwares or other types of threats. Those actions generate events that are collected by our agent. This may result to the raising of false positive alerts from our detection rules of effort level 3 and 4. It's important for customers to fine-tune these rules to reduce the occurrence of false positives.

### Intake creation and download of the executable

The first step to use the agent is to create a [new intake associated to the SEKOIA.IO Agent](https://app.sekoia.io/operations/intakes/new?match[name]=SEKOIA.IO%20Endpoint%20Agent){:target="_blank"}.
A link to download the latest version of the agent is available in the description of the intake.

### Installation

The Endpoint Detection Agent is easy to install on Windows or Linux systems once you created a dedicated intake key on SEKOIA.IO XDR.

=== "Windows"

    The following commands must be executed **as an administrator**:

    ```shell
    agent.exe install --intake-key <INTAKE_KEY>
    ```

    To make sure the agent has been successfully installed as a service you can run the following command:

    ```shell
    Get-Service SEKOIAEndpointAgent
    ```

=== "Linux"

    If `auditd` is running on the machine you must disable it before installing the linux agent:

    ```shell
    sudo systemctl stop auditd
    # In case of error "Failed to stop auditd.service: Operation refused"
    # try to set "RefuseManualStop" to "no" inside "/usr/lib/systemd/system/auditd.service"
    # reload the systemctl daemon "sudo systemctl daemon-reload"
    # and retry "sudo systemctl stop auditd"
    sudo systemctl disable auditd
    ```

    !!! note
    	It is very important that the auditd service is **stopped** for the agent to work properly. The disable command is used to allow persistence of the configuration.  

    Now that `auditd` is disabled you can install the agent:

    ```shell
    chmod +x ./agent-latest
    sudo ./agent-latest install --intake-key <INTAKE_KEY>
    ```

    To make sure the agent has been successfully installed as a service you can run the following command:

    ```shell
    sudo systemctl status SEKOIAEndpointAgent.service
    ```

 Once installed, the agent collects event logs, normalizes them and sends them to SEKOIA.IO. The contacted domain `intake.sekoia.io` uses the ip `51.159.9.95`. The protocol used to send events is HTTPS (443).

### Update

#### Disable automatic update

By default, the agent will update itself automatically. If you would like to disable this feature, the flag `--disable-auto-update` must be specified during the installation.

#### Manual update

To manually update the agent, follow the instructions specific to your OS:

=== "Windows"

    The following command must be executed **as an administrator**:

    ```shell
    $ProgramFiles\EndpointAgent\agent.exe update
    ```

    Where `$ProgramFiles` refers to the path to the `Program Files` folder, usually `c:\Program Files`.

=== "Linux"

    The following command must be executed:

    ```shell
    sudo /opt/endpoint-agent update
    ```


### Uninstall

To uninstall the agent, follow the instructions specific to your OS.

#### Since version 0.3.0

=== "Windows"

    In order to completely uninstall the agent on Windows the command must be executed using a copy of the running executable.
    You can either:

    * Download the latest version of the agent and use this binary to perform the uninstall
    * Copy the running agent located at `$ProgramFiles\EndpointAgent\agent.exe` 
      * `$ProgramFiles` refers to the path to the `Program Files` folder, usually `c:\Program Files`)

    The following command must be executed **as an administrator**:

    ```shell
    agent.exe uninstall
    ```

=== "Linux"

    The following command must be executed:

    ```shell
    sudo /opt/endpoint-agent/agent uninstall
    ```

#### For versions prior to 0.3.0

=== "Windows"

    The following commands must be executed **as an administrator** to remove the service:

    ```shell
    agent.exe -service stop
    agent.exe -service uninstall
    ```

    The folders created by the agent must then be removed:

      * `$ProgramFiles\EndpointAgent`
        * Where `$ProgramFiles` refers to the path to the `Program Files` folder, usually `c:\Program Files`
      * `$ProgramData\EndpointAgent`
        * Where `$ProgramData` refers to the path to the `ProgramData` folder, usually `c:\ProgramData` 

=== "Linux"

    The following commands must be executed to remove the service:

    ```shell
    sudo /opt/endpoint-agent/agent -service stop
    sudo /opt/endpoint-agent/agent -service uninstall
    ```

    The folders created by the agent must then be removed:

    ```shell
    sudo rm -rf /opt/endpoint-agent
    sudo rm -rf /etc/endpoint-agent
    ```

## Retention

The agent sends the host logs through the internet. If the host stops accessing the internet, the agent will store the logs locally on disk on a 100 MB memory space that cannot be customized. Once the logs exceed the size of the buffer, the older ones are replaced by newers. When the internet connexion is operational again, the older logs are sent first to SEKOIA.IO.

{!_shared_content/operations_center/integrations/generated/250e4095-fa08-4101-bb02-e72f870fcbd1.md!}

## Events examples

Here's a non-exhaustive list of kind of events the agent is able to detect

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

    


## Proxy Support

If needed, the SEKOIA.IO agent can use a proxy server for its HTTPS requests. If you want to enable this feature, edit
the configuration file at:

=== "Windows"

    ```
    C:\Windows\System32\config\systemprofile\AppData\Local\SEKOIA.IO\EndpointAgent\config.yaml
    ```

=== "Linux"

    ```
    /etc/endpoint-agent/config.yaml
    ```

and add the following line:
```
HTTPProxyURL: "<PROXY_URL>"
```

If you want to automate the installation of the agent with this configuration option, make sure that a `config.yaml` file with this line is present in the working directory before launching the install command.

The proxy URL should follow the format `http://user:pass@host:port`.

## Optional steps

=== "Windows"

    #### Install Sysmon

    If you want to improve detection and investigation capabilities, you may want to enable Sysmon. When installed, the SEKOIA.IO Agent will automatically collect logs produced by Sysmon if they are not already collected by the agent.

    !!! warning
    	The installation of this tool will generate more logs which will consume more CPU resources. Install it on equipment that are correctly 		dimensioned, or try it on low risk assets at first.

    Sysmon is a Microsoft tool downloadable from [microsoft.com](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
    A common installation instruction and configuration file is available on [Florian Roth's GitHub](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml). This configuration is an updated (and maintained) version of the [SwiftOnSecurity's configuration](https://github.com/SwiftOnSecurity/sysmon-config), which can also be used.

    #### Configure Security log auditing

    A proper security log auditing configuration will allow the agent to collect various  interresting security related events.
    
    This document can be followed for an optimal configuration: [Configuring Security Log Audit Settings](https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/main/ConfiguringSecurityLogAuditPolicies.md).

## Resources footprint

We monitor the agent metrics and try to keep its footprint as small as possible. 
Right now, our agent uses on average less than 3% of CPU and less than 1% of RAM.
