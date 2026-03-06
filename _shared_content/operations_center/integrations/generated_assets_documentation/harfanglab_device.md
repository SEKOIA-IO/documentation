## OCSF Mapping for Harfanglab Devices


**OCSF Class:** `Device Inventory Info`



**Class UID:** `5001`



**OCSF Version:** `1.6.0`


## Information Collected

The Harfanglab Devices fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### HarfangLab Device Inventory Sample
Agent data sample for harfanglab api response.

```json
{
        "id": "3891597d-8696-4fc4-a260-b04880bdbd68",
        "group_count": None,
        "groups": [],
        "status": "offline",
        "policy": {
            "id": "eaa79dde-2c4c-4fb8-822b-20a0529ba6db",
            "tenant": None,
            "origin_stack": None,
            "macos_paths_muted_exact": [
                "/Applications/Avast.app/Contents/Backend/utils/com.avast.Antivirus.EndpointSecurity.app/Contents/MacOS/com.avast.Antivirus.EndpointSecurity.",
                "/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/corespotlightd",
            ],
            "macos_paths_muted_prefixes": [
                "/Applications/WithSecure/WithSecure Agent.app/",
                "/usr/libexec/",
            ],
            "macos_paths_muted_globs": [],
            "macos_paths_read_watched_exact": [
                "/private/etc/kcpassword",
                "/System/Library/Sandbox/rootless.conf",
            ],
            "macos_paths_read_watched_prefixes": [
                "/private/var/db/dslocal/nodes/Default/users/",
                "/Library/Keychains/",
                "/Network/Library/Keychains/",
            ],
            "macos_paths_read_watched_globs": [
                "/Users/*/Library/Application Support/Litecoin/wallets/**",
                "/Users/*/.ssh/*",
                "/Users/*/Library/Application Support/Microsoft Edge/*/**",
            ],
            "macos_paths_write_watched_exact": ["/Library/Application Support/com.apple.TCC/TCC.db"],
            "macos_paths_write_watched_prefixes": [
                "/System/Library/LaunchAgents/",
                "/Library/Scripts/",
            ],
            "macos_paths_write_watched_globs": [
                "/Users/*/Library/Preferences/**",
                "/Users/*/Library/LaunchAgents/**",
            ],
            "macos_paths_other_watched_exact": ["/Library/Application Support/com.apple.TCC/TCC.db"],
            "macos_paths_other_watched_prefixes": [
                "/System/Library/LaunchAgents/",
                "/Library/Scripts/",
            ],
            "macos_paths_other_watched_globs": [
                "/Users/*/Documents/**",
                "/private/var/folders/**/NSCreateObjectFileImageFromMemory-*",
            ],
            "windows_read_watched_paths": [
                "*\\PROGRAM FILES*",
                "*\\WINDOWS\\SYSTEM32\\CONFIG\\*",
            ],
            "windows_write_watched_paths": [
                "*\\PROGRAM FILES*",
                "*\\USERS\\DEFAULT\\NTUSER.DAT",
            ],
            "windows_registry_read_whitelist": [
                "HKU\\*\\SOFTWARE\\OPENSSH\\AGENT\\KEYS\\*",
            ],
            "windows_registry_read_blacklist": [],
            "linux_paths_other_watched_globs": [
                "/home/*/*",
                "/home/*/*/*",
                "/root/*",
                "/root/*/*",
                "/tmp/**",
                "/dev/shm/**",
            ],
            "use_driver": True,
            "use_process_block": False,
            "antivirus_policy_name": "GENSECEV_HarfangLab_AV_policy",
            "agent_auto_update": False,
            "agent_auto_forget": False,
            "agent_auto_forget_max_days": 1,
            "antivirus_profile": "d060dd94-fe99-4683-900e-f304e74fe97c",
            "antivirus_profile_name": "GENSECEV_HarfangLab_AV_policy",
            "local_endpoint_cache_size": 10240,
            "name": "GENSECEV_HarfangLab_EDR_policy",
            "description": "Used to automatically generate security events **DO NOT TOUCH**",
            "revision": 2,
            "sleeptime": 60,
            "sleepjitter": 10,
            "telemetry_process_state": "live",
            "telemetry_process_limit": False,
            "telemetry_process_limit_value": 1000,
            "telemetry_network_state": "live",
            "telemetry_network_limit": False,
            "telemetry_network_limit_value": 1000,
            "telemetry_log_state": "live",
            "telemetry_log_limit": False,
            "telemetry_log_limit_value": 1000,
            "telemetry_remotethread_state": "live",
            "telemetry_remotethread_limit": False,
            "telemetry_remotethread_limit_value": 1000,
            "telemetry_driverload_state": "live",
            "telemetry_driverload_limit": False,
            "telemetry_driverload_limit_value": 1000,
            "telemetry_powershell_state": "live",
            "telemetry_powershell_limit": False,
            "telemetry_powershell_limit_value": 1000,
            "telemetry_dns_resolution_state": "live",
            "telemetry_dns_resolution_limit": False,
            "telemetry_dns_resolution_limit_value": 1000,
            "telemetry_authentication_state": "live",
            "telemetry_authentication_limit": False,
            "telemetry_authentication_limit_value": 1000,
            "telemetry_usb_activity_state": "live",
            "telemetry_usb_activity_limit": False,
            "telemetry_usb_activity_limit_value": 1000,
            "telemetry_user_group_state": "live",
            "telemetry_user_group_limit": False,
            "telemetry_user_group_limit_value": 1000,
            "telemetry_registry_state": "on_alert",
            "telemetry_registry_limit": False,
            "telemetry_registry_limit_value": 1000,
            "telemetry_raw_device_access_state": "on_alert",
            "telemetry_raw_device_access_limit": False,
            "telemetry_raw_device_access_limit_value": 1000,
            "telemetry_named_pipe_state": "on_alert",
            "telemetry_named_pipe_limit": False,
            "telemetry_named_pipe_limit_value": 1000,
            "telemetry_raw_socket_creation_state": "on_alert",
            "telemetry_raw_socket_creation_limit": False,
            "telemetry_raw_socket_creation_limit_value": 1000,
            "telemetry_network_listen_state": "on_alert",
            "telemetry_network_listen_limit": False,
            "telemetry_network_listen_limit_value": 1000,
            "telemetry_process_access_state": "on_alert",
            "telemetry_process_access_limit": False,
            "telemetry_process_access_limit_value": 1000,
            "telemetry_process_tamper_state": "on_alert",
            "telemetry_process_tamper_limit": False,
            "telemetry_process_tamper_limit_value": 1000,
            "telemetry_url_request_state": "on_alert",
            "telemetry_url_request_limit": False,
            "telemetry_url_request_limit_value": 1000,
            "telemetry_wmi_event_state": "on_alert",
            "telemetry_wmi_event_limit": False,
            "telemetry_wmi_event_limit_value": 1000,
            "telemetry_file_state": "on_alert",
            "telemetry_file_limit": False,
            "telemetry_file_limit_value": 1000,
            "telemetry_file_download_state": "live",
            "telemetry_file_download_limit": False,
            "telemetry_file_download_limit_value": 1000,
            "telemetry_library_load_state": "on_alert",
            "telemetry_library_load_limit": False,
            "telemetry_library_load_limit_value": 1000,
            "telemetry_dotnet_library_state": "on_alert",
            "telemetry_alerts_limit": False,
            "telemetry_alerts_limit_value": 1000,
            "binary_download_enabled": False,
            "library_download_enabled": False,
            "thread_download_enabled": False,
            "telemetry_on_alert_enabled": False,
            "telemetry_on_alert_pre_alert_event_count": 5000,
            "telemetry_on_alert_post_alert_max_event_count": 5000,
            "telemetry_on_alert_post_alert_max_duration_secs": 600,
            "loglevel": "DEBUG",
            "sigma_mode": 1,
            "ioc_mode": 1,
            "ioc_scan_written_executable": False,
            "ioc_scan_libraries": False,
            "hlai_mode": 1,
            "hlai_skip_signed_ms": True,
            "hlai_skip_signed_others": False,
            "hlai_scan_libraries": True,
            "hlai_written_executable": True,
            "hlai_pdf": True,
            "hlai_minimum_level": "critical",
            "hlai_scripts_mode": 1,
            "hlai_scripts_minimum_level": "critical",
            "hibou_mode": 0,
            "hibou_skip_signed_ms": False,
            "hibou_skip_signed_others": False,
            "hibou_minimum_level": "critical",
            "yara_mode": 1,
            "yara_skip_signed_ms": True,
            "yara_skip_signed_others": False,
            "yara_scan_written_executable": True,
            "yara_scan_libraries_load": True,
            "ransomguard_mode": 1,
            "ransomguard_heuristic_mode": 1,
            "driverblock_mode": 1,
            "sidewatch_mode": 1,
            "use_isolation": True,
            "linux_use_isolation": True,
            "isolation_exclusions_revision": None,
            "windows_self_protection": True,
            "windows_self_protection_feature_hosts": False,
            "windows_self_protection_feature_safe_mode": True,
            "windows_self_protection_feature_firewall": True,
            "linux_self_protection": True,
            "linux_self_protection_feature_hosts": False,
            "audit_killswitch": False,
            "linux_startup_block": False,
            "feature_callback_tampering": True,
            "feature_process_tampering": True,
            "feature_live_process_heuristics": True,
            "feature_windows_filesystem_events": True,
            "feature_dse_tampering_mode": 1,
            "feature_event_stacktrace": True,
            "feature_ppl_antimalware": False,
            "agent_ui_enabled": False,
            "agent_ui_admin_message": None,
            "agent_ui_notification_scope": 2,
            "agent_ui_notification_level": 4,
            "synchronization_status": None,
            "sigma_ruleset": None,
            "yara_ruleset": None,
            "ioc_ruleset": None,
            "firewall_policy": None,
            "fim_policy": None,
            "antivirus_policy": "d060dd94-fe99-4683-900e-f304e74fe97c",
            "vulnerability_policy": None,
        },
        "tenant": None,
        "starttime": "2025-06-11T00:14:58.000000Z",
        "additional_info": {
            "additional_info1": "vagrant",
            "additional_info2": "wks",
            "additional_info3": None,
            "additional_info4": None,
        },
        "subnet": {
            "id": "35064b52-fa8a-4357-b21d-87ab8114add2",
            "gateway_ipaddress": "1.2.3.4",
            "gateway_macaddress": "55-55-00-22-33-22",
            "gateway_oui": None,
            "name": None,
        },
        "telemetry": None,
        "disk_count": 1,
        "encrypted_disk_count": 0,
        "domainname": "TestGROUP",
        "dnsdomainname": None,
        "hostname": "testhostaname1",
        "osmajor": 10,
        "osminor": 0,
        "osproducttype": "Windows 11 Enterprise Evaluation",
        "machine_serial": "0",
        "has_valid_password": True,
        "firstseen": "2025-06-11T00:15:06.454734Z",
        "lastseen": "2025-06-11T00:27:06.693963Z",
        "lastseen_warning": "2025-06-11T00:26:59.279324Z",
        "lastseen_error": "2025-06-11T00:27:29.279324Z",
        "version": "24.12.11-0bca88184713cdbb85eec416705f6a0baa07f518-dirty",
        "bitness": "x64",
        "distroid": None,
        "domain": None,
        "installdate": "2025-06-11 00:12:06+00:00",
        "ipaddress": "1.2.2.5",
        "ipmask": "255.255.255.0",
        "external_ipaddress": None,
        "osbuild": 22631,
        "osid": "00329-20000-00001-AA837",
        "ostype": "windows",
        "osversion": "10.0.22631",
        "producttype": "worktest",
        "servicepack": None,
        "total_memory": 4277866496,
        "cpu_count": 2,
        "cpu_frequency": 3408,
        "avg_cpu": 2.4,
        "avg_memory": 164448665,
        "avg_system_cpu": 14.4,
        "avg_system_memory": 3037852467,
        "avg_av_cpu": 0,
        "avg_av_memory": 80097280,
        "machine_boottime": "2025-06-11T00:13:20Z",
        "antivirus_name": "HarfangLab Antivirus",
        "antivirus_version": "6.3.23.0",
        "antivirus_rules_version": "108237",
        "antivirus_last_update_date": None,
        "antivirus_rules_last_update_date": "2025-06-10T18:04:36Z",
        "isolation_state": False,
        "isolation_policy": False,
        "driver_enabled": True,
        "driver_policy": False,
        "driver_version": "24.12.11",
        "is_ppl_antimalware": True,
        "rollback_version": None,
        "pinned_version": None,
        "task_statuses": None,
        "uninstall_status": 0,
        "update_status": 0,
        "refresh_properties_status": None,
        "windows_groups_last_update": None,
        "windows_users_last_update": None,
        "refresh_quarantine_status": None,
        "quarantine_last_update": None,
        "boot_loop_protection_end_date": None,
        "boot_loop_protection_boot_count": 1,
        "description": None,
        "effective_sigma_revision": 4156,
        "effective_yara_revision": 878,
        "effective_ioc_revision": 49,
        "effective_whitelist_revision": 2717,
        "effective_driver_blocklists_revision": 31,
        "telemetry_last_update": "2025-06-11T00:26:31.974049Z",
    }

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `id` | `device.uid` | Device unique identifier | `string` | Direct mapping of HarfangLab agent unique ID |
| `hostname` | `device.name` | Device hostname | `string` | Direct mapping of hostname |
| `hostname` | `device.hostname` | Device fully qualified hostname | `string` | Direct mapping of hostname |
| `osproducttype` | `device.os.name` | Operating system name and version | `string` | Direct mapping of OS product type (e.g., 'Windows 10 Professional', 'Ubuntu 20.04') |
| `ostype` | `device.os.type` | Operating system type | `string` | Normalize ostype to OCSF OSTypeStr: WINDOWS→'Windows', LINUX→'Linux', MACOS→'macOS', OTHER→'Other', UNKNOWN→'Unknown' |
| `ostype` | `device.os.type_id` | OCSF operating system type ID | `integer` | Map ostype to OCSF OSTypeId: WINDOWS→100, LINUX→200, MACOS→300, OTHER→99, UNKNOWN→0 |
| `producttype` | `device.type` | Device type | `string` | Map producttype: 'Workstation'→'Desktop', 'Server'→'Server', 'Laptop'→'Laptop', else→'Other' |
| `producttype` | `device.type_id` | OCSF device type ID | `integer` | Map device type to OCSF DeviceTypeId: Desktop→1, Laptop→2, Server→8, Other→99 |
| `ipaddress` | `device.network_interfaces[0].ip` | Primary network interface IP address | `string` | Direct mapping of IP address |
| `subnet.name || 'eth0'` | `device.network_interfaces[0].name` | Network interface name | `string` | Direct mapping of subnet name; default to 'eth0' if missing |
| `subnet.id` | `device.network_interfaces[0].uid` | Network interface unique identifier | `string` | Direct mapping of subnet ID |
| `hostname` | `device.network_interfaces[0].hostname` | Network interface hostname | `string` | Direct mapping of hostname for network interface |
| `static: Wired` | `device.network_interfaces[0].type` | Network interface type | `string` | Default to 'Wired'; can be enhanced with interface type detection logic |
| `static: 1` | `device.network_interfaces[0].type_id` | OCSF network interface type ID | `integer` | OCSF NetworkInterfaceTypeId for Wired = 1 |
| `ipaddress` | `device.ip` | Device primary IP address | `string` | Direct mapping of primary IP address |
| `domainname` | `device.domain` | Device domain or realm | `string` | Direct mapping of domain name |
| `ipmask` | `device.subnet` | Device subnet mask | `string` | Direct mapping of subnet mask/CIDR |
| `policy` | `device.is_managed` | Whether device is managed by policy | `boolean` | If policy object exists and is not empty, is_managed=true; else false |
| `has_valid_password` | `device.is_trusted` | Whether device has valid credentials/password | `boolean` | Direct mapping of password validity; indicates trust status |
| `static: HarfangLab` | `device.vendor_name` | Device vendor/manufacturer | `string` | Always 'HarfangLab' as agent vendor |
| `firstseen` | `device.created_time` | Device first seen timestamp | `timestamp` | Convert ISO 8601 to Unix epoch |
| `machine_boottime` | `device.boot_time` | Device boot time | `timestamp` | Convert ISO 8601 to Unix epoch |
| `lastseen` | `device.updated_time` | Device last seen timestamp | `timestamp` | Convert ISO 8601 to Unix epoch |
| `firstseen` | `time` | OCSF event timestamp | `timestamp` | Convert ISO 8601 to Unix epoch; use for OCSF event timestamp |
| `description || producttype + ' - ' + osproducttype` | `device.desc` | Device description | `string` | Use description if provided; fallback to '<producttype> - <osproducttype>' (e.g., 'Workstation - Windows 10') |
| `static: HarfangLab EDR` | `metadata.product.name` | Source product name | `string` | Always 'HarfangLab EDR' |
| `static: 24.12` | `metadata.product.version` | Product version | `string` | Fixed HarfangLab product version |
| `static: 1.5.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `static: 2` | `activity_id` | OCSF activity ID | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' for asset inventory |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Always 'Discovery' |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: Device Inventory Info` | `class_name` | OCSF class name | `string` | Always 'Device Inventory Info' |
| `static: 5001` | `class_uid` | OCSF class UID | `integer` | Always 5001 for Device Inventory Info |
| `computed: 500100 + activity_id` | `type_uid` | OCSF type UID | `integer` | Base 500100 + activity_id (2 = 500102) |
| `computed: class_name + ': ' + activity_name` | `type_name` | OCSF type name | `string` | Concatenate 'Device Inventory Info: Collect' |
| `static: Informational` | `severity` | Event severity | `string` | Always 'Informational' for inventory events |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Always 1 for Informational severity |
| `policy.windows_self_protection_feature_firewall` | `enrichments[0].data.Firewall_status` | Firewall protection status | `string` | Extract firewall status from policy; true→'Enabled', false→'Disabled', null→null |
| `encrypted_disk_count && disk_count` | `enrichments[0].data.Storage_encryption.partitions` | Storage partition encryption status | `object` | Build partition encryption map: for each disk i in range(disk_count), set 'disk_i' to 'Enabled' if i < encrypted_disk_count, else 'Disabled' |
| `static: compliance` | `enrichments[0].name` | Enrichment object name | `string` | Always 'compliance' for enrichment type |
| `static: hygiene` | `enrichments[0].value` | Enrichment object value | `string` | Always 'hygiene' for compliance enrichment |




