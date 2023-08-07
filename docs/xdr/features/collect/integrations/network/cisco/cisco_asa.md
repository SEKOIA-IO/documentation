uuid: 466aeca2-e112-4ccc-a109-c6d85b91bbcf
name: Cisco Secure Firewall
type: intake

## Overview

The Cisco Secure Firewall (formely Next-Generation Firewall) is a security product to protect your network, from physical ones to ones hosted in the cloud.

Cisco Secure Firewall include:

  - Adaptive Security Appliance (ASA): that combines firewall, antivirus, intrusion prevention, and virtual private network (VPN) capabilities.
  - Firepower Threat Defense (FTD): a unified software image, which includes the Cisco ASA features and FirePOWER Services. This unified software is capable of offering the function of ASA and FirePOWER in one platform, both in terms of hardware and software features.
  - Next Generation IPS (NGIPS): that detect and stop intrusions in your internal network or in your public cloud. NGIPS helps you to mitigate vulnerabilities and manage patch application helps you to mitigate vulnerabilities and manage patch applications.

Sending Cisco logs to Sekoia.io will help you discovering potential network security threats, which are contextualized  thanks to our Cyber Threat Intelligence (CTI).


{!_shared_content/operations_center/detection/generated/suggested_rules_466aeca2-e112-4ccc-a109-c6d85b91bbcf_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/466aeca2-e112-4ccc-a109-c6d85b91bbcf.md!}

## Configure

### CISCO Secure Firewall logs

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

- Have administrator privileges on the CISCO appliance
- Traffic towards the concentrator must be open on `UDP 514`

#### Configure the CISCO Appliance
In order to forward the logs to the concentrator, please follow those commands:

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

## Forward logs to Sekoia.io

The reader is invited to consult the [Syslog Forwarding](../../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
