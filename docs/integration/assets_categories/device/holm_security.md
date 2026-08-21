uuid: 4df342f5-9fb0-4d45-97c0-bdae48e2e7c2
name: Holm Security Devices
type: asset

_**[Reveal module](/xdr/features/modules/reveal_index.md)**  — This feature requires the Reveal add-on module._

## Overview

Holm Security is a cloud-hosted vulnerability and attack surface management platform for system and network security. Its agent-managed devices provide rich operating system, state, and vulnerability metadata. This setup guide shows how to forward the device assets enrolled in Holm Security to Sekoia.io.

- **Vendor**: Holm Security
- **Product**: Holm Security System & Network Security
- **Supported environment**: Cloud

!!! note
    This asset connector is currently in beta. Enable the `reveal-beta-connectors` feature flag to display it.

The asset connector calls `GET /v2/devices` and `GET /v2/net-assets` on the Holm Security API (`https://se-api.holmsecurity.com`), paginates through every agent-managed device, and transforms each record into an OCSF Device Inventory Info object.

## Configure

### How to create an API token

To connect Holm Security to Sekoia.io, you need an API token in the Holm Security web console. Follow these steps:

1. Sign in to the Holm Security console, open the **main menu** (hamburger icon ≡) on the left panel, and select **API**.

2. Enable the **API**.

3. Click Create **API Token**, give it a name, set the permission to Read, and enable scope for `Network assets`, `Web assets`, and `Tags`.

4. Copy the token to a safe place and use it in Sekoia.io.

!!! warning
    - The API token is displayed only once upon creation. Store it securely; if lost, you will need to generate a new one.

### Create your asset

To start getting your Holm Security assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_1.png)

3. Choose **Holm Security Devices**, give it a name, and fill the required fields:

    - `base_url`: the base URL of the Holm Security API (default `https://se-api.holmsecurity.com`).
    - `api_token`: the API token generated in the previous section.
   
    ![Holm security connector configuration form](/assets/operation_center/asset_connectors/device/holm_security/holm_security_connector.png)

4. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/holm_security/holm_security_test.png)

5. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/holm-security_device.md!}
