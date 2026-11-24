
### Raw Events Samples { data-search-exclude }

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "analyzer"


    ```json
	{
        "_path": "analyzer",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T01:06:27.759077Z",
        "ts": "2026-09-18T01:06:27.759077Z",
        "analyzer_kind": "protocol",
        "analyzer_name": "HTTP",
        "uid": "CPqgHm2vteiLX525eh",
        "id.orig_h": "192.168.2.88",
        "id.orig_p": 51335,
        "id.resp_h": "192.168.88.95",
        "id.resp_p": 23,
        "proto": "tcp",
        "failure_reason": "not a http reply line"
    }
    ```



=== "analyzer_failure_data"


    ```json
	{
        "_path": "analyzer",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "analyzer_kind": "protocol",
        "analyzer_name": "FTP",
        "uid": "CQxCmdSeP1ymaHuC4O",
        "id.orig_h": "127.0.0.1",
        "id.orig_p": 51354,
        "id.resp_h": "127.0.0.1",
        "id.resp_p": 21,
        "proto": "tcp",
        "failure_reason": "non-numeric reply code",
        "failure_data": "99 PASV invalid"
    }
    ```



=== "conn"


    ```json
	{
        "_path": "conn",
        "_system_name": "sensor",
        "uid": "CGAXp90w9BVzA9KJf",
        "ts": "2025-03-06T20:20:18.552640Z",
        "id.orig_h": "10.10.199.202",
        "id.orig_p": 59694,
        "id.resp_h": "203.0.113.125",
        "id.resp_p": 5222,
        "proto": "tcp",
        "duration": 14.604184,
        "orig_bytes": 24,
        "resp_bytes": 23,
        "conn_state": "OTH",
        "local_orig": true,
        "local_resp": false,
        "missed_bytes": 0,
        "history": "DadA",
        "enrichment_orig.role": "Developer",
        "enrichment_orig.user": "John Doe",
        "enrichment_orig.city_location": "Arlington, VA",
        "enrichment_orig.building": "Workstation Hotel",
        "community_id": "1:wIHZAIUvY6MpjVyPUpWpv8i4UFs="
    }
    ```



=== "conn_array_envelope"


    ```json
	[
        {
            "_path": "conn",
            "_system_name": "sensor",
            "uid": "CGAXp90w9BVzA9KJf",
            "ts": "2025-03-06T20:20:18.552640Z",
            "id.orig_h": "10.10.199.202",
            "id.orig_p": 59694,
            "id.resp_h": "203.0.113.125",
            "id.resp_p": 5222,
            "proto": "tcp",
            "duration": 14.604184,
            "orig_bytes": 24,
            "resp_bytes": 23,
            "conn_state": "OTH",
            "local_orig": true,
            "local_resp": false,
            "missed_bytes": 0,
            "history": "DadA",
            "enrichment_orig.role": "Developer",
            "enrichment_orig.user": "John Doe",
            "enrichment_orig.city_location": "Arlington, VA",
            "enrichment_orig.building": "Workstation Hotel",
            "community_id": "1:wIHZAIUvY6MpjVyPUpWpv8i4UFs="
        }
    ]
    ```



=== "conn_geo"


    ```json
	{
        "_path": "conn",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:11:49.787664Z",
        "ts": "2026-09-18T19:11:39.787492Z",
        "uid": "Cm8gDdfZWGWLEDwYh",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 45466,
        "id.resp_h": "203.0.113.79",
        "id.resp_p": 53,
        "proto": "udp",
        "service": "dns",
        "duration": 0.0006630420684814453,
        "orig_bytes": 64,
        "resp_bytes": 114,
        "conn_state": "SF",
        "local_orig": true,
        "local_resp": false,
        "missed_bytes": 0,
        "history": "Dd",
        "orig_pkts": 1,
        "orig_ip_bytes": 92,
        "resp_pkts": 1,
        "resp_ip_bytes": 142,
        "tunnel_parents": [
            "CHEuc63HFna54hEME7"
        ],
        "ip_proto": 17,
        "resp_cc": "US",
        "spcap.url": "https://fleet.example.com/sensor/00-00-00-00-00-00-00-00/spcap/proxy-download/Cm8gDdfZWGWLEDwYh",
        "spcap.rule": 1,
        "spcap.trigger": "all-unencrypted",
        "orig_l2_addr": "02:00:00:00:00:01",
        "resp_l2_addr": "02:00:00:00:00:02",
        "id.orig_h_name.src": "NTLM_AUTH",
        "id.orig_h_name.vals": [
            "WINDOMAIN"
        ],
        "id.resp_h_name.src": "SSL_SNI",
        "id.resp_h_name.vals": [
            "dns.google"
        ],
        "community_id": "1:YZtCXHg+4tVOZANa7okGfDTTcCU=",
        "remote_asn": 15169,
        "remote_organization": "Example Corp",
        "remote_latitude": -1.0438338752435294e+172,
        "remote_longitude": -4.2029518960714174e+271,
        "remote_country": "Test Country"
    }
    ```



=== "conn_long"


    ```json
	{
        "_path": "conn_long",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:15:48.724176Z",
        "ts": "2026-09-17T23:15:48.516042Z",
        "uid": "C8tqC43PGIafTrkx3f",
        "id.orig_h": "172.16.56.20",
        "id.orig_p": 55957,
        "id.resp_h": "172.16.56.13",
        "id.resp_p": 6081,
        "proto": "udp",
        "service": "geneve",
        "duration": 3600.1345388889313,
        "orig_bytes": 8373204,
        "resp_bytes": 0,
        "conn_state": "S0",
        "local_orig": true,
        "local_resp": true,
        "missed_bytes": 0,
        "history": "D",
        "orig_pkts": 74201,
        "orig_ip_bytes": 10450832,
        "resp_pkts": 0,
        "resp_ip_bytes": 0,
        "ip_proto": 17,
        "spcap.url": "https://fleet.example.com/sensor/00-00-00-00-00-00-00-00/spcap/proxy-download/C8tqC43PGIafTrkx3f",
        "spcap.rule": 1,
        "spcap.trigger": "all-unencrypted",
        "community_id": "1:wY5KJKQUGuUmrph4b0w2XAAH77Q="
    }
    ```



=== "conn_no_payload"


    ```json
	{
        "_path": "conn",
        "_system_name": "sensor",
        "uid": "CTFkd44Ww0AYy035s7",
        "ts": "2025-03-06T20:20:18.552640Z",
        "id.orig_h": "fe80::8ff:c7ff:fe2f:fb11",
        "id.orig_p": 128,
        "id.resp_h": "fe80::1",
        "id.resp_p": 129,
        "proto": "icmp",
        "ip_proto": 58,
        "conn_state": "OTH",
        "local_orig": false,
        "local_resp": true,
        "missed_bytes": 0,
        "orig_ip_bytes": 56,
        "resp_ip_bytes": 0,
        "orig_pkts": 1,
        "resp_pkts": 0
    }
    ```



=== "conn_suri_ids"


    ```json
	{
        "_path": "conn",
        "_system_name": "sensor",
        "_write_ts": "2024-10-16T04:08:11.828325Z",
        "app": [
            "firefox",
            "mozilla",
            "windows"
        ],
        "community_id": "1:yLZkcBYXdcdBcAEZfgCcx8L7qZE=",
        "conn_state": "SF",
        "corelight_shunted": false,
        "duration": 65.33815288543701,
        "history": "ShADadfF",
        "id.orig_h": "10.4.30.5",
        "id.orig_h_name.src": "NTLM_AUTH",
        "id.orig_h_name.vals": [
            "WINDOMAIN"
        ],
        "id.orig_p": 49227,
        "id.resp_h": "203.0.113.208",
        "id.resp_h_name.src": "HTTP_HOST",
        "id.resp_h_name.vals": [
            "ip.example.com"
        ],
        "id.resp_p": 80,
        "local_orig": true,
        "local_resp": false,
        "missed_bytes": 0,
        "orig_bytes": 164,
        "orig_ip_bytes": 416,
        "orig_l2_addr": "02:00:00:00:00:04",
        "orig_pkts": 6,
        "pcr": -0.129973474801061,
        "proto": "tcp",
        "resp_bytes": 213,
        "resp_cc": "DE",
        "resp_ip_bytes": 417,
        "resp_l2_addr": "02:00:00:00:00:05",
        "resp_pkts": 5,
        "service": "http",
        "spcap.rule": 1,
        "spcap.trigger": "all-unencrypted",
        "spcap.url": "https://fleet.example.com/spcap/v1/?uid=CJaifqr1KnMIu1itbq",
        "suri_ids": [
            "SI7YwTINm9Rd"
        ],
        "ts": "2024-10-16T04:07:01.489619Z",
        "tunnel_parents": [
            "C2y6XKB2ovrcvv1G5"
        ],
        "uid": "CJaifqr1KnMIu1itbq",
        "vlan": 12
    }
    ```



=== "cotp"


    ```json
	{
        "_path": "cotp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:56:31.991373Z",
        "ts": "2026-09-18T00:56:31.991373Z",
        "uid": "CyNPSM27IwqixmEVy8",
        "id.orig_h": "10.10.10.30",
        "id.orig_p": 49159,
        "id.resp_h": "10.10.10.10",
        "id.resp_p": 102,
        "is_orig": false,
        "pdu_code": "0x0f",
        "pdu_name": "DT Data"
    }
    ```



=== "dce_rpc"


    ```json
	{
        "_path": "dce_rpc",
        "_system_name": "sensor",
        "_write_ts": "2026-11-04T08:55:35.576378Z",
        "endpoint": "srvsvc",
        "id.orig_h": "10.0.35.10",
        "id.orig_p": 39289,
        "id.resp_h": "192.168.100.10",
        "id.resp_p": 445,
        "named_pipe": "\\PIPE\\srvsvc",
        "operation": "NetrShareEnum",
        "rtt": 0.006824016571044922,
        "ts": "2026-11-04T08:55:35.569554Z",
        "uid": "Coyxv331fg6lduRRFa"
    }
    ```



=== "dhcp"


    ```json
	{
        "_path": "dhcp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T09:48:23.411262Z",
        "ts": "2026-09-15T09:48:11.395405Z",
        "uids": [
            "CJPb9q2cGF8baiOI06",
            "CArSw43yU4caakRltf"
        ],
        "client_addr": "172.16.56.13",
        "server_addr": "172.16.56.1",
        "mac": "02:00:00:00:00:03",
        "host_name": "hostname",
        "domain": "us-east-2.internal.test",
        "requested_addr": "172.16.56.13",
        "assigned_addr": "172.16.56.13",
        "lease_time": 3600.0,
        "msg_types": [
            "REQUEST",
            "ACK"
        ],
        "duration": 5.793571472167969e-05
    }
    ```



=== "dhcp_client_fqdn"


    ```json
	{
        "_path": "dhcp",
        "_system_name": "sensor",
        "_write_ts": "2021-11-18T08:00:21.486539Z",
        "ts": "2021-11-18T08:00:21.486539Z",
        "uids": [
            "CnZGo9RG5VvGJwRuS3"
        ],
        "client_addr": "192.168.1.102",
        "server_addr": "192.168.1.1",
        "mac": "02:00:00:00:00:08",
        "host_name": "hostname",
        "client_fqdn": "hostname.example.com.",
        "domain": "example.com",
        "assigned_addr": "192.168.1.102",
        "lease_time": 3564.0,
        "msg_types": [
            "REQUEST",
            "ACK"
        ],
        "duration": 0.16382
    }
    ```



=== "dhcp_nak"


    ```json
	{
        "_path": "dhcp",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uids": [
            "CE5Xmb47RFZAcQzvtO",
            "CkzW3R6SK54mA2oBQH",
            "CyKWTALpnvCUx2ELfj",
            "CTqmieED2UgrPpSj7s"
        ],
        "client_addr": "203.0.113.97",
        "server_addr": "203.0.113.152",
        "mac": "02:00:00:00:00:07",
        "host_name": "hostname",
        "domain": "example.com",
        "requested_addr": "203.0.113.189",
        "assigned_addr": "203.0.113.189",
        "lease_time": 900.0,
        "server_message": "requested address not available",
        "msg_types": [
            "DISCOVER",
            "OFFER",
            "REQUEST",
            "NAK",
            "REQUEST",
            "ACK",
            "DECLINE"
        ],
        "duration": 3.058797
    }
    ```



=== "dhcp_relay_agent"


    ```json
	{
        "_path": "dhcp",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uids": [
            "C3DlQXS7VCdIpMT5CS"
        ],
        "client_addr": "192.168.0.10",
        "server_addr": "10.10.0.1",
        "mac": "02:00:00:00:00:06",
        "assigned_addr": "192.168.0.10",
        "lease_time": 3600.0,
        "msg_types": [
            "ACK"
        ],
        "duration": 0.0,
        "circuit_id": "this is only a test...",
        "agent_remote_id": "\\x13",
        "subscriber_id": "-subID-"
    }
    ```



=== "dnp3"


    ```json
	{
        "_path": "dnp3",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:19:30.245320Z",
        "ts": "2026-09-18T00:19:24.495113Z",
        "uid": "C3cWYD1CRSN3RoWY26",
        "id.orig_h": "192.168.2.166",
        "id.orig_p": 2142,
        "id.resp_h": "192.168.88.95",
        "id.resp_p": 20000,
        "fc_request": "READ"
    }
    ```



