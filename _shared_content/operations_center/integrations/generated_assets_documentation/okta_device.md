## OCSF Mapping for Okta Devices


**OCSF Class:** `Device Inventory Info`



**Class UID:** `5001`




## Information Collected

The Okta Devices fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### Okta Managed Device
Okta managed device with active compliance status

```json
{
  "id": "gooabc123defGHIJKL",
  "status": "ACTIVE",
  "created": "2023-06-04T10:00:00.000Z",
  "lastUpdated": "2025-08-26T09:30:00.000Z",
  "lastSeen": "2025-08-26T09:30:00.000Z",
  "profile": {
    "displayName": "LAPTOP-MARY-001",
    "platform": "Windows",
    "osVersion": "10.0.22621",
    "serialNumber": "ABC123DEF456",
    "imei": null,
    "manufacturer": "Dell",
    "model": "Latitude 5540",
    "udid": null,
    "registered": true,
    "secureHardwarePresent": true,
    "diskEncryptionType": "BitLocker",
    "osUpdateTime": "2025-08-20T14:30:00.000Z"
  },
  "deviceType": "Computer",
  "managed": true,
  "complianceStatus": "COMPLIANT",
  "userId": "00u1a2b3c4d5e6f7g8h9",
  "_links": {
    "self": [
      {
      [...]
    ]
  }
}

```

#### Okta Non-Compliant Device
Okta device with non-compliant status

