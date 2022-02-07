
## Event Categories


The following Table lists the data source offered by this integration.

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
| Kind | `event` |
| Category | `file` |
| Type | `creation`, `info` |






## Extracted Fields

The following Table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`dns.answers.name` | `keyword` | The domain name to which this resource record pertains. |
|`dns.question.name` | `keyword` | The name being queried. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`group.name` | `keyword` | Name of the group. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.ip` | `ip` | Host ip addresses. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.pid` | `long` | Process id. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |

