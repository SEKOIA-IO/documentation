# Build playbooks

A playbook starts with a trigger, can include conditions and consists of a succession of actions.

There are two ways to create a playbook:

- Use a pre-made template
- Build a playbook from scratch

## Templates

Creating a playbook from scratch can be complex. That’s why we provide our users with a way to quickly generate a playbook: **templates**.

These fully customizable templates are available in our Playbooks’ Catalog. You can access them by clicking on `+ Playbook` then selecting `Use a template`. These could be a really good working base.

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

To create a playbook from scratch, you will need to create an empty playbook, go to the graphical view and start adding and configuring the following bricks in this specific order:

1. [Triggers](triggers.md): Alerts related triggers, manual triggers or Cron
2. [Operators](operators.md): Condition, Foreach, Store
3. [Actions](actions.md): Getters, Setters, External Data Enrichers, Notifications

Please refer to the documentation for each of these types to learn how to use them efficiently.

You can refer to our [playbook templates](https://github.com/SEKOIA-IO/Community/tree/main/playbooks/templates) and [use cases](/xdr/usecases/playbook/synchronize_alerts/) for inspiration.