=== "dnp3_control"


    ```json
	{
        "_path": "dnp3_control",
        "_system_name": "sensor",
        "_write_ts": "2026-09-17T23:15:45.734744Z",
        "ts": "2026-09-17T23:15:45.734648Z",
        "uid": "CJve7HYzdQy9MLqcd",
        "id.orig_h": "127.0.0.1",
        "id.orig_p": 64825,
        "id.resp_h": "127.0.0.1",
        "id.resp_p": 20000,
        "block_type": "Control Relay Output Block",
        "function_code": "OPERATE",
        "index_number": 1,
        "trip_control_code": "Nul",
        "operation_type": "Latch On",
        "execute_count": 1,
        "on_time": 100,
        "off_time": 100,
        "status_code": "Success"
    }
    ```



=== "dnp3_objects"


    ```json
	{
        "_path": "dnp3_objects",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:19:24.495113Z",
        "ts": "2026-09-18T00:19:24.495113Z",
        "uid": "C3cWYD1CRSN3RoWY26",
        "id.orig_h": "192.168.2.166",
        "id.orig_p": 2142,
        "id.resp_h": "192.168.88.95",
        "id.resp_p": 20000,
        "function_code": "READ",
        "object_type": "Class 0 Data"
    }
    ```



=== "dnp3_reply"


    ```json
	{
        "_path": "dnp3",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CHRqSrWgChIvXy2cKa",
        "id.orig_h": "203.0.113.250",
        "id.orig_p": 49413,
        "id.resp_h": "203.0.113.229",
        "id.resp_p": 20000,
        "fc_request": "DELAY_MEASURE",
        "fc_reply": "RESPONSE",
        "iin": 0
    }
    ```



=== "dns"


    ```json
	{
        "_path": "dns",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:20:18.552640Z",
        "uid": "CdnsTest123456",
        "id.orig_h": "10.0.35.10",
        "id.orig_p": 51000,
        "id.resp_h": "203.0.113.198",
        "id.resp_p": 53,
        "query": "abcdef0123456789.tunnel.example.com",
        "qtype_name": "NULL",
        "rcode_name": "NOERROR",
        "answers": [
            "10.0.0.1"
        ]
    }
    ```



=== "dns_full"


    ```json
	{
        "_path": "dns",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:33.302298Z",
        "ts": "2026-09-18T19:05:33.264729Z",
        "uid": "C0mDhe2ApoNUO7cGH4",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 53949,
        "id.resp_h": "10.9.18.1",
        "id.resp_p": 53,
        "proto": "udp",
        "trans_id": 62251,
        "rtt": 0.03756904602050781,
        "query": "mail.example.com",
        "qclass": 1,
        "qclass_name": "C_INTERNET",
        "qtype": 1,
        "qtype_name": "A",
        "rcode": 0,
        "rcode_name": "NOERROR",
        "AA": false,
        "TC": false,
        "RD": true,
        "RA": true,
        "Z": 0,
        "answers": [
            "203.0.113.195"
        ],
        "TTLs": [
            5.0
        ],
        "rejected": false
    }
    ```



=== "dns_nxdomain"


    ```json
	{
        "_path": "dns",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:33.302298Z",
        "ts": "2026-09-18T19:05:33.264729Z",
        "uid": "CwQ3Ke1nVd8sPx2Rfa",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 53949,
        "id.resp_h": "10.9.18.1",
        "id.resp_p": 53,
        "proto": "udp",
        "trans_id": 40817,
        "rtt": 0.03756904602050781,
        "query": "missing.example.com",
        "qclass": 1,
        "qclass_name": "C_INTERNET",
        "qtype": 1,
        "qtype_name": "A",
        "rcode": 3,
        "rcode_name": "NXDOMAIN",
        "AA": false,
        "TC": false,
        "RD": true,
        "RA": true,
        "Z": 0,
        "rejected": false
    }
    ```



=== "dns_txt_quotes"


    ```json
	{
        "_path": "dns",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:09:41.120554Z",
        "ts": "2026-09-18T19:09:41.104871Z",
        "uid": "CeR5tY2uIo8pAs3dF6",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 53712,
        "id.resp_h": "10.21.0.53",
        "id.resp_p": 53,
        "proto": "udp",
        "trans_id": 41237,
        "query": "example.com",
        "qclass": 1,
        "qclass_name": "C_INTERNET",
        "qtype": 16,
        "qtype_name": "TXT",
        "rcode": 0,
        "rcode_name": "NOERROR",
        "AA": false,
        "TC": false,
        "RD": true,
        "RA": true,
        "Z": 0,
        "answers": [
            "TXT 26 v=spf1 include:\"_spf.example.com\" ~all"
        ],
        "TTLs": [
            3600.0
        ],
        "rejected": false
    }
    ```



=== "encrypted_dns"


    ```json
	{
        "_path": "encrypted_dns",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T12:56:30.570487Z",
        "ts": "2026-09-15T12:56:30.563640Z",
        "uid": "CP1iON397iT0etNRI",
        "resp_h": "192.0.2.10",
        "sni": "dns.example.com",
        "match": "K"
    }
    ```



=== "enip"


    ```json
	{
        "_path": "enip",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:13:34.544905Z",
        "ts": "2026-09-18T00:13:34.544905Z",
        "uid": "C6NPNU1ltbQFtE6s0d",
        "id.orig_h": "192.168.2.44",
        "id.orig_p": 61428,
        "id.resp_h": "192.168.88.60",
        "id.resp_p": 44818,
        "is_orig": true,
        "enip_command_code": "0x63",
        "enip_command": "List Identity",
        "length": 0,
        "session_handle": "0x00000000",
        "enip_status": "Success",
        "sender_context": "0x00000000c1debed1",
        "options": "0x00000000"
    }
    ```



=== "etc_viz"


    ```json
	{
        "_path": "etc_viz",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:08:27.679482Z",
        "ts": "2026-09-18T19:03:27.381131Z",
        "uid": "Cb5gIf2HP0cRAYFQMh",
        "server_a": "203.0.113.36",
        "server_p": 443,
        "service": [],
        "c2s_viz.size": 10155,
        "c2s_viz.enc_dev": 1.093679540873425,
        "c2s_viz.enc_frac": 0.5841584158415841,
        "c2s_viz.pdu1_enc": false,
        "c2s_viz.clr_frac": 0.07920792079207921,
        "c2s_viz.clr_ex": "Y]^^P_PWPPWxMJMxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "s2c_viz.size": 10139,
        "s2c_viz.enc_dev": 0.6112977595031397,
        "s2c_viz.enc_frac": 0.7821782178217822,
        "s2c_viz.pdu1_enc": false,
        "s2c_viz.clr_frac": 0.009900990099009901
    }
    ```



=== "files"


    ```json
	{
        "_path": "files",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:23:38.591404Z",
        "uid": "CfilesTest123",
        "id.orig_h": "10.0.35.10",
        "id.resp_h": "203.0.113.198",
        "source": "HTTP",
        "md5": "0cea15a1205bcfa2b91de90fcc566d6c",
        "sha1": "caf07a8bdbd1c9ad3474fd6a31fefdcdc8964c5f",
        "sha256": "75475fb40984ddb7c83638cb1f4a79827396ba7b638e501f7aff6293adb8cf51",
        "mime_type": "application/x-dosexec",
        "seen_bytes": 539136
    }
    ```



=== "files_extracted"


    ```json
	{
        "_path": "files",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "fuid": "FQZZdL2WDqWxNZIZ2",
        "uid": "Cmfx5RHJaVIRijQ6sG",
        "id.orig_h": "203.0.113.5",
        "id.orig_p": 50737,
        "id.resp_h": "203.0.113.162",
        "id.resp_p": 38141,
        "source": "FTP_DATA",
        "depth": 0,
        "analyzers": [
            "EXTRACT"
        ],
        "mime_type": "text/plain",
        "duration": 0.001059,
        "local_orig": false,
        "is_orig": false,
        "seen_bytes": 16557,
        "missing_bytes": 0,
        "overflow_bytes": 0,
        "timedout": false,
        "extracted": "2",
        "extracted_cutoff": true,
        "extracted_size": 6000
    }
    ```



=== "files_no_tuple"


    ```json
	{
        "_path": "files",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:33.330111Z",
        "ts": "2026-09-18T19:05:33.303329Z",
        "fuid": "F55tHB2ssh7IsmD7O7",
        "source": "HTTP",
        "depth": 0,
        "analyzers": [
            "SHA1",
            "SHA256",
            "DATA_EVENT",
            "PE",
            "MD5"
        ],
        "mime_type": "application/x-dosexec",
        "filename": "samerton.png",
        "duration": 0.02678203582763672,
        "local_orig": false,
        "is_orig": false,
        "seen_bytes": 557056,
        "total_bytes": 557056,
        "missing_bytes": 0,
        "overflow_bytes": 0,
        "timedout": false,
        "md5": "5be11dc377ce72fe9a0f8ae24c20bf68",
        "sha1": "fdd0480a69d17d33292733668c6fd1dedf453a3c",
        "sha256": "e92dd00b092b435420f0996e4f557023fe1436110a11f0f61fbb628b959aac99",
        "tx_hosts": [
            "203.0.113.140"
        ],
        "rx_hosts": [
            "10.21.0.100"
        ],
        "conn_uids": [
            "CrkP6C18ri4M2jp02c"
        ]
    }
    ```



=== "files_transfer"


    ```json
	{
        "_path": "files",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:33.330111Z",
        "ts": "2026-09-18T19:05:33.303329Z",
        "fuid": "F55tHB2ssh7IsmD7O7",
        "uid": "CrkP6C18ri4M2jp02c",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 50861,
        "id.resp_h": "203.0.113.140",
        "id.resp_p": 80,
        "source": "HTTP",
        "depth": 0,
        "analyzers": [
            "SHA1",
            "SHA256",
            "DATA_EVENT",
            "PE",
            "MD5"
        ],
        "mime_type": "application/x-dosexec",
        "filename": "samerton.png",
        "duration": 0.02678203582763672,
        "local_orig": false,
        "is_orig": false,
        "seen_bytes": 557056,
        "total_bytes": 557056,
        "missing_bytes": 0,
        "overflow_bytes": 0,
        "timedout": false,
        "md5": "5be11dc377ce72fe9a0f8ae24c20bf68",
        "sha1": "fdd0480a69d17d33292733668c6fd1dedf453a3c",
        "sha256": "e92dd00b092b435420f0996e4f557023fe1436110a11f0f61fbb628b959aac99",
        "tx_hosts": [
            "203.0.113.140"
        ],
        "rx_hosts": [
            "10.21.0.100"
        ],
        "conn_uids": [
            "CrkP6C18ri4M2jp02c"
        ]
    }
    ```



=== "ftp"


    ```json
	{
        "_path": "ftp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T09:58:34.027006Z",
        "ts": "2026-09-16T09:58:33.978235Z",
        "uid": "CEzCPq4KO2pNP3Yc82",
        "id.orig_h": "192.168.2.22",
        "id.orig_p": 59431,
        "id.resp_h": "192.168.88.49",
        "id.resp_p": 21,
        "user": "Bob",
        "password": "changeme",
        "command": "PORT",
        "arg": "192,168,2,22,194,16",
        "reply_code": 503,
        "reply_msg": "Bad sequence of commands.",
        "data_channel.passive": false,
        "data_channel.orig_h": "192.168.88.49",
        "data_channel.resp_h": "192.168.2.22",
        "data_channel.resp_p": 49680
    }
    ```



=== "ftp_success"


    ```json
	{
        "_path": "ftp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T09:58:34.027006Z",
        "ts": "2026-09-16T09:58:33.978235Z",
        "uid": "CfT2kM8xRq5Vn3Lw9b",
        "id.orig_h": "192.168.2.22",
        "id.orig_p": 59431,
        "id.resp_h": "192.168.88.49",
        "id.resp_p": 21,
        "user": "Bob",
        "password": "changeme",
        "command": "PORT",
        "arg": "192,168,2,22,194,16",
        "reply_code": 200,
        "reply_msg": "Command okay.",
        "data_channel.passive": false,
        "data_channel.orig_h": "192.168.88.49",
        "data_channel.resp_h": "192.168.2.22",
        "data_channel.resp_p": 49680
    }
    ```



=== "generic_dns_tunnels"


    ```json
	{
        "_path": "generic_dns_tunnels",
        "_system_name": "sensor",
        "_write_ts": "2026-09-17T04:18:44.060840Z",
        "ts": "2026-09-17T04:18:44.113343Z",
        "dns_client": "192.168.200.201",
        "domain": "example.com",
        "bytes": 9632,
        "capture_secs": 86400.05226492882
    }
    ```



