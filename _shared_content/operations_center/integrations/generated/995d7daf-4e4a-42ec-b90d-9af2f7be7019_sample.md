
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_dhcp_lease"

    ```
	1673516966.834663913 FW_MX_01 events dhcp lease of ip 1.2.3.4 from mx mac AA:BB:CC:DD:EE:FF for client mac 02:00:00:00:00:14 from router 5.6.7.8 on subnet 255.255.255.0 with dns 9.10.11.12
    ```



=== "test_dhcp_no_offer"

    ```
	1673541902.311547724 FW_MX_01 events dhcp no offers for mac AA:BB:CC:DD:EE:FF
    ```



=== "test_events_anyconnect_vpn_auth_failure"

    ```
	1673596662.226844514 FW_MX_01 events type=anyconnect_vpn_auth_failure msg= 'RADIUS[373] Server IP=1.2.3.4 Server port=1812 Peer IP=5.6.7.8 Peer port=56735: Authentication request rejected. '
    ```



=== "test_events_anyconnect_vpn_auth_success"

    ```
	1673596676.426899545 FW_MX_01 events type=anyconnect_vpn_auth_success msg= 'RADIUS[374] Server IP=1.2.3.4 Server port=1812 Peer IP=5.6.7.8 Peer port=56735 User=john.doe: Authentication request accepted. '
    ```



=== "test_events_anyconnect_vpn_connect_1"

    ```
	1673614753.814828766 FW_MX_01 events anyconnect_vpn_connect user id 'john.doe@host.example.com' local ip 1.2.3.4 reconnected from 5.6.7.8
    ```



=== "test_events_anyconnect_vpn_connect_2"

    ```
	1673614753.814828766 FW_MX_01 events anyconnect_vpn_connect user id 'john.doe@host.example.com' local ip 1.2.3.4 connected from 5.6.7.8
    ```



=== "test_events_anyconnect_vpn_connection_success"

    ```
	1673516936.233050742 FW_MX_01 events type=anyconnect_vpn_connection_success msg= 'Server IP=1.2.3.4 Server port=443 Prot[TCP] Peer IP=5.6.7.8 Peer port=55760 conn_id[55356] Connection closed. '
    ```



=== "test_events_anyconnect_vpn_session_manager"

    ```
	1673614757.517501781 FW_MX_01 events type=anyconnect_vpn_session_manager msg= 'Sess-ID[289] Peer IP=1.2.3.4 User[john.doe@host.example.com]: Successfully added DTLS tunnel[289.4] '
    ```



=== "test_events_content_filtering_block"

    ```
	1673541348.531136002 FW_MX_01 events content_filtering_block url='https://example.com/...' server='1.2.3.4:443' client_mac='AA:BB:CC:DD:EE:FF'
    ```



=== "test_firewall_allow"

    ```
	1673277220.253011885 FW_MX_01 firewall src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=39247 dport=443 pattern: 0 (tcp || udp) && dst port 443
    ```



=== "test_firewall_allow_2"

    ```
	1673277220.253011885 FW_MX_01 firewall allow src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=39247 dport=443
    ```



=== "test_firewall_block"

    ```
	1673277244.954105815 FW_MX_01 firewall src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=42644 dport=543 pattern: 1 all
    ```



=== "test_firewall_block_2"

    ```
	1673277244.954105815 FW_MX_01 firewall deny src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=42644 dport=543
    ```



=== "test_flows_allow"

    ```
	1673277220.253011885 FW_MX_01 flows src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=39247 dport=443 pattern: 0 (tcp || udp) && dst port 443
    ```



=== "test_flows_allow_2"

    ```
	1673277220.253011885 FW_MX_01 flows allow src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=39247 dport=443
    ```



=== "test_flows_allow_ipv6"

    ```
	1673277220.253011885 FW_MX_01 flows src=fe80:110:8897:efab:9202:b3ff:fe1e:8329 dst=fe80:110:8897:efab:9202:b3ff:fe1e:8330 protocol=tcp sport=39247 dport=443 pattern: 0 (tcp || udp) && dst port 443
    ```



=== "test_flows_block"

    ```
	1673277244.954105815 FW_MX_01 flows src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=42644 dport=543 pattern: 1 all
    ```



=== "test_flows_block_2"

    ```
	1673277244.954105815 FW_MX_01 flows deny src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=42644 dport=543
    ```



=== "test_flows_with_mac"

    ```
	1727862163.911654119 FW_MX_01 flows allow src=1.2.3.4 dst=5.6.7.8 mac=02:00:00:00:00:03 protocol=icmp6 type=136
    ```



