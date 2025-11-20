
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "alarm1"

    ```
	time="2023-11-23 06:49:20" fw="SN12345678912345" tz=+0100 startime="2023-11-23 06:49:20" pri=4 confid=00 srcif="Ethernet4" srcifname="wan-interface" ipproto=tcp proto=unknown src=11.22.33.44 srcport=1234 srcmac=aa:bb:cc:dd:ee:ff dst=55.66.77.88 dstport=5678 dstportname=ephemeral_fw_tcp dstname=host_55.66.77.88 ipv=4 action=block msg="Protocole TCP invalide (packet too short)" class=protocol classification=0 alarmid=98 target=dst sensible=1 logtype="alarm"
    ```



=== "alarm2"

    ```
	time="2023-11-23 09:20:13" fw="SN12345678912345" tz=+0100 startime="2023-11-23 09:19:43" pri=4 msg="CRL download failed" class=system alarmid=56 repeat=3 logtype="alarm"
    ```



=== "auth"

    ```
	time="2023-11-14 16:27:30" fw="SN12345678912345" tz=+0100 startime="2023-11-14 16:27:30" user="john.doe" src=172.16.0.42 domain="sekoia.io" confid=0 ruleid=0 method="" totp="yes" error=0 msg="totp enrolment: user TOTP request registered" logtype="auth"
    ```



=== "auth2"

    ```
	id=firewall time="2025-04-22 16:05:17" fw="SN12345678912345" tz=+0200 startime="2025-04-22 16:05:17" src=1.2.3.4 user="admin" domain="" msg="SSH authentication success on the firewall" logtype="auth"
    ```



=== "auth3"

    ```
	id=firewall time="2025-04-23 12:03:28" fw="FWCLIENT" tz=+0200 startime="2025-04-23 12:03:28" src=192.168.1.1 user="admin" domain="" msg="SSH authentication success on the firewall" totp="no" logtype="auth"
    ```



=== "auth_failed"

    ```
	id=firewall time="2023-09-28 16:37:39" fw="SN12345678912345" tz=+0200 startime="2023-09-28 16:37:39" user="john.doe" src=11.22.33.44 domain="sekoia.io" confid=1 ruleid=0 method="OPENVPN" error=3 msg="Authentication Failed" logtype="auth"
    ```



=== "empty_action"

    ```
	time="2022-03-17 14:49:51" fw="SN12345678912345" tz=+0100 startime="2022-03-17 14:49:51" pri=5 confid=01 slotlevel=5 ruleid=48 srcif="Ethernet3" srcifname="in" ipproto=tcp dstif="Ethernet2" dstifname="out" proto=https src=55.66.77.88 srcport=39618 srcportname=ephemeral_fw_tcp srcname=WebProxy srcmac=00:00:00:00:00:00 dst=11.22.33.44 dstport=443 dstportname=https dstcontinent="na" dstcountry="us" ipv=4 sent=0 rcvd=0 duration=0.00 logtype="filter"
    ```



=== "filter"

    ```
	time="2022-03-03 14:21:10" fw="SN12345678912345" tz=+0100 startime="2022-03-03 14:21:10" pri=5 confid=01 slotlevel=2 ruleid=100 srcif="Ethernet3" srcifname="in" ipproto=tcp dstif="Ethernet2" dstifname="out" proto=https src=42.123.123.123 srcport=60355 srcportname=ad2009-dyn_tcp srcname=ADSERVER srcmac=00:00:00:00:00:00 dst=11.11.11.11 dstport=443 dstportname=https dstname=example_dest dstcontinent="na" dstcountry="us" ipv=4 sent=0 rcvd=0 duration=2.00 action=pass logtype="filter"
    ```



=== "filter2"

    ```
	time="2022-03-16 19:36:03" fw="SN12345678912345" tz=+0100 startime="" pri=5 confid=01 slotlevel=2 ruleid=103 srcif="Ethernet3" srcifname="in" ipproto=tcp dstif="Ethernet2" dstifname="out" proto=https src=11.11.11.11 srcport=49586 srcportname=ephemeral_fw_tcp srcname=foo_bar srcmac=00:00:00:00:00:00 srccontinent="na" srccountry="us" dst=22.22.22.22 dstport=443 dstportname=https dstcontinent="eu" dstcountry="be" modsrc=11.11.11.11 modsrcport=49586 origdst=22.22.22.22 origdstport=443 ipv=4 sent=2827291 rcvd=2728401 duration=107331.18 action=pass logtype="connection"
    ```



