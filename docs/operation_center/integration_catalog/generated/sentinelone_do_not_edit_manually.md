
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
            "action": "Agent Started Full Disk Scan",
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
            "type": [
                "info"
            ]
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
            "createdAt": "2021-03-11T12:42:56.308213Z",
            "data": {
                "accountName": "CORP",
                "computerName": "debian-SentinelOne",
                "createdAt": "2021-03-11T12:42:56.297860Z",
                "fullScopeDetails": "Group Default Group in Site Sekoia.io of Account CORP",
                "groupName": "Default Group",
                "scopeLevel": "Group",
                "scopeName": "Default Group",
                "siteName": "Sekoia.io",
                "status": "started"
            },
            "siteId": 1107851598358168475,
            "eventid": 1109290868249950294,
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


=== "activity-type-120.json"

    ```json
	
    {
        "action": {
            "type": 120
        },
        "agent": {
            "id": "977351746870921161"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "Agent Enabled",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "1113032189486913422",
            "kind": "event",
            "outcome": "success",
            "reason": "The CL002793 Agent is enabled due to time expiration.",
            "type": [
                "info"
            ]
        },
        "group": {
            "id": "797501649544140679"
        },
        "host": {
            "ip": [
                "88.127.242.225"
            ],
            "name": "CL002793"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "related": {
            "ip": [
                "88.127.242.225"
            ]
        },
        "sentinelone": {
            "createdAt": "2022-04-11T06:49:21.769668Z",
            "data": {
                "accountName": "CORP",
                "computerName": "CL002793",
                "enabledReason": "expired",
                "externalIp": "88.127.242.225",
                "fullScopeDetails": "Group DSI in Site CORP-workstations of Account CORP",
                "fullScopeDetailsPath": "Global / CORP / CORP-workstations / DSI",
                "groupName": "DSI",
                "scopeLevel": "Group",
                "scopeName": "DSI",
                "siteName": "CORP-workstations"
            },
            "eventid": 1396124097359316984,
            "siteId": 551799242253151036,
            "updatedAt": "2022-04-11T06:49:21.765992Z"
        }
    }
    	
	```


=== "activity-type-128.json"

    ```json
	
    {
        "action": {
            "type": 128
        },
        "agent": {
            "id": "859960378210728293"
        },
        "event": {
            "category": "intrusion_detection",
            "id": "1112953674841025235",
            "kind": "event",
            "outcome": "success",
            "reason": "Functionality of the SentinelOne Agent on a01pwrbi005 is limited, due to a database corruption. Contact Support.",
            "type": [
                "info"
            ],
            "action": "Agent Disabled Because of Database Corruption"
        },
        "group": {
            "id": "834457314771868699"
        },
        "host": {
            "ip": [
                "62.122.8.8"
            ],
            "name": "a01pwrbi005"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "related": {
            "ip": [
                "62.122.8.8"
            ]
        },
        "sentinelone": {
            "createdAt": "2022-04-05T09:06:38.941691Z",
            "data": {
                "accountName": "corp",
                "computerName": "a01pwrbi005",
                "disabledLevel": "db corruption",
                "externalIp": "62.122.8.8",
                "fullScopeDetails": "Group Env. 01 - Prod in Site corp-servers-windows of Account corp",
                "fullScopeDetailsPath": "Global / corp / corp-servers-windows / Env. 01 - Prod",
                "groupName": "Env. 01 - Prod",
                "scopeLevel": "Group",
                "scopeName": "Env. 01 - Prod",
                "siteName": "corp-servers-windows"
            },
            "eventid": 1391844541367588156,
            "siteId": 795516416264105067,
            "updatedAt": "2022-04-05T09:06:38.937917Z"
        }
    }
    	
	```


=== "activity-type-2001.json"

    ```json
	
    {
        "action": {
            "type": 2001
        },
        "agent": {
            "id": "997510333395640565"
        },
        "event": {
            "action": "Threat Mitigation Report Kill Success",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "1113032189486913422",
            "kind": "event",
            "outcome": "success",
            "reason": "The agent CL001234 successfully killed the threat: Run SwitchThemeColor.ps1.lnk.",
            "type": [
                "info"
            ]
        },
        "file": {
            "name": "Run SwitchThemeColor.ps1.lnk",
            "path": "\\Device\\HarddiskVolume3\\Users\\user.name\\Desktop\\Run SwitchThemeColor.ps1.lnk"
        },
        "group": {
            "id": "797501649544140679"
        },
        "host": {
            "name": "CL001234"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "sentinelone": {
            "createdAt": "2022-04-05T09:10:15.006573Z",
            "data": {
                "accountName": "corp",
                "computerName": "CL001234",
                "fileContentHash": "08731ccac0d404da077e7029062f73ca3d8faf61",
                "fileDisplayName": "Run SwitchThemeColor.ps1.lnk",
                "fullScopeDetails": "Group DSI in Site corp-workstations of Account corp",
                "fullScopeDetailsPath": "Global / corp / corp-workstations / DSI",
                "globalStatus": "success",
                "groupName": "DSI",
                "scopeLevel": "Group",
                "scopeName": "DSI",
                "siteName": "corp-workstations",
                "threatClassification": "PUA",
                "threatClassificationSource": "Engine"
            },
            "eventid": 1391846353852639605,
            "secondaryDescription": "\\Device\\HarddiskVolume3\\Users\\user.name\\Desktop\\Run SwitchThemeColor.ps1.lnk",
            "siteId": 551799242253151036,
            "threatId": "1391846352913115209",
            "updatedAt": "2022-04-05T09:10:15.001215Z"
        }
    }
    	
	```


=== "activity-type-2004.json"

    ```json
	
    {
        "action": {
            "type": 2004
        },
        "agent": {
            "id": "997510333395640565"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "Threat Mitigation Report Quarantine Success",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "1113032189486913422",
            "kind": "event",
            "outcome": "success",
            "reason": "The agent CL001234 successfully quarantined the threat: Run SwitchThemeColor.ps1.lnk.",
            "type": [
                "info"
            ]
        },
        "file": {
            "name": "Run SwitchThemeColor.ps1.lnk",
            "path": "\\Device\\HarddiskVolume3\\Users\\user.name\\Desktop\\Run SwitchThemeColor.ps1.lnk"
        },
        "group": {
            "id": "797501649544140679"
        },
        "host": {
            "name": "CL001234"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "sentinelone": {
            "createdAt": "2022-04-05T09:10:15.137471Z",
            "data": {
                "accountName": "corp",
                "computerName": "CL001234",
                "fileContentHash": "08731ccac0d404da077e7029062f73ca3d8faf61",
                "fileDisplayName": "Run SwitchThemeColor.ps1.lnk",
                "fullScopeDetails": "Group DSI in Site corp-workstations of Account corp",
                "fullScopeDetailsPath": "Global / corp / corp-workstations / DSI",
                "groupName": "DSI",
                "scopeLevel": "Group",
                "scopeName": "DSI",
                "siteName": "corp-workstations",
                "threatClassification": "PUA",
                "threatClassificationSource": "Engine"
            },
            "eventid": 1391846354951547317,
            "secondaryDescription": "\\Device\\HarddiskVolume3\\Users\\user.name\\Desktop\\Run SwitchThemeColor.ps1.lnk",
            "siteId": 551799242253151036,
            "threatId": "1391846352913115209",
            "updatedAt": "2022-04-05T09:10:15.132383Z"
        },
        "url": {
            "original": "/threats/mitigation-report/1391846354842495401",
            "path": "/threats/mitigation-report/1391846354842495401"
        }
    }
    	
	```


=== "activity-type-25.json"

    ```json
	
    {
        "action": {
            "type": 25
        },
        "event": {
            "category": "intrusion_detection",
            "kind": "event",
            "outcome": "success",
            "reason": "The management user Jean Dupont deleted the user Foo User.",
            "action": "User Deleted"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "sentinelone": {
            "createdAt": "2022-04-14T06:19:49.402205Z",
            "data": {
                "accountName": "CORP",
                "deactivationPeriodInDays": "90",
                "byUser": "Jean Dupont",
                "fullScopeDetails": "Site CORP-servers-windows of Account CORP",
                "fullScopeDetailsPath": "Global / CORP / CORP-servers-windows",
                "role": "Contr\u00f4le Interne",
                "scopeLevel": "Site",
                "scopeName": "CORP-servers-windows",
                "siteName": "CORP-servers-windows",
                "userScope": "site"
            },
            "description": "Jean Dupont",
            "eventid": 1398283556850059260,
            "siteId": 795516416264105067,
            "updatedAt": "2022-04-14T06:19:49.402210Z"
        },
        "user": {
            "full_name": "Foo User",
            "id": 1157751223520522706
        }
    }
    	
	```


=== "activity-type-3016.json"

    ```json
	
    {
        "file": {
            "path": "C:\\Windows\\system32\\diskshadow.exe"
        },
        "action": {
            "type": 3016
        },
        "event": {
            "action": "Path Exclusion Deleted",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "1113032189486913422",
            "kind": "event",
            "outcome": "success",
            "reason": "The Management user Jean DUPONT deleted the Path Exclusion C:\\Windows\\system32\\diskshadow.exe for Windows from the Group Env. 99 - Admin",
            "type": [
                "info"
            ]
        },
        "group": {
            "id": "860506107823075486"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "os": {
            "family": "windows"
        },
        "sentinelone": {
            "createdAt": "2022-04-11T07:18:34.090547Z",
            "data": {
                "accountName": "CORP",
                "exclusionType": "path",
                "fullScopeDetails": "Group Env. 99 - Admin in Site CORP-servers-windows of Account CORP",
                "fullScopeDetailsPath": "Global / CORP / CORP-servers-windows / Env. 99 - Admin",
                "groupName": "Env. 99 - Admin",
                "scopeLevel": "Group",
                "scopeName": "Env. 99 - Admin",
                "siteName": "CORP-servers-windows"
            },
            "eventid": 1396138796888471533,
            "siteId": 795516416264105067,
            "updatedAt": "2022-04-11T07:18:34.089273Z"
        },
        "user": {
            "id": 827950513703271774,
            "full_name": "Jean DUPONT"
        }
    }
    	
	```


