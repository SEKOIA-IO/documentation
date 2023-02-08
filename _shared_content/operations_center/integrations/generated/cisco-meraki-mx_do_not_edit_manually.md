
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | Meraki MX Security Appliance records traffic events flowing through |
| `Web logs` | Meraki MX Security Appliance records traffic events flowing through |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "test_dhcp_lease.json"

    ```json
	
    {
        "message": "1673516966.834663913 FW_MX_01 events dhcp lease of ip 1.2.3.4 from mx mac AA:BB:CC:DD:EE:FF for client mac 01:02:03:04:05:06 from router 5.6.7.8 on subnet 255.255.255.0 with dns 9.10.11.12",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-12T09:49:26.834664Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "dhcp_offer"
        },
        "client": {
            "ip": "1.2.3.4",
            "mac": "01:02:03:04:05:06",
            "address": "1.2.3.4"
        },
        "server": {
            "mac": "AA:BB:CC:DD:EE:FF"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4"
            ]
        }
    }
    	
	```


=== "test_dhcp_no_offer.json"

    ```json
	
    {
        "message": "1673541902.311547724 FW_MX_01 events dhcp no offers for mac AA:BB:CC:DD:EE:FF",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-12T16:45:02.311548Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "dhcp_no_offer"
        },
        "client": {
            "mac": "AA:BB:CC:DD:EE:FF"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ]
        }
    }
    	
	```


