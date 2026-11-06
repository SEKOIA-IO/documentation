---
uuid: 090027a0-89e0-4629-9792-156e1d527971
name: EasyVista Service Manager
type: playbook
---

# EasyVista Service Manager

![EasyVista Service Manager](/assets/playbooks/library/easyvista-service-manager.png){ align=right width=150 }

EasyVista Service Manager is an action-only integration for Sekoia.io playbooks. It helps analysts create and manage EasyVista requests/incidents during investigation and response.

This module provides:

- 17 playbook actions
- one account validator

It does **not** provide an intake connector, trigger, or log collection capability.

## Typical use cases

- Create an EasyVista incident from a Sekoia.io alert.
- Update the ticket during the investigation.
- Close the ticket with a resolution comment.
- Manage related documents, tasks, and workflow actions.
- Query tickets, comments, linked problems, and questionnaires.

## EasyVista prerequisites

- Use a dedicated EasyVista user profile with REST API access.
- Grant REST permissions per route and HTTP method used by your actions.
- `Update Request / Incident` and `Close Request / Incident` also require `GET /requests/{rfc_number}` to check whether the ticket is already closed.
- The account validator calls `GET /requests?max_rows=1&fields=rfc_number`.
- `tenant_id` is the EasyVista account number used in `/api/v1/{account}` and must stay a string (including leading zeros).

## Authentication and account configuration

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `base_url` | `string` | Yes | — | HTTPS host only, without path/query/credentials (example: `https://easyvista.example`). |
| `tenant_id` | `string` | Yes | — | Non-empty EasyVista account number used in `/api/v1/{account}`. Keep leading zeros. |
| `use_token` | `boolean` | No | `true` | Select authentication mode (`true` for Bearer token, `false` for Basic). |
| `token` | `string` (secret) | Yes when `use_token=true` | — | EasyVista access token. |
| `username` | `string` | Yes when `use_token=false` | — | EasyVista REST API username. |
| `password` | `string` (secret) | Yes when `use_token=false` | — | EasyVista REST API password. |
| `verify_ssl` | `boolean` | No | `true` | TLS certificate verification. |

### Creating an access token

In the EasyVista Service Manager interface:

1. At the bottom of the left panel, click the **Global Menu** button (globe icon).
2. Go to **Administration > Access Management > Access Tokens**.
3. Click **+ New**.
4. Fill at least:
    - `Access token name (*)`
    - `Employee (*)`
    - `Expiry date`
5. Click **Generate**, then copy the generated token.
6. Configure this value in the integration account field `token`.

### Basic authentication alternative

If your tenant does not use token authentication, set `use_token=false` and provide `username` + `password`.

### Important transport rule

The module enforces HTTPS for all API calls. Setting `verify_ssl=false` disables certificate verification but still does **not** allow HTTP.

### Bearer status

Bearer mode must be validated on the target integration tenant before production publication. This documentation does not claim that this live tenant validation has already been completed.

## Available actions

The 17 actions below come from the module descriptors (`action_*.json`).

### Close Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `status_guid` | `string` | No | Final status GUID |
| `comment` | `string` | No | Closing comment |
| `end_date` | `string` | No | Closing date (`MM/DD/YYYY HH:MM:SS`) |
| `catalog_guid` | `string` | No | Catalog GUID |
| `delete_actions` | `boolean` | No | Delete related actions |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | `HREF` of the closed ticket |

### Create an action related to an incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `action` | `object` | Yes | Action payload. Must provide at least one of `action_type_id`, `action_type_name`, `action_type_guid`, and at least one of `group_id`, `group_name`, `group_mail` |

`action` fields:

- `action_type_id` (`string`)
- `action_type_name` (`string`)
- `action_type_guid` (`string`)
- `group_id` (`integer`)
- `group_name` (`string`)
- `group_mail` (`string`)
- `description` (`string`)
- `comment` (`string`)

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `success` | `boolean` | `true` when the action succeeds |
| `status_code` | `integer` | HTTP status code (`201`) |
| `href` | `string` | URL returned by the API when present |

### Create Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `requests` | `array` | Yes | Exactly one item (`minItems=1`, `maxItems=1`) |

`requests[0]` fields:

