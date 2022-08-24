# Debug playbooks

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


