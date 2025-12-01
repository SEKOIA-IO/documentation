
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_ad_connector_1"

    ```
	0003360952 1 0 2025-05-07 14:27:57.047 +02:00 0051005548 25002 INFO  AD-Connector: ISE server TGT refresh succeeded,  AD-Account-Name=JOHNDOE$@EXAMPLE.LOCAL, AD-Domain=EXAMPLE.LOCAL, AD-Log-Id=1234567890/1234567,
    ```



=== "test_admin_and_oper_audit_1"

    ```
	0003901877 1 0 2025-05-07 14:29:46.982 +02:00 0723317473 61026 NOTICE EAP-TLS: Shutdown secure connection with TLS peer, ConfigVersionId=360, PeerAddress=AA-BB-CC-DD-EE-FF, PeerName=CN=example.com, UniqueConnectionIdentifier =2ce4ef7a-0575-482b-8ed5-b3b068e873a1, ShutdownReason =ClosedByISE,
    ```



=== "test_admin_auth_failed"

    ```
	CISE_Administrative_and_Operational_Audit 0026935732 1 0 2025-10-23 14:26:49.538 +02:00 0264007760 51000 NOTICE Administrator-Login: Administrator authentication failed, ConfigVersionId=118, AdminInterface=GUI, AdminIPAddress=1.2.3.4, AdminName=jdoe, OperationMessageText=Authentication failed due to invalid user or password\, or account is disabled/locked,
    ```



=== "test_authentication"

    ```
	0001514749 7 3  SelectedAuthenticationIdentityStores=Internal Endpoints, AuthenticationStatus=AuthenticationPassed, NetworkDeviceGroups=Location#All Locations#H7, NetworkDeviceGroups=Device Type#All Device Types#Cisco_3650, NetworkDeviceGroups=Groupe Imprimantes#Groupe Imprimantes, NetworkDeviceGroups=APs Indoor ou Outdoor#Groupe APs, IdentityPolicyMatchedRule=Dot1X, AuthorizationPolicyMatchedRule=Some rule, EapTunnel=EAP-FAST, EapAuthentication=EAP-MSCHAPv2, cisco-av-pair=AuthenticationIdentityStore=AD1, cisco-av-pair=FQSubjectName=000000-000-0000-00000000000#host/test, cisco-av-pair=UniqueSubjectID=XXXXXXXXXXXXXXXXXXXXX, CPMSessionID=TestSessionId, EndPointMACAddress=02:00:00:00:00:00, PostureAssessmentStatus=NotApplicable, EndPointMatchedProfile=Unknown, EapChainingResult=User failed and machine succeeded, ISEPolicySetName=WIRELESS_1X_DFS, IdentitySelectionMatchedRule=Dot1X,#015
    ```



=== "test_authentication_failed"

    ```
	0000248509 3 0 2025-02-18 14:34:01.264 +01:00 0005365098 5400 NOTICE Failed-Attempt: Authentication failed, ConfigVersionId=88, Device IP Address=3.4.5.6, Device Port=53874, DestinationIPAddress=5.6.7.8, DestinationPort=1812, RadiusPacketType=AccessRequest, UserName=john.doe, Protocol=Radius, NetworkDeviceName=WLAN, User-Name=john.doe, NAS-IP-Address=2.3.4.5, NAS-Port=1656127488, Called-Station-ID=1.2.3.4, Calling-Station-ID=192.0.2.1, NAS-Port-Type=Virtual, Tunnel-Client-Endpoint=(tag=0) 192.0.2.1, cisco-av-pair=mdm-tlv=device-platform=win, cisco-av-pair=mdm-tlv=device-mac=61-05-38-5c-f8-bd, cisco-av-pair=mdm-tlv=device-platform-version=10.0.26100 , cisco-av-pair=mdm-tlv=device-public-mac=61-05-38-5c-f8-bd, cisco-av-pair=mdm-tlv=device-type=Default string Default string, cisco-av-pair=mdm-tlv=ac-user-agent=AnyConnect Windows 4.6.03049,
    ```



