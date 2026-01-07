
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_my_event"


    ```json
	{
        "time": 1748052015,
        "host": "CiscoolBox",
        "source": "HTTP_GET",
        "sourcetype": "_json",
        "event": {
            "timezone": "+00:00",
            "device": "honeypot",
            "user_agent": {
                "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
            },
            "client": {
                "ip": "192.168.1.212",
                "port": 56419,
                "geo": {
                    "continent": null,
                    "country": null,
                    "country_iso": null,
                    "city": null,
                    "postal": null,
                    "timezone": null,
                    "as_domain": null,
                    "as_name": null,
                    "asn": null,
                    "city_geoname_id": null,
                    "city_iso": null,
                    "continent_geoname_id": null,
                    "country_geoname_id": null,
                    "accuracy_radius": null,
                    "location": {
                        "lon": null,
                        "lat": null
                    }
                }
            },
            "server": {
                "ip": "192.168.1.132",
                "port": 443
            },
            "url": {
                "path": "/login"
            },
            "http": {
                "request": {
                    "method": "GET",
                    "referrer": null,
                    "headers": {
                        "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
                        "language": "en-US,en;q=0.7"
                    }
                },
                "response": {
                    "status_code": "200"
                }
            },
            "tls": {
                "version_protocol": "http/1.1"
            },
            "user": {
                "name": null
            },
            "credential": {
                "compromised": null
            },
            "session": {
                "id": "518b913f3cf61879"
            },
            "language": "en-US,en;q=0.7",
            "logtype": 3000,
            "tracking_id": "eb2ab4dcad5bfa9908be7f29da14aa81d0f84e8a3cf9396deb477171cd7ca60e",
            "template": "openwrt",
            "action": "connection",
            "protocol_name": "TCP",
            "protocol_number": "6",
            "vulnerability": {
                "id": null,
                "description": null
            },
            "cmd": {
                "list": null
            },
            "crawler": {
                "bot_name": null,
                "bot_category": null
            },
            "file": {
                "upload_file": null,
                "mime_type": null,
                "size": null,
                "hash": {
                    "sha256": null
                }
            },
            "dns": {
                "type": null,
                "ip": null,
                "nameserver": null,
                "alias": null,
                "mname": null,
                "rname": null,
                "serial": null,
                "refresh": null,
                "retry": null,
                "expire": null,
                "minimum": null,
                "pointer": null,
                "exchange": null,
                "preference": null,
                "text": null
            },
            "ssh": {
                "local_version": null,
                "remote_version": null,
                "incoming_packet_sequence": null,
                "outgoing_packet_sequence": null,
                "keyalg": null,
                "login_attempts": null,
                "auth_method": null
            },
            "sql": {
                "client_encoding": null,
                "database": null,
                "thread_id": null,
                "hash_type": null,
                "salt": null
            },
            "vnc": {
                "client_response": null,
                "client_version": null,
                "encryption_type": null,
                "server_challenge": null
            },
            "rdp": {
                "client": null,
                "cookie": null,
                "mstshash": null
            },
            "ntp": {
                "request_type": null,
                "request_mode": null,
                "request_version": null
            },
            "sip": {
                "headers": {
                    "allow": null,
                    "call-id": null,
                    "contact": null,
                    "from": null,
                    "cseq": null,
                    "max-forwards": null,
                    "to": null,
                    "via": null,
                    "user-agent": null,
                    "content-type": null,
                    "accept": null
                },
                "error": null
            },
            "snmp": {
                "version": null,
                "community_string": null,
                "pdu_type": null,
                "request_id": null,
                "variable_bindings": null
            },
            "tftp": {
                "filename": null,
                "opcode": null,
                "mode": null
            },
            "git": {
                "repo": null,
                "host": null
            },
            "mitre": {
                "tactic": "Discovery",
                "technique": "File and Directory Discovery",
                "id": "T1083"
            },
            "raw_data": {
                "post_data": null
            },
            "related": {
                "ip": [
                    "192.168.1.212",
                    "192.168.1.132"
                ],
                "user": [
                    null
                ]
            }
        }
    }
    ```



