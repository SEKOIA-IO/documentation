# Query examples

## Join examples

### Join between events and communities tables (for Multi-tenant)

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp > ago(5m)
| limit 100
| lookup communities on sekoiaio.customer.community_uuid == uuid
| select timestamp, sekoiaio.customer.community_uuid, community.name

```
{% endtab %}
{% tab title="Results" %}

| timestamp                | sekoiaio.customer.community_uuid     | community.name     |
| ------------------------ | ------------------------------------ | ------------------- |
| 2026-03-25T15:17:20.357Z | 904df422-adf9-4be8-b2b6-d027c0d68184 | Reynholm Industries |
| 2026-03-25T15:17:57.942Z | 904df422-adf9-4be8-b2b6-d027c0d68184 | Reynholm Industries |
| 2026-03-25T15:17:15.356Z | 904df422-adf9-4be8-b2b6-d027c0d68184 | Reynholm Industries |
{% endtab %}
{% endtabs %}


### Join between events and entities tables

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp > ago(24h)
| limit 100
| aggregate count=count() by sekoiaio.entity.uuid
| lookup entities on sekoiaio.entity.uuid == uuid
| select entity.name, count

```
{% endtab %}
{% tab title="Results" %}

| entity.name        | count     |
| ------------------ | --------- |
| HQ - London Office | 100       |
| Cambridge Campus   | 20        |
{% endtab %}
{% endtabs %}

### Join between alerts and communities tables (for Multi-tenant)

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| aggregate count=count() by community_uuid
| lookup communities on community_uuid == uuid
| select community.name, community_uuid, count
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| community.name                              | community_uuid                       | count     |
| ------------------------------------------- | ------------------------------------ | --------- |
| Reynholm Industries                         | 904df422-adf9-4be8-b2b6-d027c0d68184 | 488       |
| MIT - Massachusetts Institute of Technology | c0540367-9702-46e2-90c3-7ab65ead9a27 | 464       |
{% endtab %}
{% endtabs %}

### Join between alerts and assets tables

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| lookup assets on assets.uuid == uuid
| select short_id, rule_name, asset.name, asset.type
| limit 10

```
{% endtab %}
{% tab title="Results" %}

| short_id     | rule_name                                                     | asset.name      | asset.type |
| ------------ | ------------------------------------------------------------- | --------------- | ---------- |
| ALqUHCbZMbnY | Mshta Suspicious Child Process                                | desktop-4932-vm | host       |
| ALK5mN68LpbB | Mshta Command From A Scheduled Task                           | desktop-4932-vm | host       |
| ALWzDs9pcVVb | CrowdStrike Falcon Intrusion Detection                        | root            | account    |
| ALQbzwMvo1Aj | CrowdStrike Falcon Intrusion Detection Informational Severity | root            | account    |
| ALTwu5cU16LK | PsExec Process                                                | root            | account    |
| ALHGJU7tcoGb | CrowdStrike Falcon Intrusion Detection                        | root            | account    |
| ALqPWeuUow4p | CrowdStrike Falcon Intrusion Detection High Severity          | root            | account    |
{% endtab %}
{% endtabs %}

### Join between events and intake_formats tables

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp between (?time.start .. ?time.end)
| aggregate count() by sekoiaio.intake.dialect_uuid
| lookup intake_formats on sekoiaio.intake.dialect_uuid == uuid
| select intake_format.name, count
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| intake_format.name       |  count      |
| ------------------------ |  ---------  |
| Sekoia.io Endpoint Agent |  9630384    |
| HarfangLab EDR           |  9548402    |
| Zscaler Internet Access  |  19224678   |
{% endtab %}
{% endtabs %}

### Count events per intake format (event_telemetry)

{% tabs %}
{% tab title="Query" %}

``` shell
event_telemetry
| where bucket_start_date between (?time.start .. ?time.end)
| aggregate sum(occurrences) by intake_dialect_uuid
| lookup intake_formats on intake_dialect_uuid == uuid
| select intake_format.name, sum_occurrences
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| intake_format.name       |  sum_occurrences      |
| ------------------------ |  ---------  |
| HarfangLab EDR           |  739676     |
| Sekoia.io Endpoint Agent |  744873     |
| Zscaler Internet Access  |  1475940    |
{% endtab %}
{% endtabs %}

