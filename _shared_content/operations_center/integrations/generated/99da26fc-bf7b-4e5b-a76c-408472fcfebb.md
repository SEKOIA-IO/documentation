
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `File monitoring` | Monitor files and devices activities |
| `Process monitoring` | Monitor process activities |
| `Process use of network` | Monitor network activities |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `` |
| Type | `` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "ioc_view_query.json"

    ```json
	
    {
        "message": "{\"upload_size\":1077,\"record_identifier\":\"d327f865227909ad464d67f8\",\"ioc_severity\":4,\"path\":\"HKEY_LOCAL Options\",\"ioc_detection_cvss\":\"4\",\"analysis\":\"{\\\"dep_opt_out\\\":0,\\\"dep_alwayson\\\":0,\\\"dep_opt_in\\\":1}\",\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"COMPLIANCE-DEP-PERMISSIVE\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.name\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"vulnerability_dep\\\",\\\"references\\\":[\\\"http://www.test.com/\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"01:02:03:04:05:06\",\"endpoint_id\":\"0a7e076f-k4p1-428a-8304-azedazedazef\",\"meta_public_ip_country_code\":\"FR\",\"meta_public_ip_postal\":\"35750\",\"schema_version\":\"20\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_detection_access\":\"{\\\"authentication\\\":\\\"None\\\",\\\"complexity\\\":\\\"Low\\\",\\\"vector\\\":\\\"Local\\\"}\",\"ioc_created_at\":\"2022-11-30T09:23:22.226Z\",\"ingestion_timestamp\":\"2022-11-30T09:22:29.980Z\",\"ioc_detection_attack\":\"Exposure\",\"numerics\":false,\"meta_public_ip\":\"1.2.3.4\",\"counter\":2,\"detection_id_dedup\":\"azeifazeiofuhapizefhapzieofhazeufh\",\"meta_hostname\":\"AC061-E44iauzebf\",\"ioc_detection_references\":\"[\\\"http://www.test.com\\\"]\",\"ioc_worker_name\":\"Direct Mapping Worker\",\"ioc_detection_type\":\"Vulnerability\",\"ioc_detection_category\":\"Vulnerability\",\"ioc_unix_time\":\"2022-11-30T09:22:11.000Z\",\"epoch\":1669619877,\"meta_ip_mask\":\"1.2.3.4\",\"meta_public_ip_city\":\"Paris\",\"ioc_worker_id\":\"direct_mapping_worker\",\"unix_time\":\"2022-11-30T09:22:11.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"4C4C4544-0035-4E10-8044-B3C04F5A3333\",\"partition_bucket\":\"87\",\"meta_public_ip_country\":\"France\",\"meta_public_ip_state\":\"Paris\",\"meta_boot_time\":1669798899,\"meta_os_name\":\"Microsoft Windows 10 Professionnel\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.14.90\",\"calendar_time\":\"2022-11-30T09:22:11.000Z\",\"meta_eid\":\"0a7e076f-0316-428a-8304-fea736738c7a\",\"meta_public_ip_longitude\":2.4075,\"ioc_detection_id\":\"COMPLIANCE-DEP-PERMISSIVE\",\"meta_os_platform\":\"windows\",\"meta_username\":\"AC712341234\",\"detection_identifier\":\"d327f865227909ad464d67f8fc9d8e38c4285299f4\",\"query_name\":\"vulnerability_dep\",\"key\":\"HKEY_LOCAL_MACHINE Control\",\"meta_os_version\":\"10.0.19044\",\"meta_public_ip_latitude\":39,\"mtime\":1669757890,\"ioc_detection_licenses\":\"[\\\"MTR\\\"]\",\"name\":\"SystemStartOptions\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"type\":\"REG_SZ\",\"ingest_date\":\"2022-11-30\",\"ioc_detection_impact\":\"{\\\"availability\\\":\\\"Partial\\\",\\\"confidentiality\\\":\\\"Partial\\\",\\\"integrity\\\":\\\"Partial\\\"}\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"customer_id\":\"f7193486-a186-4197-ab40-0ddc013a0a65\",\"data\":\" NOEXECUTE=OPTIN  FVEBOOT=1234567  NOVGA\",\"ioc_detection_description\":\"DEP is not Admin Opt-out or Always-on.\",\"message_identifier\":\"ofiazefoazebfaozuefazeo\",\"ioc_attack_type\":\"Exposure\",\"ioc_detection_weight\":4}",
        "event": {
            "kind": "event",
            "severity": 4,
            "code": "COMPLIANCE-DEP-PERMISSIVE"
        },
        "@timestamp": "2022-11-30T09:22:11Z",
        "user": {
            "name": "AC712341234"
        },
        "registry": {
            "path": "HKEY_LOCAL Options",
            "key": "HKEY_LOCAL_MACHINE Control",
            "data": {
                "type": "REG_SZ",
                "strings": [
                    " NOEXECUTE=OPTIN  FVEBOOT=1234567  NOVGA"
                ]
            }
        },
        "source": {
            "ip": "1.2.3.4",
            "mac": "01:02:03:04:05:06",
            "geo": {
                "country_iso_code": "FR",
                "postal_code": "35750",
                "city_name": "Paris",
                "country_name": "France"
            },
            "address": "1.2.3.4"
        },
        "host": {
            "name": "AC061-E44iauzebf",
            "id": "4C4C4544-0035-4E10-8044-B3C04F5A3333",
            "os": {
                "name": "Microsoft Windows 10 Professionnel",
                "version": "10.0.19044"
            }
        },
        "vulnerability": {
            "reference": "http://www.test.com",
            "description": "DEP is not Admin Opt-out or Always-on."
        },
        "sophos": {
            "threat_center": {
                "cvss": "4",
                "id": "0a7e076f-k4p1-428a-8304-azedazedazef",
                "detection_attack": "Exposure",
                "query": {
                    "source": "xdr_only",
                    "action": "added",
                    "pack_version": "1.14.90",
                    "name": "vulnerability_dep"
                },
                "endpoint": {
                    "type": "computer"
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "AC712341234"
            ]
        }
    }
    	
	```


