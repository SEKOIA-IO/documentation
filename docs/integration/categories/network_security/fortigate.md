uuid: 5702ae4e-7d8a-455f-a47b-ef64dd87c981
name: Fortigate
type: intake

## Overview

The range of Fortigate firewalls is a complete appliance solution whose security functions are highly developed. The firewalls run on the FortiOS operating system.

- **Vendor**: Fortinet
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Security Alerts / Network Telemetry
- **Supported application or feature**: Traffic, Web, URL Filtering, VPN
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![fortinet_fortigate_architecture](/assets/integration/fortinet_fortigate_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the Fortigate
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Standard, CSV, CEF (Common Event Format)
- **Supported verbosity level**: Alert

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Fortigate Logs to Sekoia.io

This setup guide will show you how to forward your Fortigate logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Fortigate Logs:**
    - On Fortigate appliances, most of the important hardware and software activities that are relevant for security detection and analysis are logged into three files:
      - Traffic: Local out traffic, Denied traffic, Allowed traffic
      - Web
      - URL Filtering
      - VPN

2. **Transport to the Concentrator:**

    - **Prerequisites:**
      - Administrator rights on the Fortigate
      - Traffic towards the syslog concentrator must be open on `TCP/514`

    - **Configure Fortigate:**
      - The first step is to configure Fortigate to log the awaited traffic.
      - You can configure FortiOS to send log messages to remote syslog servers in standard, CSV, or CEF (Common Event Format) format. These three formats are accepted by the Sekoia.io intake.
      - To enable syslog, log into the CLI and enter the following commands:

        ```bash
        config log syslogd setting
        set status enable
        set port 514
        set mode reliable
        set server [IP address of syslog server]
        set facility user
        set format rfc5424
        end
        ```

      - Most FortiGate features are enabled for logging by default. Ensure they are enabled by executing the following command:

        ```bash
        show full-configuration
        ```

      - Make sure the Traffic, Web, and URL Filtering features are enabled for logging with the following commands:

        ```bash
        config log syslogd filter
        set forward-traffic enable
        set local-traffic enable
        set multicast-traffic enable
        ....
        set vpn enable
        set web enable
        set url-filter enable
        end
        ```

      - With some Fortigate appliances, it may not be possible to do the above configuration through the command line. An alternative method is to use the graphical interface and go to the `Log Settings` menu. From there you can choose every logging option within `Event Logging` and `Local Traffic Log` except for the `Denied` options.

      - To use the CEF format, use the following commands:

        ```bash
        config log syslogd setting
        set format cef
        end
        ```

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/5702ae4e-7d8a-455f-a47b-ef64dd87c981_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_5702ae4e-7d8a-455f-a47b-ef64dd87c981_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/5702ae4e-7d8a-455f-a47b-ef64dd87c981.md!}

## Further readings

- [Configuring a remote Syslog server for Fortigate](https://support.fortinet.com/)