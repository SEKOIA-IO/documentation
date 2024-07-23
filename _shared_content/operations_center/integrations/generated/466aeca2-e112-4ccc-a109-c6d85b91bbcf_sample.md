
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_106001"

    ```
	%FTD-2-106001: Inbound TCP connection denied from 172.16.10.234/901 to 192.168.122.55/111 flags SYN  on interface LAN
    ```



=== "test_106006"

    ```
	%FTD-2-106006: Deny inbound UDP from 172.16.10.234/901 to 192.168.122.55/111 on interface LAN
    ```



=== "test_430002"

    ```
	%NGIPS-1-430002: EventPriority: Low, DeviceUUID: b2433c5c-a6a1-11eb-a6e7-be0b9833091f, InstanceID: 2, FirstPacketSecond: 2021-04-30T11:31:19Z, ConnectionID: 4, AccessControlRuleAction: Allow, SrcIP: 172.16.10.10, DstIP: 172.16.20.10, ICMPType: Echo Request, ICMPCode: No Code, Protocol: icmp, IngressInterface: inside, EgressInterface: outside, ACPolicy: Default Allow All Traffic, AccessControlRuleName: test, Client: ICMP client, ApplicationProtocol: ICMP, InitiatorPackets: 1, ResponderPackets: 0, InitiatorBytes: 74, ResponderBytes: 0, NAPPolicy: Balanced Security and Connectivity
    ```



=== "test_430003"

    ```
	%NGIPS-1-430003: EventPriority: Low, DeviceUUID: e8566508-eaa9-11e5-860f-de3e305d8269, InstanceID: 3, FirstPacketSecond: 2020-02-04T08:45:34Z, ConnectionID: 34774, AccessControlRuleAction: <br/>Block with reset, SrcIP: 93.157.158.93, DstIP: 10.1.9.9, SrcPort: 13723, DstPort: 80, Protocol: tcp, IngressInterface: outside, EgressInterface: seversDMZ, ACPolicy: Basic IPS/IDS and GeoIP block foreign contries, AccessControlRuleName: GeoBlock other Countries, Prefilter Policy: Unknown, ConnectionDuration: 0, InitiatorPackets: 1, ResponderPackets: 0, InitiatorBytes: 54, ResponderBytes: 0, NAPPolicy: Balanced Security and Connectivity
    ```



=== "test_430005"

    ```
	%FTD-1-430005: SrcIP: 10.0.1.20, DstIP: 81.2.69.144, SrcPort: 46004, DstPort: 80, Protocol: tcp, FileDirection: Download, FileAction: Malware Cloud Lookup, FileSHA256: 2546dcffc5ad854d4ddc64fbf056871cd5a00f2471cb7a5bfd4ac23b6e9eedad, SHA_Disposition: Unavailable, SperoDisposition: Spero detection not performed on file, ThreatName: Win.Ransomware.Eicar::95.sbx.tg, FileName: eicar_com.zip, FileType: ZIP, FileSize: 184, ApplicationProtocol: HTTP, Client: cURL, User: No Authentication Required, FirstPacketSecond: 2019-08-16T09:39:02Z, FilePolicy: malware-and-file-policy, FileStorageStatus: Not Stored (Disposition Was Pending), FileSandboxStatus: File Size Is Too Small, URI: http://www.eicar.org/download/eicar_com.zip
    ```



=== "test_ASA_106012"

    ```
	%ASA-6-106012: Deny IP from 192.168.122.143 to 224.0.0.22, IP options: "Router Alert"
    ```



=== "test_ASA_106015"

    ```
	%ASA-6-106015: Deny TCP (no connection) from 10.9.4.3/52675 to 161.5.222.141/443 flags FIN ACK on interface ACME_interface
    ```



=== "test_ASA_106023"

    ```
	%ASA-4-106023: Deny udp src ACMEsL:10.0.200.29/320 dst identity:224.0.1.129/320 by access-group "ACME_group" [0x0, 0x0]
    ```



