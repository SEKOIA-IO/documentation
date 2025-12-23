uuid: f47ac10b-58cc-4372-a567-0e02b2c3d479
name: SentinelOne EDR
type: asset

## Overview

SentinelOne is an Endpoint Detection and Response (EDR) solution that provides comprehensive endpoint protection and monitoring. This setup guide shows how to forward device assets monitored by SentinelOne EDR to Sekoia.io for centralized asset management and security operations.

- **Vendor**: SentinelOne
- **Product**: SentinelOne EDR
- **Supported environment**: Cloud

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
