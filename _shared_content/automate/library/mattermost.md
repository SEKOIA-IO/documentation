# Mattermost



[Mattermost](https://mattermost.com/) is a secure, open and flexible collaboration platform

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| hook_url | string | URL of the mattermost incoming webhook |








## Actions

### Post SEKOIA.IO Alert

Post alert to Mattermost



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| alert_uuid | string | The Unique identifier of the alert |
| channel | string | The channel the message posts in. Use the channel’s name and not the display name, e.g. use town-square, not Town Square. |
| api_key | string | The SEKOIA.IO API-Key to read the alert content. |
| base_url | string | Base URL of SEKOIA.IO api (e.g. https://api.sekoia.io/). |
| pretext | string | An optional line of text that will be shown above the alert |









### Post Message

Post message to Mattermost



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| message | string | The message to post |
| channel | string | The channel the message posts in. Use the channel’s name and not the display name, e.g. use town-square, not Town Square. |
| username | string | Overrides the username the message posts as. |














## Extra

Module **Mattermost v.1.11**