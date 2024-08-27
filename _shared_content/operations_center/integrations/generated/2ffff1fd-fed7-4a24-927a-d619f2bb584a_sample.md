
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_alert_1"


    ```json
	{
        "event_type": "ESET Inspect Alert",
        "ipv4": "3.4.5.6",
        "hostname": "desktop01.example.com",
        "os_name": "Microsoft Windows Server 2012 R2 Standard",
        "group_name": "Example/Domain Controllers",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "20-May-2024 09:08:10",
        "severity": "Warning",
        "processname": "%SYSTEM%\\nslookup.exe",
        "username": "nt authority\\system",
        "rulename": "Nslookup wrote a file [F0500]",
        "count": 1,
        "hash": "ADC83B19E793491B1C6EA0FD8B46CD9F32E592FC",
        "eialarmid": "1234",
        "eiconsolelink": "https://dark.example.org:443/console/detection/1234",
        "computer_severity_score": "60",
        "severity_score": "46"
    }
    ```



=== "test_alert_2"


    ```json
	{
        "event_type": "ESET Inspect Alert",
        "ipv4": "3.4.5.6",
        "hostname": "desktop01.example.com",
        "os_name": "Microsoft Windows Server 2012 R2 Standard",
        "group_name": "Example/Domain Controllers",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "20-May-2024 09:08:10",
        "severity": "Warning",
        "processname": "%SYSTEM%\\nslookup.exe",
        "username": "nt authority\\system",
        "rule_name": "Nslookup wrote a file [F0500]",
        "count": 1,
        "hash": "ADC83B19E793491B1C6EA0FD8B46CD9F32E592FC",
        "eialarmid": "1234",
        "eiconsolelink": "https://dark.example.org:443/console/detection/1234",
        "computer_severity_score": "60",
        "severity_score": "46"
    }
    ```



=== "test_audit_event_1"


    ```json
	{
        "event_type": "Audit_Event",
        "ipv4": "3.4.5.6",
        "hostname": "auvergnat",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "20-May-2024 09:05:05",
        "severity": "Information",
        "domain": "Update modules",
        "action": "Update",
        "detail": "Modules successfully updated.",
        "user": "jdoe",
        "result": "Success"
    }
    ```



=== "test_audit_event_2"


    ```json
	{
        "event_type": "Audit_Event",
        "ipv4": "3.4.5.6",
        "hostname": "auvergnat",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "20-May-2024 09:14:03",
        "severity": "Information",
        "domain": "Native user",
        "action": "Logout",
        "target": "Administrator",
        "detail": "Logging out native user 'Administrator'.",
        "user": "Administrator",
        "result": "Success"
    }
    ```



=== "test_audit_event_3"


    ```json
	{
        "event_type": "Audit_Event",
        "ipv4": "3.4.5.6",
        "hostname": "auvergnat",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "10-May-2024 10:59:26",
        "severity": "Information",
        "domain": "ESET INSPECT",
        "action": "Marked as Resolved",
        "target": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "detail": "Resolved via ESET INSPECT",
        "user": "Administrator",
        "result": "Success"
    }
    ```



=== "test_audit_event_4"


    ```json
	{
        "event_type": "Audit_Event",
        "ipv4": "3.4.5.6",
        "hostname": "auvergnat",
        "os_name": "Microsoft Windows Server 2019 Datacenter Evaluation",
        "group_name": "EXAMPLE/Outer",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "10-May-2024 10:58:28",
        "severity": "Information",
        "domain": "ESET INSPECT",
        "action": "Detections",
        "target": "00000000-0000-0000-7002-000000000002",
        "detail": "Detection \"Rule; Suspicious Service Executed [B0902]\" resolved",
        "user": "Administrator",
        "result": "Success"
    }
    ```



=== "test_audit_event_5"


    ```json
	{
        "event_type": "Audit_Event",
        "ipv4": "3.4.5.6",
        "hostname": "auvergnat",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "10-May-2024 10:55:05",
        "severity": "Information",
        "domain": "Single-sign-on token",
        "action": "Single sign on token issue",
        "detail": "Single Sign On Session Token '********' issued for native user 'Administrator'.",
        "user": "",
        "result": "Success"
    }
    ```



