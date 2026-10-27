# SOL technical reference: Datasources

`SOL` provides seamless access to all critical security data within Sekoia SOC platform:

| Data Source | Description | Use Cases |
|-------------|-------------|-----------|
| `events` | Security events | Threat hunting, incident investigation, SOC reporting. You will receive events that are retained for the duration of your hot storage |
| [event_telemetry](#event_telemetry) | Telemetry on events | Analytics on your ingestion pipelines |
| [eternal_events](#eternal_events) | Security events related to alerts or cases | Extract metrics from events related to alerts/cases. Access events related to an alert that are beyond your hot storage retention period |
| [alerts](#alerts) | Security alerts and detections | SOC monitoring, alert pattern analysis |
| [cases](#cases) | Security incidents and cases | Case management, incident correlation |
| [custom_statuses](#custom_statuses) | Alerts and cases custom statuses | Reporting |
| [custom_priorities](#custom_priorities) | Cases custom priorities | Reporting |
| [communities](#communities) | Communities (for multi-tenant only) | Multi-tenant reporting |
| [intakes](#intakes) | Data sources | Data source management, volume monitoring |
| [intake_formats](#intake_formats) | Intake formats (parsers) | Volume monitoring |
| [entities](#entities) | Company entities | Entity tracking, detailed reporting |
| [assets](#assets) | Known Assets | Asset Investigations |
| [asset_properties](#asset_properties) | Listing known properties related to the Asset | Asset Investigations |
| [asset_partitions](#asset_partitions) | Partitions on a per Asset basis and Hygiene related to these | Understand and improve Hygiene state Note: Part of the Reveal plan |
| [asset_accounts](#asset_accounts) | Listing local users accounts related to the Asset | Impact analysis and incident correlation Note: Part of the Reveal plan |
| [asset_applications](#asset_applications) | Software and applications installed on assets | Application discovery, software inventory, unsigned binary detection. Note: Part of the Reveal plan |
| [asset_vulnerabilities](#asset_vulnerabilities) | CVE-based vulnerabilities associated with assets, enriched from NVD | Vulnerability management, risk prioritization, patch tracking. Note: Part of the Reveal plan |
| [asset_poi](#asset_poi) | Points of interest detected on assets (UEBA, notable activity) | Threat hunting, behavioral analysis, MITRE ATT&CK mapping. Note: Part of the Reveal plan |
| [asset_risk_scores](#asset_risk_scores) | Current risk score for each asset | Current risk reporting and prioritization |
| [asset_risk_score_history](#asset_risk_score_history) | Events that affected an asset risk score | Risk trajectory and score-driver analysis |
| [rule_definitions](#rule_definitions) | Detection rule definitions (Sigma, CTI, Anomaly...) | Rules coverage reporting, audit of detection catalog |
| [rule_instances](#rule_instances) | Instances of detection rules per community | Monitor enabled/disabled rules, compliance reporting |
| [playbooks](#playbooks) | Playbooks of your community, with their status and triggers | Automation inventory, playbook health monitoring |
| [playbook_runs](#playbook_runs) | Executions of your playbooks | Success rate, failure analysis, detection of stuck runs |
| [node_runs](#node_runs) | Executions of each playbook step (triggers, actions, operators) | Root cause of failed runs, failed actions |

## event_telemetry

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

## eternal_events

The **eternal_events** data source gives you access to the events attached to an alert or a case. These events are stored permanently, whatever your retention subscription, so they remain queryable long after the same events have expired from the `events` data source.

Query **eternal_events** when the alert or case you are investigating has passed your retention window. It is also the natural data source whenever you want to scope a query to alert or case evidence, even within your retention window, since it contains nothing else: use it to investigate a given alert or to build metrics over the events that raised your alerts.

**eternal_events** shares the same schema as `events`. The filters, aggregations and functions you use against `events` apply here without change.

For a full explanation of what is preserved and how to reach it from the interface, see [Eternal events](/xdr/features/investigate/eternal_events.md).

## alerts

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
| time_to_acknowledge       | Duration in seconds between alert creation and transition to the Acknowledged status. Remains null if no such transition has been recorded.             |
| time_to_respond           | Duration in seconds between acknowledgement and transition to the Ongoing status. If no acknowledgement duration has been recorded, this is measured from alert creation instead. Remains null if no transition to Ongoing has been recorded.                               |
| time_to_resolve           | Duration in seconds recorded when the alert transitions to Closed or Rejected. Computed as the time elapsed since alert creation, minus the recorded acknowledgement and response durations. This is not necessarily the total duration from creation to closure.                             |
| time_to_ingest            | The duration from alert generation to its final ingestion into the system in seconds.        |
| occurrences               | The number of alert occurrences                                                              |
| rule_instance_uuid        | A unique identifier for the rule that generated the alert.                                   |
| cases                     | List of cases associated to the alert.                                                       |
| assets                    | List of assets associated to the alert.                                                      |
| threats                   | List of threats associated the alert.                                                        |
| custom_fields             | Structured metadata attached to the alert. Access a field with `custom_fields.<field_name>`. |

!!! note "Using alert timing fields for SLA reporting"

    Alert timing fields are populated by status transitions, not directly by comments, urgency changes, playbook executions, or remediation actions. An automated action can populate them if it performs the corresponding status transition.

    - **`time_to_acknowledge`** measures the duration from alert creation to the transition to `Acknowledged`.
    - **`time_to_respond`** measures the duration from acknowledgement to the transition to `Ongoing`. If no acknowledgement duration has been recorded, it is measured from alert creation instead.
    - **`time_to_resolve`** is recorded when the alert transitions to `Closed` or `Rejected`. It is calculated as the duration since alert creation, minus the recorded acknowledgement and response durations. It is therefore **not necessarily the total time from creation to closure**.

    A closed alert can have a `null` `time_to_respond` if it never transitioned to `Ongoing`. This does not imply that the alert was not investigated or remediated.

    For SLA reporting, distinguish two indicators:

    - **Time to acknowledge:** use `time_to_acknowledge` for alerts with a recorded acknowledgement.
    - **Total time to close:** add `time_to_acknowledge`, `time_to_respond`, and `time_to_resolve`. Treat missing acknowledgement and response durations as zero, but only include alerts with a non-null `time_to_resolve`.

    All durations are expressed in seconds. Report missing measurements separately: excluding null values from an SLA percentage means that the percentage covers only alerts with a recorded measurement, not all alerts.
    
## cases

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
| custom_fields             | Structured metadata attached to the case. Access a field with `custom_fields.<field_name>`. |

## custom_statuses

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

## custom_priorities

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

## communities

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

## intakes

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

## intake_formats

| **Property**                  | **Description**                                                                            |
|-------------------------------|--------------------------------------------------------------------------------------------|
| uuid                          | A unique identifier for the intake format.                                                 |
| community_uuid                | A unique identifier for the community related to the intake format.                        |
| name                          | The name of the intake format.                                                             |
| slug                          | A URL-friendly identifier for the intake format (e.g., azure-application-gateway).        |
| description                   | A description of the intake format.                                                        |
| created_at                    | The date and time when the intake format was created.                                      |
| created_by                    | The user or system that created the intake format.                                         |
| created_by_type               | The type of entity that created the intake format (e.g., avatar, apikey).                  |
| updated_at                    | The date and time when the intake format was last updated.                                 |
| updated_by                    | The user or system that last updated the intake format.                                    |
| updated_by_type               | The type of entity that last updated the intake format.                                    |
| automation_connector_uuid     | A unique identifier for the automation connector related to the intake format.             |

For example queries using intake_formats, see [Join examples](sol_query_examples.md#join-examples).

## entities

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

## assets

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
| tags                      | List of tags associated with the asset                                                     |
| source                    | How the asset was created: `automatic` (discovered) or `manual` (created by a user)        |
| connectors.uuid           | UUIDs of the asset connector configurations that reported the asset                        |
| connectors.connector_uuid | UUIDs of the asset connector types that reported the asset                                 |

Sekoia Asset Discovery is listed in `connectors` like any other connector, with the configuration UUID `e0437ab0-5e38-4bd3-b922-c500644889c3` and no `connector_uuid`. So `not connectors.connector_uuid` keeps the assets that no configured asset connector reported.

For example queries using tags or connectors, see [Assets query examples](sol_query_examples.md#assets-query-examples).

## asset_properties

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| asset_uuid                | UUID of the asset to which the property is associated                                      |
| value                     | The value of the property (e.g., darwin)                                                   |
| name                      | The name of the property (e.g., os)                                                        |

## asset_partitions

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| asset_uuid                | UUID of the asset to which the partitions is associated                                    |
| community_uuid            | UUID of the community the asset belongs to                                                 |
| asset_name                | The name of the asset that the partitions is associated with                               |
| last_seen                 | Last time the asset was seen                                                               |
| mountpoint                | Partition mount point (e.g., C:)                                                           |
| encrypted                 | Whether the partition is encrypted (true/false)                                            |

## asset_accounts

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

## asset_applications

*This data source is part of the Reveal plan.*

The **asset_applications** data source lists software and applications installed on assets discovered across your environment. Each record represents a unique application instance on a given asset, including version, signing status, and execution metadata.

Use this data source to build software inventories, detect unsigned binaries, and identify applications with known vulnerabilities via their CPE identifier.

| **Property**      | **Description**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| uuid              | Unique identifier of the application record                                                       |
| community_uuid    | UUID of the community the asset belongs to                                                        |
| asset_uuid        | Unique identifier of the asset                                                                    |
| name              | Application name                                                                                  |
| version           | Application version                                                                               |
| author            | Vendor or author of the application                                                               |
| filename          | Executable filename                                                                               |
| install_date      | Date the application was installed                                                                |
| install_path      | Installation path on the asset                                                                    |
| last_execution    | Last time the application was executed                                                            |
| last_user_name    | Last user who ran the application                                                                 |
| signed            | Whether the binary is digitally signed                                                            |
| signer_cn         | Common name of the signer                                                                         |
| hash              | File hash                                                                                         |
| os                | Operating system the application runs on                                                          |
| cpe               | CPE identifier, used for vulnerability matching                                                   |
| purl              | Package URL (PURL) identifier for the application                                                 |
| architecture      | CPU architecture                                                                                  |
| created_at        | Timestamp when this application was first recorded                                                |
| updated_at        | Last update timestamp                                                                             |
| deleted_at        | Timestamp when the application was removed. Applications are soft-deleted and remain in the data source after removal. Filter on `isnull(deleted_at)` to query active applications only. |

??? example "Count unsigned applications across assets"

    ```
    asset_applications
    | where signed == false and isnull(deleted_at)
    | aggregate count_distinct(asset_uuid)
    ```

??? example "Top 20 most widespread applications by number of assets"

    ```
    asset_applications
    | where isnull(deleted_at)
    | aggregate asset_count = count_distinct(asset_uuid) by name, version
    | top 20 by asset_count
    ```

## asset_vulnerabilities

*This data source is part of the Reveal plan.*

The **asset_vulnerabilities** data source exposes CVE-based vulnerabilities associated with your assets, enriched from the National Vulnerability Database (NVD). Each record links a vulnerability to the affected asset and the specific application version involved.

Use this data source to track open vulnerabilities, prioritize remediation by CVSS score, and measure your exposure over time.

| **Property**              | **Description**                                                                       |
|---------------------------|---------------------------------------------------------------------------------------|
| uuid                      | Unique identifier of the vulnerability record                                         |
| community_uuid            | UUID of the community the asset belongs to                                            |
| asset_uuid                | Unique identifier of the affected asset                                               |
| title                     | Vulnerability title, usually the CVE ID                                               |
| description               | Vulnerability description                                                             |
| cve_ids                   | List of CVE identifiers                                                               |
| cwe                       | CWE identifier associated with the vulnerability                                      |
| cvss_score                | CVSS base score                                                                       |
| unified_risk_score        | Unified risk score combining CVSS and contextual signals                              |
| unified_risk_score_str    | Human-readable label for the unified risk score (e.g., Critical, High)               |
| status                    | Vulnerability status: `open`, `accepted_risk`, `false_positive`, or `remediated`     |
| software                  | Name of the vulnerable software                                                       |
| version                   | Version of the vulnerable software                                                    |
| external_reference_id     | External identifier for the vulnerability in a third-party system                    |
| source_connector_uuid     | UUID of the connector that sourced this vulnerability                                 |
| created_at                | Date the vulnerability was first recorded                                             |
| updated_at                | Last update timestamp                                                                 |
| closed_at                 | Date the vulnerability was closed                                                     |
| closed_by                 | User or system that closed the vulnerability                                          |
| closed_by_type            | Type of entity that closed the vulnerability (e.g., avatar, apikey)                  |

??? example "Count assets with at least one open critical vulnerability (CVSS >= 9)"

    ```
    asset_vulnerabilities
    | where status == "open" and cvss_score >= 9
    | aggregate count_distinct(asset_uuid)
    ```

??? example "Top 20 assets with the most open vulnerabilities"

    ```
    asset_vulnerabilities
    | where status == "open"
    | aggregate count() by asset_uuid
    | top 20 by count
    ```

## asset_poi

*This data source is part of the Reveal plan.*

The **asset_poi** data source exposes points of interest (POIs) detected on assets, derived from UEBA analysis and notable activity detection. Each record is linked to a MITRE ATT&CK phase, giving you a structured view of behavioral signals across your asset inventory.

Use this data source to surface suspicious activity, map behavioral patterns to MITRE ATT&CK, and prioritize assets for investigation. For a functional overview of how points of interest work, see [Points of interest](/xdr/features/detect/points_of_interest.md).

| **Property**          | **Description**                                                          |
|-----------------------|--------------------------------------------------------------------------|
| uuid                  | Unique identifier of the POI record                                      |
| community_uuid        | UUID of the community the asset belongs to                               |
| asset_uuid            | Unique identifier of the asset                                           |
| poi_name              | Name of the point of interest                                            |
| poi_type              | Type of POI: `ueba` or `notable_activity`                               |
| mitre_attack_phase    | MITRE ATT&CK phase associated with the POI                               |
| severity              | Severity score from 0 (lowest) to 100 (highest)                         |
| description           | Description of the POI                                                   |
| created_at            | Timestamp when the POI was created                                       |

!!! tip "Coming soon"
    The `notable_activity` value for `poi_type` is not yet available. Queries filtering on `poi_type == "notable_activity"` will return no results until this capability is released.

??? example "Top 20 assets with the most points of interest"

    ```
    asset_poi
    | aggregate poi_count = count() by asset_uuid
    | top 20 by poi_count
    ```

??? example "Count POIs by MITRE ATT&CK phase"

    ```
    asset_poi
    | aggregate count() by mitre_attack_phase
    | sort by count desc
    ```


## asset_risk_scores

*This data source is part of the Reveal plan.*

The `asset_risk_scores` data source contains the current risk score for each asset. It contains one row per asset, and `asset_uuid` is unique across the platform.

Sekoia rewrites the row each time it recomputes the score. This data source therefore represents the current state only. Use `asset_risk_score_history` to analyze the events that affected the score over time.

These data sources are already scoped to the communities available to the user through the associated assets. To filter results for a specific community, use a lookup on the `assets` data source and filter on `community_uuid`.

The score is computed from the two sub-scores below:

- `exposure_score` measures persistent exposure from open vulnerabilities and hygiene issues. It is capped at 40.
- `recent_activity_score` measures recent alerts, cases and points of interest. Its value decreases over time and is capped at 40.

Their sum forms `base_score`. A factor derived from the asset criticality is then applied to the base score.

The calculation is expressed as follows:

```text
base_score = exposure_score + recent_activity_score
final_score = round(min(100, base_score × criticality_factor))
criticality_adjustment = final_score - base_score
```

The criticality factor increases linearly within each criticality band:

| Criticality value | Criticality band | Factor |
| --- | --- | --- |
| 0 | Not set | 1.00 |
| 1 to 24 | Low | 0.80 to 1.00 |
| 25 to 49 | High | 1.05 to 1.12 |
| 50 to 74 | Severe | 1.13 to 1.22 |
| 75 to 100 | Critical | 1.23 to 1.35 |

The risk bands displayed in the Sekoia interface are:

| Band | Score range |
| --- | --- |
| Low | 0 to 24 |
| Moderate | 25 to 49 |
| High | 50 to 74 |
| Critical | 75 to 100 |

| **Field** | **Description** |
| --- | --- |
| `uuid` | Unique identifier of the score record |
| `asset_uuid` | Unique identifier of the asset |
| `exposure_score` | Persistent risk sub-score based on open vulnerabilities and hygiene issues, such as a disabled firewall or an unencrypted disk. Capped at 40 |
| `recent_activity_score` | Time-decaying risk sub-score based on recent alerts, cases and points of interest. Capped at 40 |
| `base_score` | Sum of `exposure_score` and `recent_activity_score`, before the criticality factor is applied |
| `criticality_value` | Criticality of the asset at the time of computation, from 0 to 100. A value of 0 means that no criticality is set |
| `criticality_adjustment` | Difference between `final_score` and `base_score`, calculated after rounding. It represents the points added or removed by the criticality factor |
| `final_score` | Current asset risk score, from 0 to 100. It is calculated by applying the cap before rounding to the nearest integer |
| `last_updated` | Date and time when the score was last recomputed |

## asset_risk_score_history

*This data source is part of the Reveal plan.*

The `asset_risk_score_history` data source records the events that affected an asset risk score. It feeds the risk trajectory displayed in the asset timeline.

Each row represents one event and that event's individual contribution. The `contribution` field is not the asset's aggregate risk score.

History entries and points of interest are retained for 90 days. For `hygiene` and `criticality` events, the latest entry older than 90 days is retained for each asset and event type because the risk score engine uses it as a baseline for future calculations.

The `final_score` field is the score recalculated at the entry's `event_date`, immediately after the event. It is populated during the next score recomputation and can therefore remain empty for less than one hour while the recomputation is queued. It does not represent the asset's current score.

| **Field** | **Description** |
| --- | --- |
| `id` | Sequential identifier of the history entry |
| `asset_uuid` | Unique identifier of the asset |
| `type` | Type of event. Possible values are `alert`, `case`, `poi`, `vulnerability`, `hygiene` and `criticality` |
| `title` | Human-readable title of the event, such as `Alert created`, `Firewall disabled` or `Criticality changed to high` |
| `event_date` | Date and time when the event occurred |
| `contribution` | Contribution of the event to the score. It is expressed as points for a `delta` contribution or as a factor for a `multiplier` contribution |
| `contribution_type` | Type of contribution. `delta` adds or removes points from a sub-score. `multiplier` applies a criticality factor to the base score |
| `level` | Severity or criticality level of the event. For alerts and cases, possible values are `informational`, `low`, `medium`, `high` and `critical`. For vulnerabilities, possible values are `low`, `medium`, `high` and `critical`. For criticality events, possible values are `low`, `high`, `severe` and `critical`. This field is empty for hygiene and POI entries, and when a criticality event resets the asset criticality to 0 |
| `criticality` | New criticality of the asset, from 0 to 100. Set only for `criticality` entries |
| `previous_criticality` | Criticality of the asset before the change, from 0 to 100. Set only for `criticality` entries |
| `final_score` | Risk score recalculated at `event_date`, immediately after the event. It can be empty until the next score recomputation and does not represent the current score |
| `event_uuid` | UUID of the source alert, case or point of interest. Empty for hygiene, vulnerability and criticality entries |
| `created_at` | Date and time when the history row was written |

## rule_definitions

The **rule_definitions** data source provides the list of detection rule definitions available in your catalog, including Sekoia-managed and custom rules.

It allows you to audit your detection coverage, report on rule types and origins, and cross-reference with rule instances to understand what is deployed in your communities.

The `format_uuid` property can be joined with the [intake_formats](#intake_formats) data source to identify the integration a rule targets.

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the rule definition.                                               |
| name                      | The name of the detection rule.                                                            |
| community_uuid            | A unique identifier for the community related to the rule definition. Empty for Sekoia-managed rules available to all communities. |
| source                    | The origin of the rule (e.g., `SEKOIA`, `Custom`).                                         |
| type                      | The type of rule (e.g., `sigma`, `cti`, `anomaly`).                                        |
| format_uuid               | A unique identifier for the intake format the rule targets. Only filled for Integration rules, i.e., rules written for a specific integration tool such as Microsoft Sentinel. |
| created_at                | The date and time when the rule definition was created.                                    |
| created_by                | The user or system that created the rule definition.                                       |
| created_by_type           | The type of entity that created the rule definition (e.g., avatar, application).           |
| updated_at                | The date and time when the rule definition was last updated.                               |
| updated_by                | The user or system that last updated the rule definition.                                  |
| updated_by_type           | The type of entity that last updated the rule definition.                                  |

## rule_instances

The **rule_instances** data source provides the list of rule instances per community, i.e., the actual deployment state of each detection rule.

It can be joined with `rule_definitions` to produce reports on which rules are enabled or disabled, by type and origin.

| **Property**              | **Description**                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------|
| uuid                      | A unique identifier for the rule instance.                                                 |
| rule_definition_uuid      | UUID of the related rule definition (used for `lookup` joins).                             |
| community_uuid            | A unique identifier for the community where the rule instance is applied.                  |
| enabled                   | Whether the rule is currently enabled (`true` / `false`).                                  |
| created_at                | The date and time when the rule instance was created.                                      |
| created_by                | The user or system that created the rule instance.                                         |
| created_by_type           | The type of entity that created the rule instance (e.g., avatar, application).             |
| updated_at                | The date and time when the rule instance was last updated.                                 |
| updated_by                | The user or system that last updated the rule instance.                                    |
| updated_by_type           | The type of entity that last updated the rule instance.                                    |

??? example "Breakdown of detection rules by source and type, with enabled rules count"

    The following query generates a breakdown of detection rules by source and type, with the count of enabled rules per category. It is useful for monthly client reporting or coverage monitoring:

    ```
    rule_definitions
    | lookup rule_instances on uuid == rule_definition_uuid into rule
    | aggregate
        rules_count = count(),
        enabled_rules_count = count(iff(rule.enabled == True, True, null))
      by source = coalesce(source, "Custom"), type
    | order by source, type
    | select source, type, rules_count, enabled_rules_count
    ```

## playbooks

The **playbooks** data source lists the playbooks of your community, with their current status and their trigger configurations. Each record represents the current version of a playbook.

Use this data source to monitor the health of your automation: count active playbooks, find playbooks in error, and spot activated playbooks that stopped running. For a functional overview of playbooks, see [Playbooks](/xdr/features/automate/index.md).

!!! note "Required permission"
    Querying this data source requires the **View playbooks** permission.

| **Property**             | **Description**                                                                                                       |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------|
| uuid                     | Unique identifier of the playbook                                                                                     |
| version                  | Version number of the playbook                                                                                        |
| community_uuid           | UUID of the community the playbook belongs to                                                                         |
| meta_community_uuids     | For a meta playbook, UUIDs of the communities that run it                                                             |
| status                   | Playbook status: `activated`, `deactivated`, `starting`, `stopping`, or `error`                                       |
| status_message           | Reason of the current status, for example why the playbook is in `error`                                             |
| is_valid                 | Whether the playbook configuration is valid                                                                           |
| name                     | Playbook name                                                                                                         |
| created_at               | Date the playbook was created                                                                                         |
| created_by               | User or system that created the playbook                                                                              |
| created_by_type          | Type of entity that created the playbook                                                                              |
| updated_at               | Date the playbook was last updated                                                                                    |
| updated_by               | User or system that last updated the playbook                                                                         |
| updated_by_type          | Type of entity that last updated the playbook                                                                         |
| activated_at             | Date the playbook was last activated                                                                                  |
| activated_by             | User or system that last activated the playbook                                                                       |
| activated_by_type        | Type of entity that last activated the playbook                                                                       |
| deactivated_at           | Date the playbook was last deactivated                                                                                |
| deactivated_by           | User or system that last deactivated the playbook                                                                     |
| deactivated_by_type      | Type of entity that last deactivated the playbook                                                                     |
| is_parent                | Whether the playbook is a parent meta playbook                                                                        |
| trigger_configurations.* | Trigger configurations of the playbook: `uuid`, `name`, `value`, `trigger_id`, and `status` (`running`, `stopped`, `starting`, or `stopping`) |
| playbook_runs.*          | Runs of the playbook: `uuid`, `status`, `error`, `store`, `started_at`, `started_by`, `started_by_type`, `pending_at`, `running_at`, and `finished_at`. See [playbook_runs](#playbook_runs) |

!!! note "Properties available in SOL"
    This data source exposes a subset of the properties returned by the [Playbooks API](https://docs.sekoia.com/xdr/develop/rest_api/playbooks/). Properties such as `description`, `custom_fields`, `doctor_status`, `doctor_codes`, or `status_tags` are not available in SOL.

!!! tip "Working with the runs of a playbook"
    Each playbook record includes the list of all its runs in the `playbook_runs.*` fields. Use `project` to return only the columns you need, for example `playbooks | project name, status`. In a `where` clause, a condition on `playbook_runs.*` matches a playbook when at least one of its runs matches.

??? example "Count activated playbooks"

    ```shell
    playbooks
    | where status == "activated"
    | aggregate active_playbooks = count()
    ```

??? example "List activated playbooks without any run in the last 7 days"

    These playbooks are active but no longer run. Their trigger or the data they listen to may be broken.

    ```shell
    playbooks
    | where status == "activated"
    | where not playbook_runs.started_at > ago(7d)
    | project name, activated_at, updated_at
    ```

??? example "List playbooks in error with the reason"

    ```shell
    playbooks
    | where status == "error"
    | project name, status_message, updated_at
    ```

## playbook_runs

The **playbook_runs** data source lists the executions of your playbooks. Each record represents one run, with its status, its timing, and the playbook it belongs to.

Use this data source to measure the success rate of your automation, find the playbooks that fail the most, and detect runs that never finish.

!!! note "Required permission"
    Querying this data source requires the **View playbook runs** permission.

| **Property**      | **Description**                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| uuid              | Unique identifier of the run                                                                     |
| community_uuid    | UUID of the community the run belongs to                                                         |
| playbook.*        | Playbook that ran: `uuid`, `name`, `version`, and `status`                                       |
| event             | Name of the event that started the run                                                           |
| status            | Run status: `pending`, `running`, `finished` (success), or `error`                               |
| error             | Error message for failures raised by the playbook engine, for example when a run exceeds its time limit |
| store             | Data stored by the playbook during the run                                                       |
| started_at        | Date the run started                                                                             |
| started_by        | Identifier of what started the run                                                               |
| started_by_type   | Type of what started the run                                                                     |
| pending_at        | Date the run was queued                                                                          |
| running_at        | Date the run started executing                                                                   |
| finished_at       | Date the run ended                                                                               |

!!! tip "Find why a run failed"
    The `error` field of a run is only filled for failures raised by the playbook engine. When an action fails, the run status is `error` and the error message is stored on the failed step. To get it, query [node_runs](#node_runs) and filter on `playbook_run.status == "error"`.

??? example "Success rate over the last 7 days"

    The success rate only counts ended runs: runs still pending or running are excluded.

    ```shell
    playbook_runs
    | where started_at > ago(7d)
    | aggregate successful_runs = sum(iff(status == "finished", 1, 0)), failed_runs = sum(iff(status == "error", 1, 0))
    | where successful_runs + failed_runs > 0
    | extend success_rate = round(100.0 * successful_runs / (successful_runs + failed_runs), 1)
    ```

??? example "Daily runs by status over the last 30 days"

    ```shell
    playbook_runs
    | where started_at > ago(30d)
    | aggregate runs = count() by bin(started_at, 1d), status
    | sort by started_at asc
    | render columnchart with (x=started_at, y=runs, breakdown_by=status, mode=stacked)
    ```

??? example "Top 10 playbooks with the most failed runs over the last 7 days"

    ```shell
    playbook_runs
    | where started_at > ago(7d)
    | aggregate total_runs = count(), failed_runs = sum(iff(status == "error", 1, 0)) by playbook.name
    | where failed_runs > 0
    | extend error_rate = round(100.0 * failed_runs / total_runs, 1)
    | top 10 by failed_runs
    ```

??? example "Runs pending or running for more than one hour"

    ```shell
    playbook_runs
    | where status in ["running", "pending"]
    | where started_at < ago(1h)
    | aggregate stuck_runs = count(), oldest_run = min(started_at) by playbook.name
    | sort by stuck_runs desc
    ```

## node_runs

The **node_runs** data source lists the executions of each step of your playbook runs: triggers, actions, and operators. Each record represents one step execution, with its error message, its timing, and the module configuration it used.

Use this data source to find the root cause of failed runs, and to list the actions that failed with their error message.

!!! note "Required permission"
    Querying this data source requires the **View playbook runs** permission.

| **Property**               | **Description**                                                                                     |
|----------------------------|-----------------------------------------------------------------------------------------------------|
| uuid                       | Unique identifier of the step execution                                                             |
| community_uuid             | UUID of the community the step execution belongs to                                                 |
| node_type                  | Type of step: `trigger`, `action`, or `operator`                                                    |
| node_id                    | Identifier of the step within the playbook                                                          |
| parent_node_run_id         | For a step inside a loop, identifier of the parent step execution                                   |
| iteration                  | For a step inside a loop, index of the iteration                                                    |
| module_configuration_uuid  | UUID of the module configuration used by the step                                                   |
| module_configuration_name  | Name of the module configuration used by the step                                                   |
| action_uuid                | For an action step, UUID of the action it ran                                                       |
| action_name                | For an action step, name of the action it ran                                                       |
| triggered_by               | What triggered the step                                                                             |
| arguments                  | Arguments passed to the step                                                                        |
| outputs                    | Outputs returned by the step                                                                        |
| results                    | Results of the step                                                                                 |
| logs                       | Logs of the step                                                                                    |
| status                     | Step status: `started`, `pending`, `running`, `finished`, or `error`                                |
| error                      | Error message when the step failed                                                                  |
| started_at                 | Date the step execution was created                                                                 |
| pending_at                 | Date the step was queued                                                                            |
| running_at                 | Date a worker started executing the step                                                            |
| finished_at                | Date the step ended                                                                                 |
| playbook.*                 | Playbook the step belongs to: `uuid`, `name`, `version`, and `status`                               |
| playbook_run.*             | Run the step belongs to: `uuid`, `status`, `error`, `store`, `started_at`, `started_by`, `started_by_type`, `pending_at`, `running_at`, and `finished_at` |

!!! note "Steps inside loops"
    Each iteration of a loop creates its own step execution. A loop over 500 items that fails on every item counts 500 errors.

??? example "Top 20 errors that made a run fail over the last 7 days"

    ```shell
    node_runs
    | where started_at > ago(7d)
    | where status == "error"
    | where playbook_run.status == "error"
    | aggregate occurrences = count(), last_seen = max(started_at) by playbook.name, error
    | top 20 by occurrences
    ```

??? example "New errors over the last 30 days"

    Errors are sorted by first occurrence. A recent first occurrence often points to a change in a third-party API or in a playbook.

    ```shell
    node_runs
    | where started_at > ago(30d)
    | where status == "error"
    | aggregate first_seen = min(started_at), last_seen = max(started_at), occurrences = count() by error
    | sort by first_seen desc
    ```

??? example "Failed actions over the last 24 hours"

    ```shell
    node_runs
    | where started_at > ago(24h)
    | where node_type == "action"
    | where status == "error"
    | project started_at, playbook.name, action_name, error
    | sort by started_at desc
    ```

## Related articles

### Getting started and overview

* [SOL Overview](/xdr/features/investigate/sol_overview.md): Sekoia Operating Language overview.
* [SOL Getting Started](/xdr/features/investigate/sol_getting_started.md): This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.
* [SOL Best Practices](/xdr/features/investigate/sol_best_practices.md): Best practices to use SOL effectively.

### User guides

* [Create and Manage Queries](/xdr/features/investigate/create_manage_queries.md): Create and manage queries using SOL.
* [SOL How-to Guides](/xdr/features/investigate/sol_how_to_guides.md): Learn how to use the main functions of SOL to reach your goals (aggregate data, join tables, use external data, build a query library...).
* [SOL Query Examples](/xdr/features/investigate/sol_query_examples.md): Get inspiration from our examples.
* [SOL Datasets](/xdr/features/investigate/sol_datasets.md): Discover the CSV import feature that enables SOC analysts to enrich security investigations by importing external data sources directly into the SOL query environment.

### Technical reference

* [SOL Functions Reference](/xdr/features/investigate/sol_ref_functions.md): Reference article regarding functions used in SOL.
* [SOL Operators Reference](/xdr/features/investigate/sol_ref_operators.md): Reference article regarding operators used in the SOL language.
