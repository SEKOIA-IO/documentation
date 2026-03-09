# Export events with the CLI

The `sekoia-event-exporter` is the official command-line tool for automating the export workflow, including triggering the job, monitoring progress, and downloading the results.


## Prerequisites
* An API Key with the `SIC_MASSIVE_EXPORT_EVENTS` permission.
* A completed search in Sekoia.io (status must be `DONE`).
* The **Search Job UUID** (copied from the browser URL when viewing results).
* Sekoia.io operates in multiple regions. **Configure your region** when using the CLI.

??? info "CLI Configuration"
    ```bash
    # Using environment variable
    export API_HOST=api.usa1.sekoia.io
    uvx sekoia-event-exporter export <job_uuid>

    # Using command flag
    uvx sekoia-event-exporter export <job_uuid> --api-host api.usa1.sekoia.io
    ```

!!! note "Re-execution behavior"
    When you trigger an export, SEKOIA **does not reuse** the cached search results. Instead, it:

    - Re-runs your exact search query
    - Uses the same time range and filters
    - Streams results directly to storage
    This means **exported results may include new or late-arriving events **that weren't in your original search.

## Basic export procedure
1.  Open your terminal and set your API key:
    ```bash
    export API_KEY="your-api-key-here"
    ```
2.  Run the export command:
    ```bash
    uvx sekoia-event-exporter export <search_job_uuid>
    ```
3.  Wait for the real-time progress bar to finish.

!!! warning "Encryption key storage"
    The tool displays a unique encryption key upon completion. Save this key in a secure vault. Without it, you cannot re-download the file from S3 storage if the local copy is lost.

!!! tip "manual status check"
    If you disconnected or closed your terminal, you can resume monitoring using the status command and your Task UUID. (The task UUID appears in the first few lines of the output):
    ```bash
     uvx sekoia-event-exporter status <task_uuid>
    ```

## Advanced: Export to custom S3 buckets
You can skip manual downloads by feeding events directly into your own data lake or S3 bucket. The tool supports AWS S3 and S3-compatible storage such as MinIO or Wasabi.

1.  Configure your S3 environment variables:
    ```bash
    export S3_BUCKET="your-bucket-name"
    export S3_PREFIX="sekoia/events/"
    export S3_ACCESS_KEY_ID="<your-access-key>"
    export S3_SECRET_ACCESS_KEY="<your-secret-key>"
    export S3_REGION_NAME="eu-west-1"
    ```
2.  Execute the export with the `--no-download` flag:
    ```bash
    uvx sekoia-event-exporter export <job_uuid> --no-download
    ```

## See also: 
- To export with API, follow the [Export events with the API](/xdr/features/investigate/export_event_API.md) guide
- To review the exact quotas, processing times, and troubleshooting steps, consult the [Export technical reference](/xdr/features/investigate/export_reference.md).
- For practical examples of how to configure fields for specific security investigations, see our [Event export use cases](/xdr/usecases/massive_export.md).
