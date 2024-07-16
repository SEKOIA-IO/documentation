uuid: XXXX
name: YYYY
type: intake
last updated: DD/MM/YYYY

## Overview

- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise / SaaS
- **Version compatibility, if applicable**:

- **Detection based on**: Telemetry / Security Alerts / Audit
- **Supported application or feature**:
    - A
    - B
    - C


## High-Level Architecture Diagram

- **Type of integration**: Inbound: PULL from Sekoia.io / Outbound: PUSH to Sekoia.io

- **Schema**

![consume_azure_logs](/assets/integration/integration_catalog/<techno_name>/image.png)

## Configure Section

### Prerequisites

- **Licence level**:
    - [ ] Y
    - [ ] X

- **Resource**:
    - [ ] External Storage
    - [ ] Self managed syslog forwarder
    - [ ] None

- **Network**:
    - [ ] Customer Inbound traffic possible opening
    - [ ] Customer Outbound traffic possible opening
    - [ ] None

- **Permissions**:
    - [ ] API Credentials: _TO REPLACE Minimum level of permissions needed for API key or service account._
    - [ ] Configuration Access:  _ Minimum level of permissions required for the user doing the configuration._
    - [ ] Service account permission: The service account permission needed  for the configuration of the intake in the Sekoia.io product.
    - [ ] None

### Transport Protocol/Method

- **Cloud Storage**: Amazon S3 Bucket / Microsoft Azure Eventhub / Microsoft Azure BlobStorage / Google Pub/Sub
- **Direct HTTP**
- **Direct Syslog**
- **Indirect Syslog**

### Logs details

- **Supported type(s) of structure**:
    - [ ] CEF
    - [ ] Common Log Format (CLF)
    - [ ] Delimiter Separated Value (DSV)
    - [ ] JSON
    - [ ] Key-Value
    - [ ] Plain Text
    - [ ] Multi-line

- **Supported verbosity level**:
    - [ ] **Emergency**: system is unusable
    - [ ] **Alert**: action must be taken immediately
    - [ ] **Critical**: critical conditions
    - [ ] **Error**: error conditions
    - [ ] **Warning**: warning conditions
    - [ ] **Notice**: normal but significant condition
    - [ ] **Informational**: informational messages
    - [ ] **Debug**: debug-level messages

!!! Note
    This is a description of the log level based on the taxonomy of the [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424) for standardization purpose. Please adapt to the wording used by the editor.

- **Supported functionalities**: See section "Supported application or feature" on top of this page.
- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd party solution

__TO ADAPT__
- Detailed Procedure: Provide a detailed step-by-step guide to configure log collection with explicit events types supported by the format if needed.-
- Event Categories: List explicit event types supported by the format (e.g., Fortigate: forward-traffic, local-traffic, multicast-traffic, vpn, web, url-filter).
- Event Selection: Guidance on selecting event types when sending logs.
---> Visual Aids: Include screenshots or videos if possible.

### Instruction on Sekoia

__TO REMOVE IF NOT RELEVANT__

{!_shared_content/integration/intake_configuration.md!}

__TO REMOVE IF NOT RELEVANT__
{!_shared_content/integration/connector_configuration.md!}

### Setup a syslog forwarder (if needed)

- Encourage to use the Sekoia.io forwarder

## Detection section

_TO REPLACE by current links about Detection rules available, List of event types, List of extracted fields_

{!_shared_content/operations_center/detection/generated/suggested_rules_bf8867ee-43b7-444c-9475-a7f43754ab6d_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d6d15297-e977-4584-9bb3-f0290b99f014.md!}

## Further readings


- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/__CHANGE_ME__).
- The code of the Playbook connector is available [here](https://github.com/SEKOIA-IO/automation-library/tree/main/__CHANGE_ME__).

