
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
        "message": "{\"metadata\":{\"customerIDString\":\"46de5283260647ec8f28def00bffd094\",\"offset\":6755,\"eventType\":\"AuthActivityAuditEvent\",\"eventCreationTime\":1657663146099,\"version\":\"1.0\"},\"event\":{\"UserId\":\"foo.bar@sekoia.fr\",\"UserIp\":\"83.199.26.17\",\"OperationName\":\"twoFactorAuthenticate\",\"ServiceName\":\"CrowdStrike Authentication\",\"Success\":true,\"UTCTimestamp\":1657663146099}}",
        "event": {
            "kind": "event",
            "type": [
                "change"
            ],
            "category": [
                "configuration"
            ]
        },
        "@timestamp": "2022-07-12T21:59:06.099000Z",
        "crowdstrike": {
            "event_type": "AuthActivityAuditEvent",
            "operation_name": "twoFactorAuthenticate"
        },
        "source": {
            "ip": "83.199.26.17",
            "address": "83.199.26.17"
        },
        "service": {
            "name": "CrowdStrike Authentication"
        },
        "user": {
            "id": "foo.bar@sekoia.fr"
        },
        "related": {
            "ip": [
                "83.199.26.17"
            ]
        }
    }
    	
	```


=== "detection_summary_event.json"

    ```json
	
    {
        "message": "{\"metadata\":{\"customerIDString\":\"46de5283260647ec8f28def00bffd094\",\"offset\":189,\"eventType\":\"DetectionSummaryEvent\",\"eventCreationTime\":1657174538000,\"version\":\"1.0\"},\"event\":{\"ProcessStartTime\":1656688889,\"ProcessEndTime\":0,\"ProcessId\":22164474048,\"ParentProcessId\":22163465296,\"ComputerName\":\"nsewmkzevukn-vm\",\"UserName\":\"Administrator\",\"DetectName\":\"Overwatch Detection\",\"DetectDescription\":\"Falcon Overwatch has identified malicious activity carried out by a suspected or known eCrime operator. This activity has been raised for critical action and should be investigated urgently.\",\"Severity\":5,\"SeverityName\":\"Critical\",\"FileName\":\"explorer.exe\",\"FilePath\":\"\\\\Device\\\\HarddiskVolume2\\\\Windows\",\"CommandLine\":\"C:\\\\Windows\\\\Explorer.EXE\",\"SHA256String\":\"249cb3cb46fd875196e7ed4a8736271a64ff2d8132357222a283be53e7232ed3\",\"MD5String\":\"d45bd7c7b7bf977246e9409d63435231\",\"SHA1String\":\"0000000000000000000000000000000000000000\",\"MachineDomain\":\"nsewmkzevukn-vm\"}}",
        "event": {
            "kind": "alert",
            "type": [
                "info"
            ],
            "category": [
                "intrusion_detection"
            ]
        },
        "@timestamp": "2022-07-07T06:15:38.000000Z",
        "crowdstrike": {
            "event_type": "DetectionSummaryEvent",
            "detect_description": "Falcon Overwatch has identified malicious activity carried out by a suspected or known eCrime operator. This activity has been raised for critical action and should be investigated urgently."
        },
        "file": {
            "name": "explorer.exe",
            "path": "\\Device\\HarddiskVolume2\\Windows",
            "hash": {
                "md5": "d45bd7c7b7bf977246e9409d63435231"
            }
        },
        "host": {
            "name": "nsewmkzevukn-vm"
        },
        "log": {
            "hostname": "nsewmkzevukn-vm"
        },
        "process": {
            "pid": 22164474048,
            "parent": {
                "pid": 22163465296
            },
            "hash": {
                "sha256": "249cb3cb46fd875196e7ed4a8736271a64ff2d8132357222a283be53e7232ed3"
            },
            "command_line": "C:\\Windows\\Explorer.EXE"
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
        "message": "{\"metadata\":{\"customerIDString\":\"46de5283260647ec8f28def00bffd094\",\"offset\":733,\"eventType\":\"UserActivityAuditEvent\",\"eventCreationTime\":1657614940000,\"version\":\"1.0\"},\"event\":{\"UserId\":\"foo.bar@sekoia.fr\",\"UserIp\":\"185.162.177.26\",\"OperationName\":\"detection_update\",\"ServiceName\":\"detections\",\"AuditKeyValues\":[{\"Key\":\"detection_id\",\"ValueString\":\"ldt:5418788591a444d1b45c2b39d3b07b50:21483381998\"},{\"Key\":\"new_state\",\"ValueString\":\"closed\"},{\"Key\":\"assigned_to\",\"ValueString\":\"Erwan Chevalier\"},{\"Key\":\"assigned_to_uid\",\"ValueString\":\"foo.bar@sekoia.fr\"}],\"UTCTimestamp\":1657614940}}",
        "event": {
            "kind": "event",
            "type": [
                "change"
            ],
            "category": [
                "configuration"
            ]
        },
        "@timestamp": "2022-07-12T08:35:40.000000Z",
        "crowdstrike": {
            "event_type": "UserActivityAuditEvent",
            "operation_name": "detection_update"
        },
        "source": {
            "ip": "185.162.177.26",
            "address": "185.162.177.26"
        },
        "service": {
            "name": "detections"
        },
        "user": {
            "id": "foo.bar@sekoia.fr"
        },
        "related": {
            "ip": [
                "185.162.177.26"
            ]
        }
    }
    	
	```


=== "stream_started.json"

    ```json
	
    {
        "message": "{\"metadata\": {\"customerIDString\": \"46de5283260647ec8f28def00bffd094\", \"offset\": 174, \"eventType\": \"AuthActivityAuditEvent\", \"eventCreationTime\": 1657110865303, \"version\": \"1.0\"}, \"event\": {\"UserId\": \"api-client-id:00000000000000000000000000000000\", \"UserIp\": \"185.162.177.26\", \"OperationName\": \"streamStarted\", \"ServiceName\": \"Crowdstrike Streaming API\", \"Success\": true, \"UTCTimestamp\": 1657110865, \"AuditKeyValues\": [{\"Key\": \"partition\", \"ValueString\": \"0\"}, {\"Key\": \"offset\", \"ValueString\": \"-1\"}, {\"Key\": \"appId\", \"ValueString\": \"sio-00000\"}, {\"Key\": \"eventType\", \"ValueString\": \"All event type(s)\"}, {\"Key\": \"APIClientID\", \"ValueString\": \"00000000000000000000000000000000\"}]}}",
        "event": {
            "kind": "event",
            "type": [
                "change"
            ],
            "category": [
                "configuration"
            ]
        },
        "@timestamp": "2022-07-06T12:34:25.303000Z",
        "crowdstrike": {
            "event_type": "AuthActivityAuditEvent",
            "operation_name": "streamStarted"
        },
        "source": {
            "ip": "185.162.177.26",
            "address": "185.162.177.26"
        },
        "service": {
            "name": "Crowdstrike Streaming API"
        },
        "user": {
            "id": "api-client-id:00000000000000000000000000000000"
        },
        "related": {
            "ip": [
                "185.162.177.26"
            ]
        }
    }
    	
	```


=== "stream_stopped.json"

    ```json
	
    {
        "message": "{\"metadata\":{\"customerIDString\":\"46de5283260647ec8f28def00bffd094\",\"offset\":200,\"eventType\":\"AuthActivityAuditEvent\",\"eventCreationTime\":1657203917516,\"version\":\"1.0\"},\"event\":{\"UserId\":\"api-client-id:00000000000000000000000000000000\",\"UserIp\":\"185.162.177.26\",\"OperationName\":\"streamStopped\",\"ServiceName\":\"Crowdstrike Streaming API\",\"Success\":true,\"UTCTimestamp\":1657203917,\"AuditKeyValues\":[{\"Key\":\"APIClientID\",\"ValueString\":\"00000000000000000000000000000000\"},{\"Key\":\"partition\",\"ValueString\":\"0\"},{\"Key\":\"offset\",\"ValueString\":\"-1\"},{\"Key\":\"appId\",\"ValueString\":\"sio-00000\"},{\"Key\":\"eventType\",\"ValueString\":\"All event type(s)\"}]}}",
        "event": {
            "kind": "event",
            "type": [
                "change"
            ],
            "category": [
                "configuration"
            ]
        },
        "@timestamp": "2022-07-07T14:25:17.516000Z",
        "crowdstrike": {
            "event_type": "AuthActivityAuditEvent",
            "operation_name": "streamStopped"
        },
        "source": {
            "ip": "185.162.177.26",
            "address": "185.162.177.26"
        },
        "service": {
            "name": "Crowdstrike Streaming API"
        },
        "user": {
            "id": "api-client-id:00000000000000000000000000000000"
        },
        "related": {
            "ip": [
                "185.162.177.26"
            ]
        }
    }
    	
	```


=== "user_activity_audit.json"

    ```json
	
    {
        "message": "{\"metadata\":{\"customerIDString\":\"46de5283260647ec8f28def00bffd094\",\"offset\":747,\"eventType\":\"UserActivityAuditEvent\",\"eventCreationTime\":1657614940000,\"version\":\"1.0\"},\"event\":{\"UserId\":\"foo.bar@sekoia.fr\",\"UserIp\":\"185.162.177.26\",\"OperationName\":\"detection_update\",\"ServiceName\":\"detections\",\"AuditKeyValues\":[{\"Key\":\"detection_id\",\"ValueString\":\"ldt:5418788591a444d1b45c2b39d3b07b50:21482411386\"},{\"Key\":\"new_state\",\"ValueString\":\"closed\"},{\"Key\":\"assigned_to\",\"ValueString\":\"Foo Bar\"},{\"Key\":\"assigned_to_uid\",\"ValueString\":\"foo.bar@sekoia.fr\"}],\"UTCTimestamp\":1657614940}}",
        "event": {
            "kind": "event",
            "type": [
                "change"
            ],
            "category": [
                "configuration"
            ]
        },
        "@timestamp": "2022-07-12T08:35:40.000000Z",
        "crowdstrike": {
            "event_type": "UserActivityAuditEvent",
            "operation_name": "detection_update"
        },
        "source": {
            "ip": "185.162.177.26",
            "address": "185.162.177.26"
        },
        "service": {
            "name": "detections"
        },
        "user": {
            "id": "foo.bar@sekoia.fr"
        },
        "related": {
            "ip": [
                "185.162.177.26"
            ]
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

