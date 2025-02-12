
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "User_id_1_csv"


    ```json
	1,2020/12/04 16:00:02,016401002222,USERID,login,2305,2020/12/04 16:00:02,vsys,1.2.3.4,user1,srv1.example.local,0,1,12000,0,0,active-directory,,968683723,0x8000000000000000,12,0,0,0,,hostexample,1,,2020/12/04 16:00:02,1,0x80,user1
    ```



=== "User_id_2_csv"


    ```json
	1,2020/12/04 16:00:02,01640103000,USERID,login,2200,2020/12/04 16:00:02,vsys,10.0.0.2,user1,srv1.example.local,0,1,13000,0,0,active-directory,,968700000,0x8000000000000000,12,0,0,0,,hostname_example,1,,2020/12/04 16:00:02,1,0x0,user1
    ```



=== "auth_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|AUTH|Radius|3|ProfileToken=xxxxx dtz=UTC rt=Feb 28 2021 18:20:54 deviceExternalId=xxxxxxxxxxxxx PanOSConfigVersion=10.0 PanOSAuthenticatedUserDomain=paloaltonetwork PanOSAuthenticatedUserName=xxxxx PanOSAuthenticatedUserUUID= PanOSClientTypeName= PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSIsDuplicateLog=false PanOSIsPrismaNetworks=false PanOSIsPrismaUsers=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSRuleMatched= start=Feb 28 2021 18:20:40 cs3=vsys1 cs3Label=VirtualLocation c6a2=::ffff:0 c6a2Label=Source IPv6 Address c6a3=::ffff:0 c6a3Label=Destination IPv6 Address duser=paloaltonetwork\\xxxxx cs2=paloaltonetwork\\xxxxx cs2Label=NormalizeUser fname=Authentication object2 cs4=DC cs4Label=AuthenticationPolicy cnt=33554432 cn2=-5257671089978343424 cn2Label=MFAAuthenticationID PanOSMFAVendor=Symantec VIP cs6=rs-logging cs6Label=LogSetting cs1=deny-attackers cs1Label=AuthServerProfile PanOSAuthenticationDescription=www.something cs5=Unknown cs5Label=ClientType msg=Invalid Certificate cn1=0 cn1Label=AuthFactorNo externalId=xxxxxxxxxxxxx PanOSDGHierarchyLevel1=11 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=xxxxx PanOSVirtualSystemID=1 PanOSAuthenticationProtocol=EAP-TTLS with PAP PanOSRuleMatchedUUID= PanOSTimeGeneratedHighResolution=Feb 28 2021 18:20:41 PanOSSourceDeviceCategory=src_category_list-1 PanOSSourceDeviceProfile=src_profile_list-1 PanOSSourceDeviceModel=src_model_list-1 PanOSSourceDeviceVendor=src_vendor_list-1 PanOSSourceDeviceOSFamily=src_osfamily_list-0 PanOSSourceDeviceOSVersion=src_osversion_list-2 PanOSSourceDeviceHost=src_host_list-0 PanOSSourceDeviceMac=src_mac_list-2 PanOSAuthCacheServiceRegion= PanOSUserAgentString= PanOSSessionID=
    ```



=== "decryption_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|DECRYPTION|end|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 20:35:54 PanOSDeviceSN=xxxxxxxxxxxxx PanOSConfigVersion=null start=Mar 01 2021 20:35:54 src=1.1.1.1 dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=allow-all-employees cs1Label=Rule suser=paloaltonetwork\\\\xxxxx duser=paloaltonetwork\\\\xxxxx app=gmail-base cs3=vsys1 cs3Label=VirtualLocation cs4=datacenter cs4Label=FromZone cs5=ethernet4Zone-test1 cs5Label=ToZone deviceInboundInterface=ethernet1/1 deviceOutboundInterface=tunnel.901 cs6=test cs6Label=LogSetting PanOSTimeReceivedManagementPlane=Dec 12 2019 22:16:48 cn1=106112 cn1Label=SessionID cnt=1 spt=16524 dpt=20122 sourceTranslatedPort=15856 destinationTranslatedPort=10128 proto=tcp act=deny PanOSTunnel=N/A PanOSSourceUUID= PanOSDestinationUUID= PanOSRuleUUID=fnullacnullnulle1-2c69-4f2b-8293-46ee4c73737e PanOSClientToFirewall=null PanOSFirewallToClient=null PanOSTLSVersion=null PanOSTLSKeyExchange=null PanOSTLSEncryptionAlgorithm=null PanOSTLSAuth=null PanOSPolicyName= PanOSEllipticCurve= PanOSErrorIndex=null PanOSRootStatus=null PanOSChainStatus=null PanOSProxyType=null PanOSCertificateSerial= PanOSFingerprint= PanOSTimeNotBefore=0 PanOSTimeNotAfter=0 PanOSCertificateVersion=null PanOSCertificateSize=0 PanOSCommonNameLength=0 PanOSIssuerNameLength=0 PanOSRootCNLength=0 PanOSSNILength=0 PanOSCertificateFlags=0 PanOSCommonName= PanOSIssuerCommonName= PanOSRootCommonName= PanOSServerNameIndication= PanOSErrorMessage= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup=test PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12 PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceHost= PanOSSourceDeviceMac= PanOSDestinationDeviceCategory= PanOSDestinationDeviceProfile= PanOSDestinationDeviceModel= PanOSDestinationDeviceVendor= PanOSDestinationDeviceOSFamily= PanOSDestinationDeviceOSVersion= PanOSDestinationDeviceHost= PanOSDestinationDeviceMac= externalId=xxxxxxxxxxxxx
    ```



=== "file_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|THREAT|file|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:06:06 deviceExternalId=xxxxxxxxxxxxx PanOSConfigVersion= PanOSApplicationCategory=collaboration PanOSApplicationContainer= PanOSApplicationRisk=5 PanOSApplicationSubcategory=email PanOSApplicationTechnology=client-server PanOSCaptivePortal=false PanOSCloudHostname=PA-5220 PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDLPVersionFlag= PanOSDestinationDeviceClass= PanOSDestinationDeviceOS= dntdom= duser= duid= PanOSFileType=PNG File Upload PanOSInboundInterfaceDetailsPort=19 PanOSInboundInterfaceDetailsSlot=1 PanOSInboundInterfaceDetailsType=ethernet PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer=false PanOSIsContainer=false PanOSIsDecryptMirror=false PanOSIsDecrypted= PanOSIsDuplicateLog=false PanOSIsEncrypted= PanOSIsIPV6= PanOSIsMptcpOn=false PanOSIsNonStandardDestinationPort=false PanOSIsPacketCapture=false PanOSIsPhishing=false PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy=false PanOSIsReconExcluded=false PanOSIsSaaSApplication=false PanOSIsServertoClient=false PanOSIsSourceXForwarded= PanOSIsSystemReturn=false PanOSIsTransaction=false PanOSIsTunnelInspected=false PanOSIsURLDenied=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT=false PanOSNonStandardDestinationPort=0 PanOSOutboundInterfaceDetailsPort=19 PanOSOutboundInterfaceDetailsSlot=1 PanOSOutboundInterfaceDetailsType=ethernet PanOSOutboundInterfaceDetailsUnit=0 PanOSPacket= PanOSProfileName= PanOSSanctionedStateOfApp=false PanOSSeverity=Low PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom= suser= suid= PanOSThreatCategory= PanOSThreatNameFirewall= PanOSTunneledApplication=untunneled PanOSURL= PanOSUsers=1.1.1.1 PanOSVirtualSystemID=1 start=Mar 01 2021 21:06:06 src=1.1.1.1 dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=dg-log-policy cs1Label=Rule suser0= duser0= app=smtp cs3=smtp cs3Label=VirtualLocation cs4=tap cs4Label=FromZone cs5=tap cs5Label=ToZone deviceInboundInterface=ethernet1/19 deviceOutboundInterface=ethernet1/19 cs6=test cs6Label=LogSetting cn1=4016143 cn1Label=SessionID cnt=9 spt=37404 dpt=25 sourceTranslatedPort=0 destinationTranslatedPort=0 proto=tcp act=alert filePath=page-icon.png cs2=any cs2Label=URLCategory flexString2=client to server flexString2Label=DirectionOfAttack externalId=xxxxxxxxxxxxx PanOSSourceLocation=1.1.1.1-1.1.1.1 PanOSDestinationLocation=1.1.1.1-1.1.1.1 fileId=0 PanOSFileHash= PanOSReportID= PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStartTime=Jan 01 1970 00:00:00 PanOSTunnel=N/A PanOSContentVersion= PanOSSigFlags=0 PanOSRuleUUID= PanOSHTTP2Connection= PanOSDynamicUserGroup= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceHost= PanOSSourceDeviceMac= PanOSDestinationDeviceCategory= PanOSDestinationDeviceProfile= PanOSDestinationDeviceModel= PanOSDestinationDeviceVendor= PanOSDestinationDeviceOSFamily= PanOSDestinationDeviceOSVersion= PanOSDestinationDeviceHost= PanOSDestinationDeviceMac= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSHostID=xxxxxxxxxxxxxx PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSDomainEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSPartialHash= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12 PanOSReasonForDataFilteringAction= PanOSJustification= PanOSNSSAINetworkSliceType=
    ```



=== "fix_bug_with_int"


    ```json
	1,2023/06/16 10:41:44,001701003551,TRAFFIC,end,2305,2023/06/16 10:41:44,1.2.3.4,5.6.7.8,0.0.0.0,0.0.0.0,GEN_WINLOG_Users,domain\pusername,userdest,windows-remote-management,vsys1,PDT_STD,INFRA_ADM,aaa.111,aaa.111,Syslog_Test,2023/06/16 10:41:44,234981,1,51413,5985,0,0,15,tcp,allow,2346,1974,372,9,90,16,30,0,69678105127,0x0,10.0.0.0-10.255.255.255,10.0.0.0-10.255.255.255,0,6,3,tcp-fin,0,0,0,0,,FWPA01,from-policy,,,0,,0,,N/A,0,0,0,0,5e7eca5b-f585-4633-bbd4-9ed431f7f95b,0,0,,,,,,,
    ```



=== "fix_bug_without_int"


    ```json
	1,2023/06/16 10:41:44,001701003551,TRAFFIC,end,2305,2023/06/16 10:41:44,1.2.3.4,5.6.7.8,0.0.0.0,0.0.0.0,GEN_WINLOG_Users,domainusername,destuser,windows-remote-management,vsys1,PDT_STD,INFRA_ADM,aaa.111,aaa.111,Syslog_Test,2023/06/16 10:41:44,234981,1,51413,5985,0,0,0x1c,tcp,allow,2346,1974,372,9,2023/06/16 10:41:26,16,not-resolved,0,69678105127,0x0,10.0.0.0-10.255.255.255,10.0.0.0-10.255.255.255,0,6,3,tcp-fin,0,0,0,0,,FWPA01,from-policy,,,0,,0,,N/A,0,0,0,0,5e7eca5b-f585-4633-bbd4-9ed431f7f95b,0,0,,,,,,,
    ```



=== "globalprotect_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|GLOBALPROTECT|globalprotect|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 20:35:54 PanOSDeviceSN=xxxxxxxxxxxxx PanOSConfigVersion= start=Mar 01 2021 20:35:54 PanOSVirtualSystem=vsys1 PanOSEventIDValue=satellite-gateway-update-route PanOSStage=connected PanOSAuthMethod=RADIUS PanOSTunnelType=ipsec PanOSSourceUserName=xxxxx\\\\xxxxx PanOSSourceRegion=ET PanOSEndpointDeviceName=machine_name2 PanOSPublicIPv4=1.1.1.1 PanOSPublicIPv6=xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx PanOSPrivateIPv4=1.1.1.1 PanOSPrivateIPv6=xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx PanOSHostID=xxxxxxxxxxxxxxe667947f-d92e-4815-9222-89438203bc2b PanOSEndpointSN=serialno_list-1 PanOSGlobalProtectClientVersion=3.0.9 PanOSEndpointOSType=Intel Mac OS PanOSEndpointOSVersion=9.3.5 PanOSCountOfRepeats=16777216 PanOSQuarantineReason=Malicious Traffic PanOSConnectionError=Client cert not present PanOSDescription=opaque_list-1 PanOSEventStatus=failure PanOSGlobalProtectGatewayLocation=San Francisco PanOSLoginDuration=1 PanOSConnectionMethod=connect_method_list-1 PanOSConnectionErrorID=0 PanOSPortal=portal_list-2 PanOSSequenceNo=34401910 PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12 PanOSGatewaySelectionType= PanOSSSLResponseTime= PanOSGatewayPriority= PanOSAttemptedGateways= PanOSGateway= PanOSDGHierarchyLevel1=20 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= PanOSDeviceName=PA-VM PanOSVirtualSystemID=1
    ```



