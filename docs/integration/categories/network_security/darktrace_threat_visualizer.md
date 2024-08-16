uuid: 98fa7079-41ae-4033-a93f-bbd70d114188
name: Darktrace Threat Visualizer
type: intake

## Overview

Darktrace monitors all people and digital assets across your entire ecosystem.

- **Vendor**: Darktrace
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: Cloud
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: Darktrace Threat Visualizer

## Step-by-Step Configuration Procedure

This setup guide describes how to forward logs from Darktrace Threat visualizer to Sekoia.io.

### Instructions on the 3rd party solution
#### Acquire your public and private key

As a prerequisite, you need a Darktrace Threat Visualizer API tenant url.

See the [Darktrace documentation](https://customerportal.darktrace.com/product-guides/main/api-tokens) for intructions to acquire your public and private key.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

{!_shared_content/operations_center/integrations/generated/98fa7079-41ae-4033-a93f-bbd70d114188_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/98fa7079-41ae-4033-a93f-bbd70d114188.md!}
