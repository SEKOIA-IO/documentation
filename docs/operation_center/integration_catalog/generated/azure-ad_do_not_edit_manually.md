
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | information on AD activities are collected: domain/user/group creation, password change, token update |
| `Authentication logs` | Azure AD logs provide details on authentication: status, user, IP address |





In details, the following Table denotes the type of events produced by this integration.

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
        "message": "{\"time\": \"2019-06-24T09:21:27.3694184Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Add unverified domain\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"2f006047-a6d9-4fca-847a-fffdb209fa4d\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_5P1YA_52883815\",\"category\": \"DirectoryManagement\",\"correlationId\": \"2f006047-a6d9-4fca-847a-fffdb209fa4d\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Add unverified domain\",\"activityDateTime\": \"2019-06-24T09:21:27.3694184+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Add\",\"initiatedBy\": {\"user\": {\"id\": \"158c144c-4c1d-4eb4-be08-f2732c8338fd\",\"displayName\": null,\"userPrincipalName\": \"exampleuser_gmail.com#EXT#@exampleuser.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": null,\"displayName\": \"examplecorp.onmicrosoft.com\",\"modifiedProperties\": [{\"displayName\": \"Name\",\"oldValue\": \"[\\\"\\\"]\",\"newValue\": \"[\\\"examplecorp.onmicrosoft.com\\\"]\"},{\"displayName\": \"LiveType\",\"oldValue\": \"[\\\"None\\\"]\",\"newValue\": \"[\\\"Managed\\\"]\"},{\"displayName\": \"Included Updated Properties\",\"oldValue\": null,\"newValue\": \"\\\"Name,LiveType\\\"\"}]}],\"additionalDetails\": []}}",
        "event": {
            "created": "2019-06-24T09:21:27.3694184Z",
            "dialect": "azure active directory",
            "category": [
                "iam",
                "change"
            ]
        },
        "log": {
            "hostname": "azureactivedirectory"
        },
        "host": {
            "hostname": "azureactivedirectory"
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
        "message": "{\"category\":\"AuditLogs\",\"correlationId\":\"93154481-5703-42a7-89a5-b7de6fbace8e\",\"durationMs\":0,\"identity\":\"Microsoft Teams Services\",\"level\":\"Informational\",\"operationName\":\"Add member to group\",\"operationVersion\":\"1.0\",\"properties\":{\"activityDateTime\":\"2020-01-02T13:36:37.9515687+00:00\",\"activityDisplayName\":\"Add member to group\",\"additionalDetails\":[{\"key\":\"User-Agent\",\"value\":\"SkypeSpaces/1.0a$*+\"}],\"category\":\"GroupManagement\",\"correlationId\":\"93154481-5703-42a7-89a5-b7de6fbace8e\",\"id\":\"Directory_FI4U8_64698073\",\"initiatedBy\":{\"app\":{\"appId\":null,\"displayName\":\"Microsoft Teams Services\",\"servicePrincipalId\":\"1de0a2d4-340e-4d98-b060-2dec8434481a\",\"servicePrincipalName\":null}},\"loggedByService\":\"Core Directory\",\"operationType\":\"Assign\",\"result\":\"success\",\"resultReason\":\"\",\"targetResources\":[{\"displayName\":null,\"id\":\"e6285600-5ec8-4ea4-89fc-40db84049b26\",\"modifiedProperties\":[{\"displayName\":\"Group.ObjectID\",\"newValue\":\"\\\"f3bccb88-a12b-4bbd-a971-e6e616946872\\\"\",\"oldValue\":null},{\"displayName\":\"Group.DisplayName\",\"newValue\":\"\\\"NEWCORP\\\"\",\"oldValue\":null},{\"displayName\":\"Group.WellKnownObjectName\",\"newValue\":null,\"oldValue\":null}],\"type\":\"User\",\"userPrincipalName\":\"example.user@corp.net\"},{\"displayName\":null,\"groupType\":\"azureAD\",\"id\":\"f3bccb88-a12b-4bbd-a971-e6e616946872\",\"modifiedProperties\":[],\"type\":\"Group\"}]},\"resourceId\":\"/tenants/29218bde-dc31-4e0d-969b-bac924ce3216/providers/Microsoft.aadiam\",\"resultSignature\":\"None\",\"tenantId\":\"29218bde-dc31-4e0d-969b-bac924ce3216\",\"time\":\"2020-01-02T13:36:37.9515687Z\"}",
        "event": {
            "created": "2020-01-02T13:36:37.951Z",
            "dialect": "azure active directory"
        },
        "host": {
            "hostname": "azureactivedirectory"
        },
        "log": {
            "hostname": "azureactivedirectory"
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
            "hosts": [
                "azureactivedirectory"
            ],
            "user": [
                "Microsoft Teams Services"
            ]
        }
    }
    	
	```


=== "add_service_principal_failure.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:18:23.5860200Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Add service principal\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"resultDescription\": \"Microsoft.Online.Workflows.SpnValidationException\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"191e390a-0c29-41e1-874b-c57ca3599213\",\"identity\": \"Microsoft Azure AD Internal - Jit Provisioning\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_GMR7H_185505965\",\"category\": \"ApplicationManagement\",\"correlationId\": \"191e390a-0c29-41e1-874b-c57ca3599213\",\"result\": \"failure\",\"resultReason\": \"Microsoft.Online.Workflows.SpnValidationException\",\"activityDisplayName\": \"Add service principal\",\"activityDateTime\": \"2019-06-24T09:18:23.58602+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Add\",\"initiatedBy\": {},\"targetResources\": [{\"id\": \"224fe45d-b5c4-44e7-ace4-7bea31600122\",\"displayName\": \"Azure AD Identity Protection\",\"type\": \"ServicePrincipal\",\"modifiedProperties\": [{\"displayName\": \"AccountEnabled\",\"oldValue\": \"[]\",\"newValue\": \"[true]\"},{\"displayName\": \"AppAddress\",\"oldValue\": \"[]\",\"newValue\": \"[{\\\"AddressType\\\":0,\\\"Address\\\":\\\"https://main.protectioncenter.ext.azure.com\\\",\\\"ReplyAddressClientType\\\":0},{\\\"AddressType\\\":0,\\\"Address\\\":\\\"https://s2.cloudappdiscovery.ext.azure.com/\\\",\\\"ReplyAddressClientType\\\":0}]\"},{\"displayName\": \"AppPrincipalId\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"fc68d9e5-1f76-45ef-99aa-214805418498\\\"]\"},{\"displayName\": \"DisplayName\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"Azure AD Identity Protection\\\"]\"},{\"displayName\": \"ServicePrincipalName\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"https://s2.cloudappdiscovery.ext.azure.com/\\\",\\\"https://main.protectioncenter.ext.azure.com\\\",\\\"fc68d9e5-1f76-45ef-99aa-214805418498\\\"]\"},{\"displayName\": \"Credential\",\"oldValue\": \"[]\",\"newValue\": \"[{\\\"CredentialType\\\":2,\\\"KeyStoreId\\\":\\\"291154f0-a9f5-45bb-87be-9c8ee5b6d62c\\\",\\\"KeyGroupId\\\":\\\"375eb77d-1d23-462b-9be7-cb51db9123e3\\\"}]\"},{\"displayName\": \"Included Updated Properties\",\"oldValue\": null,\"newValue\": \"\\\"AccountEnabled, AppAddress, AppPrincipalId, DisplayName, ServicePrincipalName, Credential\\\"\"},{\"displayName\": \"MethodExecutionResult.\",\"oldValue\": null,\"newValue\": \"\\\"Microsoft.Online.Workflows.SpnValidationException\\\"\"},{\"displayName\": \"TargetId.ServicePrincipalNames\",\"oldValue\": null,\"newValue\": \"\\\"https://s2.cloudappdiscovery.ext.azure.com/;https://main.protectioncenter.ext.azure.com;fc68d9e5-1f76-45ef-99aa-214805418498\\\"\"}]}],\"additionalDetails\": []}}",
        "event": {
            "created": "2019-06-24T09:18:23.5860200Z",
            "dialect": "azure active directory",
            "reason": "Microsoft.Online.Workflows.SpnValidationException"
        },
        "host": {
            "hostname": "azureactivedirectory"
        },
        "log": {
            "hostname": "azureactivedirectory"
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
        },
        "related": {
            "hosts": [
                "azureactivedirectory"
            ]
        }
    }
    	
	```


