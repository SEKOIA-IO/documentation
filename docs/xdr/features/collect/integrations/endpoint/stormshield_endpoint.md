uuid: f5e6cf5e-bd9f-4caf-9098-fe4a9e0aeaa0
name: Stormshield Endpoint Security
type: intake

## Overview

Stormshield Endpoint Security is a comprehensive cybersecurity solution designed to protect individual devices, such as computers and servers, from various cyber threats and attacks. It encompasses advanced features like antivirus, firewall, intrusion detection and prevention, application control, and data encryption. This solution aims to safeguard endpoints from malware, ransomware, phishing, and other malicious activities, while providing centralized management and real-time threat visibility for enhanced security posture.

{!_shared_content/operations_center/detection/generated/suggested_rules_f5e6cf5e-bd9f-4caf-9098-fe4a9e0aeaa0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f5e6cf5e-bd9f-4caf-9098-fe4a9e0aeaa0.md!}

## Configure

### Prerequisites

- Have an internal log concentrator 

### Exporting logs via Syslog

To export logs via Syslog, follow the steps below:
* Define the Syslog redirection settings in the Syslog configuration panel of the server configuration policy:
    * In the Address/Hostname field,enter the IP address of the Syslog server. 
    * In the Port field,change the port number(if necessary).
    * In the Protocol field,enter the protocol required(TCP or UDP).
    * Select a Facility level.
    * Select a Severity level.
* Validate your modifications.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Stormshield Endpoint Security.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

#### Further Readings

You can read all documentation [here](https://documentation.stormshield.eu/SES/v7.2/en/Content/PDF/ses-en-administration_guide-v7.2.pdf)
