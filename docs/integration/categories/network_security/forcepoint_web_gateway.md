uuid: f0f95532-9928-4cde-a399-ddd992d48472
name: Forcepoint Secure Web Gateway
type: intake

## Overview

Forcepoint Secure Web Gateway (SWG) is a proxy, installed on the endpoint, applying routing policies and analyzing the traffic against threats.
This product is supported by Forcepoint LLC.

- **Vendor**: Forcepoint
- **Plan**: Defenb Prime
- **Supported environment**: On Premise
- **Version compatibility**: 8.5
- **Detection based on**: Telemetry
- **Supported application or feature**: HTTP traffic

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Forcepoint Web Gateway server
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

In this guide, you will configure the gateway to forward events to syslog.

!!! Information
    This procedure should be repeated for each Forcepoint Policy Server.

#### Enable SIEM Integration

Log on the Web Security module of the Forcepoint Security Manager and navigate to `Settings > General > SIEM Integration`.

In the `Internet Activity Log Data`, Click on the button `Add`.
Provide the IP address, the transport protocol (recommending `TCP`) and the listening port (`514`) of the concentrator.
Select the `syslog/CEF` as SIEM format. Click `OK` then `Save and Deploy` to enable the integration.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/f0f95532-9928-4cde-a399-ddd992d48472_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_f0f95532-9928-4cde-a399-ddd992d48472_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/f0f95532-9928-4cde-a399-ddd992d48472.md!}