```json
{
  "id": "goodef456ghiJKLMNO",
  "status": "ACTIVE",
  "created": "2023-04-15T08:00:00.000Z",
  "lastUpdated": "2025-08-26T09:30:00.000Z",
  "lastSeen": "2025-08-26T09:30:00.000Z",
  "profile": {
    "displayName": "iPhone-ROBERT-001",
    "platform": "iOS",
    "osVersion": "17.5.1",
    "serialNumber": "A2R4P7B9C1D2E3F4G5",
    "imei": "356938035643809",
    "manufacturer": "Apple",
    "model": "iPhone 14 Pro",
    "udid": "00008120-0015E40A2E59801E",
    "registered": true,
    "secureHardwarePresent": true,
    "diskEncryptionType": "FileVault",
    "osUpdateTime": "2025-08-01T10:00:00.000Z"
  },
  "deviceType": "MobileDevice",
  "managed": true,
  "complianceStatus": "NON_COMPLIANT",
  "userId": "00u2c3d4e5f6g7h8i9j0",
  "_links": {
    "self": [
      {
      [...]
    ]
  }
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `id` | `device.uid` | Okta device unique identifier | `string` | Direct mapping of Okta device ID |
| `profile.displayName` | `device.name` | Device display name | `string` | Direct mapping of display name |
| `profile.displayName` | `device.hostname` | Device hostname (from display name) | `string` | Direct mapping of display name as hostname |
| `profile.platform` | `device.os.name` | Operating system platform | `string` | Direct mapping of platform (Windows, iOS, Android, MacOS) |
| `profile.platform` | `device.os.type` | Operating system type | `string` | Map platform to OS type enum (Windows, AppleOS, Android, Linux) |
| `profile.osVersion` | `device.os.version` | Operating system version | `string` | Direct mapping of OS version |
| `profile.serialNumber` | `device.serial_number` | Device serial number | `string` | Direct mapping of device serial number |
| `profile.manufacturer` | `device.manufacturer` | Device manufacturer (Dell, Apple, Samsung, etc.) | `string` | Direct mapping of device manufacturer |
| `profile.model` | `device.model` | Device model | `string` | Direct mapping of device model |
| `profile.imei` | `device.imei` | International Mobile Equipment Identity | `string` | Direct mapping of IMEI (for mobile devices) |
| `profile.udid` | `device.udid` | Unique Device Identifier (iOS/MacOS) | `string` | Direct mapping of UDID (Apple devices) |
| `deviceType` | `device.type` | Device type classification | `string` | Direct mapping of device type (Computer, MobileDevice, etc.) |
| `status` | `device.is_enabled` | Whether device is enabled (ACTIVE status) | `boolean` | true if status is 'ACTIVE', false otherwise |
| `status` | `device.status` | Device status (ACTIVE, SUSPENDED, DEPROVISIONED) | `string` | Direct mapping of device status |
| `managed` | `device.is_managed` | Whether device is managed by Okta | `boolean` | Direct mapping of managed status |
| `complianceStatus` | `device.compliance_status` | Device compliance status (COMPLIANT, NON_COMPLIANT, UNKNOWN) | `string` | Direct mapping of compliance status |
| `profile.secureHardwarePresent` | `device.has_secure_hardware` | Whether device has secure hardware (TPM, Secure Enclave) | `boolean` | Direct mapping of secure hardware presence |
| `profile.diskEncryptionType` | `device.encryption_type` | Disk encryption type (BitLocker, FileVault, etc.) | `string` | Direct mapping of disk encryption type |
| `profile.registered` | `device.is_registered` | Whether device is registered with Okta | `boolean` | Direct mapping of registered status |
| `userId` | `device.user_uid` | Okta user ID associated with device | `string` | Direct mapping of associated user ID |
| `created` | `device.created_time` | Device creation timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch |
| `lastUpdated` | `device.updated_time` | Last updated timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch |
| `lastSeen` | `device.last_seen_time` | Last seen timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch; null if never seen |
| `profile.osUpdateTime` | `device.os_update_time` | Last OS update timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch; null if not available |
| `created` | `time` | OCSF event timestamp (device discovery time) | `integer` | Convert ISO 8601 to Unix epoch for OCSF event timestamp |
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
| `static: Okta` | `metadata.product.name` | Source product name | `string` | Always 'Okta' |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `complianceStatus` | `enrichments[0].data.compliance_status` | Device compliance status for security posture | `string` | Direct mapping of compliance status |
| `status` | `enrichments[0].data.is_enabled` | Whether device is enabled | `boolean` | true if status is 'ACTIVE', false otherwise |
| `managed` | `enrichments[0].data.is_managed` | Whether device is managed by Okta | `boolean` | Direct mapping of managed status |
| `profile.secureHardwarePresent` | `enrichments[0].data.has_secure_hardware` | Whether device has secure hardware | `boolean` | Direct mapping of secure hardware presence |
| `profile.diskEncryptionType` | `enrichments[0].data.encryption_type` | Disk encryption type for security compliance | `string` | Direct mapping of disk encryption type |
| `lastSeen` | `enrichments[0].data.last_seen` | Last seen timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix timestamp; null if never seen |
| `static: device_security` | `enrichments[0].name` | Enrichment object name | `string` | Always 'device_security' for device enrichment type |
| `static: okta_device` | `enrichments[0].value` | Enrichment object value | `string` | Always 'okta_device' for Okta device security enrichment |




### OCSF Model Structure

#### Device Inventory Info: Collect
Transformed Okta device to OCSF Device Inventory Info event

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
      "name": "Okta"
    },
    "version": "1.6.0"
  },
  "device": {
    "uid": "gooabc123defGHIJKL",
    "name": "LAPTOP-MARY-001",
    "hostname": "LAPTOP-MARY-001",
    "type": "Computer",
    "serial_number": "ABC123DEF456",
    "manufacturer": "Dell",
    "model": "Latitude 5540",
    "is_enabled": true,
    "status": "ACTIVE",
    "is_managed": true,
    "is_registered": true,
    "compliance_status": "COMPLIANT",
    "has_secure_hardware": true,
    "encryption_type": "BitLocker",
    "user_uid": "00u1a2b3c4d5e6f7g8h9",
    "created_time": 1685854800,
    "updated_time": 1725184200,
    "last_seen_time": 1725184200,
    "os_update_time": 1724044200,
    "os": {
      "name": "Windows",
      "type": "Windows",
      "version": "10.0.22621"
    }
  },
  "enrichments": [
    {
      "name": "device_security",
      "value": "okta_device",
      "data": {
        "compliance_status": "COMPLIANT",
        "is_enabled": true,
        "is_managed": true,
        "has_secure_hardware": true,
        "encryption_type": "BitLocker",
        "last_seen": 1725184200
      }
    }
  ]
}

```


