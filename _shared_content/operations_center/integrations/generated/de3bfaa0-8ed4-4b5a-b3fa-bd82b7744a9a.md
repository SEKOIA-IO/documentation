
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web logs` | None |
| `Application logs` | None |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `alert` |
| Category | `intrusion_detection` |
| Type | `info` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "event1.json"

    ```json
	
    {
        "message": "{\n  \"id\": \"eventId1\",\n  \"sourceRule\": {\n    \"__typename\": \"Control\",\n    \"id\": \"sourceRuleId1\",\n    \"name\": \"Publicly Exposed Assets with DataFindings \",\n    \"controlDescription\": \"\",\n    \"resolutionRecommendation\": \"\",\n    \"securitySubCategories\": [\n      {\n        \"title\": \"Data Security\",\n        \"category\": {\n          \"name\": \"8 Data Security\"\n        }\n      }\n    ]\n  },\n  \"createdAt\": \"2023-08-23T07:56:09.903743Z\",\n  \"updatedAt\": \"2023-09-12T08:33:16.327851Z\",\n  \"dueAt\": null,\n  \"type\": \"TOXIC_COMBINATION\",\n  \"resolvedAt\": null,\n  \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\",\n  \"status\": \"OPEN\",\n  \"severity\": \"HIGH\",\n  \"entitySnapshot\": {\n    \"id\": \"entitySnapshotId1\",\n    \"type\": \"DATA_FINDING\",\n    \"nativeType\": \"\",\n    \"name\": \"GDPR 2415\",\n    \"status\": null,\n    \"cloudPlatform\": null,\n    \"cloudProviderURL\": \"\",\n    \"providerId\": \"data##wizt-rec11111111111111##xxxx-eeeee-tttt-qqqq\",\n    \"region\": \"\"\n  }\n}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "GDPR 2415",
                    "type": "DATA_FINDING"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "event2.json"

    ```json
	
    {
        "message": "{\n  \"id\": \"eventId1\",\n  \"sourceRule\": {\n    \"__typename\": \"Control\",\n    \"id\": \"sourceRuleId1\",\n    \"name\": \"Publicly Exposed Assets with DataFindings \",\n    \"controlDescription\": \"\",\n    \"resolutionRecommendation\": \"\",\n    \"securitySubCategories\": [\n      {\n        \"title\": \"Data Security\",\n        \"category\": {\n          \"name\": \"8 Data Security\"\n        }\n      }\n    ]\n  },\n  \"createdAt\": \"2023-08-23T07:56:09.903743Z\",\n  \"updatedAt\": \"2023-09-12T08:33:16.327851Z\",\n  \"dueAt\": null,\n  \"type\": \"TOXIC_COMBINATION\",\n  \"resolvedAt\": null,\n  \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\",\n  \"status\": \"OPEN\",\n  \"severity\": \"HIGH\",\n  \"entitySnapshot\": {\n    \"id\": \"entitySnapshotId1\",\n    \"type\": \"SECURITY_TOOL_FINDING\",\n    \"nativeType\": \"\",\n    \"name\": \"GDPR 2415\",\n    \"status\": null,\n    \"cloudPlatform\": null,\n    \"cloudProviderURL\": \"\",\n    \"providerId\": \"data##wizt-rec11111111111111##xxxx-eeeee-tttt-qqqq\",\n    \"region\": \"\"\n  }\n}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "vulnerability": {
            "name": "GDPR 2415"
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "GDPR 2415",
                    "type": "SECURITY_TOOL_FINDING"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "event3.json"

    ```json
	
    {
        "message": "{\n  \"id\": \"eventId1\",\n  \"sourceRule\": {\n    \"__typename\": \"Control\",\n    \"id\": \"sourceRuleId1\",\n    \"name\": \"Publicly Exposed Assets with DataFindings \",\n    \"controlDescription\": \"\",\n    \"resolutionRecommendation\": \"\",\n    \"securitySubCategories\": [\n      {\n        \"title\": \"Data Security\",\n        \"category\": {\n          \"name\": \"8 Data Security\"\n        }\n      }\n, {\n        \"title\": \"Data Security 123\",\n        \"category\": {\n          \"name\": \"8 Data Security\"\n        }\n      }\n    ]\n  },\n  \"createdAt\": \"2023-08-23T07:56:09.903743Z\",\n  \"updatedAt\": \"2023-09-12T08:33:16.327851Z\",\n  \"dueAt\": null,\n  \"type\": \"TOXIC_COMBINATION\",\n  \"resolvedAt\": null,\n  \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\",\n  \"status\": \"OPEN\",\n  \"severity\": \"HIGH\",\n  \"entitySnapshot\": {\n    \"id\": \"entitySnapshotId1\",\n    \"type\": \"SECURITY_TOOL_FINDING\",\n    \"nativeType\": \"\",\n    \"name\": \"GDPR 2415\",\n    \"status\": null,\n    \"cloudPlatform\": null,\n    \"cloudProviderURL\": \"\",\n    \"providerId\": \"data##wizt-rec11111111111111##xxxx-eeeee-tttt-qqqq\",\n    \"region\": \"\"\n  }\n}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "vulnerability": {
            "name": "GDPR 2415"
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "GDPR 2415",
                    "type": "SECURITY_TOOL_FINDING"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security",
                        "Data Security 123"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "event4.json"

    ```json
	
    {
        "message": "{\"id\":\"xxxxxxx-xxxxxxx-xxxxxxx\",\"sourceRule\":{\"__typename\":\"Control\",\"id\":\"idxxxxxxxxxxxx\",\"name\":\"Findings with Critical Severity Vulnerabilities\",\"controlDescription\":\"Vendor severity is critical\",\"resolutionRecommendation\":\"\",\"securitySubCategories\":null,\"risks\":null},\"createdAt\":\"2025-02-11T13:56:41.048452Z\",\"updatedAt\":\"2025-02-11T13:56:41.048452Z\",\"dueAt\":null,\"type\":\"TOXIC_COMBINATION\",\"resolvedAt\":null,\"statusChangedAt\":\"2025-02-11T13:56:41.048452Z\",\"status\":\"OPEN\",\"severity\":\"MEDIUM\",\"entitySnapshot\":{\"id\":\"idxxxxxxxxxxxxxxxxxxxxcf\",\"type\":\"SECURITY_TOOL_FINDING\",\"nativeType\":\"\",\"name\":\"TEST-TEST-TEST\",\"status\":null,\"cloudPlatform\":null,\"cloudProviderURL\":\"\",\"providerId\":\"81##CloudPlatform/ContainerImage##docker.io##test/test@sha256:sha256##CVE-2022-48174##busybox-binsh##1.35.0-r29\",\"region\":\"\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2025-02-11T13:56:41.048452Z",
        "log": {
            "level": "MEDIUM"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "idxxxxxxxxxxxx",
            "name": "Findings with Critical Severity Vulnerabilities"
        },
        "vulnerability": {
            "name": "TEST-TEST-TEST"
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "TEST-TEST-TEST",
                    "type": "SECURITY_TOOL_FINDING"
                },
                "id": "xxxxxxx-xxxxxxx-xxxxxxx",
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event1.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"wow-poc\", \"type\": \"SECRET\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "wow-poc",
                    "type": "SECRET"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event10.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"https://example.org:443\", \"type\": \"ENDPOINT\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "url": {
            "domain": "example.org",
            "full": "https://example.org:443",
            "port": 443,
            "registered_domain": "example.org",
            "scheme": "https",
            "top_level_domain": "org"
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "https://example.org:443",
                    "type": "ENDPOINT"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event11.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"5.6.7.8:22\", \"type\": \"ENDPOINT\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "destination": {
            "address": "5.6.7.8",
            "ip": "5.6.7.8",
            "port": 22
        },
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "5.6.7.8"
            ]
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "5.6.7.8:22",
                    "type": "ENDPOINT"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event12.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"\", \"type\": \"DATA_WORKFLOW\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "type": "DATA_WORKFLOW"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event13.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"prometheus-collector\", \"type\": \"CONTAINER\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "container": {
            "name": "prometheus-collector"
        },
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "prometheus-collector",
                    "type": "CONTAINER"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event14.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"EXAMPLE-RSG001-NetworkSecurity-APPGWY\", \"type\": \"RESOURCE_GROUP\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "EXAMPLE-RSG001-NetworkSecurity-APPGWY",
                    "type": "RESOURCE_GROUP"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event15.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"MyDBServer\", \"type\": \"DB_SERVER\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "host": {
            "name": "MyDBServer"
        },
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "MyDBServer",
                    "type": "DB_SERVER"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event16.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"EXAMPLE-AGW001-SharedServices\", \"type\": \"LOAD_BALANCER\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "host": {
            "name": "EXAMPLE-AGW001-SharedServices"
        },
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "EXAMPLE-AGW001-SharedServices",
                    "type": "LOAD_BALANCER"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event17.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"test-allincluded\", \"type\": \"VIRTUAL_WORKSTATION\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "host": {
            "name": "test-allincluded"
        },
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "test-allincluded",
                    "type": "VIRTUAL_WORKSTATION"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event18.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"platform-cluster\", \"type\": \"KUBERNETES_CLUSTER\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "platform-cluster",
                    "type": "KUBERNETES_CLUSTER"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event2.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"WorkerNode-EKS-Cluster-Example-prod-eks\", \"type\": \"VIRTUAL_MACHINE\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "cloud": {
            "instance": {
                "name": "WorkerNode-EKS-Cluster-Example-prod-eks"
            }
        },
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "WorkerNode-EKS-Cluster-Example-prod-eks",
                    "type": "VIRTUAL_MACHINE"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event3.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"Ephemeral_aws:ec2:example-75e1255c-9dea-4af4-b3c9-4362277986ee\", \"type\": \"COMPUTE_INSTANCE_GROUP\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "Ephemeral_aws:ec2:example-75e1255c-9dea-4af4-b3c9-4362277986ee",
                    "type": "COMPUTE_INSTANCE_GROUP"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event4.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"MyServiceAccount\", \"type\": \"SERVICE_ACCOUNT\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "MyServiceAccount",
                    "type": "SERVICE_ACCOUNT"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event5.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"john.doe@exmaple.org\", \"type\": \"USER_ACCOUNT\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "user": {
            "target": {
                "email": "john.doe@exmaple.org"
            }
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "john.doe@exmaple.org",
                    "type": "USER_ACCOUNT"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event6.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"Authorization-Replication-Invok-HelloWorldFunction-CCCCCCCCCCCC\", \"type\": \"SERVERLESS\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "Authorization-Replication-Invok-HelloWorldFunction-CCCCCCCCCCCC",
                    "type": "SERVERLESS"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event7.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"mybucket-111111111111-ap-southeast-1-1tj90\", \"type\": \"BUCKET\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "mybucket-111111111111-ap-southeast-1-1tj90",
                    "type": "BUCKET"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event8.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"111111111111.dkr.ecr.us-west-2.amazonaws.com/mycontainer@sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08\", \"type\": \"CONTAINER_IMAGE\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "container": {
            "image": {
                "name": "111111111111.dkr.ecr.us-west-2.amazonaws.com/mycontainer@sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
            }
        },
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "111111111111.dkr.ecr.us-west-2.amazonaws.com/mycontainer@sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
                    "type": "CONTAINER_IMAGE"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```


=== "gen_event9.json"

    ```json
	
    {
        "message": "{\"id\": \"eventId1\", \"sourceRule\": {\"__typename\": \"Control\", \"id\": \"sourceRuleId1\", \"name\": \"Publicly Exposed Assets with DataFindings \", \"controlDescription\": \"\", \"resolutionRecommendation\": \"\", \"securitySubCategories\": [{\"title\": \"Data Security\", \"category\": {\"name\": \"8 Data Security\"}}]}, \"createdAt\": \"2023-08-23T07:56:09.903743Z\", \"updatedAt\": \"2023-09-12T08:33:16.327851Z\", \"dueAt\": null, \"type\": \"TOXIC_COMBINATION\", \"resolvedAt\": null, \"statusChangedAt\": \"2023-08-30T08:17:54.613564Z\", \"status\": \"OPEN\", \"severity\": \"HIGH\", \"entitySnapshot\": {\"name\": \"deployment-website-com-be-staging\", \"type\": \"DEPLOYMENT\"}}",
        "event": {
            "category": [
                "intrusion_detection"
            ],
            "dataset": "Issues",
            "kind": "alert",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2023-08-23T07:56:09.903743Z",
        "log": {
            "level": "HIGH"
        },
        "observer": {
            "vendor": "Wiz"
        },
        "rule": {
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings "
        },
        "wiz": {
            "issues": {
                "entitySnapshot": {
                    "name": "deployment-website-com-be-staging",
                    "type": "DEPLOYMENT"
                },
                "id": "eventId1",
                "securitySubCategories": {
                    "titles": [
                        "Data Security"
                    ]
                },
                "status": "OPEN",
                "type": "TOXIC_COMBINATION"
            }
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cloud.instance.name` | `keyword` | Instance name of the host machine. |
|`container.image.name` | `keyword` | Name of the image the container was built on. |
|`container.name` | `keyword` | Container name. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`host.name` | `keyword` | Name of the host. |
|`log.level` | `keyword` | Log level of the log event. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`rule.id` | `keyword` | Rule ID |
|`rule.name` | `keyword` | Rule name |
|`url.full` | `wildcard` | Full unparsed URL. |
|`user.target.email` | `keyword` | User email address. |
|`vulnerability.name` | `keyword` |  |
|`wiz.issues.entitySnapshot.name` | `keyword` |  |
|`wiz.issues.entitySnapshot.type` | `keyword` |  |
|`wiz.issues.id` | `keyword` |  |
|`wiz.issues.securitySubCategories.titles` | `array` |  |
|`wiz.issues.status` | `keyword` |  |
|`wiz.issues.type` | `keyword` |  |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Wiz/wiz-issues).