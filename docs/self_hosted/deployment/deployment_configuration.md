# Deployment configuration reference

The `config.yml` file is the central manifest used to describe your environment and service requirements. It dictates how the self-hosted controller orchestrates infrastructure deployment and application settings.

## Configuration example

You can use this complete example as a template for your own deployment. Ensure you replace the placeholders and environment variable references with your actual values.

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
    check_repo: "my-project/shc-probe"
    chart_repo: "my-project/charts"
    image_repo: "my-project/images"
  prometheus:
    url: env.PROMETHEUS_URL
    query_window: "1h"
    query_timeout: 10
    default_label_filters: {
      "platform": "app.dev1.sekoia.io"
    }
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
    forward_dns: "10.X.X.X"
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
        http_proxy: "http://proxy.lab:3128"
        https_proxy: "http://proxy.lab:3128"
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

## Manifest parameters

### 1. Global
This section defines the platform identity, notification behavior, and how the controller fetches release assets from remote storage.

* **global.dev** (boolean): Enables development mode behaviors, such as verbose logging and extended error reporting.
* **global.emit_mm_notif** (boolean): Enables the sending of installation progress notifications to Mattermost.
* **global.host** (string): The primary FQDN used to access the Sekoia.io platform.
* **global.alternative_hosts** (string): Secondary FQDNs used for API access or auxiliary services.

#### global.version.fetch (optional: online deployment only)
* **global.version.fetch.access-key** (string): S3 access key required to authenticate with the release bucket.
* **global.version.fetch.secret-key** (string): S3 secret key required to authenticate with the release bucket.
* **global.version.fetch.endpoint** (string): The S3 API endpoint URL (e.g., Linode, AWS, or MinIO).
* **global.version.fetch.region** (string): The geographical region of the S3 bucket.
* **global.version.fetch.bucket** (string): The name of the S3 bucket containing the self-hosted release assets.

#### global.version.platform
* **global.version.platform.version** (string): The specific version tag of the platform to deploy.
* **global.version.platform.path** (string): Local absolute path on the admin node where the release archive is stored.
* **global.version.platform.skip_existing_local** (boolean): If `true`, the controller skips downloading files already present on the local disk.
* **global.version.platform.skip_existing_manifest** (boolean): If `true`, the controller always uses the local manifest copy, bypassing age checks.
* **global.version.platform.manifest_max_age** (integer): Time in seconds before the local manifest is considered expired and re-downloaded.
* **global.version.platform.push_workers** (integer): Number of parallel threads used to push images and Helm charts to the local registry.

#### global.version.data
* **global.version.data.detection-rules** (object): Version and local path for the detection logic bundle.
* **global.version.data.intake-formats** (object): Version and local path for log parsing formats.
* **global.version.data.playbook-library** (object): Version and local path for automation playbooks.
* **global.version.data.cti** (object): Version and local path for Cyber Threat Intelligence data.

### 2. Utils
This section configures the underlying tools (Ansible, Git, Kubernetes) and external service integrations required for the deployment.

#### utils.ansible
* **utils.ansible.datadir** (string): Path to the directory containing Ansible playbooks, roles, and inventories.
* **utils.ansible.ssh-key** (string): Path or environment variable for the SSH private key used to manage nodes.
* **utils.ansible.user** (string): The remote user used for SSH connections (e.g., `root` or `debian`).
* **utils.ansible.password** (string): The sudo password or environment variable for privilege escalation.
* **utils.ansible.inventory.managers** (list): IP addresses or FQDNs of the Kubernetes manager nodes.
* **utils.ansible.inventory.workers** (list): IP addresses or FQDNs of the Kubernetes worker nodes.

#### utils.git
* **utils.git.auth_method** (string): Protocol used to authenticate with Git repositories (`http` or `ssh`).
* **utils.git.repo_url** (string): The remote URL of the Git repository containing environment manifests.
* **utils.git.http.username** (string): Username for HTTP-based Git authentication.
* **utils.git.http.password** (string): Password or Token for HTTP-based Git authentication.
* **utils.git.http.proxy** (string): Optional proxy URL specifically for Git HTTP operations.
* **utils.git.ssh.key_path** (string): Path to the SSH key for Git authentication.

#### utils.kubernetes
* **utils.kubernetes.kubeconfig_path** (string): Destination path where the generated cluster `kubeconfig` will be stored.
* **utils.kubernetes.autologin** (boolean): If `true`, automatically performs a CLI login to the cluster after deployment.

