uuid: 6a90a5c0-3365-4a9c-938d-38113cc981a0
name: Sophos EDR
type: asset

## Overview

Sophos EDR monitors, detects and mitigates threats on endpoints.
This EDR reduces the attack surface and prevents attacks by using anti-exploit, anti-ransomware, and advanced control technologies.

This setup guide shows how to forward device assets from Sophos EDR to Sekoia.io.

- **Vendor**: Sophos
- **Product**: SentinelOne EDR
- **Supported environment**: Cloud

## Configure

### Create SOPHOS EDR Credentials

!!! Warning
    If you have a "Partner" or "Organization" entity, you need to do the following procedure on every tenant attached to it. Please find more information on the [official documentation](https://developer.sophos.com/intro)

In the Sophos Central Admin console:

1. On the left panel, go to `Global Settings` and select `API Credentials Management`.
2. Click on `Add Credential` to create a credential dedicated to Sekoia.io.
3. Give it a name, select the role `Service Principal ReadOnly` and click on `Add`.
4. In the `API credential Summary`, copy the `Client ID` and the `Client Secret`. It will be used later in Sekoia.io to retrieve the events.

### Create your asset connector

To start getting your Sophos assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_1.png)

3. Choose **Sophos EDR**, give it a name, and fill the required fields in the account field:

    - **Account name**: The name of the Sophos EDR account you want to connect to.
    - **Client ID**: The client ID of the API credential you created in the Sophos Central Admin console.
    - **Client Secret**: The client secret of the API credential you created in the Sophos Central Admin console
    - **API Host**: The API host URL of your Sophos EDR instance. 

    ![Sophos EDR connector configuration form](/assets/operation_center/asset_connectors/device/sophos/sophos_connector.png)

4. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/sophos/sophos_test.png)

5. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/sophos_device.md!}