---
uuid: 9281438c-f7c3-4001-9bcc-45fd108ba1be
title: Windows
name: Windows
type: intake
---

## Overview
- **Vendor**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

Microsoft Windows is a widely used operating system that has been developed by Microsoft since 1985.

This page will provide you with two methods for collecting and forwarding Windows logs to Sekoia.io.

- The first method involves using the NXLog agent to send logs directly from the Windows machine to Sekoia.io.

- The second method involves using NXLog to forward logs from an internal log concentrator to Sekoia.io.

Additionally, this documentation will offer guidance on collecting and forwarding logs from sensitive assets, such as Domain Controllers, without requiring the installation of a third-party agent.

!!! Warning
    Please be advised that this documentation assumes the use of the 64-bit version of NXLog. If you are using the 32-bit version, it is crucial that you replace all references to `C:\Program Files\nxlog\` in the commands and configuration files with `C:\Program Files (x86)\nxlog\`. Failure to make this adjustment may result in errors.

!!! Warning
    Please be advised that collecting Windows events with NXLog on certain Windows languages that contain accents (such as French for "Système" keyword), are not correctly encoded by NXLog and results in an error of interpretation on our product. In such case, please consider the installation of our [agent](https://docs.sekoia.io/integration/integrations/endpoint/sekoiaio/) on the supported OS.

## Windows Event logs

On Microsoft Windows workstations and servers, most of the important hardware and software activities that are relevant for security detection and analysis, are logged into three files:

- `Application`: for Windows components such as drivers and built-in interface elements
- `System`: records events related to programs installed on a system
- `Security`: records events related to security (such as logon attempts and resource access)

Those logs a readable locally in the Windows Event Viewer, in the section Windows Logs.

If you want to improve detection and analysis, you may want to enable Sysmon.

Sysmon is a Microsoft tool you can download on their [website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
A common installation instruction and configuration file is available on [Florian Roth's Github](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml). This configuration is an updated (and maintained) version of the [SwiftOnSecurity's configuration](https://github.com/SwiftOnSecurity/sysmon-config), which can also be used.

!!! Warning
    Please be aware that installing this tool may generate additional logs, resulting in increased consumption of CPU resources. It is important to ensure that the equipment on which the tool is installed is appropriately sized and has sufficient resources to handle the additional workload.
    We recommend that you first test the installation on lower-risk assets before deploying it on more critical systems.

You will find dedicated NXLog configuration file for Sysmon usage in [this section](#nxlog-configuration-for-sysmon-usage).



## NXLog directly to Sekoia.io

This section describes how to configure [NXLog](https://nxlog.co/) to forward your Windows events by means of a syslog transport channel.

### NXLog setup

To get started with NXLog, follow these steps:

1. Download the NXLog installation package from the [official website](https://nxlog.co/products/all/download)
2. After the download is complete, proceed with the installation
3. Navigate to the NXLog configuration file, which is located at `C:\Program Files\nxlog\conf\nxlog.conf`
4. Update the configuration file with your intake key by following these instructions:

!!! Note
    Don't forget to replace `YOUR_INTAKE_KEY` variable with your actual intake key.


```
 ## This is a sample configuration file. See the nxlog reference manual about the configuration options.
 ## It should be installed locally and is also available online at http://nxlog.org/nxlog-docs/en/nxlog-reference-manual.html

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
  CAFile %CERTDIR%\Sekoia.io-intake.pem
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

