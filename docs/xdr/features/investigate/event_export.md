# Massive Event Export

## Overview

The Massive Event Export feature allows you to export large volumes of security events from SEKOIA.IO for offline analysis, compliance reporting, and long-term archival.

**Key Capabilities:**

- Export up to **100 million events** per job
- Select specific fields to export
- Asynchronous background processing
- Automatic compression (gzip)
- Secure storage with encryption
- Export to your own S3 bucket (optional)

**When to Use:**

- **Massive Export**: For large datasets (millions of events), long-term archival, or automated workflows
- **Direct Export**: For small, quick exports (few thousand events) that you need immediately

**Tools Available:**

- **CLI Tool**: We provide an official [sekoia-event-exporter](https://github.com/SEKOIA-IO/sekoia-event-exporter) command-line tool that automates the entire export workflow, including triggering, monitoring progress, and downloading files
- **API**: Direct API access for custom integrations and automation

**See Also:**

- [Export Large Volumes of Events - Use Case Guide](../../usecases/massive_export.md) - Practical examples and step-by-step workflows for common scenarios

## How It Works

### Export Workflow

1. **Create a search** in SEKOIA.IO and wait for it to complete
2. **Trigger an export** using the search job UUID
3. **The platform re-executes your search** and streams results to storage
4. **Download the file** when the export completes (valid for 24 hours)

### Re-Execution Behavior

When you trigger an export, SEKOIA.IO **does not reuse** the cached search results. Instead, it:

- Re-runs your exact search query
- Uses the same time range and filters
- Streams results directly to storage

**Important**: This means exported results may include new or late-arriving events that weren't in your original search.

### Task Lifecycle

Exports progress through these statuses:

```
PENDING → RUNNING → FINISHED (or FAILED)
```

- **PENDING**: Export task is queued and waiting to start
- **RUNNING**: Export is actively processing events
- **FINISHED**: Export completed successfully, file is ready to download
- **FAILED**: Export encountered an error and did not complete

You can monitor progress at any time using the task UUID.

## Prerequisites

### Permissions

Your API key needs the **`SIC_MASSIVE_EXPORT_EVENTS`** permission.

### Completed Search

Your search job must be fully complete (status: `DONE`) before you can export it.

### Quotas and Limitations

- **Events per export**: Up to 100 million events
- **Monthly data quota**: Each community can export up to 10 GB (compressed size) per calendar month. This quota resets on the 1st of each month.
- **Single community only**: You cannot export events from multiple communities in one export. Your search must be scoped to a single community.
- **One export at a time**: Only one export can run at a time per community. If you try to start a new export while another is running, you'll need to wait for the first one to complete.
- **Export limit per search**: Each search job can be exported a maximum of 10 times. If you reach this limit, create a new search with the same query parameters to continue exporting.
- **No wildcard field selection**: Wildcard patterns (like `event.*` or `source.*`) are not supported. You must specify each field name explicitly.

## Export Formats

### File Format

All exports are in **JSON Lines** format (`.jsonl`) with **gzip compression** (`.gz`):

- One complete JSON object per line
- Each line is a single event
- Compressed files are typically 60-80% smaller

**Example:**

```json
{"@timestamp":"2025-01-12T10:15:30Z","message":"Failed login","source.ip":"192.168.1.100"}
{"@timestamp":"2025-01-12T10:15:31Z","message":"Successful login","source.ip":"192.168.1.50"}
```

### Field Selection

By default, exports include `@timestamp` and `message` fields. You can customize which fields to export by specifying exact field names.

**API Request Example:**
```json
{
  "fields": [
    "@timestamp",
    "source.ip",
    "user.name",
    "event.action",
    "event.category",
    "destination.ip"
  ]
}
```

**CLI Example:**
```bash
--fields "@timestamp,source.ip,user.name,event.action,event.category,destination.ip"
```

**Important**: Wildcard patterns (like `event.*` or `source.*`) are not supported. You must specify each field name explicitly.


**Best Practices:**

- Only export fields you need (reduces file size and processing time)
- List all required fields explicitly
- Include `@timestamp` for timeline analysis
- Refer to the [Use Case Guide](../../usecases/massive_export.md) for field recommendations by scenario

## Storage and Security

### S3 Storage

All exports are stored in S3 with secure, time-limited access:

- **Storage duration**: Files available for 24 hours
- **Access**: Pre-signed download URLs
- **Encryption**: SSE-C (Server-Side Encryption with Customer-Provided Keys)

### SSE-C Encryption

Every export is automatically encrypted in S3 storage using **SSE-C**:

1. A unique 256-bit encryption key is generated for each export
2. The file is encrypted in S3 using this key
3. You need the same key to download the file later
4. **Once downloaded**, the file is just gzip-compressed (not encrypted)

**Important**: Save the encryption key displayed after export. Without it, you cannot download the file.

### Custom S3 Buckets

You can export directly to your own S3 bucket instead of using SEKOIA.IO's storage:

- Requires S3 credentials (access key, secret key)
- Supports S3-compatible storage (MinIO, Wasabi, etc.)
- Useful for automated data pipelines and data lakes

## API Reference

### Trigger Export

**Endpoint:**
```
POST /v1/sic/conf/events/search/jobs/{job_uuid}/export
```

**Request Body:**
```json
{
  "fields": ["@timestamp", "message", "source.ip", "user.name"]
}
```

**Response:**
```json
{
  "task_uuid": "550e8400-e29b-41d4-a716-446655440000"
}
```

### Check Export Status

**Endpoint:**
```
GET /v1/tasks/{task_uuid}
```

**Response:**
```json
{
  "status": "RUNNING",
  "progress": 4000000,
  "total": 10000000
}
```

### Get Download URL

**Endpoint:**
```
GET /v1/sic/conf/events/search/jobs/{job_uuid}/export-jobs
```

**Response:**
```json
{
  "download_url": "https://s3.amazonaws.com/...",
  "expire_at": "2026-02-11T14:30:00Z",
  "exported_events_count": 10000000,
  "export_size_compressed": 2147483648,
  "format": "json"
}
```

## Regional Support

SEKOIA.IO operates in multiple regions. Configure your region when using the CLI or API:

### CLI Configuration

```bash
# Using environment variable
export API_HOST=api.usa1.sekoia.io
uvx sekoia-event-exporter export <job_uuid>

# Using command flag
uvx sekoia-event-exporter export <job_uuid> --api-host api.usa1.sekoia.io
```

### API Configuration

Use the appropriate API host in your requests:

```
https://api.usa1.sekoia.io/v1/sic/conf/events/search/jobs/{job_uuid}/export
```

For a complete list of regions, see the [Sekoia.io Regions Documentation](https://docs.sekoia.io/getting_started/regions/).

## Limits and Quotas

### Export Limits

- **Maximum events per export**: 100 million
- **Maximum file size**: No hard limit (depends on field count and event size)
- **Export timeout**: Exports that take too long may timeout

### Processing Time

Typical processing times:

- **1 million events**: ~2-5 minutes
- **10 million events**: ~20-40 minutes
- **50 million events**: ~60-120 minutes

Processing time varies based on:

- Number of fields exported
- Query complexity
- Event data size
- System load

### Download Limits

- **Download URL expiration**: 24 hours
- **Download retries**: Unlimited within 24-hour window (with encryption key)

### Best Practices

To optimize export performance:

- **Limit fields**: Only export what you need
- **Split large exports**: Break very large datasets into smaller time ranges
- **Use off-peak hours**: For very large exports (50M+ events)