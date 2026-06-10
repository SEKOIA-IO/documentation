## OCSF Mapping for Okta Users


**OCSF Class:** `User Inventory Info`



**Class UID:** `5003`




## Information Collected

The Okta Users fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### Okta Active User
Okta user with active status and group membership

```json
{
  "id": "00oa1bcdefg2EXAMPLE",
  "status": "ACTIVE",
  "created": "2020-06-04T10:00:00.000Z",
  "activated": "2020-06-04T10:15:00.000Z",
  "statusChanged": "2025-08-26T09:30:00.000Z",
  "lastLogin": "2025-08-26T09:30:00.000Z",
  "lastUpdated": "2025-08-26T09:30:00.000Z",
  "passwordChanged": "2025-01-10T11:00:00.000Z",
  "profile": {
    "firstName": "Mary",
    "lastName": "Jones",
    "email": "mary.jones@example.com",
    "login": "mary.jones@example.com",
    "mobilePhone": "+1-555-234-5678",
    "primaryPhone": "+1-555-234-5678",
    "department": "Finance",
    "jobTitle": "Financial Analyst",
    "employeeNumber": "EMP456",
    "city": "New York",
    "state": "NY",
    "country": "USA"
  },
  "groupIds": [
    "00gj3k4l5mnopqrst",
    "00gh8i9j0klmnopq"
  ],
  "_links": {
    "self": [
      {
        "href": "https://example.okta.com/api/v1/users/00oa1bcdefg2EXAMPLE"
      }
    ]
  }
}

```

#### Okta Suspended User
Okta user with suspended status

