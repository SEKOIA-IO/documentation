uuid: 8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd
name: TEHTRIS Endpoint Detection & Reponse
type: intake

## Overview

TEHTRIS EDR is a security product to monitor, detect and mitigate threats on endpoints. It reduces the attack surface and prevents attacks.

This setup guide shows how to forward events produced by TEHTRIS EDR to Sekoia.io.

- **Vendor**: TEHTRIS
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: On Cloud 
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: File monitoring, Process monitoring and Anti-virus


## Configure

### Prerequisites

To forward events produced by TEHTRIS EDR to Sekoia.io, you have to:

1. Contact your TEHTRIS referent to activate the XDR Platform APIs for your tenant and ask to add the [Sekoia.io IP address](https://api.sekoia.io/outgoing-ips) to the allowlist

2. Log on the TEHTRIS XDR platform and navigate to `SOAR > Key Management`

3. Click on the button `Add`, enter the label of the API Key and select, at least, the API `Fetch Events`. You may have to create a filter

4. At the end, click on `Create` to generate the API Key

### Create the intake

To create the intake, go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `TEHTRIS Endpoint Detection & Reponse`.

### Pull events

To start to pull events, you have to:

1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new events from TEHTRIS](/integration/action_library/endpoint/tehtris/#fetch-new-events-from-tehtris) module

2. Set up the module configuration with your API key and your tenant ID (most of time, your tenant ID is the subdomain of your TEHTRIS instance; eg: `https://{tenant_id}.tehtris.net`)

3. Start the playbook and enjoy your [events](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd.md!}