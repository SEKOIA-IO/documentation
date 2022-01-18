# sekoia.io



SEKOIA.io

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

### list_tracker_notifications

The following permissions are required:
 - **INTHREAT_READ_TRACKER_NOTIFICATIONS** (`5616eb17-1e1b-4337-b8ce-9cb109184075`): Read tracker notifications from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[status] | string |  |
| start | string |  |
| end | string |  |
| match[tracker_type] | string |  |
| match[rule] | string |  |
| match[ruleset_name] | string |  |
| search | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| has_more | boolean |  |
| total | integer |  |







### trigger_an_action_on_the_alert_workflow

The workflow is a Directed acyclic graph (DAG) that define the available statuses for alerts
and define the list of actions that can be performed on alerts.

This endpoint performs an action on the alert and changes the status of the alert according to the performed
action and the workflow.
E.g.: For a pending alert, a 'acknowledge' action will acknowledge the alert
and update the status of the alert to 'acknowledged'

The identifier of the action, sent in the body of the request as a json dictionary, is brought from the
workflow (GET request on this endpoint)

The following permissions are required:
 - **WRITE_ALERTS_WORKFLOW** (`9f3df1b1-4db7-44bd-b615-af5873ad7f8a`): Triggers an action on the alert workflow



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







### list_all_tags

This endpoint accepts the following querystrings:

* `?community_uuid=community_uuid1` to return all tags belonged to the community identified by `community_uuid1`

The following permissions are required:
 - **SIC_READ_INCIDENTS** (`7c0bac3f-f2ce-491b-b663-638145078516`): Get incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| match[community_uuid] | string |  |
| limit | integer |  |
| offset | integer |  |
| community_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| items | array |  |







### relationships_get_a_relationship

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### updates_an_case

this endpoint accepts the following parameters:

* `title` to update the title of the case
* `description` to update the description of the case
* `status_name` to update the status of the case by the name of the case
* `status_uuid` to update the status of the case by the identifier of the case
* `tags`: tags to associate to the case.

this endpoint accepts the following querystrings:

* `?community_uuid=community_uuid`: the identifier of the community that the case belong to

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| title | string | Title of the case |
| description | string | Description of the case |
| status_uuid | string | Identifier of the status of the case |
| status_name | string | Name of the status of the case |
| priority | string | Priority of the case (low|medium|high) |
| subscribers | array | List of subscribers to the case |
| tags | array |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| updated_at | string |  |
| status | string |  |
| created_by | string |  |
| updated_by | string |  |
| description | string |  |
| community_uuid | string |  |
| priority | string | low|medium|high |
| uuid | string |  |
| short_id | string |  |
| status_uuid | string |  |
| number_of_alerts | integer |  |
| created_by_type | string |  |
| number_of_comments | integer |  |
| subscribers | array |  |
| tags | array | List of tags associated to the case |
| created_at | string |  |
| alerts | array |  |
| updated_by_type | string |  |
| title | string |  |







### deletes_an_attribute_from_an_asset

:param uuid.UUID uuid: The identifier of the asset
:param uuid.UUID attribute_uuid: The identifier of the attribute to delete

The following permissions are required:
 - **ASSETMANAGEMENT_DELETE_ASSET_ATTRIBUTE** (`49da4bd9-555a-4525-a5bf-19ed2dd887ae`): Allow to delete an attribute of an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| attribute_uuid | string |  |









### warning_rules_remove_a_warning_rule

The following permissions are required:
 - **INTHREAT_WRITE_WARNING_RULES** (`9042e6b4-7c86-49a6-b2cb-a66961e1fd71`): Write warning rules to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### content_proposals_relationships_list_merge_proposal_relationships_that_have_been_modified

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### objects_get_an_object

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### objects_create_a_new_object

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### content_proposals_relationships_retrieve_relationship_changes

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| relationship_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_get_a_content_proposal

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_merge_a_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### content_proposals_observables_retrieve_observable_changes

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| observable_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### create_a_new_tracker_rule

The following permissions are required:
 - **INTHREAT_WRITE_TRACKER_RULES** (`f7bb8b40-35d5-4fc4-9c65-2ceace0e4734`): Write tracker rules to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### get_an_alert

The following permissions are required:
 - **SIC_READ_ALERTS** (`9ea2b8a3-593f-4bab-92f5-d0af9b563f6f`): List and consult SIC alerts



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







### objects_get_an_objects_relationships

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### deletes_an_asset

:param str uuid: The identifier of the asset

The following permissions are required:
 - **ASSETMANAGEMENT_DELETE_ASSET** (`7c337b11-59f1-47d2-90d0-9e3a8e089208`): Allow to delete an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### content_proposals_observables_update_suggested_changes_to_the_observable

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| observable_uuid | string |  |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### adds_owners_to_an_asset

:param dict args: The parameters for the endpoint
:param uuid.UUID uuid: The identifier of the asset
:return: The list of owners
:rtype: dict

args:
    - owners: The list of owners of the asset

The following permissions are required:
 - **ASSETMANAGEMENT_CREATE_ASSET_OWNER** (`db659df4-51d4-408e-af17-985c1a2cc1df`): Allow to add an owner to an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| owners | array |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### collections_list_patterns

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| feed_id | string |  |
| limit | integer |  |
| modified_after | string |  |
| after_id | string |  |
| include_revoked | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| next_id | string |  |







