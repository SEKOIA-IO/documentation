# Palo Alto Cortex XDR (EDR)

![Palo Alto Cortex XDR (EDR)](/assets/playbooks/library/palo-alto-cortex-xdr-edr.png){ align=right width=150 }

Cortex XDR is the detection and response app that natively integrates network, endpoint and cloud data to stop sophisticated attacks.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | The API Key is your unique identifier used as the authorization header |
| `api_key_id` | `string` | The API Key ID is your unique token used to authenticate the API Key |
| `fqdn` | `string` | The FQDN is a unique host and domain name associated with each tenant |

## Triggers

### Fetch Alerts from Cortex [BETA]

Fetch last Alerts from Cortex API

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Palo Alto Cortex XDR (EDR)` v1.1.2**