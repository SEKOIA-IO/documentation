# Configure SSO with OpenID Connect

To make it easier for employees to access Sekoia.io, you can enable SSO in your Sekoia.io community.

## Prerequisites for OpenID Connect

- Your **Identity Provider** (IdP) must support the OpenID Connect standard
- Only admin user with the `Manage roles` permission can configure the SSO.

## 1. Verify your domains

Sekoia.io requires your domains to be verified in order to be used for authentication.

To do so:

1. Go to `Managed communities` (top right on **your profile** > **Community settings**) > `Security` > `Verify your domains` > `+ Domain`
2. Input your domain and validate using the **Send for verification** button
3. Your domain will have the status **Waiting for verification**
4. Once it has been validated by our team, this status will become **Verified**


## 2. Configure SSO on Sekoia.io

To set up SSO, follow these instructions:

1. Go to `Managed communities` > `Security` > `Configure single Sign-on (SSO)` > `Configure`
2. Fill in identity provider details
3. Save the configuration

Once SSO is set up and your IdP is configured to accept requests, users can log in via the Single Sign-on URL available on this page.
Share it with your users.

## 3. "Just-in-time" (JIT) Account Provisioning

You can choose to enable the automatic creation of users' accounts in your community.

By using this feature, when a user logs-in for the first time, their account will be automatically created. You can set the default role for newly created users, and you can choose the default role among all the roles available in your community.

If you don't enable "just-in-time" account creation, you will have to manually create user accounts. You can learn more about how to create user accounts in the article "[Invite users to join your community](https://docs.sekoia.io/getting_started/invite_users/)".


## Login method

Once you have completed your configuration of OpenID Connect SSO, users will be able to log in via SSO.

Users who created their account via SSO, can only log in via this method.

Only users who create their account via invitation and set up username/password can use both methods to log-in: SSO and username/password.

When the "two-factor authentication" (MFA) is enabled or enforced for your account, you won’t be asked for it when authenticating via your SSO provider.


## Disable Account

To prevent a user from retrieving your organization's data, you can easily deactivate the user from your community and your identity provider.
