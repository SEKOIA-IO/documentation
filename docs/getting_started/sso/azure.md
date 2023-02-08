# Use Azure Active Directory as your Identity Provider for Single Sign-On (SSO)

## Summary

To use Azure AD as an authentication provider, you will need to:

* Create an application with the redirect URI: https://app.sekoia.io/user/callback
* Copy the Application ID (Client ID)
* Create a secret (Client secret)
* Copy your tenant ID to create the URL of your authentication provider (https://login.microsoftonline.com/<YOUR TENANT ID>/)
* Input these data to SEKOIA.IO

## Create

1. Visit `Azure Active Directory` > `Manage` > [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps)
2. Use the `+ New registration` button to start the creation
3. Choose a name and input the redirect URI: https://app.sekoia.io/user/callback
4. Click on `Register`

## Configure

1. On the main page, save the `Application (client) ID` for latter use
2. On the main page, in `Endpoints`, copy your `OAuth 2.0 authorization endpoint` such as https://login.microsoftonline.com/<YOUR TENANT ID>/
3. In `Certificates and secrets > Client secrets` use the `+ New client secret` button to create a secret. Save this secret for latter use. 

## Restrict access

Azure Active Directory can be configured to restrict which user are allowed to access SEKOIA.IO.

1. In `Azure Active Directory` > `Enterprise applications`: select your application
2. In the `Application | Overview` > `Getting Started` > `1. Assign users and groups`

You are ready to input your configuration to SEKOIA.IO