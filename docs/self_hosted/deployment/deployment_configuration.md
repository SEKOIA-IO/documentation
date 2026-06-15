# Deployment configuration reference

The `config.yml` file is the central manifest used to describe your environment, credentials, and service settings. The Self-Hosted Controller (SHC) reads this file at runtime to drive every deployment and lifecycle operation.

## Minimal airgap configuration

For an air-gapped deployment, only the parameters below are strictly required. The SHC `common.yaml` provides sensible defaults for everything else. Fill in all values marked with `# REQUIRED` before running the SHC.

Credentials that must never be stored in the file itself are resolved from environment variables using the `env.VAR_NAME` syntax. Set those variables in the shell environment before invoking the SHC.

```yaml
global:
  host: "app.example.com"                   # REQUIRED — primary FQDN of the platform
  alternative_hosts: "api.example.com"      # alternative FQDN (API access)
  version:
    fetch:
      offline: true                         # REQUIRED for airgap — disables remote S3 download
    platform:
      version: "v0.0.1"                     # REQUIRED — release version to deploy
      path: /opt/sekoia/platform/           # local directory where release files are stored
    data:
      detection-rules:
        version: "010126"                   # REQUIRED — data bundle version
        path: /opt/sekoia/data/
      intake-formats:
        version: "010126"                   # REQUIRED
        path: /opt/sekoia/data/
      playbook-library:
        version: "010126"                   # REQUIRED
        path: /opt/sekoia/data/
      cti:
        version: "010126"                   # REQUIRED
        path: /opt/sekoia/data/

utils:
  ansible:
    ssh-key: env.SERVERS_SSH_KEY            # REQUIRED — SSH private key for node provisioning
    inventory:
      managers:
        - 10.0.0.1                          # REQUIRED — IP of the first Kubernetes manager node
      workers:
        - 10.0.0.2
        - 10.0.0.3
  git:
    auth_method: "http"
    repo_url: "https://git.example.com/sekoia/argo-stacks.git"  # REQUIRED — internal git repository
    http:
      username: env.GIT_HTTP_USERNAME
      password: env.GIT_HTTP_PASSWORD
  oci_registry:
    url: env.OCI_REGISTRY_URL               # REQUIRED — internal OCI registry URL
    username: env.REGISTRY_USERNAME         # REQUIRED
    password: env.REGISTRY_PASSWORD         # REQUIRED
    check_repo: "sekoia/shc-probe"
    chart_repo: "sekoia/charts"
    image_repo: "sekoia/images"

modules:
  k3s_install:
    kube_manager_fqdn: "10.0.0.1"          # REQUIRED — IP/FQDN of the first manager node
    registry_url: "https://registry.example.com"  # REQUIRED — internal registry for containerd
    registry_username: env.REGISTRY_USERNAME
    registry_password: env.REGISTRY_PASSWORD

  helm_install:
    kube_manager_fqdn: "10.0.0.1"          # REQUIRED — same as above
    forward_dns: "10.0.0.1"                # REQUIRED — upstream DNS forwarded by CoreDNS

  platform_configuration:
    platform_installer_command: "install"
    config:
      global:
        host: "app.example.com"            # REQUIRED — must match global.host
        alternative_hosts: "api.example.com"
        delivery_host: "admin.example.com" # REQUIRED — admin interface FQDN
        instance_public_key: env.SEKOIA_INSTANCE_PUBLIC_KEY  # REQUIRED — base64-encoded license key
      traefik:
        custom_cert:
          crt: env.TRAEFIK_PUBKEY          # TLS certificate for the platform ingress
          key: env.TRAEFIK_PRIVKEY
      quickwit:
        host: "quickwit.example.com"       # REQUIRED — S3 FQDN
        storage:
          s3:
            region: "us-east-1"
            endpoint: "https://s3.example.com"  # internal S3-compatible endpoint
            access_key: env.QW_S3_ACCESS_KEY
            secret_key: env.QW_S3_SECRET_KEY
            force_path_style_access: true
        indexer:
          replicaCount: 2
          persistentVolume:
            size: "150Gi"
            storageClass: "rook-ceph-block"
        searcher:
          replicaCount: 2
        database:
          instances: 3
          storage:
            size: "50Gi"
            storageClass: "rook-ceph-block"
      local_argocd:
        repo_url: "https://git.example.com/sekoia/argo-stacks.git"
        helm_repo_url: "oci://registry.example.com/sekoia/charts"
        git_username: env.GIT_HTTP_USERNAME
        git_password: env.GIT_HTTP_PASSWORD
        oci_username: env.REGISTRY_USERNAME
        oci_password: env.REGISTRY_PASSWORD
```