=== "globalprotect_csv"


    ```json
	1,2020/12/08 14:30:55,011111114444,GLOBALPROTECT,0,2305,2020/12/08 13:30:55,vsys1,gw-auth,login,Other,,user,FR,AAAABBBBB,1.2.3.4,0.0.0.0,0.0.0.0,0.0.0.0,aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee,ABCDEFG,5.1.4,Windows,"Microsoft Windows 10 Pro , 64-bit",1,,,"",success,,0,user-logon,0,gw1,1234567,0x8000000000000000
    ```



=== "globalprotect_csv_2"


    ```json
	1,2023/06/28 14:40:42,015451000032715,GLOBALPROTECT,0,2562,2023/06/28 14:40:42,vsys1,gateway-config-release,configuration,,,example.org\\test,EN,2021-02707,88.120.236.74,0.0.0.0,10.0.0.232,0.0.0.0,8f0fd1d3-5d3b-49c3-9bee-247ff89a52f3,DFN3535D,6.0.4,Windows,"Microsoft Windows 10 Enterprise , 64-bit",1,,,,success,,0,,0,VPN_GATEWAY,5555555555555555555,0x8000000000000000,2023-06-28T14:40:43.134+02:00,,,,,,0,0,0,0,,VPN-DOM-01,1

    ```



=== "hip_match_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|HIPMATCH||3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:20:13 deviceExternalId=xxxxxxxxxxxxx PanOSIsDuplicateLog=false PanOSIsPrismaNetworks=false PanOSIsPrismaUsers=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom=xxxxx dntdom=xxxxx suser=xxxxx xxxxx duser=xxxxx xxxxx suid= duid= PanOSTenantID=xxxxxxxxxxxxx PanOSUUID= PanOSConfigVersion= start=Mar 01 2021 21:20:13 PanOSSourceUser=xxxxx\\xxxxx xxxxx cs3=vsys1 cs3Label=VirtualLocation shost=machine_name1 dhost=machine_name1 cs2=iOS cs2Label=EndpointOSType src=1.1.1.1 dst=1.1.1.1 cat=match_name1 cnt=1 PanOSHipMatchType=HIP Profile externalId=xxxxxxxxxxxxx PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 cn2=1 cn2Label=VirtualSystemID c6a1=xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx c6a1Label=Device IPv6 Address PanOSHostID=xxxxxxxxxxxxxxe777947f-d92e-4815-9222-89438203bc2b PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceMac= PanOSSourceDeviceHost= PanOSSource= PanOSTimestampDeviceIdentification=Dec PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12
    ```



=== "icmp_allow_csv"


    ```json
	<14>Sep 16 10:00:02 PP 1,9/16/19 10:00,1801017000,TRAFFIC,start,2049,9/16/19 10:00,1.2.3.4,4.3.2.1,1.2.3.4,10.0.1.2,PING,,,ping,vsys,AAAAA,Zone1,ethernet1/1,ae2.11,Secure,9/16/19 10:00,24100,3,0,0,0,0,0x500000,icmp,allow,222,222,0,3,9/16/19 10:00,0,any,0,50660388939,0x0,Spain,France,0,3,0,n/a,0,0,0,0,,PA,from-policy,,,0,,0,,N/A,0,0,0,0
    ```



=== "iptag_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|IPTAG|iptag|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:20:13 deviceExternalId=xxxxxxxxxxxxx PanOSTenantID=xxxxxxxxxxxxx PanOSIsDuplicateLog=false PanOSIsPrismaNetworks=false PanOSIsPrismaUsers=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSetting= PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSRuleMatched= PanOSRuleMatchedUUID= PanOSConfigVersion= start=Mar 01 2021 21:20:13 cs3=vsys1 cs3Label=VirtualLocation src=1.1.1.1 dst=1.1.1.1 PanOSTagName= PanOSEventID=Unregister cnt=1 PanOSMappingTimeout=10 PanOSMappingDataSource=XMLAPI PanOSMappingDataSourceType=XML-API PanOSMappingDataSourceSubType=Unknown externalId=xxxxxxxxxxxxx PanOSDGHierarchyLevel1=18 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-VM cn2=1 cn2Label=VirtualSystemID PanOSIPSubnetRange= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12
    ```



=== "network_threat_alert_1"


    ```json
	{
        "TimeReceived": "2024-06-25T21:32:54.000000Z",
        "DeviceSN": "000011111112222",
        "LogType": "THREAT",
        "Subtype": "url",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-06-25T21:30:00.000000Z",
        "SourceAddress": "1.2.3.4",
        "DestinationAddress": "5.6.7.8",
        "NATSource": "4.3.2.1",
        "NATDestination": "8.7.6.5",
        "Rule": "Rule124",
        "SourceUser": null,
        "DestinationUser": null,
        "Application": "ssl",
        "VirtualLocation": "vsys1",
        "FromZone": "INSIDE",
        "ToZone": "OUTSIDE",
        "InboundInterface": "ethernet1/2",
        "OutboundInterface": "ethernet1/1",
        "LogSetting": "Panorama_CDL",
        "SessionID": 155600,
        "RepeatCount": 1,
        "SourcePort": 51501,
        "DestinationPort": 443,
        "NATSourcePort": 63989,
        "NATDestinationPort": 443,
        "Protocol": "tcp",
        "Action": "alert",
        "URL": "www.example.org",
        "URLCategory": "computer-and-internet-info",
        "VendorSeverity": "Informational",
        "DirectionOfAttack": "client to server",
        "SequenceNo": 7353954110769176067,
        "SourceLocation": "AZURE-EU-WEST-CBS-BELLEM",
        "DestinationLocation": "NL",
        "ContentType": null,
        "PacketID": 0,
        "URLCounter": 0,
        "UserAgent": null,
        "X-Forwarded-For": null,
        "Referer": null,
        "DGHierarchyLevel1": 982,
        "DGHierarchyLevel2": 117,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "DN-EUWEST-F2",
        "SourceUUID": null,
        "DestinationUUID": null,
        "HTTPMethod": "unknown",
        "IMSI": 0,
        "IMEI": null,
        "ParentSessionID": 0,
        "ParentStarttime": "1970-01-01T00:00:00.000000Z",
        "Tunnel": "N/A",
        "InlineMLVerdict": "unknown",
        "ContentVersion": "0",
        "SigFlags": 0,
        "HTTPHeaders": null,
        "URLCategoryList": "computer-and-internet-info,low-risk",
        "RuleUUID": "cbc3bd5d-e54c-48d7-a6c7-8710bf593e7c",
        "HTTP2Connection": 0,
        "DynamicUserGroupName": null,
        "X-Forwarded-ForIP": null,
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "ContainerID": null,
        "ContainerNameSpace": null,
        "ContainerName": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "HostID": null,
        "EndpointSerialNumber": null,
        "SourceDynamicAddressGroup": null,
        "DestinationDynamicAddressGroup": null,
        "TimeGeneratedHighResolution": "2024-06-25T21:30:00.103000Z",
        "NSSAINetworkSliceType": null
    }
    ```



=== "network_threat_alert_2"


    ```json
	{
        "TimeReceived": "2024-06-25T21:30:08.000000Z",
        "DeviceSN": "no-serial",
        "LogType": "THREAT",
        "Subtype": "url",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-06-25T21:30:00.000000Z",
        "SourceAddress": "1.2.3.4",
        "DestinationAddress": "5.6.7.8",
        "NATSource": "4.3.2.1",
        "NATDestination": "8.7.6.5",
        "Rule": "Global_Internet_Network_Awareness_Service",
        "SourceUser": "jdoe@example.org",
        "DestinationUser": null,
        "Application": "web-browsing",
        "VirtualLocation": "vsys1",
        "FromZone": "ZR-EUWS-1",
        "ToZone": "untrust",
        "InboundInterface": "tunnel.107",
        "OutboundInterface": "ethernet1/1",
        "LogSetting": "default",
        "SessionID": 1787364,
        "RepeatCount": 1,
        "SourcePort": 53610,
        "DestinationPort": 80,
        "NATSourcePort": 36160,
        "NATDestinationPort": 80,
        "Protocol": "tcp",
        "Action": "alert",
        "URL": "www.example.com/connecttest.txt",
        "URLCategory": "computer-and-internet-info",
        "VendorSeverity": "Informational",
        "DirectionOfAttack": "client to server",
        "SequenceNo": 7372845116442397960,
        "SourceLocation": "10.0.0.0-10.255.255.255",
        "DestinationLocation": "US",
        "ContentType": "text/plain",
        "PacketID": 0,
        "URLCounter": 1,
        "UserAgent": "Microsoft NCSI",
        "X-Forwarded-For": null,
        "Referer": null,
        "DGHierarchyLevel1": 463,
        "DGHierarchyLevel2": 525,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "ZR-EUWS-1",
        "SourceUUID": null,
        "DestinationUUID": null,
        "HTTPMethod": "get",
        "IMSI": 0,
        "IMEI": null,
        "ParentSessionID": 0,
        "ParentStarttime": "1970-01-01T00:00:00.000000Z",
        "Tunnel": "N/A",
        "InlineMLVerdict": "unknown",
        "ContentVersion": "0",
        "SigFlags": 0,
        "HTTPHeaders": null,
        "URLCategoryList": ".msftconnecttest.com,computer-and-internet-info,low-risk",
        "RuleUUID": "481a523a-44c0-4c37-b2d5-b6b541d775c3",
        "HTTP2Connection": 0,
        "DynamicUserGroupName": null,
        "X-Forwarded-ForIP": null,
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "ContainerID": null,
        "ContainerNameSpace": null,
        "ContainerName": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "HostID": null,
        "EndpointSerialNumber": null,
        "SourceDynamicAddressGroup": null,
        "DestinationDynamicAddressGroup": null,
        "TimeGeneratedHighResolution": "2024-06-25T21:30:00.778000Z",
        "NSSAINetworkSliceType": null
    }
    ```



