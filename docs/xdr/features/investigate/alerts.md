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

## Alert types and categories
The Alert type is associated with the rule that triggered it but can be changed with the value associated to specific indicators in case of CTI rules.
The Alert type is defined according to a custom set of values derived from the Reference Incident Classification Taxonomy of ENISA.

## Alerts listing
When you first connect to [SEKOIA.IO](http://app.sekoia.io/), the alerts list will display the last 10 alerts raised on your community ordered by Date. 
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

The Tasks tabs lists tasks and subtasks that are associated with the alert. Buttons are available to complete or reject tasks. When completing a task, you are informing the Operations Center that you have undertaken the corresponding action on your perimeter. The urgency of the alert will thereby decrease, as well as the risk indicator.

Subtasks can have an OpenC2 specification which can be displayed by clicking on the automation icon.

### Events

The Events tab lists the events that raised the alert in a display similar to the [Events page](https://docs.sekoia.io/operation_center/events/).

When interacting with individual values, it is possible to:

- Filter for: only applies to the events that raised the alert
- Filter out: only applies to the events that raised the alert
- [Search events with this value](https://docs.sekoia.io/operation_center/alerts/#search-events-with-this-value)

The `Value Selection` mode can be toggled with the button at the top right of the event list in order to select multiple values in displayed events. The selected values can then be used to:

- [Create an Alert Filter](https://docs.sekoia.io/operation_center/alerts/#create-an-alert-filter)
- [Search events with these values](https://docs.sekoia.io/operation_center/alerts/#search-events-with-this-value)

### Create an Alert Filter

Alert Filters can be used to prevent known false positives from raising the same alert in the future.

You can create an Alert Filter for the Rule that triggered the alert easily by selecting multiple values and clicking on the Alert Filter button. The filter's pattern is automatically created from selected values.

By default, "Reject the Alert" is selected to automatically reject the alert after creating the Alert Filter.

### Search Events with this value

The "Search Events with this value" feature can be used to perform a search into all events that occurred during the alert's timeframe (+- 1 hour). The search query is automatically created from selected values. A side panel opens with the search results, allowing to investigate an alert without leaving its page.

### Graph Investigation

The Graph Tab is presenting the analyst with a graphical visualization of the Alert. The following items appear on the graph:

- `Observables`: these are automatically extracted from events (IP addresses, Domain Names, URLs, User Account, etc.)
- `Observable Relationships`: relationships between observables are represented by arrows linking them on the graph. Relationships are extracted from events using the [Smart Description](https://github.com/SEKOIA-IO/Community/tree/main/events) definitions
- `CTI Objects`: STIX objects from the Intelligence Center that provide additional context
- `STIX relationships` between Threat Objects

**Threat Intelligence**

You can access Threat Intelligence by clicking on any CTI object on the graph. The left panel will display its description and lists all known relationships. Related objects can then be added on the graph to pivot into the Threat Intelligence database.

**Observables**

You can access Observable Details by clicking on any Observable on the graph. The left panel will display all events inside the alert related to this observable, with their [Smart Description](https://github.com/SEKOIA-IO/Community/tree/main/events). Full Events can be accessed into the right side panel by clicking on "Full Events". It is also possible to [Search events with this value](https://docs.sekoia.io/operation_center/alerts/#search-events-with-this-value) by clicking on the button next to the name of the observable.