### Data volume per intake format (event_telemetry)

{% tabs %}
{% tab title="Query" %}

``` shell
event_telemetry
| where bucket_start_date between (?time.start .. ?time.end)
| aggregate sum(total_event_size) by intake_dialect_uuid
| lookup intake_formats on intake_dialect_uuid == uuid
| select intake_format.name, sum_total_event_size
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| intake_format.name       |  sum_total_event_size      |
| ------------------------ |  ------------------------  |
| Zscaler Internet Access  |  1475940                   |
| HarfangLab EDR           |  739676                    |
| Sekoia.io Endpoint Agent |  744873                    |
{% endtab %}
{% endtabs %}

### Resolve intake format name from intakes

{% tabs %}
{% tab title="Query" %}

``` shell
intakes
| lookup intake_formats on format_uuid == uuid
| select name, intake_format.name
```
{% endtab %}
{% tab title="Results" %}

| name          |  intake_format.name        |
| ------------- |  ------------------------  |
| Sekoia Agent  |  Sekoia.io Endpoint Agent  |
| Zscaler       |  Zscaler Internet Access   |
| Zscaler ZIA.  |  Zscaler Internet Access   |
{% endtab %}
{% endtabs %}

## Alerts query examples

### Detection rules ranked by number of alerts

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| where created_at > ago(30d)
| aggregate total = sum(occurrences) by rule_name
| top 100 by total

```
{% endtab %}
{% tab title="Results" %}

| rule_name                                    |  total |
| -------------------------------------------- |  ----  |
| SEKOIA Intelligence Feed                     |  132   |
| Suspicious Mshta Execution                   |  82    |
| HarfangLab EDR Critical Level Rule Detection |  58    |
{% endtab %}
{% endtabs %}

### Assets ranked by number of alerts

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| where created_at > ago(30d)
| aggregate count=count() by assets.uuid
| order by count desc
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| assets.uuid                          |  count |
| ------------------------------------ |  ----  |
| 44b54aac-0d06-48aa-bda7-533d73d4e3c4 |  113   |
| c8946c7e-f502-4736-8bf2-f6025b91583a |  50    |
| 0d624ec2-8861-4956-9cf2-4fc6962a47ba |  37    |
{% endtab %}
{% endtabs %}

### Threats ranked by number of alerts

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| where created_at > ago(30d)
| aggregate count=count() by threats.name
| order by count desc
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| threats.name                                     |  count |
| ------------------------------------------------ |  ----  |
| User Execution: Malicious File                   |  52    |
| Command and Scripting Interpreter: PowerShell    |  42    |
| Create or Modify System Process: Windows Service |  42    |
{% endtab %}
{% endtabs %}

### Alerts per detection type

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| where created_at > ago(30d)
| aggregate count() by detection_type

```
{% endtab %}
{% tab title="Results" %}

| detection_type    | count |
| ---------------   | ----- |
| CTI Retrohunt     | 5     |
| Sigma Correlation | 14    |
| Sigma             | 238   |
{% endtab %}
{% endtabs %}

### Average time to detect in last 30 days

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| where created_at > ago(30d)
| aggregate avg(time_to_detect)

```
{% endtab %}
{% tab title="Results" %}

| avg_time_to_detect  |
| ------------------  |
| 1035.6561679790027  |
{% endtab %}
{% endtabs %}

### Rename columns and convert time_to_detect in minutes

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| where time_to_detect != null
| select entity = entity_name, rule = rule_name, ttd = time_to_detect/60
| limit 10