=== "sctp_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|SCTP||9|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:22:02 deviceExternalId=xxxxxxxxxxxxx PanOSCaptivePortal= PanOSContentVersion= PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceMac= PanOSDestinationDeviceModel= PanOSDestinationDeviceOS= PanOSDestinationDeviceVendor= PanOSDestinationLocation=IN PanOSDestinationUUID= PanOSDestinationUserDomain=paloaltonetwork PanOSDestinationUserName=xxxxx PanOSDestinationUserUUID= PanOSInboundInterfaceDetailsPort=1 PanOSInboundInterfaceDetailsSlot=1 PanOSInboundInterfaceDetailsType=ethernet PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer= PanOSIsContainer= PanOSIsDecryptMirror= PanOSIsDecryptedLog= PanOSIsDecryptedPayloadForward= PanOSIsDuplicateLog=false PanOSIsIPV6= PanOSIsInspectrionBeforeSession= PanOSIsMptcpOn= PanOSIsNonStandardDestinationPort= PanOSIsPacketCapture= PanOSIsPhishing= PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy= PanOSIsReconExcluded= PanOSIsServertoClient= PanOSIsSourceXForwarded= PanOSIsSystemReturn= PanOSIsTransaction= PanOSIsTunnelInspected= PanOSIsURLDenied= PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT= PanOSOutboundInterfaceDetailsPort=2 PanOSOutboundInterfaceDetailsSlot=1 PanOSOutboundInterfaceDetailsType=ethernet PanOSOutboundInterfaceDetailsUnit=0 PanOSSessionEndReason= PanOSSessionOwnerMidx= PanOSSessionTracker= PanOSSeverity=Critical PanOSSourceDeviceClass= PanOSSourceDeviceMac= PanOSSourceDeviceModel= PanOSSourceDeviceOS= PanOSSourceDeviceVendor= PanOSSourceLocation=US PanOSSourceUUID= PanOSSourceUserDomain=paloaltonetwork PanOSSourceUserName=xxxxx PanOSSourceUserUUID= PanOSTunnel=N/A PanOSVirtualSystemID=1 PanOSConfigVersion= start=Mar 01 2021 21:22:02 src=1.1.1.1 dst=1.1.1.1 PanOSNATSource=1.1.1.1 PanOSNATDestination=1.1.1.1 cs1=allow-business-apps cs1Label=Rule PanOSSourceUser=paloaltonetwork\\xxxxx PanOSDestinationUser=paloaltonetworkxxxxx PanOSApplication=panorama cs3=vsys1 cs3Label=VirtualLocation cs4=corporate cs4Label=FromZone cs5=untrust cs5Label=ToZone PanOSInboundInterface=ethernet1/1 deviceOutboundInterface=ethernet1/2 cs6=test cs6Label=LogSetting PanOSSessionID=391582 cnt=1 spt=3033 dpt=5496 PanOSNATSourcePort=26714 PanOSNATDestinationPort=15054 proto=tcp act=alert PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 externalId=xxxxxxxxxxxxx PanOSEndpointAssociationID=2086888838 PanOSPayloadProtocolID=-1 PanOSSctpChunkType=9 PanOSSCTPEventType=Kerberos single sign-on failed PanOSEventCode=3 PanOSVerificationTag1=0x3bae3042 PanOSVerificationTag2=0x1911015e PanOSSctpCauseCode=0 PanOSDiamAppID=-1 PanOSDiameterCommandCode=-1 PanOSDiamAvpCode=0 PanOSStreamID=0 PanOSAssocationEndReason= PanOSMapAppCode=0 PanOSSccpCallingSSN=0 PanOSSccpCallingGt= PanOSSctpFilter= PanOSChunksTotal=0 PanOSChunksSent=0 PanOSChunksReceived=0 PanOSPacketsTotal=0 PanOSPacketsSent=0 PanOSPacketsReceived=0 PanOSRuleUUID= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12
    ```



=== "system_csv"


    ```json
	1,2020/12/08 13:44:55,11111114444,SYSTEM,auth,0,2020/12/08 13:44:55,,auth-success,GP,0,0,general,informational,"authenticated for user 'user1'.   auth profile 'GP', vsys 'vsys123', server profile 'LDAP', server address 'srv01.entreprise.local', From: 1.2.3.4.",5211100,0x8000000000000000,0,0,0,0,,fw1
    ```



=== "tcp_allow_csv"


    ```json
	<14>Sep 16 10:00:02 PA-1 1,9/16/19 10:00,1801016000,TRAFFIC,start,2049,9/16/19 10:00,1.2.3.4,4.3.2.1,0.0.0.0,0.0.0.0,proxy1,,,web-browsing,vsys1234,v10213,zone1,a.1,b.2,Secure,9/16/19 10:00,60000,1,61000,80,0,0,0x0,tcp,allow,800,700,70,2,9/16/19 10:00,0,any,0,50660381839,0x0,10.0.0.0-10.255.255.255,10.0.0.0-10.255.255.255,0,2,1,n/a,0,0,0,0,,PP,from-policy,,,0,,0,,N/A,0,0,0,0
    ```



=== "test_cloud_election_json"


    ```json
	{
        "LogTime": "2023-02-16T15:36:37.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "url-filtering",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:36:23.000000Z",
        "VirtualLocation": null,
        "EventName": "cloud-election",
        "EventComponent": "",
        "VendorSeverity": "Informational",
        "EventDescription": "CLOUD ELECTION: serverlist2.urlcloud.paloaltonetworks.com IP: 35.244.229.101 was elected, measured alive test 143294.",
        "SequenceNo": 7200776623254143113,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:36:23.710000Z"
    }
    ```



=== "test_decryption_csv"


    ```json
	1,2024/11/03 19:09:43,111111111111,DECRYPTION,0,2562,2024/11/03 19:09:43,1.2.3.4,5.6.7.8,4.3.2.1,8.7.6.5,URL Filtering - Chrome Profile,jdoe,,ssl,vsys1,VPN-SSL,INTERNET,tunnel.16,ae2.1111,Forward-Syslog,2024/11/03 19:09:43,2020391,1,55107,443,22814,443,0x400400,tcp,allow,N/A,,,,,25185364-4f1b-46b5-a376-a96a9438d665,Unknown,Unknown,TLS1.3,ECDHE,AES_256_GCM,SHA384,NoDecrypt-rule,,None,uninspected,Uninspected,No Decrypt,,,,,V1,0,0,0,0,0,:::::NONE,,,,,,,,,,,,,2024-11-03T19:09:43.654+01:00,,,,,,,,,,,,,,,,,1111111111111111111,0x8000000000000000,53,0,0,0,,NFW-OUT-DCA,1,encrypted-tunnel,networking,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,ssl,no,no

    ```



=== "test_decryption_json"


    ```json
	{
        "TimeReceived": "2024-11-20T16:40:01.000000Z",
        "DeviceSN": "no-serial",
        "LogType": "DECRYPTION",
        "Subtype": "start",
        "SubType": "start",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-11-20T16:39:51.000000Z",
        "SourceAddress": "1.2.3.4",
        "DestinationAddress": "5.6.7.8",
        "NATSource": "4.3.2.1",
        "NATDestination": "8.7.6.5",
        "Rule": "URL Filtering - Chrome Profile",
        "SourceUser": "example\\jdoe",
        "DestinationUser": null,
        "Application": "incomplete",
        "VirtualLocation": "vsys1",
        "FromZone": "VPN-SSL",
        "ToZone": "INTERNET",
        "InboundInterface": "tunnel.16",
        "OutboundInterface": "ethernet1/1",
        "LogSetting": "Forward-Syslog",
        "TimeReceivedManagementPlane": "2024-11-20T16:39:51.000000Z",
        "SessionID": 2222222,
        "RepeatCount": 1,
        "CountOfRepeat": 1,
        "SourcePort": 58877,
        "DestinationPort": 443,
        "NATSourcePort": 1042,
        "NATDestinationPort": 443,
        "Protocol": "tcp",
        "Action": "allow",
        "Tunnel": "N/A",
        "SourceUUID": null,
        "DestinationUUID": null,
        "RuleUUID": "eaf45b26-01ef-496c-990d-bbd1d89f2ed5",
        "ClientToFirewall": "Finished",
        "FirewallToClient": "Client_Hello",
        "TLSVersion": "TLS1.2",
        "TLSKeyExchange": "ECDHE",
        "TLSEncryptionAlgorithm": "AES_256_GCM",
        "TLSAuth": "SHA384",
        "PolicyName": "TLS - https inspection - default rule",
        "EllipticCurve": "secp256r1",
        "ErrorIndex": "Protocol",
        "RootStatus": "trusted",
        "ChainStatus": "Trusted",
        "ProxyType": "Forward",
        "CertificateSerial": "059125d73c34a73fca9",
        "Fingerprint": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "TimeNotBefore": 1730875569,
        "TimeNotAfter": 1765176368,
        "CertificateVersion": "V3",
        "CertificateSize": 256,
        "CommonNameLength": 13,
        "IssuerNameLength": 29,
        "RootCNLength": 10,
        "SNILength": 23,
        "CertificateFlags": 4,
        "CommonName": "example.org",
        "IssuerCommonName": "GlobalSign ECC OV SSL CA 2018",
        "RootCommonName": "GlobalSign",
        "ServerNameIndication": "static.files.example.org",
        "ErrorMessage": "General TLS protocol error. Received fatal alert DecodeError from server",
        "ContainerID": null,
        "ContainerNameSpace": null,
        "ContainerName": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "SourceDynamicAddressGroup": null,
        "DestinationDynamicAddressGroup": null,
        "TimeGeneratedHighResolution": "2024-11-20T16:39:51.441000Z",
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "SequenceNo": 1111111111111111111
    }
    ```



=== "test_dhcp_renew_json"


    ```json
	{
        "LogTime": "2023-02-16T17:08:26.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "dhcp",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T17:08:17.000000Z",
        "VirtualLocation": null,
        "EventName": "if-renew-trigger",
        "EventComponent": "",
        "VendorSeverity": "Informational",
        "EventDescription": "DHCP RENEW: interface eth0, ip 1.2.3.4 netmask 255.255.255.0 dhcp server: 1.2.3.1",
        "SequenceNo": 7200776623254143234,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T17:08:17.774000Z"
    }
    ```



=== "test_dns_proxy_json"


    ```json
	{
        "LogTime": "2023-02-16T15:31:51.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "dnsproxy",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:31:50.000000Z",
        "VirtualLocation": null,
        "EventName": "if-inherit",
        "EventComponent": "mgmt-obj",
        "VendorSeverity": "Informational",
        "EventDescription": "DNS Proxy object: mgmt-obj inherited following values from dynamic interface: mgmt-if: Primary DNS: 1.2.3.1 Secondary DNS: ::",
        "SequenceNo": 7200776623254142979,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:31:50.584000Z"
    }
    ```



=== "test_dns_response"


    ```json
	{
        "VendorName": "test networks",
        "DeviceSN": "7FD26D6XXXXXXXX",
        "TimeReceived": "2024-07-08T09:01:10.502737Z",
        "LogType": "DNS",
        "Subtype": "realtime_dns_telemetry_response",
        "SubType": "realtime_dns_telemetry_response",
        "TimeGenerated": "2024-07-08T09:01:10.000000Z",
        "RecordType": "a",
        "DNSResolverIP": "1.2.3.4",
        "ThreatID": 0,
        "DNSCategory": "benign",
        "ThreatName": null,
        "SourceAddress": "5.6.7.8",
        "FromZone": "trust",
        "Action": "Allow",
        "DNSResponse": [
            "8.9.1.2"
        ],
        "ToZone": null,
        "DestinationUser": null
    }
    ```



=== "test_event_reason"


    ```json
	1,2024/10/25 16:04:52,024101011111,SYSTEM,userid,2522,2024/10/25 16:04:52,,connect-server-monitor-failure,,0,0,general,high,"User-ID server monitor test05(vsystest) Access denied",7389706522298800000,0x0,0,0,0,0,,FFFFF01,0,0,2024-10-25T16:04:52.574+02:00
    ```



=== "test_event_reason1"


    ```json
	1,2024/10/25 16:10:48,024101010000,SYSTEM,userid,2562,2024/10/25 16:10:48,,connect-ldap-sever,1.2.3.4,0,0,general,informational,"ldap cfg joe_done connected to server 5.6.7.8:333, initiated by: 0.0.1.1",73897065222988700000,0x0,0,0,0,0,,FFFFFF01,0,0,2024-10-25T16:10:48.575+02:00
    ```



=== "test_event_reason2"


    ```json
	1,2024/10/22 08:54:16,024101011111,SYSTEM,auth,2511,2024/10/22 08:54:17,,auth-success,FFFF,0,0,general,informational,"When authenticating user joe1595 from 1.2.3.4, a less secure authentication method PAP is used. Please migrate to PEAP or EAP-TTLS. Authentication Profile FFFF, vsys shared, Server Profile SERVER_TEST, Server Address 5.6.7.8",7389706522298800000,0x0,0,0,0,0,,FWPAN01,0,0,2024-10-22T08:54:17.012+02:0
    ```



=== "test_event_reason3"


    ```json
	1,2024/10/22 09:29:30,024101011111,SYSTEM,auth,2562,2024/10/22 09:29:30,,auth-success,FFFF,0,0,general,informational,"authenticated for user joe979.   auth profile FFFF, vsys shared, server profile server-test, server address 1.7.4.4, auth protocol PAP, admin role superuser, From: 1.2.2.7.",738970652229833333,0x0,0,0,0,0,,FFFF01,0,0,2024-10-22T09:29:30.605+02:00
    ```



=== "test_file_alert_json"


    ```json
	{
        "TimeReceived": "2024-02-06T18:17:09.000000Z",
        "DeviceSN": "no-serial",
        "LogType": "THREAT",
        "Subtype": "file",
        "SubType": "file",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-02-06T18:17:02.000000Z",
        "SourceAddress": "1.2.3.4",
        "DestinationAddress": "5.6.7.8",
        "NATSource": "9.10.11.12",
        "NATDestination": "5.6.7.8",
        "Rule": "Global_Outbound_internet_access",
        "SourceUser": "john.doe@example.com",
        "DestinationUser": null,
        "Application": "web-browsing",
        "VirtualLocation": "vsys1",
        "FromZone": "trust",
        "ToZone": "untrust",
        "InboundInterface": "tunnel.1",
        "OutboundInterface": "ethernet1/1",
        "LogSetting": "default",
        "SessionID": 1450762,
        "RepeatCount": 1,
        "SourcePort": 53514,
        "DestinationPort": 80,
        "NATSourcePort": 22444,
        "NATDestinationPort": 80,
        "Protocol": "tcp",
        "Action": "alert",
        "FileName": "some_file_name",
        "URLCategory": "computer-and-internet-info",
        "VendorSeverity": "Low",
        "DirectionOfAttack": "server to client",
        "SequenceNo": 7292474944208657622,
        "SourceLocation": "Prisma-Mobile-Users-EMEA",
        "DestinationLocation": "US",
        "PacketID": 0,
        "FileHash": null,
        "ReportID": 0,
        "DGHierarchyLevel1": 463,
        "DGHierarchyLevel2": 467,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "GP cloud service",
        "SourceUUID": null,
        "DestinationUUID": null,
        "IMSI": 0,
        "IMEI": null,
        "ParentSessionID": 0,
        "ParentStartTime": "1970-01-01T00:00:00.000000Z",
        "Tunnel": "N/A",
        "ContentVersion": "577053022",
        "SigFlags": 0,
        "RuleUUID": "c38e111b-43fc-4de4-a17c-c372af557193",
        "HTTP2Connection": 0,
        "DynamicUserGroup": null,
        "X-Forwarded-ForIP": null,
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "ContainerID": null,
        "ContainerNameSpace": null,
        "ContainerName": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "HostID": null,
        "EndpointSerialNumber": null,
        "DomainEDL": null,
        "SourceDynamicAddressGroup": null,
        "DestinationDynamicAddressGroup": null,
        "PartialHash": 0,
        "TimeGeneratedHighResolution": "2024-02-06T18:17:02.077000Z",
        "ReasonForDataFilteringAction": null,
        "Justification": null,
        "NSSAINetworkSliceType": null
    }
    ```



=== "test_globalprotect"


    ```json
	1,2024/01/12 11:41:42,015451000023232323,GLOBALPROTECT,0,2562,2024/01/12 11:41:42,vsys1,gateway-switch-to-ssl,tunnel,,SSLVPN,test.fr\JDOE,FR,2023-01724,1.2.3.4,0.0.0.0,1.2.3.4,0.0.0.0,662f0b44-e024-4a70,PF000000,6.0.4,Windows,"Microsoft Windows 10 Enterprise , 64-bit",1,,,,success,,0,,0,CD78_VPN_GP_GATEWAY,5555555555555555555,0x8000000000000000,2024-01-12T11:41:43.895+02:00,,,,,,0,0,0,0,,test-01-01,1
    ```



=== "test_hipmatch_csv"


    ```json
	1,2024/11/03 18:50:04,111111111111,HIPMATCH,0,1111,2024/11/03 18:50:04,jdoe,vsys1,DESKTOP-01,Windows,1.2.3.4,VPN Compliant,1,profile,,,1111111111111111111,0x8000000000000000,28,99,38,0,,FW-CIV1,1,0.0.0.0,3a7393a4-997f-4e5b-b6e4-4ebff71dacf4,aefee8,,2024-11-03T18:50:04.310+01:00,
    ```



=== "test_hipmatch_json"


    ```json
	{
        "TimeReceived": "2024-11-20T16:30:32.000000Z",
        "DeviceSN": "no-serial",
        "LogType": "HIPMATCH",
        "Subtype": "hipmatch",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-11-20T16:30:28.000000Z",
        "SourceUser": "jdoe@example.org",
        "VirtualLocation": "vsys1",
        "EndpointDeviceName": "DESKTOP-01",
        "EndpointOSType": "Windows",
        "SourceIP": "1.2.3.4",
        "HipMatchName": "VPN Compliant",
        "RepeatCount": 1,
        "CountOfRepeats": 1,
        "HipMatchType": "profile",
        "SequenceNo": 1111111111111111111,
        "DGHierarchyLevel1": 12,
        "DGHierarchyLevel2": 22,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "FW-ALK01",
        "VirtualSystemID": 1,
        "SourceIPv6": "",
        "HostID": "3a7393a4-997f-4e5b-b6e4-4ebff71dacf4",
        "EndpointSerialNumber": "aefee8",
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceMac": null,
        "SourceDeviceHost": null,
        "Source": null,
        "TimestampDeviceIdentification": null,
        "TimeGeneratedHighResolution": "2024-11-20T16:30:28.904000Z"
    }
    ```



=== "test_installed_package_json"


    ```json
	{
        "LogTime": "2023-02-16T15:49:04.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "general",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:48:57.000000Z",
        "VirtualLocation": "",
        "EventName": "general",
        "EventComponent": null,
        "VendorSeverity": "Informational",
        "EventDescription": "Installed contents package: panupv2-all-contents-8676-7858.tgz",
        "SequenceNo": 7200776623254143152,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:48:57.395000Z"
    }
    ```



=== "test_ldap_brute_force"


    ```json
	1,2024/08/03 12:16:42,012001002253,THREAT,vulnerability,2561,2024/08/03 12:17:45,5.6.7.8,1.2.3.4,0.0.0.0,0.0.0.0,IN_VPN-AZURE-ALSID,,paloaltonetwork\\username,ldap,vsys1,VPN,LAN,tunnel.3,ethernet1/4,default,2024/08/03 12:17:45,110079,1,62074,389,0,0,0x80002000,tcp,alert,,LDAP: User Login Brute Force Attempt(40005),any,high,client-to-server,7395125856205392467,0x8000000000000000,192.168.0.0-192.168.255.255,172.16.0.0-172.31.255.255,,,1210225322167894624,,,0,,,,,,,,0,24,315,0,0,,hostname_example,,,,,0,,0,,N/A,brute-force,AppThreat-8877-8886,0x0,0,4294967295,,,2c146dd4-d96a-455f-96fc-7f3e2c37c70d,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,0,2024-08-03T12:17:45.360+02:00,,,,auth-service,business-systems,client-server,2,\"has-known-vulnerability,tunnel-other-application,pervasive-use\",,untunneled,no,no,
    ```



=== "test_new_file_type"


    ```json
	{
        "TimeReceived": "2024-07-08T08:33:33.000000Z",
        "DeviceSN": "007954000XXXXXX",
        "LogType": "THREAT",
        "Subtype": "file",
        "SubType": "file",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-07-08T15:30:04.000000Z",
        "SourceAddress": "4.3.2.1",
        "DestinationAddress": "5.2.1.8",
        "NATSource": "2.2.1.6",
        "NATDestination": "5.2.1.8",
        "Rule": "Guest_Mobile_Internet Access",
        "SourceUser": null,
        "DestinationUser": null,
        "Application": "web-browsing",
        "VirtualLocation": "vsys1",
        "FromZone": "DTT",
        "ToZone": "Untrust",
        "InboundInterface": "ethernet1/1.111",
        "OutboundInterface": "ethernet1/1",
        "LogSetting": "Panorama_CDL",
        "SessionID": 6111111,
        "RepeatCount": 1,
        "SourcePort": 42222,
        "DestinationPort": 80,
        "NATSourcePort": 22408,
        "NATDestinationPort": 80,
        "Protocol": "tcp",
        "Action": "alert",
        "FileName": "test_file.bin",
        "URLCategory": "business-and-economy",
        "VendorSeverity": "Low",
        "DirectionOfAttack": "server to client",
        "SequenceNo": 73503956876,
        "SourceLocation": "1.2.0.0-1.2.255.255",
        "DestinationLocation": "US",
        "PacketID": 0,
        "FileHash": null,
        "ReportID": 0,
        "DGHierarchyLevel1": 999,
        "DGHierarchyLevel2": 1111,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "DN-TEST-F2",
        "SourceUUID": null,
        "DestinationUUID": null,
        "IMSI": 0,
        "IMEI": null,
        "ParentSessionID": 0,
        "ParentStartTime": "1970-01-01T00:00:00.000000Z",
        "Tunnel": "N/A",
        "ContentVersion": "581116536",
        "SigFlags": 0,
        "RuleUUID": "6935060f-6443-4257-91f8",
        "HTTP2Connection": 0,
        "DynamicUserGroup": null,
        "X-Forwarded-ForIP": null,
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": "1.0.0",
        "SourceDeviceHost": "Test-device",
        "SourceDeviceMac": "11.22.33.44.55.66",
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "ContainerID": null,
        "ContainerNameSpace": null,
        "ContainerName": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "HostID": null,
        "EndpointSerialNumber": null,
        "DomainEDL": null,
        "SourceDynamicAddressGroup": null,
        "DestinationDynamicAddressGroup": null,
        "PartialHash": 0,
        "TimeGeneratedHighResolution": "2024-07-08T15:30:04.855000Z",
        "ReasonForDataFilteringAction": null,
        "Justification": null,
        "NSSAINetworkSliceType": null
    }
    ```



=== "test_new_globalprotect"


    ```json
	{
        "TimeReceived": "2024-07-08T09:01:14.000000Z",
        "DeviceSN": "00795700000000",
        "LogType": "GLOBALPROTECT",
        "Subtype": "globalprotect",
        "LogSubtype": "globalprotect",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-07-08T09:01:14.000000Z",
        "VirtualSystem": "vsys1",
        "EventIDValue": "gateway-logout",
        "Stage": "logout",
        "AuthMethod": null,
        "TunnelType": null,
        "SourceUserName": "joe.doe@test.com",
        "SourceRegion": "1.0.0.0-1.255.255.255",
        "EndpointDeviceName": "LNL-test",
        "PublicIPv4": "1.5.7.3",
        "PublicIPv6": "",
        "PrivateIPv4": "1.2.3.4",
        "PrivateIPv6": "",
        "HostID": "e4f14dfd-bd3c-40e5-9c4e",
        "EndpointSN": "5CD4153333",
        "GlobalProtectClientVersion": "0.0.-1",
        "EndpointOSType": "Windows",
        "EndpointOSVersion": "Microsoft Windows 11 Enterprise , 64-bit",
        "RepeatCount": 1,
        "CountOfRepeats": 1,
        "QuarantineReason": null,
        "ConnectionError": null,
        "Description": "client logout",
        "EventStatus": "success",
        "GlobalProtectGatewayLocation": null,
        "LoginDuration": 3625,
        "ConnectionMethod": null,
        "ConnectionErrorID": 0,
        "Portal": "Internal_test",
        "SequenceNo": 7359635570821640000,
        "TimeGeneratedHighResolution": "2024-07-08T09:01:14.449000Z",
        "GatewaySelectionType": "",
        "SSLResponseTime": -1,
        "GatewayPriority": null,
        "AttemptedGateways": null,
        "Gateway": null,
        "DGHierarchyLevel1": 556,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "DG-test",
        "VirtualSystemID": 1
    }
    ```



=== "test_new_threat_type"


    ```json
	{
        "TimeReceived": "2024-07-08T08:55:38.000000Z",
        "DeviceSN": "007954000370000",
        "LogType": "THREAT",
        "Subtype": "vulnerability",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-07-08T15:52:09.000000Z",
        "SourceAddress": "1.2.1.3",
        "DestinationAddress": "2.2.1.4",
        "NATSource": "",
        "NATDestination": "",
        "Rule": "Public_TTT_Mgmt",
        "SourceUser": null,
        "DestinationUser": null,
        "Application": "ssh",
        "VirtualLocation": "vsys1",
        "FromZone": "Trust",
        "ToZone": "TTT",
        "InboundInterface": "ethernet1/8",
        "OutboundInterface": "ethernet1/4.124",
        "LogSetting": "test_setting",
        "SessionID": 72837,
        "RepeatCount": 1,
        "SourcePort": 52000,
        "DestinationPort": 21,
        "NATSourcePort": 0,
        "NATDestinationPort": 0,
        "Protocol": "tcp",
        "Action": "reset-both",
        "FileName": null,
        "ThreatID": "SSH User Authentication Brute Force Attempt(40015)",
        "VendorSeverity": "High",
        "DirectionOfAttack": "client to server",
        "SequenceNo": 7350395687601,
        "SourceLocation": "1.0.0.0-1.255.255.255",
        "DestinationLocation": "ID",
        "PacketID": 12103464791027,
        "FileHash": null,
        "ApplianceOrCloud": null,
        "URLCounter": 0,
        "FileType": null,
        "SenderEmail": null,
        "EmailSubject": null,
        "RecipientEmail": null,
        "ReportID": 0,
        "DGHierarchyLevel1": 997,
        "DGHierarchyLevel2": 1169,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "DN-TEST",
        "SourceUUID": null,
        "DestinationUUID": null,
        "IMSI": 0,
        "IMEI": null,
        "ParentSessionID": 0,
        "ParentStarttime": "1970-01-01T00:00:00.000000Z",
        "Tunnel": "N/A",
        "ThreatCategory": "brute-force",
        "ContentVersion": "581116536",
        "SigFlags": "0x0",
        "RuleUUID": "496a138d-6515-4043-b7c7",
        "HTTP2Connection": 0,
        "DynamicUserGroupName": null,
        "X-Forwarded-ForIP": null,
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "ContainerID": null,
        "ContainerNameSpace": null,
        "ContainerName": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "HostID": null,
        "EndpointSerialNumber": null,
        "DomainEDL": null,
        "SourceDynamicAddressGroup": null,
        "DestinationDynamicAddressGroup": null,
        "PartialHash": 0,
        "TimeGeneratedHighResolution": "2024-07-08T15:52:09.934000Z",
        "NSSAINetworkSliceType": null
    }
    ```



=== "test_new_url_type"


    ```json
	{
        "TimeReceived": "2024-07-08T06:17:04.000000Z",
        "DeviceSN": "00795400037XXXX",
        "LogType": "THREAT",
        "Subtype": "url",
        "ConfigVersion": "10.2",
        "TimeGenerated": "2024-07-08T13:13:27.000000Z",
        "SourceAddress": "19.16.1.6",
        "DestinationAddress": "17.25.11.9",
        "NATSource": "210.210.140.61",
        "NATDestination": "17.25.11.9",
        "Rule": "Guest_Mobile_Internet Access",
        "SourceUser": null,
        "DestinationUser": null,
        "Application": "ssl",
        "VirtualLocation": "vsys1",
        "FromZone": "TTT",
        "ToZone": "Untrust",
        "InboundInterface": "ethernet1/6.997",
        "OutboundInterface": "ethernet1/1",
        "LogSetting": "Test_setting",
        "SessionID": 816808,
        "RepeatCount": 1,
        "SourcePort": 35000,
        "DestinationPort": 443,
        "NATSourcePort": 28500,
        "NATDestinationPort": 443,
        "Protocol": "tcp",
        "Action": "alert",
        "URL": "test.gstatic.com/",
        "URLCategory": "computer-and-internet-info",
        "VendorSeverity": "Informational",
        "DirectionOfAttack": "client to server",
        "SequenceNo": 73503956876009,
        "SourceLocation": "19.18.0.0-19.18.255.255",
        "DestinationLocation": "US",
        "ContentType": null,
        "PacketID": 0,
        "URLCounter": 0,
        "UserAgent": null,
        "X-Forwarded-For": null,
        "Referer": null,
        "DGHierarchyLevel1": 997,
        "DGHierarchyLevel2": 1169,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "DN-TEST",
        "SourceUUID": null,
        "DestinationUUID": null,
        "HTTPMethod": "unknown",
        "IMSI": 0,
        "IMEI": null,
        "ParentSessionID": 0,
        "ParentStarttime": "1970-01-01T00:00:00.000000Z",
        "Tunnel": "N/A",
        "InlineMLVerdict": "unknown",
        "ContentVersion": "0",
        "SigFlags": 0,
        "HTTPHeaders": null,
        "URLCategoryList": "computer-and-internet-info,low-risk",
        "RuleUUID": "6935060f-6443-4257",
        "HTTP2Connection": 0,
        "DynamicUserGroupName": null,
        "X-Forwarded-ForIP": null,
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "ContainerID": null,
        "ContainerNameSpace": null,
        "ContainerName": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "HostID": null,
        "EndpointSerialNumber": null,
        "SourceDynamicAddressGroup": null,
        "DestinationDynamicAddressGroup": null,
        "TimeGeneratedHighResolution": "2024-07-08T13:13:27.233000Z",
        "NSSAINetworkSliceType": null
    }
    ```



=== "test_ntp_sync_json"


    ```json
	{
        "LogTime": "2023-02-16T15:46:40.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "ntpd",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:46:33.000000Z",
        "VirtualLocation": null,
        "EventName": "sync",
        "EventComponent": "",
        "VendorSeverity": "Informational",
        "EventDescription": "NTP sync to server de.pool.ntp.org",
        "SequenceNo": 7200776623254143145,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:46:33.917000Z"
    }
    ```



=== "test_port_up_json"


    ```json
	{
        "LogTime": "2023-02-16T15:31:51.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "port",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:31:50.000000Z",
        "VirtualLocation": null,
        "EventName": "link-change",
        "EventComponent": "ethernet1/2",
        "VendorSeverity": "Informational",
        "EventDescription": "Port ethernet1/2: Up   10Gb/s-full duplex",
        "SequenceNo": 7200776623254143073,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:31:50.851000Z"
    }
    ```



=== "test_registration_succeed_json"


    ```json
	{
        "LogTime": "2023-02-16T15:31:51.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "fb",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:31:51.000000Z",
        "VirtualLocation": null,
        "EventName": "wildfire-conn-success",
        "EventComponent": "",
        "VendorSeverity": "Medium",
        "EventDescription": "Successfully registered to Public Cloud wildfire.paloaltonetworks.com",
        "SequenceNo": 7200776623254143102,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:31:51.387000Z"
    }
    ```



=== "test_system"


    ```json
	1,2024/01/12 22:47:26,016201000000,SYSTEM,vpn,2222,2024/01/12 22:47:27,,test-event,,0,0,general,informational,"unknown test peer",55555555555555555,0x0,0,0,0,0,,test-1,0,0,2024-01-12T22:47:27.652+11:00
    ```



=== "test_system_event_10_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "Successfully connect to address: 5.6.7.8 port: 3978, conn id: triallr-5.6.7.8-2-def",
        "EventName": "general",
        "EventTime": "2023-02-03T16:31:56.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:32:07.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170508,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:31:56.151000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_11_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": "",
        "EventDescription": "PAN-DB was upgraded to version 20230203.20250.",
        "EventName": "upgrade-url-database-success",
        "EventTime": "2023-02-03T16:37:22.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:37:31.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170511,
        "Subtype": "url-filtering",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:37:22.476000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": null,
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_12_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": "",
        "EventDescription": "DHCP RENEW: interface eth0, ip 1.2.3.4 netmask 255.255.255.0 dhcp server: 1.2.3.1",
        "EventName": "if-renew-trigger",
        "EventTime": "2023-02-03T16:39:46.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:39:55.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170512,
        "Subtype": "dhcp",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:39:46.612000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": null,
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_13"


    ```json
	1,2024/11/26 22:10:01,02410100000000,SYSTEM,auth,2555,2024/11/26 22:10:01,,auth-success,FWPA,0,0,general,informational,"When authenticating user 'test000555' from '1.2.5.5', a less secure authentication method PAP is used. Please migrate to PEAP or EAP-TTLS. Authentication Profile 'FWPA', vsys 'shared', Server Profile 'RADIUS_RSA', Server Address '1.7.4.2'",738970652229900000000,0x0,0,0,0,0,,FWPAN00,0,0,2024-11-26T22:10:01.627+01:00
    ```



=== "test_system_event_14"


    ```json
	1,2024/12/16 20:19:04,016301013072,SYSTEM,auth,2561,2024/12/16 20:19:04,,auth-fail,ESA-AUTH,0,0,general,medium,"failed authentication for user john.doe. Reason: Authentication request is timed out. auth profile ESA-AUTH, vsys vsys1, server profile ESA, server address 1.2.3.4, auth protocol PAP, From: 5.6.7.8.",7439393285273531690,0x0,0,0,0,0,,FWPADC1,0,0,2024-12-16T20:19:04.851+01:00
    ```



=== "test_system_event_15"


    ```json
	1,2025/01/21 11:57:22,016301013072,SYSTEM,auth,2561,2025/01/21 11:57:23,,auth-fail,ESA-AUTH,0,0,general,medium,"failed authentication for user 'john.doe'. Reason: Authentication request is timed out. auth profile 'ESA-AUTH', vsys 'vsys1', server profile 'ESA', server address '1.2.3.4', auth protocol 'PAP', From: 5.6.7.8.",7439393285299734188,0x0,0,0,0,0,,FWPADC1,0,0,2025-01-21T11:57:23.294+01:00
    ```



=== "test_system_event_1_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "Installed WildFire package: panupv3-all-wildfire-739610-742990.tgz",
        "EventName": "general",
        "EventTime": "2023-02-03T16:30:44.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:30:52.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170505,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:30:44.868000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_2_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "WildFire update job succeeded  for user Auto update agent",
        "EventName": "general",
        "EventTime": "2023-02-03T16:45:56.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:46:05.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170521,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:45:56.725000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_3_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "Connection to Update server:  completed successfully, initiated by 1.2.3.4",
        "EventName": "general",
        "EventTime": "2023-02-03T16:45:51.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:45:56.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170515,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:45:51.118000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_4_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "WildFire job started processing. Dequeue time=2023/02/03 17:45:52. Job Id=72.   ",
        "EventName": "general",
        "EventTime": "2023-02-03T16:45:52.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:45:56.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170518,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:45:52.888000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_5_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "WildFire package upgraded from version 739610-742990 to 739613-742993 by Auto update agent",
        "EventName": "general",
        "EventTime": "2023-02-03T16:45:55.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:45:56.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170520,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:45:55.982000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_6_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "WildFire job enqueued. Enqueue time=2023/02/03 17:45:52. JobId=72.  . Type: Full",
        "EventName": "general",
        "EventTime": "2023-02-03T16:45:52.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:45:56.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170517,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:45:52.887000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_7_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "Connection to Update server: updates.paloaltonetworks.com completed successfully, initiated by 1.2.3.4",
        "EventName": "general",
        "EventTime": "2023-02-03T16:45:49.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:45:56.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170514,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:45:49.557000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_8_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "Installed WildFire package: panupv3-all-wildfire-739613-742993.tgz",
        "EventName": "general",
        "EventTime": "2023-02-03T16:45:54.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:45:56.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170519,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:45:54.757000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_system_event_9_json"


    ```json
	{
        "ConfigVersion": "10.1",
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DeviceGroup": null,
        "EventComponent": null,
        "EventDescription": "WildFire version 739613-742993 downloaded by Auto update agent",
        "EventName": "general",
        "EventTime": "2023-02-03T16:45:52.000000Z",
        "LogSourceID": "007954000351998",
        "LogSourceName": "PA-VM",
        "LogTime": "2023-02-03T16:45:56.000000Z",
        "LogType": "SYSTEM",
        "SequenceNo": 7195838274152170516,
        "Subtype": "general",
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-03T16:45:52.887000Z",
        "VendorSeverity": "Informational",
        "VirtualLocation": "",
        "VirtualSystemName": null
    }
    ```



=== "test_threat"


    ```json
	1,2024/01/12 11:21:15,016201000000,THREAT,url,2562,2024/01/12 11:21:15,1.2.3.4,5.6.7.8,9.10.11.12,0.0.0.0,SAAS vers log,,,ssl,vsys1,Outside,test-Externe,a11.30,a11.25,Panorama,2024/01/12 11:21:15,200000,1,58444,2222,58444,2222,0x50b444,tcp,alert,"test.fr:9999/",(9999),test,informational,client-to-server,55555555555555555555,0x8000000000000000,US,France,,,0,,,0,,,,,,,,0,0,0,0,0,,TEST-01,,,,,0,,0,,N/A,N/A,AppThreat-0-0,0x0,0,4294967295,,"test,low-risk",96eeeef8-bd9c-4145,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,0,2024-01-12T11:21:15.190+01:00,,,,encrypted-tunnel,networking,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,ssl,no,no,
    ```



=== "test_threat_02"


    ```json
	1,2024/08/12 15:57:12,012345678910,THREAT,vulnerability,2561,2024/08/12 15:57:04,1.2.3.4,5.6.7.8,1.2.3.4,5.6.7.8,Access_Portal-GW_GP,,,web-browsing,vsys1,INTERNET,INTERNET,ethernet1/3.302,ethernet1/3.302,default,2024/08/12 15:57:04,113535,1,56731,443,56731,20077,0x81402000,tcp,reset-both,"login.esp",Palo Alto Networks GlobalProtect OS Command Injection Vulnerability(95187),business-and-economy,critical,client-to-server,7334683348721844974,0x8000000000000000,United States,France,,,1210223766892439373,,,1,,,,,,,,0,320,90,0,0,,site1-FW01,,,,,0,,0,,N/A,code-execution,AppThreat-8879-8900,0x0,0,4294967295,,,abcdefgh-1234-5678-abcd-01234567890,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,0,2024-08-12T15:57:04.614+02:00,,,,internet-utility,general-internet,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,web-browsing,no,no,
    ```



=== "test_timestamp_palo"


    ```json
	: 1,2023/08/01 04:03:24,026701002348,SYSTEM,general,2816,2023/08/01 04:03:24,,general,,0,0,general,informational,"Request made to server ""server_test.com"" is successful . ",7261972653022396272,0x8000000000000000,0,0,0,0,,test-01,0,0,2023-08-01T04:03:24.705+02:00
    ```



=== "test_traffic_event_1_json"


    ```json
	{
        "Action": "allow",
        "ActionSource": "from-policy",
        "Application": "incomplete",
        "Bytes": 74,
        "BytesReceived": 0,
        "BytesSent": 74,
        "ChunksReceived": 0,
        "ChunksSent": 0,
        "ChunksTotal": 0,
        "ConfigVersion": "10.1",
        "ContainerID": null,
        "ContainerName": null,
        "ContainerNameSpace": null,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DestinationAddress": "5.6.7.8",
        "DestinationDeviceCategory": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceVendor": null,
        "DestinationDynamicAddressGroup": null,
        "DestinationEDL": null,
        "DestinationLocation": "US",
        "DestinationPort": 443,
        "DestinationUUID": null,
        "DestinationUser": null,
        "DeviceName": "PA-VM",
        "DeviceSN": "007954000351998",
        "DynamicUserGroupName": null,
        "EndpointAssociationID": 0,
        "EndpointSerialNumber": null,
        "FromZone": "untrusted",
        "GPHostID": null,
        "HASessionOwner": null,
        "HTTP2Connection": 0,
        "IMEI": null,
        "IMSI": 0,
        "InboundInterface": "ethernet1/1",
        "LinkChangeCount": 0,
        "LinkSwitches": null,
        "LogSetting": "default",
        "LogType": "TRAFFIC",
        "NATDestination": "",
        "NATDestinationPort": 0,
        "NATSource": "",
        "NATSourcePort": 0,
        "NSSAINetworkSliceDifferentiator": null,
        "NSSAINetworkSliceType": null,
        "OutboundInterface": "ethernet1/1",
        "PacketsReceived": 0,
        "PacketsSent": 1,
        "PacketsTotal": 1,
        "ParentSessionID": 0,
        "ParentStarttime": "1970-01-01T00:00:00.000000Z",
        "Protocol": "tcp",
        "RepeatCount": 1,
        "Rule": "intrazone-default",
        "RuleUUID": "f903db52-4b89-4610-b908-67be412704f0",
        "SDWANCluster": null,
        "SDWANClusterType": null,
        "SDWANDeviceType": null,
        "SDWANPolicyName": null,
        "SDWANSite": null,
        "SequenceNo": 7195838274152187101,
        "SessionDuration": 0,
        "SessionEndReason": "aged-out",
        "SessionID": 17635,
        "SessionStartTime": "2023-02-03T16:46:00.000000Z",
        "SourceAddress": "1.2.3.4",
        "SourceDeviceCategory": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "SourceDeviceModel": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceProfile": null,
        "SourceDeviceVendor": null,
        "SourceDynamicAddressGroup": null,
        "SourceEDL": null,
        "SourceLocation": "1.2.0.0-1.2.255.255",
        "SourcePort": 59087,
        "SourceUUID": null,
        "SourceUser": null,
        "Subtype": "end",
        "TimeGenerated": "2023-02-03T16:46:07.000000Z",
        "TimeGeneratedHighResolution": "2023-02-03T16:46:07.584000Z",
        "TimeReceived": "2023-02-03T16:46:14.000000Z",
        "ToZone": "untrusted",
        "Tunnel": "N/A",
        "URLCategory": "any",
        "VirtualLocation": "vsys1",
        "VirtualSystemName": "",
        "X-Forwarded-ForIP": null
    }
    ```



=== "test_traffic_event_2_json"


    ```json
	{
        "Action": "allow",
        "ActionSource": "from-policy",
        "Application": "incomplete",
        "Bytes": 74,
        "BytesReceived": 0,
        "BytesSent": 74,
        "ChunksReceived": 0,
        "ChunksSent": 0,
        "ChunksTotal": 0,
        "ConfigVersion": "10.1",
        "ContainerID": null,
        "ContainerName": null,
        "ContainerNameSpace": null,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "DestinationAddress": "5.6.7.8",
        "DestinationDeviceCategory": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceVendor": null,
        "DestinationDynamicAddressGroup": null,
        "DestinationEDL": null,
        "DestinationLocation": "US",
        "DestinationPort": 443,
        "DestinationUUID": null,
        "DestinationUser": null,
        "DeviceName": "PA-VM",
        "DeviceSN": "007954000351998",
        "DynamicUserGroupName": null,
        "EndpointAssociationID": 0,
        "EndpointSerialNumber": null,
        "FromZone": "untrusted",
        "GPHostID": null,
        "HASessionOwner": null,
        "HTTP2Connection": 0,
        "IMEI": null,
        "IMSI": 0,
        "InboundInterface": "ethernet1/1",
        "LinkChangeCount": 0,
        "LinkSwitches": null,
        "LogSetting": "default",
        "LogType": "TRAFFIC",
        "NATDestination": "",
        "NATDestinationPort": 0,
        "NATSource": "",
        "NATSourcePort": 0,
        "NSSAINetworkSliceDifferentiator": null,
        "NSSAINetworkSliceType": null,
        "OutboundInterface": "ethernet1/1",
        "PacketsReceived": 0,
        "PacketsSent": 1,
        "PacketsTotal": 1,
        "ParentSessionID": 0,
        "ParentStarttime": "1970-01-01T00:00:00.000000Z",
        "Protocol": "tcp",
        "RepeatCount": 1,
        "Rule": "intrazone-default",
        "RuleUUID": "f903db52-4b89-4610-b908-67be412704f0",
        "SDWANCluster": null,
        "SDWANClusterType": null,
        "SDWANDeviceType": null,
        "SDWANPolicyName": null,
        "SDWANSite": null,
        "SequenceNo": 7195838274152187100,
        "SessionDuration": 0,
        "SessionEndReason": "aged-out",
        "SessionID": 17634,
        "SessionStartTime": "2023-02-03T16:45:44.000000Z",
        "SourceAddress": "1.2.3.4",
        "SourceDeviceCategory": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "SourceDeviceModel": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceProfile": null,
        "SourceDeviceVendor": null,
        "SourceDynamicAddressGroup": null,
        "SourceEDL": null,
        "SourceLocation": "1.2.0.0-1.2.255.255",
        "SourcePort": 59087,
        "SourceUUID": null,
        "SourceUser": null,
        "Subtype": "end",
        "TimeGenerated": "2023-02-03T16:45:52.000000Z",
        "TimeGeneratedHighResolution": "2023-02-03T16:45:52.582000Z",
        "TimeReceived": "2023-02-03T16:45:56.000000Z",
        "ToZone": "untrusted",
        "Tunnel": "N/A",
        "URLCategory": "any",
        "VirtualLocation": "vsys1",
        "VirtualSystemName": "",
        "X-Forwarded-ForIP": null
    }
    ```



=== "test_traffic_event_3_json"


    ```json
	{
        "TimeReceived": "2025-01-28T17:00:36.000000Z",
        "DeviceSN": "007057000103158",
        "LogType": "TRAFFIC",
        "Subtype": "start",
        "ConfigVersion": "11.1",
        "TimeGenerated": "2025-01-28T17:01:01.000000Z",
        "SourceAddress": "1.2.3.4",
        "DestinationAddress": "5.6.7.8",
        "NATSource": "",
        "NATDestination": "",
        "Rule": "intrazone-default",
        "SourceUser": null,
        "DestinationUser": null,
        "Application": "paloalto-updates",
        "FromZone": "OUTSIDE",
        "ToZone": "OUTSIDE",
        "InboundInterface": "ethernet1/1",
        "OutboundInterface": "ethernet1/1",
        "LogSetting": "Panorama_CDL",
        "SessionID": 117195,
        "RepeatCount": 1,
        "SourcePort": 45483,
        "DestinationPort": 443,
        "NATSourcePort": 0,
        "NATDestinationPort": 0,
        "Protocol": "tcp",
        "Action": "allow",
        "Bytes": 797,
        "BytesSent": 723,
        "BytesReceived": 74,
        "PacketsTotal": 4,
        "SessionStartTime": "2025-01-28T17:01:02.000000Z",
        "SessionDuration": 0,
        "URLCategory": "computer-and-internet-info",
        "SourceLocation": "TEST_INFRA",
        "DestinationLocation": "US",
        "PacketsSent": 3,
        "PacketsReceived": 1,
        "SessionEndReason": "n-a",
        "DeviceName": "PC-01",
        "ActionSource": "from-policy",
        "RuleUUID": "6c2be47e-4724-4212-9902-26ba054fe2a9",
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "TimeGeneratedHighResolution": "2025-01-28T17:01:02.738000Z",
        "DestinationUserName": null,
        "SourceUserDomain": null,
        "Users": "1.2.3.4",
        "IsPacketCapture": false,
        "IsPhishing": false
    }
    ```



=== "test_update_content_json"


    ```json
	{
        "LogTime": "2023-02-16T15:50:25.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "general",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:50:14.000000Z",
        "VirtualLocation": "",
        "EventName": "general",
        "EventComponent": null,
        "VendorSeverity": "Informational",
        "EventDescription": "Content update job succeeded  for user admin",
        "SequenceNo": 7200776623254143155,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:50:14.343000Z"
    }
    ```



=== "test_upgrade_package_json"


    ```json
	{
        "LogTime": "2023-02-16T15:49:49.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "general",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:49:34.000000Z",
        "VirtualLocation": "",
        "EventName": "general",
        "EventComponent": null,
        "VendorSeverity": "Informational",
        "EventDescription": "Content package upgraded from version 8671-7826 to 8676-7858 by admin",
        "SequenceNo": 7200776623254143153,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:49:34.604000Z"
    }
    ```



=== "test_user_authentication_json"


    ```json
	{
        "LogTime": "2023-02-16T15:41:25.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "auth",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:41:18.000000Z",
        "VirtualLocation": null,
        "EventName": "auth-success",
        "EventComponent": "",
        "VendorSeverity": "Informational",
        "EventDescription": "authenticated for user 'admin'.   From: 1.2.3.4.",
        "SequenceNo": 7200776623254143115,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:41:18.813000Z"
    }
    ```



=== "test_userid"


    ```json
	1,2024/01/12 11:23:33,01545100000000,USERID,login,2222,2024/01/12 11:23:33,vsys1,1.2.3.4,test.fr\JDOE,,0,1,10888,0,0,vpn-client,globalprotect,555555555555555555555555,0x8000000000000000,0,0,0,0,,test-01,1,,2024/01/12 11:23:33,1,0x80000000,dtest,,2024-01-12T11:23:33.907+01:00
    ```



=== "test_web_authentication_json"


    ```json
	{
        "LogTime": "2023-02-16T15:41:25.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "general",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T15:41:18.000000Z",
        "VirtualLocation": "",
        "EventName": "general",
        "EventComponent": null,
        "VendorSeverity": "Informational",
        "EventDescription": "User admin logged in via Web from 1.2.3.4 using https",
        "SequenceNo": 7200776623254143116,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T15:41:18.825000Z"
    }
    ```



=== "test_wildfire_failure_json"


    ```json
	{
        "LogTime": "2023-02-16T17:45:55.000000Z",
        "LogSourceID": "007954000351998",
        "LogType": "SYSTEM",
        "Subtype": "fb",
        "ConfigVersion": "10.1",
        "EventTime": "2023-02-16T17:45:43.000000Z",
        "VirtualLocation": null,
        "EventName": "wildfire-conn-failed",
        "EventComponent": "",
        "VendorSeverity": "Informational",
        "EventDescription": "Failed to perform task resulting in connection timeout with WildFire Cloud wildfire.paloaltonetworks.com",
        "SequenceNo": 7200776623254143341,
        "DGHierarchyLevel1": 0,
        "DGHierarchyLevel2": 0,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": null,
        "LogSourceName": "PA-VM",
        "DeviceGroup": null,
        "Template": null,
        "TimeGeneratedHighResolution": "2023-02-16T17:45:43.111000Z"
    }
    ```



=== "threat-url-xff"


    ```json
	1,2024/03/12 15:02:32,016401004874,THREAT,url,2816,2024/03/12 15:02:32,10.0.0.2,192.168.0.1,0.0.0.0,0.0.0.0,rule-internet,x-fwd-for: 11.22.33.44,,web-browsing,vsys,env,zone2,a1.1,aec.2,default,2024/03/12 15:02:32,1384927,1,49802,80,0,0,0x8b000,tcp,alert,"www.sekoia.io:443/catalog/integrations?query=this",(9999),any,informational,client-to-server,7324220311048193508,0x0,10.0.0.0-10.255.255.255,192.168.0.0-192.168.255.255,,,0,,,10,Mozilla/4.0 (compatible; ms-office; MSOffice 16),,"11.22.33.44",,,,,0,0,0,0,0,VSYS,FW,,,,get,0,,0,,N/A,N/A,AppThreat-0-0,0x0,0,4294967295,,"Sekoia,cybertech,low-risk",ea3431a2-6869-4d9f-ad41-1858d80b406c,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,0,2024-03-12T15:02:32.650+01:00,,,,internet-utility,general-internet,browser-based,4,"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use",,web-browsing,no,no,,,NonProxyTraffic
    ```



=== "threat_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|THREAT|spyware|1|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 20:48:21 deviceExternalId=xxxxxxxxxxxxx start=Mar 01 2021 20:48:16 PanOSApplicationCategory=general-internet PanOSApplicationContainer=sina-weibo PanOSApplicationRisk=4 PanOSApplicationSubcategory=social-networking PanOSApplicationTechnology=browser-based PanOSCaptivePortal=false PanOSCloudHostname=xxxxx PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceOS= dntdom=paloaltonetwork duser=xxxxx duid= PanOSHTTPMethod=get PanOSInboundInterfaceDetailsPort=0 PanOSInboundInterfaceDetailsSlot=0 PanOSInboundInterfaceDetailsType=unknown PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer=true PanOSIsContainer=false PanOSIsDecryptMirror=false PanOSIsDecrypted=false PanOSIsDuplicateLog=false PanOSIsEncrypted=false PanOSIsIPV6=false PanOSIsMptcpOn=false PanOSIsNonStandardDestinationPort=false PanOSIsPacketCapture=false PanOSIsPhishing=false PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy=false PanOSIsReconExcluded=false PanOSIsSaaSApplication=false PanOSIsServertoClient=false PanOSIsSourceXForwarded=true PanOSIsSystemReturn=true PanOSIsTransaction=false PanOSIsTunnelInspected=false PanOSIsURLDenied=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT=false PanOSNonStandardDestinationPort=13884 PanOSOutboundInterfaceDetailsPort=0 PanOSOutboundInterfaceDetailsSlot=0 PanOSOutboundInterfaceDetailsType=unknown PanOSOutboundInterfaceDetailsUnit=0 PanOSPacket= PanOSPayloadProtocolID=-1 PanOSSanctionedStateOfApp=false PanOSSeverity=Informational PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom=paloaltonetwork suser=xxxxx suid= cat=27379 PanOSThreatNameFirewall=27379 PanOSTunneledApplication=tunneled-app PanOSURLDomain= PanOSUsers=paloaltonetwork\\xxxxx PanOSVerdict= PanOSVirtualSystemID=1 c6a2=fe80:110:8897:efab:9202:b3ff:fe1e:8329 c6a2Label=Source IPv6 Address c6a3=fe80:110:8897:efab:9202:b3ff:fe1e:8329 c6a3Label=Destination IPv6 Address sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=deny-attackers cs1Label=Rule suser0=paloaltonetwork\\xxxxx duser0=paloaltonetwork\\xxxxx app=sina-weibo-base cs3=vsys1 cs3Label=VirtualLocation cs4=datacenter cs4Label=FromZone cs5=ethernet4Zone-test4 cs5Label=ToZone deviceInboundInterface=unknown deviceOutboundInterface=unknown cs6=rs-logging cs6Label=LogSetting cn1=947181 cn1Label=SessionID cnt=1 spt=13884 dpt=4228 sourceTranslatedPort=30116 destinationTranslatedPort=20966 proto=tcp act=drop-all request=some other fake filename PanOSThreatID=27379(27379) flexString2=server to client flexString2Label=DirectionOfAttack externalId=xxxxxxxxxxxxx PanOSSourceLocation=LY PanOSDestinationLocation=BR fileId=0 PanOSFileHash= PanOSApplianceOrCloud= PanOSURLCounter=0 PanOSFileType= PanOSSenderEmail= PanOSEmailSubject= PanOSRecipientEmail= PanOSReportID=0 PanOSDGHierarchyLevel1=11 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=xxxxx PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStarttime=Jan 01 1970 00:00:00 PanOSTunnel=N/A PanOSThreatCategory=unknown PanOSContentVersion=50059 PanOSSigFlags=0x0 PanOSRuleUUID=017e4d76-2003-47f4-8afc-1d35c808c615 PanOSHTTP2Connection=0 PanOSDynamicUserGroupName= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory=X-Phone PanOSSourceDeviceProfile=x-profile PanOSSourceDeviceModel=Note 4G PanOSSourceDeviceVendor=Lenovo PanOSSourceDeviceOSFamily=K6 PanOSSourceDeviceOSVersion=Android v9 PanOSSourceDeviceHost=pan-505 PanOSSourceDeviceMac=596703749274 PanOSDestinationDeviceCategory=X-Phone PanOSDestinationDeviceProfile=x-profile PanOSDestinationDeviceModel=MI PanOSDestinationDeviceVendor=Xiaomi PanOSDestinationDeviceOSFamily=A1 PanOSDestinationDeviceOSVersion=Android v9.1 PanOSDestinationDeviceHost=pan-622 PanOSDestinationDeviceMac=620797415366 PanOSContainerID=1873cc5c-0d31 PanOSContainerNameSpace=pns_default PanOSSourceEDL= PanOSDestinationEDL= PanOSHostID=xxxxxxxxxxxxxx PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSDomainEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSPartialHash=0 PanOSTimeGeneratedHighResolution=Mar 01 2021 20:48:16 PanOSNSSAINetworkSliceType=dc
    ```



