uuid: 26075aca-cd73-49d2-98f6-d03ac58e773d
name: Microsoft Outlook
type: playbook

# Microsoft Outlook

![Microsoft Outlook](../../../../assets/playbooks/library/microsoft-outlook.png)

Microsoft Outlook is an email client and personal information manager that includes calendar, task management, contact management, note-taking, and web browsing features. It integrates with Microsoft Office suite for seamless productivity and communication.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `tenant_id` | `string` | ID of the Azure AD tenant |
| `client_id` | `string` | Client ID. An application needs to be created in the Azure Portal and assigned relevant permissions. Its Client ID should then be used in this configuration. |
| `client_secret` | `string` | Client Secret associated with the registered application. Admin Consent has to be granted to the application for it to work. |

## Actions

### Delete a message

The action that deletes a message from the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `message_id` | `['string', 'object']` | The Microsoft Graph message item ID, or a message object containing message_id |
| `user` | `string` | The user identifier or user principal name (UPN) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `action` | `string` | The action technical identifier |
| `status` | `string` | The execution status |
| `target_message_id` | `string` | The Microsoft Graph message item ID targeted by the action |
| `user` | `string` | The echo of the user identifier used for this action |

### Forward a message

The action that forwards a message from the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `comment` | `string` | The optional comment included in the forwarded message |
| `message_id` | `['string', 'object']` | The Microsoft Graph message item ID, or a message object containing message_id |
| `recipients` | `array` | The list of recipient email addresses |
| `user` | `string` | The user identifier or user principal name (UPN) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `action` | `string` | The action technical identifier |
| `comment` | `string` | The optional comment included in the forwarded message |
| `recipients` | `array` | The recipient email addresses used by the action |
| `status` | `string` | The execution status |
| `target_message_id` | `string` | The Microsoft Graph message item ID targeted by the action |
| `user` | `string` | The echo of the user identifier used for this action |

### Get a message

The action that gets message details from the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `message_id` | `['string', 'object']` | The Microsoft Graph message item ID, or a message object containing message_id |
| `user` | `string` | The user identifier or user principal name (UPN) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `from` | `object` | The sender information |
| `internet_message_id` | `string` | The Internet Message-ID (RFC 5322) |
| `message_id` | `string` | The Microsoft Graph message item ID |
| `received_date_time` | `string` | The message reception timestamp |
| `subject` | `string` | The message subject |
| `to_recipients` | `array` | The list of recipients |
| `user` | `string` | The echo of the user identifier used for this action |

### Search messages

The action that searches messages in a user's mailbox using InternetMessageId and/or NetworkMessageId

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `email_local_id` | `string` | The local message identifier mapped from email.local_id (Graph NetworkMessageId) |
| `email_message_id` | `string` | The message identifier mapped from email.message_id (Graph internetMessageId / Internet Message-ID RFC 5322) |
| `max_messages_to_return` | `integer` | The maximum number of messages to return |
| `return_most_recent_first` | `boolean` | The option to return candidates sorted by receivedDateTime descending when true |
| `user` | `string` | The user identifier or user principal name (UPN) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `has_more` | `boolean` | The indicator that is true when Graph indicates additional pages may exist |
| `message_ids` | `array` | The list of Microsoft Graph message item IDs extracted from returned messages |
| `messages` | `array` | The list of matching messages |
| `query_type` | `string` | The identifier type used for the search |
| `query_value` | `string` | The search identifier value, or concatenated values when both identifiers are provided |
| `returned_count` | `integer` | The alias of total_results for explicit count-based playbook conditions |
| `scan_limit_reached` | `boolean` | The indicator that is true when fallback scanning stops at the max scanned-messages budget |
| `total_results` | `integer` | The number of messages returned in this response |
| `user` | `string` | The echo of the user identifier used for this action, reusable in downstream playbook nodes |

### Send a message