=== "test_ASA_106100"

    ```
	%ASA-6-106100: access-list ACME_INFRA permitted udp ACME_INFRA/10.1.0.16(42592) -> ACME/10.1.1.76(161) hit-cnt 1 first hit [0x42666c4c, 0x05739900]
    ```



=== "test_ASA_110003"

    ```
	%ASA-6-110003: Routing failed to locate next hop for icmp from WAN:10.11.0.2/0 to WAN:10.112.115.1/0
    ```



=== "test_ASA_111007"

    ```
	%ASA-5-111007: Begin configuration: 10.24.25.21 reading from http [POST]
    ```



=== "test_ASA_113004"

    ```
	%ASA-6-113004: AAA user authentication Successful : server = 10.79.48.28 : user = jdoe001566
    ```



=== "test_ASA_199019"

    ```
	%ASA-7-199019: Mar  6 21:58:53 Ipc[1234]: func return 1#012
    ```



=== "test_ASA_302013"

    ```
	%ASA-6-302013: Built inbound TCP connection 1800234408 for TTA-ACME-VDO_CAM:10.1.7.248/40454 (10.1.7.248/40454) to TTA-ACME-SRV_INFRA:10.1.0.10/53 (10.1.0.10/53)
    ```



=== "test_ASA_302014"

    ```
	%ASA-6-302014: Teardown TCP connection 3642851852 for outside:9.27.0.93/63677 to Pika:172.17.1.200/443 duration 0:10:06 bytes 4666 FIN Timeout from Pika
    ```



=== "test_ASA_302020"

    ```
	%ASA-6-302020: Built inbound ICMP connection for faddr 47.241.116.84/10800 gaddr 10.11.0.2/0 laddr 10.11.0.2/0
    ```



=== "test_ASA_302020_2"

    ```
	%ASA-6-302020: Built inbound ICMP connection for faddr 1.2.3.4/1(LOCAL\USER) gaddr 1.2.3.5/0 laddr 1.2.3.5/0 (USER) type 8 code 0
    ```



=== "test_ASA_302021"

    ```
	%ASA-6-302021: Teardown ICMP connection for faddr 172.16.10.208/2189 gaddr 172.16.19.90/0 laddr 172.16.19.90/0 (karibou)
    ```



=== "test_ASA_302021_2"

    ```
	%ASA-6-302021: Teardown ICMP connection for faddr 1.2.3.4/25481 gaddr 1.2.4.3/0 laddr 1.2.4.3/0 type 8 code 0
    ```



=== "test_ASA_305011"

    ```
	%ASA-6-305011: Built dynamic TCP translation from interco_pa_asa:10.79.16.23/35928 to dmz-gce:126.189.129.55/35928
    ```



=== "test_ASA_305012"

    ```
	%ASA-6-305012: Teardown dynamic TCP translation from interco_asa:10.79.16.24/55924 to dmz:12.18.129.56/55924 duration 0:00:15
    ```



=== "test_ASA_313005"

    ```
	%ASA-4-313005: No matching connection for ICMP error message: icmp src outside:1.2.3.4(LOCAL\a.smithee) dst inside:1.4.3.2 (type 3, code 3) on outside interface.  Original IP payload: udp src 1.4.3.2/53 dst 1.2.3.4/60717.
    ```



=== "test_ASA_313008"

    ```
	%ASA-3-313008: Denied IPv6-ICMP type=136, code=0 from fe80::f037:5fbc:b824:230d on interface NEA-FOR-WIFOR
    ```



=== "test_ASA_609002"

    ```
	%ASA-7-609002: Teardown local-host outside:1.2.3.4 duration 0:10:26
    ```



=== "test_ASA_716058"

    ```
	%ASA-6-716058: Group <CLIENT_VPN> User <Acme_account> IP <86.199.78.204> AnyConnect session lost connection. Waiting to resume.
    ```



=== "test_ASA_716059"

    ```
	%ASA-6-716059: Group <CLIENT_VPN> User <User_Acme> IP <10.17.100.175> AnyConnect session resumed connection from IP <10.17.100.175>.
    ```



