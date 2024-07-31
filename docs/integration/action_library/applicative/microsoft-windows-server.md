# Microsoft Windows Server

![Microsoft Windows Server](/assets/playbooks/library/microsoft-windows-server.png){ align=right width=150 }

Microsoft Windows Server is an operating system designed for server-based computing, offering robust server management, data storage, and networking capabilities for businesses and enterprises, facilitating diverse workloads and IT operations.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `server` | `string` | Remote server dns name or IP address |
| `username` | `string` | Username to do authentication on remote server |
| `password` | `string` | Password to do authentication on remote server |

## Actions

### Change User Password

Changes specified user password on remote server

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `user_to_update` | `string` | Username you want to change password for |
| `new_password` | `string` | New password for user |

### Disable Users

Disable specified users on remote server

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `users` | `array` | List of user names to disable. `sids` or `users` must be specified |
| `sids` | `array` | List of SID`s to disable. `sids` or `users` must be specified |

### Enable Users

Enable specified users on remote server

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `users` | `array` | List of user names to enable. `sids` or `users` must be specified |
| `sids` | `array` | List of SID`s to enable. `sids` or `users` must be specified |


## Extra

Module **`Microsoft Windows Server` v1.0.3**