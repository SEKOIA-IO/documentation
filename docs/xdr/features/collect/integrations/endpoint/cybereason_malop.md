uuid: 9f89b634-0531-437b-b060-a9d9f2d270db
name: Cybereason MalOp
type: intake

## Overview

Cybereason offers a set of Endpoint Detection and Response (EDR) solutions. Through the Cybereason platform, all suspicious operations will be gathered in MalOps, a multi-stage visualizations of device activities.


{!_shared_content/operations_center/detection/generated/suggested_rules_9f89b634-0531-437b-b060-a9d9f2d270db_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/cybereason-malop-json_do_not_edit_manually.md!}

## Configure

This setup guide will lead you into forwarding all MalOp activities to SEKOIA.IO.

### Prerequisites

To forward events produced by Cybereason to SEKOIA.IO, you will need your Cybereason username and password. 

### Create your intake

On SEKOIA.IO, go to the [Intakes page](https://app.sekoia.io/operations/intakes/new) and generate a new intake with the `Cybereason MalOp` format.
Keep aside the intake key.

### Pull events

To start pulling events, you have to: 
1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new events from Cybereason](../../../automate/library/cybereason) module. 
2. Set up the module configuration with your Cybereason username and password.
3. Set up the trigger configuration with your intake key
4. Start the playbook and enjoy your [events](https://app.sekoia.io/operations/events).
