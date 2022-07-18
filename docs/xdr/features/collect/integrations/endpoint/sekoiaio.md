uuid: 250e4095-fa08-4101-bb02-e72f870fcbd1
name: SEKOIA.IO Endpoint Agent
type: intake

# SEKOIA.IO Endpoint Agent

SEKOIA.IO provides its own agent allowing to collect interresting events with a minimal configuration overhead. This agent sends events directly to SEKOIA.IO.

!!! note
    The SEKOIA.IO agent is currently in beta for Windows and Linux only.

{!_shared_content/operations_center/integrations/generated/sekoiaio-endpoint_do_not_edit_manually.md!}

## Installation

### Intake creation and download of the executable

The first step to use the agent is to create a new intake associated to the SEKOIA.IO Agent.
A link to download the latest version of the agent is available in the description of the intake.

![SEKOIA.IO for Endpoints intake](/assets/operation_center/data_collection/ingestion_methods/agent/sekoiaio_for_endpoints.png){: style="max-width:100%"}

### Installation

The Endpoint Detection Agent is a binary which you can easily install on Windows or Linux systems, after having created a dedicated intake on SEKOIA.IO XDR.

=== "Windows"

    The following command must be executed **as an administrator**:

    ```shell
    agent.exe -install -instake_key <INTAKE_KEY>
    ```

    To make sure the agent has been successfully installed as a service you can run the following command:

    ```shell
    Get-Service SEKOIAEndpointAgent
    ```

=== "Linux"

    If `auditd` is running on the machine we must disable it before installing the linux agent:

    ```shell
    sudo systemctl stop auditd
    sudo systemctl disable auditd
    ```

    Now that `auditd` is disabled we can install the agent:

    ```shell
    sudo ./agent -install -instake_key <INTAKE_KEY>
    ```

    To make sure the agent has been successfully installed as a service you can run the following command:

    ```shell
    sudo systemctl status SEKOIAEndpointAgent.service
    ```

 Once installed, the agent collects event logs, normalizes them and sends them to SEKOIA.IO. The protocol used to send events is HTTPS (443).

### Proxy Support

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

If you want to automate the installation of the agent with this configuration option, make sure a `config.yaml` file with this line is present in the working directory when launching the install command.

### Optional steps

=== "Windows"

    #### Install Sysmon

    If you want to improve detection and investigation capabilities, you may want to enable Sysmon. When installed, the SEKOIA.IO Agent will automatically collect logs produced by Sysmon if they are not already collected by the agent.

    > Warning: The installation of this tool will generate more logs, so it will consume more CPU ressources. Install it on equipements that are correctly dimensioned, or try it on low risk assets at first.

    Sysmon is a Microsoft tool you can download on their [website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
    A common installation instruction and configuration file is available on [SwiftOnSecurity's Github](https://github.com/SwiftOnSecurity/sysmon-config).
