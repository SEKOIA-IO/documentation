uuid: 02a74ceb-a9b0-467c-97d1-588319e39d71
name: Citrix NetScaler / ADC
type: intake

## Overview

Citrix NetScaler / ADC (formerly Citrix NetScaler) is a delivery controller and load-balancing tool that offers enhanced security and application performance.

- **Vendor**: Citrix
- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Telemetry
- **Supported application or feature**: Application Delivery and Security
- **Coverage Score**: 3

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![citrix_netscaler_architecture](/assets/integration/citrix_netscaler_architecture.png)

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
    - Administrator or Root access to the Citrix NetScaler appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Citrix NetScaler / ADC Logs to Sekoia.io

This setup guide will show you how to forward both your access and error logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - Have an internal log concentrator.
   - Have an NSLog server with the syslog protocol.
   - Have an auditing module running on the NetScaler appliance.

2. **Forward Audit Logs:**
   - Follow this [guide](https://docs.netscaler.com/en-us/citrix-adc/current-release/system/audit-logging/configuring-audit-logging.html) to enable syslog forwarding for audit logs.
   
   **IMPORTANT:** Make sure `-dateFormat MMDDYYYY` is set and the date is present in logs.

3. **Forward Application Firewall Logs:**
   - To enable application firewall logs forwarding, see this [guide](https://support.citrix.com/article/CTX138973/how-to-send-application-firewall-messages-to-a-separate-syslog-server) and apply the following command to convert Application Firewall logs into CEF events:
   
     ```bash
     set appfw settings CEFLogging on
     ```

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/02a74ceb-a9b0-467c-97d1-588319e39d71.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_02a74ceb-a9b0-467c-97d1-588319e39d71_do_not_edit_manually.md!}

## Further readings

- [Audit log forwarding](https://docs.netscaler.com/en-us/citrix-adc/current-release/system/audit-logging/configuring-audit-logging.html)
- [Application firewall forwarding](https://support.citrix.com/article/CTX138973/how-to-send-application-firewall-messages-to-a-separate-syslog-server)