The action that sends a message from the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bcc` | `array` | The list of BCC recipient email addresses |
| `cc` | `array` | The list of CC recipient email addresses |
| `content` | `string` | The plain-text or HTML content of the message |
| `content_type` | `string` | The content type of the message body |
| `from` | `string` | The mailbox owner email address used in the From header (usually the same as sender) |
| `importance` | `string` | The importance level of the message |
| `recipients` | `array` | The list of recipient email addresses |
| `save_to_sent_items` | `boolean` | The setting that controls whether the message is saved in Sent Items |
| `sender` | `string` | The sender email address (usually the same as mailbox owner) |
| `subject` | `string` | The subject of the message |
| `user` | `string` | The user identifier or user principal name (UPN) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `action` | `string` | The action technical identifier |
| `bcc` | `['array', 'null']` | The list of BCC recipient email addresses used by the action |
| `cc` | `['array', 'null']` | The list of CC recipient email addresses used by the action |
| `content_type` | `string` | The content type of the message body used by the action |
| `from` | `string` | The mailbox owner email address used in the From header |
| `importance` | `['string', 'null']` | The importance level of the message used by the action |
| `recipients` | `array` | The recipient email addresses used by the action |
| `save_to_sent_items` | `boolean` | The setting that controls whether the message is saved in Sent Items |
| `sender` | `string` | The sender email address used by the action |
| `status` | `string` | The execution status |
| `subject` | `string` | The subject of the message used by the action |
| `target_message_id` | `['string', 'null']` | The Microsoft Graph message item ID targeted by the action |
| `user` | `string` | The echo of the user identifier used for this action |

### Update a message

The action that updates a message in the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bcc` | `array` | The updated list of BCC recipient email addresses |
| `cc` | `array` | The updated list of CC recipient email addresses |
| `content` | `string` | The updated plain-text content of the message |
| `from` | `string` | The updated mailbox owner email address used in the From header |
| `importance` | `string` | The importance level of the message |
| `message_id` | `['string', 'object']` | The Microsoft Graph message item ID, or a message object containing message_id |
| `recipients` | `array` | The updated list of recipient email addresses |
| `sender` | `string` | The updated sender email address |
| `subject` | `string` | The updated subject of the message |
| `user` | `string` | The user identifier or user principal name (UPN) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `action` | `string` | The action technical identifier |
| `bcc` | `['array', 'null']` | The updated list of BCC recipient email addresses used by the action |
| `cc` | `['array', 'null']` | The updated list of CC recipient email addresses used by the action |
| `from` | `['object', 'null']` | The sender information |
| `importance` | `['string', 'null']` | The importance level of the message used by the action |
| `internet_message_id` | `string` | The Internet Message-ID (RFC 5322) |
| `message_id` | `string` | The Microsoft Graph message item ID |
| `received_date_time` | `string` | The message reception timestamp |
| `recipients` | `['array', 'null']` | The updated list of recipient email addresses used by the action |
| `sender` | `['object', 'null']` | The sender information returned by Microsoft Graph |
| `status` | `string` | The execution status |
| `subject` | `string` | The message subject |
| `to_recipients` | `array` | The list of recipients |
| `updated_from` | `['string', 'null']` | The updated mailbox owner email address provided in the input From header |
| `updated_sender` | `['string', 'null']` | The updated sender email address provided in the input |
| `updated_subject` | `['string', 'null']` | The updated subject provided in the input |
| `user` | `string` | The echo of the user identifier used for this action |

## Set up

### Configure

#### Create an Azure application

1. On the Azure Portal, in the search bar, go to `App registrations`
2. Click `+ New registration`
3. Type a name
4. Select `Accounts in this organizational directory only` option as account type
5. Click `Register`
6. From the `Overview` page, copy `Application (client) ID` and `Directory (tenant) ID`

#### Create a client secret

1. Go to `Manage` > `Certificates & secrets`
2. Click `+ New client secret`
3. Type a description and select the desired expiration period
4. Click `Add`
5. Copy the `Value` of the client secret

#### Add permissions

1. Go to `Manage` > `API permissions`
2. Click `Add a permissions`
3. On the right panel, Select `Microsoft APIs` tab
4. Click `Microsoft Graph`
5. Click `Application permissions`
6. Select the following permissions
    - Mail.ReadWrite
    - Mail.Send
    - User.Read.All
7. Click `Add permissions`
8. In the `API permissions` page, click `Grant admin consent for TENANT_NAME`
9. Click `Yes` in the `Grant admin consent confirmation` modal

## Extra

Module **`Microsoft Outlook` v0.5.1**