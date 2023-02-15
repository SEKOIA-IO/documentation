
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | Palo Alto can record traffic events flowing through their firewall |
| `Network protocol analysis` | Palo Alto firewall does traffic analysis at physical/data/transport layers |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `authentication`, `network` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "User_id_1_csv.json"

    ```json
	
    {
        "message": "1,2020/12/04 16:00:02,016401002222,USERID,login,2305,2020/12/04 16:00:02,vsys,1.2.3.4,user1,srv1.example.local,0,1,12000,0,0,active-directory,,968683723,0x8000000000000000,12,0,0,0,,hostexample,1,,2020/12/04 16:00:02,1,0x80,user1",
        "event": {
            "category": [
                "authentication"
            ],
            "kind": "event",
            "type": [
                "start"
            ]
        },
        "action": {
            "type": "login"
        },
        "destination": {
            "port": 0
        },
        "log": {
            "hostname": "hostexample",
            "logger": "userid"
        },
        "observer": {
            "product": "PAN-OS"
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4",
            "port": 0
        },
        "user": {
            "name": "user1"
        },
        "paloalto": {
            "Threat_ContentType": "login",
            "EventID": "0"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "user1"
            ]
        },
        "host": {
            "name": "hostexample"
        }
    }
    	
	```


=== "User_id_2_csv.json"

    ```json
	
    {
        "message": "1,2020/12/04 16:00:02,01640103000,USERID,login,2200,2020/12/04 16:00:02,vsys,10.0.0.2,user1,srv1.example.local,0,1,13000,0,0,active-directory,,968700000,0x8000000000000000,12,0,0,0,,hostname_example,1,,2020/12/04 16:00:02,1,0x0,user1",
        "event": {
            "category": [
                "authentication"
            ],
            "kind": "event",
            "type": [
                "start"
            ]
        },
        "action": {
            "type": "login"
        },
        "destination": {
            "port": 0
        },
        "log": {
            "hostname": "hostname_example",
            "logger": "userid"
        },
        "observer": {
            "product": "PAN-OS"
        },
        "source": {
            "address": "10.0.0.2",
            "ip": "10.0.0.2",
            "port": 0
        },
        "user": {
            "name": "user1"
        },
        "paloalto": {
            "Threat_ContentType": "login",
            "EventID": "0"
        },
        "related": {
            "ip": [
                "10.0.0.2"
            ],
            "user": [
                "user1"
            ]
        },
        "host": {
            "name": "hostname_example"
        }
    }
    	
	```


=== "auth_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|AUTH|Radius|3|ProfileToken=xxxxx dtz=UTC rt=Feb 28 2021 18:20:54 deviceExternalId=xxxxxxxxxxxxx PanOSConfigVersion=10.0 PanOSAuthenticatedUserDomain=paloaltonetwork PanOSAuthenticatedUserName=xxxxx PanOSAuthenticatedUserUUID= PanOSClientTypeName= PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSIsDuplicateLog=false PanOSIsPrismaNetworks=false PanOSIsPrismaUsers=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSRuleMatched= start=Feb 28 2021 18:20:40 cs3=vsys1 cs3Label=VirtualLocation c6a2=::ffff:0 c6a2Label=Source IPv6 Address c6a3=::ffff:0 c6a3Label=Destination IPv6 Address duser=paloaltonetwork\\\\xxxxx cs2=paloaltonetwork\\\\xxxxx cs2Label=NormalizeUser fname=Authentication object2 cs4=DC cs4Label=AuthenticationPolicy cnt=33554432 cn2=-5257671089978343424 cn2Label=MFAAuthenticationID PanOSMFAVendor=Symantec VIP cs6=rs-logging cs6Label=LogSetting cs1=deny-attackers cs1Label=AuthServerProfile PanOSAuthenticationDescription=www.something cs5=Unknown cs5Label=ClientType msg=Invalid Certificate cn1=0 cn1Label=AuthFactorNo externalId=xxxxxxxxxxxxx PanOSDGHierarchyLevel1=11 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=xxxxx PanOSVirtualSystemID=1 PanOSAuthenticationProtocol=EAP-TTLS with PAP PanOSRuleMatchedUUID= PanOSTimeGeneratedHighResolution=Feb 28 2021 18:20:41 PanOSSourceDeviceCategory=src_category_list-1 PanOSSourceDeviceProfile=src_profile_list-1 PanOSSourceDeviceModel=src_model_list-1 PanOSSourceDeviceVendor=src_vendor_list-1 PanOSSourceDeviceOSFamily=src_osfamily_list-0 PanOSSourceDeviceOSVersion=src_osversion_list-2 PanOSSourceDeviceHost=src_host_list-0 PanOSSourceDeviceMac=src_mac_list-2 PanOSAuthCacheServiceRegion= PanOSUserAgentString= PanOSSessionID=",
        "event": {
            "start": "2021-02-28T18:20:40.000000Z",
            "timezone": "UTC",
            "dataset": "auth",
            "kind": "event",
            "category": [
                "authentication"
            ],
            "type": [
                "info"
            ],
            "severity": 3
        },
        "@timestamp": "2021-02-28T18:20:54.000000Z",
        "destination": {
            "user": {
                "name": "paloaltonetwork\\\\xxxxx"
            }
        },
        "host": {
            "hostname": "xxxxx",
            "name": "xxxxx",
            "id": "xxxxxxxxxxxxx",
            "mac": "src_mac_list-2",
            "os": {
                "family": "src_osfamily_list-0",
                "version": "src_osversion_list-2"
            },
            "type": "src_category_list-1"
        },
        "log": {
            "hostname": "xxxxx",
            "logger": "auth"
        },
        "observer": {
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "paloalto": {
            "PanOSSourceDeviceHost": "src_host_list-0",
            "PanOSSourceDeviceVendor": "src_vendor_list-1",
            "PanOSSourceDeviceModel": "src_model_list-1",
            "PanOSSourceDeviceProfile": "src_profile_list-1"
        },
        "related": {
            "hosts": [
                "xxxxx"
            ],
            "user": [
                "paloaltonetwork\\\\xxxxx"
            ]
        }
    }
    	
	```


=== "decryption_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|DECRYPTION|end|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 20:35:54 PanOSDeviceSN=xxxxxxxxxxxxx PanOSConfigVersion=null start=Mar 01 2021 20:35:54 src=1.1.1.1 dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=allow-all-employees cs1Label=Rule suser=paloaltonetwork\\\\\\\\xxxxx duser=paloaltonetwork\\\\\\\\xxxxx app=gmail-base cs3=vsys1 cs3Label=VirtualLocation cs4=datacenter cs4Label=FromZone cs5=ethernet4Zone-test1 cs5Label=ToZone deviceInboundInterface=ethernet1/1 deviceOutboundInterface=tunnel.901 cs6=test cs6Label=LogSetting PanOSTimeReceivedManagementPlane=Dec 12 2019 22:16:48 cn1=106112 cn1Label=SessionID cnt=1 spt=16524 dpt=20122 sourceTranslatedPort=15856 destinationTranslatedPort=10128 proto=tcp act=deny PanOSTunnel=N/A PanOSSourceUUID= PanOSDestinationUUID= PanOSRuleUUID=fnullacnullnulle1-2c69-4f2b-8293-46ee4c73737e PanOSClientToFirewall=null PanOSFirewallToClient=null PanOSTLSVersion=null PanOSTLSKeyExchange=null PanOSTLSEncryptionAlgorithm=null PanOSTLSAuth=null PanOSPolicyName= PanOSEllipticCurve= PanOSErrorIndex=null PanOSRootStatus=null PanOSChainStatus=null PanOSProxyType=null PanOSCertificateSerial= PanOSFingerprint= PanOSTimeNotBefore=0 PanOSTimeNotAfter=0 PanOSCertificateVersion=null PanOSCertificateSize=0 PanOSCommonNameLength=0 PanOSIssuerNameLength=0 PanOSRootCNLength=0 PanOSSNILength=0 PanOSCertificateFlags=0 PanOSCommonName= PanOSIssuerCommonName= PanOSRootCommonName= PanOSServerNameIndication= PanOSErrorMessage= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup=test PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12 PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceHost= PanOSSourceDeviceMac= PanOSDestinationDeviceCategory= PanOSDestinationDeviceProfile= PanOSDestinationDeviceModel= PanOSDestinationDeviceVendor= PanOSDestinationDeviceOSFamily= PanOSDestinationDeviceOSVersion= PanOSDestinationDeviceHost= PanOSDestinationDeviceMac= externalId=xxxxxxxxxxxxx",
        "event": {
            "start": "2021-03-01T20:35:54.000000Z",
            "action": "deny",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "decryption",
            "kind": "event",
            "type": [
                "info"
            ],
            "severity": 3
        },
        "@timestamp": "2021-03-01T20:35:54.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 10128
            },
            "port": 20122,
            "user": {
                "name": "paloaltonetwork\\\\\\\\xxxxx"
            }
        },
        "log": {
            "logger": "decryption"
        },
        "network": {
            "application": "gmail-base",
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "ethernet4Zone-test1",
                    "name": "tunnel.901",
                    "id": "tunnel.901"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "datacenter",
                    "name": "1",
                    "id": "tunnel.901"
                }
            },
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "rule": {
            "name": "allow-all-employees",
            "uuid": "fnullacnullnulle1-2c69-4f2b-8293-46ee4c73737e"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 15856
            },
            "port": 16524,
            "user": {
                "name": "paloaltonetwork\\\\\\\\xxxxx"
            }
        },
        "user": {
            "name": "paloaltonetwork\\\\\\\\xxxxx"
        },
        "paloalto": {},
        "related": {
            "user": [
                "paloaltonetwork\\\\\\\\xxxxx"
            ],
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```


