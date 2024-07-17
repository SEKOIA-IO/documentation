uuid: XXXX
name: YYYY
type: intake
last updated: DD/MM/YYYY

## Overview

- **Vendor**:
- **Plan**: Defend Core / Defend Prime
- **Supported environment**: On Premise / SaaS
- **Version compatibility, if applicable**:

- **Detection based on**: Telemetry / Security Alerts / Audit
- **Supported application or feature**:
- **Coverage Score**:

## High-Level Architecture Diagram

- **Type of integration**: Inbound (PULL from Sekoia.io) / Outbound(PUSH to Sekoia.io)

- **Schema**

![<technology_name>_architecture](/assets/integration/<technology_name>_architecture.png)

!!! Alternative

    This will not be detailed in this documentation, but logs can also be sent directly to Sekoia.io over HTTPS using the Sekoia.io Endpoint Agent and the "Collect logs in files" method. This provides an alternative to the specified syslog collection method and may be preferable in certain environments.

## Specification

### Prerequisites

- **Licence level**:
    - Y
    - X

- **Resource**:
    - External Storage
    - Self-managed syslog forwarder

- **Network**:
    - Inbound traffic allowed
    - Outbound traffic allowed

- **Permissions**:
    - API Credentials: _TO REPLACE Minimum level of permissions needed for API key or service account._
    - Configuration Access:  _ Minimum level of permissions required for the user doing the configuration._
    - Service account permission: The service account permission needed for the configuration of the intake in the Sekoia.io product.

### Transport Protocol/Method

- **Cloud Storage**: Amazon S3 Bucket / Microsoft Azure Eventhub / Microsoft Azure BlobStorage / Google Pub/Sub
- **Direct HTTP**
- **Direct Syslog**
- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF / Common Log Format (CLF) / Delimiter Separated Value (DSV) / JSON / Key-Value / Plain Text / Multi-line

- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

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

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

__TO REMOVE IF NOT RELEVANT__
{!_shared_content/integration/connector_configuration.md!}

__TO REMOVE IF NOT RELEVANT__
{!_shared_content/integration/forwarder_configuration.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_bf8867ee-43b7-444c-9475-a7f43754ab6d_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d6d15297-e977-4584-9bb3-f0290b99f014.md!}

## Further readings

- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/__CHANGE_ME__).
- The code of the Playbook connector is available [here](https://github.com/SEKOIA-IO/automation-library/tree/main/__CHANGE_ME__).
