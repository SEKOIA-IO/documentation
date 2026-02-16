---
uuid: de3bfaa0-8ed4-4b5a-b3fa-bd82b7744a9a
name: Wiz Issues
type: intake
---

## Overview

Wiz Cloud Issues surface and classify security risks across your cloud estate—misconfigurations, vulnerabilities, secrets exposure, and policy violations.

- **Supported environment**: SaaS
- **Detection based on**: Alerts
- **Supported application or feature**:
    - Issues

## Configure

### Pre-requisite

To setup the integration, you need to have access to `Wiz Console`.

### Create Client ID and Client Secret

- Log in the Wiz console
- Go to `Settings` > `Service Accounts`
- Type a name for the new service account. e.g: [Sekoia.io](http://Sekoia.io) Integration
- Select `read:issues` permission
- Click `Add Service Account`
- Copy the Client ID and the Client Secret

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format **Wiz Issues**.

{!_shared_content/operations_center/integrations/generated/de3bfaa0-8ed4-4b5a-b3fa-bd82b7744a9a_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_de3bfaa0-8ed4-4b5a-b3fa-bd82b7744a9a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/de3bfaa0-8ed4-4b5a-b3fa-bd82b7744a9a.md!}
