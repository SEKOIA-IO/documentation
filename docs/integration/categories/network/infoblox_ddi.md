---
uuid: 864ade96-a96d-4a0e-ab3d-b7cb7b7db618
title: Infoblox DDI
name: Infoblox DDI
type: intake
---

## Overview

Infoblox DNS, DHCP, and IP address management (DDI) enables customers to control and automate their network. It performs both of the main DNS server roles, acting as an authoritative name server for domains, and acting as a recursive resolver in the network.

- **Vendor**: Infoblox
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Network Telemetry
- **Supported application or feature**: DNS, DHCP, IP Address Management

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![infoblox_ddi_architecture](/assets/integration/infoblox_ddi_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the Infoblox NIOS appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain Text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Infoblox DDI Logs to Sekoia.io

This setup guide will show you how to forward your Infoblox DDI logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - An internal syslog concentrator is required to collect and forward events to Sekoia.io.

2. **Enable Syslog Forwarding:**
   - Log on your NIOS appliance and follow [this guide](https://docs.infoblox.com/space/NAG8/22252249/Using+a+Syslog+Server) to enable syslog forwarding.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/864ade96-a96d-4a0e-ab3d-b7cb7b7db618_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_864ade96-a96d-4a0e-ab3d-b7cb7b7db618_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/864ade96-a96d-4a0e-ab3d-b7cb7b7db618.md!}

## Further readings

- [Using a Syslog Server with Infoblox](https://docs.infoblox.com/space/NAG8/22252249/Using+a+Syslog+Server)