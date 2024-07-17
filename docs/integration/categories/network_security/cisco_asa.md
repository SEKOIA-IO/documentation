uuid: 466aeca2-e112-4ccc-a109-c6d85b91bbcf
name: Cisco Secure Firewall
type: intake

## Overview

The Cisco Secure Firewall (formerly Next-Generation Firewall) is a security product designed to protect your network, from physical ones to those hosted in the cloud.

Cisco Secure Firewall includes:

- **Adaptive Security Appliance (ASA)**: Combines firewall, antivirus, intrusion prevention, and virtual private network (VPN) capabilities.
- **Firepower Threat Defense (FTD)**: A unified software image that includes the Cisco ASA features and FirePOWER Services. This unified software offers both ASA and FirePOWER functionalities on one platform, in terms of both hardware and software features.
- **Next Generation IPS (NGIPS)**: Detects and stops intrusions in your internal network or public cloud. NGIPS helps you to mitigate vulnerabilities and manage patch applications.

Sending Cisco logs to Sekoia.io will help you discover potential network security threats, which are contextualized thanks to our Cyber Threat Intelligence (CTI).

- **Vendor**: Cisco
- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Security Alerts / Telemetry
- **Supported application or feature**: Network Security
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![cisco_secure_firewall_architecture](/assets/integration/cisco_secure_firewall_architecture.png)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Licence level**:
    - Open Source
- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Cisco Secure Firewall appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF, JSON
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Cisco Secure Firewall Logs to Sekoia.io

This setup guide will show you how to forward both your access and error logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Configure Cisco Secure Firewall Logs:**
   - On Cisco appliances, most of the important hardware and software activities that are relevant for security detection and analysis can be enabled by one simple command:
   
     ```bash
     hostname(config)# logging enable
     hostname(config)# logging timestamp
     hostname(config)# logging trap informational
     ```

2. **Configure the Cisco Appliance for Log Forwarding:**
   - To forward logs to a syslog concentrator:

     ```bash
     hostname(config)# show interface
     hostname(config)# show hostname
     hostname(config)# logging host interface_name syslog_ip [ tcp[/ port ] udp [/ port ] ]
     ```

   - Example:

     ```bash
     hostname(config)# logging host interface_1 127.0.0.1 udp
     ```

   - Explanation:
     - The `interface_name` specifies the interface through which you access the syslog server.
     - The `syslog_ip` specifies the IP address of the syslog server.
     - The `tcp[/ port ]` or `udp[/ port ]` keyword specifies whether TCP or UDP is used to send syslog messages. The default is UDP on port 514.

     !!! Note
        If you specify TCP, the ASA discovers when the syslog server fails and as a security protection, new connections through the ASA are blocked. If you specify UDP, the ASA continues to allow new connections whether or not the syslog server is operational. Valid port values for either protocol range from 1025 through 65535. The default UDP port is 514, and the default TCP port is 1470. For more information about Cisco ASA logging, please refer to your [Cisco documentation](https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S.html).

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/466aeca2-e112-4ccc-a109-c6d85b91bbcf.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_466aeca2-e112-4ccc-a109-c6d85b91bbcf_do_not_edit_manually.md!}

## Further readings

- [Cisco ASA Command Reference](https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S.html).