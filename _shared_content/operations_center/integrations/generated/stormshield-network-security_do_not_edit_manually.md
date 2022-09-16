
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | Stormshield Network Security can record traffic events flowing through their firewall. |
| `Network protocol analysis` | Stormshield Network Security firewall does traffic analysis at physical/data/transport layers. |
| `SSL/TLS inspection` | Stormshield Network Security firewall can perform SSL/TLS inspection to protect company network. |
| `Anti-virus` | Stormshield firewall can be configured to perfom malware analysis. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `network` |
| Type | `connection` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "empty_action.json"

    ```json
	
    {
        "message": "time=\"2022-03-17 14:49:51\" fw=\"SN12345678912345\" tz=+0100 startime=\"2022-03-17 14:49:51\" pri=5 confid=01 slotlevel=5 ruleid=48 srcif=\"Ethernet3\" srcifname=\"in\" ipproto=tcp dstif=\"Ethernet2\" dstifname=\"out\" proto=https src=55.66.77.88 srcport=39618 srcportname=ephemeral_fw_tcp srcname=MGDFS-Proxy-02 srcmac=00:00:00:00:00:00 dst=11.22.33.44 dstport=443 dstportname=https dstcontinent=\"na\" dstcountry=\"us\" ipv=4 sent=0 rcvd=0 duration=0.00 logtype=\"filter\"",
        "event": {
            "start": "2022-03-17T13:49:51.000000Z",
            "kind": "event",
            "category": "network",
            "type": "connection",
            "timezone": "+0100",
            "risk_score": 5,
            "duration": 0.0
        },
        "stormshield": {
            "logtype": "filter",
            "dstportname": "https",
            "srcportname": "ephemeral_fw_tcp",
            "slotlevel": 5,
            "confid": 1
        },
        "@timestamp": "2022-03-17T13:49:51.000000Z",
        "observer": {
            "serial_number": "SN12345678912345",
            "ingress": {
                "interface": {
                    "name": "Ethernet3",
                    "alias": "in"
                }
            },
            "egress": {
                "interface": {
                    "name": "Ethernet2",
                    "alias": "out"
                }
            }
        },
        "network": {
            "transport": "tcp",
            "bytes": 0,
            "protocol": "https",
            "type": "4"
        },
        "source": {
            "ip": "55.66.77.88",
            "port": 39618,
            "mac": "00:00:00:00:00:00",
            "address": "55.66.77.88"
        },
        "destination": {
            "ip": "11.22.33.44",
            "port": 443,
            "geo": {
                "continent_name": "na",
                "country_iso_code": "us"
            },
            "address": "11.22.33.44"
        },
        "host": {
            "network": {
                "ingress": {
                    "bytes": 0
                },
                "egress": {
                    "bytes": 0
                }
            }
        },
        "rule": {
            "id": "48",
            "category": "5"
        },
        "related": {
            "ip": [
                "11.22.33.44",
                "55.66.77.88"
            ]
        }
    }
    	
	```


