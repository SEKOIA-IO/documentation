uuid: 92d8bb47-7c51-445d-81de-ae04edbb6f0a
name: Sekoia.io
type: playbook

# Sekoia.io

![Sekoia.io](/assets/playbooks/library/sekoia-io.png){ align=right width=150 }

Sekoia.io is a European Cybertech, expert in intelligence-based eXtended Detection and Response solutions. Our Sekoia SOC platform provides a unified view and full control of the perimeter to be defended. Our mission is to empower security operations teams with a flexible and easy-to-use platform. We protect large companies, technology scaleups, governments, and Tier One MSSP partners worldwide. 

## Configuration

This module accepts no configuration.

## Triggers

### Alert Comment Created

A comment was added to an existing Alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rule_filter` | `string` | Create a run only for alerts matching a rule name |
| `rule_names_filter` | `array` | Create a run only for alerts matching a list of rule name |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `comment` | `object` | Alert comment (object containing comment uuid, content, author, date). |
| `file_path` | `string` | File path to the alert on disk. |
| `event_type` | `string` | Action that triggered this Sekoia.io Alert notification (could be for example “alert-created”, “alert-status-changed”, etc.) |
| `alert_uuid` | `string` | Unique identifier of the Alert (UUID string). |
| `short_id` | `string` | Unique short identifier of the Alert. |
| `status` | `object` | Status of the Alert (object containing status description and name). |
| `created_at` | `integer` | Creation date of the Alert (timestamp). |
| `urgency` | `integer` | Current urgency of the Alert. |
| `entity` | `object` | Description of the entity involved with this Alert (object containing entity UUID and name). |
| `alert_type` | `object` | Category of the Alert |
| `rule` | `object` |  |
| `first_seen_at` | `string` |  |
| `last_seen_at` | `string` |  |


### Alert Created

A new Alert was created in the Operation Center

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rule_filter` | `string` | Create a run only for alerts matching a rule name |
| `rule_names_filter` | `array` | Create a run only for alerts matching a list of rule name |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | File path to the alert on disk. |
| `event_type` | `string` | Action that triggered this Sekoia.io Alert notification (could be for example “alert-created”, “alert-status-changed”, etc.) |
| `alert_uuid` | `string` | Unique identifier of the Alert (UUID string). |
| `short_id` | `string` | Unique short identifier of the Alert. |
| `status` | `object` | Status of the Alert (object containing status description and name). |
| `created_at` | `integer` | Creation date of the Alert (timestamp). |
| `urgency` | `integer` | Current urgency of the Alert. |
| `entity` | `object` | Description of the entity involved with this Alert (object containing entity UUID and name). |
| `alert_type` | `object` | Category of the Alert |
| `rule` | `object` |  |
| `first_seen_at` | `string` |  |
| `last_seen_at` | `string` |  |


### Alert Status Changed

The status of an existing alert was changed

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rule_filter` | `string` | Create a run only for alerts matching a rule name |
| `rule_names_filter` | `array` | Create a run only for alerts matching a list of rule name |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | File path to the alert on disk. |
| `event_type` | `string` | Action that triggered this Sekoia.io Alert notification (could be for example “alert-created”, “alert-status-changed”, etc.) |
| `alert_uuid` | `string` | Unique identifier of the Alert (UUID string). |
| `short_id` | `string` | Unique short identifier of the Alert. |
| `status` | `object` | Status of the Alert (object containing status description and name). |
| `created_at` | `integer` | Creation date of the Alert (timestamp). |
| `urgency` | `integer` | Current urgency of the Alert. |
| `entity` | `object` | Description of the entity involved with this Alert (object containing entity UUID and name). |
| `alert_type` | `object` | Category of the Alert |
| `rule` | `object` |  |
| `first_seen_at` | `string` |  |
| `last_seen_at` | `string` |  |


### Alert Updated

An existing alert was updated

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rule_filter` | `string` | Create a run only for alerts matching a rule name |
| `rule_names_filter` | `array` | Create a run only for alerts matching a list of rule name |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | File path to the alert on disk. |
| `event_type` | `string` | Action that triggered this Sekoia.io Alert notification (could be for example “alert-created”, “alert-status-changed”, etc.) |
| `alert_uuid` | `string` | Unique identifier of the Alert (UUID string). |
| `short_id` | `string` | Unique short identifier of the Alert. |
| `status` | `object` | Status of the Alert (object containing status description and name). |
| `created_at` | `integer` | Creation date of the Alert (timestamp). |
| `urgency` | `integer` | Current urgency of the Alert. |
| `entity` | `object` | Description of the entity involved with this Alert (object containing entity UUID and name). |
| `alert_type` | `object` | Category of the Alert |
| `rule` | `object` |  |
| `first_seen_at` | `string` |  |
| `last_seen_at` | `string` |  |


### Manual Trigger

Webhook Trigger to receive specific Sekoia.io Alerts

**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_uuid` | `string` | Unique identifier of the Alert (UUID string). |


### Case Alerts Updated

Alerts have been added to or removed from a case

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `mode_filter` | `string` | Create a run only for cases matching a mode (automatic or manual) |
| `priority_uuids_filter` | `array` | Create a run only for cases matching a list of priority uuids |
| `assignees_filter` | `array` | Create a run only for cases matching a list of assignees |
| `case_uuids_filter` | `array` | Create a run only for cases matching a list of case uuids/short ids |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | Unique identifier of the Case (UUID string). |
| `short_id` | `string` | Unique short identifier of the Case. |
| `added_alerts` | `array` | List of Unique identifier of new alerts (UUID string). |
| `deleted_alerts` | `array` | List of Unique identifier of removed alerts (UUID string). |


### Case Created

A new Case was created in the Operation Center

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `mode_filter` | `string` | Create a run only for cases matching a mode (automatic or manual) |
| `priority_uuids_filter` | `array` | Create a run only for cases matching a list of priority uuids |
| `assignees_filter` | `array` | Create a run only for cases matching a list of assignees |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | Unique identifier of the Case (UUID string). |
| `short_id` | `string` | Unique short identifier of the Case. |
| `created_at` | `string` | Creation date of the Case. |
| `created_by` | `string` | User who created the Case. |
| `mode` | `string` | Mode of the Case (automatic or manual). |
| `title` | `string` | Title of the Case. |
| `description` | `string` | Description of the Case. |
| `community_uuid` | `string` | Unique identifier of the Community (UUID string). |
| `assignees` | `array` | List of assignees of the Case. |
| `priority_uuid` | `string` | Unique identifier of the Priority (UUID string). |
| `status_uuid` | `string` | Unique identifier of the Status (UUID string). |
| `tags` | `array` | List of tags of the Case. |


### Case Updated

An existing case was updated

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `mode_filter` | `string` | Create a run only for cases matching a mode (automatic or manual) |
| `priority_uuids_filter` | `array` | Create a run only for cases matching a list of priority uuids |
| `assignees_filter` | `array` | Create a run only for cases matching a list of assignees |
| `case_uuids_filter` | `array` | Create a run only for cases matching a list of case uuids/short ids |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | Unique identifier of the Case (UUID string). |
| `short_id` | `string` | Unique short identifier of the Case. |
| `created_at` | `string` | Creation date of the Case. |
| `updated_at` | `string` | Updated date of the Case. |
| `updated_by` | `string` | User who updated the Case. |
| `title` | `string` | Title of the Case. |
| `description` | `string` | Description of the Case. |
| `assignees` | `array` | List of assignees of the Case. |
| `tags` | `array` | List of tags of the Case. |
| `status_uuid` | `string` | Unique identifier of the Status (UUID string). |
| `priority_uuid` | `string` | Unique identifier of the Priority (UUID string). |
| `verdict_uuid` | `string` | Unique identifier of the Verdict (UUID string). |


### Feed Consumption

Get all non-revoked objects from Sekoia.io Intelligence feed

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `feed_id` | `string` | ID of the Sekoia.io feed to get data from |
| `batch_size_limit` | `integer` | Size of the batch of elements to get from the Sekoia.io feed in one time |
| `modified_after` | `string` | Date from which IOCs should be retrieved. It must be a valid RFC-3339 date-time string (i.e. 2024-04-12T23:20:50.52Z) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |


### Feed IOC Consumption

Get all valid IOCs from Sekoia.io Intelligence feed

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `feed_id` | `string` | ID of the Sekoia.io feed to get data from |
| `batch_size_limit` | `integer` | Size of the batch of elements to get from the Sekoia.io feed in one time |
| `modified_after` | `string` | Date from which IOCs should be retrieved. It must be a valid RFC-3339 date-time string (i.e. 2024-04-12T23:20:50.52Z) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects_path` | `string` | Filepath of the STIX objects fetched from the collection |


