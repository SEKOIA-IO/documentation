uuid: 0de5216e-19b0-4ad3-9b91-a547cfaf52ca
name: Sophos
type: playbook

# Sophos

![Sophos](/assets/playbooks/library/sophos.png){ align=right width=150 }

Sophos is a cybersecurity company that provides a range of security solutions, including endpoint protection, firewall, and encryption services. It focuses on delivering advanced threat protection to businesses through simplified and integrated security management.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `oauth2_authorization_url` | `string` | OAuth2 authorization URL |
| `api_host` | `string` | API Url of the Sophos Central API (e.g. 'https://api-{dataRegion}.central.sophos.com') |
| `client_id` | `string` | OAuth2 client identifier |
| `client_secret` | `string` | OAuth2 client secret |

## Actions

### [BETA] Deisolate endpoint

Turn off endpoint isolation

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `endpoint_id` | `string` | Endpoint ID |

### [BETA] Isolate endpoint

Turn on endpoint isolation

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `endpoint_id` | `string` | Endpoint ID |

### [BETA] Run scan



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `endpoint_id` | `string` | Endpoint ID |


## Extra

Module **`Sophos` v1.17.3**