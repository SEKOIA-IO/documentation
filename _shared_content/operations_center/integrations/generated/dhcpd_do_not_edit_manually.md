
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device configuration` | logs include IP configuration of network devices in your networks |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `connection` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "ack.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
            "category": "network",
            "kind": "event",
            "type": "connection"
        },
        "dhcpd": {
            "query": "ack"
        },
        "destination": {
            "ip": "10.100.100.4"
        },
        "source": {
            "ip": "10.100.102.108",
            "address": "PDB746",
            "domain": "PDB746",
            "mac": "6c:88:14:1d:97:1c"
        }
    }
    	
	```


=== "discover.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
            "category": "network",
            "kind": "event",
            "type": "connection"
        },
        "dhcpd": {
            "query": "discover"
        },
        "destination": {
            "ip": "192.168.102.7"
        },
        "source": {
            "mac": "ac:cc:8e:b0:2b:8c"
        }
    }
    	
	```


=== "release.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
            "category": "network",
            "kind": "event",
            "type": "connection"
        },
        "dhcpd": {
            "query": "release"
        },
        "source": {
            "ip": "10.17.81.182",
            "mac": "00:08:5d:71:92:15",
            "domain": "6867i00085D719105"
        }
    }
    	
	```


=== "request.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
            "category": "network",
            "kind": "event",
            "type": "connection"
        },
        "dhcpd": {
            "query": "request"
        },
        "source": {
            "ip": "10.100.102.108",
            "mac": "6c:88:14:1d:96:0c",
            "domain": "PDB746"
        },
        "destination": {
            "ip": "10.100.100.4"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.ip` | `ip` | IP address of the destination. |
|`dhcpd.query` | `keyword` | None |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`source.domain` | `keyword` | The domain name of the source. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |

