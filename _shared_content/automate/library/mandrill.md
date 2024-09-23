# Mandrill

![Mandrill](/assets/playbooks/library/mandrill.svg){ align=right width=150 }

Mandrill is a transactional email platform from Mailchimp.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `apikey` | `string` | APIKEY for Mandrill |

## Actions

### Send Message

Send a new transactional message through Mandrill

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `message` | `object` | The information on the message to send |
| `async` | `boolean` | Enable a background sending mode that is optimized for bulk sending. In async mode, messages/send will immediately return a status of 'queued' for every recipient. To handle rejections when sending in async mode, set up a webhook for the 'reject' event. Defaults to false for messages with no more than 10 recipients; messages with more than 10 recipients are always sent asynchronously, regardless of the value of async. |
| `ip_pool` | `string` | The name of the dedicated ip pool that should be used to send the message. If you do not have any dedicated IPs, this parameter has no effect. If you specify a pool that does not exist, your default pool will be used instead. |
| `send_at` | `string` | When this message should be sent as a UTC timestamp in YYYY-MM-DD HH:MM:SS format. If you specify a time in the past, the message will be sent immediately. An additional fee applies for scheduled email, and this feature is only available to accounts with a positive balance. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `report` | `array` | An array of structs for each recipient containing the key 'email' with the email address, and details of the message status for that recipient |


## Extra

Module **`Mandrill` v2.10.0**