# Events Page

The events page enables investigation in the latest events received by SEKOIA.IO using the log list, search bar and filters.

## Log list:

The events page displays a list of latest events received by SEKOIA.IO.

The default columns are:

- Timestamp: Event date
- Event.dialect: Type of intake that sent the event.
- Description: Smart description with clickable links formatted by SEKOIA.IO to show the most important elements and make them easily accessible, such as IP Address, Type or Name.

It is possible to add or remove other columns using the "Show fields" tab by:

- Selecting the desired field in the "Available field" section using the "+" button.
- Selecting the field to remove in "Selected fields" section using the "-" button.
- Typing the desired field name in search bar at the top of "Selected fields".

![SEKOIA.IO Event_page_Log_list](../assets/operation_center/ev_log_list.gif){: style="max-width:600px"}

## Log lines:

Each line of log can be unrolled to show:

- Details: Detailed information retrieved from the log about event once parsed and elements related to the intake and community. These information can be used in the search bar.
- STIX: Event as a STIX bundle that will be used by detection engines.
- Raw event: Event as received by SEKOIA.IO.

![SEKOIA.IO Event_page_Log_lines](../assets/operation_center/ev_log_lines.gif){: style="max-width:600px"}


## Search bar:

You can search among the list of events by using Dork query langage, for which you can find more information [here](../searching/dork.md).

### Filters:

It is possible to use and combine filters in the search bar by using:

- Smart description: By clicking on the "+" button.
- Details: The query is made on the existing fields in the "details" section by clicking on the "+" button for one of the items.

To go back to the list of logs shown, you need to clear filters and select "Current events"

![SEKOIA.IO Event_page_Filters](../assets/operation_center/ev_filters.gif){: style="max-width:600px"}

### Save filters:

It is possible to save a query by clicking on the star icon. The period of time is not conserved with it. 
To check it out, you can click on "Saved queries" then select the wanted period of time and press enter to see the events found.

![SEKOIA.IO Event_page_Save_Filters](../assets/operation_center/ev_save_filters.gif){: style="max-width:600px"}

### Date:

It is possible to select the period of time to be taken in consideration while using a filter:

- Presets: Recommended predefined dates.
- Dates relatives: Earliest and latest moments to select.
- Date ranges: Gap between 2 dates.

Click on the blue lense to start a full search job.

![SEKOIA.IO Event_page_Date](../assets/operation_center/ev_date.gif){: style="max-width:600px"}

### Search history:

Each search result lasts 10 min by default and it is possible to configure the retention to reach 1 day (24 hours). When the result is expired, you still have the possibility of replaying it using the saved relative date or a new one.

![SEKOIA.IO Event_page_Search_History](../assets/operation_center/ev_search_history.gif){: style="max-width:600px"}
