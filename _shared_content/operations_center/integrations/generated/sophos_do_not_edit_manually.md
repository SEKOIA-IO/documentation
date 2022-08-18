
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | IPS logs and firewall logs are examined in detail |
| `Network protocol analysis` | ICMP, TCP and UDP packets are fully analyzed |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "url.json"

    ```json
	
    {
        "event": {
            "category": "network",
            "kind": "event"
        },
        "action": {
            "name": "allow"
        },
        "destination": {
            "bytes": 4563,
            "domain": "www.google.com",
            "ip": "216.58.203.100",
            "port": 80
        },
        "log": {
            "level": "Information"
        },
        "network": {
            "transport": "TCP"
        },
        "observer": {
            "name": "SG330"
        },
        "sophos": {
            "log_subtype": "Allowed"
        },
        "source": {
            "address": "10.0.5.23",
            "bytes": 310,
            "ip": "10.0.5.23",
            "port": 56332
        },
        "url": {
            "original": "http://www.google.com/dl/release2/TnV3rQKAz82ODPFMuxq1wQ_1089/f9YORelAF3Z1VnI84ysPJA"
        },
        "user": {
            "name": "b.orowi@cci.adds"
        }
    }
    	
	```


=== "utm_accept.json"

    ```json
	
    {
        "sophos": {
            "action": "accept",
            "sub": "packetfilter"
        },
        "event": {
            "category": "network",
            "kind": "event"
        },
        "destination": {
            "address": "8.8.8.8",
            "ip": "8.8.8.8",
            "mac": "00:1a:8c:f0:3f:a4",
            "port": 53
        },
        "source": {
            "address": "10.1.0.10",
            "ip": "10.1.0.10",
            "mac": "f8:0f:6f:9c:5e:2d",
            "port": 51208
        }
    }
    	
	```


=== "utm_dns.json"

    ```json
	
    {
        "event": {
            "category": "network",
            "kind": "event",
            "outcome": "success"
        },
        "sophos": {
            "action": "DNS request",
            "sub": "packetfilter"
        },
        "destination": {
            "ip": "8.8.8.8",
            "mac": "00:1a:8c:f0:3f:a4",
            "port": 53
        },
        "source": {
            "ip": "10.1.0.10",
            "mac": "f8:0f:6f:9c:5e:2d",
            "port": 51208
        }
    }
    	
	```


=== "utm_drop.json"

    ```json
	
    {
        "event": {
            "category": "network",
            "kind": "event",
            "outcome": "success",
            "type": "drop"
        },
        "destination": {
            "ip": "133.222.233.233",
            "mac": "00:1a:8c:g0:62:69",
            "port": 52938
        },
        "sophos": {
            "action": "drop",
            "sub": "packetfilter"
        },
        "source": {
            "ip": "103.188.113.55",
            "mac": "d8:94:03:g6:cd:27",
            "port": 54040
        }
    }
    	
	```


=== "xg_allow.json"

    ```json
	
    {
        "destination": {
            "address": "195.35.245.30",
            "bytes": 0,
            "ip": "195.35.245.30",
            "nat": {
                "port": 0
            },
            "packets": 0,
            "port": 62384
        },
        "log": {
            "level": "Information"
        },
        "event": {
            "category": "network",
            "kind": "event"
        },
        "action": {
            "name": "allow"
        },
        "network": {
            "transport": "UDP"
        },
        "observer": {
            "name": "SG330"
        },
        "sophos": {
            "log_subtype": "Allowed",
            "status": "Allow"
        },
        "source": {
            "address": "10.0.215.3",
            "bytes": 0,
            "ip": "10.0.215.3",
            "mac": "00:00:00:00:00:00",
            "nat": {
                "ip": "61.5.213.97",
                "port": 0
            },
            "packets": 0,
            "port": 38413
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.bytes` | `long` | Bytes sent from the destination to the source. |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.mac` | `keyword` | MAC address of the destination. |
|`destination.nat.ip` | `ip` | Destination NAT ip |
|`destination.nat.port` | `long` | Destination NAT Port |
|`destination.packets` | `long` | Packets sent from the destination to the source. |
|`destination.port` | `long` | Port of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`http.response.status_code` | `long` | HTTP response status code. |
|`log.level` | `keyword` | Log level of the log event. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`observer.name` | `keyword` | Custom name of the observer. |
|`sophos.action` | `keyword` | None |
|`sophos.log_subtype` | `keyword` | None |
|`sophos.status` | `keyword` | None |
|`sophos.sub` | `keyword` | None |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |
|`source.nat.ip` | `ip` | Source NAT ip |
|`source.nat.port` | `long` | Source NAT port |
|`source.packets` | `long` | Packets sent from the source to the destination. |
|`source.port` | `long` | Port of the source. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`url.query` | `keyword` | Query string of the request. |
|`user.group.name` | `keyword` | Name of the group. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

