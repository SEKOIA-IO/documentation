
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "query_log"

    ```
	client @0x7f62b80115d0 192.168.101.70#55575 (docs.sekoia.io): query: docs.sekoia.io IN AAAA + (192.168.100.102)
    ```



=== "query_log_category_prefix"

    ```
	queries: client @0x7f62b80115d0 192.168.101.70#55575 (docs.sekoia.io): query: docs.sekoia.io IN AAAA + (192.168.100.102)
    ```



=== "query_log_cd"

    ```
	client 192.168.101.70#55575 (docs.sekoia.io): query: docs.sekoia.io IN AAAA +TC (192.168.100.102)
    ```



=== "query_log_dhcp_1"

    ```
	Option 82: received a REQUEST DHCP packet from relay-agent eth2 with a circuit-id of "1a:02:30:00:00:00:00:76:00:00:00:00:00:00:2a:f0", a remote-id of "0a:44:70:46" for 192.168.1.222 (00:50:56:ae:b3:44) lease time is undefined seconds. (NEW)
    ```



=== "query_log_dhcp_10"

    ```
	DHCPOFFER on 1.2.3.4 to 11:22:33:44:55:66 via eth2 relay 5.6.7.8 lease-duration 119 offered-duration 3600
    ```



=== "query_log_dhcp_11"

    ```
	DHCPDISCOVER from 11:22:33:44:55:66 (ABCDEF123) via 1.2.3.4 TransID abcd1234
    ```



=== "query_log_dhcp_12"

    ```
	DHCPDISCOVER from 11:22:33:44:55:66 (TEST_HOSTNAME) via 1.2.3.4 TransID abcd1234 uid 01:11:22:33:44:55:66
    ```



=== "query_log_dhcp_13"

    ```
	DHCPDISCOVER from 11:22:33:44:55:66 via 1.2.3.4 TransID abcd1234
    ```



=== "query_log_dhcp_2"

    ```
	Option 82: received a REQUEST DHCP packet from relay-agent 192.168.1.53 with a circuit-id of "1a:02:30:00:00:00:00:76:00:00:00:00:00:00:2a:f0", a remote-id of "0a:44:70:46" for 192.168.1.53 (00:50:56:ae:b3:44) lease time is undefined seconds. (NEW)
    ```



=== "query_log_dhcp_3"

    ```
	DHCPREQUEST for 192.168.1.107 from e8:c8:29:5c:c8:99 via 192.168.1.107 TransID 80b994d6
    ```



=== "query_log_dhcp_4"

    ```
	DHCPREQUEST for 192.168.1.208 from 00:50:56:ae:17:c6 (VDPSCE080019) via eth2 TransID 823c1fa3 uid 01:00:50:56:ae:17:c6 (RENEW)
    ```



=== "query_log_dhcp_5"

    ```
	DHCPREQUEST for 192.168.1.95 (192.168.1.95) from d8:94:03:ec:da:d1 via 192.168.1.95 TransID ac1b72c4: lease 192.168.1.95 unavailable.
    ```



=== "query_log_dhcp_6"

    ```
	DHCPREQUEST for 192.168.1.159 from c8:09:a8:f8:cd:e8 via 192.168.1.159 TransID e711c0c1: ignored (unknown subnet).
    ```



=== "query_log_dhcp_7"

    ```
	DHCPACK on 192.168.1.138 to 08:71:90:8d:0b:5d (P70955) via eth2 relay 192.168.1.138 lease-duration 172800
    ```



=== "query_log_dhcp_8"

    ```
	r-l-e:192.168.1.113,Fixed,P76984,c4:d0:e3:b4:08:4d,1732119022,1732291822,,$
    ```



=== "query_log_dhcp_9"

    ```
	DHCPREQUEST for 1.2.3.4 from 11:22:33:44:55:66 (ABCDEFGHI) via eth2 TransID 1234abcd (RENEW)
    ```



=== "query_log_dns_1"

    ```
	FORMERR resolving 'test.testing.io/AAAA/IN': 192.168.1.136#53
    ```



=== "query_log_dns_2"

    ```
	client 192.168.1.1#1130: UDP: query: test.io IN A response: NXDOMAIN +
    ```



=== "query_log_dns_3"

    ```
	client 192.168.1.1#12337: UDP: query: test.org IN A response: NXDOMAIN +AE
    ```



