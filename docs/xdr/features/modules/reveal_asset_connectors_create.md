# Create an asset connector

Asset connectors link external systems to Sekoia so that asset records can be created, merged, and enriched with structured data from sources such as EDR tools, vulnerability scanners, identity providers, and CMDBs. This article explains how to create a new asset connector and verify that it is working.

## Before you begin

Confirm that the following conditions are met:

- The Reveal add-on module is enabled for your community.
- You have the credentials required by the integration you want to connect (API key, client ID, service account, or equivalent).

## Create an asset connector

### Step 1: Open the asset connectors panel

1. In the left menu, select **Configure**.
2. Select **Assets**.
3. Select **Asset connectors**.

The asset connectors panel opens and lists your existing connectors.

![!Asset connectors panel](/assets/asset_connector_panel.png){: style="width: 100%; max-width: 100%"}


### Step 2: Select an integration

1. Select **New connector**.
2. In the integration catalog, select the integration you want to configure.

![!Integration catalog for asset connector]( docs/assets/connector_choice.png){: style="width: 100%; max-width: 100%"}

### Step 3: Fill in the connector form

!!! note "Reusing accounts"
    You can reuse an existing account. Any account created here is shared with the account list, alongside those created for event connectors and playbook modules.

Enter the required fields for the selected integration. The fields vary by integration type and typically include a connector name, and an Account to synchronize.

![!Asset connectors configuration form](docs/assets/connector_config.png){: style="width: 100%; max-width: 100%"} 

### Step 4: Test the connector

Select **Test connector** to validate your credentials before saving.

!!! note "What the test checks"
    A successful test confirms that the credentials you entered are valid.

### Step 5: Create the connector

When the test is conclusive, select **Create asset connector**.

The connector starts retrieving asset data from the external system. Asset retrieval is progressive. Depending on the size of your environment and the integration, the first assets may take several minutes to appear.

!!! note "Where to find your assets"
    All assets retrieved by connectors are available on the **Assets** page. You can monitor connector health from the asset context panel under the **Security controls** tab. In the listing, you can filter assets by connector.

## Manage existing connectors

From the asset connector list, you can perform the following actions on any connector tile:

| Action | How to access |
|---|---|
| Enable or disable | Toggle on the connector tile |
| Edit configuration | Select **...** then select **Edit** |
| View logs | Select **...** then select **View logs** |
| Delete | Select **...** then select **Delete** |

## Related links

- [Troubleshoot asset connectors](/xdr/features/modules/reveal_asset_connectors_troubleshoot.md) — How to diagnose and resolve connector errors using error indicators and logs.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md) — Which data sources are required or optional for each Reveal capability.
- [Getting started with Reveal](/xdr/features/modules/reveal_getting_started.md) — Recommended setup order for all Reveal data sources.
- [Integration — Asset categories](/xdr/integration/assets_categories/overview.md) — Reference for available connector categories and integration setup.
- [Security controls](/xdr/features/modules/reveal_security_controls.md) — How to verify connector coverage from the asset context panel.
