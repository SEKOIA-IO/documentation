## Upgrade the platform

Use this procedure to upgrade an existing deployment with a separate configuration for the target version. Run `Install` in the SHC and select `upgrade` for the platform installer in that configuration.

## Prepare the target configuration

1. Use the existing `run-shc.sh` and load your credentials as described in the [deployment guide](/self_hosted/1.0/deployment/deployment_guide.md).
2. Keep the configuration used for the current version and copy it for the target version.

    ```bash
    cp "$HOME/config-v1.0.2.yaml" "$HOME/config-v1.1.0.yaml"
    ```

3. Edit the target file and apply the configuration changes required by the target release. The version numbers below are examples.

    | Configuration key | Current configuration | Target configuration |
    | --- | --- | --- |
    | `global.version.platform.version` | `v1.0.2` | `v1.1.0` |
    | `modules.platform_configuration.platform_installer_command` | `install` for the first installation | `upgrade` |

    Keep the site identity, node addresses, storage, Git repository, history directory, and deployment branch for the same environment. Preserve any inherited configuration files and the mount paths they require.

## Run the upgrade

!!! warning "One SHC instance per environment"
    Run only one self-hosted-controller (SHC) instance at a time against the same environment. Before starting an installation or upgrade, confirm that the previous SHC process and any platform-installer job it started have stopped. Concurrent runs can interfere with Helm operations.

1. Select the target configuration.

    ```bash
    export SEKOIA_CONFIG_FILE="$HOME/config-v1.1.0.yaml"
    ```

2. Check the version history and validate the target.

    ```bash
    ./run-shc.sh exec VersionsHistory
    ./run-shc.sh exec CheckVersion
    ```

3. Run the workflow and keep the terminal output.

    ```bash
    set -o pipefail
    ./run-shc.sh exec Install 2>&1 | tee upgrade-v1.1.0.log
    ```

4. Follow [Post-deployment validation](/self_hosted/1.0/deployment/deployment_guide.md#post-deployment-validation) to check the Kubernetes nodes, ArgoCD applications, databases, diagnostics, and platform access.
5. Confirm that `./run-shc.sh exec VersionsHistory` reports `success` for the target version.

## Diagnose and retry a failed upgrade

1. Identify the failed step in the saved terminal output and display the attempt details.

    ```bash
    ./run-shc.sh exec VersionsHistory --verbose
    ```

    The history includes the error, available logs from the failed step, and the archived configuration. Use the terminal log for the full output.

2. Run `./run-shc.sh exec DebugArgoCD`, `./run-shc.sh exec DebugDatabases`, or `./run-shc.sh exec Diagnostic` according to the failing component. For a pod failure, inspect its events and logs using the [debug guide](/self_hosted/1.0/troubleshooting/debug_tool.md).
3. Correct the cause and retry `Install` with the target configuration and `platform_installer_command: upgrade`.

A `check_failed` attempt leaves the minimum version unchanged. Once deployment reaches `in_progress`, its target becomes the minimum even if the attempt ends as `failed`. You can retry that version or install a newer one.

If an interruption leaves the attempt in `pending` or `in_progress`, first confirm that the original SHC process and any installer job have stopped. Then run `./run-shc.sh exec CheckVersion --reset` with the interrupted version selected and retry. The reset closes `pending` as `check_failed` and `in_progress` as `failed`.

## Related links

- [Deploy the platform](/self_hosted/1.0/deployment/deployment_guide.md) covers the first installation and post-deployment validation.
- [Configure the deployment](/self_hosted/1.0/deployment/deployment_configuration.md) describes the site configuration.
- [Debug your deployment](/self_hosted/1.0/troubleshooting/debug_tool.md) describes diagnostics, interrupted-run recovery, and support log collection.
