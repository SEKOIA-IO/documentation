# Playbooks

A playbook is a list of required steps and actions needed to successfully respond to any incident or threat.

Playbooks provide a **step-by-step approach** to **orchestration**, helping security teams establish standardized **incident response processes** and ensuring the steps are followed in **compliance** with regulatory frameworks.

In SEKOIA.IO, playbooks play a huge role in automating repetitive tasks to relieve analysts’ daily work, enriching alerts by soliciting external sources, and interconnecting with external systems like ticketing tools for example.

Because they are highly configurable, SEKOIA.IO’s playbooks supervise and execute response actions to be in line with your business and operational objectives.

---

In this documentation, you will learn how to: 

- Configure your profile to be able to efficiently use playbooks
- Set up your playbooks using templates
- Create a playbook from scratch
- Learn more about the different types of triggers, operators and actions
- Troubleshoot with code section and playbook runs

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
| SYMPHONY_WRITE_MODULES | Modify Symphony Modules |
| SYMPHONY_WRITE_PLAYBOOKS | Write Symphony Playbooks |
| SYMPHONY_WRITE_PLAYBOOK_RUNS | Modify Symphony Playbook Runs |

If you need to attribute this role to someone, go to Your Account settings > Managed Communities > The user in question > `+ Role` > Select `Symphony Operator`. 

!!! note 
    Depending on which app you’ll be creating playbooks for, you might need to have additional permissions linked to each app (Intelligence Center or Operations Center). 

**Example:** 

To create playbooks for your TIP, you will need to have the following roles and permissions in addition to Symphony Operator:

### Generate API Key

To be able to use playbooks, an API Key with the right settings is needed for the module configuration to work. 

To generate this API Key: 

