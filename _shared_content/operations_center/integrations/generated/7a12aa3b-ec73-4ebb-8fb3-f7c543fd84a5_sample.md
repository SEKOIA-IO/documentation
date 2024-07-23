
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "host_checker_policy_failed"

    ```
	id=firewall time="2021-01-28 13:46:08" pri=6 fw=172.16.128.22 vpn=CB2XXPCS02 ivs=Root user=bob realm="SEKOIA_User" roles="VDI-Pulse_User_Role" proto=auth src=176.134.164.62 dst= dstname= type=vpn op= arg="" result= sent= rcvd= agent="" duration= msg="AUT24804: Host Checker policy 'Sekoia_Host Checker' failed on host '176.134.164.62' address '00-d8-61-35-80-81' for user 'bob' reason 'Rule-Antivirus_Check:Le logiciel antivirus indiqué dans les exigences de sécurité n'est pas installé.'."
    ```



=== "host_checker_policy_success"

    ```
	id=firewall time="2021-01-28 13:46:05" pri=6 fw=172.16.128.22 vpn=CB2XXPCS02 ivs=Root user=alice realm="SEKOIA_User" roles="SEKOIA_User_Role" proto=auth src=19.160.74.9 dst= dstname= type=vpn op= arg="" result= sent= rcvd= agent="" duration= msg="AUT24803: Host Checker policy 'Sekoia_Host Checker' passed on host '19.160.74.9' address '60-f2-62-ea-2d-a1' for user 'alice'."
    ```



=== "login_failed"

    ```
	id=firewall time="2021-01-28 14:14:04" pri=6 fw=172.16.128.22 vpn=CB2XXPCS02 ivs=Default Network user=bob realm="SEKOIA_User" roles="" proto=auth src=176.168.192.159 dst= dstname= type=vpn op= arg="" result= sent= rcvd= agent="" duration= msg="AUT23457: Login failed using auth server RSA (ACE Server).  Reason: Failed"
    ```



=== "test_event_aut20920"

    ```
	id=firewall time="2023-10-17 10:21:15" pri=6 fw=3.4.5.6 vpn=EX023-V6 user=MYDomain\\johndoe realm="Example" roles="Example_Sales" type=mgmt proto=auth src=1.2.3.4 dst= dstname= sent= rcvd= msg="AUT20920: Connection from IP 1.2.3.4 not authenticated yet (URL=/cgi/pal?tm=26&key=1234567890)"

    ```



=== "test_event_aut24604"

    ```
	id=firewall time="2023-10-17 10:21:14" pri=4 fw=3.4.5.6 vpn=EX023-V6 user=System realm="" roles="" type=mgmt proto= src=1.2.3.4 dst= dstname= sent= rcvd= msg="AUT24604: SSL negotiation failed while client at source IP '1.2.3.4' was trying to connect to '5.6.7.8'. Reason: 'sslv3 alert bad certificate'"


    ```



=== "test_event_lic30499"

    ```
	id=firewall time="2023-10-17 18:18:12" pri=6 fw=3.4.5.6 vpn=EX023-V6 ivs=Root user=System realm="" roles="" type=mgmt proto= src=1.2.3.4 dst= dstname= sent= rcvd= msg="LIC30499: Leased 0 units of 'Virtual CPUs' from 1.2.3.4 - reserved: 0 maximum: 0 incremental quantum: 0"

    ```



=== "test_event_sys20704"

    ```
	id=firewall time="2023-10-17 10:19:03" pri=0 fw=3.4.5.6 vpn=EX023-V6 user=System realm="" roles="" type=mgmt proto= src=1.2.3.4 dst= dstname= sent= rcvd= msg="SYS20704: Sending iveLogNearlyFull [ logFullPercent='93' logName='event' ] SNMP trap to 5.6.7.8:162"

    ```



=== "test_event_sys31231"

    ```
	id=firewall time="2023-10-17 18:18:16" pri=6 fw=3.4.5.6 vpn=EX023-V6 ivs=Default Network user=System realm="" roles="" type=mgmt proto= src=1.2.3.4 dst= dstname= sent= rcvd= msg="SYS31231: Successfully executed 'Post Settings Request'."

    ```



=== "test_event_sys31437"

    ```
	id=firewall time="2024-01-12 23:00:22" pri=6 fw=8.8.8.8 vpn=EX023-V6 user=System realm="" roles="" type=mgmt proto= src=1.2.3.4 dst= dstname= sent= rcvd= msg="SYS31437: Successful syslog connection to peer: '3.4.5.6'"
    ```



=== "test_event_sys32083"

    ```
	id=firewall time="2023-10-17 10:14:05" pri=6 fw=3.4.5.6 vpn=EX023-V6 user=System realm="" roles="" type=mgmt proto= src=1.2.3.4 dst= dstname= sent= rcvd= msg="SYS32083: LMDB shards usage stats shard: 0:1%   1:1%   2:1%   3:1%   4:1%   5:1%   6:1%   7:1%   8:1%   9:1%   a:1%   b:1%   c:1%   d:1%   e:1%   f:1%   "

    ```



=== "unauthenticated_request"

    ```
	id=firewall time="2021-03-04 17:05:15" pri=6 fw=172.16.128.22 vpn=CB2XXPCS02 ivs=Default Network user=System realm="" roles="" proto= src=93.19.66.118 dst= dstname= type=vpn op= arg="" result= sent= rcvd= agent="" duration= msg="AUT31556: Unauthenticated request url /dana/js?prot=1&svc=4 came from IP 93.19.66.118."
    ```