=== "test_events_anyconnect_vpn_auth_failure.json"

    ```json
	
    {
        "message": "1673596662.226844514 FW_MX_01 events type=anyconnect_vpn_auth_failure msg= 'RADIUS[373] Server IP=1.2.3.4 Server port=1812 Peer IP=5.6.7.8 Peer port=56735: Authentication request rejected. '",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-13T07:57:42.226845Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "anyconnect_vpn_auth_failure"
        },
        "action": {
            "outcome": "failure",
            "outcome_reason": "Authentication request rejected. "
        },
        "client": {
            "ip": "5.6.7.8",
            "port": 56735,
            "address": "5.6.7.8"
        },
        "server": {
            "ip": "1.2.3.4",
            "port": 1812
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_events_anyconnect_vpn_auth_success.json"

    ```json
	
    {
        "message": "1673596676.426899545 FW_MX_01 events type=anyconnect_vpn_auth_success msg= 'RADIUS[374] Server IP=1.2.3.4 Server port=1812 Peer IP=5.6.7.8 Peer port=56735 User=john.doe: Authentication request accepted. '",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-13T07:57:56.426899Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "anyconnect_vpn_auth_success"
        },
        "action": {
            "outcome": "success",
            "outcome_reason": "Authentication request accepted. "
        },
        "client": {
            "ip": "5.6.7.8",
            "port": 56735,
            "address": "5.6.7.8"
        },
        "server": {
            "ip": "1.2.3.4",
            "port": 1812
        },
        "user": {
            "name": "john.doe"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ],
            "user": [
                "john.doe"
            ]
        }
    }
    	
	```


=== "test_events_anyconnect_vpn_connect_1.json"

    ```json
	
    {
        "message": "1673614753.814828766 FW_MX_01 events anyconnect_vpn_connect user id 'john.doe@sekoia.io' local ip 1.2.3.4 reconnected from 5.6.7.8",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-13T12:59:13.814829Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "anyconnect_vpn_connect"
        },
        "network": {
            "forwarded_ip": "1.2.3.4"
        },
        "client": {
            "ip": "5.6.7.8",
            "address": "5.6.7.8"
        },
        "user": {
            "name": "john.doe",
            "domain": "sekoia.io"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "5.6.7.8"
            ],
            "user": [
                "john.doe"
            ]
        }
    }
    	
	```


=== "test_events_anyconnect_vpn_connect_2.json"

    ```json
	
    {
        "message": "1673614753.814828766 FW_MX_01 events anyconnect_vpn_connect user id 'john.doe@sekoia.io' local ip 1.2.3.4 connected from 5.6.7.8",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-13T12:59:13.814829Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "anyconnect_vpn_connect"
        },
        "network": {
            "forwarded_ip": "1.2.3.4"
        },
        "client": {
            "ip": "5.6.7.8",
            "address": "5.6.7.8"
        },
        "user": {
            "name": "john.doe",
            "domain": "sekoia.io"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "5.6.7.8"
            ],
            "user": [
                "john.doe"
            ]
        }
    }
    	
	```


=== "test_events_anyconnect_vpn_connection_success.json"

    ```json
	
    {
        "message": "1673516936.233050742 FW_MX_01 events type=anyconnect_vpn_connection_success msg= 'Server IP=1.2.3.4 Server port=443 Prot[TCP] Peer IP=5.6.7.8 Peer port=55760 conn_id[55356] Connection closed. '",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-12T09:48:56.233051Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "anyconnect_vpn_connection_success"
        },
        "client": {
            "ip": "5.6.7.8",
            "port": 55760,
            "address": "5.6.7.8"
        },
        "server": {
            "ip": "1.2.3.4",
            "port": 443
        },
        "network": {
            "protocol": "TCP"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_events_anyconnect_vpn_session_manager.json"

    ```json
	
    {
        "message": "1673614757.517501781 FW_MX_01 events type=anyconnect_vpn_session_manager msg= 'Sess-ID[289] Peer IP=1.2.3.4 User[john.doe@sekoia.io]: Successfully added DTLS tunnel[289.4] '",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-13T12:59:17.517502Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "anyconnect_vpn_session_manager",
            "end_of_message": "Successfully added DTLS tunnel[289.4] "
        },
        "client": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "user": {
            "name": "john.doe",
            "domain": "sekoia.io"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "john.doe"
            ]
        }
    }
    	
	```


=== "test_events_content_filtering_block.json"

    ```json
	
    {
        "message": "1673541348.531136002 FW_MX_01 events content_filtering_block url='https://docs.sekoia.io/...' server='1.2.3.4:443' client_mac='AA:BB:CC:DD:EE:FF'",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "events",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-12T16:35:48.531136Z",
        "observer": {
            "hostname": "FW_MX_01"
        },
        "cisco_meraki": {
            "event_subtype": "content_filtering_block"
        },
        "server": {
            "ip": "1.2.3.4",
            "port": 443
        },
        "client": {
            "mac": "AA:BB:CC:DD:EE:FF"
        },
        "url": {
            "original": "https://docs.sekoia.io/...",
            "domain": "docs.sekoia.io",
            "top_level_domain": "io",
            "subdomain": "docs",
            "registered_domain": "sekoia.io",
            "scheme": "https",
            "path": "/...",
            "port": 443
        },
        "action": {
            "outcome": "block"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4"
            ]
        }
    }
    	
	```


=== "test_flows_allow.json"

    ```json
	
    {
        "message": "1673277220.253011885 FW_MX_01 flows src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=39247 dport=443 pattern: 0 (tcp || udp) && dst port 443",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "flows",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-09T15:13:40.253012Z",
        "source": {
            "ip": "1.2.3.4",
            "port": 39247,
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "port": 443,
            "address": "5.6.7.8"
        },
        "network": {
            "protocol": "tcp"
        },
        "observer": {
            "hostname": "FW_MX_01"
        },
        "action": {
            "outcome": "allow"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_flows_block.json"

    ```json
	
    {
        "message": "1673277244.954105815 FW_MX_01 flows src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=42644 dport=543 pattern: 1 all",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "flows",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-09T15:14:04.954106Z",
        "source": {
            "ip": "1.2.3.4",
            "port": 42644,
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "port": 543,
            "address": "5.6.7.8"
        },
        "network": {
            "protocol": "tcp"
        },
        "observer": {
            "hostname": "FW_MX_01"
        },
        "action": {
            "outcome": "deny"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_ip_flow_end.json"

    ```json
	
    {
        "message": "1673277245.252432409 FW_MX_01 ip_flow_end src=1.2.3.4 dst=5.6.7.8 protocol=udp sport=56391 dport=53 translated_dst_ip=9.10.11.12 translated_port=53",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "ip_flow_end",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-09T15:14:05.252432Z",
        "source": {
            "ip": "1.2.3.4",
            "port": 56391,
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "port": 53,
            "nat": {
                "ip": "9.10.11.12",
                "port": 53
            },
            "address": "5.6.7.8"
        },
        "network": {
            "protocol": "udp"
        },
        "observer": {
            "hostname": "FW_MX_01"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8",
                "9.10.11.12"
            ]
        }
    }
    	
	```


=== "test_ip_flow_start.json"

    ```json
	
    {
        "message": "1673277245.262063982 FW_MX_01 ip_flow_start src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=64365 dport=443 translated_src_ip=9.10.11.12 translated_port=64365",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "ip_flow_start",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-09T15:14:05.262064Z",
        "source": {
            "ip": "1.2.3.4",
            "port": 64365,
            "nat": {
                "ip": "9.10.11.12",
                "port": 64365
            },
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "port": 443,
            "address": "5.6.7.8"
        },
        "network": {
            "protocol": "tcp"
        },
        "observer": {
            "hostname": "FW_MX_01"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8",
                "9.10.11.12"
            ]
        }
    }
    	
	```


=== "test_urls_1.json"

    ```json
	
    {
        "message": "1673277245.257656306 FW_MX_01 urls src=1.2.3.4:51960 dst=5.6.7.8:443 mac=AA:BB:CC:DD:EE:FF request: UNKNOWN https://www.google.com/...",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "urls",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-09T15:14:05.257656Z",
        "source": {
            "ip": "1.2.3.4",
            "port": 51960,
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "port": 443,
            "address": "5.6.7.8"
        },
        "observer": {
            "hostname": "FW_MX_01"
        },
        "url": {
            "original": "https://www.google.com/...",
            "domain": "www.google.com",
            "top_level_domain": "com",
            "subdomain": "www",
            "registered_domain": "google.com",
            "path": "/...",
            "scheme": "https",
            "port": 443
        },
        "http": {
            "request": {
                "method": "UNKNOWN"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_urls_2.json"

    ```json
	
    {
        "message": "1673277244.773622789 FW_MX_01 urls src=1.2.3.4:64194 dst=5.6.7.8:80 mac=AA:BB:CC:DD:EE:FF request: GET http://www.msftconnecttest.com/connecttest.txt",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "urls",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-09T15:14:04.773623Z",
        "source": {
            "ip": "1.2.3.4",
            "port": 64194,
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "port": 80,
            "address": "5.6.7.8"
        },
        "observer": {
            "hostname": "FW_MX_01"
        },
        "url": {
            "original": "http://www.msftconnecttest.com/connecttest.txt",
            "domain": "www.msftconnecttest.com",
            "top_level_domain": "com",
            "subdomain": "www",
            "registered_domain": "msftconnecttest.com",
            "scheme": "http",
            "path": "/connecttest.txt",
            "port": 80
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```


=== "test_urls_3.json"

    ```json
	
    {
        "message": "1673277244.416181683 FW_MX_01 urls src=1.2.3.4:55566 dst=5.6.7.8:80 mac=AA:BB:CC:DD:EE:FF agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' request: GET http://docs.sekoia.io/xdr/features/collect/integrations/network/cisco_meraki/",
        "event": {
            "id": "00000000-0000-0000-0000-000000000000",
            "dataset": "urls",
            "outcome": "success"
        },
        "sekoiaio": {
            "intake": {
                "dialect": "test",
                "dialect_uuid": "00000000-0000-0000-0000-000000000000",
                "parsing_status": "success",
                "coverage": null
            }
        },
        "@timestamp": "2023-01-09T15:14:04.416182Z",
        "source": {
            "ip": "1.2.3.4",
            "port": 55566,
            "address": "1.2.3.4"
        },
        "destination": {
            "ip": "5.6.7.8",
            "port": 80,
            "address": "5.6.7.8"
        },
        "observer": {
            "hostname": "FW_MX_01"
        },
        "url": {
            "original": "http://docs.sekoia.io/xdr/features/collect/integrations/network/cisco_meraki/",
            "domain": "docs.sekoia.io",
            "top_level_domain": "io",
            "subdomain": "docs",
            "registered_domain": "sekoia.io",
            "path": "/xdr/features/collect/integrations/network/cisco_meraki/",
            "scheme": "http",
            "port": 80
        },
        "http": {
            "request": {
                "method": "GET"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "related": {
            "hosts": [
                "FW_MX_01"
            ],
            "ip": [
                "1.2.3.4",
                "5.6.7.8"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cisco_meraki.end_of_message` | `keyword` | Cisco Meraki end of message for some logs. |
|`cisco_meraki.event_subtype` | `keyword` | Cisco Meraki event subtype set in logs. |
|`client.ip` | `ip` | IP address of the client. |
|`client.mac` | `keyword` | MAC address of the client. |
|`client.port` | `long` | Port of the client. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.nat.ip` | `ip` | Destination NAT ip |
|`destination.nat.port` | `long` | Destination NAT Port |
|`destination.port` | `long` | Port of the destination. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`http.request.method` | `keyword` | HTTP request method. |
|`network.forwarded_ip` | `ip` | Host IP address when the source IP address is the proxy. |
|`network.protocol` | `keyword` | Application protocol name. |
|`observer.hostname` | `keyword` | Hostname of the observer. |
|`server.ip` | `ip` | IP address of the server. |
|`server.mac` | `keyword` | MAC address of the server. |
|`server.port` | `long` | Port of the server. |
|`source.ip` | `ip` | IP address of the source. |
|`source.nat.ip` | `ip` | Source NAT ip |
|`source.nat.port` | `long` | Source NAT port |
|`source.port` | `long` | Port of the source. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

