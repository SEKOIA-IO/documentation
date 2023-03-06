
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Anti-virus` | Vade performs behavioral-Based Anti-Malware |
| `Email gateway` | Vade for M365 blocks attacks from the first email thanks to machine learning models that perform real-time behavioral analysis of the entire email, including any URLs and attachments. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `email` |
| Type | `change`, `deletion`, `denied`, `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "email.json"

    ```json
	
    {
        "message": "{\"id\": \"zekfnzejnf576rge8768\", \"date\": \"2022-02-10T13:00:05.454Z\", \"sender_ip\": \"192.168.1.1\", \"from\": \"test@sekoia.io\", \"from_header\": \"<test@sekoia.io>\", \"to\": \"test@vadesecure.com\", \"to_header\": \"\\\"test@vadesecure.com\\\" <test@vadesecure.com>\", \"subject\": \"Lorem ipsum dolor\", \"message_id\": \"<01de2305-f75b-49db-8c61-f661bd498e63.protection.outlook.com>\", \"urls\": [{\"url\": \"https://sekoia.io\"}], \"attachments\": [{\"id\": \"ca9ph2ostndl7735uht0\", \"filename\": \"image001.png\", \"extension\": \"png\", \"size\": 12894},{\"id\": \"ca9okt0kn1e8usdf633g\", \"filename\": \"archive.zip\", \"extension\": \"zip\", \"size\": 10558}], \"status\": \"LEGIT\", \"substatus\": \"\", \"remediation_type\": \"none\", \"remediation_ids\": [], \"action\": \"NOTHING\", \"folder\": \"\", \"size\": 113475, \"current_events\": [], \"whitelisted\": false}",
        "event": {
            "category": "email",
            "kind": "event",
            "type": "info",
            "action": "nothing"
        },
        "email": {
            "local_id": "zekfnzejnf576rge8768",
            "message_id": "<01de2305-f75b-49db-8c61-f661bd498e63.protection.outlook.com>",
            "to": {
                "address": "test@vadesecure.com"
            },
            "from": {
                "address": "test@sekoia.io"
            },
            "subject": "Lorem ipsum dolor",
            "attachments": [
                {
                    "file": {
                        "name": "image001.png",
                        "size": 12894,
                        "extension": "png"
                    }
                },
                {
                    "file": {
                        "name": "archive.zip",
                        "size": 10558,
                        "extension": "zip"
                    }
                }
            ]
        },
        "source": {
            "ip": "192.168.1.1",
            "address": "192.168.1.1"
        },
        "vadesecure": {
            "from_header": "<test@sekoia.io>",
            "to_header": "\"test@vadesecure.com\" <test@vadesecure.com>",
            "status": "LEGIT",
            "attachments": [
                {
                    "filename": "image001.png",
                    "id": "ca9ph2ostndl7735uht0"
                },
                {
                    "filename": "archive.zip",
                    "id": "ca9okt0kn1e8usdf633g"
                }
            ]
        },
        "related": {
            "ip": [
                "192.168.1.1"
            ]
        }
    }
    	
	```


=== "remediation_auto.json"

    ```json
	
    {
        "message": "{\"id\": \"zekfnzejnf576rge8768\", \"date\": \"2022-02-01T23:30:33.982Z\", \"reason\": \"The email contains a URL that is flagged as Phishing by Vade Secure Global Threat Intelligence\", \"status\": {\"status\": \"PHISHING\"}, \"actions\": [{\"action\": \"MOVE\"}], \"nb_messages_remediated\": 1, \"nb_messages_remediated_read\": 0, \"nb_messages_remediated_unread\": 1}",
        "event": {
            "category": "email",
            "kind": "event",
            "type": "info",
            "reason": "The email contains a URL that is flagged as Phishing by Vade Secure Global Threat Intelligence"
        },
        "vadesecure": {
            "campaign": {
                "actions": [
                    {
                        "action": "MOVE"
                    }
                ],
                "id": "zekfnzejnf576rge8768",
                "nb_messages_remediated": 1,
                "nb_messages_remediated_read": 0,
                "nb_messages_remediated_unread": 1
            },
            "status": "PHISHING"
        }
    }
    	
	```


=== "remediation_manual.json"

    ```json
	
    {
        "message": "{\"id\": \"zekfnzejnf576rge8768\", \"date\": \"2021-11-18T15:59:39.368Z\", \"reason\": \"\", \"actions\": [{\"action\": \"DELETE\"}, {\"action\": \"FAILED\"}], \"nb_messages_remediated\": 76, \"nb_messages_remediated_read\": 0, \"nb_messages_remediated_unread\": 76}",
        "event": {
            "category": "email",
            "kind": "event",
            "type": "info"
        },
        "vadesecure": {
            "campaign": {
                "actions": [
                    {
                        "action": "DELETE"
                    },
                    {
                        "action": "FAILED"
                    }
                ],
                "id": "zekfnzejnf576rge8768",
                "nb_messages_remediated": 76,
                "nb_messages_remediated_read": 0,
                "nb_messages_remediated_unread": 76
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`email.attachments` | `array` | email.attachments |
|`email.from.address` | `keyword` | email.from.address |
|`email.local_id` | `keyword` | email.local_id |
|`email.message_id` | `keyword` | email.message_id |
|`email.subject` | `keyword` | email.subject |
|`email.to.address` | `keyword` | email.to.address |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`source.ip` | `ip` | IP address of the source. |
|`vadesecure.attachments` | `array` | vadesecure.to_header |
|`vadesecure.campaign.actions` | `array` | The actions carried out for the remediation campaign. |
|`vadesecure.campaign.id` | `keyword` | The ID of the campaign |
|`vadesecure.campaign.nb_messages_remediated` | `long` | The total number of messages involved in the remediation. |
|`vadesecure.campaign.nb_messages_remediated_read` | `long` | The number of total read messages involved in the remediation. |
|`vadesecure.campaign.nb_messages_remediated_unread` | `long` | The number of total unread messages involved in the remediation. |
|`vadesecure.folder` | `keyword` | vadesecure.folder |
|`vadesecure.from_header` | `keyword` | vadesecure.from_header |
|`vadesecure.status` | `keyword` | vadesecure.status |
|`vadesecure.substatus` | `keyword` | vadesecure.substatus |
|`vadesecure.to_header` | `keyword` | vadesecure.to_header |

