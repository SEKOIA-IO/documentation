## OCSF Mapping for Crowdstrike Falcon Devices


**OCSF Class:** `Device Inventory Info`



**Class UID:** `5001`



**OCSF Version:** `1.6.0`


## Information Collected

The Crowdstrike Falcon Devices fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### CrowdStrike falcon device sample
Sample device data from CrowdStrike Falcon API

```json
{
  "device_id": "90111cd1dc1d1beea11cc111f1a11111",
  "cid": "d0f0000b0a000de0ab0000caf0f00fc0",
  "agent_load_flags": "0",
  "agent_local_time": "2025-09-08T12:48:35.942Z",
  "agent_version": "7.27.18003.0",
  "bios_manufacturer": "Xen",
  "bios_version": "4.11.amazon",
  "config_id_base": "66666662",
  "config_id_build": "10000",
  "config_id_platform": "8",
  "cpu_signature": "222222",
  "cpu_vendor": "0",
  "external_ip": "1.2.3.4",
  "mac_address": "00-33-66-11-99-99",
  "instance_id": "i-000b0000000a6000c",
  "service_provider": "AWS_EC2_V2",
  "service_provider_account_id": "333440842243",
  "hostname": "ip-1-2-3-4",
  "filesystem_containment_status": "normal",
  "first_seen": "2025-09-08T12:46:22Z",
  "last_seen": "2025-09-08T12:49:47Z",
  "local_ip": "2.3.0.2",
  "machine_domain": "",
  "major_version": "6",
  "minor_version": "8",
  "os_version": "Ubuntu 24.04",
  "platform_id": "3",
  "platform_name": "Linux",
  "policies": [
    {
      "policy_type": "prevention",
      "policy_id": "00000000d0000b0eb000dd00d000cd10",
      "applied": true,
      "settings_hash": "00a0000c",
      "assigned_date": "2025-09-08T12:47:56.934516164Z",
      "applied_date": "2025-09-08T12:49:50.129791663Z",
      "rule_groups": []
    }
  ],
  "reduced_functionality_mode": "no",
  "device_policies": {
    "prevention": {
      "policy_type": "prevention",
      "policy_id": "01000000d0000b0eb000dd00d0b70011",
      "applied": true,
      "settings_hash": "e0a0000c",
      "assigned_date": "2025-09-08T12:47:56.934516164Z",
      "applied_date": "2025-09-08T12:49:50.129791663Z",
      "rule_groups": []
      "firewall": "enabled"
    }
  },
  "groups": [
  {,
      "id": "default",
      "name": "default",
      "description": "Default group for all devices"
    },
    {
      "id": "managed-endpoints",
      "name": "managed-endpoints"
    }
  ],
  "group_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "product_type_desc": "Server",
  "serial_number": "ec2c0000-0000-0000-0000-70de1a9d92c7",
  "status": "normal",
  "system_manufacturer": "Xen",
  "system_product_name": "HVM domU",
  "tags": [],
  "modified_timestamp": "2025-09-08T12:49:57Z",
  "meta": { "version": "6", "version_string": "31:15400986742" },
  "zone_group": "eu-west-3a",
  "kernel_version": "6.8.0-1026-aws",
  "chassis_type": "1",
  "chassis_type_desc": "Other",
  "pod_labels": [],
  "pod_annotations": [],
  "connection_ip": "11.00.00.00",
  "default_gateway_ip": "11.00.00.00",
  "connection_mac_address": "00-00-00-11-99-99",
  "linux_sensor_mode": "User Mode",
  "deployment_type": "Standard"
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `static: 2` | `activity_id` | OCSF activity ID | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' for asset inventory |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Always 'Discovery' |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: Device Inventory Info` | `class_name` | OCSF class name | `string` | Always 'Device Inventory Info' |
| `static: 5001` | `class_uid` | OCSF class UID | `integer` | Always 5001 for Device Inventory Info |
| `static: 500102` | `type_uid` | OCSF type UID | `integer` | Always 500102 for Device Inventory Info: Collect type |
| `static: Device Inventory Info: Collect` | `type_name` | OCSF type name | `string` | Always 'Device Inventory Info: Collect' for this specific event type |
| `static: Informational` | `severity` | Event severity | `string` | Always 'Informational' for inventory events |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Always 1 for Informational severity |
| `modified_timestamp` | `time` | OCSF event timestamp | `timestamp` | Convert ISO 8601 to Unix epoch; use for OCSF event timestamp; fallback to first_seen |
| `static: CrowdStrike Falcon` | `metadata.product.name` | Source product name | `string` | Always 'CrowdStrike Falcon' |
| `static: N/A` | `metadata.product.version` | Product version | `string` | CrowdStrike API does not provide a single product version field; using 'N/A' |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `device_id` | `device.uid` | Device unique identifier | `string` | Direct mapping of CrowdStrike device unique ID |
| `hostname` | `device.hostname` | Device hostname | `string` | Direct mapping of device hostname |
| `product_type_desc` | `device.type` | Device type | `string` | Map product_type_desc: 'server'→Server, 'workstation'→Desktop, 'desktop'→Desktop, 'laptop'→Laptop, 'mobile'→Mobile, 'tablet'→Tablet, 'virtual'→Virtual |
| `product_type_desc` | `device.type_id` | OCSF device type ID | `integer` | Map device type to OCSF ID: Server→1, Desktop→2, Laptop→8, Mobile→9, Tablet→10, Virtual→16, Unknown→0 |
| `platform_name` | `device.os.type` | Operating system type | `string` | Map platform_name: 'windows'→Windows, 'linux'→Linux, 'mac'→macOS, 'ios'→iOS, 'android'→Android |
| `platform_name` | `device.os.type_id` | OCSF operating system type ID | `integer` | Map OS type to OCSF ID: Windows→100, Linux→200, macOS→300, iOS→400, Android→401, Unknown→0 |
| `os_version` | `device.os.name` | Operating system name with version | `string` | Direct mapping of OS version string (e.g., '10 (Build 19045)', 'Ubuntu 20.04 LTS') |
| `external_ip` | `device.ip` | Primary device IP address | `ip` | Direct mapping of external IP address as primary device IP |
| `local_ip` | `device.network_interfaces[0].ip` | Primary network interface IP address | `ip` | Direct mapping of local IP address for primary interface |
| `mac_address` | `device.network_interfaces[0].mac` | Primary network interface MAC address | `string` | Normalize MAC address to format 'XX:XX:XX:XX:XX:XX' |
| `hostname` | `device.network_interfaces[0].hostname` | Primary interface hostname/DNS name | `string` | Direct mapping of device hostname |
| `static: primary` | `device.network_interfaces[0].name` | Primary interface name | `string` | Always 'primary' for first network interface |
| `connection_ip` | `device.network_interfaces[1].ip` | Connection/external network interface IP address | `ip` | Map connection_ip only if different from local_ip; skip if identical |
| `connection_mac_address` | `device.network_interfaces[1].mac` | Connection interface MAC address | `string` | Normalize MAC address to format 'XX:XX:XX:XX:XX:XX'; only if connection_ip differs from local_ip |
| `static: connection` | `device.network_interfaces[1].name` | Connection interface name | `string` | Always 'connection' for second network interface if it exists |
| `default_gateway_ip` | `device.subnet` | Default gateway/subnet identifier | `ip` | Direct mapping of gateway IP as subnet reference |
| `serial_number` | `device.uid_alt` | Alternative device identifier (serial number) | `string` | Direct mapping of device serial number |
| `machine_domain` | `device.domain` | Device domain membership | `string` | Direct mapping of machine domain |
| `hostname` | `device.name` | Device name | `string` | Direct mapping of device hostname as name |
| `first_seen` | `device.first_seen_time` | First seen timestamp for device | `timestamp` | Transform first_seen to timestamp |
| `last_seen` | `device.last_seen_time` | Last seen timestamp for device | `timestamp` | Transform last_seen to timestamp |
| `first_seen` | `device.created_time` | Device creation timestamp | `timestamp` | Use first_seen as device created_time; convert to timestamp |
| `agent_local_time` | `device.boot_time` | Device boot time (approximation from agent local time) | `timestamp` | Use agent_local_time as proxy for device boot time; convert to timestamp |
| `system_product_name` | `device.model` | Device model name | `string` | Direct mapping of system product name |
| `system_manufacturer` | `device.vendor_name` | Device hardware vendor/manufacturer | `string` | Direct mapping of system manufacturer |
| `bios_manufacturer` | `device.hypervisor` | Hypervisor or BIOS manufacturer | `string` | Direct mapping of BIOS manufacturer (hypervisor for virtual devices) |
| `product_type_desc` | `device.desc` | Device description based on product type | `string` | Direct mapping of product type description |
| `zone_group` | `device.region` | Geographic zone or region | `string` | Direct mapping of zone/region grouping |
| `cid` | `device.org.uid` | Organization/Customer unique identifier | `string` | Direct mapping of CrowdStrike CID (customer ID) |
| `service_provider` | `device.org.name` | Organization name | `string` | Direct mapping of service provider as organization name |
| `id` | `device.groups[].uid` | Unique identifier for device group membership | `string` | Map each group ID to device.groups array with uid |
| `name` | `device.groups[].name` | Name of device group membership | `string` | Map each group name to device.groups array with name |
| `desc` | `device.groups[].desc` | Description of device group membership | `string` | Optional description for device group; not provided in CrowdStrike API, set to null or default value |
| `zone_group` | `device.location.region` | Device geographic region (mapped from zone_group) | `string` | Map zone_group to device location region; use same value as device.region for consistency |
| `static: True` | `device.is_managed` | Whether device is under active management | `boolean` | Set to true because it's managed by crowdstrike falcon |
| `status + reduced_functionality_mode + filesystem_containment_status` | `device.is_compliant` | Device compliance status | `boolean` | true if status='normal' AND reduced_functionality_mode='no' AND filesystem_containment_status='normal'; else false; null if unable to determine |
| `static: compliance` | `enrichment[].name` | Enrichement compliance name | `string` | Always 'compliance' for this enrichment type |
| `static: hygiene` | `enrichment[].value` | Enrichement compliance value | `string` | Always 'hygiene' for this enrichment value |
| `device_policies.firewall` | `enrichment[].data.Firwall_status` | Enrichement data value | `string` | If firwall is enabled, set to 'enabled'; if disabled, set to 'disabled'' |




