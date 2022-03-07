
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Authentication logs` | Audit logs are generated for login events,logout events, as well as other user actions that can impact the security posture of the product. |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "vectra_campaign.json"

    ```json
	
    {
        "source": {
            "ip": "255.255.255.1"
        },
        "destination": {
            "ip": "255.255.255.2"
        },
        "vectra": {
            "source": {
                "name": "IP-255.255.255.1",
                "hid": 11111
            },
            "destination": {
                "name": "push.services.mozilla.com",
                "id": "external"
            },
            "timestamp": 1111111111,
            "campaign": {
                "name": "push.services.mozilla.com-13",
                "id": 222,
                "link": "https://255.255.255.3/campaigns/222"
            },
            "detection": {
                "reason": "Connection"
            }
        },
        "action": {
            "name": "ADD"
        },
        "observer": {
            "version": "6.8",
            "name": "255.255.255.3",
            "ip": "255.255.255.3"
        }
    }
    	
	```


=== "vectra_threat1.json"

    ```json
	
    {
        "event": {
            "type": "RECONNAISSANCE",
            "url": "https://255.255.255.1/detections/1900?detail_id=66777"
        },
        "observer": {
            "version": "6.8",
            "name": "255.255.255.1",
            "ip": "255.255.255.1"
        },
        "vectra": {
            "severity": 7.0,
            "risk_score_norm": 70,
            "certainty": 86,
            "triaged": false,
            "detection": {
                "id": 1900,
                "type": "rpc_recon_1to1",
                "name": "RPC Targeted Recon"
            },
            "timestamp": 1623742534
        },
        "destination": {
            "ip": "10.43.0.81",
            "port": 49668
        },
        "host": {
            "ip": "192.168.71.1",
            "name": "IP-192.168.71.1"
        }
    }
    	
	```


=== "vectra_account_scoring.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
            "type": "ACCOUNT SCORING",
            "url": "https:/198.51.100.94/accounts/522"
        },
        "observer": {
            "version": "6.12",
            "ip": "198.51.100.94"
        },
        "vectra": {
            "account": {
                "id": 123456,
                "uid": "admin-prtg@company.local"
            },
            "certainty": 0,
            "detection": {
                "last_type": "Privilege Anomaly: Unusual Service - Insider",
                "score_decreases": true,
                "tags": []
            },
            "risk_score_norm": 0,
            "timestamp": 1633338457,
            "user": {
                "privilege": 4
            },
            "history": {
                "host_access": [
                    {
                        "id": 22235,
                        "lastSeen": "2021-09-30T08:06:46+00:00",
                        "name": "HOSTNAME.COMPANY.LOCAL",
                        "privilege": null,
                        "privilegeCategory": null
                    }
                ],
                "host_access_hostname": [
                    "HOSTNAME.COMPANY.LOCAL"
                ],
                "service_access": [
                    {
                        "id": 1470943,
                        "lastSeen": "2021-09-30T08:06:46+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "cifs/serssq01.company.local@company.local"
                    },
                    {
                        "id": 5,
                        "lastSeen": "2021-09-30T08:04:19+00:00",
                        "privilege": null,
                        "privilegeCategory": null,
                        "uid": "krbtgt/company.local.company@company"
                    },
                    {
                        "id": 2614295,
                        "lastSeen": "2021-09-30T08:04:19+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "rpcss/host109.company.local@company.local"
                    },
                    {
                        "id": 2614304,
                        "lastSeen": "2021-09-30T08:04:04+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "rpcss/host2db01.company.local@company.local"
                    },
                    {
                        "id": 2614297,
                        "lastSeen": "2021-09-30T07:57:44+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "rpcss/host110.company.local@company.local"
                    },
                    {
                        "id": 990,
                        "lastSeen": "2021-09-30T07:54:04+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "rpcss/srv-appli02.company.local@company.local"
                    },
                    {
                        "id": 2614303,
                        "lastSeen": "2021-09-30T07:37:28+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "rpcss/host201.company.local@company.local"
                    },
                    {
                        "id": 4214403,
                        "lastSeen": "2021-09-30T07:21:04+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "http/alm.company.local@company.local"
                    },
                    {
                        "id": 4186134,
                        "lastSeen": "2021-09-30T07:20:50+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "http/host109.company.local@company.local"
                    },
                    {
                        "id": 3693289,
                        "lastSeen": "2021-09-30T07:20:38+00:00",
                        "privilege": 4,
                        "privilegeCategory": "Medium",
                        "uid": "http/host110.company.local@company.local"
                    }
                ],
                "service_access_uid": {
                    "host": [
                        "serssq01.company.local@company.local",
                        "company.local.company@company",
                        "host109.company.local@company.local",
                        "host2db01.company.local@company.local",
                        "host110.company.local@company.local",
                        "srv-appli02.company.local@company.local",
                        "host201.company.local@company.local",
                        "alm.company.local@company.local",
                        "host109.company.local@company.local",
                        "host110.company.local@company.local"
                    ],
                    "proto_host": [
                        "cifs/serssq01.company.local@company.local",
                        "krbtgt/company.local.company@company",
                        "rpcss/host109.company.local@company.local",
                        "rpcss/host2db01.company.local@company.local",
                        "rpcss/host110.company.local@company.local",
                        "rpcss/srv-appli02.company.local@company.local",
                        "rpcss/host201.company.local@company.local",
                        "http/alm.company.local@company.local",
                        "http/host109.company.local@company.local",
                        "http/host110.company.local@company.local"
                    ]
                }
            }
        }
    }
    	
	```


