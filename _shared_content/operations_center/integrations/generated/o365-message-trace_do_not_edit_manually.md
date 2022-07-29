
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Mail server` | Message trace follows email messages as they travel through your Exchange Online organization. |
| `Email gateway` | Message trace follows email messages as they travel through your Exchange Online organization. |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "messagetrace.json"

    ```json
	
    {
        "event": {
            "start": "2022-07-23T12:28:17.628000Z",
            "end": "2022-07-25T12:28:17.628000Z",
            "outcome": "success"
        },
        "office365": {
            "message_trace": {
                "MessageTraceId": "3b4fc661-180d-4c2f-60c9-08da6e38dd10",
                "Size": 87680,
                "Status": "GettingStatus"
            }
        },
        "email": {
            "delivery_timestamp": "2022-07-25T12:28:17.628000Z",
            "message_id": "<3a273efc-cd65-4335-96ec-5f6934f0fb10@az.uksouth.production.microsoft.com>",
            "from": {
                "address": "azure-noreply@microsoft.com"
            },
            "to": {
                "address": "foo.bar@example.corp"
            },
            "subject": "PIM: MessageTrace API service account has the Privileged Role Administrator role"
        },
        "source": {
            "ip": "1.1.1.1",
            "address": "1.1.1.1"
        },
        "organization": {
            "name": "examplecorp.onmicrosoft.com"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`email.delivery_timestamp` | `keyword` | None |
|`email.from.address` | `keyword` | None |
|`email.message_id` | `keyword` | None |
|`email.subject` | `keyword` | None |
|`email.to.address` | `keyword` | None |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`office365.message_trace.MessageTraceId` | `keyword` | None |
|`office365.message_trace.Size` | `number` | None |
|`office365.message_trace.Status` | `keyword` | None |
|`organization.name` | `keyword` | Organization name. |
|`source.ip` | `ip` | IP address of the source. |

