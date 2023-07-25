uuid: 838ed6e5-6d5e-4a5b-b079-ab35ac6b2ab9
name: Vade Cloud
type: intake

## Overview

Vade Cloud offers all protections against threats for any email inbox.

In this documentation we will explain how to collect and send Vade Cloud logs to SEKOIA.IO.


{!_shared_content/operations_center/detection/generated/suggested_rules_838ed6e5-6d5e-4a5b-b079-ab35ac6b2ab9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/838ed6e5-6d5e-4a5b-b079-ab35ac6b2ab9.md!}

## Configure

### Create the intake in SEKOIA.IO

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Vade Cloud`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the `Fetch new logs from Vade Cloud` trigger
2. Set up the module configuration with the base URL of your Netskope instance. Set up the trigger configuration with the API token and the intake key
3. Start the playbook and enjoy your events