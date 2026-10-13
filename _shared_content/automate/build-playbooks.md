# Build playbooks

A playbook starts with a trigger, can include conditions and consists of a succession of actions. This article explains how to create a playbook, then build its workflow from a template or from scratch.

## Create a playbook

To create a playbook:

1. Navigate to **Playbooks**.
2. Click **New playbook**.

The new playbook opens in the **Workflow** tab. In a multi-tenant community, you first choose the communities of the playbook. See [Meta-playbook creation](#meta-playbook-creation).

An empty playbook offers two ways to start:

- **Start from a template**: pick a ready-made playbook from the Playbooks Catalog.
- **Add a trigger** or **Add an action**: build the workflow block by block.

![Empty playbook with the Start from a template, Add a trigger and Add an action cards](/assets/operation_center/playbooks/playbook_empty_state.png){: style="max-width:100%"}

!!! tip "Playbook name"
    A new playbook is named "New playbook". If you start it with **Start from a template**, **Add a trigger** or **Add an action**, the playbook takes the name of the template or module you select, followed by the name of its community, for example "Enrich alerts with VirusTotal - Acme". The community name is not added to a meta-playbook that runs on several communities. A module added directly from the module menu does not rename the playbook.

    To rename the playbook, click the edit icon next to its name in the playbook header, enter the new name, then click **Save**.

## Start from a template

Creating a playbook from scratch can be complex. Templates give you a working base that you can customize.

To start from a template:

1. On an empty playbook, click **Start from a template**.
2. In **Select a template from our Playbooks Catalog**, search for a template or click a tag to filter the list.
3. Select a template to preview its workflow.
4. Click **Use this template**.

![Select a template from our Playbooks Catalog window](/assets/operation_center/playbooks/playbook_template_picker.png){: style="max-width:100%"}

The workflow of the template fills the graph area. Configure the accounts and settings of each block before you activate the playbook.

The Playbook Templates' Catalog is being updated frequently by our analysts and here’s a list of the main ones. All playbook templates are available in the public repo on [Github](https://github.com/SEKOIA-IO/Community/tree/main/playbooks/templates) and our users are encouraged to add new templates to the repo.

### Operations Center templates

| Category | Name | Description |
| --- | --- | --- |
| Alerts, Notifications, Webhook | Mail Webhook notification on alert | Send an email about an alert when receiving a webhook event |
| Alerts, Notifications, Webhook | Mattermost notification on alert | Notify by mattermost when new alerts are created |
| Alerts, Webhook | Qualify Internet Scan webhook | Qualify an Internet scan alert on webhook |
| Alerts | Playbook adware | Automatic validation of alerts with predefined adware domains |
| Alerts | Alert urgency to 0 when rejected | Put the urgency of an alert to 0 when it is rejected |
| Alerts, Enrichment | Enrich alerts with VirusTotal | Enrich alerts with VirusTotal informations |
| Alert, cron | Reject old alerts (1 year) | Reject old alerts not updated for 1 year. |
| Alert, Webhook, enrichment | Enrich with IKnowWhatYouDownload | Enrich with IKnowWhatYouDownload to check if the IP is known from this service, directly from Sekoia.io. |
| Alerts, TheHive | Automatically create an alert on TheHive | Automatically create an alert on TheHive when a new alert is raised in Sekoia.io. |
| Alerts, TheHive | Manually create an Alert on TheHive | Create an alert on TheHive via the alert page. |
| Alerts, Notifications | Slack notification on alert | Notify by Slack when new alerts are created. If the target is defined, it is used in the notification, otherwise the hostnames from events are used. |
| Alerts, Enrichment | Enrich alerts with AbuseIPDB | Enrich with AbuseIPDB to check if the IP is known from this service, directly from Sekoia.io. |
| Alerts, Enrichment | Alerts Enrichment Shodan Playbook | Enrich with Shodan to check if the IP is known from this service, directly from Sekoia.io. |
| Alerts, OSINT | Fetch alerts from Digital Shadows SearchLight | Synchronise alerts from Digital Shadows SearchLight to Sekoia.io events |
| AWS, Events | Forward AWS CloudTrail records to Sekoia.io | This playbook pulls records from AWS CloudTrail then push the fetched records to Sekoia.io |
| AWS, Events | Forward AWS Flow Logs records to Sekoia.io | This playbook pulls records from AWS Flow Logs then push the fetched records to Sekoia.io |
| Events | Forward Panda Security Events to Sekoia.io | This playbook pulls security events from the Panda Security Aether platform then push them to Sekoia.io |
| Events | Imperva WAF fetch logs | Fetch events from Imperva Web Application Firewall and forward them to Sekoia.io intake |
| Events | Forward Vade M365 email Events to Sekoia.io | This playbook collect logs from 'Vade for M365' then push them to Sekoia.io |
| Events, Google | Forward Google Pubsub records to Sekoia.io | This playbook consumes records from Google Pubsub and push them to Sekoia.io |

### Intelligence Center templates

| Category | Name | Description |
| --- | --- | --- |
| Observables, Shodan | Shodan Search to observables | Get IP addresses from a Shodan search and add it to Observables database with a tag |
| Observables, Fetch OSINT | Generic Fetch OSINT to observables | Retrieve observables from an OSINT to add it to observable database with a tag (eg: https://github.com/MISP/misp-warninglists/tree/main/lists) |
| Observables, Tranco, TIP  | Tranco top domains to observables | Automatically import Tranco's top 1 000 000 domain names to observable database |

---

## Build your playbooks from scratch

To build a playbook from scratch:

1. On an empty playbook, click **Add a trigger**. The **Triggers** panel of the module menu opens.
2. Click a trigger or drag it to the graph area.
3. Add operators and actions from the module menu, then connect the blocks.
4. Configure each block in the configuration panel.

A playbook combines the following bricks, in this order:

1. [Triggers](triggers.md): Alerts related triggers, manual triggers or Cron
2. [Operators](operators.md): Condition, Foreach, Store
3. [Actions](actions.md): Getters, Setters, External Data Enrichers, Notifications

Refer to the documentation of each type to learn how to use them. For a description of the module menu, see [Navigate playbooks](/xdr/features/automate/navigate-playbooks.md#module-menu).

You can refer to our [playbook templates](https://github.com/SEKOIA-IO/Community/tree/main/playbooks/templates) and [use cases](/xdr/usecases/playbook/synchronize_alerts.md) for inspiration.

## Meta-playbook creation

When you create a playbook from a multi-tenant workspace, the **Create new playbook** window asks you to **Choose a community for your playbook**. You can select one community, several communities or all of them with **Select all**, then click **Create**. A playbook created on several communities is a meta-playbook.

![playbooks-meta-new](/assets/operation_center/playbooks/playbooks-meta-new.png){: style="max-width:100%"}

If you select a single sub-community, a **Grant access to this playbook** step follows the community choice.

![playbooks-meta-single](/assets/operation_center/playbooks/playbooks-meta-single.png){: style="max-width:100%"}

Choose whether the users of this community can access the playbook, then click **Create**:

| Option | Effect |
| --- | --- |
| **No access** | Users from the community cannot access or edit the playbook. The playbook stays a meta-playbook managed from the workspace, and you can add more communities later. |
| **Access** | All users from the community can access and edit the playbook. You cannot add more communities to it later. |

![playbooks-meta-access-ok](/assets/operation_center/playbooks/playbooks-meta-access-ok.png){: style="max-width:100%"}

![playbooks-meta-access-ko](/assets/operation_center/playbooks/playbooks-meta-access-ko.png){: style="max-width:100%"}