=== "file_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|THREAT|file|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:06:06 deviceExternalId=xxxxxxxxxxxxx PanOSConfigVersion= PanOSApplicationCategory=collaboration PanOSApplicationContainer= PanOSApplicationRisk=5 PanOSApplicationSubcategory=email PanOSApplicationTechnology=client-server PanOSCaptivePortal=false PanOSCloudHostname=PA-5220 PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDLPVersionFlag= PanOSDestinationDeviceClass= PanOSDestinationDeviceOS= dntdom= duser= duid= PanOSFileType=PNG File Upload PanOSInboundInterfaceDetailsPort=19 PanOSInboundInterfaceDetailsSlot=1 PanOSInboundInterfaceDetailsType=ethernet PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer=false PanOSIsContainer=false PanOSIsDecryptMirror=false PanOSIsDecrypted= PanOSIsDuplicateLog=false PanOSIsEncrypted= PanOSIsIPV6= PanOSIsMptcpOn=false PanOSIsNonStandardDestinationPort=false PanOSIsPacketCapture=false PanOSIsPhishing=false PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy=false PanOSIsReconExcluded=false PanOSIsSaaSApplication=false PanOSIsServertoClient=false PanOSIsSourceXForwarded= PanOSIsSystemReturn=false PanOSIsTransaction=false PanOSIsTunnelInspected=false PanOSIsURLDenied=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT=false PanOSNonStandardDestinationPort=0 PanOSOutboundInterfaceDetailsPort=19 PanOSOutboundInterfaceDetailsSlot=1 PanOSOutboundInterfaceDetailsType=ethernet PanOSOutboundInterfaceDetailsUnit=0 PanOSPacket= PanOSProfileName= PanOSSanctionedStateOfApp=false PanOSSeverity=Low PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom= suser= suid= PanOSThreatCategory= PanOSThreatNameFirewall= PanOSTunneledApplication=untunneled PanOSURL= PanOSUsers=1.1.1.1 PanOSVirtualSystemID=1 start=Mar 01 2021 21:06:06 src=1.1.1.1 dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=dg-log-policy cs1Label=Rule suser0= duser0= app=smtp cs3=smtp cs3Label=VirtualLocation cs4=tap cs4Label=FromZone cs5=tap cs5Label=ToZone deviceInboundInterface=ethernet1/19 deviceOutboundInterface=ethernet1/19 cs6=test cs6Label=LogSetting cn1=4016143 cn1Label=SessionID cnt=9 spt=37404 dpt=25 sourceTranslatedPort=0 destinationTranslatedPort=0 proto=tcp act=alert filePath=page-icon.png cs2=any cs2Label=URLCategory flexString2=client to server flexString2Label=DirectionOfAttack externalId=xxxxxxxxxxxxx PanOSSourceLocation=1.1.1.1-1.1.1.1 PanOSDestinationLocation=1.1.1.1-1.1.1.1 fileId=0 PanOSFileHash= PanOSReportID= PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStartTime=Jan 01 1970 00:00:00 PanOSTunnel=N/A PanOSContentVersion= PanOSSigFlags=0 PanOSRuleUUID= PanOSHTTP2Connection= PanOSDynamicUserGroup= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceHost= PanOSSourceDeviceMac= PanOSDestinationDeviceCategory= PanOSDestinationDeviceProfile= PanOSDestinationDeviceModel= PanOSDestinationDeviceVendor= PanOSDestinationDeviceOSFamily= PanOSDestinationDeviceOSVersion= PanOSDestinationDeviceHost= PanOSDestinationDeviceMac= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSHostID=xxxxxxxxxxxxxx PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSDomainEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSPartialHash= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12 PanOSReasonForDataFilteringAction= PanOSJustification= PanOSNSSAINetworkSliceType=",
        "event": {
            "start": "2021-03-01T21:06:06.000000Z",
            "action": "alert",
            "timezone": "UTC",
            "dataset": "threat",
            "kind": "event",
            "category": [
                "file"
            ],
            "type": [
                "info"
            ],
            "severity": 3
        },
        "@timestamp": "2021-03-01T21:06:06.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "geo": {
                "country_iso_code": "1.1.1.1-1.1.1.1"
            },
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 0
            },
            "port": 25
        },
        "host": {
            "hostname": "PA-5220",
            "name": "PA-5220",
            "id": "xxxxxxxxxxxxx"
        },
        "log": {
            "hostname": "PA-5220",
            "logger": "threat"
        },
        "network": {
            "application": "smtp",
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "tap",
                    "name": "ethernet1/19",
                    "id": "19"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "tap",
                    "name": "9",
                    "id": "19"
                }
            },
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "rule": {
            "name": "dg-log-policy"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 0
            },
            "port": 37404
        },
        "paloalto": {
            "PanOSEndpointSerialNumber": "xxxxxxxxxxxxxx",
            "PanOSSourceLocation": "1.1.1.1-1.1.1.1",
            "URLCategory": "any"
        },
        "related": {
            "hosts": [
                "PA-5220"
            ],
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```


=== "globalprotect_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|GLOBALPROTECT|globalprotect|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 20:35:54 PanOSDeviceSN=xxxxxxxxxxxxx PanOSConfigVersion= start=Mar 01 2021 20:35:54 PanOSVirtualSystem=vsys1 PanOSEventIDValue=satellite-gateway-update-route PanOSStage=connected PanOSAuthMethod=RADIUS PanOSTunnelType=ipsec PanOSSourceUserName=xxxxx\\\\\\\\xxxxx PanOSSourceRegion=ET PanOSEndpointDeviceName=machine_name2 PanOSPublicIPv4=1.1.1.1 PanOSPublicIPv6=xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx PanOSPrivateIPv4=1.1.1.1 PanOSPrivateIPv6=xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx PanOSHostID=xxxxxxxxxxxxxxe667947f-d92e-4815-9222-89438203bc2b PanOSEndpointSN=serialno_list-1 PanOSGlobalProtectClientVersion=3.0.9 PanOSEndpointOSType=Intel Mac OS PanOSEndpointOSVersion=9.3.5 PanOSCountOfRepeats=16777216 PanOSQuarantineReason=Malicious Traffic PanOSConnectionError=Client cert not present PanOSDescription=opaque_list-1 PanOSEventStatus=failure PanOSGlobalProtectGatewayLocation=San Francisco PanOSLoginDuration=1 PanOSConnectionMethod=connect_method_list-1 PanOSConnectionErrorID=0 PanOSPortal=portal_list-2 PanOSSequenceNo=34401910 PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12 PanOSGatewaySelectionType= PanOSSSLResponseTime= PanOSGatewayPriority= PanOSAttemptedGateways= PanOSGateway= PanOSDGHierarchyLevel1=20 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= PanOSDeviceName=PA-VM PanOSVirtualSystemID=1",
        "event": {
            "start": "2021-03-01T20:35:54.000000Z",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "globalprotect",
            "kind": "event",
            "reason": "Client cert not present",
            "type": [
                "info"
            ],
            "severity": 3
        },
        "@timestamp": "2021-03-01T20:35:54.000000Z",
        "host": {
            "hostname": "machine_name2",
            "name": "machine_name2",
            "os": {
                "type": "Intel Mac OS"
            }
        },
        "log": {
            "logger": "globalprotect"
        },
        "network": {
            "type": "ipsec"
        },
        "observer": {
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "source": {
            "user": {
                "name": "xxxxx\\\\\\\\xxxxx"
            }
        },
        "user": {
            "name": "xxxxx\\\\\\\\xxxxx"
        },
        "paloalto": {
            "PanOSQuarantineReason": "Malicious Traffic"
        },
        "related": {
            "hosts": [
                "machine_name2"
            ],
            "user": [
                "xxxxx\\\\\\\\xxxxx"
            ]
        }
    }
    	
	```


=== "globalprotect_csv.json"

    ```json
	
    {
        "message": "1,2020/12/08 14:30:55,011111114444,GLOBALPROTECT,0,2305,2020/12/08 13:30:55,vsys1,gw-auth,login,Other,,user,FR,AAAABBBBB,1.2.3.4,0.0.0.0,0.0.0.0,0.0.0.0,aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee,ABCDEFG,5.1.4,Windows,\"Microsoft Windows 10 Pro , 64-bit\",1,,,\"\",success,,0,user-logon,0,gw1,1234567,0x8000000000000000",
        "event": {
            "category": [
                "network"
            ],
            "kind": "event",
            "type": [
                "info"
            ]
        },
        "action": {
            "type": "0",
            "outcome": "success"
        },
        "log": {
            "logger": "globalprotect"
        },
        "observer": {
            "product": "PAN-OS"
        },
        "source": {
            "address": "1.2.3.4",
            "geo": {
                "country_iso_code": "FR"
            },
            "ip": "1.2.3.4"
        },
        "user_agent": {
            "os": {
                "name": "Windows",
                "version": "Microsoft Windows 10 Pro , 64-bit"
            }
        },
        "user": {
            "name": "user"
        },
        "paloalto": {
            "Threat_ContentType": "0",
            "EventID": "gw-auth"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "user"
            ]
        }
    }
    	
	```


=== "hip_match_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|HIPMATCH||3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:20:13 deviceExternalId=xxxxxxxxxxxxx PanOSIsDuplicateLog=false PanOSIsPrismaNetworks=false PanOSIsPrismaUsers=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom=xxxxx dntdom=xxxxx suser=xxxxx xxxxx duser=xxxxx xxxxx suid= duid= PanOSTenantID=xxxxxxxxxxxxx PanOSUUID= PanOSConfigVersion= start=Mar 01 2021 21:20:13 PanOSSourceUser=xxxxx\\\\xxxxx xxxxx cs3=vsys1 cs3Label=VirtualLocation shost=machine_name1 dhost=machine_name1 cs2=iOS cs2Label=EndpointOSType src=1.1.1.1 dst=1.1.1.1 cat=match_name1 cnt=1 PanOSHipMatchType=HIP Profile externalId=xxxxxxxxxxxxx PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 cn2=1 cn2Label=VirtualSystemID c6a1=xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx c6a1Label=Device IPv6 Address PanOSHostID=xxxxxxxxxxxxxxe777947f-d92e-4815-9222-89438203bc2b PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceMac= PanOSSourceDeviceHost= PanOSSource= PanOSTimestampDeviceIdentification=Dec PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12",
        "event": {
            "start": "2021-03-01T21:20:13.000000Z",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "hipmatch",
            "kind": "event",
            "type": [
                "info"
            ],
            "severity": 3
        },
        "@timestamp": "2021-03-01T21:20:13.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "user": {
                "name": "xxxxx xxxxx"
            }
        },
        "host": {
            "hostname": "PA-5220",
            "name": "PA-5220",
            "id": "xxxxxxxxxxxxx"
        },
        "log": {
            "hostname": "PA-5220",
            "logger": "hipmatch"
        },
        "observer": {
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "user": {
                "name": "xxxxx xxxxx"
            }
        },
        "user": {
            "name": "xxxxx xxxxx"
        },
        "paloalto": {
            "PanOSEndpointSerialNumber": "xxxxxxxxxxxxxx"
        },
        "related": {
            "hosts": [
                "PA-5220"
            ],
            "user": [
                "xxxxx xxxxx"
            ],
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```


=== "icmp_allow_csv.json"

    ```json
	
    {
        "message": "<14>Sep 16 10:00:02 PP 1,9/16/19 10:00,1801017000,TRAFFIC,start,2049,9/16/19 10:00,1.2.3.4,4.3.2.1,1.2.3.4,10.0.1.2,PING,,,ping,vsys,AAAAA,Zone1,ethernet1/1,ae2.11,Secure,9/16/19 10:00,24100,3,0,0,0,0,0x500000,icmp,allow,222,222,0,3,9/16/19 10:00,0,any,0,50660388939,0x0,Spain,France,0,3,0,n/a,0,0,0,0,,PA,from-policy,,,0,,0,,N/A,0,0,0,0",
        "event": {
            "category": [
                "network"
            ],
            "duration": 0,
            "kind": "event",
            "type": [
                "start"
            ]
        },
        "action": {
            "name": "allow",
            "type": "start",
            "outcome": "success"
        },
        "destination": {
            "address": "4.3.2.1",
            "bytes": 0,
            "ip": "4.3.2.1",
            "nat": {
                "ip": "10.0.1.2",
                "port": 0
            },
            "packets": 0,
            "port": 0
        },
        "log": {
            "logger": "traffic"
        },
        "network": {
            "bytes": 222,
            "packets": 3,
            "transport": "icmp"
        },
        "observer": {
            "product": "PAN-OS"
        },
        "rule": {
            "name": "PING"
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 222,
            "ip": "1.2.3.4",
            "nat": {
                "ip": "1.2.3.4",
                "port": 0
            },
            "packets": 3,
            "port": 0
        },
        "paloalto": {
            "Threat_ContentType": "start"
        },
        "related": {
            "ip": [
                "1.2.3.4",
                "10.0.1.2",
                "4.3.2.1"
            ]
        }
    }
    	
	```


=== "iptag_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|IPTAG|iptag|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:20:13 deviceExternalId=xxxxxxxxxxxxx PanOSTenantID=xxxxxxxxxxxxx PanOSIsDuplicateLog=false PanOSIsPrismaNetworks=false PanOSIsPrismaUsers=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSetting= PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSRuleMatched= PanOSRuleMatchedUUID= PanOSConfigVersion= start=Mar 01 2021 21:20:13 cs3=vsys1 cs3Label=VirtualLocation src=1.1.1.1 dst=1.1.1.1 PanOSTagName= PanOSEventID=Unregister cnt=1 PanOSMappingTimeout=10 PanOSMappingDataSource=XMLAPI PanOSMappingDataSourceType=XML-API PanOSMappingDataSourceSubType=Unknown externalId=xxxxxxxxxxxxx PanOSDGHierarchyLevel1=18 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-VM cn2=1 cn2Label=VirtualSystemID PanOSIPSubnetRange= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12",
        "event": {
            "start": "2021-03-01T21:20:13.000000Z",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "iptag",
            "kind": "event",
            "type": [
                "info"
            ],
            "severity": 3
        },
        "@timestamp": "2021-03-01T21:20:13.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "host": {
            "hostname": "PA-VM",
            "name": "PA-VM",
            "id": "xxxxxxxxxxxxx"
        },
        "log": {
            "hostname": "PA-VM",
            "logger": "iptag"
        },
        "observer": {
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "paloalto": {},
        "related": {
            "hosts": [
                "PA-VM"
            ],
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```


=== "sctp_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|SCTP||9|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:22:02 deviceExternalId=xxxxxxxxxxxxx PanOSCaptivePortal= PanOSContentVersion= PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceMac= PanOSDestinationDeviceModel= PanOSDestinationDeviceOS= PanOSDestinationDeviceVendor= PanOSDestinationLocation=IN PanOSDestinationUUID= PanOSDestinationUserDomain=paloaltonetwork PanOSDestinationUserName=xxxxx PanOSDestinationUserUUID= PanOSInboundInterfaceDetailsPort=1 PanOSInboundInterfaceDetailsSlot=1 PanOSInboundInterfaceDetailsType=ethernet PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer= PanOSIsContainer= PanOSIsDecryptMirror= PanOSIsDecryptedLog= PanOSIsDecryptedPayloadForward= PanOSIsDuplicateLog=false PanOSIsIPV6= PanOSIsInspectrionBeforeSession= PanOSIsMptcpOn= PanOSIsNonStandardDestinationPort= PanOSIsPacketCapture= PanOSIsPhishing= PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy= PanOSIsReconExcluded= PanOSIsServertoClient= PanOSIsSourceXForwarded= PanOSIsSystemReturn= PanOSIsTransaction= PanOSIsTunnelInspected= PanOSIsURLDenied= PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT= PanOSOutboundInterfaceDetailsPort=2 PanOSOutboundInterfaceDetailsSlot=1 PanOSOutboundInterfaceDetailsType=ethernet PanOSOutboundInterfaceDetailsUnit=0 PanOSSessionEndReason= PanOSSessionOwnerMidx= PanOSSessionTracker= PanOSSeverity=Critical PanOSSourceDeviceClass= PanOSSourceDeviceMac= PanOSSourceDeviceModel= PanOSSourceDeviceOS= PanOSSourceDeviceVendor= PanOSSourceLocation=US PanOSSourceUUID= PanOSSourceUserDomain=paloaltonetwork PanOSSourceUserName=xxxxx PanOSSourceUserUUID= PanOSTunnel=N/A PanOSVirtualSystemID=1 PanOSConfigVersion= start=Mar 01 2021 21:22:02 src=1.1.1.1 dst=1.1.1.1 PanOSNATSource=1.1.1.1 PanOSNATDestination=1.1.1.1 cs1=allow-business-apps cs1Label=Rule PanOSSourceUser=paloaltonetwork\\\\xxxxx PanOSDestinationUser=paloaltonetworkxxxxx PanOSApplication=panorama cs3=vsys1 cs3Label=VirtualLocation cs4=corporate cs4Label=FromZone cs5=untrust cs5Label=ToZone PanOSInboundInterface=ethernet1/1 deviceOutboundInterface=ethernet1/2 cs6=test cs6Label=LogSetting PanOSSessionID=391582 cnt=1 spt=3033 dpt=5496 PanOSNATSourcePort=26714 PanOSNATDestinationPort=15054 proto=tcp act=alert PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 externalId=xxxxxxxxxxxxx PanOSEndpointAssociationID=2086888838 PanOSPayloadProtocolID=-1 PanOSSctpChunkType=9 PanOSSCTPEventType=Kerberos single sign-on failed PanOSEventCode=3 PanOSVerificationTag1=0x3bae3042 PanOSVerificationTag2=0x1911015e PanOSSctpCauseCode=0 PanOSDiamAppID=-1 PanOSDiameterCommandCode=-1 PanOSDiamAvpCode=0 PanOSStreamID=0 PanOSAssocationEndReason= PanOSMapAppCode=0 PanOSSccpCallingSSN=0 PanOSSccpCallingGt= PanOSSctpFilter= PanOSChunksTotal=0 PanOSChunksSent=0 PanOSChunksReceived=0 PanOSPacketsTotal=0 PanOSPacketsSent=0 PanOSPacketsReceived=0 PanOSRuleUUID= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12",
        "event": {
            "start": "2021-03-01T21:22:02.000000Z",
            "action": "alert",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "sctp",
            "kind": "event",
            "type": [
                "info"
            ],
            "severity": 9
        },
        "@timestamp": "2021-03-01T21:22:02.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "geo": {
                "country_iso_code": "IN"
            },
            "ip": "1.1.1.1",
            "packets": 0,
            "port": 5496
        },
        "host": {
            "hostname": "PA-5220",
            "name": "PA-5220",
            "id": "xxxxxxxxxxxxx"
        },
        "log": {
            "hostname": "PA-5220",
            "logger": "sctp"
        },
        "network": {
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "untrust",
                    "name": "ethernet1/2",
                    "id": "2"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "corporate"
                }
            },
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "rule": {
            "name": "allow-business-apps"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "packets": 0,
            "port": 3033,
            "user": {
                "name": "xxxxx"
            }
        },
        "user": {
            "name": "xxxxx"
        },
        "paloalto": {
            "PanOSSourceLocation": "US"
        },
        "related": {
            "hosts": [
                "PA-5220"
            ],
            "ip": [
                "1.1.1.1"
            ],
            "user": [
                "xxxxx"
            ]
        }
    }
    	
	```


=== "system_csv.json"

    ```json
	
    {
        "message": "1,2020/12/08 13:44:55,11111114444,SYSTEM,auth,0,2020/12/08 13:44:55,,auth-success,GP,0,0,general,informational,\"authenticated for user 'user1'.   auth profile 'GP', vsys 'vsys123', server profile 'LDAP', server address 'srv01.entreprise.local', From: 1.2.3.4.\",5211100,0x8000000000000000,0,0,0,0,,fw1",
        "event": {
            "kind": "event",
            "reason": "authenticated for user 'user1'.   auth profile 'GP', vsys 'vsys123', server profile 'LDAP', server address 'srv01.entreprise.local', From: 1.2.3.4.",
            "category": [
                "authentication"
            ],
            "type": [
                "start"
            ]
        },
        "action": {
            "type": "auth"
        },
        "log": {
            "hostname": "fw1",
            "level": "informational",
            "logger": "system"
        },
        "observer": {
            "product": "PAN-OS"
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "name": "user1"
        },
        "paloalto": {
            "Threat_ContentType": "auth",
            "EventID": "auth-success"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "user1"
            ]
        },
        "host": {
            "name": "fw1"
        }
    }
    	
	```


=== "tcp_allow_csv.json"

    ```json
	
    {
        "message": "<14>Sep 16 10:00:02 PA-1 1,9/16/19 10:00,1801016000,TRAFFIC,start,2049,9/16/19 10:00,1.2.3.4,4.3.2.1,0.0.0.0,0.0.0.0,proxy1,,,web-browsing,vsys1234,v10213,zone1,a.1,b.2,Secure,9/16/19 10:00,60000,1,61000,80,0,0,0x0,tcp,allow,800,700,70,2,9/16/19 10:00,0,any,0,50660381839,0x0,10.0.0.0-10.255.255.255,10.0.0.0-10.255.255.255,0,2,1,n/a,0,0,0,0,,PP,from-policy,,,0,,0,,N/A,0,0,0,0",
        "event": {
            "category": [
                "network"
            ],
            "duration": 0,
            "kind": "event",
            "type": [
                "start"
            ]
        },
        "action": {
            "name": "allow",
            "type": "start",
            "outcome": "success"
        },
        "destination": {
            "address": "4.3.2.1",
            "bytes": 70,
            "ip": "4.3.2.1",
            "nat": {
                "ip": "0.0.0.0",
                "port": 0
            },
            "packets": 1,
            "port": 80
        },
        "log": {
            "logger": "traffic"
        },
        "network": {
            "bytes": 800,
            "packets": 2,
            "transport": "tcp"
        },
        "observer": {
            "product": "PAN-OS"
        },
        "rule": {
            "name": "proxy1"
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 700,
            "ip": "1.2.3.4",
            "nat": {
                "ip": "0.0.0.0",
                "port": 0
            },
            "packets": 2,
            "port": 61000
        },
        "paloalto": {
            "Threat_ContentType": "start"
        },
        "related": {
            "ip": [
                "0.0.0.0",
                "1.2.3.4",
                "4.3.2.1"
            ]
        }
    }
    	
	```


=== "threat_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|THREAT|spyware|1|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 20:48:21 deviceExternalId=xxxxxxxxxxxxx start=Mar 01 2021 20:48:16 PanOSApplicationCategory=general-internet PanOSApplicationContainer=sina-weibo PanOSApplicationRisk=4 PanOSApplicationSubcategory=social-networking PanOSApplicationTechnology=browser-based PanOSCaptivePortal=false PanOSCloudHostname=xxxxx PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceOS= dntdom=paloaltonetwork duser=xxxxx duid= PanOSHTTPMethod=get PanOSInboundInterfaceDetailsPort=0 PanOSInboundInterfaceDetailsSlot=0 PanOSInboundInterfaceDetailsType=unknown PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer=true PanOSIsContainer=false PanOSIsDecryptMirror=false PanOSIsDecrypted=false PanOSIsDuplicateLog=false PanOSIsEncrypted=false PanOSIsIPV6=false PanOSIsMptcpOn=false PanOSIsNonStandardDestinationPort=false PanOSIsPacketCapture=false PanOSIsPhishing=false PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy=false PanOSIsReconExcluded=false PanOSIsSaaSApplication=false PanOSIsServertoClient=false PanOSIsSourceXForwarded=true PanOSIsSystemReturn=true PanOSIsTransaction=false PanOSIsTunnelInspected=false PanOSIsURLDenied=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT=false PanOSNonStandardDestinationPort=13884 PanOSOutboundInterfaceDetailsPort=0 PanOSOutboundInterfaceDetailsSlot=0 PanOSOutboundInterfaceDetailsType=unknown PanOSOutboundInterfaceDetailsUnit=0 PanOSPacket= PanOSPayloadProtocolID=-1 PanOSSanctionedStateOfApp=false PanOSSeverity=Informational PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom=paloaltonetwork suser=xxxxx suid= cat=27379 PanOSThreatNameFirewall=27379 PanOSTunneledApplication=tunneled-app PanOSURLDomain= PanOSUsers=paloaltonetwork\\\\xxxxx PanOSVerdict= PanOSVirtualSystemID=1 c6a2=fe80:110:8897:efab:9202:b3ff:fe1e:8329 c6a2Label=Source IPv6 Address c6a3=fe80:110:8897:efab:9202:b3ff:fe1e:8329 c6a3Label=Destination IPv6 Address sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=deny-attackers cs1Label=Rule suser0=paloaltonetwork\\\\xxxxx duser0=paloaltonetwork\\\\xxxxx app=sina-weibo-base cs3=vsys1 cs3Label=VirtualLocation cs4=datacenter cs4Label=FromZone cs5=ethernet4Zone-test4 cs5Label=ToZone deviceInboundInterface=unknown deviceOutboundInterface=unknown cs6=rs-logging cs6Label=LogSetting cn1=947181 cn1Label=SessionID cnt=1 spt=13884 dpt=4228 sourceTranslatedPort=30116 destinationTranslatedPort=20966 proto=tcp act=drop-all request=some other fake filename PanOSThreatID=27379(27379) flexString2=server to client flexString2Label=DirectionOfAttack externalId=xxxxxxxxxxxxx PanOSSourceLocation=LY PanOSDestinationLocation=BR fileId=0 PanOSFileHash= PanOSApplianceOrCloud= PanOSURLCounter=0 PanOSFileType= PanOSSenderEmail= PanOSEmailSubject= PanOSRecipientEmail= PanOSReportID=0 PanOSDGHierarchyLevel1=11 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=xxxxx PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStarttime=Jan 01 1970 00:00:00 PanOSTunnel=N/A PanOSThreatCategory=unknown PanOSContentVersion=50059 PanOSSigFlags=0x0 PanOSRuleUUID=017e4d76-2003-47f4-8afc-1d35c808c615 PanOSHTTP2Connection=0 PanOSDynamicUserGroupName= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory=X-Phone PanOSSourceDeviceProfile=x-profile PanOSSourceDeviceModel=Note 4G PanOSSourceDeviceVendor=Lenovo PanOSSourceDeviceOSFamily=K6 PanOSSourceDeviceOSVersion=Android v9 PanOSSourceDeviceHost=pan-505 PanOSSourceDeviceMac=596703749274 PanOSDestinationDeviceCategory=X-Phone PanOSDestinationDeviceProfile=x-profile PanOSDestinationDeviceModel=MI PanOSDestinationDeviceVendor=Xiaomi PanOSDestinationDeviceOSFamily=A1 PanOSDestinationDeviceOSVersion=Android v9.1 PanOSDestinationDeviceHost=pan-622 PanOSDestinationDeviceMac=620797415366 PanOSContainerID=1873cc5c-0d31 PanOSContainerNameSpace=pns_default PanOSSourceEDL= PanOSDestinationEDL= PanOSHostID=xxxxxxxxxxxxxx PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSDomainEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSPartialHash=0 PanOSTimeGeneratedHighResolution=Mar 01 2021 20:48:16 PanOSNSSAINetworkSliceType=dc",
        "event": {
            "start": "2021-03-01T20:48:16.000000Z",
            "action": "drop-all",
            "timezone": "UTC",
            "dataset": "threat",
            "kind": "event",
            "category": [
                "malware"
            ],
            "type": [
                "info"
            ],
            "severity": 1
        },
        "@timestamp": "2021-03-01T20:48:21.000000Z",
        "destination": {
            "geo": {
                "country_iso_code": "BR"
            },
            "nat": {
                "ip": "1.1.1.1",
                "port": 20966
            },
            "port": 4228,
            "user": {
                "name": "xxxxx"
            }
        },
        "host": {
            "hostname": "xxxxx",
            "name": "xxxxx",
            "id": "xxxxxxxxxxxxx",
            "mac": "596703749274",
            "os": {
                "family": "K6",
                "version": "Android v9"
            },
            "type": "X-Phone"
        },
        "log": {
            "hostname": "xxxxx",
            "logger": "threat"
        },
        "network": {
            "application": "sina-weibo-base",
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "ethernet4Zone-test4",
                    "name": "unknown",
                    "id": "unknown"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "datacenter",
                    "name": "n",
                    "id": "unknown"
                }
            },
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "rule": {
            "name": "deny-attackers",
            "uuid": "017e4d76-2003-47f4-8afc-1d35c808c615"
        },
        "source": {
            "nat": {
                "ip": "1.1.1.1",
                "port": 30116
            },
            "port": 13884,
            "user": {
                "name": "xxxxx"
            }
        },
        "user": {
            "name": "xxxxx"
        },
        "paloalto": {
            "PanOSEndpointSerialNumber": "xxxxxxxxxxxxxx",
            "PanOSContainerNameSpace": "pns_default",
            "PanOSDestinationDeviceMac": "620797415366",
            "PanOSDestinationDeviceHost": "pan-622",
            "PanOSDestinationDeviceOSVersion": "Android v9.1",
            "PanOSDestinationDeviceOSFamily": "A1",
            "PanOSDestinationDeviceVendor": "Xiaomi",
            "PanOSDestinationDeviceModel": "MI",
            "PanOSDestinationDeviceProfile": "x-profile",
            "PanOSDestinationDeviceCategory": "X-Phone",
            "PanOSSourceDeviceHost": "pan-505",
            "PanOSSourceDeviceVendor": "Lenovo",
            "PanOSSourceDeviceModel": "Note 4G",
            "PanOSSourceDeviceProfile": "x-profile",
            "PanOSThreatCategory": "unknown",
            "PanOSSourceLocation": "LY",
            "PanOSThreatID": "27379(27379)"
        },
        "related": {
            "hosts": [
                "xxxxx"
            ],
            "user": [
                "xxxxx"
            ],
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```


