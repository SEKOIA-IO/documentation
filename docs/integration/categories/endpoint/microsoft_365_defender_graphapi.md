uuid: f5ec9a05-7a5c-48a7-8898-057387d7c5d4
name: Microsoft Defender XDR (Graph API)
type: intake

## Overview
- **Vendor**: Microsoft
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: see section below

Microsoft Defender XDR (formerly Microsoft 365 Defender) is a unified pre- and post-breach enterprise defense suite that natively coordinates detection, prevention, investigation, and response across endpoints, identities, email, and applications to provide integrated protection against sophisticated attacks.

This setup guide describes how to forward events produced by `Microsoft Defender XDR (Graph API)` to Sekoia.io XDR.


## Microsoft Defender XDR event types supported
Here is a list of all the Microsoft Defender XDR event types supported by this integration:

* Alert
* Alert Evidence

## Configure

Collect your Tenant ID from your [Azure Portal](https://portal.azure.com/#view/Microsoft_AAD_IAM/TenantPropertiesBlade)(for more information read ([How to find your Microsoft Entra ID (Azure AD) tenant ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant)).

### Create an Azure application

1. On the Azure Portal, in the search bar, go to `App registrations`
2. Click `+ New registration`
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

### Add permissions

1. Go to `Manage` > `API permissions`
2. Click `Add a permission`
3. On the right panel, Select `Microsoft APIs` tab
4. Click `Microsoft Graph`
5. Click `Application permissions`
6. Select the permission: `SecurityAlert.Read.All`
7. Click `Add permissions`
8. In the `API permissions` page, click `Grant admin consent for TENANT_NAME`
9. Click `Yes` in the `Grant admin consent confirmation` modal

### Create an intake

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes), and follow these steps:

1. Click `+ Intake` button to create a new one
2. Choose `Microsoft Defender XDR (Graph API)`, give it a name and choose the relevant Entity
3. Edit the intake configuration:
    - Type the `Application (client) ID` in the `client id` field
    - Type the `Directory (tenant) ID` in the `tenant id` field
    - Type the `Value` of the client secret in the `client secret` field

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/f5ec9a05-7a5c-48a7-8898-057387d7c5d4_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_f5ec9a05-7a5c-48a7-8898-057387d7c5d4_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/f5ec9a05-7a5c-48a7-8898-057387d7c5d4.md!}
