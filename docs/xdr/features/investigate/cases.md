# Cases

Cases enable you to regroup your investigation findings across multiple perimeters, alerts and analysts and share your results with your end-users in an efficient manner.

You can either create a new case from an existing alert or add alerts to an existing case.

## Cases listing
The listing page lists all the cases across your community.
They can be listed following multiple filters:

- Status (open or closed cases)
- Assigned to or Created by
- Tags associated

You can also sort your cases depending on:

- Last edition (default)
- Creation date
- Priority (`low`, `medium`, `high`)

## Create a case
To create a new case, you can:

1. Open the Cases page
2. Click on `+ Case` button
3. Provide a title and a description (mandatory fields)
4. Select an assignee
5. Define a priority
6. Add tags if needed
7. Click on `Create`

## Edit a case

To edit a case, you just have to click on a case and reach the `edit` button available on the details view.

The case must be open in order to be edited.

## Case details

The Case details page contains multiple elements.

In the header, you can find the name of the case, the person that created it, the last edition date, a tag with the case ID that you can easily copy by clicking on it, the priority and the status.

The different sections of the page are then separated into 5 tabs: `Details`, `Alerts`, `Tasks`, `Events`, and `Graph Investigation`.

### Details tab

The Details tab contains basic information about the case:

- Authors, the community, and the dates of creation and edition of the case
- A description of the case that uses Markdown to enable you to format your text
- A timeline displaying comments

### Alerts tab

The Alerts tab contains a list of alerts that were added to the case.

To add alerts to a case, you can either:

- Use the `Add alerts` button on this tab
!!! tip
    To add multiple alerts to a case, we recommend to either copy the ID of your case found in the case details page then paste it in the search bar. The case will be displayed then you can select it and click on `Add to alerts` button.

- Use the `Add to case` button on the detailed page of any alert
!!! tip
    To add alerts to multiple case, we recommend to copy the ID of your alert found in the alert details page then paste it in the search bar. The alert will be displayed then you can select it OR you can scroll and select all alerts needed and click on `Add to case` button.

### Tasks

The Tasks tab allows you to manage tasks and subtasks associated with the case.

### Events

The Events tab lists the events that are associated with the case in a display similar to the [Events page](events.md).

![events](/assets/operation_center/events-in-case.png){: style="max-width:100%"}

Events associated with the case are:

- Events that raised an alert that was added to the case.
- Events that were [directly added to the case](events.md#adding-events-to-cases).

When interacting with individual values, it is possible to:

- Filter for: only applies to the events associated with the case
- Filter out: only applies to the events associated with the case
- [Search events with this value](#search-events-with-this-value)

The `Value Selection` mode can be toggled with the button at the top right of the event list to select multiple values in displayed events. The selected values can then be used to:

- Create a Sigma Rule
- [Search events with these values](#search-events-with-this-value)

#### Search Events with this value

The "Search Events with this value" feature can be used to perform a search into all events that occurred during the case's timeframe (+- 1 hour).

![search-events](/assets/operation_center/alerts/search-events.png){align=right}

The search query is automatically created from selected values.

To search events with a value:

- On the `case` page, go to `events` tab
- Click on `Toggle value selection` button in the upper right of the logs list
- Select `values` you want to search for by clicking on them in the logs list
- Click on the button `Perform a search` as shown in the screenshot

A side panel opens with the search results, allowing you to investigate a case without leaving the page.

### Graph Investigation

The Graph Investigation Tab is presenting the analyst with a graphical visualization of the Case.

![graph](/assets/operation_center/graph-in-case.png){: style="max-width:100%"}

The following items appear on the graph:

- `Observables`: these are automatically extracted from events (IP addresses, Domain Names, URLs, User Account, etc.)
- `Observable Relationships`: relationships between observables are represented by arrows linking them on the graph. Relationships are extracted from events using the [Smart Description](../collect/intakes.md) definitions
- `CTI Objects`: STIX objects from the Intelligence Center that provide additional context
- `STIX relationships` between Threat Objects

!!!note
    All changes performed inside the Graph Investigation are temporary. A new graph is generated at each visit based on the list of events associated with the case.

**Threat Intelligence**

You can access Threat Intelligence by clicking on any CTI object on the graph. The left panel will display its description and lists all known relationships. Related objects can then be added to the graph to pivot into the Threat Intelligence database.

**Observables**

You can access Observable Details by clicking on any Observable on the graph. The left panel will display all events inside the alert related to this observable, with their “Smart Description”. Full Events can be accessed in the right side panel by clicking on "Full Events". It is also possible to [Search events with this value](#search-events-with-this-value) by clicking on the button next to the name of the observable.
