uuid: 090027a0-89e0-4629-9792-156e1d527971
name: EasyVista Service Manager
type: playbook

# EasyVista Service Manager

![EasyVista Service Manager](/assets/playbooks/library/easyvista-service-manager.png){ align=right width=150 }

Manage EasyVista Service Manager incidents, requests, documents and workflow actions.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | HTTPS protocol and host of the EasyVista server, without a path |
| `tenant_id` | `string` | Non-empty EasyVista account number, including any leading zeros |
| `use_token` | `boolean` | Use access token (Bearer) authentication, recommended; false: Basic authentication |
| `username` | `string` | REST API user login; required when use_token is false |
| `password` | `string` | REST API user password; required when use_token is false |
| `token` | `string` | EasyVista access token; required when use_token is true |
| `verify_ssl` | `boolean` | Verify the server TLS certificate |

## Actions

### Close Request / Incident

Close an incident or request.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `status_guid` | `string` | Final status GUID; defaults to the Closed meta-status |
| `comment` | `string` | Closing action comment |
| `end_date` | `string` | Closing date of the ongoing actions and of the closing action (MM/DD/YYYY HH:MM:SS); defaults to now |
| `catalog_guid` | `string` | Catalog (topic) GUID; only needed to requalify the ticket before closing |
| `delete_actions` | `boolean` | Delete the ongoing actions of the ticket |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Closed ticket URL (HREF) |

### Create an action related to an incident

Create an action related to an incident (EZV_CreateRelatedAction)

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `action` | `object` | Action to create; provide one action type and one group |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `success` | `boolean` | Always true when returned; on failure the action fails and returns nothing |
| `status_code` | `integer` | HTTP status code (201) |
| `href` | `string` | Ticket URL (HREF); only when present in the response |

### Create Request / Incident

Create an incident

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `requests` | `array` | Ticket to create; exactly one per call |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Created ticket URL (HREF) |
| `rfc_number` | `string` | Ticket RFC number, derived from the last HREF path segment; use it to reference the ticket in later actions |

### Create Task

This endpoint allows you to create a new task related to the incident or request specified in the URL.

**Configuration**

