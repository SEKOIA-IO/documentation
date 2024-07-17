uuid: 903ec1b8-f206-4ba5-8563-db21da09cafd
name: Palo Alto
type: intake

## Overview

Palo Alto Networks offers an enterprise cybersecurity platform which provides network security, cloud security, endpoint protection, and various cloud-delivered security services.


{!_shared_content/operations_center/detection/generated/suggested_rules_903ec1b8-f206-4ba5-8563-db21da09cafd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/903ec1b8-f206-4ba5-8563-db21da09cafd.md!}

## Configure

On Palo Alto appliances, most of the important hardward and software activities that are relevant for security detection and analysis, are logged into three files.

- Traffic: Local out traffic, Denied traffic, Allowed traffic
- System
- Security

### Create the intake on Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Palo Alto Next-Generation Firewall`

### Send events to Sekoia.io

#### Forward events through syslog

##### Prerequisites

The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator priviledge on the Palo Alto
- Traffic towards the Rsyslog must be open on `TCP/514`

##### Configure Palo Alto NGFW

###### Configure a Syslog server profile

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

###### Configure syslog forwarding for Traffic logs

1. Select `Objects > Log Forwarding`, click `Add`, and enter a `Name` to identify the profile.
2. For each log type (here Traffic, Threat and WileFire Malicious) and each severity level, select the `Syslog server` profile and click `OK`.
3. Select `Policies > Security` and select a policy rule.
4. Select the `Actions` tab and select the `Log Forwarding` profile you created.
5. In the `Profile Type` drop-down, select `Profiles` or `Groups`, and then select the security profiles or `Group Profiles` required to trigger log generation and forwarding.
6. Select both of the `Log at Session Start` and `Log At Session End` check boxes, and click `OK`.

For detailed information about configuring a log forwarding profile and assigning the profile to a policy rule, see [Configure Log Forwarding](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/monitoring/configure-log-forwarding.html#id1443a62b-8a0b-41db-a08d-5df934bf0ffc)

###### Configure syslog forwarding for System and User-ID logs

1. In the GUI, go to `Device > Log Settings`.
2. Click each Severity level (High and Critical if also fine), select the `Syslog server` profile, and click `OK`.

#### Forward logs to Sekoia.io

Please refer to the documentation of the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

### Forward events through Palo Alto Cortex Data Lake

#### Configure Palo Alto NGFW

1. In the GUI, go to `Objects > Log Forwarding`.
2. Click `Add`, and enter a `Name` to identify the profile.
3. For each log type (here Traffic, Threat and WileFire Malicious), check the box `Cortex Data Lake` in the Forward Method and click `OK`.
4. Select `Policies > Security` and select a policy rule.
5. Select the `Actions` tab and select the `Log Forwarding` profile you created.
6. In the `Profile Type` drop-down, select `Profiles` or `Groups`, and then select the security profiles or `Group Profiles` required to trigger log generation and forwarding.
7. Select both of the `Log at Session Start` and `Log At Session End` check boxes, and click `OK`.

#### Configure Palo Alto Cortex Data Lake

1. On the Cortex Data Lake console, got to `Log Forwarding`
2. Create a new HTTPS Profiles
3. Enter a `Name` to identify the profile and set the URL to `https://intake.sekoia.io/jsons?status_code=200`
4. In the Client Authorization section, select `Basic Authorization` as Type, fill `Username` with any string (e.g. `sekoiaio`) and `Password` with your intake key
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

### Enjoy your events
Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.
