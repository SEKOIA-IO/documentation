# Deployment configuration

The `config.yml` file is the central manifest used to describe your specific environment and service requirements.

## 1. Example `config.yml`

```yaml
global:
  dev: true
  host: "app.sekoia.local"
  alternative_hosts: "api.sekoia.local"
  version:
    platform:
      version: "v0.0.1"
      path: /opt/sekoia/platform/
      skip_existing_local: true
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
    user: debian
    password: ""
    silent: false
    verbosity: 2
    inventory:
      managers: ["TBD"]
      workers: ["TBD"]
  oci_registry:
    url: https://registry.lab/
    username: env.REGISTRY_USERNAME
    password: env.REGISTRY_PASSWORD
    check_repo: "TBD"
    chart_repo: "TBD"
    image_repo: "TBD"
  git:
    repo_url: ""
    auth_method: "http"
    http:
      username: env.GIT_HTTP_USERNAME
      password: env.GIT_HTTP_PASSWORD
    ssh:
      key_path: env.GIT_SSH_KEY_PATH
  kubernetes:
    autologin: true
  platform_installer:
    image: "?"

modules:
  k3s_install:
    k3s_release: "v1.31.12+k3s1"
    k3s_tls_san: []
    kube_manager_fqdn: "TBD"
    k3s_extra_args: ""
    k3s_extra_labels: {}
    k3s_extra_taints: []
    registry_url: https://registry.lab
    registry_subpath: "TBD"
    registry_username: env.REGISTRY_USERNAME
    registry_password: env.REGISTRY_PASSWORD
    pull_images_with_proxy: true
    k3s_no_proxy: "127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.svc,.cluster.local,.lab"
    reboot_after_install: false
  helm_install:
    kube_manager_fqdn: "TBD"
    forward_dns: "TBD"
  push_argo_stacks:
    repo_path: "/tmp/argo-stacks"
    base_branch: "master"
  wipe_storage:
    enabled: true
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
        repo_name: "self-hosted"
        repo_url: "TBD"
        helm_repo_url: "TBD"
        git_username: env.GIT_HTTP_USERNAME
        git_password: env.GIT_HTTP_PASSWORD
        oci_username: env.REGISTRY_USERNAME
        oci_password: env.REGISTRY_PASSWORD
```


## 2. Manifest parameters

## 1. Global
Defines the platform identity and version management.

* **`dev`** (boolean): Enables development mode (e.g., debug logging).
* **`host`** (string): The primary FQDN (Fully Qualified Domain Name) for the platform.
* **`alternative_hosts`** (string): Additional FQDNs for API or auxiliary access.
* **`version`**: Defines software and data bundle versions.
    * **`platform`**: Platform release details.
        * `version`: The release tag (e.g., "v0.0.1").
        * `path`: Local absolute path on the admin node where the release archive is stored.
        * `skip_existing_local`: Avoids re-copying existing files.
        * `push_workers`: Parallel workers for image deployment.
    * **`data`**: Configuration for data modules (`detection-rules`, `intake-formats`, `playbook-library`, `cti`).
        * Each sub-item requires a `version` tag and a local `path`.

## 2. Utils
Contains the infrastructure "plumbing" (credentials, paths, and registry settings).

* **`ansible`**:
    * `datadir`: Local path to Ansible inventory/roles.
    * `ssh-key`: Reference to the SSH key (`env.SERVERS_SSH_KEY`).
    * `user`: SSH user (typically `debian`).
    * `password`: Sudo password (`env.SERVERS_SUDO_PASSWORD`).
    * `inventory`: Lists of `managers` and `workers` node IPs/hostnames.
* **`oci_registry`**: Container registry settings.
    * `url`: The OCI registry URL.
    * `username` / `password`: Auth credentials (`env.REGISTRY_USERNAME`, `env.REGISTRY_PASSWORD`).
    * `check_repo`, `chart_repo`, `image_repo`: Repositories used for specific operations.
* **`git`**: Authentication for ArgoCD repositories.
    * `auth_method`: Authentication type (`http` or `ssh`).
* **`platform_installer`**: URI for the controller installer image.

## 3. Modules
Configures the functional installation of the platform stacks.

### k3s_install
Handles the underlying Kubernetes layer.
* **`k3s_release`**: The Kubernetes version tag.
* **`registry_url` / `registry_subpath`**: Internal image registry configuration.
* **`pull_images_with_proxy`**: Enables HTTP proxy for container pulls.
* **`k3s_no_proxy`**: CIDR/domains excluded from proxy traffic.
* **`k3s_extra_args`**: Additional CLI flags for the K3s server.

### helm_install
Handles Kubernetes application deployment.

* **`kube_manager_fqdn`**: FQDN of the primary manager.
* **`forward_dns`**: DNS nameservers for CoreDNS.

### push_argo_stacks

* **`repo_path`**: Local directory of the Git checkout.
* **`base_branch`**: Branch used to synchronize stacks (e.g., "master").

### wipe_storage

* **`enabled`**: If `true`, allows the controller to format disk storage.

### platform_configuration
Application-layer configuration.

* **`global`**: Repeats FQDN definitions for the internal context.
* **`proxy`**: Proxy settings for application traffic (http/https/no_proxy).
* **`grafana`**: `root_url` for dashboard access.
* **`email`**: SMTP configuration (`host`, `port`, `user`, `password`, `tls`, `starttls`).
* **`local_argocd`**: Git and OCI credentials used by the internal ArgoCD instance to synchronize application manifests.