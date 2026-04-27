uuid: 042ca68e-dbdd-4646-8d9d-01ca28882c3f
name: Akamai Guardicore On-Premises
type: intake

## Overview

Akamai Guardicore delivers application-centric microsegmentation and breach detection to prevent lateral movement across on-premises and
cloud environments.
With process-level visibility, dynamic policy orchestration and automated workflows, it enforces Zero Trust controls at scale.
Simplify network segmentation, accelerate threat response and maintain continuous compliance for critical assets.

- **Vendor**: Akamai
- **Supported environment**: On-Premises
- **Version compatibility**: V51
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: see section below

!!! Warning
	Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Akamai Guardicore event types supported
Here is a list of all the Akamai Guardicore event types supported by this integration:

* Incident
* Audit log
* Network log

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Akamai Guardicore Console
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: CEF
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Configure

This setup guide will show you how to forward your Akamai Guardicore events to Sekoia.io.

## Steps to follow

- Create an intake
- Set up the forwarding for Events
- Set up the forwarding for Network Logs

### Instructions on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

### Set up the forwarding for Events

- Log in to the Akamai Guardicore console
- In the left panel, go to `System` > `INTEGRATION` > `Data Exporters`

  ![Step 01](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 01.png){: style="max-width:100%"}

- Click `+ Create Data Exporter`

  ![Step 02](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 02.png){: style="max-width:100%"}

- Select `Events syslog Exporter`
- Type a name for the exporter configuration (e.g: `Sekoia.io Events exporter`)
- In the `Connection options` section:
    - Type the address of the syslog concentrator as `Syslog host`
    - Type the port of the syslog concentrator as `Syslog port`
    - Select the matching protocol for the syslog concentrator as `Syslog protocol`
    - Disable `Verify host`

    ![Step 03 on-premises](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 03 onprem.png){: style="max-width:100%"}

- In the `Exporting options` section:
    - Enable `Export incidents`
    - Disable `Export Agent Logs`
    - Enable `Audit Logs`

    ![Step 04](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 04.png){: style="max-width:100%"}

- In the `Message format` section:
    - Select `CEF` as `Message format`
    - Select `ISO8601 (including milliseconds)` as `Format log timestamp`
    - Click `Test Connection`
    - Click `Save`

    ![Step 05 on-premises](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 05 onprem.png){: style="max-width:100%"}

### Set up the forwarding for Network logs

- Click `+ Create Data Exporter`

  ![Step 02](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 02.png){: style="max-width:100%"}

- Select `Network Log syslog Exporter`
- Type a name for the exporter configuration (e.g: `Sekoia.io Network Log exporter`)
- In the `Connection options` section:
    - Type the address of the syslog concentrator as `Syslog host`
    - Type the port of the syslog concentrator as `Syslog port`
    - Select the matching protocol for the syslog concentrator as `Syslog protocol`
    - Disable `Verify host`

    ![Step 06 on-premises](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 06 onprem.png){: style="max-width:100%"}

- In the `Exporting options` section:
    - Click `+ Add`
    - Create `export verdicts` for:
        - `Allowed`
        - `Blocked`
        - `Alerted`
        - `Allowed and Encrypted`

    ![Step 07](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 07.png){: style="max-width:100%"}

- In the `Message format` section:
    - Select `CEF` as `Message format`
    - Select `ISO8601 (including milliseconds)` as `Format log timestamp`
    - Click `Test Connection`
    - Click `Save`

    ![Step 05 on-premises](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 05 onprem.png){: style="max-width:100%"}


{!_shared_content/operations_center/integrations/generated/042ca68e-dbdd-4646-8d9d-01ca28882c3f_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_042ca68e-dbdd-4646-8d9d-01ca28882c3f_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/042ca68e-dbdd-4646-8d9d-01ca28882c3f.md!}

## Troubleshooting

### No event is received

In the Akamai Guardicore console, for each data exporter for Sekoia.io, check, in the `Message format` section:

- `ISO8601 (including milliseconds)` is selected as `Format log timestamp`
