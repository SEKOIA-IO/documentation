uuid: a423222d-e8cc-4ad0-a266-8776f8993feb
name: Microsoft Defender for Endpoint Device
type: asset

## Overview

Microsoft Defender for Endpoint is a cloud-based endpoint security platform that provides advanced threat protection, detection, investigation, and response capabilities for enterprise devices. This connector retrieves device inventory information from the Microsoft Defender for Endpoint API and enriches it with device management data from Microsoft Intune via the Microsoft Graph API.

- **Vendor**: Microsoft
- **Product**: Microsoft Defender for Endpoint
- **Supported environment**: Cloud

## Configure

### How to create an app registration with proper permissions

To connect Microsoft Defender for Endpoint to Sekoia.io, you need to create an app registration with the necessary permissions to access device information. Follow these steps:

1. Sign in to the Azure portal and navigate to Microsoft Entra ID.

    ![Azure portal Microsoft Entra ID section](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_1.png)

2. Click **App registrations** in the left navigation pane, then click **New registration**.

    ![App registrations page with New registration button highlighted](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_2.png)

3. Enter a name for the application (e.g., `sekoia-defender-reader`) and click **Register**.

    ![App registration form with name field](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_3.png)

4. Copy the **Application (client) ID** and **Directory (tenant) ID** to a safe location. You'll need these values to configure the connector in Sekoia.io.

    ![App registration overview with client and tenant IDs](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_4.png)

### How to generate a client secret

After creating the app registration, you need to generate a client secret for authentication:

1. Click **Certificates & secrets** in the left navigation pane.

2. Click **New client secret** to generate a new secret.

    ![New client secret button highlighted](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_5.png)

3. Enter a description for the secret (e.g., `sekoia-defender-secret`) and select an expiration period, then click **Add**.

    ![Client secret creation form](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_6.png)

4. Copy the **Value** of the client secret to a safe location. You'll need this secret to configure the connector in Sekoia.io.

    ![Client secret value display](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_7.png)

!!! Warning
    - The client secret value is only shown when you create it. If you lose it, you must create a new client secret.
    - Store this secret securely and never share it publicly.
    - Consider rotating client secrets regularly for security best practices.

### Required API permissions

The app registration must have the following application permissions:


### How to grant API permissions

To grant the required permissions to your app registration:

1. Click **API permissions** in the left navigation pane.

2. Click **Add a permission** to add new permissions.

    ![Add a permission button highlighted](/assets/operation_center/asset_connectors/user/microsoft/entra_id/entra_id_application_8.png)

3. Select **APIs my organization uses**, search for **WindowsDefenderATP**, and click on it.

4. Select **Application permissions** and check **Machine.Read.All**, then click **Add permissions**.

5. Click **Add a permission** again, select **Microsoft Graph**, then select **Application permissions** and check **DeviceManagementManagedDevices.Read.All**, then click **Add permissions**.

6. Click **Grant admin consent** to grant the permissions (requires admin privileges).

### Required API permissions

The App Registration must have the following application permissions:

| API | Permission | Description |
|-----|------------|-------------|
| WindowsDefenderATP | `Machine.Read.All` | Read all machine information from Microsoft Defender for Endpoint |
| Microsoft Graph | `DeviceManagementManagedDevices.Read.All` | Read Microsoft Intune managed device data |

### Create your asset

To start getting your Microsoft Defender for Endpoint devices into Sekoia.io, you need to create an asset connector on the [Assets page](https://app.sekoia.io/assets). To do so, follow these steps:

1. Click the **Asset connectors** button to create a new connector.

    ![Asset connectors button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_button.png)

2. Click the **+ New connector** button.

    ![New connector button highlighted](/assets/operation_center/asset_connectors/device/common/create_asset_connector_1.png)

3. Choose **Microsoft Defender Device**, give it a name, and fill the required fields:

4. Enter the following information:

    - **Tenant ID**: Your Azure Directory (tenant) ID
    - **App ID**: The Application (client) ID of your App Registration
    - **App Secret**: The client secret value you created
    - **Base URL**: The Microsoft Defender for Endpoint API base URL (default: `https://api.securitycenter.microsoft.com`)

5. Test the connection by clicking the **Test connector** button.

6. Click the **Create asset connector** button.

{!_shared_content/operations_center/integrations/generated_assets_documentation/microsoft-defender_device.md!}

## Further Reading

- [Microsoft Defender for Endpoint API documentation](https://learn.microsoft.com/en-us/defender-endpoint/api/)
- [List machines API](https://learn.microsoft.com/en-us/defender-endpoint/api/get-machines)
- [Microsoft Graph - List managed devices (Intune)](https://learn.microsoft.com/en-us/graph/api/intune-devices-manageddevice-list?view=graph-rest-1.0)
- [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Microsoft Defender for Endpoint API permissions](https://learn.microsoft.com/en-us/defender-endpoint/api/apis-intro)
