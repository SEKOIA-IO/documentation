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
    │ argocd   │ http://localhost:8080         │ admin                   │ <password>                       │
    ├──────────┼───────────────────────────────┼─────────────────────────┼──────────────────────────────────┤
    │ grafana  │ http://localhost:3000         │ admin                   │ <password>                       │
    ├──────────┼───────────────────────────────┼─────────────────────────┼──────────────────────────────────┤
    │ sekoiaio │ https://app.sekoia.local/user │ instanceadmin@sekoia.io │ <password>                       │
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

    | Community                | Purpose                                                                                          |
    | :---                     | :---                                                                                             |
    | Administration Community | Manages users and communities across the instance. Use this community for administrative tasks only. |
    | sekoia community         | Reserved for internal platform operations. Do not use or modify this community.                  |

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

Sekoia Self-Hosted supports Single Sign-On via OpenID Connect. SSO is configured per community and requires two steps: registering the SSO domain via API, then configuring your identity provider in the community settings.

### Step 1: Retrieve your community UUID

1. Connect to your target community.
2. Navigate to **Settings > General**.
3. Look at the URL in your browser. The community UUID is the segment between `/communities/` and `/community-details`.

    ```
    https://app.sekoia.local/communities/<community-uuid>/community-details
    ```

    Copy and save this UUID.

### Step 2: Retrieve the platform API key

On the orchestration node, run:

```bash
./run-shc.sh exec PlatformAccess
```

The command displays the platform credentials table. Copy the API key shown in the `sekoiaio` row.

### Step 3: Register the SSO domain

Run the following API call from the orchestration node, replacing the placeholders with your values:

```bash
curl 'https://<PLATFORM-DOMAIN>/api/v1/communities/<COMMUNITY-UUID>/domains' \
  -X 'PUT' \
  -H 'Authorization: Bearer <API-KEY>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"domain":"<SSO-DOMAIN>","validated":false}' \
  --insecure
```

| Placeholder          | Value                                                                           |
| :---                 | :---                                                                            |
| `<PLATFORM-DOMAIN>`  | The FQDN configured in `global.host` (e.g., `app.sekoia.local`)                |
| `<COMMUNITY-UUID>`   | The UUID retrieved in step 1                                                    |
| `<API-KEY>`          | The API key retrieved in step 2                                                 |
| `<SSO-DOMAIN>`       | The domain name to register for SSO (e.g., `example.com`)                      |

!!! note "`--insecure` flag"
    The `--insecure` flag disables TLS certificate verification. It is needed when the platform uses a self-signed certificate, which is common in air-gapped deployments. If your platform is configured with a certificate signed by a trusted CA, you can omit this flag.

### Step 4: Verify the domain registration

1. Navigate to **Settings > Security** in your community.
2. Confirm that your domain appears in the list with its validation status.

### Step 5: Configure your identity provider

1. Navigate to **Settings > SSO** in your community.
2. Enter your identity provider's client ID, client secret, and authorization endpoint.
3. Select **Save**.

Full OpenID Connect configuration documentation is available at [https://docs.sekoia.io/getting_started/sso/openid_connect/](https://docs.sekoia.io/getting_started/sso/openid_connect/).

## Related links

- [Deploy the platform](../deployment/deployment_guide.md): Deployment steps and post-deployment validation.
- [Monitor your platform](../monitoring/monitoring_guide.md): How to set up alerts and dashboards for daily operations.
- [Release notes v0.0.1](../release_notes/0.0.1.md): Feature scope and known limitations.
