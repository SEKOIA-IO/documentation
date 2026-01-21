---
uuid: d6f69e04-6ab7-40c0-9723-84060aeb5529
title: Rubycat PROVE IT
name: Rubycat PROVE IT
type: intake
---

## Overview
PROVE IT by Rubycat is a privileged access management solution.

- **Vendor**: Rubycat
- **Supported environment**: On prem
- **Version compatibility**: 5.x, 6.x and 7.x
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication logs

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder

- **Network**:
    - **On Premise**: Outbound traffic allowed
    - **SaaS**: Customer Inbound and Outbound traffic possible opening

- **Permissions**:
    - Administrator access to the Rubycat PROVE IT instance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog** for On Premise

## Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Step-by-Step Configuration Procedure

To enable Syslog server in Rubycat PROVE IT:

1. Log in to the PROVE IT administration console.
2. Go to `System` > `External servers` > `Syslog servers`.
3. Click `Add new server` to create a new Syslog server configuration.
4. Fill in the required fields:

    - **Name**: Choose a name for your syslog server configuration.
    - **Description**: Enter a description (optional).

5. Click `Next`.
6. Fill in the Syslog server details:

    - **Hostname or IP address**: Enter the hostname or IP address of your syslog forwarder.
    - **Port**: Set the port you have configured for your intake.
    - **Protocol**: Select the protocol (UDP or TCP) matching the syslog forwarder configuration (recommended: TCP).

7. Click `Next`.
8. Click `Submit`.

## Events

{!_shared_content/operations_center/integrations/generated/d6f69e04-6ab7-40c0-9723-84060aeb5529_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d6f69e04-6ab7-40c0-9723-84060aeb5529_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d6f69e04-6ab7-40c0-9723-84060aeb5529.md!}