=== "activity-type-4003.json"

    ```json
	
    {
        "organization": {
            "id": "551799238352448315"
        },
        "action": {
            "type": 4003
        },
        "agent": {
            "id": "997510333395640565"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "intrusion_detection",
            "kind": "event",
            "outcome": "success",
            "reason": "Threat with confidence level suspicious detected: Run SwitchThemeColor.ps1.lnk.",
            "action": "New Suspicious Threat Not Mitigated"
        },
        "file": {
            "name": "Run SwitchThemeColor.ps1.lnk",
            "path": "\\Device\\HarddiskVolume3\\Users\\user.name\\Desktop\\Run SwitchThemeColor.ps1.lnk"
        },
        "group": {
            "id": "797501649544140679"
        },
        "host": {
            "name": "CL001234"
        },
        "sentinelone": {
            "createdAt": "2022-04-05T09:10:14.913348Z",
            "data": {
                "accountName": "corp",
                "computerName": "CL001234",
                "confidenceLevel": "suspicious",
                "fileContentHash": "08731ccac0d404da077e7029062f73ca3d8faf61",
                "fileDisplayName": "Run SwitchThemeColor.ps1.lnk",
                "fullScopeDetails": "Group DSI in Site corp-workstations of Account corp",
                "fullScopeDetailsPath": "Global / corp / corp-workstations / DSI",
                "groupName": "DSI",
                "siteName": "corp-workstations"
            },
            "eventid": 1391846353072498959,
            "secondaryDescription": "08731ccac0d404da077e7029062f73ca3d8faf61",
            "siteId": 551799242253151036,
            "threatId": "1391846352913115209",
            "updatedAt": "2022-04-05T09:10:14.903935Z"
        }
    }
    	
	```


=== "activity-type-4008.json"

    ```json
	
    {
        "action": {
            "type": 4008
        },
        "agent": {
            "id": "997510333395640565"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "Threat Mitigation Status Changed",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "1113032189486913422",
            "kind": "event",
            "outcome": "success",
            "reason": "Status of threat Run SwitchThemeColor.ps1.lnk on agent CL001234 changed from Not mitigated to Mitigated.",
            "type": [
                "info"
            ]
        },
        "file": {
            "name": "Run SwitchThemeColor.ps1.lnk",
            "path": "\\Device\\HarddiskVolume3\\Users\\user.name\\Desktop\\Run SwitchThemeColor.ps1.lnk"
        },
        "group": {
            "id": "797501649544140679"
        },
        "host": {
            "name": "CL001234"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "sentinelone": {
            "createdAt": "2022-04-05T09:10:15.125572Z",
            "data": {
                "accountName": "corp",
                "computerName": "CL001234",
                "fileContentHash": "08731ccac0d404da077e7029062f73ca3d8faf61",
                "fileDisplayName": "Run SwitchThemeColor.ps1.lnk",
                "fullScopeDetails": "Group DSI in Site corp-workstations of Account corp",
                "fullScopeDetailsPath": "Global / corp / corp-workstations / DSI",
                "groupName": "DSI",
                "newStatus": "Mitigated",
                "originalStatus": "Not mitigated",
                "siteName": "corp-workstations",
                "threatClassification": "PUA",
                "threatClassificationSource": "Engine"
            },
            "eventid": 1391846354850884010,
            "secondaryDescription": "\\Device\\HarddiskVolume3\\Users\\user.name\\Desktop\\Run SwitchThemeColor.ps1.lnk",
            "siteId": 551799242253151036,
            "threatId": "1391846352913115209",
            "updatedAt": "2022-04-05T09:10:15.119559Z"
        }
    }
    	
	```


=== "activity-type-47.json"

    ```json
	
    {
        "action": {
            "type": 47
        },
        "agent": {
            "id": "1351979140358907826"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "intrusion_detection",
            "id": "1387492693815190915",
            "kind": "event",
            "outcome": "success",
            "reason": "Agent CL-ABCEDFG automatically decommissioned.",
            "action": "Agent Decommissioned"
        },
        "group": {
            "id": "551799242261539645"
        },
        "host": {
            "name": "CL-ABCEDFG"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "sentinelone": {
            "createdAt": "2022-04-10T22:10:31.034788Z",
            "data": {
                "accountName": "CORP",
                "computerName": "CL-ABCEDFG",
                "fullScopeDetails": "Group Default Group in Site CORP-workstations of Account CORP",
                "fullScopeDetailsPath": "Global / CORP / CORP-workstations / Default Group",
                "groupName": "Default Group",
                "scopeLevel": "Group",
                "scopeName": "Default Group",
                "siteName": "CORP-workstations",
                "uuid": "961376bbd9694a2ba2e1bb77ba027e38"
            },
            "eventid": 1395862953807825318,
            "siteId": 551799242253151036,
            "updatedAt": "2022-04-10T22:10:31.034790Z"
        }
    }
    	
	```


=== "activity-type-5009.json"

    ```json
	
    {
        "action": {
            "type": 5009
        },
        "agent": {
            "id": "841026328128144438"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "Agent Moved To A Different Group",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "2222222222222222222",
            "kind": "event",
            "outcome": "success",
            "reason": "The Agent CL001234 moved dynamically from Group DSI to Group Default Group",
            "type": [
                "info"
            ]
        },
        "group": {
            "id": "551799242261539645"
        },
        "host": {
            "name": "CL001234"
        },
        "sentinelone": {
            "createdAt": "2022-04-05T09:12:46.391928Z",
            "data": {
                "accountName": "corp",
                "computerName": "CL001234",
                "fullScopeDetails": "Group Default Group in Site corp-workstations of Account corp",
                "fullScopeDetailsPath": "Global / corp / corp-workstations / Default Group",
                "groupName": "Default Group",
                "newGroupId": "551799242261539645",
                "newGroupName": "Default Group",
                "oldGroupId": "797501649544140679",
                "oldGroupName": "DSI",
                "scopeLevel": "Group",
                "scopeName": "Default Group",
                "siteName": "corp-workstations"
            },
            "eventid": 1391847623762392173,
            "siteId": 551799242253151036,
            "updatedAt": "2022-04-05T09:12:45.472693Z"
        }
    }
    	
	```


=== "activity-type-5126.json"

    ```json
	
    {
        "event": {
            "category": "host",
            "id": "1387019684138751044",
            "kind": "event",
            "outcome": "success",
            "reason": "USB device  was connected on CORP123.",
            "type": [
                "allowed"
            ],
            "action": "Device Control Approved Event"
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
            "createdAt": "2022-03-29T17:20:31.139698Z",
            "data": {
                "accountName": "CORP",
                "computerName": "CORP123",
                "creator": "N/A",
                "deviceClass": "E0h",
                "eventId": "{1988659d-af84-11ec-914c-806e6f6e6963}",
                "eventTime": "2022-03-29T17:17:40.622+00:00",
                "eventType": "connected",
                "fullScopeDetails": "Group Default Group in Site CORP-Users of Account CORP",
                "fullScopeDetailsPath": "Global / CORP / CORP-Users / Default Group",
                "groupId": 1083054176758610128,
                "groupName": "Default Group",
                "interface": "USB",
                "lastLoggedInUserName": "user.name",
                "lmpVersion": "N/A",
                "minorClass": "N/A",
                "osType": "windows",
                "productId": "AAA",
                "profileUuids": "N/A",
                "ruleType": "productId",
                "scopeLevel": "Group",
                "scopeName": "Default Group",
                "siteName": "CORP-Users",
                "vendorId": 8087,
                "version": "N/A"
            },
            "eventid": 1387019684138751044,
            "siteId": 1083054176741832911,
            "updatedAt": "2022-03-29T17:20:30.998054Z"
        }
    }
    	
	```


=== "activity-type-5232.json"

    ```json
	
    {
        "destination": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "action": {
            "type": 5232
        },
        "agent": {
            "id": "840949586976454071"
        },
        "event": {
            "category": "intrusion_detection",
            "id": "1290568704943967230",
            "kind": "event",
            "outcome": "success",
            "reason": "Firewall Control blocked traffic on the Endpoint CORP1234 because of rule Block all in site CORP-workstations (CORP).",
            "type": [
                "info"
            ],
            "action": "Firewall Control Blocked Event"
        },
        "group": {
            "id": "551799242261539645"
        },
        "host": {
            "name": "CORP1234"
        },
        "organization": {
            "id": "551799238352448315"
        },
        "rule": {
            "description": "Flux",
            "id": "556166862007673241",
            "name": "Block all"
        },
        "network": {
            "direction": "inbound"
        },
        "sentinelone": {
            "createdAt": "2022-04-14T11:30:19.543892Z",
            "data": {
                "accountName": "CORP",
                "action": "Block",
                "applicationType": "any",
                "computerName": "CORP1234",
                "createdByUsername": "CUS_TER_211022_09_10_03_c4b7bce44eaf5d749e0399dd34f70ab83e3a1fd7",
                "durationOfMeasurement": 60,
                "fullScopeDetails": "Group Default Group in Site CORP-workstations of Account CORP",
                "fullScopeDetailsPath": "Global / CORP / CORP-workstations / Default Group",
                "groupName": "Default Group",
                "localHostType": "any",
                "localPortType": "any",
                "locationNames": [],
                "numberOfEvents": 3,
                "order": 32,
                "osTypes": [
                    "windows"
                ],
                "processId": 4,
                "remoteHostType": "any",
                "remotePortType": "any",
                "direction": "inbound",
                "ruleScopeLevel": "site",
                "ruleScopeName": "CORP-workstations (CORP)",
                "siteName": "CORP-workstations",
                "status": "Enabled",
                "tagNames": []
            },
            "eventid": 1398439837979472030,
            "siteId": 551799242253151036,
            "updatedAt": "2022-04-14T11:30:19.543894Z"
        }
    }
    	
	```


