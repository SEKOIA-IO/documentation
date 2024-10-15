# Panda Security

![Panda Security](/assets/playbooks/library/panda-security.png){ align=right width=150 }

[PandaSecurity](https://www.pandasecurity.com/), a [WatchGuard](https://www.watchguard.com/) company, is a cybsersecurity vendor, delivering products designed to protect endpoints against outside threats.

This module provides actions and triggers to interact with the [Watchguard Panda Aether platform](https://www.watchguard.com/wgrd-products/panda-endpoint-security) to act on AD360 and EPP devices

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | WatchGuard Cloud base URL (ex. https://api.usa.cloud.watchguard.com) |
| `account_id` | `string` | Your WatchGuard Cloud account ID |
| `api_key` | `string` | The API key associated to your Watchguard Cloud account |
| `access_id` | `string` | The identifier of the access credential used to authorize the requests |
| `access_secret` | `string` | The secret of the access credential used to authorize the requests |
| `audience` | `string` | The identifier of the managed account for service provider |

## Triggers

### Fetch Security Events

Fetch the last security events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds (default 12h) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `events` | `array` | A list of security events |

## Actions

### Get Security Events

Retrieves a list of security events of the specified type for the specified device for a specific time period.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `integer` | Type of security event. Specify one of these values:<br/>	- 1 — Malware<br/>	- 2 — PUPs (Potentially Unwanted Programs)<br/>	- 3 — Blocked Programs<br/>	- 4 — Exploits<br/>	- 5 — Blocked by Advanced Security<br/>	- 6 — Virus<br/>	- 7 — Spyware<br/>	- 8 — Hacking Tools and PUPs detected by Antivirus<br/>	- 9 — Phishing<br/>	- 10 — Suspicious<br/>	- 11 — Dangerous Actions<br/>	- 12 — Tracking Cookies<br/>	- 13 — Malware URLs<br/>	- 14 — Other security event by Antivirus<br/>	- 15 — Intrusion Attempts<br/>	- 16 — Blocked Connections<br/>	- 17 — Blocked Devices<br/>	- 18 — Indicators of Attack<br/>Example: 13 |
| `period` | `integer` | Period of time to retrieve security events for. Specify one of these values:<br/>	- 1 - Previous 24 hours<br/>	- 7 - Previous 7 days |
| `hostname` | `string` | Host name (base-64 encoded) of the device you want to retrieve security events for. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `accessed_data` | `boolean` | Indicates if data has been accessed. |
| `action` | `integer` | Indicates the action performed. For Indicators Of Attack:<br/>- 0: Undefined<br/>- 1: Informed<br/>- 2: Attack Blocked.<br/>For other detections:<br/>- 0: Allowed<br/>- 1: Moved Quarantine<br/>- 2: Blocked<br/>- 3: Killed<br/>- 4: Ignored<br/>- 5: Cleaned<br/>- 6: Deleted<br/>- 7: Restored<br/>- 8: Allowed By Whitelist<br/>- 9: Write Blocked<br/>- 10: User Pending<br/>- 11: Uninstalled<br/>- 13: After Process Blocked<br/>- 14: Immediately Blocked<br/>- 15: Allowed By User<br/>- 16: Detected Restart Pending<br/>- 17: Allowed By Administrator<br/>- 18: AllowedSonGwInstaller<br/>- 21: Suspend Process<br/>- 1009: Informed<br/>- 1010: Unquarantine<br/>- 1011: Rename<br/>- 1012: Block URL<br/> |
| `alias` | `string` | Alias name for device control detections. |
| `count` | `integer` | Number of occurrences in indicators of attack detections. |
| `custom_group_folder_id` | `string` | Identifier of the custom group folder assigned. |
| `custom_group_folder_info` | `string` | Hierarchical structure for the assigned group and its subgroups, in JSON format. |
| `date` | `string` | Date and time of detection. |
| `description` | `string` | Name of device description in antivirus detections. |
| `detected_by` | `` | Protection or technology in antivirus detections.<br/>- 1: On Demand Scan<br/>- 2: File Resident<br/>- 3: Mail Resident<br/>- 4: Firewall<br/>- 5: Device Control<br/>- 6: Exchange Mailbox<br/>- 7: Exchange Transport<br/>- 8: Exchange Antispam<br/>- 9: Web Protection<br/>- 10: Exchange Content<br/>- 11: Minerva<br/>- 12: Web Access Control<br/>- 13: Anti-theft<br/>- 14: Anti-tampering<br/>- 15: Personal Information Tracking<br/>- 16: Isolation<br/>- 17: Data Search Control<br/>- 18: Patch Management<br/>- 19: Personal Information Inventory<br/>- 20: Application Control<br/>- 21: Encryption USB<br/>- 22: Authorized Software<br/> |
| `detection_technology` | `string` | Name of detection technology in exploit detections. |
| `device_id` | `string` | Identifier of the device. |
| `device_type` | `` | Device type in antivirus and firewall detections.<br/>- 0: Undefined<br/>- 1: Workstation<br/>- 2: Laptop<br/>- 3: Server<br/>- 4: Mobile<br/> |
| `direction` | `` | Direction of firewall blocked connections.<br/>- 1: Incoming<br/>- 2: Outgoing<br/>- 3: Incoming and Outgoing<br/>- 4: Internal<br/> |
| `discard_motive` | `` | Reason for discarding the knowledge sample.<br/>- 0: Unknown<br/>- 1: Other Reason<br/>- 2: File Max Size<br/> |
| `domain` | `string` | Domain of device in antivirus detections. |
| `dwell_time` | `integer` | Dwell time in seconds. |
| `endpoint_event_date` | `string` | Endpoint event date in indicators of attack detections. |
| `event_id` | `integer` | Identifier of the event. |
| `event_type` | `` | Indicates the event type.<br/>- 0: Malware<br/>- 1: Exploit<br/>- 2: Pups<br/>- 3: Blocked item<br/>- 6: Lock Plus Advanced Security<br/>- 7: Lock Plus Application Control<br/>- 8: Application Control<br/> |
| `excluded` | `boolean` | Indicates if the element has been excluded in antivirus detection. |
| `exploit_technique` | `string` | Exploit technique. |
| `file_info_discard` | `string` | Hash to identify the file in antivirus detections. |
| `filed_date` | `string` | Filed date in indicators of attack detections. |
| `hash` | `string` | Hash of element. |
| `host_name` | `string` | Name of the host. |
| `id` | `string` | Identifier in antivirus detections. |
| `instance_id` | `string` | Identifier of instance for device control detections. |
| `ip_address` | `string` | IP address of the device in antivirus and firewall detections. |
| `is_excluded` | `boolean` | Indicates if data has been excluded. |
| `item_name` | `string` | Name of threat. |
| `like_lihood_of_being_malicious` | `` | Indicates the likelihood of being malicious.<br/>- 0: Low<br/>- 1: Medium<br/>- 2: High<br/>- 3: Very High<br/> |
| `local_endpoint` | `` | Firewall blocked connections for a local endpoint, in JSON format: Mac Address, IP Address, Port, and IP Type.<br/>- 0: Unknown<br/>- 1: IpV4<br/>- 2: IpV6<br/> |
| `lock_plus_rule_id` | `` | LockPlus Rule ID.<br/>- 1: Obfuscated Params Powershell<br/>- 2: User Executed Powershell<br/>- 4: Unknown Scripts<br/>- 5: Locally Built Programs<br/>- 6: Documents With Macros<br/>- 7: Windows Boot Registry<br/>- 101: Forbidden Md5<br/>- 102: Forbidden Program Name<br/> |
| `made_external_connections` | `boolean` | Indicates if malware made external connections. |
| `malware_category` | `` | Malware category in antivirus detections.<br/>- 1: Virus<br/>- 2: Spyware<br/>- 3: HackingPpnd<br/>- 4: Phishing<br/>- 5: Suspicious<br/>- 6: Blocked Operations<br/>- 7: Tracking Cookies<br/>- 8: Malware URL<br/>- 9: Others<br/> |
| `malware_name` | `string` | Malware name in antivirus detections. |
| `malware_type` | `` | Malware type in antivirus detections.<br/>- 21: Nereus Heuritic<br/>- 22: Beta trace Heuritic<br/>- 23: Smart Clean Heuritic<br/>- 24: Cloud Heuritic<br/>- 25: 1N<br/>- 26: Behavioral<br/>- 31: Confirmed Goodware<br/>- 32: Not Confirmed Goodware<br/>- 33: Unwanted Goodware<br/>- 34: Ranked<br/>- 35: Digital Signature<br/>- 101: Virus<br/>- 102: Worm<br/>- 103: Trojan<br/>- 104: TrojanPwdeal<br/>- 105: Dialer<br/>- 106: Joke<br/>- 107: Security Risk<br/>- 108: Spyware<br/>- 109: Adware<br/>- 110: WormFakefrom<br/>- 111: Tracking Cookie<br/>- 112: Pup<br/>- 113: Hacking Tool<br/>- 114: Vulnerability<br/>- 115: Max Size<br/>- 116: ZipOfDeath<br/>- 117: PackerOfDeath<br/>- 118: Hoax<br/>- 119: Phis Fraud<br/>- 120: Rootkit<br/>- 121: Backdoor<br/>- 122: Virus Constructor<br/>- 123: Malicious URL<br/>- 201: Advertising<br/>- 202: Toolbar<br/>- 203: NetTool<br/>- 204: Advert Popup<br/>- 219: Illegal<br/>- 223: Internet Tools<br/>- 227: Offensive<br/>- 236: Society Education<br/>- 241: Content Filter<br/> |
| `network_activity_type` | `` | Network activity type in firewall detections.<br/>- 1: IcmpAttack<br/>- 2: UdpPortScan<br/>- 3: HeaderLengths<br/>- 4: UdpFlood<br/>- 5: TcpFlagsCheck<br/>- 6: SmartWins<br/>- 7: IpExplicitPath<br/>- 8: LandAttack<br/>- 9: SmartDns<br/>- 10: IcmpFilterEchoRequest<br/>- 11: OsDetection<br/>- 12: SmartDhcp<br/>- 13: SynFlood<br/>- 14: SmartArp<br/>- 15: TcpPortScan<br/> |
| `number_of_occurrences` | `integer` | Number of occurrences in antivirus detections. |
| `path` | `string` | Name of threat path. |
| `platform_id` | `` | Platform of affected device.<br/>- 0: Undefined<br/>- 1: Windows<br/>- 2: Linux<br/>- 3: Mac<br/>- 4: Android<br/>- 5: IOS<br/> |
| `protection_mode` | `` | Indicates the protection mode.<br/>- 0: Undefined<br/>- 1: Audit<br/>- 2: Hardening<br/>- 3: Lock<br/> |
| `protocol` | `` | Protocol of firewall blocked connections.<br/>- 1: Tcp<br/>- 2: Udp<br/>- 3: TcpUdp<br/>- 4: Icmp<br/>- 5: IP<br/>- 6: All<br/> |
| `reclassified_to_type` | `` | Indicates the type to which it has been reclassified.<br/>- 0: Blocked<br/>- 1: Malware<br/>- 3: Pup<br/>- 6: Goodware<br/>- 11: Removed From List<br/> |
| `remote_endpoint` | `` | Firewall blocked connections for a remote endpoint, in JSON format: Mac Address, IP Address, Port, and IP Type.<br/>- 0: Unknown<br/>- 1: IpV4<br/>- 2: IpV6<br/> |
| `risk` | `boolean` | Indicates if it is a risk exploit. |
| `rule_configuration_id` | `string` | Identifier of rule configuration in firewall blocked connections. |
| `rule_id` | `string` | Identifier of rule in firewall blocked connections and in indicators of attack detections. |
| `rule_mitre` | `string` | Array with JSON pairs of the attack tactic and technique in indicators of attack detections. |
| `rule_name` | `string` | Rule name for firewall blocked connections and for indicators of attack detections. |
| `rule_obsolete` | `boolean` | Indicates if rule is obsolete in firewall blocked connections. |
| `rule_risk` | `` | Indicates the rule risk for indicators of attack detections.<br/>- 0: Undefined<br/>- 1: Critical<br/>- 2: High<br/>- 3: Medium<br/>- 4: Low<br/>- 1000: Unknown<br/> |
| `security_event_date` | `string` | Security event date and time for antivirus, firewall, and device control detections. |
| `since_until_filed` | `string` | Time since the filed date in indicators of attack detections. |
| `site_id` | `string` | Identifier of the site. |
| `site_name` | `string` | Site name in antivirus and firewall detections. |
| `source_ip` | `string` | Name of source IP. |
| `source_machine_name` | `string` | Name of source device name. |
| `source_user` | `string` | Source username. |
| `status` | `` | Indicates the status in indicators of attack detections.<br/>- 0: Undefined<br/>- 1: Pending<br/>- 2: Filed<br/> |
| `type` | `` | Type of device for device control detections.<br/>- 0: Undefined<br/>- 1: Removable Storage<br/>- 2: Image Capture<br/>- 3: Optical Storage<br/>- 4: Bluetooth<br/>- 5: Modem<br/>- 6: Mobile<br/> |
| `user_name` | `string` | Username. |
| `was_run` | `boolean` | Indicates if the item has been executed. |

### Isolate Devices

Isolates the specified devices. When you isolate a device, communication to and from the device is denied.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `device_ids` | `array` | List of IDs of devices to isolate.<br/>Example: "cb509c17-7b88-461a-ba3b-3d43e29e6cd4","2c13685e-7d1f-4726-9ad3-5c8fa7718bab" |
| `exclusion_programs` | `array` | List of programs to exclude from isolation and allow to communicate normally. |
| `customized_message` | `string` | Text to show in an alert message on the isolated devices |
| `hide_customized_alert` | `boolean` | Indicates whether to hide the customized alert message on isolated devices. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `processed_device_ids` | `array` | List of IDs of the isolated devices |

### Link Devices to Managed Configurations

Links devices to a specified configuration.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `config_id` | `string` | Identifier of the managed configuration to associate with the devices.<br/>Example: 2836d89d-1e98-4377-92b7-0a76ac2a7699 |
| `type` | `integer` | Type of configuration. Currently, only option 2 is supported.<br/>	- 2 — Workstations and servers.<br/>Example: 2 |
| `device_ids` | `array` | List of IDs of devices to link to the specified managed configuration..<br/>Example: cb509c17-7b88-461a-ba3b-3d43e29e6cd4,2c13685e-7d1f-4726-9ad3-5c8fa7718bab |

### Retrieve Devices

Retrieves a list of devices, and additional information, such as the device IP address and operating system.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `$top` | `integer` | Specifies the number of objects to retrieve.<br/>Example: 5 |
| `$skip` | `integer` | Bypasses the specified number of objects in the results returned.<br/>For example, if you specify 10, the results start at object 11.<br/>Example: 5 |
| `$search` | `string` | Returns only objects that include the specified text string. For example, "name" returns objects that include "hostname" and "username".<br/>The supported search fields depend on the endpoint:<br/>	- Devices: Host name, description, IP address, logged on user<br/>	- DeviceProtectionStatus: Host name<br/>	- ManagedConfigurations: Name, description<br/>Example: name |
| `$count` | `boolean` | Indicates whether to return a counter that shows the total number of objects in the total_items response parameter.<br/>Example: true |
| `$orderby` | `string` | Specifies how to order results. You can order by any parameter in the response and sort results in ascending or descending order.<br/>Specify a parameter name with any underscores removed, followed by a + (plus sign) and either asc (ascending) or desc (descending).<br/>For example, to order results by the host_name parameter in descending order, specify hostname+desc. If you do not specify a field to order by, the API will use the order in the database.<br/>Example: hostname+desc |
| `$config` | `boolean` | Indicates whether the security configuration name and ID are returned. The default value is true.<br/>Example: true |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `total_items` | `integer` | Total number of devices.<br/>If the count request parameter is true, total_items displays the total number of devices. If count is false, then total_items displays null.<br/>Example: 42 |
| `data` | `array` | Array of device data |

### Retrieve Managed Configurations

Retrieves a list of the specified type of managed configurations associated with your WatchGuard Cloud account.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `integer` | Type of configuration to return. Specify one of these values:<br/>	- 1 — Deployment settings<br/>	- 2 — Workstations and servers<br/>	- 3 — Android<br/>Example: 2 |
| `$top` | `integer` | Specifies the number of objects to retrieve.<br/>Example: 5 |
| `$skip` | `integer` | Bypasses the specified number of objects in the results returned.<br/>For example, if you specify 10, the results start at object 11.<br/>Example: 5 |
| `$search` | `string` | Returns only objects that include the specified text string. For example, "name" returns objects that include "hostname" and "username".<br/>The supported search fields depend on the endpoint:<br/>	- Devices: Host name, description, IP address, logged on user<br/>	- DeviceProtectionStatus: Host name<br/>	- ManagedConfigurations: Name, description<br/>Example: name |
| `$count` | `boolean` | Indicates whether to return a counter that shows the total number of objects in the total_items response parameter.<br/>Example: true |
| `$orderby` | `string` | Specifies how to order results. You can order by any parameter in the response and sort results in ascending or descending order.<br/>Specify a parameter name with any underscores removed, followed by a + (plus sign) and either asc (ascending) or desc (descending).<br/>For example, to order results by the host_name parameter in descending order, specify hostname+desc. If you do not specify a field to order by, the API will use the order in the database.<br/>Example: hostname+desc |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `total_items` | `integer` | Total number of devices.<br/>If the count request parameter is true, total_items displays the total number of devices. If count is false, then total_items displays null.<br/>Example: 42 |
| `data` | `array` | List of managed configurations. |

### Retrieve unmanaged devices

Retrieves a list of unmanaged devices discovered on the network.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `$top` | `integer` | Specifies the number of objects to retrieve.<br/>Example: 5 |
| `$skip` | `integer` | Bypasses the specified number of objects in the results returned.<br/>For example, if you specify 10, the results start at object 11.<br/>Example: 5 |
| `$search` | `string` | Returns only objects that include the specified text string. For example, "name" returns objects that include "hostname" and "username".<br/>The supported search fields depend on the endpoint:<br/>	- Devices: Host name, description, IP address, logged on user<br/>	- DeviceProtectionStatus: Host name<br/>	- ManagedConfigurations: Name, description<br/>Example: name |
| `$count` | `boolean` | Indicates whether to return a counter that shows the total number of objects in the total_items response parameter.<br/>Example: true |
| `$orderby` | `string` | Specifies how to order results. You can order by any parameter in the response and sort results in ascending or descending order.<br/>Specify a parameter name with any underscores removed, followed by a + (plus sign) and either asc (ascending) or desc (descending).<br/>For example, to order results by the host_name parameter in descending order, specify hostname+desc. If you do not specify a field to order by, the API will use the order in the database.<br/>Example: hostname+desc |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `total_items` | `integer` | Total number of devices.<br/>If the count request parameter is true, total_items displays the total number of devices. If count is false, then total_items displays null.<br/>Example: 42 |
| `data` | `array` | Array of device data |

### Count Security Events

Retrieves counts of detected security events for the specified types.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `integer` | Types of security event counters to retrieve. This parameter is a mask. Add the values of the security event counter types you want to retrieve.<br/>For example, if you want to retrieve only programs blocked, specify 8. If you want to retrieve both PUPs and programs blocked, specify 10 because 8 (programs blocked) + 2 (PUPs) = 10.<br/>	- 1 - Malware<br/>	- 2 PUPs (Potentially Unwanted Programs)<br/>	- 4 - Exploits<br/>	- 8 - Programs Blocked<br/>	- 16 - Threats detected by AV<br/>	- 255 - All counters<br/>Example: 10 |
| `filter` | `string` | Filters the security event counters by date<br/>Specify the type of security event:<br/>	- 33001 — Antivirus<br/>	- 32001 — Other types<br/>Specify the length of the time period in the format [x, y] where x is the number of units and y is the unit of time:<br/>	- 1 — Years<br/>	- 2 - Months<br/>	- 3 - Days<br/>	- 4 - Hours<br/>For example, this retrieves threats detected by AV for the last 7 days: filter=33001%20AmongTheLast%20[7,3].<br/>This retrieves security event counters for the other types for the last 3 months: filter=32001%20AmongTheLast%20[3,2].<br/>If you do not specify a filter, the API returns all of the security events for the last 30 days.<br/>Example: 33001%20AmongTheLast%20[7,3] |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `exploit_counters` | `object` |  |
| `malware_counters` | `object` |  |
| `program_blocked_counters` | `object` |  |
| `pups_counters` | `object` |  |
| `threats_by_av_counters` | `object` |  |

### Retrieve Device Protection Status

Retrieves a list of devices with their protection status and other device information.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `$top` | `integer` | Specifies the number of objects to retrieve.<br/>Example: 5 |
| `$skip` | `integer` | Bypasses the specified number of objects in the results returned.<br/>For example, if you specify 10, the results start at object 11.<br/>Example: 5 |
| `$search` | `string` | Returns only objects that include the specified text string. For example, "name" returns objects that include "hostname" and "username".<br/>The supported search fields depend on the endpoint:<br/>	- Devices: Host name, description, IP address, logged on user<br/>	- DeviceProtectionStatus: Host name<br/>	- ManagedConfigurations: Name, description<br/>Example: name |
| `$count` | `boolean` | Indicates whether to return a counter that shows the total number of objects in the total_items response parameter.<br/>Example: true |
| `$orderby` | `string` | Specifies how to order results. You can order by any parameter in the response and sort results in ascending or descending order.<br/>Specify a parameter name with any underscores removed, followed by a + (plus sign) and either asc (ascending) or desc (descending).<br/>For example, to order results by the host_name parameter in descending order, specify hostname+desc. If you do not specify a field to order by, the API will use the order in the database.<br/>Example: hostname+desc |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `total_items` | `integer` | Total number of devices.<br/>If the count request parameter is true, total_items displays the total number of devices. If count is false, then total_items displays null.<br/>Example: 42 |
| `data` | `array` | Array of device data |

### Retrieve Full Encryption Module Status

Retrieves Full Encryption statistics.

**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `total_supported_devices` | `integer` | Total number of devices that support Full Encryption. |
| `with_decrypting_drives` | `integer` | Number of devices with at least one disk currently in the decryption process. |
| `with_encrypted_by_user_drives` | `integer` | Number of devices where a user encrypted some or all of the disks. |
| `with_encrypted_drives` | `integer` | Number of devices with Full Encryption on all disks. |
| `with_encrypted_partially_by_user_drives` | `integer` | Number of devices where a user encrypted some or all of the disks. Full Encryption encrypts or decrypts the remainder. |
| `with_encrypted_partially_drives` | `integer` | Number of devices with at least one disk with Full Encryption complete. |
| `with_encrypting_drives` | `integer` | Number of devices with at least one disk currently in the encryption process. |
| `with_non_encrypted_drives` | `integer` | Number of devices with no disks encrypted by the user or Full Encryption. |
| `with_unknown_encryption_status` | `integer` | Number of devices with disks encrypted with an authentication method that Full Encryption does not support. |

### Retrieve Patch Management Module Status

Retrieves Patch Management statistics.

**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `non_security_other_patches` | `integer` | Number of other currently available patches that are not related to security. |
| `security_critical` | `integer` | Number of currently available critical security patches. |
| `security_important` | `integer` | Number of currently available security patches classified as important. |
| `security_low` | `integer` | Number of currently available security patches classified as low importance. |
| `security_moderate` | `integer` | Number of currently available security patches classified as moderate importance. |
| `security_not_classified` | `integer` | Number of security patches that do not have a severity classification. |
| `service_pack` | `integer` | Number of currently available service packs. |
| `total_supported_devices` | `integer` | Total number of devices that support Patch Management. |

### Retrieve Security overview

Retrieves counters for security overview.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `period` | `integer` | Period of time to retrieve security event counters for. Specify one of these values:<br/>	- 1 - Previous 24 hours<br/>	- 7 - Previous 7 days<br/>	- 30 - Previous 30 days<br/>Example: 7 |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `exploits` | `` |  |
| `indicators_of_attack_counters` | `` |  |
| `malware` | `` |  |
| `programs_blocked` | `` |  |
| `pups` | `` |  |
| `threats_by_av_counters` | `` |  |
| `total_devices` | `integer` | Total number of devices. |
| `total_unmanaged_devices` | `integer` | Total number of unmanaged devices. |

### Scan devices

Starts a task to scan the specified devices immediately.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `device_ids` | `array` | List of IDs of devices to scan.<br/>Example: "cb509c17-7b88-461a-ba3b-3d43e29e6cd4","2c13685e-7d1f-4726-9ad3-5c8fa7718bab" |
| `task_name` | `string` | Name of the scan task.<br/>Example: Routine scan |
| `task_description` | `string` | Description of the scan task.<br/>Example: Windows 8 machines only |
| `scan_scope` | `integer` | Scope of the scan task. Specify one of these values:<br/>	- 0 - Whole computer<br/>	- 1 - Critical areas<br/>	- 2 - Specified items<br/>Example: 0 |
| `specified_items_to_scan` | `string` | List of specific locations or items to scan. All folders and files in the specified locations are scanned.<br/>Works only when scan_scope is 2.<br/>Example: "C:\Downloads", "C:\Documents" |
| `detect_hacking_tools` | `boolean` | Indicates whether to detect hacking tools. This detects potentially unwanted programs, as well as programs used by hackers.<br/>Example: false |
| `detect_suspicious_files` | `boolean` | Indicates whether to detect suspicious files. In scheduled scans, the tool scans computer software but does not run it. Some types of threats have a lower chance of detection. Set this option to true to scan with heuristic algorithms and improve detection rates.<br/>Example: true |
| `scan_compressed_files` | `boolean` | Indicates whether to scan compressed files. This decompresses compressed files and scans their contents.<br/>Example: true |
| `apply_exclusions_on_scan` | `boolean` | Indicates whether to exclude items from the scan, such as specific files, files with a specific extension, or a specific directory.<br/>Example: false |
| `extensions_to_exclude` | `string` | List of file extensions to exclude from the scan.<br/>Works only when apply_exclusions_on_scan is true.<br/>Example: "exe","pdf" |
| `files_to_exclude` | `string` | List of file names (with their extensions) to exclude from the scan.<br/>Works only when apply_exclusions_on_scan is true.<br/>Example: "Chrome.exe", "Explorer.exe" |
| `folders_to_exclude` | `string` | List of folders to exclude from the scan. You must include the full path.<br/>Works only when apply_exclusions_on_scan is true.<br/>Example: "D:/shared_drive/documents" |
| `execution_window_expiration` | `string` | Time period in which the scan must run before it times out. The default is 7 days.<br/>Example: 8.07:06:05 specifies 8 days, 7 hours, 6 minutes, and 5 seconds |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `no_executed_by_not_found_device_ids` | `array` |  |
| `task_id` | `string` | ID of the completed scan task. |

### Send action

Initiates an action on the specified devices. For example, send an action to reboot a device.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `device_ids` | `array` | List of IDs of devices to reboot.<br/>Example: "cb509c17-7b88-461a-ba3b-3d43e29e6cd4","2c13685e-7d1f-4726-9ad3-5c8fa7718bab" |
| `action_type` | `integer` | Type of action to initiate on the device. Specify one of these values:<br/>	- 1 - Reboot |
| `count_down_type` | `integer` | Amount of time to count down to the action. Specify one of these values:<br/>	- 1 - Immediate<br/>	- 2 - Fifteen minutes<br/>	- 3 - Thirty minutes<br/>	- 4 - One hour<br/>	- 5 - Two hours<br/>	- 6 - Four hours<br/>	- 7 - Eight hours |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `processed_device_ids` | `array` | List of IDs of the rebooted devices |

### Stop devices isolation

Stops isolation on the specified devices.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `device_ids` | `array` | List of IDs of devices to remove from isolation.<br/>Example: "cb509c17-7b88-461a-ba3b-3d43e29e6cd4","2c13685e-7d1f-4726-9ad3-5c8fa7718bab" |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `processed_device_ids` | `array` | List of IDs of the devices removed from isolation |

### Uninstall protection from devices

Uninstalls protection from the specified devices.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `device_ids` | `array` | List of IDs of devices to remove the protection.<br/>Example: "cb509c17-7b88-461a-ba3b-3d43e29e6cd4","2c13685e-7d1f-4726-9ad3-5c8fa7718bab" |


## Extra

Module **`Panda Security` v1.23.1**