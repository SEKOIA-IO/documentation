# Query examples

## Join examples

### Join between events and communities tables (for Multi-tenant)

=== "Query"

    ``` shell
    events
    | where timestamp > ago(5m)
    | limit 100
    | lookup communities on sekoiaio.customer.community_uuid == uuid
    | select timestamp, sekoiaio.customer.community_uuid, community.name

    ```

=== "Results"

    | timestamp                | sekoiaio.customer.community_uuid     | community.name     |
    | ------------------------ | ------------------------------------ | ------------------- |
    | 2026-03-25T15:17:20.357Z | 904df422-adf9-4be8-b2b6-d027c0d68184 | Reynholm Industries |
    | 2026-03-25T15:17:57.942Z | 904df422-adf9-4be8-b2b6-d027c0d68184 | Reynholm Industries |
    | 2026-03-25T15:17:15.356Z | 904df422-adf9-4be8-b2b6-d027c0d68184 | Reynholm Industries |


### Join between events and entities tables

=== "Query"

    ``` shell
    events
    | where timestamp > ago(24h)
    | limit 100
    | aggregate count=count() by sekoiaio.entity.uuid
    | lookup entities on sekoiaio.entity.uuid == uuid
    | select entity.name, count

    ```

=== "Results"

    | entity.name        | count     |
    | ------------------ | --------- |
    | HQ - London Office | 100       |
    | Cambridge Campus   | 20        |

### Join between alerts and communities tables (for Multi-tenant)

=== "Query"

    ``` shell
    alerts
    | aggregate count=count() by community_uuid
    | lookup communities on community_uuid == uuid
    | select community.name, community_uuid, count
    | limit 100

    ```

=== "Results"

    | community.name                              | community_uuid                       | count     |
    | ------------------------------------------- | ------------------------------------ | --------- |
    | Reynholm Industries                         | 904df422-adf9-4be8-b2b6-d027c0d68184 | 488       |
    | MIT - Massachusetts Institute of Technology | c0540367-9702-46e2-90c3-7ab65ead9a27 | 464       |

### Join between events and intake_formats tables

=== "Query"

    ``` shell
    events
    | where timestamp between (?time.start .. ?time.end)
    | aggregate count() by sekoiaio.intake.dialect_uuid
    | lookup intake_formats on sekoiaio.intake.dialect_uuid == uuid
    | select intake_format.name, count
    | limit 100
    ```

=== "Results"

    | intake_format.name       |  count      |
    | ------------------------ |  ---------  |
    | Sekoia.io Endpoint Agent |  9630384    |
    | HarfangLab EDR           |  9548402    |
    | Zscaler Internet Access  |  19224678   |

### Count events per intake format (event_telemetry)

=== "Query"

    ``` shell
    event_telemetry
    | where bucket_start_date between (?time.start .. ?time.end)
    | aggregate sum(occurrences) by intake_dialect_uuid
    | lookup intake_formats on intake_dialect_uuid == uuid
    | select intake_format.name, sum_occurrences
    | limit 100
    ```

=== "Results"

    | intake_format.name       |  sum_occurrences      |
    | ------------------------ |  ---------  |
    | HarfangLab EDR           |  739676     |
    | Sekoia.io Endpoint Agent |  744873     |
    | Zscaler Internet Access  |  1475940    |

### Data volume per intake format (event_telemetry)

=== "Query"

    ``` shell
    event_telemetry
    | where bucket_start_date between (?time.start .. ?time.end)
    | aggregate sum(total_event_size) by intake_dialect_uuid
    | lookup intake_formats on intake_dialect_uuid == uuid
    | select intake_format.name, sum_total_event_size
    | limit 100
    ```

=== "Results"

    | intake_format.name       |  sum_total_event_size      |
    | ------------------------ |  ------------------------  |
    | Zscaler Internet Access  |  1475940                   |
    | HarfangLab EDR           |  739676                    |
    | Sekoia.io Endpoint Agent |  744873                    |

### Resolve intake format name from intakes

=== "Query"

    ``` shell
    intakes
    | lookup intake_formats on format_uuid == uuid
    | select name, intake_format.name
    ```

=== "Results"

    | name          |  intake_format.name        |
    | ------------- |  ------------------------  |
    | Sekoia Agent  |  Sekoia.io Endpoint Agent  |
    | Zscaler       |  Zscaler Internet Access   |
    | Zscaler ZIA.  |  Zscaler Internet Access   |

## Alerts query examples

### Detection rules ranked by number of alerts

=== "Query"

    ``` shell
    alerts
    | where created_at > ago(30d)
    | aggregate total = sum(occurrences) by rule_name
    | top 100 by total

    ```