### Any Alert Update

Create an event for each alert creation or modification

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rule_filter` | `string` | Create a run only for alerts matching a rule name |
| `rule_names_filter` | `array` | Create a run only for alerts matching a list of rule name |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | File path to the alert on disk. |
| `event_type` | `string` | Action that triggered this Sekoia.io Alert notification (could be for example “alert-created”, “alert-status-changed”, etc.) |
| `alert_uuid` | `string` | Unique identifier of the Alert (UUID string). |
| `short_id` | `string` | Unique short identifier of the Alert. |
| `status` | `object` | Status of the Alert (object containing status description and name). |
| `created_at` | `integer` | Creation date of the Alert (timestamp). |
| `urgency` | `integer` | Current urgency of the Alert. |
| `entity` | `object` | Description of the entity involved with this Alert (object containing entity UUID and name). |
| `alert_type` | `object` | Category of the Alert |
| `rule` | `object` |  |
| `first_seen_at` | `string` |  |
| `last_seen_at` | `string` |  |

## Actions

### Activate Countermeasure

Mark as active a countermeasure

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `cm_uuid` | `string` |  |
| `comment` | `object` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `action_steps` | `array` |  |
| `activated_by_type` | `string` | Type of the profile that activated the countermeasure |
| `comments` | `array` |  |
| `activated_at` | `string` | Date the countermeasure was activated |
| `relevance` | `integer` | Relevance of the countermeasure |
| `denied_by_type` | `string` | Type of the profile that denied the countermeasure |
| `status` | `string` | (deprecated) Status of the countermeasure |
| `created_by` | `string` | UUID of profile that created the countermeasure |
| `model_uuid` | `string` | UUID of the model from which this countermeasure has been created |
| `activated_by` | `string` | UUID of profile that activated the countermeasure |
| `description` | `string` | Description of the countermeasure |
| `name` | `string` | Name of the countermeasure |
| `uuid` | `string` | UUID of the countermeasure |
| `duration` | `string` | Estimated duration to apply the countermeasures |
| `alert_uuid` | `string` | UUID of the alert related to the countermeasure |
| `denied_at` | `string` | Date the countermeasure was denied |
| `created_by_type` | `string` | Type of the profile that created the countermeasure |
| `course_of_action` | `object` | (deprecated) STIX2 object course of action |
| `dynamic_relevance` | `integer` | Dynamic relevance of the countermeasure |
| `denied_by` | `string` | UUID of profile that denied the countermeasure |
| `assignee` | `string` | UUID of the profile assigned to the progress of the countermeasure |
| `created_at` | `string` | Date the countermeasure was created |

### Add events to a case

Add events to a case

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | UUID of the case |
| `event_ids` | `array` | List of event identifiers (__event_id) to add to the case. Do not use event.id which is a different identifier. |

### Add IOC to IOC Collection

Add indicators to an IOC Collection

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `indicators` | `array` | List of indicators to add to an IOC collection |
| `indicators_path` | `string` | Path of the indicators file to add to an IOC collection |
| `ioc_collection_id` | `string` | Identifier of the IOC collection |
| `indicator_type` | `string` | Type of IOC |
| `valid_for` | `integer` | Validity period for the created indicators (in days) |

### Add attribute to Asset

Add an attribute to an asset

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `name` | `string` |  |
| `value` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `value` | `string` |  |
| `uuid` | `string` |  |
| `name` | `string` |  |

### Add key to Asset

Adds a key to an asset

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `name` | `string` |  |
| `value` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `value` | `string` |  |
| `uuid` | `string` |  |
| `name` | `string` |  |

### Merge Assets

Merge a list of assets into a targeted asset

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `destination` | `string` |  |
| `sources` | `array` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status_code` | `integer` |  |
| `headers` | `object` |  |
| `text` | `string` |  |

### Attach Alerts to Case

