
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
        "MessageId": "<user53780@example.com>",
        "Received": "/Date(1658751973240)/",
        "SenderAddress": "user1752@example.com",
        "RecipientAddress": "user30544@example.com",
        "Subject": "PIM: MessageTrace API service account has the Privileged Role Administrator role",
        "Status": "GettingStatus",
        "ToIP": null,
        "FromIP": "198.51.100.39",
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
        "MessageId": "<user65566@example.com>",
        "Received": "/Date(1661344992170)/",
        "SenderAddress": "user75576@example.com",
        "RecipientAddress": "user29346@example.com",
        "Subject": null,
        "Status": "Delivered",
        "ToIP": null,
        "FromIP": null,
        "Size": 0,
        "MessageTraceId": "9e628ee5-39be-405f-9c3e-32f6cdd7b4d4",
        "StartDate": "/Date(1661344937835)/",
        "EndDate": "/Date(1661344997835)/",
        "Index": 5
    }
    ```



