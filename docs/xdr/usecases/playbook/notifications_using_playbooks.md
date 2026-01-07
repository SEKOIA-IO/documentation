# Send notifications to a Webhook using a playbook

This use case describes how to send a notification to a third party system like Slack or Microsoft Teams using webhooks and a playbook.

## Prerequisites

- A Sekoia.io XDR licence
- The user that configures the Playbook should have a Role that contains:
	* The SYMPHONY permissions
- An API Key with a Role that contains at least the following permission:
	* View alerts
	* View intakes

> To create your API Key, follow this [documentation](../../../getting_started/manage_api_keys.md).

## Create your playbook

Playbook templates were created to ease the process of setting up the playbooks to send the notifications to Slack or Teams. 

To create one, follow these steps: 


- **Go to** the [Playbook page](https://app.sekoia.io/operations/playbooks)
- **Click** on `+ New Playbook`
- If multi-tenant is available, **select** the Community where the Playbook should be executed
- Choose the `Use a template` option 
- Search for `Teams` or `Slack` depending on your needs
- Select the corresponding playbook and click on `Create`

## Configure your playbook

Once your playbook is created, the following configuration steps are required:

- Open each `Sekoia.io` action and select the account that needs to be used to communicate with Sekoia.io APIs. You may have to create an account with the API key you created previously if no account exists.
- Open the `Send to Slack` or `Send to Teams` action and replace the URL with the URL of your webhook

## Customize your notifications

The Slack and Teams playbook templates are provided as examples of notifications that can be sent to these solutions. You can customize the playbooks to suit your needs by adding additional actions to retrieve more data from the alerts and events and add them to the payload sent. 

Keep in mind that the payload must match the format expected by the third parties.

## External references

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [Teams Incoming Webhooks](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)