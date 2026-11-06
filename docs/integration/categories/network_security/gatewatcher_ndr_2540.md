uuid: 2f1c1e9b-7b8e-4150-879e-62a2a146c3c5
name: Gatewatcher 2.5.4.0
type: intake

## Overview

Gatewatcher 2.5.4.0 is a detection and response platform for your network that identifies malicious actions and suspicious behaviors.

- **Vendor**: Gatewatcher
- **Supported environment**: On Premise, SaaS
- **Version compatibility, if applicable**: 2.5.4.0
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

This setup guide shows you how to forward your Gatewatcher 2.5.4.0 logs to Sekoia.io by means of a syslog transport channel.

#### Setup syslog forwarding on GCenter

   - Log on your GCenter.
   - Click on the `Administration` menu > `Data` zone > `Data export` command
   - Click on the `Create a data export` button
   - In the `Logging server` section: 
       - enter the `213.32.5.228` value in the `Hostname/IP address` field : this value corresponds to `intake.sekoia.io`) domain
       - enter the `10514` value in the `Port` field 
       - enter the `5424` value in the `Syslog RFC` field
       - enter the `tcp` value in the `Protocol` field
   - In the `Structured data` section: 
     - activate the `Enable structured data`
     - click on the `Add` button
     - enter the `intake_key` value in the `Name` field 
     - enter the your intake key in the `Value` field
   - Click on the `Save changes` button to save the configuration

See [GCenter documentation](https://docs.gatewatcher.com/en/gcenter/2.5.4/V0/08_use_cases_administrator/08_06_gcenter_admin/08_06_01_data_management.html) for more details.

{!_shared_content/integration/forwarder_configuration.md!}

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/operations_center/integrations/generated/2f28e4f9-a4f3-40a6-9909-b69f3df32535_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_2f28e4f9-a4f3-40a6-9909-b69f3df32535_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2f28e4f9-a4f3-40a6-9909-b69f3df32535.md!}

## Further readings

- [GCenter 2.5.4.0 Documentation](https://docs.gatewatcher.com/en/gcenter/2.5.4/V0/)
