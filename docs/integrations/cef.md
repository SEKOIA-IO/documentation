uuid: 1d172ee6-cdc0-4713-9cfd-43f7d9595777
name: CEF

## Overview
ArcSight's Common Event Format (CEF) is an open log management standard.
If one of your applications or devices is not covered by one of the other intakes we support but can produce logs in CEF you can use this intake.

Still we recommend using an intake tailored to your specific application or device, even with CEF, in order to ensure you get the most out of your logs. If an intake is missing, please [contact us](mailto:support@sekoia.io).

## Setup
This setup guide will show you how to forward your CEF logs to SEKOIA.IO by means of an rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure the Rsyslog server
Open or create a new configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/xx-yyyyy.conf
```

Customize the following rsyslog configuration to trigger the emission of logs by your rsyslog server to SEKOIA.IO.

```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Collects logs out of the dedicated socket, uncomment  if needed
# $AddUnixListenSocket ...

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOCefTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOCefTemplate template
@@(o)intake.sekoia.io:10514;SEKOIAIOCefTemplate
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


## Further Reading
- [CEF specification](https://community.microfocus.com/dcvta86296/attachments/dcvta86296/connector-documentation/1197/2/CommonEventFormatV25.pdf)
