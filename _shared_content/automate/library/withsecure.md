# WithSecure

![WithSecure](/assets/playbooks/library/withsecure.png){ align=right width=150 }

Interact with WithSecure Elements

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client identifier |
| `secret` | `string` | API secret to authenticate |

## Triggers

### Fetch security events [beta]

Get last security events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`WithSecure` v1.0.1**