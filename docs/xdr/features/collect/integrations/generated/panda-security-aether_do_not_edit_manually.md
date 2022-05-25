
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Asset Management` | Panda Aether integrates every Panda Endpoints in a single management console. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event`, `metric` |
| Category | `host` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "CountsofSecurityEvents.json"

    ```json
	
    {
        "event": {
            "category": [
                "host"
            ],
            "kind": "metric",
            "outcome": "success",
            "type": [
                "info"
            ]
        },
        "aether": {
            "exploit_counters": {
                "total_affected_devices": 1,
                "total_alerts": 1,
                "total_data_access": 1,
                "total_executed": 1,
                "total_external_communications": 1
            },
            "malware_counters": {
                "total_affected_devices": 1,
                "total_alerts": 1,
                "total_data_access": 1,
                "total_executed": 1,
                "total_external_communications": 1
            },
            "program_blocked_counters": {
                "total_programs_blocked": 1
            },
            "pups_counters": {
                "total_affected_devices": 1,
                "total_alerts": 1,
                "total_data_access": 1,
                "total_executed": 1,
                "total_external_communications": 1
            },
            "threats_by_av_counters": {
                "total_dangerous_actions_blocked_by_av": 1,
                "total_devices_blocked_by_av": 1,
                "total_intrusion_attempted_blocked_by_av": 1,
                "total_malware_urls_blocked_by_av": 1,
                "total_phishing_detected_by_av": 1,
                "total_tracking_cookies_detected_by_av": 1
            }
        },
        "ecs": {
            "version": "1.10.0"
        }
    }
    	
	```


=== "Retrieve_Security _Events_for_Devices_indicator_type_attack.json"

    ```json
	
    {
        "source": {
            "address": "11.22.33.44",
            "ip": "11.22.33.44"
        },
        "related": {
            "ip": [
                "11.22.33.44"
            ]
        },
        "host": {
            "name": "PC01234",
            "type": "Workstation"
        },
        "action": {
            "id": 2,
            "name": "Blocked"
        },
        "aether": {
            "custom_group_folder_id": "c0594d69-c988-4b59-a43f-c6a9ba130483",
            "custom_group_folder_info": [
                "{\"is_translatable\": true, \"name\": \"Root\", \"type\": 1}",
                "{\"is_translatable\": null, \"name\": \"PC\", \"type\": 2}",
                "{\"is_translatable\": null, \"name\": \"Lorem Ipsum Foo Bar\", \"type\": 2}"
            ],
            "device_type": 1,
            "id": "ae485846-fb1b-561b-98da-a8426caf65fa",
            "malware_category": 8,
            "malware_category_translated": "Malware URL",
            "number_of_occurrences": 1,
            "path": "http://somewhere.net/click?i=lw3Bilut*ZE_0",
            "security_event_date": "2022-04-07T16:54:09Z",
            "site_name": "GROUPE CORP"
        },
        "event": {
            "category": [
                "host"
            ],
            "kind": "event",
            "outcome": "success",
            "type": [
                "info"
            ]
        }
    }
    	
	```


=== "Retrieve_Security _Events_for_Devices_indicator_type_detections.json"

    ```json
	
    {
        "action": {
            "id": 2,
            "name": "Blocked"
        },
        "host": {
            "name": "PC01234",
            "type": "Workstation"
        },
        "source": {
            "address": "11.22.33.44",
            "ip": "11.22.33.44"
        },
        "related": {
            "ip": [
                "11.22.33.44"
            ]
        },
        "aether": {
            "custom_group_folder_id": "c0594d69-c988-4b59-a43f-c6a9ba130483",
            "custom_group_folder_info": [
                "{\"is_translatable\": true, \"name\": \"Root\", \"type\": 1}",
                "{\"is_translatable\": null, \"name\": \"PC\", \"type\": 2}",
                "{\"is_translatable\": null, \"name\": \"Lorem Ipsum Foo Bar\", \"type\": 2}"
            ],
            "device_type": 1,
            "id": "d8309d70-489d-5c62-97e3-2994e9dd8f17",
            "malware_category": 8,
            "malware_category_translated": "Malware URL",
            "number_of_occurrences": 2,
            "path": "https://somewhere.net",
            "security_event_date": "2022-04-07T16:40:43Z",
            "site_name": "GROUPE CORP"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": [
                "host"
            ],
            "kind": "event",
            "outcome": "success",
            "type": [
                "info"
            ]
        }
    }
    	
	```


