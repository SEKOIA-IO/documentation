# Export events with the API

The Sekoia.io REST API allows you to programmatically trigger event exports and monitor their progress. This method is ideal for custom integrations with internal platforms or security orchestration tools.

## Prerequisites
* An API Key with the `SIC_MASSIVE_EXPORT_EVENTS` permission.
* A completed Search Job UUID (status must be `DONE`).
* A tool to send HTTP requests (e.g., cURL or Postman).
* SEKOIA operates in multiple regions. **Configure your region** when using the CLI.

??? info "API Configuration"
    Use the appropriate API host in your requests:
    example for USA1 region:
    ```
    https://api.usa1.sekoia.io/v1/sic/conf/events/search/jobs/{job_uuid}/export
    ```
    For a complete list of regions, see the [Sekoia.io Regions Documentation](https://docs.sekoia.io/getting_started/regions/).


### Step 1: Trigger the export
To start the export, send a **POST** request to the export endpoint. You must specify the fields you want to retrieve as wildcard patterns (like `event.*`) are not supported.

**Request:**
```bash
curl -X POST "[https://api.sekoia.io/v1/sic/conf/events/search/jobs/](https://api.sekoia.io/v1/sic/conf/events/search/jobs/){job_uuid}/export" \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
           "fields": ["@timestamp", "message", "source.ip", "user.name"]
         }'
```
**Result:**  
The API returns a `task_uuid`. You must use this ID to monitor the status in the next step.

###Step 2: Monitor task status
Send a GET request to verify the progress and the state of the export task.

**Request:**
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "[https://api.sekoia.io/v1/tasks/](https://api.sekoia.io/v1/tasks/){task_uuid}"
```
**Result:**
The response indicates the **status**. Possible values are PENDING, RUNNING, FINISHED, or FAILED.

### Step 3: Retrieve the download URL
Once the status is FINISHED, retrieve the pre-signed S3 URL and the metadata for the exported file.

**Request:** 
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "[https://api.sekoia.io/v1/sic/conf/events/search/jobs/](https://api.sekoia.io/v1/sic/conf/events/search/jobs/){job_uuid}/export-jobs"
```
**Result:** 
The response provides the `download_url`, `the export_size_compressed`, and the `expire_at timestamp`.

!!! warning "Encryption key retrieval"
    The API response includes the unique SSE-C encryption key. You must provide this key in the header of your final download request to S3 to decrypt the stream. This key is only valid for the current export job.download_url, the export_size_compressed, and the expire_at timestamp.

## See also: 
- To see how these API steps are automated into a single command-line interface, refer to the [Export events with the CLI](/xdr/features/investigate/export_event_cli.md) guide.
- Get inspired by practical examples and step-by-step workflows for common scenarios with our  [Export Large Volumes of Events - Use Case Guide](../../usecases/massive_export.md)