=== "threat_csv.json"

    ```json
	
    {
        "message": "1,2021/08/31 14:00:02,001701000000,THREAT,vulnerability,2049,2021/08/31 14:00:02,10.0.0.2,10.2.0.1,0.0.0.0,0.0.0.0,abcd,,,web-browsing,vsys,env,zone2,a1.1,aec.2,podl,2021/08/31 14:00:02,279429,2,12345,80,0,0,0x2000,tcp,alert,\"EXAMPLE.PDF\",PDF Exploit Evasion Found(34805),any,informational,server-to-client,1320000,0x2000000000000000,10.0.0.0-10.255.255.255,10.0.0.0-10.255.255.255,0,,0,,,1,,,,,,,,0,0,0,0,0,,FW,,,,,0,,0,,N/A,code-execution,AppThreat-0000-1111,0x0,0,422342342,",
        "event": {
            "action": "code-execution",
            "kind": "event",
            "reason": "PDF Exploit Evasion Found(34805)",
            "category": [
                "vulnerability"
            ],
            "type": [
                "info"
            ]
        },
        "action": {
            "name": "alert",
            "type": "vulnerability",
            "outcome": "success"
        },
        "destination": {
            "address": "10.2.0.1",
            "ip": "10.2.0.1",
            "nat": {
                "ip": "0.0.0.0",
                "port": 0
            },
            "port": 80
        },
        "file": {
            "path": "EXAMPLE.PDF"
        },
        "log": {
            "hostname": "FW",
            "level": "informational",
            "logger": "threat"
        },
        "network": {
            "transport": "tcp"
        },
        "observer": {
            "product": "PAN-OS"
        },
        "rule": {
            "name": "abcd"
        },
        "source": {
            "address": "10.0.0.2",
            "ip": "10.0.0.2",
            "nat": {
                "ip": "0.0.0.0",
                "port": 0
            },
            "port": 12345
        },
        "paloalto": {
            "Threat_ContentType": "vulnerability",
            "ContentType": ""
        },
        "related": {
            "ip": [
                "0.0.0.0",
                "10.0.0.2",
                "10.2.0.1"
            ]
        },
        "host": {
            "name": "FW"
        }
    }
    	
	```


