# Set up the first administrator account

After a successful deployment, the Self-Hosted Controller displays the platform access credentials directly in the terminal. This guide walks you through retrieving those credentials, logging in, creating your first community, and allocating your subscription.

## Before you begin

- You completed the post-deployment validation steps in [Deploy the platform](../deployment/deployment_guide.md).
- You have the platform URL configured in `global.host` (e.g., `https://app.sekoia.local`).
- You have the license file provided by Sekoia for your subscription.

## Retrieve the initial credentials

At the end of a successful installation, the SHC displays a credentials table in the terminal output.

??? example "Example credentials table"
    ```
                                       Platform Access Credentials

    ┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ Service  ┃ URL                           ┃ User                    ┃ Password / Token                 ┃
    ┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
    │ argocd   │ http://localhost:8080         │ admin                   │                                  │
    ├──────────┼───────────────────────────────┼─────────────────────────┼──────────────────────────────────┤
    │ grafana  │ http://localhost:3000         │ admin                   │                                  │
    ├──────────┼───────────────────────────────┼─────────────────────────┼──────────────────────────────────┤
    │ sekoiaio │ https://app.sekoia.local/user │ instanceadmin@sekoia.io │                                  │
    └──────────┴───────────────────────────────┴─────────────────────────┴──────────────────────────────────┘
    ```

The table provides credentials for three services: the Sekoia platform (`sekoiaio`), the ArgoCD GitOps console (`argocd`), and the Grafana observability dashboard (`grafana`). Save all three sets of credentials in a secure location.

!!! warning "Credentials are auto-generated"
    Passwords and tokens are randomly generated at installation time. They are displayed once at the end of the installation. If you did not save them, use the command in the next step to redisplay them.

To redisplay the credentials at any time, run:

```bash
./run-shc.sh exec PlatformAccess
```

## Log in to the platform

1. Open your browser and navigate to the `sekoiaio` URL from the credentials table (e.g., `https://app.sekoia.local/user`).
2. Enter the `sekoiaio` username (`instanceadmin@sekoia.io`) in the **Email** field.
3. Enter the corresponding password in the **Password** field.
4. Select **Log in**.

You are now logged in to the **Administration Community**. This community is dedicated to managing users and communities across your entire instance. It is not a workspace for security operations.

!!! note "Community overview"
    Your instance contains two built-in communities after installation:

    | Community | Purpose |
    | :--- | :--- |
    | Administration Community | Manages users and communities across the instance. Use this community for administrative tasks only. |
    | sekoia community | Reserved for internal platform operations. Do not use or modify this community. |

    You must create a separate community to run your security operations.

## Create your community

![communities](/assets/self_hosted/communities.png)

1. Select **Communities** in the left navigation panel.
2. Select **+ Create** in the top right corner.
3. Enter a name for your community in the **Name** field.
4. Enter a description in the **Description** field (optional).
5. In the **Administrators** field, add `instanceadmin@sekoia.io` as a community administrator.
6. Select **Create**.

Your new community appears in the list alongside the two built-in communities.

## Allocate your subscription

Your community has no active subscription until you import the license file provided by Sekoia.

![allocate](/assets/self_hosted/allocate.png)


1. Select your community from the list.
2. Select the **Subscriptions** tab.
3. Select **Allocate a subscription**.
4. Select **Import a subscription**.
5. Select the license file provided by Sekoia for your deployment.
6. Select **Import**.

Your subscription appears in the **Subscriptions** tab with its tier name, validity period, asset limit, and storage option.

![subscription](/assets/self_hosted/subscription.png)

## Connect to your community

1. Select the workspace selector in the top left corner of the interface.
2. Select your community from the list.

You are now connected to your community and have access to the full Sekoia platform capabilities within your subscription scope.

## Configure SSO (optional)

Sekoia Self-Hosted supports Single Sign-On via OpenID Connect. You configure SSO per community after the initial setup.

1. Log in to your community.
2. Navigate to **Settings > SSO**.
3. Enter your identity provider's client ID, client secret, and authorization endpoint.
4. Select **Save**.

Full OpenID Connect configuration documentation is available at [https://docs.sekoia.io/getting_started/sso/openid_connect/](https://docs.sekoia.io/getting_started/sso/openid_connect/).

## Related links

- [Deploy the platform](../deployment/deployment_guide.md): Deployment steps and post-deployment validation.
- [Monitor your platform](../monitoring/monitoring_guide.md): How to set up alerts and dashboards for daily operations.
- [Release notes v0.0.1](../release_notes/0.0.1.md): Feature scope and known limitations.
