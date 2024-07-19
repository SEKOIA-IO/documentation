uuid: 02a74ceb-a9b0-467c-97d1-588319e39d71
name: Citrix NetScaler / ADC
type: intake

## Overview

Citrix NetScaler / ADC (formerly Citrix NetScaler) is a delivery controller and load-balancing tool that offers enhanced security and application performance.

- **Vendor**: Citrix
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Detection based on**: Telemetry, Alert, Audit
- **Supported application or feature**: Application Delivery and Security

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![citrix_netscaler_architecture](/assets/integration/citrix_netscaler_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
    - NSLog server with the syslog protocol
    - Auditing module which runs on the NetScaler appliance
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Citrix NetScaler appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF (traffic), Plain text (audit)
- **Supported verbosity level**: Alert, Warning, Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

This setup guide will show you how to forward both your access and error logs to Sekoia.io by means of a syslog transport channel.

#### Forward Audit Logs

- Follow this [guide](https://docs.netscaler.com/en-us/citrix-adc/current-release/system/audit-logging/configuring-audit-logging.html) to enable syslog forwarding for audit logs.

!!! Important
    Make sure `-dateFormat MMDDYYYY` is set and the date is present in logs.

#### Forward Application Firewall Logs

- To enable application firewall logs forwarding, see this [guide](https://support.citrix.com/article/CTX138973/how-to-send-application-firewall-messages-to-a-separate-syslog-server) and apply the following command to convert Application Firewall logs into CEF events:

    ```bash
    set appfw settings CEFLogging on
    ```

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/02a74ceb-a9b0-467c-97d1-588319e39d71_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_02a74ceb-a9b0-467c-97d1-588319e39d71_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/02a74ceb-a9b0-467c-97d1-588319e39d71.md!}

## Further readings

- [Audit log forwarding](https://docs.netscaler.com/en-us/citrix-adc/current-release/system/audit-logging/configuring-audit-logging.html)
- [Application firewall forwarding](https://support.citrix.com/article/CTX138973/how-to-send-application-firewall-messages-to-a-separate-syslog-server)