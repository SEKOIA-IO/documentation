uuid: e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6
name: IBM AIX
type: intake

## Overview

AIX (Advanced Interactive eXecutive) is a series of proprietary Unix operating systems developed and sold by IBM for several of its computer platforms.

- **Vendor**: IBM
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Telemetry
- **Supported application or feature**: File Monitoring, Process monitoring, Authentication

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![ibm_aix_architecture](/assets/integration/ibm_aix_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

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
- **Supported type(s) of structure**: Text Plain
- **Supported verbosity level**: Informational / Alert

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward IBM AIX Logs to Sekoia.io

This setup guide will show you how to forward your IBM AIX logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Enable Syslog Forwarding:**
   - Follow [this guide](https://www.ibm.com/docs/en/dsm?topic=aado-configuring-aix-audit-dsm-send-syslog-events-qradar) to enable syslog forwarding for audit events.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/e8cb3372-41c8-409f-8e0e-ca4e6cecf7e6.md!}

## Further readings

- [Configuring IBM AIX to send Syslog Events](https://www.ibm.com/docs/en/dsm?topic=aado-configuring-aix-audit-dsm-send-syslog-events-qradar)