uuid: 60af2bd6-7ef0-48a7-a6db-90fcdd7236f1
name: FortiMail
type: intake

## Overview

Fortinet cybersecurity solutions sells physical products such as firewalls, plus software and services such as anti-virus protection, intrusion prevention systems and endpoint security components.


{!_shared_content/operations_center/detection/generated/suggested_rules_60af2bd6-7ef0-48a7-a6db-90fcdd7236f1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/60af2bd6-7ef0-48a7-a6db-90fcdd7236f1.md!}

## Configure

### FortiMail logs

On FortiMail appliances, most of the important hardware and software activities that are relevant for security detection and analysis, are logged into six files.

- History (statistics): Records all email traffic going through the FortiMail unit.
- System Event (kevent): Records system management activities, including changes to the system configuration as well as administrator and user log in and log outs.
- Mail Event (event): Records mail activities.
- Antispam (spam): Records spam detection events.
- Antivirus (virus): Records virus intrusion events.
- Encryption (encrypt): Records detection of IBE-related events.

## Transport to the collector

### Prerequisites
The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator privileges on the FortiMail appliance
- Traffic towards the syslog must be open on `UDP 514`

### Configure FortiMail

#### Configure logging to a syslog server

1. Go to `Log and Report > Log Settings > Remote`.
2. Click `New` to create a new entry OR double-click an existing entry to modify it. *A dialog appears*.
3. Select `Enable` to allow logging to a remote host.
4. In `Profile name`, enter a profile name.
5. In `IP`, enter the IP address of the `Syslog server` where the FortiMail unit will store the logs.
6. In `Port`, enter the UDP port number on which the Syslog server listens for connections (by default, `UDP 514`).
7. From `Level`, select the severity level that a log message must equal or exceed in order to be recorded to this storage location.
8. From `Facility`, select the facility identifier that the FortiMail unit will use to identify itself when sending log messages.

> To easily identify log messages from the FortiMail unit when they are stored on a remote logging server, enter a unique facility identifier, and verify that no other network devices use the same facility identifier.

9. From `Log protocol`, select `Syslog`.
10. In `Logging Policy Configuration`, enable the types of logs you want to record to this storage location. `Click the arrow to review the options`.
11. Click `Create`.

For detailed information about configuring a log forwarding, see [Configure FortiMail Log Forwarding](https://docs.fortinet.com/document/fortimail/6.2.0/administration-guide/332364/configuring-logging#logging_2063907032_1949484)

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
