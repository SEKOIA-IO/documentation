# Apply a patch release

A patch release fixes issues in a minor version of Sekoia Self-Hosted, for example 1.0.2 for 1.0. To apply it to an installed platform, you extract its archive, load its self-hosted-controller (SHC), set the new release in `config.yml`, and run `Install`.

This procedure applies to every patch release of 1.0, from any earlier patch release of 1.0. A patch release adds no feature, configuration key, or CLI command: your `config.yml` stays valid, and the procedures of this documentation stay the same. The [release notes](/self_hosted/1.0/release_notes.md#patch-releases) list the fixes and the updated components of each patch release.

!!! warning "Plan a maintenance window: Install restarts K3s"
    `Install` runs every stage of the installation again. It restarts the K3s service on the nodes where the K3s files changed, restarts the secret operator of the platform, and redeploys the components updated by the patch release. See [Apply a configuration change](/self_hosted/1.0/operations/apply_configuration_change.md).

## Prerequisites

- The platform is installed and healthy: `exec Diagnostic` reports `OK` for every check. Fix the current issues first, so that a failure of the run has one cause.
- You have the credentials of the Sekoia release bucket, as for the [initial download](/self_hosted/1.0/deployment/deployment_guide.md#step-1-download-and-verify-the-release-archive).
- The orchestration node has 220 GB of free disk space for the new archive and its extracted files, in addition to the current release. See [Orchestration node requirements](/self_hosted/1.0/deployment/deployment_prerequisites.md#orchestration-node-requirements).
- You run the SHC from the orchestration node, with the execution script and the environment variables described in [Deploy the platform](/self_hosted/1.0/deployment/deployment_guide.md#step-4-create-the-execution-script).
- No other SHC session is installing or updating the platform. See [Interrupted Helm operations](/self_hosted/1.0/deployment/deployment_process.md#interrupted-helm-operations).

## Apply the patch release

1. Set the patch release to apply, for example:

    ```bash
    export SH_VERSION="v1.0.2"
    ```

2. Download and verify the archive of this release. Follow [Step 1: Download and verify the release archive](/self_hosted/1.0/deployment/deployment_guide.md#step-1-download-and-verify-the-release-archive) of the deployment guide.

3. Transfer the archive to the orchestration node and extract it in the same `$SEKOIA_LOCAL_DIR` as the current release. Follow [Step 2: Transfer and extract the archive](/self_hosted/1.0/deployment/deployment_guide.md#step-2-transfer-and-extract-the-archive).

    The new release files land in `$SEKOIA_LOCAL_DIR/platform/$SH_VERSION/`, next to the files of the current release. The extraction also adds the security content bundles of the archive to `$SEKOIA_LOCAL_DIR/data/<TYPE>/` and replaces the `latest` files with the bundles it contains.

4. Load the SHC image of the new release and tag it `v1.0`. Follow [Step 3: Load the self-hosted-controller (SHC) Docker image](/self_hosted/1.0/deployment/deployment_guide.md#step-3-load-the-self-hosted-controller-shc-docker-image).

    !!! warning "Load the new SHC before you run Install"
        Each SHC only accepts the releases it supports. The SHC of an earlier patch release rejects the new release with an `UnsupportedReleaseError`.

    The `v1.0` tag moves to the new image, so the execution script `run-shc.sh` stays unchanged. To confirm, run `docker images sekoialab/self-hosted-controller-cli`: the `v1.0` tag has the same image ID as the image that you loaded.

5. In `config.yml`, set `global.version.platform.version` to the new release:

    ```yaml
    global:
      version:
        platform:
          version: "v1.0.2"
    ```

6. Start the SHC so that it reads the new value, then validate the configuration:

    ```bash
    exec CheckLocalConfig
    config show global.version.platform.version
    ```

    In the interactive interface, quit the interface and open it again after you edit `config.yml`. In one-shot CLI mode, each `./run-shc.sh <command>` reads the current file.

7. To apply the release, run:

    ```bash
    exec Install
    ```

    The run has completed when the `Install.start terminated` message reports `success=True`. In air-gapped mode, `DownloadReleaseFiles` uses the extracted files of the new release. In online mode, it downloads them from the Sekoia release bucket. The run also publishes and applies the detection rules and intake formats bundles named in the local `latest` files.

8. If a module fails, fix the cause reported in the log, then run `exec Install` again. Nothing is rolled back, and the next run applies only the differences that remain. See [Resume after a failure](/self_hosted/1.0/deployment/deployment_process.md#resume-after-a-failure).

9. To check the platform, run:

    ```bash
    exec DebugArgoCD
    exec Diagnostic
    ```

    Every ArgoCD application reports `Sync: Synced` and `Health: Healthy`. Every diagnostic check reports `OK`. `Progressing` is normal for a few minutes after the run.

### Result

The platform runs the new patch release. The components listed for this release in the [release notes](/self_hosted/1.0/release_notes.md#patch-releases) were redeployed, and the platform keeps its data and its configuration.

!!! note "No automatic rollback"
    The SHC does not roll back the platform to an earlier release. If the platform does not reach a healthy state after the run, contact Sekoia support.

## Related links

- [Release notes v1.0](/self_hosted/1.0/release_notes.md#patch-releases): Fixes and updated components of each patch release.
- [Deploy the platform](/self_hosted/1.0/deployment/deployment_guide.md): Download, extraction, and SHC image steps that this procedure reuses.
- [Apply a configuration change](/self_hosted/1.0/operations/apply_configuration_change.md): What a run of `Install` restarts on an installed platform.
- [The deployment process](/self_hosted/1.0/deployment/deployment_process.md): Installation execution plan, idempotency, and resume after a failure.
- [Run platform diagnostics](/self_hosted/1.0/monitoring/run_diagnostics.md): Check the platform services after the run.
