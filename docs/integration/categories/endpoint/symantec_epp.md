uuid: 419bd705-fa61-496c-94fa-28d6c1f2e2a8
name: Symantec Endpoint Protection
type: intake

## Overview

Symantec Endpoint Protection is a client-server solution that protects laptops, desktops, and servers in your network against malware, risks, and vulnerabilities. This product is supported by Broadcom.

- **Vendor**: Broadcom
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility**: 14.3 RU3 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: Endpoint protection and threat detection
- **Coverage Score**: 4

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![symantec_endpoint_protection_architecture](/assets/integration/symantec_endpoint_protection_architecture.png)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Licence level**:
    - Open Source
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
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Symantec Endpoint Protection Logs to Sekoia.io

In this guide, you will configure your Symantec Endpoint Protection Manager or your Symantec Endpoint Security to forward events through syslog.

#### Detailed Procedure:

1. **Enable Syslog Forwarding:**
   - Log on the console of your management server.
   - Follow [this guide](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/Monitoring-Reporting-and-Enforcing-Compliance/viewing-logs-v7522439-d37e464/exporting-data-to-a-syslog-server-v8442743-d15e1107.html) to enable log forwarding.
   - Provide the IP address, transport protocol (we recommend `TCP`), and listening port (`514`) of the syslog concentrator.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/419bd705-fa61-496c-94fa-28d6c1f2e2a8.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_419bd705-fa61-496c-94fa-28d6c1f2e2a8_do_not_edit_manually.md!}

## Further readings

- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Symantec).
- [Enable Syslog Forwarding for Symantec Endpoint Protection](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/Monitoring-Reporting-and-Enforcing-Compliance/viewing-logs-v7522439-d37e464/exporting-data-to-a-syslog-server-v8442743-d15e1107.html)