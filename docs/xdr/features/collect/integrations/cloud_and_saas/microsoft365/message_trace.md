uuid: 8461aabe-6eba-4044-ad7f-a0c39a2b2279
name: Office 365 Message Trace
type: intake

## Overview

Microsoft 365 Message trace follows email messages as they travel through your Exchange Online organization. You can determine if a message was received, rejected, deferred, or delivered by the service. It also shows what actions were taken on the message before it reached its final status. You can use the information from message trace to efficiently answer user questions about what happened to messages, troubleshoot mail flow issues, and validate policy changes ([More information on microsoft.com](https://docs.microsoft.com/en-us/previous-versions/office/developer/o365-enterprise-developers/jj984335%28v%3Doffice.15%29#rest-uris)).

{!_shared_content/operations_center/detection/generated/suggested_rules_8461aabe-6eba-4044-ad7f-a0c39a2b2279_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8461aabe-6eba-4044-ad7f-a0c39a2b2279.md!}

## Prerequisite

According to [docs.microsoft.com](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/message-trace-scc?view=o365-worldwide), Message Trace is available to the following plans :

- Exchange Online Protection
- Microsoft Defender for Office 365 plan 1 and plan 2
- Microsoft 365 Defender

In Sekoia.io XDR, [create a new intake key](xdr/features/collect/intakes/#create-an-intake-from-our-integrations-catalog) using the "Message Trace" format.

## Configure OAuth

Collect your Tenant ID from your [Azure Portal](https://portal.azure.com/#view/Microsoft_AAD_IAM/TenantPropertiesBlade) (for more information read ([How to find your Microsoft Entra ID (Azure AD)  tenant ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant)).

Add application:

1. Azure Portal, navigate to `App registrations`
2. [Register an application](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/false)
3. Name and create your application
4. Collect the `Application (client) ID` (**client_id**) from the `Overview` page

Create client's secret:

1. From your newly created client page, navigate to `Certificates & secrets`
2. In the `Client secrets` view
3. Add a client secret by choosing `+ New client secret`
4. Once create, copy the secret value (**client_secret**)

Add required permission:

1. From your newly created client page, navigate to `API permissions`
2. `Add a permissions`
3. `APIs my organization uses`
4. `Office 365 Exchange Online`
5. `Application permissions`
6. `ReportingWebService.Read.All`
7. `Add permissions`
8. To finish, use the `Grant admin consent for TENANT_NAME` button

Add required role:

1. From the `Microsoft Entra ID (Azure AD) ` page
2. Open `Roles and administrators`
3. Search and open `Global Reader`
4. Use the `+ Add assignments` to add this role to your application

For a detailed explanation, please read the related documentation [Azure portal - Assign a role](https://learn.microsoft.com/en-us/azure/active-directory/roles/manage-roles-portal).

You can now create the playbook "Create a new playbook > Create a playbook from scratch" and add the "Office 365 Message Trace OAuth" trigger.

Create a trigger configuration and input the following information:

- `client_id`
- `client_secret`
- `intake_key`
- `tenant_id`

Save your configuration and start the trigger.

## Configure Basic Auth (Deprecated)

In Microsoft Azure, create a service account with the `Reports reader` and `Security reader` rights and a strong password (for more information: [MessageTrace report required permissions](https://docs.microsoft.com/en-us/previous-versions/office/developer/o365-enterprise-developers/jj984335(v=office.15)#permissions) and [About admin roles in the Microsoft 365 admin center](https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide)).

Once a dedicated service account as been created, you can validate user's rights by running the following command:

```commandline
curl --user USERNAME:PASSWORD 'https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace?$format=json'
```

This command will contact Microsoft Reporting Web Service API with the provided credentials. 

The response should look like this one (you can use `| jq` to format the response):
```json
{
  "d": {
    "results": [
      {
        "__metadata": {
          "id": "https://reports.office365.com/ecp/ReportingWebService/Reporting.svc/MessageTrace(0)",
          "uri": "https://reports.office365.com/ecp/ReportingWebService/Reporting.svc/MessageTrace(0)",
          "type": "TenantReporting.MessageTrace"
        },
        "Organization": "corp.onmicrosoft.com",
        "MessageId": "<123@sender.foo>",
        "Received": "/Date(1659020996164)/",
        "SenderAddress": "sender@mail.sender.foo",
        "RecipientAddress": "user@corp.net",
        "Subject": "Subject",
        "Status": "Delivered",
        "ToIP": null,
        "FromIP": "1.1.1.1",
        "Size": 33435,
        "MessageTraceId": "579cd25c-9b30-4ce4-d5eb-08da70ab3b38",
        "StartDate": "/Date(1658851300604)/",
        "EndDate": "/Date(1659024100604)/",
        "Index": 0
      }
    ]
  }
}
```

You can now create the playbook "Create a new playbook > Create a playbook from scratch" and add the "Message Trace" trigger.

Create a trigger configuration and input the following information:

- account_name
- account_password
- intake_key

Save your configuration and start the trigger.

## Configure time range

Configure the trigger `timedelta` parameter to pull only events from 24 hours ago (1440 minutes) to be compliant with [Microsoft documentation](https://learn.microsoft.com/en-us/previous-versions/office/developer/o365-enterprise-developers/jj984335(v=office.15)?redirectedfrom=MSDN#data-granularity-persistence-and-availability):
> Events may be delayed by up to 24 hours before they appear in a report.

Configure the trigger `start_time` parameter to pull events from X hours ago if you want to import events that happened in the past. You can, for example, pull events from 30 days ago to now as explain in [Microsoft documentation](https://learn.microsoft.com/en-us/previous-versions/office/developer/o365-enterprise-developers/jj984335(v=office.15)?redirectedfrom=MSDN#data-granularity-persistence-and-availability):
> The information for this report is available for a period of 30 days, or until the subscription is canceled.

## Debug

If your user cannot access the MessageTrace API, please visit the [Azure Sign-in Logs dashboard](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/SignIns) and use the `Add filters` button to filter on the username. You can then choose an authentication event to learn about the issue and use the `Launch the Sign-in Diagnostic.` button to go further. 
