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
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![cisco_identity_services_engine_architecture](/assets/integration/cisco_identity_services_engine_architecture.png)

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
    - Administrator or Root access to the Cisco ISE device
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

#### Forward Cisco Identity Services Engine Logs to Sekoia.io

This setup guide will show you how to provide an integration between Cisco Identity Services Engine events and Sekoia.io.

#### Detailed Procedure:

1. **Enable Syslog Forwarding:**
   - Log on your ISE Administration Interface.
   - Follow [this guide](https://www.cisco.com/en/US/docs/security/ise/1.0/user_guide/ise10_logging.html#wp1053250).

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/8a9894f8-d7bc-4c06-b96a-8808b3c6cade.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_8a9894f8-d7bc-4c06-b96a-8808b3c6cade_do_not_edit_manually.md!}

## Further readings

- [Cisco Identity Services Engine (ISE) documentation](https://www.cisco.com/c/en/us/support/security/identity-services-engine/series.html#~tab-documents)