### content_proposals_objects_update_suggested_changes_to_the_object

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### associate_new_alerts_on_a_case

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| alerts | array | The list of identifiers of alerts to add |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| status | string |  |







### replace_the_associated_alerts_to_a_case

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| alerts | array | The list of identifiers of alerts to add |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| status | string |  |







### content_proposals_relationships_remove_relationship_changes_from_the_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| relationship_uuid | string |  |









### update_an_incident

this endpoint accepts the following parameters:

* `title` to update the title of the incident
* `description` to update the description of the incident
* `status_name` to update the status of the incident by the name of the incident
* `status_uuid` to update the status of the incident by the identifier of the incident

this endpoint accepts the following querystrings:

* `?community_uuid=community_uuid`: the identifier of the community that the incident belong to

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| incident_uuid | string |  |
| title | string | The title of the incident |
| description | string | The description of the incident |
| status_uuid | string | The identifier of the status of the incident |
| status_name | string | The name of the status of the incident |
| community_uuid | string | The identifier of the community |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| description | string |  |
| created_by_type | string |  |
| created_at | string |  |
| created_by | string |  |
| updated_by_type | string |  |
| status | string |  |
| updated_by | string |  |
| status_uuid | string |  |
| title | string |  |
| uuid | string |  |
| community_uuid | string |  |
| blocks | array |  |
| updated_at | string |  |
| short_id | string |  |







### create_a_new_incident

This endpoint requires the following parameters:

* `title`: the title of the incident
* `description`: the description of the incident
* `status_uuid`: the identifier of status of the incident

This endpoint accepts (Optional) the following parameters:

* `community_uuid`: the identifier of the community to which the incident is associated

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| title | string | The title of the incident |
| description | string | The description of the incident |
| status_uuid | string | The status of the incident |
| community_uuid | string | The identifier of the community |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| description | string |  |
| created_by_type | string |  |
| created_at | string |  |
| created_by | string |  |
| updated_by_type | string |  |
| status | string |  |
| updated_by | string |  |
| status_uuid | string |  |
| title | string |  |
| uuid | string |  |
| community_uuid | string |  |
| blocks | array |  |
| updated_at | string |  |
| short_id | string |  |







### kill_chains_list_kill_chains

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat





#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### content_proposals_modify_a_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### delete_a_comment_from_a_case

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| comment_uuid | string |  |









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







### activate_a_countermeasure

An optional comment can be provided to
be attached to the countermeasure.

The following permissions are required:
 - **SIC_WRITE_ALERTS** (`0e329f9c-173f-4fa0-bbbc-fcfc4bdf7559`): Create, Update and delete SIC alerts



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







### deletes_an_key_from_an_asset

:param uuid.UUID uuid: The identifier of the asset
:param uuid.UUID key_uuid: The identifier of the key to delete

The following permissions are required:
 - **ASSETMANAGEMENT_DELETE_ASSET_KEY** (`aefc8b12-f1f9-4840-ad30-72f3aa77fd3f`): Allow to delete a key of an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| key_uuid | string |  |









### observable_relationships_remove_a_relationship

The following permissions are required:
 - **INTHREAT_WRITE_OBSERVABLES** (`ecc1c462-f164-4b85-8aa8-1ce24b722b7d`): Write observables to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### content_proposals_relationships_update_suggested_changes_to_the_relationship

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| relationship_uuid | string |  |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_relationships_mark_relationship_as_reviewed

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| relationship_uuid | string |  |
| is_reviewed | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### warning_rules_create_a_new_warning_rule

The following permissions are required:
 - **INTHREAT_WRITE_WARNING_RULES** (`9042e6b4-7c86-49a6-b2cb-a66961e1fd71`): Write warning rules to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_create_a_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### post_reports_pdf

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



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







### collections_list_objects

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| feed_id | string |  |
| match[type] | string |  |
| cursor | string |  |
| limit | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| next_cursor | string |  |
| items | string |  |







### post_reports_url

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| url | string |  |
| source_ref | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### upload-observables-inthreat

Upload observables to inthreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| observables | array | List of observables or bundle to upload to inThreat |
| observables_path | string | Path of the observables file to upload inThreat |









### content_proposals_objects_bulk_remove_objects_from_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |
| match[id] | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | array |  |







### kill_chains_get_a_kill_chain

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_objects_reconsider_a_warning__switch_ignored_to_false_

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |
| warning_id | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### relationships_create_a_new_relationship

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### sources_list_sources

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[name] | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### observable_relationships_create_a_new_relationship

The following permissions are required:
 - **INTHREAT_WRITE_OBSERVABLES** (`ecc1c462-f164-4b85-8aa8-1ce24b722b7d`): Write observables to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### objects_get_an_object_notes_and_opinions

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### reports_get_a_report_observables

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### get_objects__object_id__context_

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| object_id | string |  |
| community_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| type | string |  |
| id | string |  |
| objects | string |  |
| spec_version | string |  |







### reports_get_a_report

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



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







### content_proposals_observables_mark_observable_as_reviewed

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| observable_uuid | string |  |
| is_reviewed | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### warning_rules_list_warning_rules