=== "test_boot_request"

    ```
	0000005921 7 5  11-22-33-44-55-66:EVENT_REASON\,dhcp-parameter-request-list=1\, 3\, 6\, 15\, 31\, 33\, 43\, 44\, 46\, 47\, 119\, 121\, 249\, 252\,OperatingSystem=Windows\,PostureApplicable=Yes\,User-Fetch-Department=\,AD-Last-Fetch-Time=1759879885138\,Issuer=CN=COMPANY-SUB-CA\\OU=DSI\\O=COMPANY\\L=RENNES\\C=FR\,NmapSubnetScanID=0\,AD-Host-DNS-Domain=domain.asso.fr\,Device Identifier=\,Airespace-Wlan-Id=12\,ipv6=\,Issuer - Organization=COMPANY\,TotalAuthenLatency=2\,MatchedPolicyID=11111111-1111-1111-1111-111111111111\,Service-Type=Framed\,op=BOOTREQUEST\,UserName=example.com$@domain.asso.fr\,FeedService=false\,TLSVersion=TLSv1.2\,AD-Host-NetBios-Name=DOMAIN\,Issuer - Location=RENNES\,SelectedAuthorizationProfiles=PermitAccess\,host-name=example.com\,COMPANY_LAN=COMPANY_LAN#COMPANY_LAN\,Subject=CN=example.com.DOMAIN.asso.fr\,
    ```



=== "test_conf_events"

    ```
	INFO: Configuration Changed: Admin=john.doe; Object Type=EPPurgeScheduler; Object Name=f36afcff-e3af-4a70-99c0-5e5304c1c336
    ```



=== "test_failed_attempts"

    ```
	Oct 27 14:29:31 HOST-01 CISE_Failed_Attempts 0001027727 1 0 2025-10-27 14:29:31.301 +01:00 0015075255 5400 NOTICE Failed-Attempt: Authentication failed, ConfigVersionId=11, Device IP Address=1.2.3.4, Device Port=42568, DestinationIPAddress=1.2.3.4, DestinationPort=1812, RadiusPacketType=AccessRequest, UserName=user1, Protocol=Radius, NetworkDeviceName=DEVICE-01, User-Name=aabbccddeeff, NAS-IP-Address=1.2.3.4, NAS-Port=19, Service-Type=Call Check, Called-Station-ID=user1:, Calling-Station-ID=user1, NAS-Port-Type=Ethernet, cisco-av-pair=audit-session-id=000000000000000000000000, OriginalUserName=aabbccddeeff, NetworkDeviceProfileName=Cisco, NetworkDeviceProfileId=00000000-0000-0000-0000-000000000000, IsThirdPartyDeviceFlow=false, RadiusFlowType=WiredMAB, SSID=user1:, AcsSessionID=HOST-01/000000000/000000, AuthenticationIdentityStore=Internal Endpoints, AuthenticationMethod=Lookup, SelectedAccessService=Default Network Access, SelectedAuthorizationProfiles=DenyAccess, UseCase=Host Lookup, RequestLatency=25, IdentityGroup=Endpoint Identity Groups:Profiled, FailureReason=15039 Rejected per authorization profile, Step=11001, Step=11017, Step=11027, Step=15049, Step=15008, Step=15048, Step=15041, Step=15048, Step=15013, Step=24209, Step=24211, Step=22037, Step=15036, Step=15048, Step=15048, Step=15048, Step=24432, Step=24325, Step=24313, Step=24318, Step=24322, Step=24352, Step=24412, Step=15048, Step=15048, Step=15016, Step=15039, Step=11003, SelectedAuthenticationIdentityStores=Internal Endpoints, NetworkDeviceGroups=Location#All Locations#SITE-01, NetworkDeviceGroups=Device Type#All Device Types#SW_Vendor_Site, NetworkDeviceGroups=IPSEC#Is IPSEC Device#No, IdentityPolicyMatchedRule=MAB, AuthorizationPolicyMatchedRule=Default, cisco-av-pair=AuthenticationIdentityStore=Internal Endpoints, UserType=Host, CPMSessionID=000000000000000000000000, EndPointMACAddress=user1, EndPointMatchedProfile=VENDOR-Device, DeviceRegistrationStatus=notRegistered, ISEPolicySetName=POLICY-01, IdentitySelectionMatchedRule=MAB, StepLatency=1=0;2=1;3=0;4=0;5=0;6=1;7=0;8=1;9=0;10=1;11=0;12=0;13=12;14=5;15=0;23=3;24=0;25=1;26=0;27=0, StepData=5= DEVICE.Location, StepData=7= Normalised Radius.RadiusFlowType, StepData=8=Internal Endpoints, StepData=13= EndPoints.LogicalProfile, StepData=14= EndPoints.EndPointPolicy, StepData=15= DEVICE.Device Type, StepData=0=AD_EXAMPLE, StepData=1=user1, StepData=2=example.local, StepData=3=example.local, StepData=5=ERROR_NO_SUCH_USER, StepData=6=AD_EXAMPLE, StepData=23= AD_EXAMPLE.ExternalGroups, StepData=24= Radius.Called-Station-ID, TotalAuthenLatency=25, ClientLatency=0, DTLSSupport=Unknown, HostIdentityGroup=Endpoint Identity Groups:Profiled, Network Device Profile=Cisco, Location=Location#All Locations#SITE-01, Device Type=Device Type#All Device Types#SW_Vendor_Site, IPSEC=IPSEC#Is IPSEC Device#No, EndPointPolicy=00000000-0000-0000-0000-000000000000, Name=Endpoint Identity Groups:Profiled, Response={RadiusPacketType=AccessReject; AuthenticationResult=Passed; UserName=AA:BB:CC:DD:EE:FF; },
    ```



