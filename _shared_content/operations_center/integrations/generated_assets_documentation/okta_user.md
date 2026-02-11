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
| `id` | `user.uid` | Okta user unique identifier | `string` | Direct mapping of Okta user ID |
| `profile.login` | `user.name` | User login/username (typically email) | `string` | Direct mapping of user login (email format) |
| `profile.firstName + ' ' + profile.lastName` | `user.full_name` | User full name | `string` | Concatenate first and last names |
| `profile.firstName` | `user.first_name` | User first name | `string` | Direct mapping of first name |
| `profile.lastName` | `user.last_name` | User last name | `string` | Direct mapping of last name |
| `profile.login` | `user.account.uid` | Okta account identifier (login/email) | `string` | Direct mapping of user login as account identifier |
| `profile.login` | `user.account.name` | Account username (login) | `string` | Direct mapping of user login |
| `static: Okta` | `user.account.type` | Account type identifier | `string` | Always 'Okta' |
| `static: 42` | `user.account.type_id` | OCSF account type ID | `integer` | Always 42 for Okta account type |
| `profile.email` | `user.email_addr` | User email address | `string` | Direct mapping of email address |
| `profile.mobilePhone` | `user.phone` | User mobile phone number | `string` | Direct mapping of mobile phone number |
| `profile.primaryPhone` | `user.work_phone` | User primary/work phone number | `string` | Direct mapping of primary phone number |
| `profile.department` | `user.department` | User department | `string` | Direct mapping of department attribute |
| `profile.jobTitle` | `user.job_title` | User job title | `string` | Direct mapping of job title |
| `profile.employeeNumber` | `user.employee_id` | Employee ID | `string` | Direct mapping of employee number |
| `profile.city + ', ' + profile.state` | `user.office_location` | Office location | `string` | Concatenate city and state |
| `status` | `user.is_enabled` | Whether user account is enabled (ACTIVE status) | `boolean` | true if status is 'ACTIVE', false otherwise |
| `status` | `user.status` | User account status (ACTIVE, SUSPENDED, DEPROVISIONED, LOCKED_OUT, PASSWORD_EXPIRED, PROVISIONED, STAGED) | `string` | Direct mapping of Okta user status |
| `groupIds | length > 0` | `user.has_groups` | Whether user belongs to any groups | `boolean` | true if user belongs to any group, false otherwise |
| `groupIds` | `user.groups` | Group memberships | `array[object]` | Create Group objects with group ID as uid and name |
| `created` | `user.created_time` | User creation timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch |
| `activated` | `user.activated_time` | User activation timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch; null if not activated |
| `lastLogin` | `user.last_login_time` | Last login timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch; null if never logged in |
| `passwordChanged` | `user.password_last_changed_time` | Password last changed timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch; null if never changed |
| `statusChanged` | `user.status_changed_time` | Status change timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch |
| `lastUpdated` | `user.updated_time` | Last updated timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix epoch |
| `created` | `time` | OCSF event timestamp (user discovery time) | `integer` | Convert ISO 8601 to Unix epoch for OCSF event timestamp |
| `static: 2` | `activity_id` | OCSF activity ID for inventory collection | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Always 'Discovery' |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: User Inventory Info` | `class_name` | OCSF class name | `string` | Always 'User Inventory Info' |
| `static: 5003` | `class_uid` | OCSF class UID | `integer` | Always 5003 for User Inventory Info |
| `computed: 500300 + activity_id` | `type_uid` | OCSF type UID | `integer` | Base 500300 + activity_id (2 = 500302) |
| `computed: class_name + ': ' + activity_name` | `type_name` | OCSF type name | `string` | Concatenate 'User Inventory Info: Collect' |
| `static: Informational` | `severity` | Event severity level | `string` | Always 'Informational' for inventory events |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Always 1 for Informational severity |
| `static: Okta` | `metadata.product.name` | Source product name | `string` | Always 'Okta' |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `status` | `enrichments[0].data.user_status` | Current user account status | `string` | Direct mapping of Okta user status |
| `status` | `enrichments[0].data.is_enabled` | Whether user account is enabled | `boolean` | true if status is 'ACTIVE', false otherwise |
| `lastLogin` | `enrichments[0].data.last_login` | Last login timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix timestamp; return null if never logged in |
| `passwordChanged` | `enrichments[0].data.password_last_changed` | Password last changed timestamp (Unix epoch) | `integer` | Convert ISO 8601 to Unix timestamp; return null if never changed |
| `groupIds | length` | `enrichments[0].data.groups_count` | Number of groups user belongs to | `integer` | Count of group memberships |
| `static: access_control` | `enrichments[0].name` | Enrichment object name | `string` | Always 'access_control' for Okta enrichment type |
| `static: okta` | `enrichments[0].value` | Enrichment object value | `string` | Always 'okta' for Okta user access enrichment |




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
  "time": 1591234567,
  "metadata": {
    "product": {
      "name": "Okta"
    },
    "version": "1.6.0"
  },
  "user": {
    "uid": "00oa1bcdefg2EXAMPLE",
    "name": "mary.jones@example.com",
    "full_name": "Mary Jones",
    "first_name": "Mary",
    "last_name": "Jones",
    "email_addr": "mary.jones@example.com",
    "is_enabled": true,
    "status": "ACTIVE",
    "department": "Finance",
    "job_title": "Financial Analyst",
    "employee_id": "EMP456",
    "office_location": "New York, NY",
    "phone": "+1-555-234-5678",
    "work_phone": "+1-555-234-5678",
    "created_time": 1591234567,
    "activated_time": 1591235100,
    "last_login_time": 1691230000,
    "password_last_changed_time": 1673346000,
    "status_changed_time": 1691230000,
    "updated_time": 1691230000,
    "has_groups": true,
    "account": {
      "uid": "mary.jones@example.com",
      "name": "mary.jones@example.com",
      "type": "Okta",
      "type_id": 42
    },
    "groups": [
      {
        "uid": "00gj3k4l5mnopqrst",
        "name": "Finance Users"
      },
      {
        "uid": "00gh8i9j0klmnopq",
        "name": "All Users"
      }
    ]
  },
  "enrichments": [
    {
      "name": "access_control",
      "value": "okta",
      "data": {
        "user_status": "ACTIVE",
        "is_enabled": true,
        "last_login": 1691230000,
        "password_last_changed": 1673346000,
        "groups_count": 2
      }
    }
  ]
}

```


