
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Access tokens` | security identifiers are extracted from several events |
| `Anti-virus` | Windows Defender events are analyzed, and need to be specifically set up |
| `Authentication logs` | audit logon events are examined in detail |
| `DLL monitoring` | information about dlls are extracted from several events |
| `File monitoring` | information about files are extracted from several events |
| `Host network interface` | Windows Filtering Platform collects information on processes having network activities |
| `Loaded DLLs` | Sysmon events provide information on DLL loading |
| `PowerShell logs` | Windows PowerShell logs are analyzed, and need to be specifically set up |
| `Process command-line parameters` | Windows Security Auditing logs provide information about process creation |
| `Process monitoring` | Windows Security Auditing logs are process tracking events |
| `Process use of network` | Windows Filtering Platform collects information on processes having network activities |
| `Windows event logs` | events related to Windows Event logs shutdown or restart are analyzed |
| `Windows Registry` | registry auditing events are examined in detail |
| `WMI Objects` | Windows WMI Activity events are analyzed, and events related to WMI process too |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "dns_results.json"

    ```json
	
    {
        "@timestamp": "2022-06-02T12:23:19.097868Z",
        "agent": {
            "id": "c7a2ee33b4ac7c46c28c597d69f4d9ad327ead3601af4375d68bc250eb62e857",
            "version": "0.1.0"
        },
        "action": {
            "id": 22,
            "properties": {
                "Image": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                "Keywords": "0x8000000000000000",
                "ProcessGuid": "{033fb112-653e-6298-8301-000000001000}",
                "ProviderGuid": "{5770385F-C22A-43E0-BF4C-06F5698FFBD9}",
                "RuleName": "-",
                "Severity": "INFO",
                "SourceName": "Microsoft-Windows-Sysmon",
                "User": "TEST-PC\\test",
                "UtcTime": "2022-06-02 12:23:18.607"
            }
        },
        "dns": {
            "answers": [
                {
                    "name": "scontent.xx.fbcdn.net",
                    "type": "CNAME"
                },
                {
                    "data": "157.240.21.20",
                    "type": "A"
                },
                {
                    "data": "185.89.219.11",
                    "type": "A"
                },
                {
                    "data": "129.134.30.11",
                    "type": "A"
                },
                {
                    "data": "185.89.218.11",
                    "type": "A"
                },
                {
                    "data": "129.134.31.11",
                    "type": "A"
                },
                {
                    "data": "2a03:2880:f1fd:b:face:b00c:0:99",
                    "type": "AAAA"
                },
                {
                    "data": "2a03:2880:f0fc:b:face:b00c:0:99",
                    "type": "AAAA"
                },
                {
                    "data": "2a03:2880:f1fc:b:face:b00c:0:99",
                    "type": "AAAA"
                },
                {
                    "data": "2a03:2880:f0fd:b:face:b00c:0:99",
                    "type": "AAAA"
                }
            ],
            "question": {
                "name": "connect.facebook.net",
                "size_in_char": 20
            },
            "response_code": "0"
        },
        "event": {
            "code": "22",
            "provider": "Microsoft-Windows-Sysmon"
        },
        "host": {
            "hostname": "test-PC"
        },
        "process": {
            "executable": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "name": "chrome.exe",
            "pid": 6440
        },
        "user": {
            "name": "test",
            "domain": "TEST-PC"
        },
        "related": {
            "hosts": [
                "test-PC"
            ],
            "user": [
                "test"
            ]
        }
    }
    	
	```


=== "endpoint_stats_event.json"

    ```json
	
    {
        "@timestamp": "2022-06-02T12:18:37.6722336Z",
        "agent": {
            "id": "c7a2ee33b4ac7c46c28c597d69f4d9ad327ead3601af4375d68bc250eb62e857",
            "version": "0.1.0"
        },
        "event": {
            "action": "stats",
            "category": "host",
            "kind": "metric",
            "type": "info"
        },
        "host": {
            "hostname": "test-PC",
            "uptime": 17899
        },
        "sekoiaio": {
            "agent": {
                "cpu_usage": 0.26030037,
                "memory_usage": 0.14199863
            },
            "intake": {
                "dialect": "sekoiaio-endpoint",
                "dialect_uuid": "250e4095-fa08-4101-bb02-e72f870fcbd1"
            },
            "host": {
                "cpu_usage": 12.285156,
                "memory_total": 16961064960,
                "memory_available": 8049606656,
                "memory_usage": 52
            }
        },
        "related": {
            "hosts": [
                "test-PC"
            ]
        }
    }
    	
	```


=== "windows_defender.json"

    ```json
	
    {
        "@timestamp": "2022-06-23T13:10:31.7691464Z",
        "agent": {
            "id": "3598e70397f8931e6288d7aa4075d336bee33fa6224627218e7b67587c3a62e9",
            "version": "0.1.0"
        },
        "action": {
            "id": 1151,
            "properties": {
                "AS security intelligence creation time": "23/06/2022 03:14:37",
                "AS security intelligence version": "1.369.112.0",
                "AV security intelligence creation time": "23/06/2022 03:14:37",
                "AV security intelligence version": "1.369.112.0",
                "BM state": "Activ\u00e9",
                "Engine up-to-date": "0",
                "Engine version": "1.1.19300.2",
                "IOAV state": "Activ\u00e9",
                "Keywords": "0x8000000000000000",
                "Last AS security intelligence age": "0",
                "Last AV security intelligence age": "0",
                "Last full scan age": "4294967295",
                "Last full scan end time": "01/01/1601 00:00:00",
                "Last full scan source": "0",
                "Last full scan start time": "01/01/1601 00:00:00",
                "Last quick scan age": "1",
                "Last quick scan end time": "22/06/2022 10:01:43",
                "Last quick scan source": "2",
                "Last quick scan start time": "22/06/2022 10:00:16",
                "Latest engine version": "1.1.19300.2",
                "Latest platform version": "4.18.2205.7",
                "NRI engine version": "1.1.19300.2",
                "NRI security intelligence version": "1.369.112.0",
                "OA state": "Activ\u00e9",
                "Platform up-to-date": "1",
                "Platform version": "4.18.2205.7",
                "Product Name": "Antivirus Microsoft Defender",
                "Product status": "0x00080000",
                "ProviderGuid": "{11CD958A-C507-4EF3-B3F2-5FD9DFBD2C78}",
                "RTP state": "Activ\u00e9",
                "Severity": "INFO",
                "SourceName": "Microsoft-Windows-Windows Defender",
                "Unused": ""
            }
        },
        "event": {
            "code": "1151",
            "provider": "Microsoft-Windows-Windows Defender"
        },
        "host": {
            "hostname": "test-PC"
        },
        "related": {
            "hosts": [
                "test-PC"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.provider` | `keyword` | Source of the event. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |

