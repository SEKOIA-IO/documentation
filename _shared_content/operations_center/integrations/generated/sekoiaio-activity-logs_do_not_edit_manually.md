
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | Activities on SEKOIA.IO are collected: alert update, entity creation, feed consumption, ... |
| `Authentication logs` | Activity logs provide details on authentication: status, user, IP address, password reset |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "activity_log_get_intake_format_picture.json"

    ```json
	
    {
        "ecs": {
            "version": "1.10.0"
        },
        "message": "{\"timestamp\":\"2022-02-22T16:31:58.286485\",\"observer\":{\"name\":\"sekoia.webapi\",\"version\":null},\"visit\":{\"id\":null,\"ip\":\"1.2.3.4\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36\",\"referrer\":\"https://app.test.sekoia.io/operations/intakes/new\"},\"action\":{\"name\":\"intake-format-picture-retrieval\",\"path\":\"/v1/ingest/formats/4d05ecd7-1a8a-4ce1-8e6d-c2de2593fa97/picture\",\"url\":\"http://api.sekoia.io/v1/ingest/formats/4d05ecd7-1a8a-4ce1-8e6d-c2de2593fa97/picture\",\"method\":\"GET\"},\"identity\":{\"user_uuid\":\"54e0ec48-8430-4ba2-b70b-710341f41447\",\"community_uuid\":\"79997bd0-dd71-4e25-a70d-a94fa475cd2b\",\"profile_type\":\"avatar\",\"profile_identity\":\"41b811fa-6571-4d3e-9d35-38fb916adfcb\"}}",
        "url": {
            "subdomain": "api",
            "domain": "api.sekoia.io",
            "path": "/v1/ingest/formats/4d05ecd7-1a8a-4ce1-8e6d-c2de2593fa97/picture",
            "registered_domain": "sekoia.io",
            "port": 80,
            "original": "http://api.sekoia.io/v1/ingest/formats/4d05ecd7-1a8a-4ce1-8e6d-c2de2593fa97/picture",
            "top_level_domain": "io",
            "scheme": "http"
        },
        "http": {
            "request": {
                "method": "GET",
                "referrer": "https://app.test.sekoia.io/operations/intakes/new"
            }
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        },
        "client": {
            "ip": "1.2.3.4",
            "user": {
                "id": "54e0ec48-8430-4ba2-b70b-710341f41447"
            },
            "address": "1.2.3.4"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "sekoia.io activity logs",
                "parsing_status": "success",
                "dialect_uuid": "41e3ca4e-a714-41aa-ad69-684a0b3835fc"
            },
            "activity": {
                "client": {
                    "id": "41b811fa-6571-4d3e-9d35-38fb916adfcb",
                    "type": "avatar"
                },
                "action": {
                    "name": "intake-format-picture-retrieval"
                }
            }
        },
        "agent": {
            "name": "sekoia.webapi"
        },
        "@timestamp": "2022-02-22T16:31:58.286485Z",
        "event": {
            "id": "25e373f2-83d1-490e-ae7e-133231e0253a",
            "dialect": "sekoia.io activity logs",
            "outcome": "success",
            "dialect_uuid": "9aa59589-1601-4ff5-ac09-b85c6dc174b0",
            "created": "2021-09-03"
        }
    }
    	
	```