=== "test_ASA_722011"

    ```
	%ASA-5-722011: Group <GroupPolicy_CLIENT_VPN> User <User_acme> IP <91.172.139.4> SVC Message: 17/WARNING: Reconnecting the VPN tunnel..
    ```



=== "test_ASA_722012"

    ```
	%ASA-5-722012: Group <GroupPolicy_CLIENT_VPN> User <User_Acme> IP <86.217.237.163> SVC Message: 16/NOTICE: Client PC is going into suspend mode (Sleep, Hibernate, etc)..
    ```



=== "test_ASA_722023"

    ```
	%ASA-6-722023: Group <GroupPolicy_CLIENT_VPN> User <User_Acme> IP <86.215.190.93> TCP SVC connection terminated without compression
    ```



=== "test_ASA_722023_2"

    ```
	%ASA-6-722023: Group <GroupPolicy-CLIENT-VPN> User <a.smithee> IP <1.2.3.4> UDP SVC connection terminated without compression
    ```



=== "test_ASA_722028"

    ```
	%ASA-5-722028: Group <GroupPolicy_CLIENT_VPN> User <User_Acme> IP <91.172.139.4> Stale SVC connection closed.
    ```



=== "test_ASA_722032"

    ```
	%ASA-5-722032: Group <GroupPolicy_CLIENT_VPN> User <User_Acme> IP <93.23.18.76> New UDP SVC connection replacing old connection.
    ```



=== "test_ASA_722033"

    ```
	%ASA-5-722033: Group <GroupPolicy_CLIENT_VPN> User <User_Acme> IP <77.205.143.138> First TCP SVC connection established for SVC session.
    ```



=== "test_ASA_722034"

    ```
	%ASA-5-722034: Group <GroupPolicy_CLIENT_VPN> User <User_Acme> IP <109.17.100.175> New TCP SVC connection, no existing connection.
    ```



=== "test_ASA_722037"

    ```
	%ASA-4-722037: Group <GroupPolicy_CLIENT_VPN> User <User_Acme> IP <92.131.212.102> SVC closing connection: Transport closing.
    ```



=== "test_ASA_725001"

    ```
	%ASA-6-725001: Starting SSL handshake with client WAN:195.101.173.60/49238 for TLS session.
    ```



=== "test_ASA_725002"

    ```
	%ASA-6-725002: Device completed SSL handshake with client WAN:90.114.208.186/65531
    ```



=== "test_ASA_725006"

    ```
	%ASA-6-725006: Device failed SSL handshake with client WAN:195.101.173.60/49699
    ```



=== "test_ASA_725007"

    ```
	<166>Nov 09 2022 10:01:59: %ASA-6-725007: SSL session with client WAN:195.101.173.60/49486 terminated.
    ```



=== "test_ASA_733100"

    ```
	%ASA-4-733100: [scanning] drop rate-1 exceeded. Current burst rate is 8 per second, max configured rate is 10; Current average rate is 23 per second, max configured rate is 5; Cumulative total count is 14188
    ```



=== "test_ASA_737016"

    ```
	%ASA-6-737016: IPAA: Freeing local pool address 192.168.122.247
    ```



=== "test_ASA_852001"

    ```
	%FTD-6-852001: Received Lightweight to full proxy event from application Snort for TCP flow 1.2.3.4/10000 to 4.3.2.1/47003
    ```



=== "test_FTD_113004"

    ```
	%FTD-6-113004: AAA user authentication Successful : server =  10.10.48.61 : user = jdoe
    ```



=== "test_FTD_430002_1"

    ```
	%FTD-1-430002: EventPriority: Low, DeviceUUID: 1662dc94-665c-4e50-97df-1c5b281556aa, InstanceID: 3, FirstPacketSecond: 2023-07-27T08:13:09Z, ConnectionID: 62230, AccessControlRuleAction: Allow, SrcIP: 1.2.3.4, DstIP: 5.6.7.8, SrcPort: 63853, DstPort: 443, Protocol: tcp, IngressInterface: WAN, EgressInterface: DMZ, IngressZone: OUT, EgressZone: DMZ, IngressVRF: Global, EgressVRF: Global, ACPolicy: ACPolicy, AccessControlRuleName: IN_KEMP_MAIL, Prefilter Policy: EXAMPLE L3-L4 Policy, InitiatorPackets: 2, ResponderPackets: 1, InitiatorBytes: 128, ResponderBytes: 66, NAPPolicy: Balanced Security and Connectivity
    ```



