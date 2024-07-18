# Git

![Git](/assets/playbooks/library/git.svg){ align=right width=150 }

[Git](https://git-scm.com/) is a free and open source distributed version control system designed to handle projects with speed and efficiency.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `repository_url` | `string` | Git Repository URL |

## Triggers

### File Changes

Trigger playbook run on file changes inside Git Repository

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sleep_time` | `integer` | Time in seconds the trigger sleeps between the checks of file changes |
| `chunk_size` | `integer` | Break results by groups of at most <chunk_size> files (only one group by default) |
| `send_initial_state` | `boolean` | Create events for the initial state of the repository |
| `filter` | `string` | Apply an fnmatch filter to the tracked files |
| `include_repository` | `boolean` | Include the full repository everytime |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `changes` | `array` | File Changes |
| `old_commit` | `string` | hexsha of the previous commit |
| `new_commit` | `string` | hexsha of the last commit |
| `repository_path` | `string` | path of the repository directory |


### New Commit

Trigger playbook run on every Git commit

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sleep_time` | `integer` | Time in seconds the trigger sleeps between the checks of new commits |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `commit` | `object` | Git Commit |
| `repository_path` | `string` | path of the repository directory |


## Extra

Module **`Git` v1.10**