=== "filter.json"

    ```json
	
    {
        "message": "time=\"2022-03-03 14:21:10\" fw=\"SN12345678912345\" tz=+0100 startime=\"2022-03-03 14:21:10\" pri=5 confid=01 slotlevel=2 ruleid=100 srcif=\"Ethernet3\" srcifname=\"in\" ipproto=tcp dstif=\"Ethernet2\" dstifname=\"out\" proto=https src=42.123.123.123 srcport=60355 srcportname=ad2009-dyn_tcp srcname=DLEM-AMPD02 srcmac=00:00:00:00:00:00 dst=11.11.11.11 dstport=443 dstportname=https dstname=example_dest dstcontinent=\"na\" dstcountry=\"us\" ipv=4 sent=0 rcvd=0 duration=2.00 action=pass logtype=\"filter\"",
        "event": {
            "start": "2022-03-03T13:21:10.000000Z",
            "kind": "event",
            "category": "network",
            "type": "connection",
            "timezone": "+0100",
            "risk_score": 5,
            "duration": 2000000000.0
        },
        "stormshield": {
            "logtype": "filter",
            "dstname": "example_dest",
            "dstportname": "https",
            "srcportname": "ad2009-dyn_tcp",
            "slotlevel": 2,
            "confid": 1,
            "filter": {
                "action": "pass"
            }
        },
        "@timestamp": "2022-03-03T13:21:10.000000Z",
        "observer": {
            "serial_number": "SN12345678912345",
            "ingress": {
                "interface": {
                    "name": "Ethernet3",
                    "alias": "in"
                }
            },
            "egress": {
                "interface": {
                    "name": "Ethernet2",
                    "alias": "out"
                }
            }
        },
        "network": {
            "transport": "tcp",
            "bytes": 0,
            "protocol": "https",
            "type": "4"
        },
        "source": {
            "ip": "42.123.123.123",
            "port": 60355,
            "mac": "00:00:00:00:00:00",
            "address": "42.123.123.123"
        },
        "destination": {
            "ip": "11.11.11.11",
            "port": 443,
            "geo": {
                "continent_name": "na",
                "country_iso_code": "us"
            },
            "address": "11.11.11.11"
        },
        "host": {
            "network": {
                "ingress": {
                    "bytes": 0
                },
                "egress": {
                    "bytes": 0
                }
            }
        },
        "rule": {
            "id": "100",
            "category": "2"
        },
        "related": {
            "ip": [
                "11.11.11.11",
                "42.123.123.123"
            ]
        }
    }
    	
	```


=== "filter2.json"

    ```json
	
    {
        "message": "time=\"2022-03-16 19:36:03\" fw=\"SN12345678912345\" tz=+0100 startime=\"\" pri=5 confid=01 slotlevel=2 ruleid=103 srcif=\"Ethernet3\" srcifname=\"in\" ipproto=tcp dstif=\"Ethernet2\" dstifname=\"out\" proto=https src=11.11.11.11 srcport=49586 srcportname=ephemeral_fw_tcp srcname=foo_bar srcmac=00:00:00:00:00:00 srccontinent=\"na\" srccountry=\"us\" dst=22.22.22.22 dstport=443 dstportname=https dstcontinent=\"eu\" dstcountry=\"be\" modsrc=11.11.11.11 modsrcport=49586 origdst=22.22.22.22 origdstport=443 ipv=4 sent=2827291 rcvd=2728401 duration=107331.18 action=pass logtype=\"connection\"",
        "event": {
            "kind": "event",
            "category": "network",
            "type": "connection",
            "timezone": "+0100",
            "risk_score": 5,
            "duration": 107331180000000.0
        },
        "stormshield": {
            "logtype": "connection",
            "dstportname": "https",
            "srcportname": "ephemeral_fw_tcp",
            "slotlevel": 2,
            "confid": 1,
            "filter": {
                "action": "pass"
            }
        },
        "@timestamp": "2022-03-16T18:36:03.000000Z",
        "observer": {
            "serial_number": "SN12345678912345",
            "ingress": {
                "interface": {
                    "name": "Ethernet3",
                    "alias": "in"
                }
            },
            "egress": {
                "interface": {
                    "name": "Ethernet2",
                    "alias": "out"
                }
            }
        },
        "network": {
            "transport": "tcp",
            "bytes": 5555692,
            "protocol": "https",
            "type": "4"
        },
        "source": {
            "ip": "11.11.11.11",
            "port": 49586,
            "mac": "00:00:00:00:00:00",
            "geo": {
                "continent_name": "na",
                "country_iso_code": "us"
            },
            "address": "11.11.11.11"
        },
        "destination": {
            "ip": "22.22.22.22",
            "port": 443,
            "geo": {
                "continent_name": "eu",
                "country_iso_code": "be"
            },
            "address": "22.22.22.22"
        },
        "host": {
            "network": {
                "ingress": {
                    "bytes": 2728401
                },
                "egress": {
                    "bytes": 2827291
                }
            }
        },
        "rule": {
            "id": "103",
            "category": "2"
        },
        "related": {
            "ip": [
                "11.11.11.11",
                "22.22.22.22"
            ]
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
|`stormshield.filter.action` | `keyword` | The action asociated to the filter rule |