=== "test_kv_with_colon_1"

    ```
	0000087238 3 1  AcsSessionID=ISE-CISCO/1111111/222222, AuthenticationIdentityStore=Internal Endpoints, AuthenticationMethod=Lookup, SelectedAccessService=AuthenticationMAB, SelectedAuthorizationProfiles=DenyAccess, UseCase=Host Lookup, RequestLatency=5, IdentityGroup=Endpoint Identity Groups:Unknown, FailureReason=15039 Rejected per authorization profile, Step=11001, Step=11017, Step=11027, Step=15049, Step=15008, Step=15048, Step=15048, Step=15048, Step=15041, Step=15013, Step=24209, Step=24211, Step=22037, Step=15036, Step=15016, Step=15039, Step=11003, SelectedAuthenticationIdentityStores=Internal Endpoints, NetworkDeviceGroups=Device Type#All Device Types#Switch, NetworkDeviceGroups=IPSEC#Is IPSEC Device#No, NetworkDeviceGroups=Location#All Locations, IdentityPolicyMatchedRule=Authentication Rule 1, AuthorizationPolicyMatchedRule=Default, cisco-av-pair=AuthenticationIdentityStore=Internal Endpoints, UserType=Host, CPMSessionID=ABCDEF0123456,
    ```



=== "test_kv_with_colon_2"

    ```
	0000089788 3 2  EndPointMACAddress=00-11-22-33-44-55, EndPointMatchedProfile=Unknown, DeviceRegistrationStatus=notRegistered, ISEPolicySetName=MAB, IdentitySelectionMatchedRule=Authentication Rule 1, StepLatency=1=0\;2=0\;3=0\;4=0\;5=0\;6=1\;7=0\;8=0\;9=1\;10=0\;11=1\;12=0\;13=0\;14=1\;15=0\;16=0, StepData=5= DEVICE.Device Type, StepData=6= Radius.NAS-IP-Address, StepData=7= Normalised Radius.RadiusFlowType, StepData=9=Internal Endpoints, TotalAuthenLatency=4, ClientLatency=0, DTLSSupport=Unknown, HostIdentityGroup=Endpoint Identity Groups:Unknown, Network Device Profile=Cisco, Location=Location#All Locations, Device Type=Device Type#All Device Types#Switch, IPSEC=IPSEC#Is IPSEC Device#No, Name=Endpoint Identity Groups:Unknown, Response={RadiusPacketType=AccessReject; AuthenticationResult=Passed; UserName=02:00:00:00:00:00; },
    ```



=== "test_miscellaneous"

    ```
	INFO: 5 endpoint(s) purged successfully
    ```



=== "test_miscellaneous1"

    ```
	2023-06-07 04:26:17.306 +0200 60198 INFO null: MnT purge event occurred, MESSAGE=completed successfully,
    ```



=== "test_miscellaneous2"

    ```
	WARN: AcsSyslogContentAaaDiagnostics:: ACTIVE_DIRECTORY_DIAGNOSTIC_TOOL_ISSUES_FOUND need to complete
    ```



=== "test_network_info_events"

    ```
	INFO: EAP Connection Timeout : Server=example.com; NAS IP Address=1.2.3.4; NAS Identifier=02:00:00:00:00:00:test1
    ```



