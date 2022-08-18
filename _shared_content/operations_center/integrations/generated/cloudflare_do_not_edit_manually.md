
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web logs` | Cloudflare act as a proxy and provide associated traffic logs |
| `Web application firewall logs` | Cloudflare protect web application with its web application firewall and provide associated traffic logs |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "http.json"

    ```json
	
    {
        "source": {
            "ip": "128.199.137.233",
            "address": "128.199.137.233"
        },
        "destination": {
            "address": "foo-bar-baz.xyz"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "bytes": 629,
                "status_code": 302
            }
        },
        "url": {
            "path": "/"
        },
        "cloudflare": {
            "EdgeEndTimestamp": 1652773910790000000,
            "EdgeStartTimestamp": 1652773910440000000,
            "RayID": "70cac52c4a7d48ee",
            "EdgeResponseBytes": 629,
            "EdgeResponseStatus": 302
        },
        "related": {
            "ip": [
                "128.199.137.233"
            ]
        }
    }
    	
	```


=== "waf.json"

    ```json
	
    {
        "event": {
            "action": "block"
        },
        "source": {
            "ip": "37.171.84.113",
            "as": {
                "number": 51207
            },
            "geo": {
                "country_name": "FR"
            },
            "address": "37.171.84.113"
        },
        "destination": {
            "address": "foo-bar-baz.xyz"
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "url": {
            "path": "/.svn/entries"
        },
        "cloudflare": {
            "clientASNDescription": "FREEM",
            "matchIndex": 0,
            "metadata": [
                {
                    "key": "group",
                    "value": "cloudflare_specials"
                },
                {
                    "key": "rule_message",
                    "value": "Version Control - Information Disclosure"
                }
            ],
            "rayName": "70de02a2c9213a99",
            "sampleInterval": 1,
            "source": "waf"
        },
        "network": {
            "protocol": "HTTP/1.1"
        },
        "@timestamp": "2022-05-19T15:54:17Z",
        "rule": {
            "id": "100016"
        },
        "user_agent": {
            "original": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
        },
        "related": {
            "ip": [
                "37.171.84.113"
            ]
        }
    }
    	
	```


=== "waf2.json"

    ```json
	
    {
        "event": {
            "outcome": "success"
        },
        "source": {
            "ip": "37.171.51.184",
            "as": {
                "number": 51207
            },
            "geo": {
                "country_name": "fr"
            },
            "port": 11620,
            "address": "37.171.51.184"
        },
        "destination": {
            "address": "foo-bar-baz.xyz"
        },
        "http": {
            "request": {
                "method": "GET",
                "bytes": 567
            },
            "response": {
                "bytes": 4314,
                "status_code": 403
            }
        },
        "url": {
            "path": "/.git/HEAD"
        },
        "cloudflare": {
            "EdgeEndTimestamp": 1653046053088000000,
            "EdgeStartTimestamp": 1653046053084000000,
            "RayID": "70e4b947c9a939ff",
            "EdgeResponseBytes": 4314,
            "EdgeResponseStatus": 403,
            "CacheCacheStatus": "unknown",
            "CacheResponseBytes": 0,
            "CacheResponseStatus": 0,
            "CacheTieredFill": false,
            "ClientDeviceType": "desktop",
            "ClientIPClass": "noRecord",
            "ClientRequestPath": "/.git/HEAD",
            "Cookies": {},
            "EdgeColoCode": "CDG",
            "EdgeColoID": 19,
            "EdgePathingOp": "wl",
            "EdgePathingSrc": "macro",
            "EdgePathingStatus": "nr",
            "EdgeRateLimitID": 0,
            "EdgeResponseCompressionRatio": 1,
            "EdgeResponseContentType": "text/html",
            "FirewallMatchesActions": [
                "block"
            ],
            "FirewallMatchesRuleIDs": [
                "100016"
            ],
            "FirewallMatchesSources": [
                "waf"
            ],
            "OriginResponseBytes": 0,
            "OriginResponseStatus": 0,
            "OriginResponseTime": 0,
            "OriginSSLProtocol": "unknown",
            "ParentRayID": "00",
            "RequestHeaders": {},
            "ResponseHeaders": {},
            "SecurityLevel": "med",
            "WAFAction": "drop",
            "WAFFlags": "0",
            "WAFProfile": "high",
            "WAFRuleID": "100016",
            "WAFRuleMessage": "Version Control - Information Disclosure",
            "WorkerCPUTime": 0,
            "WorkerStatus": "unknown",
            "WorkerSubrequest": false,
            "WorkerSubrequestCount": 0,
            "ZoneID": 545468107
        },
        "network": {
            "protocol": "HTTP/1.1"
        },
        "user_agent": {
            "original": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
        },
        "tls": {
            "cipher": "NONE",
            "version_protocol": "none"
        },
        "related": {
            "ip": [
                "37.171.51.184"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cloudflare.CacheCacheStatus` | `string` | None |
|`cloudflare.CacheResponseBytes` | `number` | None |
|`cloudflare.CacheResponseStatus` | `number` | None |
|`cloudflare.CacheTieredFill` | `bool` | None |
|`cloudflare.ClientDeviceType` | `string` | None |
|`cloudflare.ClientIPClass` | `string` | None |
|`cloudflare.ClientRequestPath` | `string` | None |
|`cloudflare.ClientXRequestedWith` | `string` | None |
|`cloudflare.Cookies` | `object` | None |
|`cloudflare.EdgeColoCode` | `string` | None |
|`cloudflare.EdgeColoID` | `number` | None |
|`cloudflare.EdgeEndTimestamp` | `number` | None |
|`cloudflare.EdgePathingOp` | `string` | None |
|`cloudflare.EdgePathingSrc` | `string` | None |
|`cloudflare.EdgePathingStatus` | `string` | None |
|`cloudflare.EdgeRateLimitAction` | `string` | None |
|`cloudflare.EdgeRateLimitID` | `number` | None |
|`cloudflare.EdgeRequestHost` | `string` | None |
|`cloudflare.EdgeResponseBytes` | `number` | None |
|`cloudflare.EdgeResponseCompressionRatio` | `float` | None |
|`cloudflare.EdgeResponseContentType` | `string` | None |
|`cloudflare.EdgeResponseStatus` | `number` | None |
|`cloudflare.EdgeServerIP` | `string` | None |
|`cloudflare.EdgeStartTimestamp` | `number` | None |
|`cloudflare.FirewallMatchesActions` | `array` | None |
|`cloudflare.FirewallMatchesRuleIDs` | `array` | None |
|`cloudflare.FirewallMatchesSources` | `array` | None |
|`cloudflare.OriginIP` | `string` | None |
|`cloudflare.OriginResponseBytes` | `number` | None |
|`cloudflare.OriginResponseHTTPExpires` | `string` | None |
|`cloudflare.OriginResponseHTTPLastModified` | `string` | None |
|`cloudflare.OriginResponseStatus` | `number` | None |
|`cloudflare.OriginResponseTime` | `number` | None |
|`cloudflare.OriginSSLProtocol` | `string` | None |
|`cloudflare.ParentRayID` | `string` | None |
|`cloudflare.RayID` | `string` | None |
|`cloudflare.RequestHeaders` | `object` | None |
|`cloudflare.ResponseHeaders` | `object` | None |
|`cloudflare.SecurityLevel` | `string` | None |
|`cloudflare.WAFAction` | `string` | None |
|`cloudflare.WAFFlags` | `string` | None |
|`cloudflare.WAFMatchedVar` | `string` | None |
|`cloudflare.WAFProfile` | `string` | None |
|`cloudflare.WAFRuleID` | `string` | None |
|`cloudflare.WAFRuleMessage` | `string` | None |
|`cloudflare.WorkerCPUTime` | `number` | None |
|`cloudflare.WorkerStatus` | `string` | None |
|`cloudflare.WorkerSubrequest` | `bool` | None |
|`cloudflare.WorkerSubrequestCount` | `number` | None |
|`cloudflare.ZoneID` | `number` | None |
|`cloudflare.clientASNDescription` | `keyword` | None |
|`cloudflare.clientRequestQuery` | `keyword` | None |
|`cloudflare.matchIndex` | `numer` | None |
|`cloudflare.metadata` | `object` | None |
|`cloudflare.rayName` | `keyword` | None |
|`cloudflare.sampleInterval` | `number` | None |
|`cloudflare.source` | `keyword` | None |
|`destination.address` | `keyword` | Destination network address. |
|`event.action` | `keyword` | The action captured by the event. |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.bytes` | `long` | Total size in bytes of the response (body and headers). |
|`http.response.status_code` | `long` | HTTP response status code. |
|`network.protocol` | `keyword` | Application protocol name. |
|`rule.id` | `keyword` | Rule ID |
|`rule.ruleset` | `keyword` | Rule ruleset |
|`source.as.number` | `long` | Unique number allocated to the autonomous system. |
|`source.geo.country_name` | `keyword` | Country name. |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`tls.cipher` | `keyword` | String indicating the cipher used during the current connection. |
|`tls.version_protocol` | `keyword` | Normalized lowercase protocol name parsed from original string. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