=== "vectra_lateral_movement.json"

    ```json
	
    {
        "destination": {
            "address": "198.51.100.38",
            "ip": "198.51.100.38",
            "port": 445
        },
        "host": {
            "ip": "198.51.100.155",
            "name": "hostname"
        },
        "event": {
            "outcome": "success",
            "type": "LATERAL MOVEMENT",
            "url": "https://198.51.100.94/detections/13295?detail_id=94908"
        },
        "observer": {
            "ip": "198.51.100.94",
            "name": "198.51.100.94",
            "version": "6.12"
        },
        "related": {
            "ip": [
                "198.51.100.155",
                "198.51.100.38",
                "198.51.100.94"
            ]
        },
        "vectra": {
            "certainty": 74,
            "detection": {
                "accounts": "user@company.net",
                "id": 13295,
                "name": "SMB Brute-Force",
                "reason": "MORE_PROCESSING_REQUIRED",
                "type": "smb_brute_force"
            },
            "risk_score_norm": 20,
            "severity": 2.0,
            "timestamp": 1633681756,
            "triaged": false
        }
    }
    	
	```


=== "vectra_command_control.json"

    ```json
	
    {
        "destination": {
            "address": "mirror.centos.org",
            "bytes": 8269214038,
            "domain": "mirror.centos.org",
            "ip": "198.51.100.1",
            "port": 8002,
            "registered_domain": "centos.org",
            "subdomain": "mirror",
            "top_level_domain": "org"
        },
        "event": {
            "outcome": "success",
            "type": "COMMAND & CONTROL",
            "url": "https://198.51.100.94/detections/13281?detail_id=94738",
            "ip": [
                "198.51.100.94",
                "198.51.100.1",
                "198.51.100.14"
            ]
        },
        "host": {
            "ip": "198.51.100.14",
            "name": "IP-198.51.100.14"
        },
        "network": {
            "protocol": "tcp"
        },
        "observer": {
            "ip": "198.51.100.94",
            "name": "198.51.100.94",
            "version": "6.12"
        },
        "source": {
            "bytes": 1476677
        },
        "vectra": {
            "certainty": 72,
            "detection": {
                "id": 13281,
                "name": "Hidden HTTP Tunnel",
                "type": "hidden_http_tunnel_cnc"
            },
            "risk_score_norm": 60,
            "severity": 6,
            "timestamp": 1633516306,
            "triaged": false
        }
    }
    	
	```


