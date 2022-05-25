
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Anti-virus` | McAfee Web Gateway analyze the content of requests and reponses to prevent malware infection |
| `Web proxy` | McAfee Web Gateway logs provide information about the connected client and the requested resource |
| `Web logs` | McAfee Web Gateway logs provide information about the connected client and the requested resource |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `access`, `allowed`, `connection`, `denied` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "mcafee_access_log_blocked.json"

    ```json
	
    {
        "message": "date=\"2022-03-11T10:39:16.390Z\" hostname=\"mwgproxy\" username=\"\" source_ip=1.2.3.4 destination_ip=2.2.2.41 destination_host=\"www.forbiddensite.com\" http_status_code=403 media_type=\"\" source_bytes=131 destination_bytes=0 http_request_first_line=\"GET http://www.forbiddensite.com/ HTTP/1.1\" url_categories=\"Pornography\" url_reputation_string=\"Minimal Risk\" url_reputation_code=-28 ruleset_name=\"Default\" rule_name=\"Block URLs Whose Category Is in Category Blocklist for Default Groups\" block_id=10 block_reason=\"Blocked by URL filtering\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"forbiddenapp\" http_referer=\"\" user_agent=\"curl/7.77.0\"",
        "source": {
            "ip": "1.2.3.4"
        },
        "destination": {
            "ip": "2.2.2.41",
            "domain": "www.forbiddensite.com"
        },
        "network": {
            "direction": "egress"
        },
        "event": {
            "action": "denied",
            "start": "2022-03-11T10:39:16.390Z",
            "code": "10",
            "reason": "Blocked by URL filtering",
            "category": "network",
            "kind": "event",
            "type": [
                "connection",
                "access",
                "denied"
            ]
        },
        "url": {
            "original": "http://www.forbiddensite.com/"
        },
        "user_agent": {
            "original": "curl/7.77.0"
        },
        "observer": {
            "hostname": "mwgproxy",
            "vendor": "McAfee Corp.",
            "product": "McAfee Web Gateway",
            "type": "proxy"
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


=== "mcafee_access_log_blocked2.json"

    ```json
	
    {
        "message": "date=\"2022-03-17T13:14:39.134Z\" hostname=\"mwgproxy\" username=\"\" source_ip=1.2.3.4 destination_ip=52.242.101.226 destination_host=\"slscr.update.microsoft.com\" http_status_code=407 media_type=\"\" source_bytes=173 destination_bytes=0 http_request_first_line=\"CONNECT slscr.update.microsoft.com:443 HTTP/1.1\" url_categories=\"Business, Software/Hardware\" url_reputation_string=\"Minimal Risk\" url_reputation_code=-42 ruleset_name=\"Authentication: Direct Proxy\" rule_name=\"Authenticate: Active Directory\" block_id=81 block_reason=\"Authentication Required\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"\" http_referer=\"\" user_agent=\"\"",
        "source": {
            "ip": "1.2.3.4"
        },
        "destination": {
            "ip": "52.242.101.226",
            "domain": "slscr.update.microsoft.com",
            "port": 443
        },
        "network": {
            "direction": "egress"
        },
        "event": {
            "action": "denied",
            "start": "2022-03-17T13:14:39.134Z",
            "code": "81",
            "reason": "Authentication Required",
            "category": "network",
            "kind": "event",
            "type": [
                "connection",
                "access",
                "denied"
            ]
        },
        "url": {
            "domain": "slscr.update.microsoft.com",
            "port": 443
        },
        "observer": {
            "hostname": "mwgproxy",
            "vendor": "McAfee Corp.",
            "product": "McAfee Web Gateway",
            "type": "proxy"
        },
        "http": {
            "request": {
                "method": "CONNECT",
                "bytes": 173
            },
            "response": {
                "bytes": 0,
                "status_code": 407
            }
        },
        "rule": {
            "ruleset": "Authentication: Direct Proxy",
            "name": "Authenticate: Active Directory"
        },
        "mcafee": {
            "webgateway": {
                "url": {
                    "reputation": "Minimal Risk",
                    "reputation_code": -42,
                    "categories": [
                        "Business",
                        "Software/Hardware"
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


=== "mcafee_access_log_empty_destination_host.json"

    ```json
	
    {
        "message": "date=\"2022-03-24T13:54:02.740Z\" hostname=\"mwgproxy\" username=\"myusername\" source_ip=1.2.3.4 destination_ip=255.255.255.255 destination_host=\"\" http_status_code=400 media_type=\"\" source_bytes=316 destination_bytes=0 http_request_first_line=\"CONNECT :80 HTTP/1.1\" url_categories=\"Business, Software/Hardware\" url_reputation_string=\"Minimal Risk\" url_reputation_code=-3 ruleset_name=\"Exception DFS\" rule_name=\"Forbidden Access\" block_id=10 block_reason=\"Blocked by URL filtering\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"\" http_referer=\"\" user_agent=\"\"",
        "source": {
            "ip": "1.2.3.4"
        },
        "destination": {
            "ip": "255.255.255.255"
        },
        "network": {
            "direction": "egress"
        },
        "event": {
            "action": "denied",
            "start": "2022-03-24T13:54:02.740Z",
            "code": "10",
            "reason": "Blocked by URL filtering",
            "category": "network",
            "kind": "event",
            "type": [
                "connection",
                "access",
                "denied"
            ]
        },
        "user": {
            "name": "myusername"
        },
        "observer": {
            "hostname": "mwgproxy",
            "vendor": "McAfee Corp.",
            "product": "McAfee Web Gateway",
            "type": "proxy"
        },
        "http": {
            "request": {
                "method": "CONNECT",
                "bytes": 316
            },
            "response": {
                "bytes": 0,
                "status_code": 400
            }
        },
        "rule": {
            "ruleset": "Exception DFS",
            "name": "Forbidden Access"
        },
        "mcafee": {
            "webgateway": {
                "url": {
                    "reputation": "Minimal Risk",
                    "reputation_code": -3,
                    "categories": [
                        "Business",
                        "Software/Hardware"
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


=== "mcafee_access_log_success.json"

    ```json
	
    {
        "message": "date=\"2022-03-11T09:50:47.399Z\" hostname=\"mwgproxy\" username=\"myusername\" source_ip=1.2.3.4 destination_ip=142.250.178.131 destination_host=\"www.google.fr\" http_status_code=200 media_type=\"\" source_bytes=127 destination_bytes=14678 http_request_first_line=\"GET http://www.google.fr/ HTTP/1.1\" url_categories=\"Search Engines\" url_reputation_string=\"Minimal Risk\" url_reputation_code=0 ruleset_name=\"Dynamic Content Classification\" rule_name=\"Block URLs Whose Category Is in Category Blocklist\" block_id=0 block_reason=\"\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"\" http_referer=\"\" user_agent=\"curl/7.77.0\"",
        "user": {
            "name": "myusername"
        },
        "source": {
            "ip": "1.2.3.4"
        },
        "destination": {
            "ip": "142.250.178.131",
            "domain": "www.google.fr"
        },
        "event": {
            "action": "allowed",
            "start": "2022-03-11T09:50:47.399Z",
            "code": "0",
            "category": "network",
            "kind": "event",
            "type": [
                "connection",
                "access",
                "allowed"
            ]
        },
        "url": {
            "original": "http://www.google.fr/"
        },
        "user_agent": {
            "original": "curl/7.77.0"
        },
        "observer": {
            "hostname": "mwgproxy",
            "vendor": "McAfee Corp.",
            "product": "McAfee Web Gateway",
            "type": "proxy"
        },
        "network": {
            "direction": "egress"
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





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
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
|`network.direction` | `keyword` | Direction of the network traffic. |
|`observer.hostname` | `keyword` | Hostname of the observer. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`rule.name` | `keyword` | Rule name |
|`rule.ruleset` | `keyword` | Rule ruleset |
|`source.ip` | `ip` | IP address of the source. |
|`url.domain` | `keyword` | Domain of the url. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`url.port` | `long` | Port of the request, such as 443. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