```
{% endtab %}
{% tab title="Results" %}

| entity             | rule                     | ttd                 |
| ------------------ | ------------------------ | ------------------- |
| HQ - London Office | SEKOIA Intelligence Feed | 0.13333333333333333 |
| HQ - London Office | OneNote Embedded File    | 0.13333333333333333 |
| HQ - London Office | SEKOIA Intelligence Feed | 31.733333333333334  |
{% endtab %}
{% endtabs %}

### Ranking of communities by alerts

{% tabs %}
{% tab title="Query" %}

``` shell
alerts
| aggregate AlertCount = count() by community_uuid
| lookup communities on community_uuid == uuid
| order by AlertCount desc
| select community.name, AlertCount

```
{% endtab %}
{% tab title="Results" %}

| community.name                              | AlertCount |
| ------------------------------------------- | ---------- |
| Reynholm Industries                         | 488        |
| MIT - Massachusetts Institute of Technology | 464        |
{% endtab %}
{% endtabs %}



## Assets query examples

### Filter assets with a specific tag

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| where tags.tag in ["Admin"]
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| uuid                                 | community_uuid                       | name          | tags              |
| ------------------------------------ | ------------------------------------ | ------------- | ----------------- |
| ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Admin"}] |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Admin"}] |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | [{"tag":"Admin"}] |
{% endtab %}
{% endtabs %}


### Filter assets with multiple tags

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| where tags.tag in ["Admin", "Backup"]
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| uuid                                 | community_uuid                       | name          | tags               |
| ------------------------------------ | ------------------------------------ | ------------- | ------------------ |
| ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Admin"}]  |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Admin"}]  |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | [{"tag":"Backup"}] |
{% endtab %}
{% endtabs %}


### Search the events of assets with a specific tag

Asset tags are not stored in the events. This query reads them from the `assets` table when it runs, so it uses the current tags, including on the events received before a tag was added.

{% tabs %}
{% tab title="Query" %}

``` shell
let tagged_assets = assets
| where tags.tag in ["Admin"]
| select uuid;

events
| where timestamp > ago(7d)
| where sekoiaio.any_asset.uuid in get_column_values("uuid", tagged_assets)
| select timestamp, sekoiaio.any_asset.name, event.action
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| timestamp                | sekoiaio.any_asset.name         | event.action |
| ------------------------ | ------------------------------- | ------------ |
| 2026-03-25T15:17:20.357Z | ["Maurice Moss","User network"] | opened-file  |
| 2026-03-25T15:16:52.104Z | ["Maurice Moss","User network"] | deleted      |
| 2026-03-25T15:15:43.981Z | ["Roy Trenneman"]               | opened-file  |
{% endtab %}
{% endtabs %}

`sekoiaio.any_asset.name` lists every asset of the event, not only the tagged ones.

{% hint style="info" %}
The tag must be assigned to fewer than 10,000 assets. Beyond that, the query returns partial results with a warning.
{% endhint %}

### Find hosts that no asset connector reports

Hosts seen by Sekoia Asset Discovery and by no configured asset connector, such as an EDR or a CMDB, are candidates for Shadow IT.

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| where type == "host"
  and source == "automatic" // Discovered, not created by a user
  and not connectors.connector_uuid // No connector type UUID: not seen by any configured Asset Connector
| limit 100
```
{% endtab %}
{% endtabs %}

To keep only the hosts that Sekoia Asset Discovery did see:

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| where connectors.uuid == "e0437ab0-5e38-4bd3-b922-c500644889c3" // Seen by Sekoia Asset Discovery (built-in configuration UUID)
  and not connectors.connector_uuid // No connector type UUID: not seen by any configured Asset Connector
| limit 100
```
{% endtab %}
{% endtabs %}

### List all distinct tags

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| distinct tags.tag
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| tags.tag |
| -------- |
| Admin.   |
| Backup   |
| Berlin   |
{% endtab %}
{% endtabs %}


