uuid: f0f95532-9928-4cde-a399-ddd992d48472
name: Forcepoint Secure Web Gateway
type: intake

## Overview

Forcepoint Secure Web Gateway (SWG) is a proxy, installed on the endpoint, applying routing policies and analyzing the traffic against threats. This product is supported by Forcepoint LLC.

!!! note
    This integration was initially developed for the on-premise product of Forcepoint Secure Web Gateway, specifically for version 8.5.

- **Vendor**: Forcepoint LLC
- **Plan**: TODO Defend Core / Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**: Version 8.5
- **Detection based on**: Network Telemetry
- **Supported application or feature**: Secure Web Gateway, Proxy

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![forcepoint_swg_architecture](/assets/integration/forcepoint_swg_architecture.png)

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
    - Administrator access to the Forcepoint Secure Web Gateway
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: syslog/CEF
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Enable SIEM Integration in Forcepoint Secure Web Gateway

In this guide, you will configure the gateway to forward events to syslog. This procedure should be repeated for each Forcepoint Policy Server.

#### Detailed Procedure:

1. **Internal Syslog Concentrator Requirement:**
   - An internal syslog concentrator is required to collect and forward events to Sekoia.io. We highly recommend using the [Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder/).

2. **Enable SIEM Integration:**
   - Log on to the Web Security module of the Forcepoint Security Manager and navigate to `Settings > General > SIEM Integration`.
   - In the `Internet Activity Log Data`, click on the button `Add`.
   - Provide the IP address, the transport protocol (recommending `TCP`), and the listening port (`514`) of the concentrator.
   - Select `syslog/CEF` as the SIEM format. Click `OK` then `Save and Deploy` to enable the integration.

3. **Create the Intake:**
   - Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Forcepoint Secure Web Gateway.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

{!_shared_content/operations_center/integrations/generated/f0f95532-9928-4cde-a399-ddd992d48472.md!}

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_f0f95532-9928-4cde-a399-ddd992d48472_do_not_edit_manually.md!}

## Further readings

- [Configuring a remote Syslog server for Forcepoint Secure Web Gateway](https://support.forcepoint.com/)