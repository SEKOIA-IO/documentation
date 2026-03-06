## OCSF Mapping for SentinelOne Devices


**OCSF Class:** `device_inventory_info`



**Class UID:** `5001`




## Information Collected

The SentinelOne Devices fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### SentinelOne Active Device
SentinelOne device with active status and protection enabled

```json
{
  "id": "475482087580431375",
  "name": "LAPTOP-JOHN-DEV",
  "type": "computer",
  "osType": "windows",
  "osVersion": "Windows 10 Pro",
  "osRevision": "22H2",
  "machineType": "laptop",
  "manufacturer": "Dell",
  "modelName": "Latitude 5540",
  "serialNumber": "ABC123DEF456GHI",
  "processorCount": 8,
  "coreCount": 8,
  "memorySize": 16384,
  "ipv4Addresses": [
    "192.168.1.100",
    "10.0.0.50"
  ],
  "ipv6Addresses": [
    "fe80::1234:5678:90ab:cdef"
  ],
  "macAddresses": [
    "00:1A:2B:3C:4D:5E"
  ],
  "isActive": true,
  "isOnline": true,
  "lastActiveDate": "2025-08-26T09:30:00.000Z",
  "createdDate": "2023-06-04T10:00:00.000Z",
  "updatedDate": "2025-08-26T09:30:00.000Z",
  "agentVersion": "23.4.1.1001",
  "agentStatus": "active",
  "threatLevel": "good",
  "encryptionEnabled": true,
  "isFirewallEnabled": true,
  "isTamperProtectionEnabled": true,
  "lastIncidentDate": null,
  "threatCount": 0,
  "domain": "example.com",
  "computerName": "LAPTOP-JOHN-DEV",
  "userId": "u1234567890abcdef",
  "userName": "john.developer@example.com",
  "userFullName": "John Developer"
}

```

#### SentinelOne Inactive Device
SentinelOne device with inactive status