- `catalog_code` (`string`)
- `title` (`string`)
- `description` (`string`)
- `urgency_id` (`integer`)
- `impact_id` (`string`)
- `recipient_name` (`string`)
- `recipient_mail` (`string`)
- `department_code` (`string`)
- `location_id` (`integer`)
- `custom_fields` (`object`)

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | `HREF` of the created ticket |
| `rfc_number` | `string` | RFC number derived from `HREF` |

### Create Task

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `action_type_id` | `string` | Cond. | Provide `action_type_id` or `action_type_name` |
| `action_type_name` | `string` | Cond. | Provide `action_type_id` or `action_type_name` |
| `group_id` | `integer` | Cond. | Provide one of `group_id`, `group_name`, `group_mail` |
| `group_name` | `string` | Cond. | Provide one of `group_id`, `group_name`, `group_mail` |
| `group_mail` | `string` | Cond. | Provide one of `group_id`, `group_name`, `group_mail` |
| `description` | `string` | No | Task description |
| `elapsed_time` | `string` | No | Elapsed time |
| `time_cost` | `string` | No | Time cost |
| `contractual_cost` | `string` | No | Contractual cost |
| `creation_date_ut` | `string` | No | Creation date |
| `start_date_ut` | `string` | No | Start date |
| `end_date_ut` | `string` | No | End date |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | URL returned by the API |

### Delete a request document

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `id` | `string` | Yes | `DOCUMENT_ID` from document list |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `success` | `boolean` | Deletion status |
| `status_code` | `integer` | HTTP status code (`200`/`204`/`590`) |
| `verified_by_listing` | `boolean` | `true` when deletion was confirmed after `590` by listing |
| `api_error` | `string` | Error details when `verified_by_listing=true` |
| `message` | `string` | Human-readable result |

### Get Questionnaires from non terminated actions

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `current_incident` | `string` | Yes | Ticket RFC number |
| `action_type_id` | `integer` | Yes | Numeric action type ID (not GUID) |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | Query `HREF` |
| `record_count` | `integer` | Number of returned items |
| `total_record_count` | `integer` | Total number of items |
| `results` | `array` | Raw questionnaire rows |

### Get a specific Document of a Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `id` | `string` | Yes | `DOCUMENT_ID` from document list |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `content_type` | `string` | HTTP `Content-Type` |
| `content_base64` | `string` | File content in base64 |

### Get the list of Documents of a Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `parent_href` | `string` | Parent ticket `HREF` |
| `href` | `string` | Collection `HREF` |
| `documents` | `array` | Raw document objects (`DOCUMENT_ID`, `DOCUMENT`, `DDL_HREF`, ...) |

### Get questionnaire from specific actions

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `current_incident` | `string` | Yes | Ticket RFC number |
| `action_type_id` | `integer` | Yes | Numeric action type ID (not GUID) |
| `action_id` | `string` | Yes | Workflow `ACTION_ID` |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | Query `HREF` |
| `record_count` | `integer` | Number of returned items |
| `total_record_count` | `integer` | Total number of items |
| `results` | `array` | Raw questionnaire rows |

### Restart Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `comment` | `string` | No | Optional restart comment |
| `done_by_id` | `integer` | No | Operator ID |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | `HREF` of restarted ticket |

### Suspend Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `comment` | `string` | No | Optional suspend comment |
| `done_by_id` | `integer` | No | Operator ID |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | `HREF` of suspended ticket |

### Update Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `append` | `boolean` | No | Append description (EV SM `2025.3+`) |
| `description` | `string` | No | Description update |
| `urgency_id` | `string` | No | Urgency |
| `external_reference` | `string` | No | External reference |
| `asset` | `string` | No | Asset |
| `asset_serial` | `string` | No | Asset serial |
| `ci` | `string` | No | CI |
| `ci_id` | `integer` | No | CI ID |
| `custom_fields` | `object` | No | EasyVista field/value map |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | `HREF` of updated ticket |

### Upload and attach a Document to a Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |
| `documents` | `array` | Yes | At least one `{ filename, filedata }` object |
| `description` | `string` | No | Optional upload description |

`documents[*]` requires:

- `filename` (`string`)
- `filedata` (`string`, base64)

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | Ticket URL returned by API |

### View Request / Incident Comment

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | Comment resource `HREF` |
| `parent_href` | `string` | Parent ticket `HREF` |
| `comment` | `string` | Ticket comment text |

