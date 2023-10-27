
## Overview

To stay informed about the latest activities on your community, you can set up notifications and get alerts each time a new alert pops up or a new report is online.

Notifications Rules, accessible through the User Center or the contextual menu, will let you:

- Focus on specific Sekoia.io events (Operations Center alerts and Intelligence Center reports)
- Add precise conditions
- Configure actions to be triggered (send an e-mail, display a notification in Sekoia.io, …)

This documentation will let you go deeper into [Sekoia.io](http://sekoia.io/)’s notifications mechanism.

## Notifications listing

When there are no notifications set up in your community, the listing page will be blank. A `+ new notification` button is highlighted as you can start creating your notification from there.

Once you have some notifications created, each notification can be modified, duplicated, deleted and (de)activated from the main Notification page in the User Center.

You can also search and filter your notifications from this page.

You can filter by type of trigger or type of actions.

!!! Warning
    Each notification is exclusively visible to the user who configured it AND within the community where it was created.

## Create a new notification

Notifications only apply to the community and the application you are in. Once configured, these notifications will only be visible to the user who created them.

### Operations Center Notifications

To write a new notification rule in the Operations Center, you first have to:

1. Select an `event` and `conditions` that will trigger your notification rule. You can configure your notification rule to be triggered on `alerts` (that can be either new or already existing)
2. Choose one or multiple `conditions` amongst multiple options (alert status, its urgency, asset concerned by the alert, etc.)

For example, you can decide to trigger a notification when the following criteria are met:

- Status of the new alert is `Ongoing`
- Urgency of the new alert is `higher than 80`
- Involved asset is `My Critical Asset`
3. Select `actions` that you want to see performed. You can choose multiple options: get an in-app notification, receive an email, send texts using webhooks or in a Mattermost channel
4. Give your notification a `name`
5. Save your changes


### Intelligence Center Notifications

You can configure your notification rule to be triggered when a new `report` is merged in Sekoia.io’s Intelligence Center.

To do so, you have to:

1. Select an `event` and `conditions` that will trigger your notification rule. You can configure your notification rule to be triggered on `reports being added`
2. Choose one or multiple `conditions` amongst multiple options (name, description, refers to, sector, country, TLP, FLINT, confidence level…)

For example, you can decide to trigger a notification when the following criteria are met:

- It refers to the malware `Cobalt Strike`
- It concerns the country `France`
3. Select `actions` that you want to see performed. You can choose multiple options: get an in-app notification, receive an email, send texts using webhooks or in a Mattermost channel
4. Give your notification a `name`
5. Save your changes


### Playbooks notifications

The "A playbook has encountered an error" trigger, if selected alone, will send a notification for each error encountered by a playbook in your community, whether or not this error causes the playbook to crash.

If you wish to be notified only if the playbook encounters an error *and* crashed, you can select the "And crashed" condition.

