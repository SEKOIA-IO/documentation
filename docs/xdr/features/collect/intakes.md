# Intakes
Intakes correspond to data sources sent to Sekoia.io. They are identified by a name, a log format, an entity and an intake key.

You can configure as much intakes as you need in order to increase Sekoia.io knowledge of your infrastructure.

All features related to intakes are visible through the “Intakes” menu on the Operations Center.
## Intakes listing
The intakes homepage allows you to view the list of intakes already created within the community but also to create new intakes.

![intakes_listing](/assets/operation_center/intakes/intakes-listing.png){: style="max-width:100%"}

On this page, you can find:

- The created intakes in your community
- The entity associated with the intake
- The number of events sent to Sekoia.io for the past 7 days
- The number of events in error
- The intake key for each intake that you can copy directly from the table to your clipboard
- The creator as well as the creation date
- A delete button that implies the events produced by the intake will no longer be analyzed



## Create an intake from our integrations catalog
To configure a new source of events in your community, you can rely on our list of continuously growing integrations that are constantly developed and enhanced by Sekoia.io’s team.
![intakes_types](/assets/operation_center/intakes/intakes-types.png){: style="max-width:100%"}

To create an intake, you have to:

1. Click on the `+ Intake` from the Intakes homepage
2. Choose the source of events that suits your needs (you can filter these sources by clicking on the categories’ tags)
3. Click on the `Create` button in the source card
4. Provide an intelligible name
5. Select the entity to which you want to associate the corresponding data
6. Click on `Create`
7. Find your newly created source of events as well as the intake key in the Intakes homepage

![intakes_creation](/assets/operation_center/intakes/modal-intake-creation.png){: style="max-width:100%"}

!!! Note
    The documentation about the integration of your data sources is also available in the [integrations](integrations/index.md) page.

## Configure a notification to report on inactive intake
An inactive intake may have devastating consequences on your security monitoring. To prevent incidents from happening, you can set up notifications to get alerted when an intake stops sending events to Sekoia.io.

To set up your notification, you will have to:

1. Go to the Intakes listing page and click on:  ![Notification logo](/assets/operation_center/intakes/Monitor_intake_logo.png){: style="max-width:10%"} on the right side of the table
2. Specify how long the intake should be inactive before sending a notification. The duration can go from 15 min to 24 hours.
3. Select how you want to be notified. Triggered actions that are available are mentioned in the page [Turn on notifications](/getting_started/notifications-Listing_Creation).

!!! note
     You can also set up this notification from the User Center > Notifications by selecting the trigger `No events are received`.

![Create notification](/assets/operation_center/intakes/Monitor_intake_create_notification.png){: style="max-width:100%"}


## Notification when an intake is not receiving events

You can set a notification when an intake stops receiving events:

- On the Intake's page by clicking on the bell next to the delete button
- On the `Notifications` page of the User Center

![Intakenotification](/assets/operation_center/intakes/2022-12-30_16h35_06.png)

Here is the needed configuration setup:

- Trigger: `No Events are received`
- Period: Period of time when the intake selected did not receive any events
- Intake
- Actions to perform:  Choose a channel where the notification will be sent
- Notification name

## Create a custom intake

To learn more about how to create a custom intake, please refer to this [section.](/../../develop/guides/format/create_a_format.md)

---

!!! note
    Do not hesitate to contact your support if:
    - The settings’ recommendations provided are not sufficient or not applicable to your system. We can then see with you how to transfer your events in the best conditions.
    - The format of the logs you want to send us is not in the list. We regularly add new formats and we can let you know when yours is available in our catalog.
