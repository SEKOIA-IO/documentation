---
uuid: 23d06c74-9311-4d56-b2ac-5d70c0b322fc
name: Microsoft Sentinel
type: intake
---

## Overview

- **Vendor**: Microsoft
- **Supported environment**: SaaS
- **Detection based on**: Telemetry, Alerts
- **Supported application or feature**:
    - Office 365 account logs
    - Office 365 audit logs
    - Office 365 trace logs
    - Third-party application logs
    - Windows event logs
    - Web application firewall logs


Microsoft Sentinel is a cloud-native security information and event management (SIEM) service that provides intelligent security analytics for your entire enterprise at cloud scale. Get immediate visibility into your cloud, on-premises, and hybrid environments. Detect and respond to threats with built-in machine learning and artificial intelligence.

## Specification

### Prerequisites

- **Resource**:
    - Azure cloud tenant
    - Microsoft Sentinel instance

- **Permissions**:
    - Administrator permissions to the Azure instance

### Transport Protocol/Method

- **HTTP/HTTPS** for SaaS

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Alert

## Step-by-Step Configuration Procedure

### Create an api key

#### Create an Azure application

1. On the Azure Portal, in the search bar, go to `App registrations`
![App registrations button](/assets/operation_center/integration_catalog/cloud_and_saas/microsoft_sentinel/app_registration_button.png){ align=center }
2. Click [`+ New registration`](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/false)
3. Type a name
4. Select `Accounts in this organizational directory only` option as account type
5. Click `Register`
6. From the `Overview` page, copy `Application (client) ID` and `Directory (tenant) ID`
![IDs](/assets/operation_center/integration_catalog/cloud_and_saas/microsoft_sentinel/ids.png){ align=center }

#### Create a client secret

1. Go to `Manage` > `Certificates & secrets`
![Certificats and secrets](/assets/operation_center/integration_catalog/cloud_and_saas/microsoft_sentinel/certificats_secrets.png){ align=center }
2. Click `+ New client secret`
![Client secret button](/assets/operation_center/integration_catalog/cloud_and_saas/microsoft_sentinel/button_create_new_button.png){ align=center }
3. Type a description and select the desirated expiration period
![Client secret configuration](/assets/operation_center/integration_catalog/cloud_and_saas/microsoft_sentinel/add_client_secret.png){ align=center }
4. Click `Add`
5. Copy the `Value` of the client secret

#### Add role to the app

1. In the search bar, go to `Subscriptions`
2. Click on one of your subscriptions
3. On the right panel, Click `Access control (IAM)`
4. Click `+ Add` > `Add role assignement`
5. In the `job function roles` sub-tab, search for `Microsoft Sentinel Contributor` and select it
6. Click `Next`
7. Select `User, group or service principal` as access
8. Click `+ Select members`
9. Type the name of the Azure application created previously, select it and click `Select`
10. Click `Review + assign`
11. In the `Overview` part, you can find the `Subscription ID`
![Subscription ID](/assets/operation_center/integration_catalog/cloud_and_saas/microsoft_sentinel/subscription_id.png){ align=center }


!!! note
    - You can find the `workspacename` on the `Overview` page under name when you create your `Microsoft Sentinel` instance.
    - The `resourcegroup` depends on the resource group in which you placed your instance. You can also find this on the `Overview page` under `Resource Group`.
    ![Microsoft Sentinel Overview page](/assets/operation_center/integration_catalog/cloud_and_saas/microsoft_sentinel/microsoft_sentinel_overview.png){ align=center }

### Instruction on Sekoia

{!_shared_content/operations_center/integrations/generated/23d06c74-9311-4d56-b2ac-5d70c0b322fc.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_23d06c74-9311-4d56-b2ac-5d70c0b322fc_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/23d06c74-9311-4d56-b2ac-5d70c0b322fc.md!}
