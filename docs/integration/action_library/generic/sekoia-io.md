# Sekoia.io

![Sekoia.io](/assets/playbooks/library/sekoia-io.svg){ align=right width=150 }

Sekoia.io

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | Sekoia.io API key |
| `base_url` | `string` | Sekoia.io base URL (ex. https://api.sekoia.io) |

## Triggers

### Alert Comment Created

A comment was added to an existing Alert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rule_filter` | `string` | Create a run only for alerts matching a rule name |


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


### Alert Created

A new Alert was created in the Operation Center

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rule_filter` | `string` | Create a run only for alerts matching a rule name |


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


### Feed Consumption

Get all non-revoked objects from Sekoia.io Intelligence feed

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `feed_id` | `string` | ID of the Sekoia.io feed to get data from |
| `batch_size_limit` | `integer` | Size of the batch of elements to get from the Sekoia.io feed in one time |


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

### Create Asset

Create a new asset

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

### Delete an asset

Delete the requested asset

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | The identifier of the asset |

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

### Get context

Get reports from a specific term

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sort` | `string` |  |
| `term` | `string` |  |

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


## Extra

Module **`Sekoia.io` v2.58.2**