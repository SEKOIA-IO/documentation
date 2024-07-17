uuid: a14b1141-2d61-414b-bf79-da99b487b1af
name: F5 BIG-IP
type: intake

## Overview

F5's BIG-IP is a family of products covering software and hardware designed around application availability, access control, and security solutions.

- **Vendor**: F5
- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Security Alerts / Telemetry
- **Supported application or feature**: ASM, APM, LTM, AFM, PSM
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![f5_bigip_architecture](/assets/integration/f5_bigip_architecture.png)

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
    - Administrator or Root access to the F5 BIG-IP
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Common Event Format (CEF), key-value
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward F5 BIG-IP Logs to Sekoia.io

This setup guide will show you how to forward your BIG-IP logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Set up the Syslog Concentrator:**
    - Please consult the [Syslog Forwarding](../../../../ingestion_methods/sekoiaio_forwarder/) documentation to set up the concentrator that will forward your logs to Sekoia.io.

2. **Configure a Log Publisher:**
    - Before creating a log publisher, you first need a *management port* log destination:
      ```
      System -> Logs -> Configuration -> Log Destinations -> Create...
      ```
      Give it a name, choose type `Management Port`, fill the address and port of your syslog concentrator, and select protocol UDP
      (alternatively, you can define a pool of syslog servers and use it as a remote high-speed log destination).

    - Then create another log destination to format your logs in CEF:
      ```
      System -> Logs -> Configuration -> Log Destinations -> Create...
      ```
      Give it a name, choose type `ArcSight`, and forward it to the log destination you just created.

    - Now, create a log publisher:
      ```
      System -> Logs -> Configuration -> Log Publishers -> Create...
      ```
      Give it a name, and select the ArcSight log destination you just created.

    - You can now use this log publisher to define logging profiles in your BIG-IP modules. As an example:
      ```
      Access -> Overview -> Event Logs -> Settings -> Create -> Access System Logs -> Publisher
      ```
      or
      ```
      Security -> Event Logs -> Logging Profiles -> Create... -> Publisher
      ```

3. **Direct Configuration:**
    - Some modules allow direct configuration to the syslog concentrator. As an example:
      ```
      Security -> Event Logs -> Logging Profiles -> Create...
      ```
      Then choose `Application Security`, select `Remote Storage` as a storage destination, `Common Event Format (ArcSight)` as a logging format, and fill in your syslog concentrator info.

    - The resulting logging profile can be applied to a given virtual server in:
      ```
      Local Traffic -> Virtual Servers -> Virtual Server List
      ```
      Then choose a virtual server, go to the `Security -> Policies` tab, and apply the log profile.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

{!_shared_content/operations_center/integrations/generated/a14b1141-2d61-414b-bf79-da99b487b1af.md!}

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_a14b1141-2d61-414b-bf79-da99b487b1af_do_not_edit_manually.md!}

## Further readings

- [Configuring a remote Syslog server for F5 BIG-IP](https://support.f5.com/)