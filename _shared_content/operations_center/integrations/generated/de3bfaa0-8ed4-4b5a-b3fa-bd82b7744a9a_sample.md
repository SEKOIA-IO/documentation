
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "event1"


    ```json
	{
        "id": "eventId1",
        "sourceRule": {
            "__typename": "Control",
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings ",
            "controlDescription": "",
            "resolutionRecommendation": "",
            "securitySubCategories": [
                {
                    "title": "Data Security",
                    "category": {
                        "name": "8 Data Security"
                    }
                }
            ]
        },
        "createdAt": "2023-08-23T07:56:09.903743Z",
        "updatedAt": "2023-09-12T08:33:16.327851Z",
        "dueAt": null,
        "type": "TOXIC_COMBINATION",
        "resolvedAt": null,
        "statusChangedAt": "2023-08-30T08:17:54.613564Z",
        "status": "OPEN",
        "severity": "HIGH",
        "entitySnapshot": {
            "id": "entitySnapshotId1",
            "type": "DATA_FINDING",
            "nativeType": "",
            "name": "GDPR 2415",
            "status": null,
            "cloudPlatform": null,
            "cloudProviderURL": "",
            "providerId": "data##wizt-rec11111111111111##xxxx-eeeee-tttt-qqqq",
            "region": ""
        }
    }
    ```



=== "event2"


    ```json
	{
        "id": "eventId1",
        "sourceRule": {
            "__typename": "Control",
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings ",
            "controlDescription": "",
            "resolutionRecommendation": "",
            "securitySubCategories": [
                {
                    "title": "Data Security",
                    "category": {
                        "name": "8 Data Security"
                    }
                }
            ]
        },
        "createdAt": "2023-08-23T07:56:09.903743Z",
        "updatedAt": "2023-09-12T08:33:16.327851Z",
        "dueAt": null,
        "type": "TOXIC_COMBINATION",
        "resolvedAt": null,
        "statusChangedAt": "2023-08-30T08:17:54.613564Z",
        "status": "OPEN",
        "severity": "HIGH",
        "entitySnapshot": {
            "id": "entitySnapshotId1",
            "type": "SECURITY_TOOL_FINDING",
            "nativeType": "",
            "name": "GDPR 2415",
            "status": null,
            "cloudPlatform": null,
            "cloudProviderURL": "",
            "providerId": "data##wizt-rec11111111111111##xxxx-eeeee-tttt-qqqq",
            "region": ""
        }
    }
    ```



=== "event3"


    ```json
	{
        "id": "eventId1",
        "sourceRule": {
            "__typename": "Control",
            "id": "sourceRuleId1",
            "name": "Publicly Exposed Assets with DataFindings ",
            "controlDescription": "",
            "resolutionRecommendation": "",
            "securitySubCategories": [
                {
                    "title": "Data Security",
                    "category": {
                        "name": "8 Data Security"
                    }
                },
                {
                    "title": "Data Security 123",
                    "category": {
                        "name": "8 Data Security"
                    }
                }
            ]
        },
        "createdAt": "2023-08-23T07:56:09.903743Z",
        "updatedAt": "2023-09-12T08:33:16.327851Z",
        "dueAt": null,
        "type": "TOXIC_COMBINATION",
        "resolvedAt": null,
        "statusChangedAt": "2023-08-30T08:17:54.613564Z",
        "status": "OPEN",
        "severity": "HIGH",
        "entitySnapshot": {
            "id": "entitySnapshotId1",
            "type": "SECURITY_TOOL_FINDING",
            "nativeType": "",
            "name": "GDPR 2415",
            "status": null,
            "cloudPlatform": null,
            "cloudProviderURL": "",
            "providerId": "data##wizt-rec11111111111111##xxxx-eeeee-tttt-qqqq",
            "region": ""
        }
    }
    ```



=== "event4"


    ```json
	{
        "id": "xxxxxxx-xxxxxxx-xxxxxxx",
        "sourceRule": {
            "__typename": "Control",
            "id": "idxxxxxxxxxxxx",
            "name": "Findings with Critical Severity Vulnerabilities",
            "controlDescription": "Vendor severity is critical",
            "resolutionRecommendation": "",
            "securitySubCategories": null,
            "risks": null
        },
        "createdAt": "2025-02-11T13:56:41.048452Z",
        "updatedAt": "2025-02-11T13:56:41.048452Z",
        "dueAt": null,
        "type": "TOXIC_COMBINATION",
        "resolvedAt": null,
        "statusChangedAt": "2025-02-11T13:56:41.048452Z",
        "status": "OPEN",
        "severity": "MEDIUM",
        "entitySnapshot": {
            "id": "idxxxxxxxxxxxxxxxxxxxxcf",
            "type": "SECURITY_TOOL_FINDING",
            "nativeType": "",
            "name": "TEST-TEST-TEST",
            "status": null,
            "cloudPlatform": null,
            "cloudProviderURL": "",
            "providerId": "81##CloudPlatform/ContainerImage##docker.io##test/test@sha256:sha256##CVE-2022-48174##busybox-binsh##1.35.0-r29",
            "region": ""
        }
    }
    ```



