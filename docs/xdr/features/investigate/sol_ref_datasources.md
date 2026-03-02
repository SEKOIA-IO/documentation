# Reference: Datasources

`SOL` provides seamless access to all critical security data within Sekoia SOC platform:

| Data Source | Description | Use Cases |
|-------------|-------------|-----------|
| `events` | Security events | Threat hunting, incident investigation, SOC reporting. You will receive events that are retained for the duration of your hot storage |
| `event_telemetry` | Telemetry on events | Analytics on your ingestion pipelines |
| `eternal_events` | Security events related to alerts or cases | Extract metrics from events related to alerts/cases. Access events related to an alert that are beyond your hot storage retention period |
| `alerts` | Security alerts and detections | SOC monitoring, alert pattern analysis |
| `cases` | Security incidents and cases | Case management, incident correlation |
| `custom_statuses` | Alerts and cases custom statuses | Reporting |
| `custom_priorities` | Cases custom priorities | Reporting |
| `communities` | Communities (for multi-tenant only) | Multi-tenant reporting |
| `intakes` | Data sources | Data source management, volume monitoring |
| `entities` | Company entities | Entity tracking, detailed reporting |
| `assets` | Known Assets | Asset Investigations |
| `asset_properties` | Listing known properties related to the Asset | Asset Investigations |
| `asset_partitions` | Partitions on a per Asset basis and Hygiene related to these | Understand and improve Hygiene state Note: Part of the Reveal plan |
| `asset_accounts` | Listing local users accounts related to the Asset | Impact analysis and incident correlation Note: Part of the Reveal plan |

## Alerts properties

| **Alert Property**        | **Description**                                                                              |
|---------------------------|----------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the alert.                                                           |
| short_ID                  | A concise identifier for quick reference to the alert.                                       |
| community_uuid            | A unique identifier for the community the alert belongs to.                                  |
| entity_uuid               | A unique identifier representing the entity associated with the alert.                       |
| entity_name               | The name of the entity linked to the alert.                                                  |
| rule_name                 | The name assigned to the rule that triggered the alert.                                      |
| rule_pattern              | The detection pattern of the alert.                                                          |
| detection_type            | The method by which the alert was detected.                                                  |
| alert_type_category       | The category of the alert.                                                                   |
| alert_type_value          | The type of the alert.                                                                       |
| status                    | The current state of the alert (e.g., open, acknowledged, resolved).                         |
| urgency                   | The level of urgency assigned to the alert.                                                  |
| created_at                | The date and time when the alert was initially created.                                      |
| update_at                 | The date and time when the alert was last updated.                                           |
| first_seen_at             | The date and time of the first alert occurrence.                                             |
| last_seen_at              | The date and time of the last alert occurrence.                                              |
| time_to_detect            | Duration taken to identify the alert from its occurrence in seconds.                         |
| time_to_acknowledge       | Time elapsed from detection to official acknowledgment of the alert in seconds.              |
| time_to_respond           | Duration taken to take action after acknowledgment in seconds.                               |
| time_to_resolve           | The total time taken to completely resolve the alert in seconds.                             |
| time_to_ingest            | The duration from alert generation to its final ingestion into the system in seconds.        |
| occurrences               | The number of alert occurrences                                                              |
| rule_instance_uuid        | A unique identifier for the rule that generated the alert.                                   |
| cases                     | List of cases associated to the alert.                                                       |
| assets                    | List of assets associated to the alert.                                                      |
| threats                   | List of threats associated the alert.                                                        |

## Cases properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the case.                                                          |
| short_id                  | A concise identifier for quick reference to the case.                                      |
| community_uuid            | A unique identifier for the community related to the case.                                 |
| title                     | The title or subject line of the case.                                                     |
| description               | A detailed description outlining the case's context or issues.                             |
| priority                  | The importance level assigned to the case, indicating its urgency.                         |
| created_at                | The date and time when the case was created.                                               |
| created_by                | The user or system that created the case.                                                  |
| created_by_type           | The type of entity that created the case (e.g., user, automated system).                   |
| updated_at                | The date and time when the case was last updated.                                          |
| updated_by                | The user or system that last updated the case.                                             |
| updated_by_type           | The type of user that last updated the case.                                               |
| first_seen_at             | The date and time when the case was first detected.                                        |
| last_seen_at              | The date and time when the case was last observed or updated.                              |

