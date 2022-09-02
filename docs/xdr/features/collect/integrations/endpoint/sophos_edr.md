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

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Sophos EDR`.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Sophos EDR connector](../../../automate/library/sophos.md).

Set up the connector configuration with the `Client ID`, the `Client Secret` and the intake key


## Further Readings

- [Sophos Central APIs: Send alert and event data to your SIEM](https://support.sophos.com/support/s/article/KB-000036372?language=en_US)