=== "add_user.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:29:28.6242725Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Add user\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"d40fb664-9901-4cfa-bd3b-afeff8d6b0de\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_HR9C4_45223131\",\"category\": \"UserManagement\",\"correlationId\": \"d40fb664-9901-4cfa-bd3b-afeff8d6b0de\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Add user\",\"activityDateTime\": \"2019-06-24T09:29:28.6242725+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Add\",\"initiatedBy\": {\"user\": {\"id\": \"158c144c-4c1d-4eb4-be08-f2732c8338fd\",\"displayName\": null,\"userPrincipalName\": \"user_gmail.com#EXT#@usergmail.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"type\": \"User\",\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"modifiedProperties\": [{\"displayName\": \"AccountEnabled\",\"oldValue\": \"[]\",\"newValue\": \"[true]\"},{\"displayName\": \"StsRefreshTokensValidFrom\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"2019-06-24T09:29:28Z\\\"]\"},{\"displayName\": \"UserPrincipalName\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"jean.dupont@usergmail.onmicrosoft.com\\\"]\"},{\"displayName\": \"UserType\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"Member\\\"]\"},{\"displayName\": \"Included Updated Properties\",\"oldValue\": null,\"newValue\": \"\\\"AccountEnabled, StsRefreshTokensValidFrom, UserPrincipalName, UserType\\\"\"}]}],\"additionalDetails\": []}}",
        "event": {
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4"
        },
        "log": {
            "hostname": "azureactivedirectory"
        },
        "host": {
            "hostname": "azureactivedirectory"
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
            "hosts": [
                "azureactivedirectory"
            ],
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
        "message": "{\"id\":\"39e3a81e-99b9-4a30-8000-f38a970e5100\",\"createdDateTime\":\"2020-09-28T10:12:41.4104242Z\",\"userDisplayName\":\"Jane Doe\",\"userPrincipalName\":\"jane.doe@sekoiacorp.onmicrosoft.com\",\"userId\":\"913f4b76-e10f-4f1c-aaf1-09356389319b\",\"appId\":\"4345a7b9-9a63-4910-a426-35363201d503\",\"appDisplayName\":\"O365 Suite UX\",\"ipAddress\":\"11.11.11.11\",\"clientAppUsed\":\"Browser\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0\",\"correlationId\":\"26e7584c-876b-425f-9119-49b411e21365\",\"conditionalAccessStatus\":\"notApplied\",\"originalRequestId\":\"39e3a81e-99b9-4a30-8000-f38a970e5100\",\"isInteractive\":false,\"tokenIssuerName\":\"\",\"tokenIssuerType\":\"AzureAD\",\"processingTimeInMilliseconds\":101,\"riskDetail\":\"hidden\",\"riskLevelAggregated\":\"hidden\",\"riskLevelDuringSignIn\":\"hidden\",\"riskState\":\"none\",\"riskEventTypes\":[],\"riskEventTypes_v2\":[],\"resourceDisplayName\":\"Windows Azure Active Directory\",\"resourceId\":\"00000002-0000-0000-c000-000000000000\",\"resourceTenantId\":\"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\",\"authenticationMethodsUsed\":[],\"authenticationRequirement\":\"multiFactorAuthentication\",\"alternateSignInName\":null,\"servicePrincipalName\":null,\"signInEventTypes\":[],\"servicePrincipalId\":\"\",\"status\":{\"errorCode\":0,\"failureReason\":\"Other.\",\"additionalDetails\":\"MFA requirement satisfied by claim in the token\"},\"deviceDetail\":{\"deviceId\":\"\",\"displayName\":null,\"operatingSystem\":\"Windows 10\",\"browser\":\"Firefox 81.0\",\"isCompliant\":null,\"isManaged\":null,\"trustType\":null},\"location\":{\"city\":\"Paris\",\"state\":\"Paris\",\"countryOrRegion\":\"FR\",\"geoCoordinates\":{\"altitude\":null,\"latitude\":48.861000061035156,\"longitude\":2.3380000591278076}},\"mfaDetail\":{\"authMethod\":null,\"authDetail\":null},\"appliedConditionalAccessPolicies\":[],\"authenticationProcessingDetails\":[{\"key\":\"Login Hint Present\",\"value\":\"True\"},{\"key\":\"IsCAEToken\",\"value\":\"False\"}],\"networkLocationDetails\":[],\"authenticationDetails\":[{\"authenticationStepDateTime\":\"2020-09-28T10:12:41.4104242Z\",\"authenticationMethod\":null,\"authenticationMethodDetail\":null,\"succeeded\":true,\"authenticationStepResultDetail\":\"MFA requirement satisfied by claim in the token\",\"authenticationStepRequirement\":\"User\"}],\"authenticationRequirementPolicies\":[]}",
        "event": {
            "category": "authentication",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "type": [
                "start"
            ]
        },
        "host": {
            "hostname": "azureactivedirectory",
            "os": {
                "name": "Windows 10"
            }
        },
        "log": {
            "hostname": "azureactivedirectory"
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
        "client": {
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
        "message": "{\"time\": \"2019-06-24T09:32:07.4637225Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Change user password\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"fd39aead-f711-4c4f-b6a9-ced2c67f3fca\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_1PF86_84995790\",\"category\": \"UserManagement\",\"correlationId\": \"fd39aead-f711-4c4f-b6a9-ced2c67f3fca\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Change user password\",\"activityDateTime\": \"2019-06-24T09:32:07.4637225+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Update\",\"initiatedBy\": {\"user\": {\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"type\": \"User\",\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"modifiedProperties\": []}],\"additionalDetails\": []}}",
        "event": {
            "created": "2019-06-24T09:32:07.4637225Z",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4"
        },
        "host": {
            "hostname": "azureactivedirectory"
        },
        "log": {
            "hostname": "azureactivedirectory"
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


=== "remove_domain.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:21:50.0418907Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Remove unverified domain\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"d60a1c27-11fa-4777-a349-c6c26ef33348\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_NFSWZ_16832133\",\"category\": \"DirectoryManagement\",\"correlationId\": \"d60a1c27-11fa-4777-a349-c6c26ef33348\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Remove unverified domain\",\"activityDateTime\": \"2019-06-24T09:21:50.0418907+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Delete\",\"initiatedBy\": {\"user\": {\"id\": \"158c144c-4c1d-4eb4-be08-f2732c8338fd\",\"displayName\": null,\"userPrincipalName\": \"use_gmail.com#EXT#@usegmail.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": null,\"displayName\": \"sekoiacorp.onmicrosoft.com\",\"modifiedProperties\": []}],\"additionalDetails\": []}}",
        "event": {
            "created": "2019-06-24T09:21:50.0418907Z",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4",
            "category": [
                "iam",
                "change"
            ]
        },
        "host": {
            "hostname": "azureactivedirectory"
        },
        "log": {
            "hostname": "azureactivedirectory"
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
        "host": {
            "hostname": "azureactivedirectory"
        },
        "client": {
            "geo": {
                "city_name": "Bordeaux",
                "country_iso_code": "FR",
                "location": {
                    "lat": "44.84040069580078",
                    "lon": "-0.5805000066757202"
                },
                "region_name": "Gironde"
            },
            "user": {
                "email": "User.Name@corp.name",
                "full_name": "User Name"
            }
        },
        "log": {
            "hostname": "azureactivedirectory"
        },
        "related": {
            "hosts": [
                "azureactivedirectory"
            ],
            "ip": [
                "11.11.11.11"
            ]
        },
        "service": {
            "name": "Office365 Shell WCSS-Server",
            "type": "ldap"
        },
        "source": {
            "address": "11.11.11.11",
            "ip": "11.11.11.11"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }
    }
    	
	```


=== "update_ststoken.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:32:07.4637225Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Update StsRefreshTokenValidFrom Timestamp\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"fd39aead-f711-4c4f-b6a9-ced2c67f3fca\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_1PF86_84995795\",\"category\": \"UserManagement\",\"correlationId\": \"fd39aead-f711-4c4f-b6a9-ced2c67f3fca\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Update StsRefreshTokenValidFrom Timestamp\",\"activityDateTime\": \"2019-06-24T09:32:07.4637225+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Update\",\"initiatedBy\": {\"user\": {\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"type\": \"User\",\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"modifiedProperties\": []}],\"additionalDetails\": []}}",
        "event": {
            "created": "2019-06-24T09:32:07.4637225Z",
            "dialect": "azure active directory",
            "dialect_uuid": "1e256ea1-3947-429e-97a6-abaec8702dc4"
        },
        "log": {
            "hostname": "azureactivedirectory"
        },
        "host": {
            "hostname": "azureactivedirectory"
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
        "host": {
            "hostname": "azureactivedirectory"
        },
        "log": {
            "hostname": "azureactivedirectory"
        },
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "User Risk Detection"
        },
        "client": {
            "geo": {
                "city_name": "La Guaiserie",
                "country_iso_code": "fr",
                "location": {
                    "lat": "47.45919",
                    "lon": "2.21955"
                },
                "region_name": "Loir-Et-Cher"
            },
            "user": {
                "email": "foo.bar@corp.eu",
                "full_name": "bar foo"
            }
        },
        "source": {
            "address": "11.22.33.44",
            "ip": "11.22.33.44"
        },
        "related": {
            "hosts": [
                "azureactivedirectory"
            ],
            "ip": [
                "11.22.33.44"
            ]
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
|`client.geo.city_name` | `keyword` | City name. |
|`client.geo.country_iso_code` | `keyword` | Country ISO code. |
|`client.geo.location` | `geo_point` | Longitude and latitude. |
|`client.geo.region_name` | `keyword` | Region name. |
|`client.ip` | `ip` | IP address of the client. |
|`client.user.email` | `keyword` | User email address. |
|`client.user.full_name` | `keyword` | User's full name, if available. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`host.os.name` | `keyword` | Operating system name, without the version. |
|`service.name` | `keyword` | Name of the service. |
|`service.type` | `keyword` | The type of the service. |
|`source.ip` | `ip` | IP address of the source. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.name` | `keyword` | Name of the user agent. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

