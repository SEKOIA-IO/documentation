# Export technical reference

This page details the constraints, formats, and API endpoints for the export system.

## Quotas and limitations
| Metric | Limit |
| :--- | :--- |
| **Events per export** | Up to 100 million |
| **Monthly Quota** | 10 GB (compressed) per community, resets on the 1st of each month|
| **Concurrency** | 1 active export at a time per community |
| **Search job limit** | Max 10 exports per unique search job |
| **Download window** | 24 hours |
| **Community scope** | Single community only (multi-community not supported) |

## Processing time expectations
Typical processing times vary based on query complexity and field count:
* **1 million events**: 2–5 minutes
* **10 million events**: 20–40 minutes
* **50 million events**: 60–120 minutes

!!! info "Processing time variations"
    Processing time varies based on:

    - Number of fields exported
    - Query complexity
    - Event data size
    - System load

!!! tip "Performance best practices"

    * **Limit fields**: Only export the specific ECS fields required for your analysis. Reducing the field count significantly decreases processing time and final file size.
    * **Split large exports**: If your dataset exceeds 50 million events, break the request into smaller time ranges (e.g., export day-by-day instead of a full week) to prevent task timeouts.
    * **Prioritize off-peak hours**: Schedule very large exports (50M+ events) during low-traffic periods to benefit from higher available processing bandwidth.

## File format and fields
* **Format**: JSON Lines (`.jsonl`) with gzip compression (`.gz`). Each line is a single event.
* **Field selection**: 
* **No Wildcards**: You must list fields explicitly. Wildcards like `source.*` are **not** supported.

!!! info "Field selection"
    By default, `@timestamp` and `message` are included.
    You can customize which fields to export by specifying exact field names. For example : `source.ip`, `user.name`, `event.action`, `event.categroy`, `destination.ip`... 

??? example

    ```json
    {"@timestamp":"2025-01-12T10:15:30Z","message":"Failed login","source.ip":"192.168.1.100"}
    {"@timestamp":"2025-01-12T10:15:31Z","message":"Successful login","source.ip":"192.168.1.50"}
    ```

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

!!! warning
    Save the encryption key displayed after export. Without it, you cannot download the file.

### Custom S3 Buckets

You can export directly to your own S3 bucket instead of using SEKOIA.IO's storage:

- Requires S3 credentials (access key, secret key)
- Supports S3-compatible storage (MinIO, Wasabi, etc.)
- Useful for automated data pipelines and data lakes


## Troubleshooting
| Issue | Possible Cause | Resolution |
| :--- | :--- | :--- |
| `Permission denied` | API key lacks permissions. | Ensure key has `SIC_MASSIVE_EXPORT_EVENTS`. |
| `Search job not found` | Search is not finished. | Verify search status is `DONE` in the UI. |
| Download failed | Missing SSE-C key. | You must use the key provided at the end of the export. |
| Export is slow | High event/field count. | Limit exported fields or split timeframe into smaller ranges. |

## Next step

- If you need a high-level overview of the export security logic, return to the [Massive event export concept](xdr/features/investigate/event_export.md).
- Get inspired by practical examples and step-by-step workflows for common scenarios with our  [Export Large Volumes of Events - Use Case Guide](../../usecases/massive_export.md)
