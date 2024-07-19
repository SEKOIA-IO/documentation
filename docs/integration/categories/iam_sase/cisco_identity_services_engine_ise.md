uuid: 8a9894f8-d7bc-4c06-b96a-8808b3c6cade
name: Cisco Identity Services Engine (ISE)
type: intake

## Overview

Cisco Identity Services Engine (ISE) is an intelligent security policy enforcement platform that reduces security risks by providing visibility of connections between all users and devices across all network infrastructure. This product provides exceptional control over the information and locations to which users have access on the network. This solution, and all its components, have been approved and rigorously tested as an integrated system.

- **Vendor**: Cisco
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility**: 3.1 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: Network access control and visibility

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![cisco_identity_services_engine_architecture](/assets/integration/cisco_ise_architecture.png)

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Cisco ISE device
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain text
- **Supported verbosity level**: Warning, Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Cisco Identity Services Engine Logs to Sekoia.io

This setup guide will show you how to provide an integration between Cisco Identity Services Engine events and Sekoia.io.

**Enable Syslog Forwarding:**
- Log on your ISE Administration Interface.
- Follow [this guide](https://www.cisco.com/en/US/docs/security/ise/1.0/user_guide/ise10_logging.html#wp1053250).

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/8a9894f8-d7bc-4c06-b96a-8808b3c6cade_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_8a9894f8-d7bc-4c06-b96a-8808b3c6cade_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8a9894f8-d7bc-4c06-b96a-8808b3c6cade.md!}

## Further readings

- [Cisco Identity Services Engine (ISE) documentation](https://www.cisco.com/c/en/us/support/security/identity-services-engine/series.html#~tab-documents)