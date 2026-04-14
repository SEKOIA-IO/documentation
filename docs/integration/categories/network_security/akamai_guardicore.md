uuid: f1eb2bd3-dd6d-4b41-b3be-80874d1bd2d5
name: Akamai Guardicore
type: intake

## Overview

Akamai Guardicore delivers application-centric microsegmentation and breach detection to prevent lateral movement across on-premises and 
cloud environments.
With process-level visibility, dynamic policy orchestration and automated workflows, it enforces Zero Trust controls at scale.
Simplify network segmentation, accelerate threat response and maintain continuous compliance for critical assets.

- **Vendor**: Akamai
- **Supported environment**: SaaS
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: see section below

!!! Warning
	Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Akamai Guardicore event types supported
Here is a list of all the Akamai Guardicore event types supported by this integration:

* Incident
* Audit log
* Network log

## Configure

This setup guide will show you how to forward your Akamai Guardicore events to Sekoia.io.

## Steps to follow

- Create an intake
- Set up the forwarding for Events
- Set up the forwarding for Network Logs

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Akamai Guardicore`. Copy the intake key.

### Set up the forwarding for Events

- Log in the Akamai Guardicore console
- With the left panel, go to `System` > `INTEGRATION` >`Data Exporters`

  ![Step 01](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 01.png){: style="max-width:100%"}

- Click `+ Create Data Exporter`

  ![Step 02](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 02.png){: style="max-width:100%"}

- Select `Events syslog Exporter`
- Type a name for the exporter configuration (e.g: `Sekoia.io Events exporter`)
- In the `Connection options` section:
    - Type `intake.sekoia.io` as `Syslog host`
    - Type `10514` as `Syslog port`
    - Select `TCP` as `Syslog protocol`
    - Enable `Use TLS`

    ![Step 03](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 03.png){: style="max-width:100%"}

!!! warning 
    The previous domain works for the FRA1 region. For any other region, replace the domain “intake.sekoia.io” with your region’s Syslog-intake domain—for example:

    intake.usa1.sekoia.io:10514

    You can find your region’s domain here: [https://docs.sekoia.io/getting_started/regions/](https://docs.sekoia.io/getting_started/regions/)

- In the `Exporting options` section:
    - Enable `Export incidents`
    - Disable `Export Agent Logs`
    - Enable `Audit Logs`

    ![Step 04](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 04.png){: style="max-width:100%"}

- In the `Message format` section:
    - Select `RFC5424` as `Message format`
    - Select `ISO8601 (including milliseconds)` as `Format log timestamp`
    - Click `Not supplied` on the `RFC5424 structured data` option
    - In the dialog
        - Paste:
        ```bash
        SEKOIA@53288 intake_key="<YOUR_INTAKE_KEY_HERE>"
        ```
        - Replace `<YOUR_INTAKE_KEY_HERE>` with the intake key created with the intake
        - Click `OK`

        ![Step 05 bis](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 05 bis.png){: style="max-width:100%"}

    - Click `Test Connection`
    - Click `Save`

    ![Step 05](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 05.png){: style="max-width:100%"}

### Set up the forwarding for Network logs

- Click `+ Create Data Exporter`

  ![Step 02](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 02.png){: style="max-width:100%"}

- Select `Network Log syslog Exporter`
- Type a name for the exporter configuration (e.g: `Sekoia.io Network Log exporter`)
- In the `Connection options` section:
    - Type `intake.sekoia.io` as `Syslog host`
    - Type `10514` as `Syslog port`
    - Select `TCP` as `Syslog protocol`
    - Enable `Use TLS`

    ![Step 06](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 06.png){: style="max-width:100%"}

!!! warning 
    The previous domain works for the FRA1 region. For any other region, replace the domain “intake.sekoia.io” with your region’s Syslog-intake domain—for example:

    intake.usa1.sekoia.io:10514

    You can find your region’s domain here: [https://docs.sekoia.io/getting_started/regions/](https://docs.sekoia.io/getting_started/regions/)

- In the `Exporting options` section:
    - Click `+ Add`
    - Create `export verdicts` for:
        - `Allowed`
        - `Blocked`
        - `Alerted`
        - `Allowed and Encrypted`

    ![Step 07](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 07.png){: style="max-width:100%"}

- In the `Message format` section:
    - Select `RFC5424` as `Message format`
    - Select `ISO8601 (including milliseconds)` as `Format log timestamp`
    - Click `Not supplied` on the `RFC5424 structured data` option
    - In the dialog
        - Paste:
        ```bash
        SEKOIA@53288 intake_key="<YOUR_INTAKE_KEY_HERE>"
        ```
        - Replace `<YOUR_INTAKE_KEY_HERE>` with the intake key created with the intake
        - Click `OK`

        ![Step 05 bis](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 05 bis.png){: style="max-width:100%"}

    - Click `Test Connection`
    - Click `Save`

    ![Step 05](/assets/operation_center/integration_catalog/network_security/akamai_guardicore/Step 05.png){: style="max-width:100%"}


{!_shared_content/operations_center/integrations/generated/f1eb2bd3-dd6d-4b41-b3be-80874d1bd2d5_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_f1eb2bd3-dd6d-4b41-b3be-80874d1bd2d5_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f1eb2bd3-dd6d-4b41-b3be-80874d1bd2d5.md!}

## Troubleshooting

### No event is received

In the Akamai Guardicore console, for each data exporters for Sekoia.io, check, in the `Message format` section:

- The intake is supplied in the `RFC5424 structured data` option
- `RFC5424` is selected as `Message format`
- `ISO8601 (including milliseconds)` is selected as `Format log timestamp`
