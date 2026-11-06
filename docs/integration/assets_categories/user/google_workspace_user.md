uuid: 0beae7f6-e483-4bf9-b106-014ec8b25283
name: Google Workspace User
type: asset

## Overview

Google Workspace is Google's suite of productivity and collaboration applications. Its directory holds the user accounts of the organization, their groups, organizational units and security settings such as 2-step verification.

This asset connector collects the users of a Google Workspace domain with the Admin SDK Directory API.

- **Vendor**: Google
- **Product**: Google Workspace
- **Supported environment**: Cloud

### Collection

The connector runs once a day. Each run lists every user of the domain and sends to Sekoia.io only the users that are new or changed since the previous run. A user who signed in since the previous run is sent again, as their last logon changed.

!!! Note
    Users deleted from Google Workspace are not removed from Sekoia.io.

## Configure

### Prerequisites

- Administrator access to the Google Cloud console and to the Google Workspace Admin console
- A Google Workspace administrator account allowed to read users and groups

### Create a dedicated service account

1. In the Google Cloud console, create or select a project.
2. Under *APIs & Services* > *Library*, select the *Admin SDK API* and click *Enable*.
3. Under *IAM & Admin* > *Service Accounts*, click *Create Service Account*, specify its details and click *Done*.
4. Select the service account, open the **Keys** tab, click **Add key** > **Create new key**, select **JSON** and click **Create**. Keep the downloaded file: its content is the credentials of the connector.

!!! Tip
    The service account used by the [Google Workspace / ChromeOS intake](../../categories/applicative/google_reports.md) can be reused. In that case, add the scopes below to its existing domain-wide delegation.

### Grant domain-wide delegation

1. In the Google Cloud console, open the service account, expand *Advanced settings* and copy its *Client ID*.
2. Sign in to the Google Workspace Admin console with a **super administrator** account.
3. Go to *Security* > *Access and data control* > *API controls* and click *Manage Domain Wide Delegation*.
4. Click *Add new* (or edit the existing entry of the service account), paste the client ID and enter the following OAuth scopes:
    - `https://www.googleapis.com/auth/admin.directory.user.readonly`: read users
    - `https://www.googleapis.com/auth/admin.directory.group.readonly`: read groups and their members
5. Click *Authorize*.

!!! Warning
    The OAuth scopes of a domain-wide delegation entry replace the previous ones. When you edit an existing entry, keep the scopes it already has.

For more details, read [Create a service account](https://developers.google.com/workspace/guides/create-credentials#service-account) and [Set up domain-wide delegation](https://support.google.com/a/answer/162106).

### Create your asset

To start getting your Google Workspace users into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.

    ![New connector button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_1.png)

3. Choose **Google Workspace Users**, give it a name, and fill the required fields:
   - **Credentials**: the content of the JSON key file of the service account
   - **Admin mail**: the email of the Google Workspace administrator the service account acts as

4. Test the connection by clicking the **Test connector** button.

    !!! Note
        The test checks the service account key only. Domain-wide delegation, OAuth scopes and the admin mail are checked at the first collection: failures are reported in the connector logs.

5. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/google_user.md!}

## Further Reading
- [Directory API: Users](https://developers.google.com/workspace/admin/directory/reference/rest/v1/users)
- [Directory API: Groups](https://developers.google.com/workspace/admin/directory/reference/rest/v1/groups)
- [Directory API: Members](https://developers.google.com/workspace/admin/directory/reference/rest/v1/members)
