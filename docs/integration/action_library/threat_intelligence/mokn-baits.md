---
uuid: 6a0181cc-5771-40ee-8001-21cc1f088921
name: "MokN - Baits"
type: playbook
description: "MokN helps detect malicious authentication activity by exposing login attempts captured on bait services."
---

# MokN - Baits

<img src="../../.gitbook/assets/library/mokn-baits.png" alt="MokN - Baits" width="150" align="right">

MokN helps detect malicious authentication activity by exposing login attempts captured on bait services.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Base URL of the MokN tenant API |
| `api_token` | `string` | MokN API key used to authenticate against the tenant API |
| `verify_ssl` | `boolean` | Whether TLS certificates must be validated |

## Actions

### Comment Attempt

Add or update the comment of a specific MokN login attempt

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `attempt_id` | `integer` | Identifier of the MokN login attempt |
| `comment` | `string` | Comment to add to the login attempt |

### Request MokN Credential Check

Request a credential check for a specific MokN login attempt

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `attempt_id` | `integer` | Identifier of the MokN login attempt |


## Extra

Module **`MokN - Baits` v1.1.1**