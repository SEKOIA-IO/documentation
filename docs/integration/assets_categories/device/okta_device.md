# okta\_device

uuid: b6e2c8a2-4f3b-4e7a-8c1d-2e4f3a6b7c9d name: Okta Device type: asset

### Overview

Okta is a cloud-based identity and access management platform that provides secure authentication, authorization, and device management services. Okta helps organizations manage device identities across multiple applications and systems, providing device trust, device compliance, and comprehensive device lifecycle management.

* **Vendor**: Okta
* **Product**: Okta Identity Platform
* **Supported environment**: Cloud

### Configure

#### How to create an API token with proper permissions

To connect Okta to Sekoia.io, you need to create an API token with the necessary permissions to access Okta devices and device trust information. Follow these steps:

1. Sign in to your Okta Admin Console and navigate to the Security section.
2. Click **API** in the left navigation pane, then click **Tokens**.
3. Click **Create Token** to generate a new API token.
4. Enter a name for the token (e.g., `sekoia-reader`)
5. Click **Create Token** to generate the API token.
6. Copy the **Token Value** to a safe location. You'll need this token to configure the connector in Sekoia.io.

!!! Warning - The token value is only shown when you create it. If you lose it, you must create a new token. - Store this token securely and never share it publicly. - Consider rotating API tokens regularly for security best practices.

#### Required API permissions

The API token must have the following scopes to successfully fetch Okta devices and device trust information:

```json
{
    "scopes": [
        "okta.devices.read",
        "okta.deviceTrust.read",
        "okta.devices.manage"
    ]
}
```

**Required Scopes:**

* `okta.devices.read`: Read device information and attributes
* `okta.deviceTrust.read`: Read device trust and compliance status
* `okta.devices.manage`: Full device management capabilities

#### Create your asset

To start getting your Okta devices into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.
2. Click the **+ New connector** button.
3. Choose **Okta Device**, give it a name, and fill the required fields:
4. Enter the following information:
   * **API Token**: The API token value from your Okta organization
   * **Base URL**: Your Okta organization’s base URL (e.g., `https://your-domain.okta.com`)
5. Test the connection by clicking the **Test connector** button.
6. Click the **Create asset connector** button.

{!\_shared\_content/operations\_center/integrations/generated\_assets\_documentation/okta\_device.md!}

### Further Reading

* [Okta Documentation](https://developer.okta.com/docs/)
* [Okta Device Management API](https://developer.okta.com/docs/reference/api/devices/)
* [Okta Device Trust API](https://developer.okta.com/docs/reference/api/device-trust/)
* [Okta API Token Management](https://developer.okta.com/docs/guides/create-an-api-token/)