=== "http"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:20:18.552640Z",
        "uid": "CbsaT01N3Llhz2HRoa",
        "id.orig_h": "10.1.146.99",
        "id.orig_p": 51000,
        "id.resp_h": "203.0.113.131",
        "id.resp_p": 80,
        "host": "c.example.com",
        "method": "GET",
        "uri": "/r/r4.crl",
        "request_body_len": 0,
        "response_body_len": 0,
        "status_code": 304,
        "status_msg": "Not Modified",
        "user_agent": "Microsoft-CryptoAPI/10.0"
    }
    ```



=== "http_100_continue"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "C4AWnWG2AlOjS5re2X",
        "id.orig_h": "192.168.3.103",
        "id.orig_p": 54102,
        "id.resp_h": "203.0.113.51",
        "id.resp_p": 80,
        "trans_depth": 1,
        "method": "POST",
        "host": "www.example.com",
        "uri": "/",
        "version": "1.1",
        "user_agent": "curl/7.17.1 (i386-apple-darwin8.11.1) libcurl/7.17.1 zlib/1.2.3",
        "request_body_len": 2001,
        "response_body_len": 60731,
        "status_code": 200,
        "status_msg": "OK",
        "info_code": 100,
        "info_msg": "Continue",
        "tags": [],
        "orig_fuids": [
            "FaNuyS3sq5pxDRJT99"
        ],
        "orig_mime_types": [
            "text/plain"
        ],
        "resp_fuids": [
            "FbJsw4PwXcbDTYGPf"
        ],
        "resp_mime_types": [
            "text/html"
        ]
    }
    ```



=== "http_connect_proxied"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CxbKDU1La1ZXwqKt5Y",
        "id.orig_h": "::1",
        "id.orig_p": 52522,
        "id.resp_h": "::1",
        "id.resp_p": 80,
        "trans_depth": 1,
        "method": "CONNECT",
        "host": "secure.example.com:443",
        "uri": "secure.example.com:443",
        "version": "1.0",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0",
        "request_body_len": 0,
        "response_body_len": 0,
        "status_code": 200,
        "status_msg": "Connection Established",
        "tags": [],
        "proxied": [
            "PROXY-CONNECTION -> keep-alive"
        ]
    }
    ```



=== "http_headers"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:33.233201Z",
        "ts": "2026-09-18T19:05:33.215397Z",
        "uid": "CKisPx2kejQfsqZhA7",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 50844,
        "id.resp_h": "203.0.113.190",
        "id.resp_p": 8080,
        "trans_depth": 1,
        "method": "POST",
        "dest_host": "www.example.com:8080",
        "uri": "/guids/acquire/",
        "referrer": "http://www.example.com/guids/acquire/",
        "version": "1.1",
        "user_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "request_body_len": 624,
        "response_body_len": 201252,
        "status_code": 200,
        "status_msg": "OK",
        "tags": [],
        "orig_fuids": [
            "FJJXFq3YIj4PQNcmw"
        ],
        "orig_mime_types": [
            "text/plain"
        ],
        "resp_fuids": [
            "Fnxkhr2GIQLqYh38p8"
        ],
        "post_body": "XfiBYA4js=nNev9MOf0HHX%2BFFh00sINC5u9hPdh4eGpDZkrF2NFjBLNCijNKK4h%2B4MgUxbhNF58mGbeGGOCNsL9XsxkXRchHq0rvUDVdelYXoBBeD2ErdyImGVCAleCbvSg8lnR5hZ6qCw3F%2FyOUhq9Je0Bo2fFBJJk0XAZOpkHdGZzpCMTA0V1%2B%2Bn2HeJUAsbDEQJ0hEHCLPpFzPLXiWeYUoKjdr5EpEcKxYVTjqwaGXoCb0GpvtrNJsu5G4MtqV7uPQI138UFv0DRfHtBMuBeIccAy7lX89oWIMLpB74TQ21PyS99F5rLfN2b3Kl9oRinC4mOWgpZLpLqrADhuEFBtXKnbVOyoJ3HqgiVLOy2wIRThm2Sl3mcnL%2FmZ9IuZlrZ6dwp7kJD5z9crtZNrq0arkDVnWfFHc1j%2FZf9iNiN1az6nXmIGOdB5y8Do%2FS8jkPCp0qN8eW%2BcHliwAIKruJ6TMWAj2K8iTdnUBMwKmeiLt7CghUztoNWQBrY4KD9%2BnkLrhr05aDfUDdBXV%2Fi%2BG3W2yLjcGynk6ATIDNAh35p5HO63xBrbYH7en58WYy13tGAj8IPGgGg%2BStPQ%3D%3D",
        "client_headers": [
            "Referer:http://www.example.com/guids/acquire/",
            "Content-Type:application/x-www-form-urlencoded",
            "DNT:1",
            "User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Host:www.example.com:8080",
            "Content-Length:624",
            "Connection:Keep-Alive",
            "Cache-Control:no-cache"
        ],
        "server_headers": [
            "Server:nginx",
            "Date:Wed, 18 Sep 2019 17:46:58 GMT",
            "Content-Type:text/html; charset=UTF-8",
            "Content-Length:201252",
            "Connection:keep-alive",
            "Vary:Accept-Encoding"
        ],
        "server": "nginx"
    }
    ```



=== "http_host_port"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:20:18.552640Z",
        "uid": "ChP3tK9wMq2Rx7Nv4b",
        "id.orig_h": "10.1.146.99",
        "id.orig_p": 51000,
        "id.resp_h": "203.0.113.131",
        "id.resp_p": 8080,
        "host": "c.example.com:8080",
        "method": "GET",
        "uri": "/r/r4.crl",
        "request_body_len": 0,
        "response_body_len": 0,
        "status_code": 304,
        "status_msg": "Not Modified",
        "user_agent": "Microsoft-CryptoAPI/10.0"
    }
    ```



=== "http_ipv6_host"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:07:12.402118Z",
        "ts": "2026-09-18T19:07:12.388240Z",
        "uid": "CzN7wB1vQe5kLp2Hd4",
        "id.orig_h": "2001:db8:10::64",
        "id.orig_p": 51022,
        "id.resp_h": "2001:db8::1",
        "id.resp_p": 8080,
        "trans_depth": 1,
        "method": "GET",
        "dest_host": "[2001:db8::1]:8080",
        "uri": "/status",
        "version": "1.1",
        "user_agent": "curl/8.5.0",
        "request_body_len": 0,
        "response_body_len": 2,
        "status_code": 200,
        "status_msg": "OK",
        "tags": []
    }
    ```



