
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
    - A user must exist before generating an API token.


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
