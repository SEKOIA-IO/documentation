
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "query_log"

    ```
	client @0x7f0000000000 192.0.2.70#55575 (app.example.test): query: app.example.test IN AAAA + (192.0.2.102)
    ```



=== "query_log_category_prefix"

    ```
	queries: client @0x7f0000000000 192.0.2.70#55575 (app.example.test): query: app.example.test IN AAAA + (192.0.2.102)
    ```



=== "query_log_cd"

    ```
	client 192.0.2.70#55575 (app.example.test): query: app.example.test IN AAAA +TC (192.0.2.102)
    ```



=== "query_log_dhcp_1"

    ```
	Option 82: received a REQUEST DHCP packet from relay-agent eth2 with a circuit-id of "01:02:03:04:05:06:07:08:09:0a:0b:0c:0d:0e:0f:10", a remote-id of "0a:0b:0c:0d" for 198.51.100.222 (00:11:22:33:44:66) lease time is undefined seconds. (NEW)
    ```



=== "query_log_dhcp_10"

    ```
	DHCPOFFER on 203.0.113.4 to 11:22:33:44:55:66 via eth2 relay 203.0.113.8 lease-duration 119 offered-duration 3600
    ```



=== "query_log_dhcp_11"

    ```
	DHCPDISCOVER from 11:22:33:44:55:66 (ABCDEF123) via 203.0.113.4 TransID abcd1234
    ```



=== "query_log_dhcp_12"

    ```
	DHCPDISCOVER from 11:22:33:44:55:66 (TEST_HOSTNAME) via 203.0.113.4 TransID abcd1234 uid 01:11:22:33:44:55:66
    ```



=== "query_log_dhcp_13"

    ```
	DHCPDISCOVER from 11:22:33:44:55:66 via 203.0.113.4 TransID abcd1234
    ```



=== "query_log_dhcp_2"

    ```
	Option 82: received a REQUEST DHCP packet from relay-agent 198.51.100.53 with a circuit-id of "01:02:03:04:05:06:07:08:09:0a:0b:0c:0d:0e:0f:10", a remote-id of "0a:0b:0c:0d" for 198.51.100.53 (00:11:22:33:44:66) lease time is undefined seconds. (NEW)
    ```



=== "query_log_dhcp_3"

    ```
	DHCPREQUEST for 198.51.100.107 from 00:11:22:33:44:77 via 198.51.100.107 TransID 80b994d6
    ```



=== "query_log_dhcp_4"

    ```
	DHCPREQUEST for 198.51.100.208 from 00:11:22:33:44:bb (HOST001) via eth2 TransID 823c1fa3 uid 01:00:11:22:33:44:bb (RENEW)
    ```



=== "query_log_dhcp_5"

    ```
	DHCPREQUEST for 198.51.100.95 (198.51.100.95) from 00:11:22:33:44:99 via 198.51.100.95 TransID ac1b72c4: lease 198.51.100.95 unavailable.
    ```



=== "query_log_dhcp_6"

    ```
	DHCPREQUEST for 198.51.100.159 from 00:11:22:33:44:aa via 198.51.100.159 TransID e711c0c1: ignored (unknown subnet).
    ```



=== "query_log_dhcp_7"

    ```
	DHCPACK on 198.51.100.138 to 00:11:22:33:44:88 (HOST002) via eth2 relay 198.51.100.138 lease-duration 172800
    ```



=== "query_log_dhcp_8"

    ```
	r-l-e:198.51.100.113,Fixed,LEASE001,00:11:22:33:44:55,1732119022,1732291822,,$
    ```



=== "query_log_dhcp_9"

    ```
	DHCPREQUEST for 203.0.113.4 from 11:22:33:44:55:66 (ABCDEFGHI) via eth2 TransID 1234abcd (RENEW)
    ```



=== "query_log_dns_1"

    ```
	FORMERR resolving 'host.example.test/AAAA/IN': 198.51.100.136#53
    ```



=== "query_log_dns_2"

    ```
	client 198.51.100.1#1130: UDP: query: example.test IN A response: NXDOMAIN +
    ```



=== "query_log_dns_3"

    ```
	client 198.51.100.1#12337: UDP: query: example.test IN A response: NXDOMAIN +AE
    ```



