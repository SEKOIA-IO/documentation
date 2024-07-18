# Atlassian JIRA

![Atlassian JIRA](/assets/playbooks/library/atlassian-jira.png){ align=right width=150 }

Integrates with JIRA

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `domain` | `string` | Your organization JIRA domain (e.g. 'sandbox.atlassian.net') |
| `email` | `string` | Email of the user |
| `api_key` | `string` | API Key to use to connect to JIRA API endpoints |

## Actions

### Change Status of an Issue

Change status of an issue in JIRA

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `issue_key` | `string` | Issue key (e.g. PROJ-1) |
| `status_name` | `string` | Exact name of the status (e.g. 'To Do') |

### Comment Issue

Add comment to an issue in JIRA

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `issue_key` | `string` | Issue key (e.g. PROJ-1) |
| `comment` | `string` | Text of a comment |

### Create Issue

Create issue in JIRA

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `project_key` | `string` | Project key (e.g. 'PRJ') |
| `summary` | `string` | Summary of an issue (e.g. 'Fix a bug') |
| `issue_type` | `string` | Issue type (e.g. 'Task') |
| `description` | `object` | Description text in ADF (Atlassian Document Format) |
| `due_date` | `string` | Due date (e.g. '2023-10-31')' |
| `labels` | `string` | Comma-separated labels (e.g. 'devops,support') |
| `assignee` | `string` | Exact display name of an assignee (e.g. John Doe) |
| `reporter` | `string` | Exact display name of a reporter (e.g. Jane Doe) |
| `priority` | `string` | Issue priority (e.g. Highest) |
| `parent_key` | `string` | Key of a parent issue (e.g. PRJ-1) |
| `custom_fields` | `object` | JSON with custom fields (e.g. {"Some Field": "2"}) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `issue_key` | `string` | Key of the created issue |


## Extra

Module **`Atlassian JIRA` v1.1**