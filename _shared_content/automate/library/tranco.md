uuid: 081074fc-240d-437f-a214-fba49691e69e
name: Tranco
type: playbook

# Tranco

![Tranco](/assets/playbooks/library/tranco.png){ align=right width=150 }

Tranco is an top sites ranking list hardened against manipulation.

## Configuration

This module accepts no configuration.

## Triggers

### Fetch List

Fetches Tranco list

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `chunk_size` | `integer` | Number of items to include in each chunk. Defaults to 10 000. |
| `interval` | `integer` | Interval in hours to wait between each trigger call. Defaults to 24. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | Tranco list file path |
| `chunk_offset` | `integer` | Offset of the chunk in the full list |
| `chunk_size` | `integer` | Size of the chunk |


## Extra

Module **`Tranco` v1.25.0**