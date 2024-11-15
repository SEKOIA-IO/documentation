# Enrich Alert with User agent in comment

This use case describes how to enrich the comments of an alert with the User agent extracted from the associated events.

## Prerequisites

- A Sekoia.io XDR licence
- The user that configures the Playbook should have a role that contains:
	* The SYMPHONY permissions
- An API Key with a role that contains at least the following permission:
	* `SIC_READ_ALERTS`
	* `SIC_WRITE_ALERTS_COMMENT`

!!!note
    To create your API Key, follow this [documentation](/getting_started/manage_api_keys.md#create-an-api-key).

## Playbook configuration

Find the playbook configuration below:

![Playbook Add_UserAgent_in_comment](/assets/playbooks/library/UseCases/Add_UserAgent_in_comment.png)

| Module | Configuration |
| --- | --- |
| Alert Created | configure module & trigger configuration |
| Get Alert | uuid = `alert_uuid` of **Created alert** |
| Get Event Field Common Values | See fields below |
| Comment Alert | See fields below |


!!!note
    The query could vary according to the event types / intakes.
    If the events does not contain user Agent, it will not retrieve any events

`Get Event Field Common Values`
  - **earliest_time**   `{{ ((node.2.first_seen_at | iso8601_to_timestamp) - 3600000) | timestamp_to_iso8601 }}`
  - **fields**  `user_agent.original`
  - **latest_time**    `now`
  - **query**   `source.ip:"{{ node.2['source'] }}" AND destination.ip:"{{ node.2['target'] }}" AND entity.uuid:"{{ node.2['entity']['uuid'] }}"`

`Comment Alert`
  - **content**  `{{ node.3| jsonpath("$.fields[*].common_values[*]['value']", True) }}% of time this user-agent "{{ node.3| jsonpath("$.fields[*].common_values[*]['name']", True) }}}" was seen on these events during the last 60 minutes.`
