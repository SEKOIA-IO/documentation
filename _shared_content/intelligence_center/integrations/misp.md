# External Integrations: MISP Feed

The default feed is available as a MISP feed.

It can be added to an existing MISP instance by following [MISP's documentation](https://www.circl.lu/doc/misp/managing-feeds/).

To fetch Sekoia.io's MISP feed, you'll have to generate an API key with the `INTHREAT_READ_OBJECTS` permission. Please read the "[Generate API keys](/getting_started/manage_api_keys.md)" page to understand how to create a new API key with the proper permissions.

The following field values are required for the feed to work properly:

-   Input Source: Network
-   URL: `https://api.sekoia.io/v1/misp-gateway/misp`
-   Source Format: MISP Feed
-   Headers: `Authorization: Bearer <APIKEY>` (please replace `<APIKEY>` with the secret API key)
-   Enabled: `True`

![!Configuring Sekoia.io's MISP feed in MISP](/assets/intelligence_center/misp_feed_configuration.png){width=400px}

You then need to make sure you have a scheduled task in place to regularly fetch the feed's content.

!!! note

    MISP adds automatically the suffix `/manifest.json` to the feed URL. If you want to try the connection to the feed outside MISP or make a custom script, you need to use the following URL: `https://api.sekoia.io/v1/misp-gateway/misp/manifest.json`

The new MISP feed contains all non-expired Sekoia.io intelligence material and is constantly kept in sync with SEKOIA.IO's intelligence feed. This way, when an indicator is updated in SEKOIA.IO, that latter will be also updated in the MISP feed. This will ensure that the indicator is not duplicated each time an indicator is updated.

The MISP feed is organized by data "source" per creation date of the indicator. Hence, if an indicator has several sources, it will be included in several MISP events.

---

# MISP IDS Attributes to IOC Collection Trigger

## Overview

The MISP IDS Attributes to IOC Collection Trigger is a polling-based integration that allows organizations to automatically feed their Sekoia.io IOC (Indicator of Compromise) collections with IDS-flagged threat intelligence from their MISP platform.

This trigger periodically polls a MISP instance for attributes flagged for IDS detection and synchronizes them to Sekoia.io IOC collections, enabling seamless threat intelligence sharing between the two platforms.

## Key Features

- **Periodic Synchronization**: Automatically polls MISP for IDS-flagged attributes at configurable intervals
- **IDS-Focused**: Only retrieves attributes marked with `to_ids=True`, ensuring only detection-ready indicators are synchronized
- **Deduplication**: Built-in caching mechanism prevents duplicate IOCs from being pushed to Sekoia.io
- **Composite Type Handling**: Intelligently extracts IOC values from composite MISP attribute types (e.g., `filename|sha256`, `ip-dst|port`)
- **Batch Processing**: Efficiently pushes IOCs in batches of up to 1,000 indicators
- **Retry Logic**: Includes automatic retry with exponential backoff for rate limiting and transient errors

## How It Works

The trigger operates as a polling service that:

1. Connects to a configured MISP instance using the PyMISP library
2. Periodically queries for attributes with `to_ids=True` within a configurable time window
3. Filters attributes to only include supported IOC types
4. Extracts IOC values, handling composite types appropriately
5. Pushes the IOCs to the specified Sekoia.io collection via the API
6. Maintains a cache to prevent duplicate processing within the time window

## Requirements

- **MISP Platform**: A running MISP instance with API access enabled
- **Sekoia.io Account**: With API access and an existing IOC collection
- **Network Access**: The trigger must be able to reach both the MISP instance and Sekoia.io API

## Supported IOC Types

The trigger supports the following MISP attribute types:

| Simple Types | Composite Types |
|-------------|-----------------|
| `ip-dst` | `ip-dst\|port` |
| `domain` | `domain\|ip` |
| `url` | `filename\|sha256` |
| `sha256` | `filename\|md5` |
| `md5` | `filename\|sha1` |
| `sha1` | |

For composite types, the trigger extracts the relevant IOC portion:

- `filename|hash` types: extracts the hash value
- `ip-dst|port` and `domain|ip`: extracts the IP or domain

## Configuration Prerequisites

Before setting up the trigger, you need:

### On MISP

- A MISP API key with read permissions on attributes
- The MISP server URL (e.g., `https://misp.your-organization.com`)

### On Sekoia.io

- A Sekoia.io API key with `IOC_COLLECTIONS_WRITE` permission
- An existing IOC collection (the trigger does not create collections)
- The UUID of the target IOC collection (format: `ioc-collection--xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

## Configuration Parameters

### Module Configuration

| Parameter | Required | Description |
|-----------|----------|-------------|
| `misp_url` | Yes | MISP server URL |
| `misp_api_key` | Yes | MISP API key with read permissions |
| `sekoia_api_key` | Yes | Sekoia.io API key with IOC collection write permissions |

### Trigger Configuration

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `ioc_collection_server` | No | `https://api.sekoia.io` | Sekoia.io API server URL |
| `ioc_collection_uuid` | Yes | - | UUID of the target IOC Collection |
| `publish_timestamp` | No | `1` | Time window in days for retrieving attributes (e.g., `1` for last 24 hours, `7` for last week) |
| `sleep_time` | No | `300` | Time in seconds between polling cycles (minimum: 60 seconds) |

## Limitations

- **Collection Limit**: Each IOC collection is limited to 500,000 indicators
- **Supported Types**: Only specific MISP attribute types are supported (see table above)
- **Collection Creation**: IOC collections must be created manually in Sekoia.io before running the trigger
- **SSL Verification**: SSL verification is disabled by default for MISP connections
- **Cache Size**: The deduplication cache is limited to 10,000 entries

## Error Handling

The trigger includes robust error handling:

- **Rate Limiting (429)**: Automatic retry with exponential backoff, respecting `Retry-After` headers
- **Authentication Errors (401/403)**: Logged and reported as fatal errors
- **Collection Not Found (404)**: Logged and reported as fatal error
- **Server Errors (5xx)**: Automatic retry up to 3 times with 5-second delays
- **Network Timeouts**: Automatic retry with 5-second delays

## Example Use Case

A SOC team wants to automatically feed their Sekoia.io detection rules with IOCs from their internal MISP instance:

1. Create an IOC collection in Sekoia.io named "MISP Internal Threat Intel"
2. Configure the trigger with their MISP credentials and the IOC collection UUID
3. Set `publish_timestamp` to `7` to capture IOCs from the last week
4. Set `sleep_time` to `3600` for hourly synchronization

The trigger will then automatically keep the Sekoia.io IOC collection in sync with IDS-flagged attributes from MISP.

## For More Information

For detailed installation instructions, configuration parameters, and deployment options, please refer to the official automation library repository:

**[MISP Automation Library on GitHub](https://github.com/SEKOIA-IO/automation-library)**

The repository includes:

- Complete configuration documentation
- Docker deployment guides
- Sample configuration files
- Troubleshooting and debugging information
