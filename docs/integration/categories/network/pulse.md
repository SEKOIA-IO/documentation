uuid: 7a12aa3b-ec73-4ebb-8fb3-f7c543fd84a5
name: Pulse Connect Secure
type: intake

## Overview

Pulse Connect Secure is an SSL VPN solution for remote and mobile users.

- **Vendor**: Pulse Secure
- **Plan**: TODO Defend Core / Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: VPN Logs
- **Supported application or feature**: SSL VPN

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![pulse_connect_secure_architecture](/assets/integration/pulse_connect_secure_architecture.png)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites


- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the Pulse Connect Secure system
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: WELF log format
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Pulse Connect Secure Logs to Sekoia.io

This setup guide will show you how to forward your Pulse Connect Secure logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Rsyslog Configuration:**
   - As of now, the main solution to collect Pulse Secure Connect logs leverages the Rsyslog recipe along with the WELF log format offered by Pulse Secure.

2. **Pulse Connect Secure Configuration:**
   - Please refer to the documentation of Pulse Secure Connect to forward events to your syslog concentrator.

3. **Forward Logs to Sekoia.io:**
   - The reader can consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

{!_shared_content/operations_center/integrations/generated/7a12aa3b-ec73-4ebb-8fb3-f7c543fd84a5.md!}

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_7a12aa3b-ec73-4ebb-8fb3-f7c543fd84a5_do_not_edit_manually.md!}

## Further readings

- [Pulse Secure Documentation](https://www.pulsesecure.net/techpubs/)