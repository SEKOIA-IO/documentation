---
uuid: 8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd
title: TEHTRIS Endpoint Detection & Reponse
name: TEHTRIS Endpoint Detection & Reponse
type: intake
---

## Overview

TEHTRIS EDR is a security product to monitor, detect and mitigate threats on endpoints. It reduces the attack surface and prevents attacks.

This setup guide shows how to forward events produced by TEHTRIS EDR to Sekoia.io.

- **Vendor**: TEHTRIS
- **Supported environment**: On Cloud
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: File monitoring, Process monitoring and Anti-virus


## Configure

### Prerequisites

To forward events produced by TEHTRIS EDR to Sekoia.io, you have to:

1. Contact your TEHTRIS referent to activate the XDR Platform APIs for your tenant and ask to add the [Sekoia.io IP address](https://api.sekoia.io/outgoing-ips) to the allowlist

2. Log on the TEHTRIS XDR platform and navigate to `SOAR > Key Management`

3. Click on the button `Add`, enter the label of the API Key and select, at least, the API `Fetch Events`. You are required to create a filter (this filter may be left empty if desired).

4. At the end, click on `Create` to generate the API Key

### Create the intake

1. To create the intake, go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `TEHTRIS Endpoint Detection & Reponse`.
2. Set up the intake configuration with your API key and your tenant ID (most of time, your tenant ID is the subdomain of your TEHTRIS instance; eg: `https://{tenant_id}.tehtris.net`)

{!_shared_content/operations_center/integrations/generated/8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd.md!}