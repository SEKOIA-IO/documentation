# Alerts Management

Alerts are created by the Operation Center when any threat is detected (when an event matches a rule).

## Concepts

### Alert Status and lifecycle

There is five possible statuses for an alert:

- **Pending**: As soon as an alert is triggered, it is placed in 'Pending' status. If the generation mode for this alert is 'Automatic', this status changes automatically to 'Ongoing'. In other cases, the following actions are accepted: Acknowledge, Reject, Validate.
- **Acknowledged**: This status is used when an analysis is ongoing. If the analyst can decide if an alert is a true or a false positive quickly, this status can be optional, time to acknowledge used in statistics will be set to time to change to Ongoing or Rejected status.The following actions are accepted: Validate, Reject.
- **Ongoing**: Alert is considered as true positive and countermeasures are not yet been applied. This status is the first one seen in case of automatic mode. The following actions are accepted: Close (countermeasures have been applied, no more alert), Reject (after more analysis, this alert was a false positive).
- **Closed**: Every necessary actions have been applied for the alert. This status is a final status, no action accepted.
- **Rejected**: The alert was a false positive. This status is a final status, no action accepted.

![Alert Workflow](../assets/operation_center/alert_workflow.png)

### Alert Urgency

The Urgency is a number used to give a score to the risk associated with a specific alert. It is calculated from the severity of a rule and the criticality of assets related to the alert.
This gives a value between 1 (very low risk) and 100 (very high risk).
The urgency is provided under two different representations on alert detail: a numerical and a textual representation.

