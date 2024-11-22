
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `File monitoring` | Monitor files and devices activities |
| `Process monitoring` | Monitor process activities |
| `Process use of network` | Monitor network activities |








### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "ioc_view_no_pwd_set.json"

    ```json
	
    {
        "message": "{\"upload_size\":1359,\"profile_path\":\"-\",\"record_identifier\":\"azertyuiop\",\"ioc_severity\":4,\"user_parameters\":\"-\",\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"EVENT-0000.star\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.name\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"00:00:00:00:00:00\",\"endpoint_id\":\"aaa-aaaa-aaa-aaa\",\"meta_public_ip_country_code\":\"FR\",\"schema_version\":\"23\",\"subject_logon_id\":\"0x111\",\"ioc_detection_mitre_attack\":\"[]\",\"user_workstations\":\"-\",\"meta_licence\":\"\",\"ioc_detection_experiment_level\":0,\"privilege_list\":\"-\",\"ioc_created_at\":\"2024-01-17T12:47:16.441Z\",\"ingestion_timestamp\":\"2024-01-17T12:46:35.825Z\",\"home_directory\":\"-\",\"ioc_detection_attack\":\"Suspicious Activity\",\"numerics\":false,\"eventid\":1234,\"meta_public_ip\":\"0.0.0.0\",\"counter\":0,\"detection_id_dedup\":\"aaaaaa\",\"password_last_set\":\"-\",\"meta_hostname\":\"xxxxxx\",\"ioc_detection_references\":\"[\\\"https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738\\\"]\",\"ioc_worker_name\":\"Security Event Service\",\"ioc_detection_type\":\"Threat\",\"ioc_detection_category\":\"Threat\",\"ioc_unix_time\":\"2024-01-17T12:46:21.000Z\",\"epoch\":1705494131,\"meta_ip_mask\":\"255.255.252.0\",\"ioc_worker_id\":\"security-event-service\",\"unix_time\":\"2024-01-17T12:46:21.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"AAA-AAAA-AAA-AAAA\",\"partition_bucket\":\"87\",\"home_path\":\"-\",\"meta_public_ip_country\":\"France\",\"meta_boot_time\":1705494314,\"subject_username\":\"XXXX\",\"meta_os_name\":\"Microsoft Windows 10 Professionnel\",\"osquery_action\":\"added\",\"script_path\":\"-\",\"account_expires\":\"-\",\"meta_query_pack_version\":\"1.18.1\",\"subject_domain\":\"TEST\",\"calendar_time\":\"2024-01-17T12:46:21.000Z\",\"meta_eid\":\"aaaa-aaa-aaa\",\"meta_public_ip_longitude\":1.111,\"ioc_detection_id\":\"WIN-EVENT-1111\",\"meta_os_platform\":\"windows\",\"meta_username\":\"\",\"detection_identifier\":\"aaaaaa\",\"query_name\":\"windows_event_user_account_changed\",\"provider_name\":\"Microsoft-Windows-Security-Auditing\",\"meta_os_type\":\"\",\"meta_os_version\":\"10.0.19045\",\"sam_account_name\":\"-\",\"meta_public_ip_latitude\":1.111,\"source\":\"Security\",\"ioc_detection_licenses\":\"[\\\"MTR\\\",\\\"MTRE\\\"]\",\"user_principal_name\":\"-\",\"description\":\"A User Account was changed\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.1.1.1\",\"ingest_date\":\"2024-01-17\",\"target_domain\":\"Domain-name\",\"uac\":\"-\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"customer_id\":\"aa-aaa-aaa-aaa\",\"ioc_detection_description\":\"Windows Event User Account Changed.\",\"message_identifier\":\"aaaaaa\",\"ioc_attack_type\":\"Security Event Service Detections\",\"target_username\":\"Administrateur\",\"display_name\":\"-\",\"allowed_to_delegate_to\":\"-\",\"ioc_detection_weight\":4}",
        "event": {
            "code": "WIN-EVENT-1111",
            "ingested": "2024-01-17T12:46:35.825000Z",
            "reason": "A User Account was changed",
            "severity": 4
        },
        "@timestamp": "2024-01-17T12:46:21Z",
        "destination": {
            "address": "Domain-name",
            "domain": "Domain-name"
        },
        "host": {
            "domain": "TEST",
            "id": "AAA-AAAA-AAA-AAAA",
            "name": "xxxxxx",
            "os": {
                "full": "Microsoft Windows 10 Professionnel",
                "name": "windows",
                "version": "10.0.19045"
            }
        },
        "process": {
            "name": "Security Event Service"
        },
        "related": {
            "hosts": [
                "Domain-name"
            ],
            "ip": [
                "0.0.0.0",
                "1.1.1.1"
            ]
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "detection_id_dedup": "aaaaaa",
                "endpoint": {
                    "type": "computer"
                },
                "event": {
                    "id": 1234
                },
                "id": "aaa-aaaa-aaa-aaa",
                "ioc": {
                    "attack_type": "Security Event Service Detections",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "category": "Threat",
                        "licences": [
                            "MTR",
                            "MTRE"
                        ],
                        "sigma": {
                            "id": "EVENT-0000.star"
                        },
                        "type": "Threat",
                        "weight": "4"
                    },
                    "log_type": "summary",
                    "unix_time": "2024-01-17T12:46:21.000000Z"
                },
                "message": {
                    "id": "aaaaaa"
                },
                "query": {
                    "action": "added",
                    "name": "windows_event_user_account_changed",
                    "pack_version": "1.18.1",
                    "source": "xdr_only"
                },
                "record_identifier": "azertyuiop",
                "worker": {
                    "id": "security-event-service"
                }
            }
        },
        "source": {
            "address": "1.1.1.1",
            "bytes": 1359,
            "geo": {
                "country_iso_code": "FR",
                "country_name": "France"
            },
            "ip": "1.1.1.1",
            "mac": "00:00:00:00:00:00",
            "nat": {
                "ip": "0.0.0.0"
            }
        },
        "user": {
            "target": {
                "name": "Administrateur"
            }
        },
        "vulnerability": {
            "description": "Windows Event User Account Changed.",
            "reference": "https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738"
        }
    }
    	
	```


=== "ioc_view_query.json"

    ```json
	
    {
        "message": "{\"upload_size\":1077,\"record_identifier\":\"d327f865227909ad464d67f8\",\"ioc_severity\":4,\"path\":\"HKEY_LOCAL Options\",\"ioc_detection_cvss\":\"4\",\"analysis\":\"{\\\"dep_opt_out\\\":0,\\\"dep_alwayson\\\":0,\\\"dep_opt_in\\\":1}\",\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"COMPLIANCE-DEP-PERMISSIVE\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.name\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"vulnerability_dep\\\",\\\"references\\\":[\\\"http://www.test.com/\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"01:02:03:04:05:06\",\"endpoint_id\":\"0a7e076f-k4p1-428a-8304-azedazedazef\",\"meta_public_ip_country_code\":\"FR\",\"meta_public_ip_postal\":\"35750\",\"schema_version\":\"20\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_detection_access\":\"{\\\"authentication\\\":\\\"None\\\",\\\"complexity\\\":\\\"Low\\\",\\\"vector\\\":\\\"Local\\\"}\",\"ioc_created_at\":\"2022-11-30T09:23:22.226Z\",\"ingestion_timestamp\":\"2022-11-30T09:22:29.980Z\",\"ioc_detection_attack\":\"Exposure\",\"numerics\":false,\"meta_public_ip\":\"1.2.3.4\",\"counter\":2,\"detection_id_dedup\":\"azeifazeiofuhapizefhapzieofhazeufh\",\"meta_hostname\":\"AC061-E44iauzebf\",\"ioc_detection_references\":\"[\\\"http://www.test.com\\\"]\",\"ioc_worker_name\":\"Direct Mapping Worker\",\"ioc_detection_type\":\"Vulnerability\",\"ioc_detection_category\":\"Vulnerability\",\"ioc_unix_time\":\"2022-11-30T09:22:11.000Z\",\"epoch\":1669619877,\"meta_ip_mask\":\"1.2.3.4\",\"meta_public_ip_city\":\"Paris\",\"ioc_worker_id\":\"direct_mapping_worker\",\"unix_time\":\"2022-11-30T09:22:11.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"4C4C4544-0035-4E10-8044-B3C04F5A3333\",\"partition_bucket\":\"87\",\"meta_public_ip_country\":\"France\",\"meta_public_ip_state\":\"Paris\",\"meta_boot_time\":1669798899,\"meta_os_name\":\"Microsoft Windows 10 Professionnel\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.14.90\",\"calendar_time\":\"2022-11-30T09:22:11.000Z\",\"meta_eid\":\"0a7e076f-0316-428a-8304-fea736738c7a\",\"meta_public_ip_longitude\":2.4075,\"ioc_detection_id\":\"COMPLIANCE-DEP-PERMISSIVE\",\"meta_os_platform\":\"windows\",\"meta_username\":\"AC712341234\",\"detection_identifier\":\"d327f865227909ad464d67f8fc9d8e38c4285299f4\",\"query_name\":\"vulnerability_dep\",\"key\":\"HKEY_LOCAL_MACHINE Control\",\"meta_os_version\":\"10.0.19044\",\"meta_public_ip_latitude\":39,\"mtime\":1669757890,\"ioc_detection_licenses\":\"[\\\"MTR\\\"]\",\"name\":\"SystemStartOptions\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"type\":\"REG_SZ\",\"ingest_date\":\"2022-11-30\",\"ioc_detection_impact\":\"{\\\"availability\\\":\\\"Partial\\\",\\\"confidentiality\\\":\\\"Partial\\\",\\\"integrity\\\":\\\"Partial\\\"}\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"customer_id\":\"f7193486-a186-4197-ab40-0ddc013a0a65\",\"data\":\" NOEXECUTE=OPTIN  FVEBOOT=1234567  NOVGA\",\"ioc_detection_description\":\"DEP is not Admin Opt-out or Always-on.\",\"message_identifier\":\"ofiazefoazebfaozuefazeo\",\"ioc_attack_type\":\"Exposure\",\"ioc_detection_weight\":4}",
        "event": {
            "code": "COMPLIANCE-DEP-PERMISSIVE",
            "ingested": "2022-11-30T09:22:29.980000Z",
            "severity": 4
        },
        "@timestamp": "2022-11-30T09:22:11Z",
        "host": {
            "id": "4C4C4544-0035-4E10-8044-B3C04F5A3333",
            "name": "AC061-E44iauzebf",
            "os": {
                "full": "Microsoft Windows 10 Professionnel",
                "name": "windows",
                "version": "10.0.19044"
            }
        },
        "process": {
            "name": "Direct Mapping Worker"
        },
        "registry": {
            "data": {
                "strings": [
                    " NOEXECUTE=OPTIN  FVEBOOT=1234567  NOVGA"
                ],
                "type": "REG_SZ"
            },
            "key": "HKEY_LOCAL_MACHINE Control",
            "path": "HKEY_LOCAL Options"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "AC712341234"
            ]
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "analysis": "{\"dep_alwayson\": 0, \"dep_opt_in\": 1, \"dep_opt_out\": 0}",
                "detection_id_dedup": "azeifazeiofuhapizefhapzieofhazeufh",
                "endpoint": {
                    "type": "computer"
                },
                "id": "0a7e076f-k4p1-428a-8304-azedazedazef",
                "ioc": {
                    "attack_type": "Exposure",
                    "detection": {
                        "access": {
                            "complexity": "Low",
                            "vector": "Local"
                        },
                        "attack": "Exposure",
                        "category": "Vulnerability",
                        "cvss": "4",
                        "impact": {
                            "availability": "Partial",
                            "confidentiality": "Partial",
                            "integrity": "Partial"
                        },
                        "licences": [
                            "MTR"
                        ],
                        "sigma": {
                            "id": "COMPLIANCE-DEP-PERMISSIVE"
                        },
                        "type": "Vulnerability",
                        "weight": "4"
                    },
                    "log_type": "summary",
                    "unix_time": "2022-11-30T09:22:11.000000Z"
                },
                "message": {
                    "id": "ofiazefoazebfaozuefazeo"
                },
                "query": {
                    "action": "added",
                    "name": "vulnerability_dep",
                    "pack_version": "1.14.90",
                    "source": "xdr_only"
                },
                "record_identifier": "d327f865227909ad464d67f8",
                "worker": {
                    "id": "direct_mapping_worker"
                }
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 1077,
            "geo": {
                "city_name": "Paris",
                "country_iso_code": "FR",
                "country_name": "France",
                "postal_code": "35750"
            },
            "ip": "1.2.3.4",
            "mac": "01:02:03:04:05:06",
            "nat": {
                "ip": "1.2.3.4"
            }
        },
        "user": {
            "name": "AC712341234"
        },
        "vulnerability": {
            "description": "DEP is not Admin Opt-out or Always-on.",
            "reference": "http://www.test.com"
        }
    }
    	
	```


