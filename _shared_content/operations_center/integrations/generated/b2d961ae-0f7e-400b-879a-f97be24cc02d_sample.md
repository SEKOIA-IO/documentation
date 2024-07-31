
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "AgentAntiMalware"

    ```
	CEF:0|Trend Micro|Deep Security Agent|<Agent version>|4000000|Eicar_test_file|6|cn1=1 cn1Label=Host ID dvchost=hostname cn2=205 cn2Label=Quarantine File Size cs6=ContainerImageName | ContainerName | ContainerID cs6Label=Container filePath=C:\Users\trend\Desktop\eicar.exe act=Delete result=Delete msg=Realtime TrendMicroDsMalwareTarget=N/A TrendMicroDsMalwareTargetType=N/A TrendMicroDsFileMD5=44D88612FEA8A8F36DE82E1278ABB02F TrendMicroDsFileSHA1=3395856CE81F2B7382DEE72602F798B642F14140 TrendMicroDsFileSHA256=275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F TrendMicroDsDetectionConfidence=95 TrendMicroDsRelevantDetectionNames=Ransom_CERBER.BZC;Ransom_CERBER.C;Ransom_CRYPNISCA.SM
    ```



=== "ApacheDOS"

    ```
	CEF:0|Trend Micro|Deep Security Agent|20.0.677|1011466|Apache HTTP Server 'mod_sed' Denial Of Service Vulnerability (CVE-2022-30522)|6|cn1=318 cn1Label=Host ID dvchost=foo.bar.fr TrendMicroDsTenant=Primary TrendMicroDsTenantId=0 dmac=22:22:22:22:22:22 smac=11:11:11:11:11:11 TrendMicroDsFrameType=IP src=2.2.2.2 dst=1.1.1.1 in=0 cs3=DF 0 cs3Label=Fragmentation Bits proto=TCP spt=58407 dpt=443 cs2=ACK cs2Label=TCP Flags cnt=2 act=IDS:Reset cn3=0 cn3Label=DPI Packet Position cs5=0 cs5Label=DPI Stream Position  cs1="CVE-2022-30522" cs1Label=DPI Note cs6=0 cs6Label=DPI Flags


    ```



=== "ApplicationControl"

    ```
	CEF:0|Trend Micro|Deep Security Agent|10.2.229|6001200|AppControl detectOnly|6|cn1=202 cn1Label=Host ID dvc=192.168.33.128 TrendMicroDsTenant=Primary TrendMicroDsTenantId=0 fileHash=80D4AC182F97D2AB48EE4310AC51DA5974167C596D133D64A83107B9069745E0 suser=root suid=0 act=detectOnly filePath=/home/user1/Desktop/Directory1//heartbeatSync.sh fsize=20 aggregationType=0 repeatCount=1 cs1=notWhitelisted cs1Label=actionReason cs2=0CC9713BA896193A527213D9C94892D41797EB7C cs2Label=sha1 cs3=7EA8EF10BEB2E9876D4D7F7E5A46CF8D cs3Label=md5
    ```



=== "DeviceControl"

    ```
	CEF:0|Trend Micro|Deep Security Agent|50.0.1063|7000000|Device Control DeviceControl|6|cn1=1 cn1Label=Host ID dvchost=test-hostname TrendMicroDsTenant=tenantName TrendMicroDsTenantId=1 device=deviceName processName=processName1 fileName=/tmp/some_path2 vendor=vendorName serial=aaaa-bbbb-cccc model=modelName computerName=computerName domainName=computerDomain deviceType=0 permission=0
    ```



=== "FirewallEventLog"

    ```
	CEF:0|Trend Micro|Deep Security Agent|<Agent version>|20|Log for TCP Port 80|0|cn1=1 cn1Label=Host ID dvc=hostname act=Log dmac=00:50:56:F5:7F:47 smac=00:0C:29:EB:35:DE TrendMicroDsFrameType=IP src=192.168.126.150 dst=72.14.204.147 out=1019 cs3=DF MF cs3Label=Fragmentation Bits proto=TCP spt=49617 dpt=80 cs2=0x00 ACK PSH cs2Label=TCP Flags cnt=1 TrendMicroDsPacketData=AFB...
    ```



=== "IntegrityMonitoring"

    ```
	CEF:0|Trend Micro|Deep Security Agent|<Agent version>|30|New Integrity Monitoring Rule|6|cn1=1 cn1Label=Host ID dvchost=hostname act=updated filePath=c:\windows\message.dll suser=admin sproc=C:\Windows\System32\notepad.exe msg=lastModified,sha1,size
    ```



=== "IntrusionPrevention"

    ```
	CEF:0|Trend Micro|Deep Security Agent|<Agent version>|1001111|Test Intrusion Prevention Rule|3|cn1=1 cn1Label=Host ID dvchost=hostname dmac=00:50:56:F5:7F:47 smac=00:0C:29:EB:35:DE TrendMicroDsFrameType=IP src=192.168.126.150 dst=72.14.204.105 out=1093 cs3=DF MF cs3Label=Fragmentation Bits proto=TCP spt=49786 dpt=80 cs2=0x00 ACK PSH cs2Label=TCP Flags cnt=1 act=IDS:Reset cn3=10 cn3Label=Intrusion Prevention Packet Position cs5=10 cs5Label=Intrusion Prevention Stream Position cs6=8 cs6Label=Intrusion Prevention Flags TrendMicroDsPacketData=R0VUIC9zP3...
    ```



=== "LogInspection"

    ```
	CEF:0|Trend Micro|Deep Security Agent|<Agent version>|3002795|Microsoft Windows Events|8|cn1=1 cn1Label=Host ID dvchost=hostname cs1Label=LI Description cs1=Multiple Windows Logon Failures fname=Security src=127.0.0.1 duser=(no user) shost=WIN-RM6HM42G65V msg=WinEvtLog Security: AUDIT_FAILURE(4625): Microsoft-Windows-Security-Auditing: (no user): no domain: WIN-RM6HM42G65V: An account failed to log on. Subject: ..
    ```



=== "SystemEventLog"

    ```
	CEF:0|Trend Micro|Workload Security Manager|<Workload Security version>|600|User Signed In|3|src=10.52.116.160 suser=admin target=admin msg=User signed in from 2001:db8::5
    ```



=== "WebReputation"

    ```
	CEF:0|Trend Micro|Deep Security Agent|<Agent version>|5000000|WebReputation|5|cn1=1 cn1Label=Host ID dvchost=hostname request=example.com msg=Blocked By Admin
    ```



