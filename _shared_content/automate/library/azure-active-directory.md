# Azure Active Directory

[Azure Active Directory (Azure AD)](https://azure.microsoft.com/en-us/services/active-directory/#overview) is an enterprise identity service that provides single sign-on, multifactor authentication, and conditional access to guard against 99.9 percent of cybersecurity attacks.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `tenant_id` | `string` | ID of the Azure AD tenant |
| `client_id` | `string` | Client ID. An application needs to be created in the Azure Portal and assigned relevent permissions. Its Client ID should then be used in this configuration. |
| `client_secret` | `string` | Client Secret associated with the registered application. Admin Consent has to be granted to the application for it to work. |

## Actions

### Disable User

Disable an Azure Active Directory user. Requires the User.ReadWrite.All permission.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |

### Enable User

Enable an Azure Active Directory user. Requires the User.ReadWrite.All permission.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |

### Get SignIns

Get the last sign ins of an Azure AD user. Requires the AuditLog.Read.All and Directory.Read.All permissions.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `signIns` | `array` |  |

### Get User

Get information about an Azure Active Directory user. Requires the User.Read.All permission.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |


#### Outputs

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

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `id` | `string` | ID of the user. id or userPrincipalName should be specified. |
| `userPrincipalName` | `string` | Principal Name of the user. id or userPrincipalName should be specified. |


#### Outputs

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


## Extra

Module **`Azure Active Directory` v1.0.0**