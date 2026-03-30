# crowdstrike\_falcon\_device

uuid: adcd0095-0f3d-4699-8621-158977b6c2c3 name: Crowdstrike Falcon devices type: asset

### Overview

CrowdStrike Falcon is an Endpoint Detection and Response solution. This setup guide shows how to forward device assets created in CrowdStrike Falcon to Sekoia.io.

* **Vendor**: CrowdStrike
* **Product**: CrowdStrike Falcon
* **Supported environment**: SaaS

### Configure

#### How to create an API token

To connect CrowdStrike Falcon to Sekoia.io, you need to create an API key pair (Client id and Client secret) in your CrowdStrike Falcon console. Follow these steps:

1. Log in to the CrowdStrike interface.
2. Click on the burger menu and go to Support and `resources` > `Resources and tools` > `API client and keys`.
3. In the `OAuth2 API Clients` tab, create a new `OAuth2 API Client` with the `Read` and `Write` permissions for the scopes `User Management`.
4. Copy the api key in a safe place and start using it in Sekoia.io.

#### Create your asset

To start getting your CrowdStrike assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.
2. Click the **+ New connector** button.
3. Choose **CrowdStrike Falcon devices**, give it a name, and fill the required fields:
4. Test the connection by clicking the **Test connector** button.
5. Click the **Create asset connector** button.

{!\_shared\_content/operations\_center/integrations/generated\_assets\_documentation/crowdstrike-falcon\_device.md!}
