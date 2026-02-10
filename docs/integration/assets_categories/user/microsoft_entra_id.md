uuid: 7dc16ecd-c119-4ca5-9039-1c83e355918a
name: Entra ID
type: asset

## Overview

Microsoft Entra ID (formerly Azure Active Directory) is a cloud-based identity and access management service that provides secure authentication, authorization, and user management services. Entra ID helps organizations manage user identities across Microsoft and third-party applications, providing single sign-on (SSO), multi-factor authentication (MFA), and comprehensive user lifecycle management.

- **Vendor**: Microsoft
- **Product**: Microsoft Entra ID
- **Supported environment**: Cloud

## Configure

### How to create an app registration with proper permissions

To connect Microsoft Entra ID to Sekoia.io, you need to create an app registration with the necessary permissions to access Entra ID users and groups. Follow these steps:

1. Sign in to the Azure portal and navigate to Microsoft Entra ID.

    ![Azure portal Microsoft Entra ID section](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_1.png)

2. Click **App registrations** in the left navigation pane, then click **New registration**.

    ![App registrations page with New registration button highlighted](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_2.png)

3. Enter a name for the application (e.g., `sekoia-user-reader`) and click **Register**.

    ![App registration form with name field](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_3.png)

4. Copy the **Application (client) ID** and **Directory (tenant) ID** to a safe location. You'll need these values to configure the connector in Sekoia.io.

    ![App registration overview with client and tenant IDs](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_4.png)

### How to generate a client secret

After creating the app registration, you need to generate a client secret for authentication:

1. Click **Certificates & secrets** in the left navigation pane.

2. Click **New client secret** to generate a new secret.

    ![New client secret button highlighted](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_5.png)

3. Enter a description for the secret (e.g., `sekoia-connector-secret`) and select an expiration period, then click **Add**.

    ![Client secret creation form](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_6.png)

4. Copy the **Value** of the client secret to a safe location. You'll need this secret to configure the connector in Sekoia.io.

    ![Client secret value display](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_7.png)

!!! Warning
    - The client secret value is only shown when you create it. If you lose it, you must create a new client secret.
    - Store this secret securely and never share it publicly.
    - Consider rotating client secrets regularly for security best practices.

### Required API permissions

The app registration must have the following permissions to successfully fetch Entra ID users and groups:

```json
{
    "permissions": [
        "User.Read.All",
        "Group.Read.All",
        "GroupMember.Read.All",
        "Directory.Read.All",
        "UserAuthenticationMethod.Read.All"
    ]
}
```

**Required Permissions:**

- `User.Read.All`: Read user profiles and attributes
- `Group.Read.All`: Read group information and memberships
- `GroupMember.Read.All`: Read group memberships
- `Directory.Read.All`: Read directory data
- `UserAuthenticationMethod.Read.All`: Read user authentication methods

### How to grant API permissions

To grant the required permissions to your app registration:

1. Click **API permissions** in the left navigation pane.

2. Click **Add a permission** to add new permissions.

    ![Add a permission button highlighted](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_8.png)

3. Select **Microsoft Graph** as the API.

    ![Microsoft Graph API selection](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_9.png)

4. Select **Application permissions** and search for the required permissions:

      - `User.Read.All`
      - `Group.Read.All`
      - `GroupMember.Read.All`
      - `Directory.Read.All`
      - `UserAuthenticationMethod.Read.All`

    ![Application permissions selection](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_10.png)

5. Click **Add permissions** to add the selected permissions.

6. Click **Grant admin consent** to grant the permissions (requires admin privileges).

### Create your asset

To start getting your Microsoft Entra ID users into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![New connector button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_1.png)

3. Choose **Microsoft Entra ID User**, give it a name, and fill the required fields:

    ![Microsoft Entra ID User connector configuration form](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_asset_1.png)

4. Enter the following information:

      - **Tenant ID**: The Directory (tenant) ID from your app registration
      - **Client ID**: The Application (client) ID from your app registration
      - **Client Secret**: The client secret value you generated

5. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_asset_2.png)

6. Click the **Create asset connector** button.

## Further Reading
- [Microsoft Entra ID Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/)
- [Microsoft Graph User API](https://docs.microsoft.com/en-us/graph/api/resources/user)
- [Microsoft Graph Groups API](https://docs.microsoft.com/en-us/graph/api/resources/group)
- [App Registration Guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

