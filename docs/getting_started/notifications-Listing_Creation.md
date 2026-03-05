# Create a notification

This procedure explains how to set up a new notification rule to monitor events and receive alerts through your preferred channel(s). 

### Prerequisites

* Access to the community where you want to monitor activities.
* (Optional) Incoming webhook URLs if you plan to integrate with Slack, Teams, or Mattermost.

## Procedure

1.  Navigate to the bottom of the left-hand panel and click **Settings**.
2.  Select the **Notifications** tab.

3.  Click the **+ New notification rule** button.
    !!! note "Initial Setup"
        If no notifications exist, the listing page appears blank with the **+ Notification** button.
4.  Enter a descriptive name in the **Notification name** field.
5.  Select the event category from the **Trigger** drop-down list.
6.  Define specific criteria (such as Alert Status, Urgency, or Involved Asset) in the **Conditions** section.
7.  Select the delivery method in the **Action to perform** section:
    * **In-app notification**: View alerts within the Sekoia.io platform.
    * **Email**: Send a notification to a specific email address.
    * **External Tools**: Select Slack, Teams, or Mattermost or provide a webhook URL.
8.  Click **Save**.

### Result

Your new notification appears in your personal listing. The system begins monitoring for the specified trigger immediately.

??? example "Example: High-Urgency Alert Notification"
    **Problem**: You need to be immediately alerted when a critical asset is involved in a high-priority incident so you can begin remediation.
    
    * **Trigger**: New alert is raised.
    * **Conditions**: 
        * `Urgency` is greater than `80`
        * `Asset name` contains `Production-Database`
    * **Action**: Send an email and a Slack message.
    
    **Result**: Whenever an alert matching these criteria occurs, you receive a direct email and a notification in your designated Slack channel with the alert details.

## Related articles

* [The notification system](/getting_started/notification_concept): Understand the logic and triggers behind the system.
* [Manage notifications](/getting_started/manage_notifications.md): Learn how to update or deactivate existing rules.
* [Notification examples](/getting_started/notifications-Examples.md): Explore more configuration templates.
