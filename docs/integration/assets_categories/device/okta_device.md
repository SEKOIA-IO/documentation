uuid: b6e2c8a2-4f3b-4e7a-8c1d-2e4f3a6b7c9d
name: Okta Device
type: asset

## Overview

Okta is a cloud-based identity and access management platform that provides secure authentication, authorization, and device management services. Okta helps organizations manage device identities across multiple applications and systems, providing device trust, device compliance, and comprehensive device lifecycle management.

- **Vendor**: Okta
- **Product**: Okta Identity Platform
- **Supported environment**: Cloud

## Configure

### How to create an API token with proper permissions

To connect Okta to Sekoia.io, you need to create an API token with the necessary permissions to access Okta devices and device trust information. Follow these steps:

1. Sign in to your Okta Admin Console and navigate to the Security section.

    ![Okta Admin Console Security section](/assets/operation_center/asset_connectors/device/okta/okta_api_key_1.png)

2. Click **API** in the left navigation pane, then click **Tokens**.

3. Click **Create Token** to generate a new API token.

    ![Create Token button highlighted](/assets/operation_center/asset_connectors/device/okta/okta_api_key_2.png)

4. Enter a name for the token (e.g., `sekoia-reader`)

5. Click **Create Token** to generate the API token.

    ![Token creation confirmation](/assets/operation_center/asset_connectors/device/okta/okta_api_key_3.png)

6. Copy the **Token Value** to a safe location. You'll need this token to configure the connector in Sekoia.io.

    ![API Token value display](/assets/operation_center/asset_connectors/device/okta/okta_api_key_4.png)

!!! Warning
    - The token value is only shown when you create it. If you lose it, you must create a new token.
    - Store this token securely and never share it publicly.
    - Consider rotating API tokens regularly for security best practices.


### Required API permissions

The API token must have the following scopes to successfully fetch Okta devices and device trust information:

```json
{
    "scopes": [
        "okta.devices.read",
        "okta.deviceTrust.read",
        "okta.devices.manage"
    ]
}
```

**Required Scopes:**

- `okta.devices.read`: Read device information and attributes
- `okta.deviceTrust.read`: Read device trust and compliance status
- `okta.devices.manage`: Full device management capabilities

### Create your asset

To start getting your Okta devices into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![New connector button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_1.png)

3. Choose **Okta Device**, give it a name, and fill the required fields:

    ![Okta Device connector configuration form](/assets/operation_center/asset_connectors/device/okta/okta_asset_device_1.png)

4. Enter the following information:

    - **API Token**: The API token value from your Okta organization
    - **Base URL**: Your Okta organization’s base URL (e.g., `https://your-domain.okta.com`)

5. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/okta/okta_asset_device_2.png)

6. Click the **Create asset connector** button.

## Information Collected

This connector collects device information from Okta and maps it to the OCSF (Open Cybersecurity Schema Framework) Device Inventory Info event model (Class 5001). The following sections detail the data mapping and structure.

### Data Mapping Table

| Source Field (Okta) | OCSF Field Path | Description | Data Type |
|---------------------|-----------------|-------------|-----------|
| `id` | `device.uid` | Unique device identifier | String |
| `profile.displayName` | `device.hostname` | Device display name | String |
| `profile.platform` | `device.os.type` / `device.os.type_id` | Operating system platform (Windows, macOS, Linux, iOS, Android) | String / Integer |
| `profile.osVersion` | `device.os.version` | Operating system version | String |
| `profile.manufacturer` | `device.vendor_name` | Device manufacturer | String |
| `profile.model` | `device.model` | Device model | String |
| `created` | `device.created_time` | Device creation timestamp | DateTime |
| `lastUpdated` | `device.last_seen_time` | Last update timestamp | DateTime |
| `profile.managed` | `device.is_managed` | Whether device is managed | Boolean |
| `profile.registered` | `device.is_compliant` | Device registration/compliance status | Boolean |
| `profile.diskEncryptionType` | `enrichments[].data.DiskEncryption.partitions` | Disk encryption configuration | Object |
| `profile.serialNumber` | `enrichments[].data.Users[]` | Hardware serial number | String (in enrichment) |
| `profile.sid` | `enrichments[].data.Users[]` | Windows Security Identifier | String (in enrichment) |
| `profile.secureHardwarePresent` | `enrichments[].data.Users[]` | Secure hardware presence | Boolean (in enrichment) |

### OCSF Model Structure

The connector produces events conforming to the **Device Inventory Info** event class (OCSF 5001) with the following structure:

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
  "time": "<timestamp>",
  "metadata": {
    "product": {
      "name": "Okta",
      "vendor_name": "Okta",
      "version": "N/A"
    },
    "version": "1.6.0"
  },
  "device": {
    "hostname": "<device_display_name>",
    "uid": "<device_id>",
    "type": "Other",
    "type_id": 99,
    "os": {
      "name": "<os_name>",
      "version": "<os_version>",
      "type": "<os_type>",
      "type_id": "<os_type_id>"
    },
    "vendor_name": "<manufacturer>",
    "model": "<model>",
    "created_time": "<timestamp>",
    "last_seen_time": "<timestamp>",
    "is_managed": true/false,
    "is_compliant": true/false
  },
  "enrichments": [...]
}
```

#### Operating System Type Mappings

| Okta Platform | OCSF OS Type | OCSF Type ID |
|---------------|--------------|--------------|
| `windows` | `Windows` | 100 |
| `macos` | `macOS` | 300 |
| `linux` | `Linux` | 200 |
| `ios` | `iOS` | 302 |
| `android` | `Android` | 201 |
| Other | `Other` | 99 |

### Enrichment Objects

The connector provides additional device context through enrichment objects. These enrichments contain hardware and security information that doesn't fit directly into the standard OCSF device schema.

#### Device Info Enrichment

**Name**: `device_info`  
**Value**: `hardware_and_security`

**Disk Encryption Object** (`enrichments[].data.DiskEncryption`):

Maps Okta's disk encryption types to partition-level encryption status:

- **ALL_INTERNAL_VOLUMES**: `{"all_internal": "Enabled"}`
- **FULL**: `{"full": "Enabled"}`
- **USER**: `{"user": "Enabled"}`
- **None/Other**: `{"none": "Disabled"}`

**Hardware Identifiers** (`enrichments[].data.Users[]`):

Contains hardware and security-related identifiers as string entries:

- `serial_number:<value>` - Device serial number
- `windows_sid:<value>` - Windows Security Identifier (SID)
- `secure_hardware_present:<true/false>` - Presence of secure hardware (TPM, Secure Enclave, etc.)


## Further Reading
- [Okta Documentation](https://developer.okta.com/docs/)
- [Okta Device Management API](https://developer.okta.com/docs/reference/api/devices/)
- [Okta Device Trust API](https://developer.okta.com/docs/reference/api/device-trust/)
- [Okta API Token Management](https://developer.okta.com/docs/guides/create-an-api-token/)