To enable the connection between your events forwarder and the Sekoia.io intake, it is necessary to download the [`ISRG ROOT X1` certificate](https://letsencrypt.org/certs/isrgrootx1.pem). Please follow these steps:

1. Open a PowerShell console as an administrator.
2. Use the following command to retrieve the certificate and save it to the appropriate directory:
   ```powershell
    Invoke-WebRequest -Uri https://letsencrypt.org/certs/isrgrootx1.pem -OutFile 'C:\\Program Files\\nxlog\\cert\\isrgrootx1.pem'
    ```

3. Restart the NXLog service through the Services tool as an administrator or use the following PowerShell command line as an administrator:
    ```powershell
    Restart-Service nxlog
    ```

After completing these steps, your events forwarder should be able to establish a secure connection with the Sekoia.io intake using the newly downloaded certificate.


## NXLog to a concentrator

### Configure NXLog

This section describes how to configure [NXLog](https://nxlog.co/) to forward your Windows events by means of a syslog transport channel to a concentrator.

To get started, follow these steps:

1. Download the NXLog installation package from the [official website](https://nxlog.co/products/all/download)
2. After the download is complete, proceed with the installation
3. Navigate to the NXLog configuration file, which is located at `C:\Program Files\nxlog\conf\nxlog.conf`
4. Update the configuration file by following these instructions:

```shell
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

!!! Info
    To ensure proper configuration, it is important to replace the `RSYSLOG_HOST` variable with the IP address of your concentrator.

!!! Warning
    `OutputType Syslog_TLS` is needed for `TCP` transport even if you do not encrypt data. It does not depend on SSL transport at all.
  **Remove it ONLY** if you use `UDP` - `om_udp`.
    For more information, consult [NXLog documentation.](https://docs.nxlog.co/refman/current/xm/syslog.html)

!!! Note
    The iso8859-1 character encoding is limited to 256 characters, which is not enough to represent all French characters. This means that some French characters might not be correctly interpreted or displayed when using iso8859-1 encoding. For example, iso8859-1 does not include characters such as é, è, ê, and ë.
    In order to correctly represent these characters, it is recommended to install the [Sekoia.io agent](https://docs.sekoia.io/integration/integrations/endpoint/sekoiaio/). This endpoint agent is specifically designed to handle such issues, ensuring the accurate and secure transmission of data.

Restart the NXLog service through the Services tool as Administrator or use this Powershell command line as admin:

```powershell
Restart-Service nxlog
```

### Configure the concentrator to forward events to Sekoia.io
Please read the dedicated documentation for each concentrator:

* [Rsyslog](/integration/ingestion_methods/syslog/overview.md)
* [Logstash](/integration/ingestion_methods/logstash.md)
* [Syslog-ng](/integration/ingestion_methods/syslog-ng.md)
* [Graylog](/integration/ingestion_methods/https/graylog.md)
* [Sekoia.io docker concentrator](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md)

!!! Note
    While Sekoia.io docker concentrator is highly recommended, you are free to use the one that you are most comfortable with.

## Windows Event Forwarder to Windows Event Collector to a concentrator

Most of the following commands are to be run as Administrator in a Powershell interpreter.

### Windows Event Collector (WEC) setup
The Windows Event Collector, also known as WEC, is a Microsoft service that can be enabled and configured to aggregate logs from the Windows Event Forwarders (WEF).

** 1. Get the WEC FQDN **

Log in the Windows Event Collector and execute the following command:
```powershell
([System.Net.Dns]::GetHostByName(($env:computerName))).Hostname
```

!!! Note
    Please take note of the following information as it will be required in the upcoming section "Deploying the GPO'. Specifically, you will need to replace the `FQDN_WEC_SERVER` field with this information to complete the deployment process.

** 2. Configure the subscription file**
Get the SDDL information by executing the following command:
```
wevtutil gl security
```

!!! Note
    Take note of the `channelAccess` information.

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
!!! warning
    You have to replace Domain Computers domain group "(A;;GA;;;DC)" by "(A;;GA;;;S-1-5-....)" using information you previously collected in the        `channelAccess`.
    More information of the SDDL format can be found [here.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379567(v=vs.85).aspx)

Ensure the file is correctly saved, then close it.

** 3. Configure the Windows Remote Management**

On the WEC server, open a command interpreter as Administrator, and run the following command:
```powershell
winrm qc -q
```

** 4. Activate the "Event Collector" service**

As Administrator, enter the following command:
```powershell
wecutil qc /q
```

** 5. Activate the subscription to a zone**

As Administrator, enter the following command:

!!! Warning
    Please change the character `FILE_PATH`.

```powershell
wecutil cs "<FILE_PATH>\DC_SUBSCRIPTION.xml"
```

** 6. Display the state of the subscription to this zone**

As Administrator, enter the following command:
```powershell
wecutil gr DC_SUBSCRIPTION
```

### Windows Event Forwarder (WEF) setup

The Windows Event Forwarder, also known as WEF, is a Microsoft service that can be activated for log forwarding towards a Windows Event Collector (WEC).

#### Configure the Event Log Reader

To configure the Event Log Reader, follow the steps below:

1. Configure the collector URI(s) to specify the location where you want to send the logs. The collector URI must be a valid HTTP or HTTPS address.

2. Start the WinRM service. Open a command prompt as an Administrator and run the following command: `net start winrm`

3. Add the Network Service account to the built-in Event Log Readers security group. This will allow the Event Log Reader to access the Windows event logs.

![Sekoia.io Operations Center Windows WEF](/assets/integration/endpoint/windows/wef_client_config.png){: style="max-width:60%"}

Note that these steps are necessary to allow the Event Log Reader to access the Windows event logs.

**Configure the Windows Remote Management**

On the AD admin console, open a command interpreter as Administrator and run the following command:
```powershell
winrm qc -q
```

**Deploying the GPO**

In Computer Configuration > Administrative Templates > Windows Components > Event Forwarding -> Configure target Subscription Manager, execute the following command:

!!! warn
    Please replace the `FQDN_WEC_SERVER` by the previously collected information

```
Server=http://FQDN_WEC_SERVER:5985/wsman/SubscriptionManager/WEC,Refresh=60
```

**Apply the GPO**

On the AD admin console, open a command interpreter as Administrator and run the following command:
```powershell
gpupdate /force
```
!!! tip
    More documentation is available on the official [Microsoft documentation.](https://docs.microsoft.com/fr-fr/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection)

### Windows Event Collector to a concentrator

To ensure proper logging configuration, please follow the steps below:

1. Verify that logs are being correctly received on the Windows Event Collector (WEC) server. To do this, open the Windows Event Viewer and navigate to Windows Logs > Forwarded Events.
2. Set up the Nxlog agent to forward the logs to the concentrator by using the following configuration:

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

!!! important
    In the above configuration, make sure to replace `RSYSLOG_HOST` variable by the IP of your concentrator.

3. Restart the NXLog service through the Services tool as Administrator or use this Powershell command line as Administrator:

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
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Neo23x0/sysmon-config/master/sysmonconfig-export.xml" -OutFile "sysmonconfig-export.xml"
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


{!_shared_content/operations_center/integrations/generated/9281438c-f7c3-4001-9bcc-45fd108ba1be_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9281438c-f7c3-4001-9bcc-45fd108ba1be_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/9281438c-f7c3-4001-9bcc-45fd108ba1be.md!}

## Further Readings
- [NXLog Community Edition Reference Manual](https://nxlog.co/docs/nxlog-ce/nxlog-reference-manual.html)
