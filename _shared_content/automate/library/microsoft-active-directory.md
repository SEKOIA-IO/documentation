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

### Enable User

Enable a Microsoft Active Directory user.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `username` | `string` | Target user |
| `basedn` | `string` | he starting point an LDAP server uses when searching for users authentication within your Directory. (e.g DC=example-domain,DC=com) |

### Reset User Password

Reset a user's password. You will need a strong password for that otherwise enable the password policy

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `username` | `string` | Target user |
| `basedn` | `string` | The starting point an LDAP server uses when searching for users authentication within your Directory. (e.g DC=example-domain,DC=com) |
| `new_password` | `string` | New password, required to reset the old one of course. |

### Search in AD

Search in AD

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `search_filter` | `string` | LDAP filter to run your query on  see https://ldap3.readthedocs.io/en/latest/searches.html#the-ldap-filter) |
| `basedn` | `string` | The starting point an LDAP server uses when searching for users authentication within your Directory. (e.g DC=example-domain,DC=com) |
| `attributes` | `` | Attributes you want to retrieve (default will be ALL)  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `search_result` | `array` |  |


## Extra

Module **`Microsoft Active Directory` v1.3.7**