```json
{
  "id": "475482087580431376",
  "name": "SERVER-OLD-PROD",
  "type": "server",
  "osType": "linux",
  "osVersion": "Ubuntu 18.04.6 LTS",
  "osRevision": "5.4.0-42-generic",
  "machineType": "server",
  "manufacturer": "HP",
  "modelName": "ProLiant DL380 Gen10",
  "serialNumber": "SG12345678",
  "processorCount": 16,
  "coreCount": 32,
  "memorySize": 131072,
  "ipv4Addresses": [
    "10.0.0.200"
  ],
  "ipv6Addresses": [],
  "macAddresses": [
    "00:30:48:2E:3A:A8"
  ],
  "isActive": false,
  "isOnline": false,
  "lastActiveDate": "2025-06-01T14:30:00.000Z",
  "createdDate": "2021-03-15T08:00:00.000Z",
  "updatedDate": "2025-08-26T09:30:00.000Z",
  "agentVersion": "21.8.2.998",
  "agentStatus": "inactive",
  "threatLevel": "unknown",
  "encryptionEnabled": false,
  "isFirewallEnabled": true,
  "isTamperProtectionEnabled": false,
  "lastIncidentDate": "2025-05-20T10:00:00.000Z",
  "threatCount": 0,
  "domain": "example.com",
  "computerName": "SERVER-OLD-PROD",
  "userId": null,
  "userName": null,
  "userFullName": null
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `id` | `device.uid` | SentinelOne device unique identifier | `string` | Direct mapping of SentinelOne device ID |
| `name` | `device.name` | Device display name | `string` | Direct mapping of device name |
| `computerName` | `device.hostname` | Device hostname | `string` | Direct mapping of computer name |
| `domain` | `device.domain` | Network domain name | `string` | Direct mapping of domain |
| `osType` | `device.os.name` | Operating system type | `string` | Direct mapping of OS type (windows, linux, macos) |
| `osType` | `device.os.type` | Operating system type enumeration | `string` | Map osType to OCSF OS type enum (Windows, AppleOS, Linux) |
| `osVersion` | `device.os.version` | Operating system version | `string` | Direct mapping of OS version |
| `osRevision` | `device.os.build` | Operating system build/revision number | `string` | Direct mapping of OS revision/build number |
| `serialNumber` | `device.serial_number` | Device serial number | `string` | Direct mapping of device serial number |
| `manufacturer` | `device.manufacturer` | Device manufacturer | `string` | Direct mapping of device manufacturer |
| `modelName` | `device.model` | Device model name | `string` | Direct mapping of device model |
| `processorCount` | `device.cpu_count` | Number of processors | `integer` | Direct mapping of processor count |
| `coreCount` | `device.core_count` | Number of CPU cores | `integer` | Direct mapping of core count |
| `memorySize` | `device.memory_size` | Total memory size in megabytes | `integer` | Direct mapping of memory size in MB |
| `ipv4Addresses | first` | `device.ip` | Primary IPv4 address | `string` | Extract first IPv4 address |
| `ipv4Addresses` | `device.ipv4_addresses` | All IPv4 addresses associated with device | `array[string]` | Direct mapping of all IPv4 addresses |
| `ipv6Addresses` | `device.ipv6_addresses` | All IPv6 addresses associated with device | `array[string]` | Direct mapping of all IPv6 addresses |
| `macAddresses | first` | `device.mac_address` | Primary MAC address | `string` | Extract first MAC address |
| `macAddresses` | `device.mac_addresses` | All MAC addresses associated with device | `array[string]` | Direct mapping of all MAC addresses |
| `type` | `device.type` | Device type classification | `string` | Direct mapping of device type (computer, server, etc.) |
| `machineType` | `device.machine_type` | Machine type (laptop, desktop, server, etc.) | `string` | Direct mapping of machine type (laptop, desktop, server, etc.) |
| `isActive` | `device.is_enabled` | Whether device is active in SentinelOne | `boolean` | Direct mapping of active status |
| `isOnline` | `device.is_online` | Whether device is currently online | `boolean` | Direct mapping of online status |
| `agentStatus` | `device.agent_status` | SentinelOne agent status | `string` | Direct mapping of agent status (active, inactive, uninstalled) |
| `agentVersion` | `device.agent_version` | SentinelOne agent version | `string` | Direct mapping of agent version |
| `threatLevel` | `device.threat_level` | Device threat level | `string` | Direct mapping of threat level (good, suspicious, bad, unknown) |
| `threatCount` | `device.threat_count` | Number of threats detected on device | `integer` | Direct mapping of threat count |
| `lastIncidentDate` | `device.last_incident_time` | Last incident timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch; null if no incidents |
| `encryptionEnabled` | `device.is_encrypted` | Whether disk encryption is enabled | `boolean` | Direct mapping of encryption status |
| `isFirewallEnabled` | `device.is_firewall_enabled` | Whether firewall is enabled | `boolean` | Direct mapping of firewall status |
| `isTamperProtectionEnabled` | `device.is_tamper_protected` | Whether tamper protection is enabled | `boolean` | Direct mapping of tamper protection status |
| `userId` | `device.user_uid` | Associated user ID | `string` | Direct mapping of associated user ID; null if not applicable |
| `userName` | `device.user_name` | Associated user name | `string` | Direct mapping of associated user name |
| `userFullName` | `device.user_full_name` | Associated user full name | `string` | Direct mapping of associated user full name |
| `createdDate` | `device.created_time` | Device creation timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch |
| `updatedDate` | `device.updated_time` | Last updated timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch |
| `lastActiveDate` | `device.last_seen_time` | Last active timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch; null if never active |
| `createdDate` | `time` | OCSF event timestamp (device discovery time) | `integer` | Convert ISO 8601 to Unix epoch for OCSF event timestamp |
| `static: 2` | `activity_id` | OCSF activity ID for inventory collection | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Always 'Discovery' |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: Device Inventory Info` | `class_name` | OCSF class name | `string` | Always 'Device Inventory Info' |
| `static: 5001` | `class_uid` | OCSF class UID | `integer` | Always 5001 for Device Inventory Info |
| `computed: 500100 + activity_id` | `type_uid` | OCSF type UID | `integer` | Base 500100 + activity_id (2 = 500102) |
| `computed: class_name + ': ' + activity_name` | `type_name` | OCSF type name | `string` | Concatenate 'Device Inventory Info: Collect' |
| `static: Informational` | `severity` | Event severity level | `string` | Always 'Informational' for inventory events |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Always 1 for Informational severity |
| `static: SentinelOne` | `metadata.product.name` | Source product name | `string` | Always 'SentinelOne' |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `threatLevel` | `enrichments[0].data.threat_level` | Device threat level for security posture | `string` | Direct mapping of threat level |
| `threatCount` | `enrichments[0].data.threat_count` | Number of active threats | `integer` | Direct mapping of threat count |
| `isActive` | `enrichments[0].data.is_enabled` | Whether device is active | `boolean` | Direct mapping of active status |
| `agentStatus` | `enrichments[0].data.agent_status` | SentinelOne agent status | `string` | Direct mapping of agent status |
| `agentVersion` | `enrichments[0].data.agent_version` | SentinelOne agent version | `string` | Direct mapping of agent version |
| `encryptionEnabled` | `enrichments[0].data.is_encrypted` | Whether device is encrypted | `boolean` | Direct mapping of encryption status |
| `isFirewallEnabled` | `enrichments[0].data.is_firewall_enabled` | Whether firewall is enabled | `boolean` | Direct mapping of firewall status |
| `isTamperProtectionEnabled` | `enrichments[0].data.is_tamper_protected` | Whether tamper protection is enabled | `boolean` | Direct mapping of tamper protection status |
| `lastActiveDate` | `enrichments[0].data.last_seen` | Last active timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix timestamp; null if never active |
| `static: device_security` | `enrichments[0].name` | Enrichment object name | `string` | Always 'device_security' for device enrichment type |
| `static: sentinelone_device` | `enrichments[0].value` | Enrichment object value | `string` | Always 'sentinelone_device' for SentinelOne device security enrichment |




