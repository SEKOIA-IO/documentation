
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_auth_access_1"

    ```
	Info     EXAMPLE LOGIN ATTEMPT: boxconfig[50357]: Login localhost_EXAMPLE from 127.0.0.1 : Allowed.
    ```



=== "test_auth_access_2"

    ```
	Info     EXAMPLE boxconfig[50512]: Session localhost_EXAMPLE: Closed
    ```



=== "test_auth_access_3"

    ```
	Security MACHINE-F380 LOGIN ATTEMPT: Login from 1.2.3.4: Denied: Firewall Rule RULENAME
    ```



=== "test_auth_service_1"

    ```
	Info     MACHINE-F380 Received 3 users from EXAMPLEVPN (DC1 IP = 1.2.3.4).
    ```



=== "test_auth_service_2"

    ```
	Info     MACHINE-F380 phibs: Authentication Login for peer=5.6.7.8 origin=DCCLIENT server=box service=dcclient box=MACHINE-F380 startport=0 endport=0 user=jdoe
    ```



=== "test_auth_service_3"

    ```
	Info     MACHINE-F380 phibs: Authentication Login for peer=1.2.3.4 origin=DCCLIENT server=box service=dcclient box=MACHINE-F380 startport=0 endport=0 user=jdoe
    ```



=== "test_auth_service_4"

    ```
	Info     MACHINE-F380 phibs: Authentication Timeout(28800) for peer=1.2.3.4 origin=DCCLIENT server=box service=dcclient box=MACHINE-F380 jdoe|||||||CN=VPN-ALL,OU=Groups,OU=Shared,OU=Business,DC=example,DC=com|1740086783|28800||msad||
    ```



=== "test_auth_service_5"

    ```
	Info     EXAMPLE MSAD-Offline-Groups Setting MSAD offline group sync cache to 178.64 MByte (auto-calculated)
    ```



=== "test_auth_service_6"

    ```
	Info     MACHINE-F380 MSAD-Offline-Groups Start sync for msad-groups for domain EXAMPLEDC04 on 1.2.3.4.
    ```



=== "test_auth_service_7"

    ```
	Info     MACHINE-F380 MSAD-Offline-Groups Start sync for domain EXAMPLEDC04 on 1.2.3.4.
    ```



=== "test_config_1"

    ```
	Info     MACHINE-F380 Session from 127.0.0.1:15743 mode=0
    ```



=== "test_config_2"

    ```
	Info     MACHINE-F380  challenge sent for localhost_MACHINE-F380_5-4_1
    ```



=== "test_config_3"

    ```
	Notice   MACHINE-F380 127.0.0.1:15743 login succeeded: localhost_MACHINE-F380_5-4_1 Valid password and valid challenge
    ```



=== "test_config_4"

    ```
	Info     MACHINE-F380 New Session GCSID_localhost_MACHINE-F380_5-4_1_127.0.0.1_15743_25308
    ```



=== "test_config_5"

    ```
	Info     EXAMPLE New Session GCSID_localhost_EXAMPLE_127.0.0.1_34031_56301
    ```



=== "test_config_6"

    ```
	Info     MACHINE-F380 Process: Session(127.0.0.1:15743) exits normally
    ```



=== "test_config_7"

    ```
	Info     MACHINE-F380 [master@1.2.3.4_36778]  Download File /var/phion/mcdownload/firmwareupdates/files/9.0 received size=71731 mode=100644
    ```



=== "test_config_8"

    ```
	Info     MACHINE-F380 [master@1.2.3.4_29010]  Commit operation: 0 Copy: bsyslog.conf from boxsrv
    ```



=== "test_config_9"

    ```
	Info     MACHINE-F380 [master@1.2.3.4_29010]  Commit operation: 0 Execute: /opt/phion/modules/box/boxsrv/bsyslog/bin/activate /opt/phion/config/active/bsyslog.conf
    ```



=== "test_event_1"

    ```
	Info     MACHINE-F380 event: [1071065] Insert Event from 127.0.0.1:56405 - (D|3|boxfw|3|firewall|4015|9.10.11.12:443|MACHINE-F380_5-4_1|1740029102|TCP 5.6.7.8:80 (bond0.21) -> 9.10.11.12:443)
    ```



=== "test_event_2"

    ```
	Info     MACHINE-F380 event: [1071065] Drop Event from 127.0.0.1:11703 - (D|3|MACHINE-F380MVPN|2|vpnserver|3002|IPSEC-EXAMPLE-1.2.3.4-5.6.7.8|MACHINE-F380_5-4_1)
    ```



=== "test_event_3"

    ```
	Info     MACHINE-F380 event: [1071032] Send Event (D|2|NGAdmin|2|Login|2420|root|MACHINE-F380_5-4_1) to Control Center 1.2.3.4
    ```



=== "test_event_4"

    ```
	Info     MACHINE-F380 event: [1071032] Send Event (D|2|control|2|controld|62|1.2.3.4/32 gateway table default dev bond0.23 via 13.14.15.16 proto 3|MACHINE-F380_5-4_1) to Control Center 5.6.7.8
    ```



=== "test_firewall_1"

    ```
	Security MACHINE-F380 firewall: [Timer] SecurityEvent: (Address-Port Scan) 149 unallowed requests for source IP 5.6.7.8 within 60 seconds
    ```



=== "test_firewall_activity_1"

    ```
	Info     MACHINE-F380 Allow: LOUT|UDP|bond0.603|1.2.3.4|61988|00:11:22:33:44:55|5.6.7.8|53|domain||RULENAME|0|9.10.11.12|5.6.7.8|0|1|0|0|0|0||||||
    ```



=== "test_firewall_activity_2"

    ```
	Security EXAMPLE LocalBlock: <cumulative>|UDP|eth0|5.6.7.8|0|00:00:00:00:00:00|9.10.11.12|811|||<no-match>|4003|||0|24|0|0|0|0||||||
    ```



=== "test_firewall_threats_1"

    ```
	Warning  MACHINE-F380 firewall: [Request] Allow:   IPS ALLIP(0) 9.10.11.12 -> 1.2.3.4:0 |[ID: 5000002 TCPIP Port or IP Address Scan]||3|Probing
    ```



=== "test_firewall_user_accounting_1"

    ```
	Info     MACHINE-F380 update|MACHINE-F380|PGRP-AUTH-jdoe-ABCD||||||1740020807|1740115598|116377688|1219271687|5.6.7.8|||jdoe
    ```



=== "test_rest_1"

    ```
	Warning  MACHINE-F380 [5647250.628103] KTINA-WARN: IPSEC-v2-EXAMPLE doesn't have a transport
    ```



=== "test_rest_2"

    ```
	Info     MACHINE-F380 control: Send status poll request status to Control Center 1.2.3.4
    ```



=== "test_rest_3"

    ```
	Info     MACHINE-F380 Log wrapping is enabled, log caching is enabled
    ```



=== "test_watchdog_1"

    ```
	Info     MACHINE-F380 was able to ping process 1126 (/var/run/syslogd.pid).
    ```



=== "test_watchdog_2"

    ```
	Info     MACHINE-F380 still alive after 23523 interval(s)
    ```



=== "test_watchdog_3"

    ```
	Info     MACHINE-F380 current load is 1 0 0
    ```



=== "test_watchdog_4"

    ```
	Info     MACHINE-F380 currently there are 3387184 kB of free memory available (209780 buffered, 1507836, cached)
    ```



