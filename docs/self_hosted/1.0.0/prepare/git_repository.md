# Prepare the Git repository

The SHC writes the description of the platform (the ArgoCD stacks) into a Git repository. ArgoCD, inside the cluster, reads this repository and deploys what it describes.

Two programs use the repository:

| Program | Where it runs | What it does |
| :--- | :--- | :--- |
| SHC | Orchestration node | Reads and **writes** (push). |
| ArgoCD | Kubernetes nodes | Reads. |

## Rules

- The repository **MUST** exist before the installation. It **MAY** be empty.
- The repository **MUST** be reached over **HTTP or HTTPS**, from the orchestration node **and** from every Kubernetes node.
- If you use HTTPS, the certificate of the Git server **MUST** be signed by a public certificate authority. A self-signed certificate or a certificate from a private authority is **not supported** for Git: use HTTP inside your network, or contact Sekoia.
- The SHC **MUST** connect with a **user name and a password** (or an access token used as the password).
- This user **MUST** have read and write (push) rights on the repository.
- The SHC writes to the **default branch** of the repository (often `main` or `master`). It **MUST** be able to push to this branch directly: the branch **MUST NOT** require a merge request (pull request) or a review.
- The repository **SHOULD** be used only by the Sekoia platform.
- The orchestration node **SHOULD** reach the Git server without a proxy.

### Configuration

| What | Where | Value |
| :--- | :--- | :--- |
| Repository URL | `config.yml`, `utils.git.repo_url` | The full URL of the repository, ending in `.git`. Format: `http://<HOST>:<PORT>/<OWNER>/<REPOSITORY>.git`. The port is optional when it is 80 (HTTP) or 443 (HTTPS). |
| User name | `env.rc`, `GIT_HTTP_USERNAME` | The Git user. |
| Password | `env.rc`, `GIT_HTTP_PASSWORD` | The password, or an access token. |

The `run-shc.sh` script already passes `GIT_HTTP_USERNAME` and `GIT_HTTP_PASSWORD` to the SHC. No other field is needed.

### If you do not follow a SHOULD rule

