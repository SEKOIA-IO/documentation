name: PROVE IT
type: intake

## Overview

PROVE IT by rubycat is a privileged access management solution.

## Setup

This setup guide will show you how to forward logs produced by PROVE IT to SEKOIA.IO by means of an Rsyslog transport channel.

On most GNU/Linux servers, two packages need to be installed: `rsyslog` and `rsyslog-gnutls`.

### Download the certificate

In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia/assets/files/SEKOIA-IO-intake.pem
```

### Configure the rsyslog server

Open or create a new PROVE IT configuration file for rsyslog:

```bash
sudo vim /etc/rsyslog.d/46-proveit.conf
```

Paste the following rsyslog configuration to trigger the emission of Pulse Connect Secure logs by your Rsyslog server to SEKOIA.IO:

```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOProveITTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOPulseTemplate template
if $hostname == "YOUR_PROVEIT_HOSTNAME" then @@(o)intake.sekoia.io:10514;SEKOIAIOProveITTemplate
```

In the above template instruction, change the `YOUR_PROVEIT_HOSTNAME` variable with the correct value, and please replace `YOUR_INTAKE_KEY variable` with your intake key.

### Restart Rsyslog

```bash
$ sudo service rsyslog restart
```

### Enjoy your events

Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.

## Related files

- [SEKOIA-IO-intake.pem](https://app.sekoia/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)
