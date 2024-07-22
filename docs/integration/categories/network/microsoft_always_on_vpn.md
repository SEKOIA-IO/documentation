uuid: 80b8382e-0667-4469-bbc9-74be1e0ca1c1
name: Microsoft Always On VPN
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:
Microsoft Always On VPN is a Windows feature allowing secure connection to protected networks.

This guide will explain how to forward Network Policy Server (NPS) logs to Sekoia.io



## Configure

### NXLog agent to a syslog concentrator

#### Configuring NPS logging

Refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-accounting-configure#configure-nps-log-file-properties) to activate the NPS logging on the server. The logs should be written as files with the IAS (legacy) format.

#### NXLog setup on Windows
This section describes how to configure [NXLog](https://nxlog.co/) to forward your Windows events through syslog.

First of all, download NXLog at the following link : https://nxlog.co/products/all/download. Then, open the NXLog configuration file at `C:\Program Files (x86)\nxlog\conf\nxlog.conf` and update it with the following instructions:
```
 ## This is a sample configuration file. See the nxlog reference manual about the
 ## configuration options. It should be installed locally and is also available
 ## online at http://nxlog.org/nxlog-docs/en/nxlog-reference-manual.html

 ## Please set the ROOT to the folder your nxlog was installed into,
 ## otherwise it will not start.

 #define ROOT C:\Program Files\nxlog
 define ROOT C:\Program Files (x86)\nxlog
 define SYSTEMROOT C:\Windows
 define CERTDIR %ROOT%\cert

 Moduledir %ROOT%\modules
 CacheDir %ROOT%\data
 Pidfile %ROOT%\data\nxlog.pid
 SpoolDir %ROOT%\data
 LogFile %ROOT%\data\nxlog.log

<Extension _syslog>
  Module xm_syslog
</Extension>

<Input nps>
    Module    im_file
    File      '%SYSTEMROOT%\System32\LogFile\*.log'
</Input>

<Output concentrator>
  Module om_tcp
  Host CONCENTRATOR_HOST
  Port 514
  OutputType Syslog_TLS

  Exec to_syslog_ietf();
</Output>
<Route eventlog_to_concentrator>
  Path eventlog => concentrator
</Route>
```

> In the above configuration make sure to replace `CONCENTRATOR_HOST` variable by your syslog concentrator IP.

Restart the NXLog service through the Services tool as Administrator or use Powershell command line: `Restart-Service nxlog`

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

### Enjoy your events
Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.


{!_shared_content/operations_center/integrations/generated/80b8382e-0667-4469-bbc9-74be1e0ca1c1_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_80b8382e-0667-4469-bbc9-74be1e0ca1c1_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/80b8382e-0667-4469-bbc9-74be1e0ca1c1.md!}

## Further Readings
- [NXLog Community Edition Reference Manual](https://nxlog.co/docs/nxlog-ce/nxlog-reference-manual.html)
- [Microsoft NPS Installation](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-accounting-configure#configure-nps-log-file-properties)
- [Microsoft NPS logging](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-accounting-configure)