=== "Retrieve_Security _Events_for_Devices_indicator_type_detections_13.json"

    ```json
	
    {
        "source": {
            "address": "11.22.33.44",
            "ip": "11.22.33.44"
        },
        "host": {
            "name": "M0897",
            "type": "Laptop"
        },
        "action": {
            "id": 2,
            "name": "Blocked"
        },
        "aether": {
            "security_event_type": 13,
            "custom_group_folder_id": "c0594d69-c988-4b59-a43f-c6a9ba130483",
            "custom_group_folder_info": [
                "{\"is_translatable\": true, \"name\": \"Root\", \"type\": 1}",
                "{\"is_translatable\": null, \"name\": \"PC\", \"type\": 2}",
                "{\"is_translatable\": null, \"name\": \"PC - Lock + Update + Patching (lundi au dimanche)  + Fw\", \"type\": 2}"
            ],
            "device_type": 2,
            "id": "6527fc9f-90ba-54b6-9116-b032ade14c05",
            "malware_category": 8,
            "malware_category_translated": "Malware URL",
            "number_of_occurrences": 8,
            "path": "https://somewhere.com",
            "security_event_date": "2022-04-08T10:12:21Z",
            "site_name": "CORP"
        },
        "event": {
            "reason": "Malware URLs detected",
            "category": [
                "host"
            ],
            "kind": "event",
            "outcome": "success",
            "type": [
                "info"
            ]
        }
    }
    	
	```


