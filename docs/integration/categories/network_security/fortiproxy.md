uuid: 270777d7-0c5a-42fb-b901-b7fadfb0ba48
name: FortiProxy
type: intake

## Overview

FortiProxy is a web proxy that protects clients against internet threats.
In this documentation, we will explain one way to collect and send FortiProxy logs to Sekoia.io.

- **Vendor**: Fortinet
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Security Alerts / Network Telemetry
- **Supported application or feature**: On FortiProxy appliances, different types of logs are available. This intake currently supports:
    - **Traffic**: Records traffic flow information, such as HTTP/HTTPS requests and responses.
    - **HTTP Transaction**: Records HTTP transaction-related traffic log.
    - **DLP**: Records data leak prevention events.

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![fortinet_fortiproxy_architecture](/assets/integration/fortinet_fortiproxy_architecture.png)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on FortiProxy
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Key-Value
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

This setup guide will show you how to forward your FortiProxy logs to Sekoia.io by means of a syslog transport channel.

#### Transport to the Concentrator

- **Prerequisites:**
    - Administrator rights on FortiProxy
    - Traffic towards the syslog concentrator must be open on `UDP 514`

- **Configure Logging to a syslog Server:**

    1. Go to `Log > Log Settings > Remote Logging and Archiving`.
    2. Tick the box `Send Logs to Syslog`.
    3. In `IP Address/FQDN`, enter the IP address or the domain name of the remote Syslog server.
    4. In `Log Settings`, you can customize what types of events you want to send to Sekoia.io. By default:
        - `Event Logging` : `All`
        - `Local Traffic Log` : `All`
    5. Click `Apply`.

    For more information, please refer to the official documentation of [FortiProxy](https://docs.fortinet.com/document/fortiproxy/7.0.0/administration-guide/707542/log-settings#Log_Settings).

{!_shared_content/integration/forwarder_configuration.md!}

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/operations_center/integrations/generated/270777d7-0c5a-42fb-b901-b7fadfb0ba48_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_270777d7-0c5a-42fb-b901-b7fadfb0ba48_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/270777d7-0c5a-42fb-b901-b7fadfb0ba48.md!}

## Further readings

- [Configure FortiProxy Log Forwarding](https://docs.fortinet.com/document/fortiproxy/7.0.0/administration-guide/707542/log-settings#Log_Settings)