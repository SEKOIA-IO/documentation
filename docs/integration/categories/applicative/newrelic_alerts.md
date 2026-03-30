---
uuid: 9df06db1-01f1-46ef-97e4-a269e24ff417
name: New Relic Alerts
type: intake
---

# newrelic\_alerts

### Overview

New Relic is a cloud-native observability platform for real-time monitoring of applications, infrastructure, logs, and metrics. It offers unified dashboards, AI-powered alerts, and distributed tracing to quickly detect and resolve anomalies. Teams use New Relic to optimize performance, reliability, and user experience across digital environments.

!!! Warning Important note - This format is currently in beta. We highly value your feedback to improve its performance.

* **Supported environment**: SaaS
* **Detection based on**: Alerts
* **Supported application or feature**:
  * Alerts

### Step-by-Step Configuration Procedure

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

### NewRelic forwarding configuration

1. Log in the New Relic Console
2. Go to `Alerts > Destinations`
3. Click `Webhook`

* Type a name for the destination (e.g `Sekoia.io Alert Forwarding`)
* Set [`https://intake.sekoia.io/plain`](https://intake.sekoia.io/plain) as the endpoint URL

!!! warning The previous URL works for the FRA1 region. For any other region, replace the domain “intake.sekoia.io” with your region’s HTTP-intake domain—for example:

```
https://app.usa1.sekoia.io/api/v1/intake-http

You can find your region’s domain here: [https://docs.sekoia.io/getting_started/regions/](https://docs.sekoia.io/getting_started/regions/)
```

* Select `Basic authorization` as authorization method
* Type any username (NewRelic requires a non-empty username to validate the form)
* Set the Sekoia.io intake key as the password
* Click `Save destination`
* Go to `Alerts > Alert Policies`
* Click on the alert policies you want to configure
* Go to `Notification` tab
*   Click `Create workflow`

    ℹ️

    In case of a workflow already exists and you cannot create a new one, edit the existing workflow and add a Webhook additional channel
* Type a name for the new workflow (e.g `Forward Alerts to Sekoia.io`)
* Enable `Enable workflow` toggle
* Click `Webhook`
* Type a name for the notification message (e.g `SekoiaForwardingAlerts`)
*   Paste the following template (default one)

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
* Click `Send test notification` and check you intake to validate the correct configuration of the forwarding
* Click `Save message`
* Click the menu on the right of the Webhook destination
* Disable all triggers except `Activated`
* Click `Activate Workflow`

{!\_shared\_content/operations\_center/integrations/generated/9df06db1-01f1-46ef-97e4-a269e24ff417\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_9df06db1-01f1-46ef-97e4-a269e24ff417\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/9df06db1-01f1-46ef-97e4-a269e24ff417.md!}
