
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
        "message": "{\"timestamp\":\"2022-02-22T16:31:58.286485\",\"observer\":{\"name\":\"sekoia.webapi\",\"version\":null},\"visit\":{\"id\":null,\"ip\":\"1.2.3.4\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36\",\"referrer\":\"https://app.test.sekoia.io/operations/intakes/new\"},\"action\":{\"name\":\"intake-format-picture-retrieval\",\"path\":\"/v1/ingest/formats/4d05ecd7-1a8a-4ce1-8e6d-c2de2593fa97/picture\",\"url\":\"http://api.sekoia.io/v1/ingest/formats/4d05ecd7-1a8a-4ce1-8e6d-c2de2593fa97/picture\",\"method\":\"GET\"},\"identity\":{\"user_uuid\":\"54e0ec48-8430-4ba2-b70b-710341f41447\",\"community_uuid\":\"79997bd0-dd71-4e25-a70d-a94fa475cd2b\",\"profile_type\":\"avatar\",\"profile_identity\":\"41b811fa-6571-4d3e-9d35-38fb916adfcb\"}}",
        "sekoiaio": {
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
        "@timestamp": "2022-02-22T16:31:58.286485Z",
        "agent": {
            "name": "sekoia.webapi"
        },
        "client": {
            "user": {
                "id": "54e0ec48-8430-4ba2-b70b-710341f41447"
            },
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        },
        "http": {
            "request": {
                "method": "GET",
                "referrer": "https://app.test.sekoia.io/operations/intakes/new"
            }
        },
        "url": {
            "original": "http://api.sekoia.io/v1/ingest/formats/4d05ecd7-1a8a-4ce1-8e6d-c2de2593fa97/picture",
            "path": "/v1/ingest/formats/4d05ecd7-1a8a-4ce1-8e6d-c2de2593fa97/picture",
            "domain": "api.sekoia.io",
            "top_level_domain": "io",
            "subdomain": "api",
            "registered_domain": "sekoia.io",
            "scheme": "http",
            "port": 80
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ]
        }
    }
    	
	```


=== "activity_log_get_me_extended.json"

    ```json
	
    {
        "message": "{\"timestamp\":\"2021-10-29T11:34:23Z\",\"observer\":{\"name\":\"sekoia.webapi\",\"version\":null},\"visit\":{\"id\":null,\"ip\":\"141.229.130.228\",\"user_agent\":\"'Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/2020-08-24 06:07:18 Firefox/3.8\",\"referrer\":\"https://api.sekoia.io/v1/user/profile/settings\"},\"action\":{\"name\":null,\"path\":\"/v1/me\",\"url\":\"http://api.sekoia.io/v1/me?extended=true\",\"method\":\"GET\"},\"identity\":{\"user_uuid\":\"5beacab7-4fc9-4c07-8ec0-e6ad73ed77fe\",\"community_uuid\":\"22806a91-459c-40b1-98db-5af6ccf291fd\",\"profile_type\":\"avatar\",\"profile_identity\":\"95267578-e797-4263-90c3-09fb230536e2\"}}",
        "sekoiaio": {
            "activity": {
                "client": {
                    "id": "95267578-e797-4263-90c3-09fb230536e2",
                    "type": "avatar"
                }
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
            "ip": "141.229.130.228",
            "address": "141.229.130.228"
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
            "top_level_domain": "io",
            "subdomain": "api",
            "registered_domain": "sekoia.io",
            "scheme": "http",
            "query": "extended=true",
            "port": 80
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
        "message": "{\"timestamp\":\"2021-11-01T12:16:21.815546\",\"observer\":{\"name\":\"sekoia.webapi\",\"version\":null},\"visit\":{\"id\":null,\"ip\":\"51.255.128.104\",\"user_agent\":\"python-requests/2.26.0\",\"referrer\":\"None\"},\"action\":{\"name\":null,\"path\":\"/v2/inthreat/bundles\",\"url\":\"http://api.sekoia.io/v2/inthreat/bundles?auto_merge=1\",\"method\":\"POST\"},\"identity\":{\"user_uuid\":null,\"community_uuid\":\"02ff3284-506e-49d6-a9f5-99dbb2ea69ed\",\"profile_type\":\"apikey\",\"profile_identity\":\"9cd287a4-4a61-4bf1-998a-74087098adf4\"}}",
        "sekoiaio": {
            "activity": {
                "client": {
                    "id": "9cd287a4-4a61-4bf1-998a-74087098adf4",
                    "type": "apikey"
                }
            }
        },
        "@timestamp": "2021-11-01T12:16:21.815546Z",
        "agent": {
            "name": "sekoia.webapi"
        },
        "client": {
            "ip": "51.255.128.104",
            "address": "51.255.128.104"
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
            "top_level_domain": "io",
            "subdomain": "api",
            "registered_domain": "sekoia.io",
            "scheme": "http",
            "query": "auto_merge=1",
            "port": 80
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
|`sekoiaio.activity.action.name` | `keyword` | The name of the operation |
|`sekoiaio.activity.action.parameters` | `keyword` | The arguments supplied for the operation |
|`sekoiaio.activity.action.results` | `keyword` | The results of the operation |
|`sekoiaio.activity.client.id` | `keyword` | The identifier of the client |
|`sekoiaio.activity.client.type` | `keyword` | The nature of the client |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

