# Darktrace

![Darktrace](/assets/playbooks/library/darktrace.png){ align=right width=150 }

Darktrace monitors and protects all people and digital assets across your entire ecosystem.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_url` | `string` | The url of the Darktrace appliance |
| `public_key` | `string` | The public key to the Darktrace API |
| `private_key` | `string` | The private key to the Darktrace API |

## Triggers

### [BETA] Fetch new logs from Darktrace

Get the newest logs from Darktrace Threat Visualizer

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `verify_certificate` | `boolean` | Is the server certificate verified |
| `ratelimit_per_minute` | `integer` | The number of requests allowed to the API in one minute |


## Extra

Module **`Darktrace` v1.5.1**