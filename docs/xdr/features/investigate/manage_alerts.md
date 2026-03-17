# Manage alerts

The Alerts page is the primary interface for monitoring security detections. By default, it displays the last 10 alerts ordered by the most recent.


## Filter the alerts listing

1. Click **Filters** or press `f`.
2. Search for and select a filter (e.g., **Asset**, **Rule**, **Urgency**).
3. Select an operator (e.g., `is`, `is not`, `is any of`).
4. Select the values to apply.

!!! tip "Keyboard shortcuts"
    | Key | Action |
    |---|---|
    | `f` | Open the filter menu |
    | `↑` / `↓` | Navigate lists |
    | `Enter` | Select values |
    | `Esc` | Close the menu |

### Pre-made filters

| Filter | Description |
|---|---|
| **Open** | Status is any of the Open or In Progress stages. |
| **New Today** | Created within the current day. |


## Process alerts in bulk

1. Select alerts using the checkboxes in the list.
2. To select alerts across all pages, click **Select all XX alerts**.
3. Perform one of the following:
   - **Add to case**: Select an existing case or create a new one.
   - **Change status**: Choose a new status and enter a comment to explain the decision.


## Create an alert filter

To prevent known false positives from triggering the same alert:

1. Navigate to the **Events** tab of an alert.
2. Below the graphic, click **Toggle value selection** icon.
3. Select the values in the logs you want to filter.
4. Click **New alert filter**.
5. Enter a **Name** and optional **Description**.
6. Click **Add**.

!!! note
    Select, **Reject the Alert** to automatically reject the current alert after creating the filter.


## Search events with values

To search all events within the alert timeframe (± 1 hour):

1. In the **Events** tab of an alert, click **Toggle value selection**.
2. Select the values you want to search.
3. Click **Perform a search**.
4. A side panel opens with the results.


## Related articles

* [Investigate alerts with Graph](/xdr/features/investigate/investigate_alerts_graph.md): Conduct deep analysis using visual correlation.
* [Alerts](/xdr/features/investigate/alerts.md): Learn about urgency calculation and similarity strategies.
* [Alert interface reference](alert_interface_reference.md): Detailed list of all available filters and table columns.
