uuid: 26075aca-cd73-49d2-98f6-d03ac58e773d
name: Microsoft Outlook
type: playbook

# Microsoft Outlook

![Microsoft Outlook](/assets/playbooks/library/microsoft-outlook.png){ align=right width=150 }

Microsoft Outlook is an email client and personal information manager that includes calendar, task management, contact management, note-taking, and web browsing features. It integrates with Microsoft Office suite for seamless productivity and communication.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `tenant_id` | `string` | ID of the Azure AD tenant |
| `client_id` | `string` | Client ID. An application needs to be created in the Azure Portal and assigned relevant permissions. Its Client ID should then be used in this configuration. |
| `client_secret` | `string` | Client Secret associated with the registered application. Admin Consent has to be granted to the application for it to work. |

## Actions

### Delete a message

Delete a message from the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `user` | `string` | The identifier or the principal name of the user |
| `message_id` | `string` | The identifier of the message to delete |

### Forward a message

Forward a message from the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `user` | `string` | The identifier or the principal name of the user |
| `message_id` | `string` | The identifier of the message to forward |
| `comment` | `string` | A comment to include |
| `recipients` | `array` | The list of recipients of the forwarding |

### Get a message

Get the detail of a message from the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `user` | `string` | The identifier or the principal name of the user |
| `message_id` | `string` | The identifier of the message to get |

### Update a message

Update a message in the user's mailbox

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `user` | `string` | The identifier or the principal name of the user |
| `message_id` | `string` | The identifier of the message to delete |
| `content` | `string` | The new content of the message |
| `recipients` | `array` | The new list of recipients |
| `bcc` | `array` | The new list of BCC recipients |
| `cc` | `array` | The new list of CC recipients |
| `sender` | `string` | The new sender of the message |
| `from` | `string` | The new mailbox owner of the message (from header) |
| `subject` | `string` | The new subject of the message |
| `importance` | `string` | The importance of the message |


## Extra

Module **`Microsoft Outlook` v0.1.1**