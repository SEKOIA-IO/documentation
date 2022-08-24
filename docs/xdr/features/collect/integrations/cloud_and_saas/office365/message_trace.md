uuid: 8461aabe-6eba-4044-ad7f-a0c39a2b2279
name: Office 365 Message Trace
type: intake

## Overview

Microsoft 365 Message trace follows email messages as they travel through your Exchange Online organization. You can determine if a message was received, rejected, deferred, or delivered by the service. It also shows what actions were taken on the message before it reached its final status. You can use the information from message trace to efficiently answer user questions about what happened to messages, troubleshoot mail flow issues, and validate policy changes ([More information on microsoft.com](https://docs.microsoft.com/en-us/previous-versions/office/developer/o365-enterprise-developers/jj984335%28v%3Doffice.15%29#rest-uris)).

{!_shared_content/operations_center/integrations/generated/o365-message-trace_do_not_edit_manually.md!}

## Prerequisite

According to [docs.microsoft.com](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/message-trace-scc?view=o365-worldwide), Message Trace is available to the following plans :

- Exchange Online Protection
- Microsoft Defender for Office 365 plan 1 and plan 2
- Microsoft 365 Defender

In SEKOIA.IO XDR, [create a new intake key](xdr/features/collect/intakes/#create-an-intake-from-our-integrations-catalog) using the "Message Trace" format.

In Microsoft Azure, create a service account with the `Reports reader` and `Security reader` rights and a strong password (for more information: [MessageTrace report required permissions](https://docs.microsoft.com/en-us/previous-versions/office/developer/o365-enterprise-developers/jj984335(v=office.15)#permissions) and [About admin roles in the Microsoft 365 admin center](https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide)).

## Configure

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

## Debug

If your user cannot access the MessageTrace API, please visit the [Azure Sign-in Logs dashboard](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/SignIns) and use the `Add filters` button to filter on the username. You can then clic on an authentication event to learn about the issue and use the `Launch the Sign-in Diagnostic.` button to go further. 