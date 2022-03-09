
## Event Categories




In details, the following Table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `connection` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "filter.json"

    ```json
	
    {
        "source": {
            "address": "42.123.123.123",
            "ip": "42.123.123.123",
            "mac": "00:5e:6f:3q:78:30",
            "port": 60355
        },
        "destination": {
            "address": "424.321.123.42",
            "ip": "424.321.123.42",
            "port": 443,
            "geo": {
                "continent_name": "na",
                "country_iso_code": "us"
            }
        },
        "host": {
            "network": {
                "egress": {
                    "bytes": 0
                },
                "ingress": {
                    "bytes": 0
                }
            }
        },
        "network": {
            "bytes": 0,
            "protocol": "https",
            "transport": "tcp",
            "type": "4"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "out",
                    "name": "Ethernet2"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "in",
                    "name": "Ethernet3"
                }
            },
            "serial_number": "SN12345678912345"
        },
        "stormshield": {
            "confid": 1,
            "dstname": "example_dest",
            "dstportname": "https",
            "filter": {
                "action": "pass"
            },
            "slotlevel": 2,
            "srcportname": "ad2009-dyn_tcp"
        },
        "@timestamp": "2022-03-03 14:21:10",
        "event": {
            "type": "connection",
            "kind": "event",
            "category": "network",
            "outcome": "success",
            "duration": 2000000000.0,
            "timezone": "+0100",
            "start": "2022-03-03 14:21:10",
            "risk_score": 5
        },
        "rule": {
            "category": "2",
            "id": "100"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.geo.continent_name` | `keyword` | Name of the continent. |
|`destination.geo.country_iso_code` | `keyword` | Country ISO code. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.risk_score` | `float` | Risk score or priority of the event (e.g. security solutions). Use your system's original value here. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.timezone` | `keyword` | Event time zone. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`host.network.egress.bytes` | `long` | The number of bytes sent on all network interfaces. |
|`host.network.ingress.bytes` | `long` | The number of bytes received on all network interfaces. |
|`network.bytes` | `long` | Total bytes transferred in both directions. |
|`network.protocol` | `keyword` | Application protocol name. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`network.type` | `keyword` | In the OSI Model this would be the Network Layer. ipv4, ipv6, ipsec, pim, etc |
|`observer.egress.interface.alias` | `keyword` | Interface alias |
|`observer.egress.interface.name` | `keyword` | Interface name |
|`observer.ingress.interface.alias` | `keyword` | Interface alias |
|`observer.ingress.interface.name` | `keyword` | Interface name |
|`observer.serial_number` | `keyword` | Observer serial number. |
|`rule.category` | `keyword` | Rule category |
|`rule.id` | `keyword` | Rule ID |
|`source.geo.continent_name` | `keyword` | Name of the continent. |
|`source.geo.country_iso_code` | `keyword` | Country ISO code. |
|`source.ip` | `ip` | IP address of the source. |
|`source.mac` | `keyword` | MAC address of the source. |
|`source.port` | `long` | Port of the source. |
|`stormshield.confid` | `float` | None |
|`stormshield.dstname` | `text` | None |
|`stormshield.dstportname` | `text` | None |
|`stormshield.filter.action` | `keyword` | None |
|`stormshield.logtype` | `text` | None |
|`stormshield.slotlevel` | `float` | None |
|`stormshield.srcportname` | `text` | None |

