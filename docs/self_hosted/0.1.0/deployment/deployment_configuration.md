# Configure the deployment

The `config.yml` file describes the environment that the Self-Hosted Controller (SHC) deploys. For Sekoia Self-Hosted 0.1.0, start from a built-in sizing profile and provide the site-specific values described on this page.

The SHC combines the built-in defaults, the selected sizing profile, and your `config.yml` into one computed configuration. It validates the result before installation and rejects missing required fields, invalid values, and unsupported keys.

This page explains every required field. To inspect supported optional settings, use the [SHC configuration commands](#inspect-the-configuration-with-the-shc).

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
      version: "v0.1.0"

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

`sizing/1tb-day.yaml` is one built-in sizing example. Additional profiles may be included in the GA release. A profile is a starting point, not a universal production recommendation: review and adjust it with Sekoia to match your event sizes, events per second, daily ingestion volume, retention requirements, and volume of search queries.

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

The platform uses S3-compatible object storage for ExaLog and other platform data. These credentials must allow the platform to create and use its required buckets.

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
| `global.version.platform.version` | Sekoia Self-Hosted release to deploy. Set it to `v0.1.0` for this GA documentation. |

### Kubernetes node access

| Field | Description |
| :--- | :--- |
| `utils.ansible.ssh-key` | Private key used by the SHC to connect to and configure every Kubernetes node. Use an environment-variable reference. |
| `utils.ansible.user` | SSH user used on every Kubernetes node. The account must meet the privilege requirements in the [technical requirements](./deployment_prerequisites.md). |
| `utils.ansible.inventory.managers` | List of manager-node IP addresses or resolvable hostnames. At least one manager is required. |

Worker nodes are configured under `utils.ansible.inventory.workers`. The field is not required by the configuration validator, but production sizing profiles normally require workers to provide the expected capacity.

### Git repository

| Field | Description |
| :--- | :--- |
| `utils.git.repo_url` | URL of the customer-managed Git repository in which the SHC publishes the ArgoCD stack manifests. |

If the repository requires authentication, use `config help utils.git` to inspect the supported HTTP and SSH authentication settings.

### OCI registry

| Field | Description |
| :--- | :--- |
| `utils.oci_registry.host` | Registry hostname, with an optional port and without a URL scheme, for example `registry.example.com` or `registry.example.com:5000`. |
| `utils.oci_registry.project` | Registry project or namespace in which the SHC publishes Sekoia artifacts, for example `sekoia-self-hosted`. |
| `utils.oci_registry.username` | Username with push, pull, and delete permissions in the registry project. Use an environment-variable reference. |
| `utils.oci_registry.password` | Password or token for the registry account. Use an environment-variable reference. |

The SHC derives the registry URL and the repositories used for checks, charts, and images from these values. Do not set the derived `url`, `check_repo`, `chart_repo`, or `image_repo` fields directly for a standard deployment. Override them only for a special registry layout or while debugging with guidance from Sekoia.

### Instance license

| Field | Description |
| :--- | :--- |
| `modules.platform_configuration.config.global.instance_public_key` | Base64-encoded public key used to validate the Sekoia instance license. Sekoia provides this value. Use an environment-variable reference. |

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
- [Use the controller interface](../operations/controller_interface.md): Run configuration commands from the interactive interface.
- [Debug your deployment](../troubleshooting/debug_tool.md): Resolve configuration and connectivity failures.
