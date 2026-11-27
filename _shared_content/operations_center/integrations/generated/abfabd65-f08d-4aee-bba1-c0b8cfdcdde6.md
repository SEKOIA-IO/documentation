
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | None |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `` |
| Type | `` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "configuration_access1.json"

    ```json
	
    {
        "message": "{\"deviceType\": \"Desktop\", \"ipAddress\": \"8.8.8.8\", \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36\", \"taskDisplayName\": \"Get OMS Session Data (Web Service)\", \"requestTime\": \"2025-11-27T08:22:48.799Z\", \"taskId\": \"dc1bea8c446c11de98360015c5e6daf6\", \"systemAccount\": \"T00000000\", \"sessionId\": \"1a1a1a\", \"activityAction\": \"READ\", \"tenantId\": \"client\", \"tenantHost\": \"wd1-service.myworkday.com\"}",
        "event": {
            "action": "Get OMS Session Data",
            "category": [
                "configuration"
            ],
            "kind": "event",
            "message": "Get OMS Session Data (Web Service)",
            "outcome": "success",
            "type": [
                "access"
            ]
        },
        "@timestamp": "2025-11-27T08:22:48.799000Z",
        "client": {
            "address": "8.8.8.8",
            "user": {
                "name": "T00000000"
            }
        },
        "observer": {
            "product": "Activity logs",
            "type": "Application",
            "vendor": "Workday"
        },
        "related": {
            "user": [
                "T00000000"
            ]
        },
        "service": {
            "name": "Web Service"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Chrome",
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "os": {
                "name": "Windows",
                "type": "Desktop",
                "version": "10"
            },
            "version": "142.0.0"
        },
        "workday": {
            "session": {
                "id": "1a1a1a"
            },
            "tenant": {
                "host": "wd1-service.myworkday.com",
                "id": "client"
            }
        }
    }
    	
	```


=== "configuration_access2.json"

    ```json
	
    {
        "message": "{\"taskId\": \"dc71c6e6446c11de98360015c5e6daf6\", \"activityAction\": \"READ\", \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0\", \"deviceType\": \"Desktop\", \"ipAddress\": \"8.8.8.8\", \"systemAccount\": \"T0000000\", \"sessionId\": \"1a1a1a\", \"requestTime\": \"2025-11-26T14:41:19.892Z\", \"taskDisplayName\": \"getEditResult -> get edit result (System)\", \"tenantId\": \"client\", \"tenantHost\": \"wd1-services.myworkday.com\"}",
        "event": {
            "action": "getEditResult -> get edit result",
            "category": [
                "configuration"
            ],
            "kind": "event",
            "message": "getEditResult -> get edit result (System)",
            "outcome": "success",
            "type": [
                "access"
            ]
        },
        "@timestamp": "2025-11-26T14:41:19.892000Z",
        "client": {
            "address": "8.8.8.8",
            "user": {
                "name": "T0000000"
            }
        },
        "observer": {
            "product": "Activity logs",
            "type": "Application",
            "vendor": "Workday"
        },
        "related": {
            "user": [
                "T0000000"
            ]
        },
        "service": {
            "name": "System"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Edge",
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
            "os": {
                "name": "Windows",
                "type": "Desktop",
                "version": "10"
            },
            "version": "142.0.0"
        },
        "workday": {
            "session": {
                "id": "1a1a1a"
            },
            "tenant": {
                "host": "wd1-services.myworkday.com",
                "id": "client"
            }
        }
    }
    	
	```


