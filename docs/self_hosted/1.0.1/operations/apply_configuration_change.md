# Apply a configuration change

To change an installed Sekoia Self-Hosted platform, edit the `config.yml` file of the self-hosted-controller (SHC), then run `Install` again. `Install` is idempotent. Each run converges the platform to the state declared in `config.yml`. It keeps what already matches and applies only the differences.

This page describes the general procedure. Use it for every change that has no dedicated procedure, for example a new SMTP server, a new proxy, a new worker replica count, or a sizing override.

!!! warning "Plan a maintenance window: Install restarts K3s"
    A run of `Install` on an installed platform runs `K3SInstall` again. This module restarts the K3s service on every node where the K3s files changed: the service unit, the registry configuration, or the proxy settings. It restarts one node at a time and waits for the service to be back before it moves to the next node. The first run of `Install` after the initial installation always restarts K3s on the first manager node. This run replaces the unit used to initialize the cluster with the standard unit. When `modules.k3s_install.reboot_after_install` is `true`, the nodes reboot instead. `PlatformInstallation` also restarts the secret operator of the platform each time it runs. It redeploys every component whose deployed state differs from the configuration.

!!! tip "Use the dedicated procedure when one exists"
    Some changes have a shorter procedure. It runs only the modules they need, without the K3s stage. Follow it instead of this page for the [platform certificate and the credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md), the [backups](/self_hosted/1.0.1/operations/backups.md#apply-the-configuration), and the [detection rules and intake formats](/self_hosted/1.0.1/operations/update_security_content.md).

## Prerequisites

- The platform is installed and healthy: `exec Diagnostic` reports `OK` for every check. Fix the current issues first, so that a failure of the run has one cause.
- You run the SHC from the orchestration node, with the execution script and the environment variables described in [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script).
- The release files and the security content bundles are still extracted in `$SEKOIA_LOCAL_DIR`, or the online mode credentials are set. `Install` validates the release files again. It also publishes the images, the charts, and the bundles again.
- `global.version.platform.version` keeps its current value. The SHC does not yet upgrade or roll back the platform automatically, and 1.0.1 is currently the only release of Sekoia Self-Hosted.
- No other SHC session is installing or updating the platform. See [Interrupted Helm operations](/self_hosted/1.0.1/deployment/deployment_process.md#interrupted-helm-operations).

## Change the configuration and run Install

1. Edit `config.yml`, or the protected file that holds the environment variables referenced by `config.yml`.

    To find the key and the format of a setting, run `config help <PREFIX>`, for example `config help modules.platform_configuration.config.email`. The required fields and the most common optional settings are described in [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md).

    !!! note "Runtime overrides are not configuration changes"
        A value passed with `exec <MODULE> --set KEY=VALUE` applies to that run only. It is never written to `config.yml`. The next run of `Install` applies the value of `config.yml` again. Write a durable change in `config.yml`.

2. Restart the SHC so that it reads the new values.

    The SHC reads `config.yml` once, when it starts. It resolves the `${env.VARIABLE}` references at the same time. In one-shot CLI mode, each `./run-shc.sh <command>` starts a new SHC and reads the current values. In the interactive interface, the values are the ones read when you opened it. Quit the interface and open it again after the change. When you changed an environment variable, load the protected file again before you start the SHC.

3. To validate the new configuration without changing the platform, run:

    ```bash
    exec CheckLocalConfig
    ```

    The command reports a missing required field, an invalid format, or an unsupported key. It names the key without printing its value. It does not validate every optional setting, so an incorrect optional value can stop `Install` in a later stage. To check a resolved value, run `config show <PREFIX>` on a section that holds no secret. See [Inspect the configuration with the SHC](/self_hosted/1.0.1/deployment/deployment_configuration.md#inspect-the-configuration-with-the-shc).

4. To apply the configuration, run:

    ```bash
    exec Install
    ```

    The command runs the four stages of the [installation execution plan](/self_hosted/1.0.1/deployment/deployment_process.md#the-installation-execution-plan), in order. It stops at the first module that fails. The run has completed when the `Install.start terminated` message reports `success=True`. Warning-level messages can appear while the run makes progress. Investigate only when a module fails or stops making progress.

    !!! note "Credentials in the run log"
        `PlatformAccess` prints the instance-administrator credentials in the output. In the interactive interface, it also writes them to the run log file.

5. If a module fails, fix the cause reported in the log. Then run `exec Install` again. Nothing is rolled back. The work done by the completed modules is kept. The next run applies only the differences that remain. See [Resume after a failure](/self_hosted/1.0.1/deployment/deployment_process.md#resume-after-a-failure).

6. Some values are read by the platform services only when they start, for example the SMTP server settings or the platform storage keys. When you changed one of them, restart the microservices:

    ```bash
    exec RestartAllMicroservices
    ```

    The command restarts every microservice of the platform and waits for their rollouts. The databases keep running. The settings that need this restart are listed in [Rotate the credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md#rotate-the-credentials).

7. To check the platform, run:

    ```bash
    exec DebugArgoCD
    exec Diagnostic
    ```

    Every ArgoCD application reports `Sync: Synced` and `Health: Healthy`. Every diagnostic check reports `OK`. `Progressing` is normal for a few minutes after the run.

### Result

The platform runs with the values declared in `config.yml`. K3s restarted on the nodes whose K3s files changed. The components whose configuration changed were redeployed. The other components kept running. A further run of `Install` with the same `config.yml` changes nothing on the platform.

## Changes that Install does not apply

The SHC rejects the following changes, or does not apply them with a run of `Install`.

| Change | Behavior | What to do |
| :--- | :--- | :--- |
| Backup encryption keys in use | `PlatformInstallation` stops when `BACKUP_ARANGO_CRYPT_KEY` or `BACKUP_CLICKHOUSE_CRYPT_KEY` differs from the key in use. | Keep the keys unchanged. See [Back up the platform](/self_hosted/1.0.1/operations/backups.md#prepare-the-encryption-keys). |
| Smaller database storage size | CloudNativePG cannot shrink a volume. | Set a value equal to or larger than the current size. See [Database storage](/self_hosted/1.0.1/deployment/deployment_configuration.md#database-storage). |
| Playbook library bundle | The bundle is downloaded in online mode. It is not published or applied after the installation. | None in 1.0.1. See [Update the security content](/self_hosted/1.0.1/operations/update_security_content.md). |
| Platform release | The SHC does not yet upgrade or roll back the platform automatically. | Keep `global.version.platform.version` unchanged: 1.0.1 is currently the only release. |

## Related links

- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md): Reference of the configuration fields and of the SHC configuration commands.
- [The deployment process](/self_hosted/1.0.1/deployment/deployment_process.md): Installation execution plan, idempotency, and resume after a failure.
- [Rotate the certificate and credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md): Dedicated procedures for the certificate and the credentials, and the components they restart.
- [Back up the platform](/self_hosted/1.0.1/operations/backups.md): Dedicated procedure to enable or change the backups.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Check the platform services after the run.
