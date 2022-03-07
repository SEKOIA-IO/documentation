
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Email gateway` | Retarus Email Security solution. |





In details, the following Table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event`, `alert` |
| Category | `malware`, `web` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "threat_pzd.json"

    ```json
	
    {
        "action": {
            "name": "THREAT",
            "outcome": "failure"
        },
        "destination": {
            "address": "retarus.de",
            "domain": "retarus.de",
            "registered_domain": "retarus.de",
            "top_level_domain": "de"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "malware",
            "kind": "alert",
            "type": "info"
        },
        "file": {
            "hash": {
                "sha256": "sha256"
            },
            "mimeType": "applicationx-dosexec"
        },
        "message": "{\"customer\": \"CuNo\", \"metaData\": {\"hashFunction\": \"sha256\", \"threatType\": \"VIRUS\", \"checksum\": \"6b84714d0fa8c77d846306f37f4f3135596d34e17dca4f84088195272fd\", \"mimeType\": \"applicationx-dosexec\", \"details\": \"EICAR-Test-File\"}, \"host\": \"events.retarus.com\", \"ts\": \"2018-10-16 14:58:56 +0200\", \"version\": \"1.0\", \"sourceIp\": \"xxx.xxx.xxx.xxx\", \"sender\": \"xxxxxx@retarus.de\", \"type\": \"PZD\", \"direction\": \"INBOUND\", \"recipient\": \"xxxxxxx@retarus.de\", \"mimeId\": \"<56168B42.xxxxxxx@retarus.net>\", \"status\": \"DETECTED\", \"class\": \"THREAT\", \"rmxId\": \"20181016-145852-xxxxxx-xxxxxx-0@mailin01\"}",
        "observer": {
            "hostname": "events.retarus.com",
            "version": "1.0"
        },
        "organization": {
            "id": "CuNo"
        },
        "related": {
            "hash": [
                "sha256"
            ],
            "hosts": [
                "events.retarus.com",
                "retarus.de"
            ],
            "ip": [
                "xxx.xxx.xxx.xxx"
            ]
        },
        "retarus": {
            "class": "THREAT",
            "email_direction": "INBOUND",
            "message_id": "20181016-145852-xxxxxx-xxxxxx-0@mailin01",
            "mime_message_id": "<56168B42.xxxxxxx@retarus.net>",
            "recipient": "xxxxxxx@retarus.de",
            "sender": "xxxxxx@retarus.de",
            "status": "DETECTED",
            "timestamp": "2018-10-16 14:58:56 +0200",
            "type": "PZD",
            "virus_name": "EICAR-Test-File"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "retarus-email-security",
                "dialect_uuid": "46fe3905-9e38-4fb2-be09-44d31626b694"
            }
        },
        "source": {
            "address": "retarus.de",
            "domain": "retarus.de",
            "ip": "xxx.xxx.xxx.xxx",
            "registered_domain": "retarus.de",
            "top_level_domain": "de"
        }
    }
    	
	```


