uuid: 466aeca2-e112-4ccc-a109-c6d85b91bbcf
name: Cisco ASA
type: intake

## Overview

The Cisco ASA is a security device that combines firewall, antivirus, intrusion prevention, and virtual private network (VPN) capabilities. It provides proactive threat defense that stops attacks before they spread through the network. Therefore, the Cisco ASA firewall is the whole package, so to speak.

- From the CISCO ASA machine to an internal log concentrator (Rsyslog), then forwarded to SEKOIA.IO

{!xdr/features/collect/integrations/generated/cisco-asa_do_not_edit_manually.md!}

## Configure

### CISCO ASA logs

On CISCO appliances, most of the important hardward and software activities that are relevant for security detection and analysis, are enable by one simple command.
To enable logging, enter the following commands:

```bash
hostname(config)# logging enable
hostname(config)# logging timestamp
hostname(config)# logging trap informational
```

### Transport to the concentrator

#### Prerequisites
The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator privileges on the CISCO ASA
- Traffic towards the Rsyslog must be open on `UDP 514`

#### Configure the CISCO ASA
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

## Transport to SEKOIA.IO

### Rsyslog

The reader is invited to consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
