# Configure Single Sign-on with Microsoft Entra ID (Azure AD)

In order to configure Azure with Sekoia.io, the following steps must be done:

1. Verify that the user that will connect have a complete profile. To authenticate, the profile must have the following information: email address, first name, last name and full name
2. Create a new application on Azure
3. Connect to Sekoia.io, add a new domain that belongs to your community and wait for its validation
4. Configure OpenID Connect in Sekoia.io (see associated documentation [Single Sign-On With OpenID Connect](/getting_started/sso/openid_connect.md))

## Important Note on SSO Configuration for Multiple Business Entities

When configuring Single Sign-On (SSO) for organizations that have multiple business entities with the same email domain, it's essential to ensure that users from one entity do not have access to the other’s Sekoia communities. Here are specific recommendations to achieve this:

- **Disable Automatic User Creation**: While configuring SSO for both entities, ensure that the "automatically create user if missing" option is **NOT** enabled. This setting will prevent unintended account creation across different communities. Only manually created account in a community will have the possibility to login to it.
- **Allow Same Domain**: SSO can be configured to support the same email domain across two distinct communities without issues. This means entities can use the same domain for authentication while keeping their communities isolated.
- **Utilize Distinct Providers**: It’s advisable to set up unique providers for each business entity, which involves **creating separate policies**. This configuration will help restrict access to specific users and reduce the possibility of misconfiguration on Sekoia.io.

## Create a Microsoft Entra ID (Azure AD)  app registration

1. Visit "Microsoft Entra ID (Azure AD) " > "Manage" > [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps)
2. Use the `+ New registration"` button to start the creation
3. Choose:
   - Name of the integration, for example: `Sekoia.io`
   - `Who can use this application or access this API?`: select the group that is allowed to use the application
   - `Redirect URI (optional)` : `Web`: `https://app.sekoia.io/user/callback` (you might need to adapt the domain if you are not working on FRA1)
4. Click on "Register"

## Configure the registration

1. On the main page, save the "Application (client) ID" for later use
2. On the main page, in "Endpoints", copy your "OAuth 2.0 authorization endpoint" such as `https://login.microsoftonline.com/<YOUR TENANT ID>/`. Be sure to remove the `/oauth2/v2.0/authorize` suffix from the URL.
3. Under "Certificates and secrets > Client secrets" use the "+ New client secret" button to create a secret. Save this secret for later use.

## Restrict access for Sekoia.io to specific users

Microsoft Entra ID (Azure AD)  can be configured to prevent some users from accessing Sekoia.io.

1. In "Microsoft Entra ID (Azure AD) " > "Enterprise applications": select your application
2. In the "Application | Overview" > "Getting Started" > "1. Assign users and groups"

You are ready to input your configuration to Sekoia.io