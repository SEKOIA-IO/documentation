uuid: 9b95c9cf-8b78-4830-a1ed-b9e88f05e67a
name: Palo Alto Cortex XDR (EDR)
type: intake


## Overview

Palo Alto Cortex XDR (EDR) is an advanced Endpoint Detection and Response solution offering real-time threat detection, investigation, and response capabilities, empowering organizations to proactively defend against sophisticated cyber threats across their endpoints.

This setup guide shows how to forward EDR detections collected on the Palo Alto Cortex XDR (EDR) platform to Sekoia.io.

Sekoia.io supports both Cortex XDR API models:

- legacy incidents/alerts model (v3 APIs)
- issues/cases model (v5 APIs)

- **Vendor**: Palo Alto
- **Supported environment**: Cloud 
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: Network device logs


## Collected events

This integration collects EDR detections through one of the two supported Cortex API models (legacy alerts or issues), depending on the intake you choose.

!!! info
    In the v5 issues/cases model, the field `is_excluded` is supported and mapped to `paloalto.cortex.xdr.alert.is_whitelisted` in normalized events.

## Supported versions

This integration was tested against the following versions:

- Palo Alto Cortex XDR (EDR) 5.x (Issues API)
- Palo Alto Cortex XDR (EDR) 3.8

## Create API Key

Before using the **Cortex XDR** connector, you must generate an API key in Cortex XDR. For that you need to follow steps bellow :

1. Within **Cortex XDR**, click **Settings**.
2. Click **Configurations**.

    ![Configuration Page](/assets/integration/cloud_and_saas/paloalto_cortex_edr/configuration.png){: style="max-width:100%; height: 500px;"}

3. In the **Configurations** menu, select **API Keys**, which appears in the **Integrations** section.
4. In the API Keys window, click **+New Key** button to create a new API key. And the **Generate API Key** window will open.

    ![Api Key Page](/assets/integration/cloud_and_saas/paloalto_cortex_edr/api_key.png){: style="max-width:100%"}

5. Select the **Standard** Security Level.
6. Select a role for the API key. After selecting the role, click **Generate**.

    ![Generation Button](/assets/integration/cloud_and_saas/paloalto_cortex_edr/generate.png){: style="max-width:100%"}

7. After you’ve generated the key, copy the **API key** value presented and keep it secure.
8. Return to the **API Keys** window, and select the API key you just generated. Also make note of the **API key ID**, which appears in the API Keys table.

    !!! info
        - You will need also the `Fqdn` which is a unique host and domain name associated with each tenant. When you generate the API Key and Key ID, you are assigned an individual `Fqdn`.


## Configure

### Create the intake

1. Go to the [Intake page](https://app.sekoia.io/operations/intakes) and create a `Palo Alto Cortex XDR (EDR)` intake.
2. Create or Select a Palo Alto account with an `API Key`, `API Key ID` and `Fqdn`.
3. Select the trigger matching your Cortex tenant model:

    - `cortex_query_alerts` for the legacy incidents/alerts model (API v3)
    - `cortex_query_issues` for the issues/cases model (API v5)

4. Edit the intake configuration with a `chunk size` - Default is `100` and a `frequency` - Default is `60`

!!! info "Migration note (v3 and v5 coexistence)"
    Both API models are supported and available through dedicated connectors.

    - Legacy model: incidents and alerts (`/public_api/v1/alerts/get_alerts_multi_events`)
    - New model: issues and cases (`/public_api/v1/issue/search`)

    There is no implicit migration between models: if your Cortex tenant uses the issues/cases framework, create or switch to an intake using `cortex_query_issues`.


{!_shared_content/operations_center/integrations/generated/9b95c9cf-8b78-4830-a1ed-b9e88f05e67a_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9b95c9cf-8b78-4830-a1ed-b9e88f05e67a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/9b95c9cf-8b78-4830-a1ed-b9e88f05e67a.md!}

## Further Readings
- [Get started with Cortex API](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-API-Reference/Get-Started-with-APIs)
- [Cortex XDR Incident management API (v3)](https://cortex-docs.paloaltonetworks.com/xdr-3-api/cortex-xdr-3.x-apis/incident-management)
- [Cortex XDR Issues API (v5) - Issue search](https://cortex-docs.paloaltonetworks.com/xdr-5-api/issues-apis/issues#post-public_api-v1-issue-search)
- [Create API KEY](https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/1.0/Cortex-Xpanse-User-Guide/Generate-an-API-Key-in-Cortex-XDR)
