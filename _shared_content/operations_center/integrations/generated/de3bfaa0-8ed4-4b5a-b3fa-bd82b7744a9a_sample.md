
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



=== "gen_event1"


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
            "name": "wow-poc",
            "type": "SECRET"
        }
    }
    ```



=== "gen_event10"


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
            "name": "https://example.org:443",
            "type": "ENDPOINT"
        }
    }
    ```



=== "gen_event11"


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
            "name": "5.6.7.8:22",
            "type": "ENDPOINT"
        }
    }
    ```



=== "gen_event12"


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
            "name": "",
            "type": "DATA_WORKFLOW"
        }
    }
    ```



=== "gen_event13"


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
            "name": "prometheus-collector",
            "type": "CONTAINER"
        }
    }
    ```



=== "gen_event14"


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
            "name": "EXAMPLE-RSG001-NetworkSecurity-APPGWY",
            "type": "RESOURCE_GROUP"
        }
    }
    ```



=== "gen_event15"


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
            "name": "MyDBServer",
            "type": "DB_SERVER"
        }
    }
    ```



=== "gen_event16"


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
            "name": "EXAMPLE-AGW001-SharedServices",
            "type": "LOAD_BALANCER"
        }
    }
    ```



=== "gen_event17"


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
            "name": "test-allincluded",
            "type": "VIRTUAL_WORKSTATION"
        }
    }
    ```



=== "gen_event18"


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
            "name": "platform-cluster",
            "type": "KUBERNETES_CLUSTER"
        }
    }
    ```



=== "gen_event2"


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
            "name": "WorkerNode-EKS-Cluster-Example-prod-eks",
            "type": "VIRTUAL_MACHINE"
        }
    }
    ```



=== "gen_event3"


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
            "name": "Ephemeral_aws:ec2:example-75e1255c-9dea-4af4-b3c9-4362277986ee",
            "type": "COMPUTE_INSTANCE_GROUP"
        }
    }
    ```



=== "gen_event4"


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
            "name": "MyServiceAccount",
            "type": "SERVICE_ACCOUNT"
        }
    }
    ```



=== "gen_event5"


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
            "name": "john.doe@exmaple.org",
            "type": "USER_ACCOUNT"
        }
    }
    ```



=== "gen_event6"


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
            "name": "Authorization-Replication-Invok-HelloWorldFunction-CCCCCCCCCCCC",
            "type": "SERVERLESS"
        }
    }
    ```



=== "gen_event7"


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
            "name": "mybucket-111111111111-ap-southeast-1-1tj90",
            "type": "BUCKET"
        }
    }
    ```



=== "gen_event8"


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
            "name": "111111111111.dkr.ecr.us-west-2.amazonaws.com/mycontainer@sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
            "type": "CONTAINER_IMAGE"
        }
    }
    ```



=== "gen_event9"


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
            "name": "deployment-website-com-be-staging",
            "type": "DEPLOYMENT"
        }
    }
    ```