Attach one or more alerts to a specific case

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `case_uuid` | `string` |  |
| `alerts` | `array` | The list of identifiers of alerts to add |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` |  |

### Create Tracker Notification

Create a notification for a specific tracker

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `object` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `object` |  |

### Create case

Creates a new case

**Configuration**

{'description': 'description of the case', 'type': 'string', 'in': 'body'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `title` | `string` | title of the case |
| `description` | `string` | description of the case |
| `status_uuid` | `string` | identifier of case’s status |
| `priority` | `string` | priority of the case |
| `tags` | `array` | tags to associate to the case |
| `subscribers` | `array` | avatars to associate to the case |
| `community_uuid` | `string` | the identifier of the community to which the case is associated |
| `verdict_uuid` | `string` | Verdict of the case |
| `custom_status_uuid` | `string` | Custom status of the case |
| `custom_priority_uuid` | `string` | Custom priority of the case |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `short_id` | `string` |  |
| `created_at` | `string` |  |
| `created_by` | `string` |  |
| `created_by_type` | `string` |  |
| `updated_at` | `string` |  |
| `updated_by` | `string` |  |
| `updated_by_type` | `string` |  |
| `title` | `string` |  |
| `description` | `string` |  |
| `priority` | `` | low|medium|high |
| `status` | `string` |  |
| `status_uuid` | `string` |  |
| `community_uuid` | `string` |  |
| `subscribers` | `array` |  |
| `tags` | `array` | List of tags associated to the case |
| `number_of_comments` | `integer` |  |
| `first_seen_at` | `string` | Date and time of the first case event |
| `last_seen_at` | `string` | Date and time of the last case event |
| `manual` | `boolean` | if True, indicates that the case was created manually |
| `is_supplied` | `boolean` | if True, indicates that alerts can be automatically added to the case |
| `verdict_uuid` | `string` | UUID of the verdict associated to the case |
| `verdict` | `object` |  |
| `custom_status_uuid` | `string` | UUID of the custom status associated to the case |
| `custom_status` | `object` |  |
| `custom_priority_uuid` | `string` | UUID of the priority associated to the case |
| `custom_priority` | `object` |  |
| `number_of_alerts` | `integer` |  |
| `alerts` | `array` |  |

### Create rule

Create a new rule

**Configuration**

{'type': 'string', 'maxLength': 1000, 'in': 'body'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `community_uuid` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `description` | `string` |  |
| `payload` | `string` |  |
| `severity` | `integer` |  |
| `effort` | `integer` |  |
| `alert_type_uuid` | `string` |  |
| `tags` | `array` |  |
| `related_object_refs` | `array` |  |
| `datasources` | `array` |  |
| `event_fields` | `array` |  |
| `enabled` | `boolean` |  |
| `parameters` | `array` |  |
| `all_entities` | `boolean` |  |
| `entities` | `array` |  |
| `all_assets` | `boolean` |  |
| `assets` | `array` |  |
| `goal` | `string` |  |
| `false_positives` | `string` |  |
| `similarity_strategy` | `array` |  |
| `available_for_subcommunities` | `boolean` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the rule |
| `enabled` | `boolean` | Is the rule enabled ? |
| `community_uuid` | `string` | The community uuid if the rule is attached to one |
| `parameters` | `array` | The parameters of the rule |
| `all_entities` | `boolean` | Should the rule be applied on all entities ? |
| `entities` | `array` | The list of entities the rule should be applied on |
| `all_assets` | `boolean` | Should the rule be applied on all assets ? |
| `assets` | `array` | The list of assets identifiers the rule should be applied on |
| `last_compilation_success` | `boolean` | Did the last compilation succeed ? |
| `last_compilation_message` | `string` | The message of the last compilation |
| `last_compilation_at` | `string` | The last compilation date of the rule |
| `name` | `string` | The name of the rule |
| `type` | `` | The type of the rule |
| `private` | `boolean` | Is the rule available only for the community ? |
| `is_private` | `boolean` | Is the rule available only for the community ? |
| `description` | `string` | The descrition of the rule |
| `payload` | `string` | The payload of the rule |
| `severity` | `integer` | The severity of the rule |
| `effort` | `integer` | The effort of the rule |
| `alert_type` | `object` | The alert type associated to the rule |
| `alert_category` | `object` | The alert category associated to the rule |
| `tags` | `array` | The list of tags associated to the rule |
| `source` | `string` | The source of the rule |
| `verified` | `boolean` | Is the rule verified ? |
| `related_object_refs` | `array` | The list of reference of objects related to the rule |
| `datasources` | `array` | The list of datasources of the rule |
| `event_fields` | `array` | The list of fields to show when displaying a matched event |
| `similarity_strategy` | `array` | Similarity Strategy used by this rule |
| `created_at` | `string` | The creation date of the rule |
| `created_by` | `string` | The profile who created the rule |
| `created_by_type` | `string` | The profile type who created the rule can be 'avatar', 'application', 'apikey' |
| `updated_at` | `string` | The modification date of the rule |
| `updated_by` | `string` | The profile who updated the rule |
| `updated_by_type` | `string` | The profile type who updated the rule can be 'rule', 'application', 'apikey' |
| `goal` | `string` | A high-level description explaining the contribution of the rule |
| `false_positives` | `string` | A possible legitimate usage which can raise a false alert |
| `references` | `string` | Details on what led to write this rule |
| `available_for_subcommunities` | `boolean` | Is the rule available for subcommunities (if applicable) ? |
| `instance_uuid` | `string` | The identifier of the instance of the rule |

### Create Asset

Create a new asset

**Configuration**

{'type': 'string', 'in': 'body'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `asset_type` | `object` |  |
| `name` | `string` |  |
| `criticity` | `integer` |  |
| `description` | `string` |  |
| `attributes` | `array` |  |
| `keys` | `array` |  |
| `owners` | `array` |  |
| `community_uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `keys` | `array` |  |
| `attributes` | `array` |  |
| `uuid` | `string` |  |
| `name` | `string` |  |
| `created_at` | `string` |  |
| `criticity` | `object` |  |
| `asset_type` | `object` |  |
| `updated_at` | `string` |  |
| `description` | `string` |  |
| `owners` | `array` |  |
| `community_uuid` | `string` |  |
| `category` | `object` |  |

### Create Asset (V2)

Create a new asset

**Configuration**

