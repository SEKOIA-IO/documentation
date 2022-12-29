# Get events information from alert

This use case describes how to get the Mac Adress of an alert

## Prerequisites

- A SEKOIA.IO XDR licence
- The user that configures the Playbook should have a Role that contains:
	* The SYMPHONY permissions
- An API Key with a Role that contains at least the following permission:
	* SIC_READ_ALERTS
	* EVENTS_READ_STATS
	* EVENTS_READ_DATASETS
	* SIC_READ_EVENT_STATS

> To create your API Key, follow this [documentation](../../../getting_started/generate_api_keys.md).
## Playbook configuration

Here is the configuration below

![Playbook Enrich_information_in_alert](docs/assets/playbooks/library/UseCases/Enrich_information_in_alert.png)

Alert created   configure module & trigger configuration
Get alert       uuid = `alert_uuid`  of **Alert created**
Get Events      
  - **earliest_time** = `first_seen_at` of **Get alert**
  - **latest_time** = `last_seen_at` of **Get alert**
  - **query** = `short_id` of **Get alert**

Read Json file    
 - **jsonpath** = `mac-addr` more information on this documentation [here](http://docs.oasis-open.org/cti/stix/v2.0/cs01/part4-cyber-observable-objects/stix-v2.0-cs01-part4-cyber-observable-objects.html#_Toc496716255)
 - **file with** = `{{node.x['events']}}`  x = event node (that can be found in code tab)
