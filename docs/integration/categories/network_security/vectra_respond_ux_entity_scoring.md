uuid: 48146ba4-4c79-4aa9-8eb3-660e984bda95
name: Vectra Response UX Entity Scoring
type: intake

## Overview
Vectra Respond UX delivers an intuitive, AI-driven interface for seamless threat investigation and response. It provides real-time visibility, guided workflows and automated remediation actions to accelerate incident resolution.

- **Vendor**: Vectra
- **Supported environment**: SaaS
- **Supported application or feature**: Entities scoring


## Configure
This setup guide will show you how to forward logs produced by your Vectra Appliance server to Sekoia.io by means of an rsyslog transport channel.

### How to create credentials
1. Log in to the Vectra Respond UX
2. Go to `Manage` > `API Clients`
3. Click `Add API Client`
4. Type a name, select a Role and type a description
5. Click `Generate Credentials`
6. Copy the Client ID and Secret Key

### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Vectra Response UX Entity Scoring`.
2. Set up the intake configuration with the base URL of the API, your client id and your client secret.


{!_shared_content/operations_center/integrations/generated/48146ba4-4c79-4aa9-8eb3-660e984bda95_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_48146ba4-4c79-4aa9-8eb3-660e984bda95_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/48146ba4-4c79-4aa9-8eb3-660e984bda95.md!}


## Further Readings
- [Vectra Platform API Quick Start Tutorial](https://support.vectra.ai/vectra/article/KB-VS-1572)
