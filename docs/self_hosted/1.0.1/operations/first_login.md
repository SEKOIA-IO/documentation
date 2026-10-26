# Set up the first administrator account

During the installation, the self-hosted-controller (SHC) displays the platform access credentials in the terminal. This guide walks you through retrieving those credentials, logging in, creating your first community, and allocating your subscription.

## Before you begin

- You completed the post-deployment validation steps in [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md).
- You have the platform URL configured in `global.host` (for example, `https://app.sekoia.local`).
- You have the license file provided by Sekoia for your subscription.

## Retrieve the initial credentials

The platform installer generates the administrator passwords and the API key of the instance administrator at installation time, and stores them in Vault. During `Install`, once the platform installer completes, the `PlatformAccess` step reads them from Vault and displays them in the terminal. Because `PlatformAccess` reads them from Vault each time it runs, you can display them again with the same command.

!!! warning "The output contains credentials in clear"
    The output holds the administrator passwords of the Sekoia platform, ArgoCD, and Grafana, and the API key of the instance administrator. Run the command only when you need them, on a terminal that nobody else can see, and never paste its output in a ticket, a chat, or a screenshot. In the TUI, the output is also written to the run log file. See [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md#navigate-the-interface).

To display the credentials, run:

```bash
exec PlatformAccess
```

??? example "Example output (sensitive)"
    ```text
    Instance access

    argocd
      url:      https://admin.sekoia.local/argo
      user:     admin
      password: <PASSWORD>

    grafana
      url:      https://admin.sekoia.local/grafana
      user:     admin
      password: <PASSWORD>

    sekoiaio
      url:      https://app.sekoia.local/user
      user:     instanceadmin@sekoia.io
      password: <PASSWORD>
      apikey:   <API_KEY>
    ```

The output provides access to three services: the ArgoCD GitOps console (`argocd`) and the Grafana observability dashboard (`grafana`), both served under `global.delivery_host`, and the Sekoia platform (`sekoiaio`), served under `global.host`. The `sekoiaio` entry also holds the API key of the instance administrator. Save these credentials in a secure location, such as a password manager.

## Log in to the platform

1. Open your browser and navigate to the `sekoiaio` URL from the `PlatformAccess` output (for example, `https://app.sekoia.local/user`).
2. In the **Email** field, enter the `sekoiaio` user (`instanceadmin@sekoia.io`).
3. In the **Password** field, enter the corresponding password.
4. Select **Log in**.

You are now logged in to the **Administration Community**. This community is dedicated to managing users and communities across your entire instance. It is not a workspace for security operations.

!!! note "Community overview"
    Your instance contains two built-in communities after installation, each with a built-in account:

    | Community                | Built-in account          | Purpose                                                                                          |
    | :---                     | :---                      | :---                                                                                             |
    | Administration Community | `instanceadmin@sekoia.io` | Manages users and communities across the instance. Use this community for administrative tasks only. |
    | sekoia community         | `admin@sekoia.io`         | Reserved for internal platform operations: it holds the permissions of the platform applications. Do not use or modify this community or its account. `PlatformAccess` does not display the credentials of this account. |

    You must create a separate community to run your security operations.

## Create your community

![The Communities page of the Administration Community, listing the two built-in communities, with the Create button in the top right corner.](/assets/self_hosted/1.0.1/first_login/communities.png)

1. In the left navigation panel, select **Communities**.
2. In the top right corner, select **+ Create**.
3. In the **Name** field, enter a name for your community.
4. In the **Description** field, enter a description (optional).
5. In the **Administrators** field, add `instanceadmin@sekoia.io` as a community administrator.
6. Select **Create**.

Your new community appears in the list alongside the two built-in communities.

## Allocate your subscription

Your community has no active subscription until you import the license file provided by Sekoia.

![The Subscriptions tab of a new community with no active subscription, and the Allocate a subscription button.](/assets/self_hosted/1.0.1/first_login/allocate.png)

1. In the communities list, select your community.
2. Select the **Subscriptions** tab.
3. Select **Allocate a subscription**.
4. Select **Import a subscription**.
5. Select the license file provided by Sekoia for your deployment.
6. Select **Import**.

Your subscription appears in the **Subscriptions** tab with its tier name, validity period, asset limit, and storage option.

![The Subscriptions tab of a community showing the imported subscription with its tier, validity period, region, asset limit, and storage options.](/assets/self_hosted/1.0.1/first_login/subscription.png)

## Connect to your community

1. In the top left corner of the interface, select the workspace selector.
2. In the list, select your community.

You are now connected to your community and have access to the full Sekoia platform capabilities within your subscription scope.

## Configure SSO (optional)

Sekoia Self-Hosted supports Single Sign-On via OpenID Connect. SSO is configured per community and requires two steps: registering the SSO domain via API, then configuring your identity provider in the community settings.

### Step 1: Retrieve your community UUID

1. Connect to your target community.
2. Navigate to **Settings > General**.
3. Look at the URL in your browser. The community UUID is the segment between `/communities/` and `/community-details`.

    ```text
    https://app.sekoia.local/communities/<community-uuid>/community-details
    ```

    Copy and save this UUID.

### Step 2: Retrieve the platform API key

On the orchestration node, run:

```bash
exec PlatformAccess
```

The command displays the platform access credentials. Copy the `apikey` value of the `sekoiaio` entry: it is the API key of the instance administrator. Handle it as a password.

### Step 3: Register the SSO domain

Run the following API call from the orchestration node, replacing the placeholders with your values:

```bash
curl 'https://<PLATFORM-DOMAIN>/api/v1/communities/<COMMUNITY-UUID>/domains' \
  -X 'PUT' \
  -H 'Authorization: Bearer <API-KEY>' \
  -H 'Content-Type: application/json' \
  --data-raw '{"domain":"<SSO-DOMAIN>","validated":false}' \
  --cacert '<CA-BUNDLE>'
```

| Placeholder          | Value                                                                           |
| :---                 | :---                                                                            |
| `<PLATFORM-DOMAIN>`  | The FQDN configured in `global.host` (for example, `app.sekoia.local`)          |
| `<COMMUNITY-UUID>`   | The UUID retrieved in step 1                                                    |
| `<API-KEY>`          | The API key retrieved in step 2                                                 |
| `<SSO-DOMAIN>`       | The domain name to register for SSO (for example, `example.com`)                |
| `<CA-BUNDLE>`        | The path of the PEM bundle of the private certificate authority that signs the platform certificate. If a certificate authority that the orchestration node already trusts signs it, remove the `--cacert` option. |

!!! warning "Self-signed test certificate"
    `curl` cannot verify a self-signed certificate. Only on a test instance that uses a self-signed certificate, replace `--cacert '<CA-BUNDLE>'` with `--insecure`. This option disables the verification of the server identity, while the request sends the API key of the instance administrator: never use it on a production instance.

### Step 4: Verify the domain registration

1. In your community, navigate to **Settings > Security**.
2. Confirm that your domain appears in the list with its validation status.

### Step 5: Configure your identity provider

1. In your community, navigate to **Settings > SSO**.
2. Enter your identity provider's client ID, client secret, and authorization endpoint.
3. Select **Save**.

For the full OpenID Connect configuration, see [Configure SSO with OpenID Connect](/getting_started/sso/openid_connect.md).

## Related links

- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Deployment steps and post-deployment validation.
- [Monitor your platform](/self_hosted/1.0.1/monitoring/monitoring_guide.md): How to set up alerts and dashboards for daily operations.
- [Release notes v1.0.1](/self_hosted/1.0.1/release_notes.md): Feature scope and known limitations.
