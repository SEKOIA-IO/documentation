uuid: b2e2e2c7-1a3e-4b7a-9c2d-8e4f3a6b7c9d
name: Okta User
type: asset

## Overview

Okta is a cloud-based identity and access management platform that provides secure authentication, authorization, and user management services. Okta helps organizations manage user identities across multiple applications and systems, providing single sign-on (SSO), multi-factor authentication (MFA), and comprehensive user lifecycle management.

- **Vendor**: Okta
- **Product**: Okta Identity Platform
- **Supported environment**: Cloud

## Configure

### How to create an API token with proper permissions

To connect Okta to Sekoia.io, you need to create an API token with the necessary permissions to access Okta users and groups. Follow these steps:

1. Sign in to your Okta Admin Console and navigate to the Security section.

    ![Okta Admin Console Security section](/assets/operation_center/asset_connectors/user/okta/okta_api_key_1.png)

2. Click **API** in the left navigation pane, then click **Tokens**.

3. Click **Create Token** to generate a new API token.

    ![Create Token button highlighted](/assets/operation_center/asset_connectors/user/okta/okta_api_key_2.png)

4. Enter a name for the token (e.g., `sekoia-user-reader`)

5. Click **Create Token** to generate the API token.

    ![Token creation confirmation](/assets/operation_center/asset_connectors/user/okta/okta_api_key_3.png)

6. Copy the **Token Value** to a safe location. You'll need this token to configure the connector in Sekoia.io.

    ![API Token value display](/assets/operation_center/asset_connectors/user/okta/okta_api_key_4.png)

!!! Warning
    - The token value is only shown when you create it. If you lose it, you must create a new token.
    - Store this token securely and never share it publicly.
    - Consider rotating API tokens regularly for security best practices.

### Required permissions

Okta API tokens have no scopes of their own. A token inherits the permissions of the administrator who created it, so create it with an account that has the minimum access listed below.

The connector only performs read operations:

| Okta API operation | Purpose | Equivalent OAuth scope |
| --- | --- | --- |
| List users | Collect user profiles | `okta.users.read` |
| List user groups | Collect group memberships | `okta.users.read` |
| List user factors | Enrich users with their MFA status | `okta.users.read` |
| List roles assigned to a user | Collect user administrator roles | `okta.roles.read` |
| List roles assigned to a group | Collect group privileges | `okta.roles.read` |

We recommend creating the token with a dedicated service account that has the **Read-Only Administrator** role. This role grants read access to users, groups, factors and administrator role assignments, and no write access.

!!! Note
    The connector needs no write permission, such as `okta.users.manage`.

!!! Warning
    If the token cannot read factors or role assignments, the connector still collects users but leaves the MFA and privilege information empty. It logs a warning, and the connection test still succeeds.

### Create your asset

To start getting your Okta users into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![New connector button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_1.png)

3. Choose **Okta User**, give it a name, and fill the required fields:

    ![Okta User connector configuration form](/assets/operation_center/asset_connectors/user/okta/okta_asset_user_1.png)

4. Enter the following information:
   - **API Token**: The API token value from your Okta organization
   - **Base URL**: Your Okta organization's base URL (e.g., `https://your-domain.okta.com`)

5. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/user/okta/okta_asset_user_2.png)

6. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/okta_user.md!}

## Further Reading
- [Okta Documentation](https://developer.okta.com/docs/)
- [Okta User Management API](https://developer.okta.com/docs/reference/api/users/)
- [Okta Groups API](https://developer.okta.com/docs/reference/api/groups/)
- [Okta API Token Management](https://developer.okta.com/docs/guides/create-an-api-token/)

