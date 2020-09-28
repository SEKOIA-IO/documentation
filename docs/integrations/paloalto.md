uuid: 903ec1b8-f206-4ba5-8563-db21da09cafd
name: Palo Alto

## Overview
Palo Alto Networks offers an enterprise cybersecurity platform which provides network security, cloud security, endpoint protection, and various cloud-delivered security services.

## Setup
This setup guide will show you how to forward logs produced by your Palo Alto firewalls to SEKOIA.IO by means of an rsyslog transport channel.

### 1. Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### 2. Configure the Rsyslog server
Open or create a new Palo Alto configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/38-paloalto.conf
```

Paste the following rsyslog configuration to trigger the emission of Palo Alto logs by your rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOPaloAltoTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOPaloAltoTemplate template
if $hostname == "YOUR_PALOALTO_HOSTNAME" then @@(o)intake.sekoia.io:10514;SEKOIAIOPaloAltoTemplate
```

In the above `template` instruction, change the `YOUR_PALOALTO_HOSTNAME` variable with the correct value, and please replace `YOUR_INTAKE_KEY` variable with your intake key.

### 3. Restart rsyslog

```bash
$ sudo service rsyslog restart
```


## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)


### 4. Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
