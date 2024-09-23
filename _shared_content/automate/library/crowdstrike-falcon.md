# CrowdStrike Falcon

![CrowdStrike Falcon](/assets/playbooks/library/crowdstrike-falcon.png){ align=right width=150 }

Integrates with CrowdStrike Falcon EDR

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client Identifier |
| `client_secret` | `string` | Client Secret |
| `base_url` | `string` | Base URL of the API |

## Triggers

### Fetch CrowdStrike Falcon Events

Get latest events from CrowdStrike Falcon

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_key` | `string` | Intake key to use when sending events |
| `tg_base_url` | `string` | The base_url for the ThreatGraphAPI |
| `tg_username` | `['string', 'null']` | The username for the ThreatGraphAPI |
| `tg_password` | `['string', 'null']` | The password for the ThreatGraphAPI |

## Actions

### Block IOC

Block the provided IOC

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `value` | `string` | The value of the IOC to block |
| `type` | `string` | Type of the IOC to block: md5, sha256 |

### Deisolate hosts

Lifts containment on the host and returns its network communications to normal.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ids` | `array` | List of host agent IDs to apply action to. |

### Isolate hosts

Contains the host and stops any network communications to locations other than the CrowdStrike cloud and IPs specified in your containment policy.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ids` | `array` | List of host agent IDs to apply action to. |

### Monitor IOC

Enable detection for the provided IOC

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `value` | `string` | The value of the IOC to monitor |
| `type` | `string` | Type of the IOC to monitor: md5, sha256, domain, ipv4, ipv6 |

### Push IOCs for prevention

Block the provided IOCs: md5 / sha256 file hashes

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |
| `sekoia_base_url` | `string` | [Optional] Sekoia base url, used to generate direct links to IOCs |

### Push IOCs for detection

Enable detections on the provided IOCs: md5 / sha256 file hashes, IPv4/v6 address, domains

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |
| `sekoia_base_url` | `string` | [Optional] Sekoia base url, used to generate direct links to IOCs |
| `valid_for` | `integer` | If set, the playbook will remove IOCs that are older than valid_for days based on the Last modified date in CrowdStrike |


## Extra

Module **`CrowdStrike Falcon` v1.20.0**