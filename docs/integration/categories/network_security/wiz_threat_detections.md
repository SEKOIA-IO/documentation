---
uuid: 016fda46-6c98-4c2d-855e-d3fd74d86cb4
name: Wiz Threat Detections
type: intake
---

## Overview

- **Supported environment**: SaaS
- **Detection based on**: Alerts
- **Supported application or feature**:
    - Threat Detection

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Configure

### Pre-requisite

To setup the integration, you need to have access to `Wiz Console`.

### Create Client ID and Client Secret

- Log in the Wiz console
- Go to `Settings` > `Service Accounts`
- Type a name for the new service account. e.g: [Sekoia.io](http://Sekoia.io) Integration
- Select next permissions:
    - `read:detection`
    - `read:cloud_events_cloud`
    - `read:cloud_events_sensor`
    - `read:security_scans`
- Click `Add Service Account`
- Copy the Client ID and the Client Secret

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format **Wiz Threat Detections**.

{!_shared_content/operations_center/integrations/generated/016fda46-6c98-4c2d-855e-d3fd74d86cb4_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_016fda46-6c98-4c2d-855e-d3fd74d86cb4_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/016fda46-6c98-4c2d-855e-d3fd74d86cb4.md!}
