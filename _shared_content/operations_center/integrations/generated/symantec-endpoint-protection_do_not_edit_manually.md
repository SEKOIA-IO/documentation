
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Anti-virus` | Symantec Endpoint Protection analyses processes and files to prevent malicious actions. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `malware` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "test_sonar.json"

    ```json
	
    {
        "message": "SONAR detection now allowed,IP Address: 1.2.3.4,Computer name: DNHFF3453,Source: Auto-Protect scan,Risk name: WS.Reputation.1,Occurrences: 1,File path: c:\\program files (x86)\\visualxxxxxxxxxx\\vtomxvision.exe,Description: ,Actual action: Action invalid,Requested action: Process terminate pending restart,Secondary action: 102,Event time: 2022-07-07 17:01:05,Event Insert Time: 2022-07-07 17:24:14,End Time: 2022-07-07 17:01:05,Last update time: 2022-07-07 17:24:14,Domain Name: MyDomain,Group Name: MyDomain\\Subdivision\\Citrix VDI persistants,Server Name: XXXXX01,User Name: Doe,Source Computer Name: ,Source Computer IP: ,Disposition: Good,Download site: ,Web domain: ,Downloaded by: c:/windows/explorer.exe,Prevalence: This file has been seen by fewer than 50 Symantec users.,Confidence: There is some evidence that this file is trustworthy.,URL Tracking Status: On,First Seen: Symantec has known about this file approximately 2 days.,Sensitivity: ,Allowed application reason: User allow list,Application hash: E13D72DE479A65E6448C779B3B2BCE45DB7B5AE52B1BAA0FE915380A667D3C01,Hash type: SHA2,Company name: Absyss S.A.S,Application name: Visual TOM,Application version: 6.6.1 (FR),Application type: 127,File size (bytes): 67352,Category set: Malware,Category type: Insight Network Threat,Location: MyDomain,Intensive Protection Level: 0,Certificate issuer: Absyss,Certificate signer: Sectigo RSA Code Signing CA,Certificate thumbprint: D31433F4C8C0BE4846E7E90318CD0CF5046EE95C,Signing timestamp: 1649155201,Certificate serial number: 044541E287C90A879334BFD15D6A3ED3",
        "event": {
            "reason": "SONAR detection now allowed",
            "kind": "event",
            "category": [
                "malware"
            ],
            "type": [
                "info"
            ],
            "action": "Process terminate pending restart"
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "ip": [
                "1.2.3.4"
            ],
            "hostname": "DNHFF3453",
            "name": "DNHFF3453"
        },
        "user": {
            "name": "Doe"
        },
        "related": {
            "hosts": [
                "DNHFF3453"
            ],
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "Doe"
            ]
        },
        "threat": {
            "enrichments": [
                {
                    "indicator": {
                        "type": "file",
                        "first_seen": "2022-07-07T17:01:05.000000Z",
                        "last_seen": "2022-07-07T17:01:05.000000Z",
                        "modified_at": "2022-07-07T17:24:14.000000Z",
                        "sightings": 1,
                        "description": "WS.Reputation.1",
                        "file": {
                            "path": "c:\\program files (x86)\\visualxxxxxxxxxx\\vtomxvision.exe",
                            "size": 67352
                        }
                    }
                }
            ]
        },
        "file": {
            "path": "c:\\program files (x86)\\visualxxxxxxxxxx\\vtomxvision.exe",
            "size": 67352
        },
        "broadcom": {
            "endpoint_protection": {
                "source": "Auto-Protect scan",
                "server": {
                    "domain": "MyDomain",
                    "group": "MyDomain\\Subdivision\\Citrix VDI persistants",
                    "name": "XXXXX01"
                },
                "threat": {
                    "type": "Insight Network Threat",
                    "category": "Malware"
                },
                "application": {
                    "code_signature": {
                        "digest_algorithm": "sha2",
                        "subject_name": "Absyss",
                        "signer": "Sectigo RSA Code Signing CA",
                        "timestamp": "2022-04-05T10:40:01.000000Z",
                        "certificate": {
                            "thumbprint": "D31433F4C8C0BE4846E7E90318CD0CF5046EE95C",
                            "serial_number": "044541E287C90A879334BFD15D6A3ED3"
                        }
                    },
                    "hash": {
                        "sha2": "E13D72DE479A65E6448C779B3B2BCE45DB7B5AE52B1BAA0FE915380A667D3C01"
                    },
                    "name": "Visual TOM",
                    "version": "6.6.1 (FR)"
                },
                "downloaded_by": {
                    "file": {
                        "path": "c:/windows/explorer.exe"
                    }
                },
                "action": {
                    "main": "Action invalid",
                    "secondary": "102"
                },
                "prevalence": "This file has been seen by fewer than 50 Symantec users.",
                "confidence": "There is some evidence that this file is trustworthy."
            }
        }
    }
    	
	```


=== "test_virus_found.json"

    ```json
	
    {
        "message": "Virus found,IP Address: 1.2.3.4,Computer name: DNHFF3453,Source: Auto-Protect scan,Risk name: EICAR Test String,Occurrences: 1,File path: C:\\Users\\admin\\Desktop\\test.txt,Description: AP realtime deferred scanning,Actual action: Cleaned by deletion,Requested action: Cleaned,Secondary action: Quarantined,Event time: 2022-07-07 14:28:39,Event Insert Time: 2022-07-07 14:30:43,End Time: 2022-07-07 14:28:39,Last update time: 2022-07-07 14:30:43,Domain Name: MyDomain,Group Name: MyDomain\\Subdivision\\Citrix VDI persistants,Server Name: XXXXX01,User Name: ADMIN,Source Computer Name: ,Source Computer IP: ,Disposition: Bad,Download site: ,Web domain: ,Downloaded by: ,Prevalence: This file has been seen by millions of Symantec users.,Confidence: This file is untrustworthy.,URL Tracking Status: On,First Seen: Reputation was not used in this detection.,Sensitivity: ,Allowed application reason: Not on the allow list,Application hash: 275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F,Hash type: SHA2,Company name: ,Application name: Nouveau document texte.txt,Application version: ,Application type: 127,File size (bytes): 68,Category set: Malware,Category type: Virus,Location: MyDomain,Intensive Protection Level: 0,Certificate issuer: ,Certificate signer: ,Certificate thumbprint: ,Signing timestamp: ,Certificate serial number: ",
        "event": {
            "reason": "Virus found",
            "kind": "event",
            "category": [
                "malware"
            ],
            "type": [
                "info"
            ],
            "action": "Cleaned"
        },
        "observer": {
            "vendor": "Broadcom",
            "product": "Symantec Endpoint Protection"
        },
        "host": {
            "ip": [
                "1.2.3.4"
            ],
            "hostname": "DNHFF3453",
            "name": "DNHFF3453"
        },
        "user": {
            "name": "ADMIN"
        },
        "related": {
            "hosts": [
                "DNHFF3453"
            ],
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ADMIN"
            ]
        },
        "threat": {
            "enrichments": [
                {
                    "indicator": {
                        "type": "file",
                        "first_seen": "2022-07-07T14:28:39.000000Z",
                        "last_seen": "2022-07-07T14:28:39.000000Z",
                        "modified_at": "2022-07-07T14:30:43.000000Z",
                        "sightings": 1,
                        "description": "EICAR Test String",
                        "file": {
                            "path": "C:\\Users\\admin\\Desktop\\test.txt",
                            "size": 68
                        }
                    }
                }
            ]
        },
        "file": {
            "path": "C:\\Users\\admin\\Desktop\\test.txt",
            "size": 68
        },
        "broadcom": {
            "endpoint_protection": {
                "source": "Auto-Protect scan",
                "server": {
                    "domain": "MyDomain",
                    "group": "MyDomain\\Subdivision\\Citrix VDI persistants",
                    "name": "XXXXX01"
                },
                "threat": {
                    "type": "Virus",
                    "category": "Malware"
                },
                "application": {
                    "code_signature": {
                        "digest_algorithm": "sha2"
                    },
                    "hash": {
                        "sha2": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F"
                    },
                    "name": "Nouveau document texte.txt"
                },
                "action": {
                    "main": "Cleaned by deletion",
                    "secondary": "Quarantined"
                },
                "prevalence": "This file has been seen by millions of Symantec users.",
                "confidence": "This file is untrustworthy."
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`broadcom.endpoint_protection.action.main` | `keyword` |  |
|`broadcom.endpoint_protection.action.secondary` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.certificate.serial_number` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.certificate.thumbprint` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.digest_algorithm` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.signer` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.subject_name` | `keyword` |  |
|`broadcom.endpoint_protection.application.code_signature.timestamp` | `keyword` |  |
|`broadcom.endpoint_protection.application.hash.sha2` | `keyword` |  |
|`broadcom.endpoint_protection.application.name` | `keyword` |  |
|`broadcom.endpoint_protection.application.version` | `keyword` |  |
|`broadcom.endpoint_protection.confidence` | `keyword` |  |
|`broadcom.endpoint_protection.downloaded_by.file.path` | `keyword` |  |
|`broadcom.endpoint_protection.prevalence` | `keyword` |  |
|`broadcom.endpoint_protection.server.domain` | `keyword` |  |
|`broadcom.endpoint_protection.server.group` | `keyword` |  |
|`broadcom.endpoint_protection.server.name` | `keyword` |  |
|`broadcom.endpoint_protection.source` | `keyword` |  |
|`broadcom.endpoint_protection.threat.category` | `keyword` |  |
|`broadcom.endpoint_protection.threat.type` | `keyword` |  |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`file.size` | `long` | File size in bytes. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.ip` | `ip` | Host ip addresses. |
|`host.name` | `keyword` | Name of the host. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`threat.enrichments` | `array` |  |
|`user.name` | `keyword` | Short name or login of the user. |

