uuid: d6d15297-e977-4584-9bb3-f0290b99f014
name: ArubaOS Switch
type: intake

## Overview

Aruba OS is the operating system developed by Aruba Networks, designed for their networking devices and infrastructure. It offers advanced features for wireless and wired networking, security, and management, enhancing network performance and reliability.

- **Vendor**: Aruba Networks
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility**: 16.10 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: Network management and performance monitoring
- **Coverage Score**: 2

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![arubaos_switch_architecture](/assets/integration/arubaos_switch_architecture.png){: style="max-width:100%"}


## Specification

### Prerequisites

- **Licence level**:
    - Open Source
- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the ArubaOS device
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain Text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward ArubaOS Logs to Sekoia.io

This setup guide will show you how to forward your ArubaOS logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Enable Syslog Forwarding for ArubaOS:**
   - Log in to your ArubaOS device using SSH, Telnet, or the web-based management interface, depending on your preferred method.
   - Access the configuration mode on your ArubaOS device. For example, if you are using the CLI, you might use the `configure terminal` command.

2. **Configure Syslog Settings:**
   - Use the following command to specify the syslog server's IP address:
     ```bash
     logging x.x.x.x
     ```
     Replace `x.x.x.x` with the IP address of your syslog concentrator.
   - Additionally, you can specify the syslog server's UDP port using the `port` keyword:
     ```bash
     logging x.x.x.x port yyyy
     ```
     Replace `yyyy` with the port number your syslog concentrator is configured to listen on.

3. **Set Log Severity Levels:**
   - Configure the severity level of logs that will be sent to the syslog server.
     ```bash
     logging level informational
     ```

4. **Save Configuration Changes:**
   - Save your configuration changes by issuing the appropriate command (e.g., `write memory` or `copy running-config startup-config`) to ensure that the syslog configuration persists across reboots.

5. **Test Syslog Forwarding (Optional):**
   - You can generate a test log entry to ensure that logs are being forwarded to the syslog server.
     For example, use the following command:
     ```bash
     logging x.x.x.x testing
     ```
     This will generate a test log message that should appear in your syslog server's logs.

6. **Verify Syslog Server Configuration:**
   - On your syslog server, verify that it is configured to accept syslog messages in UDP from the ArubaOS device on the specified port.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/d6d15297-e977-4584-9bb3-f0290b99f014_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_d6d15297-e977-4584-9bb3-f0290b99f014_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d6d15297-e977-4584-9bb3-f0290b99f014.md!}

## Further readings

- [ArubaOS documentation](https://www.arubanetworks.com/documentation/)