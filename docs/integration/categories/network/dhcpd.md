uuid: 9044ba46-2b5d-4ebd-878a-51d62e84c8df
name: ISC DHCP
type: intake

## Overview

ISC DHCP offers a complete open-source solution for implementing DHCP servers.

- **Vendor**: ISC (Internet Systems Consortium)
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Network Telemetry
- **Supported application or feature**: DHCP Server

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites


- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the ISC DHCP server
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: syslog
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward ISC DHCP Logs to Sekoia.io

This setup guide will show you how to forward your ISC DHCP logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - An internal syslog concentrator is required to collect and forward events to Sekoia.io.

2. **Rsyslog Configuration:**
   - As of now, the main solution to collect ISC DHCP logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

{!_shared_content/operations_center/integrations/generated/9044ba46-2b5d-4ebd-878a-51d62e84c8df.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9044ba46-2b5d-4ebd-878a-51d62e84c8df_do_not_edit_manually.md!}

## Further readings

- [ISC DHCP Documentation](https://www.isc.org/dhcp/)