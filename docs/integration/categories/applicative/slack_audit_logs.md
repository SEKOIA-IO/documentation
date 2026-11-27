uuid: b3aa9d39-7bbe-46fe-bdc8-f91f0d1ce2ac
name: Slack Audit Logs
type: intake

## Overview

Slack is a channel-based messaging platform where teams, tools and external partners collaborate in shared workspaces, administered together as an Enterprise Grid organization.

Slack audit logs represent the activities performed on the organization, such as logins, file accesses, application installations, channel changes and role changes.

- **Vendor**: Slack
- **Supported environment**: SaaS
- **Detection based on**: Audit
- **Supported application or feature**:
    - Audit Logs

## Configure

### Pre-requisite

To setup the integration, you need:

- A Slack organization on an `Enterprise Grid` plan. The Audit Logs API is only available on this plan.
- The credentials of an `Owner` of the Enterprise organization. Apps requesting the `auditlogs:read` scope must be installed by the Owner of the organization.

### Create the Slack app

1. Log in to [Slack API](https://api.slack.com/apps) as the Owner of the Enterprise organization
2. Click `Create New App`, then `From scratch`
3. Type a name for the app. e.g: Sekoia.io Audit Logs
4. Select a workspace of your organization and click `Create App`
5. Go to `OAuth & Permissions` and, in the `Bot Token Scopes` section, add the `team:read` scope. This scope is required to make the app installable on the organization
6. In the `User Token Scopes` section, add the `auditlogs:read` scope

### Install the app on the organization

1. Go to `Org Level Apps`, click `Opt-In`, then confirm with `Yes, Opt-in`
2. Go back to `OAuth & Permissions` and, in the `OAuth Tokens` section, click `Install to Organization`
3. Check that the app is installed on the Enterprise organization, not on an individual workspace, and click `Allow`
4. Copy the `User OAuth Token`. It starts with `xoxp-`

!!! note
    The Audit Logs API rate limit is 50 calls per minute for the whole organization, shared with your other Slack apps. Lower the `Ratelimit Per Minute` setting of the intake if other applications call this API.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format **Slack Audit Logs**.

When configuring the connector, provide the following information:

- **Token**: the `User OAuth Token` copied above
- **Base Url**: the base URL of the Slack Audit Logs API (default `https://api.slack.com/audit/v1`)

The other settings are optional:

- **Frequency**: seconds to wait between two collections of new events (default 60)
- **Limit**: maximum number of events fetched per request to Slack (default 1000, Slack caps this at 9999)
- **Ratelimit Per Minute**: maximum requests sent to Slack per minute (default 30)
- **Timebuffer**: seconds to wait before collecting a new event, so that events published with a delay by Slack are not missed (default 60)
- **Lookback Seconds**: how far back in time the very first collection goes (default 3600). It is ignored once the connector has collected at least once
- **Excluded Actions**: [Slack actions](https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference) to drop instead of forwarding, e.g. `file_downloaded`. An action added here stops being collected and cannot be recovered later

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

### Further Readings

- [Slack Audit Logs API documentation](https://docs.slack.dev/admins/audit-logs-api/)
- [Slack Audit Logs API methods & actions reference](https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference)
- [Slack organization-ready apps documentation](https://docs.slack.dev/enterprise/organization-ready-apps)