=== "ioc_view_query1.json"

    ```json
	
    {
        "message": "{\"upload_size\":1291,\"record_identifier\":\"09dd5e717aa664189dqehbfazuebfazuebfiaze\",\"ioc_severity\":4,\"path\":\"LOCAL_MACHINE/test.exe\",\"ioc_detection_cvss\":\"4\",\"analysis\":\"{\\\"os_compatibility_target\\\":\\\"test\\\"}\",\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"COMPLIANCE-APP-COMPAT\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.name\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"vulnerability_app_compatibility\\\",\\\"references\\\":[\\\"https://test.com/\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"01:02:03:04:05:06\",\"endpoint_id\":\"a3288afe-799d-aizuef-azfeef-fazef\",\"schema_version\":\"20\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_detection_access\":\"{\\\"authentication\\\":\\\"None\\\",\\\"complexity\\\":\\\"Low\\\",\\\"vector\\\":\\\"Local\\\"}\",\"ioc_created_at\":\"2022-11-30T09:25:14.805Z\",\"ingestion_timestamp\":\"2022-11-30T09:22:45.391Z\",\"ioc_detection_attack\":\"Exposure\",\"numerics\":false,\"meta_public_ip\":\"1.2.3.4\",\"counter\":0,\"detection_id_dedup\":\"432025a1cb38ad65dc6azefazef\",\"meta_hostname\":\"AKAS-TE8789897\",\"ioc_detection_references\":\"[\\\"https://test.com\\\"]\",\"ioc_worker_name\":\"Direct Mapping Worker\",\"ioc_detection_type\":\"Vulnerability\",\"ioc_detection_category\":\"Vulnerability\",\"ioc_unix_time\":\"2022-11-30T09:22:25.000Z\",\"epoch\":1111100000,\"meta_ip_mask\":\"1.2.3.0\",\"ioc_worker_id\":\"direct_mapping_worker\",\"unix_time\":\"2022-11-30T09:22:25.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"5C32B390-E1EB-D177\",\"partition_bucket\":\"87\",\"meta_boot_time\":1111100000,\"meta_os_name\":\"Microsoft Windows 10 Professionnel\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.14.90\",\"calendar_time\":\"2022-11-30T09:22:25.000Z\",\"meta_eid\":\"a3288afe-799d-46a4-9026-ad5cd41337f4\",\"ioc_detection_id\":\"COMPLIANCE-APP\",\"meta_os_platform\":\"windows\",\"meta_username\":\"AC7500JOIJOIJ\",\"detection_identifier\":\"09dd5e717aa664189d54ea1757ddd6e2beaacd676ffb\",\"query_name\":\"vulnerability_app_compatibility\",\"key\":\"LOCAL_MACHINE/Layers\",\"meta_os_version\":\"10.0.19044\",\"mtime\":1111100000,\"ioc_detection_licenses\":\"[\\\"MTR\\\"]\",\"name\":\"C:test.exe\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"type\":\"REG_SZ\",\"ingest_date\":\"2022-11-30\",\"ioc_detection_impact\":\"{\\\"availability\\\":\\\"Partial\\\",\\\"confidentiality\\\":\\\"Partial\\\",\\\"integrity\\\":\\\"Partial\\\"}\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"customer_id\":\"f7193486-a186-4197\",\"data\":\"HIGHDPITEST\",\"ioc_detection_description\":\"Applications with special compatibility set for an executable.\",\"message_identifier\":\"75e420b40149f07eada47bdb23c28281\",\"ioc_attack_type\":\"Exposure\",\"ioc_detection_weight\":4}",
        "event": {
            "kind": "event",
            "severity": 4,
            "code": "COMPLIANCE-APP"
        },
        "@timestamp": "2022-11-30T09:22:25Z",
        "user": {
            "name": "AC7500JOIJOIJ"
        },
        "registry": {
            "path": "LOCAL_MACHINE/test.exe",
            "key": "LOCAL_MACHINE/Layers",
            "data": {
                "type": "REG_SZ",
                "strings": [
                    "HIGHDPITEST"
                ]
            }
        },
        "source": {
            "ip": "1.2.3.4",
            "mac": "01:02:03:04:05:06",
            "address": "1.2.3.4"
        },
        "host": {
            "name": "AKAS-TE8789897",
            "id": "5C32B390-E1EB-D177",
            "os": {
                "name": "Microsoft Windows 10 Professionnel",
                "version": "10.0.19044"
            }
        },
        "vulnerability": {
            "reference": "https://test.com",
            "description": "Applications with special compatibility set for an executable."
        },
        "sophos": {
            "threat_center": {
                "cvss": "4",
                "id": "a3288afe-799d-aizuef-azfeef-fazef",
                "detection_attack": "Exposure",
                "query": {
                    "source": "xdr_only",
                    "action": "added",
                    "pack_version": "1.14.90",
                    "name": "vulnerability_app_compatibility"
                },
                "endpoint": {
                    "type": "computer"
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "AC7500JOIJOIJ"
            ]
        }
    }
    	
	```


