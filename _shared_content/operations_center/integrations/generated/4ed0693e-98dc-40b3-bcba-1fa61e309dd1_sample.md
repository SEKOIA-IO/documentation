
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_management_access_01"

    ```
	127.0.0.1 - admin [25/Jul/2025:05:30:52 -0700] "GET /Console/PendingChanges HTTP/1.1" 200 308
    ```



=== "test_management_access_02"

    ```
	198.51.100.10 - - [01/Jul/2026:15:53:26 +0000] "POST /j_security_check HTTP/1.1" 303 0
    ```



=== "test_management_audit_01"

    ```
	Info 6/3/2025 00:31:02 admin Applied configuration changes
    ```



=== "test_management_message_01"

    ```
	2025-07-25T12:31:06+00:00 AMC@gateway01.example.com local4.info AMC: 2025-07-25 12:31:06 +0000 INFO com.aventail.mgmt.rest.console.centralmanagement.managed.sharedstate.TrafficOptimizerConfigurationResource12_2 - Clearing traffic optimizer configuration
    ```



=== "test_management_message_02"

    ```
	2026-07-01 15:53:26 +0000 INFO    [admin]: Login succeeded - Address=198.51.100.10
    ```



=== "test_management_message_03"

    ```
	pam_unix(cron:session): session closed for user root
    ```



=== "test_management_message_04"

    ```
	2026-07-02 14:33:15 +0000 INFO    [admin]: Adding user group - Name=grp4

    ```



=== "test_management_message_05"

    ```
	2026-07-02 14:48:12 +0000 ERROR     com.aventail.mgmt.jetty.JettyServer - SSL handshake failed: Closed during handshake (198.51.100.10:40236)
    ```



=== "test_management_message_06"

    ```
	2026-07-02 14:52:48 +0000 INFO    [admin]: Added address pool - ID=ID1111111111111111 Name=Test Example
    ```



=== "test_management_message_07"

    ```
	(root) CMD (   run-parts --report /etc/cron.hourly > /dev/null 2>&1)
    ```



=== "test_network_tunnel_audit_01"

    ```
	[::ffff:198.51.100.10]:59234 - "(user02)@(CT)" "31/Jul/2025:14:41:23.073 +0530" 1.2 tunnel 203.0.113.20 -1 112639 137450 165 W"42 1a 69 3a 6c 75 ac eb-be 8a 0b 90 9b 13 c6 24"
    ```



=== "test_network_tunnel_audit_02"

    ```
	198.51.100.10:59260 - "(user02)@(CT)" "31/Jul/2025:14:40:47.815 +0530" 1.2 flow:tcp 203.0.113.20:443 0 5436 129963 125 W"42 1a 69 3a 6c 75 ac eb-be 8a 0b 90 9b 13 c6 24"
    ```



=== "test_network_tunnel_audit_03"

    ```
	[03/Sep/2026:11:04:57.514525 +0200] sma8200v-01.example.com 000000 kt 00000000 Info    Audit   Src='198.51.100.25:53083' User='(user.beta@example.com)@(EXAMPLE_ORG)' TunnelVersion='0x102' Command='Flow:TCP' Dest='203.0.113.175:7680' Error='0xffffffff' SrcBytes='52' DstBytes='0' Duration='0' PlatformPrefix='W' EquipmentId='0100_0000_0000_0000_ABCD_EF12_3456_7890.' SessionKey='SMA8200v:6a992741:00000000'
    ```



=== "test_network_tunnel_audit_04"

    ```
	EventMessage: Resource Access - User='(user.alpha@example.com)@(EXAMPLE_ORG)', Src='198.51.100.10:43496', Dest_IP='203.0.113.56:53', Rule Info='DEFAULT RULES', Full Destination='203.0.113.56:53', Access Agent='-', Allowed='1'
    ```



=== "test_network_tunnel_audit_05"

    ```
	EventMessage: Resource Access - User='(user.beta@example.com)@(EXAMPLE_ORG)', Src='198.51.100.11:52532', Dest_IP='203.0.113.239:7680', Rule Info='-', Full Destination='host-a.internal.example.com:7680', Access Agent='-', Allowed='0'
    ```



=== "test_network_tunnel_audit_06"

    ```
	EventMessage: Resource Access - User='(user.gamma@example.com)@(EXAMPLE_ORG)', Src='198.51.100.12:53210', Dest_IP='203.0.113.120:7680', Rule Info='TOULOUSE RULES', Full Destination='host-b.internal.example.com:7680', Access Agent='-', Allowed='1'
    ```



=== "test_network_tunnel_audit_07"

    ```
	EventMessage: Resource Access - User='(user.delta@example.com)@(EXAMPLE_ORG)', Src='198.51.100.13:53211', Dest_IP='203.0.113.121:389', Rule Info='-', Full Destination='203.0.113.121:389', Access Agent='-', Allowed='0'
    ```