## Custom statuses

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the custom status.                                                 |
| community_uuid            | A unique identifier for the community related to the custom status.                        |
| level                     | The numeric level of the status.                                                           |
| created_at                | The date and time when the custom status was created.                                      |
| created_by                | The user or system that created the custom status.                                         |
| created_by_type           | The type of entity that created the custom status (e.g., avatar, apikey).                  |
| updated_at                | The date and time when the custom status was last updated.                                 |
| updated_by                | The user or system that last updated the custom status.                                    |
| updated_by_type           | The type of entity that last updated the custom status.                                    |
| stage                     | The workflow stage of the status (e.g., New, In progress, Closed).                         |
| label                     | The display label for the status.                                                          |
| description               | A text description of the status.                                                          |
| type                      | The type(s) this status applies to (e.g., case, alert).                                    |

## Custom priorities

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the custom priority.                                               |
| community_uuid            | A unique identifier for the community related to the custom priority.                      |
| level                     | The numeric level of the priority.                                                         |
| created_at                | The date and time when the custom priority was created.                                    |
| created_by                | The user or system that created the custom priority.                                       |
| created_by_type           | The type of entity that created the custom priority (e.g., avatar, apikey).                |
| updated_at                | The date and time when the custom priority was last updated.                               |
| updated_by                | The user or system that last updated the custom priority.                                  |
| updated_by_type           | The type of entity that last updated the custom priority.                                  |
| color                     | The color associated with the priority (CSS variable or color name).                       |
| label                     | The display label for the priority.                                                        |
| description               | A text description of the priority.                                                        |

## Entities properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the entity.                                                        |
| name                      | The name of the entity.                                                                    |
| alerts_generation         | The alert generation mode of the entity.                                                   |
| description               | The description of the entity.                                                             |
| entity_id                 | The ID of the entity.                                                                      |
| community_uuid            | A unique identifier for the community related to the entity.                               |
| created_at                | The date and time when the entity was created.                                             |
| updated_at                | The date and time when the entity was last updated.                                        |

## Intakes properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the intake.                                                        |
| name                      | The name of the intake.                                                                    |
| community_uuid            | A unique identifier for the community related to the intake.                               |
| entity_uuid               | A unique identifier for the entity related to the intake.                                  |
| format_uuid               | A unique identifier for the format related to the intake.                                  |
| intake_key                | The intake key of the intake.                                                              |
| created_at                | The date and time when the intake was created.                                             |
| created_by                | The user or system that created the intake.                                                |
| created_by_type           | The type of entity that created the intake (e.g., avatar, apikey).                         |
| updated_at                | The date and time when the intake was last updated.                                        |
| updated_by                | The user or system that last updated the intake.                                           |
| updated_by_type           | The type of user that last updated the intake.                                             |
| is_custom_format          | Indicate if the intake uses a custom format.                                               |
| connector_configuration_uuid    | A unique identifier for the connector configuration related to the intake.           |

## Communities properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the community.                                                     |
| name                      | The name of the community.                                                                 |
| description               | The description of the community.                                                          |
| homepage_url              | The homepage url of the community.                                                         |
| picture_mode              | The picture mode of the community.                                                         |
| created_at                | The date and time when the community was created.                                          |
| created_by                | The user or system that created the community.                                             |
| created_by_type           | The type of entity that created the community (e.g., avatar, apikey).                      |
| updated_at                | The date and time when the community was last updated.                                     |
| company_size              | The size of the company.                                                                   |
| company_security_team_size  | The size of the security team.                                                           |
| company_sector            | The sector of the company.                                                                 |
| company_location          | The location of the company.                                                               |
| is_parent                 | Indicate if the community is a parent community.                                           |
| parent_uuid               | A unique identifier of the parent community.                                               |
| subcommunities            | Indicate if the community has subcommunities.                                              |
| is_mfa_enforced           | Indicate if MFA is enforced at the community level.                                        |
| session_timeout           | The duration before users are automatically logged after inactivity.                       |
| disable_inactive_avatars  | Indicate if users are disabled after 90 days of inactivity.                                |
| disabled                  | Indicate if the community is disabled.                                                     |

