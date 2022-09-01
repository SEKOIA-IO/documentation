# Debug playbooks

## Rate limiting

If too many actions are pushed, it may block running playbooks. In order to address this issue, playbooks have a rate limiting the action runs.

Every time an action from a playbook must run, SEKOIA.IO check how many actions this playbook has already started during the last minute. If the threshold is reached then the action is marked in error with a message explaining it has been rate limited.

## Rerun

Users can restart any run from a playbook. Doing so can help understand issues like stuck playbooks.

From a list of runs, you can see a “Rerun” action button with a refresh icon. This button applies to: 

- Successful runs: it restarts all actions in the playbook. 
- Failed runs: it either restarts all the actions in the playbook or only failed and pending actions.

The re-runed run will appear as a new entry in the runs' list.
