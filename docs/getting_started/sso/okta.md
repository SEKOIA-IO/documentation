# Configure Single Sign-on with Okta

In order to configure Okta with SEKOIA.IO, the following steps must be done:

1. Create a new application on Okta.
2. Connect to SEKOIA.IO and add a new domain that belongs to your community and wait for its validation.
3. Configure OpenID Connect in SEKOIA.IO (see associated documentation [Single Sign-On With OpenID Connect](../SSO_openid_connect.md))


## Create

1. Follow the menu to "admin console" > "Applications" > "Applications"
2. Use the "Create App Integration" function to start the integration:
    - As "Sign-in method" choose "OIDC - OpenID Connect".
    - As "Application type" choose "Web Application".
3. Once redirected to the "New Web App Integration", be sure to select:
    - Grant type: "Client acting on behalf of a user" > "Authorization Code"
    - Sign-in redirect URIs: `https://app.sekoia.io/user/callback`
4. In "Assignments" > "Controlled access", you can limit access to specific groups of users (during tests you can use the option "Allow everyone in your organization to access").

## Configure

Once your app has been created:

1. Save the "Client ID" & "Client secret" for later use.
2. Save your Okta domain (go to the user menu in the top right corner of the Okta interface, you will find it under your email address), you will need it to provide it in SEKOIA.IO "Authentication provider base URL" field: `https://${yourOktaDomain}/` (More info
on Okta documentation: [Composing your base URL](https://developer.okta.com/docs/reference/api/oidc/#composing-your-base-url)). Be aware that, your Okta domain is not the domain of the "Okta Admin Console".

You are ready to input your configuration to SEKOIA.IO.

## Display application icon to users

When your users login to Okta, the SEKOIA.IO app can be displayed. This feature allows users to quickly connect to their apps.

1. Navigate to "Okta admin dashboard" > "Applications" > "Applications": choose your application
2. In "General Settings" > "Edit" > "Login"
4. "Application visibility" choose: "Display application icon to users"
5. "Login flow" choose: "Redirect to app to initiate login (OIDC Compliant)"
6. "Initiate login URI" input your SEKOIA.IO SSO login URL (This URL is displayed in the SEKOIA.IO SSO configuration page at "Managed communities" > "Security" > "Configure single Sign-on (SSO)" > "Configure")
7. Save
8. Visit the end user dashboard to validate that your changes are working as expected

## Restrict access

Okta can be configured to restrict which users are allowed to access SEKOIA.IO.

To restrict access to a user or a group of users, follow these steps: 

1. In "Applications" > "Applications": select your application
2. In "Assignments" > "Settings icon" >  "Assign": you can select "Assign to People" or "Assign to Groups"

## Readings

- Okta documentation: [Build a Single Sign-On (SSO) integration](https://developer.okta.com/docs/guides/build-sso-integration/openidconnect/main/)