# Export Large Volumes of Events

This tutorial guides you through exporting up to 100 million security events from Sekoia.io for offline analysis, incident response, compliance reporting, and archival.

By using the official CLI tool, you can automate the extraction of massive datasets and stream them directly to your infrastructure or local machine.

!!! note 
    Read our overview article to learn more about [Massive event export](/xdr/features/investigate/event_export.md). 
    For complete documentation, see the [official CLI repository](https://github.com/SEKOIA-IO/sekoia-event-exporter).
    


## Prerequisites

This guide uses the **Sekoia.io Event Exporter CLI tool** to make exports simple and automated. 

Prerequisites

1. **A completed search in Sekoia.io** - Go to Events > Search, run your query, and wait for it to finish
2. **The search job UUID** - Copy it from your browser's URL when viewing the search results
3. **An API key** - Create one with the `Massive export of events` permission
4. * **Python** installed on your system to run the `uvx` command.

## Export Events with CLI

1. Set your API Key:

```bash
export API_KEY="your-api-key-here"
```

2. Run the Export command:

```bash
uvx sekoia-event-exporter export <search_job_uuid>
```

3. Replace `<search_job_uuid>` with the UUID you copied from your search.

!!! success 

    The tool:

    - Start the export
    - Show progress in real-time
    - Download the file automatically
    - Save it in your current folder

    What You'll See: 

    ```
    ✓ Export triggered

    Exporting: ████████████░░░░░░░░ 40.0% | 4M / 10M events | ⏱ 2m 30s

    ✓ Export ready!
    Downloading: export_20260214_143842.json.gz
    ✓ Download complete (15.0 MB)

    ```


## Common Use Cases

### Use Case 1: Investigating User Activity

**Situation:** You need to export all activities associated with a specific user (e.g., john.doe) for the last 7 days to investigate their actions.

**Step-by-Step:**

1. **Search for user activities in Sekoia.io**

   - Go to **Events** > **Search**
   - Query: `user.name:"john.doe"`
   - Set timeframe: Last 7 days
   - Wait for the search to complete
   - Copy the job UUID from the URL

2. **Export with user activity fields**
   ```bash
   uvx sekoia-event-exporter export <job_uuid> \
     --fields "@timestamp,user.name,source.ip,event.action,event.category,event.outcome,destination.ip,process.name,file.path,message"
   ```

3. **Analyze the user's activity**
   ```bash
   # Extract the file
   gunzip export_*.json.gz

   # View first events
   head -n 10 export_*.json

   # Search for failed login attempts
   grep "failed" export_*.json

   # Count total activities
   wc -l export_*.json
   ```

**Result:** You get a complete timeline of all activities for the user over 7 days, ready for investigation, audit, or sharing with your security team.

---

### Use Case 2: Compliance Reporting

**Situation:** Your compliance officer needs quarterly audit logs for regulatory review.

**Step-by-Step:**

1. **Search for audit events**

   - Query: `event.category:authentication OR event.category:access`
   - Timeframe: Q1 2026 (Jan 1 - Mar 31)

2. **Export with compliance fields**
   ```bash
   uvx sekoia-event-exporter export <job_uuid> \
     --fields "@timestamp,user.name,event.action,event.outcome,source.ip" \
     --output compliance_q1_2026.json.gz
   ```

3. **Save securely**
   - Keep the encryption key in your secure vault
   - Store the export in your compliance archive
   - The file is encrypted in S3 storage (you'll download a decrypted, gzip-compressed version)

---

### Use Case 3: Long-Term Archival

**Situation:** You're decommissioning a system and need to archive all its logs for regulatory retention.

**Step-by-Step:**

1. **Search for system events**

   - Query: `host.name:"old-server-01"`
   - Timeframe: All time (or specific retention period)

2. **Export all relevant data**
   ```bash
   uvx sekoia-event-exporter export <job_uuid> \
     --fields "@timestamp,message,host.name,event.action,event.category,event.outcome" \
     --output archive_oldserver_2026.json.gz
   ```

3. **Archive securely**

   - Transfer to cold storage
   - Keep the encryption key - you'll need it if you want to re-download from S3 later

!!! note
    The downloaded file is gzip-compressed but not encrypted (encryption is only for S3 storage)

---

### Use Case 4: Sharing with External Partners

**Situation:** An external security consultant needs access to specific event data.

**Step-by-Step:**

1. **Create a focused search**

   - Limit to specific timeframe and systems
   - Exclude sensitive internal data if needed

2. **Export and get the download URL** (without downloading locally)
   ```bash
   uvx sekoia-event-exporter export <job_uuid> \
     --fields "@timestamp,event.category,event.action,message" \
     --no-download
   ```

!!! success

    The tool will display:
    ```
    ✓ Export ready!
    Download URL: https://s3.storage.com/...
    Encryption key: dGhpc2lzYW5leGFtcGxl...
 
    ⚠️  URL valid for 24 hours
    ```

3. **Securely share with your partner**

   - Send the download URL (valid for 24 hours)
   - Share the encryption key separately via a different channel (phone, secure messaging, etc.)
   - Your partner needs the key to download from S3 (the file they download will be gzip-compressed, not encrypted)
   - No need to download and re-upload the file yourself

---

### Use Case 5: Export to Your Own S3 Bucket

**Situation:** You want to automatically feed Sekoia.io events into your own data lake or SIEM platform by exporting directly to your S3 bucket.

**Step-by-Step:**

1. **Prepare your S3 credentials**

   - Get your S3 bucket name (e.g., `company-security-datalake`)
   - Create AWS access keys with write permissions to the bucket
   - Note your bucket's region (e.g., `eu-west-1`)

2. **Set up environment variables** (recommended for security)

   ```bash
   export S3_BUCKET="company-security-datalake"
   export S3_PREFIX="sekoia/events/"
   export S3_ACCESS_KEY_ID="<your-access-key>"
   export S3_SECRET_ACCESS_KEY="<your-secret-key>"
   export S3_REGION_NAME="eu-west-1"
   ```

3. **Run the export to your bucket**

   ```bash
   uvx sekoia-event-exporter export <job_uuid> \
     --fields "@timestamp,event.action,event.category,event.outcome,source.ip,destination.ip,user.name,process.name" \
     --no-download
   ```

   Or specify S3 settings directly in the command:

   ```bash
   uvx sekoia-event-exporter export <job_uuid> \
     --fields "@timestamp,event.action,event.category,source.ip,destination.ip,user.name" \
     --s3-bucket company-security-datalake \
     --s3-prefix sekoia/events/ \
     --s3-access-key <access-key> \
     --s3-secret-key <secret-key> \
     --s3-region eu-west-1 \
     --no-download
   ```

4. **Verify the export**

   - Check your S3 bucket for the exported file
   - The file will be in: `s3://company-security-datalake/sekoia/events/`
   - Your data pipeline can now process it automatically

**Result:** Events are exported directly to your infrastructure, ready for automated ingestion into your data lake, SIEM, or analytics platform. No manual download and upload needed!

---
### Use case 6: Export 30M events to AWS S3
**Situation:** You need to export 30 million events directly to your company's data lake to avoid local storage limits.

**Step-by-Step:**

1. **Configure AWS**

   Set your bucket environment variables:
   
   ```bash
   export S3_BUCKET="company-security-datalake"
   export S3_REGION_NAME="eu-west-1"
   export S3_ACCESS_KEY_ID="<your-access-key>"
   export S3_SECRET_ACCESS_KEY="<your-secret-key>"
   ```

2. **Trigger Stream**
    Use the `--no-download` flag to send data directly to AWS:
    ```bash
    uvx sekoia-event-exporter export <job_uuid> --no-download
    ```

4. **Verify**: Check your S3 bucket once the CLI displays the `FINISHED` status.

**Result:** In your AWS Management Console, a new object appears in the bucket and prefix you defined (e.g., s3://company-security-datalake/sekoia/events/). 0 bytes used on your local machine; standard S3 storage consumption in AWS.

---

## Tips for SOC Analysts

### Choose the right fields:

- For investigations: Include source.ip, destination.ip, user.name, process.name, event.action
- For compliance: Include user.name, event.action, event.outcome, source.ip
- For archival or data lakes: List all fields you need explicitly (wildcards are not supported)

### Managing large exports:

- Exports can take 10-30 minutes for millions of events
- You can close your terminal:  the export continues server-side
- Use `sekoia-event-exporter status <task_uuid>` to check progress later

### Working with export files:

- Files are JSON format, one event per line
- Use `jq`, `grep`, or Python to analyze them
- Compressed files are typically 60-80% smaller than original

### Automating exports to your infrastructure:

- Export directly to your S3 bucket to skip manual downloads
- Use `--no-download` flag when exporting to custom S3 buckets
- Store S3 credentials as environment variables for security


## Quick Analysis Commands

```bash
# Extract the file
gunzip export_*.json.gz

# Count how many events
wc -l export_*.json

# View first 10 events
head -n 10 export_*.json

# Search for specific text
grep "malware" export_*.json

# Filter with jq (if installed)
cat export_*.json | jq 'select(.["source.ip"] == "192.168.1.100")'
```

??? "Python Analysis Example"

    ```python
    import json

    with open('export_20260214.json', 'r') as f:
        for line in f:
            event = json.loads(line)
            if event.get('source.ip') == '192.168.1.100':
                print(f"{event['@timestamp']}: {event['message']}")
    ```

## Next steps: 
To understand the technical boundaries and monthly data quotas of the system, consult the [Export technical reference](/xdr/features/investigate/export_reference.md).
