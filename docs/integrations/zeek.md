uuid: 428035c0-a251-4664-8e58-fed15f4e442c
name: Zeek

## Overview
Zeek is a free and open-source software network analysis framework; it was originally developed in 1994 by Vern Paxson and was named in reference to George Orwell's Big Brother from his novel Nineteen Eighty-Four. It can be used as a network intrusion detection system (NIDS) but with additional live analysis of network events.It is released under the BSD license.

## Setup
This setup guide will show you how to forward dns, http and conn logs to SEKOIA.IO by means of an rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure the Rsyslog server
We can configure rsyslog to parse the `conn.log` `http.log` and `dns.log` and report its entries to SEKOIA.IO.

Open or create a new Zeek configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/66-zeek.conf
```

At the beginning of the configuration file,  paste the following instruction to order the rsyslog server to load the module `imfile`:
```bash
$ModLoad imfile
```

Then paste the following configuration to leverage this module to monitor  zeek log files (please note that the path to the log file may change depending on the OS and your configuration):
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# conn log
$InputFileName /var/log/zeek/conn.log
$InputFileTag zeek:
$InputFileStateFile stat-zeek-conn
$InputFileSeverity notice
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# http log
$InputFileName /var/log/zeek/http.log
$InputFileTag zeek:
$InputFileStateFile stat-zeek-http
$InputFileSeverity notice
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# dns log
$InputFileName /var/log/zeek/dns.log
$InputFileTag zeek:
$InputFileStateFile stat-zeek-dns
$InputFileSeverity notice
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOZeekTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOZeekTemplate template
if $programname startswith 'zeek' then @@(o)intake.sekoia.io:10514;SEKOIAIOZeekTemplate
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
- [Zeek documentation](https://docs.zeek.org/en/stable/index.html)
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)
