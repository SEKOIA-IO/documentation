uuid: 23813540-b658-48dd-b030-e9b92168bbf4
name: Daspren Parad
type: intake

## Overview

Daspren is the only Data Detection and Response (DDR) that integrates detection and blocking of cyber attacks. Daspren goes deep, using our patented data-centric AI to meticulously dissect and analyze every data access. It seamlessly intercepts and scrutinizes these access requests, ensuring that only legitimate, authorized applications can access your data, keeping it secure and protected.

- **Vendor**: Daspren
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Parad is the data protection solution from Daspren. It monitors data activity and use AI to prevent data breaches coming from both the inside and the outside of your organization:
    - File created, opened, deleted, moved or modified,
    - Access rules breach attempts,
    - Malicious processes detected.

!!! Warning
    This format is currently in beta. We highly value your feedback to improve its performance.

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)

## Specification

### Prerequisites

- **Permissions**: Administrator or Root access to the Parad CLI

### Transport Protocol/Method

- **Direct HTTP**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Informational

!!! Note
    This is a description of the log level based on the taxonomy of the [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424) for standardization purpose. Please adapt to the wording used by the editor.

## Step-by-Step Configuration Procedure

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Instructions on the 3rd Party Solution

  1. **Open the Parad CLI**:
  2. **Create a Sink from the CLI**:
    - Go to `Sinks > Add Sink`.
    - Select the Sekoia Sink Variant.
    - Type a `Name` and paste the `Intake key` from the previous step.
  3. **Create a Reporter from the CLI**:
    - Go to `Reporters > Add Reporter`.
  4. **Create a Link**:
    - Link the previously created Sink and Reporter.

{!_shared_content/operations_center/integrations/generated/23813540-b658-48dd-b030-e9b92168bbf4_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_23813540-b658-48dd-b030-e9b92168bbf4_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/23813540-b658-48dd-b030-e9b92168bbf4.md!}
