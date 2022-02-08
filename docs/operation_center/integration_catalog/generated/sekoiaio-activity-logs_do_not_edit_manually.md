
## Event Categories


The following Table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | Activities on SEKOIA.IO are collected: alert update, entity creation, feed consumption, ... |
| `Authentication logs` | Activity logs provide details on authentication: status, user, IP address, password reset |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


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
                "url": "http://api.test.sekoia.io/v2/inthreat/bundles?auto_merge=1",
                "method": "POST"
            },
            "identity": {
                "user_uuid": null,
                "community_uuid": "02ff3284-506e-49d6-a9f5-99dbb2ea69ed",
                "profile_type": "apikey",
                "profile_identity": "9cd287a4-4a61-4bf1-998a-74087098adf4"
            }
        },
        "@timestamp": "2021-11-01T12:16:21.815546",
        "agent": {
            "name": "sekoia.webapi"
        },
        "client": {
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
            "original": "http://api.test.sekoia.io/v2/inthreat/bundles?auto_merge=1",
            "path": "/v2/inthreat/bundles"
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
                "referrer": "https://api.test.sekoia.io/v1/user/profile/settings"
            },
            "action": {
                "name": null,
                "path": "/v1/me",
                "url": "http://api.test.sekoia.io/v1/me?extended=true",
                "method": "GET"
            },
            "identity": {
                "user_uuid": "5beacab7-4fc9-4c07-8ec0-e6ad73ed77fe",
                "community_uuid": "22806a91-459c-40b1-98db-5af6ccf291fd",
                "profile_type": "avatar",
                "profile_identity": "95267578-e797-4263-90c3-09fb230536e2"
            }
        },
        "@timestamp": "2021-10-29T11:34:23Z",
        "agent": {
            "name": "sekoia.webapi"
        },
        "client": {
            "user": {
                "id": "5beacab7-4fc9-4c07-8ec0-e6ad73ed77fe"
            },
            "ip": "141.229.130.228"
        },
        "user_agent": {
            "original": "'Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/2020-08-24 06:07:18 Firefox/3.8"
        },
        "http": {
            "request": {
                "method": "GET",
                "referrer": "https://api.test.sekoia.io/v1/user/profile/settings"
            }
        },
        "url": {
            "original": "http://api.test.sekoia.io/v1/me?extended=true",
            "path": "/v1/me"
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
        }
    }
    	
	```





## Extracted Fields

The following Table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`agent.name` | `keyword` | Custom name of the agent. |
|`agent.version` | `keyword` | Version of the agent. |
|`client.ip` | `ip` | IP address of the client. |
|`client.user.id` | `keyword` | Unique identifier of the user. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`sekoiaio.activity.client.id` | `keyword` | None |
|`sekoiaio.activity.client.type` | `keyword` | None |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

