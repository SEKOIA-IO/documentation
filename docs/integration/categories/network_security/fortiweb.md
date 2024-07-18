uuid: 2259adc3-9d93-4150-9c1c-46804e636084
name: FortiWeb
type: intake

## Overview

This documentation details one way to collect and send FortiWeb logs to Sekoia.io: from the FortiWeb machine to an internal syslog concentrator, then forwarded to Sekoia.io.

- **Vendor**: Fortinet
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Network Telemetry
- **Supported application or feature**: WAF
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![fortinet_fortiweb_architecture](/assets/integration/fortinet_fortiweb_architecture.png)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the FortiWeb (read & write permission)
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Key-Value
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward FortiWeb Logs to Sekoia.io

This setup guide will show you how to forward your FortiWeb logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **FortiWeb Logs:**
    - On FortiWeb appliances, most of the important hardware and software activities that are relevant for security detection and analysis are logged into three files:
      - Traffic: Displays traffic flow information, such as HTTP/HTTPS requests and responses.
      - Event: Displays administrative events, such as downloading a backup copy of the configuration, and hardware failures.
      - Attack: Displays attack and intrusion attempt events.

2. **Transport to the Concentrator:**

    - **Prerequisites:**
      - Administrator rights on the FortiWeb (read & write permission)
      - Traffic towards the syslog concentrator must be open on `UDP 514`

    - **Configure FortiWeb:**

      **Enable logging via trigger mechanism:**

      1. Go to `Log&Report > Log Config > Other Log Settings`.
      2. Tick the boxes: Enable Attack Log / Enable Traffic Log / Enable Event Log.

      **Configure Syslog Policies:**

      1. Go to `Log&Report > Log Policy > Syslog Policy`.
      2. Click `Create New`.
      3. In `IP Address`, enter the address of the remote Syslog server.
      4. In `Port`, enter the listening port number of the Syslog server. The default is 514.
      5. Click `OK`.

      **Configure Log Destinations:**

      1. Go to `Log&Report > Log Config > Global Log Settings`.
      2. Tick the syslog box.
      3. Select the relevant Syslog Policy, Log Level, and Facility.
      4. Click `Apply`.

      For more information, please refer to the official documentation of [FortiWeb](https://docs.fortinet.com/document/fortiweb/6.1.1/administration-guide/303842/logging).

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/2259adc3-9d93-4150-9c1c-46804e636084.md!} Sample

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/2259adc3-9d93-4150-9c1c-46804e636084.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_2259adc3-9d93-4150-9c1c-46804e636084_do_not_edit_manually.md!}

## Further readings

- [Configuring a remote Syslog server for FortiWeb](https://docs.fortinet.com/document/fortiweb/6.1.1/administration-guide/303842/logging)