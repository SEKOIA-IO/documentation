uuid: a14b1141-2d61-414b-bf79-da99b487b1af
name: F5 BIG-IP
type: intake

## Overview

F5's BIG-IP is a family of products covering software and hardware designed around application availability, access control, and security solutions.

- **Vendor**: F5
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility**: 11.3 and highier
- **Detection based on**: Security Alerts, Telemetry
- **Supported application or feature**: ASM, APM, LTM, AFM, PSM

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![f5_bigip_architecture](/assets/integration/f5_bigip_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

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
- **Supported verbosity level**: Alert, Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

To configure an F5 BIG-IP system to send its Common Event Format (CEF) logs via syslog to a remote syslog server, you need to follow these steps.

#### Configure a log destination

1. Log in to the Configuration utility.
2. Go to `System > Logs > Configuration > Remote Logging`.
3. For Remote IP, enter the destination syslog server IP address, or FQDN. (DNS server configuration required)
4. For Remote Port, enter the remote syslog server UDP port (default is 514).

!!! Note
  For BIG-IP systems in a high availability (HA) configuration, the non-floating self IP address is recommended if using a Traffic Management Microkernel (TMM) based IP address.

5. Choose type `ArcSight` (as we expect CEF log format)
6. Select Add.
7. Select Update.

!!! Note
  For BIG-IP systems in a high availability (HA) configuration, perform a ConfigSync to synchronize the changes to the other devices in the device group.

Please find more information on how to configure remote loging [here](https://my.f5.com/manage/s/article/K13080).

#### Specifically send only certain types of logs

You can further refine your configuration:

- For audit logs only: Use the "audit" facility when configuring remote logging, please use [this documentation](https://my.f5.com/manage/s/article/K56602501).
- For specific module logs (e.g., LTM, ASM): Configure the system to send only those module logs to the remote syslog server, please use [this documentation](https://my.f5.com/manage/s/article/K10887436).

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/a14b1141-2d61-414b-bf79-da99b487b1af.md!} Sample

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a14b1141-2d61-414b-bf79-da99b487b1af_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a14b1141-2d61-414b-bf79-da99b487b1af.md!}

## Further readings

- [Configuring a remote Syslog server for F5 BIG-IP](https://support.f5.com/)