=== "test_ip_flow_end"

    ```
	1673277245.252432409 FW_MX_01 ip_flow_end src=1.2.3.4 dst=5.6.7.8 protocol=udp sport=56391 dport=53 translated_dst_ip=198.51.100.6 translated_port=53
    ```



=== "test_ip_flow_start"

    ```
	1673277245.262063982 FW_MX_01 ip_flow_start src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=64365 dport=443 translated_src_ip=198.51.100.6 translated_port=64365
    ```



=== "test_security_event_file_scanned_eicar_threat_name"

    ```
	1792580000.222222222 MX-DEVICE-012 security_event security_filtering_file_scanned url=http://www.example.com/download/eicar.com.txt src=192.0.2.102:53150 dst=198.51.100.31:80 mac=AA:BB:CC:00:00:0A name='EICAR:EICAR_Test_file_not_a_virus-tpd' sha256=275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f disposition=malicious action=block
    ```



=== "test_security_event_file_scanned_empty_name"

    ```
	1792559296.991289924 MX-DEVICE-007 security_event security_filtering_file_scanned url=http://example.com/appraiseradl/ANONYMIZED.cab src=192.0.2.100:62176 dst=198.51.100.207:80 mac=AA:BB:CC:00:00:08 name='' sha256=c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3 disposition=malicious action=block
    ```



=== "test_security_event_file_scanned_quoted_name"

    ```
	1792570000.111111111 MX-DEVICE-011 security_event security_filtering_file_scanned url=http://www.example.com/download/test-file.exe?id=1&lang=en src=192.0.2.101:51000 dst=198.51.100.30:80 mac=AA:BB:CC:00:00:09 name='EICAR Test File' sha256=d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4d4 disposition=malicious action=allow
    ```



=== "test_security_event_file_scanned_url_only"

    ```
	1792567764.579646373 MX-DEVICE-010 security_event security_filtering_file_scanned url=http://download.example.com/filestreamingservice/files/00000000-0000-0000-0000-000000000000?ANONYMIZED
    ```



=== "test_security_event_ids_alerted_allowed_ingress"

    ```
	1792620000.123456789 MX-DEVICE-003 security_event ids_alerted signature=1:28423:1 priority=3 timestamp=1792620000.120000 dhost=AA:BB:CC:00:00:02 direction=ingress protocol=tcp/ip src=198.51.100.20:80 dst=192.0.2.50:53023 decision=allowed message: EXPLOIT-KIT Multiple exploit kit single digit exe detection
    ```



=== "test_security_event_ids_alerted_blocked_egress"

    ```
	1792733565.976876926 MX-DEVICE-001 security_event ids_alerted signature=3:49619:1 priority=2 timestamp=1792733565.970706 shost=AA:BB:CC:00:00:01 direction=egress protocol=tcp/ip src=192.0.2.100:53557 dst=192.0.2.1:8090 decision=blocked action=reset message: SERVER-WEBAPP Cisco RV Series Routers information disclosure attempt
    ```



=== "test_security_event_ids_alerted_no_mac_no_direction"

    ```
	1792618894.462071497 MX-DEVICE-002 security_event ids_alerted signature=1:44161:2 priority=1 timestamp=1792618894.445166 protocol=udp/ip src=203.0.113.201:56355 dst=198.51.100.7:500 decision=blocked action=reset message: SERVER-OTHER tcpdump ISAKMP parser buffer overflow attempt
    ```



=== "test_urls_1"

    ```
	1673277245.257656306 FW_MX_01 urls src=1.2.3.4:51960 dst=5.6.7.8:443 mac=AA:BB:CC:DD:EE:FF request: UNKNOWN https://example.com/...
    ```



=== "test_urls_2"

    ```
	1673277244.773622789 FW_MX_01 urls src=1.2.3.4:64194 dst=5.6.7.8:80 mac=AA:BB:CC:DD:EE:FF request: GET http://example.com/connecttest.txt
    ```



=== "test_urls_3"

    ```
	1673277244.416181683 FW_MX_01 urls src=1.2.3.4:55566 dst=5.6.7.8:80 mac=AA:BB:CC:DD:EE:FF agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' request: GET http://example.com/xdr/features/collect/integrations/network/cisco_meraki/
    ```



=== "test_urls_ipv6"

    ```
	1673277244.773622789 FW_MX_01 urls src=fe80:110:8897:efab:9202:b3ff:fe1e:8329:64194 dst=fe80:110:8897:efab:9202:b3ff:fe1e:8330:80 mac=AA:BB:CC:DD:EE:FF request: GET http://example.com/connecttest.txt
    ```



