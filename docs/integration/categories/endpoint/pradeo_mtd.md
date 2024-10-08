uuid: 3cedbe29-02f8-42bf-9ec2-0158186c2827
name: Pradeo MTD
type: intake

## Overview

Pradeo Mobile Threat Defense (MTD) is a comprehensive security solution designed to protect mobile devices from various threats such as malware, phishing, and network attacks. This setup guide explains how to forward and collect the detections and activity logs of your Pradeo MTD to Sekoia.io.

- **Vendor**: Pradeo
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: 
    - Detections
    - Audit Events

## Specification

### Prerequisites

- **Permissions**:
    - Administrator access to the Pradeo Security console


## Step-by-Step Configuration Procedure


### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Instructions on the 3rd Party Solution

This setup guide will show you how to forward events from Pradeo Security to Sekoia.io.

#### Set up the Integration in Pradeo Security Console

   1. Log in to the Pradeo Security platform.
   2. From the main dashboard, select `Integration` option.
   3. Click `SIEM Integrations`.
   4. Select `Sekoia` as your preferred SIEM system.
   5. Copy the intake key in the appropriate input.
   6. Select `Detections` and `Audit logs` as event types.
   7. Select the desired fields to export.
   8. Save your configuration.

{!_shared_content/operations_center/integrations/generated/3cedbe29-02f8-42bf-9ec2-0158186c2827_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_3cedbe29-02f8-42bf-9ec2-0158186c2827_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3cedbe29-02f8-42bf-9ec2-0158186c2827.md!}