### View Request / Incident

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | Ticket `HREF` |
| `record` | `object` | Full raw ticket object returned by EasyVista |

### View Request / Incident Problem

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `rfc_number` | `string` | Yes | Ticket RFC number |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | Query `HREF` |
| `record_count` | `string` | Number of problems in page |
| `total_record_count` | `string` | Total number of linked problems |
| `records` | `array` | Raw problem objects |

### View Requests / Incidents list

**Arguments**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `max_rows` | `integer` | No | Single-page size |
| `search` | `string` | No | EasyVista filter expression |
| `sort` | `string` | No | Sort expression |
| `fields` | `string` | No | Comma-separated field names |

**Outputs**

| Name | Type | Description |
| --- | --- | --- |
| `href` | `string` | Query `HREF` |
| `record_count` | `string` | Number of records in page |
| `total_record_count` | `string` | Total number of matching records |
| `records` | `array` | Raw ticket objects |

## Playbook example (non-executable pseudocode)

The YAML below illustrates only the sequence with fictional values. It is **not** importable as-is in the Sekoia.io playbook editor/API.

For an executable playbook, use the JSON graph format documented in [playbooks_format_json_schema.md](/xdr/features/automate/playbooks_format_json_schema.md) with action UUIDs and `node.<id>` references.

Example sequence:

1. Create a ticket.
2. Read the returned `rfc_number`.
3. Update the description.
4. Close the ticket with a resolution comment.

```yaml
steps:
  - name: create_ticket
    action: easyvista-service-manager.create_request_incident
    args:
      requests:
        - catalog_code: "SEC_INCIDENT"
          title: "Suspicious PowerShell activity detected"
          description: "Alert {{ alert.uuid }} raised by detection engine."

  - name: update_ticket
    action: easyvista-service-manager.update_request_incident
    args:
      rfc_number: "{{ steps.create_ticket.result.rfc_number }}"
      description: "Investigation in progress. Host isolated."
      append: true

  - name: close_ticket
    action: easyvista-service-manager.close_request_incident
    args:
      rfc_number: "{{ steps.create_ticket.result.rfc_number }}"
      comment: "Containment and remediation completed."
```

## Behaviors and limitations

- `View Requests / Incidents list` returns a single page. `max_rows` controls page size; there is no automatic pagination.
- POST operations are not retried (to avoid potential duplicate object creation).
- Update operations with `append=true` are not retried.
- In `Update Request / Incident`, empty optional text fields are ignored.
- To intentionally clear a value, use `custom_fields` with the exact EasyVista field name and an empty string.
- Non-empty explicit action fields take precedence over matching keys in `custom_fields`.
- `Update Request / Incident` and `Close Request / Incident` check `END_DATE_UT` and fail if the ticket is already closed.
- Document upload requires JSON + base64 content.
- Document download returns base64 and keeps the full file in memory.
- Observed tenant limitation: some REST-uploaded documents are created but cannot be opened (REST and EasyVista UI). This is documented as an observed limitation, not a guaranteed behavior for every tenant.
- After a document DELETE returning `590`, the module verifies deletion by listing documents. It confirms success only when the document is absent from a complete list. A partial list cannot confirm deletion.
- Questionnaire actions require a numeric `action_type_id` from EasyVista administration.
- An empty questionnaire result is considered a successful action response.
- Minimum EasyVista versions:
  - document GET/DELETE: `2023.1+`
  - questionnaire actions: `2023.4+`
  - update with `append=true`: `2025.3+`
- Action types and groups are tenant- and catalog-dependent.
- Each API call consumes an EasyVista user license according to vendor specifications.

## Troubleshooting

| Error | What to check |
| --- | --- |
| `401` | Authentication mode, credentials/token, and `tenant_id`. |
| `403` | REST API permissions, allowed route, and HTTP method rights for the API user. |
| `404` | `base_url`, account (`tenant_id`), and target resource identifiers. |
| `590` | Read the EasyVista business message, then verify ticket state and identifiers (ticket/document/action/group/action type). |
| Connection/TLS errors | Reachability of the EasyVista host and certificate trust chain (especially with `verify_ssl=true`). |

## Extra

Module **`EasyVista Service Manager` v1.0.0**
