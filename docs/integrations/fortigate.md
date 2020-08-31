uuid: 5702ae4e-7d8a-455f-a47b-ef64dd87c981
name: fortigate

## Overview

The range of Fortigate firewalls is a complete appliance solution whose security functions are highly developed. FortiGate next-generation firewalls provide high performance, multilayered security and deep visibility for end-to-end protection across the enterprise network. Security services from FortiGuard Labs provide threat intelligence updates and automated mitigation. The firewalls run on the FortiOS operating system.

## Setup

This setup guide will show you how to forward your Fortigate firewall logs
to SEKOIA.IO by means of an Rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### 1. Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### 2. Configure Fortigate
The first step is to configure Fortigate to log the awaited traffic.
You can configure FortiOS to send log messages to remote syslog servers in standard, CSV or CEF (Common Event Format) format. These three formats are accepted by the SEKOIA.IO intake.
To enable syslog, log into the CLI and enter the following commands:

```bash
config log syslogd setting
set status enable
set port 514
set server [IP address of syslog server]
set facility user
end
```

Most FortiGate features are enabled for logging by default, but you can make sure the Traffic, Web and URL Filtering features are enabled for logging with the following commands:

```bash
config log syslogd filter
set traffic enable
set web enable
set url-filter enable
end
```

With some Fortigate appliance it may not be possible to do the above configuration through the command line. An alternative method is to use the graphical interface and go to the `Log Settings` menu. From there you can choose every logging options within `Event Logging` and `Local Traffic Log` except for the `Denied` options.

Then in order to use CEF format, use the following commands :

```bash
config log syslogd setting
set format cef
end
```

### 3. Configure the Rsyslog server
You can configure your Rsyslog server to forward your fortigate logs to SEKOIA.IO.

Open or create a new Fortigate configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/12-fortigate.conf
```

Then paste the following configuration:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOFortigateTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] CEF:%msg%\n")

# Send your Fortigate events to SEKOIA.IO intake servers under SEKOIAIOFortigateTemplate template
if $hostname == "YOUR_FORTIGATE_HOSTNAME" then @@(o)intake.sekoia.io:10514;SEKOIAIOFortigateTemplate
```

In the above `template` instruction, change the `YOUR_FORTIGATE_HOSTNAME` variable with the correct value, and please replace `YOUR_INTAKE_KEY` variable with your intake key.

### 4. Restart rsyslog

```bash
$ sudo service rsyslog restart
```

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

### 5. Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
