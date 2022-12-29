# Enrich Alert with User agent in comment

This use case describes how to enrich Alert with User agent in comment

## Prerequisites

- A SEKOIA.IO XDR licence
- The user that configures the Playbook should have a Role that contains:
	* The SYMPHONY permissions
- An API Key with a Role that contains at least the following permission:
	* SIC_READ_ALERTS
	* SIC_WRITE_ALERTS_COMMENT

> To create your API Key, follow this [documentation](../../../getting_started/generate_api_keys.md).

## Playbook configuration

Here is the configuration below

![Playbook Add_UserAgent_in_comment](docs/assets/playbooks/library/UseCases/Add_UserAgent_in_comment.md.png)

Alert Created     configure module & trigger configuration
Get_an_alert       uuid = `alert_uuid` of **Alert Created**

Get Event Field Common Values
  - **earliest_time**   `{{ ((node.2.first_seen_at | iso8601_to_timestamp) - 3600000) | timestamp_to_iso8601 }}`
  - **fields**  `user_agent.original`
  - **latest_time**    `now`    
  - **query**   `source.ip:"{{ node.2['source'] }}" AND destination.ip:"{{ node.2['target'] }}" AND [entity.name](http://entity.name/):"{{ node.2['entity']['name'] }}"`
    
post_a_comment_on_an_alert
  - **content**  `{{ node.3| jsonpath("$.fields[*].common_values[*]['value']", True) }}% of time this user-agent "{{ node.3| jsonpath("$.fields[*].common_values[*]['name']", True) }}}" was seen on these events during the last 60 minutes.`