| Display  |  Value   |
| :------: | :------: |
|   Low    |  [0-20[  |
| Moderate | [20-40[  |
|   High   | [40-60[  |
|  Major   | [60-80[  |
|  Urgent  | [80-100] |

### Alert Types and Categories

The Alert Type is associated with the rule, but can be changed with the value associated to specific indicators in case of CTI rules.

The Alert Type is defined according to a custom set of values derived from theReference Incident Classification Taxonomy of ENISA:

- abusive-usage
  - bandwidth-download
  - bandwidth-upload
  - p2p
  - high-drop
- abusive-content
  - spam
  - harmfull-speech
  - violence
- malicious-code
  - virus
  - worm
  - trojan
  - spyware
  - dialer
  - rootkit
  - malware
  - botnet-drone
  - ransomware
  - malware-configuration
  - c&c
- information-gathering
  - scanner
  - sniffing
  - social-engineering
  - portscan
  - sweepscan
  - appscan
- intrusion-attempts
  - ids-alert
  - brute-force
  - exploit
- intrusions
  - privileged-account-compromise
  - unprivileged-account-compromise
  - application-compromise
  - bot
  - defacement
  - compromised
  - backdoor
- availability
  - dos
  - ddos
  - sabotage
  - outage
- information-content-security
  - Unauthorised-information-access
  - Unauthorised-information-modification
- fraud
  - unauthorized-use-of-resources
  - copyright
  - masquerade
  - phishing
- vulnerable
  - vulnerable-service
- other
  - blacklist
  - unknown
  - other
- test
  - test

## Alert List

When you first connect to SEKOIA.IO, alerts list is filtered and will diplay 'New today' alerts and sorted in descending order of urgency. The sort and filter choices you make from this list will be kept thereafter.

On this screen, you can view the following information:

- Alert Id, begin with AL followed by 10 alphanumeric characters. On the top right of the ID box, there may be an yellow round with a number, it's the similarity counter.
- Alert creation date
- Alert status. When hovering over the icon, a frame indicates the status modification date and who modified it.
- The entity to which the alert corresponds
- Urgency of the alert, between 0 and 100, 100 being the highest.
- The category and sub-category of alerts
- The name of the rule which triggered the alert
- The source and destination IP when event is a network event.

Alerts can be filtered by two ways: a rapid filter on the top left of the list and a list of cumulative filtering criteria on the top right of the screen.

![Alert List](../assets/operation_center/alert_list.gif)

## Alert Details

The Alert Details can be reached by clicking on the line of any alert in the Alert List.

![Alert Details Headers](../assets/operation_center/alert_details/top.png)

The Alert Details header contains the Urgency, the Name and the Alert's Short ID as well as the following actions:

- Alert Status: can be used to move the Alert through its lifecycle
- Add to Case
- Playbooks: display the list of on-demand playbooks and be able to trigger them

The different sections of the page are then separated into 4 tabs: Details, Tasks, Events and Graph.

### Details

The Details tab contains the information needed to understand what the alert is about and why it was raised. It is split into two columns.

The first column contains the following items:

- The detailed alert urgency
- The alert type
- The impacted assets
- The impacted entity
- Related cases (cases in which this alert appears)
- The Kill Chain phase
- Details about the rule that was triggered
- Details from the Intelligence Center about all threats linked to this alert

The urgency and kill chain phase can be edited on hover.

![Alert Details Details](../assets/operation_center/alert_details/details.png)

The second column is the timeline. It contains all items that constitute the history of the alert:

- Alert status changes
- Comments, that can be added with the button at the top right
- Events represented by their Smart Descriptions
- Completed Tasks
- Rejected Tasks

It is possible to filter the timeline to display only items of a certain type.

![Alert Details Timeline](../assets/operation_center/alert_details/timeline.png)

### Tasks

![Alert Details Tasks](../assets/operation_center/alert_details/tasks.png)

The Tasks tabs lists tasks and subtasks that are associated with the alert. Buttons are available to complete or reject tasks. When completing a task, you are informing the Operation Center that you have undertaken the corresponding action on your perimeter. The urgency of the alert will thereby decrease, as well as the risk indicator.

Subtasks can have an OpenC2 specification which can be displayed by clicking on the automation icon.

### Events

![Alert Details Tasks](../assets/operation_center/alert_details/events.png)

The Events tab lists the events that raised the alert in a display similar to the [Events page](../events.md).

When interracting with individual values, it is possible to:

- Filter for: only applies to the events that raised the alert
- Filter out: only applies to the events that raised the alert
- [Search events with this value](#search-events-with-this-value)

The "Value Selection" mode can be toggled with the button at the top right of the event list in order to select multiple values in displayed events. The selected values can then be used to:

- [Create and Alert Filter](#create-an-alert-filter)
- [Search events with these values](#search-events-with-this-value)

#### Create an Alert Filter

Alert Filters can be used to prevent known false positives from raising the same alert in the future.

You can create an Alert Filter for the Rule that triggered the alert easily by selecting multiple values and clicking on the Alert Filter button. The filter's pattern is automatically created from selected values.

By default, "Reject the Alert" is selected to automatically reject the alert after creating the Alert Filter.

![Create an Alert Filter](../assets/operation_center/alert_details/alert_filter.gif)

#### Search Events with this value

The "Search Events with this value" feature can be used to perform a search into all events that occured during the alert's timeframe (+- 1 hour). The search query is automatically created from selected values. A side panel opens with the search results, allowing to investigate an alert without leaving its page.

![Search Events with this value](../assets/operation_center/alert_details/search_events_with_this_value.gif)

### Graph

The Graph Tab is presenting the analyst with a graphical visualisation of the Alert. The following items appear on the graph:

- Observables: these are automatically extracted from events (IP addresses, Domain Names, URLs, User Account, etc.).
- Observable Relationships: relationships between observables are represented by arrows linking them on the graph. Relationships are extracted from events using the [Smart Description](https://github.com/SEKOIA-IO/Community/tree/main/events) definitions.
- CTI Objects: STIX objects from the Intelligence Center that provide additional context.
- STIX relationships between Threat Objects.

#### Threat Intelligence

You can access Threat Intelligence by clicking on any CTI object on the graph. The left panel will display its description and let you list its known relationships. Related objects can then be added on the graph to pivot into the Threat Intelligence database.

![Threat Intelligence](../assets/operation_center/alert_details/threat_intelligence.png)

#### Observables

You can access Observable Details by clicking on any Observable on the graph. The left panel will display all events inside the alert related to this observable, with their [Smart Description](https://github.com/SEKOIA-IO/Community/tree/main/events). Full Events can be accessed into the right side panel by clicking on "Full Events". It is also possible to [Search events with this value](#search-events-with-this-value) by clicking on the button next to the observable's name.

![Threat Intelligence](../assets/operation_center/alert_details/observable_details.png)