The following permissions are required:
 - **INTHREAT_READ_WARNING_RULES** (`cf16b726-fdc5-43da-9f2f-3e9a734d0cdb`): Read warning rules from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### content_proposals_objects_retrieve_object_changes

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_observables_bulk_create_observables_in_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| data | array |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | array |  |







### list_types_for_assets

Assets of the same type share the same attributes.

One can filter asset types given
* their unique identifier (`match[uuid]`),
* their name (`match[name]`),
* their category (`match[category_name]` and `match[category_uuid]`)

A filter parameter defines filtering on the specified `field`.
A filter parameter can be specified any number of times, where each filter instance specifies
an additional filter to be applied to the resulting data. Said another way,
all filter fields are ANDed together. Each `field` MUST NOT occur more than once in a request.

It should be noted that each `match[]` MAY contain one or more values. Multiple values are separated by a comma
(U+002C COMMA, “,”) without any spaces. If multiple values are present, the match is treated as a logical OR.

Asset types can be sorted given
* their creation date (`sort=created_at`),
* their name (`sort=name`)

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_TYPE** (`d53187c1-b6c4-4660-a2e7-30b598b6150e`): Allow to list types of assets



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| match[uuid] | string |  |
| match[name] | string |  |
| match[category_name] | string |  |
| match[category_uuid] | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### objects_list_stix_objects

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[type] | string |  |
| match[subtype] | string |  |
| match[tlp] | string |  |
| match[source] | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### objects_create_a_new_note_or_opinion

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### creates_a_new_case

This endpoint requires the following parameters:

* `title`: title of the case
* `description`: description of the case
* `status_uuid`: identifier of case’s status
* `priority`: priority of the case.
* `tags`: tags to associate to the case.
* `subscribers`: avatars to associate to the case.

This endpoint accepts (Optional) the following parameters:

* `community_uuid`: the identifier of the community to which the case is associated

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| title | string | Title of the case |
| description | string | Description of the case |
| status_uuid | string | Status of the case |
| community_uuid | string | Identifier of the community |
| priority | string | Priority of the case (low|medium|high) |
| subscribers | array | List of subscribers to the case |
| tags | array |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| updated_at | string |  |
| status | string |  |
| created_by | string |  |
| updated_by | string |  |
| description | string |  |
| community_uuid | string |  |
| priority | string | low|medium|high |
| uuid | string |  |
| short_id | string |  |
| status_uuid | string |  |
| number_of_alerts | integer |  |
| created_by_type | string |  |
| number_of_comments | integer |  |
| subscribers | array |  |
| tags | array | List of tags associated to the case |
| created_at | string |  |
| alerts | array |  |
| updated_by_type | string |  |
| title | string |  |







### creates_a_new_asset

:param dict args: The parameters for the endpoint
:return: The created asset
:rtype: dict

args:
    - asset_type: The type of the asset
    - name: The name of the asset
    - criticity: The criticity of the asset
    - description: The description of the asset
    - attributes: The list of attributes of the asset
    - keys: The list of keys of the asset
    - owners: The list of owners of the asset

The following permissions are required:
 - **ASSETMANAGEMENT_CREATE_ASSET** (`21d1f3d1-1d19-4c56-b027-9d8b6a3183d2`): Allow to create a new asset



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







### content_proposals_objects_bulk_create_objects_in_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| data | array |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | array |  |







### reports_get_a_report_objects

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### observables_list_observables

The following permissions are required:
 - **INTHREAT_READ_OBSERVABLES** (`dd62e001-60f5-464f-aa67-371ca9738e67`): Read observables from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[type] | string |  |
| match[hash] | string |  |
| match[name] | string |  |
| match[value] | string |  |
| match[tag] | string |  |
| match[valid_tag] | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### returns_a_category_type_for_assets

:param dict args: The parameters for the endpoint
:param str uuid: The identifier of the category
:return: The category
:rtype: dict

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_CATEGORY** (`fb8c8a83-6843-4be0-abed-7a0ab32c2b6d`): Allow to list categories of assets
 - **ASSETMANAGEMENT_VIEW_ASSET_TYPE** (`d53187c1-b6c4-4660-a2e7-30b598b6150e`): Allow to list types of assets



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### adds_an_key_to_the_asset

:param dict args: The parameters for the endpoint
:param uuid.UUID uuid: The identifier of the asset
:return: The list of keys
:rtype: dict

args:
    - name: The name of keys
    - value: The value of keys

The following permissions are required:
 - **ASSETMANAGEMENT_CREATE_ASSET_KEY** (`d75c227f-fcc2-41c1-a3b9-557a127ea4c1`): Allow to add a key to an asset



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







### patch_an_alert

Allows to change the type and category of the alert as well as its details and urgency.

The following permissions are required:
 - **SIC_WRITE_ALERTS** (`0e329f9c-173f-4fa0-bbbc-fcfc4bdf7559`): Create, Update and delete SIC alerts



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







### content_proposals_objects_search_objects

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |
| term | string |  |
| type | string |  |
| fill_with_consolidated | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| next_cursor | string |  |
| items | string |  |







### objects_search_objects

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| term | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### list_alerts

An alert denotes the sigthing of one or more indicator given a set of events.
This paginates endpoint list all the produced SIC alerts. A set of filters can be
specified to focus on certain alerts.

