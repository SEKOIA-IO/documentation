# Filter and suppress alerts

The Alerts page lets you build complex queries to isolate specific alerts and suppress known false positives directly from event data.

## Filter the alerts listing

1. Click **Filters** or press `f`.
2. Search for and select a filter (e.g., Asset, Rule, Urgency).
3. Select an operator (`is`, `is not`, `is any of`).
4. Select one or more values to apply.

!!! tip
    You can combine multiple filters. The default operator between filters is AND. To edit a filter, click its value or operator and update it directly.

!!! note
    Your filter configuration is saved automatically and persists when you return to the page.

### Keyboard shortcuts

| Key | Action |
|---|---|
| `f` | Open the filter menu |
| `↑` / `↓` | Navigate lists |
| `Enter` | Select a value |
| `Esc` | Close the menu |

### Pre-made filters

| Filter | Description |
|---|---|
| **Open** | Status is any of all statuses in the Open and In Progress stages. |
| **New Today** | Created within the current day. |

### All available filters

| Filter | Description |
|---|---|
| **Asset** | Lists impacted assets within the alert. |
| **Created at** | Date of creation (date range or relative dates). |
| **Entity** | Entities where alerts occurred. |
| **Rule** | Rules that have raised alerts. |
| **Source** | Alert sources. |
| **Status** | All configured alert statuses. |
| **Target** | Alert targets. |
| **Threat** | Threats related to alerts. |
| **Type** | Alert types present in the table. |
| **Updated** | Date of last update (date range or relative dates). |
| **Urgency** | High [75-100], Medium [50-75[, Low [0-50[. |

!!! tip
    To filter by a specific rule, source, or target, hover over a value in the table and click **+** to add it as a filter automatically.

## Create an alert filter

Alert filters prevent known false positives from triggering the same alert in the future. You create them directly from event values in the alert.

!!! note
    By default, **Reject the Alert** is selected to automatically reject the current alert after the filter is created.

1. On the alert page, select the **Events** tab.
2. Click **Toggle value selection** icon.
3. Select the values in the logs you want to filter.
4. Click **Create an alert filter** icon.
5. Enter a **Name** (mandatory) and an optional **Description**.
6. Click **Add**.

![Events tab showing value selection mode and alert filter creation button](/assets/operation_center/alerts/alert-filter.png)

## Related articles

* [Manage alerts](/xdr/features/investigate/manage_alerts.md): Perform bulk actions and status updates on alerts.
* [Alerts](/xdr/features/investigate/alerts.md): Understand the underlying logic of alert similarity and urgency.
* [Alert interface reference](/xdr/features/investigate/alert_interface_reference.md): Detailed lookup for all filter fields and table columns.