=== "traffic1_csv.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|TRAFFIC|end|3|dtz=UTC rt=Jul 31 2022 12:46:24 deviceExternalId=000000000000 PanOSConfigVersion=10.1 start=Jul 31 2022 12:46:07 src=1.2.3.4 dst=5.6.7.8 sourceTranslatedAddress=4.3.2.1 destinationTranslatedAddress=8.7.6.5 cs1=SO Access cs1Label=Rule suser= duser= app=outlook-web-online cs3=vsys1 cs3Label=VirtualLocation cs4=Trust cs4Label=FromZone cs5=Untrust cs5Label=ToZone deviceInboundInterface=ethernet1/10 deviceOutboundInterface=ethernet1/11 cs6=Panorama_LOF cs6Label=LogSetting cn1=595456 cn1Label=SessionID cnt=1 spt=52066 dpt=443 sourceTranslatedPort=47252 destinationTranslatedPort=443 proto=tcp act=allow PanOSBytes=12503 out=5651 in=6852 cn2=24 cn2Label=PacketsTotal PanOSSessionStartTime=Jul 31 2022 12:43:06 cn3=178 cn3Label=SessionDuration cs2=computer-and-internet-info cs2Label=URLCategory externalId=1111111111111111111 PanOSSourceLocation=10.0.0.0-10.255.255.255 PanOSDestinationLocation=UK PanOSPacketsSent=13 PanOSPacketsReceived=11 reason=tcp-fin PanOSDGHierarchyLevel1=997 PanOSDGHierarchyLevel2=738 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=LF-5698-NR cat=from-policy PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStarttime=Jan 01 1970 00:00:00 PanOSTunnel=N/A PanOSEndpointAssociationID=0 PanOSChunksTotal=0 PanOSChunksSent=0 PanOSChunksReceived=0 PanOSRuleUUID=2e259acc-c7ce-43d0-857f-f1a457e02699 PanOSHTTP2Connection=0 PanOSLinkChangeCount=0 PanOSSDWANPolicyName= PanOSLinkSwitches= PanOSSDWANCluster= PanOSSDWANDeviceType= PanOSSDWANClusterType= PanOSSDWANSite= PanOSDynamicUserGroupName= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceHost= PanOSSourceDeviceMac= PanOSDestinationDeviceCategory= PanOSDestinationDeviceProfile= PanOSDestinationDeviceModel= PanOSDestinationDeviceVendor= PanOSDestinationDeviceOSFamily= PanOSDestinationDeviceOSVersion= PanOSDestinationDeviceHost= PanOSDestinationDeviceMac= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSGPHostID= PanOSEndpointSerialNumber= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSHASessionOwner= PanOSTimeGeneratedHighResolution=Jul 31 2022 12:46:07 PanOSNSSAINetworkSliceType= PanOSNSSAINetworkSliceDifferentiator=\n",
        "event": {
            "start": "2022-07-31T12:46:07.000000Z",
            "action": "allow",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "traffic",
            "duration": 178,
            "kind": "event",
            "reason": "tcp-fin",
            "type": [
                "allowed"
            ],
            "severity": 3
        },
        "@timestamp": "2022-07-31T12:46:24.000000Z",
        "destination": {
            "address": "5.6.7.8",
            "bytes": 5651,
            "geo": {
                "country_iso_code": "UK"
            },
            "ip": "5.6.7.8",
            "nat": {
                "ip": "8.7.6.5",
                "port": 443
            },
            "packets": 11,
            "port": 443
        },
        "host": {
            "hostname": "LF-5698-NR",
            "name": "LF-5698-NR",
            "id": "000000000000"
        },
        "log": {
            "hostname": "LF-5698-NR",
            "logger": "traffic"
        },
        "network": {
            "application": "outlook-web-online",
            "bytes": 12503,
            "packets": 24,
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "Untrust",
                    "name": "ethernet1/11",
                    "id": "11"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "Trust",
                    "name": "0",
                    "id": "11"
                }
            },
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "rule": {
            "name": "SO Access",
            "uuid": "2e259acc-c7ce-43d0-857f-f1a457e02699"
        },
        "source": {
            "address": "1.2.3.4",
            "bytes": 6852,
            "ip": "1.2.3.4",
            "nat": {
                "ip": "4.3.2.1",
                "port": 47252
            },
            "packets": 13,
            "port": 52066
        },
        "paloalto": {
            "PanOSSourceLocation": "10.0.0.0-10.255.255.255",
            "PanOSSessionStartTime": "Jul 31 2022 12:43:06",
            "URLCategory": "computer-and-internet-info"
        },
        "related": {
            "hosts": [
                "LF-5698-NR"
            ],
            "ip": [
                "1.2.3.4",
                "4.3.2.1",
                "5.6.7.8",
                "8.7.6.5"
            ]
        }
    }
    	
	```


=== "traffic2_csv.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|TRAFFIC|end|3|dtz=UTC rt=Aug 02 2022 06:42:20 deviceExternalId=no-serial PanOSConfigVersion=10.0 start=Aug 02 2022 06:42:01 src= dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=Global_Outbound_internet_access cs1Label=Rule suser=user.name@corp.com duser= app=ssl cs3=vsys1 cs3Label=VirtualLocation cs4=trust cs4Label=FromZone cs5=untrust cs5Label=ToZone deviceInboundInterface=tunnel.1 deviceOutboundInterface=ethernet1/1 cs6=default cs6Label=LogSetting cn1=689028 cn1Label=SessionID cnt=1 spt=63516 dpt=443 sourceTranslatedPort=43823 destinationTranslatedPort=443 proto=tcp act=allow PanOSBytes=13443 out=2755 in=10688 cn2=32 cn2Label=PacketsTotal PanOSSessionStartTime=Aug 02 2022 06:41:44 cn3=0 cn3Label=SessionDuration cs2=low-risk cs2Label=URLCategory externalId=1112030318 PanOSSourceLocation=10.0.0.0-10.255.255.255 PanOSDestinationLocation=EU PanOSPacketsSent=13 PanOSPacketsReceived=19 reason=tcp-fin PanOSDGHierarchyLevel1=463 PanOSDGHierarchyLevel2=467 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=GP cloud service cat=from-policy PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStarttime=Jan 01 1970 00:00:00 PanOSTunnel=N/A PanOSEndpointAssociationID=0 PanOSChunksTotal=0 PanOSChunksSent=0 PanOSChunksReceived=0 PanOSRuleUUID=c38e111b-43fc-4de4-a17c-c372af557193 PanOSHTTP2Connection=0 PanOSLinkChangeCount=0 PanOSSDWANPolicyName= PanOSLinkSwitches= PanOSSDWANCluster= PanOSSDWANDeviceType= PanOSSDWANClusterType= PanOSSDWANSite= PanOSDynamicUserGroupName= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory= PanOSSourceDeviceProfile= PanOSSourceDeviceModel= PanOSSourceDeviceVendor= PanOSSourceDeviceOSFamily= PanOSSourceDeviceOSVersion= PanOSSourceDeviceHost= PanOSSourceDeviceMac= PanOSDestinationDeviceCategory= PanOSDestinationDeviceProfile= PanOSDestinationDeviceModel= PanOSDestinationDeviceVendor= PanOSDestinationDeviceOSFamily= PanOSDestinationDeviceOSVersion= PanOSDestinationDeviceHost= PanOSDestinationDeviceMac= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSGPHostID= PanOSEndpointSerialNumber= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSHASessionOwner= PanOSTimeGeneratedHighResolution=Aug 02 2022 06:42:02 PanOSNSSAINetworkSliceType= PanOSNSSAINetworkSliceDifferentiator=",
        "event": {
            "start": "2022-08-02T06:42:01.000000Z",
            "action": "allow",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "traffic",
            "duration": 0,
            "kind": "event",
            "reason": "tcp-fin",
            "type": [
                "allowed"
            ],
            "severity": 3
        },
        "@timestamp": "2022-08-02T06:42:20.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "bytes": 2755,
            "geo": {
                "country_iso_code": "EU"
            },
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 443
            },
            "packets": 19,
            "port": 443
        },
        "host": {
            "hostname": "GP cloud service",
            "name": "GP cloud service",
            "id": "no-serial"
        },
        "log": {
            "hostname": "GP cloud service",
            "logger": "traffic"
        },
        "network": {
            "application": "ssl",
            "bytes": 13443,
            "packets": 32,
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "untrust",
                    "name": "ethernet1/1",
                    "id": "1"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "trust",
                    "name": "1",
                    "id": "1"
                }
            },
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "rule": {
            "name": "Global_Outbound_internet_access",
            "uuid": "c38e111b-43fc-4de4-a17c-c372af557193"
        },
        "source": {
            "bytes": 10688,
            "nat": {
                "ip": "1.1.1.1",
                "port": 43823
            },
            "packets": 13,
            "port": 63516,
            "user": {
                "name": "user.name@corp.com"
            }
        },
        "user": {
            "name": "user.name@corp.com"
        },
        "paloalto": {
            "PanOSSourceLocation": "10.0.0.0-10.255.255.255",
            "PanOSSessionStartTime": "Aug 02 2022 06:41:44",
            "URLCategory": "low-risk"
        },
        "related": {
            "hosts": [
                "GP cloud service"
            ],
            "ip": [
                "1.1.1.1"
            ],
            "user": [
                "user.name@corp.com"
            ]
        }
    }
    	
	```