=== "query_log_dns_4"

    ```
	client 192.168.1.1#37188: UDP: query: _ldap._tcp.test.test.net IN SRV response: NXDOMAIN +A
    ```



=== "query_log_dns_5"

    ```
	client 192.168.1.1#37521: UDP: query: test.test.io IN AAAA response: NOERROR +A test.test.io. 86400 IN CNAME test.test.io.
    ```



=== "query_log_dns_6"

    ```
	client 192.168.1.1#40432: UDP: query: test.test.org IN A response: NOERROR + test.test.org. 365 IN A 192.168.1.1; test.test.org. 365 IN A 192.168.1.1; test.test.org. 365 IN A 192.168.1.1; test.test.org. 365 IN A 192.168.1.1; test.test.org. 365 IN A 192.168.1.1; test.test.org. 365 IN A 192.168.1.1
    ```



=== "query_log_dns_7"

    ```
	client 192.168.1.1#49943: UDP: query: test.dev IN A response: NOERROR + test.dev. 11720 IN CNAME test.dev.; thmwh.l46l2i c8.c3r2fb7.81hxxxxxx.dev. 67 IN CNAME test.dev.; test.dev. 52 IN CNAME test.dev.; test.dev. 235 IN A 192.168.1.1; test.dev. 235 IN A 192.168.1.1; test.dev. 235 IN A 192.168.1.1; test.dev. 235 IN A 192.168.1.1; th mwh.xxxxxxxx.c3r2fb7.81hxxxxxx.dev. 235 IN A 192.168.1.1; test.dev. 235 IN A 192.168.1.1; test.dev. 235 IN A 192.168.1.1; thmwh.xxxxxxxx.c3r2fb7.81h xxxxxx.dev. 235 IN A 192.168.1.1;
    ```



=== "query_log_dns_8"

    ```
	28-Nov-2024 15:26:27.498 client 1.2.3.4#36615: UDP: query: PD2LORA2.enim.l2 IN A response: NOERROR +A test.dev. 3600 IN A 10.56.12.201;
    ```



=== "query_log_dns_9"

    ```
	28-Nov-2024 15:26:27.359 client 1.2.3.4#63175: UDP: query: www.bing.com IN A response: NOERROR + www.bing.com. 7072 IN CNAME www-www.bing.com.trafficmanager.net.; www-www.bing.com.trafficmanager.net. 56 IN CNAME www.bing.com.edgekey.net.; www.bing.com.edgekey.net. 7154 IN CNAME e86303.test.xxxxx.net.; e86303.test.xxxxx.net. 17 IN A 1.2.3.181; e86303.test.xxxxx.net. 17 IN A 1.2.3.173; e86303.test.xxxxx.net. 17 IN A 1.2.3.184; e86303.test.xxxxx.net. 17 IN A 1.2.3.185; e86303.test.xxxxx.net. 17 IN A 1.2.3.174; e86303.test.xxxxx.net. 17 IN A 1.2.3.183; e86303.test.xxxxx.net. 17 IN A 1.2.3.177; e86303.test.xxxxx.net. 17 IN A 1.2.3.179; e86303.test.xxxxx.net. 17 IN A 1.2.3.175;
    ```



=== "query_log_dnssec"

    ```
	client 192.168.103.66#42811 (ipv6.google.com): query: ipv6.google.com IN A +EDC (192.168.100.102)
    ```



=== "query_log_edns_version"

    ```
	client @0x7f4f8003d9e0 192.168.101.61#38251 (global.vortex.data.trafficmanager.net): query: global.vortex.data.trafficmanager.net IN AAAA +E(0) (192.168.100.102)
    ```



=== "query_log_no_recursion"

    ```
	client 192.168.103.66#57980 (ipv6.google.com): query: ipv6.google.com IN AAAA - (192.168.100.102)
    ```



=== "query_log_reverse"

    ```
	client 192.168.103.66#45041 (107.100.168.192.in-addr.arpa): query: 107.100.168.192.in-addr.arpa IN PTR +E (192.168.100.102)
    ```



=== "query_log_tcp"

    ```
	client 192.168.101.70#55575 (docs.sekoia.io): query: docs.sekoia.io IN AAAA +ET (192.168.100.102)
    ```



