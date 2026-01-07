# Configure Single Sign-on with Okta

In order to configure Okta with Sekoia.io, the following steps must be done:

1. Create a new application in your Okta admin console
2. Connect to Sekoia.io and add a new domain that belongs to your community and wait for its validation.
3. Configure OpenID Connect in Sekoia.io. (see associated documentation [Single Sign-On With OpenID Connect](/getting_started/sso/openid_connect.md))

{!_shared_content/sso_multiple_business.md!}

## Create a new application in Okta

1. Navigate to "admin console" > "Applications" > "Applications"
2. Use the "Create App Integration" function to start the integration:
    - As "Sign-in method" choose "OIDC - OpenID Connect"
    - As "Application type" choose "Web Application"
3. Once redirected to the "New Web App Integration", be sure to select:
    - Grant type: "Client acting on behalf of a user" > "Authorization Code"
    - Sign-in redirect URIs: `https://app.sekoia.io/user/callback`
4. Under "Assignments" > "Controlled access", you can limit access to specific groups of users. During tests, you can use the option "Allow everyone in your organization to access"

## Configure your Okta application for Sekoia.io

Once your app has been created:

1. Save the "Client ID" & "Client secret" for later use.
2. Save your Okta domain. You can find this by navigating to the user menu in the top right corner of the Okta interface, and it will be listed under your email address. You will need it to provide it in Sekoia.io "Authentication provider base URL" field: `https://${yourOktaDomain}/`

 !!! note
     You can find more info on Okta documentation: [Composing your base URL](https://developer.okta.com/docs/reference/api/oidc/#composing-your-base-url). Be aware that, your Okta domain is not the domain of the "Okta Admin Console".

You are ready to input your configuration to Sekoia.io.

## Display Sekoia.io application icon to your Okta users

When your users login to Okta, the Sekoia.io app can be displayed. This feature allows users to quickly connect to their apps.

1. Navigate to "Okta admin dashboard" > "Applications" > "Applications": choose your application
2. Under "General Settings" > "Edit" > "Login", select "Either Okta or App" as the login initiation method
3. Under "Application visibility", choose: "Display application icon to users"
4. Under "Login flow", choose: "Redirect to app to initiate login (OIDC Compliant)"
5. In the "Initiate login URI", input your Sekoia.io SSO login URL (This URL is displayed in the Sekoia.io SSO configuration page at "Managed communities" > "Security" > "Configure single Sign-on (SSO)" > "Configure")
6. Save your changes
7. Visit the end user dashboard to validate that your changes are working as expected

## Restrict access

Okta can be configured to restrict which users are allowed to access Sekoia.io.

To restrict access to a user or a group of users, follow these steps:

1. In "Applications" > "Applications": select your application
2. In "Assignments" > "Settings icon" >  "Assign": you can select "Assign to People" or "Assign to Groups"

## Readings

- Okta documentation: [Build a Single Sign-On (SSO) integration](https://developer.okta.com/docs/guides/build-sso-integration/openidconnect/main/)