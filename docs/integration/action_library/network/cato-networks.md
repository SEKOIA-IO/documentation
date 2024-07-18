# Cato Networks

![Cato Networks](/assets/playbooks/library/cato-networks.png){ align=right width=150 }

Cato Networks is a software company providing solutions to protect cloud applications.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | Api key to interact with Cato API |
| `account_id` | `string` | Account Id (4 digits) to work with Cato API |

## Triggers

### Collect Cato SASE events

Trigger playbook to get Cato SASE information

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Cato Networks` v1.3**