=== "traffic_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|TRAFFIC|end|3|ProfileToken=xxxxx dtz=UTC rt=Feb 27 2021 20:16:21 deviceExternalId=xxxxxxxxxxxxx PanOSApplicationContainer= PanOSApplicationRisk=5 PanOSApplicationSubcategory=file-sharing PanOSApplicationTechnology=peer-to-peer PanOSCaptivePortal=false PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceOS= dntdom=paloaltonetwork duser=xxxxx duid= PanOSInboundInterfaceDetailsPort=0 PanOSInboundInterfaceDetailsSlot=0 PanOSInboundInterfaceDetailsType=unknown PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer=false PanOSIsContainer=false PanOSIsDecryptMirror=false PanOSIsDecrypted=false PanOSIsDecryptedLog=false PanOSIsDecryptedPayloadForward=false PanOSIsDuplicateLog=false PanOSIsEncrypted=false PanOSIsIPV6=false PanOSIsInspectionBeforeSession=true PanOSIsMptcpOn=false PanOSIsNonStandardDestinationPort=false PanOSIsPacketCapture=false PanOSIsPhishing=false PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy=false PanOSIsReconExcluded=false PanOSIsSaaSApplication=false PanOSIsServertoClient=false PanOSIsSourceXForwarded=false PanOSIsSystemReturn=false PanOSIsTransaction=false PanOSIsTunnelInspected=false PanOSIsURLDenied=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT=false PanOSNonStandardDestinationPort=0 PanOSOutboundInterfaceDetailsPort=0 PanOSOutboundInterfaceDetailsSlot=0 PanOSOutboundInterfaceDetailsType=unknown PanOSOutboundInterfaceDetailsUnit=0 PanOSSDWANFECRatio=0.0 PanOSSanctionedStateOfApp=false PanOSSessionOwnerMidx=false PanOSSessionTracker=16 PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom=xxxxx suser=xxxxx xxxxx suid= PanOSTunneledApplication=tunneled-app PanOSUsers=xxxxx\\\\xxxxx xxxxx PanOSVirtualSystemID=1 PanOSApplicationCategory=peer2peer PanOSConfigVersion=10.0 start=Feb 27 2021 20:16:17 src=1.1.1.1 dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=deny-attackers cs1Label=Rule suser0=xxxxx\\\\xxxxx xxxxx duser0=paloaltonetwork\\\\xxxxx app=fileguri cs3=vsys1 cs3Label=VirtualLocation cs4=untrust cs4Label=FromZone cs5=ethernet4Zone-test1 cs5Label=ToZone deviceInboundInterface=unknown deviceOutboundInterface=unknown cs6=rs-logging cs6Label=LogSetting cn1=25596 cn1Label=SessionID cnt=1 spt=22871 dpt=27092 sourceTranslatedPort=24429 destinationTranslatedPort=14744 proto=tcp act=deny PanOSBytes=1370294 out=400448 in=969846 cn2=314 cn2Label=PacketsTotal PanOSSessionStartTime=Feb 27 2021 20:15:48 cn3=56 cn3Label=SessionDuration cs2=custom-category cs2Label=URLCategory externalId=xxxxxxxxxxxxx PanOSSourceLocation=east-coast PanOSDestinationLocation=BR PanOSPacketsSent=194 PanOSPacketsReceived=120 reason=unknown PanOSDGHierarchyLevel1=11 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=xxxxx cat=unknown PanOSSourceUUID= PanOSDestinationUUID= PanOSIMSI=0 PanOSIMEI= PanOSParentSessionID=0 PanOSParentStarttime=Feb 27 2021 20:15:40 PanOSTunnel=GRE PanOSEndpointAssociationID=-3746994889972252628 PanOSChunksTotal=1945 PanOSChunksSent=323 PanOSChunksReceived=1622 PanOSRuleUUID=017e4d76-2003-47f4-8afc-1d35c808c615 PanOSHTTP2Connection=469139 PanOSLinkChangeCount=0 PanOSSDWANPolicyName= PanOSLinkSwitches= PanOSSDWANCluster= PanOSSDWANDeviceType= PanOSSDWANClusterType= PanOSSDWANSite= PanOSDynamicUserGroupName=dynug-4 PanOSX-Forwarded-ForIP=1.1.1.1 PanOSSourceDeviceCategory=N-Phone PanOSSourceDeviceProfile=n-profile PanOSSourceDeviceModel=Nexus PanOSSourceDeviceVendor=Google PanOSSourceDeviceOSFamily=LG-H790 PanOSSourceDeviceOSVersion=Android v6 PanOSSourceDeviceHost=pan-301 PanOSSourceDeviceMac=839147449905 PanOSDestinationDeviceCategory=N-Phone PanOSDestinationDeviceProfile=n-profile PanOSDestinationDeviceModel=Nexus PanOSDestinationDeviceVendor=Google PanOSDestinationDeviceOSFamily=H1511 PanOSDestinationDeviceOSVersion=Android v7 PanOSDestinationDeviceHost=pan-355 PanOSDestinationDeviceMac=530589561221 PanOSContainerID=1873cc5c-0d31 PanOSContainerNameSpace=pns_default PanOSContainerName=pan-dp-77754f4 PanOSSourceEDL= PanOSDestinationEDL= PanOSGPHostID=xxxxxxxxxxxxxx PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSSourceDynamicAddressGroup= aqua_dag PanOSDestinationDynamicAddressGroup= PanOSHASessionOwner=session_owner-4 PanOSTimeGeneratedHighResolution=Feb 27 2021 20:16:18 PanOSNSSAINetworkSliceType=0 PanOSNSSAINetworkSliceDifferentiator=1bca5",
        "event": {
            "start": "2021-02-27T20:16:17.000000Z",
            "action": "deny",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "traffic",
            "duration": 56,
            "kind": "event",
            "reason": "unknown",
            "type": [
                "denied"
            ],
            "severity": 3
        },
        "@timestamp": "2021-02-27T20:16:21.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "bytes": 400448,
            "geo": {
                "country_iso_code": "BR"
            },
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 14744
            },
            "packets": 120,
            "port": 27092,
            "user": {
                "name": "xxxxx"
            }
        },
        "host": {
            "hostname": "xxxxx",
            "name": "xxxxx",
            "id": "xxxxxxxxxxxxx",
            "mac": "839147449905",
            "os": {
                "family": "LG-H790",
                "version": "Android v6"
            },
            "type": "N-Phone"
        },
        "log": {
            "hostname": "xxxxx",
            "logger": "traffic"
        },
        "network": {
            "application": "fileguri",
            "bytes": 1370294,
            "packets": 314,
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "ethernet4Zone-test1",
                    "name": "unknown",
                    "id": "unknown"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "untrust",
                    "name": "n",
                    "id": "unknown"
                }
            },
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "rule": {
            "name": "deny-attackers",
            "uuid": "017e4d76-2003-47f4-8afc-1d35c808c615"
        },
        "source": {
            "address": "1.1.1.1",
            "bytes": 969846,
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 24429
            },
            "packets": 194,
            "port": 22871,
            "user": {
                "name": "xxxxx xxxxx"
            }
        },
        "user": {
            "name": "xxxxx xxxxx"
        },
        "paloalto": {
            "PanOSHASessionOwner": "session_owner-4",
            "PanOSSourceDynamicAddressGroup": " aqua_dag",
            "PanOSEndpointSerialNumber": "xxxxxxxxxxxxxx",
            "PanOSGPHostID": "xxxxxxxxxxxxxx",
            "PanOSContainerName": "pan-dp-77754f4",
            "PanOSContainerNameSpace": "pns_default",
            "PanOSDestinationDeviceMac": "530589561221",
            "PanOSDestinationDeviceHost": "pan-355",
            "PanOSDestinationDeviceOSVersion": "Android v7",
            "PanOSDestinationDeviceOSFamily": "H1511",
            "PanOSDestinationDeviceVendor": "Google",
            "PanOSDestinationDeviceModel": "Nexus",
            "PanOSDestinationDeviceProfile": "n-profile",
            "PanOSDestinationDeviceCategory": "N-Phone",
            "PanOSSourceDeviceHost": "pan-301",
            "PanOSSourceDeviceVendor": "Google",
            "PanOSSourceDeviceModel": "Nexus",
            "PanOSSourceDeviceProfile": "n-profile",
            "PanOSX-Forwarded-ForIP": "1.1.1.1",
            "PanOSSourceLocation": "east-coast",
            "PanOSSessionStartTime": "Feb 27 2021 20:15:48",
            "URLCategory": "custom-category"
        },
        "related": {
            "hosts": [
                "xxxxx"
            ],
            "user": [
                "xxxxx",
                "xxxxx xxxxx"
            ],
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```


=== "udp_deny_csv.json"

    ```json
	
    {
        "message": "<14>Sep 16 10:00:00 PA 1,9/16/19 10:00,1801017000,TRAFFIC,deny,2049,9/16/19 10:00,10.0.0.2,1.2.3.4,5.4.4.3,5.4.3.2,DENYALL,,,protection,vsys1,DNS,AAAAA,ae2.503,ethernet1/1,Secure,9/16/19 10:00,11111,1,130000,53,6379,53,0x400000,udp,reset-both,284,284,0,1,9/16/19 10:00,0,any,0,50660381851,0x0,10.0.0.0-10.255.255.255,Spain,0,1,0,policy-deny,0,0,0,0,,PA-1,from-application,,,0,,0,,N/A,0,0,0,0",
        "event": {
            "category": [
                "network"
            ],
            "duration": 0,
            "kind": "event",
            "type": [
                "denied"
            ]
        },
        "action": {
            "name": "reset-both",
            "type": "deny",
            "outcome": "success"
        },
        "destination": {
            "address": "1.2.3.4",
            "bytes": 0,
            "ip": "1.2.3.4",
            "nat": {
                "ip": "5.4.3.2",
                "port": 53
            },
            "packets": 0,
            "port": 53
        },
        "log": {
            "logger": "traffic"
        },
        "network": {
            "bytes": 284,
            "packets": 1,
            "transport": "udp"
        },
        "observer": {
            "product": "PAN-OS"
        },
        "rule": {
            "name": "DENYALL"
        },
        "source": {
            "address": "10.0.0.2",
            "bytes": 284,
            "ip": "10.0.0.2",
            "nat": {
                "ip": "5.4.4.3",
                "port": 6379
            },
            "packets": 1,
            "port": 130000
        },
        "paloalto": {
            "Threat_ContentType": "deny"
        },
        "related": {
            "ip": [
                "1.2.3.4",
                "10.0.0.2",
                "5.4.3.2",
                "5.4.4.3"
            ]
        }
    }
    	
	```


=== "url_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|THREAT|url|1|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 20:48:21 deviceExternalId=xxxxxxxxxxxxx PanOSApplicationCategory=database PanOSApplicationContainer= PanOSApplicationRisk=2 PanOSApplicationSubcategory=database PanOSApplicationTechnology=client-server PanOSCaptivePortal=false PanOSCloudHostname=xxxxx PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceOS= dntdom=xxxxx duser=xxxxx o\"'\"test duid= PanOSHTTPRefererFQDN= PanOSHTTPRefererPort= PanOSHTTPRefererProtocol= PanOSHTTPRefererURLPath= PanOSInboundInterfaceDetailsPort=0 PanOSInboundInterfaceDetailsSlot=0 PanOSInboundInterfaceDetailsType=unknown PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer=true PanOSIsContainer=false PanOSIsDecryptMirror=false PanOSIsDecrypted=false PanOSIsDuplicateLog=false PanOSIsEncrypted=false PanOSIsIPV6=false PanOSIsMptcpOn=false PanOSIsNonStandardDestinationPort=false PanOSIsPacketCapture=false PanOSIsPhishing=false PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy=false PanOSIsReconExcluded=false PanOSIsSaaSApplication=false PanOSIsServertoClient=false PanOSIsSourceXForwarded=true PanOSIsSystemReturn=true PanOSIsTransaction=false PanOSIsTunnelInspected=false PanOSIsURLDenied=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT=false PanOSNonStandardDestinationPort=32350 PanOSOutboundInterfaceDetailsPort=2 PanOSOutboundInterfaceDetailsSlot=1 PanOSOutboundInterfaceDetailsType=ethernet PanOSOutboundInterfaceDetailsUnit=0 PanOSPacket= PanOSSanctionedStateofApp=false PanOSSeverity=Informational PanOSSourceDeviceClass= PanOSSourceDeviceOS= sntdom=xxxxx suser=xxxxx xxxxx suid= PanOSTunneledApplication=untunneled PanOSURLDomain=?% PanOSUsers=xxxxx\\\\xxxxx xxxxx PanOSVirtualSystemID=1 PanOSConfigVersion=10.0 start=Mar 01 2021 20:48:16 src=1.1.1.1 dst=1.1.1.1 sourceTranslatedAddress=1.1.1.1 destinationTranslatedAddress=1.1.1.1 cs1=allow-business-apps cs1Label=Rule suser0=xxxxx\\\\xxxxx xxxxx duser0=xxxxx\\\\xxxxx o\"'\"test app=maxdb cs3=vsys1 cs3Label=VirtualLocation cs4=ethernet4Zone-test4 cs4Label=FromZone cs5=untrust cs5Label=ToZone deviceInboundInterface=unknown deviceOutboundInterface=ethernet1/2 cs6=rs-logging cs6Label=LogSetting cn1=980296 cn1Label=SessionID cnt=1 spt=32350 dpt=1532 sourceTranslatedPort=26236 destinationTranslatedPort=12016 proto=tcp act=block-url request=?% cs2=sports cs2Label=URLCategory flexString2=server to client flexString2Label=DirectionOfAttack externalId=xxxxxxxxxxxxx PanOSSourceLocation=west-coast PanOSDestinationLocation=PK requestContext=application/jpeg fileId=0 PanOSURLCounter=1 requestClientApplication= PanOSX-Forwarded-For= PanOSReferer= PanOSDGHierarchyLevel1=11 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=xxxxx PanOSSourceUUID= PanOSDestinationUUID= requestMethod=post PanOSIMSI=1 PanOSIMEI=Navy Base PanOSParentSessionID=8802 PanOSParentStarttime=Mar 01 2021 20:48:10 PanOSTunnel=VXLAN PanOSInlineMLVerdict=overflow PanOSContentVersion=50222 PanOSSigFlags=2 PanOSHTTPHeaders= PanOSURLCategoryList=sports,\u200b11008,\u200b38340 PanOSRuleUUID=ec14df0b-c845-4435-87a2-d207730f5ae8 PanOSHTTP2Connection=8802 PanOSDynamicUserGroupName= PanOSX-Forwarded-ForIP= PanOSSourceDeviceCategory=L-Phone PanOSSourceDeviceProfile=l-profile PanOSSourceDeviceModel=Note 4G PanOSSourceDeviceVendor=Lenovo PanOSSourceDeviceOSFamily=K6 PanOSSourceDeviceOSVersion=Android v9 PanOSSourceDeviceHost=pan-505 PanOSSourceDeviceMac=596703749274 PanOSDestinationDeviceCategory=L-Phone PanOSDestinationDeviceProfile=l-profile PanOSDestinationDeviceModel=Note XT PanOSDestinationDeviceVendor=Lenovo PanOSDestinationDeviceOSFamily=K8 PanOSDestinationDeviceOSVersion=Android v8 PanOSDestinationDeviceHost=pan-506 PanOSDestinationDeviceMac=150083646537 PanOSContainerID=1873cc5c-0d31 PanOSContainerNameSpace=pns_default PanOSContainerName=pan-dp-77754f4 PanOSSourceEDL= PanOSDestinationEDL= PanOSHostID=xxxxxxxxxxxxxx PanOSEndpointSerialNumber=xxxxxxxxxxxxxx PanOSSourceDynamicAddressGroup= blue_dag PanOSDestinationDynamicAddressGroup= PanOSTimeGeneratedHighResolution=Mar 01 2021 20:48:16 PanOSNSSAINetworkSliceType=b5",
        "event": {
            "start": "2021-03-01T20:48:16.000000Z",
            "action": "block-url",
            "category": [
                "network"
            ],
            "timezone": "UTC",
            "dataset": "threat",
            "kind": "event",
            "type": [
                "info"
            ],
            "severity": 1
        },
        "@timestamp": "2021-03-01T20:48:21.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "geo": {
                "country_iso_code": "PK"
            },
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 12016
            },
            "port": 1532,
            "user": {
                "name": "xxxxx o\"'\"test"
            }
        },
        "host": {
            "hostname": "xxxxx",
            "name": "xxxxx",
            "id": "xxxxxxxxxxxxx",
            "mac": "596703749274",
            "os": {
                "family": "K6",
                "version": "Android v9"
            },
            "type": "L-Phone"
        },
        "log": {
            "hostname": "xxxxx",
            "logger": "threat"
        },
        "network": {
            "application": "maxdb",
            "transport": "tcp"
        },
        "observer": {
            "egress": {
                "interface": {
                    "alias": "untrust",
                    "name": "ethernet1/2",
                    "id": "2"
                }
            },
            "ingress": {
                "interface": {
                    "alias": "ethernet4Zone-test4",
                    "name": "n",
                    "id": "2"
                }
            },
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "rule": {
            "name": "allow-business-apps",
            "uuid": "ec14df0b-c845-4435-87a2-d207730f5ae8"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "nat": {
                "ip": "1.1.1.1",
                "port": 26236
            },
            "port": 32350,
            "user": {
                "name": "xxxxx xxxxx"
            }
        },
        "user": {
            "name": "xxxxx xxxxx"
        },
        "paloalto": {
            "PanOSSourceDynamicAddressGroup": " blue_dag",
            "PanOSEndpointSerialNumber": "xxxxxxxxxxxxxx",
            "PanOSContainerName": "pan-dp-77754f4",
            "PanOSContainerNameSpace": "pns_default",
            "PanOSDestinationDeviceMac": "150083646537",
            "PanOSDestinationDeviceHost": "pan-506",
            "PanOSDestinationDeviceOSVersion": "Android v8",
            "PanOSDestinationDeviceOSFamily": "K8",
            "PanOSDestinationDeviceVendor": "Lenovo",
            "PanOSDestinationDeviceModel": "Note XT",
            "PanOSDestinationDeviceProfile": "l-profile",
            "PanOSDestinationDeviceCategory": "L-Phone",
            "PanOSSourceDeviceHost": "pan-505",
            "PanOSSourceDeviceVendor": "Lenovo",
            "PanOSSourceDeviceModel": "Note 4G",
            "PanOSSourceDeviceProfile": "l-profile",
            "PanOSSourceLocation": "west-coast",
            "URLCategory": "sports"
        },
        "related": {
            "hosts": [
                "xxxxx"
            ],
            "user": [
                "xxxxx o\"'\"test",
                "xxxxx xxxxx"
            ],
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```


=== "userid_cef.json"

    ```json
	
    {
        "message": "CEF:0|Palo Alto Networks|LF|2.0|USERID|logout|3|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:06:02 deviceExternalId=xxxxxxxxxxxxx PanOSConfigVersion= dntdom=paloaltonetwork duser=xxxxx duid= PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSIsDuplicateLog=false PanOSIsDuplicateUser= PanOSIsPrismaNetworks=false PanOSIsPrismaUsers=false PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSUserGroupFound= start=Mar 01 2021 21:06:02 cs3=vsys1 cs3Label=VirtualLocation src=1.1.1.1 dst=1.1.1.1 duser0=paloaltonetworks\\\\xxxxx cs4=fake-data-source-169 cs4Label=MappingDataSourceName cat=0 cnt=1 cn3=3531 cn3Label=MappingTimeout spt=21015 dpt=49760 cs5=probing cs5Label=MappingDataSource cs6=netbios_probing cs6Label=MappingDataSourceType externalId=xxxxxxxxxxxxx PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 cn2=1 cn2Label=VirtualSystemID cs1=xxxxx cs1Label=MFAFactorType end=Jul 09 2019 18:15:44 cn1=3 cn1Label=AuthFactorNo PanOSUGFlags=0x100 PanOSUserIdentifiedBySource=xxxxxxxxxxxxxx PanOSTag= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12",
        "event": {
            "start": "2021-03-01T21:06:02.000000Z",
            "timezone": "UTC",
            "dataset": "userid",
            "kind": "event",
            "category": [
                "authentication"
            ],
            "type": [
                "end"
            ],
            "severity": 3
        },
        "@timestamp": "2021-03-01T21:06:02.000000Z",
        "destination": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 49760,
            "user": {
                "name": "xxxxx"
            }
        },
        "host": {
            "hostname": "PA-5220",
            "name": "PA-5220",
            "id": "xxxxxxxxxxxxx"
        },
        "log": {
            "hostname": "PA-5220",
            "logger": "userid"
        },
        "observer": {
            "product": "PAN-OS",
            "vendor": "Palo Alto Networks",
            "type": "LF",
            "version": "2.0"
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1",
            "port": 21015
        },
        "paloalto": {},
        "related": {
            "hosts": [
                "PA-5220"
            ],
            "user": [
                "xxxxx"
            ],
            "ip": [
                "1.1.1.1"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`destination.address` | `keyword` | Destination network address. |
|`destination.bytes` | `long` | Bytes sent from the destination to the source. |
|`destination.geo.country_iso_code` | `keyword` | Country ISO code. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.nat.ip` | `ip` | Destination NAT ip |
|`destination.nat.port` | `long` | Destination NAT Port |
|`destination.packets` | `long` | Packets sent from the destination to the source. |
|`destination.port` | `long` | Port of the destination. |
|`destination.user.name` | `keyword` | Short name or login of the user. |
|`email.from.address` | `keyword` | Email address from |
|`email.subject` | `keyword` | Subject |
|`email.to.address` | `keyword` | Email address to |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.dataset` | `keyword` | Name of the dataset. |
|`event.duration` | `long` | Duration of the event in nanoseconds. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.severity` | `long` | Numeric severity of the event. |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.timezone` | `keyword` | Event time zone. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.id` | `keyword` | Unique host id. |
|`host.mac` | `keyword` | Host MAC addresses. |
|`host.name` | `keyword` | Name of the host. |
|`host.os.family` | `keyword` | OS family (such as redhat, debian, freebsd, windows). |
|`host.os.type` | `keyword` | Which commercial OS family (one of: linux, macos, unix or windows). |
|`host.os.version` | `keyword` | Operating system version as a raw string. |
|`host.type` | `keyword` | Type of host. |
|`http.request.method` | `keyword` | HTTP request method. |
|`http.request.referrer` | `keyword` | Referrer for this HTTP request. |
|`log.level` | `keyword` | Log level of the log event. |
|`log.logger` | `keyword` | Name of the logger. |
|`network.application` | `keyword` | Application level protocol name. |
|`network.bytes` | `long` | Total bytes transferred in both directions. |
|`network.packets` | `long` | Total packets transferred in both directions. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`network.type` | `keyword` | In the OSI Model this would be the Network Layer. ipv4, ipv6, ipsec, pim, etc |
|`observer.egress.interface.alias` | `keyword` | Interface alias |
|`observer.egress.interface.id` | `keyword` | Interface ID |
|`observer.egress.interface.name` | `keyword` | Interface name |
|`observer.ingress.interface.alias` | `keyword` | Interface alias |
|`observer.ingress.interface.id` | `keyword` | Interface ID |
|`observer.ingress.interface.name` | `keyword` | Interface name |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`observer.version` | `keyword` | Observer version. |
|`paloalto.Threat_ContentType` | `keyword` | Type associated with the threat |
|`rule.name` | `keyword` | Rule name |
|`rule.uuid` | `keyword` | Rule UUID |
|`source.bytes` | `long` | Bytes sent from the source to the destination. |
|`source.geo.country_iso_code` | `keyword` | Country ISO code. |
|`source.ip` | `ip` | IP address of the source. |
|`source.nat.ip` | `ip` | Source NAT ip |
|`source.nat.port` | `long` | Source NAT port |
|`source.packets` | `long` | Packets sent from the source to the destination. |
|`source.port` | `long` | Port of the source. |
|`source.user.name` | `keyword` | Short name or login of the user. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.name` | `keyword` | Name of the user agent. |
|`user_agent.os.name` | `keyword` | Operating system name, without the version. |
|`user_agent.os.version` | `keyword` | Operating system version as a raw string. |

