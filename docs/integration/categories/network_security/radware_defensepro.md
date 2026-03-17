uuid: a90e587e-06e7-47c4-9738-1f9172277646
name: Radware DefensePro
type: intake

## Overview

Radware is a leading provider of cybersecurity and application-delivery solutions that keep enterprise applications fast, available and secure across on-premises, cloud and hybrid environments. The platform offers real-time DDoS protection, a web application firewall, application delivery controllers, bot management and API security, all unified under centralized management with advanced analytics and automation. By combining multi-layered defenses with performance optimization, Radware enables organizations to mitigate attacks, accelerate traffic and ensure continuous service availability.

- **Vendor**: Radware
- **Supported environment**: On-premises (DefensePro appliance)
- **Version compatibility, if applicable**:
- **Detection based on**: Telemetry
- **Supported application or feature**: DDoS Attack Detection, Attack Mitigation, Traffic Analysis

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder (e.g., Rsyslog, Syslog-ng)
- **Network**:
    - Outbound traffic from DefensePro to syslog server on TCP/UDP 514 (or custom port)
    - Outbound traffic from syslog server to Sekoia.io on TCP 10514
- **Permissions**:
    - Administrator rights on Radware DefensePro to configure syslog forwarding
    - Root access to the Linux server hosting the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog** (via syslog concentrator)

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Radware DefensePro Logs to Sekoia.io

This setup guide will show you how to forward your Radware DefensePro logs to Sekoia.io by means of a syslog transport channel through a concentrator.

#### Prerequisites

Before you start:

- Connect to [Sekoia.io SOC Platform with a Defend Plan](https://app.sekoia.io/intakes)
- Add an Intake to the relevant Entity
- Keep trace of the automatically generated Intake key
- Have a syslog concentrator (Rsyslog or Syslog-ng) already running and configured to forward logs to Sekoia.io

#### Detailed Procedure

##### Configure Syslog on Radware DefensePro

There are two ways to configure syslog on Radware DefensePro: through the Web UI or via the APSolute Vision management portal. Choose the method that best suits your environment and preferences.

###### Web UI Configuration

1. Log in to the Radware DefensePro management portal
2. Navigate to **Services** > **Syslog Reporting**
3. Choose Enable under the **Syslog Operation** menu
4. Click on **Create** to add a new syslog destination server
5. Fill in the required fields **Syslog server**, **Syslog server Source Port** (default is 514), **Syslog server destination Port** (default is 514) and select the appropriate **Protocol** (TCP or UDP)
6. Click **Set** to confirm the configuration

###### APSolute Vision Configuration

1. Log in to the APSolute Vision management portal
2. Navigate to **Configuration** > **Setup** > **Reporting Settings** > **Syslog**
3. Enable syslog and enter the syslog server address and ports
4. Select your preferred protocol (TCP or UDP)
5. Click **Submit** to apply the configuration 

{!_shared_content/integration/forwarder_configuration.md!}

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/operations_center/integrations/generated/a90e587e-06e7-47c4-9738-1f9172277646_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a90e587e-06e7-47c4-9738-1f9172277646_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a90e587e-06e7-47c4-9738-1f9172277646.md!}

## Further readings

- [Radware Syslog configuration](https://support.radware.com/app/answers/answer_view/a_id/19907/related/1)
