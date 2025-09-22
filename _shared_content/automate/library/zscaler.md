uuid: 0c97d665-e316-48ff-bcba-bbfbd4eaccc7
name: Zscaler
type: playbook

# Zscaler

![Zscaler](/assets/playbooks/library/zscaler.png){ align=right width=150 }

Zscaler is a cloud security company providing secure internet access and zero trust network access to protect enterprise data and applications. Its platform offers scalable, cloud-native solutions for secure browsing, data protection, and threat prevention.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Zscaler Base Url (ex: zscalerone.net, zscaler.net, zscloud.net) |
| `username` | `string` | Email ID of the API admin |
| `password` | `string` | Password for the API admin |
| `api_key` | `string` | API key |

## Actions

### Zscaler Activate changes

Activate changes
### Zscaler Block IoC

Block the provided IOCs: IP / domain

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `IoC` | `string` | The single value of the IoC to block |
| `IoCs` | `array` | The multiple values of IoCs to block |

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
| `IoC` | `string` | The single value of the IoC to unblock |
| `IoCs` | `array` | The multiple values of IoCs to unblock |


## Extra

Module **`Zscaler` v1.0.4**