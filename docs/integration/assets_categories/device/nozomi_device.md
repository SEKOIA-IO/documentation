uuid: b99bf94b-08b3-4717-b880-6020fb67b5c1
name: Nozomi Devices
type: asset

_**[Reveal module](/xdr/features/modules/reveal_index.md)**  — This feature requires the Reveal add-on module._

## Overview

Nozomi Networks provides visibility and threat detection for operational technology (OT), IoT, and IT environments. Its Guardian sensors and Central Management Console (CMC) passively discover every asset communicating on the industrial network, such as PLCs, HMIs, controllers, switches, and workstations, and enrich them with vendor, firmware, protocol, and zone information. This setup guide shows how to forward the device assets discovered by Nozomi Networks to Sekoia.io.

- **Vendor**: Nozomi Networks
- **Product**: Nozomi Networks Guardian / Central Management Console (CMC)
- **Supported environment**: On Premise, Cloud

The asset connector authenticates against the Guardian/CMC Open API (`POST /api/open/sign_in`), then queries the assets through `GET /api/open/query/do` with the N2QL query `assets`. It paginates through every asset ordered by creation date and transforms each record into an OCSF Device Inventory Info object.

!!! note
    The connector collects assets incrementally, based on their creation date (`created_at`). The first run collects every asset known by Nozomi; the following runs only collect assets created since the previous run.

## Configure

### Prerequisites

- A Nozomi Networks Guardian or CMC instance reachable over HTTPS from Sekoia.io.
- A Nozomi user account allowed to read assets. The API key inherits the permissions of the user who creates it.

### How to create an API key

To connect Nozomi Networks to Sekoia.io, you need an Open API key in the Guardian or CMC web console. Follow these steps:

1. Sign in to the Guardian or CMC web console with the user whose permissions the connector will use.

2. In the top navigation bar, open your **Profile** menu and select **API Keys**.

3. Click **Add**, give the key a description (e.g., `sekoia-asset-connector`), and optionally restrict the allowed source IP addresses.

4. Click **Generate**, then copy the **Key name** and the **Key token** to a safe place. You will use both in Sekoia.io.

!!! warning
    - The key token is displayed only once upon creation. Store it securely; if lost, you will need to generate a new key.
    - If you restrict the allowed IP addresses of the key, make sure the Sekoia.io outbound IP addresses are allowed.

More details are available in the Nozomi Networks documentation: [Open API keys](https://technicaldocs.nozominetworks.com/).

### Create your asset

To start getting your Nozomi Networks assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.

    ![New connector button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_1.png)

3. Choose **Nozomi Devices**, give it a name, and fill the required fields:

    - `base_url`: the URL of your Guardian or CMC instance (e.g., `https://guardian.example.com`).
    - `key_name`: the key name generated in the previous section.
    - `key_token`: the key token generated in the previous section.

4. Test the connection by clicking the **Test connector** button. The test signs in to the Open API with the provided key.

5. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/nozomi_device.md!}

## Further Reading

- [Nozomi Networks technical documentation](https://technicaldocs.nozominetworks.com/)
- [Nozomi Vantage intake](/integration/categories/network_security/nozomi_vantage.md)