=== "ioc_view_query1.json"

    ```json
	
    {
        "message": "{\"upload_size\":1291,\"record_identifier\":\"09dd5e717aa664189dqehbfazuebfazuebfiaze\",\"ioc_severity\":4,\"path\":\"LOCAL_MACHINE/test.exe\",\"ioc_detection_cvss\":\"4\",\"analysis\":\"{\\\"os_compatibility_target\\\":\\\"test\\\"}\",\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"COMPLIANCE-APP-COMPAT\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.name\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"vulnerability_app_compatibility\\\",\\\"references\\\":[\\\"https://test.com/\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"01:02:03:04:05:06\",\"endpoint_id\":\"a3288afe-799d-aizuef-azfeef-fazef\",\"schema_version\":\"20\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_detection_access\":\"{\\\"authentication\\\":\\\"None\\\",\\\"complexity\\\":\\\"Low\\\",\\\"vector\\\":\\\"Local\\\"}\",\"ioc_created_at\":\"2022-11-30T09:25:14.805Z\",\"ingestion_timestamp\":\"2022-11-30T09:22:45.391Z\",\"ioc_detection_attack\":\"Exposure\",\"numerics\":false,\"meta_public_ip\":\"1.2.3.4\",\"counter\":0,\"detection_id_dedup\":\"432025a1cb38ad65dc6azefazef\",\"meta_hostname\":\"AKAS-TE8789897\",\"ioc_detection_references\":\"[\\\"https://test.com\\\"]\",\"ioc_worker_name\":\"Direct Mapping Worker\",\"ioc_detection_type\":\"Vulnerability\",\"ioc_detection_category\":\"Vulnerability\",\"ioc_unix_time\":\"2022-11-30T09:22:25.000Z\",\"epoch\":1111100000,\"meta_ip_mask\":\"1.2.3.0\",\"ioc_worker_id\":\"direct_mapping_worker\",\"unix_time\":\"2022-11-30T09:22:25.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"5C32B390-E1EB-D177\",\"partition_bucket\":\"87\",\"meta_boot_time\":1111100000,\"meta_os_name\":\"Microsoft Windows 10 Professionnel\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.14.90\",\"calendar_time\":\"2022-11-30T09:22:25.000Z\",\"meta_eid\":\"a3288afe-799d-46a4-9026-ad5cd41337f4\",\"ioc_detection_id\":\"COMPLIANCE-APP\",\"meta_os_platform\":\"windows\",\"meta_username\":\"AC7500JOIJOIJ\",\"detection_identifier\":\"09dd5e717aa664189d54ea1757ddd6e2beaacd676ffb\",\"query_name\":\"vulnerability_app_compatibility\",\"key\":\"LOCAL_MACHINE/Layers\",\"meta_os_version\":\"10.0.19044\",\"mtime\":1111100000,\"ioc_detection_licenses\":\"[\\\"MTR\\\"]\",\"name\":\"C:test.exe\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"type\":\"REG_SZ\",\"ingest_date\":\"2022-11-30\",\"ioc_detection_impact\":\"{\\\"availability\\\":\\\"Partial\\\",\\\"confidentiality\\\":\\\"Partial\\\",\\\"integrity\\\":\\\"Partial\\\"}\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"customer_id\":\"f7193486-a186-4197\",\"data\":\"HIGHDPITEST\",\"ioc_detection_description\":\"Applications with special compatibility set for an executable.\",\"message_identifier\":\"75e420b40149f07eada47bdb23c28281\",\"ioc_attack_type\":\"Exposure\",\"ioc_detection_weight\":4}",
        "event": {
            "code": "COMPLIANCE-APP",
            "ingested": "2022-11-30T09:22:45.391000Z",
            "severity": 4
        },
        "@timestamp": "2022-11-30T09:22:25Z",
        "host": {
            "id": "5C32B390-E1EB-D177",
            "name": "AKAS-TE8789897",
            "os": {
                "full": "Microsoft Windows 10 Professionnel",
                "name": "windows",
                "version": "10.0.19044"
            }
        },
        "process": {
            "name": "Direct Mapping Worker"
        },
        "registry": {
            "data": {
                "strings": [
                    "HIGHDPITEST"
                ],
                "type": "REG_SZ"
            },
            "key": "LOCAL_MACHINE/Layers",
            "path": "LOCAL_MACHINE/test.exe"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "AC7500JOIJOIJ"
            ]
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "analysis": "{\"os_compatibility_target\": \"test\"}",
                "detection_id_dedup": "432025a1cb38ad65dc6azefazef",
                "endpoint": {
                    "type": "computer"
                },
                "id": "a3288afe-799d-aizuef-azfeef-fazef",
                "ioc": {
                    "attack_type": "Exposure",
                    "detection": {
                        "access": {
                            "complexity": "Low",
                            "vector": "Local"
                        },
                        "attack": "Exposure",
                        "category": "Vulnerability",
                        "cvss": "4",
                        "impact": {
                            "availability": "Partial",
                            "confidentiality": "Partial",
                            "integrity": "Partial"
                        },
                        "licences": [
                            "MTR"
                        ],
                        "sigma": {
                            "id": "COMPLIANCE-APP-COMPAT"
                        },
                        "type": "Vulnerability",
                        "weight": "4"
                    },
                    "log_type": "summary",
                    "unix_time": "2022-11-30T09:22:25.000000Z"
                },
                "message": {
                    "id": "75e420b40149f07eada47bdb23c28281"
                },
                "query": {
                    "action": "added",
                    "name": "vulnerability_app_compatibility",
                    "pack_version": "1.14.90",
                    "source": "xdr_only"
                },
                "record_identifier": "09dd5e717aa664189dqehbfazuebfazuebfiaze",
                "worker": {
                    "id": "direct_mapping_worker"
                }
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 1291,
            "ip": "1.2.3.4",
            "mac": "01:02:03:04:05:06",
            "nat": {
                "ip": "1.2.3.4"
            }
        },
        "user": {
            "name": "AC7500JOIJOIJ"
        },
        "vulnerability": {
            "description": "Applications with special compatibility set for an executable.",
            "reference": "https://test.com"
        }
    }
    	
	```