=== "Results"

    | rule_name                                    |  total |
    | -------------------------------------------- |  ----  |
    | SEKOIA Intelligence Feed                     |  132   |
    | Suspicious Mshta Execution                   |  82    |
    | HarfangLab EDR Critical Level Rule Detection |  58    |

### Assets ranked by number of alerts

=== "Query"

    ``` shell
    alerts
    | where created_at > ago(30d)
    | aggregate count=count() by assets.uuid
    | order by count desc
    | limit 100

    ```

=== "Results"

    | assets.uuid                          |  count |
    | ------------------------------------ |  ----  |
    | 44b54aac-0d06-48aa-bda7-533d73d4e3c4 |  113   |
    | c8946c7e-f502-4736-8bf2-f6025b91583a |  50    |
    | 0d624ec2-8861-4956-9cf2-4fc6962a47ba |  37    |

### Threats ranked by number of alerts

=== "Query"

    ``` shell
    alerts
    | where created_at > ago(30d)
    | aggregate count=count() by threats.name
    | order by count desc
    | limit 100

    ```

=== "Results"

    | threats.name                                     |  count |
    | ------------------------------------------------ |  ----  |
    | User Execution: Malicious File                   |  52    |
    | Command and Scripting Interpreter: PowerShell    |  42    |
    | Create or Modify System Process: Windows Service |  42    |

### Alerts per detection type

=== "Query"

    ``` shell
    alerts
    | where created_at > ago(30d)
    | aggregate count() by detection_type

    ```

=== "Results"

    | detection_type    | count |
    | ---------------   | ----- |
    | CTI Retrohunt     | 5     |
    | Sigma Correlation | 14    |
    | Sigma             | 238   |

### Average time to detect in last 30 days

=== "Query"

    ``` shell
    alerts
    | where created_at > ago(30d)
    | aggregate avg(time_to_detect)

    ```

=== "Results"

    | avg_time_to_detect  |
    | ------------------  |
    | 1035.6561679790027  |

### Rename columns and convert time_to_detect in minutes

=== "Query"

    ``` shell
    alerts
    | where time_to_detect != null
    | select entity = entity_name, rule = rule_name, ttd = time_to_detect/60
    | limit 10

    ```

=== "Results"

    | entity             | rule                     | ttd                 |
    | ------------------ | ------------------------ | ------------------- |
    | HQ - London Office | SEKOIA Intelligence Feed | 0.13333333333333333 |
    | HQ - London Office | OneNote Embedded File    | 0.13333333333333333 |
    | HQ - London Office | SEKOIA Intelligence Feed | 31.733333333333334  |

### Ranking of communities by alerts

=== "Query"

    ``` shell
    alerts
    | aggregate AlertCount = count() by community_uuid
    | lookup communities on community_uuid == uuid
    | order by AlertCount desc
    | select community.name, AlertCount

    ```

=== "Results"

    | community.name                              | AlertCount |
    | ------------------------------------------- | ---------- |
    | Reynholm Industries                         | 488        |
    | MIT - Massachusetts Institute of Technology | 464        |



## Assets query examples

### Filter assets with a specific tag

=== "Query"

    ``` shell
    assets
    | where tags.tag in ["Admin"]
    | limit 100
    ```

=== "Results"

    | uuid                                 | community_uuid                       | name          | tags              |
    | ------------------------------------ | ------------------------------------ | ------------- | ----------------- |
    | ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Admin"}] |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Admin"}] |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | [{"tag":"Admin"}] |


### Filter assets with multiple tags

=== "Query"

    ``` shell
    assets
    | where tags.tag in ["Admin", "Backup"]
    | limit 100
    ```

=== "Results"

    | uuid                                 | community_uuid                       | name          | tags               |
    | ------------------------------------ | ------------------------------------ | ------------- | ------------------ |
    | ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Admin"}]  |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Admin"}]  |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | [{"tag":"Backup"}] |


### List all distinct tags

=== "Query"

    ``` shell
    assets
    | distinct tags.tag
    | limit 100
    ```

=== "Results"

    | tags.tag |
    | -------- |
    | Admin.   |
    | Backup   |
    | Berlin   |


### Filter assets where tag starts with a prefix

=== "Query"

    ``` shell
    assets
    | where tags.tag startswith "Finance"
    | limit 100
    ```

=== "Results"

    | uuid                                 | community_uuid                       | name          | tags                              |
    | ------------------------------------ | ------------------------------------ | ------------- | --------------------------------- |
    | ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Finance"}]               |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Finance"}]               |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | [{"tag":"VIP"},{"tag":"Finance"}] |


### Filter assets where tag contains a string (case-insensitive)

=== "Query"

    ``` shell
    assets
    | where tags.tag contains~ "prod"
    | limit 100
    ```

