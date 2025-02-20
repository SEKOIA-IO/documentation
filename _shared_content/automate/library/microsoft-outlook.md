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

Module **`Microsoft Outlook` v0.1.1**