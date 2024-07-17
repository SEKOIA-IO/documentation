uuid: 9f47aa9f-52d7-4849-9462-cf7fc8bcd51a
name: Claroty xDome
type: intake

## Overview

Claroty xDome is an integrated cybersecurity platform designed for industrial control systems (ICS) and operational technology (OT) environments, providing comprehensive threat detection, asset discovery, and vulnerability management to safeguard critical infrastructure.

- **Vendor**: Claroty
- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise / Cloud
- **Version compatibility, if applicable**:
- **Detection based on**: Alerts / Communication Events
- **Supported application or feature**: ICS/OT Security
- **Coverage Score**: 2

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![claroty_xdome_architecture](/assets/integration/claroty_xdome_architecture.png)

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
    - Administrator or Root access to the Claroty xDome appliance
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

#### Forward Claroty xDome Logs to Sekoia.io

This setup guide will show you how to forward both your access and error logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - Have an internal log concentrator.

2. **Create an Intake:**
   - Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Claroty xDome. Copy the intake key.

3. **Set up the Integration in Claroty Console:**
   1. Log in to the Claroty platform.
   2. In the top bar, click `Settings > System Settings`.

      ![step 2](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_01.png){: style="max-width:100%"}

   3. In the left panel, click `My Integrations`.

      ![step 3](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_02.png){: style="max-width:100%"}

   4. In the `My Integrations` tab, click `+ Add Integration`.

      ![step 4](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_03.png){: style="max-width:100%"}

   5. To create the new integration, select the `Internal Services` category and the `Syslog` integration. Click `Add`.

      ![step 5](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_04.png){: style="max-width:100%"}

   6. In the settings of the integration:
      - Define the concentrator IP address and port as the destination.
      - Select `TCP` as the transport protocol.
      - Select `CEF` as the message format and `RFC 5424` as the syslog protocol standard.
      - Name the integration and select the collection server to use.

      ![step 6](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_05.png){: style="max-width:100%"}

   7. In the `Integration Tasks` section:
      - Click `Export Alerts` (1).
      - Enable the Export (2).
      - Click `Select All` (3).

      ![step 7](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_06.png){: style="max-width:100%"}

   8. In the `Integration Tasks` section:
      - Click `Export Comm. Events` (1).
      - Enable the Export (2).
      - Click `Select All` (3).

      ![step 8](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_07.png){: style="max-width:100%"}

   9. Click `Apply`.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/integrations/generated/9f47aa9f-52d7-4849-9462-cf7fc8bcd51a.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_9f47aa9f-52d7-4849-9462-cf7fc8bcd51a_do_not_edit_manually.md!}

## Further readings

- [About Claroty Syslog](https://help.claroty.com/hc/en-us/articles/10703054977053-About-Claroty-Syslog)