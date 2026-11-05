---
uuid: e76687ed-db66-482a-8549-f3ef3b248e06
name: "Digital Shadows"
type: playbook
description: "Digital Shadows is a cybersecurity company that offers digital risk protection solutions to help organizations manage their digital footprints and detect threats. It provides monitoring and intelligence to safeguard against data leaks, phishing, and other cyber risks."
---

# Digital Shadows

<img src="../../.gitbook/assets/library/digital-shadows.png" alt="Digital Shadows" width="150" align="right">

Digital Shadows is a cybersecurity company that offers digital risk protection solutions to help organizations manage their digital footprints and detect threats. It provides monitoring and intelligence to safeguard against data leaks, phishing, and other cyber risks.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_url` | `string` | URL of the SearchLight instance |
| `searchlight_account_id` | `string` | SearchLight Account ID |
| `basicauth_key` | `string` | HTTP Basic authentication key |
| `basicauth_secret` | `string` | HTTP Basic authentication secret |

## Triggers

### Get SearchLight Alerts

Get last created SearchLight alerts and incidents

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alerts` | `array` | SearchLight Alerts |


## Extra

Module **`Digital Shadows` v1.19.0**