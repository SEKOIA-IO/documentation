# Configure Single Sign-on with Azure Active Directory

In order to configure Azure with SEKOIA.IO, the following steps must be done:

1. Create a new application on Azure
2. Connect to SEKOIA.IO, add a new domain that belongs to your community and wait for its validation
3. Configure OpenID Connect in SEKOIA.IO (see associated documentation [Single Sign-On With OpenID Connect](../SSO_openid_connect.md))

## Create an Azure Active Directory app registration

1. Visit "Azure Active Directory" > "Manage" > [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps)
2. Use the "+ New registration" button to start the creation
3. Choose a name and input the redirect URI: https://app.sekoia.io/user/callback
4. Click on "Register"

## Configure the registration

1. On the main page, save the "Application (client) ID" for later use
2. On the main page, in "Endpoints", copy your "OAuth 2.0 authorization endpoint" such as `https://login.microsoftonline.com/<YOUR TENANT ID>/`
3. Under "Certificates and secrets > Client secrets" use the "+ New client secret" button to create a secret. Save this secret for later use. 

## Restrict access for SEKOIA.IO to specific users

Azure Active Directory can be configured to prevent some users from accessing SEKOIA.IO.

1. In "Azure Active Directory" > "Enterprise applications": select your application
2. In the "Application | Overview" > "Getting Started" > "1. Assign users and groups"

You are ready to input your configuration to SEKOIA.IO