=== "test_network_info_events1"

    ```
	0000738292 7 0 2025-01-09 09:28:49.914 +01:00 0043796555 5200 NOTICE Passed-Authentication: Authentication succeeded, ConfigVersionId=186, Device IP Address=192.0.2.1, DestinationIPAddress=1.2.3.4, DestinationPort=1812, UserName=user1, Protocol=Radius, NetworkDeviceName=MGCUH1-3, User-Name=user1, NAS-IP-Address=192.0.2.1, NAS-Port=1001, Service-Type=Framed, Framed-MTU=1449, State=37CPMSessionID=XXXXXXXXXXXXXX\;36SessionID=MGDFSISE2/515448264/543038\;, Called-Station-ID=a0:ec:f9:50:e2:90:DFS, Calling-Station-ID=bc:83:85:d8:88:c6, NAS-Identifier=MGCUH1-3, NAS-Port-Type=Wireless - IEEE 802.11, NAS-Port-Id=Capwap2, EAP-Key-Name=, cisco-av-pair=service-type=Framed, cisco-av-pair=audit-session-id=XXXXXXXXXXXXXX, cisco-av-pair=method=dot1x, cisco-av-pair=cisco-wlan-ssid=DFS, Airespace-Wlan-Id=5, NetworkDeviceProfileName=Cisco, NetworkDeviceProfileId=aaaaaaaaaaaaaaaaaaaaa,#015
    ```



=== "test_network_info_events2"

    ```
	CISE_RADIUS_Accounting 0002391460 1 0 2025-07-30 11:50:34.267 +02:00 0023023046 3002 NOTICE Radius-Accounting: RADIUS Accounting watchdog update, ConfigVersionId=83, Device IP Address=1.2.3.4, UserName=user1, NetworkDeviceName=Test-Network-Device-Name, User-Name=user1, NAS-IP-Address=1.2.3.4, NAS-Port=50107, Framed-IP-Address=3.4.5.6, Class=CACS:0A0D00F90000001402268B53:ise/523393559/11169221, Called-Station-ID=11-00-00-00-00-00, Calling-Station-ID=user1, Acct-Status-Type=Interim-Update, Acct-Delay-Time=0, Acct-Input-Octets=1848852125, Acct-Output-Octets=2808400785, Acct-Session-Id=00000070, Acct-Input-Packets=27991836, Acct-Output-Packets=40488347, Event-Timestamp=1753869011, NAS-Port-Type=Ethernet, NAS-Port-Id=GigabitEthernet0/7, cisco-av-pair=audit-session-id=0A0D00F90000001402268B53, cisco-av-pair=vlan-id=1330, cisco-av-pair=method=mab, AcsSessionID=MGMT-ISE01/0000000000/2185126, SelectedAccessService=Default Network Access, RequestLatency=3, Step=11004, Step=11017, Step=15049, Step=15008, Step=15048, Step=15048, Step=22094, Step=11005, NetworkDeviceGroups=Location#All Locations#Test Test#LAN#ACA, NetworkDeviceGroups=Device Type#All Device Types#Switch#2960L, NetworkDeviceGroups=IPSEC#Is IPSEC Device#No, CPMSessionID=0A0D00F90000001402268B53, StepLatency=1=0\;2=0\;3=0\;4=1\;5=0\;6=1\;7=0, StepData=4= Normalised Radius.TTTTT, StepData=5= Normalised Radius.RadiusFlowType, TotalAuthenLatency=3, ClientLatency=0, Model Name=Unknown, Software Version=Unknown, Network Device Profile=Cisco, Location=Location#All Locations#Test Test#LAN#ACA, Device Type=Device Type#All Device Types#Switch#2960L, IPSEC=IPSEC#Is IPSEC Device#No,
    ```



=== "test_network_info_events3"

    ```
	0000000000 1 0 2025-07-29 14:07:18.047 +02:00 0000000000 51000 NOTICE Administrator-Login: Administrator authentication failed, ConfigVersionId=XX, AdminInterface=GUI, AdminIPAddress=1.2.3.4, AdminName=user1, OperationMessageText=Authentication failed due to invalid user or password, or account is disabled/locked,
    ```



=== "test_network_info_events4"

    ```
	CISE_Administrative_and_Operational_Audit 0000000000 1 0 2025-07-29 14:07:18.047 +02:00 0000000000 51000 NOTICE Administrator-Login: Administrator authentication failed, ConfigVersionId=XX, AdminInterface=GUI, AdminIPAddress=1.2.3.4, AdminName=user1, OperationMessageText=Authentication failed due to invalid user or password, or account is disabled/locked,
    ```



