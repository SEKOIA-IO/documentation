# Rotate the certificate and credentials

You renew the platform certificate and rotate the credentials of your services by updating the environment variables or the `config.yml` file of the self-hosted-controller (SHC), then applying them with SHC commands. This page gives, for each certificate or credential, the commands that apply it and the components that they restart.

!!! warning "Plan a maintenance window"
    These procedures restart platform components. `PlatformInstallation` restarts the secret operator of the platform each time it runs, and redeploys every component whose deployed state differs from the configuration. `RestartAllMicroservices` restarts every microservice of the platform. `K3SInstall` restarts the K3s service of the nodes, one node at a time.

## Prerequisites

- The platform is installed and the SHC can retrieve its kubeconfig.
- The environment variables of the SHC are in a protected file that you load before each run, as described in [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md).

## Renew the platform certificate

Traefik serves one certificate on HTTPS (port 443) and on the syslog (port 10514) and RELP (port 11514) intake ports. The SHC reads this certificate and its private key from the `TRAEFIK_PUBKEY` and `TRAEFIK_PRIVKEY` environment variables. The new certificate must meet the conditions described in [TLS certificate](/self_hosted/1.0.1/deployment/deployment_configuration.md#tls-certificate).

1. To load the new certificate and its private key, run:

    ```bash
    export TRAEFIK_PUBKEY="$(cat /path/to/new-certificate.pem)"
    export TRAEFIK_PRIVKEY="$(cat /path/to/new-private-key.pem)"
    ```

    If you keep these variables in a protected file, update the file and load it instead.

2. To regenerate the platform configuration and apply it, run:

    ```bash
    exec PlatformConfigurationFile
    exec PlatformInstallation
    ```

    `PlatformInstallation` compares each component with the configuration. It redeploys Traefik with the new certificate in the `traefik-self-hosted-cert-secret` secret of the `kube-system` namespace. It also updates the `ca-bundle` ConfigMap, which holds the certificate chain that the platform services trust, in the `common`, `inthreat`, `support`, `symphony`, and `symphony-runtime` namespaces.

3. To check the certificate served on each port, run the following commands, with the value of `global.host`:

    ```bash
    for PORT in 443 10514 11514; do
      echo "Port $PORT"
      openssl s_client -connect <global.host>:$PORT -servername <global.host> </dev/null 2>/dev/null \
        | openssl x509 -noout -subject -enddate
    done
    ```

    Expected output: the subject and the expiry date of the new certificate, for each port.

If a port still serves the previous certificate, check the certificate of the secret, then the Traefik logs:

```bash
kubectl get secret -n kube-system traefik-self-hosted-cert-secret -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -enddate
kubectl logs -n kube-system -l app=traefik --prefix --tail=200
```

The `console` and `ingest` diagnostics also check the configured and the served certificates. To run them, enter `exec Diagnostic --set modules.diagnostic.targets=console,ingest`.

## Rotate the credentials

| Credential | Where you set it | Applied by | Restarted components |
| :--- | :--- | :--- | :--- |
| Platform storage keys | `STORAGE_S3_ACCESS_KEY`, `STORAGE_S3_SECRET_KEY` | `PlatformInstallation`, then `RestartAllMicroservices` | Microservices. ClickHouse server pods, when the ClickHouse backups are enabled with the default backup credentials. |
| SMTP server settings | `modules.platform_configuration.config.email.smtp.*` | `PlatformInstallation`, then `RestartAllMicroservices` | Microservices. |
| Backup S3 credentials, when they differ from the platform storage keys | `modules.platform_configuration.config.backups.s3.access_key`, `modules.platform_configuration.config.backups.s3.secret_key` | `PlatformInstallation` | ClickHouse server pods. |
| OCI registry credentials of the nodes | `REGISTRY_USERNAME`, `REGISTRY_PASSWORD` | `K3SInstall` | K3s service of each node. |
| Git and OCI registry credentials of ArgoCD | `GIT_HTTP_USERNAME`, `GIT_HTTP_PASSWORD`, `REGISTRY_USERNAME`, `REGISTRY_PASSWORD` | Not applied by the SHC. See [Credentials that you cannot rotate with the SHC](#credentials-that-you-cannot-rotate-with-the-shc). | None. |
| SSH key and sudo password of the nodes | `SERVERS_SSH_KEY`, `SERVERS_SUDO_PASSWORD` | The next SHC command. Only the SHC uses them. | None. |

The SHC itself reads the registry and Git credentials from its configuration at each run: `PushImages`, `PushCharts`, `PushDataBundles`, and `PushArgoStacks` use the new values at their next run.

### Rotate a credential stored in Vault

This procedure applies to the platform storage keys, the SMTP server settings, and the backup S3 credentials. The platform installer stores these values in Vault. Each run of `PlatformInstallation` writes the values of your configuration to Vault, replacing the previous ones, then restarts the secret operator, which refreshes the Kubernetes secrets of the platform from Vault. The platform services read these secrets when they start.

1. Create the new credential with your provider, and keep the previous one valid until the end of this procedure. For the platform storage, give the new key the same permissions on the event buckets and on the backup bucket.
2. Update the environment variable or the `config.yml` field, then load your environment variables.
3. To regenerate the platform configuration and apply it, run:

    ```bash
    exec PlatformConfigurationFile
    exec PlatformInstallation
    ```

4. For the platform storage keys and the SMTP server settings, restart the microservices so that they read the new values:

    ```bash
    exec RestartAllMicroservices
    ```

    Skip this step when you only changed the backup S3 credentials: `PlatformInstallation` already restarted the ClickHouse server pods.

5. To check the platform services, run `exec Diagnostic`. Every check reports `OK`.
6. When the backups are enabled, run `exec Backups -m run_now`, then `exec Backups` once the backups are complete. Every component reports `fresh`.
7. Revoke the previous credential with your provider.

### Restart the microservices

`RestartAllMicroservices` restarts every Deployment, StatefulSet, and DaemonSet that carries the `io.sekoia.microservice` label or annotation, in every namespace, and waits up to 300 seconds in total for their rollouts. The databases carry no such marker: the command leaves them running.

The command fails, and lists the affected workloads, when a workload has a paused, `OnDelete`, or partitioned rollout, which it does not restart, or when a rollout does not complete within 300 seconds.

### Rotate the registry credentials of the nodes

The nodes pull the container images from your registry with the credentials of the `/etc/rancher/k3s/registries.yaml` file. `K3SInstall` renders this file on every node.

!!! warning "Do not run K3SInstall in verbose mode"
    With `-v`, `K3SInstall` logs the OCI registry password in clear text, in the terminal and in the run log file of the SHC.

1. Create the new registry credential, with push, pull, and delete permissions on the registry project, and keep the previous one valid.
2. Update `REGISTRY_USERNAME` and `REGISTRY_PASSWORD`, then load your environment variables.
3. To write the new credential on the nodes, run:

    ```bash
    exec K3SInstall
    ```

    On each node where `registries.yaml` changes, the command restarts the `k3s` service of the manager nodes or the `k3s-agent` service of the worker nodes, one node at a time, and waits until the service is back.

ArgoCD keeps using the previous credential to read the Helm charts. Do not revoke it before you read [Credentials that you cannot rotate with the SHC](#credentials-that-you-cannot-rotate-with-the-shc).

## Credentials that you cannot rotate with the SHC

| Credential | Behavior | What to do |
| :--- | :--- | :--- |
| Git and OCI registry credentials of ArgoCD | ArgoCD registers your Git repository and your Helm chart repositories with the credentials used at installation. `PlatformInstallation` writes the new values to Vault, but does not register them in ArgoCD again while ArgoCD runs and its repositories have the expected settings. ArgoCD keeps the previous credentials, and can no longer read the stacks or the charts once you revoke them. | Contact Sekoia support before you revoke the previous credentials. |
| Backup encryption keys in use | `PlatformInstallation` stops, and writes no secret, when `BACKUP_ARANGO_CRYPT_KEY` or `BACKUP_CLICKHOUSE_CRYPT_KEY` differs from the key in use. The error reads `cannot replace an established Arango backup encryption key` or `cannot replace an established ClickHouse backup encryption key`. It does not check `BACKUP_VAULT_CRYPT_KEY`. | Keep the three keys unchanged. See [Back up the platform](/self_hosted/1.0.1/operations/backups.md#prepare-the-encryption-keys). |
| Sekoia release bucket credentials | Sekoia issues `S3_ACCESS_KEY` and `S3_SECRET_KEY`. Only the SHC uses them, to download the release, the content bundles, and the CTI database. | To change them, contact Sekoia. When Sekoia provides new ones, update the two variables. |

## Related links

- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md#tls-certificate): Certificate conditions and environment variables of the SHC.
- [Back up the platform](/self_hosted/1.0.1/operations/backups.md): Backup S3 credentials and encryption keys.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Check the certificate and the platform services after a rotation.
- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script): Pass the environment variables to the SHC container.
