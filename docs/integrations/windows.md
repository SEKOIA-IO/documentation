uuid: 9281438c-f7c3-4001-9bcc-45fd108ba1be
name: Windows

## Overview
Microsoft Windows is a popular operating system developed by Microsoft since 1985.

It's available in three variants:

- Windows for desktop/laptop computers, tablets and smartphones
- Windows Server for servers
- Windows PE as a lightweight version.


## Setup
This setup guide will show you how to forward events produced by a Windows system either directly to SEKOIA.IO, or through your local rsyslog server.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.
Lastly we will propose an example with sysmon tool installed.

### 1. Configure the forwarder the direct way

#### Download the certificate
In order to allow the connection of your events forwarder to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate.

In a PowerShell console run as administrator, retrieve the certificate with the following command:
```powershell
Invoke-WebRequest -Uri https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem -OutFile 'C:\Program Files (x86)\nxlog\cert\SEKOIA-IO-intake.pem'
```
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

<Output sekoia_intake>
  Module om_ssl
  Host intake.sekoia.io
  Port 10514
  CAFile %CERTDIR%\SEKOIA-IO-intake.pem
  AllowUntrusted  FALSE

  Exec to_syslog_ietf();
  Exec $raw_event = replace($raw_event, '[NXLOG@', '[SEKOIA@53288 intake_key="${YOUR_INTAKE_KEY}"][NXLOG@', 1);
  OutputType Syslog_TLS
</Output>

<Route eventlog_to_sekoia_intake>
  Path eventlog => sekoia_intake
</Route>
```

In the above `replace` function, make sure that `YOUR_INTAKE_KEY` variable was replaced by your intake key. Otherwise, please replace `YOUR_INTAKE_KEY` variable with your intake key. Also make sure that the copy/paste of the above configuation is correct, with no missing character of additional breaking line.

Restart the NXLog service through the Services tool.

### 2. Configure the forwarder through rsyslog

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
 define CERTDIR %ROOT%\cert

 Moduledir %ROOT%\modules
 CacheDir %ROOT%\data
 Pidfile %ROOT%\data\nxlog.pid
 SpoolDir %ROOT%\data
 LogFile %ROOT%\data\nxlog.log

<Extension_syslog>
  Module xm_syslog
</Extension>

<Extension_json>
  Module xm_json
</Extension>

<Input eventlog>
  # Use 'im_mseventlog' for Windows XP, 2000 and 2003
  Module im_msvistalog
  Exec $Message = to_json();
</Input>

<Output rsyslog>
  Module om_udp
  Host RSYSLOG_HOST
  Port 514

  Exec to_syslog_ietf();
</Output>
<Route eventlog_to_rsyslog>
  Path eventlog => rsyslog
</Route>
```

In the above configuration make sure to replace `RSYSLOG_HOST` variable by your rsyslog server IP.

Restart the NXLog service through the Services tool.

#### Rsyslog setup on Linux Server

##### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

##### Configure the Rsyslog server
Open or create a new windows configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/15-windows.conf
```

Paste the following rsyslog configuration to trigger the emission of windows logs by your rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOWindowsTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOWindowsTemplate template
if $programname contains 'Microsoft-Windows' then @@(o)intake.sekoia.io:10514;SEKOIAIOWindowsTemplate
```

In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key.

##### Restart rsyslog

```bash
$ sudo service rsyslog restart
```

### 3. Sysmon usage

#### Sysmon installation

Sysmon is a Microsoft tool you can download on their [website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
A common installation instruction and configuration file is available on [SwiftOnSecurity's Github](https://github.com/SwiftOnSecurity/sysmon-config).

#### NXLog setup with Sysmon

Then you need to adapt your NXLog configuration previously made.

If your are using the NXLog community edition, there's a limitation in terms of number of different eventlog entries that could be processed.
In order to monitor the common ones (Application, System, Security) and Sysmon, you could make the following changes:

```
...
<Input eventlog>
  # Use 'im_mseventlog' for Windows XP, 2000 and 2003
  Module im_msvistalog
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
</Input>
...
<Route eventlog1_to_rsyslog>
  Path eventlog1 => rsyslog
</Route>
<Route eventlog2_to_rsyslog>
  Path eventlog2 => rsyslog
</Route>
<Route eventlog3_to_rsyslog>
  Path eventlog3 => rsyslog
</Route>
<Route eventlog4_to_rsyslog>
  Path eventlog4 => rsyslog
</Route>
...
```

### 4. Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

## Further Readings
- [NXLog Community Edition Reference Manual](https://nxlog.co/docs/nxlog-ce/nxlog-reference-manual.html)