=== "ioc_view_query2.json"

    ```json
	
    {
        "message": "{\"upload_size\":1869,\"record_identifier\":\"864de39eef32\",\"ioc_severity\":5,\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"EVENT-Brute-Force-Attempt\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.name\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"windows_event\\\",\\\"references\\\":[\\\"https://test.com/auditing/event-4625\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"00:01:02:03:04:05\",\"endpoint_id\":\"51a8f1a0-db9d\",\"meta_public_ip_country_code\":\"FR\",\"remote_address\":\"1.2.3.4\",\"schema_version\":\"22\",\"authentication_package\":\"NTLM\",\"remote_port\":0,\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_created_at\":\"2023-07-17T11:34:57.524Z\",\"ingestion_timestamp\":\"2023-07-17T11:34:57.356Z\",\"ioc_detection_attack\":\"Suspicious Activity\",\"numerics\":false,\"eventid\":46254646,\"meta_public_ip\":\"1.2.3.4\",\"counter\":68,\"detection_id_dedup\":\"ab874753684df564365b\",\"logon_type\":3,\"meta_hostname\":\"mytestname-vm\",\"ioc_detection_references\":\"[\\\"https://test.com/auditing/event-4625\\\"]\",\"ioc_worker_name\":\"Direct Mapping Worker\",\"ioc_detection_type\":\"Threat\",\"ioc_detection_category\":\"Threat\",\"status\":\"0xc00000677d\",\"ioc_unix_time\":\"2023-07-17T11:34:45.000Z\",\"username_list\":\"TEST,TEST1,TEST2,TEST3,TEST4, TEST5\",\"epoch\":1689319838,\"event_timestamps\":\"1689589842,1689589974\",\"meta_ip_mask\":\"1.2.3.4\",\"meta_public_ip_city\":\"Camping\",\"failure_reason\":\"%%2313\",\"ioc_worker_id\":\"direct_mapping_worker\",\"transmitted_services\":\"-\",\"unix_time\":\"2023-07-17T11:34:45.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"7BB240A3-B6AC\",\"partition_bucket\":\"10\",\"meta_public_ip_country\":\"France\",\"meta_public_ip_state\":\"Saint Paule\",\"meta_boot_time\":1687956677,\"subject_username\":\"-\",\"meta_os_name\":\"Microsoft Windows 10 Pro N\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.16.54\",\"subject_domain\":\"-\",\"calendar_time\":\"2023-07-17T11:34:45.000Z\",\"meta_eid\":\"51a8f1a0-db9d\",\"meta_public_ip_longitude\":-477.0565,\"ioc_detection_id\":\"EVENT-4625-Brute-Force-Attempt\",\"meta_os_platform\":\"windows\",\"detection_identifier\":\"864de39eef32e68379ce450f5b6ebd4ef7f1\",\"workstation_name\":\"-\",\"query_name\":\"windows_event_invalid_logon_brute_force\",\"key_length\":0,\"provider_name\":\"Microsoft-Windows-Security\",\"meta_os_version\":\"10.0.19044\",\"sub_status\":\"0xc0000064\",\"meta_public_ip_latitude\":-221.9035,\"source\":\"Security\",\"ioc_detection_licenses\":\"[\\\"MTR\\\",\\\"MTRE\\\"]\",\"name\":\"-\",\"description\":\"Source IP is shuffling through 20 or more different usernames, appears to be a brute force attack\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"logon_process\":\"NtLmSsp \",\"ingest_date\":\"2023-07-17\",\"target_domain\":\"\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"customer_id\":\"4feff6df-7454\",\"ioc_detection_description\":\"Windows Event Brute Force Attempt Detected.\",\"message_identifier\":\"7f181e964e95390587e73b\",\"ioc_attack_type\":\"Suspicious Activity\",\"ioc_detection_weight\":5}",
        "event": {
            "code": "EVENT-4625-Brute-Force-Attempt",
            "ingested": "2023-07-17T11:34:57.356000Z",
            "reason": "Source IP is shuffling through 20 or more different usernames, appears to be a brute force attack",
            "severity": 5
        },
        "@timestamp": "2023-07-17T11:34:45Z",
        "destination": {
            "address": "1.2.3.4",
            "port": 0
        },
        "host": {
            "domain": "-",
            "id": "7BB240A3-B6AC",
            "name": "mytestname-vm",
            "os": {
                "full": "Microsoft Windows 10 Pro N",
                "name": "windows",
                "version": "10.0.19044"
            }
        },
        "process": {
            "name": "Direct Mapping Worker"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "detection_id_dedup": "ab874753684df564365b",
                "endpoint": {
                    "type": "computer"
                },
                "event": {
                    "id": 46254646
                },
                "id": "51a8f1a0-db9d",
                "ioc": {
                    "attack_type": "Suspicious Activity",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "category": "Threat",
                        "licences": [
                            "MTR",
                            "MTRE"
                        ],
                        "sigma": {
                            "id": "EVENT-Brute-Force-Attempt"
                        },
                        "type": "Threat",
                        "weight": "5"
                    },
                    "log_type": "summary",
                    "unix_time": "2023-07-17T11:34:45.000000Z"
                },
                "logon_process": "NtLmSsp ",
                "message": {
                    "id": "7f181e964e95390587e73b"
                },
                "query": {
                    "action": "added",
                    "name": "windows_event_invalid_logon_brute_force",
                    "pack_version": "1.16.54",
                    "source": "xdr_only"
                },
                "record_identifier": "864de39eef32",
                "worker": {
                    "id": "direct_mapping_worker"
                }
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 1869,
            "geo": {
                "city_name": "Camping",
                "country_iso_code": "FR",
                "country_name": "France"
            },
            "ip": "1.2.3.4",
            "mac": "00:01:02:03:04:05",
            "nat": {
                "ip": "1.2.3.4"
            }
        },
        "vulnerability": {
            "description": "Windows Event Brute Force Attempt Detected.",
            "reference": "https://test.com/auditing/event-4625"
        }
    }
    	
	```


=== "ioc_view_query3.json"

    ```json
	
    {
        "message": "{\"upload_size\":2056,\"record_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"ioc_severity\":5,\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"EVENT-0000\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_test\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"windows_event_user_account_locked_out\\\",\\\"references\\\":[\\\"https://test.com/event-0000\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"00:11:22:33:44:55\",\"endpoint_id\":\"70599d12-fec7-4129-8844-7c6cfded4642\",\"meta_public_ip_country_code\":\"FR\",\"schema_version\":\"22\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_created_at\":\"2025-12-12T13:59:12.269Z\",\"ingestion_timestamp\":\"2025-12-12T13:59:11.487Z\",\"ioc_detection_attack\":\"Suspicious Activity\",\"numerics\":false,\"eventid\":4740,\"meta_public_ip\":\"1.2.3.4\",\"counter\":1,\"detection_id_dedup\":\"b99ecce6f278bb68406f67ba7dcc76e1de263395\",\"meta_hostname\":\"CER31SVM\",\"ioc_detection_references\":\"[\\\"https://test.com/event-7777\\\"]\",\"ioc_worker_name\":\"IOC worker name\",\"ioc_detection_type\":\"Threat\",\"ioc_detection_category\":\"Threat\",\"ioc_unix_time\":\"2023-12-12T13:58:51.000Z\",\"epoch\":1699999999,\"meta_ip_mask\":\"5.5.5.5\",\"ioc_worker_id\":\"direct_mapping_worker\",\"unix_time\":\"2023-08-17T13:58:51.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"host_identifier\":\"eb37c32a-4285-11ee-be56-0242ac120002\",\"partition_bucket\":\"87\",\"meta_public_ip_country\":\"France\",\"meta_boot_time\":1611110000,\"subject_username\":\"SUBJECTUSERNAME\",\"meta_os_name\":\"Microsoft Windows Server\",\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.17.56\",\"subject_domain\":\"SUBJECTDOMAIN\",\"calendar_time\":\"2025-12-12T10:00:51.000Z\",\"meta_eid\":\"70599d12-fec7-4129-8844-7c6cfded4642\",\"meta_public_ip_longitude\":46.3387,\"ioc_detection_id\":\"WIN-EVENT-4740\",\"meta_os_platform\":\"windows\",\"meta_username\":\"AC000TEST0011\",\"detection_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002_0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"query_name\":\"windows_query_event\",\"provider_name\":\"Microsoft-Windows-Security-Auditing\",\"meta_os_version\":\"1.0.2s\",\"meta_public_ip_latitude\":55.8582,\"source\":\"Security\",\"ioc_detection_licenses\":\"[\\\"License1\\\",\\\"License2\\\"]\",\"description\":\"A user account was locked out.\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"ingest_date\":\"2023-08-17\",\"target_domain\":\"AC000-TEST0011\",\"meta_endpoint_type\":\"server\",\"meta_domain_controller\":\"False\",\"customer_id\":\"36c536f0-4282-11ee-be56-0242ac120002\",\"ioc_detection_description\":\"Windows Event User Account Locked Out.\",\"message_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"ioc_attack_type\":\"Suspicious Activity\",\"target_username\":\"Administrateur\",\"user_upn\":\"user.mail@company.fr\",\"ml_score_band\":\"HIGH_SUSPICION\",\"target_server\":\"TEST/1.2.3.4\",\"package\":\"TEST\",\"ioc_detection_weight\":5}",
        "event": {
            "code": "WIN-EVENT-4740",
            "ingested": "2025-12-12T13:59:11.487000Z",
            "reason": "A user account was locked out.",
            "severity": 5
        },
        "@timestamp": "2025-12-12T10:00:51Z",
        "destination": {
            "address": "AC000-TEST0011",
            "domain": "AC000-TEST0011"
        },
        "host": {
            "domain": "SUBJECTDOMAIN",
            "id": "eb37c32a-4285-11ee-be56-0242ac120002",
            "name": "CER31SVM",
            "os": {
                "full": "Microsoft Windows Server",
                "name": "windows",
                "version": "1.0.2s"
            }
        },
        "process": {
            "name": "IOC worker name"
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
        },
        "server": {
            "domain": "TEST/1.2.3.4"
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "detection_id_dedup": "b99ecce6f278bb68406f67ba7dcc76e1de263395",
                "endpoint": {
                    "type": "server"
                },
                "event": {
                    "id": 4740
                },
                "id": "70599d12-fec7-4129-8844-7c6cfded4642",
                "ioc": {
                    "attack_type": "Suspicious Activity",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "category": "Threat",
                        "licences": [
                            "License1",
                            "License2"
                        ],
                        "sigma": {
                            "id": "EVENT-0000"
                        },
                        "type": "Threat",
                        "weight": "5"
                    },
                    "log_type": "summary",
                    "unix_time": "2023-12-12T13:58:51.000000Z"
                },
                "message": {
                    "id": "0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002"
                },
                "ml": {
                    "score_band": "HIGH_SUSPICION"
                },
                "package": "TEST",
                "query": {
                    "action": "added",
                    "name": "windows_query_event",
                    "pack_version": "1.17.56",
                    "source": "xdr_only"
                },
                "record_identifier": "0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002",
                "user_upn": "user.mail@company.fr",
                "worker": {
                    "id": "direct_mapping_worker"
                }
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 2056,
            "geo": {
                "country_iso_code": "FR",
                "country_name": "France"
            },
            "ip": "1.2.3.4",
            "mac": "00:11:22:33:44:55",
            "nat": {
                "ip": "1.2.3.4"
            }
        },
        "user": {
            "name": "AC000TEST0011",
            "target": {
                "name": "Administrateur"
            }
        },
        "vulnerability": {
            "description": "Windows Event User Account Locked Out.",
            "reference": "https://test.com/event-7777"
        }
    }
    	
	```