=== "test_ntp_event"


    ```json
	{
        "time": 1748073000,
        "host": "CiscoolBox",
        "source": "NTP_REQUEST",
        "sourcetype": "_json",
        "event": {
            "timezone": "+00:00",
            "device": "honeypot",
            "client": {
                "ip": "148.170.245.211",
                "port": 33372,
                "geo": {
                    "continent": "Europe",
                    "country": "Belgium",
                    "country_iso": "BE",
                    "city": "Brussels",
                    "postal": "1000",
                    "timezone": "Europe/Brussels",
                    "as_domain": "easyhost.be",
                    "as_name": "Easyhost BVBA",
                    "asn": "AS28747",
                    "city_geoname_id": 2800866,
                    "city_iso": "BRU",
                    "continent_geoname_id": 6255148,
                    "country_geoname_id": 2802361,
                    "accuracy_radius": 20,
                    "location": {
                        "lon": 4.347,
                        "lat": 50.8534
                    }
                }
            },
            "server": {
                "ip": "0.0.0.0",
                "port": 123
            },
            "session": {
                "id": "7f08bb08f3c54ba"
            },
            "logtype": 11001,
            "tracking_id": "b29a2f994fdaf479ec46efd1afc4fbd5a6be90a44f337cb05b939a95019a3572",
            "action": "connection",
            "protocol_name": "UDP",
            "protocol_number": "17",
            "ntp": {
                "request_type": "Symmetric Active",
                "request_mode": "1",
                "request_version": "3"
            },
            "mitre": {
                "tactic": "Reconnaissance",
                "technique": "Active Scanning",
                "id": "T1595"
            },
            "related": {
                "ip": [
                    "148.170.245.211",
                    "0.0.0.0"
                ],
                "user": []
            }
        }
    }
    ```



=== "test_psql_event"


    ```json
	{
        "time": 1748073209,
        "host": "CiscoolBox",
        "source": "POSTGRES_LOGIN_ATTEMPT",
        "sourcetype": "_json",
        "event": {
            "timezone": "+00:00",
            "device": "honeypot",
            "client": {
                "ip": "8.98.145.113",
                "port": 55086,
                "geo": {
                    "continent": "North America",
                    "country": "United States",
                    "country_iso": "US",
                    "timezone": "America/Chicago",
                    "as_domain": "amazon.com",
                    "as_name": "Amazon.com, Inc.",
                    "asn": "AS14618",
                    "continent_geoname_id": 6255149,
                    "country_geoname_id": 6252001,
                    "accuracy_radius": 1000,
                    "location": {
                        "lon": -97.822,
                        "lat": 37.751
                    }
                }
            },
            "server": {
                "ip": "192.168.1.132",
                "port": 5432
            },
            "user": {
                "name": "postgres"
            },
            "credential": {
                "username": "postgres",
                "password": "postgres",
                "compromised": true
            },
            "session": {
                "id": "b6f6512185e4064d"
            },
            "logtype": 20001,
            "tracking_id": "b29a2f994fdaf479ec46efd1afc4fbd5a6be90a44f337cb05b939a95019a3572",
            "action": "login",
            "status": "success",
            "protocol_name": "TCP",
            "protocol_number": "6",
            "sql": {
                "client_encoding": "UTF8",
                "database": "postgres"
            },
            "mitre": {
                "tactic": "Persistence, Initial Access",
                "technique": "Valid Accounts",
                "id": "T1078"
            },
            "related": {
                "ip": [
                    "8.98.145.113",
                    "192.168.1.132"
                ],
                "user": [
                    "postgres"
                ]
            }
        }
    }
    ```



=== "test_rdp_event"


    ```json
	{
        "time": 1748075181,
        "host": "CiscoolBox",
        "source": "RDP_LOGIN_ATTEMPT",
        "sourcetype": "_json",
        "event": {
            "timezone": "+00:00",
            "device": "honeypot",
            "client": {
                "ip": "152.111.92.207",
                "port": 60892,
                "geo": {
                    "continent": "Asia",
                    "country": "South Korea",
                    "country_iso": "KR",
                    "timezone": "Asia/Seoul",
                    "as_domain": "uplus.co.kr",
                    "as_name": "LG DACOM Corporation",
                    "asn": "AS3786",
                    "continent_geoname_id": 6255147,
                    "country_geoname_id": 1835841,
                    "accuracy_radius": 200,
                    "location": {
                        "lon": 126.9741,
                        "lat": 37.5112
                    }
                }
            },
            "server": {
                "ip": "192.168.1.132",
                "port": 3389
            },
            "user": {
                "name": "admin"
            },
            "credential": {
                "username": "admin",
                "password": "windows123",
                "compromised": false
            },
            "session": {
                "id": "5a385f4d044f7c0f"
            },
            "logtype": 14003,
            "tracking_id": "b29a2f994fdaf479ec46efd1afc4fbd5a6be90a44f337cb05b939a95019a3572",
            "domain": "prod",
            "action": "login",
            "status": "failed",
            "protocol_name": "TCP",
            "protocol_number": "6",
            "rdp": {
                "client": "remina"
            },
            "mitre": {
                "tactic": "Credential Access",
                "technique": "Brute Force",
                "id": "T1110"
            },
            "related": {
                "ip": [
                    "152.111.92.207",
                    "192.168.1.132"
                ],
                "user": [
                    "admin"
                ]
            }
        }
    }
    ```



