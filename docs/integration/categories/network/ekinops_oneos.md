uuid: 4760d0bc-2194-44e5-a876-85102b18d832
name: Ekinops OneOS
type: intake

## Overview

Ekinops OneOS is a comprehensive and flexible network operating system designed to meet the evolving needs of modern telecommunications networks. It provides a unified platform for managing and orchestrating a wide range of network functions, including routing, switching, security, and more. With its modular architecture and open APIs, OneOS enables network operators to easily deploy and scale their networks, while also providing the flexibility to integrate with third-party applications and services. This allows for greater innovation and agility in network operations, ultimately leading to improved service delivery and customer satisfaction.

- **Vendor**: Ekinops
- **Plan**: Defend Prime
- **Supported environment**: On Premise / Cloud
- **Version compatibility, if applicable**:
- **Detection based on**: Network Telemetry
- **Supported application or feature**: Network Management and Security
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![ekinops_oneos_architecture](assets/integration/ekinops_oneos_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Ekinops OneOS
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain Text
- **Supported verbosity level**: Warning / Notice / Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Ekinops OneOS Logs to Sekoia.io

This setup guide will show you how to forward your Ekinops OneOS logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - Have an internal log concentrator.

2. **Enable Syslog Forwarding Logs:**
   - To enable syslog forwarding logs, follow these steps:
     1. Connect to the Ekinops OneOS console.
     2. Add the log concentrator as a new syslog server:

        ```bash
        localhost#configure terminal
        Enter configuration commands, one per line. End with CNTL/Z.
        localhost(config)#syslog server <log concentrator server ip> 23 tcp <log concentrator port>
        localhost(config)#logging syslog filter all
        localhost(config)#logging syslog informational
        localhost(config)#end
        localhost#write mem
        ```
     3. Check the configuration:

        ```bash
        localhost#show syslog servers
        S.No Syslog Server                                    Facility VrfName                       Protocol  port    Interface                  Bytes-Sent
        1    <log concentrator server ip>                     23      default 
        ```
     4. Exit the console.

3. **Create the Intake:**
   - Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Ekinops OneOS. Copy the intake key.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/4760d0bc-2194-44e5-a876-85102b18d832_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_4760d0bc-2194-44e5-a876-85102b18d832_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/4760d0bc-2194-44e5-a876-85102b18d832.md!}


## Further readings

- [Configure a remote Syslog server](https://docs.cyberwatch.fr/help/en/administration/remote_syslog_configuration/)