!!! tip "Environment variables"
    The following environment variables must be set before invoking the SHC:

    | Variable | Purpose |
    | :--- | :--- |
    | `SERVERS_SSH_KEY` | SSH private key (PEM) for Ansible node provisioning |
    | `OCI_REGISTRY_URL` | Internal OCI registry URL |
    | `REGISTRY_USERNAME` | OCI registry auth username |
    | `REGISTRY_PASSWORD` | OCI registry auth password |
    | `GIT_HTTP_USERNAME` | Git server auth username |
    | `GIT_HTTP_PASSWORD` | Git server auth password |
    | `SEKOIA_INSTANCE_PUBLIC_KEY` | Base64-encoded license public key (provided by Sekoia) |
    | `TRAEFIK_PUBKEY` | PEM-encoded TLS certificate for the platform ingress |
    | `TRAEFIK_PRIVKEY` | PEM-encoded TLS private key for the platform ingress |
    | `QW_S3_ACCESS_KEY` | S3 access key for Quickwit object storage |
    | `QW_S3_SECRET_KEY` | S3 secret key for Quickwit object storage |

## Configuration template

Use this template as a starting point for a full configuration. Replace all placeholder values before running the SHC.

??? example "Complete config.yml template"
    ```yaml
    global:
      dev: false
      emit_mm_notif: false
      host: "app.sekoia.local"
      alternative_hosts: "api.sekoia.local"
      version:
        platform:
          version: "v0.0.1"
          path: /opt/sekoia/platform/
          skip_existing_local: false
          skip_existing_manifest: false
          manifest_max_age: 300
          push_workers: 4
        data:
          detection-rules:
            version: "010126"
            path: /opt/sekoia/data/
          intake-formats:
            version: "010126"
            path: /opt/sekoia/data/
          playbook-library:
            version: "010126"
            path: /opt/sekoia/data/
          cti:
            version: "010126"
            path: /opt/sekoia/data/
    utils:
      ansible:
        datadir: "resources/ansible"
        ssh-key: env.SERVERS_SSH_KEY
        user: root
        password: env.SERVERS_SUDO_PASSWORD
        inventory:
          managers:
            - 10.0.0.1
          workers:
            - 10.0.0.2
            - 10.0.0.3
      git:
        auth_method: "http"
        repo_url: ""
        http:
          username: env.GIT_HTTP_USERNAME
          password: env.GIT_HTTP_PASSWORD
          proxy: ""
        ssh:
          key_path: env.GIT_SSH_KEY_PATH
      kubernetes:
        kubeconfig_path: "/tmp/self-hosted-controller/kubeconfig.yml"
        autologin: false
      oci_registry:
        url: env.OCI_REGISTRY_URL
        username: env.OCI_REGISTRY_USERNAME
        password: env.OCI_REGISTRY_PASSWORD
        check_repo: "your-project/shc-probe"
        chart_repo: "your-project/charts"
        image_repo: "your-project/images"
      prometheus:
        url: env.PROMETHEUS_URL
        query_window: "1h"
        query_timeout: 10
        default_label_filters:
          platform: "app.sekoia.local"
      argocd:
        namespace: "argocd"
        root_app_name: "root"
      notification:
        url: "http://localhost:6666"
        channel: "mi-self-hosted"
        thread_id: "deploy-job"
      platform_installer:
        image: "registry.sekoia.io/sekoialab/platform-installer:self-hosted-v0.14.0"
    modules:
      k3s_install:
        k3s_release: "v1.31.12+k3s1"
        k3s_tls_san: []
        kube_manager_fqdn: "10.0.0.1"
        k3s_extra_args: ""
        k3s_extra_labels: {}
        k3s_extra_taints: []
        registry_url: https://registry.sekoia.io
        registry_subpath: ""
        registry_username: env.REGISTRY_USERNAME
        registry_password: env.REGISTRY_PASSWORD
        pull_images_with_proxy: false
        k3s_http_proxy: ""
        k3s_https_proxy: ""
        k3s_no_proxy: "127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.svc,.cluster.local,.lab"
        reboot_after_install: false
      push_argo_stacks:
        repo_path: "/tmp/argo-stacks"
      helm_install:
        kube_manager_fqdn: "10.0.0.1"
        forward_dns: "10.0.0.53"
      wipe_storage:
        enabled: false
      kube_crash_recovery:
        pod_ready_timeout: 300
        poll_interval: 10
      platform_configuration:
        config:
          global:
            host: "app.sekoia.local"
            alternative_hosts: "api.sekoia.local"
            delivery_host: "app.sekoia.local"
          proxy:
            http_proxy: ""
            https_proxy: ""
            no_proxy: "127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.svc,.cluster.local,.lab"
          grafana:
            root_url: "https://app.sekoia.local/grafana"
          email:
            email_sender: "noreply@sekoia.local"
            smtp:
              host: "mail.server.local"
              user: "smtp-user"
              password: "smtp-password"
              port: "25"
              tls: "False"
              starttls: "True"
          local_argocd:
            repo_name: ""
            repo_url: ""
            helm_repo_url: ""
            git_username: env.GIT_HTTP_USERNAME
            git_password: env.GIT_HTTP_PASSWORD
            oci_username: env.REGISTRY_USERNAME
            oci_password: env.REGISTRY_PASSWORD
    ```

