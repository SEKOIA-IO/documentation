uuid: 9281438c-f7c3-4001-9bcc-45fd108ba1be
name: Windows
type: intake

## Overview
Microsoft Windows is a popular operating system developed by Microsoft since 1985.

In this documentation we will explain 2 ways to collect and send Windows logs to SEKOIA.IO.

- From the Windows machine directly to SEKOIA.IO using the NXLog agent
- From the Windows machine using NXLog to an internal log concentrator, then forwarded to SEKOIA.IO

In addition, this documentation will explain how to collect and send Windows logs from sensitive assets such as Domain Controllers, if you don't want to install a third party agent.

!!!Warning
    Be careful, in this documentation 64 bits version of NXLog is used.
    If you use the 32 bits version, be sure to replace all the commands and configuration files containing `C:\Program Files\nxlog\` with `C:\Program Files (x86)\nxlog\`

## Windows Event logs

On Microsoft Windows workstations and servers, most of the important hardward and software activities that are relevant for security detection and analysis, are logged into three files.

- Application: for Windows components such as drivers and built-in interface elements
- System: records the events related to programs installed on a system
- Security: records the events related to security, such as logon attempts and ressource access

Those logs a readable locally in the Windows Event Viewer, in the section Windows Logs.

If you want to improve detection and analysis, you may want to enable Sysmon.

Sysmon is a Microsoft tool you can download on their [website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
A common installation instruction and configuration file is available on [Florian Roth's Github](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml). This configuration is an updated (and maintained) version of the [SwiftOnSecurity's configuration](https://github.com/SwiftOnSecurity/sysmon-config), which can also be used.

!!!Warning
    The installation of this tool will generate more logs, so it will consume more CPU ressources. Install it on equipements that are correctly dimensioned, or try it on low risk assets at first.

You will find dedicated NXLog configuration file for Sysmon usage in [this section](#nxlog-configuration-for-sysmon-usage).

{!_shared_content/operations_center/detection/generated/suggested_rules_9281438c-f7c3-4001-9bcc-45fd108ba1be_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/windows_do_not_edit_manually.md!}

## NXLog directly to SEKOIA.IO
This section describes how to configure [NXLog](https://nxlog.co/) to forward your Windows events by means of a syslog transport channel.

### NXLog setup
First of all, download NXLog at the following link : https://nxlog.co/products/all/download. Install it, then, open the NXLog configuration file at `C:\Program Files\nxlog\conf\nxlog.conf` and update it with the following instructions:
> In the this template instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key.
```
 ## This is a sample configuration file. See the nxlog reference manual about the
 ## configuration options. It should be installed locally and is also available
 ## online at http://nxlog.org/nxlog-docs/en/nxlog-reference-manual.html

 ## Please set the ROOT to the folder your nxlog was installed into,
 ## otherwise it will not start.

 #define ROOT C:\Program Files (x86)\nxlog
 define ROOT C:\Program Files\nxlog
 define CERTDIR %ROOT%\cert

 Moduledir %ROOT%\modules
 CacheDir %ROOT%\data
 Pidfile %ROOT%\data\nxlog.pid
 SpoolDir %ROOT%\data
 LogFile %ROOT%\data\nxlog.log

<Extension _syslog>
  Module xm_syslog
</Extension>

<Extension _json>
  Module xm_json
</Extension>

<Input eventlog>
  # Use 'im_mseventlog' for Windows XP, 2000 and 2003
  Module im_msvistalog
  Exec $Message = to_json();
</Input>

<Output sekoia_output>
  Module om_ssl
  Host intake.sekoia.io
  Port 10514
  CAFile %CERTDIR%\SEKOIA-IO-intake.pem
  AllowUntrusted  FALSE

  Exec to_syslog_ietf();
  Exec $raw_event = replace($raw_event, '[NXLOG@', '[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"][NXLOG@', 1);
  OutputType Syslog_TLS
</Output>

<Route eventlog_to_sekoia_intake>
  Path eventlog => sekoia_output