=== "test_FTD_430003_1"

    ```
	%FTD-1-430003: EventPriority: Low, DeviceUUID: 1662dc94-665c-4e50-97df-1c5b281556aa, InstanceID: 5, FirstPacketSecond: 2023-07-27T08:13:09Z, ConnectionID: 35868, AccessControlRuleAction: Allow, SrcIP: 1.2.3.4, DstIP: 5.6.7.8, SrcPort: 56901, DstPort: 53, Protocol: udp, IngressInterface: LAN, EgressInterface: WAN, IngressZone: LAN, EgressZone: OUT, IngressVRF: Global, EgressVRF: Global, ACPolicy: ACPolicy, AccessControlRuleName: SORTIE_SRVAD_DNS_OUT, Prefilter Policy: EXAMPLE L3-L4 Policy, User: Not Found, Client: DNS client, ApplicationProtocol: DNS, ConnectionDuration: 0, InitiatorPackets: 1, ResponderPackets: 1, InitiatorBytes: 88, ResponderBytes: 152, NAPPolicy: Balanced Security and Connectivity, DNSQuery: 1.fr.pool.ntp.org, DNSRecordType: a host address, DNSResponseType: No Error, DNS_TTL: 150, NAT_InitiatorPort: 22294, NAT_ResponderPort: 53, NAT_InitiatorIP: 4.3.2.1, NAT_ResponderIP: 8.7.6.5
    ```



=== "test_FTD_430003_2"

    ```
	%FTD-1-430003: EventPriority: Low, DeviceUUID: 1662dc94-665c-4e50-97df-1c5b281556aa, InstanceID: 5, FirstPacketSecond: 2023-07-27T08:13:09Z, ConnectionID: 35871, AccessControlRuleAction: Allow, SrcIP: 1.2.3.4, DstIP: 5.6.7.8, SrcPort: 50158, DstPort: 443, Protocol: tcp, IngressInterface: LAN, EgressInterface: WAN, IngressZone: LAN, EgressZone: OUT, IngressVRF: Global, EgressVRF: Global, ACPolicy: ACPolicy, AccessControlRuleName: SORTIE_INTERNET_ALL, Prefilter Policy: EXAMPLE L3-L4 Policy, User: Not Found, Client: SSL client, ApplicationProtocol: HTTPS, WebApplication: Trend Micro, ConnectionDuration: 0, InitiatorPackets: 10, ResponderPackets: 13, InitiatorBytes: 967, ResponderBytes: 5018, NAPPolicy: Balanced Security and Connectivity, SSLPolicy: None, SSLFlowStatus: Success, SSLCipherSuite: Unknown, SSLCertificate: 3ccc5ece59e81d905ed314c1e9af0f797393fec5, SSLVersion: Unknown, SSLServerCertStatus: Valid, SSLActualAction: Do Not Decrypt, SSLExpectedAction: Do Not Decrypt, SSLServerName: example.org, URLCategory: Computer Security, URLReputation: Trusted, URL: https://example.org, NAT_InitiatorPort: 36170, NAT_ResponderPort: 443, NAT_InitiatorIP: 4.3.2.1, NAT_ResponderIP: 8.7.6.5
    ```