=== "ioc_view_query2.json"

    ```json
	
    {
        "message": "{\"upload_size\":1869,\"record_identifier\":\"864de39eef32\",\"ioc_severity\":5,\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"EVENT-Brute-Force-Attempt\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.name\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"windows_event\\\",\\\"references\\\":[\\\"https://test.com/auditing/event-4625\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"00:01:02:03:04:05\",\"endpoint_id\":\"51a8f1a0-db9d\",\"meta_public_ip_country_code\":\"FR\",\"remote_address\":\"1.2.3.4\",\"schema_version\":\"22\",\"authentication_package\":\"NTLM\",\"remote_port\":0,\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_created_at\":\"2023-07-17T11:34:57.524Z\",\"ingestion_timestamp\":\"2023-07-17T11:34:57.356Z\",\"ioc_detection_attack\":\"Suspicious Activity\",\"numerics\":false,\"eventid\":46254646,\"meta_public_ip\":\"1.2.3.4\",\"counter\":68,\"detection_id_dedup\":\"ab874753684df564365b\",\"logon_type\":3,\"meta_hostname\":\"mytestname-vm\",\"ioc_detection_references\":\"[\\\"https://test.com/auditing/event-4625\\\"]\",\"ioc_worker_name\":\"Direct Mapping Worker\",\"ioc_detection_type\":\"Threat\",\"ioc_detection_category\":\"Threat\",\"status\":\"0xc00000677d\",\"ioc_unix_time\":\"2023-07-17T11:34:45.000Z\",\"username_list\":\"TEST,TEST1,TEST2,TEST3,TEST4, TEST5\",\"epoch\":1689319838,\"event_timestamps\":\"1689589842,1689589974\",\"meta_ip_mask\":\"1.2.3.4\",\"meta_public_ip_city\":\"Camping\",\"failure_reason\":\"%%2313\",\"ioc_worker_id\":\"direct_mapping_worker\",\"transmitted_services\":\"-\",\"unix_time\":\"2023-07-17T11:34:45.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"7BB240A3-B6AC\",\"partition_bucket\":\"10\",\"meta_public_ip_country\":\"France\",\"meta_public_ip_state\":\"Saint Paule\",\"meta_boot_time\":1687956677,\"subject_username\":\"-\",\"meta_os_name\":\"Microsoft Windows 10 Pro N\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.16.54\",\"subject_domain\":\"-\",\"calendar_time\":\"2023-07-17T11:34:45.000Z\",\"meta_eid\":\"51a8f1a0-db9d\",\"meta_public_ip_longitude\":-477.0565,\"ioc_detection_id\":\"EVENT-4625-Brute-Force-Attempt\",\"meta_os_platform\":\"windows\",\"detection_identifier\":\"864de39eef32e68379ce450f5b6ebd4ef7f1\",\"workstation_name\":\"-\",\"query_name\":\"windows_event_invalid_logon_brute_force\",\"key_length\":0,\"provider_name\":\"Microsoft-Windows-Security\",\"meta_os_version\":\"10.0.19044\",\"sub_status\":\"0xc0000064\",\"meta_public_ip_latitude\":-221.9035,\"source\":\"Security\",\"ioc_detection_licenses\":\"[\\\"MTR\\\",\\\"MTRE\\\"]\",\"name\":\"-\",\"description\":\"Source IP is shuffling through 20 or more different usernames, appears to be a brute force attack\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"logon_process\":\"NtLmSsp \",\"ingest_date\":\"2023-07-17\",\"target_domain\":\"\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"customer_id\":\"4feff6df-7454\",\"ioc_detection_description\":\"Windows Event Brute Force Attempt Detected.\",\"message_identifier\":\"7f181e964e95390587e73b\",\"ioc_attack_type\":\"Suspicious Activity\",\"ioc_detection_weight\":5}",
        "event": {
            "kind": "event",
            "severity": 5,
            "reason": "Source IP is shuffling through 20 or more different usernames, appears to be a brute force attack",
            "code": "EVENT-4625-Brute-Force-Attempt"
        },
        "@timestamp": "2023-07-17T11:34:45Z",
        "registry": {
            "data": {
                "strings": [
                    ""
                ]
            }
        },
        "source": {
            "ip": "1.2.3.4",
            "mac": "00:01:02:03:04:05",
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Camping",
                "country_name": "France"
            },
            "address": "1.2.3.4"
        },
        "host": {
            "name": "mytestname-vm",
            "id": "7BB240A3-B6AC",
            "os": {
                "name": "Microsoft Windows 10 Pro N",
                "version": "10.0.19044"
            },
            "domain": "-"
        },
        "vulnerability": {
            "reference": "https://test.com/auditing/event-4625",
            "description": "Windows Event Brute Force Attempt Detected."
        },
        "sophos": {
            "threat_center": {
                "id": "51a8f1a0-db9d",
                "detection_attack": "Suspicious Activity",
                "query": {
                    "source": "xdr_only",
                    "action": "added",
                    "pack_version": "1.16.54",
                    "name": "windows_event_invalid_logon_brute_force"
                },
                "endpoint": {
                    "type": "computer"
                }
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.severity` | `long` | Numeric severity of the event. |
|`host.domain` | `keyword` | Name of the directory the group is a member of. |
|`host.id` | `keyword` | Unique host id. |
|`host.name` | `keyword` | Name of the host. |
|`host.os.name` | `keyword` | Operating system name, without the version. |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`registry.data.strings` | `wildcard` | List of strings representing what was written to the registry. |
|`registry.data.type` | `keyword` | Standard registry type for encoding contents |
|`registry.key` | `keyword` | Hive-relative path of keys. |
|`registry.path` | `keyword` | Full path, including hive, key and value |
|`sophos.threat_center.cvss` | `keyword` | The Common Vulnerability Scoring System |
|`sophos.threat_center.detection_attack` | `keyword` | The attack name |
|`sophos.threat_center.endpoint.type` | `keyword` | The type of the endpoint |
|`sophos.threat_center.id` | `keyword` | The identifier of the endpoint |
|`sophos.threat_center.query.action` | `keyword` | The query action |
|`sophos.threat_center.query.name` | `keyword` | The query name |
|`sophos.threat_center.query.pack_version` | `keyword` | The query pack version |
|`sophos.threat_center.query.source` | `keyword` | The query source |
|`source.geo.city_name` | `keyword` | City name. |
|`source.geo.country_iso_code` | `keyword` | Country ISO code. |
|`source.geo.country_name` | `keyword` | Country name. |
|`source.geo.postal_code` | `keyword` | Postal code. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |
|`user.name` | `keyword` | Short name or login of the user. |
|`vulnerability.description` | `keyword` | Description of the vulnerability. |
|`vulnerability.reference` | `keyword` | Reference of the vulnerability. |

