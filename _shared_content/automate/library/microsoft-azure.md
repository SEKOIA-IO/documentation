# Microsoft Azure

![Microsoft Azure](/assets/playbooks/library/microsoft-azure.png){ align=right width=150 }

Microsoft Azure is a cloud computing service operated by Microsoft

## Configuration

This module accepts no configuration.

## Triggers

### Consume Eventhub messages

Consume messages from Microsoft Azure Eventhub

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hub_connection_string` | `string` | The connection string to connect the eventhub on Microsoft Azure eventHub |
| `storage_connection_string` | `string` | The connection string to connect the Microsoft Azure Storage blob |
| `storage_container_name` | `string` | The name of the container to use |
| `hub_name` | `string` | The name of the hub |
| `hub_consumer_group` | `string` | The consumergroup to supplied to the hub |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |


## Extra

Module **`Microsoft Azure` v1.4.4**