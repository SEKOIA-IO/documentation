
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application Logs` | This tool forward application logs to your SIEM. |
| `Web Logs` | This tool forward application logs to your SIEM. |
| `Network device Logs` | This tool forward application logs to your SIEM. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `host` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "input.json"

    ```json
	
    {
        "event": {
            "category": [
                "host"
            ],
            "kind": "event",
            "outcome": "success",
            "type": [
                "info"
            ]
        },
        "host": {
            "id": "713FC2B45B429J291EB53467357AC1B7",
            "name": "DESKTOP-PC"
        },
        "registry": {
            "key": "\\Windows Defender\\MsMpeng.exe RegKey=\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\WicaAvPathsExpiredTemp?0"
        },
        "related": {
            "ip": [
                "192.168.0.11"
            ],
            "user": [
                "NT AUTHORITY\\SYSTEM"
            ]
        },
        "siemfeeder": {
            "broken": "true",
            "cat": "Goodware",
            "client": "1212122",
            "company": "Microsoft Corporation",
            "date": "2018-09-27 02:26:52.200188",
            "drivetype": "Fixed",
            "exetype": "Unknown",
            "hash": "C86854DF4F3AEC59D523DBAD1F5031FD",
            "imagetype": "EXE 32",
            "op": "CreateExeKey",
            "prevlastday": "Low",
            "prevalence": "Medium",
            "targetpath": "3",
            "validsig": "true"
        },
        "source": {
            "address": "192.168.0.11",
            "ip": "192.168.0.11"
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
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`host.id` | `keyword` | Unique host id. |
|`host.name` | `keyword` | Name of the host. |
|`registry.key` | `keyword` | Hive-relative path of keys. |
|`registry.path` | `keyword` | Full path, including hive, key and value |
|`siemfeeder.broken` | `keyword` | None |
|`siemfeeder.cat` | `keyword` | None |
|`siemfeeder.client` | `keyword` | None |
|`siemfeeder.company` | `keyword` | None |
|`siemfeeder.date` | `keyword` | None |
|`siemfeeder.drivetype` | `keyword` | None |
|`siemfeeder.exetype` | `keyword` | None |
|`siemfeeder.hash` | `keyword` | None |
|`siemfeeder.imagetype` | `keyword` | None |
|`siemfeeder.mwname` | `keyword` | None |
|`siemfeeder.op` | `keyword` | None |
|`siemfeeder.prevalence` | `keyword` | None |
|`siemfeeder.prevlastday` | `keyword` | None |
|`siemfeeder.targetpath` | `keyword` | None |
|`siemfeeder.validsig` | `keyword` | None |
|`source.ip` | `ip` | IP address of the source. |
|`user.name` | `keyword` | Short name or login of the user. |

