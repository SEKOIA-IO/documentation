uuid: 9f47aa9f-52d7-4849-9462-cf7fc8bcd51a
name: Claroty xDome
type: intake

## Overview

Claroty xDome is an integrated cybersecurity platform designed for industrial control systems (ICS) and operational technology (OT) environments, providing comprehensive threat detection, asset discovery, and vulnerability management to safeguard critical infrastructure.

- **Vendor**: Claroty
- **Plan**: Defend Prime
- **Supported environment**: On Premise & Cloud
- **Version compatibility, if applicable**:
- **Detection based on**: Alerts, Telemetry
- **Supported application or feature**: Network protocol analysis

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![claroty_xdome_architecture](/assets/integration/claroty_xdome_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Claroty xDome appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF
- **Supported verbosity level**: Alert

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure


### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Instructions on the 3rd Party Solution

This setup guide will show you how to forward both your access and error logs to Sekoia.io by means of a syslog transport channel.
#### Set up the Integration in Claroty Console

   1. Log in to the Claroty platform.
   2. In the top bar, click `Settings > System Settings`.

      ![step 2](/assets/integration/cloud_and_saas/claroty_xdome/step_01.png){: style="max-width:100%"}

   3. In the left panel, click `My Integrations`.

      ![step 3](/assets/integration/cloud_and_saas/claroty_xdome/step_02.png){: style="max-width:100%"}

   4. In the `My Integrations` tab, click `+ Add Integration`.

      ![step 4](/assets/integration/cloud_and_saas/claroty_xdome/step_03.png){: style="max-width:100%"}

   5. To create the new integration, select the `Internal Services` category and the `Syslog` integration. Click `Add`.

      ![step 5](/assets/integration/cloud_and_saas/claroty_xdome/step_04.png){: style="max-width:100%"}

   6. In the settings of the integration:
      - Define the concentrator IP address and port as the destination.
      - Select `TCP` as the transport protocol.
      - Select `CEF` as the message format and `RFC 5424` as the syslog protocol standard.
      - Name the integration and select the collection server to use.

      ![step 6](/assets/integration/cloud_and_saas/claroty_xdome/step_05.png){: style="max-width:100%"}

   7. In the `Integration Tasks` section:
      - Click `Export Alerts` (1).
      - Enable the Export (2).
      - Click `Select All` (3).

      ![step 7](/assets/integration/cloud_and_saas/claroty_xdome/step_06.png){: style="max-width:100%"}

   8. In the `Integration Tasks` section:
      - Click `Export Comm. Events` (1).
      - Enable the Export (2).
      - Click `Select All` (3).

      ![step 8](/assets/integration/cloud_and_saas/claroty_xdome/step_07.png){: style="max-width:100%"}

   9. Click `Apply`.

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/9f47aa9f-52d7-4849-9462-cf7fc8bcd51a_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9f47aa9f-52d7-4849-9462-cf7fc8bcd51a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/9f47aa9f-52d7-4849-9462-cf7fc8bcd51a.md!}

## Further readings

- [About Claroty Syslog](https://help.claroty.com/hc/en-us/articles/10703054977053-About-Claroty-Syslog)