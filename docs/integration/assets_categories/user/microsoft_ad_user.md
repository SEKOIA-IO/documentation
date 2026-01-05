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

1. `Account Credentials`: A valid admin account.

2. `Network Connectivity: Ensure port 636 (LDAPS) is open between your network and the Sekoia.io ingestion point to allow secure communication.

### Create connector configuration

This connector utilizes the LDAPS (LDAP over SSL/TLS) protocol to ensure that your credentials and directory data remain encrypted during transit.

A key requirement for this configuration is the Base DN, which defines the starting point for the directory search.

- `Base DN`: This identifies the specific container or domain level where the connector starts looking for users.
      
      Example: OU=Users,DC=company,DC=com

!!! Warning 
        Ensure that the account used has a password that does not expire, or remember to update the connector settings in Sekoia.io whenever the password is changed, otherwise the synchronization will fail.

### Create your asset

To start getting your Microsoft Active Directory users into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.
    
    ![New connector button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_1.png)

3. Choose **Fetch user assets from Microsoft Active Directory**, give it a name, and fill the required fields:

    ![Microsoft Entra ID User connector configuration form](/assets/operation_center/asset_connectors/user/microsoft/active_directory/connector_in_catalogue.png)

4. Enter the following information:

      - **Servername**: The FQDN (Fully Qualified Domain Name) or static IP address of your Active Directory server
      - **Admin Username**: The username of the account used for the bind.
      - **Admin Password**: The password associated with the account.

5. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/user/microsoft/active_directory/test_connection.png)

6. Click the **Create asset connector** button.

## Further Reading
- [Microsoft: What is Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [LDAP Query Basics](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ldap/lightweight-directory-access-protocol-ldap-api)
