uuid: 22f2afd2-c858-443d-8e06-7b335e439c29
name: CrowdStrike Falcon
type: intake

## Overview

CrowdStrike Falcon is an Endpoint Detection and Response solution. This setup guide explains how to forward and collect the detections and activity logs of your CrowdStrike EDR to Sekoia.io.

- **Vendor**: CrowdStrike
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Authentication logs


CrowdStrike Falcon integration gathers EDR logs. Below is a concise list of activities that can be monitored using CrowdStrike Falcon logs:

- Alerts raised by the EDR, with limited informations like hash, command line, IP...
- Crowdstrike Falcon Audit logs
- Crowdstrike Falcon Incident logs
- Identity protection events

## Supported events

This integration supports the following events from CrowdStrike Falcon:

- Detection Summaries (`DetectionSummaryEvent`)
- Incident Summaries (`IncidentSummaryEvent`)
- Audit logs (`UserActivityAuditEvent` and `AuthActivityAuditEvent`)
- Identity protection events (`IdpDetectionSummaryEvent` and `IdentityProtectionEvent`)
- Mobile Detection Summaries (`MobileDetectionSummaryEvent`)

This integration can also collect `Vertex` through the Threat Graph API (restricted feature, please contact Crowdstrike Support to activate it).

## Configure

### Prerequisites

The following prerequisites are needed in order to setup efficient events handling:

- Have a Falcon Administrator account


### Generate the Credentials

1. Log in to the crowdstrike interface
2. Click on the burger menu and go to `Support and resources` > `Resources and tools` > `API client and keys`.
3. In the `OAuth2 API Clients` tab, create an new OAuth2 API Client with the `Read` permission for the scopes `Event Stream` and `Detection`.

!!! Info
    To collect `Vertex`, add the `Threat Graph` scope with `Read` permission.


### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `CrowdStrike Falcon`.
2. Set up the intake configuration with the base URL of the API (e.g. https://api.eu-1.crowdstrike.com), your client id and your client secret.

{!_shared_content/operations_center/integrations/generated/22f2afd2-c858-443d-8e06-7b335e439c29_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_22f2afd2-c858-443d-8e06-7b335e439c29_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/22f2afd2-c858-443d-8e06-7b335e439c29.md!}