=== "activity-type-71.json"

    ```json
	
    {
        "action": {
            "type": 71
        },
        "agent": {
            "id": "1396250507390940172"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "Scan Initiated",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "1113032189486913422",
            "kind": "event",
            "outcome": "success",
            "reason": "System initiated a full disk scan to the agent: CORP-12347 (11.22.33.44).",
            "type": [
                "info"
            ]
        },
        "group": {
            "id": "901144152477592712"
        },
        "host": {
            "ip": [
                "11.22.33.44"
            ],
            "name": "CORP-12347"
        },
        "organization": {
            "id": "901144152444038278"
        },
        "related": {
            "ip": [
                "11.22.33.44"
            ]
        },
        "sentinelone": {
            "createdAt": "2022-04-11T11:00:31.291987Z",
            "data": {
                "accountName": "CORP",
                "computerName": "CORP-12347",
                "externalIp": "11.22.33.44",
                "fullScopeDetails": "Group Default Group in Site DEFAULT of Account CORP",
                "fullScopeDetailsPath": "Global / CORP / DEFAULT / Default Group",
                "groupName": "Default Group",
                "scopeLevel": "Group",
                "scopeName": "Default Group",
                "siteName": "DEFAULT",
                "uuid": "1e74916f8ac14a1b8d9b575ef7e91448",
                "system": true
            },
            "eventid": 1396250509672642912,
            "siteId": 901144152460815495,
            "updatedAt": "2022-04-11T11:00:31.291994Z"
        }
    }
    	
	```


=== "custom_rule.json"

    ```json
	
    {
        "file": {
            "name": "powershell.exe"
        },
        "organization": {
            "id": "901144152444038278"
        },
        "event": {
            "category": "intrusion_detection",
            "id": "1290568704943967230",
            "kind": "event",
            "outcome": "success",
            "reason": "Alert created for powershell.exe from Custom Rule: PowershellExecutionPolicyChanged Indicator Monito in Group LAPTOP in Site DEFAULT of Account CORP, detected on CORP-LAP-4075.",
            "type": [
                "info"
            ],
            "action": "Custom Rules - New Alert"
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
            "createdAt": "2021-11-16T15:29:38.431997Z",
            "data": {
                "accountName": "CORP",
                "alertId": 1290568698312097725,
                "alertid": 1290568698312097725,
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
                "rulescopeid": 901144152460815495,
                "rulescopelevel": "E_SITE",
                "scopeId": 901144152460815495,
                "scopeLevel": "Group",
                "scopeName": "LAPTOP",
                "severity": "E_MEDIUM",
                "siteName": "DEFAULT",
                "sourcename": "STAR",
                "sourceparentprocesscommandline": "C:\\WINDOWS\\Explorer.EXE",
                "sourceparentprocessintegritylevel": "medium",
                "sourceparentprocesskey": "811577BA383803B5",
                "sourceparentprocessmd5": "681a21a3b848ed960073475cd77634ce",
                "sourceparentprocessname": "explorer.exe",
                "sourceparentprocesspath": "C:\\WINDOWS\\explorer.exe",
                "sourceparentprocesspid": 11196,
                "sourceparentprocesssha1": "3d930943fbea03c9330c4947e5749ed9ceed528a",
                "sourceparentprocesssha256": "08d3f16dfbb5b5d7b419376a4f73350c13424de984fd43309160ce30bc1df089",
                "sourceparentprocesssigneridentity": "MICROSOFT WINDOWS",
                "sourceparentprocessstarttime": 1636964894046,
                "sourceparentprocessstoryline": "E1798FE5683F14CF",
                "sourceparentprocesssubsystem": "win32",
                "sourceparentprocessusername": "CORP\\user",
                "sourceprocesscommandline": "\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\" \"-Command\" \"if((Get-ExecutionPolicy ) -ne 'AllSigned') { Set-ExecutionPolicy -Scope Process Bypass }; & 'C:\\Users\\user\\Documents\\git\\DSP2\\API HUB\\Documentation\\Generate.ps1'\"",
                "sourceprocessfilepath": "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "sourceprocessfilesingeridentity": "MICROSOFT WINDOWS",
                "sourceprocessintegritylevel": "medium",
                "sourceprocesskey": "8C3CD6D2478943E5",
                "sourceprocessmd5": "04029e121a0cfa5991749937dd22a1d9",
                "sourceprocessname": "powershell.exe",
                "sourceprocesspid": 6676,
                "sourceprocesssha1": "f43d9bb316e30ae1a3494ac5b0624f6bea1bf054",
                "sourceprocesssha256": "9f914d42706fe215501044acd85a32d58aaef1419d404fddfa5d3b48f66ccd9f",
                "sourceprocessstarttime": 1637076505627,
                "sourceprocessstoryline": "5D1F81C984CFD44D",
                "sourceprocesssubsystem": "win32",
                "sourceprocessusername": "CORP\\user",
                "systemUser": 0,
                "userId": 111111111111111111
            },
            "eventid": 1290568704943967230,
            "secondaryDescription": "f43d9bb316e30ae1a3494ac5b0624f6bea1bf054",
            "siteId": 901144152460815495,
            "updatedAt": "2021-11-16T15:29:38.429056Z"
        },
        "user": {
            "full_name": "sentinelone",
            "id": 111111111111111111
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
            "reason": "Alert created for WebexHost_old.exe from Custom Rule: Webex.Meetings.Atucfobj.dll Monitoring in Group LAPTOP in Site DEFAULT of Account CORP, detected on USR-LAP-4141.",
            "action": "Custom Rules - New Alert"
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
            "name": "Webex.Meetings.Atucfobj.dll Monitoring",
            "id": "1360739572188076805"
        },
        "sentinelone": {
            "createdAt": "2022-03-30T09:00:18.286500Z",
            "data": {
                "alertid": 1387492689895241884,
                "accountName": "CORP",
                "agentipv4": "192.168.102.46",
                "detectedat": 1648630801340,
                "dstport": 0,
                "dveventtype": "FILEMODIFICATION",
                "externalip": "11.11.11.11",
                "fullScopeDetails": "Group LAPTOP in Site DEFAULT of Account CORP",
                "fullScopeDetailsPath": "Global / CORP / DEFAULT / LAPTOP",
                "groupName": "LAPTOP",
                "origagentmachinetype": "laptop",
                "origagentname": "USR-LAP-4141",
                "origagentosfamily": "windows",
                "origagentosname": "Windows 10 Pro",
                "origagentosrevision": "19042",
                "origagentsiteid": 901144152460815495,
                "origagentuuid": "53a4af77e0e2465abaa97d16e88a6355",
                "origagentversion": "21.7.5.1080",
                "physical": "70:b5:e8:92:72:0a",
                "rulescopeid": 901144152444038278,
                "rulescopelevel": "E_ACCOUNT",
                "scopeId": 901144152444038278,
                "scopeLevel": "Group",
                "scopeName": "LAPTOP",
                "severity": "E_MEDIUM",
                "siteName": "DEFAULT",
                "sourcename": "STAR",
                "sourceparentprocesscommandline": "\"C:\\Users\\user\\AppData\\Local\\WebEx\\WebexHost.exe\" /daemon /runFrom=autorun",
                "sourceparentprocessintegritylevel": "medium",
                "sourceparentprocesskey": "DFF45D789645E07E",
                "sourceparentprocessmd5": "66883dc802f65605077b0b05b1bc901b",
                "sourceparentprocessname": "WebexHost_old.exe",
                "sourceparentprocesspath": "C:\\Users\\user\\AppData\\Local\\WebEx\\WebexHost_old.exe",
                "sourceparentprocesspid": 10996,
                "sourceparentprocesssha1": "84580370c58b1b0c9e4138257018fd98efdf28ba",
                "sourceparentprocesssha256": "d8efbbfab923ad72057d165dc30f2c0d39a4f4d2dcb7d6fa8a8c9c5b406fcb23",
                "sourceparentprocesssigneridentity": "CISCO WEBEX LLC",
                "sourceparentprocessstarttime": 1648628294256,
                "sourceparentprocessstoryline": "114D19D4F405D782",
                "sourceparentprocesssubsystem": "win32",
                "sourceparentprocessusername": "CORP\\user",
                "sourceprocesscommandline": "\"C:\\Users\\user\\AppData\\Local\\WebEx\\WebexHost.exe\" /job=upgradeClient /channel=2af416334939280c",
                "sourceprocessfilepath": "C:\\Users\\user\\AppData\\Local\\WebEx\\WebexHost_old.exe",
                "sourceprocessfilesigneridentity": "CISCO WEBEX LLC",
                "sourceprocessintegritylevel": "medium",
                "sourceprocesskey": "634272057BAB1D81",
                "sourceprocessmd5": "66883dc802f65605077b0b05b1bc901b",
                "sourceprocessname": "WebexHost_old.exe",
                "sourceprocesspid": 7788,
                "sourceprocesssha1": "84580370c58b1b0c9e4138257018fd98efdf28ba",
                "sourceprocesssha256": "d8efbbfab923ad72057d165dc30f2c0d39a4f4d2dcb7d6fa8a8c9c5b406fcb23",
                "sourceprocessstarttime": 1648630694853,
                "sourceprocessstoryline": "114D19D4F405D782",
                "sourceprocesssubsystem": "win32",
                "sourceprocessusername": "CORP\\user",
                "srcport": 0,
                "systemUser": 0,
                "tgtfilecreatedat": 1646400756503,
                "tgtfilehashsha1": "5b1bbda6c8d9bb6e49e5e7c49909d48d5d35658a",
                "tgtfilehashsha256": "e89dd9db7c5f93ab2fd216d36e7432ea3b418b5df0191d4849fdb1967b2f6e2e",
                "tgtfileid": "5C4E2E3FE950B367",
                "tgtfileissigned": "signed",
                "tgtfilemodifiedat": 1648630718596,
                "tgtfilepath": "C:\\Users\\user\\AppData\\Local\\WebEx\\WebEx64\\Meetings\\atucfobj.dll",
                "tgtprocintegritylevel": "unknown",
                "tgtprocpid": 0,
                "userId": 901170701818003423
            },
            "eventid": 1387492693815190915,
            "secondaryDescription": "84580370c58b1b0c9e4138257018fd98efdf28ba",
            "siteId": 901144152460815495,
            "updatedAt": "2022-03-30T09:00:18.282935Z"
        },
        "file": {
            "name": "WebexHost_old.exe"
        },
        "user": {
            "full_name": "User NAME",
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
            "type": [
                "info"
            ],
            "id": "1112953674841025235"
        },
        "organization": {
            "id": "617755838952421242",
            "name": "EXAMPLE CORP"
        },
        "process": {
            "parent": {
                "name": "FileZilla_3.53.0_win64_sponsored-setup.exe"
            }
        },
        "file": {
            "name": "nsh29ED.tmp",
            "extension": "tmp",
            "path": "\\Device\\HarddiskVolume2\\Users\\User\\AppData\\Local\\Temp\\nsr1C3F.tmp\\nsh29ED.tmp",
            "size": 2976256
        },
        "related": {
            "ip": [
                "1.1.1.1",
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "2.2.2.2"
            ]
        },
        "host": {
            "ip": [
                "1.1.1.1",
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "2.2.2.2"
            ],
            "name": "VM-SentinelOne",
            "domain": "WORKGROUP",
            "os": {
                "family": "windows",
                "version": "Windows 10 Pro"
            }
        },
        "sentinelone": {
            "agentDetectionInfo": {
                "accountId": "617755838952421242",
                "accountName": "EXAMPLE CORP",
                "agentDomain": "WORKGROUP",
                "agentIpV4": "1.1.1.1",
                "agentIpV6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "agentLastLoggedInUserName": "User",
                "agentMitigationMode": "detect",
                "agentOsName": "Windows 10 Pro",
                "agentOsRevision": "19042",
                "agentRegisteredAt": "2021-03-11T11:12:30.665887Z",
                "agentUuid": "e50b53c856f041bab326d621d61db4f8",
                "agentVersion": "4.6.12.241",
                "externalIp": "2.2.2.2",
                "groupId": 1107851598374945694,
                "groupName": "Default Group",
                "siteId": 1107851598358168475,
                "siteName": "Sekoia.io"
            },
            "agentRealtimeInfo": {
                "activeThreats": 0,
                "agentComputerName": "VM-SentinelOne",
                "agentDomain": "WORKGROUP",
                "agentId": "1109245354690326957",
                "agentInfected": false,
                "agentIsActive": true,
                "agentIsDecommissioned": false,
                "agentMachineType": "desktop",
                "agentMitigationMode": "detect",
                "agentNetworkStatus": "connected",
                "agentOsRevision": "19042",
                "agentUuid": "e50b53c856f041bab326d621d61db4f8",
                "agentVersion": "4.6.12.241",
                "groupId": 1107851598374945694,
                "groupName": "Default Group",
                "networkInterfaces": [
                    {
                        "id": "1109245354698715566",
                        "inet": [
                            "1.1.1.1"
                        ],
                        "inet6": [
                            "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
                        ],
                        "name": "Ethernet",
                        "physical": "08:00:27:52:5d:be"
                    }
                ],
                "operationalState": "na",
                "rebootRequired": false,
                "scanStartedAt": "2021-03-11T11:12:43.266673Z",
                "scanStatus": "started",
                "siteId": 1107851598358168475,
                "siteName": "Sekoia.io",
                "userActionsNeeded": []
            },
            "eventid": 1112953674841025235,
            "indicators": [
                {
                    "category": "Hiding/Stealthiness",
                    "description": "The majority of sections in this PE have high entropy, a sign of obfuscation or packing.",
                    "ids": [
                        29
                    ],
                    "tactics": []
                },
                {
                    "category": "General",
                    "description": "This binary imports functions used to raise kernel exceptions.",
                    "ids": [
                        24
                    ],
                    "tactics": []
                },
                {
                    "category": "Hiding/Stealthiness",
                    "description": "This binary may contain encrypted or compressed data as measured by high entropy of the sections (greater than 6.8).",
                    "ids": [
                        12
                    ],
                    "tactics": []
                }
            ],
            "mitigationStatus": [],
            "threatInfo": {
                "externalTicketExists": false,
                "mitigatedPreemptively": false,
                "reachedEventsLimit": false,
                "analystVerdict": "undefined",
                "analystVerdictDescription": "Undefined",
                "automaticallyResolved": false,
                "classificationSource": "Cloud",
                "cloudFilesHashVerdict": "provider_unknown",
                "collectionId": "1112767491720942490",
                "detectionEngines": [
                    {
                        "key": "pre_execution_suspicious",
                        "title": "On-Write Static AI - Suspicious"
                    }
                ],
                "detectionType": "static",
                "engines": [
                    "On-Write DFI - Suspicious"
                ],
                "failedActions": false,
                "fileExtension": "TMP",
                "fileExtensionType": "Misc",
                "fileVerificationType": "NotSigned",
                "incidentStatus": "unresolved",
                "incidentStatusDescription": "Unresolved",
                "initiatedBy": "agent_policy",
                "initiatedByDescription": "Agent Policy",
                "isFileless": false,
                "isValidCertificate": false,
                "mitigationStatus": "not_mitigated",
                "mitigationStatusDescription": "Not mitigated",
                "pendingActions": false,
                "rebootRequired": false,
                "sha1": "4ffe673e3696a4287ab4a9c816d611a5fff56858",
                "storyline": "37077C139C322609",
                "threatId": "1112953674841025235",
                "updatedAt": "2021-03-16T14:00:16.874050Z"
            },
            "whiteningOptions": [
                "hash",
                "path"
            ]
        },
        "threat": {
            "enrichments": {
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
        },
        "user": {
            "name": "VM-SENTINELONE\\User"
        }
    }
    	
	```