{'description': 'Task description', 'title': 'Description', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `action_type_id` | `string` | Action type ID (tenant-specific); provide at least one of action_type_id or action_type_name |
| `action_type_name` | `string` | Action type name, in the REST API user language; provide at least one of action_type_id or action_type_name |
| `group_id` | `integer` | Assigned group ID; provide at least one of group_id, group_name or group_mail |
| `group_name` | `string` | Assigned group name; provide at least one of group_id, group_name or group_mail |
| `group_mail` | `string` | Assigned group email; provide at least one of group_id, group_name or group_mail |
| `description` | `string` | Task description |
| `elapsed_time` | `string` | Task elapsed time |
| `time_cost` | `string` | Task time cost |
| `contractual_cost` | `string` | Task contractual cost |
| `creation_date_ut` | `string` | Task creation date (UTC) |
| `start_date_ut` | `string` | Task start date (UTC) |
| `end_date_ut` | `string` | Task end date (UTC) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | URL returned by the API (HREF); may reference /actions/{rfc_number} |

### Delete a request document

Delete a request document

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `id` | `string` | Document ID (DOCUMENT_ID from the documents list) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `success` | `boolean` | true when the document is deleted: 2xx response, or 590 followed by a confirmed absence from the documents list; on failure the action fails and returns nothing |
| `status_code` | `integer` | HTTP status code of the DELETE (204, 200, or 590 when the deletion was confirmed by listing) |
| `verified_by_listing` | `boolean` | true when the API returned 590 and the deletion was confirmed by re-listing the documents; false for a plain 2xx |
| `api_error` | `string` | Error or message of the 590 body (e.g. Document was not found on the server), kept for troubleshooting; only when verified_by_listing is true |
| `message` | `string` | Human-readable outcome (e.g. Document deleted) |

### Get Questionnaires from non terminated actions

Get the questionnaires of the not completed workflow actions of the given action type on an incident or request

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `current_incident` | `string` | Ticket RFC number |
| `action_type_id` | `integer` | Action type ID (tenant-specific); not the action type GUID |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Query URL (HREF) |
| `record_count` | `integer` | Number of items returned (integer) |
| `total_record_count` | `integer` | Total number of items (integer) |
| `results` | `array` | Questionnaire items, returned unchanged: REQUEST_ID, ACTION_ID, ACTION_TYPE_ID, WORKFLOW_ID (strings) and QUESTION_LIST_ID (string or null); may contain duplicates; to read a questionnaire, use the EasyVista GET /questionnaires/{QUESTION_LIST_ID} endpoint, not exposed by this module |

### Get a specific Document of a Request / Incident

Get a specific attached document to a request The whole file is held in memory and returned as base64; large files inflate playbook results.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `id` | `string` | Document ID (DOCUMENT_ID from the documents list) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `content_type` | `string` | Response Content-Type header |
| `content_base64` | `string` | Document content (standard base64) |

### Get the list of Documents of a Request / Incident

Returns the list of documents attached to the specified incident or request

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `parent_href` | `string` | Ticket URL (PARENT_HREF) |
| `href` | `string` | Documents collection URL (HREF) |
| `documents` | `array` | Document records, returned unchanged: HREF, PARENT_HREF, DOCUMENT_ID, DOCUMENT (file name) and DDL_HREF (download link); use DOCUMENT_ID to download or delete; HREF is a web UI link and does not return the file content |

### Get questionnaire from specific actions

Get the questionnaire of the workflow step of a specific action of an incident or request

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `current_incident` | `string` | Ticket RFC number |
| `action_type_id` | `integer` | Action type ID (tenant-specific); not the action type GUID |
| `action_id` | `string` | Workflow action ID (ACTION_ID) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Query URL (HREF) |
| `record_count` | `integer` | Number of items returned (integer) |
| `total_record_count` | `integer` | Total number of items (integer) |
| `results` | `array` | Questionnaire items, returned unchanged: REQUEST_ID, ACTION_ID, ACTION_TYPE_ID, WORKFLOW_ID and QUESTION_LIST_ID |

### Restart Request / Incident

Resume a suspended incident or request, with an optional comment.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `comment` | `string` | Restart action comment |
| `done_by_id` | `integer` | Employee ID recorded as the author |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Restarted ticket URL (HREF) |

### Suspend Request / Incident

Suspend (place on hold) an incident or request, with an optional comment.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `comment` | `string` | Suspend action comment; does not change the ticket comment |
| `done_by_id` | `integer` | Employee ID recorded as the author |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Suspended ticket URL (HREF) |

### Update Request / Incident

Update an incident or request.

**Configuration**

{'description': 'Ticket description, stored in the COMMENT field; replaced unless append is true', 'title': 'Description', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `append` | `boolean` | Append description to the existing text, separated by <br><br> (EV SM 2025.3+); false or unset: replace it |
| `description` | `string` | Ticket description, stored in the COMMENT field; replaced unless append is true |
| `urgency_id` | `string` | Urgency ID (tenant-specific) |
| `external_reference` | `string` | External reference (e.g. the Sekoia alert ID) |
| `asset` | `string` | Asset tag |
| `asset_serial` | `string` | Asset serial number |
| `ci` | `string` | Configuration item name |
| `ci_id` | `integer` | Configuration item ID |
| `custom_fields` | `object` | Additional EasyVista fields (field name: value), forwarded verbatim |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Updated ticket URL (HREF) |

### Upload and attach a Document to a Request / Incident

Uploads a file (docx, pdf, txt or image file) and attach it to the specified request. Known vendor issue: REST-uploaded files may be impossible to open on some deployments.

**Configuration**

{'description': 'Attached documents description', 'title': 'Description', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |
| `documents` | `array` | Documents to attach; at least one |
| `description` | `string` | Attached documents description |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Ticket URL (HREF); use Get the list of Documents to obtain the attached document IDs |

### View Request / Incident

Returns the specified incident or request

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Ticket URL (HREF) |
| `record` | `object` | Full ticket record: RFC_NUMBER, STATUS (STATUS_EN, STATUS_GUID), RECIPIENT, REQUESTOR, LOCATION, DEPARTMENT, dates, E_* fields; COMMENT and DESCRIPTION are links ({HREF}), not text: use View Request / Incident Comment for the comment |

### View Request / Incident Comment

Returns the comment associated to the specified incident or request

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Comment resource URL (HREF) |
| `parent_href` | `string` | Ticket URL (PARENT_HREF) |
| `comment` | `string` | Ticket COMMENT text, returned verbatim (HTML <br> line breaks included); holds the description set by Create / Update |

### View Request / Incident Problem

Returns the problems linked to the specified incident or request

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `rfc_number` | `string` | Ticket RFC number |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Query URL (HREF) |
| `record_count` | `string` | Number of problems returned (string) |
| `total_record_count` | `string` | Total number of linked problems (string) |
| `records` | `array` | Problem records (RFC_NUMBER, TITLE, STATUS_ID, ...), returned unchanged |

### View Requests / Incidents list

Returns List of Incidents or Requests.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `max_rows` | `integer` | Page size (API default: 100); returns a single page |
| `search` | `string` | EasyVista filter expression, forwarded verbatim |
| `sort` | `string` | Sort expression (e.g. submit_date_ut desc) |
| `fields` | `string` | Comma-separated field names to return |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `href` | `string` | Query URL (HREF) |
| `record_count` | `string` | Number of records returned in this page (string) |
| `total_record_count` | `string` | Total number of matching records (string) |
| `records` | `array` | Ticket records, returned unchanged |

## Set up

## Configuration

This guide supplements the generated action and configuration reference with EasyVista-specific setup and operational guidance.
EasyVista recommends access-token authentication; Basic authentication is also supported.
See the official [REST API authentication documentation](https://docs.easyvista.com/docs/webservice-rest).

### In EasyVista: Configure a dedicated REST API profile

Follow EasyVista's [user profile procedure](https://docs.easyvista.com/docs/profile) to restrict access to the
routes and HTTP methods required by your playbooks.

1. Sign in with an account authorized to manage user profiles.
2. Open `Administration` > `Access Management` > `User Profiles`.
3. Create a dedicated profile, or duplicate an appropriate existing profile, and open its form.
4. Enable the `REST API` option.
5. Click the tools or gear icon next to `REST API` to open the API permissions screen.
6. Select the routes used by your playbooks and enable the corresponding HTTP method columns:
   `GET` for reads, `POST` for creation, `PUT` for updates and state changes, and `DELETE` for document deletion.
7. Save the permissions and the profile.

Grant only the routes and methods needed for your playbooks. In addition to each action's write permissions:

- Account validation requires `GET /requests`.
- Update and Close require `GET /requests/{rfc_number}` for their closed-ticket pre-check.
- Delete Document may need `GET /requests/{rfc_number}/documents` to verify a deletion after a `590` response.

The API root is `/api/v1/{account}`. Placeholder names in the permissions screen may differ from those in the action reference.

### In EasyVista: Assign the profile to a dedicated user

Use the [employee access management procedure](https://docs.easyvista.com/docs/employee) to configure the user
whose permissions the integration will use.

1. Open `Administration` > `Access Management` > `Employees`.
2. Select the dedicated integration user. If you need a new user who is not managed by LDAP or SSO, use `+ New`.
3. Run the `Update Profile` wizard and assign the REST API profile created above.
4. Run `Update Domains` and select the domains containing the tickets the integration should access.
5. Select the appropriate default domain and save the changes.
6. If you created a local user for Basic authentication, verify its login and use the `Change Password` wizard to
   set its password. Keep these credentials for the Sekoia.io account configuration.

### In EasyVista: Generate an access token

Access tokens are available in EV Service Manager 2023.1 and later. The user generating the token must have access
to the token-management menu in their profile. Follow EasyVista's
[access-token procedure](https://docs.easyvista.com/docs/access-tokens):

1. Open `Administration` > `Access Management` > `Access Tokens`.
2. Click `+ New`.
3. Enter a descriptive name, such as `Sekoia.io playbooks`, and select the dedicated integration user.
4. Click `Generate` and securely store the generated value, which is copied to the clipboard.
5. Paste this value into Sekoia.io's `token` field when configuring the account.

> **Note:** The token value is only available when it is generated. Generate a replacement if it is lost.
> If an expiry date is configured, replace the token in Sekoia.io before it expires. A revoked token must also be replaced.

### Identify the server URL and EasyVista account

The vendor's [REST API URL format](https://docs.easyvista.com/docs/webservice-rest) is:

```text
https://{server}/api/v1/{account}/{resource}
```

Obtain the server and account number from your EasyVista administrator:

- `base_url`: the HTTPS protocol and server host only, without `/api/v1` or any other path.
- `tenant_id`: the `{account}` segment, kept as a string to preserve leading zeros. This is the EasyVista account
  number, not the user's login or a Microsoft Entra tenant ID.

For example, use `https://easyvista.example` as a fictitious host and replace `{account}` with your own account number.
The integration constructs the API path; do not append it to `base_url`.

Enter the generated token in Sekoia.io without the `Bearer` prefix. The integration builds the authentication header.
For Basic authentication, use the dedicated user's credentials with the same REST profile and route permissions.
HTTPS remains mandatory even when certificate verification is disabled.

### EasyVista-specific behaviour and limitations

- **Business errors (`590`):** EasyVista can use this non-standard status for invalid identifiers or ticket state.
  Read the response's error message rather than interpreting the status as a generic server failure. The module
  does not retry `590` responses. Suspending an already suspended ticket or restarting one that is not suspended
  fails the action.
- **Closed tickets:** Update and Close read the ticket first and refuse it when `END_DATE_UT` is populated.
  This avoids an apparent API success on an already closed ticket and requires an additional read permission.
- **Appending descriptions:** Requires EV Service Manager 2025.3 or later. Appending is not idempotent, so the
  module never retries a PUT containing the `append` query parameter, whatever its value. EasyVista appends whenever
  this parameter is present, even with `append=false`. The Update action sends it only when `append` is true;
  false or unset replaces the description by omitting the parameter. Check the ticket after an uncertain timeout
  before trying again.
- **Other writes:** POST requests are also never retried because they can create duplicates.
- **Suspend and restart:** These transitions are never retried automatically. After a gateway timeout, check the
  ticket state before trying again: EasyVista may already have applied the transition.
- **Partial updates:** Empty optional text fields are omitted so that untouched playbook fields do not clear existing
  ticket values. To clear a field intentionally, send its EasyVista field name with an empty string in `custom_fields`.
  Non-empty explicit arguments take precedence over matching custom fields.
- **Pagination:** EasyVista paginates GET results from version 2024.3. This module returns only one page and does
  not follow next-page links automatically. A ticket absent from the first page is not necessarily absent from EasyVista.
- **REST-uploaded documents:** On some installations, an API upload succeeds and the attachment is listed, but
  downloading it returns `590` and opening it in the EasyVista UI returns `500`. This is an observed server-side
  issue. If affected, attach files through the EasyVista UI and contact EasyVista support.
- **Document deletion:** A `590` response can occur even when the attachment was removed. The module checks the
  document list and confirms deletion only if the ID is absent from a complete list. If verification fails or another
  page is advertised, the action fails with the original API error instead of reporting an unverified success.
- **Document size:** Downloads are returned as base64 with the entire file held in memory; large documents
  increase playbook result sizes. Document download and deletion require EV Service Manager 2023.1 or later.
- **Questionnaires:** Require EV Service Manager 2023.4 or later and a numeric action type ID from EasyVista
  administration, rather than an action type GUID. Empty questionnaire results are successful.
- **Catalogs, groups and action types:** Their identifiers and permitted combinations depend on your EasyVista
  account. Use values allowed for the ticket's catalog; a rejected action type can produce a misleading catalog error.
- **Licensing:** EasyVista states that each API call consumes a user license. Pre-checks and deletion verification
  make additional calls. See [Licensing and security](https://docs.easyvista.com/docs/webservice-rest#licensing-and-security).

### Verify access and troubleshoot

The account validator performs a read-only request to:

```text
GET /api/v1/{tenant_id}/requests?max_rows=1&fields=rfc_number
```

A successful validation confirms access to the ticket-list route. It does not prove that the user can create,
update, close or delete resources; enable and check the corresponding route and method permissions separately.
Test write actions on a ticket intended for testing.

| Error | What to check |
| --- | --- |
| `401` | The selected authentication mode, token or credentials, and EasyVista account number. |
| `403` | The profile's `REST API` option and permissions for the requested route and method. |
| `404` | The server URL, account number, and requested ticket or document identifier. |
| TLS or connection error | Server reachability and the certificate trust chain. |
| `590` | The API error message, ticket state, and account-specific catalog, group and action-type identifiers. |

### Illustrative playbook flow — not executable

**The following is a conceptual example, not an executable or importable playbook. Do not paste it into the Code tab.**
It contains no node UUIDs, account bindings or runnable JSON structure.

```text
When a Sekoia.io alert needs an EasyVista ticket:
  Create Request / Incident using a catalog allowed for the integration user.
  Save the returned rfc_number with the investigation context.

While the investigation progresses:
  Reuse that rfc_number to update or append investigation details.
  Keep the ticket open until the investigation is resolved.

When the investigation is resolved:
  Close Request / Incident with the resolution comment.
```

To build an executable template, follow the official
[Sekoia.io playbook JSON format and schema](https://docs.sekoia.com/xdr/features/automate/playbooks_format_json_schema/),
use the published module and action UUIDs, and bind the configured EasyVista account in your community.


## Extra

Module **`EasyVista Service Manager` v1.0.1**