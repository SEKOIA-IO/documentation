uuid: a9b9f7be-a036-4e10-a407-53bc3b8308b4
name: Microsoft Entra ID (Graph API)
type: intake

## Overview

**Microsoft Entra ID (Graph API)** is a cloud-based Identity and Rights management service. The service is developed and managed by Microsoft Corp.

- **Vendor**: Microsoft
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs, Authentication logs

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.
    
!!! Danger "Scalability"
    This integration will collect the events through Microsoft Graph API, which is only recommended for small environments. For larger environments, it is recommended to use the Microsoft Entra ID / Azure AD integration (see [Microsoft Entra ID](entra_id.md))

## Configure

### How to create an app registration with proper permissions

To connect Microsoft Entra ID to Sekoia.io, you need to create an app registration with the necessary permissions to access Entra ID users and groups. Follow these steps:

1. Sign in to the Azure portal and navigate to Microsoft Entra ID.

    ![Azure portal Microsoft Entra ID section](/assets/integration/cloud_and_saas/entra_id/entra_id_application_1.png)

2. Click **App registrations** in the left navigation pane, then click **New registration**.

    ![App registrations page with New registration button highlighted](/assets/integration/cloud_and_saas/entra_id/entra_id_application_2.png)

3. Enter a name for the application (e.g., `sekoia-logs-reader`) and click **Register**.

    ![App registration form with name field](/assets/integration/cloud_and_saas/entra_id/entra_id_application_3.png)

4. Copy the **Application (client) ID** and **Directory (tenant) ID** to a safe location. You'll need these values to configure the connector in Sekoia.io.

    ![App registration overview with client and tenant IDs](/assets/integration/cloud_and_saas/entra_id/entra_id_application_4.png)

### How to generate a client secret

After creating the app registration, you need to generate a client secret for authentication:

1. Click **Certificates & secrets** in the left navigation pane.

2. Click **New client secret** to generate a new secret.

    ![New client secret button highlighted](/assets/integration/cloud_and_saas/entra_id/entra_id_application_5.png)

3. Enter a description for the secret (e.g., `sekoia-connector-secret`) and select an expiration period, then click **Add**.

    ![Client secret creation form](/assets/integration/cloud_and_saas/entra_id/entra_id_application_6.png)

4. Copy the **Value** of the client secret to a safe location. You'll need this secret to configure the connector in Sekoia.io.

    ![Client secret value display](/assets/integration/cloud_and_saas/entra_id/entra_id_application_7.png)

!!! Warning
    - The client secret value is only shown when you create it. If you lose it, you must create a new client secret.
    - Store this secret securely and never share it publicly.
    - Consider rotating client secrets regularly for security best practices.

### Required API permissions

The app registration must have the following permissions to successfully fetch Entra ID users and groups:

```json
{
    "permissions": [
        "AuditLog.Read.All",
        "Directory.Read.All"
    ]
}
```

**Required Permissions:**
- `AuditLog.Read.All`: Read the log endpoint
- `Directory.Read.All`: Read directory data (optional, for advanced features)

### How to grant API permissions

To grant the required permissions to your app registration:

1. Click **API permissions** in the left navigation pane.

2. Click **Add a permission** to add new permissions.

    ![Add a permission button highlighted](/assets/integration/cloud_and_saas/entra_id/entra_id_application_8.png)

3. Select **Microsoft Graph** as the API.

    ![Microsoft Graph API selection](/assets/integration/cloud_and_saas/entra_id/entra_id_application_9.png)

4. Select **Application permissions** and search for the required permissions:
   - `AuditLog.Read.All`
   - `Directory.Read.All`

    ![Application permissions selection](/assets/integration/cloud_and_saas/entra_id/entra_id_application_10.png)

5. Click **Add permissions** to add the selected permissions.

6. Click **Grant admin consent** to grant the permissions (requires admin privileges).

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `GraphAPI for Microsoft Entra ID / Azure AD`.
2. Fill the form with the information collected during the app registration process.


#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a9b9f7be-a036-4e10-a407-53bc3b8308b4_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/a9b9f7be-a036-4e10-a407-53bc3b8308b4.md!}


