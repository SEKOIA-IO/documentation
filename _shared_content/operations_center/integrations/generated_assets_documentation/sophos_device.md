## OCSF Mapping for Sophos EDR Device Assets


**OCSF Class:** `Device Inventory Info`



**Class UID:** `5001`



**OCSF Version:** `1.6.0`


## Information Collected

The Sophos EDR Device Assets fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### Sophos EDR endpoint sample
Sample endpoint data from Sophos Central API GET /endpoint/v1/endpoints

```json
{
  "id": "00000000-0000-0000-0000-000000000001",
  "type": "computer",
  "tenant": {
    "id": "00000000-0000-0000-0000-000000000010"
  },
  "hostname": "example-workstation",
  "health": {
    "overall": "bad",
    "threats": { "status": "good" },
    "services": { "status": "bad" }
  },
  "os": {
    "isServer": false,
    "platform": "windows",
    "name": "Windows 10 Pro",
    "majorVersion": 10,
    "minorVersion": 0,
    "build": 19044
  },
  "ipv4Addresses": ["192.0.2.10"],
  "ipv6Addresses": [],
  "macAddresses": ["00:00:5E:00:53:01"],
  "tamperProtectionEnabled": true,
  "mdrManaged": false,
  "associatedPerson": {
    "name": "example-workstation\\\\user",
    "id": "00000000-0000-0000-0000-000000000020"
  },
  "group": {
    "id": "00000000-0000-0000-0000-000000000030",
    "name": "Workstations"
  },
  "lastSeenAt": "2024-01-07T06:26:08.668Z",
  "registeredAt": "2023-06-26T10:28:08.836Z",
  "online": false,
  "cloud": { "provider": "azure", "instanceId": "00000000-0000-0000-0000-000000000040" },
  "isolation": { "status": "notIsolated", "adminIsolated": false, "selfIsolated": false }
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic                                                                                                                                                                                                               |
|--------------|-----------------|-------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static: 2` | `activity_id` | OCSF activity ID – always 2 for Collect | `integer` | -                                                                                                                                                                                                                   |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | -                                                                                                                                                                                                                   |
| `static: Discovery` | `category_name` | OCSF category name | `string` | -                                                                                                                                                                                                                   |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | -                                                                                                                                                                                                                   |
| `static: Device Inventory Info` | `class_name` | OCSF class name | `string` | -                                                                                                                                                                                                                   |
| `static: 5001` | `class_uid` | OCSF class UID | `integer` | -                                                                                                                                                                                                                   |
| `static: 500102` | `type_uid` | OCSF type UID | `integer` | -                                                                                                                                                                                                                   |
| `static: Device Inventory Info: Collect` | `type_name` | OCSF type name | `string` | -                                                                                                                                                                                                                   |
| `static: Informational` | `severity` | Event severity | `string` | -                                                                                                                                                                                                                   |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | -                                                                                                                                                                                                                   |
| `lastSeenAt` | `time` | OCSF event timestamp | `timestamp` | Convert ISO 8601 to Unix epoch; fallback to registeredAt then now()                                                                                                                                                 |
| `static: Sophos EDR` | `metadata.product.name` | Source product name | `string` | -                                                                                                                                                                                                                   |
| `static: N/A` | `metadata.product.version` | Product version | `string` | -                                                                                                                                                                                                                   |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | -                                                                                                                                                                                                                   |
| `id` | `device.uid` | Sophos endpoint UUID | `string` | -                                                                                                                                                                                                                   |
| `hostname` | `device.hostname` | Device hostname | `string` | -                                                                                                                                                                                                                   |
| `hostname` | `device.name` | Device name (same as hostname) | `string` | -                                                                                                                                                                                                                   |
| `type` | `device.type / device.type_id` | OCSF device type | `string` | computer → Desktop (2), server → Server (1), else Unknown (0)                                                                                                                                                       |
| `os.platform` | `device.os.type / device.os.type_id` | OCSF OS type | `string` | windows→Windows(100), linux→Linux(200), macos→macOS(300), android→Android(201)                                                                                                                                      |
| `os.name` | `device.os.name` | Full OS name (e.g. 'Windows 10 Pro') | `string` | -                                                                                                                                                                                                                   |
| `ipv4Addresses[0] or ipv6Addresses[0]` | `device.ip` | Primary IP address | `ip` | Prefer first IPv4; fallback to first IPv6 if no IPv4 available                                                                                                                                                      |
| `ipv4Addresses[]` | `device.network_interfaces[].ip` | Network interface IPv4 addresses | `ip` | One NetworkInterface per IPv4; paired with matching MAC by index; hostname set on first interface only                                                                                                              |
| `ipv6Addresses[]` | `device.network_interfaces[].ip` | IPv6 network interface addresses | `ip` | Additional interfaces for IPv6 addresses (appended after IPv4 interfaces)                                                                                                                                           |
| `macAddresses[]` | `device.network_interfaces[].mac` | Network interface MAC addresses | `string` | Normalised to XX:XX:XX:XX:XX:XX uppercase; dashes replaced by colons; paired with IP by index                                                                                                                       |
| `hostname` | `device.network_interfaces[0].hostname` | Hostname on primary interface only | `string` | -                                                                                                                                                                                                                   |
| `group[].id / group[].name` | `device.groups[].uid / device.groups[].name` | Device group membership (Sophos group field) | `object` | Map Sophos group array (each with id and name) to OCSF Group objects; only groups with a name are included                                                                                                          |
| `tenant.id` | `device.org.uid / device.org.name` | Sophos tenant UUID used as both uid and name (no display name available from API) | `string` | -                                                                                                                                                                                                                   |
| `cloud.provider` | `device.region` | Cloud provider (azure, aws, gcp, …) | `string` | -                                                                                                                                                                                                                   |
| `associatedPerson.name` | `device.desc` | Associated user login name set as device description | `string` | -                                                                                                                                                                                                                   |
| `registeredAt` | `device.first_seen_time / device.created_time` | Endpoint registration date – used for both first_seen_time and created_time | `timestamp` | -                                                                                                                                                                                                                   |
| `lastSeenAt` | `device.last_seen_time` | Last seen date | `timestamp` | -                                                                                                                                                                                                                   |
| `static: True` | `device.is_managed` | Always true – device is enrolled in Sophos Central | `boolean` | -                                                                                                                                                                                                                   |
| `health.overall` | `device.is_compliant` | Device health / compliance status | `boolean` | good→True, bad/suspicious→False, else None                                                                                                                                                                          |
| `health.overall + isolation.status + tamperProtectionEnabled` | `device.is_trusted` | Computed trust status based on isolation, health and tamper protection | `boolean` | Calculated with 3 fields health.overall, isolation.status and tamperProtectionEnabled                                                                                                                                                      |
| `lastSeenAt (max across all items in collection run)` | `context.last_seen_cursor` | Incremental collection checkpoint | `string` | The most recent lastSeenAt ISO string seen during a collection run is persisted as the checkpoint. On the next run, this value is passed as lastSeenAfter query parameter to avoid re-fetching already-seen devices. |
| `tamperProtectionEnabled` | `enrichments[0].data.Firewall_status` | Tamper-protection / firewall-like status | `string` | true→Enabled, false→Disabled; used as proxy for endpoint protection status                                                                                                                                          |
| `static: compliance` | `enrichments[0].name` | Enrichment type name | `string` | -                                                                                                                                                                                                                   |
| `static: hygiene` | `enrichments[0].value` | Enrichment value | `string` | -                                                                                                                                                                                                                   |




