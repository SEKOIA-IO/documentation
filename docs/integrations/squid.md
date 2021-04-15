uuid: a0dbb8f3-ca1c-4c6b-aafa-595bd430c0cb
name: Squid

## Overview
Squid is a caching proxy for the Web supporting HTTP, HTTPS, FTP, and more. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages. Squid has extensive access controls and makes a great server accelerator.

## Setup

This setup guide will show you how to forward logs produced by your SQUID servers to SEKOIA.IO by means of an rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure Squid
We can configure SQUID to report access logs to your syslog server.

Open the squid configuration file (please note that the path to the configuration file may change depending on the OS and your configuration):
```bash
sudo vim /etc/squid/squid.conf
```
Then update the `access_log` directive like the following line:
```bash
access_log syslog:local5.info squid
```

### Configure the Rsyslog server
Open or create a new Squid configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/17-squid.conf
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
template(name="SEKOIAIOSquidTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOSquidTemplate template
if $programname contains 'squid' then @@(o)intake.sekoia.io:10514;SEKOIAIOSquidTemplate
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


## Further Readings
- [Squid Wiki - Log configuration](https://wiki.squid-cache.org/SquidFaq/SquidLogs)