=== "test_FTD_430003_3"

    ```
	%FTD-1-430003: EventPriority: Low, DeviceUUID: deyyyyy-844d-11e7-b104-8d1450667052, InstanceID: 1, FirstPacketSecond: 2023-08-23T12:59:00Z, ConnectionID: 55087, AccessControlRuleAction: Allow, SrcIP: 10.55.21.168, DstIP: 142.55.179.67, SrcPort: 77777, DstPort: 80, Protocol: tcp, IngressInterface: LAN, EgressInterface: WAN, IngressZone: LAN, EgressZone: OUT, IngressVRF: Global, EgressVRF: Global, ACPolicy: ACPolicy, AccessControlRuleName: SORTIE_INTERNET_ALL, Prefilter Policy: LALALAND L3-L4 Policy, User: Not Found, UserAgent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.32 Safari/537.36, Client: Chrome, ClientVersion: 60.0.3112.32, ApplicationProtocol: HTTP, WebApplication: Google, ConnectionDuration: 0, InitiatorPackets: 5, ResponderPackets: 5, InitiatorBytes: 565, ResponderBytes: 484, NAPPolicy: Balanced Security and Connectivity, ReferencedHost: connectivitycheck.gstatic.com, URLCategory: Infrastructure and Content Delivery Networks, URLReputation: Favorable, URL: http://connectivitycheck.gstatic.com/generate_204, NAT_InitiatorPort: 77777, NAT_ResponderPort: 80, NAT_InitiatorIP: 194.55.57.195, NAT_ResponderIP: 142.55.179.67
    ```



=== "test_group_1"

    ```
	Group <AnyConnect-SESAME> User <JD34242243> IP <1.2.3.4> AnyConnect session lost connection. Waiting to resume.
    ```



=== "test_group_10"

    ```
	Task ran for 100 msec, Process = aaa_shim_thread, PC = abb111cc, Call stack =   0x000000aaab89d6a0  0x000000aaab88cdec  0x000000aaab88cd68
    ```



=== "test_group_1_2"

    ```
	Group <MyGroup> User <MyUser> IP <4.3.2.1> IPv4 Address <1.2.3.4> IPv6 address <::> assigned to session
    ```



=== "test_group_1_3"

    ```
	Group <MyGroup> User <MyUser> IP <4.3.2.1> IPv4 Address <> IPv6 address <3deb:3c5e:59d0:53ad:1115:d3d7:58da:47d6> assigned to session
    ```



=== "test_group_2"

    ```
	Group <MYGROUP> User <JD34242243> IP <1.2.3.4> SVC closing connection: DPD failure.
    ```



=== "test_group_2_2"

    ```
	Group <MyGroup> User <MyUsser> IP <1.2.3.4> Client Type: Cisco AnyConnect VPN Agent for Windows 4.10.07061
    ```



=== "test_group_2_3"

    ```
	 Group <MyGroup> User <MyUsser> IP <1.2.3.4> Client Type: Cisco AnyConnect VPN Agent for Windows 4.10.07061
    ```



=== "test_group_3"

    ```
	Group = MYGROUP, Username = JD34242243, IP = 1.2.3.4, Session disconnected. Session Type: SSL, Duration: 6h:33m:18s, Bytes xmt: 220870890, Bytes rcv: 57125392, Reason: Idle Timeout
    ```



=== "test_group_4"

    ```
	Task ran for 109 msec, Process = aaa_shim_thread, PC = ade9333c, Call stack =   0x000000aaabb34820  0x000000aaabb2429c  0x000000aaabb24218
    ```



=== "test_group_5"

    ```
	TunnelGroup <AnyConnect-SESAME> GroupPolicy <MYGROUP> User <JD34242243> IP <1.2.3.4> No IPv6 address available for SVC connection
    ```



=== "test_group_6_2"

    ```
	Group <AnyConnect-EXAMPLE> User <MyUser> IP <1.2.3.4> AnyConnect session lost connection. Waiting to resume.
    ```



=== "test_group_7"

    ```
	TunnelGroup <AnyConnect-EX> GroupPolicy <MyGroup> User <MyUser> IP <4.3.2.1> No IPv6 address available for SVC connection
    ```



=== "test_group_9"

    ```
	Tunnel group search using certificate maps failed for peer certificate: serial number: 111111111111111111111111, subject name: UID=U11111111,CN=JOHN DOE,OU=Unit,O=URAAA,C=US, issuer_name: CN=Admin,OU=Unit,O=Example,C=US.
    ```



