---
title: "salesforce"
category: "library"
---
# Salesforce

![Salesforce](/assets/playbooks/library/salesforce.png){ align=right width=150 }

Salesforce provides users comprehensive tools to manage customer data, automate processes, analyze data and insights, and create personalized customer experiences. Salesforce also offers a variety of solutions for customer service, marketing automation, commerce, app development, and more

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `client_id` | `string` | Client id to interact with salesforce API |
| `client_secret` | `string` | Client secret to interact with salesforce API |
| `base_url` | `string` | Url of salesforce instance. Consists of https://<instance>.salesforce.com |

## Triggers

### Collect Salesforce events

Trigger playbook to get Salesforce information

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ratelimit_per_minute` | `integer` | Maximum number of requests per minute |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |


## Extra

Module **`Salesforce` v1.2.5**