# Import the CTI database

The self-hosted-controller (SHC) imports the Sekoia CTI database into the ArangoDB database of your platform with the `ImportArangoCollection` command. It reads the latest CTI export from the Sekoia release bucket in online mode, or from the orchestration node in air-gapped mode, and loads the STIX objects and relationships it contains.

The imported database feeds observable tags enrichment, contextualized alerts, and the `SEKOIA Intelligence Feed` detection rule. The Intelligence module is not available in Sekoia Self-Hosted 1.0.0.

## Prerequisites

- The platform is installed and the SHC can retrieve its kubeconfig.
- In online mode, the `S3_ACCESS_KEY` and `S3_SECRET_KEY` environment variables hold the Sekoia release bucket credentials provided by Sekoia, and `global.version.fetch` points to the Sekoia release bucket, as described in [Configure the deployment](../deployment/deployment_configuration.md#release-download-and-security-content).
- In air-gapped mode, `global.version.fetch.offline` is `true` and the CTI archive is extracted on the orchestration node, as described in [Prepare the CTI export in air-gapped mode](#prepare-the-cti-export-in-air-gapped-mode).

## Prepare the CTI export in air-gapped mode

The release archive does not include the CTI database. Sekoia publishes it as a separate archive in the release bucket, every day at 12:00 UTC: `data/cti/archives/cti-latest.tar`, with its SHA-256 checksum. The archive is an uncompressed `.tar` file that holds the latest export of each collection.

1. On a machine with internet access, download the archive and its checksum with the bucket credentials provided by Sekoia, then verify its integrity. Keep the `cti-latest.tar` file name: the checksum file refers to it.

    ```bash
    export AWS_ACCESS_KEY_ID=""
    export AWS_SECRET_ACCESS_KEY=""
    export AWS_DEFAULT_REGION="fr-par-2"
    export ENDPOINT="https://self-hosted.delivery.sekoia.io"
    export AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    export AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED

    aws --endpoint-url "$ENDPOINT" s3 cp s3://self-hosted/data/cti/archives/cti-latest.tar cti-latest.tar
    aws --endpoint-url "$ENDPOINT" s3 cp s3://self-hosted/data/cti/archives/cti-latest.tar.sha256 cti-latest.tar.sha256

    sha256sum -c cti-latest.tar.sha256
    ```

    Expected output: `cti-latest.tar: OK`

2. To transfer the archive to the orchestration node, run:

    ```bash
    scp cti-latest.tar user@<ORCHESTRATION_NODE>:$SEKOIA_LOCAL_DIR
    ```

    !!! note "Disk space"
        The parts of the export are already compressed, so the extracted files take about as much space as the archive. Before you transfer it, make sure the orchestration node has free space for twice the size of the archive. You can delete the archive once it is extracted.

3. To extract the archive on the orchestration node, run:

    ```bash
    tar -xf $SEKOIA_LOCAL_DIR/cti-latest.tar -C $SEKOIA_LOCAL_DIR
    ```

The archive extracts to `$SEKOIA_LOCAL_DIR/data/cti/`, with one directory per collection. Each directory holds a `latest.json` file that names the export to import, and the export folder itself:

```text
$SEKOIA_LOCAL_DIR/data/cti/
├── stix_objects/
│   ├── latest.json
│   └── <export ID>/
│       ├── checkpoint.json
│       └── part-<N>.jsonl.zst
└── stix_relationships/
    ├── latest.json
    └── <export ID>/
        ├── checkpoint.json
        └── part-<N>.jsonl.zst
```

The SHC reads each collection from `<global.version.data.cti.path>/cti/<collection>/`. The [execution script](../deployment/deployment_guide.md#step-4-create-the-execution-script) mounts `$SEKOIA_LOCAL_DIR` on `/opt/sekoia`, which matches the default value of `global.version.data.cti.path` (`/opt/sekoia/data/`).

## Import the CTI database

!!! tip "Safe to run again"
    The import updates the documents that already exist. If an import fails, run the command again.

To import the CTI database, run:

```bash
exec ImportArangoCollection
```

The SHC reads the ArangoDB root password of the platform from the `arangodb-operator-dashboard` secret of the `support` namespace. You do not pass it to the SHC. To use another password or another secret, set the following optional fields in `config.yml`:

| Field | Description | Default |
| :--- | :--- | :--- |
| `utils.arango.password` | ArangoDB password. When set, the SHC does not read the secret. | Empty |
| `utils.arango.password_secret.namespace` | Namespace of the secret holding the ArangoDB password. | `support` |
| `utils.arango.password_secret.name` | Name of the secret. | `arangodb-operator-dashboard` |
| `utils.arango.password_secret.key` | Key of the password in the secret. | `password` |

## Select a CTI version

By default, the command imports the latest CTI export. To import another export, set `global.version.data.cti.version`:

| Value | Imported export |
| :--- | :--- |
| `latest` | The latest completed export. This is the default. |
| A day, for example `2026-09-03` | The most recent completed export of that day, for each collection. |
| An exact export, for example `2026-09-03T09` | The export of that ID, for every collection. The SHC refuses it unless its checkpoint shows a completed export. |

For example, to import the export of a given day for one run:

```bash
exec ImportArangoCollection --set global.version.data.cti.version=2026-09-03
```

In air-gapped mode, the SHC only finds the exports extracted on the orchestration node, and `cti-latest.tar` holds the latest export only. To import an older export, download the dated archive of that day, `data/cti/archives/cti-<YYYY-MM-DD>.tar`, instead of `cti-latest.tar`, and keep `latest`. The release bucket keeps the dated archives of the last 10 days.

## Update the CTI database

The import is a snapshot: the CTI database of your platform does not update on its own. To refresh it, run the import again. In air-gapped mode, download and extract a new archive first.

## Result

The command logs an `Import progress` line for each part it loads, then a summary of the documents created and updated per collection. Once every collection is imported, it deletes the relationships whose source or target object is missing from the database, and logs their count.

If a collection fails, the command still imports the other ones, skips the deletion of the relationships, and lists every failure at the end.

## Related links

- [Use the SHC interface](./controller_interface.md): Run SHC commands and runtime overrides.
- [Configure the deployment](../deployment/deployment_configuration.md): Set the release bucket credentials and endpoint.
- [Deploy the platform](../deployment/deployment_guide.md): Download the release and prepare the SHC execution script.