### OCSF Model Structure

#### Device Inventory Info – Sophos EDR
Transformed Sophos endpoint to OCSF Device Inventory Info

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
  "time": 1704610568,
  "metadata": {
    "product": { "name": "Sophos EDR", "version": "N/A" },
    "version": "1.6.0"
  },
  "device": {
    "uid": "00000000-0000-0000-0000-000000000001",
    "hostname": "example-workstation",
    "name": "example-workstation",
    "desc": "example-workstation\\user",
    "type": "Desktop",
    "type_id": 2,
    "os": { "name": "Windows 10 Pro", "type": "windows", "type_id": 100 },
    "ip": "192.0.2.10",
    "network_interfaces": [
      {
        "hostname": "example-workstation",
        "ip": "192.0.2.10",
        "mac": "00:00:5E:00:53:01",
        "name": "eth0"
      }
    ],
    "groups": [
      {
        "uid": "00000000-0000-0000-0000-000000000030",
        "name": "Workstations"
      }
    ],
    "org": {
      "uid": "00000000-0000-0000-0000-000000000010",
      "name": "00000000-0000-0000-0000-000000000010"
    },
    "region": "azure",
    "is_managed": true,
    "is_compliant": false,
    "is_trusted": false,
    "first_seen_time": 1687773488,
    "created_time": 1687773488,
    "last_seen_time": 1704610568
  },
  "enrichments": [
    {
      "name": "compliance",
      "value": "hygiene",
      "data": { "Firewall_status": "Enabled" }
    }
  ]
}

```


