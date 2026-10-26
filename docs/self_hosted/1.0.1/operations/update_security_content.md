# Update the security content

The self-hosted-controller (SHC) updates the detection rules and the intake formats of an installed platform with the `UpdatePlatformData` command. It publishes the selected content bundles to your OCI registry, points the content updaters of the platform to them, and waits until the updaters have loaded them.

!!! note "Playbook library and CTI database"
    In Sekoia Self-Hosted 1.0.1, you cannot update the playbook library after the installation: `UpdatePlatformData` downloads its bundle in online mode, but does not publish or apply it. The CTI database has its own procedure, described in [Import the CTI database](/self_hosted/1.0.1/operations/import_cti_database.md).

## Prerequisites

- The platform is installed and the SHC can retrieve its kubeconfig.
- The release files are extracted on the orchestration node: the command publishes the ArgoCD stacks of the release again.
- In online mode, the `S3_ACCESS_KEY` and `S3_SECRET_KEY` environment variables hold the Sekoia release bucket credentials provided by Sekoia, and `global.version.fetch.endpoint` points to the Sekoia release bucket, as described in [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md#release-download-and-security-content).
- In air-gapped mode, `global.version.fetch.offline` is `true` and the bundles are on the orchestration node, as described in [Prepare the bundles in air-gapped mode](#prepare-the-bundles-in-air-gapped-mode).

## What the command does

`UpdatePlatformData` runs the following modules in order, and stops at the first failure:

1. `DownloadDataFiles`, in online mode only. For each bundle type, it downloads the bundle selected by `global.version.data.<TYPE>.version` to `<global.version.data.<TYPE>.path>/<TYPE>/`, unless the file is already there, and writes its file name to the local `latest` file. It keeps the three most recent archives of each type. It also downloads the playbook library bundle.
2. `PushDataBundles`. It pushes the detection rules and intake formats bundles named in the local `latest` files, with their signatures, to your registry: `<project>/images/sekoialab/rules-catalog-updater:<release ID>` and `<project>/images/sekoialab/intake-formats-updater:<release ID>`. It makes up to three attempts per bundle.
3. A verification. The command stops when a bundle is missing on the orchestration node, or when its tag is missing from your registry. At this point, nothing has changed on the platform.
4. `PushArgoStacks`. It sets the release ID of each bundle in the stack of its updater, publishes the stacks to your Git repository, and synchronizes the ArgoCD root application.
5. `SyncRulesCatalog` and `SyncIntakeFormats`. They synchronize the `rules-catalog-updater-on-self-hosted` and `intake-formats-updater-on-self-hosted` ArgoCD applications, and wait until the job that loads the content succeeds, for up to 900 seconds each.

## Select the bundles in online mode

In online mode, the SHC selects each bundle with the following fields:

| Field | Value | Default |
| :--- | :--- | :--- |
| `global.version.data.detection-rules.version` | `latest`, for the bundle named in the `latest` file of the release bucket, or the release ID of a bundle to pin. | `latest` |
| `global.version.data.intake-formats.version` | `latest`, for the bundle named in the `latest` file of the release bucket, or the release ID of a bundle to pin. | `latest` |

A daily Sekoia pipeline publishes the bundles in the release bucket, under `data/<TYPE>/`, and writes the file name of the most recent bundle to `data/<TYPE>/latest`. The release ID of a bundle is its file name without the `<TYPE>-` prefix and the `.tar.gz` extension.

`UpdatePlatformData` does not accept `--set` overrides: to pin a bundle, set its release ID in `config.yml`. For example:

```yaml
global:
  version:
    data:
      detection-rules:
        version: "2.20260813-31688094717-35a441d88ed9c2b23b078e476fb35a6c2a40df84"
```

When the selected bundle does not exist in the release bucket, `DownloadDataFiles` stops with `Data bundle not found`, before anything is published.

## Prepare the bundles in air-gapped mode

In air-gapped mode, the SHC downloads nothing and ignores the `version` fields. It uses the bundle named in the `latest` file of each `data/<TYPE>/` directory of the orchestration node.

1. On a machine with internet access, download the `latest` file of each type and the bundle that it names, with the bucket credentials provided by Sekoia:

    ```bash
    export AWS_ACCESS_KEY_ID=""
    export AWS_SECRET_ACCESS_KEY=""
    export AWS_DEFAULT_REGION="fr-par-2"
    export ENDPOINT="https://self-hosted.delivery.sekoia.io"
    export AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    export AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED

    for TYPE in detection-rules intake-formats; do
      mkdir -p "data/$TYPE"
      aws --endpoint-url "$ENDPOINT" s3 cp "s3://self-hosted/data/$TYPE/latest" "data/$TYPE/latest"
      aws --endpoint-url "$ENDPOINT" s3 cp "s3://self-hosted/data/$TYPE/$(cat "data/$TYPE/latest")" "data/$TYPE/"
    done
    ```

2. To transfer the bundles to the orchestration node, run:

    ```bash
    scp -r data user@<ORCHESTRATION_NODE>:$SEKOIA_LOCAL_DIR
    ```

The orchestration node then holds the following files:

```text
$SEKOIA_LOCAL_DIR/data/
├── detection-rules/
│   ├── latest
│   └── detection-rules-<release ID>.tar.gz
└── intake-formats/
    ├── latest
    └── intake-formats-<release ID>.tar.gz
```

Each `latest` file contains only the file name of the bundle to use, for example `detection-rules-2.20260813-31688094717-35a441d88ed9c2b23b078e476fb35a6c2a40df84.tar.gz`, and the bundle is in the same directory. The release ID uses letters, digits, `_`, `.`, and `-`, with at most 128 characters. When the `latest` file is missing, or names a file that does not follow this format or does not exist, the SHC skips the bundle with a warning. Older bundles can stay in the directory: the SHC only uses the one named in `latest`.

The SHC reads each type from `<global.version.data.<TYPE>.path>/<TYPE>/`. The [execution script](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script) mounts `$SEKOIA_LOCAL_DIR` on `/opt/sekoia`, which matches the default value of `global.version.data.<TYPE>.path` (`/opt/sekoia/data/`).

## Update the security content

!!! note "Other configuration changes are published too"
    `PushArgoStacks` generates every stack from your current `config.yml`. If you changed other settings since the last publication, the command publishes them too.

To update the detection rules and the intake formats, run:

```bash
exec UpdatePlatformData
```

## Result

For each updater, the command logs `Overriding updater release ID from registry-verified data bundle` with the `data_release_id` of the new bundle. Once the content is loaded, it logs `Data bundle updater sync complete` for `rules-catalog-updater-on-self-hosted` and `intake-formats-updater-on-self-hosted`.

When a bundle cannot be published, the command stops before it publishes the stacks, and the platform keeps the content already deployed:

| Message | Cause |
| :--- | :--- |
| `Data bundle not found` or `Missing 'latest' pointer` | Online mode only. The selected bundle, or the `latest` file of its type, does not exist in the release bucket. |
| `Data bundle unavailable: <TYPE>` | The `latest` file, or the bundle that it names, is missing or invalid on the orchestration node. |
| `Data bundle tag not published: <TYPE>:<release ID>` | The push of the bundle to your registry failed. The log shows the error of each attempt. |

When a synchronization fails or times out, the stacks already reference the new bundles. Inspect the updater application with `exec DebugArgoCD`, then run `UpdatePlatformData` again. To allow more time for a large catalog, set `modules.sync_rules_catalog.sync_timeout` or `modules.sync_intake_formats.sync_timeout` in `config.yml`, in seconds.

## Related links

- [Import the CTI database](/self_hosted/1.0.1/operations/import_cti_database.md): Import and refresh the Sekoia CTI database.
- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md#release-download-and-security-content): Set the release bucket and the bundle versions.
- [Deploy the platform](/self_hosted/1.0.1/deployment/deployment_guide.md): Install the security content shipped with the release.
- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): Inspect the ArgoCD applications of the updaters.
