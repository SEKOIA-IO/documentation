uuid: d1445e5e-8e3b-417f-ae19-bca67a10affd
name: Atlassian JIRA
type: playbook

# Atlassian JIRA

![Atlassian JIRA](/assets/playbooks/library/atlassian-jira.png){ align=right width=150 }

Atlassian JIRA is a popular project management and issue-tracking software designed to help teams plan, track, and manage agile software development projects efficiently. It offers customizable workflows and integrates seamlessly with other Atlassian products.

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

**Configuration**

{'title': 'Description', 'description': 'Description text in ADF (Atlassian Document Format)', 'type': 'object'}

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

### Get issue

Get issue

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `issue_key` | `string` | Issue key (e.g. PROJ-1) or ID |
| `fields` | `array` | A list of fields to return for the issue (*all by default) |
| `fields_by_keys` | `boolean` | Whether fields in `fields` are referenced by keys rather than IDs |
| `expand` | `string` | Comma-separated list of additional information to include |
| `properties` | `array` | A list of properties to return for the issue (*all by default) |
| `update_view_history` | `boolean` | Whether to mark the issue as recently viewed |
| `fail_fast` | `boolean` | Whether to fail the request quickly in case of an error while loading fields for an issue |

### Search issues

Find issues using provided filters

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `jql` | `string` | JQL query |
| `fields` | `array` | A list of fields to return for the issue (*all by default) |
| `expand` | `string` | Comma-separated list of additional information to include |
| `properties` | `array` | A list of properties to return for the issue (*all by default) |
| `fields_by_keys` | `boolean` | Whether fields in `fields` are referenced by keys rather than IDs |
| `fail_fast` | `boolean` | Whether to fail the request quickly in case of an error while loading fields for an issue |
| `reconcile_issues` | `array` | List of IDs to reconcile |


## Extra

Module **`Atlassian JIRA` v1.4.1**