=== "threat_csv"


    ```json
	1,2021/08/31 14:00:02,001701000000,THREAT,vulnerability,2049,2021/08/31 14:00:02,10.0.0.2,10.2.0.1,0.0.0.0,0.0.0.0,abcd,,,web-browsing,vsys,env,zone2,a1.1,aec.2,podl,2021/08/31 14:00:02,279429,2,12345,80,0,0,0x2000,tcp,alert,"EXAMPLE.PDF",PDF Exploit Evasion Found(34805),any,informational,server-to-client,1320000,0x2000000000000000,10.0.0.0-10.255.255.255,10.0.0.0-10.255.255.255,0,,0,,,1,,,,,,,,0,0,0,0,0,,FW,,,,,0,,0,,N/A,code-execution,AppThreat-0000-1111,0x0,0,422342342,
    ```



=== "traffic1_csv"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|TRAFFIC|end|3|dtz=UTC rt=Jul 31 2022 12:46:24 deviceExternalId=000000000000 PanOSConfigVersion=10.1 start=Jul 31 2022 12:46:07 src=1.2.3.4 dst=5.6.7.8 sourceTranslatedAddress=4.3.2.1 destinationTranslatedAddress=8.7.6.5 cs1=SO Access cs1Label=Rule suser= duser= app=outlook-web-online cs3=vsys1 cs3Label=VirtualLocation cs4=Trust cs4Label=FromZone cs5=Untrust cs5Label=ToZone deviceInboundInterface=ethernet1/10 deviceOutboundInterface=ethernet1/11 cs6=Panorama_LOF cs6Label=LogSetting cn1=595456 cn1Label=SessionID cnt=1 spt=52066 dpt=443 sourceTranslatedPort=47252 destinationTranslatedPort=443 proto=tcp act=allow PanOSBytes=12503 out=5651 in=6852 cn2=24 cn2Label=PacketsTotal PanOSSessionStartTime=Jul 31 2022 12:43:06 cn3=178 cn3Label=SessionDuration cs2=computer-and-internet-info cs2Label=URLCategory externalId=1111111111111111111 PanOSSourceLocation=10.0.0.0-10.255.255.255 PanOSDestinationLocation=UK PanOSPacketsSent=13 PanOSPacketsReceived=11 reason=tcp-fin PanOSDGHierarchyLevel1=997 PanOSDGHierarchyLevel2=738 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=LF-5698-NR cat=from-policy PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStarttime=Jan 01 1970 00:00:00 PanOSTunnel=N/A PanOSEndpointAssociationID=0 PanOSChunksTotal=0 PanOSChunksSent=0 PanOSChunksReceived=0 PanOSRuleUUID=2e259acc-c7ce-43d0-857f-f1a457e02699 PanOSHTTP2Connection=0 PanOSLinkChangeCount=0 PanOSSDWANPolicyName= PanOSLinkSwitches= PanOSSDWANCluster= PanOSSDWANDeviceType= PanOSSDWANClusterType= PanOSSDWANSite= PanOSDynamicUserGroupName= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceHost= PanOSSourceDeviceMac= PanOSDestinationDeviceCategory= PanOSDestinationDeviceProfile= PanOSDestinationDeviceModel= PanOSDestinationDeviceVendor= PanOSDestinationDeviceOSFamily= PanOSDestinationDeviceOSVersion= PanOSDestinationDeviceHost= PanOSDestinationDeviceMac= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSGPHostID= PanOSEndpointSerialNumber= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSHASessionOwner= PanOSTimeGeneratedHighResolution=Jul 31 2022 12:46:07 PanOSNSSAINetworkSliceType= PanOSNSSAINetworkSliceDifferentiator=

    ```



=== "traffic2_csv"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|TRAFFIC|end|3|dtz=UTC rt=Aug 02 2022 06:42:20 deviceExternalId=no-serial PanOSConfigVersion=10.0 start=Aug 02 2022 06:42:01 src= dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=Global_Outbound_internet_access cs1Label=Rule suser=user.name@corp.com duser= app=ssl cs3=vsys1 cs3Label=VirtualLocation cs4=trust cs4Label=FromZone cs5=untrust cs5Label=ToZone deviceInboundInterface=tunnel.1 deviceOutboundInterface=ethernet1/1 cs6=default cs6Label=LogSetting cn1=689028 cn1Label=SessionID cnt=1 spt=63516 dpt=443 sourceTranslatedPort=43823 destinationTranslatedPort=443 proto=tcp act=allow PanOSBytes=13443 out=2755 in=10688 cn2=32 cn2Label=PacketsTotal PanOSSessionStartTime=Aug 02 2022 06:41:44 cn3=0 cn3Label=SessionDuration cs2=low-risk cs2Label=URLCategory externalId=1112030318 PanOSSourceLocation=10.0.0.0-10.255.255.255 PanOSDestinationLocation=EU PanOSPacketsSent=13 PanOSPacketsReceived=19 reason=tcp-fin PanOSDGHierarchyLevel1=463 PanOSDGHierarchyLevel2=467 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=GP cloud service cat=from-policy PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStarttime=Jan 01 1970 00:00:00 PanOSTunnel=N/A PanOSEndpointAssociationID=0 PanOSChunksTotal=0 PanOSChunksSent=0 PanOSChunksReceived=0 PanOSRuleUUID=c38e111b-43fc-4de4-a17c-c372af557193 PanOSHTTP2Connection=0 PanOSLinkChangeCount=0 PanOSSDWANPolicyName= PanOSLinkSwitches= PanOSSDWANCluster= PanOSSDWANDeviceType= PanOSSDWANClusterType= PanOSSDWANSite= PanOSDynamicUserGroupName= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceHost= PanOSSourceDeviceMac= PanOSDestinationDeviceCategory= PanOSDestinationDeviceProfile= PanOSDestinationDeviceModel= PanOSDestinationDeviceVendor= PanOSDestinationDeviceOSFamily= PanOSDestinationDeviceOSVersion= PanOSDestinationDeviceHost= PanOSDestinationDeviceMac= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSGPHostID= PanOSEndpointSerialNumber= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSHASessionOwner= PanOSTimeGeneratedHighResolution=Aug 02 2022 06:42:02 PanOSNSSAINetworkSliceType= PanOSNSSAINetworkSliceDifferentiator=
    ```