=== "vectra_info.json"

    ```json
	
    {
        "event": {
            "type": "INFO",
            "url": "https://255.255.255.1/detections/9999?detail_id=11111"
        },
        "observer": {
            "version": "6.7",
            "name": "255.255.255.1",
            "ip": "255.255.255.1"
        },
        "vectra": {
            "certainty": 0,
            "detection": {
                "type": "si_new_host",
                "name": "New Host",
                "id": 9999
            },
            "timestamp": 1099999999,
            "triaged": false,
            "risk_score_norm": 0,
            "severity": 0
        },
        "destination": {
            "ip": "0.0.0.0",
            "port": 80
        },
        "host": {
            "ip": "10.0.0.1",
            "name": "plop-99"
        }
    }
    	
	```


=== "vectra_host_scoring.json"

    ```json
	
    {
        "event": {
            "outcome": "success",
            "type": "HOST SCORING",
            "url": "https://198.51.100.94/hosts/27617"
        },
        "observer": {
            "ip": "198.51.100.94",
            "name": "198.51.100.94",
            "product": "E123456789123456",
            "version": "6.12"
        },
        "host": {
            "ip": "198.51.100.14",
            "name": "IP-198.51.100.14"
        },
        "related": {
            "ip": [
                "198.51.100.94",
                "198.51.100.14"
            ]
        },
        "vectra": {
            "certainty": 31,
            "detection": {
                "last_type": "Hidden HTTP Tunnel",
                "profile": {
                    "name": "saas",
                    "scoringDetections": [
                        "Hidden HTTP Tunnel (C&C)"
                    ],
                    "vname": "Cloud Services"
                },
                "score_decreases": false,
                "tags": []
            },
            "history": {
                "account_access": [],
                "service_access": []
            },
            "risk_score_norm": 22,
            "source": {
                "key_asset": false
            },
            "timestamp": 1633690973,
            "user": {
                "privilege": 0
            }
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
|`destination.port` | `long` | Port of the destination. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`event.url` | `keyword` | Event investigation URL |
|`host.id` | `keyword` | Unique host id. |
|`host.ip` | `ip` | Host ip addresses. |
|`host.mac` | `keyword` | Host MAC addresses. |
|`host.name` | `keyword` | Name of the host. |
|`network.protocol` | `keyword` | Application protocol name. |
|`observer.ip` | `ip` | IP addresses of the observer. |
|`observer.name` | `keyword` | Custom name of the observer. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.version` | `keyword` | Observer version. |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.ip` | `ip` | IP address of the source. |
|`user.name` | `keyword` | Short name or login of the user. |
|`vectra.account.id` | `long` | None |
|`vectra.account.name` | `keyword` | None |
|`vectra.account.uid` | `keyword` | None |
|`vectra.audit.message` | `text` | None |
|`vectra.campaign.id` | `long` | None |
|`vectra.campaign.link` | `keyword` | None |
|`vectra.campaign.name` | `keyword` | None |
|`vectra.certainty` | `long` | None |
|`vectra.destination.id` | `keyword` | None |
|`vectra.destination.key_asset` | `keyword` | None |
|`vectra.destination.name` | `keyword` | None |
|`vectra.detection.account` | `keyword` | None |
|`vectra.detection.accounts` | `keyword` | None |
|`vectra.detection.base_object` | `keyword` | None |
|`vectra.detection.bytes_received` | `keyword` | None |
|`vectra.detection.bytes_sent` | `keyword` | None |
|`vectra.detection.client_name` | `keyword` | None |
|`vectra.detection.client_token` | `keyword` | None |
|`vectra.detection.cookie` | `keyword` | None |
|`vectra.detection.count` | `keyword` | None |
|`vectra.detection.dos_type` | `keyword` | None |
|`vectra.detection.dst_ips` | `text` | None |
|`vectra.detection.extensions` | `keyword` | None |
|`vectra.detection.function` | `keyword` | None |
|`vectra.detection.host` | `keyword` | None |
|`vectra.detection.http_method` | `keyword` | None |
|`vectra.detection.http_segment` | `keyword` | None |
|`vectra.detection.id` | `long` | None |
|`vectra.detection.ip` | `keyword` | None |
|`vectra.detection.keyboard_id` | `keyword` | None |
|`vectra.detection.keyboard_name` | `keyword` | None |
|`vectra.detection.last_type` | `keyword` | None |
|`vectra.detection.matched_domain` | `text` | None |
|`vectra.detection.matched_ip` | `text` | None |
|`vectra.detection.matched_user_agent` | `text` | None |
|`vectra.detection.name` | `keyword` | None |
|`vectra.detection.namedpipe` | `keyword` | None |
|`vectra.detection.networks` | `keyword` | None |
|`vectra.detection.normal_admins` | `The normal admins observed.` | None |
|`vectra.detection.normal_servers` | `keyword` | None |
|`vectra.detection.num_attempts` | `keyword` | None |
|`vectra.detection.port` | `keyword` | None |
|`vectra.detection.ports` | `text` | None |
|`vectra.detection.product_id` | `keyword` | None |
|`vectra.detection.profile` | `text` | None |
|`vectra.detection.protocol` | `keyword` | None |
|`vectra.detection.ransom_notes` | `keyword` | None |
|`vectra.detection.reason` | `keyword` | None |
|`vectra.detection.received_normal_pattern` | `keyword` | None |
|`vectra.detection.received_pattern` | `keyword` | None |
|`vectra.detection.referer` | `keyword` | None |
|`vectra.detection.reply_cache_control` | `keyword` | None |
|`vectra.detection.request` | `keyword` | None |
|`vectra.detection.response_code` | `keyword` | None |
|`vectra.detection.scans` | `keyword` | None |
|`vectra.detection.score_decreases` | `boolean` | None |
|`vectra.detection.sent_normal_pattern` | `keyword` | None |
|`vectra.detection.sent_pattern` | `keyword` | None |
|`vectra.detection.shares` | `keyword` | None |
|`vectra.detection.sql_fragment` | `keyword` | None |
|`vectra.detection.successes` | `keyword` | None |
|`vectra.detection.tags` | `text` | None |
|`vectra.detection.threat_feeds` | `keyword` | None |
|`vectra.detection.tunnel_type` | `keyword` | None |
|`vectra.detection.type` | `keyword` | None |
|`vectra.detection.url` | `keyword` | None |
|`vectra.detection.uuid` | `keyword` | None |
|`vectra.health.message` | `text` | None |
|`vectra.history.account_access` | `text` | None |
|`vectra.history.host_access` | `object` | None |
|`vectra.history.host_access_hostname` | `keyword` | None |
|`vectra.history.service_access` | `text` | None |
|`vectra.history.service_access_uid.host` | `keyword` | None |
|`vectra.history.service_access_uid.proto_host` | `keyword` | None |
|`vectra.host.group` | `keyword` | None |
|`vectra.host.vendor` | `keyword` | None |
|`vectra.lockdown.retry` | `boolean` | None |
|`vectra.risk_score_norm` | `long` | None |
|`vectra.severity` | `long` | None |
|`vectra.source.hid` | `long` | None |
|`vectra.source.key_asset` | `boolean` | None |
|`vectra.source.name` | `keyword` | None |
|`vectra.timestamp` | `long` | None |
|`vectra.triaged` | `boolean` | None |
|`vectra.user.agent` | `keyword` | None |
|`vectra.user.privilege` | `long` | None |
|`vectra.user.role` | `keyword` | None |

