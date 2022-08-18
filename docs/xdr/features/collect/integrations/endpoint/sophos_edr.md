uuid: 3f330d19-fdea-48ac-96bd-91a447bb26bd
name: Sophos EDR
type: intake

## Overview

Sophos EDR monitors, detects and mitigates threats on endpoints.
This EDR reduces the attack surface and prevent attacks from running with an anti-exploit, an anti-ransomware and advanced control technology.

This setup guide shows how to forward events produced by Sophos EDR to SEKOIA.IO.

{!_shared_content/operations_center/integrations/generated/sophos-edr_do_not_edit_manually.md!}

## Configure

### Credentials

In the Sophos Central Admin console, go to `Global Settings > API Credentials Management`.
Create a new token with `Add Credential`. Complete the name, appropriate role and description.
On the `API credential Summary`, copy the `Client ID` and the `Client Secret`.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS CloudTrail`.

### Pull events

Get the [Sophos Central SIEM integration script](https://github.com/sophos/Sophos-Central-SIEM-Integration) and configure it by following [this Sophos guide](https://support.sophos.com/support/s/article/KB-000036372?language=en_US).

### Forward events

See the [Ingestion methods page](https://docs.sekoia.io/operation_center/data_collection/ingestion_methods/) to select the appropriate method to forward your events to SEKOIA.IO according to your needs.


## Further Readings

- [Sophos Central APIs: Send alert and event data to your SIEM](https://support.sophos.com/support/s/article/KB-000036372?language=en_US)