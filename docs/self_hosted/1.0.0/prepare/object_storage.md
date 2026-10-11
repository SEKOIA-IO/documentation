# Prepare the S3 object storage

The platform stores the indexed events in an S3-compatible object storage. You provide this storage. Size it with [Size the object storage](../deployment/deployment_prerequisites.md#size-the-object-storage).

The platform services that write and read the events run on the Kubernetes nodes. The orchestration node does not use this storage.

## Rules

- The storage **MUST** offer the **S3 API**.
- The storage **MUST** be reached from **every Kubernetes node**.
- The storage **MUST** be reached over **HTTP or HTTPS**. If you use HTTPS, the certificate **SHOULD** be signed by a public certificate authority.
- These **16 buckets MUST exist** before the installation:

    ```
    exalog-self-hosted-events-0   exalog-self-hosted-events-4   exalog-self-hosted-events-8   exalog-self-hosted-events-c
    exalog-self-hosted-events-1   exalog-self-hosted-events-5   exalog-self-hosted-events-9   exalog-self-hosted-events-d
    exalog-self-hosted-events-2   exalog-self-hosted-events-6   exalog-self-hosted-events-a   exalog-self-hosted-events-e
    exalog-self-hosted-events-3   exalog-self-hosted-events-7   exalog-self-hosted-events-b   exalog-self-hosted-events-f
    ```

- **One** access key and its secret key **MUST** have the rights **list, read, write and delete** on these 16 buckets.
- The storage **SHOULD** accept **path-style** URLs (`https://<endpoint>/<bucket>/<object>`).
- The bucket names **SHOULD** start with `exalog-` (default prefix).
- The Kubernetes nodes **SHOULD** reach the storage without a proxy.

### Configuration

| What | Where | Value |
| :--- | :--- | :--- |
| Endpoint | `env.rc`, `STORAGE_S3_ENDPOINT` | The URL of the storage, **with** `http://` or `https://`, and the port if it is not the default port. Example: `https://s3.example.com:9000`. |
| Region | `env.rc`, `STORAGE_S3_REGION` | The region of your storage. If your storage has no region, use the value it accepts by default (for example `us-east-1` for MinIO). It **MUST NOT** be empty. |
| Access key | `env.rc`, `STORAGE_S3_ACCESS_KEY` | |
| Secret key | `env.rc`, `STORAGE_S3_SECRET_KEY` | |

The starter `config.yml` already reads these four variables in `global.platform_storage`. No other field is needed.

### If you do not follow a SHOULD rule

| SHOULD rule not followed | What you must change |
| :--- | :--- |
| HTTPS certificate from a private authority or self-signed | No configuration field exists for the certificate authority of the storage. This setup is not validated: contact Sekoia before the installation. |
| The storage accepts only virtual-hosted URLs (`https://<bucket>.<endpoint>/...`) | In `config.yml`, set `global.platform_storage.force_path_style_access: false`. A DNS record for `*.<endpoint>` **MUST** then point to the storage. |
| Your naming policy requires another prefix | In `config.yml`, set `modules.platform_configuration.config.storage-manager.s3_bucket_prefix: "<prefix>"`. The 16 bucket names become `<prefix>self-hosted-events-0` to `<prefix>self-hosted-events-f`: create these buckets instead. Use `""` for no prefix. |
| The nodes reach the storage through a proxy | In `config.yml`, set the platform proxy: see [Proxy](../deployment/deployment_configuration.md#proxy). |
| A platform proxy is configured, and the nodes reach the storage **without** it | Add the storage host name to `modules.platform_configuration.config.proxy.no_proxy`. |

### Not supported

| Situation | Result |
| :--- | :--- |
| Bucket names without the `self-hosted-events-0` … `-f` pattern | Only the prefix can change. |
| A different access key for each bucket | The platform uses one access key. |

## Create and check the buckets

These commands use the AWS CLI. They work with any S3-compatible storage. Run them on **one Kubernetes node**: the test then uses the same network path as the platform.

1. Install the AWS CLI:

    ```bash
    sudo apt-get install -y awscli
    ```

2. Set the values of your storage. Replace the four values, then paste the lines:

    ```bash
    export AWS_ACCESS_KEY_ID="<S3_ACCESS_KEY>"
    export AWS_SECRET_ACCESS_KEY='<S3_SECRET_KEY>'
    export AWS_DEFAULT_REGION="<S3_REGION>"
    export EP="<S3_ENDPOINT_URL>"
    export AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED
    export AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED
    ```

    The last two lines disable a checksum feature of recent AWS CLI versions that many S3-compatible storages do not support.

3. Use path-style URLs, like the platform:

    ```bash
    aws configure set default.s3.addressing_style path
    ```

4. Create the 16 buckets. Skip this step if your storage administrator already created them:

    ```bash
    for i in 0 1 2 3 4 5 6 7 8 9 a b c d e f; do aws --endpoint-url "$EP" s3 mb "s3://exalog-self-hosted-events-$i"; done
    ```

    **Expected result:** 16 lines `make_bucket: exalog-self-hosted-events-...`.

5. Count the buckets:

    ```bash
    aws --endpoint-url "$EP" s3 ls | grep -c "exalog-self-hosted-events-"
    ```

    **Expected result:** `16`.

6. Test write, read and delete in every bucket:

    ```bash
    echo "sekoia-test" > /tmp/s3-test.txt
    ```

    ```bash
    for i in 0 1 2 3 4 5 6 7 8 9 a b c d e f; do aws --endpoint-url "$EP" s3 cp /tmp/s3-test.txt "s3://exalog-self-hosted-events-$i/s3-test.txt" && aws --endpoint-url "$EP" s3 cp "s3://exalog-self-hosted-events-$i/s3-test.txt" /tmp/s3-read.txt && aws --endpoint-url "$EP" s3 rm "s3://exalog-self-hosted-events-$i/s3-test.txt" && echo "bucket $i OK"; done
    ```

    **Expected result:** 16 lines, from `bucket 0 OK` to `bucket f OK`. A line that starts with `upload failed`, `download failed` or `delete failed` shows a missing right.

7. Remove the credentials from the node:

    ```bash
    aws configure set default.s3.addressing_style auto && unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY
    ```

## Storage products

!!! note "No product validated yet"
    The Sekoia lab uses a storage inside the cluster for training. No external S3 storage product has a validated procedure yet. A tab is added here for each product validated in the lab or in a customer project.

<!--
To add a technology: add a "=== "<Product>"" tab here, with its "Validation status" (lab or
customer project, with the product version), the commands to create the access key with the
list/read/write/delete rights on the 16 buckets, and the "Write the values for the SHC" step.
-->

## Checklist

- [ ] The 16 buckets exist (`grep -c` prints `16`).
- [ ] The write, read and delete test prints `OK` for the 16 buckets, from a Kubernetes node.
- [ ] `STORAGE_S3_ENDPOINT`, `STORAGE_S3_REGION`, `STORAGE_S3_ACCESS_KEY` and `STORAGE_S3_SECRET_KEY` are in `env.rc`.
