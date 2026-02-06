uuid: f47ac10b-58cc-4372-a567-0e02b2c3d479
name: SentinelOne EDR
type: asset

## Overview

SentinelOne is an Endpoint Detection and Response (EDR) solution that provides comprehensive endpoint protection and monitoring. This setup guide shows how to forward device assets monitored by SentinelOne EDR to Sekoia.io for centralized asset management and security operations.

- **Vendor**: SentinelOne
- **Product**: SentinelOne EDR
- **Supported environment**: SaaS

## Configure

### How to create an API token

To connect SentinelOne to Sekoia.io, you need to generate an API token from the SentinelOne Management Console. We recommend creating a Service User to use a dedicated account for the integration.

**Important**: If you have multiple SentinelOne Management Consoles, you must generate an API Token for each one.

!!! note
    The API token you generate is time-limited. To generate a new token (and invalidate the old one), you will need to copy the Service User. Please refer to the SentinelOne documentation to obtain guidance on how to do this action.

Follow these steps to create an API token:

1. In the SentinelOne management console, go to **Policies and settings**, select **User management**, and then select **Service Users**.

2. Create a new **New Service User** by specifying a name and an expiration date.

3. Choose the **Scope** of the **Service User**: `Global`, `Account` or `Site`, select the appropriate **Account(s)** or **Site(s)** and the role to grant to the **Viewer**.

4. Select **Create User** and copy the generated API token to a safe place.

!!! warning
    - A Service User with the `Site Admin` or `IR Team` role is recommended for full functionality.
    - The API token is displayed only once at creation. Save it securely; if you lose it, you must generate a new one.
    - When copying the API token, ensure you copy the complete token value.

### Create your asset connector

To start getting your SentinelOne assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_1.png)

3. Choose **SentinelOne EDR**, give it a name, and fill the required fields:

    - **API Token**: The API token you generated from the SentinelOne Management Console
    - **URL Domain**: Your SentinelOne Management Console URL (e.g., `https://your-instance.sentinelone.net`)

    ![SentinelOne EDR connector configuration form](/assets/operation_center/asset_connectors/device/sentinelone/sentinelone_connector.png)

4. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/sentinelone/sentinelone_test.png)

5. Click the **Create asset connector** button.

!!! warning
    - Ensure you have the correct URL Domain for your SentinelOne Management Console.
    - The API token must have sufficient permissions to read endpoint and agent information.

## Information Collected

The SentinelOne EDR asset connector collects comprehensive device information from SentinelOne agents and maps it to the OCSF (Open Cybersecurity Schema Framework) Device Inventory Info standard.

### Data Mapping Table

The following table shows how SentinelOne agent data is mapped to OCSF Device model fields:

| Source Field (SentinelOne) | OCSF Field Path | Description | Data Type |
|----------------------------|-----------------|-------------|-----------|
| `computerName` | `device.hostname` | Computer/device hostname | String |
| `uuid` | `device.uid` | Primary unique identifier for the device | String |
| `id` | `device.uid_alt` | Alternate unique identifier (agent ID) | String |
| `machineType` | `device.type` / `device.type_id` | Device type (Desktop, Laptop, Server, etc.) | String / Integer |
| `osType` | `device.os.type` / `device.os.type_id` | Operating system type (Windows, Linux, macOS, etc.) | String / Integer |
| `osName` | `device.os.name` | Operating system name and version | String |
| `osRevision` | `device.os.name` | OS revision combined with OS name | String |
| `domain` | `device.domain` | Active Directory or network domain | String |
| `externalIp` | `device.ip` | External/public IP address | String |
| `groupIp` | `device.subnet` | Network subnet or IP range (e.g., "31.155.5.x") | String |
| `networkInterfaces[].name` | `device.network_interfaces[].name` | Network interface name | String |
| `networkInterfaces[].physical` | `device.network_interfaces[].mac` | MAC address | String |
| `networkInterfaces[].inet[0]` | `device.network_interfaces[].ip` | IP address (first from inet list) | String |
| `networkInterfaces[].id` | `device.network_interfaces[].uid` | Network interface unique identifier | String |
| `modelName` | `device.model` | Device hardware model | String |
| `osStartTime` | `device.boot_time` | Last boot/startup time | ISO 8601 String |
| `createdAt` | `device.created_time` | Device/agent creation timestamp | Unix Timestamp |
| `registeredAt` | `device.first_seen_time` | First registration timestamp | Unix Timestamp |
| `lastActiveDate` | `device.last_seen_time` | Last activity timestamp | Unix Timestamp |
| `isUpToDate` | `device.is_compliant` | Compliance status (agent up-to-date) | Boolean |
| `siteName` | `device.region` | SentinelOne site name used as region | String |
| `groupName` | `device.groups[].name` | Group name | String |
| `groupId` | `device.groups[].uid` | Group unique identifier | String |
| `locations[0].name` | `device.location.city` | Location city (from first location) | String |
| `agentVersion` | `metadata.product.version` | SentinelOne agent version | String |

### OCSF Model Structure

The connector produces OCSF Device Inventory Info events with the following structure:

```json
{
  "activity_id": 2,
  "activity_name": "Collect",
  "category_name": "Discovery",
  "category_uid": 5,
  "class_name": "Device Inventory Info",
  "class_uid": 5001,
  "device": {
    "hostname": "<computerName>",
    "uid": "<uuid>",
    "uid_alt": "<id>",
    "type": "<Desktop|Laptop|Server|etc>",
    "type_id": "<1-99>",
    "os": {
      "name": "<osName osRevision>",
      "type": "<Windows|Linux|macOS|etc>",
      "type_id": "<100-499>"
    },
    "domain": "<domain>",
    "ip": "<externalIp>",
    "subnet": "<groupIp>",
    "network_interfaces": [...],
    "model": "<modelName>",
    "vendor_name": "SentinelOne",
    "boot_time": "<osStartTime>",
    "created_time": "<timestamp>",
    "first_seen_time": "<timestamp>",
    "last_seen_time": "<timestamp>",
    "is_managed": true,
    "is_compliant": "<isUpToDate>",
    "region": "<siteName>",
    "groups": [...],
    "location": {
      "city": "<locations[0].name>"
    }
  },
  "enrichments": [...],
  "metadata": {
    "product": {
      "name": "SentinelOne",
      "vendor_name": "SentinelOne",
      "version": "<agentVersion>"
    },
    "version": "1.6.0"
  },
  "severity": "Informational",
  "severity_id": 1,
  "type_name": "Device Inventory Info: Collect",
  "type_uid": 500102
}
```

### Enrichment Objects

The connector creates enrichment objects to capture additional security and operational information that doesn't fit directly into the OCSF Device model:

| Enrichment Name | Source Field | Description | Value Type |
|----------------|--------------|-------------|------------|
| **Firewall** | `firewallEnabled` | Windows firewall status | "Enabled" / "Disabled" |
| **Users** | `lastLoggedInUserName`, `osUsername` | User accounts associated with the device | Comma-separated string |
| **Update Status** | `isUpToDate` | Agent update compliance status | "Up to Date" / "Update Required" |
| **Active Threats** | `activeThreats` | Number of active threats detected | String (numeric) |
| **Infection Status** | `infected` | Current infection state | "Infected" / "Clean" |

