
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "createsamluser"


    ```json
	{
        "id": "eabe0685-19ac-4c93-929d-12f92aa6a1bc",
        "action": "CreateSAMLUser",
        "requestId": "4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049",
        "status": "SUCCESS",
        "timestamp": "2025-02-06T13:39:25.30484Z",
        "actionParameters": {
            "after": null,
            "filterBy": {
                "search": "Test_UzbhTWx26DwpBUcU_"
            },
            "first": 500,
            "selection": [
                {
                    "nodes": [
                        "id",
                        "name",
                        "createdAt",
                        {
                            "lastRun": [
                                "url",
                                "status",
                                "runAt"
                            ]
                        }
                    ]
                },
                {
                    "pageInfo": [
                        "hasNextPage",
                        "endCursor"
                    ]
                }
            ]
        },
        "userAgent": "python-requests/2.31.0",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user": null
    }
    ```



=== "login"


    ```json
	{
        "id": "8517ae66-65ea-4ddc-9f77-e00920017d33",
        "action": "Login",
        "requestId": "8517ae66-65ea-4ddc-9f77-e00920017d33",
        "status": "SUCCESS",
        "timestamp": "2022-09-01T11:28:07.404058Z",
        "actionParameters": {
            "clientID": "111111111111111111111",
            "groups": null,
            "name": "Integration",
            "products": [
                "*"
            ],
            "role": "testrole",
            "scopes": [
                "read:issues",
                "read:vulnerabilities",
                "admin:audit"
            ],
            "userEmail": "",
            "userID": "service_account_id",
            "userpoolID": "us-east-2_1111111111"
        },
        "userAgent": "node",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "service_account_id",
            "name": "Integration"
        },
        "user": null
    }
    ```



=== "login_failure"


    ```json
	{
        "id": "8a1b4f5f-bde4-4caf-95ab-472a8e6f5529",
        "action": "Login",
        "requestId": "8a1b4f5f-bde4-4caf-95ab-472a8e6f5529",
        "status": "FAILED",
        "timestamp": "2025-02-06T13:38:51.386069Z",
        "actionParameters": {
            "clientID": "iE7lWweGYqpbRnTl",
            "error": "failed authenticating service account",
            "groups": null,
            "name": "",
            "products": null,
            "role": "",
            "scopes": null,
            "sourceIP": "1.2.3.4",
            "userEmail": "test@test.test",
            "userID": "service_account_id",
            "userPoolType": "sa",
            "userpoolID": "us-east-2_GQ3gwvxsQ"
        },
        "userAgent": null,
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "service_account_id",
            "name": "service_account_id"
        },
        "user": null
    }
    ```



=== "report"


    ```json
	{
        "id": "eabe0685-19ac-4c93-929d-12f92aa6a1bc",
        "action": "Reports",
        "requestId": "4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049",
        "status": "SUCCESS",
        "timestamp": "2025-02-06T13:39:25.30484Z",
        "actionParameters": {
            "after": null,
            "filterBy": {
                "search": "Test_UzbhTWx26DwpBUcU_"
            },
            "first": 500,
            "selection": [
                {
                    "nodes": [
                        "id",
                        "name",
                        "createdAt",
                        {
                            "lastRun": [
                                "url",
                                "status",
                                "runAt"
                            ]
                        }
                    ]
                },
                {
                    "pageInfo": [
                        "hasNextPage",
                        "endCursor"
                    ]
                }
            ]
        },
        "userAgent": "python-requests/2.31.0",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user": null
    }
    ```



=== "rerun_report"


    ```json
	{
        "id": "842d4a00-6e04-4e52-8119-8053f0743409",
        "action": "RerunReport",
        "requestId": "da7ab45f-9c57-4af6-859d-797b60a919dd",
        "status": "SUCCESS",
        "timestamp": "2025-02-06T13:39:25.502963Z",
        "actionParameters": {
            "input": {
                "id": "b8ad5ae3-ffea-444f-8d80-175a49e14894"
            },
            "selection": [
                {
                    "report": [
                        "id"
                    ]
                }
            ]
        },
        "userAgent": "python-requests/2.31.0",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user": null
    }
    ```