=== "configuration_change.json"

    ```json
	
    {
        "message": "{\"ipAddress\": \"8.8.8.8\", \"activityAction\": \"READ\", \"taskDisplayName\": \"Edit Customer Service Active View\", \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0\", \"taskId\": \"984c81981d0449af9ef5ef7231f146e8\", \"sessionId\": \"a1a1a1\", \"deviceType\": \"Desktop\", \"requestTime\": \"2025-11-26T14:14:48.238Z\", \"systemAccount\": \"T000000\", \"tenantId\": \"client\", \"tenantHost\": \"wd1-services.myworkday.com\"}",
        "event": {
            "action": "Edit Customer Service Active View",
            "category": [
                "configuration"
            ],
            "kind": "event",
            "message": "Edit Customer Service Active View",
            "outcome": "success",
            "type": [
                "change"
            ]
        },
        "@timestamp": "2025-11-26T14:14:48.238000Z",
        "client": {
            "address": "8.8.8.8",
            "user": {
                "name": "T000000"
            }
        },
        "observer": {
            "product": "Activity logs",
            "type": "Application",
            "vendor": "Workday"
        },
        "related": {
            "user": [
                "T000000"
            ]
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Edge",
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
            "os": {
                "name": "Windows",
                "type": "Desktop",
                "version": "10"
            },
            "version": "142.0.0"
        },
        "workday": {
            "session": {
                "id": "a1a1a1"
            },
            "tenant": {
                "host": "wd1-services.myworkday.com",
                "id": "client"
            }
        }
    }
    	
	```


=== "start_session.json"

    ```json
	
    {
        "message": "{\"sessionId\": \"1a1a1a\", \"deviceType\": \"Phone\", \"taskDisplayName\": \"Start New Session (Web Service)\", \"activityAction\": \"READ\", \"ipAddress\": \"8.8.8.8\", \"systemAccount\": \"T0000000\", \"taskId\": \"03f043df676e40cfad46bc576f89b07f\", \"userAgent\": \"Workday/2025.09.2.20064 (AndroidNative)\", \"requestTime\": \"2025-10-14T15:39:24.334Z\", \"tenantId\": \"client\", \"tenantHost\": \"wd1-service.myworkday.com\"}",
        "event": {
            "action": "Start New Session",
            "category": [
                "session"
            ],
            "kind": "event",
            "message": "Start New Session (Web Service)",
            "outcome": "success",
            "type": [
                "start"
            ]
        },
        "@timestamp": "2025-10-14T15:39:24.334000Z",
        "client": {
            "address": "8.8.8.8",
            "user": {
                "name": "T0000000"
            }
        },
        "observer": {
            "product": "Activity logs",
            "type": "Application",
            "vendor": "Workday"
        },
        "related": {
            "user": [
                "T0000000"
            ]
        },
        "service": {
            "name": "Web Service"
        },
        "user_agent": {
            "device": {
                "name": "Generic Smartphone"
            },
            "name": "Other",
            "original": "Workday/2025.09.2.20064 (AndroidNative)",
            "os": {
                "name": "Android",
                "type": "Phone"
            }
        },
        "workday": {
            "session": {
                "id": "1a1a1a"
            },
            "tenant": {
                "host": "wd1-service.myworkday.com",
                "id": "client"
            }
        }
    }
    	
	```


=== "task_info.json"

    ```json
	
    {
        "message": "{\"taskDisplayName\": \"Complete Manager Input\", \"taskId\": \"dc2d85a8446c11de98360015c5e6daf6\", \"ipAddress\": \"8.8.8.8\", \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0\", \"activityAction\": \"READ\", \"deviceType\": \"Desktop\", \"systemAccount\": \"T000000\", \"sessionId\": \"1a1a1a\", \"requestTime\": \"2025-11-27T09:05:07.593Z\", \"tenantId\": \"client\", \"tenantHost\": \"wd1-services.myworkday.com\"}",
        "event": {
            "action": "Complete Manager Input",
            "category": [
                "web"
            ],
            "kind": "event",
            "message": "Complete Manager Input",
            "type": [
                "info"
            ]
        },
        "@timestamp": "2025-11-27T09:05:07.593000Z",
        "client": {
            "address": "8.8.8.8",
            "user": {
                "name": "T000000"
            }
        },
        "observer": {
            "product": "Activity logs",
            "type": "Application",
            "vendor": "Workday"
        },
        "related": {
            "user": [
                "T000000"
            ]
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Edge",
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
            "os": {
                "name": "Windows",
                "type": "Desktop",
                "version": "10"
            },
            "version": "142.0.0"
        },
        "workday": {
            "session": {
                "id": "1a1a1a"
            },
            "tenant": {
                "host": "wd1-services.myworkday.com",
                "id": "client"
            }
        }
    }
    	
	```


