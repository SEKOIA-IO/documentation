# Rotate the certificate and credentials

You renew the platform certificate and rotate the credentials of your services by updating the environment variables or the `config.yml` file of the self-hosted-controller (SHC), then applying them with SHC commands. This page gives, for each certificate or credential, the commands that apply it and the components that they restart.

!!! warning "Plan a maintenance window"
    These procedures restart platform components. `PlatformInstallation` restarts the secret operator of the platform each time it runs, and redeploys every component whose deployed state differs from the configuration. `RestartAllMicroservices` restarts every microservice of the platform. `K3SInstall` restarts the K3s service of the nodes, one node at a time.

## Prerequisites

- The platform is installed and the SHC can retrieve its kubeconfig.
- The environment variables of the SHC are in a protected file that you load before each run, as described in [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md).

!!! note "Restart the SHC after changing a value"
    The SHC reads `config.yml` and resolves its `${env.VARIABLE}` references once, when it starts. An open interactive interface keeps the previous values. After a change, quit the interface, load the updated environment variables in the shell that starts the SHC, then open the interface again before running the commands below. If you store the variables in a protected file, load that file again before restarting the SHC. In one-shot CLI mode, each `./run-shc.sh <command>` starts a new SHC with the current configuration and the environment of the launching shell.

## Renew the platform certificate

Traefik serves one certificate on HTTPS (port 443) and on the syslog (port 10514) and RELP (port 11514) intake ports. The SHC reads this certificate and its private key from the `TRAEFIK_PUBKEY` and `TRAEFIK_PRIVKEY` environment variables. The new certificate must meet the conditions described in [TLS certificate](/self_hosted/1.0.1/deployment/deployment_configuration.md#tls-certificate).

1. In the shell that starts the SHC, load the new certificate and its private key:

    ```bash
    export TRAEFIK_PUBKEY="$(cat /path/to/new-certificate.pem)"
    export TRAEFIK_PRIVKEY="$(cat /path/to/new-private-key.pem)"
    ```

    If you keep these variables in a protected file, update the file and load it instead. Quit any open SHC interface and open it again from this shell before the next step.

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
| Git and OCI registry credentials of ArgoCD | `GIT_HTTP_USERNAME`, `GIT_HTTP_PASSWORD`, `REGISTRY_USERNAME`, `REGISTRY_PASSWORD` | `PlatformConfigurationFile`, then `PlatformInstallation` | None. ArgoCD registers the repositories again with the new credentials. |
| SSH key and sudo password of the nodes | `SERVERS_SSH_KEY`, `SERVERS_SUDO_PASSWORD` | The next SHC command after restarting the SHC. Only the SHC uses them. | None. |

After the SHC has restarted with the updated configuration, `PushImages`, `PushCharts`, `PushDataBundles`, and `PushArgoStacks` use the new registry and Git credentials at their next run.

### Rotate a credential stored in Vault

This procedure applies to the platform storage keys, the SMTP server settings, and the backup S3 credentials. The platform installer stores these values in Vault. Each run of `PlatformInstallation` writes the values of your configuration to Vault, replacing the previous ones, then restarts the secret operator, which refreshes the Kubernetes secrets of the platform from Vault. The platform services read these secrets when they start.

1. Create the new credential with your provider, and keep the previous one valid until the end of this procedure. For the platform storage, give the new key the same permissions on the event buckets and on the backup bucket.
2. Update the environment variable or the `config.yml` field. Quit any open SHC interface, load the updated environment variables in the shell that starts the SHC, then open the interface again before the next step.
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

### Rotate the Git and registry credentials

The registry credentials are used in two places. The nodes pull the container images with the credentials of the `/etc/rancher/k3s/registries.yaml` file, which `K3SInstall` renders on every node. ArgoCD reads the Helm charts from your registry, and the ArgoCD stacks from your Git repository, with the credentials registered for each repository. Each run of `PlatformInstallation` writes the credentials of your configuration to Vault, compares them with the credentials registered in ArgoCD, and registers the repositories again when they differ.

!!! tip "Apply everything in one run"
    `exec Install` runs `K3SInstall`, `PlatformConfigurationFile`, and `PlatformInstallation` in one run, with the K3s restarts described in [Apply a configuration change](/self_hosted/1.0.1/operations/apply_configuration_change.md).

1. Create the new credential, and keep the previous one valid. A registry credential needs push, pull, and delete permissions on the registry project.
2. Update `REGISTRY_USERNAME` and `REGISTRY_PASSWORD`, or `GIT_HTTP_USERNAME` and `GIT_HTTP_PASSWORD`. Quit any open SHC interface, load the updated environment variables in the shell that starts the SHC, then open the interface again before the next step.
3. For a registry credential, to write it on the nodes, run:

    ```bash
    exec K3SInstall
    ```

    On each node where `registries.yaml` changes, the command restarts the `k3s` service of the manager nodes or the `k3s-agent` service of the worker nodes, one node at a time, and waits until the service is back.

4. To register the new credentials in ArgoCD, run:

    ```bash
    exec PlatformConfigurationFile
    exec PlatformInstallation
    ```

    `PlatformInstallation` stops when ArgoCD rejects a repository registration, for example with `ArgoCD rejected the Git repository registration`, or when the registered credentials still differ from Vault after the registration, with `ArgoCD repository configuration did not converge`. Check the new credential, then run the two commands again.

5. Revoke the previous credential with your provider.
6. A few minutes later, to check that ArgoCD reads the stacks and the charts with the new credential, run `exec DebugArgoCD`. Every application reports `Sync: Synced` and `Health: Healthy`.

## Credentials that you cannot rotate with the SHC

| Credential | Behavior | What to do |
| :--- | :--- | :--- |
| Backup encryption keys in use | `PlatformInstallation` stops, and writes no secret, when `BACKUP_ARANGO_CRYPT_KEY` or `BACKUP_CLICKHOUSE_CRYPT_KEY` differs from the key in use. The error reads `cannot replace an established Arango backup encryption key` or `cannot replace an established ClickHouse backup encryption key`. It does not check `BACKUP_VAULT_CRYPT_KEY`. | Keep the three keys unchanged. See [Back up the platform](/self_hosted/1.0.1/operations/backups.md#prepare-the-encryption-keys). |
| Sekoia release bucket credentials | Sekoia issues `S3_ACCESS_KEY` and `S3_SECRET_KEY`. Only the SHC uses them, to download the release, the content bundles, and the CTI database. | To change them, contact Sekoia. When Sekoia provides new ones, update the two variables. |

## Related links

- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md#tls-certificate): Certificate conditions and environment variables of the SHC.
- [Back up the platform](/self_hosted/1.0.1/operations/backups.md): Backup S3 credentials and encryption keys.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Check the certificate and the platform services after a rotation.
- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script): Pass the environment variables to the SHC container.
