
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_authentication"

    ```
	0001514749 7 3  SelectedAuthenticationIdentityStores=Internal Endpoints, AuthenticationStatus=AuthenticationPassed, NetworkDeviceGroups=Location#All Locations#H7, NetworkDeviceGroups=Device Type#All Device Types#Cisco_3650, NetworkDeviceGroups=Groupe Imprimantes#Groupe Imprimantes, NetworkDeviceGroups=APs Indoor ou Outdoor#Groupe APs, IdentityPolicyMatchedRule=Dot1X, AuthorizationPolicyMatchedRule=Some rule, EapTunnel=EAP-FAST, EapAuthentication=EAP-MSCHAPv2, cisco-av-pair=AuthenticationIdentityStore=AD1, cisco-av-pair=FQSubjectName=000000-000-0000-00000000000#host/test, cisco-av-pair=UniqueSubjectID=XXXXXXXXXXXXXXXXXXXXX, CPMSessionID=TestSessionId, EndPointMACAddress=00-01-00-00-00-01, PostureAssessmentStatus=NotApplicable, EndPointMatchedProfile=Unknown, EapChainingResult=User failed and machine succeeded, ISEPolicySetName=WIRELESS_1X_DFS, IdentitySelectionMatchedRule=Dot1X,#015
    ```



=== "test_authentication_failed"

    ```
	0000248509 3 0 2025-02-18 14:34:01.264 +01:00 0005365098 5400 NOTICE Failed-Attempt: Authentication failed, ConfigVersionId=88, Device IP Address=3.4.5.6, Device Port=53874, DestinationIPAddress=5.6.7.8, DestinationPort=1812, RadiusPacketType=AccessRequest, UserName=john.doe, Protocol=Radius, NetworkDeviceName=WLAN, User-Name=john.doe, NAS-IP-Address=2.3.4.5, NAS-Port=1656127488, Called-Station-ID=1.2.3.4, Calling-Station-ID=4.5.6.7, NAS-Port-Type=Virtual, Tunnel-Client-Endpoint=(tag=0) 4.5.6.7, cisco-av-pair=mdm-tlv=device-platform=win, cisco-av-pair=mdm-tlv=device-mac=61-05-38-5c-f8-bd, cisco-av-pair=mdm-tlv=device-platform-version=10.0.26100 , cisco-av-pair=mdm-tlv=device-public-mac=61-05-38-5c-f8-bd, cisco-av-pair=mdm-tlv=device-type=Default string Default string, cisco-av-pair=mdm-tlv=ac-user-agent=AnyConnect Windows 4.6.03049,
    ```



=== "test_conf_events"

    ```
	INFO: Configuration Changed: Admin=john.doe; Object Type=EPPurgeScheduler; Object Name=f36afcff-e3af-4a70-99c0-5e5304c1c336
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
	INFO: EAP Connection Timeout : Server=servername; NAS IP Address=1.2.3.4; NAS Identifier=A4:57:00:64:47:C0:test1
    ```



=== "test_network_info_events1"

    ```
	0000738292 7 0 2025-01-09 09:28:49.914 +01:00 0043796555 5200 NOTICE Passed-Authentication: Authentication succeeded, ConfigVersionId=186, Device IP Address=2.3.4.5, DestinationIPAddress=1.2.3.4, DestinationPort=1812, UserName=testUserName, Protocol=Radius, NetworkDeviceName=MGCUH1-3, User-Name=testUserName, NAS-IP-Address=2.3.4.5, NAS-Port=1001, Service-Type=Framed, Framed-MTU=1449, State=37CPMSessionID=XXXXXXXXXXXXXX\;36SessionID=MGDFSISE2/515448264/543038\;, Called-Station-ID=a0:ec:f9:50:e2:90:DFS, Calling-Station-ID=bc:83:85:d8:88:c6, NAS-Identifier=MGCUH1-3, NAS-Port-Type=Wireless - IEEE 802.11, NAS-Port-Id=Capwap2, EAP-Key-Name=, cisco-av-pair=service-type=Framed, cisco-av-pair=audit-session-id=XXXXXXXXXXXXXX, cisco-av-pair=method=dot1x, cisco-av-pair=cisco-wlan-ssid=DFS, Airespace-Wlan-Id=5, NetworkDeviceProfileName=Cisco, NetworkDeviceProfileId=aaaaaaaaaaaaaaaaaaaaa,#015
    ```



=== "test_network_response"

    ```
	0001514749 7 6  Response={Class=CACS:XXXXXXXXX:asdsa/000000/111111; Tunnel-Type=(tag=1) VLAN; Tunnel-Medium-Type=(tag=1) 802; Tunnel-Private-Group-ID=(tag=1) COMPUTER; EAP-Key-Name=EAP-Key-VALUE; MS-MPPE-Send-Key=****; MS-MPPE-Recv-Key=****; LicenseTypes=1; },#015
    ```



=== "test_network_warm1"

    ```
	WARN: Dynamic Authorization Failed for Device : Server=servername; Calling Station Id=N/A; Network device IP=1.2.3.4; Network Device
    ```



=== "test_network_warm2"

    ```
	WARN: Profiler SNMP Request Failure : Server= servername; NAD Address=1.2.3.4; Error Message=Request timed out.
    ```



=== "test_network_warn_events"

    ```
	WARN: TrustSec deploy verification failed to reach NAD.: Device Name=device005.internal.example.org; Device Ip=1.2.3.4; Device login username=admin
    ```