=== "test_network_response"

    ```
	0001514749 7 6  Response={Class=CACS:XXXXXXXXX:asdsa/000000/111111; Tunnel-Type=(tag=1) VLAN; Tunnel-Medium-Type=(tag=1) 802; Tunnel-Private-Group-ID=(tag=1) COMPUTER; EAP-Key-Name=EAP-Key-VALUE; MS-MPPE-Send-Key=****; MS-MPPE-Recv-Key=****; LicenseTypes=1; },#015
    ```



=== "test_network_warm1"

    ```
	WARN: Dynamic Authorization Failed for Device : Server=example.com; Calling Station Id=N/A; Network device IP=1.2.3.4; Network Device
    ```



=== "test_network_warm2"

    ```
	WARN: Profiler SNMP Request Failure : Server= example.com; NAD Address=1.2.3.4; Error Message=Request timed out.
    ```



=== "test_network_warn_events"

    ```
	WARN: TrustSec deploy verification failed to reach NAD.: Device Name=device005.internal.example.org; Device Ip=1.2.3.4; Device login username=admin
    ```



=== "test_profiler_1"

    ```
	0003361015 2 0 2025-05-07 14:29:08.974 +02:00 0051006044 80002 INFO  Profiler: Profiler EndPoint profiling event occurred, ConfigVersionId=183, OperatingSystem=Windows 11 Entreprise, EndpointCertainityMetric=50, EndpointIPAddress=1.2.3.4, EndpointMacAddress=AA:BB:CC:DD:EE:FF, EndpointMatchedPolicy=Windows11-Workstation, EndpointOUI=Intel Corporate, EndpointPolicy=Windows11-Workstation, EndpointProperty=chaddr=AA:BB:CC:DD:EE:FF,dhcp-class-identifier=MSFT 5.0,PolicyVersion=24,dhcp-message-type=DHCPREQUEST,EndPointPolicyID=57f40927-3b0a-46b8-9f03-78d47e1383c4,LogicalProfile=,client-fqdn=abcdef.example.local,EndPointVersion=340,FirstCollection=1744718839328,CacheUpdateTime=1746620948973,StaticAssignment=false,NmapScanCount=0,PostureExpiry=,hlen=6,AD-Operating-System=Windows 11 Entreprise,AD-Join-Point=EXAMPLE.LOCAL,PortalUser=,ciaddr=0.0.0.0,BYODRegistration=Unknown,dhcp-requested-address=1.2.3.4,Total Certainty Factor=50,MDMServerID=,
    ```



=== "test_radius_accounting"

    ```
	Oct 27 15:20:43 HOST-01 CISE_RADIUS_Accounting 0001042079 1 0 2025-10-27 15:20:43.919 +01:00 0015337799 3002 NOTICE Radius-Accounting: RADIUS Accounting watchdog update, ConfigVersionId=11, Device IP Address=1.2.3.4, UserName=user1, NetworkDeviceName=DEVICE-02, User-Name=user1, NAS-IP-Address=1.2.3.4, NAS-Port=42, Service-Type=Framed, Framed-IP-Address=1.2.3.4, Class=CACS:000000000000000000000000:HOST-01/000000000/000000, Called-Station-ID=user1:, Calling-Station-ID=user1, Acct-Status-Type=Interim-Update, Acct-Delay-Time=0, Acct-Input-Octets=921941396, Acct-Output-Octets=0, Acct-Session-Id=0000000000000000, Acct-Authentic=RADIUS, Acct-Session-Time=570009, Acct-Input-Packets=0, Acct-Output-Packets=35, Acct-Input-Gigawords=922518720, Acct-Output-Gigawords=28, Event-Timestamp=1761574843, NAS-Port-Type=Ethernet, cisco-av-pair=audit-session-id=000000000000000000000000, AcsSessionID=HOST-01/000000000/000000, SelectedAccessService=Default Network Access, RequestLatency=2, Step=11004, Step=11017, Step=15049, Step=15008, Step=22094, Step=11005, NetworkDeviceGroups=Location#All Locations#SITE-02, NetworkDeviceGroups=Device Type#All Device Types#SW_Vendor_Site, NetworkDeviceGroups=IPSEC#Is IPSEC Device#No, CPMSessionID=000000000000000000000000, StepLatency=1=0;2=0;3=1;4=0;5=0, TotalAuthenLatency=2, ClientLatency=0, Network Device Profile=Cisco, Location=Location#All Locations#SITE-02, Device Type=Device Type#All Device Types#SW_Vendor_Site, IPSEC=IPSEC#Is IPSEC Device#No,
    ```



