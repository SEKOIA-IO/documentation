
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
        "message": "{\"aggregation_key\":\"40fd5973a79d4e0f21e689938e5f269d20a3be780949eb6f408d5cb65c6974d1\",\"type\":\"rtlogs\",\"agent\":{\"osversion\":\"10.0.19041\",\"domainname\":\"WORKGROUP\",\"agentid\":\"8cb8fb07-ecb4-4537-8a44-451ef855a874\",\"osproducttype\":\"Windows 10 Pro\",\"hostname\":\"REDACTED\",\"domain\":null},\"level\":\"high\",\"msg\":\"Binary was found malicious by 2 rule(s) with a score of 120\",\"tags\":[],\"rule_name\":\"YARA binary check\",\"process\":{\"signature_info\":{\"root_info\":{\"display_name\":\"\",\"thumbprint\":\"\",\"serial_number\":\"\",\"issuer_name\":\"\"},\"signed_catalog\":false,\"signer_info\":{\"display_name\":\"\",\"thumbprint\":\"\",\"serial_number\":\"\",\"issuer_name\":\"\"},\"signed_authenticode\":false},\"commandline\":\"\\\"C:\\\\Users\\\\valves\\\\Desktop\\\\mimikatz.exe\\\"\",\"matched_rules_count\":2,\"fake_parent_commandline\":null,\"dont_create_process\":true,\"session\":2,\"pid\":5736,\"process_name\":\"mimikatz.exe\",\"score\":120,\"pe_info\":{\"product_version\":\"2.2.0.0\",\"file_description\":\"mimikatz for Windows\",\"original_filename\":\"mimikatz.exe\",\"internal_name\":\"mimikatz\",\"file_version\":\"2.2.0.0\",\"company_name\":\"Braveheart\",\"legal_copyright\":\"Copyright (c) 2007 - 2020 Braveheart\",\"product_name\":\"mimikatz\"},\"fake_parent_image\":null,\"username\":\"REDACTED\\\\valves\",\"pe_timestamp_int\":1619768223,\"image_name\":\"C:\\\\Users\\\\valves\\\\Desktop\\\\mimikatz.exe\",\"parent_integrity_level\":\"High\",\"fake_parent_unique_id\":null,\"status_msg\":\"Binary was found potentially malicious on the endpoint by Yara with a score of 120 , but it is running in alert only mode\",\"log_type\":\"process\",\"logonid\":1121594,\"process_unique_id\":\"ab376ee3-ecb4-4537-1668-00993e12c556\",\"usersid\":\"S-1-5-21-794873159-2603523847-3490392889-500\",\"error_msg\":\"\",\"parent_image\":\"C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\",\"fake_ppid\":null,\"integrity_level\":\"High\",\"current_directory\":\"C:\\\\Users\\\\valves\\\\Desktop\",\"pe_timestamp\":\"2021-04-30T07:37:03.000Z\",\"parent_unique_id\":\"ab376ee3-ecb4-4537-06a4-0031a7bc3d13\",\"pe_imphash\":\"B6BC868F5046CE7764D0627266AF0200\",\"hashes\":{\"md5\":\"46f3fa15de36a0825df4dbfd94614566\",\"sha256\":\"79dd65171cdbc3a1505d11921babf62ffcab4d725ab4a28813c02a6f3a2760ff\",\"sha1\":\"41453d9b0ae75f687c7720373d7586bc0a9d1607\"},\"size\":1430016,\"matched_rules\":[{\"namespace\":\"mimikatz.yar\",\"rulename\":\"mimikatz_clear_string_markers\",\"source\":\"default\"},{\"namespace\":\"mimikatz.yar\",\"rulename\":\"mimikatz_patches_x64\",\"source\":\"default\"}],\"create_time\":\"2021/04/30 13:20:54.315189\",\"parent_commandline\":\"\\\"C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\\\" \",\"rule_revision\":81,\"signed\":false,\"ppid\":1700,\"status\":0},\"alert_time\":\"2021-04-30T13:21:20.704+00:00\",\"alert_subtype\":\"process\",\"execution\":0,\"alert_type\":\"yara\",\"rule_id\":\"YARA binary check\",\"@version\":\"1\",\"@timestamp\":\"2021-04-30T13:21:20.717Z\",\"@event_create_date\":\"2021-04-30T13:21:20.704Z\",\"log_type\":\"alert\",\"status\":\"new\",\"alert_unique_id\":\"bd13fef8-a8fd-4d28-ad97-928a83b96085\"}",
        "event": {
            "category": [
                "process"
            ],
            "type": [
                "start"
            ],
            "kind": "alert"
        },
        "@timestamp": "2021-04-30T13:21:20.704Z",
        "agent": {
            "id": "8cb8fb07-ecb4-4537-8a44-451ef855a874",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "REDACTED"
        },
        "host": {
            "hostname": "REDACTED",
            "domain": "WORKGROUP",
            "os": {
                "version": "10.0.19041",
                "full": "Windows 10 Pro"
            },
            "name": "REDACTED"
        },
        "harfanglab": {
            "level": "high",
            "alert_time": "2021-04-30T13:21:20.704+00:00",
            "alert_unique_id": "bd13fef8-a8fd-4d28-ad97-928a83b96085",
            "alert_subtype": "process",
            "execution": 0,
            "status": "new",
            "aggregation_key": "40fd5973a79d4e0f21e689938e5f269d20a3be780949eb6f408d5cb65c6974d1"
        },
        "rule": {
            "description": "Binary was found malicious by 2 rule(s) with a score of 120",
            "name": "YARA binary check",
            "category": "yara",
            "id": "YARA binary check"
        },
        "process": {
            "command_line": "\"C:\\Users\\valves\\Desktop\\mimikatz.exe\"",
            "pid": 5736,
            "name": "mimikatz.exe",
            "pe": {
                "description": "mimikatz for Windows",
                "original_file_name": "mimikatz.exe",
                "file_version": "2.2.0.0",
                "company": "Braveheart",
                "product": "mimikatz",
                "imphash": "B6BC868F5046CE7764D0627266AF0200"
            },
            "executable": "C:\\Users\\valves\\Desktop\\mimikatz.exe",
            "parent": {
                "executable": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "command_line": "\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\" "
            },
            "working_directory": "C:\\Users\\valves\\Desktop"
        },
        "user": {
            "name": "REDACTED\\valves"
        },
        "file": {
            "hash": {
                "md5": "46f3fa15de36a0825df4dbfd94614566",
                "sha256": "79dd65171cdbc3a1505d11921babf62ffcab4d725ab4a28813c02a6f3a2760ff",
                "sha1": "41453d9b0ae75f687c7720373d7586bc0a9d1607"
            }
        },
        "related": {
            "hash": [
                "41453d9b0ae75f687c7720373d7586bc0a9d1607",
                "46f3fa15de36a0825df4dbfd94614566",
                "79dd65171cdbc3a1505d11921babf62ffcab4d725ab4a28813c02a6f3a2760ff"
            ],
            "hosts": [
                "REDACTED"
            ],
            "user": [
                "REDACTED\\valves"
            ]
        }
    }
    	
	```


=== "alert_false_positive.json"

    ```json
	
    {
        "message": "{\n  \"@version\": \"1\",\n  \"agent\": {\n    \"agentid\": \"00000000-0000-0000-0000-000000000000\",\n    \"distroid\": null,\n    \"domainname\": \"domain123\",\n    \"ostype\": \"windows\",\n    \"hostname\": \"pc123\",\n    \"osversion\": \"10.0.19041\",\n    \"osproducttype\": \"Windows 10 Pro\",\n    \"domain\": null,\n    \"version\": \"2.12.6\"\n  },\n  \"type\": \"rtlogs\",\n  \"alert_subtype\": \"process\",\n  \"log_type\": \"alert\",\n  \"detection_origin\": \"agent\",\n  \"tenant\": \"\",\n  \"alert_time\": \"2022-03-15T07:26:01.276+00:00\",\n  \"alert_type\": \"sigma\",\n  \"status\": \"false_positive\",\n  \"rule_id\": \"00000000-0000-0000-0000-000000000000\",\n  \"@event_create_date\": \"2022-03-15T07:26:01.276Z\",\n  \"alert_unique_id\": \"00000000-0000-0000-0000-000000000000\",\n  \"level\": \"low\",\n  \"aggregation_key\": \"123456\",\n  \"@timestamp\": \"2022-03-15T07:26:01.311Z\",\n  \"tags\": [\n    \"attack.discovery\",\n    \"attack.t1057\",\n    \"attack.s0057\"\n  ],\n  \"process\": {\n    \"detection_timestamp\": \"2022/03/15 07:24:54.438105\",\n    \"process_unique_id\": \"00000000-0000-0000-0000-000000000000\",\n    \"parent_integrity_level\": \"Medium\",\n    \"log_platform_flag\": 0,\n    \"fake_parent_image\": null,\n    \"pid\": 11320,\n    \"image_name\": \"C:\\\\Windows\\\\SysWOW64\\\\tasklist.exe\",\n    \"username\": \"XXX\\\\XXX\",\n    \"logonid\": 151210562,\n    \"signature_info\": {\n      \"signed_authenticode\": false,\n      \"signed_catalog\": true,\n      \"root_info\": {\n        \"thumbprint\": \"3b1efd3a66ea28b16697394703a72ca340a05bd5\",\n        \"display_name\": \"Microsoft Root Certificate Authority 2010\",\n        \"serial_number\": \"28cc3a25bfba44ac449a9b586b4339aa\",\n        \"issuer_name\": \"Microsoft Root Certificate Authority 2010\"\n      },\n      \"signer_info\": {\n        \"thumbprint\": \"f7c2f2c96a328c13cda8cdb57b715bdea2cbd1d9\",\n        \"display_name\": \"Microsoft Windows\",\n        \"serial_number\": \"33000002ec6579ad1e670890130000000002ec\",\n        \"issuer_name\": \"Microsoft Windows Production PCA 2011\"\n      }\n    },\n    \"current_directory\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\",\n    \"error_msg\": \"\",\n    \"status_msg\": \"sigma match detected this process but not configured to block it\",\n    \"ppid\": 17808,\n    \"fake_parent_commandline\": null,\n    \"commandline\": \"tasklist\",\n    \"signed\": true,\n    \"grandparent_integrity_level\": \"Medium\",\n    \"log_type\": \"process\",\n    \"pe_imphash\": \"19BBD9C4E73C288A3645E163F4B82682\",\n    \"create_time\": \"2022-03-15T07:24:54.260Z\",\n    \"status\": 0,\n    \"parent_image\": \"C:\\\\Windows\\\\SysWOW64\\\\cmd.exe\",\n    \"integrity_level\": \"Medium\",\n    \"usersid\": \"S-1-5-21-299502267-725345543-82448378-2366\",\n    \"pe_info\": {\n      \"product_version\": \"10.0.19041.1\",\n      \"legal_copyright\": \"\u00a9 Microsoft Corporation. All rights reserved.\",\n      \"original_filename\": \"tasklist.exe\",\n      \"company_name\": \"Microsoft Corporation\",\n      \"file_description\": \"Lists the current running tasks\",\n      \"file_version\": \"10.0.19041.1 (WinBuild.160101.0800)\",\n      \"internal_name\": \"tasklist.exe\",\n      \"product_name\": \"Microsoft\u00ae Windows\u00ae Operating System\"\n    },\n    \"session\": 3,\n    \"pe_timestamp\": \"1994-09-11T16:43:21.000Z\",\n    \"parent_unique_id\": \"2332edf8-70c0-43c2-4590-00f912ab3d18\",\n    \"process_name\": \"tasklist.exe\",\n    \"grandparent_commandline\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\\\\EPOSConnect.exe 1\",\n    \"pe_timestamp_int\": 779301801,\n    \"grandparent_image\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\\\\EPOSConnect.exe\",\n    \"parent_commandline\": \"C:\\\\WINDOWS\\\\system32\\\\cmd.exe /d /s /c tasklist\",\n    \"fake_parent_unique_id\": null,\n    \"size\": 79360,\n    \"fake_ppid\": null,\n    \"hashes\": {\n      \"sha1\": \"7f50d8c3cf3ec79122a876e969bdb65d939becd0\",\n      \"sha256\": \"76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4\",\n      \"md5\": \"0a4448b31ce7f83cb7691a2657f330f1\"\n    }\n  },\n  \"execution\": 0,\n  \"rule_name\": \"Discovery: Process list\",\n  \"maturity\": \"stable\",\n  \"msg\": \"Detects the execution of tasklist.exe, a tool used to gather detailed information about a computer's active processes.\"\n}\n",
        "event": {
            "category": [
                "process"
            ],
            "type": [
                "start"
            ],
            "kind": "alert"
        },
        "@timestamp": "2022-03-15T07:26:01.276Z",
        "agent": {
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "pc123"
        },
        "host": {
            "hostname": "pc123",
            "domain": "domain123",
            "os": {
                "version": "10.0.19041",
                "full": "Windows 10 Pro"
            },
            "name": "pc123"
        },
        "harfanglab": {
            "level": "low",
            "alert_time": "2022-03-15T07:26:01.276+00:00",
            "alert_unique_id": "00000000-0000-0000-0000-000000000000",
            "alert_subtype": "process",
            "execution": 0,
            "status": "false_positive",
            "aggregation_key": "123456"
        },
        "rule": {
            "description": "Detects the execution of tasklist.exe, a tool used to gather detailed information about a computer's active processes.",
            "name": "Discovery: Process list",
            "category": "sigma",
            "id": "00000000-0000-0000-0000-000000000000"
        },
        "process": {
            "command_line": "tasklist",
            "pid": 11320,
            "name": "tasklist.exe",
            "pe": {
                "description": "Lists the current running tasks",
                "original_file_name": "tasklist.exe",
                "file_version": "10.0.19041.1 (WinBuild.160101.0800)",
                "company": "Microsoft Corporation",
                "product": "Microsoft\u00ae Windows\u00ae Operating System",
                "imphash": "19BBD9C4E73C288A3645E163F4B82682"
            },
            "executable": "C:\\Windows\\SysWOW64\\tasklist.exe",
            "parent": {
                "executable": "C:\\Windows\\SysWOW64\\cmd.exe",
                "command_line": "C:\\WINDOWS\\system32\\cmd.exe /d /s /c tasklist"
            },
            "working_directory": "C:\\Program Files (x86)\\EPOS\\EPOS Connect"
        },
        "user": {
            "name": "XXX\\XXX"
        },
        "file": {
            "hash": {
                "md5": "0a4448b31ce7f83cb7691a2657f330f1",
                "sha256": "76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4",
                "sha1": "7f50d8c3cf3ec79122a876e969bdb65d939becd0"
            }
        },
        "related": {
            "hash": [
                "0a4448b31ce7f83cb7691a2657f330f1",
                "76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4",
                "7f50d8c3cf3ec79122a876e969bdb65d939becd0"
            ],
            "hosts": [
                "pc123"
            ],
            "user": [
                "XXX\\XXX"
            ]
        }
    }
    	
	```


=== "investigation.json"

    ```json
	
    {
        "message": "{\"cmdline\":\"C:\\\\Windows\\\\system32\\\\svchost.exe -k wusvcs -p\",\"session\":0,\"pid\":3092,\"job_id\":\"c0cbd87c-c793-4af9-9ecf-53739f3f27a5\",\"process_bits\":64,\"@timestamp\":\"2021-05-01T07:49:08.043Z\",\"username\":\"NT AUTHORITY\\\\SYSTEM\",\"@version\":\"1\",\"log_type\":\"investigation\",\"binaryinfo\":{\"filename\":\"svchost.exe\",\"fullpath\":\"C:\\\\Windows\\\\System32\\\\svchost.exe\",\"binaryinfo\":{\"root_thumbprint\":\"3b1efd3a66ea28b16697394703a72ca340a05bd5\",\"pe_file_version\":\"10.0.17763.1 (WinBuild.160101.0800)\",\"filesize\":51696,\"signer_serial_number\":\"33000001a90f2d80c9a929387c0000000001a9\",\"pe_timestamp_int\":3103846143,\"pe_legal_copyright\":\"\u00a9 Microsoft Corporation. All rights reserved.\",\"signed_catalog\":false,\"signer_display_name\":\"Microsoft Windows Publisher\",\"sha1\":\"a1385ce20ad79f55df235effd9780c31442aa234\",\"signer_issuer_name\":\"Microsoft Windows Production PCA 2011\",\"signed_authenticode\":true,\"pe_company_name\":\"Microsoft Corporation\",\"md5\":\"8a0a29438052faed8a2532da50455756\",\"pe_product_version\":\"10.0.17763.1\",\"pe_internal_name\":\"svchost.exe\",\"pe_timestamp\":\"2068-05-10 03:29:03.000\",\"root_serial_number\":\"28cc3a25bfba44ac449a9b586b4339aa\",\"pe_imphash\":\"247B9220E5D9B720A82B2C8B5069AD69\",\"sha256\":\"7fd065bac18c5278777ae44908101cdfed72d26fa741367f0ad4d02020787ab6\",\"root_display_name\":\"Microsoft Root Certificate Authority 2010\",\"pe_file_description\":\"Host Process for Windows Services\",\"root_issuer_name\":\"Microsoft Root Certificate Authority 2010\",\"pe_original_filename\":\"svchost.exe\",\"pe_product_name\":\"Microsoft\u00ae Windows\u00ae Operating System\",\"signed\":true,\"signer_thumbprint\":\"458d803a5cf470dd3f01a475214938d97a5051e8\"},\"fullpath_cmdline\":null},\"job_instance_id\":\"c580fa86-4d9c-4cf0-bebf-24d31fc2ff56\",\"integrity_level\":\"Unknown\",\"item_status\":0,\"agent\":{\"osversion\":\"10.0.17763\",\"domainname\":\"WORKGROUP\",\"agentid\":\"77af54c8-910f-455d-b887-87cbc87430a4\",\"osproducttype\":\"Windows Server 2019 Datacenter\",\"hostname\":\"REDACTED\",\"domain\":null},\"object_type\":\"process\",\"mem_working_set\":7553024,\"critical\":true,\"signature_requested\":true,\"create_time\":\"2021-05-01T07:45:59.848Z\",\"name\":\"svchost.exe\",\"maybe_hollow\":false,\"mem_private_bytes\":1777664,\"ppid\":752,\"status\":\"running\",\"exe\":\"C:\\\\Windows\\\\System32\\\\svchost.exe\"}",
        "event": {
            "kind": "event",
            "type": [
                "info"
            ]
        },
        "agent": {
            "id": "77af54c8-910f-455d-b887-87cbc87430a4",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "REDACTED"
        },
        "host": {
            "hostname": "REDACTED",
            "domain": "WORKGROUP",
            "os": {
                "version": "10.0.17763",
                "full": "Windows Server 2019 Datacenter"
            },
            "name": "REDACTED"
        },
        "file": {
            "path": "C:\\Windows\\System32\\svchost.exe",
            "name": "svchost.exe",
            "hash": {
                "md5": "8a0a29438052faed8a2532da50455756",
                "sha1": "a1385ce20ad79f55df235effd9780c31442aa234",
                "sha256": "7fd065bac18c5278777ae44908101cdfed72d26fa741367f0ad4d02020787ab6"
            },
            "pe": {
                "description": "Host Process for Windows Services",
                "original_file_name": "svchost.exe",
                "file_version": "10.0.17763.1 (WinBuild.160101.0800)",
                "company": "Microsoft Corporation",
                "product": "Microsoft\u00ae Windows\u00ae Operating System",
                "imphash": "247B9220E5D9B720A82B2C8B5069AD69"
            }
        },
        "related": {
            "hash": [
                "7fd065bac18c5278777ae44908101cdfed72d26fa741367f0ad4d02020787ab6",
                "8a0a29438052faed8a2532da50455756",
                "a1385ce20ad79f55df235effd9780c31442aa234"
            ],
            "hosts": [
                "REDACTED"
            ]
        }
    }
    	
	```


=== "network.json"

    ```json
	
    {
        "message": "{\"event_id\":3,\"dport\":2525,\"tenant\":\"\",\"initiated\":\"true\",\"image_name\":\"E:\\\\Program Files\\\\Microsoft\\\\Exchange Server\\\\V15\\\\Bin\\\\MSExchangeHMWorker.exe\",\"username\":\"NT AUTHORITY\\\\SYSTEM\",\"saddr\":\"192.168.120.41\",\"agent\":{\"distroid\":null,\"agentid\":\"f43cb847-8227-4104-b77f-7fc849789f8e\",\"domainname\":\"EXAMPLE\",\"ostype\":\"windows\",\"hostname\":\"EXCHANGE\",\"osversion\":\"10.0.17763\",\"domain\":null,\"osproducttype\":\"Windows Server 2019 Standard\"},\"is_ipv6\":\"false\",\"sport\":21955,\"pid\":14228,\"direction\":\"out\",\"conn_type\":0,\"daddr\":\"192.168.120.41\",\"@timestamp\":\"2021-11-21T19:38:44.461Z\",\"@version\":\"1\",\"log_type\":\"network\",\"@event_create_date\":\"2021-11-21T19:38:36.820Z\",\"process_unique_id\":\"2d1de721-5d5a-46b2-3794-0097821d2ab7\"}",
        "event": {
            "category": [
                "network"
            ],
            "type": [
                "connection"
            ],
            "kind": "event"
        },
        "@timestamp": "2021-11-21T19:38:36.820Z",
        "agent": {
            "id": "f43cb847-8227-4104-b77f-7fc849789f8e",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "EXCHANGE"
        },
        "host": {
            "hostname": "EXCHANGE",
            "domain": "EXAMPLE",
            "os": {
                "version": "10.0.17763",
                "full": "Windows Server 2019 Standard"
            },
            "name": "EXCHANGE"
        },
        "destination": {
            "ip": "192.168.120.41",
            "port": 2525,
            "address": "192.168.120.41"
        },
        "source": {
            "ip": "192.168.120.41",
            "port": 21955,
            "address": "192.168.120.41"
        },
        "process": {
            "pid": 14228,
            "executable": "E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Bin\\MSExchangeHMWorker.exe"
        },
        "user": {
            "name": "NT AUTHORITY\\SYSTEM"
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
        }
    }
    	
	```


=== "network2.json"

    ```json
	
    {
        "message": "{\"daddr\":\"172.31.9.222\",\"event_id\":3,\"dport\":3389,\"agent\":{\"osversion\":\"10.0.17763\",\"domainname\":\"WORKGROUP\",\"agentid\":\"d4e3bf36-929d-4ddf-8526-492e89955808\",\"osproducttype\":\"Windows Server 2019 Datacenter\",\"hostname\":\"REDACTED\",\"domain\":null},\"conn_type\":0,\"pid\":1004,\"sport\":42221,\"is_ipv6\":\"false\",\"username\":\"NT AUTHORITY\\\\NETWORK SERVICE\",\"@timestamp\":\"2021-05-01T09:55:44.688Z\",\"@version\":\"1\",\"image_name\":\"C:\\\\Windows\\\\System32\\\\svchost.exe\",\"saddr\":\"185.202.2.238\",\"direction\":\"in\",\"initiated\":\"false\",\"log_type\":\"network\",\"@event_create_date\":\"2021-05-01T09:55:30.372Z\",\"process_unique_id\":\"9aad140d-929d-4ddf-03ec-008c68ef14a0\"}",
        "event": {
            "category": [
                "network"
            ],
            "type": [
                "connection"
            ],
            "kind": "event"
        },
        "@timestamp": "2021-05-01T09:55:30.372Z",
        "agent": {
            "id": "d4e3bf36-929d-4ddf-8526-492e89955808",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "REDACTED"
        },
        "host": {
            "hostname": "REDACTED",
            "domain": "WORKGROUP",
            "os": {
                "version": "10.0.17763",
                "full": "Windows Server 2019 Datacenter"
            },
            "name": "REDACTED"
        },
        "destination": {
            "ip": "172.31.9.222",
            "port": 3389,
            "address": "172.31.9.222"
        },
        "source": {
            "ip": "185.202.2.238",
            "port": 42221,
            "address": "185.202.2.238"
        },
        "process": {
            "pid": 1004,
            "executable": "C:\\Windows\\System32\\svchost.exe"
        },
        "user": {
            "name": "NT AUTHORITY\\NETWORK SERVICE"
        },
        "related": {
            "hosts": [
                "REDACTED"
            ],
            "ip": [
                "172.31.9.222",
                "185.202.2.238"
            ],
            "user": [
                "NT AUTHORITY\\NETWORK SERVICE"
            ]
        }
    }
    	
	```


=== "process.json"

    ```json
	
    {
        "message": "{\"tenant\":\"\",\"usersid\":\"S-1-5-18\",\"hashes\":{\"sha256\":\"100af46c952e58105dbc51eb92510f6990377a3ffc57e82074a8bfb64c56c529\",\"md5\":\"4c7a9a333afb2b0896b4e8a948e58b79\",\"sha1\":\"948febd5456420916256fcc94e3ed19aafe5390b\"},\"status_msg\":\"\",\"username\":\"NT AUTHORITY\\\\SYSTEM\",\"agent\":{\"distroid\":null,\"agentid\":\"f43cb847-8227-4104-b77f-7fc849789f8e\",\"domainname\":\"NIVURA\",\"ostype\":\"windows\",\"hostname\":\"EXCHANGE\",\"osversion\":\"10.0.17763\",\"domain\":null,\"osproducttype\":\"Windows Server 2019 Standard\"},\"status\":0,\"fake_ppid\":null,\"integrity_level\":\"System\",\"signed\":true,\"signature_info\":{\"signed_catalog\":true,\"signer_info\":{\"display_name\":\"Microsoft Windows\",\"issuer_name\":\"Microsoft Windows Production PCA 2011\",\"serial_number\":\"33000002ed2c45e4c145cf48440000000002ed\",\"thumbprint\":\"312860d2047eb81f8f58c29ff19ecdb4c634cf6a\"},\"root_info\":{\"display_name\":\"Microsoft Root Certificate Authority 2010\",\"issuer_name\":\"Microsoft Root Certificate Authority 2010\",\"serial_number\":\"28cc3a25bfba44ac449a9b586b4339aa\",\"thumbprint\":\"3b1efd3a66ea28b16697394703a72ca340a05bd5\"},\"signed_authenticode\":false},\"parent_commandline\":\"E:\\\\Program Files\\\\Microsoft\\\\Exchange Server\\\\V15\\\\Bin\\\\Microsoft.Exchange.Diagnostics.Service.exe\",\"@timestamp\":\"2021-11-21T20:03:15.736Z\",\"parent_image\":\"E:\\\\Program Files\\\\Microsoft\\\\Exchange Server\\\\V15\\\\Bin\\\\Microsoft.Exchange.Diagnostics.Service.exe\",\"log_type\":\"process\",\"current_directory\":\"C:\\\\Windows\\\\system32\",\"pe_imphash\":\"6043170F48FA2A2802231975BB43BBDA\",\"process_unique_id\":\"2d1de721-5d5a-46b2-5ae8-00feb4cdcf56\",\"size\":53760,\"log_platform_flag\":0,\"commandline\":\"relog.exe E:\\\\Program Files\\\\Microsoft\\\\Exchange Server\\\\V15\\\\Logging\\\\Diagnostics\\\\PerformanceLogsToBeProcessed\\\\ExchangeDiagnosticsPerformanceLog_11212058.blg -f csv -o E:\\\\Program Files\\\\Microsoft\\\\Exchange Server\\\\V15\\\\Logging\\\\Diagnostics\\\\PerformanceLogsToBeProcessed\\\\ExchangeDiagnosticsPerformanceLog_11212058.csvtmp -y\",\"session\":0,\"process_name\":\"relog.exe\",\"image_name\":\"C:\\\\Windows\\\\System32\\\\relog.exe\",\"parent_integrity_level\":\"System\",\"fake_parent_commandline\":null,\"pe_timestamp_int\":2652523548,\"error_msg\":\"\",\"parent_unique_id\":\"2d1de721-5d5a-46b2-0c78-009ac6cf01ea\",\"pid\":23272,\"ppid\":3192,\"fake_parent_image\":null,\"@event_create_date\":\"2021-11-21T20:03:08.226Z\",\"@version\":\"1\",\"pe_timestamp\":\"2054-01-20T12:05:48.000Z\",\"fake_parent_unique_id\":null,\"pe_info\":{\"product_version\":\"10.0.17763.1\",\"company_name\":\"Microsoft Corporation\",\"product_name\":\"Microsoft\u00ae Windows\u00ae Operating System\",\"internal_name\":\"Relog.exe\",\"file_description\":\"Performance Relogging Utility\",\"legal_copyright\":\"\u00a9 Microsoft Corporation. All rights reserved.\",\"file_version\":\"10.0.17763.1 (WinBuild.160101.0800)\",\"original_filename\":\"Relog.exe\"},\"logonid\":999}",
        "event": {
            "category": [
                "process"
            ],
            "type": [
                "start"
            ],
            "kind": "event"
        },
        "@timestamp": "2021-11-21T20:03:08.226Z",
        "agent": {
            "id": "f43cb847-8227-4104-b77f-7fc849789f8e",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "EXCHANGE"
        },
        "host": {
            "hostname": "EXCHANGE",
            "domain": "NIVURA",
            "os": {
                "version": "10.0.17763",
                "full": "Windows Server 2019 Standard"
            },
            "name": "EXCHANGE"
        },
        "process": {
            "command_line": "relog.exe E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Logging\\Diagnostics\\PerformanceLogsToBeProcessed\\ExchangeDiagnosticsPerformanceLog_11212058.blg -f csv -o E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Logging\\Diagnostics\\PerformanceLogsToBeProcessed\\ExchangeDiagnosticsPerformanceLog_11212058.csvtmp -y",
            "pid": 23272,
            "name": "relog.exe",
            "pe": {
                "description": "Performance Relogging Utility",
                "original_file_name": "Relog.exe",
                "file_version": "10.0.17763.1 (WinBuild.160101.0800)",
                "company": "Microsoft Corporation",
                "product": "Microsoft\u00ae Windows\u00ae Operating System",
                "imphash": "6043170F48FA2A2802231975BB43BBDA"
            },
            "executable": "C:\\Windows\\System32\\relog.exe",
            "parent": {
                "executable": "E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Bin\\Microsoft.Exchange.Diagnostics.Service.exe",
                "command_line": "E:\\Program Files\\Microsoft\\Exchange Server\\V15\\Bin\\Microsoft.Exchange.Diagnostics.Service.exe",
                "name": "Microsoft.Exchange.Diagnostics.Service.exe"
            },
            "working_directory": "C:\\Windows\\system32"
        },
        "user": {
            "name": "NT AUTHORITY\\SYSTEM"
        },
        "file": {
            "hash": {
                "md5": "4c7a9a333afb2b0896b4e8a948e58b79",
                "sha256": "100af46c952e58105dbc51eb92510f6990377a3ffc57e82074a8bfb64c56c529",
                "sha1": "948febd5456420916256fcc94e3ed19aafe5390b"
            }
        },
        "related": {
            "hash": [
                "100af46c952e58105dbc51eb92510f6990377a3ffc57e82074a8bfb64c56c529",
                "4c7a9a333afb2b0896b4e8a948e58b79",
                "948febd5456420916256fcc94e3ed19aafe5390b"
            ],
            "hosts": [
                "EXCHANGE"
            ],
            "user": [
                "NT AUTHORITY\\SYSTEM"
            ]
        }
    }
    	
	```


=== "process2.json"

    ```json
	
    {
        "message": "{\n  \"@version\": \"1\",\n  \"agent\": {\n    \"agentid\": \"00000000-0000-0000-0000-000000000000\",\n    \"distroid\": null,\n    \"domainname\": \"domain123\",\n    \"ostype\": \"windows\",\n    \"hostname\": \"pc123\",\n    \"osversion\": \"10.0.19041\",\n    \"osproducttype\": \"Windows 10 Pro\",\n    \"domain\": null,\n    \"version\": \"2.12.6\"\n  },\n  \"type\": \"rtlogs\",\n  \"alert_subtype\": \"process\",\n  \"log_type\": \"alert\",\n  \"detection_origin\": \"agent\",\n  \"tenant\": \"\",\n  \"alert_time\": \"2022-03-15T07:26:01.276+00:00\",\n  \"alert_type\": \"sigma\",\n  \"status\": \"false_positive\",\n  \"rule_id\": \"00000000-0000-0000-0000-000000000000\",\n  \"@event_create_date\": \"2022-03-15T07:26:01.276Z\",\n  \"alert_unique_id\": \"00000000-0000-0000-0000-000000000000\",\n  \"level\": \"low\",\n  \"aggregation_key\": \"123456\",\n  \"@timestamp\": \"2022-03-15T07:26:01.311Z\",\n  \"tags\": [\n    \"attack.discovery\",\n    \"attack.t1057\",\n    \"attack.s0057\"\n  ],\n  \"process\": {\n    \"detection_timestamp\": \"2022/03/15 07:24:54.438105\",\n    \"process_unique_id\": \"00000000-0000-0000-0000-000000000000\",\n    \"parent_integrity_level\": \"Medium\",\n    \"log_platform_flag\": 0,\n    \"fake_parent_image\": null,\n    \"pid\": 11320,\n    \"image_name\": \"C:\\\\Windows\\\\SysWOW64\\\\tasklist.exe\",\n    \"username\": \"XXX\\\\XXX\",\n    \"logonid\": 151210562,\n    \"signature_info\": {\n      \"signed_authenticode\": false,\n      \"signed_catalog\": true,\n      \"root_info\": {\n        \"thumbprint\": \"3b1efd3a66ea28b16697394703a72ca340a05bd5\",\n        \"display_name\": \"Microsoft Root Certificate Authority 2010\",\n        \"serial_number\": \"28cc3a25bfba44ac449a9b586b4339aa\",\n        \"issuer_name\": \"Microsoft Root Certificate Authority 2010\"\n      },\n      \"signer_info\": {\n        \"thumbprint\": \"f7c2f2c96a328c13cda8cdb57b715bdea2cbd1d9\",\n        \"display_name\": \"Microsoft Windows\",\n        \"serial_number\": \"33000002ec6579ad1e670890130000000002ec\",\n        \"issuer_name\": \"Microsoft Windows Production PCA 2011\"\n      }\n    },\n    \"current_directory\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\",\n    \"error_msg\": \"\",\n    \"status_msg\": \"sigma match detected this process but not configured to block it\",\n    \"ppid\": 17808,\n    \"fake_parent_commandline\": null,\n    \"commandline\": \"tasklist\",\n    \"signed\": true,\n    \"grandparent_integrity_level\": \"Medium\",\n    \"log_type\": \"process\",\n    \"pe_imphash\": \"19BBD9C4E73C288A3645E163F4B82682\",\n    \"create_time\": \"2022-03-15T07:24:54.260Z\",\n    \"status\": 0,\n    \"parent_image\": \"C:\\\\Windows\\\\SysWOW64\\\\cmd.exe\",\n    \"integrity_level\": \"Medium\",\n    \"usersid\": \"S-1-5-21-299502267-725345543-82448378-2366\",\n    \"pe_info\": {\n      \"product_version\": \"10.0.19041.1\",\n      \"legal_copyright\": \"\u00a9 Microsoft Corporation. All rights reserved.\",\n      \"original_filename\": \"tasklist.exe\",\n      \"company_name\": \"Microsoft Corporation\",\n      \"file_description\": \"Lists the current running tasks\",\n      \"file_version\": \"10.0.19041.1 (WinBuild.160101.0800)\",\n      \"internal_name\": \"tasklist.exe\",\n      \"product_name\": \"Microsoft\u00ae Windows\u00ae Operating System\"\n    },\n    \"session\": 3,\n    \"pe_timestamp\": \"1994-09-11T16:43:21.000Z\",\n    \"parent_unique_id\": \"2332edf8-70c0-43c2-4590-00f912ab3d18\",\n    \"process_name\": \"tasklist.exe\",\n    \"grandparent_commandline\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\\\\EPOSConnect.exe 1\",\n    \"pe_timestamp_int\": 779301801,\n    \"grandparent_image\": \"C:\\\\Program Files (x86)\\\\EPOS\\\\EPOS Connect\\\\EPOSConnect.exe\",\n    \"parent_commandline\": \"C:\\\\WINDOWS\\\\system32\\\\cmd.exe /d /s /c tasklist\",\n    \"fake_parent_unique_id\": null,\n    \"size\": 79360,\n    \"fake_ppid\": null,\n    \"hashes\": {\n      \"sha1\": \"7f50d8c3cf3ec79122a876e969bdb65d939becd0\",\n      \"sha256\": \"76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4\",\n      \"md5\": \"0a4448b31ce7f83cb7691a2657f330f1\"\n    }\n  },\n  \"execution\": 0,\n  \"rule_name\": \"Discovery: Process list\",\n  \"maturity\": \"stable\",\n  \"msg\": \"Detects the execution of tasklist.exe, a tool used to gather detailed information about a computer's active processes.\"\n}\n",
        "event": {
            "category": [
                "process"
            ],
            "type": [
                "start"
            ],
            "kind": "alert"
        },
        "@timestamp": "2022-03-15T07:26:01.276Z",
        "agent": {
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "pc123"
        },
        "host": {
            "hostname": "pc123",
            "domain": "domain123",
            "os": {
                "version": "10.0.19041",
                "full": "Windows 10 Pro"
            },
            "name": "pc123"
        },
        "harfanglab": {
            "level": "low",
            "alert_time": "2022-03-15T07:26:01.276+00:00",
            "alert_unique_id": "00000000-0000-0000-0000-000000000000",
            "alert_subtype": "process",
            "execution": 0,
            "status": "false_positive",
            "aggregation_key": "123456"
        },
        "rule": {
            "description": "Detects the execution of tasklist.exe, a tool used to gather detailed information about a computer's active processes.",
            "name": "Discovery: Process list",
            "category": "sigma",
            "id": "00000000-0000-0000-0000-000000000000"
        },
        "process": {
            "command_line": "tasklist",
            "pid": 11320,
            "name": "tasklist.exe",
            "pe": {
                "description": "Lists the current running tasks",
                "original_file_name": "tasklist.exe",
                "file_version": "10.0.19041.1 (WinBuild.160101.0800)",
                "company": "Microsoft Corporation",
                "product": "Microsoft\u00ae Windows\u00ae Operating System",
                "imphash": "19BBD9C4E73C288A3645E163F4B82682"
            },
            "executable": "C:\\Windows\\SysWOW64\\tasklist.exe",
            "parent": {
                "executable": "C:\\Windows\\SysWOW64\\cmd.exe",
                "command_line": "C:\\WINDOWS\\system32\\cmd.exe /d /s /c tasklist"
            },
            "working_directory": "C:\\Program Files (x86)\\EPOS\\EPOS Connect"
        },
        "user": {
            "name": "XXX\\XXX"
        },
        "file": {
            "hash": {
                "md5": "0a4448b31ce7f83cb7691a2657f330f1",
                "sha256": "76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4",
                "sha1": "7f50d8c3cf3ec79122a876e969bdb65d939becd0"
            }
        },
        "related": {
            "hash": [
                "0a4448b31ce7f83cb7691a2657f330f1",
                "76eac7b5f53e0d58a98d5a6ddf9c97e19d1462ef65c0035d7798f89988b15ab4",
                "7f50d8c3cf3ec79122a876e969bdb65d939becd0"
            ],
            "hosts": [
                "pc123"
            ],
            "user": [
                "XXX\\XXX"
            ]
        }
    }
    	
	```


=== "process3.json"

    ```json
	
    {
        "message": "{\"signature_info\":{\"root_info\":{\"display_name\":\"Microsoft Root Certificate Authority 2010\",\"thumbprint\":\"3b1efd3a66ea28b16697394703a72ca340a05bd5\",\"serial_number\":\"28cc3a25bfba44ac449a9b586b4339aa\",\"issuer_name\":\"Microsoft Root Certificate Authority 2010\"},\"signed_catalog\":true,\"signer_info\":{\"display_name\":\"Microsoft Windows\",\"thumbprint\":\"ae9c1ae54763822eec42474983d8b635116c8452\",\"serial_number\":\"33000001c422b2f79b793dacb20000000001c4\",\"issuer_name\":\"Microsoft Windows Production PCA 2011\"},\"signed_authenticode\":false},\"commandline\":\"C:\\\\Windows\\\\system32\\\\wbem\\\\wmiprvse.exe -secured -Embedding\",\"fake_parent_commandline\":null,\"session\":0,\"pid\":4028,\"process_name\":\"WmiPrvSE.exe\",\"pe_info\":{\"product_version\":\"10.0.17763.1\",\"file_description\":\"WMI Provider Host\",\"original_filename\":\"Wmiprvse.exe\",\"internal_name\":\"Wmiprvse.exe\",\"file_version\":\"10.0.17763.1 (WinBuild.160101.0800)\",\"company_name\":\"Microsoft Corporation\",\"legal_copyright\":\"\u00a9 Microsoft Corporation. All rights reserved.\",\"product_name\":\"Microsoft\u00ae Windows\u00ae Operating System\"},\"fake_parent_image\":null,\"@timestamp\":\"2021-05-02T19:52:34.492Z\",\"username\":\"NT AUTHORITY\\\\NETWORK SERVICE\",\"pe_timestamp_int\":3717952540,\"@version\":\"1\",\"image_name\":\"C:\\\\Windows\\\\System32\\\\wbem\\\\WmiPrvSE.exe\",\"parent_integrity_level\":\"System\",\"fake_parent_unique_id\":null,\"status_msg\":\"\",\"log_type\":\"process\",\"logonid\":996,\"process_unique_id\":\"9aad140d-929d-4ddf-0fbc-006fa79b94af\",\"usersid\":\"S-1-5-20\",\"error_msg\":\"\",\"parent_image\":\"C:\\\\Windows\\\\System32\\\\svchost.exe\",\"fake_ppid\":null,\"integrity_level\":\"System\",\"agent\":{\"osversion\":\"10.0.17763\",\"domainname\":\"WORKGROUP\",\"agentid\":\"d4e3bf36-929d-4ddf-8526-492e89955808\",\"osproducttype\":\"Windows Server 2019 Datacenter\",\"hostname\":\"REDACTED\",\"domain\":null},\"current_directory\":\"C:\\\\Windows\\\\system32\",\"pe_timestamp\":\"2087-10-25T20:35:40.000Z\",\"parent_unique_id\":\"9aad140d-929d-4ddf-0358-002a32b395aa\",\"pe_imphash\":\"CFECEDC01015A4FD1BAACAC9E592D88B\",\"hashes\":{\"md5\":\"06c66ff5ccdc2d22344a3eb761a4d38a\",\"sha256\":\"b5c78bef3883e3099f7ef844da1446db29107e5c0223b97f29e7fafab5527f15\",\"sha1\":\"67c25c8f28b5fa7f5baa85bf1d2726aed48e9cf0\"},\"size\":489472,\"parent_commandline\":\"C:\\\\Windows\\\\system32\\\\svchost.exe -k DcomLaunch -p\",\"@event_create_date\":\"2021-05-02T19:52:24.083Z\",\"signed\":true,\"ppid\":856,\"status\":0}",
        "event": {
            "category": [
                "process"
            ],
            "type": [
                "start"
            ],
            "kind": "event"
        },
        "@timestamp": "2021-05-02T19:52:24.083Z",
        "agent": {
            "id": "d4e3bf36-929d-4ddf-8526-492e89955808",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "REDACTED"
        },
        "host": {
            "hostname": "REDACTED",
            "domain": "WORKGROUP",
            "os": {
                "version": "10.0.17763",
                "full": "Windows Server 2019 Datacenter"
            },
            "name": "REDACTED"
        },
        "process": {
            "command_line": "C:\\Windows\\system32\\wbem\\wmiprvse.exe -secured -Embedding",
            "pid": 4028,
            "name": "WmiPrvSE.exe",
            "pe": {
                "description": "WMI Provider Host",
                "original_file_name": "Wmiprvse.exe",
                "file_version": "10.0.17763.1 (WinBuild.160101.0800)",
                "company": "Microsoft Corporation",
                "product": "Microsoft\u00ae Windows\u00ae Operating System",
                "imphash": "CFECEDC01015A4FD1BAACAC9E592D88B"
            },
            "executable": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
            "parent": {
                "executable": "C:\\Windows\\System32\\svchost.exe",
                "command_line": "C:\\Windows\\system32\\svchost.exe -k DcomLaunch -p",
                "name": "svchost.exe"
            },
            "working_directory": "C:\\Windows\\system32"
        },
        "user": {
            "name": "NT AUTHORITY\\NETWORK SERVICE"
        },
        "file": {
            "hash": {
                "md5": "06c66ff5ccdc2d22344a3eb761a4d38a",
                "sha256": "b5c78bef3883e3099f7ef844da1446db29107e5c0223b97f29e7fafab5527f15",
                "sha1": "67c25c8f28b5fa7f5baa85bf1d2726aed48e9cf0"
            }
        },
        "related": {
            "hash": [
                "06c66ff5ccdc2d22344a3eb761a4d38a",
                "67c25c8f28b5fa7f5baa85bf1d2726aed48e9cf0",
                "b5c78bef3883e3099f7ef844da1446db29107e5c0223b97f29e7fafab5527f15"
            ],
            "hosts": [
                "REDACTED"
            ],
            "user": [
                "NT AUTHORITY\\NETWORK SERVICE"
            ]
        }
    }
    	
	```


=== "wineventlog.json"

    ```json
	
    {
        "message": "{\"tenant\":\"\",\"type\":\"wineventlog\",\"@event_create_date\":\"2021-11-21T13:11:49.837Z\",\"log_name\":\"Microsoft-Windows-PowerShell/Operational\",\"event_data\":{\"param1\":\"7092\",\"param2\":\"DefaultAppDomain\"},\"agent\":{\"osversion\":\"10.0.19041\",\"hostname\":\"DESKTOP-9U3171J\",\"ostype\":\"windows\",\"agentid\":\"f43cb847-8227-4104-b77f-7fc849789f8e\",\"osproducttype\":\"Windows 10 Pro\",\"domainname\":\"WORKGROUP\",\"distroid\":null,\"domain\":null},\"keywords\":[],\"log_type\":\"eventlog\",\"@version\":\"1\",\"source_name\":\"Microsoft-Windows-PowerShell\",\"@timestamp\":\"2021-11-21T13:12:10.929Z\",\"process_id\":7092,\"task\":null,\"level\":\"Information\",\"provider_guid\":\"{A1A1853B-5C40-4B15-8766-3CF1C58F985A}\",\"user\":{\"name\":\"oliver\",\"type\":\"User\",\"domain\":\"DESKTOP-9U3171J\",\"identifier\":\"S-1-5-21-975228105-2966123187-4141390122-1001\"},\"record_number\":104780,\"computer_name\":\"DESKTOP-9U3171J\",\"thread_id\":6744,\"event_id\":53504,\"opcode\":null,\"user_data\":{}}",
        "event": {
            "kind": "event",
            "type": [
                "info"
            ],
            "provider": "Microsoft-Windows-PowerShell",
            "code": "53504"
        },
        "@timestamp": "2021-11-21T13:11:49.837Z",
        "agent": {
            "id": "f43cb847-8227-4104-b77f-7fc849789f8e",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "DESKTOP-9U3171J"
        },
        "host": {
            "hostname": "DESKTOP-9U3171J",
            "domain": "WORKGROUP",
            "os": {
                "version": "10.0.19041",
                "full": "Windows 10 Pro"
            },
            "name": "DESKTOP-9U3171J"
        },
        "action": {
            "properties": {
                "param1": "7092",
                "param2": "DefaultAppDomain"
            },
            "id": 53504
        },
        "related": {
            "hosts": [
                "DESKTOP-9U3171J"
            ]
        }
    }
    	
	```


=== "wineventlog2.json"

    ```json
	
    {
        "message": "{\"log_name\":\"Security\",\"type\":\"wineventlog\",\"source_name\":\"Microsoft-Windows-Security-Auditing\",\"event_id\":4625,\"provider_guid\":\"{54849625-5478-4994-A5BA-3E3B0328C30D}\",\"level\":\"Information\",\"opcode\":null,\"agent\":{\"osversion\":\"10.0.17763\",\"domainname\":\"WORKGROUP\",\"agentid\":\"77af54c8-910f-455d-b887-87cbc87430a4\",\"osproducttype\":\"Windows Server 2019 Datacenter\",\"hostname\":\"REDACTED\",\"domain\":null},\"user\":null,\"event_date\":\"2021-05-08T12:18:58.996Z\",\"process_id\":760,\"@timestamp\":\"2021-05-08T12:19:10.711Z\",\"user_data\":{},\"@version\":\"1\",\"event_data\":{\"IpPort\":\"0\",\"AuthenticationPackageName\":\"NTLM\",\"TransmittedServices\":\"-\",\"TargetUserSid\":\"S-1-0-0\",\"SubjectUserName\":\"-\",\"SubStatus\":\"0xc000006a\",\"IpAddress\":\"166.88.151.58\",\"SubjectLogonId\":\"0x0\",\"FailureReason\":\"%%2313\",\"WorkstationName\":\"-\",\"SubjectUserSid\":\"S-1-0-0\",\"LogonProcessName\":\"NtLmSsp \",\"TargetUserName\":\"ADMINISTRATOR\",\"ProcessName\":\"-\",\"TargetDomainName\":null,\"Status\":\"0xc000006d\",\"LmPackageName\":\"-\",\"KeyLength\":\"0\",\"SubjectDomainName\":\"-\",\"LogonType\":\"3\",\"ProcessId\":\"0x0\"},\"keywords\":[\"Audit Failure\"],\"task\":null,\"record_number\":5089212,\"thread_id\":1768,\"log_type\":\"eventlog\",\"computer_name\":\"REDACTED\"}",
        "event": {
            "kind": "event",
            "type": [
                "info"
            ],
            "provider": "Microsoft-Windows-Security-Auditing",
            "code": "4625"
        },
        "agent": {
            "id": "77af54c8-910f-455d-b887-87cbc87430a4",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "REDACTED"
        },
        "host": {
            "hostname": "REDACTED",
            "domain": "WORKGROUP",
            "os": {
                "version": "10.0.17763",
                "full": "Windows Server 2019 Datacenter"
            },
            "name": "REDACTED"
        },
        "action": {
            "properties": {
                "IpPort": "0",
                "AuthenticationPackageName": "NTLM",
                "TransmittedServices": "-",
                "TargetUserSid": "S-1-0-0",
                "SubjectUserName": "-",
                "SubStatus": "0xc000006a",
                "IpAddress": "166.88.151.58",
                "SubjectLogonId": "0x0",
                "FailureReason": "%%2313",
                "WorkstationName": "-",
                "SubjectUserSid": "S-1-0-0",
                "LogonProcessName": "NtLmSsp ",
                "TargetUserName": "ADMINISTRATOR",
                "ProcessName": "-",
                "Status": "0xc000006d",
                "LmPackageName": "-",
                "KeyLength": "0",
                "SubjectDomainName": "-",
                "LogonType": "3",
                "ProcessId": "0x0"
            },
            "id": 4625
        },
        "related": {
            "hosts": [
                "REDACTED"
            ]
        }
    }
    	
	```


=== "wineventlog3.json"

    ```json
	
    {
        "message": "{\"computer_name\":\"REDACTED\",\"process_id\":3464,\"provider_guid\":\"{11CD958A-C507-4EF3-B3F2-5FD9DFBD2C78}\",\"type\":\"wineventlog\",\"log_name\":\"Microsoft-Windows-Windows Defender/Operational\",\"task\":null,\"user\":{\"identifier\":\"S-1-5-18\",\"domain\":\"AUTORITE NT\",\"type\":\"User\",\"name\":\"Syst\u00e8me\"},\"log_type\":\"eventlog\",\"@version\":\"1\",\"tenant\":\"\",\"keywords\":[],\"@event_create_date\":\"2022-01-03T05:44:57.331Z\",\"thread_id\":23768,\"record_number\":2300,\"event_id\":1116,\"event_data\":{\"Unused4\":null,\"Threat Name\":\"Exploit:O97M/CVE-2017-11882.SMK\",\"Post Clean Status\":\"0\",\"Product Version\":\"4.18.2111.5\",\"Detection Time\":\"2022-01-03T05:44:57.284Z\",\"Detection User\":\"AUTORITE NT\\\\Syst\u00e8me\",\"Status Code\":\"1\",\"Origin ID\":\"1\",\"Category ID\":\"30\",\"FWLink\":\"https://go.microsoft.com/fwlink/?linkid=37020&name=Exploit:O97M/CVE-2017-11882.SMK!MTB&threatid=2147772194&enterprise=0\",\"Path\":\"file:_C:\\\\Program Files\\\\Avast\\\\Amex\\\\temp\\\\TMMSG_45AD4A29-D7BD-AE8F-FFBC-4115652291C2\",\"Process Name\":\"C:\\\\Program Files\\\\Avast\\\\Amex\\\\AMEX_secondary.exe\",\"Origin Name\":\"Ordinateur local\",\"Execution ID\":\"1\",\"Remediation User\":null,\"Status Description\":null,\"Category Name\":\"Attaque\",\"Type Name\":\"Concret\",\"State\":\"1\",\"Pre Execution Status\":\"0\",\"Type ID\":\"0\",\"Action Name\":\"Non applicable\",\"Unused6\":null,\"Additional Actions String\":\"No additional actions required\",\"Threat ID\":\"2147772194\",\"Execution Name\":\"Suspendu\",\"Severity ID\":\"5\",\"Error Description\":\"L\u2019op\u00e9ration a r\u00e9ussi. \",\"Engine Version\":\"AM: 1.1.18800.4, NIS: 1.1.18800.4\",\"Unused3\":null,\"Detection ID\":\"{2E51DC7F-A01D-4E9E-94C8-782C63D85C6E}\",\"Security intelligence Version\":\"AV: 1.355.1292.0, AS: 1.355.1292.0, NIS: 1.355.1292.0\",\"Product Name\":\"Antivirus Microsoft Defender\",\"Unused\":null,\"Action ID\":\"9\",\"Source ID\":\"3\",\"Additional Actions ID\":\"0\",\"Source Name\":\"Protection en temps r\u00e9el\",\"Unused5\":null,\"Severity Name\":\"Grave\",\"Error Code\":\"0x00000000\",\"Unused2\":null},\"level\":\"Warning\",\"source_name\":\"Microsoft-Windows-Windows Defender\",\"opcode\":null,\"@timestamp\":\"2022-01-03T05:45:12.816Z\",\"user_data\":{},\"agent\":{\"agentid\":\"06d70013-58c7-46e3-9231-452a383af90b\",\"domain\":null,\"osproducttype\":\"Windows Server 2019 Datacenter\",\"ostype\":\"windows\",\"osversion\":\"10.0.17763\",\"version\":\"2.12.2\",\"domainname\":\"REDACTED\",\"distroid\":null,\"hostname\":\"REDACTED\"}}",
        "event": {
            "kind": "event",
            "type": [
                "info"
            ],
            "provider": "Microsoft-Windows-Windows Defender",
            "code": "1116"
        },
        "@timestamp": "2022-01-03T05:44:57.331Z",
        "agent": {
            "id": "06d70013-58c7-46e3-9231-452a383af90b",
            "name": "harfanglab"
        },
        "log": {
            "hostname": "REDACTED"
        },
        "host": {
            "hostname": "REDACTED",
            "domain": "REDACTED",
            "os": {
                "version": "10.0.17763",
                "full": "Windows Server 2019 Datacenter"
            },
            "name": "REDACTED"
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
        },
        "related": {
            "hosts": [
                "REDACTED"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`action.properties` | `object` | A list of objects |
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
|`harfanglab.aggregation_key` | `keyword` | The key to the events aggregation |
|`harfanglab.alert_subtype` | `keyword` | The subtype of the alert |
|`harfanglab.alert_time` | `keyword` | The timestamp of the alert |
|`harfanglab.alert_unique_id` | `keyword` | The identifier of the alert |
|`harfanglab.execution` | `long` | Execution time  |
|`harfanglab.level` | `keyword` | The risk level associated to the alert |
|`harfanglab.process.powershell.command` | `keyword` | The powershell command executed |
|`harfanglab.status` | `keyword` | The status of the alert |
|`host.domain` | `keyword` | Name of the directory the group is a member of. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.os.full` | `keyword` | Operating system name, including the version or code name. |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.name` | `keyword` | Process name. |
|`process.parent.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.parent.name` | `keyword` | Process name. |
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

