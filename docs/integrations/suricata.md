uuid: 331fa58d-8cf9-454a-a87f-48a3dc07d4d3
name: Suricata

## Overview
Suricata is a free and open source, mature, fast and robust network threat detection engine. Suricata inspects the network traffic using a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats.

## Setup
Suricata leverages its EVE output module to report alerts, metadata, file info and protocol records in JSON. As described in the official documentation, this module can report its findings through the syslog facility.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure Suricata to forward events to rsyslog
Open the Suricata configuration file (please note that the path to the configuration file may change depending on the OS and your configuration):
```bash
sudo vim /etc/suricata/suricata.yaml
```

Paste the following declaration in your suricata configuration to trigger the production of syslog entries under the `local5` facility:
```
outputs:
  - eve-log:
      enabled: yes
      type:syslog
      identity: suricata
      facility: local5
      level: Info
      types:
        - alert
        - http
        - dns
        - tls
```

### Configure the Rsyslog server
Given this Suricata configuration, your local rsyslog server will handle produced records. To report these to SEKOIA.IO, open or create a new suricata configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/11-suricata.conf
```

Then paste the following rsyslog configuration:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOSuricataTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your Suricata events to SEKOIA.IO intake servers under SEKOIAIOSuricataTemplate template
if $app-name == 'suricata' then @@(o)intake.sekoia.io:10514;SEKOIAIOSuricataTemplate
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


## Further Readings
- [Suricata User Guide](https://suricata.readthedocs.io/)
