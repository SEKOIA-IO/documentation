# Playbooks

## Overview

Playbooks provide a **step-by-step approach** to **orchestration**, helping security teams establish standardized **incident response processes** and ensuring the steps are followed in **compliance** with regulatory frameworks. They will also improve your response time on any security alerts.

In Sekoia.io, playbooks play a huge role in automating repetitive tasks to relieve analysts’ daily work, enriching alerts by soliciting external sources, fetching indicators from outside and interconnecting with external systems like ticketing tools for example.

Because they are highly configurable, Sekoia.io’s playbooks supervise and execute response actions to be in line with your business and operational objectives.

---

In this documentation, you will learn how to:

- Configure your profile to efficiently use playbooks
- Set up your playbooks using templates
- Create a playbook from scratch
- Learn more about the different types of triggers, operators and actions
- Troubleshoot with playbook runs
- Create a `Meta-playbook` that works across many communities

## Prerequisites

### Necessary roles

To have access to playbooks, you will need to have the role `Symphony Operator`.

Here is the list of permissions that constitutes this role:

| Permission name | Description |
| --- | --- |
| SYMPHONY_READ_MODULES | List and get Symphony Modules |
| SYMPHONY_READ_PLAYBOOKS | List and get Symphony Playbooks |
| SYMPHONY_READ_PLAYBOOK_RUNS | List and get Symphony Playbook Runs |
| SYMPHONY_READ_PLAYBOOK_RUNS_STATS | List and get statistics about Symphony Playbook Runs |
| SYMPHONY_WRITE_PLAYBOOKS | Write Symphony Playbooks |
| SYMPHONY_WRITE_PLAYBOOK_RUNS | Modify Symphony Playbook Runs |

If you need to attribute this role to someone, go to Your Account settings > Managed Communities > The user in question > `+ Role` > Select `Symphony Operator`.

To learn more about how to attribute roles within your community, please refer to this [section.](../../../getting_started/manage_users.md)

!!! note
    Depending on which app you’ll be creating playbooks for, you might need to have additional permissions linked to each app (Intelligence Center or Operations Center).

**Example**

To create playbooks for your XDR, you will need to have the role `OC_viewer` or `OC_admin` in addition to `Symphony Operator`.

### Generate API Key

To be able to use playbooks, an API Key with the right settings is needed for the Module Configuration to work.

To generate this API Key:

1. Go to Account Settings > Managed Communities > API Keys > `+ API Key`
2. Provide a name and a description (both are mandatory)
3. Select necessary roles for your API Key, depending on if you are looking to automate operations or intelligence tasks
4. Save and copy the value of the API Key in your vault (or any safe place)
5. Paste your API Key in the Module Configuration of your playbook actions

!!! note
    Beware, the generated API Key will no longer be accessible after you’ve closed the modal.

To learn more about how to generate and revoke API keys, please refer to this [section.](../../../getting_started/manage_api_keys.md)
