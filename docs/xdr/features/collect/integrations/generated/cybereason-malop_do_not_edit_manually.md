
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | CybeReason MalOps platform provides activities of MalOps |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "malop_connection.json"

    ```json
	
    {
        "@timestamp": "2021-08-20T22:53:27.043000Z",
        "message": "CEF:0|Cybereason|Cybereason|1.0|5|Malop Connection Added|5|CybereasonCEFgeneratorBatchId1=58bc2665-b22f-4345-bd90-3f84be47c8b6 cs1=11.1323449861766643222 CybereasonCEFgeneratorcountry1Name=None dst=3.226.77.3 dpt=443 rt=1629500007043 cs1Label=MalopId",
        "observer": {
            "vendor": "Cybereason",
            "product": "Cybereason",
            "version": "1.0"
        },
        "destination": {
            "ip": "3.226.77.3",
            "port": 443
        },
        "event": {
            "severity": 5,
            "code": "5",
            "kind": "event",
            "type": "info",
            "category": [
                "session"
            ],
            "action": "Malop Connection Added"
        },
        "cybereason": {
            "event": {
                "id": "58bc2665-b22f-4345-bd90-3f84be47c8b6"
            },
            "malop": {
                "id": "11.1323449861766643222"
            },
            "cef": {
                "version": "0"
            }
        }
    }
    	
	```


=== "malop_created.json"

    ```json
	
    {
        "@timestamp": "2021-08-23T06:53:42.409000Z",
        "message": "CEF:0|Cybereason|Cybereason|1.0|1|Malop Created|5|rt=1629701622409 deviceCustomDate1=1636629776184 deviceFacility=Under Investigation CybereasonCEFgeneratorBatchId1=078e369b-ea4e-4e98-bc0d-ee71fd40d19d cs1=11.4718101284717793977 cs2=EXTENSION_MANIPULATION cs3=MALICIOUS_INFECTION cs5=maliciousByDualExtensionByFileRootCause cn1=1 cs6=https://yourserver.cybereason.net:8443//#/malop/11.4718101284717793977 cn2=1 cs4=bb9dbdca921d84381c893086f65ffca17120b23d requestContext=flashget3.7.0.1220en.pdf.exe, which has an unknown reputation, has dual extensions, which is hiding the true nature of the process. cs1Label=MalopId cs2Label=MalopDetectionType cs3Label=MalopActivityType cs4Label=MalopHashList cs5Label=DecisionFeatures cs6Label=IncidentLink cn1Label=AffectedMachinesCount cn2Label=AffectedUsersCount cn3Label=isSigned deviceCustomDate1Label=ModifiedTime",
        "observer": {
            "vendor": "Cybereason",
            "product": "Cybereason",
            "version": "1.0"
        },
        "event": {
            "severity": 5,
            "code": "1",
            "kind": "alert",
            "type": "info",
            "category": [
                "malware"
            ],
            "action": "Malop Created",
            "reason": "flashget3.7.0.1220en.pdf.exe, which has an unknown reputation, has dual extensions, which is hiding the true nature of the process.",
            "url": "https://yourserver.cybereason.net:8443//#/malop/11.4718101284717793977"
        },
        "file": {
            "hash": {
                "sha1": "bb9dbdca921d84381c893086f65ffca17120b23d"
            }
        },
        "cybereason": {
            "event": {
                "id": "078e369b-ea4e-4e98-bc0d-ee71fd40d19d"
            },
            "malop": {
                "id": "11.4718101284717793977",
                "status": "Under Investigation",
                "modified_at": "2021-11-11T11:22:56.184000Z",
                "detection": {
                    "type": "EXTENSION_MANIPULATION"
                },
                "activity": {
                    "type": "MALICIOUS_INFECTION"
                },
                "decision": "maliciousByDualExtensionByFileRootCause",
                "counters": {
                    "affected_machines": 1,
                    "affected_users": 1
                }
            },
            "cef": {
                "version": "0"
            }
        }
    }
    	
	```


=== "malop_machine.json"

    ```json
	
    {
        "@timestamp": "2021-07-08T12:48:29.151000Z",
        "message": "CEF:0|Cybereason|Cybereason|1.0|3|Malop Machine Added|5|destinationDnsDomain=desktop-aas6kq7 dst=10.0.2.15 destinationTranslatedAddress=117.99.232.147 CybereasonCEFgeneratorBatchId1=2ac124fd-def2-4073-b408-d3b3f0e764b0 cs1=11.-6654920844431693523 flexString2=True dhost=desktop-aas6kq7 CybereasonCEFgeneratorOSandVersion1=Windows_10 CybereasonCEFgeneratorMachineGuid1=-592942600.1198775089551518743 cfp3=1 rt=1625748509151 cfp2=1 cs1Label=MalopId flexString2Label=isMalicious cfp2Label=isOnline cfp3Label=isOriginalMachine request=\"C:\\\\Users\\\\chand\\\\Downloads\\\\BT_21.40.5_32_Win7.pdf.exe\" deviceProcessName=explorer.exe CybereasonCEFgeneratorChildProcess1=None",
        "observer": {
            "vendor": "Cybereason",
            "product": "Cybereason",
            "version": "1.0"
        },
        "event": {
            "severity": 5,
            "code": "3",
            "kind": "event",
            "type": "info",
            "category": [
                "intrusion_detection"
            ],
            "action": "Malop Machine Added"
        },
        "destination": {
            "ip": "10.0.2.15",
            "nat": {
                "ip": "117.99.232.147"
            }
        },
        "host": {
            "hostname": "desktop-aas6kq7",
            "ip": [
                "10.0.2.15",
                "117.99.232.147"
            ],
            "id": "-592942600.1198775089551518743",
            "os": {
                "full": "Windows 10"
            }
        },
        "process": {
            "command_line": "C:\\Users\\chand\\Downloads\\BT_21.40.5_32_Win7.pdf.exe",
            "parent": {
                "name": "explorer.exe"
            }
        },
        "cybereason": {
            "event": {
                "id": "2ac124fd-def2-4073-b408-d3b3f0e764b0"
            },
            "malop": {
                "id": "11.-6654920844431693523",
                "host": {
                    "is_online": true,
                    "is_malicious": true,
                    "is_original_machine": true
                }
            },
            "cef": {
                "version": "0"
            }
        }
    }
    	
	```