</Route>
```

### Download the certificate
In order to allow the connection of your events forwarder to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate.

In a PowerShell console run as administrator, retrieve the certificate with the following command:
```powershell
Invoke-WebRequest -Uri https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem -OutFile 'C:\Program Files\nxlog\cert\SEKOIA-IO-intake.pem'
```

Restart the NXLog service through the Services tool as Administrator or use this PowerShell command line as Administrator:

```powershell
Restart-Service nxlog
```

## NXLog to a concentrator

### Configure NXLog

This section describes how to configure [NXLog](https://nxlog.co/) to forward your Windows events by means of a syslog transport channel to a concentrator.

First of all, download NXLog at the following link : https://nxlog.co/products/all/download. Then, open the NXLog configuration file at `C:\Program Files (x86)\nxlog\conf\nxlog.conf` and update it with the following instructions:
```
 ## This is a sample configuration file. See the nxlog reference manual about the
 ## configuration options. It should be installed locally and is also available
 ## online at http://nxlog.org/nxlog-docs/en/nxlog-reference-manual.html

 ## Please set the ROOT to the folder your nxlog was installed into,
 ## otherwise it will not start.

 #define ROOT C:\Program Files\nxlog
 define ROOT C:\Program Files (x86)\nxlog
 define CERTDIR %ROOT%\cert

 Moduledir %ROOT%\modules
 CacheDir %ROOT%\data
 Pidfile %ROOT%\data\nxlog.pid
 SpoolDir %ROOT%\data
 LogFile %ROOT%\data\nxlog.log

<Extension _syslog>
  Module xm_syslog
</Extension>

<Extension _json>
  Module xm_json
</Extension>

<Input eventlog>
  # Use 'im_mseventlog' for Windows XP, 2000 and 2003
  Module im_msvistalog
  Exec $Message = to_json();
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

!!!important
    In the above configuration make sure to replace `RSYSLOG_HOST` variable by the IP of your concentrator.

