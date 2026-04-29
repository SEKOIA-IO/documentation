## OCSF Mapping for CrowdStrike Falcon Users


**OCSF Class:** `User Inventory Info`



**Class UID:** `5003`



**OCSF Version:** `1.6.0`


## Information Collected

The CrowdStrike Falcon Users fetches comprehensive information and transforms it into the OCSF (Open Cybersecurity Schema Framework) format for standardized security monitoring and asset management.


### API Response Examples

#### CrowdStrike Active Directory Administrator
Built-in administrator account from Active Directory with admin role

```json
{
  "entityId": "1c08759a-e6be-4858-8174-b308855541e9",
  "type": "USER",
  "primaryDisplayName": "administrateur",
  "secondaryDisplayName": "EXAMPLE.COM\\administrateur",
  "creationTime": "2024-10-21T09:19:20.000Z",
  "riskScore": 0.66,
  "riskScoreSeverity": "MEDIUM",
  "hasRole": true,
  "learned": false,
  "accounts": [
    {
      "dataSource": "ACTIVE_DIRECTORY",
      "domain": "EXAMPLE.COM",
      "samAccountName": "administrateur",
      "objectSid": "S-1-5-21-947947667-100116589-3603791262-500",
      "objectGuid": "1c08759a-e6be-4858-8174-b308855541e9",
      "enabled": true,
      "cn": "administrateur",
      "consistencyGuid": null,
      "description": "Built-in account for administering the computer/domain",
      "department": null,
      "title": null
    }
  ],
  "emailAddresses": [],
  "roles": [
    {
      "type": "BuiltinAdministratorRole"
    },
    {
      "type": "ProgrammaticUserAccountRole"
    }
  ]
}

```





### Data Mapping Table

The following table shows how source data is mapped to OCSF model fields:

| Source Field | OCSF Field Path | Description | Data Type | Logic |
|--------------|-----------------|-------------|-----------|-------|
| `static: 2` | `activity_id` | OCSF activity ID for inventory collection | `integer` | Always 2 for 'Collect' activity |
| `static: Collect` | `activity_name` | OCSF activity name | `string` | Always 'Collect' for asset inventory |
| `static: Discovery` | `category_name` | OCSF category name | `string` | Always 'Discovery' |
| `static: 5` | `category_uid` | OCSF category UID | `integer` | Always 5 for Discovery category |
| `static: User Inventory Info` | `class_name` | OCSF class name | `string` | Always 'User Inventory Info' |
| `static: 5003` | `class_uid` | OCSF class UID | `integer` | Always 5003 for User Inventory Info |
| `static: 500302` | `type_uid` | OCSF type UID | `integer` | Always 500302 for User Inventory Info: Collect type |
| `static: User Inventory` | `type_name` | OCSF type name | `string` | Always 'User Inventory' for this specific event type |
| `static: Informational` | `severity` | Event severity level | `string` | Always 'Informational' for inventory events |
| `static: 1` | `severity_id` | OCSF severity ID | `integer` | Always 1 for Informational severity |
| `creationTime` | `time` | OCSF event timestamp | `timestamp` | Convert ISO 8601 to Unix epoch; use for OCSF event timestamp |
| `static: Crowdstrike Falcon` | `metadata.product.name` | Source product name | `string` | Always 'Crowdstrike Falcon' |
| `static: N/A` | `metadata.product.version` | Product version | `string` | CrowdStrike Identity Protection API does not provide a product version field; using 'N/A' |
| `static: 1.6.0` | `metadata.version` | OCSF schema version | `string` | Fixed OCSF schema version |
| `entityId` | `user.uid` | User unique identifier from CrowdStrike Identity Protection | `string` | Direct mapping of CrowdStrike entity unique ID |
| `primaryDisplayName` | `user.name` | User display name (username) | `string` | Direct mapping of primary display name |
| `primaryDisplayName + secondaryDisplayName` | `user.full_name` | User full name | `string` | Concatenate primaryDisplayName and secondaryDisplayName with space; trim whitespace; fallback to primaryDisplayName if secondaryDisplayName is empty |
| `emailAddresses[0]` | `user.email_addr` | Primary email address | `string` | Extract first email from emailAddresses array; null if empty or array is missing |
| `accounts[0].domain` | `user.domain` | User domain or realm (from AD account) | `string` | Direct mapping of domain from primary account |
| `roles[] | filter(ADMIN)` | `user.type` | User type (Admin or regular User) | `string` | If any role type contains 'ADMIN' (case-insensitive), type='Admin'; else type='User' |
| `roles[] | filter(ADMIN)` | `user.type_id` | OCSF user type ID | `integer` | If any role type contains 'ADMIN', type_id=2; else type_id=1 (OCSF User type mapping) |
| `riskScore` | `user.risk_score` | Risk score for user (0-100 scale) | `integer` | Multiply riskScore (0-1 decimal) by 100 to get 0-100 scale; round to nearest integer |
| `riskScoreSeverity` | `user.risk_level` | Risk severity level | `string` | Direct mapping: 'CRITICAL'→'Critical', 'HIGH'→'High', 'MEDIUM'→'Medium', 'LOW'→'Low', 'INFO'→'Info' |
| `riskScoreSeverity` | `user.risk_level_id` | OCSF risk level ID | `integer` | Map severity to OCSF RiskLevelId: Critical→1, High→2, Medium→3, Low→4, Info→5 |
| `accounts[0].samAccountName || primaryDisplayName` | `user.account.name` | Account username (SAM account name) | `string` | Direct mapping of SAM account name; fallback to primaryDisplayName if empty or missing |
| `accounts[0].objectSid || accounts[0].objectGuid || entityId` | `user.account.uid` | Account unique identifier (SID or GUID) | `string` | Fallback chain: objectSid → objectGuid → entityId |
| `accounts[0].dataSource` | `user.account.type` | Account type (LDAP, Azure AD, etc.) | `string` | Map dataSource: 'ACTIVE_DIRECTORY' or objectSid present→'LDAP Account', 'AZURE_AD'→'Azure AD Account', else→'Other' |
| `accounts[0].dataSource` | `user.account.type_id` | OCSF account type ID | `integer` | Map account type to OCSF ID: LDAP Account→11, Azure AD Account→12, Other→15 |
| `static: account_details` | `enrichments[0].name` | Enrichment name for account details | `string` | Always 'account_details' for this enrichment type |
| `accounts[0].dataSource` | `enrichments[0].value` | Enrichment value: resolved account type string | `string` | Resolved account type string (e.g., 'LDAP Account', 'Azure AD Account', 'Other') |
| `accounts[0].enabled` | `enrichments[0].data.is_enabled` | Whether the account is enabled/active | `boolean` | Direct mapping of account enabled status; null if field absent |




### OCSF Model Structure

#### User Inventory Info: Collect
Transformed CrowdStrike Active Directory administrator to OCSF User Inventory Info event

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
  "time": 1729509560,
  "metadata": {
    "product": {
      "name": "CrowdStrike Falcon",
      "version": "Identity Protection"
    },
    "version": "1.6.0"
  },
  "user": {
    "uid": "1c08759a-e6be-4858-8174-b308855541e9",
    "name": "administrateur",
    "full_name": "administrateur EXAMPLE.COM\\administrateur",
    "email_addr": null,
    "email_addresses": [],
    "type": "Admin",
    "type_id": 1,
    "risk_score": 66,
    "risk_level": "Medium",
    "risk_level_id": 3,
    "is_enabled": true,
    "learned": false,
    "has_role": true,
    "cn": "administrateur",
    "title": null,
    "department": null,
    "roles": [
      "BuiltinAdministratorRole",
      "ProgrammaticUserAccountRole"
    ],
    "desc": "administrateur - Risk: MEDIUM",
    "created_time": 1729509560,
    "account": {
      "uid": "S-1-5-21-947947667-100116589-3603791262-500",
      "name": "administrateur",
      "domain": "EXAMPLE.COM",
      "type": "LDAP Account",
      "type_id": 11,
      "desc": "Built-in account for administering the computer/domain"
    }
  }
}

```