## global

Defines platform identity, notification behavior, and how the SHC locates release assets.

| Parameter | Required | Type | Description |
| :--- | :---: | :--- | :--- |
| `global.dev` | No | boolean | Enables development mode (verbose logging, extended error reporting). Default: `false`. |
| `global.emit_mm_notif` | No | boolean | Sends installation progress notifications to Mattermost. Requires both `global.dev: true` and `utils.notification` to be configured. Default: `false`. |
| `global.host` | Yes | string | Primary FQDN for platform access (e.g., `app.sekoia.local`). Must match a DNS A record pointing to your Load Balancer. |
| `global.alternative_hosts` | No | string | Secondary FQDNs for API access or auxiliary services (e.g., `api.sekoia.local`). |

### global.version.fetch

This section controls how the SHC fetches release assets from Sekoia's remote S3 bucket.

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `global.version.fetch.offline` | No | Set to `true` to skip all S3 downloads and operate in fully offline mode. Default: `false`. Use for air-gapped deployments where all files are pre-staged locally. |
| `global.version.fetch.access-key` | Conditional | S3 access key for the Sekoia release bucket. Required when `offline` is `false`. |
| `global.version.fetch.secret-key` | Conditional | S3 secret key for the Sekoia release bucket. Required when `offline` is `false`. |
| `global.version.fetch.endpoint` | Conditional | S3 API endpoint URL. Required when `offline` is `false`. |
| `global.version.fetch.region` | Conditional | S3 bucket region. Required when `offline` is `false`. |
| `global.version.fetch.bucket` | Conditional | Name of the S3 bucket containing release assets. Required when `offline` is `false`. |