### Filter assets where tag starts with a prefix

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| where tags.tag startswith "Finance"
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| uuid                                 | community_uuid                       | name          | tags                              |
| ------------------------------------ | ------------------------------------ | ------------- | --------------------------------- |
| ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Finance"}]               |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Finance"}]               |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | [{"tag":"VIP"},{"tag":"Finance"}] |
{% endtab %}
{% endtabs %}


### Filter assets where tag contains a string (case-insensitive)

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| where tags.tag contains~ "prod"
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| uuid                                 | community_uuid                       | name          | tags                                                     |
| ------------------------------------ | ------------------------------------ | ------------- | -------------------------------------------------------- |
| ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Tier1"},{"tag":"Production"},{"tag":"Berlin"}]  |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Pre-Prod"}]                                     |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | [{"tag":"Production"}]                                   |
{% endtab %}
{% endtabs %}

### Count assets per tag

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| aggregate count() by tags.tag
| order by count desc
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| tags.tag                                    | count |
| ------------------------------------------- | ----- |
| Local accounts                              | 16    |
| MIT - Massachusetts Institute of Technology | 11    |
{% endtab %}
{% endtabs %}

### Exclude assets with a specific tag

{% tabs %}
{% tab title="Query" %}

``` shell
assets
| where not tags.tag in ["Backup"]
| limit 100
```
{% endtab %}
{% tab title="Results" %}

| uuid                                 | community_uuid                       | name          | tags                                                     |
| ------------------------------------ | ------------------------------------ | ------------- | -------------------------------------------------------- |
| ddfeab36-f6b5-4f31-831e-5566b882dd00 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Maurice Moss  | [{"tag":"Tier1"},{"tag":"Production"},{"tag":"Berlin"}]  |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | Roy Trenneman | [{"tag":"Pre-Prod"}]                                     |
| b1ee47a2-dae2-4a6a-b4fa-ed8a56382f94 | 904df422-adf9-4be8-b2b6-d027c0d68184 | User network  | []                                                       |
{% endtab %}
{% endtabs %}




## Asset risk score query examples

{% hint style="info" %}
`asset_risk_scores` and `asset_risk_score_history` are already scoped to the communities available to the user. To filter results for a specific community, use a lookup on `assets` and filter on `community_uuid`. Filter the `assets` data source before the lookup to avoid the 10,000-row limit on the right side of a lookup.
{% endhint %}

### Top 20 assets with a critical risk score in a specific community

{% tabs %}
{% tab title="Query" %}

``` shell
asset_risk_scores
| lookup (assets | where community_uuid == "<community_uuid>") on asset_uuid == uuid
| top 20 by final_score
```
{% endtab %}
{% endtabs %}

This query returns the 20 assets with the highest current risk score in the specified community.

### Count assets with a critical risk score

{% tabs %}
{% tab title="Query" %}

``` shell
asset_risk_scores
| where final_score >= 75
| aggregate count_distinct(asset_uuid)
```
{% endtab %}
{% endtabs %}

This query counts the assets in the Critical risk band.

### Top 20 assets by risk score

{% tabs %}
{% tab title="Query" %}

``` shell
asset_risk_scores
| top 20 by final_score
```
{% endtab %}
{% endtabs %}

This query returns the 20 assets with the highest current risk score.

### Count assets whose score is mostly driven by recent activity

{% tabs %}
{% tab title="Query" %}

``` shell
asset_risk_scores
| where recent_activity_score > exposure_score
| aggregate count_distinct(asset_uuid)
```
{% endtab %}
{% endtabs %}

This query counts assets for which recent alerts, cases and points of interest contribute more than persistent exposure factors.

### Count assets with a configured criticality and a score above 50

{% tabs %}
{% tab title="Query" %}

``` shell
asset_risk_scores
| where criticality_value > 0 and final_score > 50
| aggregate count_distinct(asset_uuid)
```
{% endtab %}
{% endtabs %}