=== "test_audit_event_6"


    ```json
	{
        "event_type": "Audit_Event",
        "ipv4": "3.4.5.6",
        "hostname": "auvergnat",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "10-May-2024 10:55:05",
        "severity": "Information",
        "domain": "Single-sign-on token",
        "action": "Single sign on token issue",
        "cause": "Single Sign On Session Token '********' issued for native user 'Administrator'.",
        "user": "",
        "result": "Success"
    }
    ```



=== "test_audit_event_7"


    ```json
	{
        "event_type": "Audit_Event",
        "ipv4": "3.4.5.6",
        "hostname": "auvergnat",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "10-May-2024 10:55:05",
        "severity": "Information",
        "domain": "Single-sign-on token",
        "action": "Single sign on token issue",
        "cause": "Single Sign On Session Token '********' issued for native user 'Administrator'.",
        "user": "",
        "result": "Failure"
    }
    ```



=== "test_audit_event_8"


    ```json
	{
        "event_type": "Audit_Event",
        "ipv4": "3.4.5.6",
        "hostname": "auvergnat",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "10-May-2024 10:55:05",
        "severity": "Information",
        "domain": "Single-sign-on token",
        "action": "Single sign on token issue",
        "cause": "Single Sign On Session Token '********' issued for native user 'Administrator'.",
        "user": "john.doe@example.com",
        "result": "Failure"
    }
    ```



=== "test_firewall_1"


    ```json
	{
        "event_type": "FirewallAggregated_Event",
        "ipv4": "3.4.5.6",
        "hostname": "server01.example.org",
        "os_name": "Microsoft Windows 10 Pro",
        "group_name": "EXAMPLE/Outer",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "07-May-2024 07:42:01",
        "severity": "Fatal",
        "event": "Suspected botnet detected",
        "source_address": "1.2.3.4",
        "source_address_type": "IPv4",
        "source_port": 22089,
        "target_address": "5.6.7.8",
        "target_address_type": "IPv4",
        "target_port": 57178,
        "protocol": "TCP",
        "action": "Blocked",
        "handled": true,
        "process_name": "C:\\Windows\\Temp\\tmpseajke.exe",
        "inbound": true,
        "threat_name": "Win32/RiskWare.Meterpreter.A",
        "aggregate_count": 1
    }
    ```



=== "test_firewall_2"


    ```json
	{
        "event_type": "FirewallAggregated_Event",
        "ipv4": "3.4.5.6",
        "hostname": "server01.example.org",
        "os_name": "Microsoft Windows 10 Pro",
        "group_name": "EXAMPLE/Outer",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "07-May-2024 07:42:01",
        "severity": "Fatal",
        "event": "Suspected botnet detected",
        "source_address": "1.2.3.4",
        "source_address_type": "IPv4",
        "source_port": 22089,
        "target_address": "5.6.7.8",
        "target_address_type": "IPv4",
        "target_port": 57178,
        "protocol": "TCP",
        "action": "Blocked",
        "handled": true,
        "processname": "C:\\Windows\\Temp\\tmpseajke.exe",
        "inbound": true,
        "threat_name": "Win32/RiskWare.Meterpreter.A",
        "aggregate_count": 1
    }
    ```



=== "test_firewall_3"


    ```json
	{
        "event_type": "FirewallAggregated_Event",
        "ipv4": "3.4.5.6",
        "hostname": "server01.example.org",
        "os_name": "Microsoft Windows 10 Pro",
        "group_name": "EXAMPLE/Outer",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "07-May-2024 07:42:01",
        "severity": "Fatal",
        "event": "Suspected botnet detected",
        "source_address": "1.2.3.4",
        "source_address_type": "IPv4",
        "source_port": 22089,
        "target_address": "5.6.7.8",
        "target_address_type": "IPv4",
        "target_port": 57178,
        "protocol": "TCP",
        "action": "Blocked",
        "handled": true,
        "processname": "C:\\Windows\\Temp\\tmpseajke.exe",
        "inbound": true,
        "threat_name": "Win32/RiskWare.Meterpreter.A",
        "aggregate_count": 1
    }
    ```



