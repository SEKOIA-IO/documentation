uuid: 591feb54-1d1f-4453-b780-b225c59e9f99
name: Cisco NX-OS
type: intake

## Overview

Cisco NX-OS is a network operating system for Cisco Nexus-series switches.

- **Vendor**: Cisco
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility**: 9.3 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: Network management and operation

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![cisco_nx_os_architecture](/assets/integration/cisco_nx_os_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Cisco NX-OS device
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Cisco NX-OS Logs

This setup guide will show you how to provide an integration between Cisco NX-OS events and Sekoia.io.

**Enable Syslog Forwarding:**
- Log on your Cisco appliance.
- Follow [this guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/6-x/system_management/configuration/guide/b_Cisco_Nexus_9000_Series_NX-OS_System_Management_Configuration_Guide/sm_5syslog.html#task_5793349949823830091) to enable syslog forwarding to a managed syslog forwarder.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/591feb54-1d1f-4453-b780-b225c59e9f99_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_591feb54-1d1f-4453-b780-b225c59e9f99_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/591feb54-1d1f-4453-b780-b225c59e9f99.md!}

## Further readings

- [Cisco Nexus 9000 Series Documentation](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/6-x/system_management/configuration/guide/b_Cisco_Nexus_9000_Series_NX-OS_System_Management_Configuration_Guide.html)