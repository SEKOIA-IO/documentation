uuid: 98fa7079-41ae-4033-a93f-bbd70d114188
name: Darktrace Threat Visualizer
type: intake

## Overview

Darktrace monitors all people and digital assets across your entire ecosystem.

This setup guide describes how to forward logs from Darktrace Threat visualizer to Sekoia.io.

!!! warning
    This format is in beta.
    
{!_shared_content/operations_center/integrations/generated/98fa7079-41ae-4033-a93f-bbd70d114188.md!}

## Configure

As a prerequisite, you need a Darktrace Threat Visualizer API tenant url.

### Acquire your public and private key

See the [Darktrace documentation](https://customerportal.darktrace.com/product-guides/main/api-tokens) for intructions to acquire your public and private key.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Threat Visualizer`.


### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Darktrace connector](../../../automate/library/darktrace.md).

Set up the trigger configuration with the api url, the private key and the public key.

Start the playbook and enjoy your events.