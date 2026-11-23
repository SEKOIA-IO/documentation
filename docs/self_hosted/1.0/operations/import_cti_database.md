# Import the CTI database

The self-hosted-controller (SHC) imports the Sekoia CTI database into the ArangoDB database of your platform with the `ImportArangoCollection` command. It reads the latest CTI export from the Sekoia release bucket in online mode, or from the orchestration node in air-gapped mode, and loads the STIX objects and relationships it contains.

The imported database feeds contextualized alerts and the `SEKOIA Intelligence Feed` detection rule. It does not contain the observables and their tags, so observable tags enrichment is not available. The Intelligence module is not available in Sekoia Self-Hosted 1.0.

## Prerequisites

- The platform is installed and the SHC can retrieve its kubeconfig.
- In online mode, the `S3_ACCESS_KEY` and `S3_SECRET_KEY` environment variables hold the Sekoia release bucket credentials provided by Sekoia, and `global.version.fetch` points to the Sekoia release bucket, as described in [Configure the deployment](/self_hosted/1.0/deployment/deployment_configuration.md#release-download-and-security-content).
- In air-gapped mode, `global.version.fetch.offline` is `true` and both CTI collections are available locally on the orchestration node, as described in [Prepare the CTI export in air-gapped mode](#prepare-the-cti-export-in-air-gapped-mode).

## Prepare the CTI export in air-gapped mode

On a machine with internet access, use the AWS CLI, `jq`, and your Sekoia release bucket credentials to download both collections. Each collection's `latest.json` names its latest **completed** export. The run IDs can differ. Reading each pointer once keeps the download on the selected run even if Sekoia publishes another export during the copy.

Run this Bash snippet from a new, empty staging directory. Set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to the delivery credentials provided by Sekoia, or select an AWS CLI profile with those credentials.

```bash
(
    set -e
    export AWS_DEFAULT_REGION="fr-par-2"
    export AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    export AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED
    ENDPOINT="https://self-hosted.delivery.sekoia.io"

    for collection in stix_objects stix_relationships; do
        dir="data/cti/$collection"
        source="s3://self-hosted/$dir"
        mkdir -p "$dir"
        aws --endpoint-url "$ENDPOINT" s3 cp "$source/latest.json" "$dir/latest.json"
        run_id=$(jq -er --arg collection "$collection" '
            select(.collection == $collection and (.completed_at | type == "string" and length > 0))
            | .run_id | select(test("^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}$"))
        ' "$dir/latest.json")
        aws --endpoint-url "$ENDPOINT" s3 cp --recursive "$source/$run_id/" "$dir/$run_id/"
        test -s "$dir/$run_id/checkpoint.json"
    done
)
```

After both downloads succeed, transfer the staged `data/cti/` tree to the orchestration node using your air-gap transfer method. Copy the contents of the staging directory into `$SEKOIA_LOCAL_DIR/` to obtain the layout below. Keep the compressed parts and their names. For a refresh, copy both dated directories first, then replace each collection's local `latest.json` with the one from staging before starting the import.

```text
$SEKOIA_LOCAL_DIR/data/cti/
├── stix_objects/
│   ├── latest.json
│   └── <stix_objects run_id>/
│       ├── checkpoint.json
│       └── part-<N>.jsonl.zst
└── stix_relationships/
    ├── latest.json
    └── <stix_relationships run_id>/
        ├── checkpoint.json
        └── part-<N>.jsonl.zst
```

The SHC reads each collection from `<global.version.data.cti.path>/cti/<collection>/`. The [execution script](/self_hosted/1.0/deployment/deployment_guide.md#step-4-create-the-execution-script) mounts `$SEKOIA_LOCAL_DIR` on `/opt/sekoia`, which matches the default value of `global.version.data.cti.path` (`/opt/sekoia/data/`).

## Import the CTI database

!!! tip "Retry with the default import policy"
    With `modules.import_arango_collection.truncate=false` and `modules.import_arango_collection.on_duplicate=update` (the defaults), the import updates documents with the same `_key` without clearing the collections first. If an import fails, fix the reported cause, then run it again. Check the [import safety settings](#import-safety-and-tuning) before retrying with a custom configuration.

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

## Import safety and tuning

These settings apply to every collection in the import. Set them in `config.yml` and restart the SHC after editing, or override them for one run with `exec ImportArangoCollection --set KEY=VALUE`. Runtime overrides do not change `config.yml` or later runs.

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.import_arango_collection.truncate` | `true` clears each target collection before importing its parts. Keep `false` for routine updates and failure retries. | `false` |
| `modules.import_arango_collection.on_duplicate` | Policy for documents whose `_key` already exists: `update` merges the imported fields, `replace` replaces the document, `ignore` keeps the existing document, and `error` reports a duplicate as an import error. | `update` |
| `modules.import_arango_collection.threads` | Positive number of part files imported concurrently. Lower it to reduce memory use in the SHC and concurrent load on ArangoDB. | `8` |
| `modules.import_arango_collection.retries` | Maximum attempts per part file, including the first attempt, not additional retries. Must be at least `1`. | `5` |
| `modules.import_arango_collection.retry_backoff_seconds` | Non-negative base delay in seconds between failed attempts, doubled for each subsequent retry. | `2` |

For example, to reduce concurrent imports for one run:

```bash
exec ImportArangoCollection --set modules.import_arango_collection.threads=4
```

!!! warning "Truncation deletes existing data before the import succeeds"
    With `truncate=true`, the SHC clears each target collection that has parts to import before loading its first part. A failure can leave that collection empty or only partly imported. There is no rollback. Each new invocation clears the collections again; automatic retries of a part do not. Use truncation only for a planned full replacement, with Sekoia support and a verified ArangoDB backup. See [Back up the platform](/self_hosted/1.0/operations/backups.md). Do not leave `truncate=true` in the configuration for routine imports.

Imports are not atomic, even with truncation disabled. Successful writes remain when another part or collection fails. A retry re-reads the whole part and can encounter documents written by a previous attempt: `update` applies the imported fields again, while `error` can fail on those duplicates. A duplicate policy is not a rollback mechanism. Inspect the final per-part and per-collection errors before retrying; increasing the retry count does not repair invalid input documents.

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

In air-gapped mode, `latest` uses the two `latest.json` files you transferred. To import an older day, copy the completed dated directory for each collection from the bucket into its corresponding local collection directory, then select that day when running the import.

## Update the CTI database

The import is a snapshot: the CTI database of your platform does not update on its own. To refresh it, run the import again. In air-gapped mode, repeat the download and transfer steps for both collections first.

## Result

The command logs an `Import progress` line for each part it loads, then a summary of the documents created and updated per collection. Once every collection is imported, it deletes the relationships whose source or target object is missing from the database, and logs their count.

To confirm which export was imported, look for the `Resolved export run` log line of each collection. Its `location` field ends with the folder of the imported export, named after the export ID, an hourly timestamp such as `2026-09-03T09`. With `latest`, the line also gives the `run_id` and the `completed_at` time read from `latest.json`. With a pinned day, check that the folder name starts with that day.

If a collection fails, the command still imports the other ones, skips the deletion of the relationships, and lists every failure at the end.

## Related links

- [Use the SHC interface](/self_hosted/1.0/operations/controller_interface.md): Run SHC commands and runtime overrides.
- [Configure the deployment](/self_hosted/1.0/deployment/deployment_configuration.md): Set the release bucket credentials and endpoint.
- [Deploy the platform](/self_hosted/1.0/deployment/deployment_guide.md): Download the release and prepare the SHC execution script.
