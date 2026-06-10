# Set up the first administrator account

After a successful deployment, no administrator account exists by default. This guide walks you through provisioning the first administrator account and preparing the platform for your users.

## Before you begin

- You completed the post-deployment validation steps in [Deploy the platform](../deployment/deployment_guide.md).
- Your SMTP server is reachable and the `config.yml` email settings are correct.
- You have the primary platform URL configured in `global.host` (e.g., `https://app.sekoia.local`).

!!! warning "SMTP is required"
    The platform provisions accounts exclusively through email invitations. If your SMTP server is not reachable, the invitation email cannot be sent and you cannot complete this setup. Verify SMTP connectivity before continuing.

## Provision the first administrator

1. Open your browser and navigate to your platform URL (e.g., `https://app.sekoia.local`).
2. The platform runs a bootstrap process on first access to initialize the default community. Follow the on-screen instructions.
3. Enter the email address of the first administrator when prompted.
4. Select **Send invitation**.
5. Check the inbox of the email address you entered. Open the invitation email from Sekoia.
6. Select the invitation link in the email.
7. Enter your full name and create a password.
8. Select **Confirm** to activate the account.

The first user is provisioned as a community administrator with full access to platform settings.

> 📸 [SCREENSHOT SUGGESTION: The first-login bootstrap screen showing the email address input field and Send invitation button. | ALT TEXT: Sekoia Self-Hosted first administrator setup screen.]

## Invite additional users

Once the first administrator account is active, you can invite other users from the platform settings.

1. Log in to the platform with your administrator account.
2. Navigate to **Settings > Members**.
3. Select **Invite a member**.
4. Enter the user's email address.
5. Assign a role to the user.
6. Select **Send invitation**.

The invited user receives an email and follows the same account-creation steps as above.

> 📸 [SCREENSHOT SUGGESTION: The Members settings page showing the Invite a member button and the existing members list. | ALT TEXT: Sekoia platform Members settings page.]

## Configure SSO (optional)

Sekoia Self-Hosted supports Single Sign-On via OpenID Connect. SSO is configured per community and must be set up after the first administrator account is active.

1. Log in with your administrator account.
2. Navigate to **Settings > SSO**.
3. Enter your identity provider's client ID, client secret, and authorization endpoint.
4. Select **Save**.

Full OpenID Connect configuration documentation is available at [https://docs.sekoia.io/getting_started/sso/openid_connect/](https://docs.sekoia.io/getting_started/sso/openid_connect/).

## Understand your license limits

Your platform license defines three operational limits:

| Limit | Behavior when reached |
| :--- | :--- |
| Expiration date | Platform generates alerts. Functionality may degrade if the license is not renewed. |
| Maximum supervised assets | Platform generates alerts. Contact your Sekoia sales representative to extend the limit. |
| Maximum daily event-ingest capacity | Platform generates alerts. Contact your Sekoia sales representative to extend the limit. |

To view current license status, navigate to **Settings > License** after logging in.

## Related links

- [Deploy the platform](../deployment/deployment_guide.md): Deployment steps and post-deployment validation.
- [Monitor your platform](../monitoring/monitoring_guide.md): How to set up alerts and dashboards for daily operations.
- [Release notes v0.0.1](../release_notes/0.0.1.md): Feature scope and known limitations.