=== "revokesessions"


    ```json
	{
        "id": "eabe0685-19ac-4c93-929d-12f92aa6a1bc",
        "action": "RevokeSessions",
        "requestId": "4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049",
        "status": "SUCCESS",
        "timestamp": "2025-02-06T13:39:25.30484Z",
        "actionParameters": {
            "after": null,
            "filterBy": {
                "search": "Test_UzbhTWx26DwpBUcU_"
            },
            "first": 500,
            "selection": [
                {
                    "nodes": [
                        "id",
                        "name",
                        "createdAt",
                        {
                            "lastRun": [
                                "url",
                                "status",
                                "runAt"
                            ]
                        }
                    ]
                },
                {
                    "pageInfo": [
                        "hasNextPage",
                        "endCursor"
                    ]
                }
            ]
        },
        "userAgent": "python-requests/2.31.0",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user": null
    }
    ```



=== "test_service_account"


    ```json
	{
        "id": "11111111-1111-1111-1111-111111111111",
        "action": "Login",
        "requestId": "11111111-1111-1111-1111-111111111111",
        "status": "SUCCESS",
        "timestamp": "2025-04-09T14:09:11.559605Z",
        "actionParameters": {
            "clientID": "aaaaaaaaaaaaaaaaaaaaaaaaaa",
            "error": "",
            "groups": null,
            "name": "user_name",
            "products": [
                ""
            ],
            "role": "",
            "scopes": [
                ""
            ],
            "sourceIP": "1.2.3.4",
            "userEmail": "john.doe@company.fr",
            "userID": "1111111111111111111111111111111111111111111111111111",
            "userPoolType": "sa",
            "userpoolID": "eu-west-1_AAAAAAAAA"
        },
        "userAgent": "wiz-sensor/1.0.6349",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "1111111111111111111111111111111111111111111111111111",
            "name": "user_name"
        },
        "user": null
    }
    ```



=== "tokenrefresh"


    ```json
	{
        "id": "eabe0685-19ac-4c93-929d-12f92aa6a1bc",
        "action": "TokenRefresh",
        "requestId": "4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049",
        "status": "SUCCESS",
        "timestamp": "2025-02-06T13:39:25.30484Z",
        "actionParameters": {
            "after": null,
            "filterBy": {
                "search": "Test_UzbhTWx26DwpBUcU_"
            },
            "first": 500,
            "selection": [
                {
                    "nodes": [
                        "id",
                        "name",
                        "createdAt",
                        {
                            "lastRun": [
                                "url",
                                "status",
                                "runAt"
                            ]
                        }
                    ]
                },
                {
                    "pageInfo": [
                        "hasNextPage",
                        "endCursor"
                    ]
                }
            ]
        },
        "userAgent": "python-requests/2.31.0",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user": null
    }
    ```



=== "update_report"


    ```json
	{
        "id": "842d4a00-6e04-4e52-8119-8053f0743409",
        "action": "RerunReport",
        "requestId": "da7ab45f-9c57-4af6-859d-797b60a919dd",
        "status": "SUCCESS",
        "timestamp": "2025-02-06T13:39:25.502963Z",
        "actionParameters": {
            "input": {
                "id": "b8ad5ae3-ffea-444f-8d80-175a49e14894"
            },
            "selection": [
                {
                    "report": [
                        "id"
                    ]
                }
            ]
        },
        "userAgent": "python-requests/2.31.0",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user": null
    }
    ```



=== "updateuser"


    ```json
	{
        "id": "eabe0685-19ac-4c93-929d-12f92aa6a1bc",
        "action": "UpdateUser",
        "requestId": "4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049",
        "status": "SUCCESS",
        "timestamp": "2025-02-06T13:39:25.30484Z",
        "actionParameters": {
            "after": null,
            "filterBy": {
                "search": "Test_UzbhTWx26DwpBUcU_"
            },
            "first": 500,
            "selection": [
                {
                    "nodes": [
                        "id",
                        "name",
                        "createdAt",
                        {
                            "lastRun": [
                                "url",
                                "status",
                                "runAt"
                            ]
                        }
                    ]
                },
                {
                    "pageInfo": [
                        "hasNextPage",
                        "endCursor"
                    ]
                }
            ]
        },
        "userAgent": "python-requests/2.31.0",
        "sourceIP": "1.2.3.4",
        "serviceAccount": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user": null
    }
    ```