#### utils.oci_registry
* **utils.oci_registry.url** (string): The full URL of the OCI-compliant container registry.
* **utils.oci_registry.username** (string): Registry authentication username.
* **utils.oci_registry.password** (string): Registry authentication password.
* **utils.oci_registry.check_repo** (string): Full path to an image used for registry health-check probes.
* **utils.oci_registry.chart_repo** (string): Base repository path for Helm chart storage.
* **utils.oci_registry.image_repo** (string): Base repository path for Docker image storage.

#### utils.prometheus
* **utils.prometheus.url** (string): The endpoint URL for the Prometheus monitoring server.
* **utils.prometheus.query_window** (string): The default time window applied to metric queries (e.g., `1h`).
* **utils.prometheus.query_timeout** (integer): Maximum duration in seconds for a Prometheus query to complete.
* **utils.prometheus.default_label_filters** (object): Set of default labels used to filter all outgoing Prometheus queries.

#### utils.argocd
* **utils.argocd.namespace** (string): The Kubernetes namespace where ArgoCD services are deployed.
* **utils.argocd.root_app_name** (string): The name assigned to the "App-of-Apps" root manifest.

#### utils.notification
* **utils.notification.url** (string): Base URL for the internal notification service.
* **utils.notification.channel** (string): The Mattermost channel identifier for posting updates.
* **utils.notification.thread_id** (string): A logical identifier used to group notification messages into threads.

#### utils.platform_installer
* **utils.platform_installer.image** (string): The full Docker image URI for the Sekoia.io platform installer.

### 3. Modules
This section provides granular configuration for each functional phase of the platform installation.

#### modules.k3s_install
* **modules.k3s_install.k3s_release** (string): The Kubernetes version tag to be installed.
* **modules.k3s_install.k3s_tls_san** (list): List of additional SANs (Subject Alternative Names) for the API server certificate.
* **modules.k3s_install.kube_manager_fqdn** (string): The FQDN or IP of the primary manager node used for cluster orchestration.
* **modules.k3s_install.k3s_extra_args** (string): Additional command-line arguments passed to the K3s server/agent process.
* **modules.k3s_install.k3s_extra_labels** (object): Key-value pairs to be applied as labels to the Kubernetes nodes.
* **modules.k3s_install.k3s_extra_taints** (list): List of taints to be applied to the Kubernetes nodes.
* **modules.k3s_install.registry_url** (string): The private registry URL used by the nodes to pull images.
* **modules.k3s_install.registry_subpath** (string): Optional prefix path for rewriting registry image locations.
* **modules.k3s_install.pull_images_with_proxy** (boolean): Enables the use of an HTTP proxy for `containerd` image pulls.
* **modules.k3s_install.k3s_http_proxy** (string): The HTTP proxy URL for the K3s runtime.
* **modules.k3s_install.k3s_https_proxy** (string): The HTTPS proxy URL for the K3s runtime.
* **modules.k3s_install.k3s_no_proxy** (string): List of CIDRs and domains that bypass the proxy.
* **modules.k3s_install.reboot_after_install** (boolean): If `true`, the host nodes are rebooted immediately following the K3s installation.

#### modules.push_argo_stacks
* **modules.push_argo_stacks.repo_path** (string): Local directory path where the ArgoCD manifest repositories are synchronized.

#### modules.helm_install
* **modules.helm_install.kube_manager_fqdn** (string): FQDN or IP of the manager node for Helm deployment tasks.
* **modules.helm_install.forward_dns** (string): The upstream DNS server IP used by the cluster's CoreDNS.

#### modules.wipe_storage
* **modules.wipe_storage.enabled** (boolean): Authorizes the controller to format and wipe disks (required for Ceph/Rook storage setup).

#### modules.kube_crash_recovery
* **modules.kube_crash_recovery.pod_ready_timeout** (integer): Seconds to wait for all pods to reach the `Ready` state before a deployment phase times out.
* **modules.kube_crash_recovery.poll_interval** (integer): Frequency in seconds for checking pod status during recovery phases.

#### modules.platform_configuration
* **modules.platform_configuration.config.global** (object): Duplication of platform FQDNs for internal application context.
* **modules.platform_configuration.config.proxy** (object): Application-layer HTTP/HTTPS/NO_PROXY settings.
* **modules.platform_configuration.config.grafana.root_url** (string): The external URL used to access the Grafana dashboard.
* **modules.platform_configuration.config.email.smtp** (object): SMTP server details (`host`, `port`, `user`, `password`, `tls`, `starttls`) for platform alerts and notifications.
* **modules.platform_configuration.config.local_argocd** (object): Git and OCI credentials specifically for the ArgoCD instance to sync internal application manifests.