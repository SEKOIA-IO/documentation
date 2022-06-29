# Playbooks

Automating your security improves your cyber security operations by consolidating the use of your technologies, processes and policies.

Automation combines security tools, processes and people, and speeds up the execution of your security responses while ensuring their repeatability and verifiability.

Thus, SEKOIA.IO supervises and executes response actions to be in line with your business and operational objectives.

## Introduction

SEKOIA.IO comes with an in house GUI for creating automated investigation and orchestration actions: the playbooks.

The playbooks are capable of automatically analysing and investigating all alerts coming from your SIEM. They also allow a quick and fully automated sorting after the analysis of multiple factors.

Create your own playbooks to build your processes. Use the SEKOIA.IO interface to interconnect your tools and implement your scenarios. Configure the execution of your playbooks by triggering them manually on the alert/case page or automatically based on multiple factors.

![!SEKOIA.IO Operations Center playbook overview](/assets/operation_center/playbooks/overview_playbook.png){: style="max-width:100%"}

## Getting started with a playbook

A simple way to create your playbook: you only need to name it and add a description before validating it.

![!SEKOIA.IO Operations Center playbook creation gif](/assets/operation_center/playbooks/create_a_playbook.gif){: style="max-width:100%"}

## Prerequisites

First of all, create two roles in `Settings > Communities > Your community > Roles > + ROLE`:
- `SIC Operator` by selecting the 36 roles that starts with SIC
- `Symphony Operator` by selecting the 7 roles that starts with SYMPHONY

Then, to be able to use a `Block` such as a Sekoia trigger, you should create an API key with the right level of accreditations: SIC Operation and Symphony Operator.
To do it, go to `Settings > Communities > Your community > API Keys > + API Key`
- Name and describe your API Key
- Select the right roles for your key in order to be efficient

![!SEKOIA.IO User Center API Key creation](/assets/operation_center/playbooks/create_an_api_key.png){: style="max-width:100%"}

> Note: Save your new API Key in a vault. It will no longer be accessible!

Now you will be able to setup a configuration for the Sekoia `Blocks`, built for you.
Back in the Operations Center, section Playbooks:

- Select the trigger of your choice, for instance `Security alerts`
- Drag and drop it into the center of your screen
- On the right side, `Create new configuration`
- Paste your API key
- Fulfill the `base_url` field with `https://api.sekoia.io`
- Click `SAVE` button

## Build your playbooks with Blocks filtered into 3 types

To create a playbook, you will basically need to use the following filters. More information by following these links:

- [Triggers](triggers.md)
- [Operators](operators.md)
- [Actions](actions.md)

## Playbook templates

In order to ease the deployment of playbooks, we regularly produce Playbook templates that are ready to use for anyone with an API key.

To use one:
- Click on `+ NEW PLAYBOOK`
- Select `Use a template`
- Filter on your needs `alert`, `notification`, `webhook` or use the `Search bar`
- Select the template you are interested in
- Click on `CREATE`

A brand new playbook will be created. Then you just have to adjust the `Module Configuration` section of each block with your API key and URL. You can either create a new configuration or use an existing one that will appear on the list menu.

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