### OCSF Model Structure

#### Device Inventory Info: Collect
Transformed SentinelOne device to OCSF Device Inventory Info event

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
  "time": 1685854800,
  "metadata": {
    "product": {
      "name": "SentinelOne"
    },
    "version": "1.6.0"
  },
  "device": {
    "uid": "475482087580431375",
    "name": "LAPTOP-JOHN-DEV",
    "hostname": "LAPTOP-JOHN-DEV",
    "domain": "example.com",
    "type": "computer",
    "machine_type": "laptop",
    "serial_number": "ABC123DEF456GHI",
    "manufacturer": "Dell",
    "model": "Latitude 5540",
    "cpu_count": 8,
    "core_count": 8,
    "memory_size": 16384,
    "ip": "192.168.1.100",
    "ipv4_addresses": [
      "192.168.1.100",
      "10.0.0.50"
    ],
    "ipv6_addresses": [
      "fe80::1234:5678:90ab:cdef"
    ],
    "mac_address": "00:1A:2B:3C:4D:5E",
    "mac_addresses": [
      "00:1A:2B:3C:4D:5E"
    ],
    "is_enabled": true,
    "is_online": true,
    "is_encrypted": true,
    "is_firewall_enabled": true,
    "is_tamper_protected": true,
    "threat_level": "good",
    "threat_count": 0,
    "agent_status": "active",
    "agent_version": "23.4.1.1001",
    "user_uid": "u1234567890abcdef",
    "user_name": "john.developer@example.com",
    "user_full_name": "John Developer",
    "created_time": 1685854800,
    "updated_time": 1725184200,
    "last_seen_time": 1725184200,
    "last_incident_time": null,
    "os": {
      "name": "windows",
      "type": "Windows",
      "version": "Windows 10 Pro",
      "build": "22H2"
    }
  },
  "enrichments": [
    {
      "name": "device_security",
      "value": "sentinelone_device",
      "data": {
        "threat_level": "good",
        "threat_count": 0,
        "is_enabled": true,
        "agent_status": "active",
        "agent_version": "23.4.1.1001",
        "is_encrypted": true,
        "is_firewall_enabled": true,
        "is_tamper_protected": true,
        "last_seen": 1725184200
      }
    }
  ]
}

```


