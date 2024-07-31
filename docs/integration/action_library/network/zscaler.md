# Zscaler

![Zscaler](/assets/playbooks/library/zscaler.png){ align=right width=150 }

Integrates with Zscaler

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Zscaler Base Url (ex: zscalerone.net, zscaler.net, zscloud.net) |
| `username` | `string` | Email ID of the API admin |
| `password` | `string` | Password for the API admin |
| `api_key` | `string` | API key |

## Actions

### Zscaler Block IoC

Block the provided IOCs: IP / domain

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `IoC` | `string` | The value of the IoC to block |

### Zscaler Push IOCs for detection

Block the provided IOCs: IP / domain / Url

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |
| `sekoia_base_url` | `string` | [Optional] Sekoia base url, used to generate direct links to IOCs |

### Zscaler UnBlock IoC

UnBlock the provided IOCs: IP / domain

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `IoC` | `string` | The value of the IoC to unblock |


## Extra

Module **`Zscaler` v0.1.3**