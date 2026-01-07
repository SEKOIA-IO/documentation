uuid: 3f330d19-fdea-48ac-96bd-91a447bb26bd
name: Sophos EDR
type: intake

## Overview

Sophos EDR monitors, detects and mitigates threats on endpoints.
This EDR reduces the attack surface and prevent attacks from running with an anti-exploit, an anti-ransomware and advanced control technology.

This setup guide shows how to forward events produced by Sophos EDR to Sekoia.io.

- **Vendor**: Sophos
- **Supported environment**: Cloud
- **Detection based on**: Telemetry
- **Supported application or feature**: File monitoring, Process monitoring


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
2. Set the intake account: Write a `name` and paste the `client_id` and `client_secret` from the Sophos console and click on `Save`.

    !!! info
        - If you want to change the region with your own region, you can find your region via **protect devices field**, first click on **Protect Devices**, Then copy link of any download links and finally Check the region that appears as part of the URL.
        - No need to change the **Oauth2 Authorization Url** for the moment, as this's the only endpoint to get a JWT token

3. Set the intake configuration, choose a `frequency` - Default is `60` -


![Sophos Module Configuration](/assets/integration/cloud_and_saas/sophos_edr/sophos_module_configuration.png){: style="max-width:60%"}
![Sophos Trigger Configuration](/assets/integration/cloud_and_saas/sophos_edr/sophos_trigger_configuration.png){: style="max-width:60%"}

{!_shared_content/operations_center/integrations/generated/3f330d19-fdea-48ac-96bd-91a447bb26bd_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_3f330d19-fdea-48ac-96bd-91a447bb26bd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3f330d19-fdea-48ac-96bd-91a447bb26bd.md!}

## Further Readings

- [Sophos Central APIs: Send alert and event data to your SIEM](https://support.sophos.com/support/s/article/KB-000036372?language=en_US)
