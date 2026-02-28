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

### Add role to the APP

1. In the search bar, go to `Subscriptions`
2. Click on one of your subscriptions
3. On the right panel, Click `Access control (IAM)`
4. Click `+ Add` > `Add role assignment`
5. In the `job function roles` sub-tab, search for `Log Analytics Reader` and select it
6. Click `Next`
7. Select `User, group or service principal` as access
8. Click `+ Select members`
9. Type the name of the Azure application created previously, select it and click `Select`
10. Click `Review + assign`

!!! Warning
    Minimal permission in order to work with integration is `Microsoft.Insights/eventtypes/values/Read`, in case if you want to make your custom role

Useful resources are:
- [Azure permissions for Monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor)
- [Retrieve activity log data using Azure monitor REST API](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/rest-activity-log)

### Retrieve your Subscription ID

You also need your **Subscription ID** if you don't have a default one.

In Azure Web Portal:

1. Navigate to: `Home` > `Cost Management + Billing` > `Subscriptions`
2. From there, copy the relevant **Subscription ID** that will be used in the command line (e.g. `uuid`)

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Azure Activity Logs. 
2. Set up the intake configuration with the Subscription ID, Tenant ID, Client ID and Client Secret.

{!_shared_content/operations_center/integrations/generated/39280bac-34d7-4fa2-a6b5-c43791eed1bc.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_39280bac-34d7-4fa2-a6b5-c43791eed1bc_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/39280bac-34d7-4fa2-a6b5-c43791eed1bc.md!}
