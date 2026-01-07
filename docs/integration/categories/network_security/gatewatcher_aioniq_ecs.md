---
uuid: 2f28e4f9-a4f3-40a6-9909-b69f3df32535
title: Gatewatcher AionIQ
name: Gatewatcher AionIQ
type: intake
---

## Overview

Gatewatcher AionIQ is a detection and response platform for your network that identifies malicious actions and suspicious behaviors.

- **Vendor**: Gatewatcher
- **Supported environment**: On Premise
- **Version compatibility, if applicable**: 2.5.3.103
- **Detection based on**: Network Telemetry
- **Supported application or feature**: Malware and Network events

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the Gatewatcher GCenter
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Alert / Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

This setup guide will show you how to forward your Gatewatcher AionIQ logs to Sekoia.io by means of a syslog transport channel.

#### Setup syslog forwarding on GCenter

   - Log on your GCenter
   - Go to  `Administrators` > `Data` > `Log export`
   - Click `Data export #1` or `Data export #2`
   - Click `Enabled` to activate the data export
   - In the `Logging server` section, set the hostname to your log concentrator and the port number to `514`
   - Select `5424` as Syslog RFC and `tcp` as the protocol.
   - Select `ECS log format 1.0.0` as formatting 
   - Click `Save changes` to save the configuration

See [GCenter documentation](https://docs.gatewatcher.com/en/gcenter/2.5.3/103/08_use_cases_administrator/05_gcenter_admin/01_data_management.html) for more details.

{!_shared_content/integration/forwarder_configuration.md!}

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/operations_center/integrations/generated/2f28e4f9-a4f3-40a6-9909-b69f3df32535_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_2f28e4f9-a4f3-40a6-9909-b69f3df32535_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2f28e4f9-a4f3-40a6-9909-b69f3df32535.md!}

## Further readings

- [GCenter 2.5.3v103 Documentation](https://docs.gatewatcher.com/en/gcenter/2.5.3/103)
