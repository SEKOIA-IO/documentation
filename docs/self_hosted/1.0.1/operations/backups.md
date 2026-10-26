# Back up the platform

The self-hosted-controller (SHC) configures scheduled backups of Vault, of every PostgreSQL database, of ArangoDB, and of ClickHouse to a bucket of your S3-compatible storage. The `Backups` command checks that recent backups exist in this bucket, and starts a backup on demand.

!!! warning "No restore procedure in Sekoia Self-Hosted 1.0.1"
    Sekoia Self-Hosted 1.0.1 provides no restore procedure, and the backups are not a tested restore path. The backup status checks the backup files in S3, not that you can restore them. To restore a component, contact Sekoia support.

## What the backups contain

| Component | Content | Default schedule | Retention | S3 prefix |
| :--- | :--- | :--- | :--- | :--- |
| Vault | Encrypted snapshot of the secrets store. | Every day at 23:00, in the time zone of the K3s server nodes | The 30 latest snapshots | `vault/` |
| PostgreSQL | Every CloudNativePG cluster, including the ExaLog metastore: a base backup, plus continuous archiving of the write-ahead log (WAL). | Every day at 00:01 UTC | 30 days | `postgres/` |
| ArangoDB | Encrypted dumps in a Borg repository. | Every day at 01:00, in the time zone of the K3s server nodes | Every archive of the last day, plus 7 daily, 4 weekly, and 1 monthly archives | `arangodb/` |
| ClickHouse | Encrypted backup chains: a full base backup each month, then incremental backups. | Every day at 02:00, in the time zone of the K3s server nodes | 3 monthly chains | `clickhouse/` |

All the components write to one shared bucket, each under its own prefix, with one set of credentials. By default, the backups use your platform storage: its endpoint, its credentials, and the `exalog-self-hosted-backups` bucket, whose name starts with `modules.platform_configuration.config.storage-manager.s3_bucket_prefix` (`exalog-` by default). You cannot give a component its own destination or credentials.

The backups cover these four components only. The events stored by ExaLog are in your platform storage buckets and are not copied.

The ArangoDB backup also keeps its Borg repository on a local Ceph volume of 100 GiB. The volume is kept when you disable the ArangoDB backups.

## Prerequisites

