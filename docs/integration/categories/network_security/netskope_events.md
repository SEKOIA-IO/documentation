uuid: de9ca004-991e-4f5c-89c5-e075f3fb3216
name: Netskope Events
type: intake


## Overview

[Netskope](https://www.netskope.com/) is a cybersecurity company that provides solutions to protect data in cloud apps and network security while applying zero trust principles.

- **Vendor**: Netskope
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: authentications and activities in your Cloud applications

## Step-by-Step Configuration Procedure

This setup guide will lead you into forwarding netskope's events to Sekoia.io.

!!! Important
    This integration will collect events from the APIv2 of the Netskope platform.

### Instructions on the 3rd Party Solution
#### Generate API token

Please follow [this guide](https://docs.netskope.com/en/rest-api-v2-overview-312207.html) to create an API token.

To the API token, add the following endpoints with the privilege `Read`:

Events:

- /api/v2/events/dataexport/events/page
- /api/v2/events/dataexport/events/application
- /api/v2/events/dataexport/events/incident
- /api/v2/events/dataexport/events/audit
- /api/v2/events/dataexport/events/infrastructure
- /api/v2/events/dataexport/events/network

Alerts:

- /api/v2/events/dataexport/alerts/dlp
- /api/v2/events/dataexport/alerts/watchlist
- /api/v2/events/dataexport/alerts/ctep
- /api/v2/events/dataexport/alerts/compromisedcredential
- /api/v2/events/dataexport/alerts/malsite
- /api/v2/events/dataexport/alerts/malware
- /api/v2/events/dataexport/alerts/policy
- /api/v2/events/dataexport/alerts/remediation
- /api/v2/events/dataexport/alerts/quarantine
- /api/v2/events/dataexport/alerts/securityassessment
- /api/v2/events/dataexport/alerts/uba

### Instruction on Sekoia

#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Netskope`.
2. Set the intake configuration using:
    * Your Netskope base url 
    * Your API Token
    * A consumer group (optional)
    * `Security check only` (optional): when enabled, the connector collects only the security-check alerts — `malware` (Cloud Sandbox), `malsite` (Malicious sites) and `dlp` (DLP). Leave it disabled (default) to collect all supported events and alerts.

!!! note
    By default the connector collects all the event types (`page`, `application`, `incident`, `audit`, `infrastructure`, `network`) and all the alert types (`dlp`, `watchlist`, `ctep`, `compromisedcredential`, `malsite`, `malware`, `policy`, `remediation`, `quarantine`, `securityassessment`, `uba`). Security-check alerts (`malware`, `malsite`, `dlp`) — raised by Netskope's sandbox analysis on suspicious browsing or malware downloads — are part of this default collection. Enable `Security check only` to restrict the connector to those three alert types.

{!_shared_content/operations_center/integrations/generated/de9ca004-991e-4f5c-89c5-e075f3fb3216_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_de9ca004-991e-4f5c-89c5-e075f3fb3216_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/de9ca004-991e-4f5c-89c5-e075f3fb3216.md!}

## Further Readings

- [Netskope documentation - create an API token](https://docs.netskope.com/en/rest-api-v2-overview-312207.html)
