uuid: 23813540-b658-48dd-b030-e9b92168bbf4
name: Daspren Parad
type: intake

## Overview

Daspren is the only Data Detection and Response (DDR) that integrates detection and blocking of cyber attacks.
Daspren goes deep, using our patented data-centric AI to meticulously dissect and analyze every data access. It seamlessly intercepts and scrutinizes these access requests, ensuring that only legitimate, authorized applications can access your data, keeping it secure and protected.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

Parad is the data protection solution from Daspren. It monitors data activity and use AI to prevent data breaches coming from both the inside and the outside of your organization :

- File created, opened, deleted, moved or modified,
- Access rules breach attempts,
- Malicious processes detected.

## Supported events

This integration supports the following events:

- File monitoring events
- Malicious detection events

{!_shared_content/operations_center/detection/generated/suggested_rules_23813540-b658-48dd-b030-e9b92168bbf4_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/23813540-b658-48dd-b030-e9b92168bbf4.md!}

## Configure

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Daspren - Parad`. Copy the intake key.

### Setup a Sink

To set up the integration:

1. Open the Parad CLI
2. Create a Sink from the CLI
	1. Go to `Sinks > Add Sink`
	2. Select the Sekoia Sink Variant
	3. Type a name and paste the intake key
3. Create a Reporter from the CLI with `Reporters > Add Reporter`
4. Create a Link between the previously created Sink and Reporter
