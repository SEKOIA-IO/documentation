uuid: 63974ce1-2f0a-44f7-a4cf-3e64787c1c39
name: Microsoft IIS
type: intake

## Overview
- **Vendor**: Microsoft
- **Supported environment**: On Premise
- **Version compatibility**: 10.0 and newer
- **Detection based on**: Telemetry
- **Supported application or feature**: Application Logs
Microsoft Internet Information Services (IIS) is a web server software for Windows, providing a secure and scalable platform for hosting and managing websites, applications, and services, widely used in enterprise environments.



## Configuration

This setup guide will show you how to forward your Microsoft IIS logs to Sekoia.io by means of a syslog transport channel.

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Microsoft IIS`.
2. Copy the associated Intake key

### Activate log in Microsoft IIS

Launch the `Internet Information Services (IIS) Manager`

In the `Connections` panel, select the server then the desired site and go to the `Logging` section.

![screenshot11.png](/assets/integration/application/microsoft-iis/screenshot11.png)

Select the format `IIS` and the encoding `UTF-8` for the logs.

![screenshot12.png](/assets/integration/application/microsoft-iis/screenshot12.png)

### NXLog directly to [Sekoia.io](http://sekoia.io/)

This section describes how to configure [NXLog](https://nxlog.co/) to forward your Windows events by means of a syslog transport channel.

#### NXLog setup

To get started with NXLog, follow these steps:

1. Download the NXLog installation package from the [official website](https://nxlog.co/products/all/download)
2. After the download is complete, proceed with the installation
3. Navigate to the NXLog configuration file, which is located at `C:\\Program Files\\nxlog\\conf\\nxlog.conf`
4. Update the configuration file with your intake key by following these instructions:

!!! Note
    Don't forget to replace `YOUR_INTAKE_KEY` variable with your actual intake key.

```
 ## This is a sample configuration file. See the nxlog reference manual about the configuration options.
 ## It should be installed locally and is also available online at <http://nxlog.org/nxlog-docs/en/nxlog-reference-manual.html>

 ## Please set the ROOT to the folder your nxlog was installed into,
 ## otherwise it will not start.

 #define ROOT C:\\Program Files (x86)\\nxlog
 define ROOT C:\\Program Files\\nxlog
 define CERTDIR %ROOT%\\cert

 Moduledir %ROOT%\\modules
 CacheDir %ROOT%\\data
 Pidfile %ROOT%\\data\\nxlog.pid
 SpoolDir %ROOT%\\data
 LogFile %ROOT%\\data\\nxlog.log

<Extension _syslog>
  Module xm_syslog
</Extension>

<Input iis>
  Module im_file
  File        'C:\inetpub\logs\LogFiles\W3SVC1\u_in*.log'
  SavePos  TRUE
</Input>

<Output sekoia_output>
  Module om_ssl
  Host intake.sekoia.io
  Port 10514
  CAFile %CERTDIR%\\Sekoia.io-intake.pem
  AllowUntrusted  FALSE

  Exec to_syslog_ietf();
  Exec $raw_event = replace($raw_event, '[NXLOG@', '[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"][NXLOG@', 1);
  OutputType Syslog_TLS
</Output>

<Route iis_to_sekoia_intake>
  Path iis => sekoia_output
</Route>

```

#### Download the certificate

To enable the connection between your events forwarder and the [Sekoia.io](http://sekoia.io/) intake, it is necessary to download the [`IRG ROOT X1` certificate](https://letsencrypt.org/certs/isrgrootx1.pem). Please follow these steps:

1. Open a PowerShell console as an administrator.
2. Use the following command to retrieve the certificate and save it to the appropriate directory:
    
    ```powershell
     Invoke-WebRequest -Uri https://letsencrypt.org/certs/isrgrootx1.pem -OutFile 'C:\\Program Files\\nxlog\\cert\\isgrootx1.pem'
    ```
    
3. Restart the NXLog service through the Services tool as an administrator or use the following PowerShell command line as an administrator:
    
    ```powershell
    Restart-Service nxlog
    
    ```
    

After completing these steps, your events forwarder should be able to establish a secure connection with the [Sekoia.io](http://sekoia.io/) intake using the newly downloaded certificate.

### NXLog to a concentrator

#### Configure NXLog

This section describes how to configure [NXLog](https://nxlog.co/) to forward your Windows events by means of a syslog transport channel to a concentrator.

To get started, follow these steps:

1. Download the NXLog installation package from the [official website](https://nxlog.co/products/all/download)
2. After the download is complete, proceed with the installation
3. Navigate to the NXLog configuration file, which is located at `C:\\Program Files\\nxlog\\conf\\nxlog.conf`
4. Update the configuration file by following these instructions:

```
 ## This is a sample configuration file. See the nxlog reference manual about the
 ## configuration options. It should be installed locally and is also available
 ## online at <http://nxlog.org/nxlog-docs/en/nxlog-reference-manual.html>

 ## Please set the ROOT to the folder your nxlog was installed into,
 ## otherwise it will not start.

 #define ROOT C:\\Program Files\\nxlog
 define ROOT C:\\Program Files (x86)\\nxlog
 define CERTDIR %ROOT%\\cert

 Moduledir %ROOT%\\modules
 CacheDir %ROOT%\\data
 Pidfile %ROOT%\\data\\nxlog.pid
 SpoolDir %ROOT%\\data
 LogFile %ROOT%\\data\\nxlog.log

<Extension _syslog>
  Module xm_syslog
</Extension>

<Input iis>
  Module im_file
  File        'C:\inetpub\logs\LogFiles\W3SVC1\u_in*.log'
  SavePos  TRUE
</Input>

<Output rsyslog>
  Module om_tcp
  Host RSYSLOG_HOST
  Port 514
  OutputType Syslog_TLS

  Exec to_syslog_ietf();
</Output>
<Route iis_to_rsyslog>
  Path iis => rsyslog
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

#### Configure the concentrator to forward events to [Sekoia.io](http://sekoia.io/)

Please read the dedicated documentation for each concentrator:

- [Rsyslog](https://www.notion.so/ingestion_methods/syslog/overview/)
- [Logstash](https://www.notion.so/ingestion_methods/logstash/)
- [Syslog-ng](https://www.notion.so/ingestion_methods/syslog-ng/)
- [Graylog](https://www.notion.so/ingestion_methods/graylog/)
- [Sekoia.io docker concentrator](https://www.notion.so/ingestion_methods/sekoiaio_forwarder/)

!!! Note
    While [Sekoia.io](http://sekoia.io/) docker concentrator is highly recommended, you are free to use the one that you are most comfortable with.
{!_shared_content/operations_center/integrations/generated/63974ce1-2f0a-44f7-a4cf-3e64787c1c39_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_63974ce1-2f0a-44f7-a4cf-3e64787c1c39_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/63974ce1-2f0a-44f7-a4cf-3e64787c1c39.md!}

