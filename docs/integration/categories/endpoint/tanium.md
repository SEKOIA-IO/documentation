uuid: 59991ced-c2a0-4fb0-91f3-49e3993c16f5
name: Tanium
type: intake

## Overview
Tanium solutions manage and protect networks and endpoints.

- **Vendor**: Tanium
- **Supported environment**: On Premise
- **Version compatibility**:7.5.6
- **Detection based on**: Telemetry
- **Supported application or feature**: File, Network, Process, Registry


## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the TanOS console
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Text Plain
- **Supported verbosity level**: Informational

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Tanium Logs to Sekoia.io

This setup guide will show you how to forward your Tanium logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Enable Syslog Forwarding:**

    - Follow [this guide](https://help.tanium.com/bundle/ug_appliance_onprem/page/appliance/syslog.html) to enable syslog forwarding for events.
    - Set the syslog-forwarder as the destination of the syslog configuration.
      We recommend to disable TLS and enable TCP octet framing and RFC5424 output format.

{!_shared_content/operations_center/integrations/generated/59991ced-c2a0-4fb0-91f3-49e3993c16f5_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_59991ced-c2a0-4fb0-91f3-49e3993c16f5_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/59991ced-c2a0-4fb0-91f3-49e3993c16f5.md!}

## Further readings

- [Configuring TanOS to send Syslog Events](https://help.tanium.com/bundle/ug_appliance_onprem/page/appliance/syslog.html)
