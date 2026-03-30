uuid: a3617bc2-090f-44f6-aeb2-1c6088e24878
name: Office 365 Message Trace (Graph API)
type: intake

## Overview

Microsoft 365 Message trace follows email messages as they travel through your Exchange Online organization. You can determine if a message was received, rejected, deferred, or delivered by the service. It also shows what actions were taken on the message before it reached its final status. You can use the information from message trace to efficiently answer user questions about what happened to messages, troubleshoot mail flow issues, and validate policy changes ([More information on microsoft.com](https://docs.microsoft.com/en-us/previous-versions/office/developer/o365-enterprise-developers/jj984335%28v%3Doffice.15%29#rest-uris)).

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Vendor**: Microsoft
- **Supported environment**: Cloud
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:


## Prerequisite

According to [docs.microsoft.com](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/message-trace-scc?view=o365-worldwide), Message Trace is available to the following plans :

- Exchange Online Protection
- Microsoft Defender for Office 365 plan 1 and plan 2
- Microsoft 365 Defender

## Configure

### Provision the Microsoft application

In order to access message traces in the Microsoft Graph API, you must provision the Microsoft application `8bd644d1-64a1-4d4b-ae52-2e0cbf64e373`.

1. Log in the Azure Portal
2. Open the cloud shell
    
    ![Azure Cloud Shell](/assets/operation_center/integration_catalog/email/office365_message_trace_graph_api/azure_cloud_shell.png){: style="max-width:100%"}

3. If you use the bash cloud shell, switch to the Powershell one. Click confirm in the modal.
    
    ![Azure - Switch to Powershell](/assets/operation_center/integration_catalog/email/office365_message_trace_graph_api/azure_switch_to_powershell.png){: style="max-width:100%"}
 
    ![Azure - Confirm](/assets/operation_center/integration_catalog/email/office365_message_trace_graph_api/azure_confirm.png){: style="max-width:100%"}
    
4. Paste this command to connect to the Microsoft Graph Powershell
    
    ```powershell
    Connect-MgGraph -Scopes "Application.ReadWrite.All"
    ```
    
5. Paste this command to provision the service principal
    
    ```powershell
    New-MgServicePrincipal -AppId 8bd644d1-64a1-4d4b-ae52-2e0cbf64e373
    ```

### Configure OAuth

Collect your Tenant ID from your [Azure Portal](https://portal.azure.com/#view/Microsoft_AAD_IAM/TenantPropertiesBlade)(for more information read [How to find your Microsoft Entra ID (Azure AD) tenant ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant)).

#### Create an Azure application

1. On the Azure Portal, in the search bar, go to `App registrations`
2. Click `+ New registration`
3. Type a name
4. Select `Accounts in this organizational directory only` option as account type
5. Click `Register`
6. From the `Overview` page, copy `Application (client) ID` and `Directory (tenant) ID`

#### Create a client secret

1. Go to `Manage` > `Certificates & secrets`
2. Click `+ New client secret`
3. Type a description and select the desired expiration period
4. Click `Add`
5. Copy the `Value` of the client secret

#### Add permissions

1. Go to `Manage` > `API permissions`
2. Click `Add a permission`
3. On the right panel, Select `Microsoft APIs` tab
4. Click `Microsoft Graph`
5. Click `Application permissions`
6. Select the permission:`ExchangeMessageTrace.Read.All`
7. Click `Add permissions`
8. In the `API permissions` page, click `Grant admin consent for TENANT_NAME`
9. Click `Yes` in the `Grant admin consent confirmation` modal

### Create an intake

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes), and follow these steps:

1. Click `+ Intake` button to create a new one
2. Choose `Microsoft 365 Message Trace (Graph API)`, give it a name and choose the relevant Entity
3. Edit the intake configuration:
    - Type the `Application (client) ID` in the `client id` field
    - Type the `Directory (tenant) ID` in the `tenant id` field
    - Type the `Value` of the client secret in the `client secret` field
    
{!_shared_content/operations_center/integrations/generated/a3617bc2-090f-44f6-aeb2-1c6088e24878_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a3617bc2-090f-44f6-aeb2-1c6088e24878_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a3617bc2-090f-44f6-aeb2-1c6088e24878.md!}

## Troubleshooting

### App ID `8bd644d1-64a1-4d4b-ae52-2e0cbf64e373` not found

In order to retrieve Office365 MessageTrace logs, the Microsoft GraphAPI requires to provision the Microsoft application `8bd644d1-64a1-4d4b-ae52-2e0cbf64e373` as Service Principal in your tenant.

Please refer [Provision the Microsoft Application](#provision-the-microsoft-application).