=== "traffic_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|TRAFFIC|end|3|ProfileToken=xxxxx dtz=UTC rt=Feb 27 2021 20:16:21 deviceExternalId=xxxxxxxxxxxxx PanOSApplicationContainer= PanOSApplicationRisk=5 PanOSApplicationSubcategory=file-sharing PanOSApplicationTechnology=peer-to-peer PanOSCaptivePortal=false PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceOS= dntdom=paloaltonetwork duser=xxxxx duid= PanOSInboundInterfaceDetailsPort=0 PanOSInboundInterfaceDetailsSlot=0 PanOSInboundInterfaceDetailsType=unknown PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer=false PanOSIsContainer=false PanOSIsDecryptMirror=false PanOSIsDecrypted=false PanOSIsDecryptedLog=false PanOSIsDecryptedPayloadForward=false PanOSIsDuplicateLog=false PanOSIsEncrypted=false PanOSIsIPV6=false PanOSIsInspectionBeforeSession=true PanOSIsMptcpOn=false PanOSIsNonStandardDestinationPort=false PanOSIsPacketCapture=false PanOSIsPhishing=false PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy=false PanOSIsReconExcluded=false PanOSIsSaaSApplication=false PanOSIsServertoClient=false PanOSIsSourceXForwarded=false PanOSIsSystemReturn=false PanOSIsTransaction=false PanOSIsTunnelInspected=false PanOSIsURLDenied=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT=false PanOSNonStandardDestinationPort=0 PanOSOutboundInterfaceDetailsPort=0 PanOSOutboundInterfaceDetailsSlot=0 PanOSOutboundInterfaceDetailsType=unknown PanOSOutboundInterfaceDetailsUnit=0 PanOSSDWANFECRatio=0.0 PanOSSanctionedStateOfApp=false PanOSSessionOwnerMidx=false PanOSSessionTracker=16 PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom=xxxxx suser=xxxxx xxxxx suid= PanOSTunneledApplication=tunneled-app PanOSUsers=xxxxx\\xxxxx xxxxx PanOSVirtualSystemID=1 PanOSApplicationCategory=peer2peer PanOSConfigVersion=10.0 start=Feb 27 2021 20:16:17 src=1.1.1.1 dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=deny-attackers cs1Label=Rule suser0=xxxxx\\xxxxx xxxxx duser0=paloaltonetwork\\xxxxx app=fileguri cs3=vsys1 cs3Label=VirtualLocation cs4=untrust cs4Label=FromZone cs5=ethernet4Zone-test1 cs5Label=ToZone deviceInboundInterface=unknown deviceOutboundInterface=unknown cs6=rs-logging cs6Label=LogSetting cn1=25596 cn1Label=SessionID cnt=1 spt=22871 dpt=27092 sourceTranslatedPort=24429 destinationTranslatedPort=14744 proto=tcp act=deny PanOSBytes=1370294 out=400448 in=969846 cn2=314 cn2Label=PacketsTotal PanOSSessionStartTime=Feb 27 2021 20:15:48 cn3=56 cn3Label=SessionDuration cs2=custom-category cs2Label=URLCategory externalId=xxxxxxxxxxxxx PanOSSourceLocation=east-coast PanOSDestinationLocation=BR PanOSPacketsSent=194 PanOSPacketsReceived=120 reason=unknown PanOSDGHierarchyLevel1=11 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=xxxxx cat=unknown PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStarttime=Feb 27 2021 20:15:40 PanOSTunnel=GRE PanOSEndpointAssociationID=-3746994889972252628 PanOSChunksTotal=1945 PanOSChunksSent=323 PanOSChunksReceived=1622 PanOSRuleUUID=017e4d76-2003-47f4-8afc-1d35c808c615 PanOSHTTP2Connection=469139 PanOSLinkChangeCount=0 PanOSSDWANPolicyName= PanOSLinkSwitches= PanOSSDWANCluster= PanOSSDWANDeviceType= PanOSSDWANClusterType= PanOSSDWANSite= PanOSDynamicUserGroupName=dynug-4 PanOSX-Forwarded-ForIP=1.1.1.1 PanOSSourceDeviceCategory=N-Phone PanOSSourceDeviceProfile=n-profile PanOSSourceDeviceModel=Nexus PanOSSourceDeviceVendor=Google PanOSSourceDeviceOSFamily=LG-H790 PanOSSourceDeviceOSVersion=Android v6 PanOSSourceDeviceHost=pan-301 PanOSSourceDeviceMac=839147449905 PanOSDestinationDeviceCategory=N-Phone PanOSDestinationDeviceProfile=n-profile PanOSDestinationDeviceModel=Nexus PanOSDestinationDeviceVendor=Google PanOSDestinationDeviceOSFamily=H1511 PanOSDestinationDeviceOSVersion=Android v7 PanOSDestinationDeviceHost=pan-355 PanOSDestinationDeviceMac=530589561221 PanOSContainerID=1873cc5c-0d31 PanOSContainerNameSpace=pns_default PanOSContainerName=pan-dp-77754f4 PanOSSourceEDL= PanOSDestinationEDL= PanOSGPHostID=xxxxxxxxxxxxxx PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSSourceDynamicAddressGroup= aqua_dag PanOSDestinationDynamicAddressGroup= PanOSHASessionOwner=session_owner-4 PanOSTimeGeneratedHighResolution=Feb 27 2021 20:16:18 PanOSNSSAINetworkSliceType=0 PanOSNSSAINetworkSliceDifferentiator=1bca5
    ```



=== "traffic_with_resotimestamp"


    ```json
	1,2024/01/03 13:15:29,026701002040,TRAFFIC,end,2816,2024/01/03 13:15:29,1.2.3.4,5.6.7.8,0.0.0.0,0.0.0.0,MyRule,,,ssl,vsys1,Z_DMZ_PROXY,Z_INTERCO_WAN,ethernet1/22.301,ethernet1/3.104,Log Profile,2024/01/03 13:15:29,219781,1,60975,443,0,0,0x41c,tcp,allow,5773,758,5015,14,2024/01/03 13:15:14,0,not-resolved,,7312415129244589397,0x0,10.0.0.0-10.255.255.255,United States,,7,7,tcp-fin,0,0,0,0,,PA2314-CD,from-policy,,,0,,0,,N/A,0,0,0,0,0bbe5a53-f498-4cc2-a170-ced134f4824c,0,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2024-01-03T13:15:30.547+01:00,,,encrypted-tunnel,networking,browser-based,4,\"used-by-malware,able-to-transfer-file,has-known-vulnerability,tunnel-other-application,pervasive-use\",,ssl,no,no,0,NonProxyTraffic,
    ```



=== "udp_deny_csv"


    ```json
	<14>Sep 16 10:00:00 PA 1,9/16/19 10:00,1801017000,TRAFFIC,deny,2049,9/16/19 10:00,10.0.0.2,1.2.3.4,5.4.4.3,5.4.3.2,DENYALL,,,protection,vsys1,DNS,AAAAA,ae2.503,ethernet1/1,Secure,9/16/19 10:00,11111,1,130000,53,6379,53,0x400000,udp,reset-both,284,284,0,1,9/16/19 10:00,0,any,0,50660381851,0x0,10.0.0.0-10.255.255.255,Spain,0,1,0,policy-deny,0,0,0,0,,PA-1,from-application,,,0,,0,,N/A,0,0,0,0
    ```



=== "url_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|THREAT|url|1|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 20:48:21 deviceExternalId=xxxxxxxxxxxxx PanOSApplicationCategory=database PanOSApplicationContainer= PanOSApplicationRisk=2 PanOSApplicationSubcategory=database PanOSApplicationTechnology=client-server PanOSCaptivePortal=false PanOSCloudHostname=xxxxx PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceOS= dntdom=xxxxx duser=xxxxx o"'"test duid= PanOSHTTPRefererFQDN= PanOSHTTPRefererPort= PanOSHTTPRefererProtocol= PanOSHTTPRefererURLPath= PanOSInboundInterfaceDetailsPort=0 PanOSInboundInterfaceDetailsSlot=0 PanOSInboundInterfaceDetailsType=unknown PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer=true PanOSIsContainer=false PanOSIsDecryptMirror=false PanOSIsDecrypted=false PanOSIsDuplicateLog=false PanOSIsEncrypted=false PanOSIsIPV6=false PanOSIsMptcpOn=false PanOSIsNonStandardDestinationPort=false PanOSIsPacketCapture=false PanOSIsPhishing=false PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy=false PanOSIsReconExcluded=false PanOSIsSaaSApplication=false PanOSIsServertoClient=false PanOSIsSourceXForwarded=true PanOSIsSystemReturn=true PanOSIsTransaction=false PanOSIsTunnelInspected=false PanOSIsURLDenied=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT=false PanOSNonStandardDestinationPort=32350 PanOSOutboundInterfaceDetailsPort=2 PanOSOutboundInterfaceDetailsSlot=1 PanOSOutboundInterfaceDetailsType=ethernet PanOSOutboundInterfaceDetailsUnit=0 PanOSPacket= PanOSSanctionedStateofApp=false PanOSSeverity=Informational PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom=xxxxx suser=xxxxx xxxxx suid= PanOSTunneledApplication=untunneled PanOSURLDomain=?% PanOSUsers=xxxxx\\xxxxx xxxxx PanOSVirtualSystemID=1 PanOSConfigVersion=10.0 start=Mar 01 2021 20:48:16 src=1.1.1.1 dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=allow-business-apps cs1Label=Rule suser0=xxxxx\\xxxxx xxxxx duser0=xxxxx\\xxxxx o"'"test app=maxdb cs3=vsys1 cs3Label=VirtualLocation cs4=ethernet4Zone-test4 cs4Label=FromZone cs5=untrust cs5Label=ToZone deviceInboundInterface=unknown deviceOutboundInterface=ethernet1/2 cs6=rs-logging cs6Label=LogSetting cn1=980296 cn1Label=SessionID cnt=1 spt=32350 dpt=1532 sourceTranslatedPort=26236 destinationTranslatedPort=12016 proto=tcp act=block-url request=?% cs2=sports cs2Label=URLCategory flexString2=server to client flexString2Label=DirectionOfAttack externalId=xxxxxxxxxxxxx PanOSSourceLocation=west-coast PanOSDestinationLocation=PK requestContext=application/jpeg fileId=0 PanOSURLCounter=1 requestClientApplication= PanOSX-Forwarded-For= PanOSReferer= PanOSDGHierarchyLevel1=11 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=xxxxx PanOSSourceUUID= PanOSDestinationUUID= requestMethod=post PanOSIMSI=1 PanOSIMEI=Navy Base PanOSParentSessionID=8802 PanOSParentStarttime=Mar 01 2021 20:48:10 PanOSTunnel=VXLAN PanOSInlineMLVerdict=overflow PanOSContentVersion=50222 PanOSSigFlags=2 PanOSHTTPHeaders= PanOSURLCategoryList=sports,​11008,​38340 PanOSRuleUUID=ec14df0b-c845-4435-87a2-d207730f5ae8 PanOSHTTP2Connection=8802 PanOSDynamicUserGroupName= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory=L-Phone PanOSSourceDeviceProfile=l-profile PanOSSourceDeviceModel=Note 4G PanOSSourceDeviceVendor=Lenovo PanOSSourceDeviceOSFamily=K6 PanOSSourceDeviceOSVersion=Android v9 PanOSSourceDeviceHost=pan-505 PanOSSourceDeviceMac=596703749274 PanOSDestinationDeviceCategory=L-Phone PanOSDestinationDeviceProfile=l-profile PanOSDestinationDeviceModel=Note XT PanOSDestinationDeviceVendor=Lenovo PanOSDestinationDeviceOSFamily=K8 PanOSDestinationDeviceOSVersion=Android v8 PanOSDestinationDeviceHost=pan-506 PanOSDestinationDeviceMac=150083646537 PanOSContainerID=1873cc5c-0d31 PanOSContainerNameSpace=pns_default PanOSContainerName=pan-dp-77754f4 PanOSSourceEDL= PanOSDestinationEDL= PanOSHostID=xxxxxxxxxxxxxx PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSSourceDynamicAddressGroup= blue_dag PanOSDestinationDynamicAddressGroup= PanOSTimeGeneratedHighResolution=Mar 01 2021 20:48:16 PanOSNSSAINetworkSliceType=b5
    ```