=== "Retrieve_Security _Events_for_Devices_indicator_type_detections_15.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
            "reason": "Intrusion Attempts detected"
        },
        "host": {
            "name": "PC123",
            "type": "Laptop"
        },
        "source": {
            "address": "11.22.33.44",
            "ip": "11.22.33.44"
        },
        "aether": {
            "security_event_type": 15,
            "custom_group_folder_id": "c0594d69-c988-4b59-a43f-c6a9ba130483",
            "custom_group_folder_info": [
                "{\"is_translatable\": true, \"name\": \"Root\", \"type\": 1}",
                "{\"is_translatable\": null, \"name\": \"PC\", \"type\": 2}",
                "{\"is_translatable\": null, \"name\": \"PC - Lock + Update + Patching (lundi au dimanche)  + Fw\", \"type\": 2}"
            ],
            "device_type": 2,
            "id": "aebfd1b7-a6ec-5a18-8c55-7be2b4c8562e",
            "network_activity_type": 14,
            "network_activity_type_translated": "SmartArp",
            "security_event_date": "2022-04-08T10:15:31.737Z",
            "site_name": "CORP"
        }
    }
    	
	```


=== "Retrieve_Security _Events_for_Devices_indicator_type_detections_2.json"

    ```json
	
    {
        "source": {
            "address": "11.22.33.44",
            "ip": "11.22.33.44"
        },
        "action": {
            "id": 2,
            "name": "Blocked"
        },
        "host": {
            "name": "PC01234",
            "type": "Workstation"
        },
        "aether": {
            "security_event_type": 1,
            "custom_group_folder_id": "c0594d69-c988-4b59-a43f-c6a9ba130483",
            "custom_group_folder_info": [
                "{\"is_translatable\": true, \"name\": \"Root\", \"type\": 1}",
                "{\"is_translatable\": null, \"name\": \"PC\", \"type\": 2}",
                "{\"is_translatable\": null, \"name\": \"Lorem Ipsum Foo Bar\", \"type\": 2}"
            ],
            "device_type": 1,
            "id": "b597cc26-eb5d-5fc4-be0d-b86c08d2d91d",
            "malware_category": 8,
            "malware_category_translated": "Malware URL",
            "number_of_occurrences": 2,
            "path": "https://somewhere.net",
            "security_event_date": "2022-04-07T16:42:25Z",
            "site_name": "GROUPE CORP"
        },
        "event": {
            "reason": "Malware detected",
            "category": [
                "host"
            ],
            "kind": "event",
            "outcome": "success",
            "type": [
                "info"
            ]
        }
    }
    	
	```


=== "Retrieve_Security _Events_for_Devices_indicator_type_detections_3.json"

    ```json
	
    {
        "source": {
            "address": "SourceIPName",
            "ip": "SourceIPName"
        },
        "action": {
            "id": 1,
            "name": "Informed"
        },
        "host": {
            "name": "WIN_SERVER_XY"
        },
        "related": {
            "ip": [
                "SourceIPName"
            ],
            "user": [
                "Username"
            ]
        },
        "rule": {
            "id": "8b7205bc-60e0-45a0-9956-b17b6a8673f6"
        },
        "user": {
            "name": "Username"
        },
        "aether": {
            "security_event_type": 18,
            "rule_risk": -54492359.89028178,
            "event_type": -86726288.19318274,
            "accessed_data": true,
            "alias": "AliasName",
            "count": -10808344,
            "custom_group_folder_id": "1b7205bc-60e0-45a0-9956-b17b6a8673f6",
            "custom_group_folder_info": "urn:uuid:f4f661be-c970-38a6-b384-3b5697ffef28",
            "date": "2020-11-20T20:27:18.725Z",
            "description": "DeviceDescriptionName",
            "detected_by": 68864810.84915292,
            "detection_technology": "DetectionTechnologyName",
            "device_id": "8b7205bc-60e0-45a0-9956-b17b6a8673f6",
            "device_type": -73108038.14936246,
            "direction": 50845497.54724711,
            "discard_motive": -77046516.51787202,
            "domain": "DeviceDomain",
            "dwell_time": 51373899,
            "endpoint_event_date": "2021-07-20T20:27:18.725Z",
            "event_id": 69608597,
            "excluded": true,
            "exploit_technique": "ExploitTechnique",
            "file_info_discard": "FileIndentifierHash",
            "filed_date": "2021-07-20T20:27:18.725Z",
            "hash": "009a9b4ff00946f9a5a5659dfe9086da",
            "id": "8b7205bc-60e0-45a0-9956-b17b6a8673f6",
            "instance_id": "9b7205bc-60e0-45a0-9956-b17b6a8673f6",
            "is_excluded": true,
            "item_name": "NameMalware",
            "like_lihood_of_being_malicious": -18274273.348011777,
            "lock_plus_rule_id": -22540451.640785083,
            "made_external_connections": true,
            "malware_category": -85107213.72887051,
            "malware_name": "MalwareName",
            "malware_type": -62357590.74048821,
            "network_activity_type": -85774927.58794248,
            "number_of_occurrences": 20674256,
            "path": "ThreatPath",
            "platform_id": -70290399.75311546,
            "protection_mode": 5799409.122032538,
            "protocol": -86318449.566446,
            "reclassified_to_type": -88047622.99579449,
            "risk": true,
            "rule_configuration_id": "9b7205bc-60e0-45a0-9956-b17b6a8673f6",
            "rule_mitre": "tactic: TA0006, technique: T1003",
            "rule_name": "RuleName",
            "rule_obsolete": false,
            "security_event_date": "2021-07-20T20:27:18.725Z",
            "since_until_filed": "8.07:06:05",
            "site_id": "8b7205bc-60e0-45a0-9956-b17b6a8673f6",
            "site_name": "SiteName",
            "source_machine_name": "SourceDeviceName",
            "source_user": "SourceUsername",
            "status": 31156035.444223955,
            "was_run": true
        },
        "event": {
            "reason": "Indicators of Attack",
            "category": [
                "host"
            ],
            "kind": "event",
            "outcome": "success",
            "type": [
                "info"
            ]
        }
    }
    	
	```


=== "Retrieve_Security _Events_for_Devices_indicator_type_detections_4.json"

    ```json
	
    {
        "action": {
            "id": 13,
            "name": "After Process Blocked"
        },
        "host": {
            "name": "PC123"
        },
        "aether": {
            "security_event_type": 4,
            "date": "2022-04-07T11:02:36.06",
            "event_id": 1796693,
            "event_type": 1,
            "event_type_translated": "Exploit",
            "exploit_technique": "Exploit/RunPE",
            "hash": "5692CD3902FE3A9619F4B31A36643BAB",
            "path": "COMMON_APPDATA|\\softxyz-scc-0x60dd82a3\\softxyz-scc.exe",
            "protection_mode": 0,
            "protection_mode_translated": "Undefined",
            "risk": false
        },
        "event": {
            "category": [
                "host"
            ],
            "kind": "event",
            "outcome": "success",
            "reason": "Exploits",
            "type": [
                "info"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`aether.accessed_data` | `bool` | None |
|`aether.alias` | `keyword` | None |
|`aether.count` | `long` | None |
|`aether.custom_group_folder_id` | `keyword` | None |
|`aether.custom_group_folder_info` | `keyword` | None |
|`aether.date` | `keyword` | None |
|`aether.description` | `keyword` | None |
|`aether.detected_by` | `long` | None |
|`aether.detection_technology` | `keyword` | None |
|`aether.device_id` | `keyword` | None |
|`aether.device_type` | `long` | None |
|`aether.direction` | `long` | None |
|`aether.discard_motive` | `long` | None |
|`aether.domain` | `keyword` | None |
|`aether.dwell_time` | `long` | None |
|`aether.endpoint_event_date` | `keyword` | None |
|`aether.event_id` | `long` | None |
|`aether.event_type` | `long` | None |
|`aether.excluded` | `bool` | None |
|`aether.exploit_counters.total_affected_devices` | `long` | None |
|`aether.exploit_counters.total_alerts` | `long` | None |
|`aether.exploit_counters.total_data_access` | `long` | None |
|`aether.exploit_counters.total_executed` | `long` | None |
|`aether.exploit_counters.total_external_communications` | `long` | None |
|`aether.exploit_technique` | `keyword` | None |
|`aether.file_info_discard` | `keyword` | None |
|`aether.filed_date` | `keyword` | None |
|`aether.hash` | `keyword` | None |
|`aether.id` | `keyword` | None |
|`aether.instance_id` | `keyword` | None |
|`aether.is_excluded` | `bool` | None |
|`aether.item_name` | `keyword` | None |
|`aether.like_lihood_of_being_malicious` | `long` | None |
|`aether.lock_plus_rule_id` | `long` | None |
|`aether.made_external_connections` | `bool` | None |
|`aether.malware_category` | `long` | None |
|`aether.malware_counters.total_affected_devices` | `long` | None |
|`aether.malware_counters.total_alerts` | `long` | None |
|`aether.malware_counters.total_data_access` | `long` | None |
|`aether.malware_counters.total_executed` | `long` | None |
|`aether.malware_counters.total_external_communications` | `long` | None |
|`aether.malware_name` | `keyword` | None |
|`aether.malware_type` | `long` | None |
|`aether.network_activity_type` | `long` | None |
|`aether.number_of_occurrences` | `number` | None |
|`aether.path` | `keyword` | None |
|`aether.platform_id` | `long` | None |
|`aether.program_blocked_counters.total_programs_blocked` | `long` | None |
|`aether.protection_mode` | `long` | None |
|`aether.protocol` | `long` | None |
|`aether.pups_counters.total_affected_devices` | `long` | None |
|`aether.pups_counters.total_alerts` | `long` | None |
|`aether.pups_counters.total_data_access` | `long` | None |
|`aether.pups_counters.total_executed` | `long` | None |
|`aether.pups_counters.total_external_communications` | `long` | None |
|`aether.reclassified_to_type` | `long` | None |
|`aether.risk` | `bool` | None |
|`aether.rule_configuration_id` | `keyword` | None |
|`aether.rule_mitre` | `keyword` | None |
|`aether.rule_name` | `keyword` | None |
|`aether.rule_obsolete` | `bool` | None |
|`aether.rule_risk` | `long` | None |
|`aether.security_event_date` | `keyword` | None |
|`aether.security_event_type` | `long` | None |
|`aether.since_until_filed` | `keyword` | None |
|`aether.site_id` | `keyword` | None |
|`aether.site_name` | `keyword` | None |
|`aether.source_machine_name` | `keyword` | None |
|`aether.source_user` | `keyword` | None |
|`aether.status` | `long` | None |
|`aether.threats_by_av_counters.total_dangerous_actions_blocked_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_devices_blocked_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_intrusion_attempted_blocked_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_malware_urls_blocked_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_phishing_detected_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_tracking_cookies_detected_by_av` | `long` | None |
|`aether.was_run` | `bool` | None |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`host.name` | `keyword` | Name of the host. |
|`rule.id` | `keyword` | Rule ID |
|`source.ip` | `ip` | IP address of the source. |
|`user.name` | `keyword` | Short name or login of the user. |

