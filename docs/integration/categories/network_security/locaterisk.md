---
uuid: 35327bc2-a5aa-48ed-8e0d-96754870bf45
name: LocateRisk Cyberrisk Analysis
type: intake
---

## Overview

LocateRisk is a specialist for automated IT risk analysis and monitoring. The Cyberrisk Analysis report contains the system vulnerabilities discovered by LocateRisk's automated cyber risk analysis platform, including network, web, DNS and application findings detected per host together with their CVSS and EPSS scores.

- **Vendor**: LocateRisk
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**:
    - Vulnerability findings (network, web, DNS, application)
    - Risk scores (CVSS and EPSS)

## Configure

This setup guide will show you how to forward LocateRisk vulnerability findings to Sekoia.io.

### Pre-requisites

- A LocateRisk account with API access on [app.locaterisk.com](https://app.locaterisk.com)
- A LocateRisk scan whose findings you want to ingest

### Create an API token in LocateRisk

1. Log in to your LocateRisk account
2. Generate a personal API key from the account settings
3. Copy the API key — it is required to authenticate the connector
4. Note the identifier (`scan_id`) of the scan you want to ingest findings from

### Create your intake

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes) and follow these steps:

1. Click on **+ Intake** to create a new one
2. Search for the **LocateRisk Cyberrisk Analysis** format, give it a name and choose the relevant Entity
3. Click on **Create**
4. Provide the connector with the following parameters:
    - **API key**: the LocateRisk API key generated in the previous section
    - **Scan ID**: the identifier of the LocateRisk scan to export
    - **Report URL** *(optional)*: base URL of the LocateRisk report export endpoint. Defaults to `https://app.locaterisk.com/api/rest/report/export`
    - **Polling interval** *(optional)*: how often, in minutes, the connector polls LocateRisk for new findings. Defaults to `5`

Once configured, the connector periodically pulls the scan report as CSV from `<report_url>/<scan_id>/csv` and ingests each finding as a structured event.

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/35327bc2-a5aa-48ed-8e0d-96754870bf45_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_35327bc2-a5aa-48ed-8e0d-96754870bf45_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/35327bc2-a5aa-48ed-8e0d-96754870bf45.md!}

## Further Readings

- [LocateRisk website](https://www.locaterisk.com)
