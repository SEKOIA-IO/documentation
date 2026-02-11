uuid: adcd0095-0f3d-4699-8621-158977b6c2c3
name: Crowdstrike Falcon devices
type: asset

## Overview

CrowdStrike Falcon is an Endpoint Detection and Response solution. This setup guide shows how to forward device assets created in CrowdStrike Falcon to Sekoia.io.

- **Vendor**: CrowdStrike
- **Product**: CrowdStrike Falcon
- **Supported environment**: SaaS

## Configure

### How to create an API token

To connect CrowdStrike Falcon to Sekoia.io, you need to create an API key pair (Client id and Client secret) in your CrowdStrike Falcon console. Follow these steps:

1. Log in to the CrowdStrike interface.

2. Click on the burger menu and go to Support and `resources` > `Resources and tools` > `API client and keys`.

    ![Account page showing navigation to API Keys tab in CrowdStrike](/assets/operation_center/asset_connectors/device/crowdstrike_falcon/api_key_button.png)

3. In the `OAuth2 API Clients` tab, create a new `OAuth2 API Client` with the `Read` and `Write` permissions for the scopes `User Management`.

    ![Generate API Keys button highlighted for clarity](/assets/operation_center/asset_connectors/device/crowdstrike_falcon/create_api_key.png)

4. Copy the api key in a safe place and start using it in Sekoia.io.


### Create your asset

To start getting your CrowdStrike assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/device/common/create_asset_connector_1.png)

3. Choose **CrowdStrike Falcon devices**, give it a name, and fill the required fields:

    ![CrowdStrike Falcon devices connector configuration form](/assets/operation_center/asset_connectors/device/crowdstrike_falcon/crowdstrike_device_connector.png)

4. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/crowdstrike_falcon/add_asset_device_asset.png)

5. Click the **Create asset connector** button.

## Information Collected

This section describes the information fetched from CrowdStrike Falcon and how it maps to the OCSF (Open Cybersecurity Schema Framework) v1.6.0 Device Inventory Info model.

### Data Mapping Table

The following table shows how CrowdStrike Falcon device fields are mapped to OCSF fields:

| CrowdStrike Source Field | OCSF Field Path | Description | Data Type |
|--------------------------|-----------------|-------------|-----------|
| `device_id` | `device.uid` | Unique device identifier | String |
| `hostname` | `device.hostname` | Device hostname | String |
| `product_type_desc` | `device.type_id`, `device.type` | Device type (Server, Workstation, Laptop, Mobile, Tablet) | Enum |
| `platform_name` | `device.os.name` | Operating system name | String |
| `os_version` | `device.os.version` | Operating system version | String |
| `os_build` | `device.os.build` | Operating system build number | String |
| `external_ip` | `device.ip` | External IP address of the device | String |
| `local_ip` | `device.network_interfaces[].ip` | Local IP address | String |
| `mac_address` | `device.network_interfaces[].mac` | Primary MAC address | String |
| `connection_ip` | `device.network_interfaces[].ip` | Connection IP address | String |
| `connection_mac_address` | `device.network_interfaces[].mac` | Connection MAC address | String |
| `default_gateway_ip` | `device.subnet` | Default gateway IP address | String |
| `system_manufacturer` | `device.hw_info.manufacturer` | Hardware manufacturer | String |
| `system_product_name` | `device.hw_info.model` | Hardware model | String |
| `bios_version` | `device.hw_info.bios_ver` | BIOS version | String |
| `bios_manufacturer` | `device.hw_info.bios_manufacturer` | BIOS manufacturer | String |
| `serial_number` | `device.hw_info.serial_number` | Device serial number | String |
| `agent_version` | `device.agent_list[].version` | CrowdStrike Falcon agent version | String |
| `cid` | `device.org.uid` | CrowdStrike Customer ID | String |
| `service_provider` | `device.org.name` | Service provider name | String |
| `machine_domain` | `device.domain` | Machine domain | String |
| `ou` | `device.ou` | Organizational unit | String |
| `first_seen` | `device.first_seen_time` | First time device was seen | Timestamp |
| `last_seen` | `device.last_seen_time` | Last time device was seen | Timestamp |
| `modified_timestamp` | `device.modified_time` | Last modification timestamp | Timestamp |
| `agent_local_time` | `device.agent_list[].agent_time` | Agent local time | Timestamp |
| `kernel_version` | `device.os.kernel_version` | Operating system kernel version | String |
| `status` | `device.is_compliant` | Device compliance status (derived) | Boolean |
| `reduced_functionality_mode` | `device.is_compliant` | Reduced functionality mode status | String |
| `filesystem_containment_status` | `device.is_compliant` | Filesystem containment status | String |
| `groups` | `device.groups[].name`, `device.groups[].uid` | Device groups | Array |
| `device_policies.firewall` | `enrichments[].data.Firewall_status` | Firewall policy status | String |
| `city` | `device.location.city` | Geographic location - city | String |
| `country` | `device.location.country` | Geographic location - country | String |
| `continent` | `device.location.continent` | Geographic location - continent | String |

