
# Notifications

Stay updated on your workspace's latest activities by setting up notifications for multiple features. 

## What notifications can do

Notifications, accessible through the main menu or Settings, allow you to:

- Focus on specific events such as: 
    - A new alert is raised
    - An alert is updated
    - A report is available
    - A new rule is added to the Rules Catalog by Sekoia.io 
    - No events are received 
    - A playbook encountered an error
    - A connector encoutered an error
    - A rule from the Rules Catalog is scheduled for deprecation
    - A rule from the Rules Catalog is deprecated
    - An automated case is created
    - An automated case is edited
    - A detection rule entered rate-limited state

- Add specific conditions: 
    - Focus on the name, reference, pattern, source, intake...

- In a multi-tenant setup, specify if the notification applies to all your communities or specific ones 
- Configure actions such as sending an email or displaying an in-app notification

This documentation provides detailed information on the Sekoia.io notifications mechanism.

## Notifications Listing

If no notifications are set up in your community, the listing page will be blank with a highlighted `+ New Notification` button for creating new notifications.

Once notifications are created, you can edit, duplicate, delete, and (de)activate them from the main Notification page in the Settings. You can also search and filter notifications by trigger type or action type.

!!! Warning
    Each notification is only visible to the user who created it and within the community where it was created.

You can access your in-app notifications from the main navigation. 

## Create a new notification

**Single-tenant mode**: Notifications apply only to the current workspace.

**Multi-tenant mode**: By default, notifications come from all communities, but you can choose to receive notifications from a specific community.

1. Go to Settings > Notifications > `+ New notification`
1. Choose the event and conditions that will trigger your notification rule (e.g., new or existing alerts)
2. Set conditions like alert status, urgency, and involved asset
3. Decide on actions like in-app notifications, emails, texts via webhooks, or Mattermost channels
4. Give your notification a name
5. Save your settings

## Example notification criteria

New alert status is `Ongoing`
Alert urgency is `higher than 80`
Involved asset is `My Critical Asset`

Other examples can be found in [this section of the documentation](notifications-Examples.md). 
