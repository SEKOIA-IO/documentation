uuid: 419bd705-fa61-496c-94fa-28d6c1f2e2a8
name: Symantec Endpoint Protection
type: intake

## Overview

Symantec Endpoint Protection is a client-server solution that protects laptops, desktops, and servers in your network against malware, risks, and vulnerabilities. This product is supported by Broadcom.

- **Vendor**: Broadcom
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility**: 14.3 RU3
- **Detection based on**: Telemetry, Alert
- **Supported application or feature**: Endpoint protection and threat detection

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![symantec_endpoint_protection_architecture](/assets/integration/symantec_epp_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites


- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Symantec Endpoint Protection Manager or Symantec Endpoint Security
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Plain text
- **Supported verbosity level**: Alert / Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Symantec Endpoint Protection Logs to Sekoia.io

In this guide, you will configure your Symantec Endpoint Protection Manager or your Symantec Endpoint Security to forward events through syslog.

**Enable Syslog Forwarding:**
- Log on the console of your management server.
- Follow [this guide](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/Monitoring-Reporting-and-Enforcing-Compliance/viewing-logs-v7522439-d37e464/exporting-data-to-a-syslog-server-v8442743-d15e1107.html) to enable log forwarding.
- Provide the IP address, transport protocol (we recommend `TCP`), and listening port (`514`) of the syslog concentrator.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/419bd705-fa61-496c-94fa-28d6c1f2e2a8_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_419bd705-fa61-496c-94fa-28d6c1f2e2a8_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/419bd705-fa61-496c-94fa-28d6c1f2e2a8.md!}

## Further readings

- [Enable Syslog Forwarding for Symantec Endpoint Protection](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/Monitoring-Reporting-and-Enforcing-Compliance/viewing-logs-v7522439-d37e464/exporting-data-to-a-syslog-server-v8442743-d15e1107.html)