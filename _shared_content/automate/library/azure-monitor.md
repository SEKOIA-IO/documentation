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

## Set up

## How to configure Azure Monitor Logs module

### Create an Azure application

1. On the Azure Portal, in the search bar, go to `App registrations`
2. Click [`+ New registration`](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/false)
3. Type a name
4. Select `Accounts in this organizational directory only` option as account type
5. Click `Register`
6. From the `Overview` page, copy `Application (client) ID` and `Directory (tenant) ID`

### Create a client secret

1. Go to `Manage` > `Certificates & secrets`
2. Click `+ New client secret`
3. Type a description and select the desired expiration period
4. Click `Add`
5. Copy the `Value` of the client secret

### Add role to the APP

1. In the search bar, go to `Subscriptions`
2. Click on one of your subscriptions
3. On the right panel, Click `Access control (IAM)`
4. Click `+ Add` > `Add role assignment`
5. In the `job function roles` sub-tab, search for `Log Analytics Reader` and select it
6. Click `Next`
7. Select `User, group or service principal` as access
8. Click `+ Select members`
9. Type the name of the Azure application created previously, select it and click `Select`
10. Click `Review + assign`

[Read More](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)

## Extra

Module **`Azure Monitor` v0.1.1**