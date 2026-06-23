uuid: bbc218bf-9cf4-4d77-8938-47cebe86801f
name: ESET EDR Devices
type: asset

## Overview

ESET EDR monitors, detects and mitigates threats on endpoints. It reduces the attack surface and prevents attacks by using anti-exploit, anti-ransomware, and advanced control technologies.

This setup guide shows how to forward device assets from ESET to Sekoia.io.

- **Vendor**: ESET
- **Product**: ESET Protect Hub / ESET Business Account
- **Supported environment**: Cloud

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

    ![Add a user](/assets/operation_center/asset_connectors/device/eset/eset_add_user.png)

3. Set the desired level of permissions for the user.

4. Under the **Permissions** section, enable the toggle next to **Integrations**.

    ![Enable integrations feature](/assets/operation_center/asset_connectors/device/eset/eset_integration_button.png)

5. Click **Next** and then **Create** to apply the changes.

6. The new user receives an invitation email and must finish the account creation process.

7. The new user must **log in to ESET PROTECT Hub at least once** before using the API services.

!!! note
    If you require custom permissions for the user, assign the required permission sets directly in ESET PROTECT. You can combine several permission sets if needed. Refer to the [List of permissions](https://help.eset.com/eset_connect/en-US/create_api_user_account.html) chapter for details.

### Create your asset connector

To start getting your ESET assets into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.

    ![create_asset_step_2.png](/assets/operation_center/asset_connectors/vulnerability/common/create_asset_connector_1.png)

3. Choose **ESET EDR**, give it a name, and fill in the required fields:

    - **Username**: The username (email) of the dedicated API user account you created.
    - **Password**: The password of the dedicated API user account.
    - **Region**: The region of your ESET account (e.g., `EU` or `US`).

    ![ESET EDR connector configuration form](/assets/operation_center/asset_connectors/device/eset/eset_connector.png)

4. Test the connection by clicking the **Test connector** button.

    ![Connector test result and Create asset connector button highlighted](/assets/operation_center/asset_connectors/device/eset/eset_test.png)

5. Click the **Create asset connector** button.

!!! warning
    - Ensure the dedicated API user has logged in to ESET PROTECT Hub at least once before configuring this connector.
    - The API user must have the **Integrations** toggle enabled under their access rights/permissions.

{!_shared_content/operations_center/integrations/generated_assets_documentation/eset_device.md!}