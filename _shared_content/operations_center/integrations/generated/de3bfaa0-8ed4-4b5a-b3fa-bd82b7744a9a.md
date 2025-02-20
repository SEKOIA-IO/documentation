
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
                    "type": "SECURITY_TOOL_FINDING"
                },
                "id": "xxxxxxx-xxxxxxx-xxxxxxx",
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
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`log.level` | `keyword` | Log level of the log event. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`rule.id` | `keyword` | Rule ID |
|`rule.name` | `keyword` | Rule name |
|`vulnerability.name` | `keyword` |  |
|`wiz.issues.entitySnapshot.name` | `keyword` |  |
|`wiz.issues.entitySnapshot.type` | `keyword` |  |
|`wiz.issues.id` | `keyword` |  |
|`wiz.issues.securitySubCategories.titles` | `array` |  |
|`wiz.issues.status` | `keyword` |  |
|`wiz.issues.type` | `keyword` |  |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Wiz/wiz-issues).