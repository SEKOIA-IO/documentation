
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
        "message": "device=\"SFW\" date=2020-05-16 time=02:54:39 timezone=\"+11\" device_name=\"SG330\" device_id=S3105611453B86C log_id=050901616001 log_type=\"Content Filtering\" log_component=\"HTTP\" log_subtype=\"Allowed\" status=\"\" priority=Information fw_rule_id=6 user_name=\"b.orowi@cci.adds\" user_gp=\"CCI - Proxy - Filtrage All\u00e9g\u00e9\" iap=13 category=\"Search Engines\" category_type=\"Acceptable\" url=\"http://www.google.com/dl/release2/TnV3rQKAz82ODPFMuxq1wQ_1089/f9YORelAF3Z1VnI84ysPJA\" contenttype=\"application/octet-stream\" override_token=\"\" httpresponsecode=\"\" src_ip=10.0.5.23 dst_ip=216.58.203.100 protocol=\"TCP\" src_port=56332 dst_port=80 sent_bytes=310 recv_bytes=4563 domain=www.google.com exceptions=\"\" activityname=\"\" reason=\"\" user_agent=\"Microsoft BITS/7.8\" status_code=\"416\" transactionid=\"\" referer=\"\" download_file_name=\"\" download_file_type=\"\" upload_file_name=\"\" upload_file_type=\"\" con_id=484085624 application=\"\" app_is_cloud=0 override_name=\"\" override_authorizer=\"\"",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ]
        },
        "log": {
            "level": "Information"
        },
        "observer": {
            "name": "SG330"
        },
        "sophos": {
            "log_subtype": "Allowed"
        },
        "url": {
            "original": "http://www.google.com/dl/release2/TnV3rQKAz82ODPFMuxq1wQ_1089/f9YORelAF3Z1VnI84ysPJA",
            "domain": "www.google.com",
            "top_level_domain": "com",
            "subdomain": "www",
            "registered_domain": "google.com",
            "scheme": "http",
            "path": "/dl/release2/TnV3rQKAz82ODPFMuxq1wQ_1089/f9YORelAF3Z1VnI84ysPJA",
            "port": 80
        },
        "source": {
            "bytes": 310,
            "ip": "10.0.5.23",
            "port": 56332,
            "address": "10.0.5.23"
        },
        "destination": {
            "bytes": 4563,
            "domain": "www.google.com",
            "ip": "216.58.203.100",
            "port": 80,
            "address": "www.google.com",
            "top_level_domain": "com",
            "subdomain": "www",
            "registered_domain": "google.com"
        },
        "network": {
            "transport": "TCP"
        },
        "user": {
            "name": "b.orowi@cci.adds"
        },
        "action": {
            "name": "allow"
        },
        "related": {
            "hosts": [
                "www.google.com"
            ],
            "ip": [
                "10.0.5.23",
                "216.58.203.100"
            ],
            "user": [
                "b.orowi@cci.adds"
            ]
        }
    }
    	
	```


=== "utm_accept.json"

    ```json
	
    {
        "message": "id=\"2002\" severity=\"info\" sys=\"SecureNet\" sub=\"packetfilter\" name=\"Packet accepted\" action=\"accept\" fwrule=\"20\" initf=\"lag1.600\" outitf=\"eth1\" srcmac=\"f8:0f:6f:9c:5e:2d\" dstmac=\"00:1a:8c:f0:3f:a4\" srcip=\"10.1.0.10\" dstip=\"8.8.8.8\" proto=\"17\" length=\"103\" tos=\"0x00\" prec=\"0x00\" ttl=\"127\" srcport=\"51208\" dstport=\"53\"",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ]
        },
        "sophos": {
            "action": "accept",
            "sub": "packetfilter"
        },
        "source": {
            "mac": "f8:0f:6f:9c:5e:2d",
            "ip": "10.1.0.10",
            "port": 51208,
            "address": "10.1.0.10"
        },
        "destination": {
            "mac": "00:1a:8c:f0:3f:a4",
            "ip": "8.8.8.8",
            "port": 53,
            "address": "8.8.8.8"
        },
        "related": {
            "ip": [
                "10.1.0.10",
                "8.8.8.8"
            ]
        }
    }
    	
	```


=== "utm_dns.json"

    ```json
	
    {
        "message": "id=\"2014\" severity=\"info\" sys=\"SecureNet\" sub=\"packetfilter\" name=\"DNS request\" action=\"DNS request\" fwrule=\"60011\" initf=\"lag1.600\" srcmac=\"f8:0f:6f:9c:5e:2d\" dstmac=\"00:1a:8c:f0:3f:a4\" srcip=\"10.1.0.10\" dstip=\"8.8.8.8\" proto=\"17\" length=\"103\" tos=\"0x00\" prec=\"0x00\" ttl=\"128\" srcport=\"51208\" dstport=\"53\"",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ]
        },
        "sophos": {
            "action": "DNS request",
            "sub": "packetfilter"
        },
        "source": {
            "mac": "f8:0f:6f:9c:5e:2d",
            "ip": "10.1.0.10",
            "port": 51208,
            "address": "10.1.0.10"
        },
        "destination": {
            "mac": "00:1a:8c:f0:3f:a4",
            "ip": "8.8.8.8",
            "port": 53,
            "address": "8.8.8.8"
        },
        "related": {
            "ip": [
                "10.1.0.10",
                "8.8.8.8"
            ]
        }
    }
    	
	```


=== "utm_drop.json"

    ```json
	
    {
        "message": "id=\"2001\" severity=\"info\" sys=\"SecureNet\" sub=\"packetfilter\" name=\"Packet dropped\" action=\"drop\" fwrule=\"60002\" initf=\"eth1\" outitf=\"eth1\" srcmac=\"d8:94:03:g6:cd:27\" dstmac=\"00:1a:8c:g0:62:69\" srcip=\"103.188.113.55\" dstip=\"133.222.233.233\" proto=\"6\" length=\"40\" tos=\"0x00\" prec=\"0x00\" ttl=\"242\" srcport=\"54040\" dstport=\"52938\" tcpflags=\"SYN\"",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ]
        },
        "sophos": {
            "action": "drop",
            "sub": "packetfilter"
        },
        "source": {
            "mac": "d8:94:03:g6:cd:27",
            "ip": "103.188.113.55",
            "port": 54040,
            "address": "103.188.113.55"
        },
        "destination": {
            "mac": "00:1a:8c:g0:62:69",
            "ip": "133.222.233.233",
            "port": 52938,
            "address": "133.222.233.233"
        },
        "related": {
            "ip": [
                "103.188.113.55",
                "133.222.233.233"
            ]
        }
    }
    	
	```


=== "xg_allow.json"

    ```json
	
    {
        "message": "device=\"SFW\" date=2020-04-23 time=19:36:57 timezone=\"+11\" device_name=\"SG330\" device_id=S3105611453B86C log_id=010101600001 log_type=\"Firewall\" log_component=\"Firewall Rule\" log_subtype=\"Allowed\" status=\"Allow\" priority=Information duration=0 fw_rule_id=22 policy_type=1 user_name=\"\" user_gp=\"\" iap=0 ips_policy_id=0 appfilter_policy_id=0 application=\"\" application_risk=0 application_technology=\"\" application_category=\"\" in_interface=\"PortE0\" out_interface=\"PortE4\" src_mac=00:00:00:00:00:00 src_ip=10.0.215.3 src_country_code=R1 dst_ip=195.35.245.30 dst_country_code=NLD protocol=\"UDP\" src_port=38413 dst_port=62384 sent_pkts=0  recv_pkts=0 sent_bytes=0 recv_bytes=0 tran_src_ip=61.5.213.97 tran_src_port=0 tran_dst_ip=\"\" tran_dst_port=0 srczonetype=\"LAN\" srczone=\"LAN\" dstzonetype=\"LAN\" dstzone=\"WAN_RF\" dir_disp=\"\" connevent=\"Start\" connid=\"1950158712\" vconnid=\"\" hb_health=\"No Heartbeat\" message=\"\" appresolvedby=\"Signature\" app_is_cloud=0",
        "event": {
            "kind": "event",
            "category": [
                "network"
            ]
        },
        "log": {
            "level": "Information"
        },
        "observer": {
            "name": "SG330"
        },
        "sophos": {
            "status": "Allow",
            "log_subtype": "Allowed"
        },
        "source": {
            "bytes": 0,
            "packets": 0,
            "mac": "00:00:00:00:00:00",
            "ip": "10.0.215.3",
            "port": 38413,
            "nat": {
                "ip": "61.5.213.97",
                "port": 0
            },
            "address": "10.0.215.3"
        },
        "destination": {
            "bytes": 0,
            "packets": 0,
            "ip": "195.35.245.30",
            "port": 62384,
            "nat": {
                "port": 0
            },
            "address": "195.35.245.30"
        },
        "network": {
            "transport": "UDP"
        },
        "action": {
            "name": "allow"
        },
        "related": {
            "ip": [
                "10.0.215.3",
                "195.35.245.30",
                "61.5.213.97"
            ]
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
|`sophos.action` | `keyword` | event related action |
|`sophos.log_subtype` | `keyword` | event sub type |
|`sophos.status` | `keyword` | event status |
|`sophos.sub` | `keyword` | event category |
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