=== "threat2.json"

    ```json
	
    {
        "user": {
            "name": "tdr-vm-template\\tdr"
        },
        "process": {
            "parent": {
                "name": "explorer.exe"
            }
        },
        "event": {
            "category": "malware",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "1113032189486913422",
            "kind": "alert",
            "outcome": "success",
            "type": [
                "info"
            ]
        },
        "file": {
            "name": "mimikatz.exe",
            "extension": "exe",
            "path": "\\Device\\HarddiskVolume2\\Users\\tdr\\Downloads\\mimikatz_trunk\\x64\\mimikatz.exe",
            "size": 1309448
        },
        "host": {
            "domain": "WORKGROUP",
            "os": {
                "family": "windows",
                "version": "Windows 10 Pro"
            },
            "ip": [
                "10.0.1.4",
                "1.1.1.1",
                "fe80::9ddd:fd78:1f21:f709",
                "fe80::9ddd:fd78:1f21:f708",
                "fe80::9ddd:fd78:1f21:f707",
                "55.55.55.55"
            ],
            "name": "tdr-vm-template"
        },
        "organization": {
            "id": "617755838952421242",
            "name": "CORP"
        },
        "sentinelone": {
            "agentDetectionInfo": {
                "accountId": "617755838952421242",
                "accountName": "CORP",
                "agentDomain": "WORKGROUP",
                "agentIpV4": "10.0.1.4,1.1.1.1",
                "agentIpV6": "fe80::9ddd:fd78:1f21:f709,fe80::9ddd:fd78:1f21:f708,fe80::9ddd:fd78:1f21:f707",
                "agentLastLoggedInUserName": "tdr",
                "agentMitigationMode": "detect",
                "agentOsName": "Windows 10 Pro",
                "agentOsRevision": "19041",
                "agentRegisteredAt": "2021-03-16T16:24:28.049913Z",
                "agentUuid": "ab268977a30842c88136c5afb77f3e12",
                "agentVersion": "4.6.12.241",
                "externalIp": "55.55.55.55",
                "groupId": 1107851598374945694,
                "groupName": "Default Group",
                "siteId": 1107851598358168475,
                "siteName": "Sekoia.io"
            },
            "agentRealtimeInfo": {
                "activeThreats": 9,
                "agentInfected": true,
                "agentIsActive": false,
                "agentIsDecommissioned": false,
                "rebootRequired": false,
                "agentComputerName": "tdr-vm-template",
                "agentDomain": "WORKGROUP",
                "agentId": "1113026246149650919",
                "agentMachineType": "desktop",
                "agentMitigationMode": "detect",
                "agentNetworkStatus": "connected",
                "agentOsRevision": "19041",
                "agentUuid": "ab268977a30842c88136c5afb77f3e12",
                "agentVersion": "4.6.12.241",
                "groupId": 1107851598374945694,
                "groupName": "Default Group",
                "networkInterfaces": [
                    {
                        "id": "1113026246158039528",
                        "inet": [
                            "10.0.1.4"
                        ],
                        "inet6": [
                            "fe80::9ddd:fd78:1f21:f709"
                        ],
                        "name": "Ethernet 2",
                        "physical": "00:0d:3a:b0:42:18"
                    }
                ],
                "operationalState": "na",
                "scanStartedAt": "2021-03-16T16:25:02.304681Z",
                "scanStatus": "started",
                "siteId": 1107851598358168475,
                "siteName": "Sekoia.io",
                "userActionsNeeded": []
            },
            "eventid": 1113032189486913422,
            "indicators": [
                {
                    "category": "InfoStealer",
                    "description": "This uses mimikatz, an open-source application that shows and saves credentials.",
                    "ids": [
                        38
                    ],
                    "tactics": []
                },
                {
                    "category": "General",
                    "description": "This binary imports functions used to raise kernel exceptions.",
                    "ids": [
                        24
                    ],
                    "tactics": []
                },
                {
                    "category": "General",
                    "description": "This binary imports debugger functions.",
                    "ids": [
                        6
                    ],
                    "tactics": []
                },
                {
                    "category": "General",
                    "description": "This binary creates a System Service.",
                    "ids": [
                        5
                    ],
                    "tactics": []
                }
            ],
            "mitigationStatus": [],
            "threatInfo": {
                "externalTicketExists": false,
                "mitigatedPreemptively": false,
                "reachedEventsLimit": false,
                "analystVerdict": "true_positive",
                "analystVerdictDescription": "True positive",
                "automaticallyResolved": false,
                "classificationSource": "Cloud",
                "cloudFilesHashVerdict": "black",
                "collectionId": "984546260612443092",
                "detectionEngines": [
                    {
                        "key": "pre_execution_suspicious",
                        "title": "On-Write Static AI - Suspicious"
                    }
                ],
                "detectionType": "static",
                "engines": [
                    "On-Write DFI - Suspicious"
                ],
                "failedActions": false,
                "fileExtension": "EXE",
                "fileExtensionType": "Executable",
                "fileVerificationType": "SignedVerified",
                "incidentStatus": "resolved",
                "incidentStatusDescription": "Resolved",
                "initiatedBy": "agent_policy",
                "initiatedByDescription": "Agent Policy",
                "isFileless": false,
                "isValidCertificate": true,
                "mitigationStatus": "not_mitigated",
                "mitigationStatusDescription": "Not mitigated",
                "pendingActions": false,
                "publisherName": "OPEN SOURCE DEVELOPER, BENJAMIN DELPY",
                "rebootRequired": false,
                "sha1": "d241df7b9d2ec0b8194751cd5ce153e27cc40fa4",
                "storyline": "D8F484ABE8543750",
                "threatId": "1113032189486913422",
                "updatedAt": "2021-03-16T17:33:41.910607Z"
            }
        },
        "threat": {
            "enrichments": {
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
            "name": "OfficeTimeline.exe",
            "extension": "exe",
            "path": "\\Device\\HarddiskVolume3\\Users\\USERNAME\\Downloads\\OfficeTimeline.exe",
            "size": 65517824
        },
        "host": {
            "domain": "DOMAIN",
            "os": {
                "family": "windows",
                "version": "Windows 10 Pro"
            },
            "ip": [
                "192.168.56.1",
                "10.4.4.69",
                "fe80::e4a1:7fce:33f3:d50e",
                "fe80::605f:b34f:31ac:498",
                "66.66.66.66"
            ],
            "name": "LSYN98873"
        },
        "related": {
            "ip": [
                "10.4.4.69",
                "fe80::e4a1:7fce:33f3:d50e",
                "192.168.56.1",
                "fe80::605f:b34f:31ac:498",
                "66.66.66.66"
            ]
        },
        "organization": {
            "id": "111111111111111111",
            "name": "REDACTED"
        },
        "process": {
            "parent": {
                "name": "chrome.exe"
            }
        },
        "sentinelone": {
            "EventTime": "2022-03-11 14:14:54",
            "agentDetectionInfo": {
                "accountId": "111111111111111111",
                "accountName": "REDACTED",
                "agentDomain": "DOMAIN",
                "agentIpV4": "192.168.56.1,10.4.4.69",
                "agentIpV6": "fe80::e4a1:7fce:33f3:d50e,fe80::605f:b34f:31ac:498",
                "agentLastLoggedInUserName": "USERNAME",
                "agentMitigationMode": "protect",
                "agentOsName": "Windows 10 Pro",
                "agentOsRevision": "19044",
                "agentRegisteredAt": "2021-02-10T16:12:18.659760Z",
                "agentUuid": "5e4482b45d134ae8bf4901cb52b65e88",
                "agentVersion": "21.7.5.1080",
                "externalIp": "66.66.66.66",
                "groupId": 1083054176758610128,
                "groupName": "Default Group",
                "siteId": 1083054176741832911,
                "siteName": "REDACTED-Users"
            },
            "agentRealtimeInfo": {
                "activeThreats": 0,
                "agentComputerName": "LSYN98873",
                "agentInfected": false,
                "agentIsActive": true,
                "agentIsDecommissioned": false,
                "rebootRequired": false,
                "agentDomain": "DOMAIN",
                "agentId": "1088377752722254024",
                "agentMachineType": "laptop",
                "agentMitigationMode": "protect",
                "agentNetworkStatus": "connected",
                "agentOsRevision": "19044",
                "agentUuid": "5e4482b45d134ae8bf4901cb52b65e88",
                "agentVersion": "21.7.5.1080",
                "groupId": 1083054176758610128,
                "groupName": "Default Group",
                "networkInterfaces": [
                    {
                        "id": "1373748335430042703",
                        "inet": [
                            "10.4.4.69"
                        ],
                        "inet6": [
                            "fe80::605f:b34f:31ac:498"
                        ],
                        "name": "Ethernet",
                        "physical": "98:fa:9b:5f:f2:bd"
                    },
                    {
                        "id": "1362550279953160460",
                        "inet": [
                            "192.168.56.1"
                        ],
                        "inet6": [
                            "fe80::e4a1:7fce:33f3:d50e"
                        ],
                        "name": "Ethernet 2",
                        "physical": "0a:00:27:00:00:0b"
                    }
                ],
                "operationalState": "na",
                "scanFinishedAt": "2022-01-31T13:56:31.482859Z",
                "scanStartedAt": "2022-01-28T15:25:03.885250Z",
                "scanStatus": "finished",
                "siteId": 1083054176741832911,
                "siteName": "REDACTED-Users",
                "userActionsNeeded": []
            },
            "eventid": 1373834705420286869,
            "indicators": [
                {
                    "category": "Exploitation",
                    "description": "Document behaves abnormally",
                    "ids": [
                        62
                    ],
                    "tactics": [
                        {
                            "name": "Execution",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1059/",
                                    "name": "T1059"
                                },
                                {
                                    "link": "https://attack.mitre.org/techniques/T1203/",
                                    "name": "T1203"
                                },
                                {
                                    "link": "https://attack.mitre.org/techniques/T1204/002",
                                    "name": "T1204.002"
                                }
                            ]
                        },
                        {
                            "name": "Initial Access",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1566/001/",
                                    "name": "T1566.001"
                                }
                            ]
                        }
                    ]
                },
                {
                    "category": "Persistence",
                    "description": "Application registered itself to become persistent via scheduled task",
                    "ids": [
                        197
                    ],
                    "tactics": [
                        {
                            "name": "Persistence",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1053/005/",
                                    "name": "T1053.005"
                                }
                            ]
                        }
                    ]
                },
                {
                    "category": "Evasion",
                    "description": "Suspicious registry key was created",
                    "ids": [
                        171
                    ],
                    "tactics": [
                        {
                            "name": "Defense Evasion",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1112/",
                                    "name": "T1112"
                                }
                            ]
                        }
                    ]
                },
                {
                    "category": "Injection",
                    "description": "Suspicious library loaded into the process memory",
                    "ids": [
                        126
                    ],
                    "tactics": []
                },
                {
                    "category": "General",
                    "description": "User logged on",
                    "ids": [
                        266
                    ],
                    "tactics": [
                        {
                            "name": "Persistence",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1078/",
                                    "name": "T1078"
                                }
                            ]
                        }
                    ]
                },
                {
                    "category": "Persistence",
                    "description": "Application registered itself to become persistent via an autorun",
                    "ids": [
                        199
                    ],
                    "tactics": [
                        {
                            "name": "Persistence",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1547/001/",
                                    "name": "T1547.001"
                                }
                            ]
                        },
                        {
                            "name": "Privilege Escalation",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1547/001/",
                                    "name": "T1547.001"
                                }
                            ]
                        }
                    ]
                }
            ],
            "mitigationStatus": [
                {
                    "action": "quarantine",
                    "actionsCounters": {
                        "failed": 0,
                        "notFound": 0,
                        "pendingReboot": 0,
                        "success": 172,
                        "total": 172
                    },
                    "agentSupportsReport": true,
                    "groupNotFound": false,
                    "lastUpdate": "2022-03-11T12:44:33.508808Z",
                    "latestReport": "/threats/mitigation-report/1373834825528452160",
                    "mitigationEndedAt": "2022-03-11T12:44:32.875000Z",
                    "mitigationStartedAt": "2022-03-11T12:44:18.331000Z",
                    "status": "success"
                },
                {
                    "action": "kill",
                    "actionsCounters": {
                        "failed": 0,
                        "notFound": 0,
                        "pendingReboot": 0,
                        "success": 15,
                        "total": 15
                    },
                    "agentSupportsReport": true,
                    "groupNotFound": false,
                    "lastUpdate": "2022-03-11T12:44:19.294889Z",
                    "latestReport": "/threats/mitigation-report/1373834706275925531",
                    "mitigationEndedAt": "2022-03-11T12:44:17.112000Z",
                    "mitigationStartedAt": "2022-03-11T12:44:17.111000Z",
                    "status": "success"
                }
            ],
            "threatInfo": {
                "externalTicketExists": false,
                "mitigatedPreemptively": false,
                "reachedEventsLimit": false,
                "analystVerdict": "undefined",
                "analystVerdictDescription": "Undefined",
                "automaticallyResolved": false,
                "classificationSource": "Static",
                "collectionId": "1370955486150335176",
                "detectionEngines": [
                    {
                        "key": "executables",
                        "title": "Behavioral AI"
                    }
                ],
                "detectionType": "dynamic",
                "engines": [
                    "DBT - Executables"
                ],
                "failedActions": false,
                "fileExtension": "EXE",
                "fileExtensionType": "Executable",
                "fileVerificationType": "SignedVerified",
                "incidentStatus": "unresolved",
                "incidentStatusDescription": "Unresolved",
                "initiatedBy": "agent_policy",
                "initiatedByDescription": "Agent Policy",
                "isFileless": false,
                "isValidCertificate": true,
                "maliciousProcessArguments": "\"C:\\Users\\USERNAME\\Downloads\\OfficeTimeline.exe\"",
                "mitigationStatus": "mitigated",
                "mitigationStatusDescription": "Mitigated",
                "pendingActions": false,
                "publisherName": "OFFICE TIMELINE, LLC",
                "rebootRequired": false,
                "sha1": "25e43630e04e0858418f0b1a3843ddfd626c1fba",
                "storyline": "BB74E569F93D579E",
                "threatId": "1373834705420286869",
                "updatedAt": "2022-03-11T12:44:33.501615Z"
            },
            "whiteningOptions": [
                "certificate",
                "path",
                "hash"
            ]
        },
        "threat": {
            "enrichments": {
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
        },
        "user": {
            "name": "DOMAIN\\USERNAME"
        }
    }
    	
	```


