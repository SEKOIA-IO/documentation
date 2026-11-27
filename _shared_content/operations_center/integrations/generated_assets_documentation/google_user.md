## OCSF Mapping for Google Workspace Users


**OCSF Class:** `User Inventory Info`



**Class UID:** `5003`



**OCSF Version:** `1.6.0`


## Information Collected

The Google Workspace Users connector fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### Administrator with organization
Google Workspace user returned by the Directory API users.list endpoint, member of the Engineering group

```json
{
  "kind": "admin#directory#user",
  "id": "100000000000000000001",
  "etag": "\"etag-1\"",
  "primaryEmail": "jane.doe@example.com",
  "name": {
    "givenName": "Jane",
    "familyName": "Doe",
    "fullName": "Jane Doe",
    "displayName": "Jane D."
  },
  "isAdmin": true,
  "isDelegatedAdmin": false,
  "suspended": false,
  "archived": false,
  "isEnrolledIn2Sv": true,
  "isEnforcedIn2Sv": false,
  "lastLoginTime": "2026-09-28T08:15:00.000Z",
  "creationTime": "2021-03-01T10:00:00.000Z",
  "orgUnitPath": "/Engineering",
  "organizations": [
    {
      "name": "Example Corp",
      "title": "CTO",
      "department": "Engineering",
      "location": "Paris",
      "primary": true
    }
  ],
  "externalIds": [
    {
      "type": "organization",
      "value": "E-42"
    }
  ],
  "customerId": "C00000000"
}

```

#### Group
Group returned by the Directory API groups.list endpoint. Its members come from members.list

```json
{
  "kind": "admin#directory#group",
  "id": "000000000000001",
  "email": "engineering@example.com",
  "name": "Engineering",
  "description": "Engineers",
  "directMembersCount": "12"
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `static: 2` | `activity_id` | OCSF activity ID – always 2 for Collect | `integer` | Static value |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Static value |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Static value |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Static value |
| `static: User Inventory Info` | `class_name` | OCSF class name | `string` | Static value |
| `static: 5003` | `class_uid` | OCSF class UID | `integer` | Static value |
| `static: User Inventory Info: Collect` | `type_name` | OCSF type name | `string` | Static value |
| `static: 500302` | `type_uid` | OCSF type UID | `integer` | Static value |
| `static: Informational` | `severity` | Event severity | `string` | Static value |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Static value |
| `static: Google Workspace` | `metadata.product.name` | Source product name | `string` | Static value |
| `static: Google` | `metadata.product.vendor_name` | Source product vendor | `string` | Static value |
| `static: N/A` | `metadata.product.version` | Product version | `string` | Static value |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Static value |
| `creationTime` | `time` | Creation date of the user | `timestamp` | Parse ISO-8601 timestamp; convert to Unix epoch float |
| `id` | `user.uid` | Unique Google Workspace user identifier | `string` | Direct mapping |
| `primaryEmail` | `user.name / user.email_addr` | Primary email address, used as login | `string` | Direct mapping |
| `primaryEmail (part after '@')` | `user.domain` | Google Workspace domain of the user | `string` | Domain of the primary email address |
| `name.fullName` | `user.full_name` | Full name of the user | `string` | Direct mapping |
| `name.displayName` | `user.display_name` | Display name of the user | `string` | Direct mapping |
| `isEnrolledIn2Sv` | `user.has_mfa` | Whether the user is enrolled in 2-step verification | `boolean` | Direct mapping |
| `isAdmin || isDelegatedAdmin` | `user.type_id / user.type` | OCSF user type | `integer / string` | Super administrator or delegated administrator → 2 / Admin, otherwise 1 / User |
| `id + primaryEmail` | `user.account` | Google Workspace account of the user | `object` | uid=id, name=primaryEmail, type_id=15 / type=Google Workspace |
| `groups.list + members.list` | `user.groups[]` | Google Workspace group memberships | `array` | Groups the user is a direct member of (member type USER), plus the groups whose member is the whole customer (member type CUSTOMER): uid=group id, name=group name (fallback: group email), desc=group description (omitted when empty). Sorted by uid; omitted when the user has no group. EXTERNAL and GROUP members are ignored |
| `organizations[primary].name (fallback: user.domain)` | `user.org.name` | Organization of the user | `string` | Name of the primary organization, or the first one when none is flagged primary; the email domain when the user has no organization |
| `orgUnitPath` | `user.org.ou_name` | Organizational unit of the user in Google Workspace | `string` | Direct mapping |
| `name.givenName` | `user.ldap_person.given_name` | Given name of the user | `string` | Direct mapping |
| `name.familyName` | `user.ldap_person.surname` | Family name of the user | `string` | Direct mapping |
| `organizations[primary].title` | `user.ldap_person.job_title` | Job title of the user | `string` | Title in the primary organization |
| `organizations[primary].department` | `user.ldap_person.department` | Department of the user | `string` | Department in the primary organization |
| `organizations[primary].location` | `user.ldap_person.office_location` | Office location of the user | `string` | Location in the primary organization |
| `externalIds[type=organization].value` | `user.ldap_person.employee_uid` | Employee identifier | `string` | Value of the first external id of type organization |
| `static: access_control / google_workspace` | `enrichments[0].name / enrichments[0].value` | Enrichment describing the account state | `string` | Static value |
| `suspended, archived` | `enrichments[0].data.is_enabled` | Whether the account can be used | `boolean` | False when the user is suspended or archived, True otherwise |
| `lastLoginTime` | `enrichments[0].data.last_logon` | Date of the last login | `string` | Direct mapping; omitted when the user never logged in (1970-01-01T00:00:00.000Z) |




### OCSF Model Structure

#### Administrator with organization – OCSF output
Transformed OCSF UserOCSFModel for the administrator sample, member of the Engineering group

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
  "time": 1614592800.0,
  "metadata": {
    "product": {
      "name": "Google Workspace",
      "vendor_name": "Google",
      "version": "N/A"
    },
    "version": "1.6.0"
  },
  "user": {
    "has_mfa": true,
    "name": "jane.doe@example.com",
    "uid": "100000000000000000001",
    "account": {
      "name": "jane.doe@example.com",
      "type_id": 15,
      "type": "Google Workspace",
      "uid": "100000000000000000001"
    },
    "groups": [
      {
        "name": "Engineering",
        "desc": "Engineers",
        "uid": "000000000000001"
      }
    ],
    "full_name": "Jane Doe",
    "email_addr": "jane.doe@example.com",
    "display_name": "Jane D.",
    "domain": "example.com",
    "type_id": 2,
    "type": "Admin",
    "org": {
      "name": "Example Corp",
      "ou_name": "/Engineering"
    },
    "ldap_person": {
      "job_title": "CTO",
      "department": "Engineering",
      "employee_uid": "E-42",
      "given_name": "Jane",
      "surname": "Doe",
      "office_location": "Paris"
    }
  },
  "enrichments": [
    {
      "name": "access_control",
      "value": "google_workspace",
      "data": {
        "is_enabled": true,
        "last_logon": "2026-09-28T08:15:00.000Z"
      }
    }
  ]
}

```