=== "test_network_tunnel_audit_08"

    ```
	[03/Sep/2026:11:04:58.123456 +0200] sma8200v-02.example.com 000000 kt 00000000 Info    Audit   Src='198.51.100.30:54001' User='(user.gamma@example.com)@(EXAMPLE_ORG)' TunnelVersion='0x102' Command='Flow:TCP' Dest='203.0.113.88:443' Error='0' SrcBytes='1024' DstBytes='2048' Duration='9' PlatformPrefix='W' EquipmentId='0100_0000_0000_0000_ABCD_EF12_3456_7891.' SessionKey='SMA8200v:6a992742:00000000'
    ```



=== "test_network_tunnel_audit_09"

    ```
	[03/Sep/2026:11:04:59.654321 +0200] sma8200v-03.example.com 000000 kt 00000000 Info    Audit   Src='198.51.100.31:54002' User='(user.delta@example.com)@(EXAMPLE_ORG)' TunnelVersion='0x102' Command='Flow:UDP' Dest='203.0.113.89:5353' Error='0xffffff92' SrcBytes='512' DstBytes='256' Duration='3' PlatformPrefix='W' EquipmentId='0100_0000_0000_0000_ABCD_EF12_3456_7892.' SessionKey='SMA8200v:6a992743:00000000'
    ```



=== "test_system_message_01"

    ```
	[29/Jul/2025:14:02:38.051761 +0000] gateway-kernel-01.example.com 000000 kp 0000020a Internal Misc <KERNEL> created channel (pid=6268):0000000021ce9936
    ```



=== "test_system_message_02"

    ```
	[6/3/2025 00:32:36.115] E-Class SMASSLVPN 002421 ps 100004b3 Info EWACL User ' (198.51.100.10 (user-example)@(group01)' connecting from '198.51.100.10:37975' matched rule 'accessRule(AV1091719670706:preauth access rule)', access to '127.0.0.1:455' is permitted.
    ```



=== "test_system_message_03"

    ```
	[6/3/2025 00:32:36.115 +0000] E-Class SMASSLVPN 027186 uk 00000001 Verbose System ::API::FAKEA145dFYNZimCKNWHB7p2q2Y=::(user01)@(group01)::CLIENT:: Interrogation: Evaluation of OPSWATAV AV1128462569762A [NortonAV.dll,Symantec Corp.,Symantec Client Security,>=,9.x,,,,,FALSE] results: FALSE
    ```



=== "test_system_message_04"

    ```
	[02/Jul/2025:18:47:29.113075 +0000] SMAnode 013581 ps 00000000 Info System Auth: CRL-CERT: Cert verification status = 0, err = 19, reason = 'self-signed certificate in certificate chain', subject='/C=US/ST=Washington/L=Seattle/O=SonicWall/OU=Engineering/CN=Untrusted CA'
    ```



=== "test_unregistered_device_01"

    ```
	https://gateway.internal.example.com:8443/UnregisteredDevices.xml
    ```



=== "test_unregistered_device_02"

    ```
	https://gateway.internal.example.com:8443/UnregisteredDevices.xml?lastLoginTime=2026-08-07T12:00:00Z&platform=Windows&realm=Students&username=user.test&exported=true&deviceCount=10&limit=100
    ```



=== "test_web_proxy_audit_01"

    ```
	198.51.100.10 - (user01)@(AD) [6/3/2025 00:32:36.115 +0000] "GET /workplace/access/home HTTP/1.1" 200 15424
    ```



=== "test_workplace_01"

    ```
	2025-06-30T14:17:23+05:30 WP@client-gateway.example.com local7.debug WP: 2025-06-30 14:17:24 +0530 DEBUG - GOT: CredentialsManager[teamSessionId=FAKESESSIONID7QuQWL3BGdokQ==,teamcredentials={username=user01} ,credentials={}]
    ```



=== "test_workplace_02"

    ```
	2025-06-30T14:17:23+05:30 WP@client-gateway.example.com local7.debug WP: 2025-06-30 14:17:23 +0530 DEBUG - PolicyClientSession: <authorize:exit> uri=http://127.0.0.1:8085/ctdownload/ status=PCL_STATUS_SUCCESS
    ```



=== "test_workplace_03"

    ```
	2025-06-30T14:17:23+05:30 127.0.0.1/127.0.0.1 local7.debug DEBUG [22:03:03,617] pcsession: <authorize:exit> uri=smb://fileshare01.example.com/marketing status=SUCCESS
    ```



=== "test_workplace_04"

    ```
	2025-06-30T14:17:23+05:30 127.0.0.1/127.0.0.1 local7.debug DEBUG [22:12:15,043] pcsession: <authorize:exit> uri=http://app.internal.example.com status=FAILURE
    ```



=== "test_workplace_05"

    ```
	2025-06-30T14:17:23+05:30 WP@client-gateway.example.com local7.debug WP: 2025-06-30 14:17:23 +0530 DEBUG - PolicyClientSession: <authorize:exit> uri=http://127.0.0.1:8085/ctdownload/ status=PCL_STATUS_SUCCESa
    ```



