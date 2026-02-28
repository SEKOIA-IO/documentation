# Export Large Volumes of Events

This guide shows how to export large volumes of security events from SEKOIA.IO for offline analysis, incident response, compliance reporting, and archival purposes.

## What You Can Do

Export up to 100 million events from your searches for:

- **Incident investigation** - Deep forensic analysis of security incidents
- **Compliance reporting** - Quarterly or annual audit log exports
- **Long-term archival** - Preserve logs for regulatory retention
- **External analysis** - Share data with partners or use specialized tools
- **Custom analytics** - Feed events into your own analysis pipelines

## Before You Start

This guide uses the **SEKOIA.IO Event Exporter CLI tool** to make exports simple and automated. For complete documentation, see the [official CLI repository](https://github.com/SEKOIA-IO/sekoia-event-exporter).

You'll need:

1. **A completed search in SEKOIA.IO** - Go to Events > Search, run your query, and wait for it to finish
2. **The search job UUID** - Copy it from your browser's URL when viewing the search results
3. **An API key** - Create one with the `Massive export of events` permission

## How to Export Events

### Step 1: Set Up Your API Key

```bash
export API_KEY="your-api-key-here"
```

### Step 2: Run the Export

```bash
uvx sekoia-event-exporter export <search_job_uuid>
```

Replace `<search_job_uuid>` with the UUID you copied from your search.

**That's it!** The tool will:

- Start the export
- Show progress in real-time
- Download the file automatically
- Save it in your current folder

### What You'll See

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

1. **Search for user activities in SEKOIA.IO**

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
   - Note: The downloaded file is gzip-compressed but not encrypted (encryption is only for S3 storage)

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

**Situation:** You want to automatically feed SEKOIA.IO events into your own data lake or SIEM platform by exporting directly to your S3 bucket.

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

## Tips for SOC Analysts

**Choose the right fields:**

- For investigations: Include source.ip, destination.ip, user.name, process.name, event.action
- For compliance: Include user.name, event.action, event.outcome, source.ip
- For archival or data lakes: List all fields you need explicitly (wildcards are not supported)

**Managing large exports:**

- Exports can take 10-30 minutes for millions of events
- You can close your terminal - the export continues server-side
- Use `sekoia-event-exporter status <task_uuid>` to check progress later

**Working with export files:**

- Files are JSON format, one event per line
- Use `jq`, `grep`, or Python to analyze them
- Compressed files are typically 60-80% smaller than original

**Automating exports to your infrastructure:**

- Export directly to your S3 bucket to skip manual downloads
- Use `--no-download` flag when exporting to custom S3 buckets
- Store S3 credentials as environment variables for security



## Working with Export Files

Export files are in **JSON Lines format** (`.jsonl`) and **gzip-compressed** (`.gz`).

Each line in the file is one complete event:

```json
{"@timestamp":"2025-01-12T10:15:30Z","message":"Failed login for user admin","source.ip":"192.168.1.100"}
{"@timestamp":"2025-01-12T10:15:31Z","message":"Failed login for user root","source.ip":"192.168.1.100"}
{"@timestamp":"2025-01-12T10:15:33Z","message":"Successful login for user alice","source.ip":"192.168.1.50"}
```

### Quick Analysis Commands

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

### Python Analysis Example

```python
import json

with open('export_20260214.json', 'r') as f:
    for line in f:
        event = json.loads(line)
        if event.get('source.ip') == '192.168.1.100':
            print(f"{event['@timestamp']}: {event['message']}")
```

---

## Important Things to Know

**Exports are re-executed searches:**

- When you export, SEKOIA.IO runs your search query again
- Results may differ slightly if new events arrived since your original search
- This ensures you get the most up-to-date data

**Exports are encrypted in S3 storage:**

- Every export gets a unique SSE-C encryption key for S3 storage
- The key is shown when the export completes - **save it!**
- You need this key to download the file from S3
- Once downloaded, the file is gzip-compressed (not encrypted)
- Store encryption keys in your password manager or secure vault

**Download links expire:**

- Export files are available for 24 hours
- Download the file promptly after export completes
- If you miss the window, you'll need to run a new export

**For different regions:**
If you're using SEKOIA.IO in a non-European region, add the `--api-host` flag:

```bash
# USA region example
uvx sekoia-event-exporter export <job_uuid> --api-host api.usa1.sekoia.io
```

---

## Troubleshooting

**"Permission denied" or "403 Forbidden"**

- Ask your SEKOIA.IO admin to give you the `Massive export of events` permission
- Check you're using the right API key

**"Search job not found"**

- Make sure your search has finished (you see "Search completed" in the UI)
- Double-check you copied the correct UUID from the URL

**"Can't download the file" or S3 encryption errors**

- Make sure you saved the SSE-C encryption key from when the export finished
- The key is needed to access the file from S3 storage
- Copy the entire key exactly - no spaces or line breaks

**Export is taking forever**

- Large exports (millions of events) can take 10-30 minutes
- Try exporting fewer fields to speed it up
- Or split into smaller time ranges (export one week at a time)

**Need help?**

- Contact your SEKOIA.IO administrator
- Check the [CLI tool documentation](https://github.com/sekoia-io/sekoia-event-exporter)
- Reach out to SEKOIA.IO support if you hit quota limits
