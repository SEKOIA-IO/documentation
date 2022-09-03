
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Authentication logs` | activities on the CrowdStrike console is traced including authentication |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `alert`, `event` |
| Category | `configuration`, `intrusion_detection`, `session` |
| Type | `change`, `info`, `start`, `stop` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "auth_activity_audit.json"

    ```json
	
    {
        "@timestamp": "2022-07-12T21:59:06.099000Z",
        "crowdstrike": {
            "event_type": "AuthActivityAuditEvent",
            "operation_name": "twoFactorAuthenticate"
        },
        "event": {
            "category": "configuration",
            "kind": "event",
            "type": "change",
            "outcome": "success"
        },
        "service": {
            "name": "CrowdStrike Authentication"
        },
        "related": {
            "ip": [
                "83.199.26.17"
            ]
        },
        "source": {
            "address": "83.199.26.17",
            "ip": "83.199.26.17"
        },
        "user": {
            "id": "foo.bar@sekoia.fr"
        }
    }
    	
	```


=== "detection_summary_event.json"

    ```json
	
    {
        "@timestamp": "2022-07-07T06:15:38.000000Z",
        "crowdstrike": {
            "detect_description": "Falcon Overwatch has identified malicious activity carried out by a suspected or known eCrime operator. This activity has been raised for critical action and should be investigated urgently.",
            "event_type": "DetectionSummaryEvent"
        },
        "event": {
            "category": "intrusion_detection",
            "kind": "alert",
            "outcome": "success",
            "type": "info"
        },
        "file": {
            "hash": {
                "md5": "d45bd7c7b7bf977246e9409d63435231"
            },
            "name": "explorer.exe",
            "path": "\\Device\\HarddiskVolume2\\Windows"
        },
        "host": {
            "name": "nsewmkzevukn-vm"
        },
        "log": {
            "hostname": "nsewmkzevukn-vm"
        },
        "process": {
            "command_line": "C:\\Windows\\Explorer.EXE",
            "hash": {
                "sha256": "249cb3cb46fd875196e7ed4a8736271a64ff2d8132357222a283be53e7232ed3"
            },
            "parent": {
                "pid": 22163465296
            },
            "pid": 22164474048
        },
        "related": {
            "hash": [
                "249cb3cb46fd875196e7ed4a8736271a64ff2d8132357222a283be53e7232ed3",
                "d45bd7c7b7bf977246e9409d63435231"
            ]
        }
    }
    	
	```


=== "detection_update.json"

    ```json
	
    {
        "@timestamp": "2022-07-12T08:35:40.000000Z",
        "crowdstrike": {
            "event_type": "UserActivityAuditEvent",
            "operation_name": "detection_update"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "configuration",
            "kind": "event",
            "type": "change"
        },
        "related": {
            "ip": [
                "185.162.177.26"
            ]
        },
        "service": {
            "name": "detections"
        },
        "source": {
            "address": "185.162.177.26",
            "ip": "185.162.177.26"
        },
        "user": {
            "id": "foo.bar@sekoia.fr"
        }
    }
    	
	```


=== "stream_started.json"

    ```json
	
    {
        "@timestamp": "2022-07-06T12:34:25.303000Z",
        "crowdstrike": {
            "event_type": "AuthActivityAuditEvent",
            "operation_name": "streamStarted"
        },
        "event": {
            "category": "session",
            "kind": "event",
            "outcome": "success",
            "type": "start"
        },
        "related": {
            "ip": [
                "185.162.177.26"
            ]
        },
        "service": {
            "name": "Crowdstrike Streaming API"
        },
        "source": {
            "address": "185.162.177.26",
            "ip": "185.162.177.26"
        },
        "user": {
            "id": "api-client-id:00000000000000000000000000000000"
        }
    }
    	
	```


=== "stream_stopped.json"

    ```json
	
    {
        "@timestamp": "2022-07-07T14:25:17.516000Z",
        "crowdstrike": {
            "event_type": "AuthActivityAuditEvent",
            "operation_name": "streamStopped"
        },
        "event": {
            "category": "session",
            "kind": "event",
            "outcome": "success",
            "type": "start"
        },
        "related": {
            "ip": [
                "185.162.177.26"
            ]
        },
        "service": {
            "name": "Crowdstrike Streaming API"
        },
        "source": {
            "address": "185.162.177.26",
            "ip": "185.162.177.26"
        },
        "user": {
            "id": "api-client-id:00000000000000000000000000000000"
        }
    }
    	
	```


=== "user_activity_audit.json"

    ```json
	
    {
        "event": {
            "kind": "event",
            "category": "configuration",
            "type": "change"
        },
        "@timestamp": "2022-07-12T08:35:40.000000Z",
        "crowdstrike": {
            "event_type": "UserActivityAuditEvent",
            "operation_name": "detection_update"
        },
        "related": {
            "ip": [
                "185.162.177.26"
            ]
        },
        "service": {
            "name": "detections"
        },
        "source": {
            "address": "185.162.177.26",
            "ip": "185.162.177.26"
        },
        "user": {
            "id": "foo.bar@sekoia.fr"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`agent.id` | `keyword` | Unique identifier of this agent. |
|`crowdstrike.customer_id` | `keyword` | Customer ID (cid) |
|`crowdstrike.detect_description` | `keyword` | A description of what an adversary was trying to do in the environment and guidance on how to begin an investigation. |
|`crowdstrike.detect_id` | `keyword` | The Detection ID for the detection. Can be used in other APIs, such as Detection Resolution and ThreatGraph. |
|`crowdstrike.event_type` | `keyword` | Type of the event |
|`crowdstrike.host_id` | `keyword` | The crowdstrike identifier of the host |
|`crowdstrike.incident_end` | `date` | Time of the latest activity in the incident |
|`crowdstrike.incident_id` | `keyword` | The incident ID of the incident |
|`crowdstrike.incident_start` | `date` | Time of the first activity in the incident |
|`crowdstrike.operation_name` | `keyword` | Operation name |
|`crowdstrike.state` | `keyword` | Shows if the incident is still active. open = the incident is still active, closed = the incident is not active |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.hash.md5` | `keyword` | MD5 hash. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`host.ip` | `ip` | Host ip addresses. |
|`host.mac` | `keyword` | Host MAC addresses. |
|`host.name` | `keyword` | Name of the host. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.end` | `date` | The time the process ended. |
|`process.hash.sha256` | `keyword` | SHA256 hash. |
|`process.parent.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.parent.pid` | `long` | Process id. |
|`process.pid` | `long` | Process id. |
|`process.start` | `date` | The time the process started. |
|`service.name` | `keyword` | Name of the service. |
|`source.ip` | `ip` | IP address of the source. |
|`threat.tactic.name` | `keyword` | Threat tactic. |
|`threat.technique.name` | `keyword` | Threat technique name. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |

