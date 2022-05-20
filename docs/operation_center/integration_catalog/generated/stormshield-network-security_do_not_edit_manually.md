
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | Stormshield Network Security can record traffic events flowing through their firewall. |
| `Network protocol analysis` | Stormshield Network Security firewall does traffic analysis at physical/data/transport layers. |
| `SSL/TLS inspection` | Stormshield Network Security firewall can perform SSL/TLS inspection to protect company network. |
| `Anti-virus` | Stormshield firewall can be configured to perfom malware analysis. |





In details, the following Table denotes the type of events produced by this integration.

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
        "@timestamp": "2022-03-17T13:49:51.000000Z",
        "destination": {
            "address": "11.22.33.44",
            "geo": {
                "continent_name": "na",
                "country_iso_code": "us"
            },
            "ip": "11.22.33.44",
            "port": 443
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "network",
            "duration": 0.0,
            "kind": "event",
            "outcome": "success",
            "risk_score": 5,
            "start": "2022-03-17T13:49:51.000000Z",
            "timezone": "+0100",
            "type": "connection"
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
        "message": "time=\"2022-03-17 14:49:51\" fw=\"SN12345678912345\" tz=+0100 startime=\"2022-03-17 14:49:51\" pri=5 confid=01 slotlevel=5 ruleid=48 srcif=\"Ethernet3\" srcifname=\"in\" ipproto=tcp dstif=\"Ethernet2\" dstifname=\"out\" proto=https src=55.66.77.88 srcport=39618 srcportname=ephemeral_fw_tcp srcname=MGDFS-Proxy-02 srcmac=00:00:00:00:00:00 dst=11.22.33.44 dstport=443 dstportname=https dstcontinent=\"na\" dstcountry=\"us\" ipv=4 sent=0 rcvd=0 duration=0.00 logtype=\"filter\"",
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
        "related": {
            "ip": [
                "11.22.33.44",
                "55.66.77.88"
            ]
        },
        "rule": {
            "category": "5",
            "id": "48"
        },
        "sekoiaio": {
            "entity": {
                "id": "jNZ0wDmv",
                "name": "w5gjMeE2rgO7n0CI",
                "uuid": "9a42db14-0072-4c5a-bd51-92f4cd060d96"
            },
            "intake": {
                "created": "2021-04-23T20:02:05.017771Z",
                "dialect": "sns",
                "dialect_uuid": "79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4",
                "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
                "parsing_status": "success"
            },
            "log": {
                "syslog": {
                    "facility": {
                        "code": "21",
                        "name": "local5"
                    },
                    "priority": "3",
                    "severity": {
                        "code": "3",
                        "name": "err"
                    }
                }
            }
        },
        "source": {
            "address": "55.66.77.88",
            "ip": "55.66.77.88",
            "mac": "00:00:00:00:00:00",
            "port": 39618
        },
        "stormshield": {
            "confid": 1,
            "dstportname": "https",
            "filter": {
                "action": "log"
            },
            "slotlevel": 5,
            "srcportname": "ephemeral_fw_tcp"
        }
    }
    	
	```


=== "filter.json"

    ```json
	
    {
        "source": {
            "address": "42.123.123.123",
            "ip": "42.123.123.123",
            "mac": "00:00:00:00:00:00",
            "port": 60355
        },
        "destination": {
            "address": "11.11.11.11",
            "ip": "11.11.11.11",
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
        "@timestamp": "2022-03-03T13:21:10.000000Z",
        "event": {
            "type": "connection",
            "kind": "event",
            "category": "network",
            "outcome": "success",
            "duration": 2000000000.0,
            "timezone": "+0100",
            "start": "2022-03-03T13:21:10.000000Z",
            "risk_score": 5
        },
        "rule": {
            "category": "2",
            "id": "100"
        }
    }
    	
	```


=== "filter2.json"

    ```json
	
    {
        "@timestamp": "2022-03-16T18:36:03.000000Z",
        "destination": {
            "address": "22",
            "geo": {
                "continent_name": "eu",
                "country_iso_code": "be"
            },
            "ip": "22",
            "port": 443
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": "network",
            "duration": 107331180000000.0,
            "kind": "event",
            "outcome": "success",
            "risk_score": 5,
            "start": "2022-03-03T13:21:10+00:00",
            "timezone": "+0100",
            "type": "connection"
        },
        "host": {
            "network": {
                "egress": {
                    "bytes": 2827291
                },
                "ingress": {
                    "bytes": 2728401
                }
            }
        },
        "message": "time=\"2022-03-16 19:36:03\" fw=\"SN12345678912345\" tz=+0100 startime=\"\" pri=5 confid=01 slotlevel=2 ruleid=103 srcif=\"Ethernet3\" srcifname=\"in\" ipproto=tcp dstif=\"Ethernet2\" dstifname=\"out\" proto=https src=11.11.11.11 srcport=49586 srcportname=ephemeral_fw_tcp srcname=foo_bar srcmac=00:00:00:00:00:00 srccontinent=\"na\" srccountry=\"us\" dst=22.22.22.22 dstport=443 dstportname=https dstcontinent=\"eu\" dstcountry=\"be\" modsrc=11.11.11.11 modsrcport=49586 origdst=22.22.22.22 origdstport=443 ipv=4 sent=2827291 rcvd=2728401 duration=107331.18 action=pass logtype=\"connection\"",
        "network": {
            "bytes": 5555692,
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
        "related": {
            "ip": [
                "11.11.11.11",
                "22"
            ]
        },
        "rule": {
            "category": "2",
            "id": "103"
        },
        "sekoiaio": {
            "entity": {
                "id": "jNZ0wDmv",
                "name": "w5gjMeE2rgO7n0CI",
                "uuid": "9a42db14-0072-4c5a-bd51-92f4cd060d96"
            },
            "intake": {
                "created": "2021-04-23T20:02:05.017771Z",
                "dialect": "sns",
                "dialect_uuid": "79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4",
                "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430",
                "parsing_status": "success"
            },
            "log": {
                "syslog": {
                    "facility": {
                        "code": "21",
                        "name": "local5"
                    },
                    "priority": "3",
                    "severity": {
                        "code": "3",
                        "name": "err"
                    }
                }
            }
        },
        "source": {
            "address": "11.11.11.11",
            "geo": {
                "continent_name": "na",
                "country_iso_code": "us"
            },
            "ip": "11.11.11.11",
            "mac": "00:00:00:00:00:00",
            "port": 49586
        },
        "stormshield": {
            "confid": 1,
            "dstportname": "https",
            "filter": {
                "action": "pass"
            },
            "slotlevel": 2,
            "srcportname": "ephemeral_fw_tcp"
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
|`stormshield.dstname` | `keyword` | None |
|`stormshield.dstportname` | `keyword` | None |
|`stormshield.filter.action` | `keyword` | None |
|`stormshield.logtype` | `keyword` | None |
|`stormshield.scirep` | `keyword` |  |
|`stormshield.slotlevel` | `float` | None |
|`stormshield.srcportname` | `keyword` | None |

