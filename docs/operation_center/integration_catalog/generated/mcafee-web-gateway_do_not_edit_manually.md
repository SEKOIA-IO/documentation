
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Anti-virus` | McAfee Web Gateway analyze the content of requests and reponses to prevent malware infection |
| `Web proxy` | McAfee Web Gateway logs provide information about the connected client and the requested resource |
| `Web logs` | McAfee Web Gateway logs provide information about the connected client and the requested resource |





In details, the following Table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `network` |
| Type | `` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "mcafee_access_log_success.json"

    ```json
	
    {
        "sekoiaio": {
            "intake": {
                "dialect": "mcafee-web-gateway",
                "dialect_uuid": "40bac399-2d8e-40e3-af3b-f73a622c9687",
                "parsing_status": "success"
            }
        },
        "message": "date=\"2022-03-11T09:50:47.399Z\" hostname=\"mwgproxy\" username=\"myusername\" source_ip=1.2.3.4 destination_ip=142.250.178.131 destination_host=\"www.google.fr\" http_status_code=200 media_type=\"\" source_bytes=127 destination_bytes=14678 http_request_first_line=\"GET http://www.google.fr/ HTTP/1.1\" url_categories=\"Search Engines\" url_reputation_string=\"Minimal Risk\" url_reputation_code=0 ruleset_name=\"Dynamic Content Classification\" rule_name=\"Block URLs Whose Category Is in Category Blocklist\" block_id=0 block_reason=\"\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"\" http_referer=\"\" user_agent=\"curl/7.77.0\"",
        "user": {
            "name": "myusername"
        },
        "source": {
            "ip": "1.2.3.4"
        },
        "destination": {
            "ip": "142.250.178.131"
        },
        "event": {
            "action": "allowed",
            "start": "2022-03-11T09:50:47.399Z",
            "code": "0",
            "category": "network"
        },
        "url": {
            "original": "http://www.google.fr/"
        },
        "user_agent": {
            "original": "curl/7.77.0"
        },
        "observer": {
            "hostname": "mwgproxy"
        },
        "http": {
            "request": {
                "method": "GET",
                "bytes": 127
            },
            "response": {
                "bytes": 14678,
                "status_code": 200
            }
        },
        "rule": {
            "ruleset": "Dynamic Content Classification",
            "name": "Block URLs Whose Category Is in Category Blocklist"
        },
        "mcafee": {
            "webgateway": {
                "url": {
                    "reputation": "Minimal Risk",
                    "reputation_code": 0,
                    "categories": [
                        "Search Engines"
                    ]
                },
                "application": {
                    "reputation": "Unverified"
                },
                "http": {
                    "body": {
                        "infected": "false",
                        "modified": "false"
                    }
                }
            }
        }
    }
    	
	```


=== "mcafee_access_log_blocked.json"

    ```json
	
    {
        "sekoiaio": {
            "intake": {
                "dialect": "mcafee-web-gateway",
                "dialect_uuid": "40bac399-2d8e-40e3-af3b-f73a622c9687",
                "parsing_status": "success"
            }
        },
        "message": "date=\"2022-03-11T10:39:16.390Z\" hostname=\"mwgproxy\" username=\"\" source_ip=1.2.3.4 destination_ip=2.2.2.41 destination_host=\"www.forbiddensite.com\" http_status_code=403 media_type=\"\" source_bytes=131 destination_bytes=0 http_request_first_line=\"GET http://www.forbiddensite.com/ HTTP/1.1\" url_categories=\"Pornography\" url_reputation_string=\"Minimal Risk\" url_reputation_code=-28 ruleset_name=\"Default\" rule_name=\"Block URLs Whose Category Is in Category Blocklist for Default Groups\" block_id=10 block_reason=\"Blocked by URL filtering\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"forbiddenapp\" http_referer=\"\" user_agent=\"curl/7.77.0\"",
        "source": {
            "ip": "1.2.3.4"
        },
        "destination": {
            "ip": "2.2.2.41"
        },
        "event": {
            "action": "denied",
            "start": "2022-03-11T10:39:16.390Z",
            "code": "10",
            "reason": "Blocked by URL filtering",
            "category": "network"
        },
        "url": {
            "original": "http://www.forbiddensite.com/"
        },
        "user_agent": {
            "original": "curl/7.77.0"
        },
        "observer": {
            "hostname": "mwgproxy"
        },
        "http": {
            "request": {
                "method": "GET",
                "bytes": 131
            },
            "response": {
                "bytes": 0,
                "status_code": 403
            }
        },
        "rule": {
            "ruleset": "Default",
            "name": "Block URLs Whose Category Is in Category Blocklist for Default Groups"
        },
        "mcafee": {
            "webgateway": {
                "url": {
                    "reputation": "Minimal Risk",
                    "reputation_code": -28,
                    "categories": [
                        "Pornography"
                    ]
                },
                "application": {
                    "reputation": "Unverified",
                    "name": "forbiddenapp"
                },
                "http": {
                    "body": {
                        "infected": "false",
                        "modified": "false"
                    }
                }
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.ip` | `ip` | IP address of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.bytes` | `long` | Total size in bytes of the response (body and headers). |
|`http.response.mime_type` | `keyword` | Mime type of the body of the response. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`mcafee.webgateway.application.name` | `keyword` | None |
|`mcafee.webgateway.application.reputation` | `keyword` | None |
|`mcafee.webgateway.http.body.infected` | `keyword` | None |
|`mcafee.webgateway.http.body.modified` | `keyword` | None |
|`mcafee.webgateway.url.categories` | `text` | None |
|`mcafee.webgateway.url.reputation` | `keyword` | None |
|`mcafee.webgateway.url.reputation_code` | `number` | None |
|`mcafee.webgateway.viruses` | `text` | None |
|`observer.hostname` | `keyword` | Hostname of the observer. |
|`rule.name` | `keyword` | Rule name |
|`rule.ruleset` | `keyword` | Rule ruleset |
|`source.ip` | `ip` | IP address of the source. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