- The platform is installed and the SHC can retrieve its kubeconfig.
- The backup bucket exists on your S3-compatible storage. The SHC does not create it on your storage. The backup credentials can list, read, write, and delete the objects of this bucket.
- The orchestration node reaches the S3 endpoint of the backups: `exec Backups` connects to it directly.
- You plan a maintenance window to enable the backups, because the ClickHouse server pods restart. See [Apply the configuration](#apply-the-configuration).

## Prepare the encryption keys

Vault, ArangoDB, and ClickHouse encrypt their backups with a key that you provide in an environment variable. The PostgreSQL backups need no key.

| Variable | Component | Format |
| :--- | :--- | :--- |
| `BACKUP_VAULT_CRYPT_KEY` | Vault | At least 16 characters. |
| `BACKUP_ARANGO_CRYPT_KEY` | ArangoDB | Passphrase of the Borg repository, at least 16 characters. |
| `BACKUP_CLICKHOUSE_CRYPT_KEY` | ClickHouse | AES-256 key: exactly 64 hexadecimal characters. |

When a component is enabled, `PlatformConfigurationFile` stops if its key is missing or does not match its format. The error names the variable, not its value.

!!! warning "Keep a copy of each key outside the platform"
    The platform stores the keys in Vault, and Vault is one of the components that the backups protect. Without a copy outside the platform, you cannot decrypt the backups once the cluster is lost. Once a key is in use, do not change it: the retained backups still need it. The SHC refuses a new ArangoDB or ClickHouse key, including after you disable and enable the backups again. It does not check the Vault key.

1. To generate the three keys and add them to the protected file that holds your SHC environment variables, run:

    ```bash
    echo "BACKUP_VAULT_CRYPT_KEY=$(openssl rand -hex 32)" >> /path/to/shc.env
    echo "BACKUP_ARANGO_CRYPT_KEY=$(openssl rand -hex 32)" >> /path/to/shc.env
    echo "BACKUP_CLICKHOUSE_CRYPT_KEY=$(openssl rand -hex 32)" >> /path/to/shc.env
    ```

    `openssl rand -hex 32` returns 64 hexadecimal characters, which matches the format of every key. Copy the three keys to a secret store outside the platform.

2. To pass the keys to the SHC container, add the following options to the `docker run` command of the [execution script](/self_hosted/1.0.1/deployment/deployment_guide.md#step-4-create-the-execution-script), next to the other `-e` options:

    ```bash
      -e BACKUP_VAULT_CRYPT_KEY="$BACKUP_VAULT_CRYPT_KEY" \
      -e BACKUP_ARANGO_CRYPT_KEY="$BACKUP_ARANGO_CRYPT_KEY" \
      -e BACKUP_CLICKHOUSE_CRYPT_KEY="$BACKUP_CLICKHOUSE_CRYPT_KEY" \
    ```

3. To load the variables in your shell before you run the SHC, run:

    ```bash
    set -a; . /path/to/shc.env; set +a
    ```

## Enable the backups

To enable the backups of the four components, set the master switch in `config.yml`:

```yaml
modules:
  platform_configuration:
    config:
      backups:
        enabled: true
```

The master switch sets the default value of the `enabled` field of each component. To keep one component disabled, set its field to `false`, for example `backups.arango.enabled: false`. A disabled component needs no encryption key.

The following optional fields are under `modules.platform_configuration.config.backups`:

| Field | Description | Default |
| :--- | :--- | :--- |
| `vault.schedule`, `postgres.schedule`, `arango.schedule`, `clickhouse.schedule` | Schedule of each component, as a five-field cron expression: minute, hour, day of the month, month, and day of the week. PostgreSQL runs in UTC, the other components in the time zone of the K3s server nodes. | See [What the backups contain](#what-the-backups-contain) |
| `vault.retention` | Number of Vault snapshots kept. | `30` |
| `postgres.retention` | Retention of the PostgreSQL backups: a number followed by `d`, `w`, or `m`, for example `30d`. | `30d` |
| `clickhouse.retention_months` | Number of monthly ClickHouse chains kept, with their base and incremental backups. | `3` |
| `arango.storage.size` | Size of the local volume of the ArangoDB Borg repository. | `100Gi` |
| `s3.endpoint`, `s3.region`, `s3.access_key`, `s3.secret_key`, `s3.force_path_style_access` | Shared S3 destination and credentials of the backups. | The values of `global.platform_storage` |
| `s3.bucket` | Shared bucket of the backups. | `exalog-self-hosted-backups` |
| `vault.s3.path`, `postgres.s3.path`, `arango.s3.path`, `clickhouse.s3.path` | Prefix of each component in the bucket. Two prefixes must not overlap. | `vault/`, `/postgres/`, `arangodb/`, `clickhouse/` |

`PlatformConfigurationFile` rejects a schedule that is not a five-field cron expression, such as `@daily` or an expression with seconds. To list every backup field, run `config help modules.platform_configuration.config.backups`. The fields that only the backup status reads are described in [Check the backup status](#check-the-backup-status).

### Apply the configuration

The backup settings reach the platform through the ArgoCD stacks and through the platform installer. Apply them with the following modules: as in the `platform` stage of `Install`, `PushArgoStacks` runs before `PlatformInstallation`.

!!! warning "ClickHouse restarts"
    When the ClickHouse backups are enabled, or when their destination or credentials change, `PlatformInstallation` restarts the ClickHouse server pods and waits until they are ready. `PlatformInstallation` also restarts the secret operator of the platform each time it runs. Apply the configuration in a maintenance window.

1. To validate the backup settings, run:

    ```bash
    exec PlatformConfigurationFile
    ```

    The command generates the platform configuration file without changing the platform. It stops when a key is missing or malformed, when a schedule is invalid, when two prefixes overlap.

2. To publish the backup schedules and settings in the ArgoCD stacks, run:

    ```bash
    exec PushArgoStacks
    ```

    `PushArgoStacks` generates every stack from your current `config.yml`: it also publishes the other settings that you changed since the last publication.

3. To write the keys and the backup credentials to Vault, synchronize the backup applications, and configure the PostgreSQL backups, run:

    ```bash
    exec PlatformInstallation
    ```

The `vault-backup`, `arango-backup`, and `clickhouse-backup` CronJobs of the enabled components exist in the `support` namespace, and the first backups run at their next scheduled time. To create backups right away, see [Start a backup now](#start-a-backup-now).

## Check the backup status

To check the backups, run:

```bash
exec Backups
```

`exec Backups -m status` is equivalent. The command runs on the orchestration node and reads the backup bucket directly, with the backup S3 settings of your `config.yml`. It does not need the Kubernetes cluster.

!!! note "The status is not a restore test"
    The status checks the presence and the size of the backup files. It does not decrypt them, does not check their content, and does not restore them.

The command prints the `S3 backup health (not a restore test)` table, with one row for Vault, ArangoDB, and ClickHouse, and one row per PostgreSQL server:

| Column | Content |
| :--- | :--- |
| `Component / server` | Component, or `PostgreSQL / <server>`. |
| `State` | State of the backups, described below. |
| `Latest completed` | Completion time of the latest valid backup, in UTC. |
| `Expected due` | Scheduled time at or after which the latest backup must have started, in UTC. |
| `Schedule timezone` | Time zone used to read the schedule. |
| `Reason` | Explanation of the state. |

A valid backup is a complete backup whose files all exist in S3 with their expected size:

- For Vault, ArangoDB, and ClickHouse, the `_backup.success.json` manifest written at the end of the backup lists its files with their size, and its start and completion times. A ClickHouse incremental backup counts only with the base backup of its month.
- For PostgreSQL, the `backup.info` file of the base backup reports the `DONE` status, and its archives exist.

| State | Meaning |
| :--- | :--- |
| `fresh` | The latest valid backup started at or after the expected due time. |
| `overdue` | The latest valid backup started before the expected due time. |
| `missing` | The prefix of the component holds no valid backup. |
| `inaccessible` | The SHC cannot reach the S3 endpoint, or the storage refuses the credentials. |
| `unknown` | The SHC cannot conclude: a monitoring setting is invalid, an S3 setting is missing, no PostgreSQL server is listed, or the backup layout is not supported. |
| `disabled` | The backups of the component are disabled. The SHC does not access S3. |

The expected due time is the latest scheduled time of the component at or before the current time minus `monitoring.grace_seconds`. Each backup therefore has one hour by default to complete before the status expects it.

The following fields are under `modules.platform_configuration.config.backups`. `exec Backups` reads them from your `config.yml` at each run: you do not need to apply them to the platform.

| Field | Description | Default |
| :--- | :--- | :--- |
| `postgres.servers` | PostgreSQL servers to check, one status row each. Each name uses letters, digits, `_`, and `-`, with at most 100 names. When the list is empty, the PostgreSQL row reports `unknown`. | `[]` |
| `monitoring.timezone` | IANA time zone used to read the Vault, ArangoDB, and ClickHouse schedules. Set it to the time zone of the K3s server nodes. The PostgreSQL schedule is always read in UTC. | `UTC` |
| `monitoring.grace_seconds` | Seconds that a backup has to complete after its scheduled time. | `3600` |
| `monitoring.not_before` | Time before which the status ignores the backups, as an ISO 8601 timestamp with a time zone offset, for example `2026-10-26T00:00:00+00:00`. | Empty |

### List the PostgreSQL servers

The status checks PostgreSQL per Barman server. Each server is a directory directly under the PostgreSQL prefix of the bucket, `postgres/` by default, that holds a `base/` directory of backups.

1. Once the first PostgreSQL backups are complete, list the directories under the PostgreSQL prefix with an S3 client and the backup credentials. With the default settings and the AWS CLI, run:

    ```bash
    export AWS_ACCESS_KEY_ID="$STORAGE_S3_ACCESS_KEY"
    export AWS_SECRET_ACCESS_KEY="$STORAGE_S3_SECRET_KEY"
    export AWS_DEFAULT_REGION="$STORAGE_S3_REGION"
    export AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    export AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED

    aws --endpoint-url "$STORAGE_S3_ENDPOINT" s3 ls s3://exalog-self-hosted-backups/postgres/
    ```

    Each `PRE <server>/` line of the output is one server.

2. Add every server to `config.yml`:

    ```yaml
    modules:
      platform_configuration:
        config:
          backups:
            postgres:
              servers:
                - <server-1>
                - <server-2>
    ```

3. To check the status of each server, run `exec Backups`.

### Ignore the backups of a previous installation

`PlatformDestroy` and `PlatformScaleDown` do not delete the backup bucket. When you reinstall the platform with the same bucket, the status can count the backups of the previous installation. To exclude them, set `monitoring.not_before` to the start of the new installation: the status then ignores every backup that started before this time. Without this field, the `Reason` column reports `installation identity unknown`.

The ArangoDB backup refuses to create a new Borg repository over the repository of a previous installation. Before you enable the ArangoDB backups with a bucket that holds the backups of a previous installation, contact Sekoia support.

## Start a backup now

To start a backup of every enabled component, run:

```bash
exec Backups -m run_now
```

The command retrieves the kubeconfig, then proceeds as follows:

- For Vault, ArangoDB, and ClickHouse, it creates a Job from the `<component>-backup` CronJob of the `support` namespace, named `<component>-backup-manual-<timestamp>`. It skips a component whose backup is already running, or whose CronJob does not exist.
- For PostgreSQL, it creates a CloudNativePG `Backup` resource for every cluster that has backups configured.
- It skips the disabled components with a warning.

The command does not wait for the backups. Once they are complete, run `exec Backups`: the state of each component is `fresh`.

## Related links

- [Configure the deployment](/self_hosted/1.0.1/deployment/deployment_configuration.md#backups): Enable the backups and set the encryption keys at installation time.
- [Rotate the certificate and credentials](/self_hosted/1.0.1/operations/rotate_certificate_and_credentials.md): Change the backup S3 credentials, and the keys that cannot change.
- [Reset or destroy the platform](/self_hosted/1.0.1/operations/reset_platform.md): Data kept in S3 after a reset.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): Run SHC commands from the interactive interface.