=== "url_access.json"

    ```json
	
    {
        "message": "{\"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0\", \"deviceType\": \"Desktop\", \"taskDisplayName\": \"feature/toggles/get (GET) (v0 - \u2005)\", \"systemAccount\": \"T0000000\", \"activityAction\": \"READ\", \"ipAddress\": \"8.8.8.8\", \"taskId\": \"d71d2db783c51220103fd29958a38117\", \"sessionId\": \"1a1a1a\", \"requestTime\": \"2025-10-14T15:34:25.638Z\", \"tenantId\": \"client\", \"tenantHost\": \"wd1-service.myworkday.com\"}",
        "event": {
            "category": [
                "web"
            ],
            "kind": "event",
            "message": "feature/toggles/get (GET) (v0 - \u2005)",
            "outcome": "success",
            "type": [
                "access"
            ]
        },
        "@timestamp": "2025-10-14T15:34:25.638000Z",
        "client": {
            "address": "8.8.8.8",
            "user": {
                "name": "T0000000"
            }
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "observer": {
            "product": "Activity logs",
            "type": "Application",
            "vendor": "Workday"
        },
        "related": {
            "user": [
                "T0000000"
            ]
        },
        "url": {
            "original": "feature/toggles/get",
            "path": "feature/toggles/get"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Edge",
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
            "os": {
                "name": "Windows",
                "type": "Desktop",
                "version": "10"
            },
            "version": "140.0.0"
        },
        "workday": {
            "session": {
                "id": "1a1a1a"
            },
            "tenant": {
                "host": "wd1-service.myworkday.com",
                "id": "client"
            }
        }
    }
    	
	```


=== "url_access2.json"

    ```json
	
    {
        "message": "{\"sessionId\": \"1a1a1a\", \"activityAction\": \"READ\", \"taskDisplayName\": \"sso/idTokenForSession/forTargetService (GET) (v1 - \u2005)\", \"taskId\": \"dfdeaac4dec91000098116a0f74b8794\", \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36\", \"systemAccount\": \"T0000000\", \"deviceType\": \"Desktop\", \"ipAddress\": \"8.8.8.8\", \"requestTime\": \"2025-10-14T15:31:00.642Z\", \"tenantId\": \"client\", \"tenantHost\": \"wd1-service.myworkday.com\"}",
        "event": {
            "category": [
                "web"
            ],
            "kind": "event",
            "message": "sso/idTokenForSession/forTargetService (GET) (v1 - \u2005)",
            "outcome": "success",
            "type": [
                "access"
            ]
        },
        "@timestamp": "2025-10-14T15:31:00.642000Z",
        "client": {
            "address": "8.8.8.8",
            "user": {
                "name": "T0000000"
            }
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "observer": {
            "product": "Activity logs",
            "type": "Application",
            "vendor": "Workday"
        },
        "related": {
            "user": [
                "T0000000"
            ]
        },
        "url": {
            "original": "sso/idTokenForSession/forTargetService",
            "path": "sso/idTokenForSession/forTargetService"
        },
        "user_agent": {
            "device": {
                "name": "Other"
            },
            "name": "Chrome",
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
            "os": {
                "name": "Windows",
                "type": "Desktop",
                "version": "10"
            },
            "version": "141.0.0"
        },
        "workday": {
            "session": {
                "id": "1a1a1a"
            },
            "tenant": {
                "host": "wd1-service.myworkday.com",
                "id": "client"
            }
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`client.address` | `keyword` | Client network address. |
|`client.user.name` | `keyword` | Short name or login of the user. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`http.request.method` | `keyword` | HTTP request method. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`service.name` | `keyword` | Name of the service. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |
|`user_agent.os.type` | `keyword` | Which commercial OS family (one of: linux, macos, unix or windows). |
|`workday.session.id` | `keyword` |  |
|`workday.tenant.host` | `keyword` |  |
|`workday.tenant.id` | `keyword` |  |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/WorkDay/workday-activity-logs).