### OCSF Model Structure

#### Device Inventory Info: Collect
Transformed HarfangLab api response to OCSF Device Inventory Info event

```json
{
  "activity_id": 2,
  "activity_name": "Collect",
  "category_name": "Discovery",
  "category_uid": 5,
  "class_name": "Device Inventory Info",
  "class_uid": 5001,
  "type_name": "Device Inventory Info: Collect",
  "type_uid": 500102,
  "severity": "Informational",
  "severity_id": 1,
  "time": 1749316506,
  "metadata": {
    "product": {
      "name": "HarfangLab EDR",
      "version": "24.12.11"
    },
    "version": "1.6.0"
  },
  "device": {
    "uid": "3891597d-8696-4fc4-a260-b04880bdbd68",
    "name": "testhostaname1",
    "hostname": "testhostaname1",
    "type": "Desktop",
    "type_id": 1,
    "vendor_name": "HarfangLab",
    "ip": "1.2.2.5",
    "domain": "TestGROUP",
    "subnet": "255.255.255.0",
    "is_managed": true,
    "is_trusted": true,
    "created_time": 1749316506,
    "boot_time": 1749315200,
    "updated_time": 1749321426,
    "desc": "worktest - Windows 11 Enterprise Evaluation",
    "os": {
      "name": "Windows 11 Enterprise Evaluation",
      "type": "Windows",
      "type_id": 100
    },
    "network_interfaces": [
      {
        "hostname": "testhostaname1",
        "name": "eth0",
        "ip": "1.2.2.5",
        "type": "Wired",
        "type_id": 1,
        "uid": "35064b52-fa8a-4357-b21d-87ab8114add2"
      }
    ]
  }
}

```


