uuid: c3888137-b34e-4526-ab61-836b2d45a742
name: Netfilter

## Overview

Netfilter is a framework provided by the Linux kernel that offers
various functions and operations for packet filtering, network address
translation, and port translation.

The firewall ruleset might be configured by using several user-space
tools such as `iptables` or `nftables` or even with high level
configuration tools such as firewalld, UFW or ferm. The framework also
provides several ways to log events (`LOG`, `NFLOG`, `ULOG`, etc.).

In this example, we only cover the `iptables` syntax and the basic
`LOG` targets that sends messages to your local syslog server.

The only requirement from SEKOIA.IO’s perspective is that your
`iptables` uses the following prefix: `IPTables/XXX: ` (`XXX` is user
configurable and represents the action, could be `Dropped` for
example).

## Setup

This setup guide will show you how to forward your Linux firewall logs
to SEKOIA.IO by means of an Rsyslog transport channel.
On most linux servers, two packages need to be installed: rsyslog and rsyslog-gnutls.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure Netfilter
The first step is to configure Netfilter to log the awaited
trafic. For example, if you want to only allow HTTP and HTTPS trafic
and log everything else, you could use the following `iptables`
commands:

```bash
# Create a chain that logs packets and then drops them.
$ iptables -N DROP_LOGGING
$ iptables -A DROP_LOGGING -m limit --limit 60/min -j LOG --log-prefix "IPTables/Dropped: " --log-level 4
$ iptables -A DROP_LOGGING -j DROP

# Allow established communications.
$ iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow HTTP communications.
$ iptables -A INPUT -p tcp --dport 80,443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# Log and drop everything else.
$ iptables -A INPUT -j DROP_LOGGING
```

### Configure the Rsyslog server
You can configure your Rsyslog server to forward your `iptables` logs to SEKOIA.IO.

Open or create a new Netfilter configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/11-netfilter.conf
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
template(name="SEKOIAIONetfilterTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your Netfilter events to SEKOIA.IO intake servers under SEKOIAIONetfilterTemplate template
if $programname == "kernel" and  $msg contains "IPTables/"  then @@(o)intake.sekoia.io:10514;SEKOIAIONetfilterTemplate
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
- [netfilter/iptables project homepage](https://www.netfilter.org/)