One can filter alerts given
* the entity the alert refers to (`match[entity_name]` and `match[entity_uuid]`),
* the current status of the alert by the identifier of the status (`match[status_uuid]`),
* the current status of the alert by the name of the status (`match[status_name]`),
* the alert type (`match[type_category]`, `match[type_value]`),
* the source of the alert (`match[source]`),
* the target of the alert (`match[target]`),
* either the source or the target of the alert (`match[node]`),
* any STIX object contained in the alert by refering its identifier (`match[stix_object]`),
* the rule that triggered the alert (`match[rule_uuid]` and `match[rule_name]`),
* a range on the creation date of the alert (`date[created_at]`),
* a range on the update date of the alert (`date[updated_at]`),
* the alert urgency (`match[urgency]`),
* the short_id (`match[short_id]`)
* the title (`match[title]`)
* the similarity (`match[similar]`)

A filter parameter defines filtering on the specified `field`.
A filter parameter can be specified any number of times, where each filter instance specifies
an additional filter to be applied to the resulting data. Said another way,
all filter fields are ANDed together. Each `field` MUST NOT occur more than once in a request.

It should be noted that each `match[]` MAY contain one or more values. Multiple values are separated by a comma
(U+002C COMMA, “,”) without any spaces. If multiple values are present, the match is treated as a logical OR.

