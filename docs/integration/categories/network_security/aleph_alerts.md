---
uuid: ece8311e-0e93-4ca8-9aa0-4ef2e19618df
name: Aleph Alerts
type: intake
---

## Overview

Aleph Alert immediately warns you of any data leak on the Deep & Dark Webs, which expose your company to cyber attacks.

- **Vendor**: Aleph Networks
- **Supported environment**: SaaS

!!! Warning
	Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)

## Specification

### Prerequisites

- **Resource**:
    - Aleph Alerts
- **Permissions**:
    - Licence for Aleph Alerts

### Transport Protocol/Method

- **HTTP Receiver**

### Logs details

- **Supported functionalities**: Daily results
- **Supported type(s) of structure**: JSON

## Step-by-Step Configuration Procedure

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Instructions on the 3rd Party Solution

To configure Aleph Alerts to send daily generated results, you need to follow these steps.

1. Retrieve the intake key generated during the creation of the intake into Sekoia platform (refer to [Instruction on Sekoia](#Instruction on Sekoia))
2. Contact Aleph technical team
3. Give your intake key to the Aleph technical team

{!_shared_content/operations_center/integrations/generated/ece8311e-0e93-4ca8-9aa0-4ef2e19618df_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ece8311e-0e93-4ca8-9aa0-4ef2e19618df_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/ece8311e-0e93-4ca8-9aa0-4ef2e19618df.md!}