=== "ioc_view_query4.json"

    ```json
	
    {
        "message": "{\"upload_size\":2088,\"record_identifier\":\"0242ac1200020cd6e1e0428211eebe560242ac120002\",\"ioc_severity\":5,\"ioc_detection_sigma\":\"{\\\"id\\\":\\\"EVENT-0000\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_test\\\"],\\\"product\\\":\\\"windows\\\",\\\"platform\\\":\\\"windows\\\",\\\"category\\\":\\\"windows_event_user_account_locked_out\\\",\\\"references\\\":[\\\"https://test.com/event-0000\\\"]}}\",\"folded\":0,\"meta_mac_address\":\"00:11:22:33:44:55\",\"endpoint_id\":\"70599d12-fec7-4129-8844-7c6cfded4642\",\"meta_public_ip_country_code\":\"FR\",\"schema_version\":\"22\",\"ioc_detection_mitre_attack\":\"[]\",\"ioc_detection_experiment_level\":0,\"ioc_created_at\":\"2025-12-12T13:59:12.269Z\",\"ingestion_timestamp\":\"2025-12-12T13:59:11.487Z\",\"ioc_detection_attack\":\"Suspicious Activity\",\"numerics\":false,\"eventid\":4740,\"meta_public_ip\":\"1.2.3.4\",\"detection_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002_0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"query_name\":\"windows_query_event\",\"provider_name\":\"Microsoft-Windows-Security-Auditing\",\"meta_os_version\":\"1.0.2s\",\"meta_public_ip_latitude\":55.8582,\"source\":\"Security\",\"ioc_detection_licenses\":\"[\\\"License1\\\",\\\"License2\\\"]\",\"description\":\"A user account was locked out.\",\"meta_aggressive_activity\":\"False\",\"meta_ip_address\":\"1.2.3.4\",\"ingest_date\":\"2023-08-17\",\"target_domain\":\"AC000-TEST0011\",\"meta_endpoint_type\":\"server\",\"meta_domain_controller\":\"False\",\"customer_id\":\"36c536f0-4282-11ee-be56-0242ac120002\",\"ioc_detection_description\":\"Windows Event User Account Locked Out.\",\"message_identifier\":\"0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002\",\"ioc_attack_type\":\"Suspicious Activity\",\"target_username\":\"Administrateur\",\"user_upn\":\"user.mail@company.fr\",\"ml_score_band\":\"HIGH_SUSPICION\",\"target_server\":\"TEST/1.2.3.4\",\"package\":\"TEST\",\"ioc_detection_weight\":5,\"logon_process\":\"logon_process\",\"is_process_file_signed\":\"1\",\"sha1\":\"d4baeeb9180a4284b33fa3602d86c\",\"process_cmd_line\":\"\\\"C:\\\\Program Files (x86)\\\\test.exe\\\" --te /test:5\",\"process_ml_score_band\":\"ml_score\",\"process_parent_name\":\"process_parent.exe\",\"threat_type\":\"threat_type\",\"threat_source\":\"threat_source\",\"ioc_event_path\":\"C:\\\\Program Files (x86)\\\\TEST.EXE\",\"sha256\":\"94256542e235681ba64a20bc50910dd745d52347\",\"cmdline\":\"get_test \",\"password_last_set\":\"18/08/2021 03:37:25\",\"lolbins_ml_results\":{\"score\":19,\"score_label\":\"score_label\",\"sha256\":\"dd6748642b108262f933260c3ae8\"}}",
        "event": {
            "ingested": "2025-12-12T13:59:11.487000Z",
            "reason": "A user account was locked out.",
            "severity": 5
        },
        "destination": {
            "address": "AC000-TEST0011",
            "domain": "AC000-TEST0011"
        },
        "file": {
            "directory": "C:\\Program Files (x86)",
            "hash": {
                "sha1": "d4baeeb9180a4284b33fa3602d86c",
                "sha256": "94256542e235681ba64a20bc50910dd745d52347"
            },
            "name": "TEST.EXE",
            "path": "C:\\Program Files (x86)\\TEST.EXE"
        },
        "host": {
            "os": {
                "version": "1.0.2s"
            }
        },
        "process": {
            "code_signature": {
                "exists": true
            },
            "command_line": "\"C:\\Program Files (x86)\\test.exe\" --te /test:5",
            "hash": {
                "sha1": "d4baeeb9180a4284b33fa3602d86c",
                "sha256": "94256542e235681ba64a20bc50910dd745d52347"
            },
            "parent": {
                "name": "process_parent.exe"
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
        },
        "server": {
            "domain": "TEST/1.2.3.4"
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "endpoint": {
                    "type": "server"
                },
                "event": {
                    "id": 4740
                },
                "id": "70599d12-fec7-4129-8844-7c6cfded4642",
                "ioc": {
                    "attack_type": "Suspicious Activity",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "licences": [
                            "License1",
                            "License2"
                        ],
                        "sigma": {
                            "id": "EVENT-0000"
                        },
                        "weight": "5"
                    }
                },
                "logon_process": "logon_process",
                "lolbins_ml_results": {
                    "score": "19",
                    "score_label": "score_label",
                    "sha256": "dd6748642b108262f933260c3ae8"
                },
                "message": {
                    "id": "0cd6e1e0428211eebe560242ac1200020cd6e1e0428211eebe560242ac120002"
                },
                "ml": {
                    "score": "19",
                    "score_band": "ml_score"
                },
                "package": "TEST",
                "password": {
                    "last_set": "2021-08-18T03:37:25.000000Z"
                },
                "process": {
                    "executable": {
                        "is_signed": true
                    }
                },
                "query": {
                    "name": "windows_query_event"
                },
                "record_identifier": "0242ac1200020cd6e1e0428211eebe560242ac120002",
                "threat_type": "threat_type",
                "user_upn": "user.mail@company.fr"
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 2088,
            "geo": {
                "country_iso_code": "FR"
            },
            "ip": "1.2.3.4",
            "mac": "00:11:22:33:44:55",
            "nat": {
                "ip": "1.2.3.4"
            }
        },
        "threat": {
            "indicator": {
                "provider": "threat_source"
            }
        },
        "user": {
            "target": {
                "name": "Administrateur"
            }
        },
        "vulnerability": {
            "description": "Windows Event User Account Locked Out."
        }
    }
    	
	```


