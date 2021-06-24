uuid: ee54dd8e-4bd4-4fe8-9d9d-1a018cd8c4bb
name: Log Insight Windows

## Overview
Microsoft Windows is a popular operating system developed by Microsoft since 1985.

It's available in three variants:

- Windows for desktop/laptop computers, tablets and smartphones
- Windows Server for servers
- Windows PE as a lightweight version.


## Setup
This setup guide will show you how to forward events produced by a Windows system, collected by Log Insight agent and forward to SEKOIA.IO through your local rsyslog server.

### Configure the forwarder through rsyslog

#### Rsyslog setup on Linux Server 

##### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
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
sudo service rsyslog restart
```

### 3. Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.

