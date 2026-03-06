# Troubleshooting the event export

This guide provides structured solutions for common errors and performance issues encountered when using the Massive Event Export feature via the CLI or API.

??? failure "Permission denied or 403 Forbidden"

    * **Condition**: The CLI or API returns an "Unauthorized" or "Forbidden" status code during the export trigger or status check.
    * **Cause**: The API key used for the request lacks the required administrative permissions for high-volume data extraction.
    * **Solution**: Contact your Sekoia.io administrator to ensure your API key is assigned the `SIC_MASSIVE_EXPORT_EVENTS` (Massive export of events) permission. Verify that the `API_KEY` environment variable is correctly set in your current terminal session.

??? failure "Search job not found"

    * **Condition**: The export system returns an error stating it cannot locate the search job UUID.
    * **Cause**: The search job has not yet reached a final state, or the UUID provided is incorrect/expired.
    * **Solution**: Ensure the search has fully finished in the Sekoia.io console; the status must display **Search completed** or **DONE**. Re-copy the UUID from the browser URL, ensuring no characters are missing.

??? failure "Encryption errors or download failure"

    * **Condition**: The download fails with a decryption error, or the file cannot be accessed from the S3 link.
    * **Cause**: The SSE-C encryption key provided during the download request is missing, incomplete, or does not match the key generated at the time of export.
    * **Solution**: Locate the unique 256-bit encryption key displayed by the CLI when the export task finished. Ensure the key is copied exactly—without extra spaces or line breaks—into your download command or header. If more than 24 hours have passed since the export, the link has expired and you must trigger a new export.

??? failure "Export task duration exceeded or timeout"

    * **Condition**: The export task remains in the `RUNNING` state for an extended period or terminates with a timeout.
    * **Cause**: The export request involves a high volume of events (e.g., >50M) combined with a high number of selected fields, or the search query is computationally expensive.
    * **Solution**: Optimize the request by explicitly limiting the fields using the `--fields` flag. For very large datasets, split the export into smaller time ranges (e.g., daily increments). Check the [Optimization Guide](../concepts/optimization.md) to ensure you are exporting during recommended off-peak windows.

### Summary of common fixes

| Category | Action |
| :--- | :--- |
| **Permissions** | Verify `SIC_MASSIVE_EXPORT_EVENTS` is active. |
| **Job Status** | Ensure Search status is `DONE` before triggering. |
| **Security** | Copy the SSE-C key exactly as shown in the CLI output. |
| **Retention** | Download within 24 hours of the task finishing. |
| **Performance** | Limit `--fields` to essential data only. |


## Next steps
To understand the technical boundaries and monthly data quotas of the system, consult the [Export technical reference](xdr/features/investigate/export_reference.md).

### Getting further assistance
If the troubleshooting steps above do not resolve your issue:
* **Technical Documentation**: Consult the [CLI tool documentation](https://github.com/sekoia-io/sekoia-event-exporter).
* **Community Limits**: Contact your administrator to verify if your community has reached its 10 GB monthly compressed data quota.
* **Support**: Reach out to Sekoia.io support, if you hit quota limit or for persistent infrastructure timeouts.
