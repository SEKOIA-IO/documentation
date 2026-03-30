# okta\_user

uuid: b2e2e2c7-1a3e-4b7a-9c2d-8e4f3a6b7c9d name: Okta User type: asset

### Overview

Okta is a cloud-based identity and access management platform that provides secure authentication, authorization, and user management services. Okta helps organizations manage user identities across multiple applications and systems, providing single sign-on (SSO), multi-factor authentication (MFA), and comprehensive user lifecycle management.

* **Vendor**: Okta
* **Product**: Okta Identity Platform
* **Supported environment**: Cloud

### Configure

#### How to create an API token with proper permissions

To connect Okta to Sekoia.io, you need to create an API token with the necessary permissions to access Okta users and groups. Follow these steps:

1. Sign in to your Okta Admin Console and navigate to the Security section.
2. Click **API** in the left navigation pane, then click **Tokens**.
3. Click **Create Token** to generate a new API token.
4. Enter a name for the token (e.g., `sekoia-user-reader`)
5. Click **Create Token** to generate the API token.
6. Copy the **Token Value** to a safe location. You'll need this token to configure the connector in Sekoia.io.

!!! Warning - The token value is only shown when you create it. If you lose it, you must create a new token. - Store this token securely and never share it publicly. - Consider rotating API tokens regularly for security best practices.

#### Required API permissions

The API token must have the following scopes to successfully fetch Okta users and groups:

```json
{
    "scopes": [
        "okta.users.read",
        "okta.groups.read",
        "okta.users.manage"
    ]
}
```

**Required Scopes:**

* `okta.users.read`: Read user profiles and attributes
* `okta.groups.read`: Read group information and memberships
* `okta.users.manage`: Full user management capabilities

#### Create your asset

To start getting your Okta users into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.
2. Click the **+ New connector** button.
3. Choose **Okta User**, give it a name, and fill the required fields:
4. Enter the following information:
   * **API Token**: The API token value from your Okta organization
   * **Base URL**: Your Okta organization's base URL (e.g., `https://your-domain.okta.com`)
5. Test the connection by clicking the **Test connector** button.
6. Click the **Create asset connector** button.

{!\_shared\_content/operations\_center/integrations/generated\_assets\_documentation/okta\_user.md!}

### Further Reading

* [Okta Documentation](https://developer.okta.com/docs/)
* [Okta User Management API](https://developer.okta.com/docs/reference/api/users/)
* [Okta Groups API](https://developer.okta.com/docs/reference/api/groups/)
* [Okta API Token Management](https://developer.okta.com/docs/guides/create-an-api-token/)
