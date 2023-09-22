
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

Find below few samples of events and how they are normalized by Sekoia.io.


=== "ioc_view_query.json"

    ```json
	
    {
        "message": "{\"upload_size\":1077,\"record_identifier\":\"d327f865227909ad464d67f8\",\"ioc_severity\":4,\"path\":\"HKEY_LOCAL Options\",\"ioc_detection_cvss\":\"4\",\"analysis\":\"{\\\"dep_opt_out\\\":0,\\\"dep_alwayson\\\":0,\\\"dep_opt_in\\\":1}\",\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"COMPLIANCE-DEP-PERMISSIVE\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.name\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"vulnerability_dep\\\",\\\"references\\\":[\\\"http://www.test.com/\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"01:02:03:04:05:06\",\"endpoint_id\":\"0a7e076f-k4p1-428a-8304-azedazedazef\",\"meta_public_ip_country_code\":\"FR\",\"meta_public_ip_postal\":\"35750\",\"schema_version\":\"20\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_detection_access\":\"{\\\"authentication\\\":\\\"None\\\",\\\"complexity\\\":\\\"Low\\\",\\\"vector\\\":\\\"Local\\\"}\",\"ioc_created_at\":\"2022-11-30T09:23:22.226Z\",\"ingestion_timestamp\":\"2022-11-30T09:22:29.980Z\",\"ioc_detection_attack\":\"Exposure\",\"numerics\":false,\"meta_public_ip\":\"1.2.3.4\",\"counter\":2,\"detection_id_dedup\":\"azeifazeiofuhapizefhapzieofhazeufh\",\"meta_hostname\":\"AC061-E44iauzebf\",\"ioc_detection_references\":\"[\\\"http://www.test.com\\\"]\",\"ioc_worker_name\":\"Direct Mapping Worker\",\"ioc_detection_type\":\"Vulnerability\",\"ioc_detection_category\":\"Vulnerability\",\"ioc_unix_time\":\"2022-11-30T09:22:11.000Z\",\"epoch\":1669619877,\"meta_ip_mask\":\"1.2.3.4\",\"meta_public_ip_city\":\"Paris\",\"ioc_worker_id\":\"direct_mapping_worker\",\"unix_time\":\"2022-11-30T09:22:11.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"4C4C4544-0035-4E10-8044-B3C04F5A3333\",\"partition_bucket\":\"87\",\"meta_public_ip_country\":\"France\",\"meta_public_ip_state\":\"Paris\",\"meta_boot_time\":1669798899,\"meta_os_name\":\"Microsoft Windows 10 Professionnel\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.14.90\",\"calendar_time\":\"2022-11-30T09:22:11.000Z\",\"meta_eid\":\"0a7e076f-0316-428a-8304-fea736738c7a\",\"meta_public_ip_longitude\":2.4075,\"ioc_detection_id\":\"COMPLIANCE-DEP-PERMISSIVE\",\"meta_os_platform\":\"windows\",\"meta_username\":\"AC712341234\",\"detection_identifier\":\"d327f865227909ad464d67f8fc9d8e38c4285299f4\",\"query_name\":\"vulnerability_dep\",\"key\":\"HKEY_LOCAL_MACHINE Control\",\"meta_os_version\":\"10.0.19044\",\"meta_public_ip_latitude\":39,\"mtime\":1669757890,\"ioc_detection_licenses\":\"[\\\"MTR\\\"]\",\"name\":\"SystemStartOptions\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"type\":\"REG_SZ\",\"ingest_date\":\"2022-11-30\",\"ioc_detection_impact\":\"{\\\"availability\\\":\\\"Partial\\\",\\\"confidentiality\\\":\\\"Partial\\\",\\\"integrity\\\":\\\"Partial\\\"}\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"customer_id\":\"f7193486-a186-4197-ab40-0ddc013a0a65\",\"data\":\" NOEXECUTE=OPTIN  FVEBOOT=1234567  NOVGA\",\"ioc_detection_description\":\"DEP is not Admin Opt-out or Always-on.\",\"message_identifier\":\"ofiazefoazebfaozuefazeo\",\"ioc_attack_type\":\"Exposure\",\"ioc_detection_weight\":4}",
        "event": {
            "kind": "event",
            "severity": 4,
            "code": "COMPLIANCE-DEP-PERMISSIVE",
            "ingested": "2022-11-30T09:22:29.980000Z"
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
            "nat": {
                "ip": "1.2.3.4"
            },
            "mac": "01:02:03:04:05:06",
            "geo": {
                "country_iso_code": "FR",
                "postal_code": "35750",
                "city_name": "Paris",
                "country_name": "France"
            },
            "bytes": 1077,
            "address": "1.2.3.4"
        },
        "host": {
            "name": "AC061-E44iauzebf",
            "id": "4C4C4544-0035-4E10-8044-B3C04F5A3333",
            "os": {
                "full": "Microsoft Windows 10 Professionnel",
                "name": "windows",
                "version": "10.0.19044"
            }
        },
        "vulnerability": {
            "reference": "http://www.test.com",
            "description": "DEP is not Admin Opt-out or Always-on."
        },
        "process": {
            "name": "Direct Mapping Worker"
        },
        "sophos": {
            "threat_center": {
                "record_identifier": "d327f865227909ad464d67f8",
                "id": "0a7e076f-k4p1-428a-8304-azedazedazef",
                "endpoint": {
                    "type": "computer"
                },
                "worker": {
                    "id": "direct_mapping_worker"
                },
                "aggressive_activity": "False",
                "detection_id_dedup": "azeifazeiofuhapizefhapzieofhazeufh",
                "ioc": {
                    "log_type": "summary",
                    "attack_type": "Exposure",
                    "unix_time": "2022-11-30T09:22:11.000000Z",
                    "detection": {
                        "attack": "Exposure",
                        "cvss": "4",
                        "weight": "4",
                        "licences": [
                            "MTR"
                        ],
                        "type": "Vulnerability",
                        "category": "Vulnerability",
                        "impact": {
                            "availability": "Partial",
                            "integrity": "Partial",
                            "confidentiality": "Partial"
                        },
                        "access": {
                            "complexity": "Low",
                            "vector": "Local"
                        },
                        "sigma": {
                            "id": "COMPLIANCE-DEP-PERMISSIVE"
                        }
                    }
                },
                "query": {
                    "source": "xdr_only",
                    "action": "added",
                    "pack_version": "1.14.90",
                    "name": "vulnerability_dep"
                },
                "analysis": "{\"dep_alwayson\": 0, \"dep_opt_in\": 1, \"dep_opt_out\": 0}"
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
            "code": "COMPLIANCE-APP",
            "ingested": "2022-11-30T09:22:45.391000Z"
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
            "nat": {
                "ip": "1.2.3.4"
            },
            "mac": "01:02:03:04:05:06",
            "bytes": 1291,
            "address": "1.2.3.4"
        },
        "host": {
            "name": "AKAS-TE8789897",
            "id": "5C32B390-E1EB-D177",
            "os": {
                "full": "Microsoft Windows 10 Professionnel",
                "name": "windows",
                "version": "10.0.19044"
            }
        },
        "vulnerability": {
            "reference": "https://test.com",
            "description": "Applications with special compatibility set for an executable."
        },
        "process": {
            "name": "Direct Mapping Worker"
        },
        "sophos": {
            "threat_center": {
                "record_identifier": "09dd5e717aa664189dqehbfazuebfazuebfiaze",
                "id": "a3288afe-799d-aizuef-azfeef-fazef",
                "endpoint": {
                    "type": "computer"
                },
                "worker": {
                    "id": "direct_mapping_worker"
                },
                "aggressive_activity": "False",
                "detection_id_dedup": "432025a1cb38ad65dc6azefazef",
                "ioc": {
                    "log_type": "summary",
                    "attack_type": "Exposure",
                    "unix_time": "2022-11-30T09:22:25.000000Z",
                    "detection": {
                        "attack": "Exposure",
                        "cvss": "4",
                        "weight": "4",
                        "licences": [
                            "MTR"
                        ],
                        "type": "Vulnerability",
                        "category": "Vulnerability",
                        "impact": {
                            "availability": "Partial",
                            "integrity": "Partial",
                            "confidentiality": "Partial"
                        },
                        "access": {
                            "complexity": "Low",
                            "vector": "Local"
                        },
                        "sigma": {
                            "id": "COMPLIANCE-APP-COMPAT"
                        }
                    }
                },
                "query": {
                    "source": "xdr_only",
                    "action": "added",
                    "pack_version": "1.14.90",
                    "name": "vulnerability_app_compatibility"
                },
                "analysis": "{\"os_compatibility_target\": \"test\"}"
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
            "code": "EVENT-4625-Brute-Force-Attempt",
            "ingested": "2023-07-17T11:34:57.356000Z"
        },
        "@timestamp": "2023-07-17T11:34:45Z",
        "source": {
            "ip": "1.2.3.4",
            "nat": {
                "ip": "1.2.3.4"
            },
            "mac": "00:01:02:03:04:05",
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Camping",
                "country_name": "France"
            },
            "bytes": 1869,
            "address": "1.2.3.4"
        },
        "host": {
            "name": "mytestname-vm",
            "id": "7BB240A3-B6AC",
            "os": {
                "full": "Microsoft Windows 10 Pro N",
                "name": "windows",
                "version": "10.0.19044"
            },
            "domain": "-"
        },
        "vulnerability": {
            "reference": "https://test.com/auditing/event-4625",
            "description": "Windows Event Brute Force Attempt Detected."
        },
        "process": {
            "name": "Direct Mapping Worker"
        },
        "destination": {
            "port": 0,
            "address": "1.2.3.4"
        },
        "sophos": {
            "threat_center": {
                "record_identifier": "864de39eef32",
                "event": {
                    "id": 46254646
                },
                "id": "51a8f1a0-db9d",
                "logon_process": "NtLmSsp ",
                "endpoint": {
                    "type": "computer"
                },
                "worker": {
                    "id": "direct_mapping_worker"
                },
                "aggressive_activity": "False",
                "detection_id_dedup": "ab874753684df564365b",
                "ioc": {
                    "log_type": "summary",
                    "attack_type": "Suspicious Activity",
                    "unix_time": "2023-07-17T11:34:45.000000Z",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "weight": "5",
                        "licences": [
                            "MTR",
                            "MTRE"
                        ],
                        "type": "Threat",
                        "category": "Threat",
                        "sigma": {
                            "id": "EVENT-Brute-Force-Attempt"
                        }
                    }
                },
                "query": {
                    "source": "xdr_only",
                    "action": "added",
                    "pack_version": "1.16.54",
                    "name": "windows_event_invalid_logon_brute_force"
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


=== "ioc_view_query3.json"

    ```json
	
    {
        "message": "{\"upload_size\":2056,\"record_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"ioc_severity\":5,\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"EVENT-0000\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_test\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"windows_event_user_account_locked_out\\\",\\\"references\\\":[\\\"https://test.com/event-0000\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"00:11:22:33:44:55\",\"endpoint_id\":\"70599d12-fec7-4129-8844-7c6cfded4642\",\"meta_public_ip_country_code\":\"FR\",\"schema_version\":\"22\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_created_at\":\"2025-12-12T13:59:12.269Z\",\"ingestion_timestamp\":\"2025-12-12T13:59:11.487Z\",\"ioc_detection_attack\":\"Suspicious Activity\",\"numerics\":false,\"eventid\":4740,\"meta_public_ip\":\"1.2.3.4\",\"counter\":1,\"detection_id_dedup\":\"b99ecce6f278bb68406f67ba7dcc76e1de263395\",\"meta_hostname\":\"CER31SVM\",\"ioc_detection_references\":\"[\\\"https://test.com/event-7777\\\"]\",\"ioc_worker_name\":\"IOC worker name\",\"ioc_detection_type\":\"Threat\",\"ioc_detection_category\":\"Threat\",\"ioc_unix_time\":\"2023-12-12T13:58:51.000Z\",\"epoch\":1699999999,\"meta_ip_mask\":\"5.5.5.5\",\"ioc_worker_id\":\"direct_mapping_worker\",\"unix_time\":\"2023-08-17T13:58:51.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"eb37c32a-4285-11ee-be56-0242ac120002\",\"partition_bucket\":\"87\",\"meta_public_ip_country\":\"France\",\"meta_boot_time\":1611110000,\"subject_username\":\"SUBJECTUSERNAME\",\"meta_os_name\":\"Microsoft Windows Server\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.17.56\",\"subject_domain\":\"SUBJECTDOMAIN\",\"calendar_time\":\"2025-12-12T10:00:51.000Z\",\"meta_eid\":\"70599d12-fec7-4129-8844-7c6cfded4642\",\"meta_public_ip_longitude\":46.3387,\"ioc_detection_id\":\"WIN-EVENT-4740\",\"meta_os_platform\":\"windows\",\"meta_username\":\"AC000TEST0011\",\"detection_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002_0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"query_name\":\"windows_query_event\",\"provider_name\":\"Microsoft-Windows-Security-Auditing\",\"meta_os_version\":\"1.0.2s\",\"meta_public_ip_latitude\":55.8582,\"source\":\"Security\",\"ioc_detection_licenses\":\"[\\\"License1\\\",\\\"License2\\\"]\",\"description\":\"A user account was locked out.\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"ingest_date\":\"2023-08-17\",\"target_domain\":\"AC000-TEST0011\",\"meta_endpoint_type\":\"server\",\"meta_domain_controller\":\"False\",\"customer_id\":\"36c536f0-4282-11ee-be56-0242ac120002\",\"ioc_detection_description\":\"Windows Event User Account Locked Out.\",\"message_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"ioc_attack_type\":\"Suspicious Activity\",\"target_username\":\"Administrateur\",\"user_upn\":\"user.mail@company.fr\",\"ml_score_band\":\"HIGH_SUSPICION\",\"target_server\":\"TEST/1.2.3.4\",\"package\":\"TEST\",\"ioc_detection_weight\":5}",
        "event": {
            "kind": "event",
            "severity": 5,
            "reason": "A user account was locked out.",
            "code": "WIN-EVENT-4740",
            "ingested": "2025-12-12T13:59:11.487000Z"
        },
        "@timestamp": "2025-12-12T10:00:51Z",
        "user": {
            "name": "AC000TEST0011",
            "target": {
                "name": "Administrateur"
            }
        },
        "source": {
            "ip": "1.2.3.4",
            "nat": {
                "ip": "1.2.3.4"
            },
            "mac": "00:11:22:33:44:55",
            "geo": {
                "country_iso_code": "FR",
                "country_name": "France"
            },
            "bytes": 2056,
            "address": "1.2.3.4"
        },
        "host": {
            "name": "CER31SVM",
            "id": "eb37c32a-4285-11ee-be56-0242ac120002",
            "os": {
                "full": "Microsoft Windows Server",
                "name": "windows",
                "version": "1.0.2s"
            },
            "domain": "SUBJECTDOMAIN"
        },
        "vulnerability": {
            "reference": "https://test.com/event-7777",
            "description": "Windows Event User Account Locked Out."
        },
        "process": {
            "name": "IOC worker name"
        },
        "destination": {
            "domain": "AC000-TEST0011",
            "address": "AC000-TEST0011"
        },
        "server": {
            "domain": "TEST/1.2.3.4"
        },
        "sophos": {
            "threat_center": {
                "record_identifier": "0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002",
                "event": {
                    "id": 4740
                },
                "id": "70599d12-fec7-4129-8844-7c6cfded4642",
                "user_upn": "user.mail@company.fr",
                "package": "TEST",
                "endpoint": {
                    "type": "server"
                },
                "worker": {
                    "id": "direct_mapping_worker"
                },
                "aggressive_activity": "False",
                "detection_id_dedup": "b99ecce6f278bb68406f67ba7dcc76e1de263395",
                "ioc": {
                    "log_type": "summary",
                    "attack_type": "Suspicious Activity",
                    "unix_time": "2023-12-12T13:58:51.000000Z",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "weight": "5",
                        "licences": [
                            "License1",
                            "License2"
                        ],
                        "type": "Threat",
                        "category": "Threat",
                        "sigma": {
                            "id": "EVENT-0000"
                        }
                    }
                },
                "query": {
                    "source": "xdr_only",
                    "action": "added",
                    "pack_version": "1.17.56",
                    "name": "windows_query_event"
                },
                "ml": {
                    "score_band": "HIGH_SUSPICION"
                }
            }
        },
        "related": {
            "hosts": [
                "AC000-TEST0011",
                "TEST/1.2.3.4"
            ],
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "AC000TEST0011"
            ]
        }
    }
    	
	```


=== "ioc_view_query4.json"

    ```json
	
    {
        "message": "{\"upload_size\":2088,\"record_identifier\":\"0242ac1200020cd6e1e0428211eebe560242ac120002\",\"ioc_severity\":5,\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"EVENT-0000\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_test\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"windows_event_user_account_locked_out\\\",\\\"references\\\":[\\\"https://test.com/event-0000\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"00:11:22:33:44:55\",\"endpoint_id\":\"70599d12-fec7-4129-8844-7c6cfded4642\",\"meta_public_ip_country_code\":\"FR\",\"schema_version\":\"22\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_created_at\":\"2025-12-12T13:59:12.269Z\",\"ingestion_timestamp\":\"2025-12-12T13:59:11.487Z\",\"ioc_detection_attack\":\"Suspicious Activity\",\"numerics\":false,\"eventid\":4740,\"meta_public_ip\":\"1.2.3.4\",\"detection_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002_0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"query_name\":\"windows_query_event\",\"provider_name\":\"Microsoft-Windows-Security-Auditing\",\"meta_os_version\":\"1.0.2s\",\"meta_public_ip_latitude\":55.8582,\"source\":\"Security\",\"ioc_detection_licenses\":\"[\\\"License1\\\",\\\"License2\\\"]\",\"description\":\"A user account was locked out.\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"ingest_date\":\"2023-08-17\",\"target_domain\":\"AC000-TEST0011\",\"meta_endpoint_type\":\"server\",\"meta_domain_controller\":\"False\",\"customer_id\":\"36c536f0-4282-11ee-be56-0242ac120002\",\"ioc_detection_description\":\"Windows Event User Account Locked Out.\",\"message_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"ioc_attack_type\":\"Suspicious Activity\",\"target_username\":\"Administrateur\",\"user_upn\":\"user.mail@company.fr\",\"ml_score_band\":\"HIGH_SUSPICION\",\"target_server\":\"TEST/1.2.3.4\",\"package\":\"TEST\",\"ioc_detection_weight\":5,\"logon_process\":\"logon_process\",\"is_process_file_signed\":\"1\",\"sha1\":\"d4baeeb9180a4284b33fa3602d86c\",\"process_cmd_line\":\"\\\"C:\\\\Program Files (x86)\\\\test.exe\\\" --te /test:5\",\"process_ml_score_band\":\"ml_score\",\"process_parent_name\":\"process_parent.exe\",\"threat_type\":\"threat_type\",\"threat_source\":\"threat_source\",\"ioc_event_path\":\"C:\\\\Program Files (x86)\\\\TEST.EXE\",\"sha256\":\"94256542e235681ba64a20bc50910dd745d52347\",\"cmdline\":\"get_test \",\"password_last_set\":\"18/08/2021 03:37:25\",\"lolbins_ml_results\":{\"score\":19,\"score_label\":\"score_label\",\"sha256\":\"dd6748642b108262f933260c3ae8\"}}",
        "event": {
            "kind": "event",
            "severity": 5,
            "reason": "A user account was locked out.",
            "ingested": "2025-12-12T13:59:11.487000Z"
        },
        "user": {
            "target": {
                "name": "Administrateur"
            }
        },
        "source": {
            "ip": "1.2.3.4",
            "nat": {
                "ip": "1.2.3.4"
            },
            "mac": "00:11:22:33:44:55",
            "geo": {
                "country_iso_code": "FR"
            },
            "bytes": 2088,
            "address": "1.2.3.4"
        },
        "host": {
            "os": {
                "version": "1.0.2s"
            }
        },
        "vulnerability": {
            "description": "Windows Event User Account Locked Out."
        },
        "process": {
            "hash": {
                "sha1": "d4baeeb9180a4284b33fa3602d86c",
                "sha256": "94256542e235681ba64a20bc50910dd745d52347"
            },
            "parent": {
                "name": "process_parent.exe"
            },
            "command_line": "\"C:\\Program Files (x86)\\test.exe\" --te /test:5",
            "code_signature": {
                "exists": true
            }
        },
        "destination": {
            "domain": "AC000-TEST0011",
            "address": "AC000-TEST0011"
        },
        "threat": {
            "indicator": {
                "provider": "threat_source"
            }
        },
        "server": {
            "domain": "TEST/1.2.3.4"
        },
        "file": {
            "path": "C:\\Program Files (x86)\\TEST.EXE",
            "hash": {
                "sha1": "d4baeeb9180a4284b33fa3602d86c",
                "sha256": "94256542e235681ba64a20bc50910dd745d52347"
            },
            "name": "TEST.EXE",
            "directory": "C:\\Program Files (x86)"
        },
        "sophos": {
            "threat_center": {
                "record_identifier": "0242ac1200020cd6e1e0428211eebe560242ac120002",
                "event": {
                    "id": 4740
                },
                "id": "70599d12-fec7-4129-8844-7c6cfded4642",
                "user_upn": "user.mail@company.fr",
                "logon_process": "logon_process",
                "package": "TEST",
                "endpoint": {
                    "type": "server"
                },
                "aggressive_activity": "False",
                "threat_type": "threat_type",
                "process": {
                    "executable": {
                        "is_signed": true
                    }
                },
                "ioc": {
                    "attack_type": "Suspicious Activity",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "weight": "5",
                        "licences": [
                            "License1",
                            "License2"
                        ],
                        "sigma": {
                            "id": "EVENT-0000"
                        }
                    }
                },
                "query": {
                    "name": "windows_query_event"
                },
                "ml": {
                    "score": "19",
                    "score_band": "ml_score"
                },
                "lolbins_ml_results": {
                    "score": "19",
                    "score_label": "score_label",
                    "sha256": "dd6748642b108262f933260c3ae8"
                },
                "password": {
                    "last_set": "2021-08-18T03:37:25.000000Z"
                }
            }
        },
        "related": {
            "hash": [
                "94256542e235681ba64a20bc50910dd745d52347",
                "d4baeeb9180a4284b33fa3602d86c"
            ],
            "hosts": [
                "AC000-TEST0011",
                "TEST/1.2.3.4"
            ],
            "ip": [
                "1.2.3.4"
            ]
        }
    }
    	
	```


=== "ioc_view_query5.json"

    ```json
	
    {
        "message": "{\n  \"parent\": 25740,\n  \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"upload_size\": 2376,\n  \"record_identifier\": \"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044\",\n  \"ioc_severity\": 5,\n  \"path\": \"C:\\\\Windows\\\\System32\\\\wbem\\\\WMIC.exe\",\n  \"is_process_file_signed\": \"1\",\n  \"ml_score_data\": \"{\\\"configVersion\\\":\\\"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044\\\",\\\"expireTime\\\":0,\\\"peMalwareScore\\\":7,\\\"pePuaScore\\\":15,\\\"vdlFlags\\\":0,\\\"version\\\":2}\",\n  \"ioc_detection_sigma\": \"{\\\"id\\\":\\\"WIN-EXE-ENR-ML-SUSPICIOUS-1.star\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.columns.sophosPID\\\",\\\"detection.id\\\"]}}\",\n  \"company_name\": \"Microsoft Corporation\",\n  \"pua_score\": 15,\n  \"folded\": 0,\n  \"meta_mac_address\": \"00:05:9a:3c:7a:00\",\n  \"endpoint_id\": \"7df406c7-efc9-4c7d-806f-1c7216031630\",\n  \"meta_public_ip_country_code\": \"FR\",\n  \"schema_version\": \"22\",\n  \"uid\": 292948,\n  \"ioc_detection_mitre_attack\": \"[{\\\"tactic\\\":{\\\"id\\\":\\\"TA0002\\\",\\\"name\\\":\\\"Execution\\\",\\\"techniques\\\":[{\\\"id\\\":\\\"T1059\\\",\\\"name\\\":\\\"Command and Scripting Interpreter\\\"}]}}]\",\n  \"meta_licence\": \"\",\n  \"ioc_detection_experiment_level\": 0,\n  \"ioc_created_at\": \"2023-08-30T15:04:40.934Z\",\n  \"cmdline\": \"wmic /Namespace:\\\\\\\\root\\\\SecurityCenter2 Path AntivirusProduct Get displayName,productState\",\n  \"ingestion_timestamp\": \"2023-08-30T15:04:17.022Z\",\n  \"ioc_detection_attack\": \"Execution\",\n  \"numerics\": false,\n  \"meta_public_ip\": \"194.0.166.130\",\n  \"counter\": 1414,\n  \"detection_id_dedup\": \"b758901433312f4077ce4ed46b776ecc895712ff\",\n  \"meta_hostname\": \"H3333333333333\",\n  \"username\": \"U11111111\",\n  \"ioc_worker_name\": \"Security Event Service\",\n  \"ioc_detection_type\": \"process\",\n  \"sha1\": \"adc83b19e793491b1c6ea0fd8b46cd9f32e592fc\",\n  \"ioc_detection_category\": \"Threat\",\n  \"ioc_unix_time\": \"2023-08-30T15:03:56.000Z\",\n  \"epoch\": 1693206450,\n  \"meta_ip_mask\": \"255.255.252.0\",\n  \"file_size\": 576000,\n  \"ioc_worker_id\": \"security-event-service\",\n  \"global_rep_data\": \"{\\\"expireTime\\\":0,\\\"lookupType\\\":0,\\\"reputation\\\":-1,\\\"reputationData\\\":\\\"\\\",\\\"sampleRate\\\":0,\\\"version\\\":1}\",\n  \"parent_name\": \"idea64.exe\",\n  \"unix_time\": \"2023-08-30T15:03:56.000Z\",\n  \"pid\": 3984,\n  \"ioc_log_type\": \"summary\",\n  \"original_filename\": \"wmic.exe\",\n  \"ml_score_band\": \"LIKELY_BENIGN\",\n  \"query_source\": \"xdr_only\",\n  \"sophos_pid\": \"3984:133378811508910039\",\n  \"host_identifier\": \"689FF239-6905-4EB3-8CA4-716E63BDB63D\",\n  \"partition_bucket\": \"87\",\n  \"meta_public_ip_country\": \"United-Kingdom\",\n  \"meta_boot_time\": 1693382499,\n  \"local_rep\": 91,\n  \"meta_os_name\": \"Microsoft Windows 10 Professionnel\",\n  \"sha256_reputation_score\": 70,\n  \"osquery_action\": \"added\",\n  \"lolbins_ml_results\": {\n    \"score\": 99.0,\n    \"score_label\": \"Suspicious\",\n    \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\"\n  },\n  \"parent_path\": \"C:\\\\Program Files\\\\JetBrains\\\\IntelliJ IDEA 2021.3.3\\\\bin\\\\idea64.exe\",\n  \"meta_query_pack_version\": \"1.17.56\",\n  \"calendar_time\": \"2023-08-30T15:03:56.000Z\",\n  \"meta_eid\": \"aecc2aae-83d8-4f39-b65a-53413caa415f\",\n  \"meta_public_ip_longitude\": -0.076198,\n  \"ioc_detection_id\": \"WIN-EXE-ENR-ML-SUSPICIOUS-1\",\n  \"meta_os_platform\": \"windows\",\n  \"meta_username\": \"U111111111\",\n  \"detection_identifier\": \"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044_b758901433312f4077ce4ed46b776ecc895712ff\",\n  \"query_name\": \"running_processes_windows_sophos\",\n  \"meta_os_type\": \"\",\n  \"meta_os_version\": \"10.0.19045\",\n  \"parent_cmdline\": \"\\\"C:\\\\Program Files\\\\JetBrains\\\\IntelliJ IDEA 2021.3.3\\\\bin\\\\idea64.exe\\\" \",\n  \"meta_public_ip_latitude\": 51.5082,\n  \"local_rep_data\": \"{\\\"reputationData\\\":{\\\"isSigned\\\":1,\\\"signerInfo\\\":[{\\\"cryptoAlgorithm\\\":32780,\\\"cryptoStrength\\\":112,\\\"isValid\\\":1,\\\"signer\\\":\\\"Microsoft Windows\\\",\\\"thumbprint\\\":\\\"2724aeb0c497bf5fd732958120d1ae3341cfd252ab1680de03d10503abc666c1\\\"}]}}\",\n  \"ioc_detection_licenses\": \"[\\\"MTR\\\"]\",\n  \"parent_sophos_pid\": \"22222:666666666666666666\",\n  \"name\": \"WMIC.exe\",\n  \"global_rep\": -1,\n  \"meta_aggressive_activity\": \"False\",\n  \"meta_ip_address\": \"1.2.3.4\",\n  \"time\": 1693407550,\n  \"file_version\": \"10.0.19041.1741 (WinBuild.160101.0800)\",\n  \"ingest_date\": \"2023-08-30\",\n  \"file_description\": \"WMI Commandline Utility\",\n  \"ml_score\": 7,\n  \"sha256_reputation_band\": \"KNOWN_GOOD\",\n  \"meta_endpoint_type\": \"computer\",\n  \"meta_domain_controller\": \"False\",\n  \"customer_id\": \"9cc350ec-283c-451a-b072-4c7df065d350\",\n  \"ioc_detection_description\": \"Identifies Lolbin processes labeled as suspicious by a machine learning model.\",\n  \"message_identifier\": \"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044\",\n  \"ioc_attack_type\": \"Security Event Service Detections\",\n  \"product_name\": \"Microsoft\u00ae Windows\u00ae Operating System\",\n  \"gid\": 292948,\n  \"ioc_detection_weight\": 5\n}\n",
        "event": {
            "kind": "event",
            "severity": 5,
            "code": "WIN-EXE-ENR-ML-SUSPICIOUS-1",
            "ingested": "2023-08-30T15:04:17.022000Z"
        },
        "@timestamp": "2023-08-30T15:03:56Z",
        "user": {
            "name": "U111111111"
        },
        "source": {
            "ip": "1.2.3.4",
            "nat": {
                "ip": "194.0.166.130"
            },
            "mac": "00:05:9a:3c:7a:00",
            "geo": {
                "country_iso_code": "FR",
                "country_name": "United-Kingdom"
            },
            "bytes": 2376,
            "address": "1.2.3.4"
        },
        "host": {
            "name": "H3333333333333",
            "id": "689FF239-6905-4EB3-8CA4-716E63BDB63D",
            "os": {
                "full": "Microsoft Windows 10 Professionnel",
                "name": "windows",
                "version": "10.0.19045"
            }
        },
        "vulnerability": {
            "description": "Identifies Lolbin processes labeled as suspicious by a machine learning model."
        },
        "process": {
            "pid": 3984,
            "name": "Security Event Service",
            "hash": {
                "sha1": "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc",
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            },
            "parent": {
                "name": "idea64.exe",
                "executable": "C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.3\\bin\\idea64.exe",
                "command_line": "\"C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.3\\bin\\idea64.exe\" "
            },
            "command_line": "wmic /Namespace:\\\\root\\SecurityCenter2 Path AntivirusProduct Get displayName,productState",
            "code_signature": {
                "exists": true
            }
        },
        "file": {
            "size": 576000,
            "hash": {
                "sha1": "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc",
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            },
            "name": "WMIC.exe",
            "path": "C:\\Windows\\System32\\wbem\\WMIC.exe"
        },
        "sophos": {
            "threat_center": {
                "record_identifier": "f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044",
                "id": "7df406c7-efc9-4c7d-806f-1c7216031630",
                "sha256": {
                    "reputation_band": "KNOWN_GOOD",
                    "reputation_score": "70"
                },
                "endpoint": {
                    "type": "computer"
                },
                "worker": {
                    "id": "security-event-service"
                },
                "file": {
                    "version": "10.0.19041.1741 (WinBuild.160101.0800)",
                    "description": "WMI Commandline Utility",
                    "original": {
                        "name": "wmic.exe"
                    }
                },
                "aggressive_activity": "False",
                "detection_id_dedup": "b758901433312f4077ce4ed46b776ecc895712ff",
                "process": {
                    "executable": {
                        "is_signed": true
                    }
                },
                "ioc": {
                    "log_type": "summary",
                    "attack_type": "Security Event Service Detections",
                    "unix_time": "2023-08-30T15:03:56.000000Z",
                    "detection": {
                        "attack": "Execution",
                        "weight": "5",
                        "licences": [
                            "MTR"
                        ],
                        "type": "process",
                        "category": "Threat",
                        "sigma": {
                            "id": "WIN-EXE-ENR-ML-SUSPICIOUS-1.star"
                        }
                    }
                },
                "query": {
                    "source": "xdr_only",
                    "action": "added",
                    "pack_version": "1.17.56",
                    "name": "running_processes_windows_sophos"
                },
                "ml": {
                    "score": "7",
                    "score_band": "LIKELY_BENIGN"
                },
                "lolbins_ml_results": {
                    "score": "99.0",
                    "score_label": "Suspicious",
                    "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
                },
                "pua": {
                    "score": "15"
                },
                "global_rep": -1,
                "ml_score_data": {
                    "config_version": "f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044"
                }
            }
        },
        "related": {
            "hash": [
                "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
                "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc"
            ],
            "ip": [
                "1.2.3.4",
                "194.0.166.130"
            ],
            "user": [
                "U111111111"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.address` | `keyword` | Destination network address. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.ingested` | `date` | Timestamp when an event arrived in the central data store. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.severity` | `long` | Numeric severity of the event. |
|`file.hash.sha1` | `keyword` | SHA1 hash. |
|`file.hash.sha256` | `keyword` | SHA256 hash. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`file.size` | `long` | File size in bytes. |
|`host.domain` | `keyword` | Name of the directory the group is a member of. |
|`host.id` | `keyword` | Unique host id. |
|`host.name` | `keyword` | Name of the host. |
|`host.os.full` | `keyword` | Operating system name, including the version or code name. |
|`host.os.name` | `keyword` | Operating system name, without the version. |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`process.code_signature.exists` | `boolean` | Boolean to capture if a signature is present. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.hash.sha1` | `keyword` | SHA1 hash. |
|`process.hash.sha256` | `keyword` | SHA256 hash. |
|`process.name` | `keyword` | Process name. |
|`process.parent.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.parent.name` | `keyword` | Process name. |
|`process.pid` | `long` | Process id. |
|`registry.data.strings` | `wildcard` | List of strings representing what was written to the registry. |
|`registry.data.type` | `keyword` | Standard registry type for encoding contents |
|`registry.key` | `keyword` | Hive-relative path of keys. |
|`registry.path` | `keyword` | Full path, including hive, key and value |
|`server.domain` | `keyword` | The domain name of the server. |
|`sophos.threat_center.aggressive_activity` | `keyword` | Is there an aggressive activity |
|`sophos.threat_center.analysis` | `keyword` | DEP out mode |
|`sophos.threat_center.detection_id_dedup` | `keyword` | deduplication ID |
|`sophos.threat_center.endpoint.type` | `keyword` | The type of the endpoint |
|`sophos.threat_center.event.id` | `long` | Event id |
|`sophos.threat_center.file.description` | `keyword` | File description |
|`sophos.threat_center.file.original.name` | `keyword` | The original name of the file |
|`sophos.threat_center.file.version` | `keyword` | The version of the file |
|`sophos.threat_center.global_rep` | `integer` | The global response |
|`sophos.threat_center.id` | `keyword` | The identifier of the endpoint |
|`sophos.threat_center.ioc.attack_type` | `keyword` | The attack type |
|`sophos.threat_center.ioc.detection.access.authentication` | `keyword` | Authentication access |
|`sophos.threat_center.ioc.detection.access.complexity` | `keyword` | Complexity access |
|`sophos.threat_center.ioc.detection.access.vector` | `keyword` | Vector access |
|`sophos.threat_center.ioc.detection.attack` | `keyword` | The attack name |
|`sophos.threat_center.ioc.detection.category` | `keyword` | IOC category |
|`sophos.threat_center.ioc.detection.cvss` | `keyword` | The Common Vulnerability Scoring System |
|`sophos.threat_center.ioc.detection.impact.availability` | `keyword` | Availability impact |
|`sophos.threat_center.ioc.detection.impact.confidentiality` | `keyword` | Confidentiality impact |
|`sophos.threat_center.ioc.detection.impact.integrity` | `keyword` | Integrity Impact |
|`sophos.threat_center.ioc.detection.licences` | `keyword` | Detected Licences |
|`sophos.threat_center.ioc.detection.sigma.id` | `keyword` | Sigma ID |
|`sophos.threat_center.ioc.detection.type` | `keyword` | IOC type |
|`sophos.threat_center.ioc.detection.weight` | `keyword` | vulnerability weight |
|`sophos.threat_center.ioc.log_type` | `keyword` | Log type |
|`sophos.threat_center.ioc.unix_time` | `keyword` | Unix time |
|`sophos.threat_center.logon_process` | `keyword` | Verify the identity of the user or system attempting to access the resources |
|`sophos.threat_center.lolbins_ml_results.score` | `keyword` | Lolbins machine learning score |
|`sophos.threat_center.lolbins_ml_results.score_label` | `keyword` | Lolbins machine learning score label |
|`sophos.threat_center.lolbins_ml_results.sha256` | `keyword` | Lolbins machine learning sha256 |
|`sophos.threat_center.ml.score` | `keyword` | Machine learning score |
|`sophos.threat_center.ml.score_band` | `keyword` | Machine learning score band |
|`sophos.threat_center.ml_score_data.config_version` | `keyword` |  |
|`sophos.threat_center.ml_score_data.expire_time` | `keyword` |  |
|`sophos.threat_center.ml_score_data.pe.malware.score` | `keyword` |  |
|`sophos.threat_center.ml_score_data.pe.pua.score` | `keyword` |  |
|`sophos.threat_center.ml_score_data.vldflags` | `keyword` |  |
|`sophos.threat_center.package` | `keyword` | Name of package files |
|`sophos.threat_center.password.last_set` | `keyword` | last time the password is set  |
|`sophos.threat_center.process.executable.is_signed` | `boolean` | Is the image of the process signed |
|`sophos.threat_center.pua.score` | `keyword` | The PUA score |
|`sophos.threat_center.query.action` | `keyword` | The query action |
|`sophos.threat_center.query.name` | `keyword` | The query name |
|`sophos.threat_center.query.pack_version` | `keyword` | The query pack version |
|`sophos.threat_center.query.source` | `keyword` | The query source |
|`sophos.threat_center.record_identifier` | `keyword` | Record identifier |
|`sophos.threat_center.sha256.reputation_band` | `keyword` | sha256 reputation |
|`sophos.threat_center.sha256.reputation_score` | `keyword` | sha256 reputation |
|`sophos.threat_center.threat_type` | `keyword` | Threat type |
|`sophos.threat_center.user_upn` | `keyword` | User Principal Name |
|`sophos.threat_center.worker.id` | `keyword` | Process worker ID (it's a text not a number) |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.geo.city_name` | `keyword` | City name. |
|`source.geo.country_iso_code` | `keyword` | Country ISO code. |
|`source.geo.country_name` | `keyword` | Country name. |
|`source.geo.postal_code` | `keyword` | Postal code. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |
|`source.nat.ip` | `ip` | Source NAT ip |
|`threat.indicator.provider` | `keyword` | Indicator provider |
|`user.name` | `keyword` | Short name or login of the user. |
|`user.target.name` | `keyword` | Short name or login of the user. |
|`vulnerability.description` | `keyword` | Description of the vulnerability. |
|`vulnerability.reference` | `keyword` | Reference of the vulnerability. |

