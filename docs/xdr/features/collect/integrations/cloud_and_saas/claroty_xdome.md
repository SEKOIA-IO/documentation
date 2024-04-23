uuid: 9f47aa9f-52d7-4849-9462-cf7fc8bcd51a
name: Claroty xDome
type: intake

## Overview

 Claroty XDome is an integrated cybersecurity platform designed for industrial control systems (ICS) and operational technology (OT) environments, providing comprehensive threat detection, asset discovery, and vulnerability management to safeguard critical infrastructure.

## Supported events

This integration supports the following events from Claroty xDome:

- Alerts
- Communication Events

{!_shared_content/operations_center/detection/generated/suggested_rules_9f47aa9f-52d7-4849-9462-cf7fc8bcd51a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/9f47aa9f-52d7-4849-9462-cf7fc8bcd51a.md!}

## Configure

This guide shows you how to set up an integration between Claroty xDome and Sekoia.io.

### Prerequisites

- Have an internal log concentrator

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Claroty xDome. Copy the intake key.

### Set up the integration

To forward the events, set up a new integration in our Claroty console:

1. Log in our Claroty platform
2. In the top bar, click `Settings > System Settings`

    ![step 2](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_01.png){: style="max-width:100%"}

3. In the left panel, click `My Integrations`

    ![step 3](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_02.png){: style="max-width:100%"}

4. In the `My Integrations` tab, click `+ Add Integration`

    ![step 4](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_03.png){: style="max-width:100%"}

5. To create the new integration, select the `Internal Services` category and the `Syslog` integration. Click `Add`

    ![step 5](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_04.png){: style="max-width:100%"}

6. In the settings of the integration:
    - Define the concentrator ip address and port as the destination
    - Select `TCP` as the transport protocol
    - Select `CEF` as the message format and `RFC 5424` as the syslog protocol standard
    - Name the integration and select the collection server to use

    ![step 6](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_05.png){: style="max-width:100%"}

7. In the `Integration Tasks` section:
    - Click `Export Alerts` (1)
    - Enable the Export (2)
    - Click `Select All` (3)

    ![step 7](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_06.png){: style="max-width:100%"}

8. In the `Integration Tasks` section:
    - Click `Export Comm. Events` (1)
    - Enable the Export (2)
    - Click `Select All` (3)

    ![step 8](/assets/operation_center/integration_catalog/cloud_and_saas/claroty_xdome/step_07.png){: style="max-width:100%"}

9. Click `Apply`

## Further readings
- [About Claroty Syslog](https://help.claroty.com/hc/en-us/articles/10703054977053-About-Claroty-Syslog)
