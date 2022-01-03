uuid: ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9
name: HAProxy

## Overview
HAProxy is a free, open source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers. HAProxy has a lot of features and because it is located between your infrastructure and your clients, it can give you a lot of information about either of them.

## Setup
This setup guide will show you how to forward your HAProxy logs to SEKOIA.IO by means of an rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure the Rsyslog server
Open or create a new Haproxy configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/49-haproxy.conf
```

Paste the following rsyslog configuration to trigger the emission of haproxy logs by your rsyslog server to SEKOIA.IO.

```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Collects haproxy logs out of the dedicated HAProxy socket
$AddUnixListenSocket /var/lib/haproxy/dev/log

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOHaproxyTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your HAProxy events to SEKOIA.IO intake servers under SEKOIAIOHaproxyTemplate template
if $programname startswith 'haproxy' then @@(o)intake.sekoia.io:10514;SEKOIAIOHaproxyTemplate
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
- [HAProxy Official Documentation](http://www.haproxy.org/#docs)
