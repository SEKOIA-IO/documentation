uuid: 995d7daf-4e4a-42ec-b90d-9af2f7be7019
name: Cisco Meraki MX
type: intake

## Overview

Cisco Meraki MX is a multifunctional security and SD-WAN enterprise appliance with a wide set of capabilities.

- **Vendor**: Cisco
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility**: Latest version as of now
- **Detection based on**: Telemetry
- **Supported application or feature**: Security and SD-WAN
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![cisco_meraki_mx_architecture](/assets/integration/cisco_meraki_mx_architecture.png)

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
    - Administrator or Root access to the Cisco Meraki MX device
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

#### Forward Cisco Meraki MX Logs to Sekoia.io

This setup guide will show you how to provide an integration between Cisco Meraki MX events and Sekoia.io.

#### Detailed Procedure:

1. **Enable Syslog Forwarding:**
   - Log on your Cisco Meraki MX appliance.
   - Follow [this guide](https://documentation.meraki.com/General_Administration/Monitoring_and_Reporting/Syslog_Server_Overview_and_Configuration#Configure_Dashboard) to enable syslog forwarding.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/995d7daf-4e4a-42ec-b90d-9af2f7be7019.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_995d7daf-4e4a-42ec-b90d-9af2f7be7019_do_not_edit_manually.md!}

## Further readings

- [Cisco Meraki MX documentation](https://documentation.meraki.com/MX)