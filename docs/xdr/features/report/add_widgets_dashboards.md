# Configuring Widgets and layout

The practical guide to building your Dashboard: adding Widgets, organizing the layout, and using dynamic Filters.

## Working with Widgets

### Add Widgets
1.  Click the **Add New Widget** button in the top right corner.
2.  Select Widgets from the available **Queries** (custom) or **Presets** (built-in).

### Edit Widgets
Click the **three dots (...)** on a Widget and select **Edit Widget**.
* **Query visualization:** You are redirected to the Query settings page to edit parameters.
* **Preset:** An editing panel appears to adjust options like time range or visualization type.

### Remove Widgets
Click the **three dots (...)** on a Widget and select **Delete from dashboard**.

## Reorganizing the layout

1.  Click the **Edit button** in the top right corner of the screen.
2.  **Move:** Drag and drop Widgets to your preferred locations.
3.  **Resize:** Change the size of each Widget.
4.  Click **Save** to apply changes.

## Using Query Builders

You can insert existing Query Builders into Dashboards to streamline visualization.

* **Synchronization:** Changes made to a Query on the Query Builder page are automatically propagated to all Dashboards using it.
* **Tracking:** On the Query Builder’s edit page, you can view a list of all Dashboards utilizing that specific Query.
* **Visualization:** The Widget utilizes the visualization settings saved within the Query Builder (refer to Query Builders documentation for details).

## Configuring Filters

> !!! Note "Availability"

        Filters are currently released under the Early Access Program.
        
Filters make Dashboards interactive by acting as shared controls that update multiple Widgets instantly.

### Syntax
Filters are dynamic inputs referenced in a SPL query using `?filter_name`.
*Example:* `events | where process.name == ?process_name`

### Pinning Filters
You can "pin" these Filters to the top of the Dashboard so they control all Widgets referencing the same Filter name.

1.  Open the Dashboard and click **Edit dashboard**.
2.  In the Widget's panel, click the **pin icon** next to the Filter you want to pin.
3.  **Save** the Dashboard.

### Behavior
* **Pinned:** The Filter appears in the Dashboard header. Changing it refreshes all linked Widgets.
* **Unpinned:** The Widget retains its own local Filter configuration.

---
**Next steps**
* See the list of available presets in the [Built-in Widgets reference](#).
