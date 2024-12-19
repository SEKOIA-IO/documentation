# Get events information from alert

This use case describes how to get the MAC address of events associated with an alert. 

## Prerequisites

- A Sekoia.io XDR licence
- The user that configures the Playbook should have a role that contains:
	* The SYMPHONY permissions
- An API Key with a role that contains at least the following permissions:
	* `View alerts`
	* `View anomaly stats`
	* `View anomaly dataset`
	* `View event stats in asset listing`

!!! note 
    To create your API Key, follow this [documentation](/getting_started/manage_api_keys.md).
    
## Playbook configuration

Here is the configuration below: 

![Playbook Enrich_information_in_alert](/assets/playbooks/library/UseCases/Enrich_information_in_alert.png)

| Module | Configuration |
| --- | --- |
| Alert Created | configure module & trigger configuration |
| Get Alert | uuid = `alert_uuid`  of **Alert created** |
| Get Events | See fields below |
| Read JSON File | See fields below |

**Get Events**  
- **earliest_time** = `first_seen_at` of **Get alert**
- **latest_time** = `last_seen_at` of **Get alert**
- **query** = alert_short_ids: `{{ node.x.alert_uuid }}`  copy `short_id` of **Get alert****

**Read JSON File** 
- **jsonpath** = `mac-addr` more information on this documentation [here](http://docs.oasis-open.org/cti/stix/v2.0/cs01/part4-cyber-observable-objects/stix-v2.0-cs01-part4-cyber-observable-objects.html#_Toc496716255)
- **file** = `{{node.x['events']}}`  x = event node (that can be found in code tab)
