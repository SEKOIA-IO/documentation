uuid: 8461aabe-6eba-4044-ad7f-a0c39a2b2279
name: Office 365 Message Trace
type: intake

## Overview

Microsoft 365 Message trace follows email messages as they travel through your Exchange Online organization. You can determine if a message was received, rejected, deferred, or delivered by the service. It also shows what actions were taken on the message before it reached its final status. You can use the information from message trace to efficiently answer user questions about what happened to messages, troubleshoot mail flow issues, and validate policy changes ([More information on microsoft.com](https://docs.microsoft.com/en-us/previous-versions/office/developer/o365-enterprise-developers/jj984335%28v%3Doffice.15%29#rest-uris)).

{!_shared_content/operations_center/integrations/generated/o365-message-trace_do_not_edit_manually.md!}

## Configure

First, create a Microsoft service account with the `Reports reader` rights and a strong password.

Once the account created, you can validate user's rights:

```commandline
curl -sS  --user USERNAME:PASSWORD 'https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace?$format=json'
```

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

You can now create enable the trigger "Create a new playbook" > "Create a playbook from scratch" and add the "Message Trace" trigger.