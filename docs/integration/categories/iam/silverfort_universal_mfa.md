uuid: be2dfa31-3def-4bc0-9250-65a8b3563848
name: Silverfort Universal MFA
type: intake

## Overview

Silverfort Universal MFA is an identity security solution that provides Multi-Factor Authentication (MFA) for Windows Logon, RDP, VPN access, and other resources across on-premises environments, without requiring changes to applications or infrastructure.

- **Vendor**: Silverfort
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication Logs, DailyAuthStatistics

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Admin access to Silverfort Universal MFA Console
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF (Common Event Format)
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

This setup guide will show you how to forward your Silverfort Universal MFA logs to Sekoia.io by means of a syslog transport channel.

#### Configure Syslog Forwarding

1. Log into the Silverfort Universal MFA console and navigate to:

    ```
    SYSTEM SETTINGS > Notifications > Syslog
    ```

2. Add a new Syslog Server and configure the following fields:
    - **Server Name**: Enter a descriptive name for the syslog destination.
    - **Host**: Enter the IP address or hostname of your syslog forwarder.
    - **Protocol**: Select `TCP` (recommended).

3. Save the configuration.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/be2dfa31-3def-4bc0-9250-65a8b3563848_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_be2dfa31-3def-4bc0-9250-65a8b3563848_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/be2dfa31-3def-4bc0-9250-65a8b3563848.md!}
