
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | activites performed on SentinelOne infrastructure are logged |





In details, the following Table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `alert`, `event` |
| Category | `host`, `intrusion_detection`, `malware` |
| Type | `allowed`, `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "activities.json"

    ```json
	
    {
        "event": {
            "action": "Agent started full disk scan",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "hash": "59ae1c109a0426a55e76ef030a2eea2e73ff6ce1",
            "id": "1109290868249950294",
            "kind": "event",
            "original": "1sjze813YtXlmgHp3a1jU4rOAwYpBKMFaWtYCeTQ0QhEtg36Z68bcNi4ahZ2G7Fz",
            "outcome": "success",
            "reason": "Agent debian-SentinelOne started full disk scan at Thu, 11 Mar 2021, 12:42:56 UTC.",
            "type": "info"
        },
        "group": {
            "id": "1107851598374945694",
            "name": "Default Group"
        },
        "organization": {
            "id": "617755838952421242",
            "name": "CORP"
        },
        "action": {
            "type": 90
        },
        "host": {
            "name": "debian-SentinelOne"
        },
        "agent": {
            "id": "1109290742018175361"
        },
        "sentinelone": {
            "eventid": 1109290868249950294,
            "data": {
                "fullScopeDetails": "Group Default Group in Site Sekoia.io of Account CORP",
                "accountName": "CORP",
                "groupName": "Default Group",
                "scopeLevel": "Group",
                "scopeName": "Default Group",
                "siteName": "Sekoia.io",
                "status": "started"
            },
            "siteId": "1107851598358168475",
            "sitename": "Sekoia.io",
            "updatedAt": "2021-03-11T12:42:56.301271Z"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "activities2.json"

    ```json
	
    {
        "event": {
            "category": "host",
            "id": "1387019684138751044",
            "kind": "event",
            "outcome": "success",
            "reason": "USB device  was connected on CORP123.",
            "type": "allowed"
        },
        "group": {
            "id": "1083054176758610128"
        },
        "organization": {
            "id": "123456789831564686"
        },
        "rule": {
            "id": "-1"
        },
        "action": {
            "type": 5126
        },
        "agent": {
            "id": "1098352279374896038"
        },
        "host": {
            "name": "CORP123"
        },
        "sentinelone": {
            "eventid": 1387019684138751044,
            "data": {
                "accountName": "CORP",
                "deviceClass": "E0h",
                "fullScopeDetails": "Group Default Group in Site CORP-Users of Account CORP",
                "groupName": "Default Group",
                "interface": "USB",
                "lmpVersion": "N/A",
                "productId": "AAA",
                "profileUuids": "N/A",
                "ruleType": "productId",
                "scopeLevel": "Group",
                "scopeName": "Default Group",
                "siteName": "CORP-Users",
                "vendorId": 8087,
                "version": "N/A"
            },
            "siteId": "1083054176741832911",
            "updatedAt": "2022-03-29T17:20:30.998054Z"
        }
    }
    	
	```


=== "custom_rule.json"

    ```json
	
    {
        "message": "{\"accountId\": \"901144152444038278\", \"activityType\": 3608, \"agentId\": \"1183145065000215213\", \"agentUpdatedVersion\": null, \"applications\": null, \"comments\": null, \"createdAt\": \"2021-11-16T15:29:38.431997Z\", \"data\": {\"accountName\": \"CORP\", \"alertId\": 1290568698312097725, \"alertid\": 1290568698312097725, \"detectedat\": 1637076565467, \"dveventid\": \"\", \"dveventtype\": \"BEHAVIORALINDICATORS\", \"fullScopeDetails\": \"Group LAPTOP in Site DEFAULT of Account CORP\", \"groupName\": \"LAPTOP\", \"k8sclustername\": \"\", \"k8scontainerid\": \"\", \"k8scontainerimage\": \"\", \"k8scontainerlabels\": \"\", \"k8scontainername\": \"\", \"k8scontrollerkind\": \"\", \"k8scontrollerlabels\": \"\", \"k8scontrollername\": \"\", \"k8snamespace\": \"\", \"k8snamespacelabels\": \"\", \"k8snode\": \"\", \"k8spod\": \"\", \"k8spodlabels\": \"\", \"origagentmachinetype\": \"laptop\", \"origagentname\": \"CORP-LAP-4075\", \"origagentosfamily\": \"windows\", \"origagentosname\": \"Windows 10 Pro\", \"origagentosrevision\": \"19042\", \"origagentsiteid\": \"901144152460815495\", \"origagentuuid\": \"058fd4868adb4b87be24a4c5e9f89220\", \"origagentversion\": \"4.6.14.304\", \"ruleId\": 1259119070812474070, \"ruledescription\": \"Rule migrated from Watchlist\", \"ruleid\": 1259119070812474070, \"rulename\": \"PowershellExecutionPolicyChanged Indicator Monito\", \"rulescopeid\": 901144152460815495, \"rulescopelevel\": \"E_SITE\", \"scopeId\": 901144152460815495, \"scopeLevel\": \"Group\", \"scopeName\": \"LAPTOP\", \"severity\": \"E_MEDIUM\", \"siteName\": \"DEFAULT\", \"sourcename\": \"STAR\", \"sourceparentprocesscommandline\": \"C:\\\\WINDOWS\\\\Explorer.EXE\", \"sourceparentprocessintegritylevel\": \"medium\", \"sourceparentprocesskey\": \"811577BA383803B5\", \"sourceparentprocessmd5\": \"681a21a3b848ed960073475cd77634ce\", \"sourceparentprocessname\": \"explorer.exe\", \"sourceparentprocesspath\": \"C:\\\\WINDOWS\\\\explorer.exe\", \"sourceparentprocesspid\": 11196, \"sourceparentprocesssha1\": \"3d930943fbea03c9330c4947e5749ed9ceed528a\", \"sourceparentprocesssha256\": \"08d3f16dfbb5b5d7b419376a4f73350c13424de984fd43309160ce30bc1df089\", \"sourceparentprocesssigneridentity\": \"MICROSOFT WINDOWS\", \"sourceparentprocessstarttime\": 1636964894046, \"sourceparentprocessstoryline\": \"E1798FE5683F14CF\", \"sourceparentprocesssubsystem\": \"win32\", \"sourceparentprocessusername\": \"CORP\\\\user\", \"sourceprocesscommandline\": \"\\\"C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\\\" \\\"-Command\\\" \\\"if((Get-ExecutionPolicy ) -ne 'AllSigned') { Set-ExecutionPolicy -Scope Process Bypass }; & 'C:\\\\Users\\\\user\\\\Documents\\\\git\\\\DSP2\\\\API HUB\\\\Documentation\\\\Generate.ps1'\\\"\", \"sourceprocessfilepath\": \"C:\\\\WINDOWS\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\", \"sourceprocessfilesingeridentity\": \"MICROSOFT WINDOWS\", \"sourceprocessintegritylevel\": \"medium\", \"sourceprocesskey\": \"8C3CD6D2478943E5\", \"sourceprocessmd5\": \"04029e121a0cfa5991749937dd22a1d9\", \"sourceprocessname\": \"powershell.exe\", \"sourceprocesspid\": 6676, \"sourceprocesssha1\": \"f43d9bb316e30ae1a3494ac5b0624f6bea1bf054\", \"sourceprocesssha256\": \"9f914d42706fe215501044acd85a32d58aaef1419d404fddfa5d3b48f66ccd9f\", \"sourceprocessstarttime\": 1637076505627, \"sourceprocessstoryline\": \"5D1F81C984CFD44D\", \"sourceprocesssubsystem\": \"win32\", \"sourceprocessusername\": \"CORP\\\\user\", \"systemUser\": 0, \"userId\": 824463119127413794, \"userName\": \"sentinelone\"}, \"description\": null, \"groupId\": \"924347507640996620\", \"hash\": null, \"id\": \"1290568704943967230\", \"osFamily\": null, \"primaryDescription\": \"Alert created for powershell.exe from Custom Rule: PowershellExecutionPolicyChanged Indicator Monito in Group LAPTOP in Site DEFAULT of Account CORP, detected on CORP-LAP-4075.\", \"secondaryDescription\": \"f43d9bb316e30ae1a3494ac5b0624f6bea1bf054\", \"siteId\": \"901144152460815495\", \"threatId\": null, \"updatedAt\": \"2021-11-16T15:29:38.429056Z\", \"userId\": \"824463119127413794\"}",
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        },
        "event": {
            "category": "intrusion_detection",
            "id": "1290568704943967230",
            "kind": "event",
            "outcome": "success",
            "reason": "Alert created for powershell.exe from Custom Rule: PowershellExecutionPolicyChanged Indicator Monito in Group LAPTOP in Site DEFAULT of Account CORP, detected on CORP-LAP-4075.",
            "type": "info"
        },
        "group": {
            "id": "924347507640996620"
        },
        "action": {
            "type": 3608
        },
        "agent": {
            "id": "1183145065000215213"
        },
        "process": {
            "command_line": "\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\" \"-Command\" \"if((Get-ExecutionPolicy ) -ne 'AllSigned') { Set-ExecutionPolicy -Scope Process Bypass }; & 'C:\\Users\\user\\Documents\\git\\DSP2\\API HUB\\Documentation\\Generate.ps1'\"",
            "executable": "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
            "hash": {
                "md5": "04029e121a0cfa5991749937dd22a1d9",
                "sha1": "f43d9bb316e30ae1a3494ac5b0624f6bea1bf054",
                "sha256": "9f914d42706fe215501044acd85a32d58aaef1419d404fddfa5d3b48f66ccd9f"
            },
            "name": "powershell.exe",
            "parent": {
                "code_signature": {
                    "subject_name": "MICROSOFT WINDOWS"
                },
                "command_line": "C:\\WINDOWS\\Explorer.EXE",
                "executable": "C:\\WINDOWS\\explorer.exe",
                "hash": {
                    "md5": "681a21a3b848ed960073475cd77634ce",
                    "sha1": "3d930943fbea03c9330c4947e5749ed9ceed528a",
                    "sha256": "08d3f16dfbb5b5d7b419376a4f73350c13424de984fd43309160ce30bc1df089"
                },
                "name": "explorer.exe",
                "pid": 11196,
                "start": 1636964894046
            },
            "pid": 6676,
            "start": 1637076505627
        },
        "related": {
            "hash": [
                "f43d9bb316e30ae1a3494ac5b0624f6bea1bf054",
                "681a21a3b848ed960073475cd77634ce",
                "3d930943fbea03c9330c4947e5749ed9ceed528a",
                "9f914d42706fe215501044acd85a32d58aaef1419d404fddfa5d3b48f66ccd9f",
                "04029e121a0cfa5991749937dd22a1d9",
                "08d3f16dfbb5b5d7b419376a4f73350c13424de984fd43309160ce30bc1df089"
            ]
        },
        "rule": {
            "description": "Rule migrated from Watchlist",
            "name": "PowershellExecutionPolicyChanged Indicator Monito",
            "id": "1259119070812474070"
        },
        "sentinelone": {
            "eventid": 1290568704943967230,
            "data": {
                "accountName": "CORP",
                "alertId": 1290568698312097725,
                "detectedat": 1637076565467,
                "dveventtype": "BEHAVIORALINDICATORS",
                "fullScopeDetails": "Group LAPTOP in Site DEFAULT of Account CORP",
                "groupName": "LAPTOP",
                "origagentmachinetype": "laptop",
                "origagentname": "CORP-LAP-4075",
                "origagentosfamily": "windows",
                "origagentosname": "Windows 10 Pro",
                "origagentosrevision": "19042",
                "origagentsiteid": 901144152460815495,
                "origagentuuid": "058fd4868adb4b87be24a4c5e9f89220",
                "origagentversion": "4.6.14.304",
                "rulescopelevel": "E_SITE",
                "rulescopeid": 901144152460815495,
                "scopeId": 901144152460815495,
                "scopeLevel": "Group",
                "scopeName": "LAPTOP",
                "severity": "E_MEDIUM",
                "siteName": "DEFAULT",
                "sourcename": "STAR",
                "sourceparentprocessintegritylevel": "medium",
                "sourceparentprocesskey": "811577BA383803B5",
                "sourceparentprocessstoryline": "E1798FE5683F14CF",
                "sourceparentprocesssubsystem": "win32",
                "sourceparentprocessusername": "CORP\\user",
                "sourceprocessfilesingeridentity": "MICROSOFT WINDOWS",
                "sourceprocesskey": "8C3CD6D2478943E5",
                "sourceprocessstoryline": "5D1F81C984CFD44D",
                "sourceprocesssubsystem": "win32",
                "sourceprocessusername": "CORP\\user",
                "sourceprocessintegritylevel": "medium",
                "systemUser": 0,
                "userName": "sentinelone"
            },
            "secondaryDescription": "f43d9bb316e30ae1a3494ac5b0624f6bea1bf054",
            "siteId": "901144152460815495",
            "updatedAt": "2021-11-16T15:29:38.429056Z"
        },
        "organization": {
            "id": "901144152444038278"
        },
        "user": {
            "id": 824463119127413794
        }
    }
    	
	```


=== "custom_rule2.json"

    ```json
	
    {
        "event": {
            "category": "intrusion_detection",
            "id": "1387492693815190915",
            "kind": "event",
            "outcome": "success",
            "reason": "Alert created for WebexHost_old.exe from Custom Rule: Webex.Meetings.Atucfobj.dll Monitoring in Group LAPTOP in Site DEFAULT of Account CORP, detected on USR-LAP-4141."
        },
        "group": {
            "id": "924347507640996620"
        },
        "action": {
            "type": 3608
        },
        "agent": {
            "id": "1277428815225733296"
        },
        "organization": {
            "id": "901144152444038278"
        },
        "process": {
            "command_line": "\"C:\\Users\\user\\AppData\\Local\\WebEx\\WebexHost.exe\" /job=upgradeClient /channel=2af416334939280c",
            "executable": "C:\\Users\\user\\AppData\\Local\\WebEx\\WebexHost_old.exe",
            "hash": {
                "md5": "66883dc802f65605077b0b05b1bc901b",
                "sha1": "84580370c58b1b0c9e4138257018fd98efdf28ba",
                "sha256": "d8efbbfab923ad72057d165dc30f2c0d39a4f4d2dcb7d6fa8a8c9c5b406fcb23"
            },
            "name": "WebexHost_old.exe",
            "parent": {
                "code_signature": {
                    "subject_name": "CISCO WEBEX LLC"
                },
                "command_line": "\"C:\\Users\\user\\AppData\\Local\\WebEx\\WebexHost.exe\" /daemon /runFrom=autorun",
                "executable": "C:\\Users\\user\\AppData\\Local\\WebEx\\WebexHost_old.exe",
                "hash": {
                    "md5": "66883dc802f65605077b0b05b1bc901b",
                    "sha1": "84580370c58b1b0c9e4138257018fd98efdf28ba",
                    "sha256": "d8efbbfab923ad72057d165dc30f2c0d39a4f4d2dcb7d6fa8a8c9c5b406fcb23"
                },
                "name": "WebexHost_old.exe",
                "pid": 10996,
                "start": 1648628294256
            },
            "pid": 7788,
            "start": 1648630694853
        },
        "related": {
            "hash": [
                "66883dc802f65605077b0b05b1bc901b",
                "84580370c58b1b0c9e4138257018fd98efdf28ba",
                "d8efbbfab923ad72057d165dc30f2c0d39a4f4d2dcb7d6fa8a8c9c5b406fcb23"
            ]
        },
        "rule": {
            "description": "Ecriture d'une dll webex \"atucfobj.dll\" inconnu du syst\u00e8me sur le parc.",
            "name": "Webex.Meetings.Atucfobj.dll Monitoring"
        },
        "sentinelone": {
            "eventid": 1387492693815190915,
            "data": {
                "accountName": "CORP",
                "detectedat": 1648630801340,
                "dveventtype": "FILEMODIFICATION",
                "fullScopeDetails": "Group LAPTOP in Site DEFAULT of Account CORP",
                "groupName": "LAPTOP",
                "origagentmachinetype": "laptop",
                "origagentname": "USR-LAP-4141",
                "origagentosfamily": "windows",
                "origagentosname": "Windows 10 Pro",
                "origagentosrevision": "19042",
                "origagentsiteid": 901144152460815495,
                "origagentuuid": "53a4af77e0e2465abaa97d16e88a6355",
                "origagentversion": "21.7.5.1080",
                "rulescopeid": 901144152444038278,
                "rulescopelevel": "E_ACCOUNT",
                "scopeId": 901144152444038278,
                "scopeLevel": "Group",
                "scopeName": "LAPTOP",
                "severity": "E_MEDIUM",
                "siteName": "DEFAULT",
                "sourcename": "STAR",
                "sourceparentprocessintegritylevel": "medium",
                "sourceprocessintegritylevel": "medium",
                "sourceparentprocesskey": "DFF45D789645E07E",
                "sourceparentprocessstoryline": "114D19D4F405D782",
                "sourceparentprocesssubsystem": "win32",
                "sourceparentprocessusername": "CORP\\user",
                "sourceprocesskey": "634272057BAB1D81",
                "sourceprocessstoryline": "114D19D4F405D782",
                "sourceprocesssubsystem": "win32",
                "sourceprocessusername": "CORP\\user",
                "systemUser": 0,
                "userName": "User NAME"
            },
            "secondaryDescription": "84580370c58b1b0c9e4138257018fd98efdf28ba",
            "siteId": "901144152460815495",
            "updatedAt": "2022-03-30T09:00:18.282935Z"
        },
        "user": {
            "id": 901170701818003423
        }
    }
    	
	```


=== "threat.json"

    ```json
	
    {
        "event": {
            "category": "malware",
            "kind": "alert",
            "type": "info",
            "id": "1112953674841025235"
        },
        "organization": {
            "id": "617755838952421242",
            "name": "EXAMPLE CORP"
        },
        "file": {
            "extension": "tmp",
            "path": "\\Device\\HarddiskVolume2\\Users\\User\\AppData\\Local\\Temp\\nsr1C3F.tmp\\nsh29ED.tmp",
            "size": 2976256
        },
        "host": {
            "domain": "WORKGROUP",
            "ip": [
                "1.1.1.1",
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "2.2.2.2"
            ],
            "os": {
                "family": "windows",
                "version": "Windows 10 Pro"
            }
        },
        "sentinelone": {
            "eventid": 1112953674841025235,
            "agentDetectionInfo": {
                "agentLastLoggedInUserName": "User",
                "mitigationStatus": "User"
            },
            "groupname": "Default Group",
            "sitename": "Sekoia.io",
            "threatInfo": {
                "analystVerdict": "undefined",
                "analystVerdictDescription": "Undefined",
                "automaticallyResolved": false,
                "classificationSource": "Cloud",
                "cloudFilesHashVerdict": "provider_unknown",
                "detectionType": "static",
                "failedActions": false,
                "fileVerificationType": "NotSigned",
                "incidentStatus": "unresolved",
                "incidentStatusDescription": "Unresolved",
                "initiatedBy": "agent_policy",
                "initiatedByDescription": "Agent Policy",
                "isFileless": false,
                "isValidCertificate": false,
                "mitigationStatusDescription": "Not mitigated",
                "originatorProcess": "FileZilla_3.53.0_win64_sponsored-setup.exe",
                "processUser": "VM-SENTINELONE\\User",
                "threatId": "1112953674841025235",
                "updatedAt": "2021-03-16T14:00:16.874050Z",
                "pendingActions": false,
                "rebootRequired": false
            }
        },
        "threat": {
            "enrichments": {
                "indicator": {
                    "file": {
                        "name": "nsh29ED.tmp"
                    }
                },
                "matched": {
                    "occurred": "2021-03-16T14:00:14.188000Z"
                }
            },
            "indicator": {
                "confidence": "suspicious",
                "file": {
                    "created": "2021-03-16T14:00:16.879105Z",
                    "size": 2976256
                }
            },
            "software": {
                "type": "Malware"
            }
        }
    }
    	
	```


=== "threat2.json"

    ```json
	
    {
        "event": {
            "dialect": "sentinelone",
            "category": "malware",
            "kind": "alert",
            "id": "1113032189486913422",
            "type": "info",
            "outcome": "success",
            "action": "Agent started full disk scan",
            "created": "2021-04-23T20:02:05.017771Z"
        },
        "file": {
            "extension": "exe",
            "path": "\\Device\\HarddiskVolume2\\Users\\tdr\\Downloads\\mimikatz_trunk\\x64\\mimikatz.exe",
            "size": 1309448
        },
        "host": {
            "domain": "WORKGROUP",
            "ip": [
                "10.0.1.4",
                "1.1.1.1",
                "fe80::9ddd:fd78:1f21:f709",
                "fe80::9ddd:fd78:1f21:f708",
                "fe80::9ddd:fd78:1f21:f707",
                "55.55.55.55"
            ],
            "os": {
                "family": "windows",
                "version": "Windows 10 Pro"
            }
        },
        "organization": {
            "id": "617755838952421242",
            "name": "CORP"
        },
        "sentinelone": {
            "eventid": 1113032189486913422,
            "agentDetectionInfo": {
                "agentLastLoggedInUserName": "tdr",
                "mitigationStatus": "tdr"
            },
            "groupname": "Default Group",
            "sitename": "Sekoia.io",
            "threatInfo": {
                "analystVerdict": "true_positive",
                "analystVerdictDescription": "True positive",
                "automaticallyResolved": false,
                "classificationSource": "Cloud",
                "cloudFilesHashVerdict": "black",
                "detectionType": "static",
                "fileVerificationType": "SignedVerified",
                "incidentStatus": "resolved",
                "incidentStatusDescription": "Resolved",
                "initiatedBy": "agent_policy",
                "initiatedByDescription": "Agent Policy",
                "mitigationStatusDescription": "Not mitigated",
                "originatorProcess": "explorer.exe",
                "processUser": "tdr-vm-template\\tdr",
                "threatId": "1113032189486913422",
                "updatedAt": "2021-03-16T17:33:41.910607Z",
                "isFileless": false,
                "isValidCertificate": true,
                "pendingActions": false,
                "rebootRequired": false,
                "failedActions": false
            }
        },
        "threat": {
            "enrichments": {
                "indicator": {
                    "file": {
                        "name": "mimikatz.exe"
                    }
                },
                "matched": {
                    "occurred": "2021-03-16T16:36:16.157000Z"
                }
            },
            "indicator": {
                "confidence": "malicious",
                "file": {
                    "code_signature": {
                        "signing_id": "OPEN SOURCE DEVELOPER, BENJAMIN DELPY"
                    },
                    "created": "2021-03-16T16:36:16.554368Z",
                    "size": 1309448
                }
            },
            "software": {
                "type": "Infostealer"
            }
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "threat3.json"

    ```json
	
    {
        "event": {
            "category": "malware",
            "id": "1290568704943967230",
            "kind": "alert",
            "outcome": "success",
            "type": [
                "info"
            ]
        },
        "file": {
            "extension": "exe",
            "path": "\\Device\\HarddiskVolume3\\Users\\USERNAME\\Downloads\\OfficeTimeline.exe",
            "size": 65517824
        },
        "organization": {
            "id": "111111111111111111",
            "name": "REDACTED"
        },
        "host": {
            "domain": "DOMAIN",
            "ip": [
                "192.168.56.1",
                "10.4.4.69",
                "fe80::e4a1:7fce:33f3:d50e",
                "fe80::605f:b34f:31ac:498",
                "66.66.66.66"
            ],
            "os": {
                "family": "windows",
                "version": "Windows 10 Pro"
            }
        },
        "sentinelone": {
            "agentDetectionInfo": {
                "agentLastLoggedInUserName": "USERNAME",
                "mitigationStatus": "USERNAME"
            },
            "eventid": 1373834705420286869,
            "groupname": "Default Group",
            "sitename": "REDACTED-Users",
            "threatInfo": {
                "analystVerdict": "undefined",
                "analystVerdictDescription": "Undefined",
                "automaticallyResolved": false,
                "classificationSource": "Static",
                "detectionType": "dynamic",
                "failedActions": false,
                "fileVerificationType": "SignedVerified",
                "incidentStatus": "unresolved",
                "incidentStatusDescription": "Unresolved",
                "initiatedBy": "agent_policy",
                "initiatedByDescription": "Agent Policy",
                "isFileless": false,
                "isValidCertificate": true,
                "maliciousProcessArguments": "\"C:\\Users\\USERNAME\\Downloads\\OfficeTimeline.exe\"",
                "mitigationStatusDescription": "Mitigated",
                "originatorProcess": "chrome.exe",
                "pendingActions": false,
                "processUser": "DOMAIN\\USERNAME",
                "rebootRequired": false,
                "threatId": "1373834705420286869",
                "updatedAt": "2022-03-11T12:44:33.501615Z"
            }
        },
        "threat": {
            "enrichments": {
                "indicator": {
                    "file": {
                        "name": "OfficeTimeline.exe"
                    }
                },
                "matched": {
                    "occurred": "2022-03-11T12:44:16.158000Z"
                }
            },
            "indicator": {
                "confidence": "suspicious",
                "file": {
                    "code_signature": {
                        "signing_id": "OFFICE TIMELINE, LLC"
                    },
                    "created": "2022-03-11T12:44:19.192413Z",
                    "size": 65517824
                }
            },
            "software": {
                "type": "Malware"
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`action.type` | `long` | None |
|`agent.id` | `keyword` | Unique identifier of this agent. |
|`agent.version` | `keyword` | Version of the agent. |
|`container.id` | `keyword` | Unique container id. |
|`container.image.name` | `keyword` | Name of the image the container was built on. |
|`container.labels` | `object` | Image labels. |
|`container.name` | `keyword` | Container name. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.extension` | `keyword` | File extension, excluding the leading dot. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`file.size` | `long` | File size in bytes. |
|`group.id` | `keyword` | Unique identifier for the group on the system/platform. |
|`group.name` | `keyword` | Name of the group. |
|`host.domain` | `keyword` | Name of the directory the group is a member of. |
|`host.ip` | `ip` | Host ip addresses. |
|`host.name` | `keyword` | Name of the host. |
|`host.os.family` | `keyword` | OS family (such as redhat, debian, freebsd, windows). |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`organization.id` | `keyword` | None |
|`organization.name` | `keyword` | None |
|`os.family` | `keyword` | None |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.hash.md5` | `keyword` | MD5 hash. |
|`process.hash.sha1` | `keyword` | SHA1 hash. |
|`process.hash.sha256` | `keyword` | SHA256 hash. |
|`process.name` | `keyword` | Process name. |
|`process.parent.code_signature.subject_name` | `keyword` | Subject name of the code signer |
|`process.parent.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.parent.hash.md5` | `keyword` | MD5 hash. |
|`process.parent.hash.sha1` | `keyword` | SHA1 hash. |
|`process.parent.hash.sha256` | `keyword` | SHA256 hash. |
|`process.parent.name` | `keyword` | Process name. |
|`process.parent.pid` | `long` | Process id. |
|`process.parent.start` | `date` | The time the process started. |
|`process.pid` | `long` | Process id. |
|`process.start` | `date` | The time the process started. |
|`rule.description` | `keyword` | Rule description |
|`rule.id` | `keyword` | Rule ID |
|`rule.name` | `keyword` | Rule name |
|`sentinelone.agentDetectionInfo.agentLastLoggedInUserName` | `keyword` | None |
|`sentinelone.agentDetectionInfo.mitigationStatus` | `keyword` | None |
|`sentinelone.comments` | `keyword` | None |
|`sentinelone.data.accountName` | `keyword` | None |
|`sentinelone.data.action` | `keyword` | None |
|`sentinelone.data.activatedEngines` | `keyword` | None |
|`sentinelone.data.alertId` | `long` | None |
|`sentinelone.data.bluetoothAddress` | `keyword` | None |
|`sentinelone.data.byUser` | `keyword` | None |
|`sentinelone.data.current` | `keyword` | None |
|`sentinelone.data.deactivatedEngines` | `keyword` | None |
|`sentinelone.data.detectedat` | `long` | None |
|`sentinelone.data.deviceClass` | `keyword` | None |
|`sentinelone.data.deviceInformationServiceInfoKey` | `keyword` | None |
|`sentinelone.data.deviceInformationServiceInfoValue` | `keyword` | None |
|`sentinelone.data.deviceName` | `keyword` | None |
|`sentinelone.data.disabledLevel` | `keyword` | None |
|`sentinelone.data.dveventid` | `long` | None |
|`sentinelone.data.dveventtype` | `keyword` | None |
|`sentinelone.data.enabledReason` | `keyword` | None |
|`sentinelone.data.exclusionType` | `keyword` | None |
|`sentinelone.data.expiration` | `keyword` | None |
|`sentinelone.data.fileContentHash` | `keyword` | None |
|`sentinelone.data.fullScopeDetails` | `keyword` | None |
|`sentinelone.data.gattService` | `keyword` | None |
|`sentinelone.data.groupName` | `keyword` | None |
|`sentinelone.data.interface` | `keyword` | None |
|`sentinelone.data.k8sclustername` | `keyword` | None |
|`sentinelone.data.k8scontrollerkind` | `keyword` | None |
|`sentinelone.data.k8scontrollerlabels` | `keyword` | None |
|`sentinelone.data.k8scontrollername` | `keyword` | None |
|`sentinelone.data.k8snamespace` | `keyword` | None |
|`sentinelone.data.k8snamespacelabels` | `keyword` | None |
|`sentinelone.data.k8snode` | `keyword` | None |
|`sentinelone.data.k8spod` | `keyword` | None |
|`sentinelone.data.k8spodlabels` | `keyword` | None |
|`sentinelone.data.lmpVersion` | `keyword` | None |
|`sentinelone.data.manufacturerName` | `keyword` | None |
|`sentinelone.data.minorClasses` | `keyword` | None |
|`sentinelone.data.order` | `keyword` | None |
|`sentinelone.data.origagentmachinetype` | `keyword` | None |
|`sentinelone.data.origagentname` | `keyword` | None |
|`sentinelone.data.origagentosfamily` | `keyword` | None |
|`sentinelone.data.origagentosname` | `keyword` | None |
|`sentinelone.data.origagentosrevision` | `keyword` | None |
|`sentinelone.data.origagentsiteid` | `long` | None |
|`sentinelone.data.origagentuuid` | `keyword` | None |
|`sentinelone.data.origagentversion` | `keyword` | None |
|`sentinelone.data.policy` | `keyword` | None |
|`sentinelone.data.policyName` | `keyword` | None |
|`sentinelone.data.previous` | `keyword` | None |
|`sentinelone.data.productId` | `keyword` | None |
|`sentinelone.data.profileUuids` | `keyword` | None |
|`sentinelone.data.reason` | `keyword` | None |
|`sentinelone.data.role` | `keyword` | None |
|`sentinelone.data.ruleType` | `keyword` | None |
|`sentinelone.data.rulescopeid` | `long` | None |
|`sentinelone.data.rulescopelevel` | `keyword` | None |
|`sentinelone.data.scopeId` | `long` | None |
|`sentinelone.data.scopeLevel` | `keyword` | None |
|`sentinelone.data.scopeName` | `keyword` | None |
|`sentinelone.data.setting` | `keyword` | None |
|`sentinelone.data.severity` | `keyword` | None |
|`sentinelone.data.shouldReboot` | `keyword` | None |
|`sentinelone.data.siteName` | `keyword` | None |
|`sentinelone.data.source` | `keyword` | None |
|`sentinelone.data.sourcename` | `keyword` | None |
|`sentinelone.data.sourceparentprocessintegritylevel` | `keyword` | None |
|`sentinelone.data.sourceparentprocesskey` | `keyword` | None |
|`sentinelone.data.sourceparentprocessstoryline` | `keyword` | None |
|`sentinelone.data.sourceparentprocesssubsystem` | `keyword` | None |
|`sentinelone.data.sourceparentprocessusername` | `keyword` | None |
|`sentinelone.data.sourceprocessfilesingeridentity` | `keyword` | None |
|`sentinelone.data.sourceprocessintegritylevel` | `keyword` | None |
|`sentinelone.data.sourceprocesskey` | `keyword` | None |
|`sentinelone.data.sourceprocessstoryline` | `keyword` | None |
|`sentinelone.data.sourceprocesssubsystem` | `keyword` | None |
|`sentinelone.data.sourceprocessusername` | `keyword` | None |
|`sentinelone.data.status` | `keyword` | None |
|`sentinelone.data.systemUser` | `long` | None |
|`sentinelone.data.uid` | `keyword` | None |
|`sentinelone.data.uploadedFilename` | `keyword` | None |
|`sentinelone.data.userName` | `keyword` | None |
|`sentinelone.data.userscope` | `keyword` | None |
|`sentinelone.data.uuid` | `keyword` | None |
|`sentinelone.data.vendorId` | `long` | None |
|`sentinelone.data.version` | `keyword` | None |
|`sentinelone.description` | `keyword` | None |
|`sentinelone.eventid` | `long` | None |
|`sentinelone.groupname` | `keyword` | None |
|`sentinelone.hash` | `keyword` | None |
|`sentinelone.secondaryDescription` | `keyword` | None |
|`sentinelone.siteId` | `keyword` | None |
|`sentinelone.sitename` | `keyword` | None |
|`sentinelone.threatId` | `keyword` | None |
|`sentinelone.threatInfo.AuthenticationPackageName` | `keyword` | None |
|`sentinelone.threatInfo.NewTargetUserName` | `keyword` | None |
|`sentinelone.threatInfo.analystVerdict` | `keyword` | None |
|`sentinelone.threatInfo.analystVerdictDescription` | `keyword` | None |
|`sentinelone.threatInfo.automaticallyResolved` | `bool` | None |
|`sentinelone.threatInfo.browserType` | `keyword` | None |
|`sentinelone.threatInfo.classificationSource` | `keyword` | None |
|`sentinelone.threatInfo.cloudFilesHashVerdict` | `keyword` | None |
|`sentinelone.threatInfo.detectionType` | `keyword` | None |
|`sentinelone.threatInfo.failedActions` | `bool` | None |
|`sentinelone.threatInfo.fileVerificationType` | `keyword` | None |
|`sentinelone.threatInfo.incidentStatus` | `keyword` | None |
|`sentinelone.threatInfo.incidentStatusDescription` | `keyword` | None |
|`sentinelone.threatInfo.initiatedBy` | `keyword` | None |
|`sentinelone.threatInfo.initiatedByDescription` | `keyword` | None |
|`sentinelone.threatInfo.initiatingUserId` | `keyword` | None |
|`sentinelone.threatInfo.initiatingUsername` | `keyword` | None |
|`sentinelone.threatInfo.isFileless` | `bool` | None |
|`sentinelone.threatInfo.isValidCertificate` | `bool` | None |
|`sentinelone.threatInfo.maliciousProcessArguments` | `keyword` | None |
|`sentinelone.threatInfo.mitigationStatusDescription` | `keyword` | None |
|`sentinelone.threatInfo.originatorProcess` | `keyword` | None |
|`sentinelone.threatInfo.pendingActions` | `bool` | None |
|`sentinelone.threatInfo.processUser` | `keyword` | None |
|`sentinelone.threatInfo.rebootRequired` | `bool` | None |
|`sentinelone.threatInfo.threatId` | `keyword` | None |
|`sentinelone.threatInfo.updatedAt` | `keyword` | None |
|`sentinelone.updatedAt` | `keyword` | None |
|`threat.enrichments.indicator.file.hash.md5` | `keyword` | MD5 hash. |
|`threat.enrichments.indicator.file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`threat.enrichments.matched.occurred` | `date` | Date of match |
|`threat.indicator.confidence` | `keyword` | Indicator confidence rating |
|`threat.indicator.file.code_signature.signing_id` | `keyword` | The identifier used to sign the process. |
|`threat.indicator.file.created` | `date` | File creation time. |
|`threat.indicator.file.size` | `long` | File size in bytes. |
|`threat.software.type` | `keyword` | Software type. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.id` | `long` | None |
|`user.name` | `keyword` | Short name or login of the user. |