| SHOULD rule not followed | What you must change |
| :--- | :--- |
| The orchestration node reaches Git through a proxy | In `config.yml`, set `utils.git.http.proxy: "http://<PROXY_HOST>:<PROXY_PORT>"`. |
| The Kubernetes nodes reach Git through a proxy | In `config.yml`, set the platform proxy: see [Proxy](../deployment/deployment_configuration.md#proxy). |
| The Kubernetes nodes reach Git **without** a proxy, but a proxy is configured for the platform | Add the Git host name to `modules.platform_configuration.config.proxy.no_proxy`. An IP range does not match a host name. |
| The repository is shared with other projects | No change. The SHC writes only in the `argocd/` directory of the repository, and **replaces this whole directory** at each run: never put other files in it. |

### Not supported

| Situation | Result |
| :--- | :--- |
| Git over SSH (`git@host:...`) | ArgoCD cannot read the repository. |
| A branch other than the default branch | ArgoCD reads the default branch only. Create a dedicated repository instead. |
| A protected default branch (merge request or review required) | The SHC push fails. |
| HTTPS with a self-signed or private certificate | The SHC cannot connect. |
| A repository without authentication | The SHC cannot push. |

## Install the Git server

=== "Gogs"

    **Validation status:** validated in the Sekoia lab (Debian 13, Gogs in Docker, image `gogs/gogs:latest`, HTTP on port 3000).

    In the lab, Gogs runs on the same virtual machine as the OCI registry. Gogs uses port 3000 because the registry uses ports 80 and 443. The data is stored on a data disk mounted on `/opt/workspace`.

    **Before you start:** Docker is installed on the server. Use the procedure of [Install Docker](./orchestration_node.md#step-1-install-docker).

    1. Install the tools used by the next steps:

        ```bash
        sudo apt-get install -y curl jq git
        ```

    2. Set the values of your installation. Replace the three values, then paste the lines. The user name **MUST NOT** be `admin`: Gogs reserves this name.

        ```bash
        export GIT_IP="<GIT_IP>"
        export GIT_ADMIN_USER="sekoia"
        export GIT_ADMIN_PASSWORD='<A_STRONG_PASSWORD>'
        ```

        The next commands use these variables. Run every command in the **same terminal**.

    3. Create the data directories:

        ```bash
        sudo mkdir -p /opt/workspace/gogs/gogs/conf
        ```

    4. Create the Gogs configuration file:

        ```bash
        sudo tee /opt/workspace/gogs/gogs/conf/app.ini > /dev/null <<EOF
        [database]
        TYPE = sqlite3
        PATH = /data/gogs/gogs.db

        [server]
        PROTOCOL = http
        HTTP_ADDR = 0.0.0.0
        HTTP_PORT = 3000
        DOMAIN = ${GIT_IP}
        EXTERNAL_URL = http://${GIT_IP}:3000/
        SSH_PORT = 22
        START_SSH_SERVER = false
        DISABLE_SSH = false

        [auth]
        DISABLE_REGISTRATION = true

        [security]
        INSTALL_LOCK = true

        [log]
        MODE = console
        LEVEL = Info
        EOF
        ```

    5. Download the Gogs image:

        ```bash
        sudo docker pull gogs/gogs:latest
        ```

    6. Start Gogs. The container restarts automatically after a reboot:

        ```bash
        sudo docker run -d --name gogs --restart unless-stopped -p 3000:3000 -p 222:22 -v /opt/workspace/gogs:/data gogs/gogs:latest
        ```

    7. Wait 30 seconds, then check that Gogs answers:

        ```bash
        curl -s -o /dev/null -w '%{http_code}\n' http://${GIT_IP}:3000/
        ```

        **Expected result:** `200`.

    8. Create the Gogs administrator. The SHC uses this account:

        ```bash
        sudo docker exec -u git:git gogs /app/gogs/gogs admin create-user --name "$GIT_ADMIN_USER" --password "$GIT_ADMIN_PASSWORD" --email sekoia@example.com --admin
        ```

        **Expected result:** a message that says that the user has been successfully created.

    9. Create an access token for the API:

        ```bash
        export GIT_TOKEN=$(curl -s -u "$GIT_ADMIN_USER:$GIT_ADMIN_PASSWORD" -H "Content-Type: application/json" -d '{"name":"selfhosted"}' http://${GIT_IP}:3000/api/v1/users/${GIT_ADMIN_USER}/tokens | jq -r .sha1)
        ```

        Check that the token is not empty:

        ```bash
        echo "$GIT_TOKEN"
        ```

        **Expected result:** a string of 40 letters and digits. If you see `null` or nothing, check the user name and the password.

    10. Create the repository `selfhosted`:

        ```bash
        curl -s -H "Authorization: token $GIT_TOKEN" -H "Content-Type: application/json" -d '{"name":"selfhosted","description":"","private":false,"auto_init":true,"readme":"Default"}' http://${GIT_IP}:3000/api/v1/user/repos | jq -r .clone_url
        ```

        **Expected result:** `http://<GIT_IP>:3000/<GIT_ADMIN_USER>/selfhosted.git`.

    11. Check read access and the default branch:

        ```bash
        git ls-remote --symref "http://${GIT_ADMIN_USER}:${GIT_ADMIN_PASSWORD}@${GIT_IP}:3000/${GIT_ADMIN_USER}/selfhosted.git" HEAD
        ```

        **Expected result:** a first line that starts with `ref: refs/heads/` followed by the name of the default branch, and ends with `HEAD`. The SHC detects this branch automatically.

    12. Write the values for the SHC.

        In `config.yml`:

        ```yaml
        utils:
          git:
            repo_url: "http://<GIT_IP>:3000/<GIT_ADMIN_USER>/selfhosted.git"
        ```

        In `env.rc` on the orchestration node:

        ```bash
        export GIT_HTTP_USERNAME="<GIT_ADMIN_USER>"
        export GIT_HTTP_PASSWORD='<GIT_ADMIN_PASSWORD>'
        ```

    13. Before the installation, check access from the orchestration node with the SHC: `./run-shc.sh exec CheckLocalGit`.

    !!! note "Private repository"
        The lab repository is created with `"private": false`, inside an isolated network. The SHC and ArgoCD always send the user name and the password, so a private repository is expected to work, but it is not validated yet.

<!--
To add a technology: copy a tab, set its "Validation status" (lab or customer project, with the
Debian and product versions), and list every command in order with its expected result.
Keep the "Write the values for the SHC" step: it is the link between the product and config.yml.
-->

## Checklist

- [ ] The repository exists, and `git ls-remote` works from the orchestration node.
- [ ] Every Kubernetes node reaches the Git server on its port (for example `curl -s -o /dev/null -w '%{http_code}\n' http://<GIT_IP>:3000/` prints `200`).
- [ ] The default branch accepts a direct push from the SHC user.
- [ ] `utils.git.repo_url` is in `config.yml`, and `GIT_HTTP_USERNAME` and `GIT_HTTP_PASSWORD` are in `env.rc`.
