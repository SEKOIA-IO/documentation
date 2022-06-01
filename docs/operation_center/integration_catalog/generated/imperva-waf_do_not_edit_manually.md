
## Event Categories




In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `["connection", "access"]`, `["connection", "allowed"]`, `["connection", "denied"]`, `["connection", "error"]` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "access.json"

    ```json
	
    {
        "imperva": {
            "request": {
                "headers": [
                    {
                        "Accept": "*/*"
                    },
                    {
                        "x-v": "1"
                    },
                    {
                        "x-fapi-interaction-id": "10.10.10.10"
                    }
                ],
                "x_forwarded_for": "44.44.44.44"
            },
            "response": {
                "headers": [
                    {
                        "Content-Type": "text/html; charset\\=UTF-8"
                    }
                ]
            },
            "pop": "mia"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        },
        "client": {
            "geo": {
                "country_iso_code": "IL",
                "city_name": "Rehovot",
                "location": {
                    "lon": 34.8186,
                    "lat": 31.8969
                }
            }
        },
        "url": {
            "full": "site123.abcd.info/main.css",
            "original": "site123.abcd.info/main.css"
        },
        "http": {
            "request": {
                "referrer": "www.incapsula.com/lama",
                "method": "GET",
                "bytes": 54,
                "id": "33411452762204224"
            },
            "response": {
                "status_code": 200
            }
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 443,
            "ip": "12.12.12.12"
        },
        "tls": {
            "version": "1.2",
            "version_protocol": "tls",
            "cipher": "ECDHE-RSA-AES128-GCM-SHA256"
        },
        "event": {
            "start": "1970-01-02T10:17:36.789000Z",
            "end": "1970-01-03T14:04:16.789000Z",
            "duration": 100000000.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "access"
            ]
        },
        "@timestamp": "1970-01-02T10:17:36.789000Z"
    }
    	
	```


=== "access_security_bad.json"

    ```json
	
    {
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Webkit Browser"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/"
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4"
        },
        "event": {
            "action": "REQ_BAD_PARSE_ERROR",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "error"
            ],
            "reason": "The HTTP request was malformated"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z"
    }
    	
	```


=== "access_security_blacklisted.json"

    ```json
	
    {
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Webkit Browser"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/"
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4"
        },
        "event": {
            "action": "REQ_DOMAIN_BLACKLISTED",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "denied"
            ],
            "reason": "The destination was blacklisted"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z"
    }
    	
	```


=== "access_security_blocked.json"

    ```json
	
    {
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Webkit Browser"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/"
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4"
        },
        "event": {
            "action": "REQ_BLOCKED_VISITOR",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "denied"
            ],
            "reason": "The request was blocked based on WAF settings"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z"
    }
    	
	```


=== "access_security_cached.json"

    ```json
	
    {
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Webkit Browser"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/"
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4"
        },
        "event": {
            "action": "REQ_CACHED_WEBSITE",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "allowed"
            ],
            "reason": ""
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z"
    }
    	
	```


=== "access_security_challenged.json"

    ```json
	
    {
        "imperva": {
            "pop": "mia",
            "request": {
                "x_forwarded_for": "44.44.44.44",
                "headers": [
                    {
                        "Accept": "*/*"
                    },
                    {
                        "x-v": "1"
                    },
                    {
                        "x-fapi-interaction-id": "10.10.10.10"
                    }
                ]
            },
            "response": {
                "headers": [
                    {
                        "Content-Type": "text/html; charset\\=UTF-8"
                    }
                ]
            },
            "session": {
                "id": 3412341160002518171
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NOT_SUPPORTED"
            },
            "visitor": {
                "id": "c2e72124-0e8a-4dd8-b13b-3da246af3ab2"
            },
            "user_agent": {
                "type": "Browser"
            },
            "attack": {
                "type": "30037,1001,",
                "id": "2,1,"
            },
            "rule": {
                "names": [
                    "Block Malicious User",
                    "High Risk Resources"
                ],
                "additional_info": ",,[{\"api_specification_violation_type\":\"INVALID_PARAM_NAME\",\"parameter_name\":\"somename\"}]"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "name": "Firefox"
        },
        "client": {
            "geo": {
                "country_iso_code": "IL",
                "city_name": "Rehovot",
                "location": {
                    "lat": 31.8969,
                    "lon": 34.8186
                }
            }
        },
        "http": {
            "response": {
                "status_code": 200
            },
            "request": {
                "bytes": 54,
                "method": "GET",
                "id": "33411452762204224"
            }
        },
        "url": {
            "full": "site123.abcd.info/",
            "original": "site123.abcd.info/",
            "query": "p\\=%2fetc%2fpasswd"
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 443,
            "ip": "12.12.12.12"
        },
        "tls": {
            "version_protocol": "tls",
            "version": "1.2",
            "cipher": "ECDHE-RSA-AES128-GCM-SHA256"
        },
        "event": {
            "action": "REQ_CHALLENGED_CAPTCHA",
            "start": "1970-01-02T10:17:36.789000Z",
            "end": "1970-01-03T14:04:16.789000Z",
            "duration": 100000000.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "denied"
            ],
            "reason": "A challenge was submitted to the client"
        },
        "rule": {
            "name": "Block Malicious User,High Risk Resources,"
        },
        "@timestamp": "1970-01-02T10:17:36.789000Z"
    }
    	
	```