=== "userid_cef"


    ```json
	CEF:0|Palo Alto Networks|LF|2.0|USERID|logout|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:06:02 deviceExternalId=xxxxxxxxxxxxx PanOSConfigVersion= dntdom=paloaltonetwork duser=xxxxx duid= PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSIsDuplicateLog=false PanOSIsDuplicateUser= PanOSIsPrismaNetworks=false PanOSIsPrismaUsers=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSUserGroupFound= start=Mar 01 2021 21:06:02 cs3=vsys1 cs3Label=VirtualLocation src=1.1.1.1 dst=1.1.1.1 duser0=paloaltonetworks\\xxxxx cs4=fake-data-source-169 cs4Label=MappingDataSourceName cat=0 cnt=1 cn3=3531 cn3Label=MappingTimeout spt=21015 dpt=49760 cs5=probing cs5Label=MappingDataSource cs6=netbios_probing cs6Label=MappingDataSourceType externalId=xxxxxxxxxxxxx PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 cn2=1 cn2Label=VirtualSystemID cs1=xxxxx cs1Label=MFAFactorType end=Jul 09 2019 18:15:44 cn1=3 cn1Label=AuthFactorNo PanOSUGFlags=0x100 PanOSUserIdentifiedBySource=xxxxxxxxxxxxxx PanOSTag= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12
    ```



