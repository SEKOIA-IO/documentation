uuid: f7da3627-6016-415d-9885-231e1455a7a5
name: Harfanglab EDR
type: asset

## Overview

HarfangLab EDR is a European EDR for Windows, macOS, and Linux that delivers real-time telemetry, ATT&CK-mapped detections, and rapid response (host isolation, process kill, quarantine). This setup guide shows how to forward device assets monitored by HarfangLab EDR to Sekoia.io.

- **Vendor**: HarfangLab
- **Product**: HarfangLab EDR
- **Supported environment**: SaaS

## Configure

### How to create an API token

To connect HarfangLab to Sekoia.io, you need to create an API key in your
HarfangLab console. Follow these steps:

1. Click on **Users** under administration panel.

    ![Account page showing navigation to API Keys tab in HarfangLab](/assets/operation_center/asset_connectors/device/harfanglab/users_button.png)

2. Click on the user you want.

3. Click **Generate token** to generate API token.

    ![Generate API Keys button highlighted for clarity](/assets/operation_center/asset_connectors/device/harfanglab/generate_button.png)

4. Copy the API key to a safe place and start using it in Sekoia.io.

!!! warning
    - Ensure the user account exists before generating an API token.
    - The API token is displayed only once at creation. Save it securely; if you lose it, you must generate a new one.
    - When copying the API key, ensure you copy only the raw key value (excluding any `token_` prefix if displayed).


### Create your asset

To start getting your HarfangLab assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_1.png)

3. Choose **HarfangLab EDR**, give it a name, and fill the required fields:

    ![HarfangLab EDR connector configuration form](/assets/operation_center/asset_connectors/device/harfanglab/harfanglab_connector.png)

4. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/harfanglab/harfanglab_page.png)

5. Click the **Create asset connector** button.

!!! warning
    - Make sure to include your port number in the `URL` field by appending it to the URL, for example: `https://your-harfanglab-instance.com:8443`.

## Information Collected

This section describes the device asset information collected from HarfangLab EDR and how it maps to the OCSF (Open Cybersecurity Schema Framework) Device Inventory model.

### Data Mapping Table

The following table shows how HarfangLab EDR asset fields are mapped to OCSF Device model fields:

| Source Field (HarfangLab) | OCSF Field Path | Description | Data Type |
|---------------------------|-----------------|-------------|-----------|
| `id` | `device.uid` | Unique identifier for the device | String |
| `hostname` | `device.hostname` | Device hostname | String |
| `domainname` | `device.domain` | Domain name the device belongs to | String |
| `ipaddress` | `device.ip` | Primary IP address of the device | String |
| `ipmask` | `device.subnet` | Subnet mask | String |
| `firstseen` | `device.first_seen_time` | Timestamp when device was first seen (UTC) | Timestamp |
| `lastseen` | `device.last_seen_time` | Timestamp when device was last seen (UTC) | Timestamp |
| `boottime` | `device.boot_time` | Device boot time (UTC) | Timestamp |
| `installdate` | `device.created_time` | Installation date of the OS (UTC) | Timestamp |
| `ostype` | `device.os.type` / `device.os.type_id` | Operating system type (Windows, Linux, macOS, etc.) | String / Integer |
| `osproducttype` | `device.os.name` | Detailed OS product type | String |
| `producttype` | `device.model` | Device model/product type | String |
| `description` | `device.desc` | Device description | String |
| `policy` | `device.is_managed` | Whether device has a policy assigned | Boolean |
| `has_valid_password` | `device.is_trusted` | Password validation status | Boolean |
| `subnet.id` | `device.network_interfaces[].uid` | Network subnet unique identifier | String |
| `subnet.name` | `device.network_interfaces[].name` | Network interface name | String |
| `ipaddress` | `device.network_interfaces[].ip` | Network interface IP address | String |
| `hostname` | `device.network_interfaces[].hostname` | Network interface hostname | String |
| `encrypted_disk_count` | `enrichments[].data.Storage_encryption.partitions` | Number of encrypted disks | Integer |
| `disk_count` | `enrichments[].data.Storage_encryption.partitions` | Total number of disks | Integer |
| `policy.windows_self_protection_feature_firewall` | `enrichments[].data.Firewall_status` | Windows firewall status | String |

### OCSF Model Structure

The connector generates OCSF Device Inventory events (Class UID: 5001) with the following structure:

#### Base Event Fields
- **activity_id**: 1 (Create)
- **activity_name**: "Create"
- **category_uid**: 5 (Asset Management)
- **category_name**: "Asset Management"
- **class_uid**: 5001 (Device Inventory)
- **class_name**: "Device Inventory"
- **type_uid**: 500101
- **type_name**: "Device Inventory: Create"
- **time**: Event timestamp (extracted from `firstseen`)

#### Device Object Fields
- **type_id**: 7 (Desktop)
- **type**: "Desktop"
- **uid**: Device unique identifier
- **hostname**: Device hostname
- **domain**: Domain name
- **ip**: Primary IP address
- **subnet**: Subnet mask
- **network_interfaces**: Array of network interface objects
- **first_seen_time**: First seen timestamp
- **last_seen_time**: Last seen timestamp
- **boot_time**: Boot timestamp
- **created_time**: Installation timestamp
- **desc**: Device description
- **is_managed**: Policy assignment status
- **is_trusted**: Password validation status
- **model**: Product/model type
- **vendor_name**: "HarfangLab"

#### Operating System Object
- **name**: OS product type
- **type**: OS type (Windows, Linux, macOS, etc.)
- **type_id**: Numeric OS type identifier

#### Network Interface Object
Network interface types are automatically detected based on interface name patterns:
- **Wireless**: WiFi, WLAN, 802.11
- **Mobile**: Cellular, LTE, 4G/5G, 3G
- **Tunnel**: VPN, tunnel, tun/tap interfaces
- **Wired**: Default for other interfaces

Each network interface includes:
- **hostname**: Interface hostname
- **ip**: IP address
- **name**: Interface name
- **type**: Interface type (Wireless, Mobile, Tunnel, Wired)
- **type_id**: Numeric interface type identifier
- **uid**: Subnet identifier

### Enrichment Objects

The connector provides compliance and hygiene enrichment data when available:

#### Compliance Enrichment
- **name**: "compliance"
- **value**: "hygiene"
- **data**: Device data object containing:

##### Firewall Status
Extracted from `policy.windows_self_protection_feature_firewall`:
- **Enabled**: Firewall is active
- **Disabled**: Firewall is inactive
- **null**: Status unknown

##### Storage Encryption
Calculated from `encrypted_disk_count` and `disk_count`:
- **partitions**: Dictionary mapping disk identifiers to encryption status
  - Format: `{"disk_0": "Enabled", "disk_1": "Disabled", ...}`
  - Number of "Enabled" entries equals `encrypted_disk_count`
  - Remaining entries up to `disk_count` are marked "Disabled"

