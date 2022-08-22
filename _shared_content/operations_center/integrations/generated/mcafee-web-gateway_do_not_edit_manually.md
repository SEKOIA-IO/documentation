
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
        "event": {
            "category": "network",
            "code": "10",
            "kind": "event",
            "reason": "Blocked by URL filtering",
            "action": "denied",
            "type": [
                "connection",
                "access",
                "denied"
            ],
            "start": "2022-03-11T10:39:16.390Z"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "2.2.2.41",
            "domain": "www.forbiddensite.com",
            "address": "www.forbiddensite.com",
            "top_level_domain": "com",
            "subdomain": "www",
            "registered_domain": "forbiddensite.com"
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
        "observer": {
            "hostname": "mwgproxy",
            "type": "proxy",
            "vendor": "McAfee Corp.",
            "product": "McAfee Web Gateway"
        },
        "rule": {
            "ruleset": "Default",
            "name": "Block URLs Whose Category Is in Category Blocklist for Default Groups"
        },
        "network": {
            "direction": "egress"
        },
        "user_agent": {
            "original": "curl/7.77.0"
        },
        "url": {
            "original": "http://www.forbiddensite.com/",
            "domain": "www.forbiddensite.com",
            "top_level_domain": "com",
            "subdomain": "www",
            "registered_domain": "forbiddensite.com",
            "path": "/",
            "scheme": "http",
            "port": 80
        },
        "mcafee": {
            "webgateway": {
                "application": {
                    "reputation": "Unverified",
                    "name": "forbiddenapp"
                },
                "url": {
                    "reputation": "Minimal Risk",
                    "reputation_code": -28,
                    "categories": [
                        "Pornography"
                    ]
                },
                "http": {
                    "body": {
                        "infected": "false",
                        "modified": "false"
                    }
                }
            }
        },
        "related": {
            "hosts": [
                "mwgproxy",
                "www.forbiddensite.com"
            ],
            "ip": [
                "1.2.3.4",
                "2.2.2.41"
            ]
        }
    }
    	
	```


=== "mcafee_access_log_blocked2.json"

    ```json
	
    {
        "message": "date=\"2022-03-17T13:14:39.134Z\" hostname=\"mwgproxy\" username=\"\" source_ip=1.2.3.4 destination_ip=52.242.101.226 destination_host=\"slscr.update.microsoft.com\" http_status_code=407 media_type=\"\" source_bytes=173 destination_bytes=0 http_request_first_line=\"CONNECT slscr.update.microsoft.com:443 HTTP/1.1\" url_categories=\"Business, Software/Hardware\" url_reputation_string=\"Minimal Risk\" url_reputation_code=-42 ruleset_name=\"Authentication: Direct Proxy\" rule_name=\"Authenticate: Active Directory\" block_id=81 block_reason=\"Authentication Required\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"\" http_referer=\"\" user_agent=\"\"",
        "event": {
            "category": "network",
            "code": "81",
            "kind": "event",
            "reason": "Authentication Required",
            "action": "denied",
            "type": [
                "connection",
                "access",
                "denied"
            ],
            "start": "2022-03-17T13:14:39.134Z"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "52.242.101.226",
            "domain": "slscr.update.microsoft.com",
            "port": 443,
            "address": "slscr.update.microsoft.com",
            "top_level_domain": "com",
            "subdomain": "slscr.update",
            "registered_domain": "microsoft.com"
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
        "observer": {
            "hostname": "mwgproxy",
            "type": "proxy",
            "vendor": "McAfee Corp.",
            "product": "McAfee Web Gateway"
        },
        "rule": {
            "ruleset": "Authentication: Direct Proxy",
            "name": "Authenticate: Active Directory"
        },
        "network": {
            "direction": "egress"
        },
        "url": {
            "domain": "slscr.update.microsoft.com",
            "port": 443,
            "top_level_domain": "com",
            "subdomain": "slscr.update",
            "registered_domain": "microsoft.com"
        },
        "mcafee": {
            "webgateway": {
                "application": {
                    "reputation": "Unverified"
                },
                "url": {
                    "reputation": "Minimal Risk",
                    "reputation_code": -42,
                    "categories": [
                        "Business",
                        "Software/Hardware"
                    ]
                },
                "http": {
                    "body": {
                        "infected": "false",
                        "modified": "false"
                    }
                }
            }
        },
        "related": {
            "hosts": [
                "mwgproxy",
                "slscr.update.microsoft.com"
            ],
            "ip": [
                "1.2.3.4",
                "52.242.101.226"
            ]
        }
    }
    	
	```


=== "mcafee_access_log_empty_destination_host.json"

    ```json
	
    {
        "message": "date=\"2022-03-24T13:54:02.740Z\" hostname=\"mwgproxy\" username=\"myusername\" source_ip=1.2.3.4 destination_ip=255.255.255.255 destination_host=\"\" http_status_code=400 media_type=\"\" source_bytes=316 destination_bytes=0 http_request_first_line=\"CONNECT :80 HTTP/1.1\" url_categories=\"Business, Software/Hardware\" url_reputation_string=\"Minimal Risk\" url_reputation_code=-3 ruleset_name=\"Exception DFS\" rule_name=\"Forbidden Access\" block_id=10 block_reason=\"Blocked by URL filtering\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"\" http_referer=\"\" user_agent=\"\"",
        "event": {
            "category": "network",
            "code": "10",
            "kind": "event",
            "reason": "Blocked by URL filtering",
            "action": "denied",
            "type": [
                "connection",
                "access",
                "denied"
            ],
            "start": "2022-03-24T13:54:02.740Z"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "255.255.255.255",
            "address": "255.255.255.255"
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
        "observer": {
            "hostname": "mwgproxy",
            "type": "proxy",
            "vendor": "McAfee Corp.",
            "product": "McAfee Web Gateway"
        },
        "rule": {
            "ruleset": "Exception DFS",
            "name": "Forbidden Access"
        },
        "network": {
            "direction": "egress"
        },
        "user": {
            "name": "myusername"
        },
        "mcafee": {
            "webgateway": {
                "application": {
                    "reputation": "Unverified"
                },
                "url": {
                    "reputation": "Minimal Risk",
                    "reputation_code": -3,
                    "categories": [
                        "Business",
                        "Software/Hardware"
                    ]
                },
                "http": {
                    "body": {
                        "infected": "false",
                        "modified": "false"
                    }
                }
            }
        },
        "related": {
            "hosts": [
                "mwgproxy"
            ],
            "ip": [
                "1.2.3.4",
                "255.255.255.255"
            ],
            "user": [
                "myusername"
            ]
        }
    }
    	
	```


=== "mcafee_access_log_success.json"

    ```json
	
    {
        "message": "date=\"2022-03-11T09:50:47.399Z\" hostname=\"mwgproxy\" username=\"myusername\" source_ip=1.2.3.4 destination_ip=142.250.178.131 destination_host=\"www.google.fr\" http_status_code=200 media_type=\"\" source_bytes=127 destination_bytes=14678 http_request_first_line=\"GET http://www.google.fr/ HTTP/1.1\" url_categories=\"Search Engines\" url_reputation_string=\"Minimal Risk\" url_reputation_code=0 ruleset_name=\"Dynamic Content Classification\" rule_name=\"Block URLs Whose Category Is in Category Blocklist\" block_id=0 block_reason=\"\" body_infected=false virus_names=\"\" body_modified=false application_reputation=\"Unverified\" application_name=\"\" http_referer=\"\" user_agent=\"curl/7.77.0\"",
        "event": {
            "category": "network",
            "code": "0",
            "kind": "event",
            "action": "allowed",
            "type": [
                "connection",
                "access",
                "allowed"
            ],
            "start": "2022-03-11T09:50:47.399Z"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "142.250.178.131",
            "domain": "www.google.fr",
            "address": "www.google.fr",
            "top_level_domain": "fr",
            "subdomain": "www",
            "registered_domain": "google.fr"
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
        "observer": {
            "hostname": "mwgproxy",
            "type": "proxy",
            "vendor": "McAfee Corp.",
            "product": "McAfee Web Gateway"
        },
        "rule": {
            "ruleset": "Dynamic Content Classification",
            "name": "Block URLs Whose Category Is in Category Blocklist"
        },
        "network": {
            "direction": "egress"
        },
        "user_agent": {
            "original": "curl/7.77.0"
        },
        "url": {
            "original": "http://www.google.fr/",
            "domain": "www.google.fr",
            "top_level_domain": "fr",
            "subdomain": "www",
            "registered_domain": "google.fr",
            "path": "/",
            "scheme": "http",
            "port": 80
        },
        "user": {
            "name": "myusername"
        },
        "mcafee": {
            "webgateway": {
                "application": {
                    "reputation": "Unverified"
                },
                "url": {
                    "reputation": "Minimal Risk",
                    "reputation_code": 0,
                    "categories": [
                        "Search Engines"
                    ]
                },
                "http": {
                    "body": {
                        "infected": "false",
                        "modified": "false"
                    }
                }
            }
        },
        "related": {
            "hosts": [
                "mwgproxy",
                "www.google.fr"
            ],
            "ip": [
                "1.2.3.4",
                "142.250.178.131"
            ],
            "user": [
                "myusername"
            ]
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

