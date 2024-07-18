uuid: e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6
name: IBM AIX 
type: intake

## Overview

AIX (Advanced Interactive eXecutive) is a series of proprietary Unix operating systems developed and sold by IBM for several of its computer platforms.

- **Vendor**: IBM
- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Audit Logs
- **Supported application or feature**: System Monitoring and Security
- **Coverage Score**: 1

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![ibm_aix_architecture](/assets/integration/ibm_aix_architecture.png)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Licence level**:
    - Proprietary
- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the AIX system
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: syslog
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward IBM AIX Logs to Sekoia.io

This setup guide will show you how to forward your IBM AIX logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Enable Syslog Forwarding:**
   - Follow [this guide](https://www.ibm.com/docs/en/dsm?topic=aado-configuring-aix-audit-dsm-send-syslog-events-qradar) to enable syslog forwarding for audit events.

2. **Create the Intake:**
   - Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format IBM AIX. Copy the intake key.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

{!_shared_content/operations_center/integrations/generated/e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6.md!}

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6_do_not_edit_manually.md!}

## Further readings

- [Configuring IBM AIX to send Syslog Events](https://www.ibm.com/docs/en/dsm?topic=aado-configuring-aix-audit-dsm-send-syslog-events-qradar)