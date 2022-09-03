
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `DNS records` | Cloudflare DNS logs provides detailed logs on handled DNS queries |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "dns_type_1.json"

    ```json
	
    {
        "@timestamp": "2022-07-07T22:42:06.004000Z",
        "dns": {
            "question": {
                "name": "foO-BAR-baz.xYz",
                "type": "A"
            },
            "response_code": "NoError"
        },
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "dataset": "dns_logs"
        }
    }
    	
	```


=== "dns_type_2.json"

    ```json
	
    {
        "@timestamp": "2022-07-07T22:42:06.004000Z",
        "dns": {
            "question": {
                "name": "foO-BAR-baz.xYz",
                "type": "NS"
            },
            "response_code": "NoError"
        },
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "dataset": "dns_logs"
        }
    }
    	
	```


=== "dns_type_28.json"

    ```json
	
    {
        "@timestamp": "2022-07-07T22:42:06.004000Z",
        "dns": {
            "question": {
                "name": "foO-BAR-baz.xYz",
                "type": "AAAA"
            },
            "response_code": "NoError"
        },
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "dataset": "dns_logs"
        }
    }
    	
	```


=== "dns_type_65535.json"

    ```json
	
    {
        "@timestamp": "2022-07-07T22:42:06.004000Z",
        "dns": {
            "question": {
                "name": "foO-BAR-baz.xYz"
            },
            "response_code": "NoError"
        },
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "dataset": "dns_logs"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cloudflare.ColoCode` | `keyword` | IATA airport code of data center that received the request |
|`cloudflare.EDNSSubnet` | `keyword` | EDNS Client Subnet (IPv4 or IPv6) |
|`cloudflare.EDNSSubnetLength` | `number` | EDNS Client Subnet length |
|`cloudflare.ResponseCached` | `bool` | Whether the response was cached or not |
|`dns.question.name` | `keyword` | The name being queried. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`source.ip` | `ip` | IP address of the source. |