### OCSF Model Structure

The connector generates OCSF Device Inventory Info events (Class UID: 5001) with the following structure:

**Event Metadata:**
- **activity_id**: 2 (Collect)
- **activity_name**: "Collect"
- **category_name**: "Discovery"
- **category_uid**: 5
- **class_name**: "Device Inventory Info"
- **class_uid**: 5001
- **type_name**: "Device Inventory Info: Collect"
- **type_uid**: 500102
- **severity**: "Informational" (severity_id: 1)

**Device Object Structure:**
```
device:
  - uid: Device unique identifier
  - hostname: Device hostname
  - type_id: Device type ID (enum)
  - type: Device type string
  - os: Operating system information
    - name: OS name
    - version: OS version
    - build: OS build number
    - type_id: OS type ID
    - type: OS type string
    - kernel_version: Kernel version
  - ip: External IP address
  - network_interfaces: Array of network interfaces
    - hostname: Interface hostname
    - ip: IP address
    - mac: MAC address (normalized format)
    - name: Interface name (e.g., "primary", "connection")
  - subnet: Default gateway/subnet
  - hw_info: Hardware information
    - manufacturer: Hardware manufacturer
    - model: Hardware model
    - bios_ver: BIOS version
    - bios_manufacturer: BIOS manufacturer
    - serial_number: Serial number
  - agent_list: Array of agent information
    - type: "EDR"
    - vendor: "Crowdstrike"
    - name: "Falcon"
    - version: Agent version
    - agent_time: Agent local timestamp
  - org: Organization information
    - uid: Customer ID (CID)
    - name: Service provider
  - domain: Machine domain
  - ou: Organizational unit
  - first_seen_time: First seen timestamp
  - last_seen_time: Last seen timestamp
  - modified_time: Last modification timestamp
  - is_compliant: Compliance status (boolean)
  - groups: Array of groups
    - name: Group name
    - uid: Group ID
  - location: Geographic location
    - city: City name
    - country: Country name
    - continent: Continent name
```

### Enrichment Objects

The connector includes enrichment objects with additional CrowdStrike-specific data:

**Compliance Enrichment:**
- **name**: "compliance"
- **value**: "hygiene"
- **data**:
  - **Firewall_status**: Status of the device's firewall policy ("Enabled" or "Disabled")

### Data Processing Notes

1. **Timestamp Handling**: All timestamps from CrowdStrike are parsed from ISO 8601 format and converted to UNIX timestamps.

2. **MAC Address Normalization**: MAC addresses are normalized to the standard format (e.g., "00:1A:2B:3C:4D:5E").

3. **Device Type Mapping**: CrowdStrike's `product_type_desc` field is mapped to OCSF device types:
   - Server → DeviceTypeId.SERVER
   - Workstation/Desktop → DeviceTypeId.DESKTOP
   - Laptop → DeviceTypeId.LAPTOP
   - Mobile/Phone → DeviceTypeId.MOBILE
   - Tablet → DeviceTypeId.TABLET

4. **OS Type Mapping**: Platform names are mapped to OCSF OS types:
   - Windows → OS_TYPE_WINDOWS
   - Mac → OS_TYPE_MACOS
   - Linux → OS_TYPE_LINUX
   - iOS → OS_TYPE_IOS
   - Android → OS_TYPE_ANDROID

5. **Compliance Status**: Device compliance is determined based on multiple factors:
   - Status is "normal"
   - Not in reduced functionality mode
   - Not in filesystem containment

6. **Network Interfaces**: The connector creates multiple network interface entries when available:
   - Primary interface (using local_ip and mac_address)
   - Connection interface (using connection_ip and connection_mac_address if different from local)

7. **Groups**: Device groups are extracted from the `groups` array, with the first two groups being prioritized.
