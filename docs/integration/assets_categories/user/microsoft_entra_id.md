uuid: b6e2e2e2-4c3a-4b7a-9e2a-1f2c3d4e5f6a
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
        "UserAuthenticationMethod.Read.All",
        "AuditLog.Read.All"

    ]
}
```

**Required Permissions:**

- `User.Read.All`: Read user profiles and attributes
- `Group.Read.All`: Read group information and memberships
- `GroupMember.Read.All`: Read group memberships
- `Directory.Read.All`: Read directory data
- `UserAuthenticationMethod.Read.All`: Read user authentication methods
- `AuditLog.Read.All`: Read audit logs (optional, for enhanced logging and monitoring)

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
      - `AuditLog.Read.All`

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

## Information Collected

The Microsoft Entra ID asset connector retrieves comprehensive user information from your Entra ID tenant and maps it to the OCSF (Open Cybersecurity Schema Framework) User Inventory model. Below is a detailed mapping table showing how data is collected and transformed:

### Data Mapping Table

| Microsoft Entra ID Field | OCSF Field Path | Description | Data Type |
|--------------------------|-----------------|-------------|-----------|
| `id` | `user.uid` | Unique user identifier in Entra ID | String |
| `displayName` | `user.name` | User's display name | String |
| `mail` | `user.email_addr` | User's primary email address | String |
| `userPrincipalName` | `user.account.name` | User principal name (UPN) | String |
| `userPrincipalName` (domain part) | `user.domain` | Domain extracted from UPN (after @) | String |
| `mailNickname` | `user.email_addr` (fallback) | Email alias if primary email is unavailable | String |
| `accountEnabled` | `enrichments[].data.is_enabled` | Account enabled/disabled status | Boolean |
| `department` | `enrichments[].data` (employment) | User's department | String |
| `jobTitle` | `enrichments[].data` (employment) | User's job title | String |
| `employeeId` | `enrichments[].data` (employment) | Employee identifier | String |
| `employeeType` | `enrichments[].data` (employment) | Type of employee (e.g., employee, contractor) | String |
| `companyName` | `user.org.name` | Company/organization name | String |
| `officeLocation` | `user.org.ou_name` | Physical office location | String |
| `createdDateTime` | `time` | Account creation timestamp | DateTime |
| `signInActivity.lastSignInDateTime` | `enrichments[].data.last_logon` | Last successful sign-in timestamp | DateTime |
| `isManagementRestricted` | `enrichments[].data.is_restricted` | Management restriction status | Boolean |
| **Derived from Groups API** | | | |
| Group membership | `user.groups[]` | List of groups user belongs to | Array |
| Group `id` | `user.groups[].uid` | Group unique identifier | String |
| Group `displayName` | `user.groups[].name` | Group display name | String |
| **Derived from Directory Roles API** | | | |
| Admin role membership | `user.type_id` / `user.type_str` | User type (User=0, Admin=1) | Enum |
| **Derived from Authentication Methods API** | | | |
| MFA methods (Authenticator, Phone, OATH) | `enrichments[].data.is_mfa` | Multi-factor authentication status | Boolean |

### OCSF Model Structure

The connector generates a complete OCSF User Inventory event with the following structure:

- **OCSF Class**: User Inventory Info (class_uid: 5003)
- **OCSF Category**: Discovery (category_uid: 5)
- **Activity**: Collect (activity_id: 2)
- **Type**: User Inventory (type_uid: 500302)

### Enrichment Objects

The connector creates multiple enrichment objects to provide additional context:

1. **Account Status Enrichment** (`enrichments[0]`):
   - `name`: "account"
   - `value`: "status"
   - Contains: `is_enabled`, `is_mfa`, `is_restricted`, `last_logon`

2. **Employment Information Enrichment** (`enrichments[1]`, if applicable):
   - `name`: "employment"
   - `value`: Department and Job Title
   - Contains: Employment-related attributes

### API Endpoints Used

The connector makes the following Microsoft Graph API calls:

1. **Users List**: `GET /users` - Retrieves user profiles with filtering by creation date
2. **User Groups**: `GET /users/{user_id}/memberOf` - Fetches group memberships
3. **Admin Roles**: `GET /users/{user_id}/transitiveMemberOf/microsoft.graph.directoryRole` - Checks for admin role assignments
4. **MFA Methods**: `GET /users/{user_id}/authentication/methods` - Retrieves configured authentication methods

!!! Note
    - The connector supports incremental synchronization, fetching only users created after the last successful run.
    - Pagination is automatically handled for large datasets.
    - All timestamps are converted to Unix epoch format for OCSF compatibility.

## Further Reading
- [Microsoft Entra ID Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/)
- [Microsoft Graph User API](https://docs.microsoft.com/en-us/graph/api/resources/user)
- [Microsoft Graph Groups API](https://docs.microsoft.com/en-us/graph/api/resources/group)
- [App Registration Guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

