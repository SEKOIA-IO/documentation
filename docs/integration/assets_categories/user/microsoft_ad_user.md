uuid: 226573e7-3969-4e31-bb3a-0846760b35b9
name: Microsoft Active Directory User
type: asset

## Overview

Microsoft Active Directory (AD) is a directory service developed by Microsoft for Windows domain networks. It provides central authentication and authorization for users, computers, and other resources in an on-premise environment. Integrating Active Directory with Sekoia.io allows for the synchronization of users to enhance security analysis and alert context.

- **Vendor**: Microsoft
- **Product**: Microsoft Active Directory
- **Supported environment**: On-premise

## Configure

### Prerequisites

To connect your on-premise Active Directory to Sekoia.io, ensure the following requirements are met:

1. `Service Account`: A dedicated service account with read-only permissions.

    !!! tip "Recommended: Create a least-privilege account"
        Instead of using an admin account, create a dedicated service account with minimal permissions:
        
        1. Open **Active Directory Users and Computers**
        2. Create a new user account (e.g., `svc-sekoia-sync`)
        3. Right-click on the OU containing your users → **Delegate Control**
        4. Add the service account and select **Read all user information**
        5. Apply to the relevant OUs containing users
        
        This account only needs:
        
        - Read permissions on the Users container (or specific OUs)
        - Read All Properties on User objects
        - No write, delete, or modify permissions

2. `Network Connectivity`: Ensure port 636 (LDAPS) is open between your network and the Sekoia.io ingestion point to allow secure communication.


### Create connector configuration

This connector utilizes the LDAPS (LDAP over SSL/TLS) protocol to ensure that your credentials and directory data remain encrypted during transit.

A key requirement for this configuration is the Base DN, which defines the starting point for the directory search.

- `Base DN`: This identifies the specific container or domain level where the connector starts looking for users.
      
  Example: `OU=Users,DC=company,DC=com`

!!! Warning 
        Ensure that the account used has a password that does not expire, or remember to update the connector settings in Sekoia.io whenever the password is changed, otherwise the synchronization will fail.

### Create your asset

To start getting your Microsoft Active Directory users into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![New connector button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_1.png)

3. Choose **Fetch user assets from Microsoft Active Directory**, give it a name, and fill the required fields:

    ![Microsoft Active Directory User connector configuration form](/assets/operation_center/asset_connectors/user/microsoft/active_directory/connector_in_catalogue.png)

4. Enter the following information:

      - **Servername**: The FQDN (Fully Qualified Domain Name) or static IP address of your Active Directory server
      - **Admin Username**: The username of the account used for the bind.
      - **Admin Password**: The password associated with the account.

5. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/user/microsoft/active_directory/test_connection.png)

6. Click the **Create asset connector** button.

## Information Collected

This section describes the data fields collected from Microsoft Active Directory and how they map to the Open Cybersecurity Schema Framework (OCSF) User Inventory model.

### Data Mapping Table

The following table shows the mapping between Active Directory attributes and OCSF model fields:

| AD Attribute | OCSF Field Path | Description | Data Type |
|--------------|-----------------|-------------|-----------|
| `givenName` | `user.name` | User's first name (combined with `sn` for full name) | String |
| `sn` | `user.name` | User's last name (surname, combined with `givenName`) | String |
| `userPrincipalName` | `user.account.name` | User Principal Name (e.g., user@domain.com) | String |
| `objectSid` | `user.uid` | Security Identifier - unique identifier for the user | String |
| `objectSid` | `user.account.uid` | Security Identifier used for account identification | String |
| `objectGUID` | `user.uid_alt` | Globally Unique Identifier - alternative identifier | String (GUID) |
| `displayName` | `user.full_name` | User's display name | String |
| `displayName` | `user.display_name` | User's display name | String |
| `mail` | `user.email_addr` | User's email address | String |
| `distinguishedName` | `user.domain` | Distinguished Name indicating organizational location | String |
| `member_of` | `user.groups[]` | List of groups the user belongs to | Array of Groups |
| `whenCreated` | `time` | Timestamp when the user was created in AD | Datetime |
| `userAccountControl` | `enrichments[].data.is_enabled` | Indicates if the account is enabled (UAC & 2 check) | Boolean |
| `lastLogon` | `enrichments[].data.last_logon` | Timestamp of user's last logon | Timestamp |
| `badPwdCount` | `enrichments[].data.bad_password_count` | Number of failed password attempts | Integer |
| `logonCount` | `enrichments[].data.number_of_logons` | Total number of successful logons | Integer |

### OCSF Model Structure

The connector produces user assets conforming to the OCSF User Inventory Info event class (UID: 5003) with the following structure:

**Event Metadata:**

- `activity_id`: 2 (Collect)
- `activity_name`: "Collect"
- `category_uid`: 5 (Discovery)
- `category_name`: "Discovery"
- `class_uid`: 5003 (User Inventory Info)
- `class_name`: "User Inventory Info"
- `type_uid`: 500302
- `type_name`: "User Inventory"
- `severity`: "Informational"
- `severity_id`: 1

**Product Metadata:**

- `metadata.product.name`: "Microsoft Active Directory"
- `metadata.product.vendor_name`: "Microsoft"
- `metadata.product.version`: "N/A"
- `metadata.version`: "1.6.0" (OCSF schema version)

**User Object:**

- `user.name`: Constructed from first and last name
- `user.uid`: objectSid (primary identifier)
- `user.uid_alt`: objectGUID (alternative identifier)
- `user.full_name`: Display name
- `user.display_name`: Display name
- `user.email_addr`: Email address
- `user.domain`: Distinguished Name
- `user.type`: "User" or "Admin" (based on group membership)
- `user.type_id`: 1 (User) or 2 (Admin)
- `user.account`: Account object with type LDAP_ACCOUNT
- `user.groups`: Array of Group objects

### Enrichment Objects

The connector provides additional enrichment data through the `enrichments` array:

**Login Information Enrichment:**

- `name`: "login"
- `value`: "infos"
- `data`: UserDataObject containing:
  - `is_enabled`: Boolean indicating if the account is enabled (derived from userAccountControl bit flag)
  - `last_logon`: Timestamp of the user's last successful logon (null if never logged in or invalid)
  - `bad_password_count`: Number of failed password attempts
  - `number_of_logons`: Total count of successful logons

**User Type Detection:**

The connector automatically determines user type based on group membership:

- **Admin User**: If any group DN contains "admin" (case-insensitive)
- **Regular User**: Default type for all other users

**Notes:**

- All attributes marked as "Unknown" if not present in Active Directory
- The `lastLogon` value is validated to exclude invalid dates (before 1601)
- The `objectGUID` is stripped of curly braces for consistent formatting
- Group names are extracted from the Distinguished Name of each group membership

## Further Reading
- [Microsoft: What is Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [LDAP Query Basics](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ldap/lightweight-directory-access-protocol-ldap-api)