=== "access_security_ipv6_not_supported.json"

    ```json
	
    {
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Webkit Browser"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/"
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4"
        },
        "event": {
            "action": "REQ_IPV6_NOT_SUPPORTED",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "error"
            ],
            "reason": "The destination doesn't support IPv6 addresses"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z"
    }
    	
	```


=== "access_security_passed.json"

    ```json
	
    {
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Webkit Browser"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/"
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4"
        },
        "event": {
            "action": "REQ_PASSED",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "allowed"
            ]
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z"
    }
    	
	```


=== "access_security_unresolved.json"

    ```json
	
    {
        "imperva": {
            "pop": "cdg",
            "session": {
                "id": 393000630126853202
            },
            "client": {
                "js_support": true,
                "cookie_support": true,
                "captcha_support": "NA"
            },
            "visitor": {
                "id": "a99e6166-5092-4cce-8fb6-afae61ef7493"
            },
            "user_agent": {
                "type": "Browser"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "name": "Webkit Browser"
        },
        "client": {
            "geo": {
                "country_iso_code": "FR",
                "city_name": "Strasbourg",
                "location": {
                    "lat": 48.34,
                    "lon": 7.4508
                }
            }
        },
        "http": {
            "request": {
                "method": "GET",
                "id": "195557299895996363"
            }
        },
        "url": {
            "full": "www.test.com/",
            "original": "www.test.com/"
        },
        "network": {
            "protocol": "http"
        },
        "source": {
            "port": 45208,
            "ip": "1.2.3.4"
        },
        "event": {
            "action": "REQ_UNRESOLVED_SITE_INVALID_CNAME",
            "start": "2022-04-12T14:09:58.763000Z",
            "end": "2022-04-12T14:09:58.765000Z",
            "duration": 2.0,
            "kind": "event",
            "category": "network",
            "type": [
                "connection",
                "error"
            ],
            "reason": "The proxy failed to resolve the destination"
        },
        "@timestamp": "2022-04-12T14:09:58.763000Z"
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`client.geo.city_name` | `keyword` | City name. |
|`client.geo.country_iso_code` | `keyword` | Country ISO code. |
|`client.geo.location` | `geo_point` | Longitude and latitude. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.request.id` | `keyword` | HTTP request ID. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`imperva.attack.id` | `keyword` | None |
|`imperva.attack.type` | `keyword` | None |
|`imperva.client.captcha_support` | `keyword` | None |
|`imperva.client.cookie_support` | `boolean` | None |
|`imperva.client.js_support` | `boolean` | None |
|`imperva.pop` | `keyword` | None |
|`imperva.request.headers` | `array` | None |
|`imperva.request.x_forwarded_for` | `text` | None |
|`imperva.response.headers` | `array` | None |
|`imperva.rule.additional_info` | `text` | None |
|`imperva.rule.names` | `array` | None |
|`imperva.session.id` | `long` | None |
|`imperva.user_agent.type` | `keyword` | None |
|`imperva.visitor.id` | `keyword` | None |
|`network.protocol` | `keyword` | Application protocol name. |
|`rule.name` | `keyword` | Rule name |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`tls.cipher` | `keyword` | String indicating the cipher used during the current connection. |
|`tls.version` | `keyword` | Numeric part of the version parsed from the original string. |
|`tls.version_protocol` | `keyword` | Normalized lowercase protocol name parsed from original string. |
|`url.full` | `wildcard` | Full unparsed URL. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`url.query` | `keyword` | Query string of the request. |
|`user_agent.name` | `keyword` | Name of the user agent. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