=== "query_log_dns_4"

    ```
	client 198.51.100.1#37188: UDP: query: _ldap._tcp.ad.example.test IN SRV response: NXDOMAIN +A
    ```



=== "query_log_dns_5"

    ```
	client 198.51.100.1#37521: UDP: query: sub.example.test IN AAAA response: NOERROR +A sub.example.test. 86400 IN CNAME sub.example.test.
    ```



=== "query_log_dns_6"

    ```
	client 198.51.100.1#40432: UDP: query: app.example.test IN A response: NOERROR + app.example.test. 365 IN A 198.51.100.1; app.example.test. 365 IN A 198.51.100.1; app.example.test. 365 IN A 198.51.100.1; app.example.test. 365 IN A 198.51.100.1; app.example.test. 365 IN A 198.51.100.1; app.example.test. 365 IN A 198.51.100.1
    ```



=== "query_log_dns_7"

    ```
	client 198.51.100.1#49943: UDP: query: host1.example.test IN A response: NOERROR + host1.example.test. 11720 IN CNAME host1.example.test.; edge1.sub1.cdn.example.test. 67 IN CNAME host1.example.test.; host1.example.test. 52 IN CNAME host1.example.test.; host1.example.test. 235 IN A 198.51.100.1; host1.example.test. 235 IN A 198.51.100.1; host1.example.test. 235 IN A 198.51.100.1; host1.example.test. 235 IN A 198.51.100.1; edge2.cdn.example.test. 235 IN A 198.51.100.1; host1.example.test. 235 IN A 198.51.100.1; host1.example.test. 235 IN A 198.51.100.1; edge2.cdn.example.test. 235 IN A 198.51.100.1;
    ```



=== "query_log_dns_8"

    ```
	28-Nov-2024 15:26:27.498 client 203.0.113.4#36615: UDP: query: host1.corp.local IN A response: NOERROR +A host1.example.test. 3600 IN A 198.51.100.201;
    ```



=== "query_log_dns_9"

    ```
	28-Nov-2024 15:26:27.359 client 203.0.113.4#63175: UDP: query: www.app.example.test IN A response: NOERROR + www.app.example.test. 7072 IN CNAME www-www.app.cdn.example.test.; www-www.app.cdn.example.test. 56 IN CNAME www.app.edge.example.test.; www.app.edge.example.test. 7154 IN CNAME cache1.cdn.example.test.; cache1.cdn.example.test. 17 IN A 203.0.113.181; cache1.cdn.example.test. 17 IN A 203.0.113.173; cache1.cdn.example.test. 17 IN A 203.0.113.184; cache1.cdn.example.test. 17 IN A 203.0.113.185; cache1.cdn.example.test. 17 IN A 203.0.113.174; cache1.cdn.example.test. 17 IN A 203.0.113.183; cache1.cdn.example.test. 17 IN A 203.0.113.177; cache1.cdn.example.test. 17 IN A 203.0.113.179; cache1.cdn.example.test. 17 IN A 203.0.113.175;
    ```



=== "query_log_dnssec"

    ```
	client 192.0.2.66#42811 (ipv6.example.test): query: ipv6.example.test IN A +EDC (192.0.2.102)
    ```



=== "query_log_edns_version"

    ```
	client @0x7f0000000001 192.0.2.61#38251 (global.vortex.data.example.test): query: global.vortex.data.example.test IN AAAA +E(0) (192.0.2.102)
    ```



=== "query_log_no_recursion"

    ```
	client 192.0.2.66#57980 (ipv6.example.test): query: ipv6.example.test IN AAAA - (192.0.2.102)
    ```



=== "query_log_reverse"

    ```
	client 192.0.2.66#45041 (2.0.0.192.in-addr.arpa): query: 2.0.0.192.in-addr.arpa IN PTR +E (192.0.2.102)
    ```



=== "query_log_tcp"

    ```
	client 192.0.2.70#55575 (app.example.test): query: app.example.test IN AAAA +ET (192.0.2.102)
    ```



=== "test_admin_login_allowed"

    ```
	2026-03-02 16:41:03.302Z [adminsec]: Login_Allowed - - to=AdminConnector ip=192.0.2.50 auth=LOCAL group=G-ADMIN apparently_via=API
    ```