=== "plugin"

    ```
	time="2023-11-23 09:19:44" fw="SN12345678912345" tz=+0100 startime="2023-11-23 09:19:43" pri=5 confid=01 slotlevel=2 ruleid=11 rulename="18b60ffd8cd_5" ipproto=tcp dstif="Ethernet0" dstifname="wan-interface" proto=http src=11.22.33.44 srcport=1025 srcportname=dyn_tcp srcname=host_11.22.33.44 dst=55.66.77.88 dstport=80 dstportname=http dstname=www.sekoia.io dstcontinent="eu" dstcountry="fr" modsrc=11.22.33.44 modsrcport=1025 origdst=55.66.77.88 origdstport=80 ipv=4 rtname="router" rt="gateway-orange" sent=98 rcvd=766 duration=0.01 action=pass op=GET result=200 arg="/en/integrations-catalog/" logtype="plugin"
    ```



=== "server"

    ```
	id=firewall time="2023-07-03 18:26:30" fw="SN12345678912345" tz=+0200 startime="2023-07-03 18:26:30" error=0 user="admin" address=11.11.11.11 sessionid=5 msg="SYSTEM IDENT" logtype="server"
    ```



=== "system"

    ```
	time="2023-11-23 09:20:59" fw="SN12345678912345" tz=+0100 startime="2023-11-23 09:20:58" pri=5 msg="Licence Update: (licence1-sns.stormshieldcs.eu) Cannot contact server" service=sysevent alarmid=70 logtype="system"
    ```



=== "test_monitor"

    ```
	id=firewall time=2025-10-29 09:56:16 fw=ABSDC1MSLFWL01P tz=+0100 startime=2025-10-29 09:56:16 security=0 system=0 CPU=0,8,0 Pvm=0,0,0,0,0,0,0,0,0,0,0 vlan2=int-vlan2722,94891849,152692456,239447742,491018456,9364723,254 vlan1=int-vlan2954,12345,37352,3150,7320,1277,51 vlan0=int-vlan3718,214020032,482644112,70059432,123508648,13766296,611 Agg1=agg-0,0,0,0,0,0,0 Agg0=agg-1,0,0,0,0,0,0 sslvpn1=sslvpn_udp,0,0,0,0,0,0 sslvpn0=sslvpn,0,0,0,0,0,0 Ethernet1=Ethernet_1,0,0,0,0,0,0 Ethernet0=int-admin,59966,235120,996276,1169176,35692,22 Ethernet4=int-ha1,0,0,0,0,0,0 Ethernet2=Ethernet_2,0,0,0,0,0,0 Ethernet8=int-ha2,0,0,0,0,0,0 Ethernet6=Ethernet_6,0,0,0,0,0,0 ipsec=ipsec,68057620,125860320,217711664,469077136,8940118,0 Qid0=BYPASS_ipsec,6497892,12083160,185329240,889392592,539224,0 Qid1=BYPASS_Ethernet_6,0,0,0,0,0,0 Qid2=BYPASS_int-ha2,0,0,0,0,0,0 Qid3=BYPASS_Ethernet_2,0,0,0,0,0,0 Qid4=BYPASS_int-ha1,0,0,0,0,0,0 Qid5=BYPASS_int-admin,782264,2867304,232,2716264,33925,0 Qid6=BYPASS_Ethernet_1,0,0,0,0,0,0 Qid7=BYPASS_agg-1,0,0,0,0,0,0 Qid8=BYPASS_agg-0,0,0,0,0,0,0 Qid9=BYPASS_int-vlan3718,68073086,233044984,2537316,30750848,8633769,0 Qid10=BYPASS_int-vlan2954,0,65936,0,0,1357,0 Qid11=BYPASS_int-vlan2722,0,0,211743348,956867504,0,0  logtype=monitor
    ```



