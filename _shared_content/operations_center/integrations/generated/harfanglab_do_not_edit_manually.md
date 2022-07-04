
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


=== "alert.json"

    ```json
	
    {
        "agent": {
            "id": "8cb8fb07-ecb4-4537-8a44-451ef855a874",
            "name": "harfanglab"
        },
        "file": {
            "hash": {
                "md5": "46f3fa15de36a0825df4dbfd94614566",
                "sha1": "41453d9b0ae75f687c7720373d7586bc0a9d1607",
                "sha256": "79dd65171cdbc3a1505d11921babf62ffcab4d725ab4a28813c02a6f3a2760ff"
            }
        },
        "host": {
            "domain": "WORKGROUP",
            "hostname": "REDACTED",
            "os": {
                "full": "Windows 10 Pro",
                "version": "10.0.19041"
            }
        },
        "log": {
            "hostname": "REDACTED"
        },
        "process": {
            "name": "mimikatz.exe",
            "command_line": "\"C:\\Users\\valves\\Desktop\\mimikatz.exe\"",
            "executable": "C:\\Users\\valves\\Desktop\\mimikatz.exe",
            "parent": {
                "command_line": "\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\" ",
                "executable": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
            },
            "pe": {
                "company": "Braveheart",
                "description": "mimikatz for Windows",
                "file_version": "2.2.0.0",
                "imphash": "B6BC868F5046CE7764D0627266AF0200",
                "original_file_name": "mimikatz.exe",
                "product": "mimikatz"
            },
            "pid": 5736,
            "working_directory": "C:\\Users\\valves\\Desktop"
        },
        "rule": {
            "category": "yara",
            "description": "Binary was found malicious by 2 rule(s) with a score of 120",
            "id": "YARA binary check",
            "name": "YARA binary check"
        },
        "event": {
            "kind": "alert",
            "category": "process",
            "type": "start",
            "id": "1bc56688-8099-44bd-96c0-1515641070e1",
            "dialect": "harfanglab",
            "created": "2021-04-30T13:21:20.840949+00:00",
            "dialect_uuid": "3c7057d3-4689-4fae-8033-6f1f887a70f2",
            "outcome": "success"
        },
        "harfanglab": {
            "aggregation_key": "40fd5973a79d4e0f21e689938e5f269d20a3be780949eb6f408d5cb65c6974d1",
            "alert_subtype": "process",
            "alert_time": "2021-04-30T13:21:20.704+00:00",
            "alert_unique_id": "bd13fef8-a8fd-4d28-ad97-928a83b96085",
            "execution": 0,
            "level": "high",
            "status": "new"
        },
        "user": {
            "name": "REDACTED\\valves"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "alert_false_positive.json"

    ```json
	
    {
        "harfanglab": {
            "aggregation_key": "123456",
            "alert_subtype": "process",
            "alert_time": "2022-03-15T07:26:01.276+00:00",
            "alert_unique_id": "00000000-0000-0000-0000-000000000000",
            "execution": 0,
            "level": "low",
            "status": "false_positive"
        },
        "agent": {
            "name": "harfanglab",
            "id": "00000000-0000-0000-0000-000000000000"
        },
        "event": {
            "category": "process",
            "kind": "alert",
            "id": "00000000-0000-0000-0000-000000000000",
            "dialect": "harfanglab",
            "created": "2021-04-30T13:21:20.840949+00:00",
            "dialect_uuid": "3c7057d3-4689-4fae-8033-6f1f887a70f2",
            "outcome": "success",
            "type": "start"
        },
        "file": {
            "hash": {
                "md5": "0a4448b31ce7f83cb7691a2657f330f1",
                "sha1": "7f50d8c3cf3ec79122a876e969bdb65d939becd0",
                "sha256": "76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4"
            }
        },
        "host": {
            "domain": "domain123",
            "hostname": "pc123",
            "os": {
                "full": "Windows 10 Pro",
                "version": "10.0.19041"
            }
        },
        "log": {
            "hostname": "pc123"
        },
        "process": {
            "command_line": "tasklist",
            "executable": "C:\\Windows\\SysWOW64\\tasklist.exe",
            "name": "tasklist.exe",
            "parent": {
                "command_line": "C:\\WINDOWS\\system32\\cmd.exe /d /s /c tasklist",
                "executable": "C:\\Windows\\SysWOW64\\cmd.exe"
            },
            "pe": {
                "company": "Microsoft Corporation",
                "description": "Lists the current running tasks",
                "file_version": "10.0.19041.1 (WinBuild.160101.0800)",
                "imphash": "19BBD9C4E73C288A3645E163F4B82682",
                "original_file_name": "tasklist.exe",
                "product": "Microsoft\u00ae Windows\u00ae Operating System"
            },
            "pid": 11320,
            "working_directory": "C:\\Program Files (x86)\\EPOS\\EPOS Connect"
        },
        "rule": {
            "category": "sigma",
            "description": "Detects the execution of tasklist.exe, a tool used to gather detailed information about a computer's active processes.",
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "Discovery: Process list"
        },
        "user": {
            "name": "XXX\\XXX"
        }
    }
    	
	```


=== "investigation.json"

    ```json
	
    {
        "agent": {
            "id": "77af54c8-910f-455d-b887-87cbc87430a4",
            "name": "harfanglab"
        },
        "event": {
            "kind": "event",
            "type": "info",
            "outcome": "success",
            "created": "2021-05-01T07:49:08.292995+00:00",
            "id": "8273efd0-fdba-4df6-aeb1-07595834ee36",
            "dialect": "harfanglab",
            "dialect_uuid": "3c7057d3-4689-4fae-8033-6f1f887a70f2"
        },
        "host": {
            "domain": "WORKGROUP",
            "hostname": "REDACTED",
            "os": {
                "full": "Windows Server 2019 Datacenter",
                "version": "10.0.17763"
            }
        },
        "log": {
            "hostname": "REDACTED"
        },
        "file": {
            "hash": {
                "md5": "8a0a29438052faed8a2532da50455756",
                "sha1": "a1385ce20ad79f55df235effd9780c31442aa234",
                "sha256": "7fd065bac18c5278777ae44908101cdfed72d26fa741367f0ad4d02020787ab6"
            },
            "name": "svchost.exe",
            "path": "C:\\Windows\\System32\\svchost.exe",
            "pe": {
                "company": "Microsoft Corporation",
                "description": "Host Process for Windows Services",
                "file_version": "10.0.17763.1 (WinBuild.160101.0800)",
                "imphash": "247B9220E5D9B720A82B2C8B5069AD69",
                "original_file_name": "svchost.exe",
                "product": "Microsoft\u00ae Windows\u00ae Operating System"
            }
        }
    }
    	
	```


=== "network.json"

    ```json
	
    {
        "destination": {
            "address": "192.168.120.41",
            "ip": "192.168.120.41",
            "port": 2525
        },
        "agent": {
            "name": "harfanglab",
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
        "log": {
            "hostname": "EXCHANGE"
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


=== "network2.json"

    ```json
	
    {
        "agent": {
            "id": "d4e3bf36-929d-4ddf-8526-492e89955808",
            "name": "harfanglab"
        },
        "destination": {
            "address": "172.31.9.222",
            "ip": "172.31.9.222",
            "port": 3389
        },
        "event": {
            "kind": "event",
            "category": "network",
            "type": "connection",
            "outcome": "success",
            "dialect_uuid": "3c7057d3-4689-4fae-8033-6f1f887a70f2",
            "id": "8c1c804b-182b-410a-b7c5-fbea731b750f",
            "created": "2021-05-01T09:55:44.797896+00:00",
            "dialect": "harfanglab"
        },
        "host": {
            "domain": "WORKGROUP",
            "hostname": "REDACTED",
            "os": {
                "full": "Windows Server 2019 Datacenter",
                "version": "10.0.17763"
            }
        },
        "log": {
            "hostname": "REDACTED"
        },
        "process": {
            "executable": "C:\\Windows\\System32\\svchost.exe",
            "pid": 1004
        },
        "source": {
            "address": "185.202.2.238",
            "ip": "185.202.2.238",
            "port": 42221
        },
        "user": {
            "name": "NT AUTHORITY\\NETWORK SERVICE"
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
            "name": "harfanglab",
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
        "log": {
            "hostname": "EXCHANGE"
        },
        "file": {
            "hash": {
                "md5": "4c7a9a333afb2b0896b4e8a948e58b79",
                "sha1": "948febd5456420916256fcc94e3ed19aafe5390b",
                "sha256": "100af46c952e58105dbc51eb92510f6990377a3ffc57e82074a8bfb64c56c529"
            }
        },
        "process": {
            "command_line": "relog.exe E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Logging\\Diagnostics\\PerformanceLogsToBeProcessed\\ExchangeDiagnosticsPerformanceLog_11212058.blg -f csv -o E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Logging\\Diagnostics\\PerformanceLogsToBeProcessed\\ExchangeDiagnosticsPerformanceLog_11212058.csvtmp -y",
            "executable": "C:\\Windows\\System32\\relog.exe",
            "name": "relog.exe",
            "parent": {
                "command_line": "E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Bin\\Microsoft.Exchange.Diagnostics.Service.exe",
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
            "name": "harfanglab",
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
        "file": {
            "hash": {
                "md5": "0a4448b31ce7f83cb7691a2657f330f1",
                "sha1": "7f50d8c3cf3ec79122a876e969bdb65d939becd0",
                "sha256": "76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4"
            }
        },
        "harfanglab": {
            "aggregation_key": "123456",
            "alert_unique_id": "00000000-0000-0000-0000-000000000000",
            "alert_subtype": "process",
            "alert_time": "2022-03-15T07:26:01.276+00:00",
            "execution": 0,
            "level": "low",
            "status": "false_positive"
        },
        "process": {
            "command_line": "tasklist",
            "executable": "C:\\Windows\\SysWOW64\\tasklist.exe",
            "name": "tasklist.exe",
            "parent": {
                "command_line": "C:\\WINDOWS\\system32\\cmd.exe /d /s /c tasklist",
                "executable": "C:\\Windows\\SysWOW64\\cmd.exe"
            },
            "pe": {
                "company": "Microsoft Corporation",
                "description": "Lists the current running tasks",
                "file_version": "10.0.19041.1 (WinBuild.160101.0800)",
                "imphash": "19BBD9C4E73C288A3645E163F4B82682",
                "original_file_name": "tasklist.exe",
                "product": "Microsoft\u00ae Windows\u00ae Operating System"
            },
            "pid": 11320,
            "working_directory": "C:\\Program Files (x86)\\EPOS\\EPOS Connect"
        },
        "host": {
            "domain": "domain123",
            "hostname": "pc123",
            "os": {
                "full": "Windows 10 Pro",
                "version": "10.0.19041"
            }
        },
        "log": {
            "hostname": "pc123"
        },
        "rule": {
            "category": "sigma",
            "description": "Detects the execution of tasklist.exe, a tool used to gather detailed information about a computer's active processes.",
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "Discovery: Process list"
        },
        "user": {
            "name": "XXX\\XXX"
        }
    }
    	
	```


=== "process3.json"

    ```json
	
    {
        "agent": {
            "id": "d4e3bf36-929d-4ddf-8526-492e89955808",
            "name": "harfanglab"
        },
        "event": {
            "kind": "event",
            "category": "process",
            "type": "start",
            "outcome": "success",
            "id": "6826a2a9-8830-46f4-b474-c4ccf7c41f88",
            "created": "2021-05-02T19:52:34.626001+00:00",
            "dialect": "harfanglab",
            "dialect_uuid": "3c7057d3-4689-4fae-8033-6f1f887a70f2"
        },
        "host": {
            "domain": "WORKGROUP",
            "hostname": "REDACTED",
            "os": {
                "full": "Windows Server 2019 Datacenter",
                "version": "10.0.17763"
            }
        },
        "log": {
            "hostname": "REDACTED"
        },
        "file": {
            "hash": {
                "md5": "06c66ff5ccdc2d22344a3eb761a4d38a",
                "sha1": "67c25c8f28b5fa7f5baa85bf1d2726aed48e9cf0",
                "sha256": "b5c78bef3883e3099f7ef844da1446db29107e5c0223b97f29e7fafab5527f15"
            }
        },
        "process": {
            "command_line": "C:\\Windows\\system32\\wbem\\wmiprvse.exe -secured -Embedding",
            "executable": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
            "name": "WmiPrvSE.exe",
            "parent": {
                "command_line": "C:\\Windows\\system32\\svchost.exe -k DcomLaunch -p",
                "executable": "C:\\Windows\\System32\\svchost.exe"
            },
            "pe": {
                "company": "Microsoft Corporation",
                "description": "WMI Provider Host",
                "file_version": "10.0.17763.1 (WinBuild.160101.0800)",
                "imphash": "CFECEDC01015A4FD1BAACAC9E592D88B",
                "original_file_name": "Wmiprvse.exe",
                "product": "Microsoft\u00ae Windows\u00ae Operating System"
            },
            "pid": 4028,
            "working_directory": "C:\\Windows\\system32"
        },
        "user": {
            "name": "NT AUTHORITY\\NETWORK SERVICE"
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
            "name": "harfanglab",
            "id": "f43cb847-8227-4104-b77f-7fc849789f8e"
        },
        "host": {
            "domain": "WORKGROUP",
            "hostname": "DESKTOP-9U3171J",
            "os": {
                "full": "Windows 10 Pro",
                "version": "10.0.19041"
            }
        },
        "log": {
            "hostname": "DESKTOP-9U3171J"
        },
        "action": {
            "id": 53504,
            "properties": {
                "param1": "7092",
                "param2": "DefaultAppDomain"
            }
        }
    }
    	
	```


=== "wineventlog2.json"

    ```json
	
    {
        "event": {
            "dialect_uuid": "3c7057d3-4689-4fae-8033-6f1f887a70f2",
            "id": "8c1c804b-182b-410a-b7c5-fbea731b750f",
            "created": "2021-05-01T09:55:44.797896+00:00",
            "dialect": "harfanglab",
            "provider": "Microsoft-Windows-Security-Auditing",
            "kind": "event",
            "type": "info",
            "code": "4625",
            "outcome": "success"
        },
        "agent": {
            "id": "77af54c8-910f-455d-b887-87cbc87430a4",
            "name": "harfanglab"
        },
        "host": {
            "domain": "WORKGROUP",
            "hostname": "REDACTED",
            "os": {
                "full": "Windows Server 2019 Datacenter",
                "version": "10.0.17763"
            }
        },
        "log": {
            "hostname": "REDACTED"
        },
        "action": {
            "properties": {
                "AuthenticationPackageName": "NTLM",
                "FailureReason": "%%2313",
                "IpAddress": "166.88.151.58",
                "IpPort": "0",
                "KeyLength": "0",
                "LmPackageName": "-",
                "LogonProcessName": "NtLmSsp ",
                "LogonType": "3",
                "ProcessId": "0x0",
                "ProcessName": "-",
                "Status": "0xc000006d",
                "SubStatus": "0xc000006a",
                "SubjectDomainName": "-",
                "SubjectLogonId": "0x0",
                "SubjectUserName": "-",
                "SubjectUserSid": "S-1-0-0",
                "TargetUserName": "ADMINISTRATOR",
                "TargetUserSid": "S-1-0-0",
                "TransmittedServices": "-",
                "WorkstationName": "-"
            },
            "id": 4625
        }
    }
    	
	```


=== "wineventlog3.json"

    ```json
	
    {
        "event": {
            "created": "2022-02-07T13:30:25.317955Z",
            "original": "uRj4yUOMrLDlgLT3thJGDJrLrodS7GIDdL6fiWnt4IMOQkw4822dnPq93BB9Xiy0",
            "dialect_uuid": "c9a1fcc4-37f4-4805-b163-3fdda8eb8029",
            "id": "b81c7b8f-6c25-4dc0-84e5-333874f9170e",
            "outcome": "success",
            "kind": "event",
            "type": "info",
            "code": "1116",
            "dialect": "harfanglab",
            "provider": "Microsoft-Windows-Windows Defender"
        },
        "agent": {
            "id": "06d70013-58c7-46e3-9231-452a383af90b",
            "name": "harfanglab"
        },
        "host": {
            "domain": "REDACTED",
            "hostname": "REDACTED",
            "os": {
                "full": "Windows Server 2019 Datacenter",
                "version": "10.0.17763"
            }
        },
        "log": {
            "hostname": "REDACTED"
        },
        "action": {
            "properties": {
                "ThreatName": "Exploit:O97M/CVE-2017-11882.SMK",
                "PostCleanStatus": "0",
                "ProductVersion": "4.18.2111.5",
                "DetectionTime": "2022-01-03T05:44:57.284Z",
                "DetectionUser": "AUTORITE NT\\Syst\u00e8me",
                "StatusCode": "1",
                "OriginID": "1",
                "CategoryID": "30",
                "FWLink": "https://go.microsoft.com/fwlink/?linkid=37020&name=Exploit:O97M/CVE-2017-11882.SMK!MTB&threatid=2147772194&enterprise=0",
                "Path": "file:_C:\\Program Files\\Avast\\Amex\\temp\\TMMSG_45AD4A29-D7BD-AE8F-FFBC-4115652291C2",
                "ProcessName": "C:\\Program Files\\Avast\\Amex\\AMEX_secondary.exe",
                "OriginName": "Ordinateur local",
                "ExecutionID": "1",
                "CategoryName": "Attaque",
                "TypeName": "Concret",
                "State": "1",
                "PreExecutionStatus": "0",
                "TypeID": "0",
                "ActionName": "Non applicable",
                "AdditionalActionsString": "No additional actions required",
                "ThreatID": "2147772194",
                "ExecutionName": "Suspendu",
                "SeverityID": "5",
                "ErrorDescription": "L\u2019op\u00e9ration a r\u00e9ussi. ",
                "EngineVersion": "AM: 1.1.18800.4, NIS: 1.1.18800.4",
                "DetectionID": "{2E51DC7F-A01D-4E9E-94C8-782C63D85C6E}",
                "SecurityintelligenceVersion": "AV: 1.355.1292.0, AS: 1.355.1292.0, NIS: 1.355.1292.0",
                "ProductName": "Antivirus Microsoft Defender",
                "ActionID": "9",
                "SourceID": "3",
                "AdditionalActionsID": "0",
                "SourceName": "Protection en temps r\u00e9el",
                "SeverityName": "Grave",
                "ErrorCode": "0x00000000"
            },
            "id": 1116
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`action.properties` | `object` | None |
|`agent.id` | `keyword` | Unique identifier of this agent. |
|`agent.name` | `keyword` | Custom name of the agent. |
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
|`harfanglab.aggregation_key` | `keyword` | None |
|`harfanglab.alert_subtype` | `keyword` | None |
|`harfanglab.alert_time` | `keyword` | None |
|`harfanglab.alert_unique_id` | `keyword` | None |
|`harfanglab.execution` | `long` | None |
|`harfanglab.level` | `keyword` | None |
|`harfanglab.process.powershell.command` | `keyword` | None |
|`harfanglab.status` | `keyword` | None |
|`host.domain` | `keyword` | Name of the directory the group is a member of. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.os.full` | `keyword` | Operating system name, including the version or code name. |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.name` | `keyword` | Process name. |
|`process.parent.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.pe.company` | `keyword` | Internal company name of the file, provided at compile-time. |
|`process.pe.description` | `keyword` | Internal description of the file, provided at compile-time. |
|`process.pe.file_version` | `keyword` | Process name. |
|`process.pe.imphash` | `keyword` | A hash of the imports in a PE file. |
|`process.pe.original_file_name` | `keyword` | Internal name of the file, provided at compile-time. |
|`process.pe.product` | `keyword` | Internal product name of the file, provided at compile-time. |
|`process.pid` | `long` | Process id. |
|`process.working_directory` | `keyword` | The working directory of the process. |
|`registry.hive` | `keyword` | Abbreviated name for the hive. |
|`registry.key` | `keyword` | Hive-relative path of keys. |
|`registry.path` | `keyword` | Full path, including hive, key and value |
|`registry.value` | `keyword` | Name of the value written. |
|`rule.category` | `keyword` | Rule category |
|`rule.description` | `keyword` | Rule description |
|`rule.id` | `keyword` | Rule ID |
|`rule.name` | `keyword` | Rule name |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`user.name` | `keyword` | Short name or login of the user. |

