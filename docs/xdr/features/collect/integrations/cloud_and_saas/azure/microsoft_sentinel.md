uuid: 32be933b-ea74-4590-ad01-e81b0c58202f
name: Microsoft Sentinel
type: intake

## Overview
[Microsoft Sentinel](https://learn.microsoft.com/fr-fr/azure/sentinel/), officially known as Microsoft Sentinel, is a cloud-native security information and event management (SIEM) platform developed by Microsoft. It is designed to help organizations detect, investigate, and respond to cybersecurity threats and incidents. Microsoft Sentinel collects and analyzes vast amounts of data from various sources, such as logs, security events, and other telemetry, providing security teams with insights to identify and mitigate potential security risks. The platform leverages advanced analytics, machine learning, and automation to enhance threat detection and response capabilities, aiming to improve overall security posture for organizations using Microsoft Azure and other integrated services.

## Configure
This setup guide will show you how to forward events produced by a Microsoft Sentinel instance hosted on Azure platform to Sekoia.io using a Sentinel playbook. This integration will transmit individual Sentinel incidents along with their corresponding alerts. Notably, this integration excludes coverage for Sentinel events; its primary objective is to exclusively relay alerts, allowing for a more in-depth analysis on the Sentinel side.

Theses changes have to be made from the [Azure Web Portal](https://portal.azure.com).

### Microsoft Sentinel Playbook

As a prerequisite, you need to have a up and running Microsoft Sentinel instance

#### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Microsoft Sentinel`.

#### Create a new playbook

In Azure Web Portal:

1. Navigate to your Sentinel instance
2. Then, from your workspace, select `Automation` in the `Configuration` menu
3. From there, create a new playbook with an Incident trigger `+ Create` > `Playbook with incident trigger`

#### Initialize your playbook

Fill the playbook form with some `Basics` informations: 

- Your subscription 
- An existing resource group or a new one if needed 
- A region and a name

Then, define the Microsoft Sentinel connection which will be use by your playbook to retrieve Sentinel incidents. 

Finally, review and create your new playbook

#### Edit your playbook

Once your playbook has been initialized, you have to edit it in order to format incoming events and forward them to Sekoia.io:

- Click on the `Edit` button to enter the `Logic Apps Designer` page. 
- Go to the `Code View` tab and copy/paste the following code under the "actions" json key (do not forget to add your intake key):
    ```json
        "For_each_-_alert": {
            "foreach": "@triggerBody()?['object']?['properties']?['Alerts']",
            "actions": {
                "Send_an_alert_with_entities": {
                    "runAfter": {},
                    "type": "Http",
                    "inputs": {
                        "body": "@concat('{','\n','\"alertDisplayName\": \"',items('For_each_-_alert')?['properties']?['alertDisplayName'],'\",','\n','\"alertKind\":\"',items('For_each_-_alert')?['kind'],'\",','\n','\"relatedEntities\":',triggerBody()?['object']?['properties']?['relatedEntities'],',','\n','\"alertDescription\": \"', replace(items('For_each_-_alert')?['properties']?['description'], '\n', ' - '),'\",','\n','\"severity\":\"',items('For_each_-_alert')?['properties']?['severity'],'\",','\n','\"systemAlertId\":\"',items('For_each_-_alert')?['properties']?['systemAlertId'],'\",','\n','\"alertTime\":\"',items('For_each_-_alert')?['properties']?['timeGenerated'],'\",','\n','\"ResourceGroupName\":\"',triggerBody()?['workspaceInfo']?['ResourceGroupName'],'\",','\n','\"SubscriptionId\":\"',triggerBody()?['workspaceInfo']?['SubscriptionId'],'\",','\n','\"alertType\":\"',items('For_each_-_alert')?['properties']?['alertType'],'\",','\n','\"providerAlertId\":\"',items('For_each_-_alert')?['properties']?['providerAlertId'],'\",','\n','\"alertStartTime\":\"',items('For_each_-_alert')?['properties']?['startTimeUtc'],'\",','\n','\"alertEndTime\":\"',items('For_each_-_alert')?['properties']?['endTimeUtc'],'\",','\n','\"incidentNumber\": \"',triggerBody()?['object']?['properties']?['incidentNumber'],'\",','\n','\"incidentDescription\": \"',replace(triggerBody()?['object']?['properties']?['description'],'\n', ' - '),'\",','\n','\"vendorName\": \"',items('For_each_-_alert')?['properties']?['vendorName'],'\",','\n','\"productName\": \"',items('For_each_-_alert')?['properties']?['productName'],'\",','\n','\"incidentUrl\": \"',triggerBody()?['object']?['properties']?['incidentUrl'],'\",','\n','\"incidentTactics\":',triggerBody()?['object']?['properties']?['additionalData']?['tactics'],',','\n','\"incidentTechniques\":',triggerBody()?['object']?['properties']?['additionalData']?['techniques'],'\n','}')",
                        "headers": {
                            "X-SEKOIAIO-INTAKE-KEY": "YOUR-INTAKE-KEY"
                        },
                        "method": "POST",
                        "uri": "https://intake.sekoia.io/plain"
                    }
                }
            },
            "runAfter": {},
            "type": "Foreach"
        }
    ```
- Finally, save your playbook

Your playbook will be triggered when a new incident is created on the Sentinel side. Subsequently, for each alert related to this incident, an event will be sent to Sekoia.io. Additionally, you have the option to manually run your playbook on a past incident.