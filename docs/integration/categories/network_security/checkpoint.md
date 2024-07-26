uuid: f0a10c21-37d1-419f-8671-77903dc8de69
name: Check Point
type: intake

## Overview

Check Point’s Next Generation Firewalls (NGFWs) are trusted by customers for their highest security effectiveness and their ability to keep organizations protected from sophisticated fifth-generation cyber-attacks. Check Point’s NGFW includes 23 Firewall models optimized for running all threat prevention technologies simultaneously, including full SSL traffic inspection, without compromising on security or performance.

- **Vendor**: Check Point
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: On Premise
- **Version compatibility**: R81.10
- **Detection based on**: Telemetry, Alert
- **Supported application or feature**: Firewall and threat prevention

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![check_point_ngfw_architecture](/assets/check_point_ngfw_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Check Point device
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

The solution to collect Check Point logs leverages the [Log Exporter](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk122323) method and Syslog forwarding.

#### Configure Log Exporter

   - Set up the Log Exporter to send logs in the **CEF format** by following [this guide](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk122323).

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/f0a10c21-37d1-419f-8671-77903dc8de69_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_f0a10c21-37d1-419f-8671-77903dc8de69_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f0a10c21-37d1-419f-8671-77903dc8de69.md!}

## Further readings

- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Check_Point).
- [Log Exporter Configuration](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk122323)