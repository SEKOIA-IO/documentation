## OCSF Mapping for Nozomi Devices


**OCSF Class:** `Device Inventory Info`



**Class UID:** `5001`



**OCSF Version:** `1.5.0`


## Information Collected

The Nozomi Devices fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### Nozomi Guardian asset (controller)
Raw asset returned by the Guardian/CMC query API (query=assets)

```json
{
  "name": "plc-01",
  "id": "00000000-0000-4000-8000-000000000001",
  "ip": ["192.0.2.10"],
  "mac_address": ["00:00:5e:00:53:01"],
  "mac_vendor": ["ABB"],
  "os": "",
  "roles": ["producer"],
  "vendor": "ABB",
  "firmware_version": "5.1.100.13",
  "product_name": "AC 800M PM851",
  "serial_number": "",
  "type": "controller",
  "protocols": ["cotp", "mms"],
  "zones": ["Production_B"],
  "levels": ["2"],
  "created_at": "1724888822710",
  "last_activity_time": "1789542303500",
  "device_id": "00000000-0000-4000-8000-0000000000d1"
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `static: 2` | `activity_id` | OCSF activity ID | `integer` | Always 2 for the 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Constant |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Constant |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Constant |
| `static: Device Inventory Info` | `class_name` | OCSF class name | `string` | Constant |
| `static: 5001` | `class_uid` | OCSF class UID | `integer` | Constant |
| `static: Device Inventory Info: Collect` | `type_name` | OCSF type name | `string` | Constant |
| `static: 500102` | `type_uid` | OCSF type UID | `integer` | Constant |
| `asset.created_at` | `time` | OCSF event timestamp | `timestamp` | Convert epoch-milliseconds string to Unix epoch seconds; falls back to now() if missing |
| `asset.id` | `device.uid` | Unique device identifier | `string` | Direct mapping |
| `asset.name || asset.id` | `device.hostname` | Device hostname | `string` | Use asset name, fall back to id (hostname is required) |
| `asset.name` | `device.name` | Device name | `string` | Direct mapping |
| `asset.type` | `device.type / device.type_id` | OCSF device type | `string` | Map Nozomi asset type to OCSF DeviceTypeId (server->1, desktop/workstation->2, mobile->5, virtual->6, firewall->9, switch->10, unknown type->OTHER 99, missing->UNKNOWN 0) |
| `asset.os` | `device.os.name / device.os.type / device.os.type_id` | Operating system | `string` | Normalize os string to OCSF OSTypeStr/OSTypeId; unknown value->OTHER; empty->os omitted |
| `asset.ip[0]` | `device.ip` | Primary IP address | `string` | First IP address of the asset |
| `asset.ip[] + asset.mac_address[]` | `device.network_interfaces[]` | Network interfaces | `object` | The API gives no IP/MAC relationship. Single MAC: one wired interface per IP, each with that MAC (MAC-only interface if no IP). No MAC or several MACs: one IP-only interface per IP plus one MAC-only interface per MAC, so no MAC is dropped and no pairing is invented. Duplicates and empty values are removed |
| `asset.vendor || asset.mac_vendor[0]` | `device.vendor_name` | Device vendor | `string` | Use vendor, fall back to first mac_vendor |
| `asset.product_name` | `device.model` | Device model / product name | `string` | Direct mapping |
| `asset.created_at` | `device.created_time / device.first_seen_time` | Creation / first seen time | `timestamp` | Convert epoch-milliseconds string to Unix epoch seconds |
| `asset.last_activity_time` | `device.last_seen_time` | Last seen time | `timestamp` | Convert epoch-milliseconds string to Unix epoch seconds |
| `asset.firmware_version` | `enrichments[] (name=firmware_version)` | Firmware version enrichment | `string` | Added as enrichment when present |
| `asset.serial_number` | `enrichments[] (name=serial_number)` | Serial number enrichment | `string` | Added as enrichment when present |
| `asset.zones / asset.roles / asset.protocols / asset.levels` | `enrichments[]` | OT context enrichments | `string` | Each non-empty list is joined with ', ' and added as a named enrichment |




### OCSF Model Structure

#### Transformed OCSF Device
The OCSF Device inventory output after transformation

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
  "time": 1724888822.71,
  "metadata": {
    "product": {"name": "Nozomi Networks", "version": "1.0.0"},
    "version": "1.5.0"
  },
  "device": {
    "type": "Other",
    "type_id": 99,
    "uid": "00000000-0000-4000-8000-000000000001",
    "hostname": "plc-01",
    "name": "plc-01",
    "ip": "192.0.2.10",
    "network_interfaces": [
      {
        "hostname": "plc-01",
        "ip": "192.0.2.10",
        "mac": "00:00:5e:00:53:01",
        "type": "Wired",
        "type_id": 1
      }
    ],
    "vendor_name": "ABB",
    "model": "AC 800M PM851",
    "created_time": 1724888822.71,
    "first_seen_time": 1724888822.71,
    "last_seen_time": 1789542303.5
  },
  "enrichments": [
    {"name": "firmware_version", "value": "5.1.100.13"},
    {"name": "zones", "value": "Production_B"},
    {"name": "roles", "value": "producer"},
    {"name": "protocols", "value": "cotp, mms"},
    {"name": "levels", "value": "2"}
  ]
}

```