=== "test_cef_dns_query_a"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Query|DNS Query IN A|1|dst=192.0.2.1 src=198.51.100.10 spt=46842 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=host1.in.example.net InfobloxDNSQClass=IN InfobloxDNSQType=A InfobloxDNSQFlags=+ InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_query_aaaa"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Query|DNS Query IN AAAA|1|dst=192.0.2.1 src=198.51.100.20 spt=36442 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=proxy-app.example.net InfobloxDNSQClass=IN InfobloxDNSQType=AAAA InfobloxDNSQFlags=+ InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_query_ptr"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Query|DNS Query IN PTR|1|dst=192.0.2.1 src=198.51.100.40 spt=37690 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=2.1.254.169.in-addr.arpa InfobloxDNSQClass=IN InfobloxDNSQType=PTR InfobloxDNSQFlags=+ InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_query_srv"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Query|DNS Query IN SRV|1|dst=192.0.2.1 src=198.51.100.30 spt=44481 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=_gc._tcp.ad.example.net InfobloxDNSQClass=IN InfobloxDNSQType=SRV InfobloxDNSQFlags=+ InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_query_txt"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Query|DNS Query IN TXT|1|dst=192.0.2.1 src=198.51.100.50 spt=44831 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=_nfsv4idmapdomain.in.example.net InfobloxDNSQClass=IN InfobloxDNSQType=TXT InfobloxDNSQFlags=+ InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_a_noerror"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN A NOERROR|1|dst=192.0.2.1 src=198.51.100.10 spt=46842 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=host1.in.example.net InfobloxDNSQClass=IN InfobloxDNSQType=A InfobloxDNSQFlags=+A InfobloxDNSRCode=NOERROR msg="host1.in.example.net. 3600 IN A 198.51.100.11" InfobloxAnCount=1 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_a_noerror_no_msg"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN A NOERROR|1|dst=192.0.2.1 src=127.0.0.1 spt=36615 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=. InfobloxDNSQClass=IN InfobloxDNSQType=A InfobloxDNSQFlags=+ InfobloxDNSRCode=NOERROR InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_a_nxdomain"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN A NXDOMAIN|1|dst=192.0.2.1 src=198.51.100.60 spt=42552 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=host2.in.example.net.ex.example.net InfobloxDNSQClass=IN InfobloxDNSQType=A InfobloxDNSQFlags=+A InfobloxDNSRCode=NXDOMAIN InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_aaaa_noerror"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN AAAA NOERROR|1|dst=192.0.2.1 src=198.51.100.20 spt=36442 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=proxy-app.example.net InfobloxDNSQClass=IN InfobloxDNSQType=AAAA InfobloxDNSQFlags=+A InfobloxDNSRCode=NOERROR InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_aaaa_nxdomain"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN AAAA NXDOMAIN|1|dst=192.0.2.1 src=198.51.100.60 spt=5183 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=host2.in.example.net.cloud.example.com InfobloxDNSQClass=IN InfobloxDNSQType=AAAA InfobloxDNSQFlags=+ InfobloxDNSRCode=NXDOMAIN InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_ptr_noerror"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN PTR NOERROR|1|dst=192.0.2.2 src=127.0.0.1 spt=46588 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=1.0.0.127.in-addr.arpa InfobloxDNSQClass=IN InfobloxDNSQType=PTR InfobloxDNSQFlags=+A InfobloxDNSRCode=NOERROR msg="1.0.0.127.in-addr.arpa. 3600 IN PTR localhost." InfobloxAnCount=1 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_ptr_nxdomain"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN PTR NXDOMAIN|1|dst=192.0.2.1 src=198.51.100.40 spt=37690 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=2.1.254.169.in-addr.arpa InfobloxDNSQClass=IN InfobloxDNSQType=PTR InfobloxDNSQFlags=+ InfobloxDNSRCode=NXDOMAIN InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_srv_nxdomain"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN SRV NXDOMAIN|1|dst=192.0.2.1 src=198.51.100.30 spt=55893 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=_gc._tcp.ad.example.net InfobloxDNSQClass=IN InfobloxDNSQType=SRV InfobloxDNSQFlags=+ InfobloxDNSRCode=NXDOMAIN InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_cef_dns_response_txt_nxdomain"

    ```
	CEF:0|Infoblox|Data Connector|2.1.3|DNS Response|DNS Response IN TXT NXDOMAIN|1|dst=192.0.2.1 src=198.51.100.50 spt=44831 proto=UDP app=DNS InfobloxDNSView=Internal destinationDnsDomain=_nfsv4idmapdomain.in.example.net InfobloxDNSQClass=IN InfobloxDNSQType=TXT InfobloxDNSQFlags=+A InfobloxDNSRCode=NXDOMAIN InfobloxAnCount=0 InfobloxNsCount=0 InfobloxArCount=0
    ```



