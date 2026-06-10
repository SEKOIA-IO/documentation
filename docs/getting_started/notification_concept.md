# The notification system

The Sekoia.io notification system allows you to stay informed about specific activities within your workspace through various channels. By defining triggers and conditions, you ensure that relevant security events reach the right stakeholders immediately.

Notifications function as automated rules that monitor your communities for specific events, such as alert updates or system errors. When an event matches your predefined criteria, the system executes an action, such as sending an email or triggering a message in a third-party application.



## Notification triggers

You can monitor several categories of events within the platform:

* **Alerts**: Creation of new alerts, status updates, or automated case modifications.
* **Intelligence**: New rules added to the Rules Catalog, or rules scheduled for deprecation.
* **Operations**: Playbook execution errors, connector failures, or detection rules entering a rate-limited state.
* **Reporting**: Availability of new reports.
* **Data Ingestion**: Notifications when no events are received for a specific period (intake monitoring).

??? note "Triggers comprehensive list" 
    - A new alert is raised
    - An alert is updated
    - A report is available
    - A new rule is added to the Rules Catalog by Sekoia.io 
    - No events are received 
    - A playbook encountered an error
    - A connector encountered an error
    - A rule from the Rules Catalog is scheduled for deprecation
    - A rule from the Rules Catalog is deprecated
    - An automated case is created
    - An automated case is edited
    - A detection rule entered rate-limited state
    

## Delivery channels

The system supports multiple ways to receive information:

* **In-app**: Notifications appear directly within the Sekoia.io interface.
* **Email**: Direct messages sent to an email address.
* **Messaging Platforms**: Real-time messages sent to Slack, Microsoft Teams, or Mattermost channels.
* **Custom Webhooks**: JSON payloads sent to a specific URL for custom automation.

## Workspace modes

The behavior of notifications depends on your workspace hierarchy:

* **Single-tenant mode**: Notifications apply only to the current workspace.
* **Multi-tenant mode**: Notifications can monitor all managed communities or be restricted to specific ones.

!!! note "User Visibility"

    Notifications are personal. A notification rule is only visible to and manageable by the user who created it within the community where it was created.

## Next steps
* [Create a notification](/getting_started/notifications-Listing_Creation.md): Learn how to set up your first notification rule.
* [Manage notifications](/getting_started/manage_notifications.md): Instructions on editing, disabling, or deleting rules.
* [Notification examples](/getting_started/manage_notifications.md): Practical use cases for common security scenarios.
