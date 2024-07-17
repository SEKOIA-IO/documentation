uuid: aeb7d407-db57-44b2-90b6-7df6738d5d7f
name: FreeRADIUS
type: intake

## Overview

FreeRADIUS is an implementation of RADIUS, a protocol for remote user Authentication, Authorization, and Accounting.

In this documentation, you will learn how to collect and send FreeRADIUS logs to Sekoia.io.

- **Vendor**: FreeRADIUS
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Network Telemetry
- **Supported application or feature**: Authentication, Authorization, and Accounting
- **Coverage Score**: 2

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![freeradius_architecture](/assets/integration/freeradius_architecture.png)

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the FreeRADIUS host
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain Text
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward FreeRADIUS Logs to Sekoia.io

This setup guide will lead you into forwarding FreeRADIUS's logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - An internal syslog concentrator is required to collect and forward events to Sekoia.io.

2. **Create the Intake in Sekoia.io:**
   - Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `FreeRADIUS`. Copy the intake key.

3. **Enable Syslog Forwarding for FreeRADIUS:**

   On the system hosting FreeRADIUS:

   1. Edit the file `/etc/freeradius/radiusd.conf` and update the log section:

      ```bash
      $ vi /etc/freeradius/radiusd.conf
      log {
        destination = syslog
        syslog_facility = local1
        stripped_names = no
        auth = yes

        # don't log passwords
        auth_badpass = no 
        auth_goodpass = no
      }
      ```

   2. Forward logs to the concentrator:

      - For Debian-based and RedHat-based Linux distributions, edit the file `/etc/rsyslog.conf` and forward facility `local1`'s logs to the log concentrator:

        ```bash
        $ vi /etc/rsyslog.conf
        # ensure the module imuxsock is not commented, to provide support for local system logging
        module(load="imuxsock")

        local1.* @<ip to the concentrator>
        ```

        Restart the rsyslog service:

        ```bash
        $ systemctl restart rsyslog
        ```

      - For other Linux distributions and BSD systems, edit the file `/etc/syslog.conf` and forward facility `local1`'s logs to the concentrator:

        ```bash
        $ vi /etc/syslog.conf
        local1.* @<ip to the concentrator>
        ```

        Restart the syslog service.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/aeb7d407-db57-44b2-90b6-7df6738d5d7f.md!} Sample

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/aeb7d407-db57-44b2-90b6-7df6738d5d7f.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_aeb7d407-db57-44b2-90b6-7df6738d5d7f_do_not_edit_manually.md!}

## Further readings

- [Configure FreeRADIUS Log Forwarding](https://freeradius.org/documentation/)