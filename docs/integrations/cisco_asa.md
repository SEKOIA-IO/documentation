uuid: 466aeca2-e112-4ccc-a109-c6d85b91bbcf 
name: cisco-asa

## Overview

The Cisco ASA is a security device that combines firewall, antivirus, intrusion prevention, and virtual private network (VPN) capabilities. It provides proactive threat defense that stops attacks before they spread through the network. Therefore, the Cisco ASA firewall is the whole package, so to speak.

In this documentation we will explain one way to collect and send CISCO ASA logs to SEKOIA.IO.

- From the CISCO ASA machine to an internal log concentrator (Rsyslog), then forwarded to SEKOIA.IO

## I. CISCO ASA logs

On CISCO appliances, most of the important hardward and software activities that are relevant for security detection and analysis, are enable by one simple command.
To enable logging, enter the following commands:

```bash
hostname(config)# logging enable
hostname(config)# logging timestamp
hostname(config)# logging trap informational
```

## II. Transport to the concentrator

### Prerequisites
The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator privileges on the CISCO ASA
- Traffic towards the Rsyslog must be open on `UDP 514`

### Configure the CISCO ASA
In ordre to forward the logs to a Rsyslog, please follow those commands:

> Note the interface name
```bash
hostname(config)# show interface
```

> Note the host name
```bash
hostname(config)# show hostname
```

You then have to configure an output destination for logs. Here, we choose to send syslog messages to an external syslog server.
```bash
hostname(config)# logging host interface_name syslog_ip [ tcp[/ port ] udp [/ port ]
```

Example:
```bash
hostname(config)# logging host interface_1 127.0.0.1 udp
```

Explanations:

- The `interface_name` argument specifies the interface through which you access the syslog server.
- The `syslog_ip` argument specifies the IP address of the syslog server.
- The tcp[/ port ] or udp[/ port ] keyword and argument pair specify that the ASA and ASASM should use TCP or UDP to send syslog messages to the syslog server.
- You can configure the ASA to send data to a syslog server using either UDP or TCP, but not both. The default protocol is UDP if you do not specify a protocol.

> If you specify TCP, the ASA discovers when the syslog server fails and as a security protection, new connections through the ASA are blocked. 
> If you specify UDP, the ASA continues to allow new connections whether or not the syslog server is operational. Valid port values for either protocol are 1025 through 65535. The default UDP port is 514. The default TCP port is 1470.
> For more information about Cisco ASA logging, please refer to your [Cisco documentation](https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S.html).

## III. Transport to SEKOIA.IO

### Configure the Rsyslog to forward to SEKOIA.IO

#### Rsyslog prerequisites
In order to allow the Rsyslog to work properly, please ensure the following packages are installed:

```bash
sudo apt install rsyslog rsyslog-gnutls wget
```

Please ensure the UDP incoming events are allowed in the /etc/rsyslog.conf
```bash
....
# provides UDP syslog reception
module(load="imudp")
input(type="imudp" port="514")
....
```

#### Download the certificate
In order to allow the connection of your Rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

#### Configure the Rsyslog server
Open or create a new cisco-asa configuration file for Rsyslog:
```bash
sudo vim /etc/rsyslog.d/11-cisco-asa.conf
```

Paste the following Rsyslog configuration to trigger the emission of CISCO logs by your Rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOCiscoAsaTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")


# Send your events to SEKOIA.IO intake servers under SEKOIAIOCiscoAsaTemplate template
if ($hostname == "YOUR_CISCO_ASA_HOSTNAME") then {
    action(
        type="omfwd"
        protocol="tcp"
        target="intake.sekoia.io"
        port="10514"
        TCP_Framing="octet-counted"
        StreamDriver="gtls"
        StreamDriverMode="1"
        StreamDriverAuthMode="x509/name"
        StreamDriverPermittedPeers="intake.sekoia.io"
        Template="SEKOIAIOCiscoAsaTemplate"
    )
}
```

> In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key you can find in the Operation Center > Configure > Intakes
> And change the `YOUR_CISCO_ASA_HOSTNAME` variable with the correct value.

#### Restart Rsyslog

```bash
sudo systemctl restart rsyslog.service
```

## IV. Enjoy your events

Go to the [events page](/sic/events) to watch your incoming events.
