# SEKOIA.IO Endpoint Agent

SEKOIA.IO provides its own agent allowing to collect interresting events with a minimal configuration overhead.

!!! note
    The SEKOIA.IO agent is currently in beta and for Windows only.

## Installation

### Intake creation and download of the executable

The first step to use the agent is to create a new intake associated to the SEKOIA.IO Agent.
A link to download the latest version of the agent is available in the description of the intake.

[Screenshot of the intake once it is released with the appropriate description]: <>

### Installation

The Endpoint Detection Agent is a Windows binary which you can easily install on Windows systems, after having created a dedicated intake on SEKOIA.IO XDR. The following command must be executed **as an administrator**:

```shell
agent.exe -install -instake_key <INTAKE_KEY>
```

To make sure the agent is successfully installed as a service you can run the following command:

```shell
 Get-Service SEKOIAEndpointAgent
```

Once installed, the agent collects Windows event logs from ETW (Event Tracing for Windows), normalizes them and sends them to SEKOIA.IO.

### Recommended: Install Sysmon

The SEKOIA.IO agent can leverage Sysmon when it is installed. To install it, follow the instructions on the [Microsoft website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
