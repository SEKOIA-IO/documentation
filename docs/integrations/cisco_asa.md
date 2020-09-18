uuid: 466aeca2-e112-4ccc-a109-c6d85b91bbcf 
name: cisco-asa

## Overview

The Cisco ASA 5500 series is Cisco's follow up of the Cisco PIX 500 series firewall.  However, the ASA is not just a pure hardware firewall. The Cisco ASA is a security device that combines firewall, antivirus, intrusion prevention, and virtual private network (VPN) capabilities. It provides proactive threat defense that stops attacks before they spread through the network. Therefore, the Cisco ASA firewall is the whole package, so to speak.

## Setup

This setup guide will show you how to forward your Cisco ASA logs to SEKOIA.IO by means of an Rsyslog transport channel.

### 1. Download the certificate

In order to allow the connection of your rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### 2. Configure Cisco ASA

The first step is to configure Cisco ASA to log the awaited traffic. 

To enable logging, enter the following commands:

```bash
hostname(config) # logging enable
```

You then have to configure an output destination for logs. Here, we choose to send syslog messages to an external syslog server.

```bash
hostname(config)# logging host interface_name syslog_ip [ tcp [/ port ] | udp [/ port ] [ format emblem ]]
```

Explanations:

- The `format emblem` keyword enables EMBLEM format logging for the syslog server with UDP only.
- The `interface_name` argument specifies the interface through which you access the syslog server.
- The `syslog_ip` argument specifies the IP address of the syslog server.
- The `tcp[/ port ]` or `udp[/ port ]` keyword and argument pair specify that the ASA and ASASM should use TCP or UDP to send syslog messages to the syslog server.
- You can configure the ASA to send data to a syslog server using either UDP or TCP, but not both. The default protocol is UDP if you do not specify a protocol.
If you specify TCP, the ASA discover when the syslog server fails and as a security protection, new connections through the ASA are blocked. If you specify UDP, the ASA continue to allow new connections whether or not the syslog server is operational. Valid port values for either protocol are 1025 through 65535. The default UDP port is 514. The default TCP port is 1470.
- For more information about Cisco ASA logging, please refer to your Cisco documentation.

### 3. Configure the Rsyslog server

You can configure your Rsyslog server to forward your Cisco ASA logs to SEKOIA.IO.

Open or create a new Cisco ASA configuration file for Rsyslog:

```bash
sudo vim /etc/rsyslog.d/11-cisco-asa.conf
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
template(name="SEKOIAIOCiscoAsaTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your Cisco ASA events to SEKOIA.IO intake servers under SEKOIAIOCiscoAsaTemplate template
if $hostname == "YOUR_CISCO_ASA_HOSTNAME" then @@(o)intake.sekoia.io:10514;SEKOIAIOCiscoAsaTemplate
```

In the above `template` instruction, change `YOUR_CISCO_ASA_HOSTNAME` and `YOUR_INTAKE_KEY` with the correct values.

### 4. Restart Rsyslog

```bash
$ sudo service rsyslog restart
```

### 5. Enjoy your events

Go to the [events page](/sic/events) to watch your incoming events.
