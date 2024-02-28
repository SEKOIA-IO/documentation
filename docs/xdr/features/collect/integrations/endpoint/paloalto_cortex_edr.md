uuid: b5968b0a-1206-4d3b-b960-e6b61e7f6ee6
name: Palo Alto Cortex XDR (EDR)
type: intake


## Overview

Palo Alto Cortex XDR (EDR) is an advanced Endpoint Detection and Response solution offering real-time threat detection, investigation, and response capabilities, empowering organizations to proactively defend against sophisticated cyber threats across their endpoints.

This setup guide shows how to forward EDR alerts collected on the Palo Alto Cortex XDR (EDR) platform to Sekoia.io.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.
    
## Collected events

This integration collects the following events:

- alerts
- telemetry events related to the alerts.

## Supported versions

This integration was tested against the following versions:

- Palo Alto Cortex XDR (EDR) 3.8

{!_shared_content/operations_center/detection/generated/suggested_rules_9b95c9cf-8b78-4830-a1ed-b9e88f05e67a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/9b95c9cf-8b78-4830-a1ed-b9e88f05e67a.md!}



## Create API Key

Before using the **Cortex XDR** connector, you must generate an API key in Cortex XDR. For that you need to follow steps bellow :

1. Within **Cortex XDR**, click **Settings**.
2. Click **Configurations**.

    ![Configuration Page](/assets/operation_center/integration_catalog/cloud_and_saas/paloalto_cortex_edr/configuration.png){: style="max-width:100%; height: 500px;"}

3. In the **Configurations** menu, select **API Keys**, which appears in the **Integrations** section.
4. In the API Keys window, click **+New Key** button to create a new API key. And the **Generate API Key** window will open.

    ![Api Key Page](/assets/operation_center/integration_catalog/cloud_and_saas/paloalto_cortex_edr/api_key.png){: style="max-width:100%"}

5. Select the **Standard** Security Level.
6. Select a role for the API key. After selecting the role, click **Generate**.

    ![Generation Button](/assets/operation_center/integration_catalog/cloud_and_saas/paloalto_cortex_edr/generate.png){: style="max-width:100%"}

7. After you’ve generated the key, copy the **API key** value presented and keep it secure.
8. Return to the **API Keys** window, and select the API key you just generated. Also make note of the **API key ID**, which appears in the API Keys table.

    !!! info
        - You will need also the `Fqdn` which is a unique host and domain name associated with each tenant. When you generate the API Key and Key ID, you are assigned an individual `Fqdn`.


## Configure

### Create the intake

1. Go to the [Intake page](https://app.sekoia.io/operations/intakes) and create a new `Palo Alto Cortex XDR (EDR)` intake.
2. Copy the associated Intake key ( You will use it in the playbook part )

### Pull events

1. Go to the [Playbook page](https://app.sekoia.io/operations/playbooks).
2. Click on `+ PLAYBOOK` and choose `Create a playbook from scratch`.  
3. Give it a name and a description and click on `Next`.
4. In `Choose a trigger`, select the `Fetch Alerts from Cortex`.
5. Click on the `Fetch Alerts from Cortex` module on the right sidebar and in the `Module Configuration` section, select `Create new configuration`.
6. Write a `name` and paste the `API Key`, `API Key ID` and `Fqdn`, then click on `Save`.
7. In the `Trigger Configuration` section, click on `Create new configuration`.
8. Write a `name`, choose a `frequency` - Default is `60` -, paste the `intake_key` associated to your `Fetch Alerts from Cortex` intake and click on `Save`.
9. On the top right corner, start the Playbook. You should see monitoring messages in the `Trigger Logs` section.
10. Check on the Events page that the Cortex logs are being received.

## Further Readings
- [Get start with cortex API](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-API-Reference/Get-Started-with-APIs)
- [Create API KEY](https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/1.0/Cortex-Xpanse-User-Guide/Generate-an-API-Key-in-Cortex-XDR)
