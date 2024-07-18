uuid: 23b75d0c-2026-4d3e-b916-636c27ba4931
name: Cisco Web Security Appliance
type: intake

## Overview

The Cisco Web Security Appliance is a security device that analyzes HTTP(S) traffic with malware detection and reputation filtering. Sending Cisco Web Security Appliance logs to Sekoia.io enables the discovery of potential network security threats, which are contextualized by means of Sekoia.io's Cyber Threat Intelligence (CTI).

- **Vendor**: Cisco
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Security Alerts / Telemetry
- **Supported application or feature**: HTTP(S) traffic analysis

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![cisco_web_security_appliance_architecture](/assets/integration/cisco_web_security_appliance_architecture.png)

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Cisco Web Security Appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain text
- **Supported verbosity level**: Alert, Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Enable Syslog Forwarding

1. **Log on your Cisco Web Security Appliance** and follow [this guide](https://www.cisco.com/c/en/us/td/docs/security/wsa/wsa11-0/user_guide/b_WSA_UserGuide/b_WSA_UserGuide_chapter_010111.html#ariaid-title7) to create a log subscription with the retrieval method `Syslog Push` and the concentrator as the destination.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/23b75d0c-2026-4d3e-b916-636c27ba4931_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_23b75d0c-2026-4d3e-b916-636c27ba4931_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/23b75d0c-2026-4d3e-b916-636c27ba4931.md!}
## Further readings

- [User Guide for AsyncOS 11.0 for Cisco Web Security Appliances](https://www.cisco.com/c/en/us/td/docs/security/wsa/wsa11-0/user_guide/b_WSA_UserGuide/b_WSA_UserGuide_chapter_010111.html)