### global.version.platform

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `global.version.platform.version` | Yes | Version tag to deploy (e.g., `v0.0.1`). |
| `global.version.platform.path` | Yes | Absolute path on the orchestration node to the extracted release directory. |
| `global.version.platform.fail_on_missing_data_files` | No | If `true`, treats missing or empty data bundle directories as errors instead of warnings. Default: `false`. |
| `global.version.platform.skip_existing_local` | No | If `true`, skips downloading files already present locally. Default: `false`. |
| `global.version.platform.skip_existing_manifest` | No | If `true`, uses the local manifest without checking its age. Default: `false`. |
| `global.version.platform.manifest_max_age` | No | Seconds before the local manifest is considered stale and re-downloaded. Default: `300`. |
| `global.version.platform.push_workers` | No | Number of parallel threads for pushing images and charts to the registry. Default: `4`. |

### global.version.data

Defines the version and local path for each security content bundle. Every bundle is shipped with the platform release.

!!! note "Version string format"
    Data bundle versions use the format `DDMMYY`. For example, `010126` represents January 1st, 2026. This is a content publication date, not a semantic version. Check the release notes or the archive manifest to find valid version strings for a given release.

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `global.version.data.detection-rules` | Yes | Version and local path for the detection rules bundle. |
| `global.version.data.intake-formats` | Yes | Version and local path for log parsing formats. |
| `global.version.data.playbook-library` | Yes | Version and local path for automation playbooks. |
| `global.version.data.cti` | Yes | Version and local path for Cyber Threat Intelligence data. |

## utils

Configures the underlying tools and external service integrations.

### utils.ansible

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `utils.ansible.datadir` | Yes | Path to the directory containing Ansible playbooks, roles, and inventories. |
| `utils.ansible.ssh-key` | Yes | SSH private key used to manage nodes. Accepts `env.VAR_NAME` references. |
| `utils.ansible.user` | Yes | Remote user for SSH connections (e.g., `root` or `debian`). |
| `utils.ansible.password` | No | Sudo password for privilege escalation. Required only if your SSH configuration uses password-based sudo. |
| `utils.ansible.inventory.managers` | Yes | IP addresses or FQDNs of Kubernetes manager nodes. At least 1 required. |
| `utils.ansible.inventory.workers` | Yes | IP addresses or FQDNs of Kubernetes worker nodes. |

### utils.git

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `utils.git.auth_method` | Yes | Authentication protocol: `http` or `ssh`. |
| `utils.git.repo_url` | Yes | Remote URL of the Git repository for ArgoCD stacks. |
| `utils.git.http.username` | Conditional | Username for HTTP Git authentication. Required if `auth_method` is `http`. |
| `utils.git.http.password` | Conditional | Password or token for HTTP Git authentication. Required if `auth_method` is `http`. |
| `utils.git.http.proxy` | No | Proxy URL for Git HTTP operations. |
| `utils.git.ssh.key_path` | Conditional | Path to the SSH key. Required if `auth_method` is `ssh`. |

### utils.kubernetes

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `utils.kubernetes.kubeconfig_path` | Yes | Path where the generated cluster kubeconfig will be stored. |
| `utils.kubernetes.autologin` | No | If `true`, performs a CLI login to the cluster after deployment. Default: `false`. |

### utils.oci_registry

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `utils.oci_registry.url` | Yes | Full URL of the OCI-compliant container registry. |
| `utils.oci_registry.username` | Yes | Registry authentication username. |
| `utils.oci_registry.password` | Yes | Registry authentication password. |
| `utils.oci_registry.check_repo` | Yes | Image path used for registry health-check probes (e.g., `your-project/shc-probe`). Must point to an existing image in your registry. |
| `utils.oci_registry.chart_repo` | Yes | Base path for Helm chart storage (e.g., `your-project/charts`). |
| `utils.oci_registry.image_repo` | Yes | Base path for Docker image storage (e.g., `your-project/images`). |

### utils.prometheus

Required only if you use SHC commands that query Prometheus (e.g., `DebugResourceAllocation`).

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `utils.prometheus.url` | Conditional | Prometheus server endpoint URL. |
| `utils.prometheus.query_window` | No | Default time window for metric queries (e.g., `1h`). |
| `utils.prometheus.query_timeout` | No | Maximum query duration in seconds. |
| `utils.prometheus.default_label_filters` | No | Default label filters for all queries. Set `platform` to your actual platform FQDN. |

