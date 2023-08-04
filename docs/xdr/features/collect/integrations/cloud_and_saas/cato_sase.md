uuid: 469bd3ae-61c9-4c39-9703-7452882e70da
name: Cato SASE
type: intake

## Overview

Cato Networks is a software company providing solutions to protect cloud applications. Cato SASE Cloud provides zero trust network access to on-premises and cloud applications.

{!_shared_content/operations_center/detection/generated/suggested_rules_469bd3ae-61c9-4c39-9703-7452882e70da_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/469bd3ae-61c9-4c39-9703-7452882e70da.md!}

## Configure

This setup guide will show you how to provide an integration between Cato SASE events and Sekoia.io.

### Configure connector

1. Get `api_key` and `account_id` from your Cato Networks account

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cato SASE. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Cato SASE](../../../automate/library/cato_sase.md) trigger
2. Set up the module configuration with the Api Key and Account Id. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events
