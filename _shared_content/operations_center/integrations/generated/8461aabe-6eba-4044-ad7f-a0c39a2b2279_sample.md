
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "messagetrace"


    ```json
	{
        "__metadata": {
            "id": "https://reports.office365.com/ecp/ReportingWebService/Reporting.svc/MessageTrace(0)",
            "uri": "https://reports.office365.com/ecp/ReportingWebService/Reporting.svc/MessageTrace(0)",
            "type": "TenantReporting.MessageTrace"
        },
        "Organization": "examplecorp.onmicrosoft.com",
        "MessageId": "<3a273efc-cd65-4335-96ec-5f6934f0fb10@az.uksouth.production.microsoft.com>",
        "Received": "/Date(1658751973240)/",
        "SenderAddress": "azure-noreply@microsoft.com",
        "RecipientAddress": "foo.bar@example.corp",
        "Subject": "PIM: MessageTrace API service account has the Privileged Role Administrator role",
        "Status": "GettingStatus",
        "ToIP": null,
        "FromIP": "1.1.1.1",
        "Size": 87680,
        "MessageTraceId": "3b4fc661-180d-4c2f-60c9-08da6e38dd10",
        "StartDate": "/Date(1658579297628)/",
        "EndDate": "/Date(1658752097628)/",
        "Index": 0
    }
    ```



=== "messagetrace2"


    ```json
	{
        "__metadata": {
            "id": "https://reports.office365.com/ecp/ReportingWebService/Reporting.svc/MessageTrace(5)",
            "uri": "https://reports.office365.com/ecp/ReportingWebService/Reporting.svc/MessageTrace(5)",
            "type": "TenantReporting.MessageTrace"
        },
        "Organization": "abc.onmicrosoft.com",
        "MessageId": "<123456@abc-prod2.mcc-soft.com>",
        "Received": "/Date(1661344992170)/",
        "SenderAddress": "support@abc.com",
        "RecipientAddress": "user@abc.fr",
        "Subject": null,
        "Status": "Delivered",
        "ToIP": null,
        "FromIP": null,
        "Size": 0,
        "MessageTraceId": "1203cd7a-18d5-4a92-4343-08da85ce34c9",
        "StartDate": "/Date(1661344937835)/",
        "EndDate": "/Date(1661344997835)/",
        "Index": 5
    }
    ```



