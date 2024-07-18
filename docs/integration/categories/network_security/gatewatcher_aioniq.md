uuid: bba2bed2-d925-440f-a0ce-dbcae04eaf26
name: Gatewatcher AionIQ
type: intake

## Overview

Gatewatcher AionIQ is a detection and response platform for your network that identifies malicious actions and suspicious behaviors.

- **Vendor**: Gatewatcher
- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Network Telemetry
- **Supported application or feature**: Detection and Response
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![gatewatcher_aioniq_architecture](/assets/integration/gatewatcher_aioniq_architecture.png)

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
    - Administrator rights on the GCenter
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

#### Forward Gatewatcher AionIQ Logs to Sekoia.io

This setup guide will show you how to forward your Gatewatcher AionIQ logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - An internal syslog concentrator is required to collect and forward events to Sekoia.io.

2. **Enable Syslog Forwarding:**
   - Log on your GCenter and follow [this guide](https://docs.gatewatcher.com/en/gcenter/2.5.3/101/itg-ext/syslog.html) to enable syslog forwarding.
   - Set the hostname to your log concentrator and the port number to `514`.
   - Select `json` as the codec, `5424` as RFC and `tcp` as the protocol.

3. **Create the Intake:**
   - Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Gatewatcher AionIQ.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

{!_shared_content/operations_center/integrations/generated/bba2bed2-d925-440f-a0ce-dbcae04eaf26.md!}

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_bba2bed2-d925-440f-a0ce-dbcae04eaf26_do_not_edit_manually.md!}

## Further readings

- [GCenter Syslog configuration overview](https://docs.gatewatcher.com/en/gcenter/2.5.3/101