---
uuid: 69b52166-b804-4f47-860f-2d3fd0b46987
title: Azure Front Door
name: Azure Front Door
type: intake
---

## Overview

Microsoft Azure Front Door is a scalable and secure entry point for fast delivery of your global web applications. This setup guide describe how to forward events produced by `Azure Front Door` to Sekoia.io.

- **Vendor**: Microsoft Azure
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Web logs, Web application firewall logs

## Configure

### Prerequisites

To forward events to Sekoia.io, create [an Event hub namespace and an Event hub](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create) with a consumergroup.

Once created, in your EventHubs, go to `Setting > Shared access policies`.
Create a new policy with the option `Listen` then copy the `Connection string-primary key`.

Create a [Storage accounts](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create) or use an existing one. Go to `Data storage > containers` and create a new container.
Then go to `Security + networking > Access keys` and copy the key1 `Connection string`

Configure Azure Front door to stream its logs to the EventHub with [this guide](https://docs.microsoft.com/en-us/azure/frontdoor/standard-premium/how-to-logs#configure-logs).

### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Azure Front Door`.
2. Set up the intake configuration with the EventHub's `Connection string-primary key`, the hub name, the consumer group, the storage's `Connection string-primary key` and the container name.

{!_shared_content/operations_center/integrations/generated/69b52166-b804-4f47-860f-2d3fd0b46987_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_69b52166-b804-4f47-860f-2d3fd0b46987_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/69b52166-b804-4f47-860f-2d3fd0b46987.md!}

## Further Readings

- [Azure Front Door logs](https://docs.microsoft.com/en-us/azure/frontdoor/standard-premium/how-to-logs)
