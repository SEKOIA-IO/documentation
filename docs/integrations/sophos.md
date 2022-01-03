uuid: 325369ba-8515-45b4-b750-5db882ea1266
name: sophos

## Overview
Sophos firewalls offer an integrated software solution that provides superior performance in an all-in-one firewall. Its hardened operating system, stateful packet inspection, content filtering (virus & surf protection), application proxies and IPsec based VPN provides powerful solutions to today's security issues. It is designed to maximise networks security without compromising its performance enabling telecommuters, branch offices, customers and suppliers to safely share critical business information.

## Setup

This setup guide will show you how to forward your Sophos logs
to SEKOIA.IO by means of an Rsyslog transport channel.

### Download the certificate
In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure Sophos Firewall
You can configure a syslog server in Sophos Firewall by following the instructions below (Which is appropriate for an XG Firewall, please refer to your documentation in other cases).

- Go to System Services > Log Settings and click Add to configure a syslog server.
- Enter a name for the syslog server.
- Enter the IP Address of the syslog server. Messages from the device will be sent to the entered IP address.
- Enter a Port number that the device will use for communicating with the syslog server. Device will send messages using the selected port.
- Select the Facility from the available options. Note: Facility informs the syslog server of the log message's source. It is defined by the syslog protocol. You can configure the facility to distinguish log messages from different devices. This parameter helps you identify the device that recorded a specific log file.
- Select the Severity Level from the available options.
- Click Save to save the configuration.

### Configure the Rsyslog server
You can configure your Rsyslog server to forward your Sophos logs to SEKOIA.IO.

Open or create a new Sophos configuration file for rsyslog:
```bash
sudo vim /etc/rsyslog.d/23-sophos.conf
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
template(name="SEKOIAIOSophosTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your Sophos events to SEKOIA.IO intake servers under SEKOIAIOSophosTemplate template
if $hostname == \"YOUR_SOPHOS_HOSTNAME\" then @@(o)intake.sekoia.io:10514;SEKOIAIOSophosTemplate
```

In the above `template` instruction, change `YOUR_SOPHOS_HOSTNAME` and `YOUR_INTAKE_KEY` with the correct values.

### Restart Rsyslog

```bash
$ sudo service rsyslog restart
```

### Enjoy your events
Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.