### utils.argocd

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `utils.argocd.namespace` | Yes | Kubernetes namespace where ArgoCD is deployed. Default: `argocd`. |
| `utils.argocd.root_app_name` | Yes | Name of the ArgoCD App-of-Apps root manifest. Default: `root`. |

### utils.platform_installer

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `utils.platform_installer.image` | Yes | Full Docker image URI for the Sekoia platform installer. Provided by Sekoia in the release notes. |

## modules

Granular configuration for each installation phase.

### modules.k3s_install

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `k3s_release` | Yes | Kubernetes version tag (e.g., `v1.31.12+k3s1`). Use the version specified in the release notes. |
| `kube_manager_fqdn` | Yes | FQDN or IP of the primary manager node. |
| `registry_url` | Yes | URL of the private registry used by nodes to pull images. |
| `registry_username` | Yes | Registry username for containerd image pulls. |
| `registry_password` | Yes | Registry password for containerd image pulls. |
| `k3s_tls_san` | No | Additional SANs for the API server TLS certificate. |
| `k3s_extra_args` | No | Additional CLI arguments passed to the K3s process. |
| `k3s_extra_labels` | No | Key-value labels applied to Kubernetes nodes. |
| `k3s_extra_taints` | No | Taints applied to Kubernetes nodes. |
| `pull_images_with_proxy` | No | Enables HTTP proxy for containerd image pulls. Default: `false`. |
| `k3s_http_proxy` / `k3s_https_proxy` | No | Proxy URLs for the K3s runtime. |
| `k3s_no_proxy` | No | CIDR and domain bypass list for the proxy. |
| `reboot_after_install` | No | If `true`, reboots nodes after K3s installation. Default: `false`. |

### modules.helm_install

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `kube_manager_fqdn` | Yes | FQDN or IP of the manager node used for Helm deployment tasks. |
| `forward_dns` | Yes | Upstream DNS server IP used by the cluster's CoreDNS (e.g., `10.0.0.53`). Replace with your actual internal DNS resolver. |

### modules.wipe_storage

!!! warning "Destructive operation"
    Setting `enabled: true` authorizes the SHC to format and wipe disks. Enable this only if Sekoia explicitly instructs you to do so for your storage configuration.

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `enabled` | Yes | Authorizes disk wipe and format. Default: `false`. |

### modules.platform_configuration

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `platform_installer_command` | No | Platform-installer subcommand to run inside the Kubernetes job. Default: `install`. Use `install --skip-provisioners` to skip data provisioners on subsequent runs. |
| `config.global.host` | Yes | Must match `global.host`. |
| `config.global.alternative_hosts` | No | Must match `global.alternative_hosts`. |
| `config.global.delivery_host` | Yes | FQDN used for internal content delivery services. |
| `config.global.instance_public_key` | Yes | Base64-encoded public key used to validate Sekoia licenses. Set via `env.SEKOIA_INSTANCE_PUBLIC_KEY`. Provided by Sekoia at contract time. |
| `config.proxy.http_proxy` / `https_proxy` | No | Application-layer proxy settings. Required if your environment uses a forward proxy. |
| `config.proxy.no_proxy` | No | CIDR and domain bypass list for the application proxy. |
| `config.grafana.root_url` | No | External URL for the Grafana dashboard (e.g., `https://app.sekoia.local/grafana`). |
| `config.email.email_sender` | No | Sender address for platform notification emails. |
| `config.email.smtp.host` | No | SMTP server hostname or IP. |
| `config.email.smtp.port` | No | SMTP server port (e.g., `25`, `465`, `587`). Default: `25`. |
| `config.email.smtp.user` | No | SMTP authentication username. |
| `config.email.smtp.password` | No | SMTP authentication password. |
| `config.email.smtp.tls` | No | Enable SMTP over TLS (SMTPS). Accepts `"True"` or `"False"` as a string. Default: `"False"`. |
| `config.email.smtp.starttls` | No | Enable STARTTLS upgrade. Accepts `"True"` or `"False"` as a string. Default: `"True"`. |

