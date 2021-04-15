uuid: 6c2a44e3-a86a-4d98-97a6-d575ffcb29f7
name: Apache

## Overview
The Apache HTTP Server, colloquially called Apache, is free and open-source cross-platform web server software, released under the terms of Apache License 2.0. Apache is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.

## Setup
This setup guide will show you how to forward both your access and error logs to SEKOIA.IO by means of an rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure the Rsyslog server
We can configure rsyslog to parse the `access_log` and `error_log` and report its entries to SEKOIA.IO.

Open or create a new Apache configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/45-apache.conf
```

At the beginning of the configuration file,  paste the following instruction to order the rsyslog server to load the module `imfile`:
```bash
$ModLoad imfile
```

Then paste the following configuration to leverage this module to monitor apache httpd access and error output files (please note that the path to the log file may change depending on the OS and your configuration):
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# error log
$InputFileName /var/log/apache2/error.log
$InputFileTag apache:
$InputFileStateFile stat-apache-error
$InputFileSeverity error
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# access log
$InputFileName /var/log/apache2/access.log
$InputFileTag apache:
$InputFileStateFile stat-apache-access
$InputFileSeverity notice
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOApacheTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOApacheTemplate template
if $programname startswith 'apache' then @@(o)intake.sekoia.io:10514;SEKOIAIOApacheTemplate
```

In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key.

### Restart rsyslog

```bash
$ sudo service rsyslog restart
```

### Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

## Further Reading
- [Apache documentation](http://httpd.apache.org/docs/)
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)
