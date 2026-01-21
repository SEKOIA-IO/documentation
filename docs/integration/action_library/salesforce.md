# Salesforce

![Salesforce](/assets/playbooks/library/salesforce.png){ align=right width=150 }

Salesforce provides users comprehensive tools to manage customer data, automate processes, analyze data and insights, and create personalized customer experiences. Salesforce also offers a variety of solutions for customer service, marketing automation, commerce, app development, and more

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `org_type` | `string` | Organization type. Might be one of the following: 'production', 'sandbox', 'trial', 'developer'. Default is 'production' |
| `client_id` | `string` | Client id to interact with salesforce API |
| `client_secret` | `string` | Client secret to interact with salesforce API |
| `rate_limit` | `string` | Rate limit for requests to salesforce. Value should have next format {max_rate}/{time_period}. For example: 3/60. Sekoia will use default rate limits if value is empty or invalid. More information you can find in docs: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm |
| `base_url` | `string` | Url of salesforce instance. Consists of https://<instance>.salesforce.com |

## Triggers

### Collect Salesforce events

Trigger playbook to get Salesforce information

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `chunk_size` | `integer` | The max size of chunks for the batch processing |
| `frequency` | `integer` | Batch frequency in seconds |
| `fetch_daily_logs` | `boolean` | Fetch daily logs. By default, it will fetch Hourly logs |


## Extra

Module **`Salesforce` v1.6.1**