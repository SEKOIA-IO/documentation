# Notification examples

## Triggers

### Intakes 

Set up notifications to alert you when an intake stops sending events. This ensures you are promptly informed of any disruptions.

1. Select the trigger `No events are received` 
2. Choose the intake you want to monitor 
3. Specify the duration of inactivity that will trigger the notification, ranging from 15 minutes to 24 hours

### Rules Catalog 

Stay updated on changes in the Rules Catalog by triggering notifications when new rules are added by Sekoia.io. Customize these notifications for more granular updates.

1. Choose the New rule added trigger
2. Specify conditions such as: Name, Description, Pattern and Severity levels 
3. Combine multiple conditions within a single notification rule for precise alerts

### New reports 

Stay informed when new reports are added to the platform by Sekoia. Whether you're interested in all new FLINT reports or just specific TLP Amber reports, you can customize your notifications to keep you updated.

1. Select "A report is available" as the trigger 
2. Specify conditions such as: Name, description, threat, sector, country, TLP, confidence levels, and if it's a FLINT or not
3. Combine multiple conditions within a single notification rule for more precise reports 

### Alerts

Stay informed when alerts are raised or updated on the platform. Customize your notifications to ensure you are promptly alerted to significant changes and updates.

#### Alerts raised

When a new alert is raised, you can set up notifications based on the following conditions:

- Assets: Monitor alerts related to specific assets
- Entities: Track alerts associated with particular entities
- Triggering rule: Receive notifications for alerts triggered by specific rules
- Urgency level: Set conditions based on the urgency level of the alert
- Alert status: Be informed about alerts with specific statuses (e.g., new, ongoing)
- Asset criticality: Focus on alerts concerning assets with defined criticality levels

#### Alerts updated

For alerts that are updated, customize your notifications with these conditions:

- Recurrence: Get notified on recurring alerts
- Assets: Monitor updates related to specific assets
- Entities: Track updates associated with particular entities
- Triggering rule: Receive notifications for updates triggered by specific rules
- Urgency level: Set conditions based on the updated urgency level of the alert
- Alert status: Be informed about changes in alert status
- Asset criticality: Focus on updates concerning assets with defined criticality levels

By setting up these conditions, you can ensure that you receive timely and relevant notifications about alerts that are most important to your operations.

### Playbooks 

The "A playbook has encountered an error" trigger allows you to stay informed about issues within your playbooks.

- If this trigger is selected alone, you will receive a notification for every error encountered by a playbook in your community, regardless of whether the error causes the playbook to crash.

- If you want to be notified only when a playbook encounters an error that also causes it to crash, select the "And it crashed" condition in addition to the error trigger.

By configuring these triggers, you can ensure that you are promptly alerted to both minor issues and critical failures within your playbooks, allowing for timely troubleshooting and resolution.


## Conditions 

After setting up your conditions, you need to choose the actions that will be triggered by the notification mechanism. You can enable one or more actions for each notification rule. For example, you can decide to send an email and post a message on a Mattermost channel.

### Sekoia.io in-app notification

The Notification action allows you to send in-app notifications that will be available across Sekoia.io. These notifications can be accessed from the `Notifications` entry in the menu. You just click on it and it will open the notification panel to view all notifications.


### Email Notification

The Email notification will let you send an e-mail to a specified address with two different options:

- By default, simple notification content will be sent with a link to Sekoia.io page corresponding of the Condition(s) set up
- If you enable the `Enrich email with contextual infos` toggle, the email will include more detailed contextual information related to your alert.

!!! Warning 
    Each email recipient can receive up to 10 emails per hour for each notification rule.

### Mattermost Notification

Mattermost is a popular professional chat service. The Mattermost Notification action allows you to send messages to any Mattermost instance. To set this up, you'll need to configure a new Incoming Webhook on your Mattermost instance and specify the Mattermost channel where the message should be sent.

