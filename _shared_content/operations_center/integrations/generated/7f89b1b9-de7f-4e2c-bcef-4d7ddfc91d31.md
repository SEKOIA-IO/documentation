
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web logs` | None |
| `Application logs` | None |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `authentication`, `configuration`, `iam`, `process`, `session` |
| Type | `change`, `creation`, `deletion`, `end`, `info`, `start` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "createsamluser.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"eabe0685-19ac-4c93-929d-12f92aa6a1bc\",\n    \"action\": \"CreateSAMLUser\",\n    \"requestId\": \"4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049\",\n    \"status\": \"SUCCESS\",\n    \"timestamp\": \"2025-02-06T13:39:25.30484Z\",\n    \"actionParameters\": {\n      \"after\": null,\n      \"filterBy\": {\n        \"search\": \"Test_UzbhTWx26DwpBUcU_\"\n      },\n      \"first\": 500,\n      \"selection\": [\n        {\n          \"nodes\": [\n            \"id\",\n            \"name\",\n            \"createdAt\",\n            {\n              \"lastRun\": [\n                \"url\",\n                \"status\",\n                \"runAt\"\n              ]\n            }\n          ]\n        },\n        {\n          \"pageInfo\": [\n            \"hasNextPage\",\n            \"endCursor\"\n          ]\n        }\n      ]\n    },\n    \"userAgent\": \"python-requests/2.31.0\",\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"xNgww7tONKtQK6zw\",\n      \"name\": \"ax-us\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "CreateSAMLUser",
            "category": [
                "iam"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "creation"
            ]
        },
        "@timestamp": "2025-02-06T13:39:25.304840Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ax-us"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Python Requests",
            "original": "python-requests/2.31.0",
            "os": {
                "name": "Other"
            },
            "version": "2.31"
        },
        "wiz": {
            "audit": {
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "login.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"8517ae66-65ea-4ddc-9f77-e00920017d33\",\n    \"action\": \"Login\",\n    \"requestId\": \"8517ae66-65ea-4ddc-9f77-e00920017d33\",\n    \"status\": \"SUCCESS\",\n    \"timestamp\": \"2022-09-01T11:28:07.404058Z\",\n    \"actionParameters\": {\n      \"clientID\": \"111111111111111111111\",\n      \"groups\": null,\n      \"name\": \"Integration\",\n      \"products\": [\n        \"*\"\n      ],\n      \"role\": \"testrole\",\n      \"scopes\": [\n        \"read:issues\",\n        \"read:vulnerabilities\",\n        \"admin:audit\"\n      ],\n      \"userEmail\": \"\",\n      \"userID\": \"service_account_id\",\n      \"userpoolID\": \"us-east-2_1111111111\"\n    },\n    \"userAgent\": \"node\",\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"service_account_id\",\n      \"name\": \"Integration\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "Login",
            "category": [
                "authentication"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "start"
            ]
        },
        "@timestamp": "2022-09-01T11:28:07.404058Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "Integration"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "service_account_id",
            "name": "Integration"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Other",
            "original": "node",
            "os": {
                "name": "Other"
            }
        },
        "wiz": {
            "audit": {
                "products": [
                    "*"
                ],
                "role": "testrole",
                "scopes": [
                    "admin:audit",
                    "read:issues",
                    "read:vulnerabilities"
                ],
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "login_failure.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"8a1b4f5f-bde4-4caf-95ab-472a8e6f5529\",\n    \"action\": \"Login\",\n    \"requestId\": \"8a1b4f5f-bde4-4caf-95ab-472a8e6f5529\",\n    \"status\": \"FAILED\",\n    \"timestamp\": \"2025-02-06T13:38:51.386069Z\",\n    \"actionParameters\": {\n      \"clientID\": \"iE7lWweGYqpbRnTl\",\n      \"error\": \"failed authenticating service account\",\n      \"groups\": null,\n      \"name\": \"\",\n      \"products\": null,\n      \"role\": \"\",\n      \"scopes\": null,\n      \"sourceIP\": \"1.2.3.4\",\n      \"userEmail\": \"test@test.test\",\n      \"userID\": \"service_account_id\",\n      \"userPoolType\": \"sa\",\n      \"userpoolID\": \"us-east-2_GQ3gwvxsQ\"\n    },\n    \"userAgent\": null,\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"service_account_id\",\n      \"name\": \"service_account_id\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "Login",
            "category": [
                "authentication"
            ],
            "dataset": "Audit Logs",
            "message": "failed authenticating service account",
            "outcome": "failure",
            "type": [
                "start"
            ]
        },
        "@timestamp": "2025-02-06T13:38:51.386069Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "service_account_id"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "service_account_id",
            "name": "service_account_id"
        },
        "wiz": {
            "audit": {
                "service_account": {
                    "creator": {
                        "email": "test@test.test"
                    }
                },
                "status": "FAILED",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "report.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"eabe0685-19ac-4c93-929d-12f92aa6a1bc\",\n    \"action\": \"Reports\",\n    \"requestId\": \"4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049\",\n    \"status\": \"SUCCESS\",\n    \"timestamp\": \"2025-02-06T13:39:25.30484Z\",\n    \"actionParameters\": {\n      \"after\": null,\n      \"filterBy\": {\n        \"search\": \"Test_UzbhTWx26DwpBUcU_\"\n      },\n      \"first\": 500,\n      \"selection\": [\n        {\n          \"nodes\": [\n            \"id\",\n            \"name\",\n            \"createdAt\",\n            {\n              \"lastRun\": [\n                \"url\",\n                \"status\",\n                \"runAt\"\n              ]\n            }\n          ]\n        },\n        {\n          \"pageInfo\": [\n            \"hasNextPage\",\n            \"endCursor\"\n          ]\n        }\n      ]\n    },\n    \"userAgent\": \"python-requests/2.31.0\",\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"xNgww7tONKtQK6zw\",\n      \"name\": \"ax-us\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "Reports",
            "category": [
                "configuration"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2025-02-06T13:39:25.304840Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ax-us"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Python Requests",
            "original": "python-requests/2.31.0",
            "os": {
                "name": "Other"
            },
            "version": "2.31"
        },
        "wiz": {
            "audit": {
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "rerun_report.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"842d4a00-6e04-4e52-8119-8053f0743409\",\n    \"action\": \"RerunReport\",\n    \"requestId\": \"da7ab45f-9c57-4af6-859d-797b60a919dd\",\n    \"status\": \"SUCCESS\",\n    \"timestamp\": \"2025-02-06T13:39:25.502963Z\",\n    \"actionParameters\": {\n      \"input\": {\n        \"id\": \"b8ad5ae3-ffea-444f-8d80-175a49e14894\"\n      },\n      \"selection\": [\n        {\n          \"report\": [\n            \"id\"\n          ]\n        }\n      ]\n    },\n    \"userAgent\": \"python-requests/2.31.0\",\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"xNgww7tONKtQK6zw\",\n      \"name\": \"ax-us\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "RerunReport",
            "category": [
                "process"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "start"
            ]
        },
        "@timestamp": "2025-02-06T13:39:25.502963Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ax-us"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Python Requests",
            "original": "python-requests/2.31.0",
            "os": {
                "name": "Other"
            },
            "version": "2.31"
        },
        "wiz": {
            "audit": {
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "revokesessions.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"eabe0685-19ac-4c93-929d-12f92aa6a1bc\",\n    \"action\": \"RevokeSessions\",\n    \"requestId\": \"4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049\",\n    \"status\": \"SUCCESS\",\n    \"timestamp\": \"2025-02-06T13:39:25.30484Z\",\n    \"actionParameters\": {\n      \"after\": null,\n      \"filterBy\": {\n        \"search\": \"Test_UzbhTWx26DwpBUcU_\"\n      },\n      \"first\": 500,\n      \"selection\": [\n        {\n          \"nodes\": [\n            \"id\",\n            \"name\",\n            \"createdAt\",\n            {\n              \"lastRun\": [\n                \"url\",\n                \"status\",\n                \"runAt\"\n              ]\n            }\n          ]\n        },\n        {\n          \"pageInfo\": [\n            \"hasNextPage\",\n            \"endCursor\"\n          ]\n        }\n      ]\n    },\n    \"userAgent\": \"python-requests/2.31.0\",\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"xNgww7tONKtQK6zw\",\n      \"name\": \"ax-us\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "RevokeSessions",
            "category": [
                "session"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "end"
            ]
        },
        "@timestamp": "2025-02-06T13:39:25.304840Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ax-us"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Python Requests",
            "original": "python-requests/2.31.0",
            "os": {
                "name": "Other"
            },
            "version": "2.31"
        },
        "wiz": {
            "audit": {
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "test_service_account.json"

    ```json
	
    {
        "message": "{\"id\":\"11111111-1111-1111-1111-111111111111\",\"action\":\"Login\",\"requestId\":\"11111111-1111-1111-1111-111111111111\",\"status\":\"SUCCESS\",\"timestamp\":\"2025-04-09T14:09:11.559605Z\",\"actionParameters\":{\"clientID\":\"aaaaaaaaaaaaaaaaaaaaaaaaaa\",\"error\":\"\",\"groups\":null,\"name\":\"user_name\",\"products\":[\"\"],\"role\":\"\",\"scopes\":[\"\"],\"sourceIP\":\"1.2.3.4\",\"userEmail\":\"john.doe@company.fr\",\"userID\":\"1111111111111111111111111111111111111111111111111111\",\"userPoolType\":\"sa\",\"userpoolID\":\"eu-west-1_AAAAAAAAA\"},\"userAgent\":\"wiz-sensor/1.0.6349\",\"sourceIP\":\"1.2.3.4\",\"serviceAccount\":{\"id\":\"1111111111111111111111111111111111111111111111111111\",\"name\":\"user_name\"},\"user\":null}",
        "event": {
            "action": "Login",
            "category": [
                "authentication"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "start"
            ]
        },
        "@timestamp": "2025-04-09T14:09:11.559605Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "user_name"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "1111111111111111111111111111111111111111111111111111",
            "name": "user_name"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Other",
            "original": "wiz-sensor/1.0.6349",
            "os": {
                "name": "Other"
            }
        },
        "wiz": {
            "audit": {
                "products": [
                    ""
                ],
                "scopes": [
                    ""
                ],
                "service_account": {
                    "creator": {
                        "email": "john.doe@company.fr"
                    }
                },
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "tokenrefresh.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"eabe0685-19ac-4c93-929d-12f92aa6a1bc\",\n    \"action\": \"TokenRefresh\",\n    \"requestId\": \"4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049\",\n    \"status\": \"SUCCESS\",\n    \"timestamp\": \"2025-02-06T13:39:25.30484Z\",\n    \"actionParameters\": {\n      \"after\": null,\n      \"filterBy\": {\n        \"search\": \"Test_UzbhTWx26DwpBUcU_\"\n      },\n      \"first\": 500,\n      \"selection\": [\n        {\n          \"nodes\": [\n            \"id\",\n            \"name\",\n            \"createdAt\",\n            {\n              \"lastRun\": [\n                \"url\",\n                \"status\",\n                \"runAt\"\n              ]\n            }\n          ]\n        },\n        {\n          \"pageInfo\": [\n            \"hasNextPage\",\n            \"endCursor\"\n          ]\n        }\n      ]\n    },\n    \"userAgent\": \"python-requests/2.31.0\",\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"xNgww7tONKtQK6zw\",\n      \"name\": \"ax-us\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "TokenRefresh",
            "category": [
                "session"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2025-02-06T13:39:25.304840Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ax-us"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Python Requests",
            "original": "python-requests/2.31.0",
            "os": {
                "name": "Other"
            },
            "version": "2.31"
        },
        "wiz": {
            "audit": {
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "update_report.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"842d4a00-6e04-4e52-8119-8053f0743409\",\n    \"action\": \"RerunReport\",\n    \"requestId\": \"da7ab45f-9c57-4af6-859d-797b60a919dd\",\n    \"status\": \"SUCCESS\",\n    \"timestamp\": \"2025-02-06T13:39:25.502963Z\",\n    \"actionParameters\": {\n      \"input\": {\n        \"id\": \"b8ad5ae3-ffea-444f-8d80-175a49e14894\"\n      },\n      \"selection\": [\n        {\n          \"report\": [\n            \"id\"\n          ]\n        }\n      ]\n    },\n    \"userAgent\": \"python-requests/2.31.0\",\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"xNgww7tONKtQK6zw\",\n      \"name\": \"ax-us\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "RerunReport",
            "category": [
                "process"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "start"
            ]
        },
        "@timestamp": "2025-02-06T13:39:25.502963Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ax-us"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Python Requests",
            "original": "python-requests/2.31.0",
            "os": {
                "name": "Other"
            },
            "version": "2.31"
        },
        "wiz": {
            "audit": {
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```


=== "updateuser.json"

    ```json
	
    {
        "message": "{\n    \"id\": \"eabe0685-19ac-4c93-929d-12f92aa6a1bc\",\n    \"action\": \"UpdateUser\",\n    \"requestId\": \"4a6d5d7d-85ba-49c6-aa0d-93bfe3e49049\",\n    \"status\": \"SUCCESS\",\n    \"timestamp\": \"2025-02-06T13:39:25.30484Z\",\n    \"actionParameters\": {\n      \"after\": null,\n      \"filterBy\": {\n        \"search\": \"Test_UzbhTWx26DwpBUcU_\"\n      },\n      \"first\": 500,\n      \"selection\": [\n        {\n          \"nodes\": [\n            \"id\",\n            \"name\",\n            \"createdAt\",\n            {\n              \"lastRun\": [\n                \"url\",\n                \"status\",\n                \"runAt\"\n              ]\n            }\n          ]\n        },\n        {\n          \"pageInfo\": [\n            \"hasNextPage\",\n            \"endCursor\"\n          ]\n        }\n      ]\n    },\n    \"userAgent\": \"python-requests/2.31.0\",\n    \"sourceIP\": \"1.2.3.4\",\n    \"serviceAccount\": {\n      \"id\": \"xNgww7tONKtQK6zw\",\n      \"name\": \"ax-us\"\n    },\n    \"user\": null\n  }",
        "event": {
            "action": "UpdateUser",
            "category": [
                "iam"
            ],
            "dataset": "Audit Logs",
            "outcome": "success",
            "type": [
                "change"
            ]
        },
        "@timestamp": "2025-02-06T13:39:25.304840Z",
        "observer": {
            "vendor": "Wiz"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ax-us"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "id": "xNgww7tONKtQK6zw",
            "name": "ax-us"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Python Requests",
            "original": "python-requests/2.31.0",
            "os": {
                "name": "Other"
            },
            "version": "2.31"
        },
        "wiz": {
            "audit": {
                "status": "SUCCESS",
                "user": {
                    "type": "service_account"
                }
            }
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`source.ip` | `ip` | IP address of the source. |
|`user.email` | `keyword` | User email address. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |
|`wiz.audit.groups` | `array` |  |
|`wiz.audit.products` | `array` |  |
|`wiz.audit.role` | `keyword` |  |
|`wiz.audit.scopes` | `array` |  |
|`wiz.audit.service_account.creator.email` | `keyword` | The email of the user who created the service account |
|`wiz.audit.status` | `keyword` |  |
|`wiz.audit.user.type` | `keyword` | The nature of the user |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Wiz/wiz-audit-logs).