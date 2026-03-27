The Subscriptions page is a dedicated section within Sekoia designed to provide community admins with a comprehensive overview of their subscriptions. 

From there, they can easily track active and inactive subscriptions, allocate subscriptions to specific communities, and manage trial periods for newly created communities. 

To access the Subscriptions page, the pre-requisites are:

- Admins, analysts and guests can have access to the page
- Only `Admin roles` can allocate trial and subscriptions 
- Permissions: Read community licenses, Manage community licenses

## Single-tenant communities

The subscription page will show the following information:

- Current subscriptions
- Expired subscriptions

Admins can view a comprehensive list of all active subscriptions across their community. They can monitor the status of subscriptions, including:

- The type of plan (e.g., Defend Core, Defend Prime, Intelligence).
- Key properties such as the subscription period, region, number of defended assets, and retention durations.
- The remaining days of their subscription

They can also compare the different plans of Sekoia by clicking on `Compare plans` and contact our teams using the button `Contact us`.

## MSSP (multi-tenant) communities

From the workspace, it is possible to access the current subscription for the workspace as well as have an overview of all your community subscriptions. 

The double navigation allows for a quick overview of all communities. This listing includes the name of the community as well as the status of the subscription. A red icon shows that the community has no active subscription. 

The subscription page will show the following information:

- Current subscriptions
- Expired subscriptions

Admins can view a comprehensive list of all active subscriptions across their community. They can monitor the status of subscriptions, including:

- The type of plan (e.g., Defend Core, Defend Prime, Intelligence).
- Key properties such as the subscription period, region, number of defended assets, and retention durations.
- The remaining days of their subscription

They can also compare the different plans of Sekoia by clicking on `Compare plans` and contact our teams using the button `Contact us`.

### Community subscriptions overview

From the workspace, admins can have a quick overview of all their managed communities subscriptions. 

They can: 

- See the list of all communities and their subscriptions
- Filter by: Trial, nearly expired, not active
- Search for a specific community using the search bar

## Allocate trial subscription

A **trial** is a temporary subscription that allows users to access the platform's features and functionalities for a limited time, without any financial commitment. In Sekoia, the trial subscription offered is for a duration of **45 days**.

- **Duration**: 45 days
- **Plan**: Defend Prime
- **Number of assets**: Up to 1000 assets
- **Hot storage**: 7 days
- **Archiving duration**: 0 days

When creating a new community, a trial subscription is **automatically made available**.

## Subscription notifications

Sekoia automatically sends email notifications to inform administrators about key events in the subscription lifecycle, 
such as upcoming expirations or expired licenses.

The system evaluates notifications through scheduled daily processes. With the exception of manual operations, Sekoia does not process subscription status changes or notifications in real-time.

Only users with the Admin role receive subscription-related email notifications.

### Expired license

When a subscription expires, Sekoia sends an email to the administrators of the affected community to inform them that the license is inactive.
The system checks for license expiration daily at 02:00 (UTC). If the system detects an expired license during this check, it automatically sends the notification.

### Nearly expired license

To help administrators anticipate subscription renewals, Sekoia notifies them when a license is approaching its expiration date.

These notifications are evaluated daily, around 08:00 UTC, based on the license duration and on the administrator scope.
Sekoia currently supports two notification channels for nearly expired licenses:

* **email notifications**
* **in-app banners**, displayed at the top of the application

The in-app banner is shown on the same day as the email notification.

**Workspace**

Workspace admins receive a notification when at least one managed community has a subscription close to expiration:

* **Long-term licenses:** If the license duration is greater than 100 days, the notification is sent when the license expires in less than 90 days.
* **Short-term licenses:**: If the license duration is 100 days or less, the notification is sent when the license expires in less than 10 days.

These notifications provide a consolidated view of upcoming expirations across all managed communities.

**Community**

Community admins receive a notification when their community subscription is close to expiration:

* **Long-term licenses:** If the license duration is greater than 100 days, the notification is sent when the license expires in less than 30 days.
* **Short-term licenses:** If the license duration is 100 days or less, the notification is sent when the license expires in less than 5 days.

### In-app banner behavior

When a nearly expired license notification is triggered, Sekoia can also display an in-app banner at the top of the application.

The banner is displayed only to:

* community admins of communities with a nearly expired license
* workspace admins of workspaces containing one or more communities with a nearly expired license

Users can dismiss the banner from the interface. This dismissal is temporary:

* the banner stays hidden until the next daily recomputation
* if the license is still nearly expired after recomputation, the banner is displayed again the next day

This behavior ensures repeated visibility until the situation is resolved, while allowing users to temporarily hide the message.

### Notification schedule

| Event                      | Recipient        | Condition                                      | Evaluation time (UTC) |
| -------------------------- | ---------------- | ---------------------------------------------- | --------------------- |
| License expired            | Community admins | License end date reached                       | Daily at 02:00        |
| Nearly expired (workspace) | Workspace admins | < 90 days (or < 10 days if license ≤ 100 days) | Daily ~08:00          |
| Nearly expired (community) | Community admins | < 30 days (or < 5 days if license ≤ 100 days)  | Daily ~08:00          |

