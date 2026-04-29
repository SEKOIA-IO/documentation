## OCSF Mapping for Microsoft Active Directory Users


**OCSF Class:** `User Inventory Info`



**Class UID:** `5003`




## Information Collected

The Microsoft Active Directory Users fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### Active Directory Active User
Active Directory user with console access and group membership

```json
{
  "objectSid": "S-1-5-21-3623811015-3361044348-30300820-1013",
  "userPrincipalName": "mary.jones@example.com",
  "displayName": "Mary Jones",
  "givenName": "Mary",
  "sn": "Jones",
  "mail": "mary.jones@example.com",
  "objectGUID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "userAccountControl": 512,
  "memberOf": [
    "CN=Finance Users,OU=Groups,DC=example,DC=com",
    "CN=All Users,OU=Groups,DC=example,DC=com"
  ],
  "department": "Finance",
  "title": "Financial Analyst",
  "employeeID": "EMP456",
  "physicalDeliveryOfficeName": "New York, NY",
  "mobile": "+1-555-234-5678",
  "telephoneNumber": "+1-555-234-5678",
  "distinguishedName": "CN=mary.jones,OU=Users,DC=example,DC=com",
  "whenCreated": "20200604100000.0Z",
  "whenChanged": "20250826093000.0Z",
  "lastLogonTimestamp": "20250826093000.0Z",
  "pwdLastSet": "20250101110000.0Z",
  "accountExpires": "0",
  "lastLogon": "20250826093000.0Z",
  "badPwdCount": 0,
  "logonCount": 156
}

```

#### Active Directory Disabled User
Active Directory user with account disabled and expired

```json
{
  "objectSid": "S-1-5-21-3623811015-3361044348-30300820-1014",
  "userPrincipalName": "robert.smith@example.com",
  "displayName": "Robert Smith",
  "givenName": "Robert",
  "sn": "Smith",
  "mail": "robert.smith@example.com",
  "objectGUID": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "userAccountControl": 514,
  "memberOf": [
    "CN=Engineering Users,OU=Groups,DC=example,DC=com"
  ],
  "department": "Engineering",
  "title": "Senior Software Engineer",
  "employeeID": "EMP789",
  "physicalDeliveryOfficeName": "San Francisco, CA",
  "mobile": "+1-555-345-6789",
  "telephoneNumber": "+1-555-345-6789",
  "distinguishedName": "CN=robert.smith,OU=Users,DC=example,DC=com",
  "whenCreated": "20200604100000.0Z",
  "whenChanged": "20250818150000.0Z",
  "lastLogonTimestamp": "20250610140000.0Z",
  "pwdLastSet": "20210101120000.0Z",
  "accountExpires": "20240826150000.0Z",
  "lastLogon": "20250610140000.0Z",
  "badPwdCount": 3,
  "logonCount": 89
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `static: 2` | `activity_id` | OCSF activity ID for inventory collection | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' |
| `static: Collect` | `category_name` | OCSF category name | `string` | Always 'Collect' (OCSF_CATEGORY_NAME constant) |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: User Inventory Info` | `class_name` | OCSF class name | `string` | Always 'User Inventory Info' |
| `static: 5003` | `class_uid` | OCSF class UID | `integer` | Always 5003 for User Inventory Info |
| `static: 500302` | `type_uid` | OCSF type UID | `integer` | Always 500302 (OCSF_TYPE_UID constant) |
| `static: User Inventory` | `type_name` | OCSF type name | `string` | Always 'User Inventory' (OCSF_TYPE_NAME constant) |
| `static: Informational` | `severity` | Event severity level | `string` | Always 'Informational' for inventory events |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Always 1 for Informational severity |
| `whenCreated` | `time` | OCSF event timestamp (user creation time) | `integer` | Convert LDAP generalized time (YYYYMMDDhhmmss.0Z) to Unix timestamp for OCSF event timestamp |
| `static: Microsoft Active Directory` | `metadata.product.name` | Source product name | `string` | Always 'Microsoft Active Directory' |
| `static: Microsoft` | `metadata.product.vendor_name` | Source product vendor name | `string` | Always 'Microsoft' |
| `static: N/A` | `metadata.product.version` | Product version | `string` | Always 'N/A' (PRODUCT_VERSION constant) |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `objectSid` | `user.uid` | Active Directory user unique identifier (SID) | `string` | Direct mapping of user SID (Security Identifier) |
| `givenName + ' ' + sn` | `user.name` | User full name built from first and last name | `string` | Concatenate givenName and sn; fallback to givenName only, sn only, or 'Unknown' if both absent |
| `displayName` | `user.full_name` | User full name (from displayName attribute) | `string` | Direct mapping of display name as full name |
| `displayName` | `user.display_name` | User display name (User.display_name) | `string` | Direct mapping of display name |
| `mail` | `user.email_addr` | User email address | `string` | Direct mapping of email address |
| `distinguishedName` | `user.domain` | User domain (stored as full DN) | `string` | Direct mapping of distinguished name as domain reference |
| `objectGUID` | `user.uid_alt` | Active Directory user GUID (alternative UID) | `string` | Direct mapping of GUID; strip surrounding curly braces if present |
| `memberOf` | `user.type` | User type (UserTypeStr): Admin if in an admin group, else User | `string` | Iterate memberOf DNs; if any contains 'admin' (case-insensitive) -> UserTypeStr.ADMIN ('Admin'), else -> UserTypeStr.USER ('User') |
| `memberOf` | `user.type_id` | OCSF user type ID (UserTypeId) | `integer` | Derive from type: Admin -> UserTypeId.ADMIN (2), User -> UserTypeId.USER (1) |
| `objectSid` | `user.account.uid` | Account UID (objectSid) | `string` | Direct mapping of objectSid as account UID |
| `userPrincipalName` | `user.account.name` | User principal name (UPN) as account name | `string` | Direct mapping of user principal name |
| `static: LDAP Account` | `user.account.type` | Account type string | `string` | Always 'LDAP Account' (AccountTypeStr.LDAP_ACCOUNT) |
| `static: 1` | `user.account.type_id` | OCSF account type ID | `integer` | Always 1 for LDAP Account (AccountTypeId.LDAP_ACCOUNT) |
| `memberOf` | `user.groups` | Group memberships (Group.name = full DN) | `array[object]` | Create Group objects from memberOf list; each Group.name is set to the full DN string |
| `static: login` | `enrichments[0].name` | Enrichment object name | `string` | Always 'login' for user enrichment type |
| `static: infos` | `enrichments[0].value` | Enrichment object value | `string` | Always 'infos' (UserEnrichmentObject.value constant) |
| `userAccountControl` | `enrichments[0].data.is_enabled` | Whether user account is enabled (UserDataObject.is_enabled) | `boolean` | Compute account enabled status: enabled = not (userAccountControl & 2) |
| `lastLogon` | `enrichments[0].data.last_logon` | Last logon as string timestamp (UserDataObject.last_logon) | `string` | Convert lastLogon datetime to string Unix timestamp; return null if year <= 1601 or invalid |
| `badPwdCount` | `enrichments[0].data.bad_password_count` | Number of failed password attempts (UserDataObject.bad_password_count) | `integer` | Direct mapping of bad password attempt count |
| `logonCount` | `enrichments[0].data.number_of_logons` | Total number of logons (UserDataObject.number_of_logons) | `integer` | Direct mapping of logon count |




