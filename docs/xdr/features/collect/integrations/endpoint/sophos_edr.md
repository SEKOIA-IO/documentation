uuid: 3f330d19-fdea-48ac-96bd-91a447bb26bd
name: Sophos EDR
type: intake

## Overview

Sophos EDR monitors, detects and mitigates threats on endpoints.
This EDR reduces the attack surface and prevent attacks from running with an anti-exploit, an anti-ransomware and advanced control technology.

This setup guide shows how to forward events produced by Sophos EDR to Sekoia.io.

{!_shared_content/operations_center/detection/generated/suggested_rules_3f330d19-fdea-48ac-96bd-91a447bb26bd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3f330d19-fdea-48ac-96bd-91a447bb26bd.md!}

## Configure

### Create SOPHOS EDR Credentials

!!! Warning
    If you have a "Partner" or "Organization" entity, you need to do the following procedure on every tenant attached to it. Please find more information on the [official documentation](https://developer.sophos.com/intro)

In the Sophos Central Admin console:

1. On the left panel, go to `Global Settings` and select `API Credentials Management`.
2. Click on `Add Credential` to create a credential dedicated to Sekoia.io.
3. Give it a name, select the role `Service Principal ReadOnly` and click on `Add`.
4. In the `API credential Summary`, copy the `Client ID` and the `Client Secret`. It will be used later in Sekoia.io to retrieve the events.

### Create the intake

1. Go to the [Intake page](https://app.sekoia.io/operations/intakes) and create a new `Sophos EDR` intake.
2. Copy the associated Intake key

### Pull events

1. Go to the [Playbook page](https://app.sekoia.io/operations/playbooks).
2. Click on `+ PLAYBOOK` and choose `Create a playbook from scratch`.  
3. Give it a name and a description and click on `Next`.
4. In `Choose a trigger`, select the [Get Sophos events](../../../../automate/library/sophos/#get-sophos-events).
5. Click on the `Get Sophos events` module on the right sidebar and in the `Module Configuration` section, select `Create new configuration`.
6. Write a `name` and paste the `client_id` and `client_secret` from the Sophos console and click on `Save`.

    !!! info
        - If you want to change the region with your own region, you can find your region via **protect devices field**, first click on **Protect Devices**, Then copy link of any download links and finally Check the region that appears as part of the URL.

7. In the `Trigger Configuration` section, click on `Create new configuration`.
8. Write a `name`, choose a `frequency` - Default is `60` -, paste the `intake_key` associated to your `Sophos EDR` intake and click on `Save`.
9. On the top right corner, start the Playbook. You should see monitoring messages in the `Logs` section.
10. Check on the Events page that the Sophos logs are being received.

![Sophos Module Configuration](/assets/operation_center/integration_catalog/cloud_and_saas/sophos_edr/sophos_module_configuration.png){: style="max-width:60%"}
![Sophos Trigger Configuration](/assets/operation_center/integration_catalog/cloud_and_saas/sophos_edr/sophos_trigger_configuration.png){: style="max-width:60%"}

## Further Readings

- [Sophos Central APIs: Send alert and event data to your SIEM](https://support.sophos.com/support/s/article/KB-000036372?language=en_US)
