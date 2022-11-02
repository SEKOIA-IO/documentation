
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
        "message": "{\"QueryName\":\"foO-BAR-baz.xYz.\",\"QueryType\":1,\"ResponseCode\":0,\"Timestamp\":1657233726004000000}\n",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "dataset": "dns_logs"
        },
        "@timestamp": "2022-07-07T22:42:06.004000Z",
        "dns": {
            "question": {
                "name": "foO-BAR-baz.xYz",
                "type": "A",
                "top_level_domain": "xYz",
                "registered_domain": "foO-BAR-baz.xYz"
            },
            "response_code": "NoError"
        }
    }
    	
	```


=== "dns_type_2.json"

    ```json
	
    {
        "message": "{\"QueryName\":\"foO-BAR-baz.xYz.\",\"QueryType\":2,\"ResponseCode\":0,\"Timestamp\":1657233726004000000}\n",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "dataset": "dns_logs"
        },
        "@timestamp": "2022-07-07T22:42:06.004000Z",
        "dns": {
            "question": {
                "name": "foO-BAR-baz.xYz",
                "type": "NS",
                "top_level_domain": "xYz",
                "registered_domain": "foO-BAR-baz.xYz"
            },
            "response_code": "NoError"
        }
    }
    	
	```


=== "dns_type_28.json"

    ```json
	
    {
        "message": "{\"QueryName\":\"foO-BAR-baz.xYz.\",\"QueryType\":28,\"ResponseCode\":0,\"Timestamp\":1657233726004000000}\n",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "dataset": "dns_logs"
        },
        "@timestamp": "2022-07-07T22:42:06.004000Z",
        "dns": {
            "question": {
                "name": "foO-BAR-baz.xYz",
                "type": "AAAA",
                "top_level_domain": "xYz",
                "registered_domain": "foO-BAR-baz.xYz"
            },
            "response_code": "NoError"
        }
    }
    	
	```


=== "dns_type_65535.json"

    ```json
	
    {
        "message": "{\"QueryName\":\"foO-BAR-baz.xYz.\",\"QueryType\":65353,\"ResponseCode\":0,\"Timestamp\":1657233726004000000}\n",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "dataset": "dns_logs"
        },
        "@timestamp": "2022-07-07T22:42:06.004000Z",
        "dns": {
            "question": {
                "name": "foO-BAR-baz.xYz",
                "top_level_domain": "xYz",
                "registered_domain": "foO-BAR-baz.xYz"
            },
            "response_code": "NoError"
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

