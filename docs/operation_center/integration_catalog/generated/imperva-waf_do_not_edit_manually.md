


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
            "start": "1973-11-29T21:33:09.000000Z",
            "end": "1977-01-30T07:19:49.000000Z",
            "duration": 100000000.0
        }
    }
    	
	```


=== "access_security.json"

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
            "action": "REQ_CHALLENGE_CAPTCHA",
            "start": "1973-11-29T21:33:09.000000Z",
            "end": "1977-01-30T07:19:49.000000Z",
            "duration": 100000000.0
        },
        "rule": {
            "name": "Block Malicious User,High Risk Resources,"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`client.geo.city_name` | `keyword` | City name. |
|`client.geo.country_iso_code` | `keyword` | Country ISO code. |
|`client.geo.location` | `geo_point` | Longitude and latitude. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
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

