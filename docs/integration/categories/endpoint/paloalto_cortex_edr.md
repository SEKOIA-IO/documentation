uuid: 9b95c9cf-8b78-4830-a1ed-b9e88f05e67a
name: Palo Alto Cortex XDR (EDR)
type: intake


## Overview

Palo Alto Cortex XDR (EDR) is an advanced Endpoint Detection and Response solution offering real-time threat detection, investigation, and response capabilities, empowering organizations to proactively defend against sophisticated cyber threats across their endpoints.

This setup guide shows how to forward EDR alerts collected on the Palo Alto Cortex XDR (EDR) platform to Sekoia.io.

- **Vendor**: Palo Alto
- **Supported environment**: Cloud 
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: Network device logs


## Collected events

This integration collects the following events:

- alerts
- telemetry events related to the alerts.

## Supported versions

This integration was tested against the following versions:

- Palo Alto Cortex XDR (EDR) 3.8

## Create API Key

Before using the **Cortex XDR** connector, you must generate an API key in Cortex XDR. For that you need to follow steps bellow :

1. Within **Cortex XDR**, click **Settings**.
2. Click **Configurations**.

    ![Configuration Page](/assets/integration/cloud_and_saas/paloalto_cortex_edr/configuration.png){: style="max-width:100%; height: 500px;"}

3. In the **Configurations** menu, select **API Keys**, which appears in the **Integrations** section.
4. In the API Keys window, click **+New Key** button to create a new API key. And the **Generate API Key** window will open.

    ![Api Key Page](/assets/integration/cloud_and_saas/paloalto_cortex_edr/api_key.png){: style="max-width:100%"}

5. Select the **Standard** Security Level.
6. Select a role for the API key. After selecting the role, click **Generate**.

    ![Generation Button](/assets/integration/cloud_and_saas/paloalto_cortex_edr/generate.png){: style="max-width:100%"}

7. After you’ve generated the key, copy the **API key** value presented and keep it secure.
8. Return to the **API Keys** window, and select the API key you just generated. Also make note of the **API key ID**, which appears in the API Keys table.

    !!! info
        - You will need also the `Fqdn` which is a unique host and domain name associated with each tenant. When you generate the API Key and Key ID, you are assigned an individual `Fqdn`.


## Configure

### Create the intake

1. Go to the [Intake page](https://app.sekoia.io/operations/intakes) and create a new `Palo Alto Cortex XDR (EDR)` intake.
2. Create or Select a Palo Alto account with an `API Key`, `API Key ID` and `Fqdn`.
3. Edit the intake configuration with a `chunk size` - Default is `100` and a `frequency` - Default is `60`


{!_shared_content/operations_center/integrations/generated/9b95c9cf-8b78-4830-a1ed-b9e88f05e67a_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9b95c9cf-8b78-4830-a1ed-b9e88f05e67a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/9b95c9cf-8b78-4830-a1ed-b9e88f05e67a.md!}

## Further Readings
- [Get start with cortex API](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-API-Reference/Get-Started-with-APIs)
- [Create API KEY](https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/1.0/Cortex-Xpanse-User-Guide/Generate-an-API-Key-in-Cortex-XDR)