=== "wildfire1_json"


    ```json
	{
        "TimeReceived": "2023-05-30T06:54:42.000000Z",
        "DeviceSN": "111111111111",
        "LogType": "THREAT",
        "Subtype": "wildfire",
        "ConfigVersion": "10.1",
        "TimeGenerated": "2023-05-30T06:52:13.000000Z",
        "SourceAddress": "1.2.3.4",
        "DestinationAddress": "5.6.7.8",
        "NATSource": "4.3.2.1",
        "NATDestination": "8.7.6.5",
        "Rule": "Normal Internet Access browser",
        "SourceUser": "john.doe@example.org",
        "DestinationUser": null,
        "Application": "web-browsing",
        "VirtualLocation": "vsys1",
        "FromZone": "Trust",
        "ToZone": "Untrust",
        "InboundInterface": "ethernet1/20",
        "OutboundInterface": "ethernet1/1",
        "LogSetting": "Panorama_CDL",
        "SessionID": 444444,
        "RepeatCount": 1,
        "SourcePort": 55555,
        "DestinationPort": 80,
        "NATSourcePort": 40114,
        "NATDestinationPort": 80,
        "Protocol": "tcp",
        "Action": "block",
        "FileName": "mp3.exe",
        "ThreatID": "Windows Executable (EXE)(52020)",
        "VendorSeverity": "Informational",
        "DirectionOfAttack": "server to client",
        "SequenceNo": 7117268851537282868,
        "SourceLocation": "10.0.0.0-10.255.255.255",
        "DestinationLocation": "CN",
        "PacketID": 0,
        "FileHash": "adc83b19e793491b1c6ea0fd8b46cd9f32e592fc",
        "ApplianceOrCloud": "wildfire.paloaltonetworks.com\u0000",
        "URLCounter": 1,
        "FileType": "pe",
        "SenderEmail": null,
        "EmailSubject": null,
        "RecipientEmail": null,
        "ReportID": 33333333333,
        "DGHierarchyLevel1": 997,
        "DGHierarchyLevel2": 738,
        "DGHierarchyLevel3": 0,
        "DGHierarchyLevel4": 0,
        "VirtualSystemName": "",
        "DeviceName": "MyDevice",
        "SourceUUID": null,
        "DestinationUUID": null,
        "IMSI": 0,
        "IMEI": null,
        "ParentSessionID": 0,
        "ParentStarttime": "1970-01-01T00:00:00.000000Z",
        "Tunnel": "N/A",
        "ThreatCategory": "unknown",
        "ContentVersion": "0",
        "SigFlags": "0x0",
        "RuleUUID": "50afdf91-0d37-4729-8052-1382912d9895",
        "HTTP2Connection": 0,
        "DynamicUserGroupName": null,
        "X-Forwarded-ForIP": null,
        "SourceDeviceCategory": null,
        "SourceDeviceProfile": null,
        "SourceDeviceModel": null,
        "SourceDeviceVendor": null,
        "SourceDeviceOSFamily": null,
        "SourceDeviceOSVersion": null,
        "SourceDeviceHost": null,
        "SourceDeviceMac": null,
        "DestinationDeviceCategory": null,
        "DestinationDeviceProfile": null,
        "DestinationDeviceModel": null,
        "DestinationDeviceVendor": null,
        "DestinationDeviceOSFamily": null,
        "DestinationDeviceOSVersion": null,
        "DestinationDeviceHost": null,
        "DestinationDeviceMac": null,
        "ContainerID": null,
        "ContainerNameSpace": null,
        "ContainerName": null,
        "SourceEDL": null,
        "DestinationEDL": null,
        "HostID": null,
        "EndpointSerialNumber": "xxxxxxxxxxx",
        "DomainEDL": null,
        "SourceDynamicAddressGroup": null,
        "DestinationDynamicAddressGroup": null,
        "PartialHash": 0,
        "TimeGeneratedHighResolution": "2023-05-30T06:52:14.052000Z",
        "NSSAINetworkSliceType": null
    }
    ```



