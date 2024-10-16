uuid: ea265b9d-fb48-4e92-9c26-dcfbf937b630
name: Palo Alto Prisma Access
type: intake

## Overview

Palo Alto Prisma Access is a cloud-delivered security platform that provides secure access to applications and data, using a scalable network to protect users and devices across all locations. It integrates advanced threat prevention and access controls to ensure consistent security policies.

- **Vendor**: Palo Alto
- **Supported environment**: Cloud
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**: Traffic, Threat and WildFire Malicious

## Specification

### Prerequisites

- **Resource**:
	- Palo Alto Strata Logging
- **Permissions**:
    - Administrator rights on Palo Alto Stata Logging

### Transport Protocol/Method

- **HTTPS forwarding**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Informational

## Step-by-Step Configuration Procedure
### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Forward events through Palo Alto Strata Logging

Palo Alto Prima Access forwards all logs to the Strata Logging Service.

#### Configure Palo Alto Strata Logging

1. On the Strata Logging console, got to `Log Forwarding`
2. Create a new HTTPS Profiles
3. Enter a `Name` to identify the profile and set the URL to `https://intake.sekoia.io/jsons?status_code=200`
4. In the Client Authorization section, select `Basic Authorization` as Type, fill `Username` with any string (e.g. `sekoiaio`) and `Password` with your **intake key** (see step "Instruction on Sekoia")
5. Click `Test Connection` then click `Next`
6. Select `Array JSON` as Payload Format
7. In `Filters`, add log sources to forward:

	|  Log Source   |  Log Type      |
	| ------------- | -------------- |
	| Common Logs   | System         |
	| Common Logs   | Configuration  |
	| Network Logs  | Authentication |
	| Network Logs  | Decryption     |
	| Network Logs  | DNS Security   |
	| Network Logs  | File           |
	| Network Logs  | GlobalProtect  |
	| Network Logs  | HIP Match      |
	| Network Logs  | IPtag          |
	| Network Logs  | SCTP           |
	| Network Logs  | Threat         |
	| Network Logs  | Traffic        |
	| Network Logs  | Tunnel         |
	| Network Logs  | URL            |
	| Network Logs  | UserID         |

8. Click `Save`

{!_shared_content/operations_center/integrations/generated/ea265b9d-fb48-4e92-9c26-dcfbf937b630_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ea265b9d-fb48-4e92-9c26-dcfbf937b630_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/ea265b9d-fb48-4e92-9c26-dcfbf937b630.md!}