=== "Results"

    | uuid                                 | community_uuid                       | name          | tags                                                     |
    | ------------------------------------ | ------------------------------------ | ------------- | -------------------------------------------------------- |
    | ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Tier1"},{"tag":"Production"},{"tag":"Berlin"}]  |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Pre-Prod"}]                                     |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | [{"tag":"Production"}]                                   |

### Count assets per tag

=== "Query"

    ``` shell
    assets
    | aggregate count() by tags.tag
    | order by count desc
    | limit 100
    ```

=== "Results"

    | tags.tag                                    | count |
    | ------------------------------------------- | ----- |
    | Local accounts                              | 16    |
    | MIT - Massachusetts Institute of Technology | 11    |

### Exclude assets with a specific tag

=== "Query"

    ``` shell
    assets
    | where not tags.tag in ["Backup"]
    | limit 100
    ```

=== "Results"

    | uuid                                 | community_uuid                       | name          | tags                                                     |
    | ------------------------------------ | ------------------------------------ | ------------- | -------------------------------------------------------- |
    | ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Tier1"},{"tag":"Production"},{"tag":"Berlin"}]  |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Pre-Prod"}]                                     |
    | b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | []                                                       |



## Events query examples

### Number of unique command lines per host.name

=== "Query"

    ``` shell
    events
    | where timestamp > ago(24h)
    | aggregate count=count_distinct(process.command_line) by host.name
    | order by count desc
    | limit 100

    ```

=== "Results"

    | host.name        | count |
    | ---------------- | ----- |
    | laptop-6a1ec62f  | 16    |
    | laptop-chris     | 525   |
    | laptop-b3205bc2  | 517   |

### Number of unique hostname per month

=== "Query"

    ``` shell
    events
    | where timestamp > ago(90d)
    | aggregate count=count_distinct(log.hostname) by month(timestamp)

    ```

=== "Results"

    | timestamp_month  | count |
    | ---------------- | ----- |
    | 2026-03          | 63    |

### Top 10 visited URL

=== "Query"

    ``` shell
    events
    | where timestamp >= ago(24h)
    | aggregate count() by url.domain
    | top 10 by count

    ```

=== "Results"

    | url.domain           | count |
    | -------------------- | ----- |
    | clients2.google.com  | 2088  |
    | www.deloitte.com     | 2040  |
    | www.squarespace.com  | 2010  |


### Top 10 blocked URL

=== "Query"

    ``` shell
    events
    | where timestamp >= ago(24h) and event.action == 'blocked' and user.name != null and url.domain != null
    | aggregate count() by url.domain
    | top 10 by count

    ```

=== "Results"

    | url.domain      | count |
    | --------------- | ----- |
    | www.amazon.fr   | 1044  |
    | www.myfritz.net | 1040  |
    | www.uol.com.br  | 1021  |

### Top 10 login failures on Windows

=== "Query"

    ``` shell
    events
    | where timestamp > ago(24h) and event.code == 4625
    | aggregate failed_login_count=count() by user.target.name
    | top 10 by failed_login_count

    ```

=== "Results"

    | user.target.name  | failed_login_count |
    | ----------------- | ------------------ |
    | barbara_liskov    | 204                |
    | ken_thompson      | 202                |
    | geoffrey_hinton   | 188                |

### Sekoia.io endpoint agents per version

=== "Query"

    ``` shell
    events
    | where timestamp >= ago(24h)
    | where sekoiaio.intake.dialect == 'sekoia.io endpoint agent'
    | where event.action == 'stats'
    | aggregate count_distinct(agent.id) by agent.version

    ```

=== "Results"

    | agent.version                                    | count_distinct_agent.id |
    | ------------------------------------------------ | ----------------------- |
    | v1.9.0+62292d9c63d80859269661252cfc84db4ff66d81  | 304                     |


### List unique user.name

=== "Query"

    ``` shell
    events
    | where timestamp >= ago(24h)
    | distinct(user.name)
    | limit 100

    ```

=== "Results"

    | user.name    |
    | ------------ |
    | SYSTEM       |
    | a_borg       |
    | ada_lovelace |

### Number of events per IP address

=== "Query"

    ``` shell
    events
    | where timestamp > ago(30d)
    | aggregate count=count() by client.ip
    | order by count desc
    | limit 100

    ```

=== "Results"

    | client.ip       | count |
    | --------------- | ----- |
    | 192.168.2.10    | 204   |
    | 192.168.2.22    | 202   |
    | 192.168.2.100   | 188   |


### Aggregate events by source.ip and action.outcome

=== "Query"

    ``` shell
    events
    | where timestamp >= ago(24h) and event.category == 'authentication'
    | aggregate count() by source.ip, action.outcome
    | limit 100

    ```

