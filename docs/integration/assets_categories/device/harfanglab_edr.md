
## Overview

HarfangLab EDR is a European EDR for Windows, macOS, and Linux that delivers real-time telemetry, ATT&CK-mapped detections, and rapid response (host isolation, process kill, quarantine). This setup guide shows how to forward assets monitored by HarfangLab EDR to Sekoia.io.

- **Vendor**: Harfanglab
- **Product**: Harfanglab EDR
- **Supported environment**: SaaS

## Configure

### How to create an API token

To connect Harfanglab to Sekoia.io, you need to create an API key pair (Access Key and Secret Key) in your
HarfangLab console. Follow these steps:

1. Click on **Users** under administration panel.

    ![Account page showing navigation to API Keys tab in Harfanglab](/assets/operation_center/asset_connectors/device/users_button.png)

2. Click on the user you want.

3. Click **Generate token** to generate api token.

    ![Generate API Keys button highlighted for clarity](/assets/operation_center/asset_connectors/device/generate_button.png)

4. Copy the api key in a safe place. And start using it in Sekoia.io.

!!! important
    - A user must exist before generating an API token.


### Create your asset

To start getting your Harfanglab assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/tenable/asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/vulnerability/tenable/new_connector_button.png)

3. Choose **Harfanglab EDR**, give it a name, and fill the required fields:

    ![Harfanglab EDR connector configuration form](/assets/operation_center/asset_connectors/vulnerability/tenable/tenable_asset_connector.png)

4. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/harfanglab_page.png)

5. Click the **Create asset connector** button.
