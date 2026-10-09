# Configure the deployment

The `config.yml` file describes the environment that the self-hosted-controller (SHC) deploys. For Sekoia Self-Hosted 1.0.0, start from a built-in sizing profile and provide the site-specific values described on this page.

The SHC combines the built-in defaults, the selected sizing profile, and your `config.yml` into one computed configuration. It validates the result before installation and rejects missing required fields, invalid values, and unsupported keys.

This page explains every required field, the settings whose default value is a placeholder, and the most common optional settings. To inspect every other supported setting, use the [SHC configuration commands](#inspect-the-configuration-with-the-shc).

!!! warning "Validation does not catch every incorrect value"
    `CheckLocalConfig` rejects a required field that is missing or empty, but it does not check the optional fields that your environment needs. For example, the S3 credentials of the online mode are optional for the validator: when they are empty, the installation fails later, during the `push` stage. To confirm that every value your deployment needs is present and correct, inspect the computed configuration with `config show`.

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
      version: "v1.0.0"

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
| `SEKOIA_INSTANCE_PUBLIC_KEY` | Base64-encoded instance public key provided by Sekoia. |

The [deployment guide](./deployment_guide.md#step-4-create-the-execution-script) shows how to pass these variables to the SHC container.

## Select and adjust a sizing profile

`global.inherit_config` selects a sizing profile shipped with the SHC image. The profile supplies service replicas, resource allocations, storage sizes, and other capacity-related defaults, while your site configuration overrides the values specific to your environment.

The SHC image ships two sizing profiles. Each one adjusts only the resources whose load grows with the ingestion volume: Kafka, ExaLog, the KeyDB workflow cache, the intake and ingestion workers, and Sigma Workflow. Every other value comes from the built-in defaults.

| Profile | `global.inherit_config` value | Target |
| :--- | :--- | :--- |
| Minimal | `sizing/minimal.yaml` | Smallest supported footprint. Its values are pending performance validation. |
| 1 TB/day | `sizing/1tb-day.yaml` | Mid-range deployment ingesting around 1 TB of events per day. |

The `sizing/` path resolves against the configuration directory shipped in the SHC image, wherever you mount your own `config.yml`. A profile is a starting point, not a universal production recommendation: review and adjust it with Sekoia to match your event sizes, events per second, daily ingestion volume, retention requirements, and volume of search queries.

Use `config show` to review the result after inheritance, and `config help` to identify supported sizing overrides. Do not copy undocumented keys into your configuration: the SHC rejects unsupported fields.

## Required fields

### Platform endpoints

| Field | Description |
| :--- | :--- |
| `global.host` | Primary FQDN used to access the Sekoia platform, for example `app.example.com`. Configure DNS and the load balancer so this hostname reaches the platform. |
| `global.delivery_host` | Public FQDN used by delivery services, including the administrator portal, for example `admin.example.com`. |
| `global.kube_manager_host` | IP address or hostname used to reach the Kubernetes manager endpoint. For a highly available deployment, use the address of a TCP load balancer in front of the manager nodes. |
| `global.forward_dns` | DNS nameserver address forwarded by CoreDNS for name resolution outside the Kubernetes cluster. |

### Platform storage

The platform stores the ExaLog indexes in S3-compatible object storage. These credentials must allow the platform to use the event buckets listed in [Storage](./deployment_prerequisites.md#storage).

| Field | Description |
| :--- | :--- |
| `global.platform_storage.region` | Region configured by your S3-compatible storage provider. |
| `global.platform_storage.endpoint` | Endpoint used to access the S3-compatible storage. Include the URL scheme, for example `https://s3.example.com`. |
| `global.platform_storage.access_key` | Access key for the S3-compatible storage. Use an environment-variable reference. |
| `global.platform_storage.secret_key` | Secret key for the S3-compatible storage. Use an environment-variable reference. |

ExaLog storage configuration is derived from `global.platform_storage`. Some computed configuration keys retain `quickwit` in their names, but they configure the ExaLog capability.

### Release

| Field | Description |
| :--- | :--- |
| `global.version.platform.version` | Sekoia Self-Hosted release to deploy. Set it to `v1.0.0` for this GA documentation. |

### Kubernetes node access

| Field | Description |
| :--- | :--- |
| `utils.ansible.ssh-key` | Private key used by the self-hosted-controller (SHC) to connect to and configure every Kubernetes node. Use an environment-variable reference. |
| `utils.ansible.user` | SSH user used on every Kubernetes node. The account must meet the privilege requirements in the [technical requirements](./deployment_prerequisites.md). |
| `utils.ansible.inventory.managers` | List of manager-node IP addresses or resolvable hostnames. At least one manager is required. |

Worker nodes are configured under `utils.ansible.inventory.workers`. The field is not required by the configuration validator, but production sizing profiles normally require workers to provide the expected capacity.

### Git repository

| Field | Description |
| :--- | :--- |
| `utils.git.repo_url` | URL of the customer-managed Git repository in which the self-hosted-controller (SHC) publishes the ArgoCD stack manifests. |

If the repository requires authentication, use `config help utils.git` to inspect the supported HTTP and SSH authentication settings.

### OCI registry

| Field | Description |
| :--- | :--- |
| `utils.oci_registry.host` | Registry hostname, with an optional port and without a URL scheme, for example `registry.example.com` or `registry.example.com:5000`. |
| `utils.oci_registry.project` | Registry project or namespace in which the self-hosted-controller (SHC) publishes Sekoia artifacts, for example `sekoia-self-hosted`. |
| `utils.oci_registry.username` | Username with push, pull, and delete permissions in the registry project. Use an environment-variable reference. |
| `utils.oci_registry.password` | Password or token for the registry account. Use an environment-variable reference. |

The registry must serve HTTPS: ArgoCD pulls the Helm charts over HTTPS, even when `utils.oci_registry.scheme` is `http`. The SHC derives the registry URL and the repositories used for checks, charts, and images from these values. Do not set the derived `url`, `check_repo`, `chart_repo`, or `image_repo` fields directly for a standard deployment. Override them only for a special registry layout or while debugging with guidance from Sekoia.

### Instance license

| Field | Description |
| :--- | :--- |
| `modules.platform_configuration.config.global.instance_public_key` | Base64-encoded public key used to validate the Sekoia instance license. Sekoia provides this value. Use an environment-variable reference. |

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

    Pass every environment variable you reference to the SHC container. For example, add `-e SMTP_PASSWORD="$SMTP_PASSWORD"` to the `docker run` command of the [execution script](./deployment_guide.md#step-4-create-the-execution-script).

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
| `global.version.data.<TYPE>.path` | Local directory of the bundles of each type. The bundles are stored in a `<TYPE>` subdirectory. | `/opt/sekoia/data/` |

??? example "Online mode in `config.yml`"
    ```yaml
    global:
      version:
        fetch:
          endpoint: "https://self-hosted.delivery.sekoia.io"
    ```

    The SHC reads the bucket credentials from the `S3_ACCESS_KEY` and `S3_SECRET_KEY` environment variables. The [execution script](./deployment_guide.md#step-4-create-the-execution-script) passes them to the container.

The release ID of a bundle is its file name without the `<TYPE>-` prefix and the `.tar.gz` extension. For example, the file `detection-rules-2.20260813-31688094717-35a441d88ed9c2b23b078e476fb35a6c2a40df84.tar.gz` has the release ID `2.20260813-31688094717-35a441d88ed9c2b23b078e476fb35a6c2a40df84`.

!!! note "Bundle selection in air-gapped mode"
    In air-gapped mode, the `version` fields of the bundles are ignored. The SHC uses the bundle named in the `latest` file of each `data/<TYPE>/` directory.

### Custom TLS certificate

To serve the platform with a certificate issued by your own certificate authority, provide the certificate and its private key in PEM format. The SHC reads them from two environment variables.

| Field | Environment variable | Description |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.traefik.custom_cert.crt` | `TRAEFIK_PUBKEY` | Certificate in PEM format. |
| `modules.platform_configuration.config.traefik.custom_cert.key` | `TRAEFIK_PRIVKEY` | Private key of the certificate in PEM format. |

1. To load the certificate and its key on the orchestration node, run:

    ```bash
    export TRAEFIK_PUBKEY="$(cat /path/to/certificate.pem)"
    export TRAEFIK_PRIVKEY="$(cat /path/to/private-key.pem)"
    ```

2. Add `-e TRAEFIK_PUBKEY="$TRAEFIK_PUBKEY"` and `-e TRAEFIK_PRIVKEY="$TRAEFIK_PRIVKEY"` to the `docker run` command of the [execution script](./deployment_guide.md#step-4-create-the-execution-script).

The certificate must be valid for every hostname the platform serves: `global.host`, `global.delivery_host`, and `global.alternative_hosts`. Traefik serves it on HTTPS and on the syslog and RELP intake ports.

!!! warning "Without a custom certificate"
    When `TRAEFIK_PUBKEY` and `TRAEFIK_PRIVKEY` are not set, the certificate secret of Traefik is empty and Traefik serves its own self-signed default certificate. Browsers, API clients, and event forwarders then report an untrusted certificate.

### Proxy

Configure these fields when the platform, the container runtime, or the SHC reaches external services through an HTTP or HTTPS proxy. Each component uses its own settings.

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.proxy.http_proxy` | HTTP proxy URL used by the platform components that reach external services: ArgoCD, ExaLog indexing, the threat intelligence backend, and playbook actions. | Empty |
| `modules.platform_configuration.config.proxy.https_proxy` | HTTPS proxy URL used by the platform components. | Empty |
| `modules.platform_configuration.config.proxy.no_proxy` | Comma-separated destinations that the platform components reach without the proxy. | `127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.svc,.cluster.local,.lab` |
| `modules.k3s_install.pull_images_with_proxy` | Routes the container image pulls of the Kubernetes nodes through a proxy. | `false` |
| `modules.k3s_install.k3s_http_proxy` | HTTP proxy URL used for image pulls when `pull_images_with_proxy` is `true`. | Empty |
| `modules.k3s_install.k3s_https_proxy` | HTTPS proxy URL used for image pulls when `pull_images_with_proxy` is `true`. | Empty |
| `modules.k3s_install.k3s_no_proxy` | Destinations reached without the proxy for image pulls. | `127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.svc,.cluster.local,.lab` |
| `utils.git.http.proxy` | Proxy URL used by the SHC for Git operations over HTTP or HTTPS. | Empty |

!!! tip "Keep the default exclusions"
    To exclude more destinations from the proxy, append them to the default `no_proxy` value instead of replacing it. The default list keeps the cluster-internal and private addresses out of the proxy. Add your Git, OCI registry, and S3 hostnames when they are reachable without the proxy: an address range does not match a hostname.

### Database storage

These fields set the disk size of each instance of the PostgreSQL clusters whose data grows with platform usage. Each cluster runs three instances.

!!! warning "Storage size can only increase"
    CloudNativePG cannot shrink a volume. Set a value equal to or larger than the current size of the cluster volumes.

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_configuration.config.assetmanagement.database.storage.size` | Storage size of the asset management database. | `50Gi` |
| `modules.platform_configuration.config.sicalertapi.database.storage.size` | Storage size of the alerts database. | `50Gi` |
| `modules.platform_configuration.config.hatchet.database.storage.size` | Storage size of the workflow engine database. | `30Gi` |
| `modules.platform_configuration.config.symphony.database.storage.size` | Storage size of the playbooks database. | `30Gi` |

## Inspect the configuration with the SHC

Use the SHC itself to discover supported optional fields and verify the computed configuration.

To list supported configuration fields, run:

```bash
config help
```

Add a prefix to focus on one section:

```bash
config help global.platform_storage
config help utils.oci_registry
```

To display the configuration after defaults, inheritance, environment references, and derived values have been resolved, run:

```bash
config show
```

You can also display one section:

```bash
config show global.platform_storage
```

!!! warning "Protect resolved secrets"
    `config show` includes resolved credentials. Do not paste its output into tickets, chat messages, or logs. Redact all secrets before sharing it with Sekoia support.

Finally, validate the configuration before starting an installation:

```bash
exec CheckLocalConfig
```

The command reports missing required values, invalid formats, and unsupported keys. Correct every error before continuing.

## Related links

- [Deploy the platform](./deployment_guide.md): Prepare the SHC execution script and install the platform.
- [Use the SHC interface](../operations/controller_interface.md): Run configuration commands from the interactive interface.
- [Debug your deployment](../troubleshooting/debug_tool.md): Resolve configuration and connectivity failures.
