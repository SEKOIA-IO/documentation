# SEKOIA.IO



SEKOIA.IO

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| api_key | string | SEKOIA.IO API key |
| base_url | string | SEKOIA.IO base URL (ex. https://api.sekoia.io) |
| liveapi_url | string | SEKOIA.IO's LiveAPI URL (ex. wss://live.sekoia.io) |





## Triggers

### security_alerts_trigger

New SEKOIA.IO Security Alert





#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| file_path | string | File path to the alert on disk. |
| event_type | string | Action that triggered this SEKOIA.IO Alert notification (could be for example “alert-created”, “alert-status-changed”, etc.) |
| alert_uuid | string | Unique identifier of the Alert (UUID string). |
| short_id | string | Unique short identifier of the Alert. |
| status | object | Status of the Alert (object containing status description and name). |
| created_at | integer | Creation date of the Alert (timestamp). |
| urgency | integer | Current urgency of the Alert. |
| entity | object | Description of the entity involved with this Alert (object containing entity UUID and name). |
| alert_type | object | Category of the Alert |







### alert_webhook

Webhook Trigger to receive specific SEKOIA.IO Alerts





#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| alert_uuid | string | Unique identifier of the Alert (UUID string). |













## Actions

### Update Alert Status

Triggers an action on an alert to update its status



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| action_uuid | string | UUID of the action to trigger |
| comment | string | a comment to describe why the alert status has changed |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| actions | array |  |







### Get Alert

Retrieve the definition of an alert



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| stix | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| urgency | object |  |
| history | array |  |
| is_incident | boolean |  |
| assets | array |  |
| countermeasures | array |  |
| updated_at | integer |  |
| comments | array |  |
| ttps | array |  |
| number_of_unseen_comments | integer |  |
| status | object |  |
| created_by | string |  |
| updated_by | string |  |
| source | string |  |
| community_uuid | string |  |
| number_of_total_comments | integer |  |
| uuid | string |  |
| rule | object |  |
| adversaries | array |  |
| short_id | string |  |
| first_seen_at | string |  |
| last_seen_at | string |  |
| event_uuids | array |  |
| kill_chain_short_id | string |  |
| similar | integer |  |
| alert_type | object |  |
| details | string |  |
| stix | object |  |
| created_by_type | string |  |
| entity | object |  |
| created_at | integer |  |
| updated_by_type | string |  |
| title | string |  |
| target | string |  |







### Attach Alerts to Case

Attach one or more alerts to a specific case



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| alerts | array | The list of identifiers of alerts to add |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| status | string |  |







### Get Event Field Common Values

Get the most common values of fields observed under a specific query



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string | Event search query |
| earliest_time | string | The earliest time of the time range of the search |
| latest_time | string | The latest time of the time range of the search |
| fields | string | Fields to compute the most common values (use a coma between fields) |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| fields | array |  |







### Activate Countermeasure

Mark as active a countermeasure



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| cm_uuid | string |  |
| comment | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| action_steps | array |  |
| activated_by_type | string | Type of the profile that activated the countermeasure |
| comments | array |  |
| activated_at | string | Date the countermeasure was activated |
| relevance | integer | Relevance of the countermeasure |
| denied_by_type | string | Type of the profile that denied the countermeasure |
| status | string | (deprecated) Status of the countermeasure |
| created_by | string | UUID of profile that created the countermeasure |
| model_uuid | string | UUID of the model from which this countermeasure has been created |
| activated_by | string | UUID of profile that activated the countermeasure |
| description | string | Description of the countermeasure |
| name | string | Name of the countermeasure |
| uuid | string | UUID of the countermeasure |
| duration | string | Estimated duration to apply the countermeasures |
| alert_uuid | string | UUID of the alert related to the countermeasure |
| denied_at | string | Date the countermeasure was denied |
| created_by_type | string | Type of the profile that created the countermeasure |
| course_of_action | object | (deprecated) STIX2 object course of action |
| dynamic_relevance | integer | Dynamic relevance of the countermeasure |
| denied_by | string | UUID of profile that denied the countermeasure |
| assignee | string | UUID of the profile assigned to the progress of the countermeasure |
| created_at | string | Date the countermeasure was created |







### Create Content Proposal from PDF

Creates a content proposal with the content extracted from the specified PDF



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| name | string |  |
| file | string |  |
| source_ref | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### Create Content Proposal from URL

Creates a content proposal with the content extracted from the specified URL



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| url | string |  |
| source_ref | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### Upload Observables

Upload observables to inthreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| observables | array | List of observables or bundle to upload to inThreat |
| observables_path | string | Path of the observables file to upload inThreat |









### Get CTI Report

Retrieve the details of a report



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### Push Events to Intake





#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| intake_key | string | Intake Key |
| event | object | Event to push on Intake |
| events | array | Events to push on Intake |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| event_ids | array |  |







### Create Asset

Create a new asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| asset_type | object |  |
| name | string |  |
| criticity | integer |  |
| description | string |  |
| attributes | array |  |
| keys | array |  |
| owners | array |  |
| community_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| keys | array |  |
| attributes | array |  |
| uuid | string |  |
| name | string |  |
| created_at | string |  |
| criticity | object |  |
| asset_type | object |  |
| updated_at | string |  |
| description | string |  |
| owners | array |  |
| community_uuid | string |  |
| category | object |  |







### Add key to Asset

Adds a key to an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| name | string |  |
| value | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| value | string |  |
| uuid | string |  |
| name | string |  |







### Edit Alert

Edit the details of an alert



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| alert_type_category | string | Category of the alert type |
| alert_type_value | string | Name of the alert type, required if `alert_type_category` is present |
| details | string | Description of the alert |
| urgency | integer | The urgency of the alert |
| kill_chain_short_id | string | The ID of the kill chain step this alert denotes |
| title | string | Title of the alert |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| urgency | object |  |
| is_incident | boolean |  |
| assets | array |  |
| updated_at | integer |  |
| ttps | array |  |
| number_of_unseen_comments | integer |  |
| status | object |  |
| created_by | string |  |
| updated_by | string |  |
| source | string |  |
| community_uuid | string |  |
| number_of_total_comments | integer |  |
| uuid | string |  |
| rule | object |  |
| adversaries | array |  |
| short_id | string |  |
| first_seen_at | string |  |
| last_seen_at | string |  |
| event_uuids | array |  |
| kill_chain_short_id | string |  |
| similar | integer |  |
| alert_type | object |  |
| details | string |  |
| stix | object |  |
| created_by_type | string |  |
| entity | object |  |
| created_at | integer |  |
| updated_by_type | string |  |
| title | string |  |
| target | string |  |







### Search Alerts

find alerts that match your filters



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| match[community_uuid] | string |  |
| match[entity_name] | string |  |
| match[entity_uuid] | string |  |
| match[status_uuid] | string |  |
| match[status_name] | string |  |
| match[type_category] | string |  |
| match[type_value] | string |  |
| match[source] | string |  |
| match[target] | string |  |
| match[node] | string |  |
| match[stix_object] | string |  |
| match[rule_uuid] | string |  |
| match[rule_name] | string |  |
| match[short_id] | string |  |
| match[uuid] | string |  |
| match[title] | string |  |
| date[created_at] | string |  |
| date[updated_at] | string |  |
| range[urgency] | string |  |
| range[similar] | string |  |
| visible | boolean |  |
| limit | integer |  |
| offset | integer |  |
| stix | boolean |  |
| sort | string |  |
| direction | string |  |
| with_count | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| has_more | boolean |  |
| items | array |  |







### Deny Countermeasure

Mark as denied a countermeasure



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| cm_uuid | string |  |
| comment | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| action_steps | array |  |
| activated_by_type | string | Type of the profile that activated the countermeasure |
| comments | array |  |
| activated_at | string | Date the countermeasure was activated |
| relevance | integer | Relevance of the countermeasure |
| denied_by_type | string | Type of the profile that denied the countermeasure |
| status | string | (deprecated) Status of the countermeasure |
| created_by | string | UUID of profile that created the countermeasure |
| model_uuid | string | UUID of the model from which this countermeasure has been created |
| activated_by | string | UUID of profile that activated the countermeasure |
| description | string | Description of the countermeasure |
| name | string | Name of the countermeasure |
| uuid | string | UUID of the countermeasure |
| duration | string | Estimated duration to apply the countermeasures |
| alert_uuid | string | UUID of the alert related to the countermeasure |
| denied_at | string | Date the countermeasure was denied |
| created_by_type | string | Type of the profile that created the countermeasure |
| course_of_action | object | (deprecated) STIX2 object course of action |
| dynamic_relevance | integer | Dynamic relevance of the countermeasure |
| denied_by | string | UUID of profile that denied the countermeasure |
| assignee | string | UUID of the profile assigned to the progress of the countermeasure |
| created_at | string | Date the countermeasure was created |







### Create Content Proposal

Create Content Proposal



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| bundle | object | STIX Bundle to upload |
| bundle_path | string | Path of the STIX Bundle to upload |
| auto_merge | boolean | Whether or not the uploaded bundle can automatically be merged to the consolidated database |
| enrich | boolean | Whether or not the uploaded bundle should be enriched |
| name | string | Name to use for the new content proposal |
| assigned_to | string | Avatar assigned to the content proposal |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| file_name | string |  |
| content_proposal_id | string |  |







### Comment Alert

Attach a new comment on an Alert



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| content | string | Content of the comment |
| author | string | Author of the comment |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| created_by | string | The identifier of the creator of the comment |
| content | string | Content of the comment |
| author | string | Author of the comment |
| unseen | boolean |  |
| date | integer |  |
| created_by_type | string | The type of the creator of the comment |
| uuid | string | Identifier of the comment |







### Create Alert

Create a Security Alert



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string | Optional UUID of the alert to create. |
| created_at | string | Creation date of the alert |
| community_uuid | string | UUID of the community that owns the alert. |
| entity_uuid | string | UUID of the entity associated to the alert. |
| entity_name | string | Name of the entity. |
| rule_uuid | string | UUID of the rule that detected the alert. |
| rule_name | string | Name of the rule that detected the alert. |
| rule_pattern | string | Pattern of the rule that detected the alert. |
| rule_description | string | Description of the rule that detected the alert. |
| rule_severity | integer | The severity of the rule that detected the alert |
| rule_type | string | Type of the rule that detected the alert. |
| alert_type_category | string | Category of the alert type. |
| alert_type_value | string | Name of the alert type. |
| source | string | Source of the main event that triggered the alert. |
| target | string | Target of the main eventr that related the alert. |
| status_uuid | string | UUID of the current status of the alert (default is '2efc4930-1442-4abb-acf2-58ba219a4fd0' ~ pending). |
| urgency_value | integer | Urgency of the alert. |
| urgency_severity | integer | Severity of the alert. |
| urgency_criticity | integer | Criticity of the alert. |
| urgency_display | string | Human-friendly description of the alert urgency. |
| details | string | Details of the alert. |
| similar | integer | Number of similar alerts (default is 0). |
| stix | object | STIX bundle of the detection. |
| kill_chain_short_id | string | The ID of the kill chain step this alert denotes |
| auto_validate | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| status | string | Current status of the task (pending or completed). |
| created_by | string | Identifier of the task creator |
| failure_count | integer | Number of alert that failed to be created |
| created_at | string | Created date of the task |
| pendings | array | UUIDs of all pending alerts |
| total_count | integer | Number of alerts to create |
| failures | array | UUIDs of all the alert that failed to be created |
| successes | array | UUIDs of all the alert succesfully created |
| name | string | Name of the task |
| created_by_type | string | Profile type of the task creator |
| uuid | string | Unique identifier of the task |
| pending_count | integer | Number of pending alert |
| success_count | integer | Number of alert succesfully created |







### Create Tracker Notification

Create a notification for a specific tracker



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### Add attribute to Asset

Add an attribute to an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| name | string |  |
| value | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| value | string |  |
| uuid | string |  |
| name | string |  |







### Predict Alert State

Predict the state of an alert



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| alert | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| worth_human_attention | boolean |  |












## Extra

Module **SEKOIA.IO v.2.0**