You can refer to the Mattermost documentation on how to [create a new Mattermost “incoming webhook”](https://developers.mattermost.com/integrate/webhooks/incoming/).

### Teams and Slack Notifications 

You can now send notifications directly to your Teams or Slack channels, making it easy to keep your team informed about important activity.

1. Navigate to **Settings** > **Notifications** from the main menu
2. Click the **"Create new notification"** button
3. Choose the **event** or **metric** you want to receive an alert for
4. In the **"Actions to perform"** section, select **Teams** or **Slack** from the dropdown menu
5. Paste your incoming webhook URL into the field provided
6. Click **Save** to activate the notification

Once saved, any future notifications triggered by your selected event or metric will automatically be sent to the designated Teams or Slack channel.

#### Finding Your Webhook URL

If you don't know where to find your webhook URL, here are the official guides for each platform:

- **Teams:** [Create incoming webhooks](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)
- **Slack:** [Sending messages using Incoming Webhooks](https://api.slack.com/messaging/webhooks)

### WebHook Notification

The WebHook Notification allows you to send messages to interact with third-party software. Technical information related to the event will be pushed to an HTTP server, which can then interpret the received payload and take further actions. For example, the server could retrieve more information about the event using Sekoia.io APIs and then push a notification to an internal messaging service.


!!! info 
    You cannot use the WebHook notification mechanism to push information directly to third-party services like Slack or Telegram. Instead, use an intermediate server to handle the data. Solutions like IFTTT or a custom HTTP server can facilitate this process (Examples can be found below). 

    There are also playbook templates that can be used to send notifications to Slack or Microsoft Teams directly using Webhooks. See how to [send notifications to a Webhook using a playbook](../xdr/usecases/playbook/notifications_using_playbooks.md) for more information.

#### Example of a WebHook notification 

Here’s an example of a posted content to a configured destination via the WebHook mechanism:

```json
{
  "type": "alert",
  "action": "created",
  "attributes": {
    "uuid": "5696845f-9ecf-4431-9f0f-48ee0ee2eff1",
    "short_id": "ALEY4fqz8moo"
  },
  "metadata": {
    "version": 2,
    "created_at": "2022-01-14T15:06:57.398005+00:00",
    "community_uuid": "d6cea089-0f36-46c4-a10a-0e4c2e20fb10",
    "avatar_uuid": null,
    "user_uuid": null,
    "permissions": []
  }
}
```

This payload is about a newly `_created_ _alert_` which concerns the `d6cea089-0f36-46c4-a10a-0e4c2e20fb10` community and which identifier is `ALEY4fqz8moo` (or `5696845f-9ecf-4431-9f0f-48ee0ee2eff1` if you prefer the UUID form).

Here's the description of the payload fields description:

| Payload title             | Availability   | Description                                                                                            |
|---------------------------|----------------|--------------------------------------------------------------------------------------------------------|
| `type`                    | Always         | Event type, can be `alert` or `content-proposal` (for reports). More types will be added in the future |
| `action`                  | Always         | Action that took place, can be `created`, `updated`, `deleted`.                                        |
| `metadata`                | Always         | This object contains information around the event itself                                               |
| `metadata.version`        | Always         | Version of the event, WebHook events are currently at version 2.                                       |
| `metadata.created`        | Always         | Date of creation of the _event_.                                                                       |
| `metadata.community_uuid` | Always         | Community concerned by the event.                                                                      |
| `metadata.avatar_uuid`    | Always         | Event that concerns only a single member of a community (not used for alerts or reports).              |
| `metadata.user_uuid`      | Always         | Event that concerns only a single user of Sekoia.io.                                                   |
| `metadata.permissions`    | Always         | Unused.                                                                                                |
| `attributes.uuid`         | Alert specific | Unique identifier of the alert (UUID). Can be used to talk to the Alert API.                           |
| `attributes.short_id`     | Alert specific | Human readable alert unique identifier.                                                                 |


Now, let’s say that you want to post a notification to your internal Microsoft Teams messaging system when a new alert is raised. To do so, you have to:

- Configure a small HTTP server that will receive the payload
- It will then talk to Sekoia.io’s Alert API to retrieve more information about the alert itself (its title, its urgency, etc.)
- The final message is computed and pushed to Microsoft Teams via their incoming WebHook system

Here’s an example of an HTTP server written in Python and FastAPI:

```python title="main.py"
"""Sample notification handler for Sekoia.io WebHook Notifications.

Sample FastAPI application that is in charge of receiving WebHook events from Sekoia.io’s Notification mechanism, enrich event by talking to Sekoia.io’s Alert API and then to push a notification to Microsoft Teams, via an incoming WebHook.

"""

from datetime import datetime
from typing import Literal, Optional

import httpx
from fastapi import BackgroundTasks, FastAPI
from pydantic.v1 import BaseModel, BaseSettings


class WebHookSettings(BaseSettings): # (4)
    apikey: str
    teams_webhook_url: Optional[str] = None


class SEKOIAIOWebHookAlertAttributes(BaseModel):
    uuid: str
    short_id: str


class SEKOIAIOWebHookMetadata(BaseModel):
    version: int = 2
    created_at: datetime
    community_uuid: str
    avatar_uuid: Optional[str] = None
    user_uuid: Optional[str] = None
    permissions: Optional[list[str]] = None


class SEKOIAIOWebHookEvent(BaseModel): # (5)
    type: Literal["alert"]
    action: str
    attributes: SEKOIAIOWebHookAlertAttributes
    metadata: SEKOIAIOWebHookMetadata


app = FastAPI()
settings = WebHookSettings()


async def push_notification_to_teams(event: SEKOIAIOWebHookEvent):
    """Simple task that will extract the retrieve the full alert via
    Sekoia.io API and then creates a message that will be posted on
    Microsoft Teams via a predefined incoming WebHook.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get( # (2)
            f"https://api.sekoia.io/v1/sic/alerts/{event.attributes.uuid}",
            params={"stix": False},
            headers={"Authorization": f"Bearer {settings.apikey}"},
        )
        if response.status_code == 200:
            alert = response.json()
            message = (
                f"A new alert “{alert['title']}” was created on Sekoia.io with "
                "status “{alert['status']['name']}” and “{alert['urgency']['display']}” severity."
            )
            if settings.teams_webhook_url:
                client.post(settings.teams_webhook_url, json={"text": message}) # (3)


@app.post("/hooks/67a7472b-b43c-415d-b1ce-c135fb1dfb0e") # (1)
async def handle_new_alert(
    event: SEKOIAIOWebHookEvent, background_tasks: BackgroundTasks
):
    background_tasks.add_task(push_notification_to_teams, event)
```

1. Entrypoint of our HTTP server that receives Sekoia.io WebHook notifications. Please define a unique URL, using and UUID for example.
2. Code in charge of collecting more information on the alert itself by talking to Sekoia.io APIs.
3. Send the final text message to Microsoft Teams.
4. Environment variables that needs to be defined to let the server work.
5. Base model that will be used to parse incoming events (this version only handles alerts).

Now, you have to [create a new API Key in Sekoia.io](manage_api_keys.md). That one should have at least the right to read alerts (`SIC_READ_ALERT` permissions).

Then you have to install requirements and start the HTTP server with the appropriate environment variables:

```bash
python -m venv venv
source venv/bin/activate # (1)

pip install "fastapi[uvicorn]" "uvicorn[classic]" "httpx" # (2)

export APIKEY="eyJ0eXAiOiJ…" # (3)
export TEAMS_WEBHOOK_URL="https://…"

poetry run uvicorn main:app # (4)

ngrok http 8000 # (5)
```

1. Create a Python virtual environment to install our code
2. Install requirements
3. Export environment variables
4. Start the server
5. Use ngrok to provide access to your local code (development only)

Finally, you can configure Sekoia.io’s WebHook notification to push events to your HTTP server on the following URL: `https://ad76-2a01-cb08-8b87-5600-777f-e748-9e82-49c2.ngrok.io/hooks/67a7472b-b43c-415d-b1ce-c135fb1dfb0e`.
