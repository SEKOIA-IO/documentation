uuid: a199fbde-508e-4cb9-ae37-842703494be0
name: BIND

## Overview

BIND is an implementation of the Domain Name System (DNS) of the Internet. It performs both of the main DNS server roles, acting as an authoritative name server for domains, and acting as a recursive resolver in the network.

## Setup

This setup guide will show you how to forward logs produced by your BIND server to SEKOIA.IO by means of an rsyslog transport channel.

On most GNU/Linux servers, two packages need to be installed: `rsyslog` and `rsyslog-gnutls`.

### 1. Download the certificate

In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### 2. Configure BIND to log queries

First, you need to configure your BIND daemon to log queries and forward them to your rsyslog instance. If rsyslog and BIND are installed on the same box, you can simply add the following statement in your BIND’s main configuration file:

```
logging {
        channel syslog_chan {
                syslog daemon;
                severity dynamic;
        };
        category default { syslog_chan; };
        category queries { syslog_chan; };
        category config { syslog_chan; };
        category security { syslog_chan; };
};
```

You can find more informations on [how to configure your BIND instance on its official website](https://kb.isc.org/docs/aa-01526).

### 3. Configure the rsyslog server

Open or create a new BIND configuration file for rsyslog:

```bash
sudo vim /etc/rsyslog.d/46-bind.conf
```

Paste the following rsyslog configuration to trigger the emission of BIND logs by your rsyslog server to SEKOIA.IO:

```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOBINDTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to SEKOIA.IO intake servers under SEKOIAIOBINDTemplate template
if $programname startswith 'named' then @@(o)intake.sekoia.io:10514;SEKOIAIOBINDTemplate
```

In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key.

### 4. Restart rsyslog

```bash
$ sudo service rsyslog restart
```

### 5. Enjoy your events

Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.


## Related files

- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)