=== "ioc_view_query5.json"

    ```json
	
    {
        "message": "{\n  \"parent\": 25740,\n  \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\n  \"upload_size\": 2376,\n  \"record_identifier\": \"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044\",\n  \"ioc_severity\": 5,\n  \"path\": \"C:\\\\Windows\\\\System32\\\\wbem\\\\WMIC.exe\",\n  \"is_process_file_signed\": \"1\",\n  \"ml_score_data\": \"{\\\"configVersion\\\":\\\"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044\\\",\\\"expireTime\\\":0,\\\"peMalwareScore\\\":7,\\\"pePuaScore\\\":15,\\\"vdlFlags\\\":0,\\\"version\\\":2}\",\n  \"ioc_detection_sigma\": \"{\\\"id\\\":\\\"WIN-EXE-ENR-ML-SUSPICIOUS-1.star\\\",\\\"logsource\\\":{\\\"dedup_fields\\\":[\\\"machine_data.columns.sophosPID\\\",\\\"detection.id\\\"]}}\",\n  \"company_name\": \"Microsoft Corporation\",\n  \"pua_score\": 15,\n  \"folded\": 0,\n  \"meta_mac_address\": \"00:05:9a:3c:7a:00\",\n  \"endpoint_id\": \"7df406c7-efc9-4c7d-806f-1c7216031630\",\n  \"meta_public_ip_country_code\": \"FR\",\n  \"schema_version\": \"22\",\n  \"uid\": 292948,\n  \"ioc_detection_mitre_attack\": \"[{\\\"tactic\\\":{\\\"id\\\":\\\"TA0002\\\",\\\"name\\\":\\\"Execution\\\",\\\"techniques\\\":[{\\\"id\\\":\\\"T1059\\\",\\\"name\\\":\\\"Command and Scripting Interpreter\\\"}]}}]\",\n  \"meta_licence\": \"\",\n  \"ioc_detection_experiment_level\": 0,\n  \"ioc_created_at\": \"2023-08-30T15:04:40.934Z\",\n  \"cmdline\": \"wmic /Namespace:\\\\\\\\root\\\\SecurityCenter2 Path AntivirusProduct Get displayName,productState\",\n  \"ingestion_timestamp\": \"2023-08-30T15:04:17.022Z\",\n  \"ioc_detection_attack\": \"Execution\",\n  \"numerics\": false,\n  \"meta_public_ip\": \"194.0.166.130\",\n  \"counter\": 1414,\n  \"detection_id_dedup\": \"b758901433312f4077ce4ed46b776ecc895712ff\",\n  \"meta_hostname\": \"H3333333333333\",\n  \"username\": \"U11111111\",\n  \"ioc_worker_name\": \"Security Event Service\",\n  \"ioc_detection_type\": \"process\",\n  \"sha1\": \"adc83b19e793491b1c6ea0fd8b46cd9f32e592fc\",\n  \"ioc_detection_category\": \"Threat\",\n  \"ioc_unix_time\": \"2023-08-30T15:03:56.000Z\",\n  \"epoch\": 1693206450,\n  \"meta_ip_mask\": \"255.255.252.0\",\n  \"file_size\": 576000,\n  \"ioc_worker_id\": \"security-event-service\",\n  \"global_rep_data\": \"{\\\"expireTime\\\":0,\\\"lookupType\\\":0,\\\"reputation\\\":-1,\\\"reputationData\\\":\\\"\\\",\\\"sampleRate\\\":0,\\\"version\\\":1}\",\n  \"parent_name\": \"idea64.exe\",\n  \"unix_time\": \"2023-08-30T15:03:56.000Z\",\n  \"pid\": 3984,\n  \"ioc_log_type\": \"summary\",\n  \"original_filename\": \"wmic.exe\",\n  \"ml_score_band\": \"LIKELY_BENIGN\",\n  \"query_source\": \"xdr_only\",\n  \"sophos_pid\": \"3984:133378811508910039\",\n  \"host_identifier\": \"689FF239-6905-4EB3-8CA4-716E63BDB63D\",\n  \"partition_bucket\": \"87\",\n  \"meta_public_ip_country\": \"United-Kingdom\",\n  \"meta_boot_time\": 1693382499,\n  \"local_rep\": 91,\n  \"meta_os_name\": \"Microsoft Windows 10 Professionnel\",\n  \"sha256_reputation_score\": 70,\n  \"osquery_action\": \"added\",\n  \"lolbins_ml_results\": {\n    \"score\": 99.0,\n    \"score_label\": \"Suspicious\",\n    \"sha256\": \"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\"\n  },\n  \"parent_path\": \"C:\\\\Program Files\\\\JetBrains\\\\IntelliJ IDEA 2021.3.3\\\\bin\\\\idea64.exe\",\n  \"meta_query_pack_version\": \"1.17.56\",\n  \"calendar_time\": \"2023-08-30T15:03:56.000Z\",\n  \"meta_eid\": \"aecc2aae-83d8-4f39-b65a-53413caa415f\",\n  \"meta_public_ip_longitude\": -0.076198,\n  \"ioc_detection_id\": \"WIN-EXE-ENR-ML-SUSPICIOUS-1\",\n  \"meta_os_platform\": \"windows\",\n  \"meta_username\": \"U111111111\",\n  \"detection_identifier\": \"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044_b758901433312f4077ce4ed46b776ecc895712ff\",\n  \"query_name\": \"running_processes_windows_sophos\",\n  \"meta_os_type\": \"\",\n  \"meta_os_version\": \"10.0.19045\",\n  \"parent_cmdline\": \"\\\"C:\\\\Program Files\\\\JetBrains\\\\IntelliJ IDEA 2021.3.3\\\\bin\\\\idea64.exe\\\" \",\n  \"meta_public_ip_latitude\": 51.5082,\n  \"local_rep_data\": \"{\\\"reputationData\\\":{\\\"isSigned\\\":1,\\\"signerInfo\\\":[{\\\"cryptoAlgorithm\\\":32780,\\\"cryptoStrength\\\":112,\\\"isValid\\\":1,\\\"signer\\\":\\\"Microsoft Windows\\\",\\\"thumbprint\\\":\\\"2724aeb0c497bf5fd732958120d1ae3341cfd252ab1680de03d10503abc666c1\\\"}]}}\",\n  \"ioc_detection_licenses\": \"[\\\"MTR\\\"]\",\n  \"parent_sophos_pid\": \"22222:666666666666666666\",\n  \"name\": \"WMIC.exe\",\n  \"global_rep\": -1,\n  \"meta_aggressive_activity\": \"False\",\n  \"meta_ip_address\": \"1.2.3.4\",\n  \"time\": 1693407550,\n  \"file_version\": \"10.0.19041.1741 (WinBuild.160101.0800)\",\n  \"ingest_date\": \"2023-08-30\",\n  \"file_description\": \"WMI Commandline Utility\",\n  \"ml_score\": 7,\n  \"sha256_reputation_band\": \"KNOWN_GOOD\",\n  \"meta_endpoint_type\": \"computer\",\n  \"meta_domain_controller\": \"False\",\n  \"customer_id\": \"9cc350ec-283c-451a-b072-4c7df065d350\",\n  \"ioc_detection_description\": \"Identifies Lolbin processes labeled as suspicious by a machine learning model.\",\n  \"message_identifier\": \"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044\",\n  \"ioc_attack_type\": \"Security Event Service Detections\",\n  \"product_name\": \"Microsoft\u00ae Windows\u00ae Operating System\",\n  \"gid\": 292948,\n  \"ioc_detection_weight\": 5\n}\n",
        "event": {
            "code": "WIN-EXE-ENR-ML-SUSPICIOUS-1",
            "ingested": "2023-08-30T15:04:17.022000Z",
            "severity": 5
        },
        "@timestamp": "2023-08-30T15:03:56Z",
        "file": {
            "hash": {
                "sha1": "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc",
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            },
            "name": "WMIC.exe",
            "path": "C:\\Windows\\System32\\wbem\\WMIC.exe",
            "size": 576000
        },
        "host": {
            "id": "689FF239-6905-4EB3-8CA4-716E63BDB63D",
            "name": "H3333333333333",
            "os": {
                "full": "Microsoft Windows 10 Professionnel",
                "name": "windows",
                "version": "10.0.19045"
            }
        },
        "process": {
            "code_signature": {
                "exists": true
            },
            "command_line": "wmic /Namespace:\\\\root\\SecurityCenter2 Path AntivirusProduct Get displayName,productState",
            "hash": {
                "sha1": "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc",
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            },
            "name": "Security Event Service",
            "parent": {
                "command_line": "\"C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.3\\bin\\idea64.exe\" ",
                "executable": "C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.3\\bin\\idea64.exe",
                "name": "idea64.exe"
            },
            "pid": 3984
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
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "detection_id_dedup": "b758901433312f4077ce4ed46b776ecc895712ff",
                "endpoint": {
                    "type": "computer"
                },
                "file": {
                    "description": "WMI Commandline Utility",
                    "original": {
                        "name": "wmic.exe"
                    },
                    "version": "10.0.19041.1741 (WinBuild.160101.0800)"
                },
                "global_rep": -1,
                "id": "7df406c7-efc9-4c7d-806f-1c7216031630",
                "ioc": {
                    "attack_type": "Security Event Service Detections",
                    "detection": {
                        "attack": "Execution",
                        "category": "Threat",
                        "licences": [
                            "MTR"
                        ],
                        "sigma": {
                            "id": "WIN-EXE-ENR-ML-SUSPICIOUS-1.star"
                        },
                        "type": "process",
                        "weight": "5"
                    },
                    "log_type": "summary",
                    "unix_time": "2023-08-30T15:03:56.000000Z"
                },
                "lolbins_ml_results": {
                    "score": "99.0",
                    "score_label": "Suspicious",
                    "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
                },
                "message": {
                    "id": "f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044"
                },
                "ml": {
                    "score": "7",
                    "score_band": "LIKELY_BENIGN"
                },
                "ml_score_data": {
                    "config_version": "f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044"
                },
                "process": {
                    "executable": {
                        "is_signed": true
                    }
                },
                "pua": {
                    "score": "15"
                },
                "query": {
                    "action": "added",
                    "name": "running_processes_windows_sophos",
                    "pack_version": "1.17.56",
                    "source": "xdr_only"
                },
                "record_identifier": "f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044",
                "sha256": {
                    "reputation_band": "KNOWN_GOOD",
                    "reputation_score": "70"
                },
                "worker": {
                    "id": "security-event-service"
                }
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 2376,
            "geo": {
                "country_iso_code": "FR",
                "country_name": "United-Kingdom"
            },
            "ip": "1.2.3.4",
            "mac": "00:05:9a:3c:7a:00",
            "nat": {
                "ip": "194.0.166.130"
            }
        },
        "user": {
            "name": "U111111111"
        },
        "vulnerability": {
            "description": "Identifies Lolbin processes labeled as suspicious by a machine learning model."
        }
    }
    	
	```