=== "Results"

    | source.ip | action.outcome | count |
    | ----------| -------------- | ----- |
    | 1.0.0.95  | failure        | 33    |
    | 1.0.0.95  | success        | 142   |
    | 1.5.178.82  | failure      | 24    |
    | 1.5.178.82  | success      | 136   |


### Events where process.name starts with 'chrome'

=== "Query"

    ``` shell
    events
    | where timestamp > ago(24h) and process.name startswith('chrome')
    | limit 100

    ```

=== "Results"

    | timestamp                                    |  dialect     | smart description |
    | -------------------------------------------- |  ----------  | ----------------- |
    | 2026-03-26T15:35:14.738Z                     |  Sekoia      | Text              |
    | 2026-03-26T15:35:03.740Z                     |  Sekoia      | Text              |
    | 2026-03-26T15:35:04.539Z                     |  Sekoia.     | Text              |


### Events of specific intake

=== "Query"

    ``` shell
    let intake_uuids = intakes | where name == '<intake name>' | distinct uuid;

    events
    | where timestamp >= ago(24h)
    | where sekoiaio.intake.uuid in intake_uuids
    | limit 100

    ```

=== "Results"

    | timestamp                                    |  dialect     | smart description |
    | -------------------------------------------- |  ----------  | ----------------- |
    | 2026-03-26T15:35:14.738Z                     |  HarfangLab  | Text              |
    | 2026-03-26T15:35:03.740Z                     |  HarfangLab  | Text              |
    | 2026-03-26T15:35:04.539Z                     |  HarfangLab  | Text              |


### Number of defended assets: unique host.name with more than 10 events during 2 weeks in the last 30 days

=== "Query"

    ``` shell
    events
    | where timestamp > ago(30d)
    | aggregate events_count = count() by host.name, week = week(timestamp)
    | where events_count > 10
    | aggregate week_count = count(), total_count = sum(events_count) by host.name
    | where week_count >= 2
    | order by total_count
    | project host.name, total_count
    | limit 100

    ```

=== "Results"

    | host.name       | total_count |
    | --------------- | ----------- |
    | desktop_awk     | 359626      |
    | desktop_neural  | 358417      |
    | laptop_coursera | 358319      |

!!! note
    Please note: the `select` command can also be used. `select` and `project` are aliases and both return the same results.

### host.os.type per Sekoia endpoint agent

=== "Query"

    ``` shell
    events
    | where timestamp >= ago(24h)
    | where sekoiaio.intake.dialect == 'sekoia.io endpoint agent'
    | aggregate count() by host.os.type
    | limit 100

    ```

=== "Results"

    | host.os.type    | count  |
    | --------------- | ------ |
    | windows         | 590720 |


### Received Kbytes per month per intake

=== "Query"

    ``` shell
    event_telemetry
    | where bucket_start_date >= ago(30d)
    | aggregate sum_bytes = sum(total_message_size) by intake_uuid
    | lookup intakes on intake_uuid == uuid
    | select sum_gb = sum_bytes / (1000*1000*1000), intake.name
    | order by sum_gb desc

    ```

=== "Results"

    | sum_gb       | intake.name  |
    | ------------ | ------------ |
    | 36.160241918 | Sekoia Agent |
    | 27.997688794 | Zscaler      |
    | 27.989695219 | Zscaler ZIA  |

## Related articles

### Getting Started & Overview
* [SOL Overview](/xdr/features/investigate/sol_overview.md): Sekoia Operating Language overview.
* [SOL Getting Started](/xdr/features/investigate/sol_getting_started.md): This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.
* [SOL Best Practices](/xdr/features/investigate/sol_best_practices.md): Best practices to use SOL effectively.

### User Guides
* [Create and Manage Queries](/xdr/features/investigate/create_manage_queries.md): Create and manage queries using SOL.
* [SOL How-to Guides](/xdr/features/investigate/sol_how_to_guides.md): Learn how to use the main functions of SOL to reach your goals (aggregate data, join tables, use external data, build a query library...).
* [SOL Datasets](/xdr/features/investigate/sol_datasets.md): Discover the CSV import feature that enables SOC analysts to enrich security investigations by importing external data sources directly into the SOL query environment.

### Technical Reference
* [SOL Data Sources Reference](/xdr/features/investigate/sol_ref_datasources.md): Technical references to access security data within the Sekoia platform thanks to SOL.
* [SOL Functions Reference](/xdr/features/investigate/sol_ref_functions.md): Reference article regarding functions used in SOL.
* [SOL Operators Reference](/xdr/features/investigate/sol_ref_operators.md): Reference article regarding operators used in the SOL language.