```json
{
  "id": "00oa2cdefgh3EXAMPLE",
  "status": "SUSPENDED",
  "created": "2020-06-04T10:00:00.000Z",
  "activated": "2020-06-04T10:15:00.000Z",
  "statusChanged": "2025-06-10T14:00:00.000Z",
  "lastLogin": "2025-06-10T14:00:00.000Z",
  "lastUpdated": "2025-06-10T14:00:00.000Z",
  "passwordChanged": "2021-01-15T09:00:00.000Z",
  "profile": {
    "firstName": "Robert",
    "lastName": "Smith",
    "email": "robert.smith@example.com",
    "login": "robert.smith@example.com",
    "mobilePhone": "+1-555-345-6789",
    "primaryPhone": "+1-555-345-6789",
    "department": "Engineering",
    "jobTitle": "Senior Software Engineer",
    "employeeNumber": "EMP789",
    "city": "San Francisco",
    "state": "CA",
    "country": "USA"
  },
  "groupIds": [
    "00gj3k4l5mnopqrst"
  ],
  "_links": {
    "self": [
      {
        "href": "https://example.okta.com/api/v1/users/00oa2cdefgh3EXAMPLE"
      }
    ]
  }
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `static: 2` | `activity_id` | OCSF activity ID for inventory collection | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Always 'Discovery' |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: User Inventory Info` | `class_name` | OCSF class name | `string` | Always 'User Inventory Info' |
| `static: 5003` | `class_uid` | OCSF class UID | `integer` | Always 5003 for User Inventory Info |
| `static: 500302` | `type_uid` | OCSF type UID | `integer` | Always 500302 for User Inventory Info: Collect type |
| `static: User Inventory Info: Collect` | `type_name` | OCSF type name | `string` | Always 'User Inventory Info: Collect' |
| `static: Informational` | `severity` | Event severity level | `string` | Always 'Informational' for inventory events |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Always 1 for Informational severity |
| `created` | `time` | OCSF event timestamp (user discovery time) | `integer` | Convert ISO 8601 to Unix epoch for OCSF event timestamp |
| `static: Okta` | `metadata.product.name` | Source product name | `string` | Always 'Okta' |
| `static: Okta` | `metadata.product.vendor_name` | Source product vendor name | `string` | Always 'Okta' |
| `static: N/A` | `metadata.product.version` | Source product version | `string` | Always 'N/A' since Okta is a SaaS product without traditional versioning |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `id` | `user.uid` | Okta user unique identifier | `string` | Direct mapping of Okta user ID |
| `calculated: profile.firstName and profile.lastName` | `user.full_name` | User full name | `string` | Concatenate first and last names |
| `profile.email` | `user.email_addr` | User email address | `string` | Direct mapping of email address |
| `profile.login` | `user.name` | User login/username (typically email) | `string` | Direct mapping of user login |
| `profile.login` | `user.account.name` | Account username (login) | `string` | Direct mapping of user login |
| `static: OTHER` | `user.account.type` | Account type identifier | `string` | Always 'OTHER' for Okta account type |
| `static: 99` | `user.account.type_id` | OCSF account type ID | `integer` | Always 99 for Okta account type |
| `id` | `user.account.uid` | Idential Okta user ID for account correlation | `string` | Direct mapping of Okta user ID as account UID for correlation |
| `group.id` | `user.groups[].uid` | Group unique identifier | `string` | Direct mapping of Okta group ID to group UID in user groups array |
| `group.profile.name` | `user.groups[].name` | Group name | `string` | Direct mapping of Okta group name to group name in user groups array |
| `group.profile.description` | `user.groups[].desc` | Group description | `string` | Direct mapping of Okta group description to group description in user groups array |
| `id` | `user.has_mfa` | MFA enrollment status | `boolean` | True if user has any MFA factors enrolled, false otherwise (requires additional API call to check factors) |
| `profile.displayName` | `user.display_name` | User display name | `string` | Direct mapping of display name |
| `calculated: profile.email` | `user.domain` | User domain | `string` | Extract domain from email address, otherwise set to null |
| `profile.login` | `user.uid_alt` | Alternate user identifier (login/email) for correlation | `string` | Direct mapping of user login as alternate UID for correlation |
| `calculated: roles assigned to user` | `user.type_id` | User type ID  | `integer` | If user has admin roles, set to 'Admin'; otherwise set to 'None' |
| `calculated: roles assigned to user` | `user.type` | User type | `string` | If user has admin roles, set to 'Admin'; otherwise set to 'None' |
| `profile.organization` | `user.org.name` | Organization name | `string` | Use Okta profile.organization if present and string, else fall back to email domain |
| `profile.department` | `user.org.ou_name` | Organizational unit name | `string` | Use Okta profile.department if present and string, else set to null |
| `static: access_control` | `enrichments[].name` | Enrichment name for access control insights | `string` | Always 'access_control' for this enrichment |
| `static: okta` | `enrichments[].value` | Enrichment value indicating Okta as source | `string` | Always 'okta' to indicate enrichment source |
| `calculated: is user account enabled in Okta` | `enrichments[].data.is_enabled` | Indicates if the user account is currently enabled in Okta | `boolean` | True if user status is 'ACTIVE', false otherwise |
| `lastLogin` | `enrichments[].data.last_logon` | The last time the user logged in according to Okta | `string` | Map Okta lastLogin timestamp to enrichment data for last logon time |
| `passwordChanged` | `enrichments[].data.last_time_password_change` | The last time the user changed their password according to Okta | `integer` | Convert Okta passwordChanged timestamp to Unix epoch for enrichment data |




### OCSF Model Structure

#### User Inventory Info: Collect
Transformed Okta user to OCSF User Inventory Info event

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
  "time": 1591234567.0,
  "metadata": {
    "product": {
      "name": "Okta",
      "vendor_name": "Okta",
      "version": "N/A"
    },
    "version": "1.6.0"
  },
  "user": {
    "uid": "00oa1bcdefg2EXAMPLE",
    "name": "mary.jones@example.com",
    "full_name": "Mary Jones",
    "display_name": "Mary Jones",
    "email_addr": "mary.jones@example.com",
    "uid_alt": "mary.jones@example.com",
    "domain": "example.com",
    "has_mfa": true,
    "type_id": null,
    "type": null,
    "account": {
      "uid": "00oa1bcdefg2EXAMPLE",
      "name": "mary.jones@example.com",
      "type": "Other",
      "type_id": 99
    },
    "org": {
      "name": "example.com",
      "ou_name": "Finance"
    },
    "groups": [
      {
        "uid": "00gj3k4l5mnopqrst",
        "name": "Finance Users",
        "desc": "Finance department group",
        "privileges": []
      }
    ]
  },
  "enrichments": [
    {
      "name": "access_control",
      "value": "okta",
      "data": {
        "is_enabled": true,
        "last_logon": "2025-08-26T09:30:00.000Z",
        "last_time_password_change": 1736507400.0
      }
    }
  ]
}

```


