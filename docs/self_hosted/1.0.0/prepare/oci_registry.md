# Prepare the OCI registry

The SHC copies the container images and the Helm charts of the release into your OCI registry. The Kubernetes nodes and ArgoCD then download them from this registry.

Three programs use the registry:

| Program | Where it runs | What it does |
| :--- | :--- | :--- |
| SHC | Orchestration node | Pushes, pulls and deletes (checks). |
| containerd (Kubernetes) | Every Kubernetes node | Pulls the images. |
| ArgoCD | Kubernetes nodes | Pulls the Helm charts. |

## Rules

- The registry **MUST** serve **HTTPS**. Plain HTTP is not supported.
- A **self-signed certificate is accepted**. The SHC, containerd and ArgoCD do not verify the certificate of the registry.
- The registry **MUST** be reached from the orchestration node and from every Kubernetes node.
- The orchestration node **MUST** reach the registry **without a proxy**.
- A **project** (also called namespace or organization) **MUST** exist before the installation. Its name **MUST** contain only letters, digits, `-` and `_`. It **MUST NOT** contain `/`.
- The SHC user **MUST** be able to **push, pull and delete** in this project, and to create new repositories in it. The SHC creates `<project>/images/...`, `<project>/charts/...` and `<project>/shc-probe`.
- The registry **SHOULD** have **1 TB** of storage.
- The Kubernetes nodes **SHOULD** reach the registry without a proxy.

### Configuration

| What | Where | Value |
| :--- | :--- | :--- |
| Registry address | `config.yml`, `utils.oci_registry.host` | The host name or IP address, with the port if it is not 443. **No `https://`.** Examples: `10.0.0.60`, `registry.example.com:8443`. |
| Project | `config.yml`, `utils.oci_registry.project` | The project name, for example `sekoia-self-hosted`. |
| User name | `env.rc`, `REGISTRY_USERNAME` | |
| Password | `env.rc`, `REGISTRY_PASSWORD` | |

### If you do not follow a SHOULD rule

| SHOULD rule not followed | What you must change |
| :--- | :--- |
| Less than 1 TB of storage | No configuration change. Each release adds its images to the registry: delete the images of old releases before the registry is full. |
| The Kubernetes nodes reach the registry through a proxy | In `config.yml`, set `modules.k3s_install.pull_images_with_proxy: true`, `modules.k3s_install.k3s_http_proxy` and `modules.k3s_install.k3s_https_proxy`. See [Proxy](../deployment/deployment_configuration.md#proxy). |
| A platform proxy is configured, and the nodes reach the registry **without** it | Add the registry host name to `modules.platform_configuration.config.proxy.no_proxy` and to `modules.k3s_install.k3s_no_proxy`. |

### Not supported

| Situation | Result |
| :--- | :--- |
| Registry over plain HTTP | ArgoCD cannot download the Helm charts. |
| Project path with `/` (for example `group/project`) | Rejected by `CheckLocalConfig`. |
| Orchestration node that reaches the registry only through a proxy | The SHC has no proxy setting for the registry. |

## Install the registry

=== "Harbor"

    **Validation status:** validated in the Sekoia lab (Debian 13, Harbor 2.15.0 offline installer, self-signed certificate on the IP address, HTTPS on port 443).

    In the lab, Harbor runs on a virtual machine with 8 CPUs, 30 GB of RAM and a 500 GB data disk mounted on `/opt/workspace`. Gogs runs on the same machine (see [Prepare the Git repository](./git_repository.md)).

    **Before you start:**

    - Docker and the Docker Compose plugin are installed. Use the procedure of [Install Docker](./orchestration_node.md#step-1-install-docker): it installs `docker-compose-plugin`.
    - The data disk is mounted on `/opt/workspace`. Use the procedure of [Prepare the release disk](./orchestration_node.md#step-3-prepare-the-release-disk).
    - On an air-gapped site, download the Harbor offline installer (about 600 MB) **before** you go to the site.

    1. Set the values of your installation. Replace the values, then paste the lines. The administrator password **MUST** have 8 characters or more, with at least one uppercase letter, one lowercase letter and one digit.

        ```bash
        export REGISTRY_IP="<REGISTRY_IP>"
        export HARBOR_ADMIN_PASSWORD='<A_STRONG_PASSWORD>'
        ```

        The next commands use these variables. Run every command in the **same terminal**.

    2. Download the Harbor offline installer:

        ```bash
        curl -fL -o /tmp/harbor-offline-installer-v2.15.0.tgz https://github.com/goharbor/harbor/releases/download/v2.15.0/harbor-offline-installer-v2.15.0.tgz
        ```

    3. Extract it:

        ```bash
        sudo mkdir -p /opt/harbor
        ```

        ```bash
        sudo tar -xzf /tmp/harbor-offline-installer-v2.15.0.tgz -C /opt/harbor
        ```

    4. Create the certificate directory:

        ```bash
        sudo mkdir -p /data/cert
        ```

    5. Create the private key of the certificate:

        ```bash
        sudo openssl genrsa -out /data/cert/registry.key 4096
        ```

    6. Create a self-signed certificate, valid 10 years, for the IP address of the registry:

        ```bash
        sudo openssl req -x509 -new -nodes -key /data/cert/registry.key -sha256 -days 3650 -subj "/CN=${REGISTRY_IP}" -addext "subjectAltName=IP:${REGISTRY_IP}" -out /data/cert/registry.crt
        ```

        If clients reach the registry by a DNS name instead of an IP address, use the DNS name in `-subj` and write `subjectAltName=DNS:<name>` instead of `subjectAltName=IP:...`. This variant is not validated in the lab.

    7. Create the Harbor configuration file:

        ```bash
        sudo tee /opt/harbor/harbor/harbor.yml > /dev/null <<EOF
        hostname: ${REGISTRY_IP}
        http:
          port: 80
        https:
          port: 443
          certificate: /data/cert/registry.crt
          private_key: /data/cert/registry.key

        harbor_admin_password: ${HARBOR_ADMIN_PASSWORD}
        database:
          password: ${HARBOR_ADMIN_PASSWORD}
        data_volume: /opt/workspace/harbor

        jobservice:
          max_job_workers: 10
          max_job_duration_hours: 24
          job_loggers:
            - STD_OUTPUT
            - FILE
          logger_sweeper_duration: 1

        notification:
          webhook_job_max_retry: 3
          webhook_job_http_client_timeout: 3

        chart:
          absolute_url: disabled

        proxy:
          http_proxy:
          https_proxy:
          no_proxy:
          components:
            - core
            - jobservice
            - trivy

        metric:
          enabled: false
          port: 9090
          path: /metrics

        upload_purging:
          enabled: true
          age: 72h
          interval: 24h
          dryrun: false

        log:
          level: info
          local:
            rotate_count: 50
            rotate_size: 200M
            location: /var/log/harbor

        cache:
          enabled: false
          expire_hours: 24

        _version: 2.15.0
        EOF
        ```

    8. Install and start Harbor. The installation takes a few minutes:

        ```bash
        cd /opt/harbor/harbor && sudo ./install.sh
        ```

        **Expected result:** the last line says that Harbor has been installed and started successfully.

    9. Check that Harbor answers:

        ```bash
        curl -sk https://${REGISTRY_IP}/api/v2.0/ping
        ```

        **Expected result:** `Pong`.

    10. Create the project `sekoia-self-hosted`:

        ```bash
        curl -sk -o /dev/null -w '%{http_code}\n' -u "admin:${HARBOR_ADMIN_PASSWORD}" -H "Content-Type: application/json" -d '{"project_name":"sekoia-self-hosted","public":false,"metadata":{"public":"false"}}' https://${REGISTRY_IP}/api/v2.0/projects
        ```

        **Expected result:** `201` (project created) or `409` (the project already exists).

    11. Write the values for the SHC.

        In `config.yml`:

        ```yaml
        utils:
          oci_registry:
            host: "<REGISTRY_IP>"
            project: "sekoia-self-hosted"
        ```

        In `env.rc` on the orchestration node:

        ```bash
        export REGISTRY_USERNAME="admin"
        export REGISTRY_PASSWORD='<HARBOR_ADMIN_PASSWORD>'
        ```

    12. Before the installation, check access from the orchestration node with the SHC: `./run-shc.sh exec CheckLocalOCIRegistry`.

    !!! note "Harbor after a reboot"
        Harbor starts its containers again after a reboot of the server. If the web interface does not answer after a reboot, run `cd /opt/harbor/harbor && sudo docker compose up -d`.

<!--
To add a technology: copy a tab, set its "Validation status" (lab or customer project, with the
Debian and product versions), and list every command in order with its expected result.
Keep the "Write the values for the SHC" step: it is the link between the product and config.yml.
-->

## Checklist

- [ ] The registry answers over HTTPS from the orchestration node and from every Kubernetes node (for example `curl -sk https://<REGISTRY_IP>/api/v2.0/ping` prints `Pong` with Harbor).
- [ ] The project exists.
- [ ] `utils.oci_registry.host` and `utils.oci_registry.project` are in `config.yml`, and `REGISTRY_USERNAME` and `REGISTRY_PASSWORD` are in `env.rc`.
