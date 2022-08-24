# Alerts
Alerts are created by the Operations Center when an event matches a rule and a threat is detected.
## Concepts
### Alert Status and lifecycle

An alert can have five possible statuses:

| Status | Description | Possible actions to do |
| --- | --- | --- |
| **Pending** | As soon as an alert is triggered, it is placed in 'Pending' status. If the generation mode for this alert is 'Automatic', this status changes automatically to 'Ongoing'. | Acknowledge, Reject, Validate |
| **Acknowledged** | This status is used when an analysis is ongoing. If the analyst can decide if an alert is a true or a false positive quickly, this status can be optional, time to acknowledge used in statistics will be set to time to change to Ongoing or Rejected status. | Validate, Reject |
| **Ongoing** | Alert is considered as true positive and countermeasures have not yet been applied. This status is the first one seen in case of automatic mode. | Close (countermeasures have been applied, no more alert), Reject (after more analysis, this alert was a false positive) |
| **Closed** | All necessary actions have been applied to the alert. This status is a final status. | No action accepted |
| **Rejected** | The alert was a false positive. This status is a final status. |  No action accepted |

### Alerts Workflow
![alert_workflow](/assets/operation_center/alerts/alert_workflow.png){: style="max-width:100%"}

### Alert Urgency
The Urgency is a number used to give a score to the risk associated with a specific alert.
It is calculated from the severity of a rule and the criticality of assets related to the alert.
This gives a value between 1 (very low risk) and 100 (very high risk).

The urgency of an alert is calculated using the following formula:
`Alert urgency = (Severity of the rule + Criticality of the asset) / 2`

The urgency can have two different representations on the interface: a numerical and a textual representation.

