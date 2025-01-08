uuid: 903ec1b8-f206-4ba5-8563-db21da09cafd
name: Palo Alto Next-Generation Firewall
type: intake

## Overview

Palo Alto Networks offers an enterprise cybersecurity platform which provides network security, cloud security, endpoint protection, and various cloud-delivered security services.

- **Vendor**: Palo Alto
- **Supported environment**: On Premise
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**: Traffic, Threat and WildFire Malicious

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder

	OR

	- Palo Alto Strata Logging Service (formely Palo Alto Cortex Data Lake)

- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on Palo Alto Firewall
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CSV, CEF
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure
### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Instructions on the 3rd Party Solution

#### Option A - Forward events through a Syslog Forwarder

##### Configure a Syslog server profile

1. In the GUI, go to `Device > Serve Profiles > Syslog`.
2. Click `Add` and enter a name for the profile such as `Syslog server`.
3. If the firewall has more than one virtual system (vsys), select the `Location` (vsys or `Shared`) where this profile is available.
4. Click `Add` and enter the information that the firewall requires to connect to it:

	- Name — Unique name for the server profile.
	- Syslog Server — IP address or fully qualified domain name (FQDN) of the syslog server.
	- Transport — Select TCP.
	- Port — Select the default is TCP on port 514.
	- Format — Select the syslog message format to use: IETF
	- Facility — Select a syslog standard value (default is LOG_USER) to calculate the priority (PRI) field.

5. Click `OK` to save the server profile.

##### Configure syslog forwarding for Traffic logs

1. Select `Objects > Log Forwarding`, click `Add`, and enter a `Name` to identify the profile.
2. For each log type (here Traffic, Threat and WileFire Malicious) and each severity level, select the `Syslog server` profile and click `OK`.
3. Select `Policies > Security` and select a policy rule.
4. Select the `Actions` tab and select the `Log Forwarding` profile you created.
5. In the `Profile Type` drop-down, select `Profiles` or `Groups`, and then select the security profiles or `Group Profiles` required to trigger log generation and forwarding.
6. Select `Log At Session End` check boxes, and click `OK`.

!!! Warning
	Log At Session Start consumes more resources than logging only at the session end. In most cases, you only Log At Session End. Enable both Log At Session Start and Log At Session End only for troubleshooting, for long-lived tunnel sessions such as GRE tunnels (you can't see these sessions in the ACC unless you log at the start of the session), and to gain visibility into Operational Technology/Industrial Control Systems (OT/ICS) sessions, which are also long-lived sessions.

For detailed information about configuring a log forwarding profile and assigning the profile to a policy rule, see [Configure Log Forwarding](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/configure-log-forwarding#id1443a62b-8a0b-41db-a08d-5df934bf0ffc_idd40c0d1a-7191-4616-9573-f02a99352eae)

##### Configure syslog forwarding for System, Configuration, GlobalProtect, HIP Match, and User-ID logs.

1. In the GUI, go to `Device > Log Settings`.
2. Click each Severity level (High and Critical if also fine), select the `Syslog server` profile, and click `OK`.

Please follow [Configure Log Forwarding](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/configure-log-forwarding#id1443a62b-8a0b-41db-a08d-5df934bf0ffc_idd40c0d1a-7191-4616-9573-f02a99352eae) from the official Palo Alto documentation for more information.

{!_shared_content/integration/forwarder_configuration.md!}

### Option B - Forward events through Palo Alto Strata Logging Service

#### Configure Palo Alto NGFW

1. In the GUI, go to `Objects > Log Forwarding`.
2. Click `Add`, and enter a `Name` to identify the profile.
3. For each log type (here Traffic, Threat and WileFire Malicious), check the box `Strata Logging Service` (or `Cortex Data Lake`) in the Forward Method and click `OK`.
4. Select `Policies > Security` and select a policy rule.
5. Select the `Actions` tab and select the `Log Forwarding` profile you created.
6. In the `Profile Type` drop-down, select `Profiles` or `Groups`, and then select the security profiles or `Group Profiles` required to trigger log generation and forwarding.
7. Select both of the `Log at Session Start` and `Log At Session End` check boxes, and click `OK`.

#### Configure Palo Alto Strata Logging Service

1. On the Strata Logging Service console, go to `Log Forwarding`
2. In the `Https` section, click `+` to create a new HTTPS Profiles
3. Enter a `Name` to identify the profile and set the URL to `https://intake.sekoia.io/jsons?status_code=200`
4. In the Client Authorization section, select `Basic Authorization` as Type, fill `Username` with any string (e.g. `sekoiaio`) and `Password` with your **intake key** (see step "Instruction on Sekoia")
5. Click `Test Connection` then click `Next`
6. Select `Array JSON` as Payload Format
7. In `Filters`, add log sources to forward:

	|  Log Source   |  Log Type      |
	| ------------- | -------------- |
	| Common Logs   | System         |
	| Common Logs   | Configuration  |
	| Firewall Logs | Authentication |
	| Firewall Logs | Decryption     |
	| Firewall Logs | DNS Security   |
	| Firewall Logs | File           |
	| Firewall Logs | GlobalProtect  |
	| Firewall Logs | HIP Match      |
	| Firewall Logs | IPtag          |
	| Firewall Logs | SCTP           |
	| Firewall Logs | Threat         |
	| Firewall Logs | Traffic        |
	| Firewall Logs | Tunnel         |
	| Firewall Logs | URL            |
	| Firewall Logs | UserID         |

8. Click `Save`

{!_shared_content/operations_center/integrations/generated/903ec1b8-f206-4ba5-8563-db21da09cafd_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_903ec1b8-f206-4ba5-8563-db21da09cafd_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/903ec1b8-f206-4ba5-8563-db21da09cafd.md!}
