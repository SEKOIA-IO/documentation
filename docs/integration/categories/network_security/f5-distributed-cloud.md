---
uuid: d1d24b7a-c6a7-482d-8334-affc0a11dedd
title: F5 Distributed Cloud
name: F5 Distributed Cloud
type: intake
---

## Overview

F5 Distributed Cloud is a cloud-native platform that provides integrated solutions for application delivery, security, and multi-cloud networking. The platform combines capabilities like API security, DDoS protection, bot defense, load balancing, and global traffic management with centralized visibility and control.

- **Vendor**: F5
- **Supported environment**: SaaS
- **Detection based on**: Alerts, Telemetry (API validation failures)
- **Supported application or feature**: 
    - WAF events
    - Bot detections
    - Malicious user detections
    - Service policy violations
    - API Validation failures

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)

## Specification

### Prerequisites

- **Resource**:
    - F5XC Global Log Receiver
- **Permissions**:
    - Administrator to F5XC Console

### Transport Protocol/Method

- **HTTP Receiver**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON, key-value

## Step-by-Step Configuration Procedure

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Instructions on the 3rd Party Solution

To configure F5 Distributed Cloud to send Security, Request, DNS or Audit logs, you need to follow these steps.

#### Configure a Global Log Receiver destination

1. Log in to the F5XC Console
2. Navigate to `Shared Configuration > Manage > Global Log Receiver`.
3. Create a new Global Log Receiver with the following settings :
    - Log Type: `Security Events`
    - Log Message Selection: choose the Namespace(s) from where the logs will be sent
    - Receiver Configuration: HTTP Receiver
        - HTTP Uri: https://intake.sekoia.io/plain/batch
        - Authentication: `BASIC`
            - Username: `None`
            - Password: YOUR_INTAKE_KEY
4. Save your Global Log Receiver object.

!!! warning 
    The previous URL works for the FRA1 region. For any other region, replace the domain “intake.sekoia.io” with your region’s HTTP-intake domain—for example:

    https://app.usa1.sekoia.io/api/v1/intake-http

    You can find your region’s domain here: [https://docs.sekoia.io/getting_started/regions/](https://docs.sekoia.io/getting_started/regions/)

Please find more information on how to configure remote loging [here](https://docs.cloud.f5.com/docs-v2/multi-cloud-network-connect/how-tos/others/global-log-streaming?searchQuery=global%20log%20receiver).

#### Specifically send only certain types of logs

You can create another Global Log Receiver object for each kind of log (Request, DNS and Audit)

{!_shared_content/operations_center/integrations/generated/d1d24b7a-c6a7-482d-8334-affc0a11dedd_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d1d24b7a-c6a7-482d-8334-affc0a11dedd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d1d24b7a-c6a7-482d-8334-affc0a11dedd.md!}
