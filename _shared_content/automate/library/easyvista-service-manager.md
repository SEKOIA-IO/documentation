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

In EasyVista, create a token from **Administration > Access Management > Access Tokens**, then configure it in `token`.

### Basic authentication alternative

If your tenant does not use token authentication, set `use_token=false` and provide `username` + `password`.

### Important transport rule

The module enforces HTTPS for all API calls. Setting `verify_ssl=false` disables certificate verification but still does **not** allow HTTP.

### Bearer validation status

Bearer mode must be validated on the target integration tenant before production publication. This documentation does not claim that this live tenant validation has already been completed.

## Available actions

The 17 action names below come from the module descriptors (`action_*.json`):

1. `Close Request / Incident`
2. `Create an action related to an incident`
3. `Create Request / Incident`
4. `Create Task`
5. `Delete a request document`
6. `Get Questionnaires from non terminated actions`
7. `Get a specific Document of a Request / Incident`
8. `Get the list of Documents of a Request / Incident`
9. `Get questionnaire from specific actions`
10. `Restart Request / Incident`
11. `Suspend Request / Incident`
12. `Update Request / Incident`
13. `Upload and attach a Document to a Request / Incident`
14. `View Request / Incident Comment`
15. `View Request / Incident`
16. `View Request / Incident Problem`
17. `View Requests / Incidents list`

At the moment, action-library pages in this repository are maintained as static Markdown pages (no built-in include/generator for action argument/output schemas from automation descriptors).

## Playbook example (fictional values)

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