!!! warning "SMTP boolean values"
    The `tls` and `starttls` fields accept **string values**, not YAML booleans. Use `"True"` or `"False"` (with quotes). Using unquoted `true` or `false` will cause a runtime error.

    ```yaml
    tls: "False"      # Correct
    starttls: "True"  # Correct
    tls: false        # Incorrect — will cause a runtime error
    ```

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `config.local_argocd.repo_url` | No | Git repository URL for ArgoCD synchronization. |
| `config.local_argocd.helm_repo_url` | No | Helm chart repository URL for ArgoCD (bare host/path without `oci://` scheme). |
| `config.local_argocd.git_username` | No | Git credentials for ArgoCD. |
| `config.local_argocd.git_password` | No | Git password or token for ArgoCD. |
| `config.local_argocd.oci_username` | No | OCI registry credentials for ArgoCD image pulls. |
| `config.local_argocd.oci_password` | No | OCI registry password for ArgoCD. |

### modules.platform_configuration.config.traefik

Optional. Configure a custom TLS certificate for the Traefik ingress controller. If omitted, Traefik generates a self-signed certificate.

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `config.traefik.custom_cert.crt` | No | Public certificate in PEM format. Accepts `env.TRAEFIK_PUBKEY`. |
| `config.traefik.custom_cert.key` | No | Private key in PEM format. Accepts `env.TRAEFIK_PRIVKEY`. |

### modules.platform_configuration.config.quickwit

Configures the Quickwit event indexer that backs the SOL query engine.

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `config.quickwit.host` | Yes | Quickwit internal FQDN (e.g., `quickwit.sekoia.local`). |
| `config.quickwit.storage.s3.region` | No | S3 region for Quickwit storage. |
| `config.quickwit.storage.s3.endpoint` | No | S3 endpoint URL for Quickwit storage. |
| `config.quickwit.storage.s3.access_key` | No | S3 access key. Accepts `env.QW_S3_ACCESS_KEY`. |
| `config.quickwit.storage.s3.secret_key` | No | S3 secret key. Accepts `env.QW_S3_SECRET_KEY`. |
| `config.quickwit.storage.s3.force_path_style_access` | No | Use path-style S3 access. Required for some S3-compatible providers. Default: `false`. |
| `config.quickwit.indexer.replicaCount` | No | Number of Quickwit indexer replicas. Default: `2`. |
| `config.quickwit.indexer.persistentVolume.size` | No | Persistent volume size for the indexer (e.g., `150Gi`). |
| `config.quickwit.indexer.persistentVolume.storageClass` | No | Storage class for the indexer PV. Default: `rook-ceph-block`. |
| `config.quickwit.searcher.replicaCount` | No | Number of Quickwit searcher replicas. Default: `2`. |

### modules.debug_argocd_sync_all

Controls the behavior of the `DebugArgoCDSyncAll` command.

| Parameter | Required | Description |
| :--- | :---: | :--- |
| `sync_timeout` | No | Maximum seconds to wait per application sync. Default: `300`. |
| `max_workers` | No | Maximum number of applications synced in parallel. Default: `32`. |
| `match_regex` | No | Regex for resource kinds to sync in the partial-sync phase (phase 1). Default: `(secretgenerator\|configmap)`. |
| `require_healthy` | No | If `true`, the post-sync check also requires `Health: Healthy` in addition to `Sync: Synced`. Default: `true`. |
| `operator_restart_wait` | No | Seconds to wait after restarting the `sekoiaio-secret-operator` before the full sync begins. Default: `60`. |

## Related links

- [Deploy the platform](./deployment_guide.md): Step-by-step installation instructions.
- [The deployment process](./deployment_process.md): How the SHC executes the configuration.
- [Debug your deployment](../troubleshooting/debug_tool.md): How to validate your configuration with `CheckLocalConfig`.