=== "test_firewall_4"


    ```json
	{
        "event_type": "FirewallAggregated_Event",
        "ipv4": "3.4.5.6",
        "hostname": "server01.example.org",
        "os_name": "Microsoft Windows 10 Pro",
        "group_name": "EXAMPLE/Outer",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "07-May-2024 07:42:01",
        "severity": "Fatal",
        "event": "Suspected botnet detected",
        "destination_address": "1.2.3.4",
        "source_address_type": "IPv4",
        "destination_port": 22089,
        "target_address": "5.6.7.8",
        "target_address_type": "IPv4",
        "target_port": 57178,
        "protocol": "TCP",
        "action": "Blocked",
        "handled": true,
        "process_name": "C:\\Windows\\Temp\\tmpseajke.exe",
        "inbound": true,
        "threat_name": "Win32/RiskWare.Meterpreter.A",
        "aggregate_count": 1
    }
    ```



=== "test_hips_1"


    ```json
	{
        "event_type": "HipsAggregated_Event",
        "ipv4": "192.168.30.181",
        "hostname": "test-w10-uefi",
        "group_name": "Lost & found",
        "source_uuid": "5dbe31ae-4ca7-4e8c-972f-15c197d12474",
        "occured": "21-Jun-2021 11:53:21",
        "severity": "Critical",
        "application": "C:\\Users\\Administrator\\Desktop\\es_pack_to_test\\test\\java.exe",
        "operation": "Attempt to run a suspicious object",
        "target": "C:\\Users\\Administrator\\Desktop\\es_pack_to_test\\test\\trojan.exe",
        "action": "blocked",
        "handled": true,
        "rule_id": "Suspicious attempt to launch an application",
        "aggregate_count": 2
    }
    ```



=== "test_hips_2"


    ```json
	{
        "event_type": "HipsAggregated_Event",
        "ipv4": "192.168.30.181",
        "hostname": "test-w10-uefi",
        "group_name": "Lost & found",
        "source_uuid": "5dbe31ae-4ca7-4e8c-972f-15c197d12474",
        "occured": "21-Jun-2021 11:53:21",
        "severity": "Critical",
        "application": "C:\\Users\\Administrator\\Desktop\\es_pack_to_test\\test\\java.exe",
        "operation": "Attempt to run a suspicious object",
        "target": "C:\\Users\\Administrator\\Desktop\\es_pack_to_test\\test\\trojan.exe",
        "action": "blocked",
        "handled": true,
        "rule_id": "Suspicious attempt to launch an application",
        "aggregate_count": 2
    }
    ```



=== "test_threat_1"


    ```json
	{
        "event_type": "Threat_Event",
        "ipv4": "3.4.5.6",
        "hostname": "server01.example.org",
        "os_name": "Microsoft Windows 10 Pro",
        "group_name": "Example/Outer",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "07-May-2024 08:21:10",
        "severity": "Warning",
        "threat_type": "Trojan",
        "threat_name": "Win32/ShellcodeRunner.B",
        "threat_flags": "Variant",
        "scanner_id": "Idle scanner",
        "scan_id": "ndl3714149360.dat",
        "engine_version": "29184 (20240507)",
        "object_type": "File",
        "object_uri": "file:///C:/Windows/Temp/tmpsesusx.exe",
        "action_taken": "Cleaned by deleting",
        "threat_handled": true,
        "need_restart": false,
        "username": "EXAMPLE NT\\SYSTEM",
        "firstseen": "07-May-2024 07:44:39",
        "hash": "ADC83B19E793491B1C6EA0FD8B46CD9F32E592FC"
    }
    ```



=== "test_threat_2"


    ```json
	{
        "event_type": "Threat_Event",
        "ipv4": "3.4.5.6",
        "hostname": "server01.example.org",
        "os_name": "Microsoft Windows 10 Pro",
        "group_name": "Example/Outer",
        "source_uuid": "7c94f9e1-5a7f-4f69-8f33-8e8316798b0b",
        "occured": "06-May-2024 14:39:17",
        "severity": "Warning",
        "threat_type": "Trojan",
        "threat_name": "Win32/ShellcodeRunner.B",
        "threat_flags": "Variant",
        "scanner_id": "On-demand scanner",
        "scan_id": "ndl1556677733.dat",
        "engine_version": "29180 (20240506)",
        "object_type": "Operating memory",
        "object_uri": "file:///",
        "action_taken": "Contained infected files",
        "threat_handled": true,
        "need_restart": false,
        "username": "Example\\jdoe"
    }
    ```



