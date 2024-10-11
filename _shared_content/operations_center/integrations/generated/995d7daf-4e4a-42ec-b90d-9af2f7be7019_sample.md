
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_dhcp_lease"

    ```
	1673516966.834663913 FW_MX_01 events dhcp lease of ip 1.2.3.4 from mx mac AA:BB:CC:DD:EE:FF for client mac 01:02:03:04:05:06 from router 5.6.7.8 on subnet 255.255.255.0 with dns 9.10.11.12
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
	1673614753.814828766 FW_MX_01 events anyconnect_vpn_connect user id 'john.doe@sekoia.io' local ip 1.2.3.4 reconnected from 5.6.7.8
    ```



=== "test_events_anyconnect_vpn_connect_2"

    ```
	1673614753.814828766 FW_MX_01 events anyconnect_vpn_connect user id 'john.doe@sekoia.io' local ip 1.2.3.4 connected from 5.6.7.8
    ```



=== "test_events_anyconnect_vpn_connection_success"

    ```
	1673516936.233050742 FW_MX_01 events type=anyconnect_vpn_connection_success msg= 'Server IP=1.2.3.4 Server port=443 Prot[TCP] Peer IP=5.6.7.8 Peer port=55760 conn_id[55356] Connection closed. '
    ```



=== "test_events_anyconnect_vpn_session_manager"

    ```
	1673614757.517501781 FW_MX_01 events type=anyconnect_vpn_session_manager msg= 'Sess-ID[289] Peer IP=1.2.3.4 User[john.doe@sekoia.io]: Successfully added DTLS tunnel[289.4] '
    ```



=== "test_events_content_filtering_block"

    ```
	1673541348.531136002 FW_MX_01 events content_filtering_block url='https://docs.sekoia.io/...' server='1.2.3.4:443' client_mac='AA:BB:CC:DD:EE:FF'
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
	1727862163.911654119 FW_MX_01 flows allow src=1.2.3.4 dst=5.6.7.8 mac=00:11:22:33:44:55 protocol=icmp6 type=136
    ```



=== "test_ip_flow_end"

    ```
	1673277245.252432409 FW_MX_01 ip_flow_end src=1.2.3.4 dst=5.6.7.8 protocol=udp sport=56391 dport=53 translated_dst_ip=9.10.11.12 translated_port=53
    ```



=== "test_ip_flow_start"

    ```
	1673277245.262063982 FW_MX_01 ip_flow_start src=1.2.3.4 dst=5.6.7.8 protocol=tcp sport=64365 dport=443 translated_src_ip=9.10.11.12 translated_port=64365
    ```



=== "test_urls_1"

    ```
	1673277245.257656306 FW_MX_01 urls src=1.2.3.4:51960 dst=5.6.7.8:443 mac=AA:BB:CC:DD:EE:FF request: UNKNOWN https://www.google.com/...
    ```



=== "test_urls_2"

    ```
	1673277244.773622789 FW_MX_01 urls src=1.2.3.4:64194 dst=5.6.7.8:80 mac=AA:BB:CC:DD:EE:FF request: GET http://www.msftconnecttest.com/connecttest.txt
    ```



=== "test_urls_3"

    ```
	1673277244.416181683 FW_MX_01 urls src=1.2.3.4:55566 dst=5.6.7.8:80 mac=AA:BB:CC:DD:EE:FF agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' request: GET http://docs.sekoia.io/xdr/features/collect/integrations/network/cisco_meraki/
    ```



=== "test_urls_ipv6"

    ```
	1673277244.773622789 FW_MX_01 urls src=fe80:110:8897:efab:9202:b3ff:fe1e:8329:64194 dst=fe80:110:8897:efab:9202:b3ff:fe1e:8330:80 mac=AA:BB:CC:DD:EE:FF request: GET http://www.msftconnecttest.com/connecttest.txt
    ```



