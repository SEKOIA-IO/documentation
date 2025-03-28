uuid: 28d53bf5-738a-42a4-8ce4-67e00195590e
name: Azure Monitor
type: playbook

# Azure Monitor

![Azure Monitor](/assets/playbooks/library/azure-monitor.png){ align=right width=150 }

Azure Monitor is a comprehensive solution for collecting, analyzing, and acting on telemetry from cloud and on-premises environments to maximize the performance and availability of applications.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `tenant_id` | `string` | Tenant ID |
| `client_id` | `string` | Client ID. An application needs to be created in the Azure Portal and assigned relevant permissions. Its Client ID should then be used in this configuration. |
| `client_secret` | `string` | Client Secret associated with the registered application. Admin Consent has to be granted to the application for it to work. |

## Actions

### [BETA] Query Azure Monitor Logs

Execute an Analytics query

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `workspace_id` | `string` | Workspace ID to search in |
| `query` | `string` | Query |
| `from_date` | `string` | Get data after this timestamp |
| `to_date` | `string` | Get data before or at this timestamp |
| `timeout` | `integer` | The maximum time, in seconds, the query should be processed in (default 300s) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `array` | Query results |


## Extra

Module **`Azure Monitor` v0.1.1**