## Assets

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the asset.                                                         |
| community_uuid            | A unique identifier for the community related to the asset.                                |
| name                      | The name of the Asset                                                                      |
| type                      | Type of asset (host, account or  network.)                                                 |
| category                  | Category of the asset                                                                      |
| criticality               | Criticality of the asset                                                                   |
| created_at                | The date and time when the asset was created.                                              |
| updated_at                | The date and time when the asset was last updated.                                         |
| revoked                   | Indicates whether the asset is revoked                                                     |
| reviewed                  | Indicates if the asset has been reviewed                                                   |
| atoms                     | List of related names/identifiers (e.g., hostname, IPs, etc.)                              |

## Asset Properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| asset_uuid                | UUID of the asset to which the property is associated                                      |
| value                     | The value of the property (e.g., darwin)                                                   |
| name                      | The name of the property (e.g., os)                                                        |

## Asset Partitions

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| asset_uuid                | UUID of the asset to which the partitions is associated                                    |
| community_uuid            | UUID of the community the asset belongs to                                                 |
| asset_name                | The name of the asset that the partitions is associated with                               |
| last_seen                 | Last time the asset was seen                                                               |
| mountpoint                | Partition mount point (e.g., C:)                                                           |
| encrypted                 | Whether the partition is encrypted (true/false)                                            |

## Asset Accounts

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| asset_uuid                | UUID of the asset to which the accounts is associated                                      |
| community_uuid            | UUID of the community the asset belongs to                                                 |
| asset_name                | The name of the asset that the partitions is associated with                               |
| last_seen                 | Last time the asset was seen                                                               |
| username                  | Name of the local user account                                                             |
| is_enabled                | Whether the account is enabled                                                             |
| is_admin                  | Whether the account has administrative privileges                                          |
| last_logon                | Last time the account was used to log in                                                   |
| bad_password_count        | Number of failed logon attempts                                                            |
| number_of_logons          | Total number of logons recorded                                                            |
| account_type              | Type of account (LocalUser, MicrosoftAccount, ...)                                         |

## Event Telemetry

The **event_telemetry** data source provides aggregated metrics about the events processed by your intakes.
It allows you to monitor, report, and troubleshoot data ingestion across your Sekoia.io tenant.

Each record in **event_telemetry** represents a time-bucketed summary of event activity for a given intake, including the number of events, total data volume, event sizes, and processing lags.
This makes it easy to:

* Analyze your data usage over time, per intake
* Identify anomalies such as sudden spikes in data volume or processing delays
* Detect potential misconfigurations that could lead to unexpected data costs or ingestion issues

Typical Use Cases:

* Usage reporting: Track how much data each intake is sending over specific timeframes.
* Performance monitoring: Observe event size distributions and processing lags to ensure optimal pipeline performance.
* Root cause analysis: Investigate policy violations or overages by drilling down into intake-level telemetry.

You can query **event_telemetry** in the SOL query builder and combine it with other sources (e.g., intakes) to enrich your reports with intake names and configurations.


| **Property**            | **Description**                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------|
| community_uuid          | UUID of the community the events belongs to                                                  |
| intake_uuid             | UUID of the intake source generating the events                                              |
| intake_dialect_uuid     | UUID representing the dialect used for the intake                                            |
| bucket_start_date       | UTC timestamp representing the beginning of the aggregation window                           |
| bucket_end_date         | UTC timestamp representing the end of the aggregation windows                                |
| occurrences             | Number of events in the aggregation                                                          |
| total_message_size      | Total size (in bytes) of raw events in the bucket                                            |
| max_message_size        | Size (in bytes) of the largest raw event in the bucket                                       |
| min_message_size        | Size (in bytes) of the smallest raw event in the bucket                                      |
| total_event_size        | Total size (in bytes) of all events in the bucket                                            |
| max_event_size          | Size (in bytes) of the largest event in the bucket                                           |
| min_event_size          | Size (in bytes) of the smallest event in the bucket                                          |
| max_lag                 | Maximum observed delay (in seconds) between the event's timestamp and its reception date.    |
| min_lag                 | Minimum observed delay (in seconds) between the event's timestamp and its reception date.    |
| total_lag               | Total accumulated lag (in seconds) across all events in the bucket.                          |
| max_processing_lag      | Maximum processing time (in seconds) taken by Sekoia.io to process an event.                 |
| min_processing_lag      | Minimum processing time (in seconds) taken by Sekoia.io to process an event.                 |
| total_processing_lag    | Total accumulated processing time (in seconds) for all events in the bucket.                 |
