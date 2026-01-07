---
uuid: 9df06db1-01f1-46ef-97e4-a269e24ff417
name: New Relic Alerts
type: intake
---

## Overview

New Relic is a cloud-native observability platform for real-time monitoring of applications, infrastructure, logs, and metrics.
It offers unified dashboards, AI-powered alerts, and distributed tracing to quickly detect and resolve anomalies.
Teams use New Relic to optimize performance, reliability, and user experience across digital environments.


!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Supported environment**: SaaS
- **Detection based on**: Alerts
- **Supported application or feature**:
    - Alerts
    
## Step-by-Step Configuration Procedure

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

## NewRelic forwarding configuration

1. Log in the New Relic Console
    
    ![Step 01.png](/assets/integration/application/newrelic/step_1.png)
    
2. Go to `Alerts > Destinations`
3. Click `Webhook`
    
    ![Step 02.png](/assets/integration/application/newrelic/step_2.png)
    
- Type a name for the destination (e.g `Sekoia.io Alert Forwarding`)
- Set [`https://intake.sekoia.io/plain`](https://intake.sekoia.io/plain) as the endpoint URL

!!! warning 
    The previous URL works for the FRA1 region. For any other region, replace the domain “intake.sekoia.io” with your region’s HTTP-intake domain—for example:

    https://app.usa1.sekoia.io/api/v1/intake-http

    You can find your region’s domain here: [https://docs.sekoia.io/getting_started/regions/](https://docs.sekoia.io/getting_started/regions/)

- Select `Basic authorization` as authorization method
- Type any username (NewRelic requires a non-empty username to validate the form)
- Set the Sekoia.io intake key as the password
- Click `Save destination`
    
    ![Step 03.png](/assets/integration/application/newrelic/step_3.png)
    
- Go to `Alerts > Alert Policies`
- Click on the alert policies you want to configure
    
    ![Step 04.png](/assets/integration/application/newrelic/step_4.png)
    
- Go to `Notification` tab
- Click `Create workflow`
    
    ![Step 05.png](/assets/integration/application/newrelic/step_5.png)
    
    <aside>
    ℹ️
    
    In case of a workflow already exists and you cannot create a new one, edit the existing workflow and add a Webhook additional channel
    
    </aside>
    
- Type a name for the new workflow (e.g `Forward Alerts to Sekoia.io`)
- Enable `Enable workflow` toggle
- Click `Webhook`
    
    ![Step 06.png](/assets/integration/application/newrelic/step_6.png)
    
- Type a name for the notification message (e.g `SekoiaForwardingAlerts`)
- Paste the following template (default one)
    
    ```jsx
    {
    	"id": {{ json issueId }},
    	"issueUrl": {{ json issuePageUrl }},
    	"title": {{ json annotations.title.[0] }},
    	"priority": {{ json priority }},
    	"impactedEntities": {{json entitiesData.names}},
    	"totalIncidents": {{json totalIncidents}},
    	"state": {{ json state }},
    	"trigger": {{ json triggerEvent }},
    	"isCorrelated": {{ json isCorrelated }},
    	"createdAt": {{ createdAt }},
    	"updatedAt": {{ updatedAt }},
    	"sources": {{ json accumulations.source }},
    	"alertPolicyNames": {{ json accumulations.policyName }},
    	"alertConditionNames": {{ json accumulations.conditionName }},
    	"workflowName": {{ json workflowName }}
    }
    ```
    
- Click `Send test notification` and check you intake to validate the correct configuration of the forwarding
- Click `Save message`
    
    ![Step 07.png](/assets/integration/application/newrelic/step_7.png)
    
- Click the menu on the right of the Webhook destination
- Disable all triggers except `Activated`
- Click `Activate Workflow`
    
    ![Step 08.png](/assets/integration/application/newrelic/step_8.png)

{!_shared_content/operations_center/integrations/generated/9df06db1-01f1-46ef-97e4-a269e24ff417_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9df06db1-01f1-46ef-97e4-a269e24ff417_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/9df06db1-01f1-46ef-97e4-a269e24ff417.md!}