### OCSF Model Structure

#### User Inventory Info: Collect
Transformed AD user to OCSF User Inventory Info event

```json
{
  "activity_id": 2,
  "activity_name": "Collect",
  "category_name": "Discovery",
  "category_uid": 5,
  "class_name": "User Inventory Info",
  "class_uid": 5003,
  "type_name": "User Inventory Info: Collect",
  "type_uid": 500302,
  "severity": "Informational",
  "severity_id": 1,
  "time": 1591234567,
  "metadata": {
    "product": {
      "name": "Microsoft Active Directory"
    },
    "version": "1.6.0"
  },
  "user": {
    "uid": "S-1-5-21-3623811015-3361044348-30300820-1013",
    "name": "Mary Jones",
    "full_name": "Mary Jones",
    "email_addr": "mary.jones@example.com",
    "is_enabled": true,
    "domain": "example.com",
    "department": "Finance",
    "job_title": "Financial Analyst",
    "employee_id": "EMP456",
    "office_location": "New York, NY",
    "phone": "+1-555-234-5678",
    "work_phone": "+1-555-234-5678",
    "created_time": 1591234567,
    "updated_time": 1691234000,
    "last_login_time": 1691230000,
    "password_last_changed_time": 1681234567,
    "has_groups": true,
    "account": {
      "uid": "CN=mary.jones,OU=Users,DC=example,DC=com",
      "name": "mary.jones@example.com",
      "type": "LDAP",
      "type_id": 4000
    },
    "groups": [
      {
        "uid": "CN=Finance Users,OU=Groups,DC=example,DC=com",
        "name": "Finance Users"
      }
    ],
    "uid_alt": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  },
  "enrichments": [
    {
      "name": "login",
      "value": "account_security",
      "data": {
        "is_enabled": true,
        "last_logon": 1691230000,
        "bad_password_count": 0,
        "number_of_logons": 156
      }
    }
  ]
}

```