!!!warning
    `OutputType Syslog_TLS` is needed for `TCP` transport even if you do not encrypt data. **It does not depend on SSL transport at all**.

    **Remove it ONLY** if you use `UDP` - `om_udp`. For more information, consult [NXLog documentation](https://docs.nxlog.co/refman/current/xm/syslog.html)

Restart the NXLog service through the Services tool as Administrator or use this Powershell command line as admin:

```powershell
Restart-Service nxlog
```

### Configure the concentrator to forward events to SEKOIA.IO
Please consult the dedicated documentation for each concentrator :

* [Rsyslog](../../../ingestion_methods/rsyslog/)
* [Logstash](../../../ingestion_methods/logstash/)
* [Syslog-ng](../../../ingestion_methods/syslog-ng/)
* [Graylog](../../../ingestion_methods/graylog/)

!!!Note
    Rsyslog is now recommanded because it is on this concentrator that SEKOIA has the best expertise.
    However, feel free to use the one you are the most confortable with.

## Windows Event Forwarder to Windows Event Collector to a concentrator
Most of the following commands are to be run as Administrator in a Powershell interpretor.

### Windows Event Collector (WEC) setup
The Windows Event Collector, also known as WEC is a Microsoft service that can be activate and configured to aggregate logs from the Windows Event Forwarders (WEF).

#### Get the WEC FQDN
Log in the Windows Event Collector, and execute the following command:
```powershell
([System.Net.Dns]::GetHostByName(($env:computerName))).Hostname
```
> Note it, you will need it on the section WEF: "Deploying the GPO" for `FQDN_WEC_SERVER` field to replace

#### Configure the subscription file
Get the SDDL information by executing the following command:
```
wevtutil gl security
```
> Note the `channelAccess` information.

On the WEC server, create an XML file, named `DC_SUBSCRIPTION.xml` with the following information:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Subscription xmlns="http://schemas.microsoft.com/2006/03/windows/events/subscription">
    <!-- Name of subscription -->
    <SubscriptionId>DC_SUBSCRIPTION</SubscriptionId>
    <!-- Push mode (DC to WEC) -->
    <SubscriptionType>SourceInitiated</SubscriptionType>
    <Description>Source Initiated Subscription from DC_SUBSCRIPTION</Description>
    <!-- Subscription is active -->
    <Enabled>true</Enabled>
    <Uri>http://schemas.microsoft.com/wbem/wsman/1/windows/EventLog</Uri>
    <!-- This mode ensures that events are delivered with minimal delay -->
    <!-- It is an appropriate choice if you are collecting alerts or critical events -->
    <!-- It uses push delivery mode and sets a batch timeout of 30 seconds -->
    <ConfigurationMode>MinLatency</ConfigurationMode>
    <!-- Event log to retrieved -->
    <Query>
        <![CDATA[
            <QueryList>
                <Query Id="0">
                    <Select Path="Application">*</Select>
                    <Select Path="Security">*</Select>
                    <Select Path="System">*</Select>
                </Query>
            </QueryList>
        ]]>
    </Query>
    <!-- Collect events generated since the subscription (not oldest) -->
    <ReadExistingEvents>false</ReadExistingEvents>
    <!-- Protocol and port used (DC to WEC) -->
    <TransportName>http</TransportName>
    <!-- Mandatory value (https://www-01.ibm.com/support/docview.wss?crawler=1&uid=swg1IV71375) -->
    <ContentFormat>RenderedText</ContentFormat>
    <Locale Language="en-US"/>
    <!-- Target Event log on WEC -->
    <LogFile>ForwardedEvents</LogFile>
    <!-- Define which domain computers are allowed or not to initiate subscriptions -->
    <!-- This exemple grants members of the Domain Computers domain group, as well as the local Network Service group (for local forwarder) -->
    <AllowedSourceDomainComputers>O:NSG:NSD:(A;;GA;;;DC)(A;;GA;;;NS)</AllowedSourceDomainComputers>
</Subscription>
```
> Warning: replace Domain Computers domain group "(A;;GA;;;DC)" by "(A;;GA;;;S-1-5-....)" previously collected in the `channelAccess`
> More information of the SDDL format (https://msdn.microsoft.com/en-us/library/windows/desktop/aa379567(v=vs.85).aspx)

Ensure the file is correctly saved, then close it.

#### Configure the Windows Remote Management
On the WEC server, open a command interpretor as Administrator, and run the following command:
```powershell
winrm qc -q
```

#### Activate the "Event Collector" service
As Administrator, enter the following command:
```powershell
wecutil qc /q
```

#### Activate the subscription to a zone
As Administrator, enter the following command:
> Warning: please change the character `FILE_PATH`
```powershell
wecutil cs "<FILE_PATH>\DC_SUBSCRIPTION.xml"
```

#### Display the state of the subscription to this zone
As Administrator, enter the following command:
```powershell
wecutil gr DC_SUBSCRIPTION
```

### Windows Event Forwarder (WEF) setup
The Windows Event Forwarder, also known as WEF is a Microsoft service that can be activated for log forwarding towards a Windows Event Collector (WEC).

#### Configure the Event Log Reader
- Configure the collector URI(s).
- Start the WinRM service (run as Administrator)
- Add the Network Service account to the built-in Event Log Readers security group. As show hereafter:

![SEKOIA.IO Operations Center Windows WEF](/assets/operation_center/integration_catalog/endpoint/windows/wef_client_config.png){: style="max-width:60%"}

#### Configure the Windows Remote Management
On the AD admin console, open a command interpretor as Administrator, and run the following command:
```powershell
winrm qc -q
```

#### Deploying the GPO
In Computer Configuration > Administrative Templates > Windows Components > Event Forwarding -> Configure target Subscription Manager, execute the following command:
> Warning: Please replace the `FQDN_WEC_SERVER` by the previously collected information
```
Server=http://FQDN_WEC_SERVER:5985/wsman/SubscriptionManager/WEC,Refresh=60
```

#### Apply the GPO
On the AD admin console, open a command interpretor as Administrator, and run the following command:
```powershell
gpupdate /force
```

- More documentation available here on [Microsoft documentation](https://docs.microsoft.com/fr-fr/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection)

### Windows Event Collector to a concentrator

- Ensure the logs are correctly reveived on the WEC server, using the Windows Event Viewer and selecting Windows Logs > Forwarded Events
- Setup the Nxlog agent to forward the logs to the concentrator by using this configuration :

```
define ROOT C:\Program Files (x86)\nxlog

Moduledir %ROOT%\modules
CacheDir %ROOT%\data
Pidfile %ROOT%\data\nxlog.pid
SpoolDir %ROOT%\data
LogFile %ROOT%\data\nxlog.log

<Extension _syslog>
  Module xm_syslog
</Extension>

<Extension _json>
  Module xm_json
</Extension>

<Input eventlog1>
  Module im_msvistalog
  Query <QueryList><Query Id="0"><Select Path="Application">*</Select></Query></QueryList>
  Exec $Message = to_json();
</Input>
<Input eventlog2>
  Module im_msvistalog
  Query <QueryList><Query Id="0"><Select Path="System">*</Select></Query></QueryList>
  Exec $Message = to_json();
</Input>
<Input eventlog3>
  Module im_msvistalog
  Query <QueryList><Query Id="0"><Select Path="Security">*</Select></Query></QueryList>
  Exec $Message = to_json();
</Input>
<Input eventlog4>
  Module im_msvistalog
  Query <QueryList><Query Id="0"><Select Path="ForwardedEvents">*</Select></Query></QueryList>
  Exec $Message = to_json();
</Input>

<Output rsyslog>
  Module om_tcp
  Host RSYSLOG_HOST
  Port 514
  OutputType Syslog_TLS

  Exec to_syslog_ietf();
</Output>

<Route eventlog_to_rsyslog>
  Path eventlog1, eventlog2, eventlog3, eventlog4 => rsyslog
</Route>
```

!!!important
    In the above configuration make sure to replace `RSYSLOG_HOST` variable by the IP of your concentrator.

Restart the NXLog service through the Services tool as Administrator or use this Powershell command line as Administrator:
```poweshell
Restart-Service nxlog
```

## Sysmon usage
Sysmon is a Microsoft tool you can download on their [website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
A common installation instruction and configuration file is available on [Florian Roth's Github](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml). This configuration is an updated (and maintained) version of the [SwiftOnSecurity's configuration](https://github.com/SwiftOnSecurity/sysmon-config), which can also be used.

### Install Sysmon

1. Download and extract Sysmon from the official the [website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon). With powershell:
```powershell
Invoke-WebRequest -Uri "https://download.sysinternals.com/files/Sysmon.zip" -OutFile "Sysmon.zip"
Expand-Archive -Path Sysmon.zip -DestinationPath Sysmon
```

2. Download the configuration you want to use, for instance from [Florian Roth's Github](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml). With Powershell:
```powershell
cd .\Sysmon\
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Neo23x0/sysmon-config/master/sysmonconfig-export.xml" -OutFile "sysmonconfig-export.xml" -OutFile "sysmonconfig-export.xml"
```

3. Install Sysmon
```powershell
.\Sysmon64.exe -accepteula -i sysmonconfig-export.xml
```

### NXLog configuration for Sysmon usage

If you are using the NXLog community edition, there is a limitation in terms of number of different eventlog entries that could be processed.
In order to monitor Sysmon and the common ones (Application, System, Security), make the following changes in `C:\Program Files\nxlog\conf\nxlog.conf`:

```
...
<Input eventlog1>
  Module im_msvistalog
  Query <QueryList><Query Id="0"><Select Path="Application">*</Select></Query></QueryList>
  Exec $Message = to_json();
</Input>
<Input eventlog2>
  Module im_msvistalog
  Query <QueryList><Query Id="0"><Select Path="System">*</Select></Query></QueryList>
  Exec $Message = to_json();
</Input>
<Input eventlog3>
  Module im_msvistalog
  Query <QueryList><Query Id="0"><Select Path="Security">*</Select></Query></QueryList>
  Exec $Message = to_json();
</Input>
<Input eventlog4>
  Module im_msvistalog
  Query <QueryList><Query Id="0"><Select Path="Microsoft-Windows-Sysmon/Operational">*</Select></Query></QueryList>
  Exec $Message = to_json();
</Input>
...
<Route eventlog_to_rsyslog>
  Path eventlog1, eventlog2, eventlog3, eventlog4 => rsyslog
</Route>
...
```

Restart the NXLog service through the Services tool as Administrator or use this PowerShell command line as Administrator:

```powershell
Restart-Service nxlog
```

## Further Readings
- [NXLog Community Edition Reference Manual](https://nxlog.co/docs/nxlog-ce/nxlog-reference-manual.html)
