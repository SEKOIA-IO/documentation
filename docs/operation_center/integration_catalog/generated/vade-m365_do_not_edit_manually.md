
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
        "event": {
            "outcome": "success",
            "category": "email",
            "kind": "event",
            "type": "info"
        },
        "message": " {\"id\": \"zekfnzejnf576rge8768\", \"date\": \"2022-02-10T13:00:05.454Z\", \"sender_ip\": \"192.168.1.1\", \"from\": \"test@sekoia.io\", \"from_header\": \"<test@sekoia.io>\", \"to\": \"test@vadesecure.com\", \"to_header\": \"\\\"test@vadesecure.com\\\" <test@vadesecure.com>\", \"subject\": \"Lorem ipsum dolor\", \"message_id\": \"<01de2305-f75b-49db-8c61-f661bd498e63.protection.outlook.com>\", \"urls\": [{\"url\": \"https://sekoia.io\"}], \"attachments\": [{\"id\": \"ca9ph2ostndl7735uht0\", \"filename\": \"image001.png\", \"extension\": \"png\", \"size\": 12894},{\"id\": \"ca9okt0kn1e8usdf633g\", \"filename\": \"archive.zip\", \"extension\": \"zip\", \"size\": 10558}], \"status\": \"LEGIT\", \"substatus\": \"\", \"remediation_type\": \"none\", \"remediation_ids\": [], \"action\": \"NOTHING\", \"folder\": \"\", \"size\": 113475, \"current_events\": [], \"whitelisted\": false} ",
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        },
        "email": {
            "from": {
                "address": "test@sekoia.io"
            },
            "local_id": "zekfnzejnf576rge8768",
            "message_id": "<01de2305-f75b-49db-8c61-f661bd498e63.protection.outlook.com>",
            "subject": "Lorem ipsum dolor",
            "to": {
                "address": "test@vadesecure.com"
            },
            "attachments": [
                {
                    "file": {
                        "extension": "png",
                        "name": "image001.png",
                        "size": 12894
                    }
                },
                {
                    "file": {
                        "extension": "zip",
                        "name": "archive.zip",
                        "size": 10558
                    }
                }
            ]
        },
        "source": {
            "address": "192.168.1.1",
            "ip": "192.168.1.1"
        },
        "vadesecure": {
            "from_header": "<test@sekoia.io>",
            "status": "LEGIT",
            "to_header": "\"test@vadesecure.com\" <test@vadesecure.com>",
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
        }
    }
    	
	```


=== "remediation_auto.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
            "category": "email",
            "kind": "event",
            "type": "info",
            "reason": "The email contains a URL that is flagged as Phishing by Vade Secure Global Threat Intelligence"
        },
        "vadesecure": {
            "status": "PHISHING",
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
            }
        }
    }
    	
	```


=== "remediation_manual.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
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
|`vadesecure.campaign.actions` | `array` | None |
|`vadesecure.campaign.id` | `keyword` | None |
|`vadesecure.campaign.nb_messages_remediated` | `long` | None |
|`vadesecure.campaign.nb_messages_remediated_read` | `long` | None |
|`vadesecure.campaign.nb_messages_remediated_unread` | `long` | None |
|`vadesecure.folder` | `keyword` | vadesecure.folder |
|`vadesecure.from_header` | `keyword` | vadesecure.from_header |
|`vadesecure.status` | `keyword` | vadesecure.status |
|`vadesecure.substatus` | `keyword` | vadesecure.substatus |
|`vadesecure.to_header` | `keyword` | vadesecure.to_header |