=== "malop_process_added.json"

    ```json
	
    {
        "@timestamp": "2021-08-23T06:38:02.928000Z",
        "message": "CEF:0|Cybereason|Cybereason|1.0|2|Malop Process Added|5|CybereasonCEFgeneratorBatchId1=2ac124fd-def2-4073-b408-d3b3f0e764b0 cs1=11.-6654920844431693523 cs4=76030baf8e80653b883474f56c06164c33417ece request=\"C:\\\\Users\\\\chand\\\\Downloads\\\\BT_21.40.5_32_Win7.pdf.exe\" flexString2=True cn3=1 reason=indifferent rt=1629700682928 cs1Label=MalopId flexString2Label=isMalicious cs4Label=processSha1 cn3Label=isSigned",
        "observer": {
            "vendor": "Cybereason",
            "product": "Cybereason",
            "version": "1.0"
        },
        "event": {
            "severity": 5,
            "code": "2",
            "kind": "event",
            "type": "info",
            "category": [
                "intrusion_detection"
            ],
            "action": "Malop Process Added"
        },
        "file": {
            "hash": {
                "sha1": "76030baf8e80653b883474f56c06164c33417ece"
            }
        },
        "process": {
            "command_line": "C:\\Users\\chand\\Downloads\\BT_21.40.5_32_Win7.pdf.exe",
            "start": "2021-08-23T06:38:02.928000Z"
        },
        "cybereason": {
            "event": {
                "id": "2ac124fd-def2-4073-b408-d3b3f0e764b0"
            },
            "malop": {
                "id": "11.-6654920844431693523",
                "host": {
                    "is_malicious": true
                },
                "file": {
                    "is_signed": true
                }
            },
            "cef": {
                "version": "0"
            }
        }
    }
    	
	```


=== "malop_user.json"

    ```json
	
    {
        "message": "CEF:0|Cybereason|Cybereason|1.0|6|Malop User Added|5|CybereasonCEFgeneratorBatchId1=2ac124fd-def2-4073-b408-d3b3f0e764b0 cs1=11.-6654920844431693523 dpriv=None dhost=desktop-aas6kq7 CybereasonCEFgeneratorOrganizationName1=INTEGRATION duser=system cs1Label=MalopId",
        "observer": {
            "vendor": "Cybereason",
            "product": "Cybereason",
            "version": "1.0"
        },
        "event": {
            "severity": 5,
            "code": "6",
            "kind": "event",
            "type": "info",
            "category": [
                "intrusion_detection"
            ],
            "action": "Malop User Added"
        },
        "user": {
            "name": "system",
            "domain": "INTEGRATION"
        },
        "host": {
            "hostname": "desktop-aas6kq7"
        },
        "cybereason": {
            "event": {
                "id": "2ac124fd-def2-4073-b408-d3b3f0e764b0"
            },
            "malop": {
                "id": "11.-6654920844431693523"
            },
            "cef": {
                "version": "0"
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cybereason.cef.version` | `keyword` | None |
|`cybereason.event.id` | `keyword` | None |
|`cybereason.malop.activity.type` | `keyword` | None |
|`cybereason.malop.counters.affected_machines` | `float` | None |
|`cybereason.malop.counters.affected_users` | `float` | None |
|`cybereason.malop.decision` | `text` | None |
|`cybereason.malop.detection.type` | `keyword` | None |
|`cybereason.malop.file.is_signed` | `boolean` | None |
|`cybereason.malop.host.is_malicious` | `boolean` | None |
|`cybereason.malop.host.is_online` | `boolean` | None |
|`cybereason.malop.host.is_original_machine` | `boolean` | None |
|`cybereason.malop.id` | `keyword` | None |
|`cybereason.malop.modified_at` | `text` | None |
|`cybereason.malop.status` | `keyword` | None |
|`destination.geo.country_name` | `keyword` | Country name. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.nat.ip` | `ip` | Destination NAT ip |
|`destination.port` | `long` | Port of the destination. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.severity` | `long` | Numeric severity of the event. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`event.url` | `keyword` | Event investigation URL |
|`file.hash.sha1` | `keyword` | SHA1 hash. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.id` | `keyword` | Unique host id. |
|`host.ip` | `ip` | Host ip addresses. |
|`host.os.full` | `keyword` | Operating system name, including the version or code name. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`observer.version` | `keyword` | Observer version. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.name` | `keyword` | Process name. |
|`process.parent.name` | `keyword` | Process name. |
|`process.start` | `date` | The time the process started. |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.name` | `keyword` | Short name or login of the user. |