This query counts assets with a configured criticality and a risk score above 50.

### Count score-affecting events by type

{% tabs %}
{% tab title="Query" %}

``` shell
asset_risk_score_history
| where event_date > ago(7d)
| aggregate event_count = count() by type
| order by event_count desc
```
{% endtab %}
{% endtabs %}

This query counts the events that affected asset risk scores during the last seven days, grouped by event type.

### Top 20 assets by alerts and cases

{% tabs %}
{% tab title="Query" %}

``` shell
asset_risk_score_history
| where event_date > ago(30d) and type in ["alert", "case"]
| aggregate event_count = count_distinct(event_uuid) by asset_uuid
| top 20 by event_count
```
{% endtab %}
{% endtabs %}

This query returns the 20 assets with the highest number of distinct alerts and cases contributing to their risk history during the last 30 days. The history can contain several entries for the same alert or case as its contribution decays over time, so `count_distinct(event_uuid)` counts source alerts and cases rather than history entries.

### List criticality changes

{% tabs %}
{% tab title="Query" %}

``` shell
asset_risk_score_history
| where type == "criticality" and event_date > ago(30d)
| order by event_date desc
```
{% endtab %}
{% endtabs %}

This query lists criticality changes recorded during the last 30 days, starting with the most recent event.

{% hint style="info" %}
`asset_risk_scores` contains the current score only. Use `asset_risk_score_history` to analyze the events that affected the score or the risk trajectory.
{% endhint %}

{% hint style="info" %}
Rows older than 90 days are deleted daily from `asset_risk_score_history`. For each asset and event type, the latest `hygiene` and `criticality` entry older than 90 days is retained for baseline reconstruction.
{% endhint %}

{% hint style="warning" %}
`final_score` can be empty on newly created history rows until the next score recomputation.
{% endhint %}

## Events query examples

### Number of unique command lines per host.name

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp > ago(24h)
| aggregate count=count_distinct(process.command_line) by host.name
| order by count desc
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| host.name        | count |
| ---------------- | ----- |
| laptop-6a1ec62f  | 16    |
| laptop-chris     | 525   |
| laptop-b3205bc2  | 517   |
{% endtab %}
{% endtabs %}

### Number of unique hostname per month

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp > ago(90d)
| aggregate count=count_distinct(log.hostname) by month(timestamp)

```
{% endtab %}
{% tab title="Results" %}

| timestamp_month  | count |
| ---------------- | ----- |
| 2026-03          | 63    |
{% endtab %}
{% endtabs %}

### Top 10 visited URL

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp >= ago(24h)
| aggregate count() by url.domain
| top 10 by count

```
{% endtab %}
{% tab title="Results" %}

| url.domain           | count |
| -------------------- | ----- |
| clients2.google.com  | 2088  |
| www.deloitte.com     | 2040  |
| www.squarespace.com  | 2010  |
{% endtab %}
{% endtabs %}


### Top 10 blocked URL

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp >= ago(24h) and event.action == 'blocked' and user.name != null and url.domain != null
| aggregate count() by url.domain
| top 10 by count

```
{% endtab %}
{% tab title="Results" %}

| url.domain      | count |
| --------------- | ----- |
| www.amazon.fr   | 1044  |
| www.myfritz.net | 1040  |
| www.uol.com.br  | 1021  |
{% endtab %}
{% endtabs %}

### Top 10 login failures on Windows

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp > ago(24h) and event.code == 4625
| aggregate failed_login_count=count() by user.target.name
| top 10 by failed_login_count

```
{% endtab %}
{% tab title="Results" %}

| user.target.name  | failed_login_count |
| ----------------- | ------------------ |
| barbara_liskov    | 204                |
| ken_thompson      | 202                |
| geoffrey_hinton   | 188                |
{% endtab %}
{% endtabs %}

### Sekoia.io endpoint agents per version

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp >= ago(24h)
| where sekoiaio.intake.dialect == 'sekoia.io endpoint agent'
| where event.action == 'stats'
| aggregate count_distinct(agent.id) by agent.version

