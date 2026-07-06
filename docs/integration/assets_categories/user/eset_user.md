uuid: 661ac982-171b-4308-9a77-6c28fa275a7f
name: ESET User
type: asset

## Overview

ESET user management centralizes the identities managed through ESET Cloud Office Security (ECOS) — the Microsoft 365 and Google Workspace users protected by ESET. This asset connector forwards those users, with their identity provider, groups and profile attributes, to Sekoia.io.

This setup guide shows how to forward user assets from ESET to Sekoia.io.

- **Vendor**: ESET
- **Product**: ESET PROTECT / ESET Cloud Office Security
- **Supported environment**: Cloud

!!! warning
    The ESET user management API is only available on accounts with an **ESET Cloud Office Security (ECOS)** subscription. ESET users are the Microsoft 365 / Google Workspace identities synced through ECOS. Without an ECOS subscription the API returns `501 Not Implemented`; the connector handles this gracefully (it logs a warning and collects no users), so it is safe to enable but will only produce assets once ECOS is in place.

## Configure

### Create a dedicated API user account

We recommend creating a dedicated API user to separate your regular account from API activities.

!!! note
    Only the Root or Superuser can create a user with access to API endpoints. API access rights cannot be granted to the ESET Business Account Superuser, ESET MSP Administrator 2 Root user, and ESET PROTECT Hub Superuser accounts.

#### For ESET Business Account and ESET MSP Administrator 2

1. Log in as a **Superuser** (or Root) to your `ESET Business Account` or `ESET MSP Administrator 2`.

2. Navigate to **User management** and create a new user with the desired level of access rights.

3. Under the **Access Rights** section, enable the toggle next to **Integrations**.

4. Click **Create** to apply the changes.

5. The new user receives an invitation email and must finish the account creation process.

#### For ESET PROTECT Hub

1. Log in as a **Superuser** to your `ESET PROTECT Hub` account.

2. Navigate to **Users** and add a new user.

3. Set the desired level of permissions for the user.

4. Under the **Permissions** section, enable the toggle next to **Integrations**.

5. Click **Next** and then **Create** to apply the changes.

6. The new user receives an invitation email and must finish the account creation process.

7. The new user must **log in to ESET PROTECT Hub at least once** before using the API services.

!!! note
    If you require custom permissions for the user, assign the required permission sets directly in ESET PROTECT. You can combine several permission sets if needed. Refer to the [List of permissions](https://help.eset.com/eset_connect/en-US/create_api_user_account.html) chapter for details.

### Create your asset connector

To start getting your ESET users into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.

    ![New connector button highlighted](/assets/operation_center/asset_connectors/user/common/create_asset_connector_1.png)

3. Choose **ESET User**, give it a name, and fill in the required fields:

    - **Username**: The username (email) of the dedicated API user account you created.
    - **Password**: The password of the dedicated API user account.
    - **Region**: The region of your ESET account (e.g., `eu` or `us`).

4. Test the connection by clicking the **Test connector** button.

5. Click the **Create asset connector** button.

!!! warning
    - Ensure the dedicated API user has logged in to ESET PROTECT Hub at least once before configuring this connector.
    - The API user must have the **Integrations** toggle enabled under their access rights/permissions.
    - An ESET Cloud Office Security (ECOS) subscription is required for users to be returned.

{!_shared_content/operations_center/integrations/generated_assets_documentation/eset_user.md!}

## Further Reading
- [ESET Connect User Management API](https://help.eset.com/eset_connect/en-US/user_management.html)
- [ESET Cloud Office Security](https://help.eset.com/ecos/en-US/)
- [ESET Connect API user account](https://help.eset.com/eset_connect/en-US/create_api_user_account.html)