| Display | Value |
| --- | --- |
| Low | [0-20[ |
| Moderate | [20-40[ |
| High | [40-60[ |
| Major | [60-80[ |
| Urgent | [80-100] |

### Alert Similarity 
Alert similarity (Occurence) is the process by which we collect similar events in the same alert. 
The information is available in the Alerts table → Column `Occurrence`. 


**Example**

If an alert has 24 occurrences, it means that it contains 24 events that were classified as similar and put in the same alert. 

### Similarity strategies
Alerts are considered similar if a list of fields defined by the similarity strategy have the same values for all events. Some fields may also be grouped together to specify that their values may be swapped.
There are three possibilities to define the similarity strategy to use. By order:  

1. [Similarity is forced by the rule](#similarity-by-rule)
2. [Similarity is forced by event](#similarity-by-event)
3. [Similarity by default](#default-similarity)

#### Similarity by rule

Rules written by SEKOIA.IO and available in the Rules Catalog may define specific similarity strategies.

Similarity strategies by rule are not shown and cannot be edited on the interface. The API may be used to access this parameter.


#### Similarity by event

Depending on the events that triggered an alert, SEKOIA.IO applies a similarity logic. This logic follows SEKOIA.IO guidelines and cannot be edited by users directly.

If the event matches one of the conditions listed below, the associated similarity strategy is used.

| Conditions | Similarity Strategy |
| --- | --- |
| If `dns.question.name` exists | [`sekoiaio.entity.uuid`, [`source.ip`, `destination.ip`], `dns.question.name`] |
| If `event.dialect` is Azure Windows and `user.name` exists | [`sekoiaio.entity.uuid`, `user.name`, `user.id`] |
| If `event.dialect` is Azure Windows and `process.name` exists | [`sekoiaio.entity.uuid`, `process.name`, `process.command_line`] |
| If `event.dialect` is Azure Active Directory and `user.name` exists and `action.name` exists  | [`sekoiaio.entity.uuid`, `user.name`, `user.id`, `action.name`, `action.type`, `action.outcome`] |
| If `event.dialect` is Azure Active Directory and `action.name` exists | [`sekoiaio.entity.uuid`, `action.name`, `action.type`, `action.outcome`] |
| If `event.dialect` is postfix | [`sekoiaio.entity.uuid`, `email.from.address`] |
| If `file.hash.sha256`matches the rule | [`sekoiaio.entity.uuid`, `file.hash.sha256`] |
| If `file.hash.sha1` matches the rule | [`sekoiaio.entity.uuid`, `file.hash.sha1`] |
| If `file.hash.md5`matches the rule | [`sekoiaio.entity.uuid`, `file.hash.md5`] |

!!!note
    In case similarity forced by your events does not answer your needs, feel free to contact us at support@sekoia.io.

#### Default similarity

If there is no similarity forced by the rule or by the event, you can rely on SEKOIA.IO default similarity formula: same `entity`, same `source.ip` and `destination.ip`. 

`source.ip` and `destination.ip` can be used interchangeably. 

!!! important 
    When there is no data due to parsing issues, alert similarity is not shown except when there is a NULL propriety in `source.ip` or `destination.ip`. When the `source.ip` and the `destination.ip` are empty, we might use the value NULL as a similarity basis.
    
#### Similarity and alert status
As long as there is an existing similar alert with status **Pending**, **Acknowledged** or **Ongoing**, new matches are added to the alert as occurrences.

If only **Closed** or **Rejected** alerts are similar, a new alert is created. **Closed** and **Rejected** similar alerts are listed inside the [Similar Alerts](#similar-alerts) tab.
## Alert types and categories
The Alert type is associated with the rule that triggered it but can be changed with the value associated to specific indicators in case of CTI rules.
The Alert type is defined according to a custom set of values derived from the Reference Incident Classification Taxonomy of ENISA.
![alert_categories](/assets/operation_center/alerts/alert_categories.png){: style="max-width:100%"}

## Alerts listing
When you first connect to [SEKOIA.IO](http://app.sekoia.io/), the alerts list will display the last 10 alerts raised on your community ordered by Date.
![alert_listing](/assets/operation_center/alerts/alert_listing.png){: style="max-width:100%"}

From the left to the right, 7 features are available on the top screen:

- A `refresh` button to show the newly generated alerts
- Two tabs: `All` to list all alerts and `New today` to list today’s alerts
- A `show/hide` columns button that lets you display fields you’re interested in. You can select or deselect columns but also drag and drop them depending on the order you need
- `filters`that let you display alerts by order of Most Frequent, Recently Updated, Recently Created or Most Urgent
- Filters that let you display alerts by `status` Status: Pending, Acknowledged, Ongoing, Rejected or Closed
- Advanced filters capacities: Date range, Entity, Urgency, Type, Rule, Asset, Threats, Source and Target.

On the main alert listing, it is also possible to:

- Select multiple alerts in the same time, then choose and apply a massive change of status
- Filter all rules with the same Rule Name
- Get more information on the related threats by clicking on it, so you should be redirected on the Intelligence Center focused on this specific Threat

By default, the alert listing displays the following information (more information on the meaning of these fields is provided after the Alert Details section):

- A `Selector` so you can perform an action on multiple alerts on the same time
- A `Similarity` counter, showing the alert was raised multiple time for the same reason, rather than simply adding a new line on the alert feed
- Alert creation `Date`
- Alert `Status`. When hovering over the icon, a frame indicates the status modification date and who modified it
- The `Entity` to which the alert corresponds
- `Urgency` of the alert, between 0 and 100, 100 being the highest
- The `Type` of alert
- The `Name` of the rule which triggered the alert
- The `Threats` related to the alert in termes of malicious activities, related tools, Campaign...
- A `first seen` and `last seen`date
- The `ID` and the `UUID` of the alert
- The `source` and `target`of the alert

> Your custom configuration will be saved in order to allow you to keep your selected filters when you come back to this page.
>
> For Partners, an additional filter is available in order to display all or a subset of alerts related to its managed communities.
>
> The alert listing also displays the Communities related to the alerts.

## Alert details

The Alert Details page can be reached by clicking on any alert in the Alert Listing. This will provide you with a new view for quick and deep investigations.

![alert_details](/assets/operation_center/alerts/alert-detail-layout.png){: style="max-width:100%"}


The Alert Details header contains the `urgency`, the `name` and the `short ID` of the alert, as well as the following actions:

- `Alert Status`: can be used to move the Alert through its lifecycle
- Add to `Case`: add the alert to a case to gather all the needed information for an extensive investigation
- `Playbooks`: display the list of on-demand playbooks and be able to trigger them

The different sections of the page are then separated into 4 tabs: `Details`, `Tasks`, `Events` and `Graph Investigation`.

### Details

The Details tab contains the information needed to understand what the alert is about and why it was raised. It’s split into two columns.

The first column contains the following items:

- The detailed alert urgency (can be edited on hover)
- The alert type
- The impacted assets
- The impacted entity
- Related cases (cases in which this alert appears)
- The Kill Chain phase (can be edited on hover)
- Details about the rule that was triggered
- Details from the Intelligence Center about all threats linked to this alert

The second column is the `timeline`. It contains all items that constitute the history of the alert:

- Alert status changes
- Comments (that can be added with the button at the top right)
- Events represented by their Smart Descriptions
- Completed Tasks
- Rejected Tasks

It is possible to filter the timeline to display only items of a certain type.

### Tasks

The Tasks tabs lists tasks and subtasks that are associated with the alert.
![tasks](/assets/operation_center/alerts/alert-tasks.png){: style="max-width:100%"}

Buttons are available to complete or reject tasks. When completing a task, you are informing the Operations Center that you have undertaken the corresponding action on your perimeter. The urgency of the alert will thereby decrease, as well as the risk indicator.

Subtasks can have an OpenC2 specification which can be displayed by clicking on the automation icon.

### Similar alerts

Operators need as much information as possible to determine what to do with a new alert. With the similar alerts tab, SEKOIA.IO has that information in store and is able to display it to the operator in a comprehensive and useful way, while also providing recommendations based on the previous operator decisions.

To find similar alerts linked to a specific alert, you will need to access the detail page dedicated to this alert. The similar alerts tab will be automatically loaded next to the [Details](#details), [Tasks](#tasks), [Graph Investigation](#graph-investigation) and [Events](#events) tabs.

![similar_alerts](/assets/operation_center/alerts/similar_alerts.png){: style="max-width:100%"}

To help you compare between alerts, you can choose which columns you want to display in the table by clicking on the icon in the upper right of the table.

!!! tip
    You can click on the alerts to see the full details of a similar alert or open several of them in new tabs to compare them more easily.

The similar alerts tab is divided into two parts:

- **The suggestion message:** In a callout, you’ll find a text that reminds you of the status of the majority of previous similar alerts. This message suggests you change the alert status based on the previous alerts. You can also find an action button to apply the status on your alert (except for Closed alerts).
- **The similar alerts table:** It gathers all the similar alerts that previously occurred. The columns of this table can be customized to help you investigate the similarities between alerts.


!!! note
    Please note that if SEKOIA.IO doesn’t find previous similar alerts, a message will be displayed to notify you.

### Events

The Events tab lists the events that raised the alert in a display similar to the [Events page](events.md).

![events](/assets/operation_center/alerts/alert-events.png){: style="max-width:100%"}

When interacting with individual values, it is possible to:

- Filter for: only applies to the events that raised the alert
- Filter out: only applies to the events that raised the alert
- [Search events with this value](#search-events-with-this-value)

The `Value Selection` mode can be toggled with the button at the top right of the event list in order to select multiple values in displayed events. The selected values can then be used to:

- [Create an Alert Filter](#create-an-alert-filter)
- [Search events with these values](#search-events-with-this-value)

#### Create an Alert Filter

Alert Filters can be used to prevent known false positives from raising the same alert in the future.

![alert-filter](/assets/operation_center/alerts/alert-filter.png){align=right}

You can create an Alert Filter for the rule that triggered the alert by following these steps: 

- On the `alert`page, go to `events` tab 
- Click on `Toggle value selection` button in the upper right of the logs list
- Select `values` you want to filter by clicking on them in the logs list
- Click on the button `Create an Alert filter` as shown in the screenshot
- As the modal appears, fill in the `name` of the alert filter (mandatory)
- Provide a `description` (optional)
- The filter's pattern is automatically created from selected values.
- Click on `Add` to add this alert filter to the rule that triggered this alert

!!!note 
    By default, `Reject the Alert` is selected by default to automatically reject the alert after creating the Alert Filter.


#### Search Events with this value

The "Search Events with this value" feature can be used to perform a search into all events that occurred during the alert's timeframe (+- 1 hour).

![search-events](/assets/operation_center/alerts/search-events.png){align=right}

The search query is automatically created from selected values. 

To search events with a value: 

- On the `alert`page, go to `events` tab 
- Click on `Toggle value selection` button in the upper right of the logs list
- Select `values` you want to search for by clicking on them in the logs list
- Click on the button `Perform a search` as shown in the screenshot

A side panel opens with the search results, allowing you to investigate an alert without leaving the page.

### Graph Investigation

The Graph Tab is presenting the analyst with a graphical visualization of the Alert.

![graph](/assets/operation_center/alerts/alert-graph.png){: style="max-width:100%"}

The following items appear on the graph:

- `Observables`: these are automatically extracted from events (IP addresses, Domain Names, URLs, User Account, etc.)
- `Observable Relationships`: relationships between observables are represented by arrows linking them on the graph. Relationships are extracted from events using the [Smart Description](https://github.com/SEKOIA-IO/Community/tree/main/events) definitions
- `CTI Objects`: STIX objects from the Intelligence Center that provide additional context
- `STIX relationships` between Threat Objects

**Threat Intelligence**

You can access Threat Intelligence by clicking on any CTI object on the graph. The left panel will display its description and lists all known relationships. Related objects can then be added on the graph to pivot into the Threat Intelligence database.

**Observables**

You can access Observable Details by clicking on any Observable on the graph. The left panel will display all events inside the alert related to this observable, with their “Smart Description”. Full Events can be accessed into the right side panel by clicking on "Full Events". It is also possible to [Search events with this value](#search-events-with-this-value) by clicking on the button next to the name of the observable.
