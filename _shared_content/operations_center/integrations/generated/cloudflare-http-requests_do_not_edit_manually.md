
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web logs` | Cloudflare act as a proxy and provide associated traffic logs |
| `Web application firewall logs` | Cloudflare protect web application with its web application firewall and provide associated traffic logs |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `web` |
| Type | `access` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "http.json"

    ```json
	
    {
        "event": {
            "category": [
                "web"
            ],
            "dataset": "http_requests",
            "end": "2022-07-20T01:48:22.371000Z",
            "kind": "event",
            "outcome": "success",
            "start": "2022-07-20T01:47:51.671000Z",
            "type": [
                "access"
            ]
        },
        "source": {
            "ip": "34.142.121.18",
            "address": "34.142.121.18"
        },
        "destination": {
            "address": "foo-bar-baz.xyz"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "bytes": 279,
                "status_code": 522
            }
        },
        "url": {
            "path": "/wp1/wp-includes/wlwmanifest.xml"
        },
        "cloudflare": {
            "ClientIP": "34.142.121.18",
            "ClientRequestHost": "foo-bar-baz.xyz",
            "ClientRequestMethod": "GET",
            "ClientRequestURI": "/wp1/wp-includes/wlwmanifest.xml",
            "EdgeEndTimestamp": "1658281702371000000",
            "EdgeResponseBytes": 279,
            "EdgeResponseStatus": 522,
            "EdgeStartTimestamp": "1658281671671000000",
            "RayID": "72d807ffeba5753d"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "ip": [
                "34.142.121.18"
            ]
        }
    }
    	
	```


=== "http2.json"

    ```json
	
    {
        "event": {
            "category": [
                "web"
            ],
            "dataset": "http_requests",
            "kind": "event",
            "outcome": "success",
            "type": [
                "access"
            ]
        },
        "cloudflare": {
            "WAFMatchedVar": "",
            "WAFProfile": "unknown",
            "WAFRuleID": "",
            "WAFRuleMessage": "",
            "WorkerCPUTime": 0,
            "WorkerStatus": "unknown",
            "WorkerSubrequest": false,
            "WorkerSubrequestCount": 0,
            "ZoneID": 545468107,
            "ZoneName": "foo-bar-baz.xyz"
        },
        "ecs": {
            "version": "1.10.0"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.address` | `keyword` | Destination network address. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
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