=== "test_monitor_2"

    ```
	id=firewall time=2025-10-28 13:14:08 fw=ABSDC1MSLFWL01P tz=+0100 startime=2025-10-28 13:14:08 security=0 system=0 CPU=0,7,0 Pvm=0,0,0,0,0,0,0,0,0,0,0 vlan2=int-vlan2723,66077451,91570072,216671312,383138048,11881282,197 vlan1=int-vlan2955,25972,53744,6376,11600,3558,41 vlan0=int-vlan3728,196621857,349377320,40027851,57390200,16559344,1954 Agg1=agg-1,0,0,0,0,0,0 Agg0=agg-0,0,0,0,0,0,0 sslvpn1=sslvpn_udp,0,0,0,0,0,0 sslvpn0=sslvpn,0,0,0,0,0,0 Ethernet1=Ethernet_1,0,0,0,0,0,0 Ethernet0=int-admin,90025,332128,1295038,1597520,60863,30 Ethernet4=int-ha1,0,0,0,0,0,0 Ethernet2=Ethernet_2,0,0,0,0,0,0 Ethernet8=int-ha2,0,0,0,0,0,0 Ethernet6=Ethernet_6,0,0,0,0,0,0 ipsec=ipsec,39754748,56979056,202705988,358098320,10640410,0 Qid0=BYPASS_ipsec,5523681,8258384,170409876,362899048,372264,0 Qid1=BYPASS_Ethernet_6,0,0,0,0,0,0 Qid2=BYPASS_int-ha2,0,0,0,0,0,0 Qid3=BYPASS_Ethernet_2,0,0,0,0,0,0 Qid4=BYPASS_int-ha1,0,0,0,0,0,0 Qid5=BYPASS_int-admin,1153686,2275752,185227,1114216,71734,0 Qid6=BYPASS_Ethernet_1,0,0,0,0,0,0 Qid7=BYPASS_agg-0,0,0,0,0,0,0 Qid8=BYPASS_agg-1,0,0,0,0,0,0 Qid9=BYPASS_int-vlan3728,54539899,176290960,4000940,5246536,10385185,0 Qid10=BYPASS_int-vlan2955,23742,143376,0,0,3782,0 Qid11=BYPASS_int-vlan2723,0,0,192347577,398852072,0,0  logtype=monitor
    ```



=== "vpn_phase1"

    ```
	id=firewall time="2023-07-04 11:27:09" fw="SN12345678912345" tz=+0200 startime="2023-07-04 11:27:09" pri=5 src=33.33.33.33 srcname=Firewall_out dst=44.44.44.44 dstname=host_44.44.44.44 ikev=2 ruletype=gateway phase=1 side=initiator cookie_i=0x3b77dce129c457dc cookie_r=0x57dd9eabc5b7f8dd peername=Sekoia_peer msg="Local NAT detected, switching to port 4500" logtype="vpn"
    ```



=== "vpn_phase2"

    ```
	id=firewall time="2023-07-03 18:20:02" fw="SN12345678912345" tz=+0200 startime="2023-07-03 18:20:02" pri=5 src=11.11.11.11 srcname=Firewall_out dst=22.22.22.22 dstname=host_22.22.22.22 ikev=2 ruletype=gateway phase=2 side=initiator cookie_i=0x573ebe1ca6e085fc cookie_r=0x8c196f302bdc378b localnet=192.168.10.0/27 remotenet=192.168.10.32/27 spi_in=0xc848d405 spi_out=0xc287574b remoteid=22.22.22.22 rulename=vpn_sekoia msg="Sending DELETE for IPSEC SA (ESP)" logtype="vpn"
    ```



=== "xvpn1"

    ```
	id=firewall time="2025-04-23 07:41:56" fw="FWCLIENT" tz=+0200 startime="2025-04-23 07:41:56" ipproto="TCP" user="user1" domain="client.com" src=1.2.3.4 msg="Error during authentication : authentication failed, bad password" logtype="xvpn"
    ```



=== "xvpn2"

    ```
	id=firewall time="2024-08-26 23:53:57" fw="IJM" tz=+0200 startime="2024-08-26 23:53:57" ipproto="UDP" user="johndoe" domain="example.com" src=1.2.3.4 remotenet=10.0.1.6 localnet=10.0.1.5 msg="User authenticated in ASQ" logtype="xvpn"
    ```



=== "xvpn3"

    ```
	id=firewall time="2024-08-26 23:53:57" fw="IJM" tz=+0200 startime="2024-08-26 23:53:57" ipproto="UDP" user="johndoe" domain="example.com" src=1.2.3.4 remotenet=10.0.1.6 localnet=10.0.1.5 port=59505 msg="SSL tunnel created" logtype="xvpn"
    ```