### OCSF Model Structure

#### Device Inventory Info
Transformed CrowdStrike falcon api response to OCSF Device Inventory Info

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
  "time": 1725011130,
  "metadata": {
    "product": {
      "name": "CrowdStrike Falcon",
      "version": "7.8.0.0"
    },
    "version": "1.6.0"
  },
  "device": {
    "uid": "abc000def000ghi000",
    "uid_alt": "1A2B3C4D5E6F",
    "name": "WORKSTATIONTEST-001",
    "hostname": "WORKSTATIONTEST-001",
    "type": "Desktop",
    "type_id": 2,
    "vendor_name": "Dell Inc.",
    "model": "OptiPlex 7090",
    "hypervisor": "Dell Inc.",
    "ip": "1.1.1.1",
    "domain": "example.com",
    "region": "US-EAST",
    "state": "Normal",
    "agent_version": "7.8.0.0",
    "is_managed": true,
    "is_compliant": true,
    "created_time": 1705329000,
    "boot_time": 1725011130,
    "updated_time": 1725011130,
    "subnet": "192.168.1.1",
    "desc": "Workstation - Windows",
    "os": {
      "name": "10 (Build 19045)",
      "type": "Windows",
      "type_id": 100
    },
    "network_interfaces": [
      {
        "name": "primary",
        "ip": "192.168.1.100",
        "hostname": "WORKSTATION-001",
        "mac": "00:1A:2B:3C:4D:5E"
      }
    ],
    "groups": [
      {
        "uid": "default",
        "name": "default"
      },
      {
        "uid": "managed-endpoints",
        "name": "managed-endpoints"
      }
    ],
    "org": {
      "uid": "abc123def456",
      "name": "CrowdStrike"
    }
  }
}

```


