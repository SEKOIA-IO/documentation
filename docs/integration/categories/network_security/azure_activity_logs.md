---
uuid: 39280bac-34d7-4fa2-a6b5-c43791eed1bc
name: Azure Activity Logs
type: intake
---

## Overview

Azure Activity Logs deliver a subscription-level audit trail of
control-plane events—resource creations, modifications, deletions and
service health incidents.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Supported environment**: SaaS
- **Detection based on**: Telemetry, Alerts, Audit
- **Supported application or feature**:
    - Administrative events
    - Alerts
    - Security events
    - Policy events

## Configure

### Configuring activity log export

1. Go to the Azure portal, and access the **Activity Logs** section.

    ![1](/assets/integration/network_security/azure_activity_logs/1.png){: style="max-width:100%"}
       
2. Select **Activity log** > **Export Activity Logs.**
3. Find and select the subscription, and then select **Add diagnostic setting.**

    ![2](/assets/integration/network_security/azure_activity_logs/2.png){: style="max-width:100%"}

4. In the Diagnostic setting name box, enter a name. Select all applicable categories and then select Save.

    ![3](/assets/integration/network_security/azure_activity_logs/3.png){: style="max-width:100%"}

### Retrieve your Subscription ID

You also need your **Subscription ID** if you don't have a default one.

In Azure Web Portal:

1. Navigate to: `Home` > `Cost Management + Billing` > `Subscriptions`
2. From there, copy the relevant **Subscription ID** that will be used in the command line (e.g. `uuid`)

### Create an Azure application

1. On the Azure Portal, in the search bar, go to `App registrations`
2. Click [`+ New registration`](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/false)
3. Type a name
4. Select `Accounts in this organizational directory only` option as account type
5. Click `Register`
6. From the `Overview` page, copy `Application (client) ID` and `Directory (tenant) ID`

### Create a client secret

1. Go to `Manage` > `Certificates & secrets`
2. Click `+ New client secret`
3. Type a description and select the desired expiration period
4. Click `Add`
5. Copy the `Value` of the client secret

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Azure Activity Logs. 
2. Set up the intake configuration with the Subscription ID, Tenant ID, Client ID and Client Secret.

{!_shared_content/operations_center/integrations/generated/39280bac-34d7-4fa2-a6b5-c43791eed1bc.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_39280bac-34d7-4fa2-a6b5-c43791eed1bc_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/39280bac-34d7-4fa2-a6b5-c43791eed1bc.md!}


## Further Readings

- [Configure Azure activity log export](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-monitor/activity-logs/config-export/configuring-azure-activity-log-export-comprehensive-guide)