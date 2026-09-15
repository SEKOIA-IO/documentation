uuid: 1a3734fa-0919-4c38-877c-e8320eb3ec6b
name: Upwind
type: intake

## Overview

Upwind Security is a cloud-native security platform providing runtime threat detection, vulnerability management, and risk prioritization for cloud environments (AWS, Azure, GCP, Kubernetes). The integration collects detections raised by Upwind and forwards them to Sekoia.io.

- **Vendor**: Upwind
- **Supported environment**: SaaS
- **Detection based on**: Alerts
- **Supported application or feature**:
    - Detections

## Configure

### Prerequisite

To set up the integration, you need access to the `Upwind` console with permissions to manage credentials, as well as your Upwind **Organization ID**.

The Upwind API uses OAuth 2.0 with the client credentials grant. You must generate client credentials (a `Client ID` and `Client Secret`) that Sekoia.io will use to obtain an access token and call the API.

### Generate client credentials

1. Log into the Upwind console.
2. Go to `Settings` > `Credentials`.
3. Click the `Generate Credential` button.
4. Choose `API` as the credential type and give the credential a friendly name (or keep the auto-generated one).
5. Assign the permissions (scope and roles) required to read detections. You can mirror the permissions of an existing member group or define a custom scope and roles. Credentials can never exceed your own access levels.
6. Click `Generate`, then click `Save` in the bottom right-hand corner.
7. Copy the `Client ID` and `Client Secret`. The secret is only displayed once, so store it securely.
8. Note your `Organization ID` from the organization settings.

For more details, refer to the [Credentials](https://docs.upwind.io/settings/credentials) page in the Upwind documentation.

!!! note
    Access tokens automatically expire after 24 hours. The Sekoia.io connector requests a new token as needed using the client credentials, so no manual token rotation is required.

!!! warning "Select the correct region"
    Upwind exposes regional API endpoints. The **Base URL** you configure must match the region of your Upwind organization:

    - **US**: `https://api.upwind.io`
    - **EU**: `https://api.eu.upwind.io`
    - **ME**: `https://api.me.upwind.io`

    An access token is only valid for the region it was issued for and cannot be used across regions.

### Create your intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format **Upwind**.

When configuring the connector, provide the following information:

- **Base URL**: base URL of the Upwind API matching your region (`https://api.upwind.io` for US, `https://api.eu.upwind.io` for EU, `https://api.me.upwind.io` for ME)
- **Auth URL**: OAuth2 token endpoint (default `https://auth.upwind.io/oauth/token`)
- **Client ID**: the OAuth2 client ID created above
- **Client Secret**: the OAuth2 client secret created above
- **Organization ID**: your Upwind organization ID

{!_shared_content/operations_center/integrations/generated/1a3734fa-0919-4c38-877c-e8320eb3ec6b_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_1a3734fa-0919-4c38-877c-e8320eb3ec6b_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/1a3734fa-0919-4c38-877c-e8320eb3ec6b.md!}

### Further Readings

- [Upwind REST API documentation](https://docs.upwind.io/restapi/v1/introduction)
- [Upwind Credentials documentation](https://docs.upwind.io/settings/credentials)
