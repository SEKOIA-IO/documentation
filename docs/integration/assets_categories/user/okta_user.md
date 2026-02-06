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

### Required API permissions

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

- `okta.users.read`: Read user profiles and attributes
- `okta.groups.read`: Read group information and memberships
- `okta.users.manage`: Full user management capabilities

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

## Information Collected

The Okta User asset connector fetches comprehensive user information from Okta and transforms it into the OCSF (Open Cybersecurity Schema Framework) User Inventory format for standardized security monitoring and asset management.

### Data Mapping Table

The following table shows how Okta user data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type |
|--------------|-----------------|-------------|-----------|
| `id` | `user.uid` | Okta user unique identifier | String |
| `profile.login` | `user.name` | User's login name/username | String |
| `profile.login` | `user.uid_alt` | Alternative user identifier (login name) | String |
| `profile.firstName` + `profile.lastName` | `user.full_name` | User's full name (concatenated) | String |
| `profile.email` | `user.email_addr` | User's primary email address | String |
| `profile.displayName` | `user.display_name` | User's display name | String |
| `profile.email` (domain part) | `user.domain` | Domain extracted from email address | String |
| `profile.login` | `user.account.name` | Account name (same as login) | String |
| `id` | `user.account.uid` | Account unique identifier (same as user ID) | String |
| Static value | `user.account.type` | Always "Okta Account" | String (Enum) |
| Static value | `user.account.type_id` | Always 99 (Other) | Integer (Enum) |
| `Groups[].id` | `user.groups[].uid` | Group unique identifier | String |
| `Groups[].profile.name` | `user.groups[].name` | Group name | String |
| `Groups[].profile.description` | `user.groups[].desc` | Group description | String |
| `Groups[].roles[].label` | `user.groups[].privileges[]` | List of role labels for the group (only active roles) | Array[String] |
| `Factors[]` | `user.has_mfa` | Whether user has MFA factors configured | Boolean |
| `Roles[].type` | `user.type` | User type: "Admin" if has admin role, otherwise "User" | String (Enum) |
| `Roles[].type` | `user.type_id` | User type ID: 2 (Admin) or 1 (User) | Integer (Enum) |
| `created` | `time` | User creation timestamp (Unix epoch) | Integer (timestamp) |

### OCSF Model Structure

The connector generates OCSF User Inventory events (class UID 5003) with the following structure:

```json
{
  "activity_id": 2,
  "activity_name": "Collect",
  "category_name": "Discovery",
  "category_uid": 5,
  "class_name": "User Inventory Info",
  "class_uid": 5003,
  "type_name": "User Inventory Info: Collect",
  "type_uid": 5003002,
  "severity": "Informational",
  "severity_id": 1,
  "time": "<unix_timestamp>",
  "metadata": {
    "product": {
      "name": "Okta",
      "version": "<version>"
    },
    "version": "<ocsf_version>"
  },
  "user": {
    "uid": "<user_id>",
    "name": "<login>",
    "uid_alt": "<login>",
    "full_name": "<firstName lastName>",
    "email_addr": "<email>",
    "display_name": "<displayName>",
    "domain": "<domain_from_email>",
    "type": "User|Admin",
    "type_id": 1|2,
    "has_mfa": true|false,
    "account": {
      "name": "<login>",
      "uid": "<user_id>",
      "type": "Okta Account",
      "type_id": 99
    },
    "groups": [
      {
        "uid": "<group_id>",
        "name": "<group_name>",
        "desc": "<group_description>",
        "privileges": ["<role_label>", ...]
      }
    ]
  }
}
```

### Enrichment Objects

The connector performs several enrichment operations to provide comprehensive user context:

#### User Groups Enrichment
- **Source**: `list_user_groups` API call
- **Enrichment**: Fetches all groups a user belongs to with pagination support
- **Fields added**: `user.groups[]` with group ID, name, and description
- **API Endpoint**: `/api/v1/users/{userId}/groups`
- **Pagination**: Uses `resp.has_next()` to iterate through all pages
- **Error Handling**: Continues on error, returns partial results

#### Group Privileges Enrichment
- **Source**: `list_group_assigned_roles` API call
- **Enrichment**: Retrieves all roles/privileges assigned to each group
- **Fields added**: `user.groups[].privileges[]` with role labels
- **API Endpoint**: `/api/v1/groups/{groupId}/roles`
- **Filtering**: Only includes roles with `ACTIVE` status
- **Purpose**: Provides visibility into effective permissions through group membership

#### MFA Status Enrichment
- **Source**: `list_factors` API call
- **Enrichment**: Determines if user has multi-factor authentication configured
- **Fields added**: `user.has_mfa` (boolean)
- **API Endpoint**: `/api/v1/users/{userId}/factors`
- **Logic**: Returns `true` if any factors exist, `false` if none or on error
- **Purpose**: Identifies users without MFA for security compliance

#### User Roles Enrichment
- **Source**: `list_assigned_roles_for_user` API call
- **Enrichment**: Retrieves roles directly assigned to the user
- **Fields added**: Used to determine `user.type` and `user.type_id`
- **API Endpoint**: `/api/v1/users/{userId}/roles`
- **Admin Detection**: Searches for "admin" in role type (case-insensitive)
- **Role Types Identified**: 
  - Admin roles: Sets `user.type` = "Admin", `user.type_id` = 2
  - Standard roles: Sets `user.type` = "User", `user.type_id` = 1

#### Full Name Construction
- **Source**: `profile.firstName` and `profile.lastName` fields
- **Enrichment**: Concatenates first and last name
- **Fields added**: `user.full_name`
- **Handling**: Uses "None" as placeholder if fields are null/empty
- **Format**: `"<firstName> <lastName>"` with trailing spaces stripped

#### Domain Extraction
- **Source**: `profile.email` field
- **Enrichment**: Extracts domain portion from email address
- **Fields added**: `user.domain`
- **Logic**: Splits email by "@" and takes the second part
- **Example**: `john.doe@example.com` → `example.com`
- **Fallback**: Returns empty string if email format is invalid

#### Display Name Mapping
- **Source**: `profile.displayName` field
- **Enrichment**: Maps Okta display name directly
- **Fields added**: `user.display_name`
- **Purpose**: Provides user-friendly name for UI display

#### Account Object Creation
- **Source**: `id` and `profile.login` fields
- **Enrichment**: Creates OCSF Account object for the user
- **Fields added**: 
  - `user.account.name` (login name)
  - `user.account.uid` (user ID)
  - `user.account.type` ("Okta Account")
  - `user.account.type_id` (99 for Other)

### API Endpoints Used

The connector uses the following Okta API endpoints to collect user information:

| API Endpoint | Purpose | Pagination | Error Handling |
|--------------|---------|------------|----------------|
| `/api/v1/users` | Retrieve all users in the organization | Yes (cursor-based) | Continues collection on error |
| `/api/v1/users/{userId}/groups` | Get groups for a specific user | Yes (cursor-based) | Returns empty list on error |
| `/api/v1/groups/{groupId}/roles` | Get roles assigned to a group | No | Returns empty list on error |
| `/api/v1/users/{userId}/factors` | Get MFA factors for a user | No | Returns false on error |
| `/api/v1/users/{userId}/roles` | Get roles assigned to a user | No | Returns empty list on error |


## Further Reading
- [Okta Documentation](https://developer.okta.com/docs/)
- [Okta User Management API](https://developer.okta.com/docs/reference/api/users/)
- [Okta Groups API](https://developer.okta.com/docs/reference/api/groups/)
- [Okta API Token Management](https://developer.okta.com/docs/guides/create-an-api-token/)

