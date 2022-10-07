uuid: 80b8382e-0667-4469-bbc9-74be1e0ca1c1
name: Microsoft Always On VPN
type: intake

## Overview
Microsoft Always On VPN is a Windows 10 feature enabling secure connection to protected networks.

This guide will explain how to forward Network Policy Server (NPS) logs to SEKOIA.IO

{!_shared_content/operations_center/detection/generated/suggested_rules_80b8382e-0667-4469-bbc9-74be1e0ca1c1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/microsoft-always-on-vpn_do_not_edit_manually.md!}

## Configure

### NXLog agent to the Rsyslog

#### Configuring NPS logging

Refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-accounting-configure#configure-nps-log-file-properties) to activate the NPS logging on the server. The logs should be write in files with the IAS (legacy) format.

#### NXLog setup on Windows
This section describes how to configure [NXLog](https://nxlog.co/) to forward your Windows events by means of a syslog transport channel.

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

<Output rsyslog>
  Module om_tcp
  Host RSYSLOG_HOST
  Port 514
  OutputType Syslog_TLS

  Exec to_syslog_ietf();
</Output>
<Route eventlog_to_rsyslog>
  Path eventlog => rsyslog
</Route>
```

> In the above configuration make sure to replace `RSYSLOG_HOST` variable by your Rsyslog server IP.

Restart the NXLog service through the Services tool as Administrator or use Powershell command line: `Restart-Service nxlog`

### Configure the Rsyslog to forward to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

### Enjoy your events
Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.

## Further Readings
- [NXLog Community Edition Reference Manual](https://nxlog.co/docs/nxlog-ce/nxlog-reference-manual.html)
- [Microsoft NPS Installation](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-accounting-configure#configure-nps-log-file-properties)
- [Microsoft NPS logging](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-accounting-configure)