=== "test_dhcp_balanced_pool"

    ```
	balanced pool 563a3ae5f670 192.0.2.64/28  total 11  free 0  backup 1  lts 0  max-misbal 0  queue 1
    ```



=== "test_dhcp_balancing_pool"

    ```
	balancing pool 563a3ae5f670 192.0.2.64/28  total 11  free 1  backup 0  lts 1  max-own (+/-)0
    ```



=== "test_dhcp_expire"

    ```
	DHCPEXPIRE on 192.0.2.100 to 00:11:22:33:44:cc
    ```



=== "test_dhcp_failover_peer"

    ```
	failover peer DHCP-FAILOVER(1770103776p): 1 leases added to send queue from pool 563a3ae5f670 192.0.2.64/28
    ```



=== "test_dhcp_inform_not_authoritative"

    ```
	DHCPINFORM from 192.0.2.50 via 192.0.2.2 TransID 34df1cdc: not authoritative for subnet 192.0.2.0
    ```



=== "test_dhcp_option82_discover"

    ```
	Option 82: received a DISCOVER DHCP packet from relay-agent 203.0.113.1 with a link-selection of "203.0.113.0", a server-id-override of "203.0.113.2" for 203.0.113.10 (00:11:22:33:44:dd) lease time is undefined seconds. (NEW)
    ```



=== "test_dhcp_option82_discover_circuit_id"

    ```
	Option 82: received a DISCOVER DHCP packet from relay-agent 203.0.113.3 with a circuit-id of "00:04:01:02:03:04", a link-selection of "203.0.113.0", a server-id-override of "203.0.113.2" for 203.0.113.11 (00:11:22:33:44:dd) lease time is undefined seconds. (NEW)
    ```



=== "test_dhcp_option82_request_circuit_link"

    ```
	Option 82: received a REQUEST DHCP packet from relay-agent 203.0.113.5 with a circuit-id of "00:04:05:06:07:08", a link-selection of "203.0.113.128", a server-id-override of "203.0.113.129" for 203.0.113.131 (00:11:22:33:44:ee) lease time is undefined seconds. (NEW)
    ```



=== "test_dhcp_option82_request_link_selection"

    ```
	Option 82: received a REQUEST DHCP packet from relay-agent 203.0.113.4 with a link-selection of "203.0.113.128", a server-id-override of "203.0.113.129" for 203.0.113.130 (00:11:22:33:44:ee) lease time is undefined seconds. (NEW)
    ```



=== "test_dns_bind_update_rejected"

    ```
	bind update on 192.0.2.27 from DHCP-FAILOVER(1770103776p) rejected: incoming update is less critical than outgoing update
    ```



=== "test_dns_internal_send_error"

    ```
	internal_send: 192.0.2.231#53: Invalid argument
    ```



=== "test_dns_refused_rcode"

    ```
	REFUSED unexpected RCODE resolving 'maps.example.com/A/IN': 203.0.113.99#53
    ```



=== "test_dns_socket_error"

    ```
	socket.c:1771: unexpected error:
    ```



=== "test_storage_log_file_deleted"

    ```
	Log file /storage/reporting-capture-data/captured-dns-ns1-1771869582-1771869642.gz was deleted cause of logs directory overflow.
    ```



=== "test_storage_md5_file_deleted"

    ```
	MD5 file /storage/reporting-capture-data/captured-dns-ns1-1771869582-1771869642.gz.md5 was deleted cause of logs directory overflow.
    ```



=== "test_storage_uploaded_file_deleted"

    ```
	Uploaded file /storage/tmp/captured-dns-ns1-1771869582-1771869642.gz was deleted cause of logs directory overflow.
    ```



