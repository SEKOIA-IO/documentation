uuid: 4df342f5-9fb0-4d45-97c0-bdae48e2e7c2
name: Holm Security Devices
type: asset

## Overview

Holm Security is a cloud-hosted vulnerability and attack surface management platform for system and network security. Its agent-managed devices provide rich operating system, state, and vulnerability metadata. This setup guide shows how to forward the device assets enrolled in Holm Security to Sekoia.io.

- **Vendor**: Holm Security
- **Product**: Holm Security System & Network Security
- **Supported environment**: Cloud

The asset connector calls `GET /v2/devices` on the Holm Security API (`https://se-api.holmsecurity.com`), paginates through every agent-managed device, and transforms each record into an OCSF Device Inventory Info object.

## Configure

### How to create an API token

To connect Holm Security to Sekoia.io, you need an API token created by an administrator in the Holm Security web console. Follow these steps:

1. Sign in to the Holm Security console with an administrator account.

    ![Holm Security login page](/assets/operation_center/asset_connectors/device/holm_security/login.png)

2. Open **Settings** and select the **API tokens** section.

    ![Navigation to API tokens in Holm Security settings](/assets/operation_center/asset_connectors/device/holm_security/api_tokens.png)

3. Click **Generate token**, give it a descriptive name, and confirm.

    ![Generate token button in Holm Security](/assets/operation_center/asset_connectors/device/holm_security/generate_token.png)

4. Copy the token to a safe place and use it in Sekoia.io.

!!! warning
    - The API token is displayed only once at creation. Save it securely; if you lose it, you must generate a new one.
    - Use an administrator account, otherwise the `GET /v2/devices` endpoint returns an authorization error.

### Create your asset

To start getting your Holm Security assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.

    ![New connector button highlighted](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_1.png)

3. Choose **Holm Security Devices**, give it a name, and fill the required fields:

    - `base_url`: the base URL of the Holm Security API (default `https://se-api.holmsecurity.com`).
    - `api_token`: the API token generated in the previous section.

4. Test the connection by clicking the **Test connector** button.

5. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/holm-security_device.md!}
