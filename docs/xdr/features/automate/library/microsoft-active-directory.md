uuid: b2d96259-af89-4f7a-ae6e-a0af2d2400f3
name: Microsoft Active Directory
type: playbook

# Microsoft Active Directory

![Microsoft Active Directory](/assets/playbooks/library/microsoft-active-directory.png){ align=right width=150 }

Microsoft Active Directory (Microsoft AD), is a directory service developed by Microsoft for Windows domain networks. It is a centralized system that stores information about networked resources and makes these resources easily accessible to users and administrators. Active Directory provides services for authentication and authorization, organizing and managing resources, such as users, computers, and devices, in a networked environment.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `servername` | `string` | IP or name of your host |
| `admin_username` | `string` | The username of the account that have necessary permisions to change passwords (e.g admin@example.com ) |
| `admin_password` | `string` | The dedicated password of the account |

## Actions

### Disable User

Disable a Microsoft Active Directory user.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `username` | `string` | Target user |
| `basedn` | `string` | The starting point an LDAP server uses when searching for users authentication within your Directory. (e.g DC=example-domain,DC=com) |
| `email` | `string` | Filter by email address (mail attribute) to narrow results when multiple users share the same name |
| `apply_to_all` | `boolean` | When true, apply action to all matching users instead of failing when multiple users are found |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected_users` | `array` | List of users affected by the action (only when apply_to_all is true) |
| `total_found` | `integer` |  |
| `total_success` | `integer` |  |
| `total_failed` | `integer` |  |

### Enable User

Enable a Microsoft Active Directory user.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `username` | `string` | Target user |
| `basedn` | `string` | The starting point an LDAP server uses when searching for users authentication within your Directory. (e.g DC=example-domain,DC=com) |
| `email` | `string` | Filter by email address (mail attribute) to narrow results when multiple users share the same name |
| `apply_to_all` | `boolean` | When true, apply action to all matching users instead of failing when multiple users are found |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected_users` | `array` | List of users affected by the action (only when apply_to_all is true) |
| `total_found` | `integer` |  |
| `total_success` | `integer` |  |
| `total_failed` | `integer` |  |

### Reset User Password

Reset a user's password. You will need a strong password for that otherwise enable the password policy

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `username` | `string` | Target user |
| `basedn` | `string` | The starting point an LDAP server uses when searching for users authentication within your Directory. (e.g DC=example-domain,DC=com) |
| `new_password` | `string` | New password, required to reset the old one of course. |
| `email` | `string` | Filter by email address (mail attribute) to narrow results when multiple users share the same name |
| `apply_to_all` | `boolean` | When true, apply action to all matching users instead of failing when multiple users are found |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `affected_users` | `array` | List of users affected by the action (only when apply_to_all is true) |
| `total_found` | `integer` |  |
| `total_success` | `integer` |  |
| `total_failed` | `integer` |  |

### Search in AD

Search in AD

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `search_filter` | `string` | LDAP filter to run your query on  see https://ldap3.readthedocs.io/en/latest/searches.html#the-ldap-filter) |
| `basedn` | `string` | The starting point an LDAP server uses when searching for users authentication within your Directory. (e.g DC=example-domain,DC=com) |
| `attributes` | `` | Attributes you want to retrieve (default will be ALL)  |
| `to_file` | `boolean` | Whether the event should be saved in a file or sent directly |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `search_result` | `array` |  |
| `output_path` | `object` | Path to the file with the content |

### Synchronize AD assets with Sekoia.io

Run one fetch cycle of the Microsoft Active Directory user asset connector as an action. Reads users from Active Directory and pushes them as assets to the matching asset connector configuration in Sekoia.io. Designed to run on an on-premise runner so Active Directory is never exposed to Sekoia.io.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `asset_connector_uuid` | `string` | UUID of the asset connector configuration to push the assets to, and that owns the checkpoint and the logs |
| `connector_configuration_token` | `string` | Token used to send the connector logs to Sekoia.io |
| `basedn` | `string` | The base distinguished name (DN) to use for LDAP queries (e.g DC=example-domain,DC=com) |
| `sekoia_base_url` | `string` | Base URL of the Sekoia.io API of your region |
| `sekoia_api_key` | `string` | API key allowed to push assets to the asset connector |
| `batch_size` | `integer` | Number of assets to send in each batch to Sekoia.io |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `fetched` | `integer` | Number of assets fetched from Active Directory during the cycle |
| `pushed_batches` | `integer` | Number of asset batches successfully pushed to Sekoia.io |
| `failed_batches` | `integer` | Number of asset batches that could not be pushed to Sekoia.io. The cycle stops at the first failure, the run ends in error and the next scheduled run restarts from the previous checkpoint |
| `has_more` | `boolean` | Whether the cycle was interrupted before its end and the action should run again to resume |


## Extra

Module **`Microsoft Active Directory` v1.6.5**