{'default': '', 'in': 'body', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `` |  |
| `community_uuid` | `string` |  |
| `entity_uuid` | `` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `type` | `string` |  |
| `category` | `['string', 'null']` |  |
| `criticality` | `integer` |  |
| `props` | `['object', 'null']` | Attach contextual properties |
| `atoms` | `['object', 'null']` | Attach detection properties |
| `tags` | `array` |  |
| `reviewed` | `boolean` | Mark the asset as reviewed |
| `source` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the asset |
| `entity_uuid` | `` |  |
| `community_uuid` | `string` | The community of the asset |
| `name` | `string` | The name of the asset |
| `type` | `string` | The type of the asset |
| `category` | `['object', 'string', 'null']` | The category of the asset |
| `criticality` | `['integer', 'null']` |  |
| `created_at` | `` | The creation date of the asset |
| `created_by` | `` |  |
| `created_by_type` | `['string', 'null']` |  |
| `updated_at` | `` | The modification date of the asset |
| `first_seen` | `` |  |
| `last_seen` | `` |  |
| `nb_events` | `['integer', 'null']` |  |
| `nb_alerts` | `['integer', 'null']` |  |
| `nb_atoms` | `integer` |  |
| `atoms` | `['object', 'null']` |  |
| `props` | `['object', 'null']` |  |
| `tags` | `array` |  |
| `revoked` | `boolean` |  |
| `revoked_at` | `` |  |
| `revoked_by` | `` |  |
| `reviewed` | `boolean` |  |
| `reviewed_at` | `` |  |
| `reviewed_by` | `` |  |
| `source` | `string` |  |
| `rule_uuid` | `` |  |
| `rule_version` | `['string', 'null']` |  |
| `criticity` | `['object', 'null']` | The criticality of the asset |
| `asset_type` | `['object', 'null']` | The type of the asset |

### Delete Case

Delete a case

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `case_uuid` | `string` |  |

### Delete rule

Delete a rule

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `community_uuid` | `string` |  |

### Delete an asset

Delete the requested asset

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the asset |

### Delete an asset (V2)

Delete the requested asset

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the asset |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the asset |
| `entity_uuid` | `` |  |
| `community_uuid` | `string` | The community of the asset |
| `name` | `string` | The name of the asset |
| `type` | `string` | The type of the asset |
| `category` | `['object', 'string', 'null']` | The category of the asset |
| `criticality` | `['integer', 'null']` |  |
| `created_at` | `` | The creation date of the asset |
| `created_by` | `` |  |
| `created_by_type` | `['string', 'null']` |  |
| `updated_at` | `` | The modification date of the asset |
| `first_seen` | `` |  |
| `last_seen` | `` |  |
| `nb_events` | `['integer', 'null']` |  |
| `nb_alerts` | `['integer', 'null']` |  |
| `nb_atoms` | `integer` |  |
| `atoms` | `['object', 'null']` |  |
| `props` | `['object', 'null']` |  |
| `tags` | `array` |  |
| `revoked` | `boolean` |  |
| `revoked_at` | `` |  |
| `revoked_by` | `` |  |
| `reviewed` | `boolean` |  |
| `reviewed_at` | `` |  |
| `reviewed_by` | `` |  |
| `source` | `string` |  |
| `rule_uuid` | `` |  |
| `rule_version` | `['string', 'null']` |  |
| `criticity` | `['object', 'null']` | The criticality of the asset |
| `asset_type` | `['object', 'null']` | The type of the asset |

### Deny Countermeasure

Mark as denied a countermeasure

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `cm_uuid` | `string` |  |
| `comment` | `object` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `action_steps` | `array` |  |
| `activated_by_type` | `string` | Type of the profile that activated the countermeasure |
| `comments` | `array` |  |
| `activated_at` | `string` | Date the countermeasure was activated |
| `relevance` | `integer` | Relevance of the countermeasure |
| `denied_by_type` | `string` | Type of the profile that denied the countermeasure |
| `status` | `string` | (deprecated) Status of the countermeasure |
| `created_by` | `string` | UUID of profile that created the countermeasure |
| `model_uuid` | `string` | UUID of the model from which this countermeasure has been created |
| `activated_by` | `string` | UUID of profile that activated the countermeasure |
| `description` | `string` | Description of the countermeasure |
| `name` | `string` | Name of the countermeasure |
| `uuid` | `string` | UUID of the countermeasure |
| `duration` | `string` | Estimated duration to apply the countermeasures |
| `alert_uuid` | `string` | UUID of the alert related to the countermeasure |
| `denied_at` | `string` | Date the countermeasure was denied |
| `created_by_type` | `string` | Type of the profile that created the countermeasure |
| `course_of_action` | `object` | (deprecated) STIX2 object course of action |
| `dynamic_relevance` | `integer` | Dynamic relevance of the countermeasure |
| `denied_by` | `string` | UUID of profile that denied the countermeasure |
| `assignee` | `string` | UUID of the profile assigned to the progress of the countermeasure |
| `created_at` | `string` | Date the countermeasure was created |

### Disable rule

Disable a rule

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `community_uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the rule |
| `enabled` | `boolean` | Is the rule enabled ? |
| `community_uuid` | `string` | The community uuid if the rule is attached to one |
| `parameters` | `array` | The parameters of the rule |
| `all_entities` | `boolean` | Should the rule be applied on all entities ? |
| `entities` | `array` | The list of entities the rule should be applied on |
| `all_assets` | `boolean` | Should the rule be applied on all assets ? |
| `assets` | `array` | The list of assets identifiers the rule should be applied on |
| `last_compilation_success` | `boolean` | Did the last compilation succeed ? |
| `last_compilation_message` | `string` | The message of the last compilation |
| `last_compilation_at` | `string` | The last compilation date of the rule |
| `name` | `string` | The name of the rule |
| `type` | `` | The type of the rule |
| `private` | `boolean` | Is the rule available only for the community ? |
| `is_private` | `boolean` | Is the rule available only for the community ? |
| `description` | `string` | The descrition of the rule |
| `payload` | `string` | The payload of the rule |
| `severity` | `integer` | The severity of the rule |
| `effort` | `integer` | The effort of the rule |
| `alert_type` | `object` | The alert type associated to the rule |
| `alert_category` | `object` | The alert category associated to the rule |
| `tags` | `array` | The list of tags associated to the rule |
| `source` | `string` | The source of the rule |
| `verified` | `boolean` | Is the rule verified ? |
| `related_object_refs` | `array` | The list of reference of objects related to the rule |
| `datasources` | `array` | The list of datasources of the rule |
| `event_fields` | `array` | The list of fields to show when displaying a matched event |
| `similarity_strategy` | `array` | Similarity Strategy used by this rule |
| `created_at` | `string` | The creation date of the rule |
| `created_by` | `string` | The profile who created the rule |
| `created_by_type` | `string` | The profile type who created the rule can be 'avatar', 'application', 'apikey' |
| `updated_at` | `string` | The modification date of the rule |
| `updated_by` | `string` | The profile who updated the rule |
| `updated_by_type` | `string` | The profile type who updated the rule can be 'rule', 'application', 'apikey' |
| `goal` | `string` | A high-level description explaining the contribution of the rule |
| `false_positives` | `string` | A possible legitimate usage which can raise a false alert |
| `references` | `string` | Details on what led to write this rule |
| `available_for_subcommunities` | `boolean` | Is the rule available for subcommunities (if applicable) ? |
| `instance_uuid` | `string` | The identifier of the instance of the rule |

### Enable rule

Enable a rule

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `community_uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the rule |
| `enabled` | `boolean` | Is the rule enabled ? |
| `community_uuid` | `string` | The community uuid if the rule is attached to one |
| `parameters` | `array` | The parameters of the rule |
| `all_entities` | `boolean` | Should the rule be applied on all entities ? |
| `entities` | `array` | The list of entities the rule should be applied on |
| `all_assets` | `boolean` | Should the rule be applied on all assets ? |
| `assets` | `array` | The list of assets identifiers the rule should be applied on |
| `last_compilation_success` | `boolean` | Did the last compilation succeed ? |
| `last_compilation_message` | `string` | The message of the last compilation |
| `last_compilation_at` | `string` | The last compilation date of the rule |
| `name` | `string` | The name of the rule |
| `type` | `` | The type of the rule |
| `private` | `boolean` | Is the rule available only for the community ? |
| `is_private` | `boolean` | Is the rule available only for the community ? |
| `description` | `string` | The descrition of the rule |
| `payload` | `string` | The payload of the rule |
| `severity` | `integer` | The severity of the rule |
| `effort` | `integer` | The effort of the rule |
| `alert_type` | `object` | The alert type associated to the rule |
| `alert_category` | `object` | The alert category associated to the rule |
| `tags` | `array` | The list of tags associated to the rule |
| `source` | `string` | The source of the rule |
| `verified` | `boolean` | Is the rule verified ? |
| `related_object_refs` | `array` | The list of reference of objects related to the rule |
| `datasources` | `array` | The list of datasources of the rule |
| `event_fields` | `array` | The list of fields to show when displaying a matched event |
| `similarity_strategy` | `array` | Similarity Strategy used by this rule |
| `created_at` | `string` | The creation date of the rule |
| `created_by` | `string` | The profile who created the rule |
| `created_by_type` | `string` | The profile type who created the rule can be 'avatar', 'application', 'apikey' |
| `updated_at` | `string` | The modification date of the rule |
| `updated_by` | `string` | The profile who updated the rule |
| `updated_by_type` | `string` | The profile type who updated the rule can be 'rule', 'application', 'apikey' |
| `goal` | `string` | A high-level description explaining the contribution of the rule |
| `false_positives` | `string` | A possible legitimate usage which can raise a false alert |
| `references` | `string` | Details on what led to write this rule |
| `available_for_subcommunities` | `boolean` | Is the rule available for subcommunities (if applicable) ? |
| `instance_uuid` | `string` | The identifier of the instance of the rule |

### Get aggregation query

Make an aggregation query

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `aggregation_type` | `string` | The aggregation type. Can be `avg`, `cardinality`, `max`, `min`, `sum` or `count`. |
| `aggregation_field` | `string` | The field on which apply the aggregation. Should be null only for `count` aggregation. |
| `query_term` | `string` |  |
| `earliest_time` | `string` |  |
| `latest_time` | `string` |  |
| `minutes_per_bucket` | `integer` |  |
| `filters` | `array` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `aggregations` | `array` |  |
| `anomaly_detection_candidate_score_y_acf1` | `number` |  |
| `anomaly_detection_candidate_score_y_acf5` | `number` |  |
| `anomaly_detection_candidate_score_seas_acf1` | `number` |  |
| `anomaly_detection_candidate` | `boolean` |  |

### Get Alert

Retrieve the definition of an alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `stix` | `boolean` |  |
| `cases` | `boolean` | Get the cases associated with this alert |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `urgency` | `object` |  |
| `history` | `array` |  |
| `is_incident` | `boolean` |  |
| `assets` | `array` |  |
| `countermeasures` | `array` |  |
| `updated_at` | `integer` |  |
| `comments` | `array` |  |
| `ttps` | `array` |  |
| `number_of_unseen_comments` | `integer` |  |
| `status` | `object` |  |
| `created_by` | `string` |  |
| `updated_by` | `string` |  |
| `source` | `string` |  |
| `community_uuid` | `string` |  |
| `number_of_total_comments` | `integer` |  |
| `uuid` | `string` |  |
| `rule` | `object` |  |
| `adversaries` | `array` |  |
| `short_id` | `string` |  |
| `first_seen_at` | `string` |  |
| `last_seen_at` | `string` |  |
| `event_uuids` | `array` |  |
| `kill_chain_short_id` | `string` |  |
| `similar` | `integer` |  |
| `alert_type` | `object` |  |
| `details` | `string` |  |
| `stix` | `object` |  |
| `created_by_type` | `string` |  |
| `entity` | `object` |  |
| `created_at` | `integer` |  |
| `updated_by_type` | `string` |  |
| `title` | `string` |  |
| `target` | `string` |  |
| `cases` | `array` |  |

### Get case

Retrieve the properties of a case

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | UUID of the case |
| `community_uuid` | `string` | (Optional) Identifier of the community |
| `render` | `boolean` | (Optional) Render boolean |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `short_id` | `string` |  |
| `created_at` | `string` |  |
| `created_by` | `string` |  |
| `created_by_type` | `string` |  |
| `updated_at` | `string` |  |
| `updated_by` | `string` |  |
| `updated_by_type` | `string` |  |
| `title` | `string` |  |
| `description` | `string` |  |
| `priority` | `` | low|medium|high |
| `status` | `string` |  |
| `status_uuid` | `string` |  |
| `community_uuid` | `string` |  |
| `subscribers` | `array` |  |
| `tags` | `array` | List of tags associated to the case |
| `number_of_comments` | `integer` |  |
| `first_seen_at` | `string` | Date and time of the first case event |
| `last_seen_at` | `string` | Date and time of the last case event |
| `manual` | `boolean` | if True, indicates that the case was created manually |
| `is_supplied` | `boolean` | if True, indicates that alerts can be automatically added to the case |
| `verdict_uuid` | `string` | UUID of the verdict associated to the case |
| `verdict` | `object` |  |
| `custom_status_uuid` | `string` | UUID of the custom status associated to the case |
| `custom_status` | `object` |  |
| `custom_priority_uuid` | `string` | UUID of the priority associated to the case |
| `custom_priority` | `object` |  |
| `number_of_alerts` | `integer` |  |
| `alerts` | `array` |  |

### Get Community

Retrieve a community

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The UUID of the community |
| `name` | `string` | The name of the community |
| `description` | `string` | The description of the community |
| `homepage_url` | `string` | URL of the community's homepage |
| `created_at` | `string` | The date and time the community was created |
| `created_by` | `string` | The user who created the community |
| `created_by_type` | `string` | The type of user who created the community |
| `updated_at` | `string` | The date and time the community was last updated |
| `is_parent` | `boolean` | Whether the community is a multi-tenant community |
| `parent_community_uuid` | `string` | The UUID of the parent community (if any) |
| `subcommunities` | `array` | List of UUIDs of communities that are managed by this multi-tenant community |
| `is_mfa_enforced` | `boolean` | Whether the community has enforced multi-factor authentication |
| `session_timeout` | `number` | The session timeout in minutes for the community (if any) |
| `disable_inactive_avatars` | `boolean` | Whether the community automatically disables inactive avatars (after 90 days) |
| `disabled` | `boolean` | Whether the community is disabled |

### Get context

Get reports from a specific term

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sort` | `string` |  |
| `term` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `items` | `array` |  |
| `has_more` | `boolean` |  |

### Get custom priority

Get a single custom priority based on its UUID

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `priority_uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `community_uuid` | `string` |  |
| `level` | `integer` |  |
| `created_at` | `string` |  |
| `created_by` | `string` |  |
| `created_by_type` | `string` |  |
| `updated_at` | `string` |  |
| `updated_by` | `string` |  |
| `updated_by_type` | `string` |  |
| `color` | `string` |  |
| `label` | `string` |  |
| `description` | `string` |  |
| `is_used` | `boolean` |  |

### Get custom status

Get a single custom status based on its UUID

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status_uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `community_uuid` | `string` |  |
| `level` | `integer` |  |
| `created_at` | `string` |  |
| `created_by` | `string` |  |
| `created_by_type` | `string` |  |
| `updated_at` | `string` |  |
| `updated_by` | `string` |  |
| `updated_by_type` | `string` |  |
| `stage` | `string` |  |
| `label` | `string` |  |
| `description` | `string` |  |
| `is_used` | `boolean` |  |

### Get custom verdict

Get a single custom verdict based on its UUID

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `verdict_uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `community_uuid` | `string` |  |
| `level` | `integer` |  |
| `created_at` | `string` |  |
| `created_by` | `string` |  |
| `created_by_type` | `string` |  |
| `updated_at` | `string` |  |
| `updated_by` | `string` |  |
| `updated_by_type` | `string` |  |
| `stage` | `string` |  |
| `label` | `string` |  |
| `description` | `string` |  |
| `is_used` | `boolean` |  |

### Get Entity

Retrieve an entity

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The UUID of the entity |
| `name` | `string` | The name of the entity |
| `entity_id` | `string` | The chosen ID of the entity |
| `community_uuid` | `string` | The UUID of the community the entity belongs to |
| `description` | `string` | The description of the entity |
| `alerts_generation` | `string` | Whether alerts generated for this entity require analyst approval |
| `number_of_intakes` | `number` | The number of configured intakes for this entity |

### Get Event Field Common Values

Get the most common values of fields observed under a specific query

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | Event search query |
| `earliest_time` | `string` | The earliest time of the time range of the search |
| `latest_time` | `string` | The latest time of the time range of the search |
| `fields` | `string` | Fields to compute the most common values (use a coma between fields) |
| `limit` | `number` | Maximum number of events to retrieve |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `fields` | `array` |  |

### Get Events

Query events

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | Event search query |
| `earliest_time` | `string` | The earliest time of the time range of the search |
| `latest_time` | `string` | The latest time of the time range of the search |
| `limit` | `number` | Maximum number of events to retrieve |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `events` | `array` |  |

### Get Intake

Retrieve an intake

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The UUID of the intake |
| `name` | `string` | The name of the intake |
| `community_uuid` | `string` | The UUID of the community the intake belongs to |
| `format_uuid` | `string` | The UUID of the format of the intake |
| `intake_key` | `string` | The key to use to send events to the intake |
| `created_at` | `string` | The date and time the intake was created |
| `created_by` | `string` | The user who created the intake |
| `created_by_type` | `string` | The type of user who created the intake |
| `updated_at` | `string` | The date and time the intake was last updated |
| `updated_by` | `string` | The user who last updated the intake |
| `updated_by_type` | `string` | The type of user who last updated the intake |
| `is_custom_format` | `boolean` | Whether the format is custom (not maintained by Sekoia) |
| `connector_configuration_uuid` | `string` | The UUID of the connector configuration, for pulling intakes |
| `status` | `string` | A string representation of the status of the intake (mainly for pulling intakes) |
| `entity` | `` |  |

### Get rule

Get a rule

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the rule |
| `enabled` | `boolean` | Is the rule enabled ? |
| `community_uuid` | `string` | The community uuid if the rule is attached to one |
| `parameters` | `array` | The parameters of the rule |
| `all_entities` | `boolean` | Should the rule be applied on all entities ? |
| `entities` | `array` | The list of entities the rule should be applied on |
| `all_assets` | `boolean` | Should the rule be applied on all assets ? |
| `assets` | `array` | The list of assets identifiers the rule should be applied on |
| `last_compilation_success` | `boolean` | Did the last compilation succeed ? |
| `last_compilation_message` | `string` | The message of the last compilation |
| `last_compilation_at` | `string` | The last compilation date of the rule |
| `name` | `string` | The name of the rule |
| `type` | `` | The type of the rule |
| `private` | `boolean` | Is the rule available only for the community ? |
| `is_private` | `boolean` | Is the rule available only for the community ? |
| `description` | `string` | The descrition of the rule |
| `payload` | `string` | The payload of the rule |
| `severity` | `integer` | The severity of the rule |
| `effort` | `integer` | The effort of the rule |
| `alert_type` | `object` | The alert type associated to the rule |
| `alert_category` | `object` | The alert category associated to the rule |
| `tags` | `array` | The list of tags associated to the rule |
| `source` | `string` | The source of the rule |
| `verified` | `boolean` | Is the rule verified ? |
| `related_object_refs` | `array` | The list of reference of objects related to the rule |
| `datasources` | `array` | The list of datasources of the rule |
| `event_fields` | `array` | The list of fields to show when displaying a matched event |
| `similarity_strategy` | `array` | Similarity Strategy used by this rule |
| `created_at` | `string` | The creation date of the rule |
| `created_by` | `string` | The profile who created the rule |
| `created_by_type` | `string` | The profile type who created the rule can be 'avatar', 'application', 'apikey' |
| `updated_at` | `string` | The modification date of the rule |
| `updated_by` | `string` | The profile who updated the rule |
| `updated_by_type` | `string` | The profile type who updated the rule can be 'rule', 'application', 'apikey' |
| `goal` | `string` | A high-level description explaining the contribution of the rule |
| `false_positives` | `string` | A possible legitimate usage which can raise a false alert |
| `references` | `string` | Details on what led to write this rule |
| `available_for_subcommunities` | `boolean` | Is the rule available for subcommunities (if applicable) ? |
| `instance_uuid` | `string` | The identifier of the instance of the rule |

### Create Content Proposal

Create Content Proposal

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle` | `object` | STIX Bundle to upload |
| `bundle_path` | `string` | Path of the STIX Bundle to upload |
| `auto_merge` | `boolean` | Whether or not the uploaded bundle can automatically be merged to the consolidated database |
| `enrich` | `boolean` | Whether or not the uploaded bundle should be enriched |
| `name` | `string` | Name to use for the new content proposal |
| `assigned_to` | `string` | Avatar assigned to the content proposal |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_name` | `string` |  |
| `content_proposal_id` | `string` |  |

### Upload Observables

Upload observables to inthreat

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `observables` | `array` | List of observables or bundle to upload to inThreat |
| `observables_path` | `string` | Path of the observables file to upload inThreat |

### Search Alerts

find alerts that match your filters

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `match[community_uuid]` | `string` |  |
| `match[entity_name]` | `string` |  |
| `match[entity_uuid]` | `string` |  |
| `match[status_uuid]` | `string` |  |
| `match[status_name]` | `string` |  |
| `match[type_category]` | `string` |  |
| `match[type_value]` | `string` |  |
| `match[source]` | `string` |  |
| `match[target]` | `string` |  |
| `match[node]` | `string` |  |
| `match[stix_object]` | `string` |  |
| `match[rule_uuid]` | `string` |  |
| `match[rule_name]` | `string` |  |
| `match[short_id]` | `string` |  |
| `match[uuid]` | `string` |  |
| `match[title]` | `string` |  |
| `date[created_at]` | `string` |  |
| `date[updated_at]` | `string` |  |
| `range[urgency]` | `string` |  |
| `range[similar]` | `string` |  |
| `visible` | `boolean` |  |
| `limit` | `integer` |  |
| `offset` | `integer` |  |
| `stix` | `boolean` |  |
| `sort` | `string` |  |
| `direction` | `string` |  |
| `with_count` | `boolean` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `total` | `integer` |  |
| `has_more` | `boolean` |  |
| `items` | `array` |  |

### List Assets

Return a list of assets according to the filters

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `limit` | `integer` | The number of assets to return |
| `offset` | `integer` | The position of the first asset to return |
| `match[uuid]` | `string` | Filter assets according to their identifier |
| `match[name]` | `string` | Filter assets according to their name |
| `match[category_name]` | `string` | Filter assets according to their category |
| `match[category_uuid]` | `string` | Filter assets according to their category |
| `match[type_name]` | `string` | Filter assets according to their type |
| `match[type_uuid]` | `string` | Filter assets according to their type |
| `range[criticality]` | `string` | Filter assets according to their criticality |
| `date[created_at]` | `string` | Filter assets according to their creation date |
| `date[updated_at]` | `string` | Filter assets according to their modification date |
| `sort` | `string` | The field to use to sort the list |
| `direction` | `string` | The direction to sort the list |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `items` | `array` |  |
| `total` | `integer` |  |

### List Assets (V2)

Return a list of assets according to the filters

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `search` | `['string', 'null']` | Search assets by name |
| `uuids` | `['string', 'null']` | Filter by comma-separated list of asset UUIDs |
| `community_uuids` | `['string', 'null']` | Filter by comma-separated list of community UUIDs |
| `type` | `['string', 'null']` | Filter by comma-separated list of asset types |
| `category` | `['string', 'null']` | Filter by comma-separated list of asset categories |
| `source` | `['string', 'null']` | Filter by comma-separated list of asset sources |
| `reviewed` | `['boolean', 'null']` | Filter reviewed assets only |
| `criticality` | `['integer', 'null']` | Filter assets with higher criticality |
| `sort` | `` | Sort criterion |
| `direction` | `` | Sort order |
| `rule_uuid` | `['string', 'null']` | Rule Uuid |
| `rule_version` | `['string', 'null']` | Rule Version |
| `offset` | `integer` | The position of the first asset to return |
| `limit` | `integer` | The number of assets to return |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `items` | `array` |  |
| `total` | `integer` |  |

### Edit Alert

Edit the details of an alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `alert_type_category` | `string` | Category of the alert type |
| `alert_type_value` | `string` | Name of the alert type, required if `alert_type_category` is present |
| `details` | `string` | Description of the alert |
| `urgency` | `integer` | The urgency of the alert |
| `kill_chain_short_id` | `string` | The ID of the kill chain step this alert denotes |
| `title` | `string` | Title of the alert |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `urgency` | `object` |  |
| `is_incident` | `boolean` |  |
| `assets` | `array` |  |
| `updated_at` | `integer` |  |
| `ttps` | `array` |  |
| `number_of_unseen_comments` | `integer` |  |
| `status` | `object` |  |
| `created_by` | `string` |  |
| `updated_by` | `string` |  |
| `source` | `string` |  |
| `community_uuid` | `string` |  |
| `number_of_total_comments` | `integer` |  |
| `uuid` | `string` |  |
| `rule` | `object` |  |
| `adversaries` | `array` |  |
| `short_id` | `string` |  |
| `first_seen_at` | `string` |  |
| `last_seen_at` | `string` |  |
| `event_uuids` | `array` |  |
| `kill_chain_short_id` | `string` |  |
| `similar` | `integer` |  |
| `alert_type` | `object` |  |
| `details` | `string` |  |
| `stix` | `object` |  |
| `created_by_type` | `string` |  |
| `entity` | `object` |  |
| `created_at` | `integer` |  |
| `updated_by_type` | `string` |  |
| `title` | `string` |  |
| `target` | `string` |  |

### Comment case

Add a new comment to a case

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | UUID of the case |
| `content` | `string` | Content of the comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `content` | `string` |  |
| `created_at` | `string` |  |
| `created_by` | `string` |  |
| `created_by_type` | `string` |  |
| `updated_at` | `string` |  |

### Comment Alert

Attach a new comment on an Alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `content` | `string` | Content of the comment |
| `author` | `string` | Author of the comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `created_by` | `string` | The identifier of the creator of the comment |
| `content` | `string` | Content of the comment |
| `author` | `string` | Author of the comment |
| `unseen` | `boolean` |  |
| `date` | `integer` |  |
| `created_by_type` | `string` | The type of the creator of the comment |
| `uuid` | `string` | Identifier of the comment |

### Create Content Proposal from PDF

Creates a content proposal with the content extracted from the specified PDF

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` |  |
| `file` | `string` |  |
| `source_ref` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `object` |  |

### Create Content Proposal from URL

Creates a content proposal with the content extracted from the specified URL

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` |  |
| `source_ref` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `object` |  |

### Predict Alert State

Predict the state of an alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert` | `object` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `worth_human_attention` | `boolean` |  |

### Push Events to Intake



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `intake_key` | `string` | Intake Key |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `event` | `object` | Event to push on Intake |
| `event_path` | `string` | File path to the event to push on Intake |
| `events` | `array` | Events to push on Intake |
| `events_path` | `string` | File path to the events to push on Intake |
| `keep_file_after_push` | `boolean` | If set and if the events are supplied through a file, this option keeps the file after the events were sent to the intake |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `event_ids` | `array` |  |

### Remove event from case

Remove an event from a case

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `case_uuid` | `string` |  |
| `event_id` | `string` |  |

### Get CTI Report

Retrieve the details of a report

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `string` |  |

### Get Asset

Return an asset according its identifier

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the asset |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `keys` | `array` | The keys of the asset |
| `attributes` | `array` | The attributes of the asset |
| `uuid` | `string` |  |
| `name` | `string` |  |
| `created_at` | `string` |  |
| `criticity` | `object` | The criticality associated with the asset |
| `asset_type` | `object` |  |
| `updated_at` | `string` |  |
| `description` | `string` |  |
| `owners` | `array` |  |
| `community_uuid` | `string` |  |
| `category` | `object` |  |

### Get Asset (V2)

Return an asset according to its identifier

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the asset |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the asset |
| `entity_uuid` | `` |  |
| `community_uuid` | `string` | The community of the asset |
| `name` | `string` | The name of the asset |
| `type` | `string` | The type of the asset |
| `category` | `['object', 'string', 'null']` | The category of the asset |
| `criticality` | `['integer', 'null']` |  |
| `created_at` | `` | The creation date of the asset |
| `created_by` | `` |  |
| `created_by_type` | `['string', 'null']` |  |
| `updated_at` | `` | The modification date of the asset |
| `first_seen` | `` |  |
| `last_seen` | `` |  |
| `nb_events` | `['integer', 'null']` |  |
| `nb_alerts` | `['integer', 'null']` |  |
| `nb_atoms` | `integer` |  |
| `atoms` | `['object', 'null']` |  |
| `props` | `['object', 'null']` |  |
| `tags` | `array` |  |
| `revoked` | `boolean` |  |
| `revoked_at` | `` |  |
| `revoked_by` | `` |  |
| `reviewed` | `boolean` |  |
| `reviewed_at` | `` |  |
| `reviewed_by` | `` |  |
| `source` | `string` |  |
| `rule_uuid` | `` |  |
| `rule_version` | `['string', 'null']` |  |
| `criticity` | `['object', 'null']` | The criticality of the asset |
| `asset_type` | `['object', 'null']` | The type of the asset |

### Synchronize Assets with AD

Create, merge and edit asset to synchronize asset with ad

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `community_uuid` | `string` |  |
| `user_ad_data` | `object` |  |
| `user_ad_data_path` | `object` | File name to the User AD file to read. |
| `asset_synchronization_configuration` | `object` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `array` |  |

### Update Alert Status

Triggers an action on an alert to update its status

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `action_uuid` | `string` | UUID of the action to trigger |
| `comment` | `string` | a comment to describe why the alert status has changed |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `actions` | `array` |  |

### Update Alert Status by name

Triggers an action on an alert to update its status by name

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The UUID of the alert to update |
| `status` | `string` | Name of the status to update the alert to |
| `comment` | `string` | A comment to describe why the alert status has changed |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `actions` | `array` |  |

### Edit case

Edit the properties of a case

**Configuration**

{'description': 'description of the case', 'type': 'string', 'in': 'body'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | UUID of the case |
| `title` | `string` | title of the case |
| `description` | `string` | description of the case |
| `status_uuid` | `string` | identifier of case’s status |
| `priority` | `string` | priority of the case |
| `tags` | `array` | tags to associate to the case |
| `subscribers` | `array` | avatars to associate to the case |
| `verdict_uuid` | `string` | Verdict of the case |
| `custom_status_uuid` | `string` | Custom status of the case |
| `custom_priority_uuid` | `string` | Custom priority of the case |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `short_id` | `string` |  |
| `created_at` | `string` |  |
| `created_by` | `string` |  |
| `created_by_type` | `string` |  |
| `updated_at` | `string` |  |
| `updated_by` | `string` |  |
| `updated_by_type` | `string` |  |
| `title` | `string` |  |
| `description` | `string` |  |
| `priority` | `` | low|medium|high |
| `status` | `string` |  |
| `status_uuid` | `string` |  |
| `community_uuid` | `string` |  |
| `subscribers` | `array` |  |
| `tags` | `array` | List of tags associated to the case |
| `number_of_comments` | `integer` |  |
| `first_seen_at` | `string` | Date and time of the first case event |
| `last_seen_at` | `string` | Date and time of the last case event |
| `manual` | `boolean` | if True, indicates that the case was created manually |
| `is_supplied` | `boolean` | if True, indicates that alerts can be automatically added to the case |
| `verdict_uuid` | `string` | UUID of the verdict associated to the case |
| `verdict` | `object` |  |
| `custom_status_uuid` | `string` | UUID of the custom status associated to the case |
| `custom_status` | `object` |  |
| `custom_priority_uuid` | `string` | UUID of the priority associated to the case |
| `custom_priority` | `object` |  |
| `number_of_alerts` | `integer` |  |
| `alerts` | `array` |  |

### Update rule

Update a rule

**Configuration**

{'in': 'body', 'type': 'string', 'maxLength': 1000}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` |  |
| `community_uuid` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `description` | `string` |  |
| `payload` | `string` |  |
| `severity` | `integer` |  |
| `effort` | `integer` |  |
| `alert_type_uuid` | `string` |  |
| `tags` | `array` |  |
| `related_object_refs` | `array` |  |
| `datasources` | `array` |  |
| `event_fields` | `array` |  |
| `enabled` | `boolean` |  |
| `parameters` | `array` |  |
| `all_entities` | `boolean` |  |
| `entities` | `array` |  |
| `all_assets` | `boolean` |  |
| `assets` | `array` |  |
| `goal` | `string` |  |
| `false_positives` | `string` |  |
| `similarity_strategy` | `array` |  |
| `available_for_subcommunities` | `boolean` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the rule |
| `enabled` | `boolean` | Is the rule enabled ? |
| `community_uuid` | `string` | The community uuid if the rule is attached to one |
| `parameters` | `array` | The parameters of the rule |
| `all_entities` | `boolean` | Should the rule be applied on all entities ? |
| `entities` | `array` | The list of entities the rule should be applied on |
| `all_assets` | `boolean` | Should the rule be applied on all assets ? |
| `assets` | `array` | The list of assets identifiers the rule should be applied on |
| `last_compilation_success` | `boolean` | Did the last compilation succeed ? |
| `last_compilation_message` | `string` | The message of the last compilation |
| `last_compilation_at` | `string` | The last compilation date of the rule |
| `name` | `string` | The name of the rule |
| `type` | `` | The type of the rule |
| `private` | `boolean` | Is the rule available only for the community ? |
| `is_private` | `boolean` | Is the rule available only for the community ? |
| `description` | `string` | The descrition of the rule |
| `payload` | `string` | The payload of the rule |
| `severity` | `integer` | The severity of the rule |
| `effort` | `integer` | The effort of the rule |
| `alert_type` | `object` | The alert type associated to the rule |
| `alert_category` | `object` | The alert category associated to the rule |
| `tags` | `array` | The list of tags associated to the rule |
| `source` | `string` | The source of the rule |
| `verified` | `boolean` | Is the rule verified ? |
| `related_object_refs` | `array` | The list of reference of objects related to the rule |
| `datasources` | `array` | The list of datasources of the rule |
| `event_fields` | `array` | The list of fields to show when displaying a matched event |
| `similarity_strategy` | `array` | Similarity Strategy used by this rule |
| `created_at` | `string` | The creation date of the rule |
| `created_by` | `string` | The profile who created the rule |
| `created_by_type` | `string` | The profile type who created the rule can be 'avatar', 'application', 'apikey' |
| `updated_at` | `string` | The modification date of the rule |
| `updated_by` | `string` | The profile who updated the rule |
| `updated_by_type` | `string` | The profile type who updated the rule can be 'rule', 'application', 'apikey' |
| `goal` | `string` | A high-level description explaining the contribution of the rule |
| `false_positives` | `string` | A possible legitimate usage which can raise a false alert |
| `references` | `string` | Details on what led to write this rule |
| `available_for_subcommunities` | `boolean` | Is the rule available for subcommunities (if applicable) ? |
| `instance_uuid` | `string` | The identifier of the instance of the rule |


## Extra

Module **`Sekoia.io` v2.67.13**