=== "threat_multiscan.json"

    ```json
	
    {
        "action": {
            "name": "THREAT",
            "outcome": "failure"
        },
        "destination": {
            "address": "retarus.de",
            "domain": "retarus.de",
            "registered_domain": "retarus.de",
            "top_level_domain": "de"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "malware",
            "kind": "alert",
            "type": "info"
        },
        "message": "{\"customer\": \"CuNo\", \"metaData\": {\"details\": \"EICAR-AV-Test\"}, \"host\": \"events.retarus.com\", \"ts\": \"2018-10-16 14:58:43 +0200\", \"version\": \"1.0\", \"sourceIp\": \"xxx.xxx.xxx.xxx\", \"sender\": \"xxxxxxx@retarus.com\", \"type\": \"MultiScan\", \"direction\": \"OUTBOUND\", \"recipient\": \"xxxxxxx@retarus.de\", \"mimeId\": \"<5616dfeid.xxxxxxxxxx@retarus.net>\", \"status\": \"INFECTED\", \"class\": \"THREAT\", \"rmxId\": \"20181016-145842-xxxxxx-xxxxxx-0@mailin27\"}",
        "observer": {
            "hostname": "events.retarus.com",
            "version": "1.0"
        },
        "organization": {
            "id": "CuNo"
        },
        "related": {
            "hosts": [
                "retarus.com",
                "retarus.de",
                "events.retarus.com"
            ],
            "ip": [
                "xxx.xxx.xxx.xxx"
            ]
        },
        "retarus": {
            "class": "THREAT",
            "email_direction": "OUTBOUND",
            "message_id": "20181016-145842-xxxxxx-xxxxxx-0@mailin27",
            "mime_message_id": "<5616dfeid.xxxxxxxxxx@retarus.net>",
            "recipient": "xxxxxxx@retarus.de",
            "sender": "xxxxxxx@retarus.com",
            "status": "INFECTED",
            "timestamp": "2018-10-16 14:58:43 +0200",
            "type": "MultiScan",
            "virus_name": "EICAR-AV-Test"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "retarus-email-security",
                "dialect_uuid": "46fe3905-9e38-4fb2-be09-44d31626b694"
            }
        },
        "source": {
            "address": "retarus.com",
            "domain": "retarus.com",
            "ip": "xxx.xxx.xxx.xxx",
            "registered_domain": "retarus.com",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "threat_sandboxing.json"

    ```json
	
    {
        "action": {
            "name": "THREAT",
            "outcome": "failure"
        },
        "destination": {
            "address": "retarus.de",
            "domain": "retarus.de",
            "registered_domain": "retarus.de",
            "top_level_domain": "de"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "malware",
            "kind": "alert",
            "type": "info"
        },
        "file": {
            "hash": {
                "sha256": "sha256"
            }
        },
        "message": "{\"customer\": \"CuNo\", \"metaData\": {\"hashFunction\": \"sha256\", \"checksum\": \"cbfdedf25f7f04daf9d705548cf6b6546d66bc206ea1a166fff15ece9434\"}, \"host\": \"events.retarus.com\", \"ts\": \"2018-10-16 15:03:43 +0200\", \"version\": \"1.0\", \"sourceIp\": \"xxx.xxx.xxx.xxx\", \"sender\": \"xxxxxxx@retarus.com\", \"type\": \"Sandboxing\", \"direction\": \"INBOUND\", \"recipient\": \"xxxxxxx@retarus.de\", \"mimeId\": \"<37357C96.xxxxxxx@retarus.net>\", \"status\": \"SUSPICIOUS\", \"class\": \"THREAT\", \"rmxId\": \"20181016-145902-xxxxxx-0@mailin08\"}",
        "observer": {
            "hostname": "events.retarus.com",
            "version": "1.0"
        },
        "organization": {
            "id": "CuNo"
        },
        "related": {
            "hash": [
                "sha256"
            ],
            "hosts": [
                "retarus.de",
                "events.retarus.com",
                "retarus.com"
            ],
            "ip": [
                "xxx.xxx.xxx.xxx"
            ]
        },
        "retarus": {
            "class": "THREAT",
            "email_direction": "INBOUND",
            "message_id": "20181016-145902-xxxxxx-0@mailin08",
            "mime_message_id": "<37357C96.xxxxxxx@retarus.net>",
            "recipient": "xxxxxxx@retarus.de",
            "sender": "xxxxxxx@retarus.com",
            "status": "SUSPICIOUS",
            "timestamp": "2018-10-16 15:03:43 +0200",
            "type": "Sandboxing"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "retarus-email-security",
                "dialect_uuid": "46fe3905-9e38-4fb2-be09-44d31626b694"
            }
        },
        "source": {
            "address": "retarus.com",
            "domain": "retarus.com",
            "ip": "xxx.xxx.xxx.xxx",
            "registered_domain": "retarus.com",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "example1.json"

    ```json
	
    {
        "destination": {
            "address": "recipientdomain.fr",
            "domain": "recipientdomain.fr",
            "registered_domain": "recipientdomain.fr",
            "top_level_domain": "fr"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "message": "{\"class\": \"EVENT\", \"rmxId\": \"0001\", \"sourceIp\": \"1.1.1.1\", \"metaData\": {\"header\": {\"from\": \"sender <sender@senderdomain.fr>\", \"subject\": \"This is a subject\"}, \"transportEncryption\": {\"requested\": true, \"established\": true, \"protocol\": \"TLSv1.2\", \"cipherSuite\": \"ecdhe-ecdsa-aes128-gcm-sha256\"}}, \"recipient\": \"recipient@recipientdomain.fr\", \"mimeId\": \"<11111111>\", \"sender\": \"sender@senderdomain.fr\", \"version\": \"1.0\", \"customer\": \"1\", \"host\": \"host.fr\", \"subtype\": \"INCOMING\", \"type\": \"AAA\", \"ts\": \"2021-10-1 09:00:00 +0200\", \"direction\": \"OUTBOUND\", \"status\": \"ACCEPTED\"}",
        "observer": {
            "hostname": "host.fr",
            "version": "1.0"
        },
        "organization": {
            "id": "1"
        },
        "related": {
            "hosts": [
                "host.fr",
                "senderdomain.fr",
                "recipientdomain.fr"
            ],
            "ip": [
                "1.1.1.1"
            ]
        },
        "retarus": {
            "class": "EVENT",
            "email_direction": "OUTBOUND",
            "message_id": "0001",
            "mime_message_id": "<11111111>",
            "recipient": "recipient@recipientdomain.fr",
            "sender": "sender@senderdomain.fr",
            "status": "ACCEPTED",
            "timestamp": "2021-10-1 09:00:00 +0200",
            "type": "AAA"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "deep-visibility",
                "dialect_uuid": "cccccccc-cccc-bbbb-aaaa-fffffffffffff"
            }
        },
        "source": {
            "address": "senderdomain.fr",
            "domain": "senderdomain.fr",
            "ip": "1.1.1.1",
            "registered_domain": "senderdomain.fr",
            "top_level_domain": "fr"
        }
    }
    	
	```


=== "event.json"

    ```json
	
    {
        "action": {
            "name": "EVENT",
            "outcome": "success",
            "outcome_reason": "ACCEPTED"
        },
        "destination": {
            "address": "mail.com",
            "domain": "mail.com",
            "registered_domain": "mail.com",
            "top_level_domain": "com"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "kind": "event"
        },
        "message": "{\"direction\": \"OUTBOUND\", \"class\": \"EVENT\", \"version\": \"1.0\", \"type\": \"MTA\", \"ts\": \"2021-05-18 16:50:30 +0200\", \"host\": \"events.retarus.com\", \"customer\": \"45987FR\", \"metaData\": {}, \"sender\": \"utilisateur@mail.fr\", \"status\": \"ACCEPTED\", \"mimeId\": \"<d12b9brrfd3c89723ee5@STZE007.super.corp>\", \"rmxId\": \"20210518-32464-yvrfukcZEcd-0@out33.fg\", \"sourceIp\": \"255.255.255.1\", \"recipient\": \"recepient@mail.com\"}",
        "observer": {
            "hostname": "events.retarus.com",
            "version": "1.0"
        },
        "organization": {
            "id": "45987FR"
        },
        "related": {
            "hosts": [
                "mail.fr",
                "events.retarus.com",
                "mail.com"
            ],
            "ip": [
                "255.255.255.1"
            ]
        },
        "retarus": {
            "class": "EVENT",
            "email_direction": "OUTBOUND",
            "message_id": "20210518-32464-yvrfukcZEcd-0@out33.fg",
            "mime_message_id": "<d12b9brrfd3c89723ee5@STZE007.super.corp>",
            "recipient": "recepient@mail.com",
            "sender": "utilisateur@mail.fr",
            "status": "ACCEPTED",
            "timestamp": "2021-05-18 16:50:30 +0200",
            "type": "MTA"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "retarus-email-security",
                "dialect_uuid": "46fe3905-9e38-4fb2-be09-44d31626b694"
            }
        },
        "source": {
            "address": "mail.fr",
            "domain": "mail.fr",
            "ip": "255.255.255.1",
            "registered_domain": "mail.fr",
            "top_level_domain": "fr"
        }
    }
    	
	```


=== "threat_cx0.json"

    ```json
	
    {
        "action": {
            "name": "THREAT",
            "outcome": "failure"
        },
        "destination": {
            "address": "retarus.de",
            "domain": "retarus.de",
            "registered_domain": "retarus.de",
            "top_level_domain": "de"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "malware",
            "kind": "alert",
            "type": "info"
        },
        "message": "{\"customer\": \"CuNo\", \"metaData\": {}, \"host\": \"events.retarus.com\", \"ts\": \"2018-10-16 14:58:18 +0200\", \"version\": \"1.0\", \"sourceIp\": \"xxx.xxx.xxx.xxx\", \"sender\": \"xxxxxxx@retarus.com\", \"type\": \"CxO\", \"direction\": \"INBOUND\", \"recipient\": \"xxxxxxx@retarus.de\", \"mimeId\": \"<164D6G96.xxxxxxx@retarus.net>\", \"status\": \"DETECTED\", \"class\": \"THREAT\", \"rmxId\": \"20181016-145817-42ZFjPxxxxxx-0@mailin01\"}",
        "observer": {
            "hostname": "events.retarus.com",
            "version": "1.0"
        },
        "organization": {
            "id": "CuNo"
        },
        "related": {
            "hosts": [
                "retarus.com",
                "retarus.de",
                "events.retarus.com"
            ],
            "ip": [
                "xxx.xxx.xxx.xxx"
            ]
        },
        "retarus": {
            "class": "THREAT",
            "email_direction": "INBOUND",
            "message_id": "20181016-145817-42ZFjPxxxxxx-0@mailin01",
            "mime_message_id": "<164D6G96.xxxxxxx@retarus.net>",
            "recipient": "xxxxxxx@retarus.de",
            "sender": "xxxxxxx@retarus.com",
            "status": "DETECTED",
            "timestamp": "2018-10-16 14:58:18 +0200",
            "type": "CxO"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "retarus-email-security",
                "dialect_uuid": "46fe3905-9e38-4fb2-be09-44d31626b694"
            }
        },
        "source": {
            "address": "retarus.com",
            "domain": "retarus.com",
            "ip": "xxx.xxx.xxx.xxx",
            "registered_domain": "retarus.com",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "event_outbound.json"

    ```json
	
    {
        "action": {
            "name": "EVENT",
            "outcome": "success",
            "outcome_reason": "ACCEPTED"
        },
        "destination": {
            "address": "retarus.de",
            "domain": "retarus.de",
            "registered_domain": "retarus.de",
            "top_level_domain": "de"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "kind": "event"
        },
        "message": "{\"customer\": \"CuNo\",\"metaData\": {\"transportEncryption\": {\"requested\": true,\"established\": true,\"protocol\": \"TLSv1.2\",\"cipherSuite\": \"ECDHE-RSA-AES128-SHA256(128/128bits)\"},\"header\": {\"subject\": \"This is a test mail\",\"from\": \"sender@example.com\"}},\"host\": \"events.retarus.com\",\"ts\": \"2021-07-11 14:58:43 +0200\",\"version\": \"1.0\",\"sourceIp\": \"255.255.255.1\",\"sender\": \"xxxxxxx@retarus.com\",\"type\": \"MTA\",\"subtype\": \"INCOMING\",\"direction\": \"OUTBOUND\",\"recipient\": \"xxxxxxx@retarus.de\",\"mimeId\": \"<5616dfeid.xxxxxxxxxx@retarus.net>\",\"status\": \"ACCEPTED\",\"class\": \"EVENT\",\"rmxId\": \"20210711-145842-xxxxxx-xxxxxx-0@mailin27\"}",
        "observer": {
            "hostname": "events.retarus.com",
            "version": "1.0"
        },
        "organization": {
            "id": "CuNo"
        },
        "related": {
            "hosts": [
                "retarus.de",
                "retarus.com",
                "events.retarus.com"
            ],
            "ip": [
                "255.255.255.1"
            ]
        },
        "retarus": {
            "class": "EVENT",
            "email_direction": "OUTBOUND",
            "message_id": "20210711-145842-xxxxxx-xxxxxx-0@mailin27",
            "mime_message_id": "<5616dfeid.xxxxxxxxxx@retarus.net>",
            "recipient": "xxxxxxx@retarus.de",
            "sender": "xxxxxxx@retarus.com",
            "status": "ACCEPTED",
            "timestamp": "2021-07-11 14:58:43 +0200",
            "type": "MTA"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "retarus-email-security",
                "dialect_uuid": "46fe3905-9e38-4fb2-be09-44d31626b694"
            }
        },
        "source": {
            "address": "retarus.com",
            "domain": "retarus.com",
            "ip": "255.255.255.1",
            "registered_domain": "retarus.com",
            "top_level_domain": "com"
        }
    }
    	
	```


=== "event_inbound.json"

    ```json
	
    {
        "action": {
            "name": "EVENT",
            "outcome": "success",
            "outcome_reason": "ACCEPTED"
        },
        "destination": {
            "address": "retarus.de",
            "domain": "retarus.de",
            "registered_domain": "retarus.de",
            "top_level_domain": "de"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "kind": "event"
        },
        "message": "{\"customer\": \"CuNo\",\"metaData\": {\"authentication\": {\"dkim\": {\"status\": \"dkim=none\",\"details\": \"dkim=none reason=\\\"no signature\\\"\"}},\"transportEncryption\": {\"requested\": false,\"established\": false},\"header\": {\"subject\": \"This is a test mail\",\"from\": \"sender@example.com\"},\"contentEncryption\": false},\"host\": \"events.retarus.com\",\"ts\": \"2021-07-11 14:58:43 +0200\",\"version\": \"1.0\",\"sourceIp\": \"xxx.xxx.xxx.xxx\",\"sender\": \"xxxxxxx@retarus.com\",\"type\": \"MTA\",\"subtype\": \"INCOMING\",\"direction\": \"INBOUND\",\"recipient\": \"xxxxxxx@retarus.de\",\"mimeId\": \"<5616dfeid.xxxxxxxxxx@retarus.net>\",\"status\": \"ACCEPTED\",\"class\": \"EVENT\",\"rmxId\": \"20210711-145842-xxxxxx-xxxxxx-0@mailin27\"}",
        "observer": {
            "hostname": "events.retarus.com",
            "version": "1.0"
        },
        "organization": {
            "id": "CuNo"
        },
        "related": {
            "hosts": [
                "events.retarus.com",
                "retarus.com",
                "retarus.de"
            ],
            "ip": [
                "xxx.xxx.xxx.xxx"
            ]
        },
        "retarus": {
            "class": "EVENT",
            "email_direction": "INBOUND",
            "message_id": "20210711-145842-xxxxxx-xxxxxx-0@mailin27",
            "mime_message_id": "<5616dfeid.xxxxxxxxxx@retarus.net>",
            "recipient": "xxxxxxx@retarus.de",
            "sender": "xxxxxxx@retarus.com",
            "status": "ACCEPTED",
            "timestamp": "2021-07-11 14:58:43 +0200",
            "type": "MTA"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "retarus-email-security",
                "dialect_uuid": "46fe3905-9e38-4fb2-be09-44d31626b694"
            }
        },
        "source": {
            "address": "retarus.com",
            "domain": "retarus.com",
            "ip": "xxx.xxx.xxx.xxx",
            "registered_domain": "retarus.com",
            "top_level_domain": "com"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.domain` | `keyword` | The domain name of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.hash.sha1` | `keyword` | SHA1 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.hash.sha512` | `keyword` | SHA512 hash. |
|`file.hash.ssdeep` | `keyword` | SSDEEP hash. |
|`file.mimeType` | `keyword` | None |
|`observer.hostname` | `keyword` | Hostname of the observer. |
|`observer.version` | `keyword` | Observer version. |
|`organization.id` | `keyword` | Unique identifier for the organization. |
|`retarus.class` | `keyword` | None |
|`retarus.email_direction` | `keyword` | None |
|`retarus.message_id` | `keyword` | None |
|`retarus.mime_message_id` | `keyword` | None |
|`retarus.phishing_identifier` | `long` | None |
|`retarus.recipient` | `keyword` | None |
|`retarus.sender` | `keyword` | None |
|`retarus.status` | `keyword` | None |
|`retarus.timestamp` | `keyword` | None |
|`retarus.type` | `keyword` | None |
|`retarus.virus_name` | `keyword` | None |
|`source.domain` | `keyword` | The domain name of the source. |
|`source.ip` | `ip` | IP address of the source. |
|`url.full` | `wildcard` | Full unparsed URL. |

