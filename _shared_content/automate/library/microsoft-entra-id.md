uuid: 3abf7928-65ef-4a5f-ba3e-5fbe56123d0c
name: Microsoft Entra ID
type: playbook

# Microsoft Entra ID

![Microsoft Entra ID](/assets/playbooks/library/microsoft-entra-id.png){ align=right width=150 }

Microsoft Entra ID (formely Azure Active Directory) is an enterprise identity service that provides single sign-on, multifactor authentication, and conditional access to guard against 99.9 percent of cybersecurity attacks.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `tenant_id` | `string` | ID of the Microsoft Entra ID tenant |
| `client_id` | `string` | Client ID. An application needs to be created in the Azure Portal and assigned relevent permissions. Its Client ID should then be used in this configuration. |
| `client_secret` | `string` | Client Secret associated with the registered application. Admin Consent has to be granted to the application for it to work. |
| `username` | `string` | The username of the delegated account used for some administrative tasks (eg: reset password) |
| `password` | `string` | The password of the delegated account used for some administrative tasks (eg: reset password) |

## Actions

### Delete app

Delete an app in azure AD. Requires the Application.ReadWrite.OwnedBy or Application.ReadWrite.All.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Object ID of the app. |

### Disable User

Disable an Azure Active Directory user. Requires the User.ReadWrite.All permission.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |

### Enable User

Enable an Azure Active Directory user. Requires the User.ReadWrite.All permission.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |

### Get SignIns

Get the last sign ins of an Azure AD user. Requires the AuditLog.Read.All and Directory.Read.All permissions.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `signIns` | `array` |  |

### Get User

Get information about an Azure Active Directory user. Requires the User.Read.All permission.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` |  |
| `accountEnabled` | `boolean` |  |
| `assignedLicenses` | `array` |  |
| `city` | `string` |  |
| `companyName` | `string` |  |
| `country` | `string` |  |
| `createdDateTime` | `string` |  |
| `creationType` | `string` |  |
| `deletedDateTime` | `string` |  |
| `department` | `string` |  |
| `displayName` | `string` |  |
| `identities` | `array` |  |
| `jobTitle` | `string` |  |
| `lastPasswordChangeDateTime` | `string` |  |
| `mail` | `string` |  |
| `mobilePhone` | `string` |  |
| `userPrincipalName` | `string` |  |

### Get User Authentication Methods

Get information about an user's authentication methods (such as their MFA status). Requires the UserAuthenticationMethod.Read.All permission.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `userPrincipalName` | `string` | Principal name of the user, which may correspond to their Azure email address. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `authenticationResults` | `array` |  |

### Reset User Password

Reset a user's password. You will need UserAuthenticationMethod.ReadWrite.All deleguated permission. And to disable the MFA authentication in your azure AD

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |
| `userNewPassword` | `string` | New password, required to reset the old one of course. |

### Revoke Sign in

Invalidates all the refresh tokens issued to applications for a user. Requires the User.ReadWrite.All or Directory.ReadWrite.All permissions.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the app. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |


## Extra

Module **`Microsoft Entra ID` v2.8.5**