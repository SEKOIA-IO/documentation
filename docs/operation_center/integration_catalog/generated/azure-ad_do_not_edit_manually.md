
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | information on AD activities are collected: domain/user/group creation, password change, token update |
| `Authentication logs` | Azure AD logs provide details on authentication: status, user, IP address |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `authentication`, `change`, `iam` |
| Type | `connection`, `start` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "add_domain.json"

    ```json
	
    {
        "azuread": {
            "durationMs": 0,
            "category": "AuditLogs",
            "correlationId": "2f006047-a6d9-4fca-847a-fffdb209fa4d",
            "operationName": "Add unverified domain",
            "operationVersion": "1.0",
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "properties": {
                "correlationId": "2f006047-a6d9-4fca-847a-fffdb209fa4d",
                "id": "Directory_5P1YA_52883815"
            }
        },
        "event": {
            "created": "2019-06-24T09:21:27.3694184Z",
            "dialect": "azure active directory",
            "category": [
                "iam",
                "change"
            ]
        },
        "user": {
            "id": "158c144c-4c1d-4eb4-be08-f2732c8338fd",
            "name": "exampleuser_gmail.com#EXT#@exampleuser.onmicrosoft.com"
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Add unverified domain",
            "type": "add",
            "outcome": "success",
            "target": "user",
            "properties": [
                {
                    "name": "Name",
                    "oldValue": "[\"\"]",
                    "newValue": "[\"examplecorp.onmicrosoft.com\"]"
                },
                {
                    "name": "LiveType",
                    "oldValue": "[\"None\"]",
                    "newValue": "[\"Managed\"]"
                }
            ]
        },
        "related": {
            "user": [
                "exampleuser_gmail.com#EXT#@exampleuser.onmicrosoft.com"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "add_member_to_group.json"

    ```json
	
    {
        "azuread": {
            "durationMs": 0,
            "category": "AuditLogs",
            "correlationId": "93154481-5703-42a7-89a5-b7de6fbace8e",
            "identity": "Microsoft Teams Services",
            "operationName": "Add member to group",
            "operationVersion": "1.0",
            "resourceId": "/tenants/29218bde-dc31-4e0d-969b-bac924ce3216/providers/Microsoft.aadiam",
            "tenantId": "29218bde-dc31-4e0d-969b-bac924ce3216",
            "properties": {
                "correlationId": "93154481-5703-42a7-89a5-b7de6fbace8e",
                "id": "Directory_FI4U8_64698073"
            }
        },
        "event": {
            "created": "2020-01-02T13:36:37.951Z",
            "dialect": "azure active directory"
        },
        "user": {
            "id": "1de0a2d4-340e-4d98-b060-2dec8434481a",
            "name": "Microsoft Teams Services"
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Add member to group",
            "type": "assign",
            "outcome": "success",
            "target": "user",
            "properties": [
                {
                    "name": "Group.ObjectID",
                    "oldValue": "",
                    "newValue": "\"f3bccb88-a12b-4bbd-a971-e6e616946872\""
                },
                {
                    "name": "Group.DisplayName",
                    "oldValue": "",
                    "newValue": "\"NEWCORP\""
                },
                {
                    "name": "Group.WellKnownObjectName",
                    "oldValue": "",
                    "newValue": ""
                },
                {
                    "type": "targetedUser",
                    "name": "example.user@corp.net",
                    "id": "e6285600-5ec8-4ea4-89fc-40db84049b26"
                }
            ]
        },
        "related": {
            "user": [
                "Microsoft Teams Services"
            ]
        }
    }
    	
	```


=== "add_service_principal_failure.json"

    ```json
	
    {
        "azuread": {
            "durationMs": 0,
            "category": "AuditLogs",
            "correlationId": "191e390a-0c29-41e1-874b-c57ca3599213",
            "identity": "Microsoft Azure AD Internal - Jit Provisioning",
            "operationName": "Add service principal",
            "operationVersion": "1.0",
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "properties": {
                "correlationId": "191e390a-0c29-41e1-874b-c57ca3599213",
                "id": "Directory_GMR7H_185505965"
            }
        },
        "event": {
            "created": "2019-06-24T09:18:23.5860200Z",
            "dialect": "azure active directory",
            "reason": "Microsoft.Online.Workflows.SpnValidationException"
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Add service principal",
            "type": "add",
            "outcome": "failure",
            "outcome_reason": "Microsoft.Online.Workflows.SpnValidationException",
            "properties": [
                {
                    "name": "AccountEnabled",
                    "oldValue": "[]",
                    "newValue": "[true]"
                },
                {
                    "name": "AppAddress",
                    "oldValue": "[]",
                    "newValue": "[{\"AddressType\":0,\"Address\":\"https://main.protectioncenter.ext.azure.com\",\"ReplyAddressClientType\":0},{\"AddressType\":0,\"Address\":\"https://s2.cloudappdiscovery.ext.azure.com/\",\"ReplyAddressClientType\":0}]"
                },
                {
                    "name": "AppPrincipalId",
                    "oldValue": "[]",
                    "newValue": "[\"fc68d9e5-1f76-45ef-99aa-214805418498\"]"
                },
                {
                    "name": "DisplayName",
                    "oldValue": "[]",
                    "newValue": "[\"Azure AD Identity Protection\"]"
                },
                {
                    "name": "ServicePrincipalName",
                    "oldValue": "[]",
                    "newValue": "[\"https://s2.cloudappdiscovery.ext.azure.com/\",\"https://main.protectioncenter.ext.azure.com\",\"fc68d9e5-1f76-45ef-99aa-214805418498\"]"
                },
                {
                    "name": "Credential",
                    "oldValue": "[]",
                    "newValue": "[{\"CredentialType\":2,\"KeyStoreId\":\"291154f0-a9f5-45bb-87be-9c8ee5b6d62c\",\"KeyGroupId\":\"375eb77d-1d23-462b-9be7-cb51db9123e3\"}]"
                },
                {
                    "name": "MethodExecutionResult.",
                    "oldValue": "",
                    "newValue": "\"Microsoft.Online.Workflows.SpnValidationException\""
                },
                {
                    "name": "TargetId.ServicePrincipalNames",
                    "oldValue": "",
                    "newValue": "\"https://s2.cloudappdiscovery.ext.azure.com/;https://main.protectioncenter.ext.azure.com;fc68d9e5-1f76-45ef-99aa-214805418498\""
                }
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "add_user.json"

    ```json
	
    {
        "azuread": {
            "durationMs": 0,
            "category": "AuditLogs",
            "correlationId": "d40fb664-9901-4cfa-bd3b-afeff8d6b0de",
            "operationName": "Add user",
            "operationVersion": "1.0",
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "properties": {
                "correlationId": "d40fb664-9901-4cfa-bd3b-afeff8d6b0de",
                "id": "Directory_HR9C4_45223131"
            }
        },
        "event": {
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4"
        },
        "user": {
            "id": "158c144c-4c1d-4eb4-be08-f2732c8338fd",
            "name": "user_gmail.com#EXT#@usergmail.onmicrosoft.com"
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Add user",
            "type": "add",
            "outcome": "success",
            "target": "user",
            "properties": [
                {
                    "name": "AccountEnabled",
                    "oldValue": "[]",
                    "newValue": "[true]"
                },
                {
                    "name": "StsRefreshTokensValidFrom",
                    "oldValue": "[]",
                    "newValue": "[\"2019-06-24T09:29:28Z\"]"
                },
                {
                    "name": "UserPrincipalName",
                    "oldValue": "[]",
                    "newValue": "[\"jean.dupont@usergmail.onmicrosoft.com\"]"
                },
                {
                    "name": "UserType",
                    "oldValue": "[]",
                    "newValue": "[\"Member\"]"
                },
                {
                    "type": "targetedUser",
                    "name": "jean.dupont@usergmail.onmicrosoft.com",
                    "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3"
                }
            ]
        },
        "related": {
            "user": [
                "user_gmail.com#EXT#@usergmail.onmicrosoft.com"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "auth.json"

    ```json
	
    {
        "azuread": {
            "authenticationDetails": [
                {
                    "authenticationMethod": null,
                    "authenticationMethodDetail": null,
                    "authenticationStepDateTime": "2020-09-28T10:12:41.4104242Z",
                    "authenticationStepRequirement": "User",
                    "authenticationStepResultDetail": "MFA requirement satisfied by claim in the token",
                    "succeeded": true
                }
            ],
            "authenticationRequirement": "multiFactorAuthentication",
            "authenticationRequirementPolicies": [],
            "correlationId": "26e7584c-876b-425f-9119-49b411e21365",
            "resourceId": "00000002-0000-0000-c000-000000000000",
            "resourceTenantId": "aa09a079-7796-46a8-a4d4-4d21b0dcf1b2",
            "tokenIssuerType": "AzureAD"
        },
        "event": {
            "category": "authentication",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "type": [
                "start"
            ]
        },
        "host": {
            "os": {
                "name": "Windows 10"
            }
        },
        "user": {
            "id": "913f4b76-e10f-4f1c-aaf1-09356389319b",
            "name": "jane.doe@sekoiacorp.onmicrosoft.com"
        },
        "service": {
            "type": "ldap",
            "name": "Windows Azure Active Directory"
        },
        "action": {
            "name": "authentication",
            "target": "user"
        },
        "source": {
            "address": "11.11.11.11",
            "ip": "11.11.11.11"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
            "name": "Firefox 81.0"
        },
        "related": {
            "user": [
                "jane.doe@sekoiacorp.onmicrosoft.com"
            ],
            "ip": [
                "11.11.11.11"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "change_user_password.json"

    ```json
	
    {
        "azuread": {
            "durationMs": 0,
            "category": "AuditLogs",
            "correlationId": "fd39aead-f711-4c4f-b6a9-ced2c67f3fca",
            "operationName": "Change user password",
            "operationVersion": "1.0",
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "properties": {
                "correlationId": "fd39aead-f711-4c4f-b6a9-ced2c67f3fca",
                "id": "Directory_1PF86_84995790"
            }
        },
        "event": {
            "created": "2019-06-24T09:32:07.4637225Z",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4"
        },
        "user": {
            "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3",
            "name": "jean.dupont@usergmail.onmicrosoft.com"
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Change user password",
            "type": "update",
            "outcome": "success",
            "target": "user",
            "properties": [
                {
                    "type": "targetedUser",
                    "name": "jean.dupont@usergmail.onmicrosoft.com",
                    "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3"
                }
            ]
        },
        "related": {
            "user": [
                "jean.dupont@usergmail.onmicrosoft.com"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "empty_geolocalisation.json"

    ```json
	
    {
        "action": {
            "name": "Sign-in activity"
        },
        "azuread": {
            "Level": 4,
            "callerIpAddress": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "category": "SignInLogs",
            "correlationId": "7ee10819-f631-4ab1-8edb-4efb7286baba",
            "durationMs": 0,
            "identity": "DUPONT Jean",
            "operationName": "Sign-in activity",
            "operationVersion": "1.0",
            "properties": {
                "correlationId": "7ee10819-f631-4ab1-8edb-4efb7286baba",
                "id": "b2fdcc8f-954d-4d88-a035-58daefab4f00",
                "riskDetail": "none",
                "riskState": "none",
                "status": {
                    "errorCode": "0"
                }
            },
            "resourceId": "/tenants/e6eb2b5c-ad71-4c33-9856-1ed49b85bfe2/providers/Microsoft.aadiam",
            "tenantId": "e6eb2b5c-ad71-4c33-9856-1ed49b85bfe2"
        },
        "ecs": {
            "version": "1.10.0"
        },
        "event": {
            "category": [
                "iam",
                "change"
            ],
            "created": "2019-06-24T09:21:50.0418907Z",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "outcome": "success"
        },
        "related": {
            "ip": [
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
            ]
        },
        "service": {
            "name": "Office 365 Exchange Online",
            "type": "ldap"
        },
        "source": {
            "address": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "ip": "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        },
        "user": {
            "email": "jean.dupont@corp.com",
            "full_name": "DUPONT Jean"
        },
        "user_agent": {
            "original": "Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.14326; Pro)"
        }
    }
    	
	```


=== "remove_domain.json"

    ```json
	
    {
        "azuread": {
            "durationMs": 0,
            "category": "AuditLogs",
            "correlationId": "d60a1c27-11fa-4777-a349-c6c26ef33348",
            "operationName": "Remove unverified domain",
            "operationVersion": "1.0",
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "properties": {
                "correlationId": "d60a1c27-11fa-4777-a349-c6c26ef33348",
                "id": "Directory_NFSWZ_16832133"
            }
        },
        "event": {
            "created": "2019-06-24T09:21:50.0418907Z",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "category": [
                "iam",
                "change"
            ]
        },
        "user": {
            "id": "158c144c-4c1d-4eb4-be08-f2732c8338fd",
            "name": "use_gmail.com#EXT#@usegmail.onmicrosoft.com"
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Remove unverified domain",
            "type": "delete",
            "outcome": "success",
            "target": "user",
            "properties": []
        },
        "related": {
            "user": [
                "use_gmail.com#EXT#@usegmail.onmicrosoft.com"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "sign-in_activity.json"

    ```json
	
    {
        "event": {
            "category": "authentication",
            "outcome": "success",
            "reason": "External security challenge was not satisfied."
        },
        "action": {
            "name": "Sign-in activity"
        },
        "azuread": {
            "durationMs": 0,
            "Level": 4,
            "callerIpAddress": "11.11.11.11",
            "category": "SignInLogs",
            "correlationId": "e68960e2-8996-448c-ba7a-e54eeb8ff2ed",
            "identity": "User Name",
            "operationName": "Sign-in activity",
            "operationVersion": "1.0",
            "resourceId": "/tenants/34314e6e-4023-4e4b-a15e-143f63244e2b/providers/Microsoft.aadiam",
            "tenantId": "34314e6e-4023-4e4b-a15e-143f63244e2b",
            "properties": {
                "correlationId": "e68960e2-8996-448c-ba7a-e54eeb8ff2ed",
                "id": "22253f56-6fc4-45f2-b148-d7fe15504900",
                "riskDetail": "none",
                "riskState": "none",
                "status": {
                    "errorCode": "50158",
                    "failureReason": "External security challenge was not satisfied."
                }
            }
        },
        "source": {
            "address": "11.11.11.11",
            "ip": "11.11.11.11",
            "geo": {
                "city_name": "Bordeaux",
                "country_iso_code": "FR",
                "location": {
                    "lat": 44.84040069580078,
                    "lon": -0.5805000066757202
                },
                "region_name": "Gironde"
            }
        },
        "user": {
            "email": "User.Name@corp.name",
            "full_name": "User Name"
        },
        "related": {
            "ip": [
                "11.11.11.11"
            ]
        },
        "service": {
            "name": "Office365 Shell WCSS-Server",
            "type": "ldap"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }
    }
    	
	```


=== "sign-in_activity2.json"

    ```json
	
    {
        "azuread": {
            "durationMs": 0,
            "Level": 4,
            "callerIpAddress": "11.11.11.11",
            "category": "SignInLogs",
            "correlationId": "467c1340-0762-40d2-b6fb-339235633ebb",
            "identity": "Admin Jean Dupont",
            "operationName": "Sign-in activity",
            "operationVersion": "1.0",
            "resourceId": "/tenants/34314e6e-4023-4e4b-a15e-143f63244e2b/providers/Microsoft.aadiam",
            "tenantId": "34314e6e-4023-4e4b-a15e-143f63244e2b",
            "properties": {
                "correlationId": "467c1340-0762-40d2-b6fb-339235633ebb",
                "id": "8795994f-0bb8-46d7-8797-8c9c385d5900",
                "riskDetail": "none",
                "riskState": "none",
                "status": {
                    "errorCode": "0"
                }
            }
        },
        "action": {
            "name": "Sign-in activity"
        },
        "user": {
            "email": "admin.jdupont@corp.net",
            "full_name": "Admin Jean Dupont"
        },
        "source": {
            "geo": {
                "city_name": "Bordeaux",
                "country_iso_code": "FR",
                "location": {
                    "lat": 44.84040069580078,
                    "lon": -0.5805000066757202
                },
                "region_name": "Gironde"
            },
            "address": "11.11.11.11",
            "ip": "11.11.11.11"
        },
        "event": {
            "category": "authentication",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "outcome": "success",
            "type": [
                "start"
            ]
        },
        "related": {
            "ip": [
                "11.11.11.11"
            ]
        },
        "service": {
            "name": "Windows Azure Active Directory",
            "type": "ldap"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
        }
    }
    	
	```


=== "update_ststoken.json"

    ```json
	
    {
        "azuread": {
            "durationMs": 0,
            "category": "AuditLogs",
            "correlationId": "fd39aead-f711-4c4f-b6a9-ced2c67f3fca",
            "operationName": "Update StsRefreshTokenValidFrom Timestamp",
            "operationVersion": "1.0",
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "properties": {
                "correlationId": "fd39aead-f711-4c4f-b6a9-ced2c67f3fca",
                "id": "Directory_1PF86_84995795"
            }
        },
        "event": {
            "created": "2019-06-24T09:32:07.4637225Z",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4"
        },
        "user": {
            "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3",
            "name": "jean.dupont@usergmail.onmicrosoft.com"
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Update StsRefreshTokenValidFrom Timestamp",
            "type": "update",
            "outcome": "success",
            "target": "user",
            "properties": [
                {
                    "type": "targetedUser",
                    "name": "jean.dupont@usergmail.onmicrosoft.com",
                    "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3"
                }
            ]
        },
        "related": {
            "user": [
                "jean.dupont@usergmail.onmicrosoft.com"
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```


=== "user_risk_detection.json"

    ```json
	
    {
        "message": "{\"time\":\"3/24/2022 2:42:35 PM\",\"resourceId\":\"/tenants/2d0c1986-ef7b-4bbf-8428-3c837471e7ad/providers/microsoft.aadiam\",\"operationName\":\"User Risk Detection\",\"operationVersion\":\"1.0\",\"category\":\"UserRiskEvents\",\"tenantId\":\"2d0c1986-ef7b-4bbf-8428-3c837471e7ad\",\"resultSignature\":\"None\",\"durationMs\":0,\"callerIpAddress\":\"11.22.33.44\",\"correlationId\":\"ef7868bd7e94b06ecd6cc965fc826c85d367bb5b9b083da9a26686786a791080\",\"identity\":\"bar foo\",\"Level\":4,\"location\":\"fr\",\"properties\":{\"id\":\"ef7868bd7e94b06ecd6cc965fc826c85d367bb5b9b083da9a26686786a791080\",\"requestId\":\"d38b6ab7-65b0-419c-b83a-a5787d6fa100\",\"correlationId\":\"325294e4-4026-4cc7-889d-b4be570b3254\",\"riskType\":\"unfamiliarFeatures\",\"riskEventType\":\"unfamiliarFeatures\",\"riskState\":\"dismissed\",\"riskLevel\":\"low\",\"riskDetail\":\"aiConfirmedSigninSafe\",\"source\":\"IdentityProtection\",\"detectionTimingType\":\"realtime\",\"activity\":\"signin\",\"ipAddress\":\"11.22.33.44\",\"location\":{\"city\":\"La Guaiserie\",\"state\":\"Loir-Et-Cher\",\"countryOrRegion\":\"FR\",\"geoCoordinates\":{\"altitude\":0.0,\"latitude\":47.45919,\"longitude\":2.21955}},\"activityDateTime\":\"2022-03-24T14:40:04.234Z\",\"detectedDateTime\":\"2022-03-24T14:40:04.234Z\",\"lastUpdatedDateTime\":\"2022-03-24T14:42:35.066Z\",\"userId\":\"4c64c30a-7a60-4211-bef1-5e4279854e85\",\"userDisplayName\":\"bar foo\",\"userPrincipalName\":\"foo.bar@corp.eu\",\"additionalInfo\":\"[{\\\"Key\\\":\\\"userAgent\\\",\\\"Value\\\":\\\"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148\\\"}]\",\"tokenIssuerType\":\"AzureAD\",\"resourceTenantId\":null,\"homeTenantId\":\"2d0c1986-ef7b-4bbf-8428-3c837471e7ad\",\"userType\":\"member\",\"crossTenantAccessType\":\"none\"}}",
        "event": {
            "category": "authentication",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "reason": "unfamiliarFeatures",
            "type": [
                "connection"
            ]
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "User Risk Detection"
        },
        "user": {
            "email": "foo.bar@corp.eu",
            "full_name": "bar foo"
        },
        "source": {
            "geo": {
                "city_name": "La Guaiserie",
                "country_iso_code": "fr",
                "location": {
                    "lat": 47.45919,
                    "lon": 2.21955
                },
                "region_name": "Loir-Et-Cher"
            },
            "address": "11.22.33.44",
            "ip": "11.22.33.44"
        },
        "related": {
            "ip": [
                "11.22.33.44"
            ]
        },
        "azuread": {
            "durationMs": 0,
            "Level": 4,
            "callerIpAddress": "11.22.33.44",
            "category": "UserRiskEvents",
            "correlationId": "ef7868bd7e94b06ecd6cc965fc826c85d367bb5b9b083da9a26686786a791080",
            "identity": "bar foo",
            "operationName": "User Risk Detection",
            "operationVersion": "1.0",
            "resourceId": "/tenants/2d0c1986-ef7b-4bbf-8428-3c837471e7ad/providers/microsoft.aadiam",
            "tenantId": "2d0c1986-ef7b-4bbf-8428-3c837471e7ad",
            "properties": {
                "activity": "signin",
                "correlationId": "325294e4-4026-4cc7-889d-b4be570b3254",
                "detectionTimingType": "realtime",
                "id": "ef7868bd7e94b06ecd6cc965fc826c85d367bb5b9b083da9a26686786a791080",
                "requestId": "d38b6ab7-65b0-419c-b83a-a5787d6fa100",
                "riskDetail": "aiConfirmedSigninSafe",
                "riskEventType": "unfamiliarFeatures",
                "riskLevel": "low",
                "riskState": "dismissed",
                "source": "IdentityProtection"
            }
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`action.properties` | `array` | action.properties |
|`action.target` | `keyword` | action.target |
|`azuread.Level` | `long` | None |
|`azuread.activityDateTime` | `keyword` | None |
|`azuread.additionalInfo` | `keyword` | None |
|`azuread.authenticationDetails` | `array` | None |
|`azuread.authenticationProtocol` | `keyword` | None |
|`azuread.authenticationRequirement` | `keyword` | None |
|`azuread.authenticationRequirementPolicies` | `array` | None |
|`azuread.autonomousSystemNumber` | `long` | None |
|`azuread.callerIpAddress` | `keyword` | None |
|`azuread.category` | `keyword` | None |
|`azuread.correlationId` | `keyword` | None |
|`azuread.crossTenantAccessType` | `keyword` | None |
|`azuread.detectedDateTime` | `keyword` | None |
|`azuread.durationMs` | `long` | None |
|`azuread.flaggedForReview` | `bool` | None |
|`azuread.homeTenantId` | `keyword` | None |
|`azuread.identity` | `keyword` | None |
|`azuread.incomingTokenType` | `keyword` | None |
|`azuread.isTenantRestricted` | `bool` | None |
|`azuread.lastUpdatedDateTime` | `keyword` | None |
|`azuread.operationName` | `keyword` | None |
|`azuread.operationVersion` | `keyword` | None |
|`azuread.privateLinkDetails` | `list` | None |
|`azuread.properties.activity` | `keyword` | None |
|`azuread.properties.correlationId` | `keyword` | None |
|`azuread.properties.detectionTimingType` | `keyword` | None |
|`azuread.properties.id` | `keyword` | None |
|`azuread.properties.requestId` | `keyword` | None |
|`azuread.properties.riskDetail` | `keyword` | None |
|`azuread.properties.riskEventType` | `keyword` | None |
|`azuread.properties.riskLevel` | `keyword` | None |
|`azuread.properties.riskState` | `keyword` | None |
|`azuread.properties.source` | `keyword` | None |
|`azuread.properties.status.errorCode` | `keyword` | None |
|`azuread.properties.status.failureReason` | `keyword` | None |
|`azuread.resourceId` | `keyword` | None |
|`azuread.resourceTenantId` | `keyword` | None |
|`azuread.resultSignature` | `keyword` | None |
|`azuread.servicePrincipalId` | `keyword` | None |
|`azuread.ssoExtensionVersion` | `keyword` | None |
|`azuread.tenantId` | `keyword` | None |
|`azuread.tokenIssuerType` | `keyword` | None |
|`azuread.uniqueTokenIdentifier` | `keyword` | None |
|`azuread.userType` | `keyword` | None |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`host.os.name` | `keyword` | Operating system name, without the version. |
|`service.name` | `keyword` | Name of the service. |
|`service.type` | `keyword` | The type of the service. |
|`source.geo.city_name` | `keyword` | City name. |
|`source.geo.country_iso_code` | `keyword` | Country ISO code. |
|`source.geo.location` | `geo_point` | Longitude and latitude. |
|`source.geo.region_name` | `keyword` | Region name. |
|`source.ip` | `ip` | IP address of the source. |
|`user.email` | `keyword` | User email address. |
|`user.full_name` | `keyword` | User's full name, if available. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.name` | `keyword` | Name of the user agent. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

