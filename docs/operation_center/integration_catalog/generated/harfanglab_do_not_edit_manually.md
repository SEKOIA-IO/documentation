
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Binary file metadata` | to be defined |
| `Disk forensics` | to be defined |
| `File monitoring` | to be defined |
| `Host network interface` | to be defined |
| `Kernel drivers` | to be defined |
| `Loaded DLLs` | to be defined |
| `Named Pipes` | to be defined |
| `PowerShell logs` | to be defined |
| `Process command-line parameters` | to be defined |
| `Process monitoring` | to be defined |
| `Process use of network` | to be defined |
| `Services` | to be defined |
| `Windows event logs` | to be defined |
| `Windows Registry` | registry auditing events are examined in detail |
| `WMI Objects` | Windows WMI Activity events are analyzed, and events related to WMI process too |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `alert`, `event` |
| Category | `network`, `process` |
| Type | `connection`, `info`, `start` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "network.json"

    ```json
	
    {
        "destination": {
            "address": "192.168.120.41",
            "ip": "192.168.120.41",
            "port": 2525
        },
        "agent": {
            "id": "f43cb847-8227-4104-b77f-7fc849789f8e"
        },
        "event": {
            "category": "network",
            "kind": "event",
            "outcome": "success",
            "event": {
                "outcome": "success"
            },
            "type": "connection"
        },
        "host": {
            "domain": "EXAMPLE",
            "hostname": "EXCHANGE",
            "os": {
                "full": "Windows Server 2019 Standard",
                "version": "10.0.17763"
            }
        },
        "process": {
            "executable": "E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Bin\\MSExchangeHMWorker.exe",
            "pid": 14228
        },
        "related": {
            "hosts": [
                "EXCHANGE"
            ],
            "ip": [
                "192.168.120.41"
            ],
            "user": [
                "NT AUTHORITY\\SYSTEM"
            ]
        },
        "source": {
            "address": "192.168.120.41",
            "ip": "192.168.120.41",
            "port": 21955
        },
        "user": {
            "name": "NT AUTHORITY\\SYSTEM"
        }
    }
    	
	```


=== "process.json"

    ```json
	
    {
        "event": {
            "category": "process",
            "kind": "event",
            "type": "start"
        },
        "agent": {
            "id": "f43cb847-8227-4104-b77f-7fc849789f8e"
        },
        "host": {
            "domain": "NIVURA",
            "hostname": "EXCHANGE",
            "os": {
                "full": "Windows Server 2019 Standard",
                "version": "10.0.17763"
            }
        },
        "process": {
            "executable": "C:\\Windows\\System32\\relog.exe",
            "hash": {
                "md5": "4c7a9a333afb2b0896b4e8a948e58b79",
                "sha1": "948febd5456420916256fcc94e3ed19aafe5390b",
                "sha256": "100af46c952e58105dbc51eb92510f6990377a3ffc57e82074a8bfb64c56c529"
            },
            "name": "relog.exe",
            "parent": {
                "executable": "E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Bin\\Microsoft.Exchange.Diagnostics.Service.exe"
            },
            "pe": {
                "company": "Microsoft Corporation",
                "description": "Performance Relogging Utility",
                "file_version": "10.0.17763.1 (WinBuild.160101.0800)",
                "imphash": "6043170F48FA2A2802231975BB43BBDA",
                "original_file_name": "Relog.exe",
                "product": "Microsoft\u00ae Windows\u00ae Operating System"
            },
            "pid": 23272,
            "working_directory": "C:\\Windows\\system32"
        },
        "related": {
            "hash": [
                "948febd5456420916256fcc94e3ed19aafe5390b",
                "4c7a9a333afb2b0896b4e8a948e58b79",
                "100af46c952e58105dbc51eb92510f6990377a3ffc57e82074a8bfb64c56c529"
            ],
            "hosts": [
                "EXCHANGE"
            ],
            "user": [
                "NT AUTHORITY\\SYSTEM"
            ]
        },
        "user": {
            "name": "NT AUTHORITY\\SYSTEM"
        }
    }
    	
	```


=== "process2.json"

    ```json
	
    {
        "message": "{\n  \"@version\": \"1\",\n  \"agent\": {\n    \"agentid\": \"00000000-0000-0000-0000-000000000000\",\n    \"distroid\": null,\n    \"domainname\": \"domain123\",\n    \"ostype\": \"windows\",\n    \"hostname\": \"pc123\",\n    \"osversion\": \"10.0.19041\",\n    \"osproducttype\": \"Windows 10 Pro\",\n    \"domain\": null,\n    \"version\": \"2.12.6\"\n  },\n  \"type\": \"rtlogs\",\n  \"alert_subtype\": \"process\",\n  \"log_type\": \"alert\",\n  \"detection_origin\": \"agent\",\n  \"tenant\": \"\",\n  \"alert_time\": \"2022-03-15T07:26:01.276+00:00\",\n  \"alert_type\": \"sigma\",\n  \"status\": \"false_positive\",\n  \"rule_id\": \"00000000-0000-0000-0000-000000000000\",\n  \"@event_create_date\": \"2022-03-15T07:26:01.276Z\",\n  \"alert_unique_id\": \"00000000-0000-0000-0000-000000000000\",\n  \"level\": \"low\",\n  \"aggregation_key\": \"123456\",\n  \"@timestamp\": \"2022-03-15T07:26:01.311Z\",\n  \"tags\": [\n    \"attack.discovery\",\n    \"attack.t1057\",\n    \"attack.s0057\"\n  ],\n  \"process\": {\n    \"detection_timestamp\": \"2022/03/15 07:24:54.438105\",\n    \"process_unique_id\": \"00000000-0000-0000-0000-000000000000\",\n    \"parent_integrity_level\": \"Medium\",\n    \"log_platform_flag\": 0,\n    \"fake_parent_image\": null,\n    \"pid\": 11320,\n    \"image_name\": \"C:\\\\Windows\\\\SysWOW64\\\\tasklist.exe\",\n    \"username\": \"XXX\\\\XXX\",\n    \"logonid\": 151210562,\n    \"signature_info\": {\n      \"signed_authenticode\": false,\n      \"signed_catalog\": true,\n      \"root_info\": {\n        \"thumbprint\": \"3b1efd3a66ea28b16697394703a72ca340a05bd5\",\n        \"display_name\": \"Microsoft Root Certificate Authority 2010\",\n        \"serial_number\": \"28cc3a25bfba44ac449a9b586b4339aa\",\n        \"issuer_name\": \"Microsoft Root Certificate Authority 2010\"\n      },\n      \"signer_info\": {\n        \"thumbprint\": \"f7c2f2c96a328c13cda8cdb57b715bdea2cbd1d9\",\n        \"display_name\": \"Microsoft Windows\",\n        \"serial_number\": \"33000002ec6579ad1e670890130000000002ec\",\n        \"issuer_name\": \"Microsoft Windows Production PCA 2011\"\n      }\n    },\n    \"current_directory\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\",\n    \"error_msg\": \"\",\n    \"status_msg\": \"sigma match detected this process but not configured to block it\",\n    \"ppid\": 17808,\n    \"fake_parent_commandline\": null,\n    \"commandline\": \"tasklist\",\n    \"signed\": true,\n    \"grandparent_integrity_level\": \"Medium\",\n    \"log_type\": \"process\",\n    \"pe_imphash\": \"19BBD9C4E73C288A3645E163F4B82682\",\n    \"create_time\": \"2022-03-15T07:24:54.260Z\",\n    \"status\": 0,\n    \"parent_image\": \"C:\\\\Windows\\\\SysWOW64\\\\cmd.exe\",\n    \"integrity_level\": \"Medium\",\n    \"usersid\": \"S-1-5-21-299502267-725345543-82448378-2366\",\n    \"pe_info\": {\n      \"product_version\": \"10.0.19041.1\",\n      \"legal_copyright\": \"\u00a9 Microsoft Corporation. All rights reserved.\",\n      \"original_filename\": \"tasklist.exe\",\n      \"company_name\": \"Microsoft Corporation\",\n      \"file_description\": \"Lists the current running tasks\",\n      \"file_version\": \"10.0.19041.1 (WinBuild.160101.0800)\",\n      \"internal_name\": \"tasklist.exe\",\n      \"product_name\": \"Microsoft\u00ae Windows\u00ae Operating System\"\n    },\n    \"session\": 3,\n    \"pe_timestamp\": \"1994-09-11T16:43:21.000Z\",\n    \"parent_unique_id\": \"2332edf8-70c0-43c2-4590-00f912ab3d18\",\n    \"process_name\": \"tasklist.exe\",\n    \"grandparent_commandline\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\\\\EPOSConnect.exe 1\",\n    \"pe_timestamp_int\": 779301801,\n    \"grandparent_image\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\\\\EPOSConnect.exe\",\n    \"parent_commandline\": \"C:\\\\WINDOWS\\\\system32\\\\cmd.exe /d /s /c tasklist\",\n    \"fake_parent_unique_id\": null,\n    \"size\": 79360,\n    \"fake_ppid\": null,\n    \"hashes\": {\n      \"sha1\": \"7f50d8c3cf3ec79122a876e969bdb65d939becd0\",\n      \"sha256\": \"76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4\",\n      \"md5\": \"0a4448b31ce7f83cb7691a2657f330f1\"\n    }\n  },\n  \"execution\": 0,\n  \"rule_name\": \"Discovery: Process list\",\n  \"maturity\": \"stable\",\n  \"msg\": \"Detects the execution of tasklist.exe, a tool used to gather detailed information about a computer's active processes.\"\n}\n",
        "agent": {
            "id": "00000000-0000-0000-0000-000000000000"
        },
        "event": {
            "category": "process",
            "event": {
                "outcome": "success"
            },
            "kind": "alert",
            "outcome": "success",
            "type": "start"
        },
        "harfanglab": {
            "alert_unique_id": "00000000-0000-0000-0000-000000000000",
            "alert_subtype": "process",
            "alert_time": "2022-03-15T07:26:01.276+00:00",
            "execution": 0,
            "level": "low",
            "status": "false_positive"
        },
        "host": {
            "domain": "domain123",
            "hostname": "pc123",
            "os": {
                "full": "Windows 10 Pro",
                "version": "10.0.19041"
            }
        },
        "related": {
            "hosts": [
                "pc123"
            ]
        },
        "rule": {
            "category": "sigma",
            "description": "Detects the execution of tasklist.exe, a tool used to gather detailed information about a computer's active processes.",
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "Discovery: Process list"
        }
    }
    	
	```


=== "wineventlog.json"

    ```json
	
    {
        "event": {
            "code": "53504",
            "kind": "event",
            "provider": "Microsoft-Windows-PowerShell",
            "type": "info"
        },
        "agent": {
            "id": "f43cb847-8227-4104-b77f-7fc849789f8e"
        },
        "host": {
            "domain": "WORKGROUP",
            "hostname": "DESKTOP-9U3171J",
            "os": {
                "full": "Windows 10 Pro",
                "version": "10.0.19041"
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`agent.id` | `keyword` | Unique identifier of this agent. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.provider` | `keyword` | Source of the event. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.hash.sha1` | `keyword` | SHA1 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`file.pe.company` | `keyword` | Internal company name of the file, provided at compile-time. |
|`file.pe.description` | `keyword` | Internal description of the file, provided at compile-time. |
|`file.pe.file_version` | `keyword` | Process name. |
|`file.pe.imphash` | `keyword` | A hash of the imports in a PE file. |
|`file.pe.original_file_name` | `keyword` | Internal name of the file, provided at compile-time. |
|`file.pe.product` | `keyword` | Internal product name of the file, provided at compile-time. |
|`harfanglab.alert_subtype` | `keyword` | None |
|`harfanglab.alert_time` | `keyword` | None |
|`harfanglab.alert_unique_id` | `keyword` | None |
|`harfanglab.execution` | `long` | None |
|`harfanglab.level` | `keyword` | None |
|`harfanglab.status` | `keyword` | None |
|`host.domain` | `keyword` | Name of the directory the group is a member of. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.os.full` | `keyword` | Operating system name, including the version or code name. |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.hash.md5` | `keyword` | MD5 hash. |
|`process.hash.sha1` | `keyword` | SHA1 hash. |
|`process.hash.sha256` | `keyword` | SHA256 hash. |
|`process.name` | `keyword` | Process name. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.pe.company` | `keyword` | Internal company name of the file, provided at compile-time. |
|`process.pe.description` | `keyword` | Internal description of the file, provided at compile-time. |
|`process.pe.file_version` | `keyword` | Process name. |
|`process.pe.imphash` | `keyword` | A hash of the imports in a PE file. |
|`process.pe.original_file_name` | `keyword` | Internal name of the file, provided at compile-time. |
|`process.pe.product` | `keyword` | Internal product name of the file, provided at compile-time. |
|`process.pid` | `long` | Process id. |
|`process.working_directory` | `keyword` | The working directory of the process. |
|`rule.category` | `keyword` | Rule category |
|`rule.description` | `keyword` | Rule description |
|`rule.id` | `keyword` | Rule ID |
|`rule.name` | `keyword` | Rule name |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`user.name` | `keyword` | Short name or login of the user. |