=== "activity_log_get_me_extended.json"

    ```json
	
    {
        "message": {
            "timestamp": "2021-10-29T11:34:23Z",
            "observer": {
                "name": "sekoia.webapi",
                "version": null
            },
            "visit": {
                "id": null,
                "ip": "141.229.130.228",
                "user_agent": "'Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/2020-08-24 06:07:18 Firefox/3.8",
                "referrer": "https://api.sekoia.io/v1/user/profile/settings"
            },
            "action": {
                "name": null,
                "path": "/v1/me",
                "url": "http://api.sekoia.io/v1/me?extended=true",
                "method": "GET"
            },
            "identity": {
                "user_uuid": "5beacab7-4fc9-4c07-8ec0-e6ad73ed77fe",
                "community_uuid": "22806a91-459c-40b1-98db-5af6ccf291fd",
                "profile_type": "avatar",
                "profile_identity": "95267578-e797-4263-90c3-09fb230536e2"
            }
        },
        "@timestamp": "2021-10-29T11:34:23.000000Z",
        "agent": {
            "name": "sekoia.webapi"
        },
        "client": {
            "user": {
                "id": "5beacab7-4fc9-4c07-8ec0-e6ad73ed77fe"
            },
            "address": "141.229.130.228",
            "ip": "141.229.130.228"
        },
        "user_agent": {
            "original": "'Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/2020-08-24 06:07:18 Firefox/3.8"
        },
        "http": {
            "request": {
                "method": "GET",
                "referrer": "https://api.sekoia.io/v1/user/profile/settings"
            }
        },
        "url": {
            "original": "http://api.sekoia.io/v1/me?extended=true",
            "path": "/v1/me",
            "domain": "api.sekoia.io",
            "port": 80,
            "query": "extended=true",
            "registered_domain": "sekoia.io",
            "scheme": "http",
            "subdomain": "api",
            "top_level_domain": "io"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "sekoiaio-activity-logs",
                "dialect_uuid": "41e3ca4e-a714-41aa-ad69-684a0b3835fc"
            },
            "activity": {
                "client": {
                    "id": "95267578-e797-4263-90c3-09fb230536e2",
                    "type": "avatar"
                }
            }
        },
        "event": {
            "id": "0088f426-d1b7-462b-ad8a-99aca6301432",
            "created": "2021-10-29T11:37:11Z",
            "outcome": "failure"
        },
        "related": {
            "ip": [
                "141.229.130.228"
            ]
        }
    }
    	
	```


=== "activity_log_post_bundle.json"

    ```json
	
    {
        "message": {
            "timestamp": "2021-11-01T12:16:21.815546",
            "observer": {
                "name": "sekoia.webapi",
                "version": null
            },
            "visit": {
                "id": null,
                "ip": "51.255.128.104",
                "user_agent": "python-requests/2.26.0",
                "referrer": "None"
            },
            "action": {
                "name": null,
                "path": "/v2/inthreat/bundles",
                "url": "http://api.sekoia.io/v2/inthreat/bundles?auto_merge=1",
                "method": "POST"
            },
            "identity": {
                "user_uuid": null,
                "community_uuid": "02ff3284-506e-49d6-a9f5-99dbb2ea69ed",
                "profile_type": "apikey",
                "profile_identity": "9cd287a4-4a61-4bf1-998a-74087098adf4"
            }
        },
        "@timestamp": "2021-11-01T12:16:21.815546Z",
        "agent": {
            "name": "sekoia.webapi"
        },
        "client": {
            "address": "51.255.128.104",
            "ip": "51.255.128.104"
        },
        "user_agent": {
            "original": "python-requests/2.26.0"
        },
        "http": {
            "request": {
                "method": "POST"
            }
        },
        "url": {
            "original": "http://api.sekoia.io/v2/inthreat/bundles?auto_merge=1",
            "path": "/v2/inthreat/bundles",
            "domain": "api.sekoia.io",
            "registered_domain": "sekoia.io",
            "subdomain": "api",
            "top_level_domain": "io",
            "scheme": "http",
            "port": 80,
            "query": "auto_merge=1"
        },
        "event": {
            "id": "624a4f6a-73f4-41a8-b202-01e9ba5712be",
            "created": "2021-11-01T12:19:11Z",
            "outcome": "failure"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "sekoiaio-activity-logs",
                "dialect_uuid": "41e3ca4e-a714-41aa-ad69-684a0b3835fc"
            },
            "activity": {
                "client": {
                    "id": "9cd287a4-4a61-4bf1-998a-74087098adf4",
                    "type": "apikey"
                }
            }
        },
        "related": {
            "ip": [
                "51.255.128.104"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`agent.name` | `keyword` | Custom name of the agent. |
|`agent.version` | `keyword` | Version of the agent. |
|`client.ip` | `ip` | IP address of the client. |
|`client.user.id` | `keyword` | Unique identifier of the user. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`sekoiaio.activity.action.name` | `keyword` | None |
|`sekoiaio.activity.action.parameters` | `keyword` | None |
|`sekoiaio.activity.action.results` | `keyword` | None |
|`sekoiaio.activity.client.id` | `keyword` | None |
|`sekoiaio.activity.client.type` | `keyword` | None |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

