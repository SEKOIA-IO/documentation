uuid: 98fa7079-41ae-4033-a93f-bbd70d114188
name: Darktrace Threat Visualizer
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

Darktrace monitors all people and digital assets across your entire ecosystem.

This setup guide describes how to forward logs from Darktrace Threat visualizer to Sekoia.io.
    

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
{!_shared_content/operations_center/integrations/generated/98fa7079-41ae-4033-a93f-bbd70d114188_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/integrations/generated/98fa7079-41ae-4033-a93f-bbd70d114188.md!}

