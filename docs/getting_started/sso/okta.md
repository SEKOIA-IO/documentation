# Use Okta as your Identity Provider for Single Sign-On (SSO)

## Create

1. Follow the menu to `admin console` > `Applications` > `Applications`
2. Use the `Create App Integration` function to start the integration:
    - As `Sign-in method` choose `OIDC - OpenID Connect`
    - As `Application type` choose `Web Application`
3. Once redirected to the `New Web App Integration`, be sure to select:
    - `Grant type`: `Client credentials`
    - `Sign-in redirect URIs`: https://app.sekoia.io/user/callback
4. In `Assignments` > `Controlled access`, you can limit access to specific groups of users

## Configure

Once your app has been created:

1. Save the `Client ID` & `Client secret` for further use
2. Create your `Authentication provider base URL` https://${yourOktaDomain}/ (More info
   on [okta.com: Composing your base URL](https://developer.okta.com/docs/reference/api/oidc/#composing-your-base-url)).

You are ready to input your configuration to SEKOIA.IO.

## Restrict access

Okta can be configured to restrict which users are allowed to access SEKOIA.IO.

1. `Applications` > `Applications`: select your application
2. In `Assignments` > `Assign` you can select `Assign to People` or `Assign to Groups`

## Readings

- [okta.com: Build a Single Sign-On (SSO) integration](https://developer.okta.com/docs/guides/build-sso-integration/openidconnect/main/)