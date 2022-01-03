uuid: 44d41a2b-96cb-4d37-84e0-4f0c0f9138b8
name: Alsid

## Overview
Alsid is an automated security solution that monitors the components of Active Directory infrastructures by detecting attacks in real time, identifying existing weaknesses and vulnerabilities.

## Setup
This setup guide will show you how to forward logs produced by Alsid to SEKOIA.IO by means of a rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure the Rsyslog server
Open or create a new Alsid configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/58-alsid.conf
```

Paste the following rsyslog configuration to trigger the emission of Alsid logs by your rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOAlsidTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOAlsidTemplate template
if $hostname == "YOUR_ALSID_HOSTNAME" then @@(o)intake.sekoia.io:10514;SEKOIAIOAlsidTemplate
```

In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key.


### Restart rsyslog

```bash
$ sudo service rsyslog restart
```

### Enjoy your events
Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.


## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)