```
{% endtab %}
{% tab title="Results" %}

| agent.version                                    | count_distinct_agent.id |
| ------------------------------------------------ | ----------------------- |
| v1.9.0+62292d9c63d80859269661252cfc84db4ff66d81  | 304                     |
{% endtab %}
{% endtabs %}


### List unique user.name

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp >= ago(24h)
| distinct(user.name)
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| user.name    |
| ------------ |
| SYSTEM       |
| a_borg       |
| ada_lovelace |
{% endtab %}
{% endtabs %}

### Number of events per IP address

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp > ago(30d)
| aggregate count=count() by client.ip
| order by count desc
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| client.ip       | count |
| --------------- | ----- |
| 192.168.2.10    | 204   |
| 192.168.2.22    | 202   |
| 192.168.2.100   | 188   |
{% endtab %}
{% endtabs %}


### Aggregate events by source.ip and action.outcome

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp >= ago(24h) and event.category == 'authentication'
| aggregate count() by source.ip, action.outcome
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| source.ip | action.outcome | count |
| ----------| -------------- | ----- |
| 1.0.0.95  | failure        | 33    |
| 1.0.0.95  | success        | 142   |
| 1.5.178.82  | failure      | 24    |
| 1.5.178.82  | success      | 136   |
{% endtab %}
{% endtabs %}


### Events where process.name starts with 'chrome'

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp > ago(24h) and process.name startswith('chrome')
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| timestamp                                    |  dialect     | smart description |
| -------------------------------------------- |  ----------  | ----------------- |
| 2026-03-26T15:35:14.738Z                     |  Sekoia      | Text              |
| 2026-03-26T15:35:03.740Z                     |  Sekoia      | Text              |
| 2026-03-26T15:35:04.539Z                     |  Sekoia.     | Text              |
{% endtab %}
{% endtabs %}


### Events of specific intake

{% tabs %}
{% tab title="Query" %}

``` shell
let intake_uuids = intakes | where name == '<intake name>' | distinct uuid;

events
| where timestamp >= ago(24h)
| where sekoiaio.intake.uuid in intake_uuids
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| timestamp                                    |  dialect     | smart description |
| -------------------------------------------- |  ----------  | ----------------- |
| 2026-03-26T15:35:14.738Z                     |  HarfangLab  | Text              |
| 2026-03-26T15:35:03.740Z                     |  HarfangLab  | Text              |
| 2026-03-26T15:35:04.539Z                     |  HarfangLab  | Text              |
{% endtab %}
{% endtabs %}


### Number of defended assets: unique host.name with more than 10 events during 2 weeks in the last 30 days

{% tabs %}
{% tab title="Query" %}

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
{% endtab %}
{% tab title="Results" %}

| host.name       | total_count |
| --------------- | ----------- |
| desktop_awk     | 359626      |
| desktop_neural  | 358417      |
| laptop_coursera | 358319      |
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Please note: the `select` command can also be used. `select` and `project` are aliases and both return the same results.
{% endhint %}

### host.os.type per Sekoia endpoint agent

{% tabs %}
{% tab title="Query" %}

``` shell
events
| where timestamp >= ago(24h)
| where sekoiaio.intake.dialect == 'sekoia.io endpoint agent'
| aggregate count() by host.os.type
| limit 100

```
{% endtab %}
{% tab title="Results" %}

| host.os.type    | count  |
| --------------- | ------ |
| windows         | 590720 |
{% endtab %}
{% endtabs %}


### Received Kbytes per month per intake

{% tabs %}
{% tab title="Query" %}

``` shell
event_telemetry
| where bucket_start_date >= ago(30d)
| aggregate sum_bytes = sum(total_message_size) by intake_uuid
| lookup intakes on intake_uuid == uuid
| select sum_gb = sum_bytes / (1000*1000*1000), intake.name
| order by sum_gb desc

```
{% endtab %}
{% tab title="Results" %}

