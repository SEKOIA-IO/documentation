uuid: 7a4170d6-e359-4beb-92b5-28c00a447406
name: WithSecure Elements
type: asset

## Overview

WithSecure Elements, formerly known as F-Secure Business, provides endpoint protection, detection and response for computers, servers and mobile devices.

This setup guide shows how to forward device assets from WithSecure Elements to Sekoia.io.

- **Vendor**: WithSecure
- **Product**: WithSecure Elements
- **Supported environment**: Cloud

!!! Note
    The connector collects the active devices of the default organization of the API client.

## Configure

### Create WithSecure Elements Credentials

In the WithSecure Elements Security Center:

1. On the left panel, go to `Management` and select `API clients`.
2. Click on `Add new` to create a new API client dedicated to Sekoia.io.
3. Give it a description, check it is `Read-Only` and click on `Add`.
4. In the `API client` Summary, copy the `Client ID` and the `Secret` before checking the box `I have copied and stored the secret` and closing the window. They will be used later in Sekoia.io to retrieve the assets.

![WithSecure API Client Creation](/assets/integration/endpoint/withsecure/withsecure_create_api_client.png){: style="max-width:80%"}

### Create your asset connector

To start getting your WithSecure Elements assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.

    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_1.png)

3. Choose **WithSecure Elements Devices**, give it a name, and fill the required fields in the account field:

    - **Account name**: The name of the WithSecure Elements account you want to connect to.
    - **Client ID**: The client ID of the API client you created in the WithSecure Elements Security Center.
    - **Secret**: The secret of the API client you created in the WithSecure Elements Security Center.

4. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/withsecure_device.md!}