1. Go to Account Settings > Managed Communities > API Keys > `+ API Key` 
2. Provide a name and a description (both are mandatory)
3. Select necessary roles for your API Key (Symphony Operator + (?) 
4. Save and copy the value of the API Key in your volt (or any safe place)
5. Paste your API Key in the Module Configuration of your playbook actions

!!! note
    Beware, the generated API Key will no longer be accessible after you’ve closed the modal.

Check out this section to learn more about how to configure your actions using this API Key.

> add an example of module configuration <

## Navigate playbooks' interface

### Playbooks listing

In the playbooks homepage, all playbooks are listed by order of **last edited**. From this view, you can: 

- Create a new playbook
- Search for available playbooks
- Filter available playbooks by status (enabled/disabled)
- Enable and disable playbooks directly from the listing using the toggle button
- Access playbook runs

### Details panel

When clicking on a playbook card, a details panel appears on the right. 

In this panel, you can: 

- Enable or disable the playbook
- Edit playbook
- See how many runs have been going as well as their status (`in progress`, `succeede`d, `error`)
- Quickly access last performed runs and filter them by status

### Playbook details

#### Graphical view

#### Playbook code

#### Playbook details 

#### Playbook runs


## Create and edit a playbook

A playbook starts with a trigger, can include conditions and consists of a succession of actions. 

There are two ways to create a playbook: 
- Use a template 
- Build a playbook from scratch

### Templates

Creating a playbook from scratch can be discouraging. That’s why we provide our users with a way to quickly generate a playbook: **templates**. These fully customizable templates are available in our Playbooks’ Catalog. You can access them by clicking on `+ Playbook` then selecting `Use a template`. 

The Playbooks Catalog is being updated frequently by our analysts, but here’s a list of the main ones. All playbook templates are available on the public repo in [Github.](https://github.com/SEKOIA-IO/Community/tree/main/playbooks/templates) 

#### Operations Center templates

| Category | Name | Description |
| --- | --- | --- |
| Alerts, Notifications, Webhook | Mail Webhook notification on alert | Send an email about an alert when receiving a webhook event |
| Alerts, Notifications, Webhook | Mattermost notification on alert | Notify by mattermost when new alerts are created |
| Alerts, Webhook | Qualify Internet Scan webhook | Qualify an Internet scan alert on webhook |
| Alerts | Playbook adware | Automatic validation of alerts with predefined adware domains |
| Alerts | Alert urgency to 0 when rejected | Put the urgency of an alert to 0 when it is rejected |
| Alerts, Enrichment | Enrich alerts with VirusTotal | Enrich alerts with VirusTotal informations |
| Alert, cron | Reject old alerts (1 year) | Reject old alerts not updated for 1 year. |
| Alert, Webhook, enrichment | Enrich with IKnowWhatYouDownload | Enrich with IKnowWhatYouDownload to check if the IP is known from this service, directly from SEKOIA.IO. |
| Alerts, TheHive | Automatically create an alert on TheHive | Automatically create an alert on TheHive when a new alert is raised in SEKOIA.IO. |
| Alerts, TheHive | Manually create an Alert on TheHive | Create an alert on TheHive via the alert page. |
| Alerts, Notifications | Slack notification on alert | Notify by Slack when new alerts are created. If the target is defined, it is used in the notification, otherwise the hostnames from events are used. |
| Alerts, Enrichment | Enrich alerts with AbuseIPDB | Enrich with AbuseIPDB to check if the IP is known from this service, directly from SEKOIA.IO. |
| Alerts, Enrichment | Alerts Enrichment Shodan Playbook | Enrich with Shodan to check if the IP is known from this service, directly from SEKOIA.IO. |
| Alerts, OSINT | Fetch alerts from Digital Shadows SearchLight | Synchronise alerts from Digital Shadows SearchLight to SEKOIA.IO events |
| AWS, Events | Forward AWS CloudTrail records to SEKOIA.IO | This playbook pulls records from AWS CloudTrail then push the fetched records to SEKOIA.IO |
| AWS, Events | Forward AWS Flow Logs records to SEKOIA.IO | This playbook pulls records from AWS Flow Logs then push the fetched records to SEKOIA.IO |
| Events | Forward Panda Security Events to SEKOIA.IO | This playbook pulls security events from the Panda Security Aether platform then push them to SEKOIA.IO |
| Events | Imperva WAF fetch logs | Fetch events from Imperva Web Application Firewall and forward them to SEKOIA.IO intake |
| Events | Forward Vade M365 email Events to SEKOIA.IO | This playbook collect logs from 'Vade for M365' then push them to SEKOIA.IO |
| Events, Google | Forward Google Pubsub records to SEKOIA.IO | This playbook consumes records from Google Pubsub and push them to SEKOIA.IO |

#### Intelligence Center templates

| Category | Name | Description |
| --- | --- | --- |
| Observables, Shodan | Shodan Search to observables | Get IP addresses from a Shodan search and add it to Observables database with a tag |
| Observables, Fetch OSINT | Generic Fetch OSINT to observables | Retrieve observables from an OSINT to add it to observable database with a tag (eg: https://github.com/MISP/misp-warninglists/tree/main/lists) |
| Observables, Tranco, TIP  | Tranco top domains to observables | Automatically import Tranco's top 1 000 000 domain names to observable database |

## Build your playbooks from scratch

To create a playbook from scratch, you will need to create an empty playbook, go to the graphical view and start adding and configuring the following bricks in this specific order:

- Step 1: [Triggers](/triggers.md) (can be Alerts, Webhook or Cron)
    - **Alerts** allow users to collect information from an alert such as the `alert_uuid`, its date of creation (`created_at`), its category (`alert_type`), its `urgency` or the action that triggered THIS alert notification (`event_type`) for example `alert-created`, `alert-status-changed`, `alert-comment-created` etc.
    - **Cron** allows users to periodically launch an automatic action that should be defined and created by a user.
    - **Webhooks** allows an external service to start a particular action through a single HTTP request.
- Step 2: [Operators](operators.md) (can be Condition, Foreach, Store)
- Step 3: [Actions](actions.md) (Getters, Setters, External Data Enrichers, Notifications)

## Troubleshooting

### RUN feature
If for some reason, a playbook is not working properly, it is possible to display its execution workflow on the section `Playbook > <PlaybookName> Click on RUN`

In the following animation, you will see an issue on the `IF Condition` where the Green overlay ceased and the output of the if un Yellow.

![!SEKOIA.IO Operations Center RUN Feature](/assets/operation_center/playbooks/playbook_in_error.gif){: style="max-width:100%"}

An example of correct playbook workflow should be in green from the begining to the end, as followed:

![!SEKOIA.IO Operations Center RUN Feature 2](/assets/operation_center/playbooks/troubleshooting_running.png){: style="max-width:100%"}

### CODE feature
In addition of the RUN feature, the values of the playbook execution can be displayed in section, juste `next to the RUN button`.

In order to set information parameters to a `Block`, the Copy-Past feature create small sections of content written in JINJA.
> For more information on this language, please follow this [documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/).

It is possible to test your JINJA code on a JSON file (Copy-Past the CODE of your playbook AND remove the nodes) with this small python script:

```python
import json
from jinja2 import Template

file_json = open("file.json", "r")
loading = json.load(file_json)

# The JINJA partern to be tested
jinja_patern = "{{urgency.value}}"

tm = Template(jinja_patern)

msg = tm.render(urgency=loading["urgency"])
print(msg)
```

## Rate limiting

If too many actions are pushed it may block running playbooks. In order to address those issues, playbooks have a rate limiting the action runs.

Every time an action from a playbook must run, we check how many actions this playbook has already started during the last minute. If the threshold is reached then the action is marked in error with a message explaining it has been rate limited.

## Rerun

The user can rerun any run from a playbook. It can help understand issues like stuck playbooks.

From a list of runs, you can see a “Rerun” action button.

- For a successful run, you can rerun all the playbooks.
- For a failed run, you can rerun all the actions in the playbook or only failed and pending actions.

The re-runed run will appear as a new run in the run list.

