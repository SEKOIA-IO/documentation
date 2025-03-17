---
uuid: 7f89b1b9-de7f-4e2c-bcef-4d7ddfc91d31
name: Wiz Audit Logs
type: intake
---

## Overview

- **Supported environment**: SaaS
- **Detection based on**: Audit
- **Supported application or feature**:
    - Audit Logs

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Configure

### Pre-requisite

To setup the integration, you need to have access to `Wiz Console`.

### Create Client ID and Client Secret

- Log in the Wiz console
- Go to `Settings` > `Service Accounts`
- Type a name for the new service account. e.g: [Sekoia.io](http://Sekoia.io) Integration
- Select `admin:audit` permission
- Click `Add Service Account`
- Copy the Client ID and the Client Secret

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format **Wiz Audit Logs**.

{!_shared_content/operations_center/integrations/generated/7f89b1b9-de7f-4e2c-bcef-4d7ddfc91d31_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_7f89b1b9-de7f-4e2c-bcef-4d7ddfc91d31_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/7f89b1b9-de7f-4e2c-bcef-4d7ddfc91d31.md!}
