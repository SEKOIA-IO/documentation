
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
        "message": "DHCPACK on 10.100.102.108 to 6c:88:14:1d:97:1c (PDB746) via 10.100.100.4",
        "event": {
            "kind": "event",
            "category": "network",
            "type": "connection"
        },
        "dhcpd": {
            "query": "ack"
        },
        "source": {
            "ip": "10.100.102.108",
            "mac": "6c:88:14:1d:97:1c",
            "domain": "PDB746",
            "address": "PDB746"
        },
        "destination": {
            "ip": "10.100.100.4",
            "address": "10.100.100.4"
        },
        "related": {
            "ip": [
                "10.100.100.4",
                "10.100.102.108"
            ],
            "hosts": [
                "PDB746"
            ]
        }
    }
    	
	```


=== "discover.json"

    ```json
	
    {
        "message": "DHCPDISCOVER from ac:cc:8e:b0:2b:8c via 192.168.102.7: network 192.168.102.0/23: no free leases",
        "event": {
            "kind": "event",
            "category": "network",
            "type": "connection"
        },
        "dhcpd": {
            "query": "discover"
        },
        "source": {
            "mac": "ac:cc:8e:b0:2b:8c"
        },
        "destination": {
            "ip": "192.168.102.7",
            "address": "192.168.102.7"
        },
        "related": {
            "ip": [
                "192.168.102.7"
            ]
        }
    }
    	
	```


=== "release.json"

    ```json
	
    {
        "message": "DHCPRELEASE of 10.17.81.182 from 00:08:5d:71:92:15 (6867i00085D719105) via enp4s0f0 (found)",
        "event": {
            "kind": "event",
            "category": "network",
            "type": "connection"
        },
        "dhcpd": {
            "query": "release"
        },
        "source": {
            "ip": "10.17.81.182",
            "mac": "00:08:5d:71:92:15",
            "domain": "6867i00085D719105",
            "address": "6867i00085D719105"
        },
        "related": {
            "hosts": [
                "6867i00085D719105"
            ],
            "ip": [
                "10.17.81.182"
            ]
        }
    }
    	
	```


=== "request.json"

    ```json
	
    {
        "message": "DHCPREQUEST for 10.100.102.108 from 6c:88:14:1d:96:0c (PDB746) via 10.100.100.4",
        "event": {
            "kind": "event",
            "category": "network",
            "type": "connection"
        },
        "dhcpd": {
            "query": "request"
        },
        "source": {
            "ip": "10.100.102.108",
            "mac": "6c:88:14:1d:96:0c",
            "domain": "PDB746",
            "address": "PDB746"
        },
        "destination": {
            "ip": "10.100.100.4",
            "address": "10.100.100.4"
        },
        "related": {
            "ip": [
                "10.100.100.4",
                "10.100.102.108"
            ],
            "hosts": [
                "PDB746"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`destination.ip` | `ip` | IP address of the destination. |
|`dhcpd.query` | `keyword` | name of the DHCP query |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`source.domain` | `keyword` | The domain name of the source. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |

