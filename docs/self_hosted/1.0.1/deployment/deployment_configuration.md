# Configure the deployment

The `config.yml` file describes the environment that the self-hosted-controller (SHC) deploys. For Sekoia Self-Hosted 1.0.1, start from a built-in sizing profile and provide the site-specific values described on this page.

The SHC combines the built-in defaults, the selected sizing profile, and your `config.yml` into one computed configuration. It validates the result before installation and rejects missing required fields, invalid values, and unsupported keys.

This page explains every required field, the settings whose default value is a placeholder, and the most common optional settings. To inspect every other supported setting, use the [SHC configuration commands](#inspect-the-configuration-with-the-shc).

!!! warning "Validation does not catch every incorrect value"
    `CheckLocalConfig` rejects a required field that is missing or empty, but it does not check the optional fields that your environment needs. For example, the S3 credentials of the online mode are optional for the validator: when they are empty, the installation fails later, when `DownloadReleaseFiles` runs in the `checks` stage. In the same way, when backups are enabled, a missing encryption key stops the installation only in the `platform` stage. To confirm that every value your deployment needs is present and correct, inspect the computed configuration with `config show`, with the precautions described in [Inspect the configuration with the SHC](#inspect-the-configuration-with-the-shc).

## Create the configuration file

Use the following configuration as a starting point. Replace every example value before running the SHC.

```yaml
global:
  inherit_config: sizing/1tb-day.yaml
  host: "app.example.com"
  delivery_host: "admin.example.com"
  kube_manager_host: "kubernetes.example.com"
  forward_dns: "10.0.0.100"
  platform_storage:
    region: "${env.STORAGE_S3_REGION}"
    endpoint: "${env.STORAGE_S3_ENDPOINT}"
    access_key: "${env.STORAGE_S3_ACCESS_KEY}"
    secret_key: "${env.STORAGE_S3_SECRET_KEY}"
  version:
    platform:
      version: "v1.0.1"
  logging:
    file: /opt/sekoia/logs/self-hosted-controller.log

utils:
  ansible:
    ssh-key: "${env.SERVERS_SSH_KEY}"
    user: debian
    inventory:
      managers:
        - 10.0.0.1
        - 10.0.0.2
        - 10.0.0.3
      workers:
        - 10.0.0.10
        - 10.0.0.11
        - 10.0.0.12
  git:
    repo_url: "https://git.example.com/sekoia/self-hosted.git"
  oci_registry:
    host: "registry.example.com"
    project: "sekoia-self-hosted"
    username: "${env.REGISTRY_USERNAME}"
    password: "${env.REGISTRY_PASSWORD}"

modules:
  platform_configuration:
    config:
      global:
        instance_public_key: "${env.SEKOIA_INSTANCE_PUBLIC_KEY}"
```

References such as `${env.STORAGE_S3_REGION}` read values from environment variables when the SHC loads the file. Use this syntax for credentials instead of storing secrets directly in `config.yml`. The former `env.VARIABLE_NAME` syntax is not supported.

!!! warning "Protect the configuration and the credentials"
    `config.yml` and these environment variables give access to your nodes, registry, Git repository, and storage. Restrict `config.yml`, the SSH private key, and any file that stores the variables to the accounts that need them, for example with `chmod 600`. The SHC container runs as UID 1000 and must still be able to read `config.yml`: when another account owns the file, give UID 1000 read access to it. Do not type a secret value on the command line, for example in `export VARIABLE=value`, because the shell history keeps it. Load the values from a protected file instead, for example with `set -a; . /path/to/shc.env; set +a`.

Set these environment variables before running the SHC:

| Variable | Purpose |
| :--- | :--- |
| `STORAGE_S3_REGION` | Region of the S3-compatible storage used by the platform. |
| `STORAGE_S3_ENDPOINT` | Endpoint of the S3-compatible storage used by the platform. |
| `STORAGE_S3_ACCESS_KEY` | Access key for platform storage. |
| `STORAGE_S3_SECRET_KEY` | Secret key for platform storage. |
| `SERVERS_SSH_KEY` | SSH private key used to configure the Kubernetes nodes. |
| `REGISTRY_USERNAME` | Username for the OCI registry. |
| `REGISTRY_PASSWORD` | Password for the OCI registry. |
| `GIT_HTTP_USERNAME` | Username for the Git repository, read by `utils.git.http.username`. |
| `GIT_HTTP_PASSWORD` | Password or access token for the Git repository, read by `utils.git.http.password`. |
| `SEKOIA_INSTANCE_PUBLIC_KEY` | Base64-encoded instance public key provided by Sekoia. |
| `TRAEFIK_PUBKEY` | Platform certificate in PEM format. See [TLS certificate](#tls-certificate). |
| `TRAEFIK_PRIVKEY` | Private key of the platform certificate in PEM format. |
| `SERVERS_SUDO_PASSWORD` | Optional. Password that `sudo` asks for on the nodes, if any. See [Node access](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#node-access). |
| `S3_ACCESS_KEY` | Online mode only. Access key for the Sekoia release bucket, provided by Sekoia. |
| `S3_SECRET_KEY` | Online mode only. Secret key for the Sekoia release bucket, provided by Sekoia. |
| `BACKUP_VAULT_CRYPT_KEY` | Required when Vault backups are enabled. Encryption key of the Vault snapshots, at least 16 characters. See [Backups](#backups). |
| `BACKUP_ARANGO_CRYPT_KEY` | Required when ArangoDB backups are enabled. Passphrase of the ArangoDB backups, at least 16 characters. |
| `BACKUP_CLICKHOUSE_CRYPT_KEY` | Required when ClickHouse backups are enabled. AES-256 key of the ClickHouse backups: exactly 64 hexadecimal characters, for example the output of `openssl rand -hex 32`. |

The [deployment guide](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script) shows how to pass these variables to the SHC container. Pass every variable you set, including the `BACKUP_*` variables when you enable backups.

## Select and adjust a sizing profile

`global.inherit_config` selects a sizing profile shipped with the SHC image. The profile supplies service replicas, resource allocations, storage sizes, and other capacity-related defaults, while your site configuration overrides the values specific to your environment.

The SHC image ships two sizing profiles. Each one adjusts only the resources whose load grows with the ingestion volume: Kafka, ExaLog, the KeyDB workflow cache, the intake and ingestion workers, and Sigma Workflow. Every other value comes from the built-in defaults.

| Profile | `global.inherit_config` value | Target |
| :--- | :--- | :--- |
| Minimal | `sizing/minimal.yaml` | Smallest footprint shipped with the SHC. |
| 1 TB/day | `sizing/1tb-day.yaml` | Mid-range deployment ingesting around 1 TB of events per day. |

The values of both profiles are initial estimates, pending performance validation. A profile sets the resources and the replicas of the services, not the number of nodes: size the servers and the object storage with [Cluster sizing](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#cluster-sizing). The rows of that table do not map one-to-one to the profiles.

The `sizing/` path resolves against the configuration directory shipped in the SHC image, wherever you mount your own `config.yml`. A profile is a starting point, not a universal production recommendation: choose the profile and adjust it with Sekoia to match your event sizes, events per second, daily ingestion volume, retention requirements, and volume of search queries.

Use `config show` to review the result after inheritance, and `config help` to identify supported sizing overrides. Do not copy undocumented keys into your configuration: the SHC rejects unsupported fields.

## Required fields

### Platform endpoints

| Field | Description |
| :--- | :--- |
| `global.host` | Primary FQDN used to access the Sekoia platform, for example `app.example.com`. Configure DNS and the load balancer so this hostname reaches the platform. |
| `global.delivery_host` | Public FQDN used by delivery services, including the administrator portal, for example `admin.example.com`. |
| `global.kube_manager_host` | IP address or hostname of the Kubernetes API endpoint, without a port. The SHC, the nodes that join the cluster, and the Cilium network layer all reach the API through this address. For a highly available deployment, use the address of a TCP load balancer that forwards port 6443 to the three manager nodes. Otherwise, use the IP address of the first manager node. A hostname must resolve on every node and on the orchestration node. |
| `global.forward_dns` | DNS server to which CoreDNS forwards every name outside the Kubernetes cluster. To use several servers, separate their addresses with a space, for example `"10.0.0.10 10.0.0.11"`. |

The platform services resolve names outside the cluster only through `global.forward_dns`: they do not read the `/etc/hosts` file of the nodes. The Git repository, the OCI registry, the S3 storage, and the SMTP server must resolve through this DNS server, or be configured with their IP address.

### Platform storage

The platform stores the ExaLog indexes in S3-compatible object storage. These credentials must allow the platform to use the ExaLog event buckets. The platform does not create these buckets; see [Event storage buckets](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#event-storage-buckets).

| Field | Description |
| :--- | :--- |
| `global.platform_storage.region` | Region configured by your S3-compatible storage provider. |
| `global.platform_storage.endpoint` | Endpoint used to access the S3-compatible storage. Include the URL scheme, for example `https://s3.example.com`. |
| `global.platform_storage.access_key` | Access key for the S3-compatible storage. Use an environment-variable reference. |
| `global.platform_storage.secret_key` | Secret key for the S3-compatible storage. Use an environment-variable reference. |

ExaLog storage configuration is derived from `global.platform_storage`. Some computed configuration keys retain `quickwit` in their names, but they configure the ExaLog capability.

The following optional fields adjust how the platform reaches the storage:

| Field | Description | Default |
| :--- | :--- | :--- |
| `global.platform_storage.force_path_style_access` | `true` to send path-style requests, so bucket names do not need DNS records. Set it to `false` only when your storage requires virtual-hosted-style requests. | `true` |
| `modules.platform_configuration.config.quickwit.searcher.s3_max_get_object_connections` | Maximum number of concurrent S3 GET connections of each ExaLog searcher. Lower it to limit the load that searches put on the storage. The limit applies to each searcher, so the total grows with the number of searchers, set in `quickwit.searcher.replicaCount`. | `1024` |

### Release

| Field | Description |
| :--- | :--- |
| `global.version.platform.version` | Sekoia Self-Hosted release to deploy. Set it to `v1.0.1` for this GA documentation. |

### Kubernetes node access

| Field | Description |
| :--- | :--- |
| `utils.ansible.ssh-key` | Private key used by the self-hosted-controller (SHC) to connect to and configure every Kubernetes node. Use an environment-variable reference. |
| `utils.ansible.user` | SSH user used on every Kubernetes node. The account must meet the requirements in [Node access](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#node-access). |
| `utils.ansible.inventory.managers` | List of the IPv4 addresses of the manager nodes. Hostnames and IPv6 addresses are rejected. Set exactly three managers: this is the supported production topology. |

The validator only rejects an empty list of managers: it accepts any other number. Do not deploy another number in production. With one or two managers, etcd has no fault tolerance, and the loss of a single manager stops the Kubernetes API. The manager nodes also run platform workloads, like the worker nodes. See [Cluster sizing](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#cluster-sizing).

Worker nodes are configured under `utils.ansible.inventory.workers`, with their IPv4 addresses. The field is not required by the configuration validator, but production sizing profiles require workers to provide the expected capacity: when you omit it, the SHC installs a cluster of manager nodes only, without any error.

### Git repository

| Field | Description |
| :--- | :--- |
| `utils.git.repo_url` | URL of the customer-managed Git repository in which the self-hosted-controller (SHC) publishes the ArgoCD stack manifests. |

The SHC publishes the stacks to a branch of this repository, and ArgoCD tracks the same branch for the root and child applications. To choose the branch, set the following optional field:

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.push_argo_stacks.base_branch` | Branch to publish the stacks to and to track in ArgoCD. Required when the repository is empty. Otherwise, the branch must already exist. | Default branch of the repository |

!!! warning "Empty repository"
    If the repository has no commit yet, set `modules.push_argo_stacks.base_branch`. Without it, `PushArgoStacks` fails. `PushArgoStacks` also fails, without overwriting anything, when its local checkout has uncommitted changes or when the local and remote branches have diverged.

If the repository requires authentication, use `config help utils.git` to inspect the supported HTTP authentication settings. ArgoCD connects to the repository with a username and a password over HTTP or HTTPS.

The repository must meet the following conditions:

- It is reached over HTTP or HTTPS, from the orchestration node and from every Kubernetes node. Git over SSH is not supported: ArgoCD receives only the username and the password.
- With HTTPS, its certificate is signed by a public certificate authority. The SHC has no setting to trust a private certificate authority for Git.
- The SHC account can push directly to the branch. A protected branch that requires a merge request or a review makes `PushArgoStacks` fail.
- The SHC owns the `argocd/` directory of the repository and replaces it at each push. Do not store other files in this directory.

### OCI registry

| Field | Description |
| :--- | :--- |
| `utils.oci_registry.host` | Registry hostname, with an optional port and without a URL scheme, for example `registry.example.com` or `registry.example.com:5000`. |
| `utils.oci_registry.project` | Registry project or namespace in which the self-hosted-controller (SHC) publishes Sekoia artifacts, for example `sekoia-self-hosted`. The project must exist before the installation. Use lowercase letters, digits, `-`, and `_`, starting with a letter or a digit: `CheckLocalConfig` rejects `/` and `.`. |
| `utils.oci_registry.username` | Username with push, pull, and delete permissions in the registry project, including the creation of new repositories in it. Use an environment-variable reference. |
| `utils.oci_registry.password` | Password or token for the registry account. Use an environment-variable reference. |

The registry must serve HTTPS: ArgoCD pulls the Helm charts over HTTPS, even when `utils.oci_registry.scheme` is `http`. The SHC derives the registry URL and the repositories used for checks, charts, and images from these values. Do not set the derived `url`, `check_repo`, `chart_repo`, or `image_repo` fields directly for a standard deployment. Override them only for a special registry layout or while debugging with guidance from Sekoia.

The registry must meet the following conditions:

- It uses token (Bearer) authentication. When a client connects without a token, the registry answers `401` with a `WWW-Authenticate: Bearer` header. The SHC rejects a registry that answers with `WWW-Authenticate: Basic`. To check your registry, run `curl -sk -o /dev/null -D - https://<REGISTRY_HOST>/v2/ | grep -i www-authenticate`.
- A self-signed certificate is accepted: the SHC, the Kubernetes nodes, and ArgoCD do not verify the certificate of the registry.
- The orchestration node reaches the registry without a proxy. The SHC has no proxy setting for the registry.

The SHC publishes the images under `<project>/images/`, the Helm charts under `<project>/charts/`, and checks the account permissions with a temporary `<project>/shc-probe` image that it pushes, pulls, and deletes.

### Instance license

| Field | Description |
| :--- | :--- |
| `modules.platform_configuration.config.global.instance_public_key` | Base64-encoded public key used to validate the Sekoia instance license. Sekoia provides this value. Use an environment-variable reference. |

### TLS certificate

Traefik serves the platform with your certificate on HTTPS and on the syslog and RELP intake ports. Provide the certificate and its private key in PEM format. The SHC reads them from two environment variables, and the [execution script](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script) passes both to the SHC container.

| Field | Environment variable | Description |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.traefik.custom_cert.crt` | `TRAEFIK_PUBKEY` | Certificate chain in PEM format. |
| `modules.platform_configuration.config.traefik.custom_cert.key` | `TRAEFIK_PRIVKEY` | Private key of the certificate in PEM format, without a passphrase. |

The certificate must meet the following conditions:

- It is valid for every hostname the platform serves: `global.host`, `global.delivery_host`, and `global.alternative_hosts`. Each name is in its Subject Alternative Name, directly or through a wildcard.
- The file starts with the server certificate, followed by the intermediate certificates.
- When a private certificate authority signs it, the file ends with the root certificate of this authority. The platform services trust this file, in addition to the public authorities, when they call the platform through `global.host` and when they connect to your SMTP server. If your SMTP server uses a certificate from a private authority, append the root certificate of this authority too.

To load the certificate and its key on the orchestration node, run:

```bash
export TRAEFIK_PUBKEY="$(cat /path/to/certificate.pem)"
export TRAEFIK_PRIVKEY="$(cat /path/to/private-key.pem)"
```

!!! warning "A certificate is required"
    Sekoia Self-Hosted 1.0.1 does not support an installation without a certificate. When `TRAEFIK_PUBKEY` is empty, the `CustomCA` step of the installation fails with `Custom CA not defined`. When the variables are not passed to the SHC container at all, the SHC only logs an `Unresolved template marker` warning: the certificate secret of Traefik then holds no valid certificate, Traefik serves its own default certificate, and the `console` and `ingest` diagnostics report the certificate secret as critical. For a test platform, generate a self-signed certificate that covers the platform hostnames.

To check the certificate that the platform serves on HTTPS, syslog, and RELP, see [Check the load balancer listeners](/self_hosted/1.0.1/deployment/network_requirements.md#check-the-load-balancer-listeners). To renew or replace the certificate after the installation, see [Rotate the certificate and credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md).

## Settings with placeholder defaults

The following settings are not required by the validator, but their default values are examples that do not match your environment. `CheckLocalConfig` accepts them as they are, so review each one before the installation.

!!! warning "Replace the placeholder values"
    With the default values, the platform sends its emails to a server named `mail.server.local` and builds the Grafana links on `admin.sekoia.local`. Set the values for your domain before you run `Install`.

### Email notifications

The platform sends notifications and user invitation emails through your SMTP server.

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.email.email_sender` | Sender address of the platform emails. | `noreply@sekoia.local` |
| `modules.platform_configuration.config.email.smtp.host` | Hostname of the SMTP server. | `mail.server.local` |
| `modules.platform_configuration.config.email.smtp.port` | Port of the SMTP server. | `25` |
| `modules.platform_configuration.config.email.smtp.user` | SMTP username. | `smtp-user` |
| `modules.platform_configuration.config.email.smtp.password` | SMTP password. Use an environment-variable reference. | `smtp-password` |
| `modules.platform_configuration.config.email.smtp.tls` | `"True"` to open the connection with implicit TLS, commonly on port 465. | `"False"` |
| `modules.platform_configuration.config.email.smtp.starttls` | `"True"` to upgrade the connection with STARTTLS, commonly on port 587. | `"True"` |

The `tls` and `starttls` fields accept only the strings `"True"` and `"False"`, with an uppercase first letter.

### Grafana URL

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.grafana.root_url` | Public URL of Grafana. Grafana is served under the `/grafana` path of `global.delivery_host`, so set it to `https://<global.delivery_host>/grafana`. | `https://admin.sekoia.local/grafana` |

### Alternative hostname

| Field | Description | Default |
| :--- | :--- | :--- |
| `global.alternative_hosts` | Additional FQDN accepted by the platform alongside `global.host`. It accepts one hostname. Set it to a hostname of your domain and create its DNS record. | `api.sekoia.local` |

??? example "Placeholder settings in `config.yml`"
    ```yaml
    global:
      alternative_hosts: "api.example.com"

    modules:
      platform_configuration:
        config:
          grafana:
            root_url: "https://admin.example.com/grafana"
          email:
            email_sender: "noreply@example.com"
            smtp:
              host: "smtp.example.com"
              port: "587"
              user: "sekoia"
              password: "${env.SMTP_PASSWORD}"
              tls: "False"
              starttls: "True"
    ```

    Pass every environment variable you reference to the SHC container. For example, add `-e SMTP_PASSWORD="$SMTP_PASSWORD"` to the `docker run` command of the [execution script](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script).

## Optional settings

### Release download and security content

The SHC reads the platform release and the security content bundles from local directories. In online mode, it first downloads them from the Sekoia S3 bucket at `https://self-hosted.delivery.sekoia.io`, with the `S3_ACCESS_KEY` and `S3_SECRET_KEY` credentials provided by Sekoia. In air-gapped mode, it uses the files extracted from the release archive.

| Field | Description | Default |
| :--- | :--- | :--- |
| `global.version.fetch.offline` | `true` to skip every download from the Sekoia S3 bucket. Set it to `true` for an air-gapped deployment. | `false` |
| `global.version.fetch.endpoint` | Online mode only. Endpoint of the Sekoia release bucket. Set it to `https://self-hosted.delivery.sekoia.io`: the default value is not the customer delivery endpoint. | Not applicable |
| `global.version.fetch.connect-timeout` | Online mode only. Seconds to wait for a connection to the S3 endpoint, per attempt. | `10` |
| `global.version.fetch.read-timeout` | Online mode only. Seconds to wait for data from the S3 endpoint, per attempt. Increase it behind a slow proxy. | `60` |
| `global.version.fetch.max-attempts` | Online mode only. Total attempts per S3 request, first try included. | `3` |
| `global.version.platform.path` | Local directory of the platform release files. | `/opt/sekoia/platform/` |
| `global.version.data.detection-rules.version` | Online mode only. Detection rules bundle to download: `latest`, or the release ID of a bundle to pin. | `latest` |
| `global.version.data.intake-formats.version` | Online mode only. Intake formats bundle to download: `latest`, or the release ID of a bundle to pin. | `latest` |
| `global.version.data.playbook-library.version` | Online mode only. Playbook library bundle to download: `latest`, or the release ID of a bundle to pin. | `latest` |
| `global.version.data.cti.version` | CTI export imported by `ImportArangoCollection`: `latest`, a day such as `2026-09-03`, or an exact export such as `2026-09-03T09`. See [Import the CTI database](/self_hosted/1.0.1/operations/import_cti_database.md). | `latest` |
| `global.version.data.<TYPE>.path` | Local directory of the bundles of each type. The bundles are stored in a `<TYPE>` subdirectory. | `/opt/sekoia/data/` |

??? example "Online mode in `config.yml`"
    ```yaml
    global:
      version:
        fetch:
          endpoint: "https://self-hosted.delivery.sekoia.io"
    ```

    The SHC reads the bucket credentials from the `S3_ACCESS_KEY` and `S3_SECRET_KEY` environment variables. The [execution script](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script) passes them to the container.

The release ID of a bundle is its file name without the `<TYPE>-` prefix and the `.tar.gz` extension. For example, the file `detection-rules-2.20260813-31688094717-35a441d88ed9c2b23b078e476fb35a6c2a40df84.tar.gz` has the release ID `2.20260813-31688094717-35a441d88ed9c2b23b078e476fb35a6c2a40df84`.

!!! note "Bundle selection in air-gapped mode"
    In air-gapped mode, the `version` fields of the bundles are ignored. The SHC uses the bundle named in the `latest` file of each `data/<TYPE>/` directory.

### Proxy

Configure these fields when the platform, the container runtime, or the SHC reaches external services through an HTTP or HTTPS proxy. Each component uses its own settings.

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.proxy.http_proxy` | HTTP proxy URL used by the platform components that reach external services: ArgoCD, ExaLog indexing, the threat intelligence backend, and playbook actions. | Empty |
| `modules.platform_configuration.config.proxy.https_proxy` | HTTPS proxy URL used by the platform components. | Empty |
| `modules.platform_configuration.config.proxy.no_proxy` | Comma-separated destinations that the platform components reach without the proxy. Keep the default value and use `additional_no_proxy` for your own entries. | `127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.svc,.cluster.local,.lab` |
| `modules.platform_configuration.config.proxy.additional_no_proxy` | Comma-separated destinations appended to `no_proxy` when the SHC generates the platform configuration. Set your Git, OCI registry, and S3 hostnames here when they are reachable without the proxy. | Empty |
| `modules.platform_configuration.config.proxy.no_proxy_include_platform_domain` | `true` to append the platform FQDNs (`global.host`, `global.alternative_hosts`, and `global.delivery_host`) to `no_proxy`, so that the platform components reach their own endpoints without the proxy. | `true` |
| `modules.k3s_install.pull_images_with_proxy` | Routes the container image pulls of the Kubernetes nodes through a proxy. | `false` |
| `modules.k3s_install.k3s_http_proxy` | HTTP proxy URL used for image pulls when `pull_images_with_proxy` is `true`. | Empty |
| `modules.k3s_install.k3s_https_proxy` | HTTPS proxy URL used for image pulls when `pull_images_with_proxy` is `true`. | Empty |
| `modules.k3s_install.k3s_no_proxy` | Destinations reached without the proxy for image pulls. | `127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.svc,.cluster.local,.lab` |
| `utils.git.http.proxy` | Proxy URL used by the SHC for Git operations over HTTP or HTTPS. | Empty |

!!! tip "Keep the default exclusions"
    To exclude more destinations from the proxy, set them in `additional_no_proxy` instead of editing `no_proxy`. The default `no_proxy` list keeps the cluster-internal and private addresses out of the proxy, and the platform FQDNs are added automatically. Add your Git, OCI registry, and S3 hostnames when they are reachable without the proxy: an address range does not match a hostname.

The SHC computes the final `no_proxy` value when `PlatformConfigurationFile` runs, by concatenating three lists:

1. The value of `no_proxy`.
2. The platform FQDNs, when `no_proxy_include_platform_domain` is `true`.
3. The value of `additional_no_proxy`.

Duplicate entries are removed. These three fields only apply to the platform components. The image pulls of the nodes use `modules.k3s_install.k3s_no_proxy`, which is applied as is.

??? example "Proxy configuration in `config.yml`"
    ```yaml
    modules:
      platform_configuration:
        config:
          proxy:
            http_proxy: "http://proxy.example.com:3128"
            https_proxy: "http://proxy.example.com:3128"
            additional_no_proxy: "git.example.com,registry.example.com,s3.example.com"
    ```

### Traefik service IP

Traefik is the HTTP entry point of the platform. The SHC gives its Kubernetes service a fixed cluster-internal IP. Inside the cluster, CoreDNS resolves the platform FQDNs to that IP: `global.host`, `global.alternative_hosts`, and `global.delivery_host`. The platform components therefore reach each other without leaving the cluster.

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.traefik.service_ip` | Fixed ClusterIP of the Traefik service, inside the K3s service network `10.43.0.0/16`. Leave empty to let Kubernetes assign one. | `10.43.111.111` |

!!! warning "Empty value disables the internal resolution of the platform FQDNs"
    When the field is empty, `HelmInstall` adds no entry to CoreDNS, so the platform FQDNs resolve inside the cluster through the DNS servers of `global.forward_dns` only.

### SHC log file

Every SHC run, in CLI or TUI mode, writes its log lines to a dedicated file. The SHC takes the directory and file name from `global.logging.file`, and prefixes the file name with the start time of the run, for example `20261023-153000_self-hosted-controller.log`, so that successive runs never overwrite each other. Sekoia support asks for this file when you escalate an issue.

| Field | Description | Default |
| :--- | :--- | :--- |
| `global.logging.file` | Path of the per-run log file, inside the SHC container. Set it under `/opt/sekoia`, the mount point of `$SEKOIA_LOCAL_DIR`, to keep the file on the orchestration node. The field does not appear in `config help`. | `/tmp/self-hosted-controller.log` |

!!! warning "The default path loses the file"
    The execution script runs the container with `--rm` and mounts only `$SEKOIA_CONFIG_FILE` and `$SEKOIA_LOCAL_DIR`. With the default value, the file is written to `/tmp` inside the container and deleted when the command exits. Set the field in every deployment.

??? example "Log file on the orchestration node in `config.yml`"
    ```yaml
    global:
      logging:
        file: /opt/sekoia/logs/self-hosted-controller.log
    ```

    With this value, the log of a run started on 23 October 2026 at 15:30:00 is kept at `$SEKOIA_LOCAL_DIR/logs/20261023-153000_self-hosted-controller.log` on the orchestration node.

The SHC creates the directory if it does not exist. If it cannot create the file, it starts without file logging: the CLI reports nothing, and the TUI displays `log: (disabled)` at the bottom of the interface. Give UID 1000 write access to `$SEKOIA_LOCAL_DIR`, as described in the [container user](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script) note of the deployment guide.

### Database storage

These fields set the disk size of each instance of the PostgreSQL clusters of the platform. Each cluster runs three instances. The asset management, alerts, workflow engine, playbooks, and ExaLog metastore databases grow with platform usage.

!!! warning "Storage size can only increase"
    CloudNativePG cannot shrink a volume. Set a value equal to or larger than the current size of the cluster volumes.

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.assetmanagement.database.storage.size` | Storage size of the asset management database. | `1Ti` |
| `modules.platform_configuration.config.sicalertapi.database.storage.size` | Storage size of the alerts database. | `50Gi` |
| `modules.platform_configuration.config.quickwit.database.storage.size` | Storage size of the ExaLog metastore database. | `50Gi` |
| `modules.platform_configuration.config.hatchet.database.storage.size` | Storage size of the workflow engine database. | `30Gi` |
| `modules.platform_configuration.config.symphony.database.storage.size` | Storage size of the playbooks database. | `30Gi` |
| `modules.platform_configuration.config.quickwit.database.storage.size` | Storage size of the ExaLog metastore database. | `50Gi` |
| `modules.platform_configuration.config.communityapi.database.storage.size` | Storage size of the community and user database. | `20Gi` |
| `modules.platform_configuration.config.crmapi.database.storage.size` | Storage size of the `crmapi` database. | `20Gi` |
| `modules.platform_configuration.config.dashboardapi.database.storage.size` | Storage size of the dashboards database. | `20Gi` |
| `modules.platform_configuration.config.notificationapi.database.storage.size` | Storage size of the notifications database. | `20Gi` |
| `modules.platform_configuration.config.taskapi.database.storage.size` | Storage size of the tasks database. | `20Gi` |
| `modules.platform_configuration.config.ingest.database.storage.size` | Storage size of the ingestion database. | `20Gi` |
| `modules.platform_configuration.config.xdr-agent-api.database.storage.size` | Storage size of the `xdr-agent-api` database. The service is deployed but not supported in 1.0.1. | `20Gi` |

The asset management database also defaults to 2 CPUs and 4 GiB of memory per instance, set in `assetmanagement.database.resources.cpu` and `assetmanagement.database.resources.memory`.

### Ceph storage devices

By default, Ceph uses every unused raw disk of every node, as described in [Dedicated storage disk](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#dedicated-storage-disk). To use only the disks or the LVM logical volumes that you select, set the manual mode:

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.rook.storage.mode` | `auto` to use every unused raw disk, or `manual` to use only the devices listed in `nodes`. | `auto` |
| `modules.platform_configuration.config.rook.storage.nodes` | Manual mode only. List of nodes, each with a `name`, the hostname of the node, and a `devices` list of `name` entries, the `/dev/` paths of the selected devices. Must be empty in `auto` mode. | `[]` |

??? example "Manual Ceph storage in `config.yml`"
    ```yaml
    modules:
      platform_configuration:
        config:
          rook:
            storage:
              mode: manual
              nodes:
                - name: node-01
                  devices:
                    - name: /dev/sdb
                - name: node-02
                  devices:
                    - name: /dev/vg-ceph/lv-ceph
    ```

In manual mode, the following conditions apply:

- Each `name` is the hostname of one node of the inventory, in lowercase. `CheckServerSpec` fails when a name matches no node.
- Each device is a whole raw disk or an LVM logical volume that you created and activated, 200 GB or larger, writable, not mounted, and without a filesystem, a partition table, or another signature. `CheckServerSpec` checks every selected device before the installation.
- `lvm2` is already installed on every node that has a selected device: `CheckServerSpec` checks it before the SHC installs any package.
- Ceph creates one unencrypted OSD per device.
- `WipeStorageDisks` does not wipe the selected devices and does not remove `/var/lib/rook` from the nodes. After a `PlatformDestroy`, clean them yourself before you reuse them.

### Backups

Backups are disabled by default. To back up Vault, the PostgreSQL databases, ArangoDB, and ClickHouse to S3, set `modules.platform_configuration.config.backups.enabled` to `true`. Before you enable backups:

- Create the backup bucket, `exalog-self-hosted-backups` by default, on your S3-compatible storage. See [Backup bucket](/self_hosted/1.0.1/deployment/deployment_prerequisites.md#backup-bucket).
- Set the `BACKUP_VAULT_CRYPT_KEY`, `BACKUP_ARANGO_CRYPT_KEY`, and `BACKUP_CLICKHOUSE_CRYPT_KEY` environment variables, and pass them to the SHC container. Keep a copy of each key outside the platform.

!!! warning "Missing backup keys stop the installation late"
    `CheckLocalConfig` does not report a missing backup encryption key. When backups are enabled and a key is empty, `PlatformConfigurationFile` stops the installation in the `platform` stage, after Kubernetes is installed.

For the per-component settings, the schedules, the retention, and the backup status check, see [Back up the platform](/self_hosted/1.0.1/operations/backups.md).

## Inspect the configuration with the SHC

Use the SHC itself to discover supported optional fields and verify the computed configuration.

!!! note
    These commands require the SHC Docker image and the execution script. If you have not prepared them yet, complete the [Preparation](/self_hosted/1.0.1/deployment/deployment_guide.md#preparation) steps of the deployment guide, then come back to this section before you start the installation.

To list supported configuration fields, run:

```bash
config help
```

Add a prefix to focus on one section:

```bash
config help global.platform_storage
config help utils.oci_registry
```

!!! warning "Protect resolved secrets"
    `config show` prints every resolved value in clear text, including the S3 keys, the registry and Git passwords, the SSH private key, the private key of the certificate, and the backup encryption keys. It has no option to mask them. Prefer displaying a section that holds no secret, such as `config show utils.ansible.inventory`. Do not paste its output into tickets, chat messages, or logs. Redact all secrets before sharing it with Sekoia support. To check for missing or invalid values without printing them, run `exec CheckLocalConfig` instead.

To display the configuration after defaults, inheritance, environment references, and derived values have been resolved, run:

```bash
config show
```

You can also display one section:

```bash
config show utils.ansible.inventory
```

Finally, validate the configuration before starting an installation:

```bash
exec CheckLocalConfig
```

The command reports missing required values, invalid formats, and unsupported keys. It names the configuration key of each error, without printing its value. Correct every error before continuing.

## Related links

- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Prepare the SHC execution script and install the platform.
- [Apply a configuration change](/self_hosted/1.0.1/operations/apply_configuration_change.md): Change `config.yml` after the installation and apply it with `Install`.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): Run configuration commands from the interactive interface.
- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): Resolve configuration and connectivity failures.