Alerts can be sorted given
* its creation date (`sort=created_at`),
* its update date (`sort=updated_at`),
* its source or target (`sort=source`, `sort=target`),
* its urgency (`sort=urgency`),
* the rule that triggered it (`sort=rule_name`),
* the entity is applies on (`sort=entity`),
* the alert type (`sort=type'),
* its status (`sort=status`).
* its similarity (`sort=similar`).

One can sort ascending or descending by specifing `direction=asc` or `direction=desc`.

The following permissions are required:
 - **SIC_READ_ALERTS** (`9ea2b8a3-593f-4bab-92f5-d0af9b563f6f`): List and consult SIC alerts



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







### create_a_new_comment_on_a_case

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| content | string | content of the comment |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| created_by | string |  |
| content | string |  |
| updated_at | string |  |
| created_at | string |  |
| created_by_type | string |  |
| uuid | string |  |







### lists_keys_of_an_assets

:param dict args: The parameters for the endpoint
:param uuid.UUID uuid: The identifier of the asset
:return: The list of keys
:rtype: dict

args:
    - offset: The position of the first asset
    - limit: The number of asset to return

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_KEY** (`579a9221-8ade-4f91-b16b-2495f3c35957`): Allow to retrieve or list keys of an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### get_objects__object_id__files__hash_

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat
 - **INTHREAT_RESTRICTED_ACCESS** (`819c3f13-2a52-4fac-af25-e1ed727b2778`): Customer access to the application



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| object_id | string |  |
| hash | string |  |









### content_proposals_objects_retrieve_relationships

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |
| limit | integer |  |
| offset | integer |  |
| fill_with_consolidated | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### observable_relationships_get_a_relationship

The following permissions are required:
 - **INTHREAT_READ_OBSERVABLES** (`dd62e001-60f5-464f-aa67-371ca9738e67`): Read observables from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### deny_a_countermeasure

An optional comment can be provided to
be attached to the countermeasure.

The following permissions are required:
 - **SIC_WRITE_ALERTS** (`0e329f9c-173f-4fa0-bbbc-fcfc4bdf7559`): Create, Update and delete SIC alerts



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







### get_images__name_

None



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| name | string |  |









### reports_list_stix_reports

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### observables_get_an_observable_relationships

The following permissions are required:
 - **INTHREAT_READ_OBSERVABLES** (`dd62e001-60f5-464f-aa67-371ca9738e67`): Read observables from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### content_proposals_objects_ignore_a_warning

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |
| warning_id | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### lists_names_for_keys_of_asset

:param dict args: The parameters for the endpoint
:return: The list of attribute names
:rtype: dict

args:
    - category: Option to filter attribute names according to associated category
    - type: Option to filter attribute names according to associated type
    - offset: The position of the first category
    - limit: The number of category to return

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ATTRIBUTE_NAME** (`8734c047-de38-4693-9ca4-3e9ffdccde1a`): Allow to list attribute names



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| category | string |  |
| type | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### objects_get_an_object_reports

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### content_proposals_objects_list_merge_proposal_objects_that_have_been_modified

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |
| match[type] | string |  |
| match[name] | string |  |
| has_warnings | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| next_cursor | string |  |
| items | string |  |







### content_proposals_bulk_merge_content_proposals

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[id] | string |  |









### feeds_list_feeds

The following permissions are required:
 - **INTHREAT_READ_FEEDS** (`b30103ab-408d-4ccf-86c9-3d9a820c97d9`): Read feeds from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### post-stix-bundle

POST STIX bundle to inthreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| bundle | object | STIX Bundle to upload to inThreat |
| bundle_path | string | Path of the STIX Bundle to upload to inThreat |
| auto_merge | boolean | Whether or not the uploaded bundle can automatically be merged to the consolidated database |
| enrich | boolean | Whether or not the uploaded bundle should be enriched |
| name | string | Name to use for the new Content Proposal |
| assigned_to | string | Avatar assigned to the content proposal |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| file_name | string |  |
| content_proposal_id | string |  |







### returns_a_type_for_assets

:param str uuid: The identifier of the type
:return: The type
:rtype: dict

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_TYPE** (`d53187c1-b6c4-4660-a2e7-30b598b6150e`): Allow to list types of assets



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| name | string |  |
| description | string |  |







### content_proposals_relationships_add_new_relationship_to_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### returns_an_attribute_of_an_asset

:param uuid.UUID uuid: The identifier of the asset
:param uuid.UUID attribute_uuid: The identifier of the attribute
:return: The attribute
:rtype: dict

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_ATTRIBUTE** (`9541580b-8ced-4037-a534-28666ca8fcf8`): Allow to retrieve or list attributes of an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| attribute_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| value | string |  |
| uuid | string |  |
| name | string |  |







### content_proposals_list_content_proposals

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[assigned_to] | string |  |
| match[reviewer] | string |  |
| match[status] | string |  |
| match[source_ref] | string |  |
| match[name] | string |  |
| sort | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### get_the_list_of_comments_of_a_case

The following permissions are required:
 - **SIC_READ_INCIDENTS** (`7c0bac3f-f2ce-491b-b663-638145078516`): Get incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| limit | integer |  |
| offset | integer |  |
| date[created_at] | string |  |
| match[created_by] | string |  |
| sort | string |  |
| direction | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| items | array |  |







### expiration_rules_create_a_new_expiration_rule

The following permissions are required:
 - **INTHREAT_WRITE_EXPIRATION_RULES** (`ad10236c-d732-4690-98b3-1bde06b4bca1`): Write expiration rules to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### expiration_rules_list_expiration_rules

The following permissions are required:
 - **INTHREAT_READ_EXPIRATION_RULES** (`506b1320-2c46-4712-83e3-d8a95c685324`): Read expiration rules from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### content_proposals_objects_mark_object_as_reviewed

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |
| is_reviewed | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_reject_a_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### get_a_tracker_notification

The following permissions are required:
 - **INTHREAT_READ_TRACKER_NOTIFICATIONS** (`5616eb17-1e1b-4337-b8ce-9cb109184075`): Read tracker notifications from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### feeds_get_a_feed

The following permissions are required:
 - **INTHREAT_READ_FEEDS** (`b30103ab-408d-4ccf-86c9-3d9a820c97d9`): Read feeds from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### get_an_incident

This endpoint accepts the following querystrings:

* `?community_uuid=community_uuid1` to return an incident belonged to the community identified by `community_uuid1` # noqa

The following permissions are required:
 - **SIC_READ_INCIDENTS** (`7c0bac3f-f2ce-491b-b663-638145078516`): Get incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| incident_uuid | string |  |
| community_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| description | string |  |
| created_by_type | string |  |
| created_at | string |  |
| created_by | string |  |
| updated_by_type | string |  |
| status | string |  |
| updated_by | string |  |
| status_uuid | string |  |
| title | string |  |
| uuid | string |  |
| community_uuid | string |  |
| blocks | array |  |
| updated_at | string |  |
| short_id | string |  |







### objects_revoke_an_object

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### content_proposals_relationships_bulk_remove_relationships_from_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |
| match[id] | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | array |  |







### observables_search_observables

The following permissions are required:
 - **INTHREAT_READ_OBSERVABLES** (`dd62e001-60f5-464f-aa67-371ca9738e67`): Read observables from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| term | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### content_proposals_observables_add_new_observable_to_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### objects_get_an_object_sources

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### qualify_a_tracker_notification

The following permissions are required:
 - **INTHREAT_WRITE_TRACKER_NOTIFICATIONS** (`ff760d5b-f93b-4a71-b0b6-23280d5c0090`): Write tracker notifications to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| status | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### list_tracker_rules

The following permissions are required:
 - **INTHREAT_READ_TRACKER_RULES** (`34c333ab-9ad4-46ff-a888-1b9ac1c329fd`): Read tracker rules from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[name] | string |  |
| match[ruleset_name] | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### returns_a_category_for_assets

:param dict args: The parameters for the endpoint
:param str uuid: The identifier of the category
:return: The category
:rtype: dict

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_CATEGORY** (`fb8c8a83-6843-4be0-abed-7a0ab32c2b6d`): Allow to list categories of assets
 - **ASSETMANAGEMENT_VIEW_ASSET_TYPE** (`d53187c1-b6c4-4660-a2e7-30b598b6150e`): Allow to list types of assets



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### get_the_comment_of_a_case

The following permissions are required:
 - **SIC_READ_INCIDENTS** (`7c0bac3f-f2ce-491b-b663-638145078516`): Get incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| comment_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| created_by | string |  |
| content | string |  |
| updated_at | string |  |
| created_at | string |  |
| created_by_type | string |  |
| uuid | string |  |







### objects_get_an_object_duplicates

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### returns_an_asset

:param str uuid: The identifier of the asset
:return: The asset
:rtype: dict

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET** (`4b0f38a9-a890-4f9b-ae7a-e5025162ff33`): Allow to retrieve or list assets



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






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







### content_proposals_objects_retrieve_observables

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |
| fill_with_consolidated | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### post_a_comment_on_an_alert

The following permissions are required:
 - **WRITE_ALERTS_COMMENTS** (`341436f9-1c33-4cf7-bec3-a6955133ea04`): Post a comment on an alert



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







### lists_cases

This endpoint exposes filters that can narrow down the returned cases:

* `?match['status_uuid']=status_uuid1,status_uuid2` to filter for cases with the statuses identified by `status_uuid1` or `status_uuid2`
* `?match['status_name']=status_name1,status_name2` to filter for cases with the statuses identified by `status_name1` or `status_name2`
* `?match['reference']=reference1,reference2` to filter for cases with the references `reference1` or `reference2` set in their blocks
* `?date['created_at']=start_date,end_date` to filter for cases created from `start_date` to ènd_date
* `?match['community_uuid']=community_uuid1` to filter for cases belonged to the community identified by `community_uuid`
* `?match['assignees']=avatar_uuid1,avatar_uuid2` to filter for cases with the subscribers identified by `avatar_uuid1` or `avatar_uuid2`
* `?match['title']=title1,title2` to filter cases with their title
* `?match['alert_uuid']=alert_uuid1,alert_uuid2` to filter for cases associated to alerts identified by `alert_uuid1` or `alert_uuid2`

The following permissions are required:
 - **SIC_READ_INCIDENTS** (`7c0bac3f-f2ce-491b-b663-638145078516`): Get incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| date[created_at] | string |  |
| match[tags] | string |  |
| match[assignees] | string |  |
| match[created_by] | string |  |
| match[title] | string |  |
| match[alert_uuid] | string |  |
| match[priority] | string |  |
| match[community_uuid] | string |  |
| limit | integer |  |
| offset | integer |  |
| match[status_uuid] | string |  |
| match[status_name] | string |  |
| sort | string |  |
| direction | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| items | array |  |







### feeds_remove_a_feed

The following permissions are required:
 - **INTHREAT_WRITE_FEEDS** (`a24140c3-8088-4120-aaf1-6df0f893e700`): Write feeds to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### create_a_new_block

This endpoint requires the following parameters:

* `title`: the title of the block
* `content`: the content of the block
* `is_relevant`: the relevance of the block
* `object_refs`: a list of reference to objects

This endpoint accepts (Optional) the following parameters:

* `community_uuid`: the identifier of the community to which the block is associated

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| incident_uuid | string |  |
| title | string | The title of the true |
| content | string | The content of the true |
| is_relevant | boolean | Flag to set the relevance of the block |
| object_refs | array |  |
| community_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| created_by_type | string |  |
| created_at | string |  |
| created_by | string |  |
| content | string |  |
| is_relevant | boolean |  |
| updated_by_type | string |  |
| updated_by | string |  |
| object_refs | array |  |
| title | string |  |
| uuid | string |  |
| updated_at | string |  |
| short_id | string |  |







### create_an_alert

The provided details are used to specify the alert to create.
The alert creation process is performed asynchronously and
in consequence this methods returns the creation task status.

The following permissions are required:
 - **SIC_WRITE_ALERTS** (`0e329f9c-173f-4fa0-bbbc-fcfc4bdf7559`): Create, Update and delete SIC alerts



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







### expiration_rules_remove_an_expiration_rule

The following permissions are required:
 - **INTHREAT_WRITE_EXPIRATION_RULES** (`ad10236c-d732-4690-98b3-1bde06b4bca1`): Write expiration rules to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### returns_an_key_of_an_asset

:param uuid.UUID uuid: The identifier of the asset
:param uuid.UUID key_uuid: The identifier of the key
:return: The key
:rtype: dict

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_KEY** (`579a9221-8ade-4f91-b16b-2495f3c35957`): Allow to retrieve or list keys of an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| key_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| value | string |  |
| uuid | string |  |
| name | string |  |







### list_incidents

This endpoint exposes filters that can narrow down the returned incidents:

* `?match['status_uuid']=status_uuid1,status_uuid2` to filter for incidents with the statuses identified by `status_uuid1` or `status_uuid2` # noqa
* `?match['status_name']=status_name1,status_name2` to filter for incidents with the statuses identified by `status_name1` or `status_name2` # noqa
* `?match['reference']=reference1,reference2` to filter for incidents with the references `reference1` or `reference2` set in their blocks # noqa
* `?date['created_at']=start_date,end_date` to filter for incidents created from `start_date` to ènd_date
* `?match['community_uuid']=community_uuid1` to filter for incidents belonged to the community identified by `community_uuid` # noqa

The following permissions are required:
 - **SIC_READ_INCIDENTS** (`7c0bac3f-f2ce-491b-b663-638145078516`): Get incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| date[created_at] | string |  |
| match[status_uuid] | string |  |
| match[status_name] | string |  |
| match[reference] | string |  |
| match[community_uuid] | string |  |
| sort | string |  |
| direction | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### lists_owners_of_an_assets

:param dict args: The parameters for the endpoint
:param uuid.UUID uuid: The identifier of the asset
:return: The list of owners
:rtype: dict

args:
    - offset: The position of the first asset
    - limit: The number of asset to return

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_ONwER** (`79dcf483-334b-467a-bb85-f6bb93476089`): Allow to retrieve or list owners of an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### observable_relationships_list_observables_relationships

The following permissions are required:
 - **INTHREAT_READ_OBSERVABLES** (`dd62e001-60f5-464f-aa67-371ca9738e67`): Read observables from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### warning_rules_get_a_warning_rule

The following permissions are required:
 - **INTHREAT_READ_WARNING_RULES** (`cf16b726-fdc5-43da-9f2f-3e9a734d0cdb`): Read warning rules from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_reopen_a_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### content_proposals_observables_bulk_remove_observables_from_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |
| match[id] | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | array |  |







### get_a_tracker_rule_quality

The following permissions are required:
 - **INTHREAT_READ_TRACKER_RULES** (`34c333ab-9ad4-46ff-a888-1b9ac1c329fd`): Read tracker rules from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| quality | number |  |







### deletes_an_owner_from_an_asset

:param uuid.UUID uuid: The identifier of the asset
:param uuid.UUID owner_uuid: The identifier of the owner to delete

The following permissions are required:
 - **ASSETMANAGEMENT_DELETE_ASSET_OWNER** (`b1b68459-40e5-4292-b2d4-e45250905836`): Allow to delete an owner of an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| owner_uuid | string |  |









### content_proposals_observables_list_merge_proposal_observables_that_have_been_modified

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### create_a_new_tracker_notification

The following permissions are required:
 - **INTHREAT_WRITE_TRACKER_NOTIFICATIONS** (`ff760d5b-f93b-4a71-b0b6-23280d5c0090`): Write tracker notifications to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_relationships_bulk_create_relationships_in_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| data | array |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | array |  |







### list_assets

An asset denotes a resource of interest that is part of your defensive perimeter.
This paginated endpoint list all the assets. A set of filters can be specified to focus
on certain asset.

If the extended flag is set (`extended=True`), listing includes the keys and attributes of the assets.

One can filter assets given
* their unique identifier (`match[uuid]`),
* their name (`match[name]`),
* their category (`match[category_name]`, `match[category_uuid]`),
* their type (`match[type_name]`, `match[type_uuid]`),
* the range on the criticity of the asset (`range[criticity]`),
* the range on the creation date of the asset (`date[created_at]`),
* the range on the update date of the asset (`date[updated_at]`),

A filter parameter defines filtering on the specified `field`.
A filter parameter can be specified any number of times, where each filter instance specifies
an additional filter to be applied to the resulting data. Said another way,
all filter fields are ANDed together. Each `field` MUST NOT occur more than once in a request.

It should be noted that each `match[]` MAY contain one or more values. Multiple values are separated by a comma
(U+002C COMMA, “,”) without any spaces. If multiple values are present, the match is treated as a logical OR.

Assets can be sorted given
* their creation date (`sort=created_at`),
* their update date (`sort=updated_at`),
* their name (`sort=name`),
* their criticality (`sort=criticality`)
* their category (`sort=category_name`, `sort=category_uuid`),
* their type (`sort=type_name`, `sort=type_uuid`)

One can sort ascending or descending by specifying `direction=asc` or `direction=desc`.

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET** (`4b0f38a9-a890-4f9b-ae7a-e5025162ff33`): Allow to retrieve or list assets



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| extended | boolean |  |
| match[community_uuid] | string |  |
| match[uuid] | string |  |
| match[name] | string |  |
| match[category_name] | string |  |
| match[category_uuid] | string |  |
| match[type_name] | string |  |
| match[type_uuid] | string |  |
| range[criticality] | string |  |
| date[created_at] | string |  |
| date[updated_at] | string |  |
| sort | string |  |
| direction | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### lists_attributes_of_an_assets

:param dict args: The parameters for the endpoint
:param uuid.UUID uuid: The identifier of the asset
:return: The list of attributes
:rtype: dict

args:
    - offset: The position of the first asset
    - limit: The number of asset to return

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_ATTRIBUTE** (`9541580b-8ced-4037-a534-28666ca8fcf8`): Allow to retrieve or list attributes of an asset



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### content_proposals_observables_search_observables

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |
| term | string |  |
| type | string |  |
| fill_with_consolidated | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### post_images_

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| file | string |  |









### convert_a_notification_into_a_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| auto_merge | boolean |  |
| name | string |  |
| enrich | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### observables_get_an_observable_reports

The following permissions are required:
 - **INTHREAT_READ_OBSERVABLES** (`dd62e001-60f5-464f-aa67-371ca9738e67`): Read observables from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | string |  |
| total | integer |  |







### observables_get_an_observable

The following permissions are required:
 - **INTHREAT_READ_OBSERVABLES** (`dd62e001-60f5-464f-aa67-371ca9738e67`): Read observables from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### remove_a_tracker_rule

The following permissions are required:
 - **INTHREAT_WRITE_TRACKER_RULES** (`f7bb8b40-35d5-4fc4-9c65-2ceace0e4734`): Write tracker rules to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### get_a_cyber_kill_chain_stage

This endpoint can be use to retrieve the definition of
a Cyber Kill Chain Step following either its unique identifier or its short id (`uuid`).

The following permissions are required:
 - **SIC_READ_ALERTS** (`9ea2b8a3-593f-4bab-92f5-d0af9b563f6f`): List and consult SIC alerts



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string | Unique identifier of the kill chain step |
| description | string | description of the kill chain step |
| name | string | name of the kill chain step |
| stix_name | string | The STIXv2 name for this kill chain step |
| order_id | integer | Order identifier of the kill chain step |
| short_id | string | Unique short id of the kill chain step |







### relationships_revoke_a_relationship

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |









### returns_an_attribute_name

:param str uuid: The identifier of the attribute name
:return: The attribute name
:rtype: dict

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ATTRIBUTE_NAME** (`8734c047-de38-4693-9ca4-3e9ffdccde1a`): Allow to list attribute names



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| name | string |  |
| asset_type | string |  |
| description | string |  |
| asset_category | string |  |







### content_proposals_observables_retrieve_indicators

The following permissions are required:
 - **INTHREAT_READ_CONTENT_PROPOSALS** (`5f4b1f5b-cab7-49a7-8f95-d897ec262289`): Read InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |
| fill_with_consolidated | boolean |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| next_cursor | string |  |
| items | string |  |







### content_proposals_objects_remove_object_changes_from_the_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| object_uuid | string |  |









### relationships_list_stix_relationships

The following permissions are required:
 - **INTHREAT_READ_OBJECTS** (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### observables_create_a_new_observable

The following permissions are required:
 - **INTHREAT_WRITE_OBSERVABLES** (`ecc1c462-f164-4b85-8aa8-1ce24b722b7d`): Write observables to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | string |  |







### feeds_create_a_new_feed

The following permissions are required:
 - **INTHREAT_WRITE_FEEDS** (`a24140c3-8088-4120-aaf1-6df0f893e700`): Write feeds to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### content_proposals_observables_remove_observable_changes_from_the_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| observable_uuid | string |  |









### lists_categories_for_assets

:param dict args: The parameters for the endpoint
:return: The list of categories
:rtype: dict

args:
    - offset: The position of the first category
    - limit: The number of category to return

The following permissions are required:
 - **ASSETMANAGEMENT_VIEW_ASSET_CATEGORY** (`fb8c8a83-6843-4be0-abed-7a0ab32c2b6d`): Allow to list categories of assets



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items | array |  |
| total | integer |  |







### adds_an_attribute_to_the_asset

:param dict args: The parameters for the endpoint
:param uuid.UUID uuid: The identifier of the asset
:return: The list of attributes
:rtype: dict

args:
    - name: The name of attributes
    - value: The value of attributes

The following permissions are required:
 - **ASSETMANAGEMENT_CREATE_ASSET_ATTRIBUTE** (`23207f56-0cff-4879-b4d9-29387ef3ee77`): Allow to add an attribute to an asset



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







### predict_the_state_of_an_alert

The following permissions are required:
 - **PREDICTION_PREDICT_ALERT** (`fe76d027-e000-4816-bb0e-5ba27edcb4a1`): Predict the state of an alert



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| alert | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| worth_human_attention | boolean |  |







### content_proposals_objects_add_new_object_to_content_proposal

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |
| data | object |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### get_a_tracker_rule

The following permissions are required:
 - **INTHREAT_READ_TRACKER_RULES** (`34c333ab-9ad4-46ff-a888-1b9ac1c329fd`): Read tracker rules from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |







### lists_alerts_associated_to_the_case_uuid

The following permissions are required:
 - **SIC_READ_INCIDENTS** (`7c0bac3f-f2ce-491b-b663-638145078516`): Get incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| has_more | boolean |  |
| items | array |  |







### get_a_case

This endpoint accepts the following querystrings:

* `?community_uuid=community_uuid1` to return an case belonged to the community identified by `community_uuid1`

The following permissions are required:
 - **SIC_READ_INCIDENTS** (`7c0bac3f-f2ce-491b-b663-638145078516`): Get incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| community_uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| updated_at | string |  |
| status | string |  |
| created_by | string |  |
| updated_by | string |  |
| description | string |  |
| community_uuid | string |  |
| priority | string | low|medium|high |
| uuid | string |  |
| short_id | string |  |
| status_uuid | string |  |
| number_of_alerts | integer |  |
| created_by_type | string |  |
| number_of_comments | integer |  |
| subscribers | array |  |
| tags | array | List of tags associated to the case |
| created_at | string |  |
| alerts | array |  |
| updated_by_type | string |  |
| title | string |  |







### post_objects__object_id__files_

The following permissions are required:
 - **INTHREAT_WRITE_OBJECTS** (`33ea2a27-26ee-434e-a072-f064617f9f6d`): Write objects to InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| object_id | string |  |
| file | string |  |









### content_proposals_bulk_reject_content_proposals

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[id] | string |  |









### update_a_comment_of_a_case

The following permissions are required:
 - **SIC_WRITE_INCIDENTS** (`e56fb404-268b-47d2-abad-d68d86ddf7bd`): Edit incidents



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| case_uuid | string |  |
| comment_uuid | string |  |
| content | string | content of the comment |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| created_by | string |  |
| content | string |  |
| updated_at | string |  |
| created_at | string |  |
| created_by_type | string |  |
| uuid | string |  |







### content_proposals_bulk_update_content_proposals

The following permissions are required:
 - **INTHREAT_WRITE_CONTENT_PROPOSALS** (`623f27aa-7778-49db-b6fa-9d1e25e2e0b4`): Modify InThreat content proposals



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| limit | integer |  |
| offset | integer |  |
| match[id] | string |  |
| data | object |  |









### expiration_rules_get_an_expiration_rule

The following permissions are required:
 - **INTHREAT_READ_EXPIRATION_RULES** (`506b1320-2c46-4712-83e3-d8a95c685324`): Read expiration rules from InThreat



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| uuid | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| data | object |  |












## Extra

Module **sekoia.io v.1.63**
