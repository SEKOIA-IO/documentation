# entra\_id\_graph\_api

uuid: a9b9f7be-a036-4e10-a407-53bc3b8308b4 name: Microsoft Entra ID (Graph API) type: intake

### Overview

**Microsoft Entra ID (Graph API)** is a cloud-based Identity and Rights management service. The service is developed and managed by Microsoft Corp.

* **Vendor**: Microsoft
* **Supported environment**: SaaS
* **Detection based on**: Telemetry
* **Supported application or feature**: Application logs, Authentication logs
* **Supported events**:
  * [Interactive user sign-in events](https://learn.microsoft.com/en-us/graph/api/signin-list)
  * [Federated sign-in events](https://learn.microsoft.com/en-us/graph/api/signin-list)
  * [Provisioning events](https://learn.microsoft.com/en-us/graph/api/provisioningobjectsummary-list)
  * [Audit logs](https://learn.microsoft.com/en-us/graph/api/directoryaudit-list)

!!! Danger "Scalability" This integration will collect the events through Microsoft Graph API, which is only recommended for small environments. We can suggest using next numbers in order to decide which integration to use:

```
1. Sign-ins per day: < 300,000

2. Sign-ins per second (peak): < 10/sec

3. Audit logs per day: < 100,000

4. Total logs/day: < 500,000

5. Total logs/day: 250,000 – 1,500,000

If your environment exceeds these numbers, we strongly recommend to use the Microsoft Entra ID / Azure AD integration (see [Microsoft Entra ID](entra_id.md))
```

### Configure

#### How to create an app registration with proper permissions

To connect Microsoft Entra ID to Sekoia.io, you need to create an app registration with the necessary permissions to access Entra ID users and groups. Follow these steps:

1. Sign in to the Azure portal and navigate to Microsoft Entra ID.
2. Click **App registrations** in the left navigation pane, then click **New registration**.
3. Enter a name for the application (e.g., `sekoia-logs-reader`) and click **Register**.
4. Copy the **Application (client) ID** and **Directory (tenant) ID** to a safe location. You'll need these values to configure the connector in Sekoia.io.

#### How to generate a client secret

After creating the app registration, you need to generate a client secret for authentication:

1. Click **Certificates & secrets** in the left navigation pane.
2. Click **New client secret** to generate a new secret.
3. Enter a description for the secret (e.g., `sekoia-connector-secret`) and select an expiration period, then click **Add**.
4. Copy the **Value** of the client secret to a safe location. You'll need this secret to configure the connector in Sekoia.io.

!!! Warning - The client secret value is only shown when you create it. If you lose it, you must create a new client secret. - Store this secret securely and never share it publicly. - Consider rotating client secrets regularly for security best practices.

#### Required API permissions

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

* `AuditLog.Read.All`: Read the log endpoint
* `Directory.Read.All`: Read directory data (optional, for advanced features)

#### How to grant API permissions

To grant the required permissions to your app registration:

1. Click **API permissions** in the left navigation pane.
2. Click **Add a permission** to add new permissions.
3. Select **Microsoft Graph** as the API.
4. Select **Application permissions** and search for the required permissions:
   * `AuditLog.Read.All`
   * `Directory.Read.All`
5. Click **Add permissions** to add the selected permissions.
6. Click **Grant admin consent** to grant the permissions (requires admin privileges).

#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `GraphAPI for Microsoft Entra ID / Azure AD`.
2. Fill the form with the information collected during the app registration process.

**Enjoy your events on the** [**Events page**](https://app.sekoia.io/operations/events)

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_a9b9f7be-a036-4e10-a407-53bc3b8308b4\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/a9b9f7be-a036-4e10-a407-53bc3b8308b4.md!}
