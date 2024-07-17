uuid: 2ee6048e-8322-4575-8e47-1574946412b6
name: Cisco Email Security Appliance
type: intake

## Overview

Cisco Email Security Appliance (ESA) is an email gateway appliance that provides protection against spam, malware, viruses, and other email threats.

- **Vendor**: Cisco
- **Plan**: Defend Core
- **Supported environment**: On Premise
- **Version compatibility**: 14.2 (Latest version as of now)
- **Detection based on**: Telemetry
- **Supported application or feature**: Email threat protection
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![cisco_email_security_appliance_architecture](/assets/integration/cisco_email_security_appliance_architecture.png)

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
    - Administrator or Root access to the Cisco Email Security Appliance
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

#### Forward Cisco Email Security Appliance Logs to Sekoia.io

This setup guide will show you how to provide an integration between Cisco Email Security Appliance events and Sekoia.io.

#### Detailed Procedure:

1. **Enable Syslog Forwarding:**
   - Log in to your Cisco appliance
   - Go to `System Administration > Log Subscriptions`
   - In `Add Log Subscription`, select `Consolidated Event Logs` as the log type
   - Select the fields that you want in the consolidated event logs
   - In `Retrieval Method`, check `Syslog Push` and fill the form with the IP address and the port of your log concentrator
   - Submit and commit your changes

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/2ee6048e-8322-4575-8e47-1574946412b6.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_2ee6048e-8322-4575-8e47-1574946412b6_do_not_edit_manually.md!}

## Further readings

- [Single Log Line (SLL)](https://docs.ces.cisco.com/docs/single-log-line-sll)