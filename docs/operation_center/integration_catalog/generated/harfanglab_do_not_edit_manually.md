
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





In details, the following Table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event`, `alert` |
| Category | `process`, `network` |
| Type | `info`, `connection`, `start` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


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
|`harfanglab.alert_unique_id` | `long` | None |
|`harfanglab.execution` | `long` | None |
|`harfanglab.level` | `keyword` | None |
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

