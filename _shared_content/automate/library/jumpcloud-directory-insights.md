# Jumpcloud Directory Insights

![Jumpcloud Directory Insights](/assets/playbooks/library/jumpcloud-directory-insights.png){ align=right width=150 }

Directory Insights allows you to read event logs, view activity in your directory, and monitor user authentications to the console, RADIUS, LDAP, and SSO apps. Directory Insights analyzes the audit trails that lead to critical events so you know the what, where, when, how, and who of your directory activities.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Jumpcloud Directory Insights API Base URL |
| `apikey` | `string` | The API key to authenticate calls to the Jumpcloud Directory Insights API |

## Triggers

### Jumpcloud Directory Insights Connector



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_server` | `string` |  |
| `intake_key` | `string` |  |
| `chunk_size` | `integer` |  |
| `frequency` | `integer` |  |
| `service` | `string` | Comma separated list of Jumpcloud services logs to collect |


## Extra

Module **`Jumpcloud Directory Insights` v1.8.1**