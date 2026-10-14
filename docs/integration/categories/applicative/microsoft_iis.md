---
uuid: 63974ce1-2f0a-44f7-a4cf-3e64787c1c39
name: Microsoft IIS
type: intake
---

## Overview

- **Vendor**: Microsoft
- **Supported environment**: On-premises
- **Version compatibility**: 10.0 and newer
- **Detection based on**: Telemetry
- **Supported application or feature**: Application Logs

Microsoft Internet Information Services (IIS) is a web server software for Windows that provides a secure and scalable platform for hosting and managing websites, applications, and services.

## Configuration

This guide explains how to forward Microsoft IIS logs to Sekoia.io using NXLog and a syslog transport channel.

!!! warning

    To avoid time offset issues when events are parsed by Sekoia.io, configure your server timezone to **UTC**.

    For more information, see the [Sekoia.io timezone requirements](https://docs.sekoia.com/xdr/FAQ/datetime/) documentation.

### Create an intake

1. Go to the [Intakes](https://app.sekoia.io/operations/intakes) page and create a new intake using the **Microsoft IIS** format.

2. Copy the associated intake key. You will use it in the NXLog configuration.

### Activate logging in Microsoft IIS

1. Open the **Internet Information Services (IIS) Manager**.

2. In the **Connections** panel, select the server, then the required website.

3. Open the **Logging** section.

![IIS logging configuration](/assets/integration/application/microsoft-iis/screenshot11.png)

4. Select the **IIS** log format and set the encoding to **UTF-8**.

![IIS log format and encoding](/assets/integration/application/microsoft-iis/screenshot12.png)

## Forward logs with NXLog

NXLog can forward IIS logs directly to Sekoia.io or to an intermediate syslog service, such as the Sekoia.io Forwarder.

### NXLog directly to Sekoia.io

This section explains how to configure NXLog to forward IIS logs directly to a Sekoia.io intake over TLS.

### Install NXLog

1. Download the NXLog installation package from the [official NXLog website](https://nxlog.co/products/all/download).

2. Install NXLog.

3. Open the NXLog configuration file:

    ```text
    C:\Program Files\nxlog\conf\nxlog.conf
    ```

4. Update the configuration file with your intake key.

!!! note

    Replace `YOUR_INTAKE_KEY` with the intake key created for Microsoft IIS.

```text
## This is a sample configuration file.
## See the NXLog reference manual for information about the configuration options.

## Set ROOT to the directory where NXLog is installed.
## Otherwise, NXLog may not start.

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

<Input iis>
    Module im_file
    File 'C:\inetpub\logs\LogFiles\W3SVC1\u_in\*.log'
    SavePos TRUE
</Input>

<Output sekoia_output>
    Module om_ssl
    Host intake.sekoia.io
    Port 10514
    CAFile %CERTDIR%\isrgrootx1.pem
    AllowUntrusted FALSE

    Exec to_syslog_ietf();
    Exec $raw_event = replace(
        $raw_event,
        '[NXLOG@',
        '[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"][NXLOG@',
        1
    );

    OutputType Syslog_TLS
</Output>

<Route iis_to_sekoia_intake>
    Path iis => sekoia_output
</Route>
```

### Download the certificate

To establish a secure connection with the Sekoia.io intake, download the **ISRG Root X1** certificate and save it in the directory configured by `CERTDIR`.

1. Open PowerShell as an administrator.

2. Download the certificate:

```powershell
Invoke-WebRequest `
    -Uri https://letsencrypt.org/certs/isrgrootx1.pem `
    -OutFile 'C:\Program Files\nxlog\cert\isrgrootx1.pem'
```

3. Restart the NXLog service:

```powershell
Restart-Service nxlog
```

After restarting NXLog, the service can establish a secure connection with the Sekoia.io intake using the downloaded certificate.

## Forward logs through a syslog service

Use this configuration when NXLog sends IIS logs to an intermediate syslog service, such as the [Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md).

### Configure NXLog

1. Download the NXLog installation package from the [official NXLog website](https://nxlog.co/products/all/download).

2. Install NXLog.

3. Open the NXLog configuration file:

    ```text
    C:\Program Files\nxlog\conf\nxlog.conf
    ```

4. Update the configuration file with the hostname or IP address of your syslog service.

```text
## This is a sample configuration file.
## See the NXLog reference manual for information about the configuration options.

## Set ROOT to the directory where NXLog is installed.
## Otherwise, NXLog may not start.

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

<Input iis>
    Module im_file
    File 'C:\inetpub\logs\LogFiles\W3SVC1\u_in\*.log'
    SavePos TRUE
</Input>

<Output syslog_service>
    Module om_tcp
    Host SYSLOG_SERVICE_HOST
    Port 514
    OutputType Syslog_TLS

    Exec to_syslog_ietf();
</Output>

<Route iis_to_syslog_service>
    Path iis => syslog_service
</Route>
```

!!! info

    Replace `SYSLOG_SERVICE_HOST` with the hostname or IP address of your syslog service.

!!! warning

    Keep `OutputType Syslog_TLS` when using the TCP configuration shown above. Remove it only if you change the output module to UDP with `om_udp`.

For more information, see the [NXLog syslog documentation](https://docs.nxlog.co/refman/current/xm/syslog.html).

!!! note

    The `iso8859-1` character encoding supports only 256 characters. It does not include some French characters, such as `é`, `è`, `ê`, and `ë`.

    To process these characters correctly, use the [Sekoia.io agent](https://docs.sekoia.com/integration/integrations/endpoint/sekoiaio/), which is designed to provide secure and accurate endpoint event collection.

5. Restart the NXLog service:

```powershell
Restart-Service nxlog
```

### Configure the syslog service to forward events to Sekoia.io

Use the [Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) to collect syslog events from NXLog and forward them to the corresponding Sekoia.io intake.

The Forwarder maps each listening port to an intake key. Configure a dedicated listening port for the Microsoft IIS intake.

For third-party syslog services, see [Third-party syslog services](/integration/ingestion_methods/syslog/syslog_service.md).

!!! note

    The Sekoia.io Forwarder is the recommended option for this setup. You can also use another syslog service if you prefer to manage and maintain your own forwarding infrastructure.

{!_shared_content/operations_center/integrations/generated/63974ce1-2f0a-44f7-a4cf-3e64787c1c39_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_63974ce1-2f0a-44f7-a4cf-3e64787c1c39_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/63974ce1-2f0a-44f7-a4cf-3e64787c1c39.md!}