| sum_gb       | intake.name  |
| ------------ | ------------ |
| 36.160241918 | Sekoia Agent |
| 27.997688794 | Zscaler      |
| 27.989695219 | Zscaler ZIA  |
{% endtab %}
{% endtabs %}

## Asset applications query examples

{% hint style="info" %}
Removed applications stay in `asset_applications` with `deleted_at` set. Add `isnull(deleted_at)` to query installed applications only.
{% endhint %}

### Count assets with unsigned applications

{% tabs %}
{% tab title="Query" %}

``` shell
asset_applications
| where signed == false and isnull(deleted_at)
| aggregate count_distinct(asset_uuid)
```
{% endtab %}
{% endtabs %}

This query counts the assets with at least one unsigned application installed.

### Top 20 most widespread applications

{% tabs %}
{% tab title="Query" %}

``` shell
asset_applications
| where isnull(deleted_at)
| aggregate asset_count = count_distinct(asset_uuid) by name, version
| top 20 by asset_count
```
{% endtab %}
{% endtabs %}

This query returns the 20 applications and versions installed on the most assets.

### Versions of an application across assets

{% tabs %}
{% tab title="Query" %}

``` shell
asset_applications
| where name == "Google Chrome" and isnull(deleted_at)
| aggregate asset_count = count_distinct(asset_uuid) by version
| order by asset_count desc
```
{% endtab %}
{% endtabs %}

This query shows how many assets run each version of an application, to spot outdated versions.

### Top 20 publishers

{% tabs %}
{% tab title="Query" %}

``` shell
asset_applications
| where isnull(deleted_at)
| aggregate asset_count = count_distinct(asset_uuid) by publisher
| top 20 by asset_count
```
{% endtab %}
{% endtabs %}

This query returns the 20 publishers whose applications are installed on the most assets.

### Applications recently seen for the first time

{% tabs %}
{% tab title="Query" %}

``` shell
asset_applications
| where created_at > ago(7d) and isnull(deleted_at)
| aggregate asset_count = count_distinct(asset_uuid) by name, publisher
| top 20 by asset_count
```
{% endtab %}
{% endtabs %}

This query returns the applications first recorded during the last seven days. `created_at` is the date Sekoia first saw the application, use `install_date` for the date reported by the asset.

### Applications removed during the last 7 days

{% tabs %}
{% tab title="Query" %}

``` shell
asset_applications
| where deleted_at > ago(7d)
| lookup assets on asset_uuid == uuid
| select asset.name, name, version, deleted_at
| order by deleted_at desc
```
{% endtab %}
{% endtabs %}

This query lists the applications removed from assets during the last seven days, with the asset name.

## Related articles

### Getting Started & Overview
* [SOL Overview](sol_overview.md): Sekoia Operating Language overview.
* [SOL Getting Started](sol_getting_started.md): This tutorial walks you through writing your first SOL queries. By the end, you'll be able to search events, filter results, and save queries for reuse.
* [SOL Best Practices](sol_best_practices.md): Best practices to use SOL effectively.

### User Guides
* [Create and Manage Queries](create_manage_queries.md): Create and manage queries using SOL.
* [SOL How-to Guides](sol_how_to_guides.md): Learn how to use the main functions of SOL to reach your goals (aggregate data, join tables, use external data, build a query library...).
* [SOL Datasets](sol_datasets.md): Discover the CSV import feature that enables SOC analysts to enrich security investigations by importing external data sources directly into the SOL query environment.

### Technical Reference
* [SOL Data Sources Reference](sol_ref_datasources.md): Technical references to access security data within the Sekoia platform thanks to SOL.
* [SOL Functions Reference](sol_ref_functions.md): Reference article regarding functions used in SOL.
* [SOL Operators Reference](sol_ref_operators.md): Reference article regarding operators used in the SOL language.
