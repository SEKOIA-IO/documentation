# Microsoft Entra ID (Azure AD) 

![Microsoft Entra ID (Azure AD) ](/assets/playbooks/library/entra-id.svg){ align=right width=150 }

[Microsoft Entra ID (Azure AD)](https://azure.microsoft.com/en-us/services/active-directory/#overview) is an enterprise identity service that provides single sign-on, multifactor authentication, and conditional access to guard against 99.9 percent of cybersecurity attacks.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `tenant_id` | `string` | ID of the Microsoft Entra ID (Azure AD)  tenant |
| `client_id` | `string` | Client ID. An application needs to be created in the Azure Portal and assigned relevent permissions. Its Client ID should then be used in this configuration. |
| `client_secret` | `string` | Client Secret associated with the registered application. Admin Consent has to be granted to the application for it to work. |
| `username` | `string` | The username of the delegated account used for some administrative tasks (eg: reset password) |
| `password` | `string` | The password of the delegated account used for some administrative tasks (eg: reset password) |

## Actions

### Delete app

Delete an app in Microsoft Entra ID (Azure AD) . Requires the Application.ReadWrite.OwnedBy or Application.ReadWrite.All.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | Object ID of the app. |

### Disable User

Disable an Microsoft Entra ID (Azure AD)  user. Requires the User.ReadWrite.All permission.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |

### Enable User

Enable an Microsoft Entra ID (Azure AD)  user. Requires the User.ReadWrite.All permission.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |

### Get SignIns

Get the last sign ins of an Microsoft Entra ID (Azure AD)  user. Requires the AuditLog.Read.All and Directory.Read.All permissions.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `signIns` | `array` |  |

### Get User

Get information about an Microsoft Entra ID (Azure AD)  user. Requires the User.Read.All permission.

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
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` |  |
| `userPrincipalName` | `string` |  |
| `userDisplayName` | `string` |  |
| `isSsprRegistered` | `boolean` |  |
| `isSsprEnabled` | `boolean` |  |
| `isSsprCapable` | `boolean` |  |
| `isMfaRegistered` | `boolean` |  |
| `isMfaCapable` | `boolean` |  |
| `isPasswordlessCapable` | `boolean` |  |
| `methodsRegistered` | `array` |  |
| `defaultMfaMethod` | `string` |  |

### Reset User Password

Reset a user's password. You will need UserAuthenticationMethod.ReadWrite.All deleguated permission. And to disable the MFA authentication in your Microsoft Entra ID (Azure AD) 

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |
| `userNewPassword` | `string` | [New password](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-password-ban-bad-combined-policy), required to reset the old one of course. |

### Revoke Sign in

Invalidates all the refresh tokens issued to applications for a user. Requires the User.ReadWrite.All or Directory.ReadWrite.All permissions.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the app. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |


## Extra

Module **`Microsoft Entra ID (Azure AD) ` v2.5.4**