=== "http_multipart_origin"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "Chgd4JEAyk0OGABC8H",
        "id.orig_h": "127.0.0.1",
        "id.orig_p": 45376,
        "id.resp_h": "127.0.0.1",
        "id.resp_p": 8000,
        "trans_depth": 1,
        "method": "POST",
        "host": "localhost:8000",
        "uri": "/",
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "origin": "null",
        "request_body_len": 767,
        "response_body_len": 0,
        "tags": [],
        "orig_fuids": [
            "FeaAeS2KrXTNRvTtBh"
        ],
        "orig_filenames": [
            "test.txt"
        ],
        "orig_mime_types": [
            "text/plain"
        ]
    }
    ```



=== "http_resp_filename"


    ```json
	{
        "_path": "http",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "ChsMafdqUyYvl3wNLx",
        "id.orig_h": "10.1.9.63",
        "id.orig_p": 63526,
        "id.resp_h": "203.0.113.246",
        "id.resp_p": 80,
        "trans_depth": 1,
        "method": "GET",
        "host": "www.example.com",
        "uri": "/response-headers?Content-Type=application/octet-stream; charset=UTF-8&Content-Disposition=attachment; filename=\"test.json\"",
        "version": "1.1",
        "user_agent": "curl/7.45.0",
        "request_body_len": 0,
        "response_body_len": 191,
        "status_code": 200,
        "status_msg": "OK",
        "tags": [],
        "resp_fuids": [
            "FiokML36uuy5agr5x3"
        ],
        "resp_filenames": [
            "test.json"
        ],
        "resp_mime_types": [
            "text/json"
        ]
    }
    ```



=== "intel"


    ```json
	{
        "_path": "intel",
        "_system_name": "sensor",
        "ts": "2018-05-21T20:58:18.214197Z",
        "uid": "CintelTest12",
        "id.orig_h": "10.0.0.1",
        "id.orig_p": 55552,
        "id.resp_h": "203.0.113.94",
        "id.resp_p": 53,
        "seen.indicator": "evil.example.com",
        "seen.indicator_type": "Intel::DOMAIN",
        "seen.where": "DNS::IN_REQUEST",
        "matched": [
            "Intel::DOMAIN"
        ],
        "sources": [
            "MyList"
        ]
    }
    ```



=== "intel_file_name"


    ```json
	{
        "_path": "intel",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "ClqPaRsNn5cpvJ8kvj",
        "id.orig_h": "10.1.9.63",
        "id.orig_p": 63526,
        "id.resp_h": "203.0.113.246",
        "id.resp_p": 80,
        "seen.indicator": "test.json",
        "seen.indicator_type": "Intel::FILE_NAME",
        "seen.where": "Files::IN_NAME",
        "seen.node": "zeek",
        "matched": [
            "Intel::FILE_NAME"
        ],
        "sources": [
            "source1"
        ],
        "fuid": "FiokML36uuy5agr5x3",
        "file_desc": "http://www.example.com/response-headers?Content-Type=application/octet-stream; charset=UTF-8&Content-Disposition=attachment; filename=\"test.json\""
    }
    ```



=== "ipsec"


    ```json
	{
        "_path": "ipsec",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T10:10:33.269735Z",
        "ts": "2026-09-16T10:10:33.269735Z",
        "uid": "C8lAos3ns4eWz4hztk",
        "id.orig_h": "10.100.152.128",
        "id.orig_p": 500,
        "id.resp_h": "192.0.2.76",
        "id.resp_p": 500,
        "is_orig": true,
        "initiator_spi": "bf178fe4e593b7b9",
        "responder_spi": "0000000000000000",
        "maj_ver": 1,
        "min_ver": 0,
        "exchange_type": 2,
        "flag_e": false,
        "flag_c": false,
        "flag_a": false,
        "flag_i": false,
        "flag_v": false,
        "flag_r": false,
        "message_id": 0,
        "vendor_ids": [
            "UNKNOWN:",
            "Dead Peer Detection v1.0",
            "RFC 3947 NAT-T",
            "draft-ietf-ipsec-nat-t-ike-03",
            "draft-ietf-ipsec-nat-t-ike-02",
            "draft-ietf-ipsec-nat-t-ike-02",
            "draft-ietf-ipsec-nat-t-ike-00",
            "IKE Fragmentation",
            "UNKNOWN:c33272b6ebcf606af6cc2fc7492eaa95",
            "UNKNOWN:80dbf81ba815edf6b87910bb92cd58b7",
            "UNKNOWN:68dc8d102dc2e84623a7a3df153aee62",
            "UNKNOWN:388ab3cb6e15198d3d43a8f750d3885f"
        ],
        "notify_messages": [],
        "transforms": [
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1"
        ],
        "ke_dh_groups": [],
        "proposals": [
            0
        ],
        "protocol_id": 1,
        "certificates": [],
        "transform_attributes": [
            "0:1:Life Type=1",
            "0:1:Life Duration=3600",
            "0:1:Encryption Algorithm=7",
            "0:1:Hash Algorithm=2",
            "0:1:Authentication Method=3",
            "0:1:Group Description=18",
            "0:1:Key Length=256",
            "0:1:Life Type=1",
            "0:1:Life Duration=3600",
            "0:1:Encryption Algorithm=7",
            "0:1:Hash Algorithm=2",
            "0:1:Authentication Method=3",
            "0:1:Group Description=17",
            "0:1:Key Length=256",
            "0:1:Life Type=1",
            "0:1:Life Duration=3600",
            "0:1:Encryption Algorithm=7",
            "0:1:Hash Algorithm=2",
            "0:1:Authentication Method=3",
            "0:1:Group Description=16",
            "0:1:Key Length=256",
            "0:1:Life Type=1",
            "0:1:Life Duration=3600",
            "0:1:Encryption Algorithm=7",
            "0:1:Hash Algorithm=2",
            "0:1:Authentication Method=3",
            "0:1:Group Description=15",
            "0:1:Key Length=256",
            "0:1:Life Type=1",
            "0:1:Life Duration=3600",
            "0:1:Encryption Algorithm=7",
            "0:1:Hash Algorithm=2",
            "0:1:Authentication Method=3",
            "0:1:Group Description=14",
            "0:1:Key Length=256",
            "0:1:Life Type=1",
            "0:1:Life Duration=3600",
            "0:1:Encryption Algorithm=7",
            "0:1:Hash Algorithm=2",
            "0:1:Authentication Method=3",
            "0:1:Group Description=5",
            "0:1:Key Length=256",
            "0:1:Life Type=1",
            "0:1:Life Duration=3600",
            "0:1:Encryption Algorithm=7",
            "0:1:Hash Algorithm=2",
            "0:1:Authentication Method=3",
            "0:1:Group Description=2",
            "0:1:Key Length=256"
        ],
        "length": 528,
        "hash": "682464bb389df0e313fa4f2699bf6a8f",
        "doi": 1,
        "situation": "\\x00\\x00\\x00\\x01"
    }
    ```



=== "kerberos"


    ```json
	{
        "_path": "kerberos",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T09:12:03.110000Z",
        "ts": "2026-09-15T09:12:02.848000Z",
        "uid": "CHhAvVGS1DHFjwGM9",
        "id.orig_h": "10.0.0.20",
        "id.orig_p": 52424,
        "id.resp_h": "10.0.0.5",
        "id.resp_p": 88,
        "request_type": "TGS",
        "client": "Alice/TEST.CORP",
        "service": "LDAP/dc.test.corp/test.corp",
        "success": true,
        "till": "2037-09-13T02:48:05.000000Z",
        "cipher": "aes256-cts-hmac-sha1-96",
        "forwardable": true,
        "renewable": true
    }
    ```



=== "kerberos_as_from"


    ```json
	{
        "_path": "kerberos",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CFSWdTgm5Sh77GIkHK",
        "id.orig_h": "192.168.1.31",
        "id.orig_p": 63576,
        "id.resp_h": "192.168.1.32",
        "id.resp_p": 88,
        "request_type": "AS",
        "client": "Alice/TEST.CORP",
        "service": "krbtgt/TEST.CORP",
        "success": true,
        "from": "2015-01-19T22:56:45.000000Z",
        "till": "2015-01-19T22:56:46.000000Z",
        "cipher": "aes256-cts-hmac-sha1-96",
        "forwardable": false,
        "renewable": false
    }
    ```



=== "kerberos_failure"


    ```json
	{
        "_path": "kerberos",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T09:15:44.000000Z",
        "ts": "2026-09-15T09:15:43.702000Z",
        "uid": "CWtRfY3bbnLpqZ4hK2",
        "id.orig_h": "10.0.0.20",
        "id.orig_p": 52501,
        "id.resp_h": "10.0.0.5",
        "id.resp_p": 88,
        "request_type": "AS",
        "client": "Bob",
        "service": "krbtgt/TEST.CORP",
        "success": false,
        "error_msg": "KDC_ERR_PREAUTH_FAILED",
        "cipher": "rc4-hmac",
        "forwardable": false,
        "renewable": false
    }
    ```



=== "kerberos_service_principal"


    ```json
	{
        "_path": "kerberos",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T09:12:03.110000Z",
        "ts": "2026-09-15T09:12:02.848000Z",
        "uid": "CkP8vR3mTw5Nx2Lq9s",
        "id.orig_h": "10.0.0.20",
        "id.orig_p": 52424,
        "id.resp_h": "10.0.0.5",
        "id.resp_p": 88,
        "request_type": "TGS",
        "client": "Service/Account/TEST.CORP",
        "service": "LDAP/dc.test.corp/test.corp",
        "success": true,
        "till": "2037-09-13T02:48:05.000000Z",
        "cipher": "aes256-cts-hmac-sha1-96",
        "forwardable": true,
        "renewable": true
    }
    ```



=== "known_certs"


    ```json
	{
        "_path": "known_certs",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T01:08:46.248324Z",
        "ts": "2026-09-18T01:01:34.497993Z",
        "duration": 42.31651592254639,
        "kuid": "KfIbVJqHisfH2",
        "host_ip": "192.168.88.60",
        "annotations": [],
        "hash": "5555555555555555555555555555555555555555",
        "port": 443,
        "protocol": "tcp",
        "serial": "0A0B0C0D0E0F1011",
        "subject": "CN=example.com,O=Test Org",
        "issuer_subject": "CN=example.com,O=Test Org",
        "num_instances": 3
    }
    ```



=== "known_devices"


    ```json
	{
        "_path": "known_devices",
        "_system_name": "sensor",
        "_write_ts": "2026-09-20T08:08:46.365787Z",
        "ts": "2026-09-20T08:05:24.725027Z",
        "duration": 0.0,
        "kuid": "KfQZre3HMaUM5",
        "host_ip": "172.16.56.13",
        "annotations": [],
        "mac": "02:00:00:00:00:03",
        "vendor_mac": "Randomized",
        "protocols": [
            "DHCP"
        ],
        "num_instances": 1
    }
    ```



=== "known_domains"


    ```json
	{
        "_path": "known_domains",
        "_system_name": "sensor",
        "_write_ts": "2026-09-20T08:08:46.365787Z",
        "ts": "2026-09-20T08:05:24.725027Z",
        "duration": 0.0,
        "kuid": "KfQZre3HMaUM5",
        "host_ip": "172.16.56.13",
        "annotations": [],
        "domain": "example.com",
        "protocols": [
            "DHCP"
        ],
        "num_instances": 1
    }
    ```



=== "known_hosts"


    ```json
	{
        "_path": "known_hosts",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:38:46.290087Z",
        "ts": "2026-09-18T19:29:00.115695Z",
        "duration": 0.003679990768432617,
        "kuid": "KfeDvcHGTyOW4",
        "host_ip": "10.21.0.100",
        "annotations": [],
        "long_conns": 0,
        "n_opened": 1,
        "n_closed": 1,
        "n_pending": 0
    }
    ```



=== "known_names"


    ```json
	{
        "_path": "known_names",
        "_system_name": "sensor",
        "_write_ts": "2026-09-20T08:08:46.365787Z",
        "ts": "2026-09-20T08:05:24.725027Z",
        "duration": 0.0,
        "kuid": "KfQZre3HMaUM5",
        "host_ip": "172.16.56.13",
        "annotations": [],
        "hostname": "hostname",
        "protocols": [
            "DHCP"
        ],
        "num_instances": 1
    }
    ```



=== "known_services"


    ```json
	{
        "_path": "known_services",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T01:23:46.250370Z",
        "ts": "2026-09-18T01:07:52.205146Z",
        "duration": 20.859540939331055,
        "kuid": "KfwQvq45Dc98c",
        "host_ip": "192.168.88.115",
        "annotations": [],
        "port_num": 80,
        "protocol": "tcp",
        "service": [
            "HTTP"
        ],
        "software": [
            "GoAhead-Webs"
        ],
        "app": [
            "firefox",
            "mozilla",
            "linux"
        ],
        "num_conns_pending": -4,
        "num_conns_complete": 33
    }
    ```



=== "known_users"


    ```json
	{
        "_path": "known_users",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T12:47:13.389168Z",
        "ts": "2026-09-15T12:39:53.349167Z",
        "duration": 1.1437749862670898,
        "kuid": "KfMEORvw7EwD2",
        "host_ip": "10.0.35.10",
        "annotations": [],
        "server_ip": "192.168.100.10",
        "user": "Administrator",
        "protocol": "NTLM",
        "num_instances": 25
    }
    ```



=== "ldap"


    ```json
	{
        "_path": "ldap",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T11:31:07.640000Z",
        "ts": "2026-09-15T11:31:07.412000Z",
        "uid": "CqlBEt1z5A9mTAZ3Sh",
        "id.orig_h": "10.0.0.20",
        "id.orig_p": 49234,
        "id.resp_h": "10.0.0.5",
        "id.resp_p": 389,
        "message_id": 1,
        "version": 3,
        "opcode": "bind simple",
        "result": "success",
        "object": "cn=Administrator,dc=test,dc=corp",
        "argument": "REDACTED"
    }
    ```



=== "ldap_bind_failure"


    ```json
	{
        "_path": "ldap",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T11:35:02.000000Z",
        "ts": "2026-09-15T11:35:01.884000Z",
        "uid": "CpQ8nR4xxZmVbT1aL9",
        "id.orig_h": "10.0.0.20",
        "id.orig_p": 49301,
        "id.resp_h": "10.0.0.5",
        "id.resp_p": 389,
        "message_id": 1,
        "version": 3,
        "opcode": "bind simple",
        "result": "invalid credentials",
        "object": "cn=Bob,dc=test,dc=corp",
        "argument": "REDACTED"
    }
    ```



=== "ldap_sasl_bind_failure"


    ```json
	{
        "_path": "ldap",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "ClG3AP03J0yYDe0HiR",
        "id.orig_h": "192.168.66.141",
        "id.orig_p": 53653,
        "id.resp_h": "192.168.66.138",
        "id.resp_p": 389,
        "message_id": 66,
        "version": 3,
        "opcode": "bind SASL",
        "result": "invalid credentials",
        "diagnostic_message": "8009030C: LdapErr: DSID-0C090569, comment: AcceptSecurityContext error, data 52e, v4563?",
        "argument": "GSS-SPNEGO"
    }
    ```



=== "ldap_sasl_bind_success"


    ```json
	{
        "_path": "ldap",
        "_system_name": "sensor",
        "_write_ts": "2026-11-04T09:09:34.003241Z",
        "argument": "GSS-SPNEGO",
        "id.orig_h": "203.0.113.10",
        "id.orig_p": 53093,
        "id.resp_h": "203.0.113.11",
        "id.resp_p": 389,
        "message_id": 3,
        "opcode": "bind SASL",
        "result": "success",
        "ts": "2026-11-04T09:09:33.803182Z",
        "uid": "Cqyc171UEWVcFy8eEa",
        "version": 3
    }
    ```



=== "ldap_sasl_in_progress"


    ```json
	{
        "_path": "ldap",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T11:31:07.640000Z",
        "ts": "2026-09-15T11:31:07.412000Z",
        "uid": "ClS2wK7nQx4Pm9Rv3t",
        "id.orig_h": "10.0.0.20",
        "id.orig_p": 49234,
        "id.resp_h": "10.0.0.5",
        "id.resp_p": 389,
        "message_id": 1,
        "version": 3,
        "opcode": "bind SASL",
        "result": "sasl bind in progress",
        "object": ""
    }
    ```



=== "ldap_search"


    ```json
	{
        "_path": "ldap_search",
        "_system_name": "sensor",
        "_write_ts": "2026-11-04T09:09:44.908040Z",
        "base_object": "dc=test,dc=corp",
        "deref_aliases": "never",
        "filter": "(objectcategory=group)",
        "id.orig_h": "203.0.113.10",
        "id.orig_p": 53093,
        "id.resp_h": "203.0.113.11",
        "id.resp_p": 389,
        "message_id": 8,
        "result": "success",
        "result_count": 51,
        "scope": "tree",
        "ts": "2026-11-04T09:09:40.903220Z",
        "uid": "Cqyc171UEWVcFy8eEa"
    }
    ```



=== "ldap_search_attributes"


    ```json
	{
        "_path": "ldap_search",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CJk6ZhFnHsOISFSNVS",
        "id.orig_h": "10.0.0.1",
        "id.orig_p": 25936,
        "id.resp_h": "10.0.0.2",
        "id.resp_p": 3268,
        "message_id": 2,
        "scope": "tree",
        "deref_aliases": "always",
        "base_object": "DC=xx,DC=xxx,DC=xxxxx,DC=net",
        "result_count": 1,
        "result": "success",
        "filter": "(&(objectclass=*)(sAMAccountName=xxxxxxxx))",
        "attributes": [
            "sAMAccountName"
        ]
    }
    ```



=== "ldap_search_no_such_object"


    ```json
	{
        "_path": "ldap_search",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CXl5nsJCmq3WzXfJHz",
        "id.orig_h": "10.199.2.121",
        "id.orig_p": 59356,
        "id.resp_h": "10.199.2.111",
        "id.resp_p": 389,
        "message_id": 11,
        "scope": "base",
        "deref_aliases": "never",
        "base_object": "CN=00000000-0000-0000-0000-000000000000,CN=Device Registration Configuration,CN=services,CN=Configuration,DC=test,DC=corp",
        "result_count": 0,
        "result": "no such object",
        "diagnostic_message": "0000208D: NameErr: DSID-0310028B, problem 2001 (NO_OBJECT), data 0, best match of:??'CN=Services,CN=Configuration,DC=test,DC=corp'??",
        "filter": "(ObjectClass=*)"
    }
    ```



=== "ldap_unbind"


    ```json
	{
        "_path": "ldap",
        "_system_name": "sensor",
        "_write_ts": "2026-11-04T09:09:45.103206Z",
        "id.orig_h": "203.0.113.10",
        "id.orig_p": 53093,
        "id.resp_h": "203.0.113.11",
        "id.resp_p": 389,
        "message_id": 9,
        "opcode": "unbind",
        "ts": "2026-11-04T09:09:45.103206Z",
        "uid": "Cqyc171UEWVcFy8eEa"
    }
    ```



=== "modbus"


    ```json
	{
        "_path": "modbus",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:34:24.069673Z",
        "ts": "2026-09-18T00:34:24.069673Z",
        "uid": "Cz5vqh2PP45bzYCeoa",
        "id.orig_h": "192.168.2.42",
        "id.orig_p": 59470,
        "id.resp_h": "192.168.88.100",
        "id.resp_p": 502,
        "tid": 0,
        "unit": 255,
        "func": "ENCAP_INTERFACE_TRANSPORT_EXCEPTION",
        "pdu_type": "RESP",
        "exception": "SLAVE_DEVICE_FAILURE"
    }
    ```



=== "modbus_detailed"


    ```json
	{
        "_path": "modbus_detailed",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:01:02.037097Z",
        "ts": "2026-09-18T19:01:02.037097Z",
        "uid": "CzOjlp44fnm5T03Ro4",
        "id.orig_h": "10.21.0.150",
        "id.orig_p": 51411,
        "id.resp_h": "10.21.0.100",
        "id.resp_p": 502,
        "is_orig": false,
        "tid": 19828,
        "unit": 255,
        "func": "WRITE_SINGLE_REGISTER",
        "request_response": "RESPONSE",
        "address": 100,
        "quantity": 1,
        "values": "0"
    }
    ```



=== "modbus_read_device_identification"


    ```json
	{
        "_path": "modbus_read_device_identification",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:34:23.767695Z",
        "ts": "2026-09-18T00:34:23.767695Z",
        "uid": "Cz5vqh2PP45bzYCeoa",
        "id.orig_h": "192.168.2.42",
        "id.orig_p": 59470,
        "id.resp_h": "192.168.88.100",
        "id.resp_p": 502,
        "is_orig": true,
        "tid": 0,
        "unit": 255,
        "func": "ENCAP_INTERFACE_TRANSPORT",
        "request_response": "REQUEST",
        "mei_type": "READ-DEVICE-IDENTIFICATION",
        "device_id_code": 1,
        "object_id_code": "0x00",
        "object_id": "Basic Device Identification"
    }
    ```



=== "mysql"


    ```json
	{
        "_path": "mysql",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T12:43:43.825056Z",
        "ts": "2026-09-15T12:43:43.825056Z",
        "uid": "CoIqCh3NW96MbSfeZe",
        "id.orig_h": "172.27.0.137",
        "id.orig_p": 42802,
        "id.resp_h": "172.28.0.18",
        "id.resp_p": 3306,
        "cmd": "query",
        "arg": "LOCK TABLES `user` READ, `db` READ, `proc` READ",
        "success": true,
        "rows": 0
    }
    ```



=== "mysql_failure"


    ```json
	{
        "_path": "mysql",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CnbfyWk8vYzyctr16h",
        "id.orig_h": "192.168.1.3",
        "id.orig_p": 55845,
        "id.resp_h": "192.168.1.8",
        "id.resp_p": 3306,
        "cmd": "login",
        "arg": "root_nope",
        "success": false,
        "response": "Access denied for user 'root_nope'@'hostname' (using password: NO)"
    }
    ```



=== "notice"


    ```json
	{
        "_path": "notice",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:20:18.552640Z",
        "uid": "CnoticeTest1",
        "id.orig_h": "10.0.35.10",
        "id.resp_h": "192.168.100.10",
        "note": "ATTACK::Lateral_Movement",
        "msg": "SMB::FILE_WRITE to admin file share",
        "sub": "Saved a copy of the file written to SMB admin file share"
    }
    ```



=== "notice_file_desc"


    ```json
	{
        "_path": "notice",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CvatMSNltCec7ErQUa",
        "id.orig_h": "127.0.0.1",
        "id.orig_p": 48770,
        "id.resp_h": "127.0.0.1",
        "id.resp_p": 8080,
        "fuid": "FDXrtA2UOyNDs2wzk8",
        "file_mime_type": "text/plain",
        "file_desc": "http://localhost:8080:8080/zeek.txt",
        "proto": "tcp",
        "note": "NoticeTestType",
        "msg": "test",
        "src": "127.0.0.1",
        "dst": "127.0.0.1",
        "p": 8080,
        "actions": [
            "Notice::ACTION_LOG"
        ],
        "email_dest": [],
        "suppress_for": 3600.0
    }
    ```



=== "notice_no_connection"


    ```json
	{
        "_path": "notice",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:31.517644Z",
        "ts": "2026-09-18T19:05:31.517644Z",
        "note": "Scan::Address_Scan",
        "msg": "10.21.0.100 scanned at least 222 unique hosts on ports 449/tcp, 25/tcp, 587/tcp, 465/tcp, 26/tcp in 0m1s",
        "sub": "local",
        "src": "10.21.0.100",
        "peer_descr": "proxy-1",
        "actions": [
            "Notice::ACTION_LOG"
        ],
        "suppress_for": 3600.0,
        "severity.level": 3,
        "severity.name": "error"
    }
    ```



=== "ntlm"


    ```json
	{
        "_path": "ntlm",
        "_system_name": "sensor",
        "_write_ts": "2026-11-04T08:55:36.697668Z",
        "domainname": "TEST",
        "hostname": "hostname",
        "id.orig_h": "10.0.35.10",
        "id.orig_p": 42851,
        "id.resp_h": "192.168.100.10",
        "id.resp_p": 445,
        "server_dns_computer_name": "dc.test.corp",
        "server_nb_computer_name": "DC",
        "server_tree_name": "test.corp",
        "success": true,
        "ts": "2026-11-04T08:55:36.690907Z",
        "uid": "CmMroS157SAYhCDUXa",
        "username": "Administrator"
    }
    ```



=== "ntlm_failure"


    ```json
	{
        "_path": "ntlm",
        "_system_name": "sensor",
        "_write_ts": "2026-11-04T08:55:36.697668Z",
        "domainname": "TEST",
        "hostname": "hostname",
        "id.orig_h": "10.0.35.10",
        "id.orig_p": 42851,
        "id.resp_h": "192.168.100.10",
        "id.resp_p": 445,
        "server_dns_computer_name": "dc.test.corp",
        "server_nb_computer_name": "DC",
        "server_tree_name": "test.corp",
        "success": false,
        "ts": "2026-11-04T08:55:36.690907Z",
        "uid": "CbN5tR8wKx2Lm4Qz7p",
        "username": "Bob"
    }
    ```



=== "ntp"


    ```json
	{
        "_path": "ntp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:02:44.409272Z",
        "ts": "2026-09-16T08:02:44.409272Z",
        "uid": "CoIcCQ3OPiWDL87yoa",
        "id.orig_h": "172.27.0.137",
        "id.orig_p": 45125,
        "id.resp_h": "192.0.2.56",
        "id.resp_p": 123,
        "version": 4,
        "mode": 4,
        "stratum": 2,
        "poll": 128.0,
        "precision": 2.9802322387695312e-08,
        "root_delay": 0.0011444091796875,
        "root_disp": 0.0002899169921875,
        "ref_id": "192.0.2.249",
        "ref_time": "2023-11-15T21:50:49.980112Z",
        "org_time": "1932-01-13T13:06:48.872473Z",
        "rec_time": "2023-11-15T21:51:34.234660Z",
        "xmt_time": "2023-11-15T21:51:34.236187Z",
        "num_exts": 0
    }
    ```



=== "ocsp"


    ```json
	{
        "_path": "ocsp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:05:40.877987Z",
        "ts": "2026-09-16T08:05:40.877987Z",
        "id": "FQJlZO34CUdUG3F7Ke",
        "hashAlgorithm": "sha1",
        "issuerNameHash": "9999999999999999999999999999999999999999",
        "issuerKeyHash": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "serialNumber": "0102030405060708090A0B0C0D0E0F1011",
        "certStatus": "good",
        "thisUpdate": "2023-03-26T02:14:09.000000Z",
        "nextUpdate": "2023-04-01T15:50:13.000000Z"
    }
    ```



=== "ocsp_revoked"


    ```json
	{
        "_path": "ocsp",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "id": "Fv1Mrl4zObGy9drLdg",
        "hashAlgorithm": "sha1",
        "issuerNameHash": "6666666666666666666666666666666666666666",
        "issuerKeyHash": "7777777777777777777777777777777777777777",
        "serialNumber": "0102030405060708090A0B0C0D0E0F10",
        "certStatus": "revoked",
        "revoketime": "2015-05-14T14:58:49.000000Z",
        "revokereason": "superseded",
        "thisUpdate": "2015-07-07T16:28:34.000000Z",
        "nextUpdate": "2015-09-29T01:12:42.000000Z"
    }
    ```



=== "pe"


    ```json
	{
        "_path": "pe",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:05:10.682362Z",
        "ts": "2026-09-16T08:05:10.638487Z",
        "id": "FM5pNQ1btziw6Awvd9",
        "machine": "AMD64",
        "compile_ts": "2022-08-10T15:07:27.000000Z",
        "os": "Windows Vista or Server 2008",
        "subsystem": "WINDOWS_GUI",
        "is_exe": true,
        "is_64bit": true,
        "uses_aslr": true,
        "uses_dep": true,
        "uses_code_integrity": false,
        "uses_seh": true,
        "has_import_table": true,
        "has_export_table": true,
        "has_cert_table": false,
        "has_debug_data": true,
        "section_names": [
            ".text",
            ".rdata",
            ".data",
            ".pdata",
            "_RDATA",
            ".rsrc",
            ".reloc"
        ]
    }
    ```



=== "quic"


    ```json
	{
        "_path": "quic",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:18:35.887387Z",
        "ts": "2026-09-16T08:16:41.482170Z",
        "uid": "CptgZT35pzG9XrPOpa",
        "id.orig_h": "10.8.21.248",
        "id.orig_p": 64972,
        "id.resp_h": "192.0.2.147",
        "id.resp_p": 443,
        "version": "1",
        "client_initial_dcid": "97b214c00a8018c9",
        "client_scid": "",
        "server_scid": "4b4ea0bd0600d632",
        "server_name": "www.example.com",
        "client_protocol": "h3",
        "history": "IISiiishhhhHHHIIiiihhhhHHH"
    }
    ```



=== "quic_client_scid"


    ```json
	{
        "_path": "quic",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CMOcJrtyrjFVGQAKiB",
        "id.orig_h": "2001:db8::10",
        "id.orig_p": 39264,
        "id.resp_h": "2001:db8::443",
        "id.resp_p": 443,
        "version": "1",
        "client_initial_dcid": "ceef7990f5bb4071",
        "client_scid": "1e6dc7",
        "server_scid": "eeef7990f5bb4071",
        "server_name": "www.example.com",
        "client_protocol": "h3",
        "history": "IXIXISZXiiiiishooIHOOoO"
    }
    ```



=== "rdp"


    ```json
	{
        "_path": "rdp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:05:03.785143Z",
        "ts": "2026-09-16T08:04:58.764985Z",
        "uid": "CJwawf4ZWYkQ8ZV0il",
        "id.orig_h": "192.168.100.11",
        "id.orig_p": 41301,
        "id.resp_h": "192.168.200.201",
        "id.resp_p": 3389,
        "cookie": "hello",
        "result": "encrypted",
        "security_protocol": "HYBRID",
        "cert_count": 0,
        "auth_success": false,
        "channels_joined": 0,
        "inferences": []
    }
    ```



=== "rdp_client_info"


    ```json
	{
        "_path": "rdp",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "C7EDYMhVXCahaiTaQF",
        "id.orig_h": "192.168.1.1",
        "id.orig_p": 54990,
        "id.resp_h": "192.168.1.2",
        "id.resp_p": 3389,
        "cookie": "hostname",
        "result": "Success",
        "security_protocol": "RDP",
        "client_channels": [
            "rdpdr",
            "rdpsnd",
            "cliprdr",
            "drdynvc"
        ],
        "keyboard_layout": "English - United States",
        "client_build": "RDP 8.1",
        "client_name": "hostname",
        "client_dig_product_id": "3c571ed0-3415-474b-ae94-74e151b",
        "desktop_width": 1920,
        "desktop_height": 1080,
        "requested_color_depth": "16bit",
        "cert_type": "X.509",
        "cert_count": 2,
        "cert_permanent": false,
        "encryption_level": "Client compatible",
        "encryption_method": "128bit"
    }
    ```



=== "rdp_fingerprint"


    ```json
	{
        "_path": "rdp",
        "_system_name": "sensor",
        "_write_ts": "2024-10-16T04:18:12.066275Z",
        "cert_count": 1,
        "cert_permanent": true,
        "cert_type": "RSA",
        "channels_joined": 0,
        "client_build": "RDP 5.1",
        "client_channels": [
            "cliprdr"
        ],
        "client_dig_product_id": "3c571ed0-3415-474b-ae94-74e151b",
        "client_name": "hostname",
        "cookie": "hello",
        "desktop_height": 600,
        "desktop_width": 800,
        "encryption_level": "Client compatible",
        "encryption_method": "128bit",
        "id.orig_h": "192.168.202.16",
        "id.orig_p": 52593,
        "id.resp_h": "192.168.2.100",
        "id.resp_p": 3389,
        "inferences": [],
        "keyboard_layout": "English - United States",
        "rdfp_hash": "27956f914067e63f3dba1e7d563e0e86",
        "rdfp_string": "4,8,00000003,00000009,00000000,cliprdr:0000a0c0",
        "requested_color_depth": "24bit",
        "result": "Success",
        "security_protocol": "RDP",
        "ts": "2024-10-16T04:18:00.877142Z",
        "uid": "CBwC08Nbefm4DZcaCT"
    }
    ```



=== "rdp_success"


    ```json
	{
        "_path": "rdp",
        "_system_name": "sensor",
        "_write_ts": "2026-11-04T09:28:47.509468Z",
        "auth_success": true,
        "cert_count": 0,
        "channels_joined": 6,
        "cookie": "admin",
        "id.orig_h": "192.168.1.106",
        "id.orig_p": 55358,
        "id.resp_h": "192.168.1.134",
        "id.resp_p": 3389,
        "inferences": [
            "APWA"
        ],
        "result": "encrypted",
        "security_protocol": "SSL",
        "ts": "2026-11-04T09:23:47.284392Z",
        "uid": "CF0fgU2XfZz1PUkjwj"
    }
    ```



=== "s7comm"


    ```json
	{
        "_path": "s7comm",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:56:31.991373Z",
        "ts": "2026-09-18T00:56:31.991373Z",
        "uid": "CyNPSM27IwqixmEVy8",
        "id.orig_h": "10.10.10.30",
        "id.orig_p": 49159,
        "id.resp_h": "10.10.10.10",
        "id.resp_p": 102,
        "is_orig": false,
        "rosctr_code": 3,
        "rosctr_name": "ACK-Data",
        "pdu_reference": 2306,
        "function_code": "0x05",
        "function_name": "Write Variable",
        "error_class": "No error",
        "error_code": "0x00"
    }
    ```



=== "s7comm_read_szl"


    ```json
	{
        "_path": "s7comm_read_szl",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:34:08.836543Z",
        "ts": "2026-09-18T00:34:08.836543Z",
        "uid": "CxCEHu3aqc47vfonEh",
        "id.orig_h": "192.168.2.42",
        "id.orig_p": 45148,
        "id.resp_h": "192.168.88.30",
        "id.resp_p": 102,
        "is_orig": true,
        "pdu_reference": 0,
        "method": "Request",
        "szl_id": "0x001c",
        "szl_id_name": "Component Identification",
        "szl_index": "0x0001",
        "return_code": "0xff",
        "return_code_name": "Success"
    }
    ```



=== "s7comm_user_data"


    ```json
	{
        "_path": "s7comm",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "Cw9tU9ISm9xwr1cFLR",
        "id.orig_h": "203.0.113.131",
        "id.orig_p": 51212,
        "id.resp_h": "203.0.113.211",
        "id.resp_p": 102,
        "is_orig": true,
        "source_h": "203.0.113.131",
        "source_p": 51212,
        "destination_h": "203.0.113.211",
        "destination_p": 102,
        "rosctr_code": 7,
        "rosctr_name": "User-Data",
        "pdu_reference": 1,
        "function_code": "0x44",
        "function_name": "Request: CPU Functions",
        "subfunction_code": "0x01",
        "subfunction_name": "Read SZL"
    }
    ```



=== "smb_files"


    ```json
	{
        "_path": "smb_files",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:13:36.555745Z",
        "ts": "2026-09-16T08:12:48.590051Z",
        "uid": "Cni6904jWHeOt0LsBc",
        "id.orig_h": "10.21.0.102",
        "id.orig_p": 53003,
        "id.resp_h": "10.21.0.103",
        "id.resp_p": 445,
        "fuid": "FDcDVw23etbV9dhIBj",
        "action": "SMB::FILE_WRITE",
        "object_path": "\\\\wef.test.corp\\pslogs",
        "name": "20230329\\PowerShell_transcript.DC.20230329130820.txt",
        "size": 0,
        "times.modified": "2023-03-29T13:08:20.904013Z",
        "times.accessed": "2023-03-29T13:08:20.904013Z",
        "times.created": "2023-03-29T13:08:20.904013Z",
        "times.changed": "2023-03-29T13:08:20.904013Z",
        "data_offset_req": 7340032,
        "data_len_req": 4177
    }
    ```



=== "smb_files_delete"


    ```json
	{
        "_path": "smb_files",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:13:36.555745Z",
        "ts": "2026-09-16T08:12:48.590051Z",
        "uid": "CsD4lV9pRm3Kx7Qn2w",
        "id.orig_h": "10.21.0.102",
        "id.orig_p": 53003,
        "id.resp_h": "10.21.0.103",
        "id.resp_p": 445,
        "fuid": "FdL6tW3nPq9Rk2Mx5s",
        "action": "SMB::FILE_DELETE",
        "object_path": "\\\\wef.test.corp\\pslogs",
        "name": "20230329\\PowerShell_transcript.DC.20230329130820.txt",
        "size": 0,
        "times.modified": "2023-03-29T13:08:20.904013Z",
        "times.accessed": "2023-03-29T13:08:20.904013Z",
        "times.created": "2023-03-29T13:08:20.904013Z",
        "times.changed": "2023-03-29T13:08:20.904013Z"
    }
    ```



=== "smb_files_open"


    ```json
	{
        "_path": "smb_files",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:13:36.555745Z",
        "ts": "2026-09-16T08:12:48.590051Z",
        "uid": "CsB3nW7qKx5Rm2Tv8p",
        "id.orig_h": "10.21.0.102",
        "id.orig_p": 53003,
        "id.resp_h": "10.21.0.103",
        "id.resp_p": 445,
        "fuid": "FaO1pN4wLq7Xs2Vm9k",
        "action": "SMB::FILE_OPEN",
        "object_path": "\\\\wef.test.corp\\pslogs",
        "name": "20230329\\PowerShell_transcript.DC.20230329130820.txt",
        "size": 0,
        "times.modified": "2023-03-29T13:08:20.904013Z",
        "times.accessed": "2023-03-29T13:08:20.904013Z",
        "times.created": "2023-03-29T13:08:20.904013Z",
        "times.changed": "2023-03-29T13:08:20.904013Z"
    }
    ```



=== "smb_files_read"


    ```json
	{
        "_path": "smb_files",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:13:36.555745Z",
        "ts": "2026-09-16T08:12:48.590051Z",
        "uid": "CsR8kT2vNq6Wx4Lm1b",
        "id.orig_h": "10.21.0.102",
        "id.orig_p": 53003,
        "id.resp_h": "10.21.0.103",
        "id.resp_p": 445,
        "fuid": "FrE5dQ2mKw8Tn3Xp6v",
        "action": "SMB::FILE_READ",
        "object_path": "\\\\wef.test.corp\\pslogs",
        "name": "20230329\\PowerShell_transcript.DC.20230329130820.txt",
        "size": 0,
        "times.modified": "2023-03-29T13:08:20.904013Z",
        "times.accessed": "2023-03-29T13:08:20.904013Z",
        "times.created": "2023-03-29T13:08:20.904013Z",
        "times.changed": "2023-03-29T13:08:20.904013Z",
        "data_offset_req": 0,
        "data_len_req": 4177
    }
    ```



=== "smb_files_response"


    ```json
	{
        "_path": "smb_files",
        "_system_name": "sensor",
        "_write_ts": "2026-09-17T23:16:39.774111Z",
        "ts": "2026-09-17T23:16:39.759981Z",
        "uid": "CFSUqq2ugHLFiHvv3d",
        "id.orig_h": "10.0.35.10",
        "id.orig_p": 42851,
        "id.resp_h": "192.168.100.10",
        "id.resp_p": 445,
        "action": "SMB::FILE_WRITE",
        "object_path": "IPC$",
        "name": "\\srvsvc",
        "size": 0,
        "data_offset_req": 0,
        "data_len_req": 100,
        "data_len_rsp": 100
    }
    ```



=== "smb_mapping"


    ```json
	{
        "_path": "smb_mapping",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:01:03.736402Z",
        "ts": "2026-09-16T08:01:03.733426Z",
        "uid": "ClulJU11FBv30eWZb9",
        "id.orig_h": "10.0.35.10",
        "id.orig_p": 34401,
        "id.resp_h": "192.168.100.10",
        "id.resp_p": 445,
        "object_path": "Network Share 1",
        "service": "A:",
        "native_file_system": "NTFS",
        "share_type": "DISK"
    }
    ```



=== "smb_mapping_disk"


    ```json
	{
        "_path": "smb_mapping",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CbdsKeolsv2JINBV1x",
        "id.orig_h": "10.0.0.11",
        "id.orig_p": 49208,
        "id.resp_h": "10.0.0.12",
        "id.resp_p": 445,
        "path": "\\\\\\\\10.0.0.12\\\\smb2",
        "share_type": "DISK"
    }
    ```



=== "smtp"


    ```json
	{
        "_path": "smtp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:30.841247Z",
        "ts": "2026-09-18T19:05:30.831201Z",
        "uid": "CIR9eO1756JR3H7Gdg",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 49412,
        "id.resp_h": "192.0.2.25",
        "id.resp_p": 2525,
        "trans_depth": 6,
        "helo": "[192.0.2.25]",
        "mailfrom": "bounce-538234@example.com",
        "rcptto": [
            "bob@example.com"
        ],
        "date": "Wed, 18 Sep 2019 17:33:45 +0000",
        "from": "alice@example.com",
        "to": [
            "bob@example.com"
        ],
        "subject": "RE: Premium audit request for policy 538234 - reply to bob@example.com",
        "last_reply": "250 2.0.0 Ok: queued as 41B223E838",
        "path": [
            "192.0.2.25",
            "10.21.0.100"
        ],
        "tls": false,
        "fuids": [
            "FliSuU3BtqLMkTQDId",
            "FK2yZt1ycPDgSy6iOg"
        ],
        "is_webmail": false,
        "urls": [
            "https://www.example.com/track/open.php?u=6d752b423e19561c&id=d4ae017d43",
            "https://gallery.example.com/6d752b423e19561c/images/71aaf10a.png"
        ],
        "domains": [
            "www.example.com",
            "gallery.example.com"
        ]
    }
    ```



=== "smtp_display_name"


    ```json
	{
        "_path": "smtp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:30.841247Z",
        "ts": "2026-09-18T19:05:30.831201Z",
        "uid": "CsM6nQ2vKw9Tx4Rp8l",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 49412,
        "id.resp_h": "192.0.2.25",
        "id.resp_p": 2525,
        "trans_depth": 6,
        "helo": "[192.0.2.25]",
        "mailfrom": "bounce-538234@example.com",
        "rcptto": [
            "bob@example.com"
        ],
        "date": "Wed, 18 Sep 2019 17:33:45 +0000",
        "from": "\"Alice\" <alice@example.com>",
        "to": [
            "\"Bob\" <bob@example.com>",
            "charlie@example.com"
        ],
        "subject": "RE: Premium audit request for policy 538234 - reply to bob@example.com",
        "last_reply": "250 2.0.0 Ok: queued as 41B223E838",
        "path": [
            "192.0.2.25",
            "10.21.0.100"
        ],
        "tls": false,
        "fuids": [
            "FliSuU3BtqLMkTQDId",
            "FK2yZt1ycPDgSy6iOg"
        ],
        "is_webmail": false,
        "urls": [
            "https://www.example.com/track/open.php?u=6d752b423e19561c&id=d4ae017d43",
            "https://gallery.example.com/6d752b423e19561c/images/71aaf10a.png"
        ],
        "domains": [
            "www.example.com",
            "gallery.example.com"
        ],
        "cc": [
            "\"Dave\" <dave@example.com>"
        ],
        "reply_to": "\"Alice\" <alice@example.com>"
    }
    ```



=== "smtp_links"


    ```json
	{
        "_path": "smtp_links",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:30.811849Z",
        "ts": "2026-09-18T19:05:30.811849Z",
        "uid": "CIR9eO1756JR3H7Gdg",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 49412,
        "id.resp_h": "192.0.2.25",
        "id.resp_p": 2525,
        "fuid": "F9VVXl2pMdwD5HImb2",
        "link": "https://www.example.com/newsletter/2019-09/notice.html",
        "domain": "www.example.com"
    }
    ```



=== "smtp_received_headers"


    ```json
	{
        "_path": "smtp",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CGR4YFw9R8zYXt9Obs",
        "id.orig_h": "203.0.113.18",
        "id.orig_p": 56074,
        "id.resp_h": "203.0.113.83",
        "id.resp_p": 25,
        "trans_depth": 1,
        "helo": "mail.example.com",
        "mailfrom": "list-owner@example.com",
        "rcptto": [
            "bob@example.com"
        ],
        "date": "Thu, 4 Mar 2021 11:38:56 +0200",
        "from": "Alice <alice@example.com>",
        "to": [
            "Bob <bob@example.com>"
        ],
        "cc": [
            "Charlie <charlie@example.com>",
            "open list <list@example.com>",
            "Dave <dave@example.com>",
            "\"erin@example.com\" <erin@example.com>",
            "Alice <alice@example.org>"
        ],
        "msg_id": "<0123456789abcdef@mail.example.com>",
        "in_reply_to": "<20210303163125.0123456789abcdef@example.com>",
        "subject": "Re: [PATCH 1/2] Example patch",
        "first_received": "by mail.example.com with SMTP id 0123456789abcdef        for <list@example.com>; Thu, 04 Mar 2021 01:39:13 -0800 (PST)",
        "second_received": "from mail.example.com (mail.example.com [IPv6:2001:db8::42f])        by relay.example.com (Postfix) with ESMTPS id 0123456789AB        for <list@example.com>; Thu,  4 Mar 2021 01:39:13 -0800 (PST)",
        "last_reply": "250 OK id=1lHkUh-008hPw-NY",
        "path": [
            "203.0.113.83",
            "203.0.113.18",
            "203.0.113.19"
        ],
        "tls": false,
        "fuids": [
            "FnJaFv4OCDjqLe4uN1"
        ]
    }
    ```



=== "snmp"


    ```json
	{
        "_path": "snmp",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T00:34:22.132778Z",
        "ts": "2026-09-18T00:33:21.923946Z",
        "uid": "CR7kAN3nzDsifTWZIa",
        "id.orig_h": "192.168.2.22",
        "id.orig_p": 57279,
        "id.resp_h": "192.168.88.30",
        "id.resp_p": 161,
        "duration": 0.20161914825439453,
        "version": "1",
        "community": "public",
        "get_requests": 134,
        "get_bulk_requests": 0,
        "get_responses": 134,
        "set_requests": 0,
        "display_string": "Siemens, SIMATIC S7, CPU-1200, 6ES7 212-1BD30-0XB0, 1, V.1.0.1",
        "up_since": "2026-09-17T00:33:49.728050Z"
    }
    ```



=== "software"


    ```json
	{
        "_path": "software",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:01:01.968683Z",
        "ts": "2026-09-16T08:01:01.954147Z",
        "host_header": "10.0.35.10",
        "host_p": 8080,
        "software_type": "HTTP::SERVER",
        "name": "Apache",
        "version.major": 2,
        "version.minor": 2,
        "version.minor2": 14,
        "version.addl": "Ubuntu",
        "unparsed_version": "Apache/2.2.14 (Ubuntu) mod_mono/2.4.3 PHP/5.3.2-1ubuntu4.5 with Suhosin-Patch proxy_html/3.0.1 mod_python/3.3.1 Python/2.6.5 mod_ssl/2.2.14 OpenSSL/0.9.8k Phusion_Passenger/3.0.17 mod_perl/2.0.4 Perl/v5.10.1"
    }
    ```



=== "ssh"


    ```json
	{
        "_path": "ssh",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T12:41:07.520466Z",
        "ts": "2026-09-15T12:40:57.846906Z",
        "uid": "C90gJN25ZpBCXlNPOh",
        "id.orig_h": "192.0.2.50",
        "id.orig_p": 62977,
        "id.resp_h": "10.0.0.10",
        "id.resp_p": 22,
        "community_id": "1:mOZsn4tEbX5ejO4M5OU1ifERz6U=",
        "version": 2,
        "auth_success": true,
        "auth_attempts": 3,
        "direction": "INBOUND",
        "client": "SSH-2.0-OpenSSH_9.0",
        "server": "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.4",
        "cipher_alg": "chacha20-poly1305@openssh.com",
        "mac_alg": "umac-64-etm@openssh.com",
        "compression_alg": "none",
        "kex_alg": "sntrup761x25519-sha512@openssh.com",
        "host_key_alg": "ssh-ed25519",
        "host_key": "00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff",
        "hassh": "78c05d999799066a2b4554ce7b1585a6",
        "hasshServer": "699519fdcc30cbcd093d5cd01e4b1d56",
        "hasshVersion": "1.0",
        "hasshAlgorithms": "sntrup761x25519-sha512@openssh.com,curve25519-sha256;chacha20-poly1305@openssh.com,aes128-ctr;umac-64-etm@openssh.com,hmac-sha2-256;none,zlib",
        "hasshServerAlgorithms": "curve25519-sha256,ecdh-sha2-nistp256;chacha20-poly1305@openssh.com,aes128-ctr;umac-64-etm@openssh.com,hmac-sha2-256;none,zlib",
        "cshka": "ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,ssh-ed25519,rsa-sha2-256",
        "sshka": "rsa-sha2-512,rsa-sha2-256,ecdsa-sha2-nistp256,ssh-ed25519",
        "inferences": [
            "APWA",
            "KS",
            "CTS",
            "AUTO",
            "LFD"
        ],
        "remote_location.country_code": "US",
        "remote_location.region": "GA",
        "remote_location.city": "Atlanta",
        "remote_location.latitude": 33.749,
        "remote_location.longitude": -84.388
    }
    ```



=== "ssh_auth_failure"


    ```json
	{
        "_path": "ssh",
        "_system_name": "sensor",
        "_write_ts": "2026-11-04T09:16:26.803170Z",
        "auth_attempts": 7,
        "auth_success": false,
        "cipher_alg": "aes128-ctr",
        "client": "SSH-2.0-MEDUSA_1.0",
        "compression_alg": "none",
        "cshka": "ssh-rsa,ssh-dss",
        "hassh": "92674389fa1e47a27ddd8d9b63ecd42b",
        "hasshAlgorithms": "diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1,diffie-hellman-group1-sha1;aes128-ctr,aes192-ctr,aes256-ctr,aes256-cbc,rijndael-cbc@lysator.liu.se,aes192-cbc,aes128-cbc,blowfish-cbc,arcfour128,arcfour,cast128-cbc,3des-cbc;hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96,hmac-ripemd160,hmac-ripemd160@openssh.com;none",
        "hasshServer": "cca34b641961a75a15b91d1f1a13a3fb",
        "hasshServerAlgorithms": "ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1;aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,aes128-gcm@openssh.com,aes256-gcm@openssh.com,aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,aes192-cbc,aes256-cbc,arcfour,rijndael-cbc@lysator.liu.se;hmac-md5-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-ripemd160-etm@openssh.com,hmac-sha1-96-etm@openssh.com,hmac-md5-96-etm@openssh.com,hmac-md5,hmac-sha1,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-ripemd160,hmac-ripemd160@openssh.com,hmac-sha1-96,hmac-md5-96;none,zlib@openssh.com",
        "hasshVersion": "1.0",
        "host_key": "00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff",
        "host_key_alg": "ssh-rsa",
        "id.orig_h": "10.10.3.66",
        "id.orig_p": 35442,
        "id.resp_h": "10.10.3.16",
        "id.resp_p": 22,
        "inferences": [
            "SA",
            "CTS"
        ],
        "kex_alg": "diffie-hellman-group14-sha1",
        "mac_alg": "hmac-sha1",
        "server": "SSH-2.0-OpenSSH_6.4",
        "sshka": "ssh-rsa,ecdsa-sha2-nistp256",
        "ts": "2026-11-04T09:16:21.172427Z",
        "uid": "C43Qmn4CFguMzP2pBh",
        "version": 2
    }
    ```



=== "ssh_outbound"


    ```json
	{
        "_path": "ssh",
        "_system_name": "sensor",
        "_write_ts": "2026-09-15T12:41:07.520466Z",
        "ts": "2026-09-15T12:40:57.846906Z",
        "uid": "CmQ4rV3bTzW8kHn1sa",
        "id.orig_h": "10.0.0.10",
        "id.orig_p": 62977,
        "id.resp_h": "192.0.2.50",
        "id.resp_p": 22,
        "community_id": "1:u3Iir9v+OCIh1M9S7ILCkSbHSRE=",
        "version": 2,
        "auth_success": true,
        "auth_attempts": 3,
        "direction": "OUTBOUND",
        "client": "SSH-2.0-OpenSSH_9.0",
        "server": "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.4",
        "cipher_alg": "chacha20-poly1305@openssh.com",
        "mac_alg": "umac-64-etm@openssh.com",
        "compression_alg": "none",
        "kex_alg": "sntrup761x25519-sha512@openssh.com",
        "host_key_alg": "ssh-ed25519",
        "host_key": "00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff",
        "hassh": "78c05d999799066a2b4554ce7b1585a6",
        "hasshServer": "699519fdcc30cbcd093d5cd01e4b1d56",
        "hasshVersion": "1.0",
        "hasshAlgorithms": "sntrup761x25519-sha512@openssh.com,curve25519-sha256;chacha20-poly1305@openssh.com,aes128-ctr;umac-64-etm@openssh.com,hmac-sha2-256;none,zlib",
        "hasshServerAlgorithms": "curve25519-sha256,ecdh-sha2-nistp256;chacha20-poly1305@openssh.com,aes128-ctr;umac-64-etm@openssh.com,hmac-sha2-256;none,zlib",
        "cshka": "ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,ssh-ed25519,rsa-sha2-256",
        "sshka": "rsa-sha2-512,rsa-sha2-256,ecdsa-sha2-nistp256,ssh-ed25519",
        "inferences": [
            "APWA",
            "KS",
            "CTS",
            "AUTO",
            "LFD"
        ],
        "remote_location.country_code": "US",
        "remote_location.region": "GA",
        "remote_location.city": "Atlanta",
        "remote_location.latitude": 33.749,
        "remote_location.longitude": -84.388
    }
    ```



=== "ssl"


    ```json
	{
        "_path": "ssl",
        "_system_name": "sensor",
        "ts": "2025-03-06T20:26:09.490256Z",
        "uid": "Cx0XUo11iFOMEEz2Ck",
        "id.orig_h": "10.1.75.180",
        "id.orig_p": 54122,
        "id.resp_h": "203.0.113.32",
        "id.resp_p": 443,
        "version": "TLSv13",
        "cipher": "TLS_AES_256_GCM_SHA384",
        "curve": "secp384r1",
        "established": true,
        "ja3": "d76a5a80b4bb0c75ac45782b0b53da91",
        "ja3s": "15af977ce25de452b96affa2addb1036",
        "server_name": "westus-0.in.telemetry.example.com",
        "validation_status": "self signed certificate"
    }
    ```



=== "ssl_chain"


    ```json
	{
        "_path": "ssl",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:03:27.743981Z",
        "ts": "2026-09-18T19:03:27.743584Z",
        "uid": "C54mYf2LDmRt9SGbA1",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 58589,
        "id.resp_h": "203.0.113.15",
        "id.resp_p": 443,
        "version": "TLSv12",
        "cipher": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
        "curve": "secp384r1",
        "server_name": "settings.example.com",
        "resumed": false,
        "next_protocol": "h2",
        "established": true,
        "ssl_history": "CsxknGIi",
        "cert_chain_fps": [
            "1111111111111111111111111111111111111111111111111111111111111111",
            "2222222222222222222222222222222222222222222222222222222222222222"
        ],
        "client_cert_chain_fps": [],
        "subject": "CN=settings.example.com,OU=WSE,O=Example Corp,L=Test City,ST=Test State,C=US",
        "issuer": "CN=Example Secure Server CA,O=Example Corp,L=Test City,ST=Test State,C=US",
        "sni_matches_cert": true,
        "validation_status": "unable to get local issuer certificate",
        "ja3": "091f51a7a1c3a4504a224cc081ce9cee",
        "ja3s": "2fe9b0e731d3d41b2b84e8e1d6186836"
    }
    ```



=== "ssl_handshake_failure"


    ```json
	{
        "_path": "ssl",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "uid": "CofDGyd9lmi8FApci7",
        "id.orig_h": "192.168.4.149",
        "id.orig_p": 53525,
        "id.resp_h": "203.0.113.37",
        "id.resp_p": 443,
        "resumed": false,
        "last_alert": "handshake_failure",
        "established": false,
        "ssl_history": "Cl"
    }
    ```



=== "suricata_corelight"


    ```json
	{
        "_path": "suricata_corelight",
        "_system_name": "sensor.lan",
        "_write_ts": "2020-04-20T18:47:54.345633Z",
        "ts": "2020-04-20T18:47:54.339051Z",
        "uid": "CoO6zA3B7cX7KT6v07",
        "id.orig_h": "10.3.11.194",
        "id.orig_p": 50136,
        "id.resp_h": "203.0.113.98",
        "id.resp_p": 447,
        "suri_id": "SYy9Irj5XdH2",
        "service": "tls",
        "flow_id": 504752850478551,
        "tx_id": 0,
        "alert.action": "allowed",
        "alert.gid": 1,
        "alert.signature_id": 2810654,
        "alert.rev": 4,
        "alert.signature": "ETPRO POLICY Possibly Suspicious example.com SSL Cert",
        "alert.category": "A Network Trojan was detected",
        "alert.severity": 1,
        "community_id": "1:N1oDDyjYzz+fPeYBDpb3sK/sNJs="
    }
    ```



=== "suricata_flow_metadata"


    ```json
	{
        "_path": "suricata_corelight",
        "_system_name": "sensor",
        "_write_ts": "2022-08-09T13:38:52.527706Z",
        "ts": "2022-08-09T13:38:52.510541Z",
        "uid": "CPMnDWWmo3fPW8YSXd",
        "id.orig_h": "192.168.100.101",
        "id.orig_p": 49855,
        "id.resp_h": "203.0.113.38",
        "id.resp_p": 80,
        "suri_id": "SvlnhqHl2CL4",
        "service": "http",
        "flow_id": 1108036658398154,
        "tx_id": 0,
        "pcap_cnt": 0,
        "alert.action": "allowed",
        "alert.gid": 1,
        "alert.signature_id": 2035076,
        "alert.rev": 8,
        "alert.signature": "ET MALWARE Win32/Emotet CnC Activity (POST) M9",
        "alert.category": "A Network Trojan was detected",
        "alert.severity": 1,
        "alert.metadata": [
            "affected_product:Windows_XP_Vista_7_8_10_Server_32_64_Bit",
            "attack_target:Client_Endpoint",
            "created_at:2020_05_04",
            "deployment:Perimeter",
            "former_category:MALWARE",
            "malware_family:Emotet",
            "signature_severity:Major",
            "updated_at:2020_12_23"
        ],
        "metadata": [
            "flowbits:ET.formdata",
            "flowbits:http.dottedquadhost"
        ]
    }
    ```



=== "suricata_payload"


    ```json
	{
        "_path": "suricata_corelight",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:11:39.792915Z",
        "ts": "2026-09-18T19:11:39.784169Z",
        "uid": "CDTr7M3DG1PqLWUgja",
        "id.orig_h": "10.21.0.100",
        "id.orig_p": 49730,
        "id.resp_h": "203.0.113.162",
        "id.resp_p": 443,
        "suri_id": "SkEmoflvTyr1",
        "service": "tls",
        "flow_id": 1098731368304957,
        "tx_id": 0,
        "alert.action": "allowed",
        "alert.gid": 1,
        "alert.signature_id": 2049372,
        "alert.rev": 2,
        "alert.signature": "ET FILE_SHARING File Sharing Domain Observed in TLS SNI (mega .nz)",
        "alert.category": "Misc activity",
        "alert.severity": 3,
        "alert.metadata": [
            "affected_product:Any",
            "attack_target:Client_Endpoint",
            "confidence:High",
            "created_at:2023_11_28",
            "deployment:Perimeter",
            "former_category:INFO",
            "performance_impact:Low",
            "signature_severity:Informational",
            "updated_at:2024_06_12"
        ],
        "community_id": "1:Leme5h32r8dD+xj6FzjD72c3TPY=",
        "payload": "FgMBBhoBAAYWAwPja1cuUH21YjeEf3AjFiAASl2JkRmVNd2n5LYh3W648CBq7x4phIZ0cEgmZkcymYWJd2LMcOq2BsyZLgOKYah2fAA8EwITAxMBwCzAMACfzKnMqMyqwCvALwCewCTAKABrwCPAJwBnwArAFAA5wAnAEwAzAJ0AnAA9ADwANQAvAQAFkf8BAAEAAAAADAAKAAAHbWVnYS5uegALAAQDAAECAAoAEgAQEewAHQAXAB4AGAAZAQABAQAQAA4ADAJoMghodHRwLzEuMQAWAAAAFwAAADEAAAANADYANAkFCQYJBAQDBQMGAwgHCAgIGggbCBwICQgKCAsIBAgFCAYEAQUBBgEDAwMBAwIEAgUCBgIAKwAFBAMEAwMALQACAQEAMwTqBOgR7ATA37qGVygPVxCg/YAsJbLO9ZiBzUh0UVVeQlWlYXkoLQM/4XFbPrnAykFebEMKN8ETl3qwXZzO0XjNhCwkv8F8VlDCkpFqGaqDfsi9HGWJNcufx4t0qQJn4/MLbpSp6fG/SzdBtdt6FdMTdmwPFOaa81Bnv/wYj9yHwOKKdjzJePtZbKg7HrEEBpgeDQK74wixWsAQZ6SWWqsJ6mBzQAUhQXlFKSJU10N7hpyC/fU1d7RjhUO1qUdPdMdUXoxvSwZpJTnENiml8ZBu3WxCsMS9GDyZ6Ai/3gs1/NKVgCwe1rXK9gOY0gS8VWHJpOsk4PhDHfI6EYFk6Qo25kJEKcEv6toujACM5TljBqtH3vlEQDa3CoJoqoJjqIOeyVp2K9xBIsEdHbyH1wyaEccL44tp2RqXDeYx7AEnq3cgyRFXeEZJJmuzfXLM8AZPw9AnfSENx0Oq8+F19MZHB9MmfPWW91qc0BbATiB68iU1EbZTZ0IbnXh7aZKqaSIAsJazINyGptxC94BPu3Q7mHK0S+yv7fGaOzdR09Fb5yoPXmxgSQYIDCufSvyZ7zQ7tdcmBucqy1GqDjVcFKekfMUXm6FKuwklGTmMLQULVuGY/4jK4Et93lhpL2do9Sx4egTCfqW+UHMGtjNd+1MuTHOjV7NmZsE44hBohsSPlkVb43wLJQCLaOiFbrIfnyrGG2J3cQI8h7Z3ExrFCIlWccfGkVjCkImIshnOB/Utb3qCphwPEdCvYoRPbEg4tQVqGqe1z5AcpPZ/JVFzL4tjNgNJsZcb7RGxF3F89krIzKwcenxcGhUeD7t/MJVlfuFSgrVFUSRBRnqvJii4fBlAAMjH0JOnlxExnDRfWJFxqxWZXgWqhuuZCuw+wIOSvypkaZOo+LzJLXWlcxJcHIhb5eIy31xg5vBNw4I0d/CuPzpJOMiME5lu76SDGot1fzUU6/MBI5HGt/CKOkdVHLBrcLl5Xwp+mhq7CUmFpkDFbliqXeITu/urULJgDvXAUPwlVroTk8TIUhDE6/SK8cw7RJZbWNYYW9igYCYwfFvEH5R8OOxQM6ON+DcquZMXP3q8CrByE0Gr1DPC9UFFTnVsvMDO4bbMa9cXVEp7PKAOEmkkexwPP3Y8IQhV4ho3gJV/NaGoXlCFMpwMNYammONH+Qw/CYhgi4YGKSBWVMECqQAFQhp31oPCgtVvdyg/zIeKtIyOVENSF7ZNpHqluje/QmNhdTTGeBqS2dBkZqW1DKIGCQkaAzQ/5mmtE0CnFrG649R+m5uVk0ZVyYgzmAYS1VBW+OoH9NF5N+i+8ECYicQO0oOGivR9j0u6s+iz1mJU4fQdC8sSP8uEywO3+yVgm3QE02htLZNS5gu9pER+Ncl1Qhq6uAcbpKSJRwdUqUm+GYyO5gVAkJkTa3i10xdNxGCkPsoyAUIqSkeYx0UZxQqqWaO0mPRrc3uL62Y7IwQQsyo1psJe5pjOq2gmmHivhrCJDEynjDKSlht0WxMbeiwVJ/DPCVdAtacs4GwqzQAoC0JbPlVND0i14akKU+4aNlfe7JKDDM8pIvEYqwKGsoKcagrIKnACMvyrF+jMBHkQTTCu6+UZ0ngdgA8vYrDDxkLM9D2BdgAdACCUe/J11eYGKGyGtTJSyRnaZE0s9254jh95+jIFYUeDeQAbAAUEAAEAAw==",
        "payload_printable": "............kW.P}.b7..p#. .J]....5....!.n.. j..)..tpH&fG2...wb.p........a.v|.<.......,.0.........+./...$.(.k.#.'.g.\n...9.....3.....=.<.5./..............\n...mega.nz.........\n...........................h2.http/1.1.........1...\r.6.4.........................\n...........................+........-.....3...........W(.W....,%......HtQU^BU.ay(-.?.q[>...A^lC\n7...z.]...x..,$..|VP...j...~...e.5....t..g...n.....K7A..z...vl.....Pg.........v<.x.Yl.;......\r.....Z..g..Z...`admin@example.com!AyE)\"T.C{.....5w.c.C..GOt.T^.oK.i%9.6)...n.lB....<......5....,..........Ua...$..C..:..d.\n6.BD)./admin@example.com\n.h..c....Zv+.A\".............i...\r.1..'.w ..WxFI&k.}r...O..'}!\r.C...u..G..&|...Z....N z.%5..SgB..x{i..i\".... ....B..O.t;.r.K.....;7Q..[.*.^l`I...+.J...4;..&..*.Q..5\\...|....J..%.9.-..V......K}.Xi/gh.,xz..~..Ps..3].S.Ls.W.ff.8..h....E[.|.%..h..n...*..bwq.<..w.....Vq...X.........-oz.......b.OlH8..j.........%Qs/.c6.I.......q|.J....z|\\......0.e~.R..EQ$AFz.&(.|admin@example.com^.....\n.>....*di.....-u.s.\\..[..2.\\`..M..4w..?:I8....n.....u.5....#.....:GU..kp.y_\n~admin@example.com].....P.`...P.%V.....R.......;D.[X..[..`&0|[...|8.P3...7*...?z.\n.r.A..3..AENul......k..TJ{<...i${..?v<!.U..7...5..^P.2..5....G..?..`...) VT.....B.w.....ow(?......TCR..M.z..7.Bcau4.x....df.........4?admin@example.com~admin@example.com}.K.....bT......?......%`.t..hm-.R....D~admin@example.com`.>.2.B*JG..E..\n.Y....ks{..f;#...*5..^....h&.x.....L..2...t[..z,.'admin@example.com,.l*..(.B[>UM.H...\nS..6W......)\"........j\n.*p.2......y.M0.....x.../b...B..=.v... .{.u...(l..2R...dM,.nx..y.2.aG.y........."
    }
    ```



=== "tunnel"


    ```json
	{
        "_path": "tunnel",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:00:44.219976Z",
        "ts": "2026-09-16T08:00:44.219976Z",
        "uid": "CNiyFs44lpCzJjDDwk",
        "id.orig_h": "192.168.200.200",
        "id.orig_p": 53246,
        "id.resp_h": "192.0.2.114",
        "id.resp_p": 3544,
        "tunnel_type": "Tunnel::TEREDO",
        "action": "Tunnel::DISCOVER"
    }
    ```



=== "unknown_protocols"


    ```json
	{
        "_path": "unknown_protocols",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:25:55.278615Z",
        "ts": "2026-09-18T19:25:55.278615Z",
        "analyzer": "ETHERNET",
        "protocol_id": "0xa15",
        "first_bytes": "00640a150066c7380185",
        "analyzer_history": [
            "ETHERNET",
            "IP",
            "UDP",
            "VXLAN",
            "ETHERNET"
        ]
    }
    ```



=== "weird"


    ```json
	{
        "_path": "weird",
        "_system_name": "sensor",
        "_write_ts": "2026-09-16T08:02:25.115735Z",
        "ts": "2026-09-16T08:02:25.115735Z",
        "uid": "CtEFmN3cYT5UV7a579",
        "id.orig_h": "10.21.0.104",
        "id.orig_p": 62433,
        "id.resp_h": "192.0.2.154",
        "id.resp_p": 443,
        "name": "JA3_repeat_different",
        "addl": "# hello = 2, prev = 13bfc12e18208dfea99cd8fa09d1d00b/771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,11-51-45-65281-13-0-5-17513-23-10-27-43-35-18-16-21,29-23-24,0, new = 4dec7483a060b5c94a35a80d191fe7e4/771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,11-51-45-65281-13-0-5-17513-23-10-27-43-35-18-16,29-23-24,0",
        "notice": false,
        "peer": "worker-02"
    }
    ```



=== "x509"


    ```json
	{
        "_path": "x509",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:05:31.353099Z",
        "ts": "2026-09-18T19:05:31.353099Z",
        "fingerprint": "3333333333333333333333333333333333333333333333333333333333333333",
        "certificate.version": 3,
        "certificate.serial": "0A1B2C3D4E5F6071",
        "certificate.subject": "CN=smtp.example.com,OU=Domain Control Validated",
        "certificate.issuer": "CN=Example Secure Certificate Authority - G2,O=Example Corp,L=Test City,ST=Test State,C=US",
        "certificate.not_valid_before": "2018-09-20T19:23:15.000000Z",
        "certificate.not_valid_after": "2020-09-20T19:23:15.000000Z",
        "certificate.key_alg": "rsaEncryption",
        "certificate.sig_alg": "sha256WithRSAEncryption",
        "certificate.key_type": "rsa",
        "certificate.key_length": 2048,
        "certificate.exponent": "65537",
        "san.dns": [
            "smtp.example.com",
            "www.smtp.example.com",
            "mail.example.com"
        ],
        "basic_constraints.ca": false,
        "client_cert": false,
        "host_cert": true
    }
    ```



=== "x509_ca_path_len"


    ```json
	{
        "_path": "x509",
        "_system_name": "sensor",
        "_write_ts": "2026-10-01T12:00:00.000000Z",
        "ts": "2026-10-01T12:00:00.000000Z",
        "fingerprint": "8888888888888888888888888888888888888888888888888888888888888888",
        "certificate.version": 3,
        "certificate.serial": "0A1B2C3D4E5F6072",
        "certificate.subject": "CN=Example Intermediate CA,OU=Example Trust Center,O=Example Corp,L=Test City,ST=Test State,C=US",
        "certificate.issuer": "CN=Example Root CA,OU=Example Trust Center,O=Example Corp,C=US",
        "certificate.not_valid_before": "2013-03-01T13:58:29.000000Z",
        "certificate.not_valid_after": "2019-07-09T23:59:00.000000Z",
        "certificate.key_alg": "rsaEncryption",
        "certificate.sig_alg": "sha1WithRSAEncryption",
        "certificate.key_type": "rsa",
        "certificate.key_length": 2048,
        "certificate.exponent": "65537",
        "basic_constraints.ca": true,
        "basic_constraints.path_len": 0,
        "host_cert": false,
        "client_cert": false
    }
    ```



=== "x509_curve"


    ```json
	{
        "_path": "x509",
        "_system_name": "sensor",
        "_write_ts": "2026-09-18T19:03:26.472923Z",
        "ts": "2026-09-18T19:03:26.472923Z",
        "fingerprint": "4444444444444444444444444444444444444444444444444444444444444444",
        "certificate.version": 3,
        "certificate.serial": "0102030405060708090A0B0C0D0E0F1011121314",
        "certificate.subject": "CN=*.prod.telemetry.example.com,OU=DSP,O=Example Corp,L=Test City,ST=Test State,C=US",
        "certificate.issuer": "CN=Example ECC Secure Server CA,O=Example Corp,L=Test City,ST=Test State,C=US",
        "certificate.not_valid_before": "2025-12-11T19:07:58.000000Z",
        "certificate.not_valid_after": "2026-12-11T19:07:58.000000Z",
        "certificate.key_alg": "id-ecPublicKey",
        "certificate.sig_alg": "ecdsa-with-SHA384",
        "certificate.key_type": "ecdsa",
        "certificate.key_length": 256,
        "certificate.curve": "prime256v1",
        "san.dns": [
            "*.prod.telemetry.example.com"
        ],
        "basic_constraints.ca": false,
        "host_cert": true,
        "client_cert": false
    }
    ```