=== "ioc_view_query6.json"

    ```json
	
    {
        "message": "{\"upload_size\":4486,\"record_identifier\":\"9be070bb55a846a99c85f38e82afb01b9be070bb55a846a99c85f3\",\"ioc_severity\":5,\"process_cmd_line\":\"\\\"C:\\\\process_cmd_line.EXE\\\" \",\"ioc_event_path\":\"C:\\\\ioc_event_path.EXE\",\"process_ml_score_band\":\"LIKELY_BENIGN\",\"process_parent_name\":\"process_parent_name.exe\",\"folded\":0,\"meta_mac_address\":\"00:11:22:33:44:55\",\"endpoint_id\":\"3494ce1f-08fd-4a03-8948-0cb0945ac521\",\"meta_public_ip_country_code\":\"MAR\",\"schema_version\":\"22\",\"ioc_detection_mitre_attack\":\"[{\\\"tactic\\\":{\\\"description\\\":\\\"description tactic \\\",\\\"external_references\\\":[{\\\"external_id\\\":\\\"EE0003\\\",\\\"source_name\\\":\\\"mitre-attack\\\",\\\"url\\\":\\\"https://test.org/tactics/EE0003\\\"}],\\\"id\\\":\\\"EE0003\\\",\\\"name\\\":\\\"Persistence\\\",\\\"techniques\\\":[{\\\"description\\\":\\\"techniques description\\\",\\\"external_references\\\":[{\\\"external_id\\\":\\\"E1997.009\\\",\\\"source_name\\\":\\\"mitre-attack\\\",\\\"url\\\":\\\"https://test.org/techniques/E1997/009\\\"},{\\\"external_id\\\":\\\"EEEEE-132\\\",\\\"source_name\\\":\\\"EEEEE\\\",\\\"url\\\":\\\"https://test.org/132.html\\\"},{\\\"description\\\":\\\"EEE description\\\",\\\"source_name\\\":\\\"source name 2020 - LNK Elastic\\\",\\\"url\\\":\\\"https://www.youtube.com/watch?v=EEEEEEEE\\\"}],\\\"id\\\":\\\"T1547.009\\\",\\\"name\\\":\\\"Shortcut Modification\\\",\\\"platforms\\\":[\\\"Windows\\\"]}]}}]\",\"ioc_detection_experiment_level\":0,\"ioc_created_at\":\"2023-09-20T09:31:41.937Z\",\"process_name\":\"process_name.EXE\",\"ingestion_timestamp\":\"2023-09-20T09:31:41.090Z\",\"ioc_detection_attack\":\"Suspicious Activity\",\"numerics\":false,\"ioc_event_sid\":\"\",\"process_global_rep\":-1,\"meta_public_ip\":\"1.2.3.4\",\"counter\":33,\"detection_id_dedup\":\"e880fc47a0dc0086a8c2f05b92971d2bce2bdaf3\",\"process_sha256_reputation_band\":\"KNOWN_GOOD\",\"meta_hostname\":\"H3333333333333\",\"ioc_event_sophos_tid\":\"\",\"ioc_event_threat_source\":\"Behavioral\",\"ioc_detection_references\":\"[]\",\"process_file_size\":2119600,\"ioc_worker_name\":\"Direct Mapping Worker\",\"ioc_detection_type\":\"Threat\",\"ioc_event_username\":\"\",\"process_path\":\"C:\\\\process_path.EXE\",\"ioc_detection_category\":\"Threat\",\"ioc_unix_time\":\"2023-09-20T09:28:15.000Z\",\"epoch\":1695009925,\"meta_ip_mask\":\"255.255.255.0\",\"ioc_worker_id\":\"direct_mapping_worker\",\"unix_time\":\"2023-09-20T09:28:15.000Z\",\"ioc_log_type\":\"summary\",\"query_source\":\"xdr_only\",\"sophos_pid\":\"12120:111111111111111111\",\"host_identifier\":\"6f80b628-5b7c-11ee-8c99-0242ac120002\",\"partition_bucket\":\"87\",\"meta_public_ip_country\":\"France\",\"process_local_rep_signers\":\"{\\\"reputationData\\\":{\\\"isSigned\\\":1,\\\"signerInfo\\\":[{\\\"isValid\\\":1,\\\"signer\\\":\\\"Microsoft Corporation\\\"},{\\\"isValid\\\":1,\\\"signer\\\":\\\"Microsoft Corporation\\\"}]}}\",\"meta_boot_time\":1695182611,\"process_pua_score\":17,\"process_sha256_reputation_score\":70,\"meta_os_name\":\"Microsoft Windows 10 Professionnel\",\"process_ml_score\":8,\"osquery_action\":\"added\",\"meta_query_pack_version\":\"1.18.1\",\"calendar_time\":\"2023-09-20T09:28:15.000Z\",\"meta_eid\":\"9cc350ec-283c-451a-b072-4c7df065d350\",\"meta_public_ip_longitude\":-0.076198,\"ioc_detection_id\":\"WIN-DET-T1547.009\",\"meta_os_platform\":\"windows\",\"meta_username\":\"JDOE\",\"process_parent_sophos_pid\":\"14208:111111111111111111\",\"detection_identifier\":\"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044_b758901433312f4077ce4ed46b776ecc895712ff\",\"query_name\":\"sophos_runtime_iocs_windows\",\"process_cmd_line_truncated\":0,\"meta_os_version\":\"10.0.19045\",\"meta_public_ip_latitude\":51.5082,\"process_sha256\":\"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\",\"event_count\":1,\"ioc_event_time\":\"2023-09-20T09:28:15.000Z\",\"meta_aggressive_activity\":\"False\",\"ioc_event_events\":\"[{\\\"cmdline\\\":\\\"\\\\\\\"C:\\\\\\\\Program Files (x86)\\\\\\\\Microsoft Office\\\\\\\\root\\\\\\\\Office16\\\\\\\\ONENOTE.EXE\\\\\\\" \\\",\\\"irep\\\":5,\\\"newSpid\\\":{\\\"!spid\\\":\\\"[12120:111111111111111111]\\\"},\\\"pwin32Path\\\":\\\"c:\\\\\\\\Windows\\\\\\\\explorer.exe\\\",\\\"rep\\\":5,\\\"sha256\\\":{\\\"!sha256\\\":\\\"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b\\\"},\\\"spid\\\":{\\\"!spid\\\":\\\"[14208:111111111111111111]\\\"},\\\"type\\\":\\\"ProcessCreate\\\",\\\"win32Path\\\":\\\"C:\\\\\\\\Program Files (x86)\\\\\\\\Microsoft Office\\\\\\\\root\\\\\\\\Office16\\\\\\\\ONENOTE.EXE\\\"},{\\\"fileAttributes\\\":32,\\\"irep\\\":5,\\\"process\\\":\\\"C:\\\\\\\\Program Files (x86)\\\\\\\\Microsoft Office\\\\\\\\root\\\\\\\\Office16\\\\\\\\ONENOTE.EXE\\\",\\\"rep\\\":5,\\\"size\\\":{\\\"!uint64\\\":\\\"0\\\"},\\\"spid\\\":{\\\"!spid\\\":\\\"[12120:111111111111111111]\\\"},\\\"stid\\\":{\\\"!stid\\\":\\\"[5816:111111111111111111]\\\"},\\\"type\\\":\\\"FileOpen\\\",\\\"win32Path\\\":\\\"C:\\\\\\\\Users\\\\\\\\JDOE\\\\\\\\AppData\\\\\\\\Roaming\\\\\\\\Microsoft\\\\\\\\Windows\\\\\\\\Start Menu\\\\\\\\Programs\\\\\\\\Startup\\\\\\\\Envoyer \\\\u00e0 OneNote.lnk\\\"}]\",\"meta_ip_address\":\"1.2.3.4\",\"process_local_rep\":91,\"ingest_date\":\"2023-09-20\",\"meta_endpoint_type\":\"computer\",\"meta_domain_controller\":\"False\",\"ioc_event_ttp_summary\":\"TA0003-T1547.009\",\"customer_id\":\"9cc350ec-283c-451a-b072-4c7df065d350\",\"message_identifier\":\"f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044\",\"ioc_attack_type\":\"Suspicious Activity\",\"process_pid\":12120,\"ioc_events_size\":1247,\"process_parent_path\":\"C:\\\\Windows\\\\process_parent_path.exe\",\"ioc_detection_weight\":5}",
        "event": {
            "code": "WIN-DET-T1547.009",
            "ingested": "2023-09-20T09:31:41.090000Z",
            "severity": 5
        },
        "@timestamp": "2023-09-20T09:28:15Z",
        "file": {
            "directory": "C:",
            "name": "ioc_event_path.EXE",
            "path": "C:\\ioc_event_path.EXE",
            "size": 2119600
        },
        "host": {
            "id": "6f80b628-5b7c-11ee-8c99-0242ac120002",
            "name": "H3333333333333",
            "os": {
                "full": "Microsoft Windows 10 Professionnel",
                "name": "windows",
                "version": "10.0.19045"
            }
        },
        "process": {
            "command_line": "\"C:\\process_cmd_line.EXE\" ",
            "hash": {
                "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            },
            "name": "Direct Mapping Worker",
            "parent": {
                "name": "process_parent_name.exe",
                "working_directory": "C:\\Windows\\process_parent_path.exe"
            }
        },
        "related": {
            "hash": [
                "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            ],
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "JDOE"
            ]
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "detection_id_dedup": "e880fc47a0dc0086a8c2f05b92971d2bce2bdaf3",
                "endpoint": {
                    "type": "computer"
                },
                "id": "3494ce1f-08fd-4a03-8948-0cb0945ac521",
                "ioc": {
                    "attack_type": "Suspicious Activity",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "category": "Threat",
                        "type": "Threat",
                        "weight": "5"
                    },
                    "log_type": "summary",
                    "ttp_summary": "TA0003-T1547.009",
                    "unix_time": "2023-09-20T09:28:15.000000Z"
                },
                "message": {
                    "id": "f94976c04e9a3863965cf49ea581e5a0cb2cad90fa949a44a443b7b2b3c9a044"
                },
                "ml": {
                    "score_band": "LIKELY_BENIGN"
                },
                "process": {
                    "hash": {
                        "sha256": {
                            "reputation_band": "KNOWN_GOOD",
                            "reputation_score": "70"
                        }
                    },
                    "ml_score": "8",
                    "pua": {
                        "score": "17"
                    }
                },
                "query": {
                    "action": "added",
                    "name": "sophos_runtime_iocs_windows",
                    "pack_version": "1.18.1",
                    "source": "xdr_only"
                },
                "record_identifier": "9be070bb55a846a99c85f38e82afb01b9be070bb55a846a99c85f3",
                "worker": {
                    "id": "direct_mapping_worker"
                }
            }
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 4486,
            "geo": {
                "country_iso_code": "MAR",
                "country_name": "France"
            },
            "ip": "1.2.3.4",
            "mac": "00:11:22:33:44:55",
            "nat": {
                "ip": "1.2.3.4"
            }
        },
        "user": {
            "name": "JDOE"
        }
    }
    	
	```


