# Debug playbooks

## Rate limiting

If too many actions are pushed, it may block running playbooks. In order to address this issue, playbooks have rate limiting applied on their action runs.

Every time an action from a playbook must run, Sekoia.io checks how many actions this playbook has already started during the last minute.

If the threshold is reached, the action is marked in error with a text explaining it has been rate limited.

## Rerun

Users can restart any run from a playbook. Doing so can help understand issues like stuck playbooks.

From a list of runs, you can see a `Rerun` action button with a refresh icon. This button applies to:

- Successful runs: it restarts all actions in the playbook.
- Failed runs: it either restarts all the actions in the playbook or only failed and pending actions.

When a successful run is restarted (thus restarting all actions in the playbook), it will create a new entry in the runs' list.
When a failed or a pending run is restarted, it will update the run that was restarted, but not create add a new run in the runs' list.

## Playbook logs

#### Switch Mode

After a playbook run is executed, it is possible to switch modes after selecting a module. Log information will be displayed in the different modes:

- Edition:  logs returned and displayed in a tab
- Run Results: results of an executed module
