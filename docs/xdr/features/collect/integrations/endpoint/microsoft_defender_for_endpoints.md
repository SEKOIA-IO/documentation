uuid: 05e6f36d-cee0-4f06-b575-9e43af779f9f
name: Microsoft Defender for Endpoints
type: intake

## Overview

Microsoft Defender for Endpoint is an enterprise endpoint security platform designed to help enterprise networks prevent, detect, investigate, and respond to advanced threats.

This setup guide describes how to forward events produced by `Microsoft Defender for Endpoints` to Sekoia.io XDR.


{!_shared_content/operations_center/detection/generated/suggested_rules_05e6f36d-cee0-4f06-b575-9e43af779f9f_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/05e6f36d-cee0-4f06-b575-9e43af779f9f.md!}

## Configure

### Prerequisites

To forward events to Sekoia.io, please follow [this guide](https://docs.microsoft.com/en-us/microsoft-365/security/defender/streaming-api-event-hub) to create an EventHubs namespace with an EventHubs that enable the data streaming on the hub.

Once the data streaming is configured, in your EventHubs, go to `Setting > Shared access policies`.
Create a new policy with the option `Listen` then copy the `Connection string-primary key`.

Create a `Storage accounts` or use an existing one. Go to `Data storage > containers` and create a new container.
Then go to `Security + networking > Access keys` and copy the key1 `Connection string`

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Microsoft 365 Defender`.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Consume Eventhub messages](../../../automate/library/microsoft-azure.md#consume-eventhub-messages) module. 

Set up the trigger configuration with the EventHub's `Connection string-primary key`, the hub name, the consumer group, the storage's `Connection string-primary key` and the container name.

Start the playbook and enjoy your [events](https://app.sekoia.io/operations/events).


## Further Readings

- [Configure Microsoft 365 Defender to stream Advanced Hunting events to your Azure Event Hub](https://docs.microsoft.com/en-us/microsoft-365/security/defender/streaming-api-event-hub)
