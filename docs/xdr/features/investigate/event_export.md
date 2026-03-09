# Massive event export

## Overview

The Massive Event Export feature allows you to extract up to 100 million security events from Sekoia.io for offline analysis, compliance reporting, and long-term archival.

While the platform offers a Direct Export for small, immediate datasets (up to 500 events), the Massive Export is designed for large-scale data movements, automated workflows, and regulatory log retention. 

!!! note "Small export"
    [Learn more about this option in our Events FAQ](/xdr/FAQ/get_events.md))

## How it works

The export process is asynchronous and follows a specific security and operational logic:

- **Re-execution behavior:** When you trigger an export, Sekoia.io does not reuse cached search results. It re-runs your exact search query with the same time range and filters. This ensures you capture any late-arriving events that were not present in your initial search results.
- **Task lifecycle:** Exports progress through four distinct statuses:

  - `PENDING`: The task is queued and waiting for resources.
  - `RUNNING`: The platform is actively streaming results to storage.
  - `FINISHED`: The export is complete and the file is ready for download.
  - `FAILED`: An error occurred (e.g., quota exceeded or search job expired).

!!! note 

    You can monitor progress at any time using the task UUID.

**Key Capabilities:**

- Export up to **100 million events** per job
- Select specific fields to export
- Asynchronous background processing
- Automatic compression (gzip)
- Secure storage with encryption
- Export to your own S3 bucket (optional)

**Tools Available:**

- **CLI Tool**: We provide an official [sekoia-event-exporter](https://github.com/SEKOIA-IO/sekoia-event-exporter) command-line tool that automates the entire export workflow, including triggering, monitoring progress, and downloading files
- **API**: Direct API access for custom integrations and automation



## Next steps:
- [Export events with the CLI (recommended)](/xdr/features/investigate/export_event_cli.md): To begin your first export using our official tool, follow the **Export events with the CLI** guide.
- [Export Large Volumes of Events - Use Case Guide](../../usecases/massive_export.md)  Practical examples and step-by-step workflows for common scenarios
- [Export events with the API](/xdr/features/investigate/export_event_API.md): If you rather like exporting with API, follow the **Export events with the API** guide.




