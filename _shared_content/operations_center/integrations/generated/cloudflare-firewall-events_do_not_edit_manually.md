
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Web application firewall logs` | Cloudflare protect web application with its web application firewall |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "403.json"

    ```json
	
    {
        "@timestamp": "2022-07-12T12:57:06.219000Z",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "denied"
            ],
            "action": "block",
            "dataset": "firewall-events"
        },
        "source": {
            "ip": "113.206.179.28",
            "address": "113.206.179.28"
        },
        "destination": {
            "address": "foo-bar-baz.xyz",
            "domain": "foo-bar-baz.xyz",
            "registered_domain": "foo-bar-baz.xyz",
            "top_level_domain": "xyz"
        },
        "http": {
            "request": {
                "method": "GET"
            },
            "response": {
                "status_code": 403
            }
        },
        "url": {
            "domain": "foo-bar-baz.xyz",
            "path": "/static/favicon.ico",
            "registered_domain": "foo-bar-baz.xyz",
            "top_level_domain": "xyz"
        },
        "related": {
            "hosts": [
                "foo-bar-baz.xyz"
            ],
            "ip": [
                "113.206.179.28"
            ]
        },
        "cloudflare": {
            "RayID": "7299f155dda47d6b",
            "EdgeResponseStatus": 403
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cloudflare.ClientIPClass` | `string` | None |
|`cloudflare.ClientRefererHost` | `string` | None |
|`cloudflare.ClientRefererPath` | `string` | None |
|`cloudflare.ClientRefererQuery` | `string` | None |
|`cloudflare.ClientRefererScheme` | `string` | None |
|`cloudflare.EdgeColoCode` | `string` | None |
|`cloudflare.EdgeResponseStatus` | `number` | None |
|`cloudflare.Kind` | `string` | None |
|`cloudflare.OriginResponseStatus` | `number` | None |
|`cloudflare.OriginatorRayID` | `string` | None |
|`cloudflare.RayID` | `string` | None |
|`cloudflare.clientASNDescription` | `keyword` | None |
|`cloudflare.matchIndex` | `number` | None |
|`cloudflare.metadata` | `object` | None |
|`cloudflare.source` | `keyword` | None |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`http.request.bytes` | `long` | Total size in bytes of the request (body and headers). |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`http.version` | `keyword` | HTTP version. |
|`network.protocol` | `keyword` | Application protocol name. |
|`rule.id` | `keyword` | Rule ID |
|`rule.ruleset` | `keyword` | Rule ruleset |
|`source.as.number` | `long` | Unique number allocated to the autonomous system. |
|`source.geo.country_name` | `keyword` | Country name. |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`tls.cipher` | `keyword` | String indicating the cipher used during the current connection. |
|`tls.version_protocol` | `keyword` | Normalized lowercase protocol name parsed from original string. |
|`url.domain` | `keyword` | Domain of the url. |
|`url.path` | `wildcard` | Path of the request, such as "/search". |
|`url.query` | `keyword` | Query string of the request. |
|`url.scheme` | `keyword` | Scheme of the url. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

