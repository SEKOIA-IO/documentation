
## Overview

CrowdStrike Falcon is an Endpoint Detection and Response solution. This setup guide shows how to forward user assets created in CrowdStrike Falcon to Sekoia.io.

- **Vendor**: CrowdStrike
- **Product**: CrowdStrike Falcon
- **Supported environment**: SaaS

## Configure

### How to create an API token

To connect Crowdstrike Falcon to Sekoia.io, you need to create an API key pair (Client id and Client secret) in your Crowdstrike Falcon console. Follow these steps:

1. Log in to the crowdstrike interface.

2. Click on the burger menu and go to Support and `resources` > `Resources and tools` > `API client and keys`.

    ![Account page showing navigation to API Keys tab in Harfanglab](/assets/operation_center/asset_connectors/user/crowdstrike_falcon/api_key_button.png)

3. In the `OAuth2 API Clients` tab, create an new `OAuth2 API Client` with the `Read` and `Write` permissions for the scopes `User Management.

    ![Generate API Keys button highlighted for clarity](/assets/operation_center/asset_connectors/user/crowdstrike_falcon/create_api_key.png)

4. Copy the api key in a safe place. And start using it in Sekoia.io.


### Create your asset

To start getting your Harfanglab assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/tenable/asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/vulnerability/tenable/new_connector_button.png)

3. Choose **Get Crowdstrike Falcon users**, give it a name, and fill the required fields:

    ![Crowdstrike Falcon users connector configuration form](/assets/operation_center/asset_connectors/vulnerability/tenable/tenable_asset_connector.png)

4. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/user/crowdstrike_falcon/add_asset_user_asset.png)

5. Click the **Create asset connector** button.
