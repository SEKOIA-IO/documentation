uuid: 19cd2ed6-f90c-47f7-a46b-974354a107bb
name: Microsoft Entra ID (Azure AD)
type: intake

## Overview
- **Vendor**: Microsoft
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs, Authentication logs

**Microsoft Entra ID (Azure AD) ** is a cloud-based Identity and Rights management service. The service is developed and managed by Microsoft Corp.



## Configure

To forward **Microsoft Entra ID (Azure AD) ** events from Azure to Sekoia.io you need to send your event to an Azure **Event Hub** where Sekoia.io will collect the events.
<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/integration/cloud_and_saas/event_hub/consume_azure_logs.png">
</div>

### Prerequisite

You must have Contributor write on Azure to perform the following installation.

{!_shared_content/operations_center/integrations/event_hub.md!}

### Send logs from Microsoft Entra ID (Azure AD)  to Azure Event Hub

When you have an **Event Hub** follow this guide to send your **Microsoft Entra ID (Azure AD) ** events from Azure to the **Event Hub**:

You need to activate and configure the **Microsoft Entra ID (Azure AD) ** diagnostic settings (e.g. `company-ad`),
to receive logs from the **Microsoft Entra ID (Azure AD) ** into your **Event Hub**.

Navigate to [Home > Microsoft Entra ID (Azure AD)  (e.g. `company-ad`) > Monitoring > Diagnostic settings](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/DiagnosticSettings):

1. Add a new diagnostic setting, and select “Stream to an event hub” and click on configure.
2. Select the previously created “Event hubs”, “Event Hub” and “SharedAccessKey” (**see step 3 of the event hub guide**).
3. In the log section, select all log categories (as shown below).
4. Choose a name for this configuration and click on “Save”.

![diag](https://github.com/jdpju/documentation/assets/113444861/b5e55fd3-da86-4f2f-8095-3c1704ae7a20){: style="max-width:100%"}

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Microsoft Entra ID / Azure AD`.
2. To fill the form, use the table completed during the creation of the **Event Hub**.


#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_19cd2ed6-f90c-47f7-a46b-974354a107bb_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/19cd2ed6-f90c-47f7-a46b-974354a107bb.md!}

#### Further Readings

- [Microsoft Github diagnostic Active Directory documentation](https://github.com/MicrosoftDocs/SupportArticles-docs/blob/main/support/windows-server/active-directory/configure-ad-and-lds-event-logging.md)
