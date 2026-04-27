# MISP IDS Attributes to IOC Collection Trigger

## Overview

This trigger periodically retrieves IDS-flagged attributes from a MISP instance and pushes them to a Sekoia.io IOC Collection. Attributes with the `to_ids` flag enabled in MISP are automatically imported as IOCs in Sekoia, enabling detection and alerting when these indicators are observed in your environment.

## Prerequisites

1. **MISP Instance**: Access to a MISP instance with published events containing IDS-flagged attributes
2. **MISP API Key**: Valid API key with read permissions
3. **Sekoia IOC Collection**: Pre-created IOC Collection in your Sekoia.io community
4. **Sekoia API Key**: API key with write permissions to the IOC Collection

## Configuration

### Step 1: Obtain MISP Credentials

1. Log in to your MISP instance
2. Navigate to **Event Actions** > **Automation**
3. Copy your **Authkey** (this is your MISP API key)
4. Note your MISP instance URL (e.g., `https://misp.example.com`)

### Step 2: Create Sekoia IOC Collection

1. Log in to Sekoia.io
2. Navigate to **Observe** > **IOC Collections**
3. Click **+ Collection**
4. Provide a name (e.g., "MISP IDS Indicators"), Description
5. If multi-tenant is activated, choose the suitable community to host the collection
6. Tic the box to create a detection rule if the objective is to raise alerts in Sekoia based on your MISP IOCs
7. Click **Next**
8. In **Text import** add an IOC manually to complete the creation of the collection. 
9. Click **Next**
10. Fulfill the threat metadata or leave it empty, then Click **Import**
11. From the URL, Copy the **IOC Collection UUID** (format: `ioc-collection--xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

### Step 3: Generate Sekoia API Key

1. In Sekoia.io, navigate to **Settings** > **Workspace** > **API Keys**
2. Select the same community select in step 2.5
3. Click **Create API Key**
4. Grant **Write** permissions to **IOC Collections**
5. Copy the generated API key

### Step 4: Configure the Trigger in Sekoia Playbooks

1. Navigate to **Playbooks** > **+ New Playbook**
2. Select the same community select in step 2.5
3. Choose **Create a playbook from scratch**
4. Provide a name (e.g., "MISP IDS Indicators to IOC Collection"), Description
5. Click **Next**
6. Click **Skip this step**
7. In the Workflow tab, click **+** icon on the left panel, open **MISP** section from the trigger tab, click on **MISP IDS Attributes to IOC Collection**
8. Create an **Account** with the following parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| **Http Proxy** | HTTP proxy URL for Private regions | `http://proxy:8080` | 
| **Https Proxy** | HTTPS proxy URL for Private regions | `https://proxy:8080` | 
| **MISP API Key** | Your MISP authentication key | `<your_misp_api_key>` |
| **MISP URL** | URL of your MISP instance | `https://misp.example.com` |
| **Sekoia API Key** | API key with write permissions | `sio_xxxxxxxxxxxxxx...` |

9. Create a **Trigger Configuration** with the following parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| **IOC Collection Server** | Sekoia API server URL of your region | `https://api.sekoia.io` |
| **IOC Collection UUID** | UUID of your IOC Collection | `ioc-collection--12345678-...` |
| **Published Timestamp** | Number of days to look back for attributes | `1` (default) |
| **Sleep Time** | Polling interval in seconds | `300` (default: 5 minutes) |

10. **Save and activate** the playbook

## Supported IOC Types

The following MISP attribute types are supported:

- `ip-dst`: Destination IP address → Sekoia `ipv4-addr.value`
- `domain`: Domain name → Sekoia `domain-name.value`
- `url`: Full URL → Sekoia `url.value`
- `sha256`: SHA-256 hash → Sekoia `file.hashes.SHA-256`
- `md5`: MD5 hash → Sekoia `file.hashes.MD5`
- `sha1`: SHA-1 hash → Sekoia `file.hashes.SHA-1`

**Note**: Only attributes with the `to_ids` flag enabled in MISP will be imported.

## How It Works

1. **Polling**: The trigger polls your MISP instance every `sleep_time` seconds
2. **Filtering**: Retrieves attributes with `to_ids=1` published within the configured time window
3. **Type Filtering**: Only supported IOC types are processed
4. **Deduplication**: Previously processed attributes are skipped using a cache
5. **Batching**: IOCs are grouped and sent to Sekoia in batches of up to 1,000 per request
6. **Storage**: IOCs are added to your IOC Collection in Sekoia

## Troubleshooting

### No IOCs are being imported

- Verify your MISP API key has read permissions
- Check that MISP events are published and contain attributes with `to_ids=1`
- Ensure the `publish_timestamp` window is appropriate (try increasing it)
- Review trigger logs in Sekoia.io for errors

### Authentication errors

- Verify MISP URL is correct and accessible
- Check MISP API key is valid and not expired
- Verify Sekoia API key has write permissions to the IOC Collection
- Ensure IOC Collection UUID is correct

### Rate limiting

- Increase the `sleep_time` parameter to reduce polling frequency
- Check MISP instance rate limits

## Best Practices

- Start with a small `publish_timestamp` value (e.g., 1 day) and increase if needed
- Monitor the trigger logs to ensure IOCs are being processed successfully
- Link the IOC Collection to appropriate detection rules in Sekoia
- Regularly review the IOC Collection to ensure relevant indicators are being imported

## Support

- [MISP Project Documentation](https://www.misp-project.org/documentation/)