---
uuid: 62e667fa-f143-42ef-bc52-3f2e86f0013c
name: CyberRisk Analysis
type: intake
---

## Overview

LocateRisk is a specialist for automated IT risk analysis and monitoring. The Cyberrisk Analysis report contains vulnerabilities discovered by LocateRisk's cyber risk analysis platform, including network, web, DNS, and application findings detected per host with their CVSS and EPSS context.

- **Vendor**: LocateRisk
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**:
    - Vulnerability findings (network, web, DNS, application)
    - Risk scoring context (CVSS and EPSS)

## Configure

### Prerequisites

Before starting, ensure you have:

- A LocateRisk account with API access on [app.locaterisk.com](https://app.locaterisk.com)
- A LocateRisk API key
- The identifier (`scan_id`) of the LocateRisk scan you want to ingest
- An intake key from your Sekoia.io CyberRisk Analysis intake

### Configuration Procedure

#### 1. Create an API token in LocateRisk

1. Log in to your LocateRisk account
2. Generate a personal API key from the account settings
3. Copy the API key
4. Note the identifier (`scan_id`) of the scan you want to ingest findings from

#### 2. Create a LocateRisk intake in Sekoia.io

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes) and follow these steps:

1. Click on **+ Intake** to create a new one
2. Search for the **CyberRisk Analysis** format, give it a name and choose the relevant Entity
3. Click on **Create**

#### 3. Configure connector parameters

Mandatory parameters:

- **API key**: the LocateRisk API key generated in the previous section
- **Scan ID**: the identifier of the LocateRisk scan to export

Optional parameters:

- **Report URL**: base URL of the LocateRisk report export endpoint. Default: `https://app.locaterisk.com/api/rest/report/export`
- **Polling interval**: how often, in minutes, the connector polls LocateRisk for new findings. Default: `5`

Once configured, the connector polls the scan report as CSV from `<report_url>/<scan_id>/csv`, parses each row as a finding, tags events with `source=locaterisk`, and ingests them as structured events.

### Validation

1. Verify that the connector starts successfully from the intake page.
2. Confirm that findings appear on the [Events page](https://app.sekoia.io/operations/events).
3. On subsequent polls, unchanged rows are not resent; only new or changed rows are ingested.

### Behavior Notes

- The report is polled as a full snapshot at each cycle.
- To avoid duplicates, only new or changed rows are forwarded after the first successful poll.
- The connector accepts only HTTPS values for `report_url`.

### Troubleshooting

- **401/403 errors**: verify that your API key is valid and still authorized in LocateRisk.
- **404 errors**: verify that `scan_id` and `report_url` target a valid LocateRisk report export endpoint.
- **No events after initial ingestion**: if the report has not changed, this behavior is expected due to row-level deduplication.

{!_shared_content/operations_center/integrations/generated/62e667fa-f143-42ef-bc52-3f2e86f0013c_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_62e667fa-f143-42ef-bc52-3f2e86f0013c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/62e667fa-f143-42ef-bc52-3f2e86f0013c.md!}

## Further Readings

- [LocateRisk website](https://www.locaterisk.com)