=== "ioc_view_query7.json"

    ```json
	
    {
        "message": "{\n  \"upload_size\": 1406,\n  \"profile_path\": \"%%XXXX\",\n  \"record_identifier\": \"xxxxxxxxx01xxxxxxxxxxxxxxxxxxxxx\",\n  \"ioc_severity\": 4,\n  \"handler_verdicts_case_descriptions\": {\n    \"default\": \"{\\\"correlated_reason_id\\\":\\\"\\\",\\\"created_reason_id\\\":\\\"\\\"}\"\n  },\n  \"user_parameters\": \"%%XXXX\",\n  \"folded\": 0,\n  \"meta_mac_address\": \"c5:1a:64:c1:65:3a\",\n  \"endpoint_id\": \"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\",\n  \"handler_verdict_suppression_mdr\": false,\n  \"meta_public_ip_country_code\": \"FR\",\n  \"schema_version\": \"24\",\n  \"subject_logon_id\": \"0x3e7\",\n  \"ioc_detection_mitre_attack\": \"[]\",\n  \"handler_verdicts_entities\": \"[{\\\"attributes\\\":{\\\"domain_controller\\\":\\\"False\\\",\\\"endpoint_type\\\":\\\"computer\\\",\\\"hostname\\\":\\\"XXXX-XXXXXXXX\\\",\\\"id\\\":\\\"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\\\",\\\"os_platform\\\":\\\"windows\\\",\\\"os_type\\\":\\\"\\\"},\\\"id\\\":\\\"b5c47470231d356f5cf8d90a31999db59172206adef7958ec9c650b9ce99147b\\\",\\\"integration_id\\\":\\\"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\\\",\\\"source_system\\\":\\\"osquery\\\",\\\"type\\\":\\\"device\\\"},{\\\"attributes\\\":{\\\"address\\\":\\\"1.2.3.4\\\",\\\"external\\\":true,\\\"id\\\":\\\"263522d8b9d989b8c304a6d2f088f107b6ee0010675a11fb459b326eb27edefd\\\",\\\"type\\\":\\\"ipv4\\\"},\\\"id\\\":\\\"46ce85dc0d61d3ddc073e7a66074a8add18e75b082eef550e08863895dcbadb0\\\",\\\"integration_id\\\":\\\"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\\\",\\\"source_system\\\":\\\"osquery\\\",\\\"type\\\":\\\"ip_address\\\"},{\\\"attributes\\\":{\\\"address\\\":\\\"1.2.3.1\\\",\\\"external\\\":false,\\\"id\\\":\\\"ead232f295b08325f6b65bd85a8454239cd479ef30e470f594f2fcb628ec3d64\\\",\\\"type\\\":\\\"ipv4\\\"},\\\"id\\\":\\\"a2bf7ac1f3a3e09342ef4510b4d63f53100334262aa0fe8eef47a0e3642a34fe\\\",\\\"integration_id\\\":\\\"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\\\",\\\"source_system\\\":\\\"osquery\\\",\\\"type\\\":\\\"ip_address\\\"}]\",\n  \"user_workstations\": \"%%XXXX\",\n  \"meta_licence\": \"MTR\",\n  \"ioc_detection_experiment_level\": 0,\n  \"privilege_list\": \"-\",\n  \"ioc_created_at\": \"2024-10-22T14:41:22.595Z\",\n  \"ingestion_timestamp\": \"2024-10-22T14:41:09.572Z\",\n  \"home_directory\": \"%%XXXX\",\n  \"ioc_detection_attack\": \"Suspicious Activity\",\n  \"numerics\": false,\n  \"eventid\": 4738,\n  \"meta_public_ip\": \"1.2.3.4\",\n  \"counter\": 0,\n  \"detection_id_dedup\": \"detectionIdDedup-xxxxxxxxxxxxxxx\",\n  \"password_last_set\": \"%%1794\",\n  \"meta_hostname\": \"XXXX-XXXXXXXX\",\n  \"ioc_detection_references\": \"[\\\"https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738\\\"]\",\n  \"ioc_worker_name\": \"Security Event Service\",\n  \"ioc_detection_type\": \"Threat\",\n  \"ioc_detection_category\": \"Threat\",\n  \"ioc_unix_time\": \"2024-10-22T14:40:48.000Z\",\n  \"epoch\": 1729607690,\n  \"meta_ip_mask\": \"255.255.252.0\",\n  \"ioc_worker_id\": \"security-event-service\",\n  \"handler_verdict_suppression_xdr\": false,\n  \"unix_time\": \"2024-10-22T14:40:48.000Z\",\n  \"ioc_log_type\": \"summary\",\n  \"query_source\": \"xdr_only\",\n  \"host_identifier\": \"hostIdentifier-xxxxxxxxxxxxxxx\",\n  \"partition_bucket\": \"87\",\n  \"home_path\": \"%%XXXX\",\n  \"meta_public_ip_country\": \"France\",\n  \"meta_boot_time\": 1729607865,\n  \"subject_username\": \"XXXX-XXXXXXXX$\",\n  \"handler_verdicts_detection_descriptions\": {\n    \"default\": \"{\\\"created_reason_id\\\":\\\"WIN-EVENT-4738\\\",\\\"significance_id\\\":\\\"WIN-EVENT-4738\\\"}\"\n  },\n  \"meta_os_name\": \"Microsoft Windows 11 Professionnel\",\n  \"osquery_action\": \"added\",\n  \"script_path\": \"%%XXXX\",\n  \"account_expires\": \"%%1794\",\n  \"meta_query_pack_version\": \"1.21.26\",\n  \"subject_domain\": \"ACOSS\",\n  \"handler_verdict_suppression\": false,\n  \"calendar_time\": \"2024-10-22T14:40:48.000Z\",\n  \"meta_eid\": \"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\",\n  \"meta_public_ip_longitude\": 2.3387,\n  \"ioc_detection_id\": \"WIN-EVENT-4738\",\n  \"meta_os_platform\": \"windows\",\n  \"meta_username\": \"\",\n  \"detection_identifier\": \"xxxxxxxxx01xxxxxxxxxxxxxxxxxxxxx_detectionIdDedup-xxxxxxxxxxxxxxx\",\n  \"handler_verdict_escalation\": false,\n  \"query_name\": \"windows_event_user_account_changed\",\n  \"provider_name\": \"Microsoft-Windows-Security-Auditing\",\n  \"meta_os_type\": \"\",\n  \"meta_os_version\": \"10.0.22631\",\n  \"sam_account_name\": \"TestUser\",\n  \"meta_public_ip_latitude\": 48.8582,\n  \"source\": \"Security\",\n  \"ioc_detection_licenses\": \"[\\\"MTR\\\",\\\"XDR\\\"]\",\n  \"user_principal_name\": \"-\",\n  \"description\": \"A User Account was changed\",\n  \"meta_aggressive_activity\": \"False\",\n  \"meta_ip_address\": \"1.2.3.1\",\n  \"handler_verdicts\": \"{\\\"default\\\":{\\\"correlation\\\":{\\\"correlate\\\":false,\\\"correlationIds\\\":null,\\\"id\\\":\\\"hostIdentifier-xxxxxxxxxxxxxxx111-xxxx-xxxxx-xxxxxx111111\\\"},\\\"escalation\\\":false,\\\"labels\\\":[],\\\"matched_rules\\\":[{\\\"description\\\":\\\"Define the mutation data structure for subsequent mutation rules to reference\\\",\\\"kb\\\":\\\"mutation\\\",\\\"name\\\":\\\"define_mutation_structure\\\"},{\\\"description\\\":\\\"rule to normalize osquery detections\\\",\\\"kb\\\":\\\"mutation\\\",\\\"name\\\":\\\"normalize_osquery_detections\\\"},{\\\"description\\\":\\\"Update the description in handler verdicts to add detection id\\\",\\\"kb\\\":\\\"mutation\\\",\\\"name\\\":\\\"add_detection_id\\\"},{\\\"description\\\":\\\"Correlate Osquery detections on customer ID and host ID\\\",\\\"kb\\\":\\\"correlation\\\",\\\"name\\\":\\\"osquery_correlation_id\\\"}],\\\"mutations\\\":{\\\"descriptions\\\":{\\\"case_descriptions\\\":{\\\"correlated_reason_id\\\":\\\"\\\",\\\"created_reason_id\\\":\\\"\\\"},\\\"detection_descriptions\\\":{\\\"created_reason_id\\\":\\\"WIN-EVENT-4738\\\",\\\"significance_id\\\":\\\"WIN-EVENT-4738\\\"}},\\\"entities\\\":[{\\\"attributes\\\":{\\\"domain_controller\\\":\\\"False\\\",\\\"endpoint_type\\\":\\\"computer\\\",\\\"hostname\\\":\\\"XXXX-XXXXXXXX\\\",\\\"id\\\":\\\"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\\\",\\\"os_platform\\\":\\\"windows\\\",\\\"os_type\\\":\\\"\\\"},\\\"id\\\":\\\"b5c47470231d356f5cf8d90a31999db59172206adef7958ec9c650b9ce99147b\\\",\\\"integration_id\\\":\\\"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\\\",\\\"source_system\\\":\\\"osquery\\\",\\\"type\\\":\\\"device\\\"},{\\\"attributes\\\":{\\\"address\\\":\\\"1.2.3.4\\\",\\\"external\\\":true,\\\"id\\\":\\\"263522d8b9d989b8c304a6d2f088f107b6ee0010675a11fb459b326eb27edefd\\\",\\\"type\\\":\\\"ipv4\\\"},\\\"id\\\":\\\"46ce85dc0d61d3ddc073e7a66074a8add18e75b082eef550e08863895dcbadb0\\\",\\\"integration_id\\\":\\\"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\\\",\\\"source_system\\\":\\\"osquery\\\",\\\"type\\\":\\\"ip_address\\\"},{\\\"attributes\\\":{\\\"address\\\":\\\"1.2.3.1\\\",\\\"external\\\":false,\\\"id\\\":\\\"ead232f295b08325f6b65bd85a8454239cd479ef30e470f594f2fcb628ec3d64\\\",\\\"type\\\":\\\"ipv4\\\"},\\\"id\\\":\\\"a2bf7ac1f3a3e09342ef4510b4d63f53100334262aa0fe8eef47a0e3642a34fe\\\",\\\"integration_id\\\":\\\"xxxxxxxx-xxxxxx-xxxxxx-xxxxxx\\\",\\\"source_system\\\":\\\"osquery\\\",\\\"type\\\":\\\"ip_address\\\"}],\\\"labels\\\":[]},\\\"rule_hits\\\":[],\\\"rule_hits_summary\\\":{\\\"correlation\\\":[\\\"osquery_correlation_id\\\"],\\\"escalation\\\":[],\\\"mutation\\\":[\\\"define_mutation_structure\\\",\\\"normalize_osquery_detections\\\",\\\"add_detection_id\\\"],\\\"suppression\\\":[]},\\\"suppression\\\":false},\\\"mdr\\\":{\\\"correlation\\\":{\\\"correlate\\\":false,\\\"correlationIds\\\":null,\\\"id\\\":\\\"\\\"},\\\"escalation\\\":false,\\\"labels\\\":[],\\\"matched_rules\\\":[{\\\"description\\\":\\\"Define the mutation data structure for subsequent mutation rules to reference\\\",\\\"kb\\\":\\\"mutation\\\",\\\"name\\\":\\\"define_mutation_structure\\\"}],\\\"mutations\\\":{\\\"descriptions\\\":{\\\"case_descriptions\\\":{\\\"correlated_reason_id\\\":\\\"\\\",\\\"created_reason_id\\\":\\\"\\\"},\\\"detection_descriptions\\\":{\\\"created_reason_id\\\":\\\"\\\",\\\"significance_id\\\":\\\"\\\"}},\\\"entities\\\":[],\\\"labels\\\":[]},\\\"rule_hits\\\":[],\\\"rule_hits_summary\\\":{\\\"correlation\\\":[],\\\"escalation\\\":[],\\\"mutation\\\":[\\\"define_mutation_structure\\\"],\\\"suppression\\\":[]},\\\"suppression\\\":false},\\\"xdr\\\":{\\\"correlation\\\":{\\\"correlate\\\":false,\\\"id\\\":\\\"\\\",\\\"correlationIds\\\":null},\\\"mutations\\\":{},\\\"matched_rules\\\":[],\\\"labels\\\":[],\\\"rule_hits\\\":[],\\\"rule_hits_summary\\\":{\\\"correlation\\\":[],\\\"escalation\\\":[],\\\"mutation\\\":[],\\\"suppression\\\":[]},\\\"escalation\\\":false,\\\"suppression\\\":false}}\",\n  \"ingest_date\": \"2024-10-22\",\n  \"target_domain\": \"XXXX-XXXXXXXX\",\n  \"uac\": \"-\",\n  \"meta_endpoint_type\": \"computer\",\n  \"meta_domain_controller\": \"False\",\n  \"customer_id\": \"111-xxxx-xxxxx-xxxxxx111111\",\n  \"ioc_detection_description\": \"Windows Event User Account Changed.\",\n  \"message_identifier\": \"fbf30057d0b09be51ec23ca2d8354d1fe1c4329a6d52e6ed3bddca127cad105d\",\n  \"ioc_attack_type\": \"Security Event Service Detections\",\n  \"target_username\": \"TestUser\",\n  \"display_name\": \"%%XXXX\",\n  \"allowed_to_delegate_to\": \"-\",\n  \"ioc_detection_weight\": 4\n}",
        "event": {
            "code": "WIN-EVENT-4738",
            "ingested": "2024-10-22T14:41:09.572000Z",
            "reason": "A User Account was changed",
            "severity": 4
        },
        "@timestamp": "2024-10-22T14:40:48Z",
        "destination": {
            "address": "XXXX-XXXXXXXX",
            "domain": "XXXX-XXXXXXXX"
        },
        "host": {
            "domain": "ACOSS",
            "id": "hostIdentifier-xxxxxxxxxxxxxxx",
            "name": "XXXX-XXXXXXXX",
            "os": {
                "full": "Microsoft Windows 11 Professionnel",
                "name": "windows",
                "version": "10.0.22631"
            }
        },
        "process": {
            "name": "Security Event Service"
        },
        "related": {
            "hosts": [
                "XXXX-XXXXXXXX"
            ],
            "ip": [
                "1.2.3.1",
                "1.2.3.4"
            ]
        },
        "sophos": {
            "threat_center": {
                "aggressive_activity": "False",
                "detection_id_dedup": "detectionIdDedup-xxxxxxxxxxxxxxx",
                "endpoint": {
                    "type": "computer"
                },
                "event": {
                    "id": 4738
                },
                "id": "xxxxxxxx-xxxxxx-xxxxxx-xxxxxx",
                "ioc": {
                    "attack_type": "Security Event Service Detections",
                    "detection": {
                        "attack": "Suspicious Activity",
                        "category": "Threat",
                        "licences": [
                            "MTR",
                            "XDR"
                        ],
                        "type": "Threat",
                        "weight": "4"
                    },
                    "log_type": "summary",
                    "unix_time": "2024-10-22T14:40:48.000000Z"
                },
                "message": {
                    "id": "fbf30057d0b09be51ec23ca2d8354d1fe1c4329a6d52e6ed3bddca127cad105d"
                },
                "query": {
                    "action": "added",
                    "name": "windows_event_user_account_changed",
                    "pack_version": "1.21.26",
                    "source": "xdr_only"
                },
                "record_identifier": "xxxxxxxxx01xxxxxxxxxxxxxxxxxxxxx",
                "worker": {
                    "id": "security-event-service"
                }
            }
        },
        "source": {
            "address": "1.2.3.1",
            "bytes": 1406,
            "geo": {
                "country_iso_code": "FR",
                "country_name": "France"
            },
            "ip": "1.2.3.1",
            "mac": "c5:1a:64:c1:65:3a",
            "nat": {
                "ip": "1.2.3.4"
            }
        },
        "user": {
            "target": {
                "name": "TestUser"
            }
        },
        "vulnerability": {
            "description": "Windows Event User Account Changed.",
            "reference": "https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738"
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.address` | `keyword` | Destination network address. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.ingested` | `date` | Timestamp when an event arrived in the central data store. |
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
|`process.parent.working_directory` | `keyword` | The working directory of the process. |
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
|`sophos.threat_center.ioc.ttp_summary` | `keyword` | Tactics, Techniques, and Procedures summary |
|`sophos.threat_center.ioc.unix_time` | `keyword` | Unix time |
|`sophos.threat_center.logon_process` | `keyword` | Verify the identity of the user or system attempting to access the resources |
|`sophos.threat_center.lolbins_ml_results.score` | `keyword` | Lolbins machine learning score |
|`sophos.threat_center.lolbins_ml_results.score_label` | `keyword` | Lolbins machine learning score label |
|`sophos.threat_center.lolbins_ml_results.sha256` | `keyword` | Lolbins machine learning sha256 |
|`sophos.threat_center.message.id` | `keyword` | Message ID |
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
|`sophos.threat_center.process.hash.sha256.reputation_band` | `keyword` | Hash reputation band |
|`sophos.threat_center.process.hash.sha256.reputation_score` | `keyword` | Hash reputation score |
|`sophos.threat_center.process.ml_score` | `keyword` | An AI detection score |
|`sophos.threat_center.process.pua.score` | `keyword` | Potentially Unwanted Application score |
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



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Sophos/sophos-analysis-threat-center).