=== "test_ssh_event"


    ```json
	{
        "time": 1748070903,
        "host": "CiscoolBox",
        "source": "SSH_LOGIN_ATTEMPT",
        "sourcetype": "_json",
        "event": {
            "timezone": "+00:00",
            "device": "honeypot",
            "client": {
                "ip": "158.94.46.176",
                "port": 41958,
                "geo": {
                    "continent": "Asia",
                    "country": "Malaysia",
                    "country_iso": "MY",
                    "city": "Klang",
                    "postal": "41700",
                    "timezone": "Asia/Kuala_Lumpur",
                    "as_domain": "tm.com.my",
                    "as_name": "TM TECHNOLOGY SERVICES SDN. BHD.",
                    "asn": "AS4788",
                    "city_geoname_id": 1732905,
                    "city_iso": "10",
                    "continent_geoname_id": 6255147,
                    "country_geoname_id": 1733045,
                    "accuracy_radius": 20,
                    "location": {
                        "lon": 101.4432,
                        "lat": 3.0477
                    }
                }
            },
            "server": {
                "ip": "192.168.1.132",
                "port": 22
            },
            "user": {
                "name": "root"
            },
            "credential": {
                "username": "root",
                "password": "root",
                "compromised": true
            },
            "session": {
                "id": "929b8e7f24f61cf8"
            },
            "logtype": 4002,
            "tracking_id": "b29a2f994fdaf479ec46efd1afc4fbd5a6be90a44f337cb05b939a95019a3572",
            "action": "login",
            "protocol_name": "TCP",
            "protocol_number": "6",
            "ssh": {
                "local_version": "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1",
                "remote_version": "SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.11",
                "incoming_packet_sequence": 8,
                "outgoing_packet_sequence": 8,
                "keyalg": "ssh-rsa",
                "login_attempts": 1,
                "auth_method": "password"
            },
            "mitre": {
                "tactic": "Persistence, Initial Access",
                "technique": "Valid Accounts",
                "id": "T1078"
            },
            "related": {
                "ip": [
                    "158.94.46.176",
                    "192.168.1.132"
                ],
                "user": [
                    "root"
                ]
            }
        }
    }
    ```



=== "test_tftp_event"


    ```json
	{
        "time": 1748074463,
        "host": "CiscoolBox",
        "source": "TFTP_READ_ATTEMPT",
        "sourcetype": "_json",
        "event": {
            "timezone": "+00:00",
            "device": "honeypot",
            "client": {
                "ip": "22.163.115.179",
                "port": 49037,
                "geo": {
                    "continent": "Europe",
                    "country": "Germany",
                    "country_iso": "DE",
                    "city": "Duisburg",
                    "postal": "47167",
                    "timezone": "Europe/Berlin",
                    "as_domain": "continentale.de",
                    "as_name": "Continentale Krankenversicherung a.G.",
                    "asn": "AS56919",
                    "city_geoname_id": 2934691,
                    "city_iso": "NW",
                    "continent_geoname_id": 6255148,
                    "country_geoname_id": 2921044,
                    "accuracy_radius": 100,
                    "location": {
                        "lon": 6.8017,
                        "lat": 51.5117
                    }
                }
            },
            "server": {
                "ip": "0.0.0.0",
                "port": 69
            },
            "session": {
                "id": "bb9fc65c3645ceeb"
            },
            "logtype": 10002,
            "tracking_id": "b29a2f994fdaf479ec46efd1afc4fbd5a6be90a44f337cb05b939a95019a3572",
            "action": "connection",
            "protocol_name": "UDP",
            "protocol_number": "17",
            "tftp": {
                "filename": "bootrom.ld",
                "opcode": "READ",
                "mode": "octet"
            },
            "mitre": {
                "tactic": "Exfiltration",
                "technique": "Exfiltration Over Alternative Protocol",
                "id": "T1048"
            },
            "related": {
                "ip": [
                    "22.163.115.179",
                    "0.0.0.0"
                ],
                "user": []
            }
        }
    }
    ```



=== "test_vnc_event"


    ```json
	{
        "time": 1748072722,
        "host": "CiscoolBox",
        "source": "VNC_LOGIN_ATTEMPT",
        "sourcetype": "_json",
        "event": {
            "timezone": "+00:00",
            "device": "honeypot",
            "client": {
                "ip": "192.168.1.123",
                "port": 53678
            },
            "server": {
                "ip": "192.168.1.132",
                "port": 5900
            },
            "credential": {
                "password": "12345678"
            },
            "session": {
                "id": "be64fd6f5563f951"
            },
            "logtype": 12002,
            "tracking_id": "b29a2f994fdaf479ec46efd1afc4fbd5a6be90a44f337cb05b939a95019a3572",
            "action": "login",
            "status": "failed",
            "protocol_name": "TCP",
            "protocol_number": "6",
            "vnc": {
                "client_response": "0835cbd4461cb5d2d4792da86cfc590d",
                "client_version": "RFB 003.008",
                "encryption_type": "DES",
                "server_challenge": "fe5e3254598eb0182e7d9e553377f7dc"
            },
            "mitre": {
                "tactic": "Credential Access",
                "technique": "Brute Force",
                "id": "T1110"
            },
            "related": {
                "ip": [
                    "192.168.1.123",
                    "192.168.1.132"
                ],
                "user": []
            }
        }
    }
    ```