=== "threat3_empty_ipv6.json"

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
            "name": "OfficeTimeline.exe",
            "extension": "exe",
            "path": "\\Device\\HarddiskVolume3\\Users\\USERNAME\\Downloads\\OfficeTimeline.exe",
            "size": 65517824
        },
        "host": {
            "domain": "DOMAIN",
            "os": {
                "family": "windows",
                "version": "Windows 10 Pro"
            },
            "ip": [
                "192.168.56.1",
                "10.4.4.69",
                "66.66.66.66"
            ],
            "name": "LSYN98873"
        },
        "related": {
            "ip": [
                "10.4.4.69",
                "fe80::e4a1:7fce:33f3:d50e",
                "192.168.56.1",
                "fe80::605f:b34f:31ac:498",
                "66.66.66.66"
            ]
        },
        "organization": {
            "id": "111111111111111111",
            "name": "REDACTED"
        },
        "process": {
            "parent": {
                "name": "chrome.exe"
            }
        },
        "sentinelone": {
            "EventTime": "2022-03-11 14:14:54",
            "agentDetectionInfo": {
                "accountId": "111111111111111111",
                "accountName": "REDACTED",
                "agentDomain": "DOMAIN",
                "agentIpV4": "192.168.56.1,10.4.4.69",
                "agentLastLoggedInUserName": "USERNAME",
                "agentMitigationMode": "protect",
                "agentOsName": "Windows 10 Pro",
                "agentOsRevision": "19044",
                "agentRegisteredAt": "2021-02-10T16:12:18.659760Z",
                "agentUuid": "5e4482b45d134ae8bf4901cb52b65e88",
                "agentVersion": "21.7.5.1080",
                "externalIp": "66.66.66.66",
                "groupId": 1083054176758610128,
                "groupName": "Default Group",
                "siteId": 1083054176741832911,
                "siteName": "REDACTED-Users"
            },
            "agentRealtimeInfo": {
                "activeThreats": 0,
                "agentComputerName": "LSYN98873",
                "agentInfected": false,
                "agentIsActive": true,
                "agentIsDecommissioned": false,
                "rebootRequired": false,
                "agentDomain": "DOMAIN",
                "agentId": "1088377752722254024",
                "agentMachineType": "laptop",
                "agentMitigationMode": "protect",
                "agentNetworkStatus": "connected",
                "agentOsRevision": "19044",
                "agentUuid": "5e4482b45d134ae8bf4901cb52b65e88",
                "agentVersion": "21.7.5.1080",
                "groupId": 1083054176758610128,
                "groupName": "Default Group",
                "networkInterfaces": [
                    {
                        "id": "1373748335430042703",
                        "inet": [
                            "10.4.4.69"
                        ],
                        "inet6": [
                            "fe80::605f:b34f:31ac:498"
                        ],
                        "name": "Ethernet",
                        "physical": "98:fa:9b:5f:f2:bd"
                    },
                    {
                        "id": "1362550279953160460",
                        "inet": [
                            "192.168.56.1"
                        ],
                        "inet6": [
                            "fe80::e4a1:7fce:33f3:d50e"
                        ],
                        "name": "Ethernet 2",
                        "physical": "0a:00:27:00:00:0b"
                    }
                ],
                "operationalState": "na",
                "scanFinishedAt": "2022-01-31T13:56:31.482859Z",
                "scanStartedAt": "2022-01-28T15:25:03.885250Z",
                "scanStatus": "finished",
                "siteId": 1083054176741832911,
                "siteName": "REDACTED-Users",
                "userActionsNeeded": []
            },
            "eventid": 1373834705420286869,
            "indicators": [
                {
                    "category": "Exploitation",
                    "description": "Document behaves abnormally",
                    "ids": [
                        62
                    ],
                    "tactics": [
                        {
                            "name": "Execution",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1059/",
                                    "name": "T1059"
                                },
                                {
                                    "link": "https://attack.mitre.org/techniques/T1203/",
                                    "name": "T1203"
                                },
                                {
                                    "link": "https://attack.mitre.org/techniques/T1204/002",
                                    "name": "T1204.002"
                                }
                            ]
                        },
                        {
                            "name": "Initial Access",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1566/001/",
                                    "name": "T1566.001"
                                }
                            ]
                        }
                    ]
                },
                {
                    "category": "Persistence",
                    "description": "Application registered itself to become persistent via scheduled task",
                    "ids": [
                        197
                    ],
                    "tactics": [
                        {
                            "name": "Persistence",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1053/005/",
                                    "name": "T1053.005"
                                }
                            ]
                        }
                    ]
                },
                {
                    "category": "Evasion",
                    "description": "Suspicious registry key was created",
                    "ids": [
                        171
                    ],
                    "tactics": [
                        {
                            "name": "Defense Evasion",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1112/",
                                    "name": "T1112"
                                }
                            ]
                        }
                    ]
                },
                {
                    "category": "Injection",
                    "description": "Suspicious library loaded into the process memory",
                    "ids": [
                        126
                    ],
                    "tactics": []
                },
                {
                    "category": "General",
                    "description": "User logged on",
                    "ids": [
                        266
                    ],
                    "tactics": [
                        {
                            "name": "Persistence",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1078/",
                                    "name": "T1078"
                                }
                            ]
                        }
                    ]
                },
                {
                    "category": "Persistence",
                    "description": "Application registered itself to become persistent via an autorun",
                    "ids": [
                        199
                    ],
                    "tactics": [
                        {
                            "name": "Persistence",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1547/001/",
                                    "name": "T1547.001"
                                }
                            ]
                        },
                        {
                            "name": "Privilege Escalation",
                            "source": "MITRE",
                            "techniques": [
                                {
                                    "link": "https://attack.mitre.org/techniques/T1547/001/",
                                    "name": "T1547.001"
                                }
                            ]
                        }
                    ]
                }
            ],
            "mitigationStatus": [
                {
                    "action": "quarantine",
                    "actionsCounters": {
                        "failed": 0,
                        "notFound": 0,
                        "pendingReboot": 0,
                        "success": 172,
                        "total": 172
                    },
                    "agentSupportsReport": true,
                    "groupNotFound": false,
                    "lastUpdate": "2022-03-11T12:44:33.508808Z",
                    "latestReport": "/threats/mitigation-report/1373834825528452160",
                    "mitigationEndedAt": "2022-03-11T12:44:32.875000Z",
                    "mitigationStartedAt": "2022-03-11T12:44:18.331000Z",
                    "status": "success"
                },
                {
                    "action": "kill",
                    "actionsCounters": {
                        "failed": 0,
                        "notFound": 0,
                        "pendingReboot": 0,
                        "success": 15,
                        "total": 15
                    },
                    "agentSupportsReport": true,
                    "groupNotFound": false,
                    "lastUpdate": "2022-03-11T12:44:19.294889Z",
                    "latestReport": "/threats/mitigation-report/1373834706275925531",
                    "mitigationEndedAt": "2022-03-11T12:44:17.112000Z",
                    "mitigationStartedAt": "2022-03-11T12:44:17.111000Z",
                    "status": "success"
                }
            ],
            "threatInfo": {
                "externalTicketExists": false,
                "mitigatedPreemptively": false,
                "reachedEventsLimit": false,
                "analystVerdict": "undefined",
                "analystVerdictDescription": "Undefined",
                "automaticallyResolved": false,
                "classificationSource": "Static",
                "collectionId": "1370955486150335176",
                "detectionEngines": [
                    {
                        "key": "executables",
                        "title": "Behavioral AI"
                    }
                ],
                "detectionType": "dynamic",
                "engines": [
                    "DBT - Executables"
                ],
                "failedActions": false,
                "fileExtension": "EXE",
                "fileExtensionType": "Executable",
                "fileVerificationType": "SignedVerified",
                "incidentStatus": "unresolved",
                "incidentStatusDescription": "Unresolved",
                "initiatedBy": "agent_policy",
                "initiatedByDescription": "Agent Policy",
                "isFileless": false,
                "isValidCertificate": true,
                "maliciousProcessArguments": "\"C:\\Users\\USERNAME\\Downloads\\OfficeTimeline.exe\"",
                "mitigationStatus": "mitigated",
                "mitigationStatusDescription": "Mitigated",
                "pendingActions": false,
                "publisherName": "OFFICE TIMELINE, LLC",
                "rebootRequired": false,
                "sha1": "25e43630e04e0858418f0b1a3843ddfd626c1fba",
                "storyline": "BB74E569F93D579E",
                "threatId": "1373834705420286869",
                "updatedAt": "2022-03-11T12:44:33.501615Z"
            },
            "whiteningOptions": [
                "certificate",
                "path",
                "hash"
            ]
        },
        "threat": {
            "enrichments": {
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
        },
        "user": {
            "name": "DOMAIN\\USERNAME"
        }
    }
    	
	```


=== "user_logged_in.json"

    ```json
	
    {
        "action": {
            "type": 27
        },
        "source": {
            "address": "11.22.33.44",
            "ip": "11.22.33.44"
        },
        "user": {
            "id": 111111111111111111,
            "full_name": "Jean DUPONT"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "action": "User Logged In",
            "category": "intrusion_detection",
            "created": "2021-04-23T20:02:05.017771Z",
            "dialect": "sentinelone",
            "id": "2222222222222222222",
            "kind": "event",
            "outcome": "success",
            "reason": "The management user Jean DUPONT logged in to the management console with IP Address 11.22.33.44.",
            "type": [
                "info"
            ]
        },
        "organization": {
            "id": "111111111111111111"
        },
        "sentinelone": {
            "createdAt": "2022-04-01T08:14:35.018328Z",
            "data": {
                "accountName": "CORP",
                "fullScopeDetails": "Account CORP",
                "fullScopeDetailsPath": "Global / CORP",
                "ipAddress": "11.22.33.44",
                "role": "Admin",
                "scopeLevel": "Account",
                "scopeName": "CORP",
                "userScope": "account",
                "source": "mgmt"
            },
            "eventid": 1388919233083515416,
            "updatedAt": "2022-04-01T08:14:35.013748Z"
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
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
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
|`network.direction` | `keyword` | Direction of the network traffic. |
|`network.protocol` | `keyword` | Application protocol name. |
|`orchestrator.cluster.name` | `keyword` | Name of the cluster. |
|`orchestrator.namespace` | `keyword` | Namespace in which the action is taking place. |
|`orchestrator.type` | `keyword` | Orchestrator cluster type (e.g. kubernetes, nomad or cloudfoundry). |
|`organization.id` | `keyword` | None |
|`organization.name` | `keyword` | None |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.hash.md5` | `keyword` | MD5 hash. |
|`process.hash.sha1` | `keyword` | SHA1 hash. |
|`process.hash.sha256` | `keyword` | SHA256 hash. |
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
|`sentinelone.EventTime` | `keyword` | None |
|`sentinelone.agentDetectionInfo.accountId` | `keyword` | None |
|`sentinelone.agentDetectionInfo.accountName` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentDetectionState` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentDomain` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentIpV4` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentIpV6` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentLastLoggedInUserName` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentMitigationMode` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentOsName` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentOsRevision` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentRegisteredAt` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentUuid` | `keyword` | None |
|`sentinelone.agentDetectionInfo.agentVersion` | `keyword` | None |
|`sentinelone.agentDetectionInfo.externalIp` | `keyword` | None |
|`sentinelone.agentDetectionInfo.groupId` | `long` | None |
|`sentinelone.agentDetectionInfo.groupName` | `keyword` | None |
|`sentinelone.agentDetectionInfo.siteId` | `long` | None |
|`sentinelone.agentDetectionInfo.siteName` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.activeThreats` | `long` | None |
|`sentinelone.agentRealtimeInfo.agentComputerName` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentDecommissionedAt` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentDomain` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentId` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentInfected` | `bool` | None |
|`sentinelone.agentRealtimeInfo.agentIsActive` | `bool` | None |
|`sentinelone.agentRealtimeInfo.agentIsDecommissioned` | `bool` | None |
|`sentinelone.agentRealtimeInfo.agentMachineType` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentMitigationMode` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentNetworkStatus` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentOsRevision` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentUuid` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.agentVersion` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.groupId` | `long` | None |
|`sentinelone.agentRealtimeInfo.groupName` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.networkInterfaces` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.operationalState` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.rebootRequired` | `bool` | None |
|`sentinelone.agentRealtimeInfo.scanAbortedAt` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.scanFinishedAt` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.scanStartedAt` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.scanStatus` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.siteId` | `long` | None |
|`sentinelone.agentRealtimeInfo.siteName` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.storageName` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.storageType` | `keyword` | None |
|`sentinelone.agentRealtimeInfo.userActionsNeeded` | `keyword` | None |
|`sentinelone.applications` | `keyword` | None |
|`sentinelone.comments` | `keyword` | None |
|`sentinelone.createdAt` | `keyword` | None |
|`sentinelone.data.accountName` | `keyword` | None |
|`sentinelone.data.action` | `keyword` | None |
|`sentinelone.data.activatedEngines` | `keyword` |  |
|`sentinelone.data.agentipv4` | `keyword` | None |
|`sentinelone.data.alertId` | `long` | None |
|`sentinelone.data.alertid` | `long` | None |
|`sentinelone.data.application` | `keyword` | None |
|`sentinelone.data.applicationType` | `keyword` | None |
|`sentinelone.data.bluetoothAddress` | `keyword` | None |
|`sentinelone.data.byUser` | `keyword` | None |
|`sentinelone.data.computerName` | `keyword` | None |
|`sentinelone.data.confidenceLevel` | `keyword` | None |
|`sentinelone.data.createdAt` | `keyword` | None |
|`sentinelone.data.createdByUsername` | `keyword` | None |
|`sentinelone.data.creator` | `keyword` | None |
|`sentinelone.data.current` | `keyword` |  |
|`sentinelone.data.deactivatedEngines` | `keyword` |  |
|`sentinelone.data.deactivationPeriodInDays` | `keyword` | None |
|`sentinelone.data.detectedat` | `long` | None |
|`sentinelone.data.deviceClass` | `keyword` | None |
|`sentinelone.data.deviceInformationServiceInfoKey` | `keyword` | None |
|`sentinelone.data.deviceInformationServiceInfoValue` | `keyword` | None |
|`sentinelone.data.deviceName` | `keyword` | None |
|`sentinelone.data.direction` | `keyword` | None |
|`sentinelone.data.disabledLevel` | `keyword` | None |
|`sentinelone.data.dnsrequest` | `keyword` | None |
|`sentinelone.data.dnsresponse` | `keyword` | None |
|`sentinelone.data.dstip` | `keyword` | None |
|`sentinelone.data.dstport` | `long` | None |
|`sentinelone.data.durationOfMeasurement` | `int` | None |
|`sentinelone.data.dveventid` | `keyword` | None |
|`sentinelone.data.dveventtype` | `keyword` | None |
|`sentinelone.data.enabledReason` | `keyword` | None |
|`sentinelone.data.escapedMaliciousProcessArguments` | `keyword` | None |
|`sentinelone.data.eventId` | `keyword` | None |
|`sentinelone.data.eventTime` | `keyword` | None |
|`sentinelone.data.eventType` | `keyword` | None |
|`sentinelone.data.exclusionType` | `keyword` | None |
|`sentinelone.data.expiration` | `keyword` |  |
|`sentinelone.data.externalIp` | `keyword` | None |
|`sentinelone.data.externalip` | `keyword` | None |
|`sentinelone.data.fileContentHash` | `keyword` | None |
|`sentinelone.data.fileDisplayName` | `keyword` | None |
|`sentinelone.data.fullScopeDetails` | `keyword` | None |
|`sentinelone.data.fullScopeDetailsPath` | `keyword` | None |
|`sentinelone.data.gattService` | `keyword` | None |
|`sentinelone.data.globalStatus` | `keyword` | None |
|`sentinelone.data.groupId` | `long` | None |
|`sentinelone.data.groupName` | `keyword` | None |
|`sentinelone.data.indicatorcategory` | `keyword` | None |
|`sentinelone.data.indicatordescription` | `keyword` | None |
|`sentinelone.data.indicatorname` | `keyword` | None |
|`sentinelone.data.interface` | `keyword` | None |
|`sentinelone.data.ipAddress` | `keyword` | None |
|`sentinelone.data.k8sclustername` | `keyword` | None |
|`sentinelone.data.k8scontainerid` | `keyword` | None |
|`sentinelone.data.k8scontainerimage` | `keyword` | None |
|`sentinelone.data.k8scontainerlabels` | `keyword` | None |
|`sentinelone.data.k8scontainername` | `keyword` | None |
|`sentinelone.data.k8scontrollerkind` | `keyword` | None |
|`sentinelone.data.k8scontrollerlabels` | `keyword` | None |
|`sentinelone.data.k8scontrollername` | `keyword` | None |
|`sentinelone.data.k8snamespace` | `keyword` | None |
|`sentinelone.data.k8snamespacelabels` | `keyword` | None |
|`sentinelone.data.k8snode` | `keyword` | None |
|`sentinelone.data.k8spod` | `keyword` | None |
|`sentinelone.data.k8spodlabels` | `keyword` | None |
|`sentinelone.data.lastLoggedInUserName` | `keyword` | None |
|`sentinelone.data.lmpVersion` | `keyword` | None |
|`sentinelone.data.localHost` | `keyword` | None |
|`sentinelone.data.localHostType` | `keyword` | None |
|`sentinelone.data.localPortType` | `keyword` | None |
|`sentinelone.data.localPorts` | `keyword` | None |
|`sentinelone.data.locationNames` | `array` | None |
|`sentinelone.data.loginaccountdomain` | `keyword` | None |
|`sentinelone.data.loginaccountsid` | `keyword` | None |
|`sentinelone.data.loginisadministratorequivalent` | `keyword` | None |
|`sentinelone.data.loginissuccessful` | `keyword` | None |
|`sentinelone.data.loginsusername` | `keyword` | None |
|`sentinelone.data.logintype` | `keyword` | None |
|`sentinelone.data.manufacturerName` | `keyword` | None |
|`sentinelone.data.minorClass` | `keyword` | None |
|`sentinelone.data.minorClasses` | `keyword` |  |
|`sentinelone.data.modulepath` | `keyword` | None |
|`sentinelone.data.modulesha1` | `keyword` | None |
|`sentinelone.data.neteventdirection` | `keyword` | None |
|`sentinelone.data.newGroupId` | `keyword` | None |
|`sentinelone.data.newGroupName` | `keyword` | None |
|`sentinelone.data.newStatus` | `keyword` | None |
|`sentinelone.data.numberOfEvents` | `int` | None |
|`sentinelone.data.oldGroupId` | `keyword` | None |
|`sentinelone.data.oldGroupName` | `keyword` | None |
|`sentinelone.data.order` | `long` | None |
|`sentinelone.data.origagentmachinetype` | `keyword` | None |
|`sentinelone.data.origagentname` | `keyword` | None |
|`sentinelone.data.origagentosfamily` | `keyword` | None |
|`sentinelone.data.origagentosname` | `keyword` | None |
|`sentinelone.data.origagentosrevision` | `keyword` | None |
|`sentinelone.data.origagentsiteid` | `long` | None |
|`sentinelone.data.origagentuuid` | `keyword` | None |
|`sentinelone.data.origagentversion` | `keyword` | None |
|`sentinelone.data.originalStatus` | `keyword` | None |
|`sentinelone.data.osType` | `keyword` | None |
|`sentinelone.data.osTypes` | `keyword` | None |
|`sentinelone.data.physical` | `keyword` | None |
|`sentinelone.data.policy` | `keyword` |  |
|`sentinelone.data.policyName` | `keyword` |  |
|`sentinelone.data.previous` | `keyword` |  |
|`sentinelone.data.processId` | `int` | None |
|`sentinelone.data.processName` | `keyword` | None |
|`sentinelone.data.productId` | `keyword` | None |
|`sentinelone.data.profileUuids` | `keyword` | None |
|`sentinelone.data.protocol` | `keyword` | None |
|`sentinelone.data.reason` | `keyword` | None |
|`sentinelone.data.registrykeypath` | `keyword` | None |
|`sentinelone.data.registryoldvalue` | `keyword` | None |
|`sentinelone.data.registryoldvaluetype` | `keyword` | None |
|`sentinelone.data.registrypath` | `keyword` | None |
|`sentinelone.data.registryvalue` | `keyword` | None |
|`sentinelone.data.remoteHost` | `keyword` | None |
|`sentinelone.data.remoteHostType` | `keyword` | None |
|`sentinelone.data.remotePortType` | `keyword` | None |
|`sentinelone.data.remotePorts` | `keyword` | None |
|`sentinelone.data.role` | `keyword` | None |
|`sentinelone.data.ruleScopeLevel` | `keyword` | None |
|`sentinelone.data.ruleScopeName` | `keyword` | None |
|`sentinelone.data.ruleType` | `keyword` | None |
|`sentinelone.data.rulescopeid` | `long` | None |
|`sentinelone.data.rulescopelevel` | `keyword` | None |
|`sentinelone.data.scopeId` | `long` | None |
|`sentinelone.data.scopeLevel` | `keyword` | None |
|`sentinelone.data.scopeName` | `keyword` | None |
|`sentinelone.data.setting` | `keyword` |  |
|`sentinelone.data.severity` | `keyword` | None |
|`sentinelone.data.shouldReboot` | `keyword` |  |
|`sentinelone.data.siteName` | `keyword` | None |
|`sentinelone.data.source` | `keyword` | None |
|`sentinelone.data.sourcename` | `keyword` | None |
|`sentinelone.data.sourceparentprocesscommandline` | `keyword` | None |
|`sentinelone.data.sourceparentprocessintegritylevel` | `keyword` | None |
|`sentinelone.data.sourceparentprocesskey` | `keyword` | None |
|`sentinelone.data.sourceparentprocessmd5` | `keyword` | None |
|`sentinelone.data.sourceparentprocessname` | `keyword` | None |
|`sentinelone.data.sourceparentprocesspath` | `keyword` | None |
|`sentinelone.data.sourceparentprocesspid` | `long` | None |
|`sentinelone.data.sourceparentprocesssha1` | `keyword` | None |
|`sentinelone.data.sourceparentprocesssha256` | `keyword` | None |
|`sentinelone.data.sourceparentprocesssigneridentity` | `keyword` | None |
|`sentinelone.data.sourceparentprocessstarttime` | `long` | None |
|`sentinelone.data.sourceparentprocessstoryline` | `keyword` | None |
|`sentinelone.data.sourceparentprocesssubsystem` | `keyword` | None |
|`sentinelone.data.sourceparentprocessusername` | `keyword` | None |
|`sentinelone.data.sourceprocesscommandline` | `keyword` | None |
|`sentinelone.data.sourceprocessfilepath` | `keyword` | None |
|`sentinelone.data.sourceprocessfilesigneridentity` | `keyword` | None |
|`sentinelone.data.sourceprocessfilesingeridentity` | `keyword` | None |
|`sentinelone.data.sourceprocessintegritylevel` | `keyword` | None |
|`sentinelone.data.sourceprocesskey` | `keyword` | None |
|`sentinelone.data.sourceprocessmd5` | `keyword` | None |
|`sentinelone.data.sourceprocessname` | `keyword` | None |
|`sentinelone.data.sourceprocesspid` | `long` | None |
|`sentinelone.data.sourceprocesssha1` | `keyword` | None |
|`sentinelone.data.sourceprocesssha256` | `keyword` | None |
|`sentinelone.data.sourceprocessstarttime` | `long` | None |
|`sentinelone.data.sourceprocessstoryline` | `keyword` | None |
|`sentinelone.data.sourceprocesssubsystem` | `keyword` | None |
|`sentinelone.data.sourceprocessusername` | `keyword` | None |
|`sentinelone.data.srcip` | `keyword` | None |
|`sentinelone.data.srcmachineip` | `keyword` | None |
|`sentinelone.data.srcport` | `long` | None |
|`sentinelone.data.status` | `keyword` | None |
|`sentinelone.data.system` | `bool` | None |
|`sentinelone.data.systemUser` | `long` | None |
|`sentinelone.data.tagNames` | `keyword` | None |
|`sentinelone.data.tgtfilecreatedat` | `long` | None |
|`sentinelone.data.tgtfilehashsha1` | `keyword` | None |
|`sentinelone.data.tgtfilehashsha256` | `keyword` | None |
|`sentinelone.data.tgtfileid` | `keyword` | None |
|`sentinelone.data.tgtfileissigned` | `keyword` | None |
|`sentinelone.data.tgtfilemodifiedat` | `long` | None |
|`sentinelone.data.tgtfileoldpath` | `keyword` | None |
|`sentinelone.data.tgtfilepath` | `keyword` | None |
|`sentinelone.data.tgtproccmdline` | `keyword` | None |
|`sentinelone.data.tgtprocessstarttime` | `keyword` | None |
|`sentinelone.data.tgtprocimagepath` | `keyword` | None |
|`sentinelone.data.tgtprocintegritylevel` | `keyword` | None |
|`sentinelone.data.tgtprocname` | `keyword` | None |
|`sentinelone.data.tgtprocpid` | `long` | None |
|`sentinelone.data.tgtprocsignedstatus` | `keyword` | None |
|`sentinelone.data.tgtprocstorylineid` | `keyword` | None |
|`sentinelone.data.tgtprocuid` | `keyword` | None |
|`sentinelone.data.threatClassification` | `keyword` | None |
|`sentinelone.data.threatClassificationSource` | `keyword` | None |
|`sentinelone.data.tiindicatorcomparisonmethod` | `keyword` | None |
|`sentinelone.data.tiindicatorsource` | `keyword` | None |
|`sentinelone.data.tiindicatortype` | `keyword` | None |
|`sentinelone.data.tiindicatorvalue` | `keyword` | None |
|`sentinelone.data.uid` | `keyword` | None |
|`sentinelone.data.uploadedFilename` | `keyword` |  |
|`sentinelone.data.userId` | `long` | None |
|`sentinelone.data.userScope` | `keyword` | None |
|`sentinelone.data.userscope` | `keyword` |  |
|`sentinelone.data.uuid` | `keyword` | None |
|`sentinelone.data.vendorId` | `long` | None |
|`sentinelone.data.version` | `keyword` | None |
|`sentinelone.description` | `keyword` | None |
|`sentinelone.eventid` | `long` | None |
|`sentinelone.hash` | `keyword` | None |
|`sentinelone.indicators` | `keyword` | None |
|`sentinelone.kubernetesInfo.controllerKind` | `keyword` | None |
|`sentinelone.kubernetesInfo.controllerLabels` | `keyword` | None |
|`sentinelone.kubernetesInfo.controllerName` | `keyword` | None |
|`sentinelone.kubernetesInfo.namespaceLabels` | `keyword` | None |
|`sentinelone.kubernetesInfo.node` | `keyword` | None |
|`sentinelone.kubernetesInfo.pod` | `keyword` | None |
|`sentinelone.kubernetesInfo.podLabels` | `keyword` | None |
|`sentinelone.mitigationStatus` | `keyword` | None |
|`sentinelone.secondaryDescription` | `keyword` | None |
|`sentinelone.siteId` | `long` | None |
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
|`sentinelone.threatInfo.collectionId` | `keyword` | None |
|`sentinelone.threatInfo.detectionEngines` | `keyword` | None |
|`sentinelone.threatInfo.detectionType` | `keyword` | None |
|`sentinelone.threatInfo.engines` | `keyword` | None |
|`sentinelone.threatInfo.externalTicketExists` | `bool` | None |
|`sentinelone.threatInfo.externalTicketId` | `keyword` | None |
|`sentinelone.threatInfo.failedActions` | `bool` | None |
|`sentinelone.threatInfo.fileExtension` | `keyword` | None |
|`sentinelone.threatInfo.fileExtensionType` | `keyword` | None |
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
|`sentinelone.threatInfo.mitigatedPreemptively` | `bool` | None |
|`sentinelone.threatInfo.mitigationStatus` | `keyword` | None |
|`sentinelone.threatInfo.mitigationStatusDescription` | `keyword` | None |
|`sentinelone.threatInfo.pendingActions` | `bool` | None |
|`sentinelone.threatInfo.publisherName` | `keyword` | None |
|`sentinelone.threatInfo.reachedEventsLimit` | `bool` | None |
|`sentinelone.threatInfo.rebootRequired` | `bool` | None |
|`sentinelone.threatInfo.sha1` | `keyword` | None |
|`sentinelone.threatInfo.sha256` | `keyword` | None |
|`sentinelone.threatInfo.storyline` | `keyword` | None |
|`sentinelone.threatInfo.threatId` | `keyword` | None |
|`sentinelone.threatInfo.updatedAt` | `keyword` | None |
|`sentinelone.updatedAt` | `keyword` | None |
|`sentinelone.whiteningOptions` | `keyword` | None |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`threat.enrichments.indicator.file.hash.md5` | `keyword` | MD5 hash. |
|`threat.enrichments.matched.occurred` | `date` | Date of match |
|`threat.indicator.confidence` | `keyword` | Indicator confidence rating |
|`threat.indicator.file.code_signature.signing_id` | `keyword` | The identifier used to sign the process. |
|`threat.indicator.file.created` | `date` | File creation time. |
|`threat.indicator.file.size` | `long` | File size in bytes. |
|`threat.software.type` | `keyword` | Software type. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.full_name` | `keyword` | User's full name, if available. |
|`user.id` | `long` | None |
|`user.name` | `keyword` | Short name or login of the user. |

