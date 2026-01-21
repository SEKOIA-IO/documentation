uuid: 19cf9b48-dc7a-485f-ba14-3b7b998774c1
name: OSINT
type: playbook

# OSINT

![OSINT](/assets/playbooks/library/osint.svg){ align=right width=150 }

This module exposes actions to process OSINT data

## Configuration

This module accepts no configuration.

## Triggers

### Fetch OSINT

Fetch objects from a osint collection source

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `collection_sources` | `array` | OSINT Sources |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle_path` | `string` | Filepath of the bundle of STIX objects fetched from the collection |


## Extra

Module **`OSINT` v1.46.0**