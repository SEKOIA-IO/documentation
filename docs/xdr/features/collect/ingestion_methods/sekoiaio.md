# SEKOIA.IO Endpoint Agent

SEKOIA.IO provides its own agent allowing to collect interresting events with a minimal configuration overhead.

!!! note
    The SEKOIA.IO agent is currently in beta and for Windows only.

## Installation

### Intake creation and download of the executable

The first step to use the agent is to create a new intake associated to the SEKOIA.IO Agent.
A link to download the latest version of the agent is available in the description of the intake.

![SEKOIA.IO for Endpoints intake](/assets/operation_center/data_collection/ingestion_methods/agent/sekoiaio_for_endpoints.png){: style="max-width:100%"}

### Installation

The Endpoint Detection Agent is a Windows binary which you can easily install on Windows systems, after having created a dedicated intake on SEKOIA.IO XDR. The following command must be executed **as an administrator**:

```shell
agent.exe -install -intake-key <INTAKE_KEY>
```

To make sure the agent is successfully installed as a service you can run the following command:

```shell
 Get-Service SEKOIAEndpointAgent
```

Once installed, the agent collects Windows event logs from ETW (Event Tracing for Windows), normalizes them and sends them to SEKOIA.IO.

### Proxy Support

If needed, the SEKOIA.IO agent can use a proxy server for its HTTPS requests. If you want to enable this feature, edit
the configuration file at `C:\Windows\System32\config\systemprofile\AppData\Local\SEKOIA.IO\EndpointAgent\config.yaml` and add the following line:

```
HTTPProxyURL: "<PROXY_URL>"
```

If you want to automate the installation of the agent with this configuration option, make sure a `config.yaml` file with this line is present in the working directory when launching the install command.

### Recommended: Install Sysmon

If you want to improve detection and investigation capabilities, you may want to enable Sysmon. When installed, the SEKOIA.IO Agent will automatically collect logs produced by Sysmon.

> Warning: The installation of this tool will generate more logs, so it will consume more CPU ressources. Install it on equipements that are correctly dimensioned, or try it on low risk assets at first.

Sysmon is a Microsoft tool you can download on their [website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
A common installation instruction and configuration file is available on [SwiftOnSecurity's Github](https://github.com/SwiftOnSecurity/sysmon-config).
