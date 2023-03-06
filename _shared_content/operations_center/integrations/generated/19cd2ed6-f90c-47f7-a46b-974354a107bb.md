
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
| Category | `authentication` |
| Type | `connection`, `start` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "add_domain.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:21:27.3694184Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Add unverified domain\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"2f006047-a6d9-4fca-847a-fffdb209fa4d\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_5P1YA_52883815\",\"category\": \"DirectoryManagement\",\"correlationId\": \"2f006047-a6d9-4fca-847a-fffdb209fa4d\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Add unverified domain\",\"activityDateTime\": \"2019-06-24T09:21:27.3694184+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Add\",\"initiatedBy\": {\"user\": {\"id\": \"158c144c-4c1d-4eb4-be08-f2732c8338fd\",\"displayName\": null,\"userPrincipalName\": \"exampleuser_gmail.com#EXT#@exampleuser.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": null,\"displayName\": \"examplecorp.onmicrosoft.com\",\"modifiedProperties\": [{\"displayName\": \"Name\",\"oldValue\": \"[\\\"\\\"]\",\"newValue\": \"[\\\"examplecorp.onmicrosoft.com\\\"]\"},{\"displayName\": \"LiveType\",\"oldValue\": \"[\\\"None\\\"]\",\"newValue\": \"[\\\"Managed\\\"]\"},{\"displayName\": \"Included Updated Properties\",\"oldValue\": null,\"newValue\": \"\\\"Name,LiveType\\\"\"}]}],\"additionalDetails\": []}}",
        "event": {
            "category": [
                "iam"
            ]
        },
        "@timestamp": "2019-06-24T09:21:27.369418Z",
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Add unverified domain",
            "properties": [
                {
                    "name": "Name",
                    "newValue": "[\"examplecorp.onmicrosoft.com\"]",
                    "oldValue": "[\"\"]"
                },
                {
                    "name": "LiveType",
                    "newValue": "[\"Managed\"]",
                    "oldValue": "[\"None\"]"
                }
            ],
            "target": "user",
            "outcome": "success",
            "type": "add"
        },
        "azuread": {
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "operationName": "Add unverified domain",
            "operationVersion": "1.0",
            "category": "AuditLogs",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "durationMs": 0,
            "correlationId": "2f006047-a6d9-4fca-847a-fffdb209fa4d",
            "properties": {
                "id": "Directory_5P1YA_52883815",
                "correlationId": "2f006047-a6d9-4fca-847a-fffdb209fa4d"
            }
        },
        "user": {
            "id": "158c144c-4c1d-4eb4-be08-f2732c8338fd",
            "name": "exampleuser_gmail.com#EXT#@exampleuser.onmicrosoft.com"
        },
        "related": {
            "user": [
                "exampleuser_gmail.com#EXT#@exampleuser.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "add_member_to_group.json"

    ```json
	
    {
        "message": "{\"category\":\"AuditLogs\",\"correlationId\":\"93154481-5703-42a7-89a5-b7de6fbace8e\",\"durationMs\":0,\"identity\":\"Microsoft Teams Services\",\"level\":\"Informational\",\"operationName\":\"Add member to group\",\"operationVersion\":\"1.0\",\"properties\":{\"activityDateTime\":\"2020-01-02T13:36:37.9515687+00:00\",\"activityDisplayName\":\"Add member to group\",\"additionalDetails\":[{\"key\":\"User-Agent\",\"value\":\"SkypeSpaces/1.0a$*+\"}],\"category\":\"GroupManagement\",\"correlationId\":\"93154481-5703-42a7-89a5-b7de6fbace8e\",\"id\":\"Directory_FI4U8_64698073\",\"initiatedBy\":{\"app\":{\"appId\":null,\"displayName\":\"Microsoft Teams Services\",\"servicePrincipalId\":\"1de0a2d4-340e-4d98-b060-2dec8434481a\",\"servicePrincipalName\":null}},\"loggedByService\":\"Core Directory\",\"operationType\":\"Assign\",\"result\":\"success\",\"resultReason\":\"\",\"targetResources\":[{\"displayName\":null,\"id\":\"e6285600-5ec8-4ea4-89fc-40db84049b26\",\"modifiedProperties\":[{\"displayName\":\"Group.ObjectID\",\"newValue\":\"\\\"f3bccb88-a12b-4bbd-a971-e6e616946872\\\"\",\"oldValue\":null},{\"displayName\":\"Group.DisplayName\",\"newValue\":\"\\\"NEWCORP\\\"\",\"oldValue\":null},{\"displayName\":\"Group.WellKnownObjectName\",\"newValue\":null,\"oldValue\":null}],\"type\":\"User\",\"userPrincipalName\":\"example.user@corp.net\"},{\"displayName\":null,\"groupType\":\"azureAD\",\"id\":\"f3bccb88-a12b-4bbd-a971-e6e616946872\",\"modifiedProperties\":[],\"type\":\"Group\"}]},\"resourceId\":\"/tenants/29218bde-dc31-4e0d-969b-bac924ce3216/providers/Microsoft.aadiam\",\"resultSignature\":\"None\",\"tenantId\":\"29218bde-dc31-4e0d-969b-bac924ce3216\",\"time\":\"2020-01-02T13:36:37.9515687Z\"}",
        "event": {
            "category": [
                "iam"
            ]
        },
        "@timestamp": "2020-01-02T13:36:37.951568Z",
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Add member to group",
            "properties": [
                {
                    "name": "Group.ObjectID",
                    "newValue": "\"f3bccb88-a12b-4bbd-a971-e6e616946872\"",
                    "oldValue": ""
                },
                {
                    "name": "Group.DisplayName",
                    "newValue": "\"NEWCORP\"",
                    "oldValue": ""
                },
                {
                    "name": "Group.WellKnownObjectName",
                    "newValue": "",
                    "oldValue": ""
                },
                {
                    "name": "example.user@corp.net",
                    "id": "e6285600-5ec8-4ea4-89fc-40db84049b26",
                    "type": "targetedUser"
                }
            ],
            "target": "user",
            "outcome": "success",
            "type": "assign"
        },
        "azuread": {
            "resourceId": "/tenants/29218bde-dc31-4e0d-969b-bac924ce3216/providers/Microsoft.aadiam",
            "operationName": "Add member to group",
            "operationVersion": "1.0",
            "category": "AuditLogs",
            "tenantId": "29218bde-dc31-4e0d-969b-bac924ce3216",
            "durationMs": 0,
            "correlationId": "93154481-5703-42a7-89a5-b7de6fbace8e",
            "identity": "Microsoft Teams Services",
            "properties": {
                "id": "Directory_FI4U8_64698073",
                "correlationId": "93154481-5703-42a7-89a5-b7de6fbace8e"
            }
        },
        "user": {
            "id": "1de0a2d4-340e-4d98-b060-2dec8434481a",
            "name": "Microsoft Teams Services"
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
        "message": "{\"time\": \"2019-06-24T09:18:23.5860200Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Add service principal\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"resultDescription\": \"Microsoft.Online.Workflows.SpnValidationException\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"191e390a-0c29-41e1-874b-c57ca3599213\",\"identity\": \"Microsoft Azure AD Internal - Jit Provisioning\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_GMR7H_185505965\",\"category\": \"ApplicationManagement\",\"correlationId\": \"191e390a-0c29-41e1-874b-c57ca3599213\",\"result\": \"failure\",\"resultReason\": \"Microsoft.Online.Workflows.SpnValidationException\",\"activityDisplayName\": \"Add service principal\",\"activityDateTime\": \"2019-06-24T09:18:23.58602+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Add\",\"initiatedBy\": {},\"targetResources\": [{\"id\": \"224fe45d-b5c4-44e7-ace4-7bea31600122\",\"displayName\": \"Azure AD Identity Protection\",\"type\": \"ServicePrincipal\",\"modifiedProperties\": [{\"displayName\": \"AccountEnabled\",\"oldValue\": \"[]\",\"newValue\": \"[true]\"},{\"displayName\": \"AppAddress\",\"oldValue\": \"[]\",\"newValue\": \"[{\\\"AddressType\\\":0,\\\"Address\\\":\\\"https://main.protectioncenter.ext.azure.com\\\",\\\"ReplyAddressClientType\\\":0},{\\\"AddressType\\\":0,\\\"Address\\\":\\\"https://s2.cloudappdiscovery.ext.azure.com/\\\",\\\"ReplyAddressClientType\\\":0}]\"},{\"displayName\": \"AppPrincipalId\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"fc68d9e5-1f76-45ef-99aa-214805418498\\\"]\"},{\"displayName\": \"DisplayName\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"Azure AD Identity Protection\\\"]\"},{\"displayName\": \"ServicePrincipalName\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"https://s2.cloudappdiscovery.ext.azure.com/\\\",\\\"https://main.protectioncenter.ext.azure.com\\\",\\\"fc68d9e5-1f76-45ef-99aa-214805418498\\\"]\"},{\"displayName\": \"Credential\",\"oldValue\": \"[]\",\"newValue\": \"[{\\\"CredentialType\\\":2,\\\"KeyStoreId\\\":\\\"291154f0-a9f5-45bb-87be-9c8ee5b6d62c\\\",\\\"KeyGroupId\\\":\\\"375eb77d-1d23-462b-9be7-cb51db9123e3\\\"}]\"},{\"displayName\": \"Included Updated Properties\",\"oldValue\": null,\"newValue\": \"\\\"AccountEnabled, AppAddress, AppPrincipalId, DisplayName, ServicePrincipalName, Credential\\\"\"},{\"displayName\": \"MethodExecutionResult.\",\"oldValue\": null,\"newValue\": \"\\\"Microsoft.Online.Workflows.SpnValidationException\\\"\"},{\"displayName\": \"TargetId.ServicePrincipalNames\",\"oldValue\": null,\"newValue\": \"\\\"https://s2.cloudappdiscovery.ext.azure.com/;https://main.protectioncenter.ext.azure.com;fc68d9e5-1f76-45ef-99aa-214805418498\\\"\"}]}],\"additionalDetails\": []}}",
        "event": {
            "reason": "Microsoft.Online.Workflows.SpnValidationException",
            "category": [
                "iam"
            ]
        },
        "@timestamp": "2019-06-24T09:18:23.586020Z",
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Add service principal",
            "properties": [
                {
                    "name": "AccountEnabled",
                    "newValue": "[true]",
                    "oldValue": "[]"
                },
                {
                    "name": "AppAddress",
                    "newValue": "[{\"AddressType\":0,\"Address\":\"https://main.protectioncenter.ext.azure.com\",\"ReplyAddressClientType\":0},{\"AddressType\":0,\"Address\":\"https://s2.cloudappdiscovery.ext.azure.com/\",\"ReplyAddressClientType\":0}]",
                    "oldValue": "[]"
                },
                {
                    "name": "AppPrincipalId",
                    "newValue": "[\"fc68d9e5-1f76-45ef-99aa-214805418498\"]",
                    "oldValue": "[]"
                },
                {
                    "name": "DisplayName",
                    "newValue": "[\"Azure AD Identity Protection\"]",
                    "oldValue": "[]"
                },
                {
                    "name": "ServicePrincipalName",
                    "newValue": "[\"https://s2.cloudappdiscovery.ext.azure.com/\",\"https://main.protectioncenter.ext.azure.com\",\"fc68d9e5-1f76-45ef-99aa-214805418498\"]",
                    "oldValue": "[]"
                },
                {
                    "name": "Credential",
                    "newValue": "[{\"CredentialType\":2,\"KeyStoreId\":\"291154f0-a9f5-45bb-87be-9c8ee5b6d62c\",\"KeyGroupId\":\"375eb77d-1d23-462b-9be7-cb51db9123e3\"}]",
                    "oldValue": "[]"
                },
                {
                    "name": "MethodExecutionResult.",
                    "newValue": "\"Microsoft.Online.Workflows.SpnValidationException\"",
                    "oldValue": ""
                },
                {
                    "name": "TargetId.ServicePrincipalNames",
                    "newValue": "\"https://s2.cloudappdiscovery.ext.azure.com/;https://main.protectioncenter.ext.azure.com;fc68d9e5-1f76-45ef-99aa-214805418498\"",
                    "oldValue": ""
                }
            ],
            "outcome_reason": "Microsoft.Online.Workflows.SpnValidationException",
            "outcome": "failure",
            "type": "add"
        },
        "azuread": {
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "operationName": "Add service principal",
            "operationVersion": "1.0",
            "category": "AuditLogs",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "durationMs": 0,
            "correlationId": "191e390a-0c29-41e1-874b-c57ca3599213",
            "identity": "Microsoft Azure AD Internal - Jit Provisioning",
            "properties": {
                "id": "Directory_GMR7H_185505965",
                "correlationId": "191e390a-0c29-41e1-874b-c57ca3599213"
            }
        }
    }
    	
	```


=== "add_user.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:29:28.6242725Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Add user\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"d40fb664-9901-4cfa-bd3b-afeff8d6b0de\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_HR9C4_45223131\",\"category\": \"UserManagement\",\"correlationId\": \"d40fb664-9901-4cfa-bd3b-afeff8d6b0de\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Add user\",\"activityDateTime\": \"2019-06-24T09:29:28.6242725+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Add\",\"initiatedBy\": {\"user\": {\"id\": \"158c144c-4c1d-4eb4-be08-f2732c8338fd\",\"displayName\": null,\"userPrincipalName\": \"user_gmail.com#EXT#@usergmail.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"type\": \"User\",\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"modifiedProperties\": [{\"displayName\": \"AccountEnabled\",\"oldValue\": \"[]\",\"newValue\": \"[true]\"},{\"displayName\": \"StsRefreshTokensValidFrom\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"2019-06-24T09:29:28Z\\\"]\"},{\"displayName\": \"UserPrincipalName\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"jean.dupont@usergmail.onmicrosoft.com\\\"]\"},{\"displayName\": \"UserType\",\"oldValue\": \"[]\",\"newValue\": \"[\\\"Member\\\"]\"},{\"displayName\": \"Included Updated Properties\",\"oldValue\": null,\"newValue\": \"\\\"AccountEnabled, StsRefreshTokensValidFrom, UserPrincipalName, UserType\\\"\"}]}],\"additionalDetails\": []}}",
        "event": {
            "category": [
                "iam"
            ]
        },
        "@timestamp": "2019-06-24T09:29:28.624272Z",
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Add user",
            "properties": [
                {
                    "name": "AccountEnabled",
                    "newValue": "[true]",
                    "oldValue": "[]"
                },
                {
                    "name": "StsRefreshTokensValidFrom",
                    "newValue": "[\"2019-06-24T09:29:28Z\"]",
                    "oldValue": "[]"
                },
                {
                    "name": "UserPrincipalName",
                    "newValue": "[\"jean.dupont@usergmail.onmicrosoft.com\"]",
                    "oldValue": "[]"
                },
                {
                    "name": "UserType",
                    "newValue": "[\"Member\"]",
                    "oldValue": "[]"
                },
                {
                    "name": "jean.dupont@usergmail.onmicrosoft.com",
                    "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3",
                    "type": "targetedUser"
                }
            ],
            "target": "user",
            "outcome": "success",
            "type": "add"
        },
        "azuread": {
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "operationName": "Add user",
            "operationVersion": "1.0",
            "category": "AuditLogs",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "durationMs": 0,
            "correlationId": "d40fb664-9901-4cfa-bd3b-afeff8d6b0de",
            "properties": {
                "targetUserPrincipalName": "jean.dupont@usergmail.onmicrosoft.com",
                "id": "Directory_HR9C4_45223131",
                "correlationId": "d40fb664-9901-4cfa-bd3b-afeff8d6b0de"
            }
        },
        "user": {
            "id": "158c144c-4c1d-4eb4-be08-f2732c8338fd",
            "name": "user_gmail.com#EXT#@usergmail.onmicrosoft.com"
        },
        "related": {
            "user": [
                "user_gmail.com#EXT#@usergmail.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "auth.json"

    ```json
	
    {
        "message": "{\"id\":\"39e3a81e-99b9-4a30-8000-f38a970e5100\",\"createdDateTime\":\"2020-09-28T10:12:41.4104242Z\",\"userDisplayName\":\"Jane Doe\",\"userPrincipalName\":\"jane.doe@sekoiacorp.onmicrosoft.com\",\"userId\":\"913f4b76-e10f-4f1c-aaf1-09356389319b\",\"appId\":\"4345a7b9-9a63-4910-a426-35363201d503\",\"appDisplayName\":\"O365 Suite UX\",\"ipAddress\":\"11.11.11.11\",\"clientAppUsed\":\"Browser\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0\",\"correlationId\":\"26e7584c-876b-425f-9119-49b411e21365\",\"conditionalAccessStatus\":\"notApplied\",\"originalRequestId\":\"39e3a81e-99b9-4a30-8000-f38a970e5100\",\"isInteractive\":false,\"tokenIssuerName\":\"\",\"tokenIssuerType\":\"AzureAD\",\"processingTimeInMilliseconds\":101,\"riskDetail\":\"hidden\",\"riskLevelAggregated\":\"hidden\",\"riskLevelDuringSignIn\":\"hidden\",\"riskState\":\"none\",\"riskEventTypes\":[],\"riskEventTypes_v2\":[],\"resourceDisplayName\":\"Windows Azure Active Directory\",\"resourceId\":\"00000002-0000-0000-c000-000000000000\",\"resourceTenantId\":\"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\",\"authenticationMethodsUsed\":[],\"authenticationRequirement\":\"multiFactorAuthentication\",\"alternateSignInName\":null,\"servicePrincipalName\":null,\"signInEventTypes\":[],\"servicePrincipalId\":\"\",\"status\":{\"errorCode\":0,\"failureReason\":\"Other.\",\"additionalDetails\":\"MFA requirement satisfied by claim in the token\"},\"deviceDetail\":{\"deviceId\":\"\",\"displayName\":null,\"operatingSystem\":\"Windows 10\",\"browser\":\"Firefox 81.0\",\"isCompliant\":null,\"isManaged\":null,\"trustType\":null},\"location\":{\"city\":\"Paris\",\"state\":\"Paris\",\"countryOrRegion\":\"FR\",\"geoCoordinates\":{\"altitude\":null,\"latitude\":48.861000061035156,\"longitude\":2.3380000591278076}},\"mfaDetail\":{\"authMethod\":null,\"authDetail\":null},\"appliedConditionalAccessPolicies\":[],\"authenticationProcessingDetails\":[{\"key\":\"Login Hint Present\",\"value\":\"True\"},{\"key\":\"IsCAEToken\",\"value\":\"False\"}],\"networkLocationDetails\":[],\"authenticationDetails\":[{\"authenticationStepDateTime\":\"2020-09-28T10:12:41.4104242Z\",\"authenticationMethod\":null,\"authenticationMethodDetail\":null,\"succeeded\":true,\"authenticationStepResultDetail\":\"MFA requirement satisfied by claim in the token\",\"authenticationStepRequirement\":\"User\"}],\"authenticationRequirementPolicies\":[]}",
        "event": {
            "category": [
                "authentication"
            ],
            "type": [
                "start"
            ]
        },
        "@timestamp": "2020-09-28T10:12:41.410424Z",
        "service": {
            "type": "ldap",
            "name": "Windows Azure Active Directory"
        },
        "user": {
            "id": "913f4b76-e10f-4f1c-aaf1-09356389319b",
            "name": "jane.doe@sekoiacorp.onmicrosoft.com"
        },
        "source": {
            "ip": "11.11.11.11",
            "address": "11.11.11.11"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
            "name": "Firefox",
            "device": {
                "name": "Other"
            },
            "version": "81.0",
            "os": {
                "name": "Windows",
                "version": "10"
            }
        },
        "azuread": {
            "resourceId": "00000002-0000-0000-c000-000000000000",
            "correlationId": "26e7584c-876b-425f-9119-49b411e21365",
            "tokenIssuerType": "AzureAD",
            "resourceTenantId": "aa09a079-7796-46a8-a4d4-4d21b0dcf1b2",
            "authenticationRequirementPolicies": [],
            "authenticationRequirement": "multiFactorAuthentication",
            "authenticationDetails": [
                {
                    "authenticationStepDateTime": "2020-09-28T10:12:41.4104242Z",
                    "authenticationMethod": null,
                    "authenticationMethodDetail": null,
                    "succeeded": true,
                    "authenticationStepResultDetail": "MFA requirement satisfied by claim in the token",
                    "authenticationStepRequirement": "User"
                }
            ]
        },
        "action": {
            "target": "user",
            "name": "authentication"
        },
        "host": {
            "os": {
                "name": "Windows 10"
            }
        },
        "related": {
            "ip": [
                "11.11.11.11"
            ],
            "user": [
                "jane.doe@sekoiacorp.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "change_user_password.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:32:07.4637225Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Change user password\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"fd39aead-f711-4c4f-b6a9-ced2c67f3fca\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_1PF86_84995790\",\"category\": \"UserManagement\",\"correlationId\": \"fd39aead-f711-4c4f-b6a9-ced2c67f3fca\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Change user password\",\"activityDateTime\": \"2019-06-24T09:32:07.4637225+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Update\",\"initiatedBy\": {\"user\": {\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"type\": \"User\",\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"modifiedProperties\": []}],\"additionalDetails\": []}}",
        "event": {
            "category": [
                "iam"
            ]
        },
        "@timestamp": "2019-06-24T09:32:07.463722Z",
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Change user password",
            "properties": [
                {
                    "name": "jean.dupont@usergmail.onmicrosoft.com",
                    "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3",
                    "type": "targetedUser"
                }
            ],
            "target": "user",
            "outcome": "success",
            "type": "update"
        },
        "azuread": {
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "operationName": "Change user password",
            "operationVersion": "1.0",
            "category": "AuditLogs",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "durationMs": 0,
            "correlationId": "fd39aead-f711-4c4f-b6a9-ced2c67f3fca",
            "properties": {
                "targetUserPrincipalName": "jean.dupont@usergmail.onmicrosoft.com",
                "id": "Directory_1PF86_84995790",
                "correlationId": "fd39aead-f711-4c4f-b6a9-ced2c67f3fca"
            }
        },
        "user": {
            "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3",
            "name": "jean.dupont@usergmail.onmicrosoft.com"
        },
        "related": {
            "user": [
                "jean.dupont@usergmail.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "empty_geolocalisation.json"

    ```json
	
    {
        "message": "{\"time\":\"2022-04-05T13:07:16.7796535Z\",\"resourceId\":\"/tenants/e6eb2b5c-ad71-4c33-9856-1ed49b85bfe2/providers/Microsoft.aadiam\",\"operationName\":\"Sign-in activity\",\"operationVersion\":\"1.0\",\"category\":\"SignInLogs\",\"tenantId\":\"e6eb2b5c-ad71-4c33-9856-1ed49b85bfe2\",\"resultType\":\"0\",\"resultSignature\":\"None\",\"durationMs\":0,\"callerIpAddress\":\"2001:0db8:85a3:0000:0000:8a2e:0370:7334\",\"correlationId\":\"7ee10819-f631-4ab1-8edb-4efb7286baba\",\"identity\":\"DUPONT Jean\",\"Level\":4,\"properties\":{\"id\":\"b2fdcc8f-954d-4d88-a035-58daefab4f00\",\"createdDateTime\":\"2022-04-05T13:07:16.7796535+00:00\",\"userDisplayName\":\"DUPONT Jean\",\"userPrincipalName\":\"jean.dupont@corp.com\",\"userId\":\"a1c4edf3-59b6-40a8-a1cd-820691c0bab0\",\"appId\":\"00000002-0000-0ff1-ce00-000000000000\",\"appDisplayName\":\"Office 365 Exchange Online\",\"ipAddress\":\"2001:0db8:85a3:0000:0000:8a2e:0370:7334\",\"status\":{\"errorCode\":0},\"clientAppUsed\":\"Exchange Web Services\",\"userAgent\":\"Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.14326; Pro)\",\"deviceDetail\":{\"deviceId\":\"\",\"operatingSystem\":\"Windows 10\",\"browser\":\"Microsoft Office 16.0\"},\"location\":{\"geoCoordinates\":{}},\"correlationId\":\"7ee10819-f631-4ab1-8edb-4efb7286baba\",\"conditionalAccessStatus\":\"notApplied\",\"appliedConditionalAccessPolicies\":[{\"id\":\"57b51b76-0ff5-41fe-b9be-49449a02e65a\",\"displayName\":\"MFA conditionnel BE\",\"enforcedGrantControls\":[\"Mfa\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"ccb983ba-87fb-41bd-bf12-40fd651ff48c\",\"displayName\":\"MFA-Office365-Test\",\"enforcedGrantControls\":[],\"enforcedSessionControls\":[],\"result\":\"notEnabled\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":0},{\"id\":\"3a723733-f1ed-472e-bbe0-51cadafa2a44\",\"displayName\":\"MFA-Docusign-Test\",\"enforcedGrantControls\":[],\"enforcedSessionControls\":[],\"result\":\"notEnabled\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":0}],\"authenticationContextClassReferences\":[],\"originalRequestId\":\"b2fdcc8f-954d-4d88-a035-58daefab4f00\",\"isInteractive\":true,\"tokenIssuerName\":\"\",\"tokenIssuerType\":\"AzureAD\",\"authenticationProcessingDetails\":[{\"key\":\"Legacy TLS (TLS 1.0, 1.1, 3DES)\",\"value\":\"False\"},{\"key\":\"Oauth Scope Info\",\"value\":\"[\\\"AuditLog.Create\\\",\\\"Chat.Read\\\",\\\"DataLossPreventionPolicy.Evaluate\\\",\\\"Directory.Read.All\\\",\\\"EduRoster.ReadBasic\\\",\\\"Files.ReadWrite.All\\\",\\\"Group.ReadWrite.All\\\",\\\"InformationProtectionPolicy.Read\\\",\\\"Notes.Create\\\",\\\"OnlineMeetings.Read\\\",\\\"OnlineMeetings.ReadWrite\\\",\\\"People.Read\\\",\\\"SensitiveInfoType.Detect\\\",\\\"SensitiveInfoType.Read.All\\\",\\\"SensitivityLabel.Evaluate\\\",\\\"User.Invite.All\\\",\\\"User.Read\\\",\\\"User.ReadBasic.All\\\"]\"},{\"key\":\"Is CAE Token\",\"value\":\"False\"}],\"networkLocationDetails\":[],\"processingTimeInMilliseconds\":143,\"riskDetail\":\"none\",\"riskLevelAggregated\":\"none\",\"riskLevelDuringSignIn\":\"none\",\"riskState\":\"none\",\"riskEventTypes\":[],\"riskEventTypes_v2\":[],\"resourceDisplayName\":\"Office 365 Exchange Online\",\"resourceId\":\"00000002-0000-0ff1-ce00-000000000000\",\"resourceTenantId\":\"e6eb2b5c-ad71-4c33-9856-1ed49b85bfe2\",\"homeTenantId\":\"e6eb2b5c-ad71-4c33-9856-1ed49b85bfe2\",\"authenticationDetails\":[{\"authenticationStepDateTime\":\"2022-04-05T13:07:16.7796535+00:00\",\"authenticationMethod\":\"Password\",\"authenticationMethodDetail\":\"Password Hash Sync\",\"succeeded\":true,\"authenticationStepRequirement\":\"Primary authentication\",\"StatusSequence\":0,\"RequestSequence\":1}],\"authenticationRequirementPolicies\":[],\"authenticationRequirement\":\"singleFactorAuthentication\",\"alternateSignInName\":\"jean.dupont@corp.com\",\"signInIdentifier\":\"jean.dupont@corp.com\",\"servicePrincipalId\":\"\",\"userType\":\"Member\",\"flaggedForReview\":false,\"isTenantRestricted\":false,\"crossTenantAccessType\":\"none\",\"privateLinkDetails\":{},\"ssoExtensionVersion\":\"\",\"uniqueTokenIdentifier\":\"11111111111111111111111111\",\"incomingTokenType\":\"none\",\"authenticationProtocol\":\"ropc\",\"appServicePrincipalId\":null,\"resourceServicePrincipalId\":\"51e8e487-e7b3-4d36-ae84-13f30beca934\"}}",
        "event": {
            "category": [
                "authentication"
            ]
        },
        "@timestamp": "2022-04-05T13:07:16.779653Z",
        "service": {
            "type": "ldap",
            "name": "Office 365 Exchange Online"
        },
        "action": {
            "name": "Sign-in activity"
        },
        "azuread": {
            "resourceId": "/tenants/e6eb2b5c-ad71-4c33-9856-1ed49b85bfe2/providers/Microsoft.aadiam",
            "operationName": "Sign-in activity",
            "operationVersion": "1.0",
            "category": "SignInLogs",
            "tenantId": "e6eb2b5c-ad71-4c33-9856-1ed49b85bfe2",
            "durationMs": 0,
            "correlationId": "7ee10819-f631-4ab1-8edb-4efb7286baba",
            "identity": "DUPONT Jean",
            "Level": 4,
            "callerIpAddress": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "properties": {
                "id": "b2fdcc8f-954d-4d88-a035-58daefab4f00",
                "correlationId": "7ee10819-f631-4ab1-8edb-4efb7286baba",
                "appDisplayName": "Office 365 Exchange Online",
                "authenticationProtocol": "ropc",
                "riskEventTypes": [],
                "riskEventTypes_v2": [],
                "riskLevelAggregated": "none",
                "riskLevelDuringSignIn": "none",
                "riskState": "none",
                "riskDetail": "none",
                "status": {
                    "errorCode": "0"
                }
            }
        },
        "source": {
            "ip": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "address": "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        },
        "user": {
            "full_name": "DUPONT Jean",
            "email": "jean.dupont@corp.com"
        },
        "user_agent": {
            "original": "Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.14326; Pro)",
            "device": {
                "name": "Other"
            },
            "name": "Outlook",
            "version": "2016",
            "os": {
                "name": "Windows",
                "version": "10"
            }
        },
        "related": {
            "ip": [
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
            ]
        }
    }
    	
	```


=== "remove_domain.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:21:50.0418907Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Remove unverified domain\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"d60a1c27-11fa-4777-a349-c6c26ef33348\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_NFSWZ_16832133\",\"category\": \"DirectoryManagement\",\"correlationId\": \"d60a1c27-11fa-4777-a349-c6c26ef33348\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Remove unverified domain\",\"activityDateTime\": \"2019-06-24T09:21:50.0418907+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Delete\",\"initiatedBy\": {\"user\": {\"id\": \"158c144c-4c1d-4eb4-be08-f2732c8338fd\",\"displayName\": null,\"userPrincipalName\": \"use_gmail.com#EXT#@usegmail.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": null,\"displayName\": \"sekoiacorp.onmicrosoft.com\",\"modifiedProperties\": []}],\"additionalDetails\": []}}",
        "event": {
            "category": [
                "iam"
            ]
        },
        "@timestamp": "2019-06-24T09:21:50.041890Z",
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Remove unverified domain",
            "properties": [],
            "target": "user",
            "outcome": "success",
            "type": "delete"
        },
        "azuread": {
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "operationName": "Remove unverified domain",
            "operationVersion": "1.0",
            "category": "AuditLogs",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "durationMs": 0,
            "correlationId": "d60a1c27-11fa-4777-a349-c6c26ef33348",
            "properties": {
                "id": "Directory_NFSWZ_16832133",
                "correlationId": "d60a1c27-11fa-4777-a349-c6c26ef33348"
            }
        },
        "user": {
            "id": "158c144c-4c1d-4eb4-be08-f2732c8338fd",
            "name": "use_gmail.com#EXT#@usegmail.onmicrosoft.com"
        },
        "related": {
            "user": [
                "use_gmail.com#EXT#@usegmail.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "sign-in_activity.json"

    ```json
	
    {
        "message": "{\"time\":\"2022-03-30T14:52:21.7062186Z\",\"resourceId\":\"/tenants/34314e6e-4023-4e4b-a15e-143f63244e2b/providers/Microsoft.aadiam\",\"operationName\":\"Sign-in activity\",\"operationVersion\":\"1.0\",\"category\":\"SignInLogs\",\"tenantId\":\"34314e6e-4023-4e4b-a15e-143f63244e2b\",\"resultType\":\"50158\",\"resultSignature\":\"None\",\"resultDescription\":\"External security challenge was not satisfied.\",\"durationMs\":0,\"callerIpAddress\":\"11.11.11.11\",\"correlationId\":\"e68960e2-8996-448c-ba7a-e54eeb8ff2ed\",\"identity\":\"User Name\",\"Level\":4,\"location\":\"FR\",\"properties\":{\"id\":\"22253f56-6fc4-45f2-b148-d7fe15504900\",\"createdDateTime\":\"2022-03-30T14:52:21.7062186+00:00\",\"userDisplayName\":\"User Name\",\"userPrincipalName\":\"User.Name@corp.name\",\"userId\":\"469a0b32-4a8d-4b73-89aa-25ab78df7523\",\"appId\":\"89bee1f7-5e6e-4d8a-9f3d-ecd601259da7\",\"appDisplayName\":\"Office365 Shell WCSS-Client\",\"ipAddress\":\"11.11.11.11\",\"status\":{\"errorCode\":50158,\"failureReason\":\"External security challenge was not satisfied.\"},\"clientAppUsed\":\"Browser\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36\",\"deviceDetail\":{\"deviceId\":\"\",\"operatingSystem\":\"Windows 10\",\"browser\":\"Chrome 99.0.4844\"},\"location\":{\"city\":\"Bordeaux\",\"state\":\"Gironde\",\"countryOrRegion\":\"FR\",\"geoCoordinates\":{\"latitude\":44.84040069580078,\"longitude\":-0.5805000066757202}},\"correlationId\":\"e68960e2-8996-448c-ba7a-e54eeb8ff2ed\",\"conditionalAccessStatus\":\"failure\",\"appliedConditionalAccessPolicies\":[{\"id\":\"bc737765-a8db-4902-8000-f389a97feefd\",\"displayName\":\"Check Point Harmony MFA\",\"enforcedGrantControls\":[\"Checkpoint Custom Control\"],\"enforcedSessionControls\":[],\"result\":\"failure\",\"conditionsSatisfied\":3,\"conditionsNotSatisfied\":0},{\"id\":\"174e7650-f969-47fc-bbd5-83e633e0925e\",\"displayName\":\"Access Control Nine Work for Android\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"5fbf9306-99b8-4781-b5fc-81a0787fb289\",\"displayName\":\"Access Control PowerBI (Poste de travail)\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"d1144840-7d4a-44eb-83f1-543c15f89eb8\",\"displayName\":\"Access Control Snowflake\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"90c5434d-decc-4195-b7f9-024cd39fdca4\",\"displayName\":\"Access Control PowerBI (Mobile)\",\"enforcedGrantControls\":[],\"enforcedSessionControls\":[],\"result\":\"notEnabled\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":0},{\"id\":\"989ecd36-d0e1-4990-bd92-b08250fd45f3\",\"displayName\":\"Access Control Gmail\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"fead0f30-10f4-4472-8bc1-c119d511154d\",\"displayName\":\"MFA Cycloid\",\"enforcedGrantControls\":[\"Mfa\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"6d0db7f6-3263-48b4-84e9-9c37c3959161\",\"displayName\":\"Block - Webmail Exchange Online\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"0ba349bc-748a-4108-b103-298ccd5b1d3f\",\"displayName\":\"Require MFA - Privileged accounts\",\"enforcedGrantControls\":[\"Mfa\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":1,\"conditionsNotSatisfied\":2}],\"originalRequestId\":\"22253f56-6fc4-45f2-b148-d7fe15504900\",\"isInteractive\":true,\"tokenIssuerName\":\"\",\"tokenIssuerType\":\"AzureAD\",\"authenticationProcessingDetails\":[{\"key\":\"Login Hint Present\",\"value\":\"True\"},{\"key\":\"Legacy TLS (TLS 1.0, 1.1, 3DES)\",\"value\":\"False\"},{\"key\":\"Oauth Scope Info\",\"value\":\"\"},{\"key\":\"Is CAE Token\",\"value\":\"False\"}],\"networkLocationDetails\":[{\"networkType\":\"trustedNamedLocation\",\"networkNames\":[\"IP corp\"]}],\"processingTimeInMilliseconds\":91,\"riskDetail\":\"none\",\"riskLevelAggregated\":\"none\",\"riskLevelDuringSignIn\":\"none\",\"riskState\":\"none\",\"riskEventTypes\":[],\"riskEventTypes_v2\":[],\"resourceDisplayName\":\"Office365 Shell WCSS-Server\",\"resourceId\":\"5f09333a-842c-47da-a157-57da27fcbca5\",\"resourceTenantId\":\"34314e6e-4023-4e4b-a15e-143f63244e2b\",\"homeTenantId\":\"34314e6e-4023-4e4b-a15e-143f63244e2b\",\"authenticationDetails\":[{\"authenticationStepDateTime\":\"2022-03-30T14:52:21.7062186+00:00\",\"authenticationMethod\":\"Previously satisfied\",\"succeeded\":true,\"authenticationStepResultDetail\":\"First factor requirement satisfied by claim in the token\",\"authenticationStepRequirement\":\"Primary authentication\",\"StatusSequence\":0,\"RequestSequence\":0}],\"authenticationRequirementPolicies\":[],\"authenticationRequirement\":\"singleFactorAuthentication\",\"servicePrincipalId\":\"\",\"userType\":\"Member\",\"flaggedForReview\":false,\"isTenantRestricted\":false,\"autonomousSystemNumber\":48744,\"crossTenantAccessType\":\"none\",\"privateLinkDetails\":{},\"ssoExtensionVersion\":\"\",\"uniqueTokenIdentifier\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\"incomingTokenType\":\"none\",\"authenticationProtocol\":\"none\"}}",
        "event": {
            "reason": "External security challenge was not satisfied.",
            "category": [
                "authentication"
            ]
        },
        "@timestamp": "2022-03-30T14:52:21.706218Z",
        "service": {
            "type": "ldap",
            "name": "Office365 Shell WCSS-Server"
        },
        "action": {
            "name": "Sign-in activity"
        },
        "azuread": {
            "resourceId": "/tenants/34314e6e-4023-4e4b-a15e-143f63244e2b/providers/Microsoft.aadiam",
            "operationName": "Sign-in activity",
            "operationVersion": "1.0",
            "category": "SignInLogs",
            "tenantId": "34314e6e-4023-4e4b-a15e-143f63244e2b",
            "durationMs": 0,
            "correlationId": "e68960e2-8996-448c-ba7a-e54eeb8ff2ed",
            "identity": "User Name",
            "Level": 4,
            "callerIpAddress": "11.11.11.11",
            "properties": {
                "id": "22253f56-6fc4-45f2-b148-d7fe15504900",
                "correlationId": "e68960e2-8996-448c-ba7a-e54eeb8ff2ed",
                "appDisplayName": "Office365 Shell WCSS-Client",
                "authenticationProtocol": "none",
                "riskEventTypes": [],
                "riskEventTypes_v2": [],
                "riskLevelAggregated": "none",
                "riskLevelDuringSignIn": "none",
                "riskState": "none",
                "riskDetail": "none",
                "status": {
                    "errorCode": "50158",
                    "failureReason": "External security challenge was not satisfied."
                }
            }
        },
        "source": {
            "ip": "11.11.11.11",
            "geo": {
                "city_name": "Bordeaux",
                "region_name": "Gironde",
                "country_iso_code": "FR",
                "location": {
                    "lon": -0.5805000066757202,
                    "lat": 44.84040069580078
                }
            },
            "address": "11.11.11.11"
        },
        "user": {
            "full_name": "User Name",
            "email": "User.Name@corp.name"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
            "device": {
                "name": "Other"
            },
            "name": "Chrome",
            "version": "99.0.4844",
            "os": {
                "name": "Windows",
                "version": "10"
            }
        },
        "related": {
            "ip": [
                "11.11.11.11"
            ]
        }
    }
    	
	```


=== "sign-in_activity2.json"

    ```json
	
    {
        "message": "{\"time\":\"2022-03-31T12:26:46.0190957Z\",\"resourceId\":\"/tenants/34314e6e-4023-4e4b-a15e-143f63244e2b/providers/Microsoft.aadiam\",\"operationName\":\"Sign-in activity\",\"operationVersion\":\"1.0\",\"category\":\"SignInLogs\",\"tenantId\":\"34314e6e-4023-4e4b-a15e-143f63244e2b\",\"resultType\":\"0\",\"resultSignature\":\"None\",\"durationMs\":0,\"callerIpAddress\":\"11.11.11.11\",\"correlationId\":\"467c1340-0762-40d2-b6fb-339235633ebb\",\"identity\":\"Admin Jean Dupont\",\"Level\":4,\"location\":\"FR\",\"properties\":{\"id\":\"8795994f-0bb8-46d7-8797-8c9c385d5900\",\"createdDateTime\":\"2022-03-31T12:26:46.0190957+00:00\",\"userDisplayName\":\"Admin Jean Dupont\",\"userPrincipalName\":\"admin.jdupont@corp.net\",\"userId\":\"16cc2d55-637f-4e04-850d-a1048b659112\",\"appId\":\"0000000c-0000-0000-c000-000000000000\",\"appDisplayName\":\"Microsoft App Access Panel\",\"ipAddress\":\"11.11.11.11\",\"status\":{\"errorCode\":0,\"additionalDetails\":\"MFA requirement satisfied by claim in the token\"},\"clientAppUsed\":\"Browser\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0\",\"deviceDetail\":{\"deviceId\":\"\",\"operatingSystem\":\"Windows 10\",\"browser\":\"Firefox 98.0\"},\"location\":{\"city\":\"Bordeaux\",\"state\":\"Gironde\",\"countryOrRegion\":\"FR\",\"geoCoordinates\":{\"latitude\":44.84040069580078,\"longitude\":-0.5805000066757202}},\"mfaDetail\":{},\"correlationId\":\"467c1340-0762-40d2-b6fb-339235633ebb\",\"conditionalAccessStatus\":\"success\",\"appliedConditionalAccessPolicies\":[{\"id\":\"174e7650-f969-47fc-bbd5-83e633e0925e\",\"displayName\":\"Access Control Nine Work for Android\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"5fbf9306-99b8-4781-b5fc-81a0787fb289\",\"displayName\":\"Access Control PowerBI (Poste de travail)\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"d1144840-7d4a-44eb-83f1-543c15f89eb8\",\"displayName\":\"Access Control Snowflake\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"90c5434d-decc-4195-b7f9-024cd39fdca4\",\"displayName\":\"Access Control PowerBI (Mobile)\",\"enforcedGrantControls\":[],\"enforcedSessionControls\":[],\"result\":\"notEnabled\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":0},{\"id\":\"989ecd36-d0e1-4990-bd92-b08250fd45f3\",\"displayName\":\"Access Control Gmail\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"fead0f30-10f4-4472-8bc1-c119d511154d\",\"displayName\":\"MFA Cycloid\",\"enforcedGrantControls\":[\"Mfa\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"bc737765-a8db-4902-8000-f389a97feefd\",\"displayName\":\"Check Point Harmony MFA\",\"enforcedGrantControls\":[\"Checkpoint Custom Control\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"6d0db7f6-3263-48b4-84e9-9c37c3959161\",\"displayName\":\"Block - Webmail Exchange Online\",\"enforcedGrantControls\":[\"Block\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":0,\"conditionsNotSatisfied\":1},{\"id\":\"0ba349bc-748a-4108-b103-298ccd5b1d3f\",\"displayName\":\"Require MFA - Privileged accounts\",\"enforcedGrantControls\":[\"Mfa\"],\"enforcedSessionControls\":[],\"result\":\"notApplied\",\"conditionsSatisfied\":3,\"conditionsNotSatisfied\":8}],\"originalRequestId\":\"8795994f-0bb8-46d7-8797-8c9c385d5900\",\"isInteractive\":true,\"tokenIssuerName\":\"\",\"tokenIssuerType\":\"AzureAD\",\"authenticationProcessingDetails\":[{\"key\":\"Legacy TLS (TLS 1.0, 1.1, 3DES)\",\"value\":\"False\"},{\"key\":\"Oauth Scope Info\",\"value\":\"\"},{\"key\":\"Is CAE Token\",\"value\":\"False\"}],\"networkLocationDetails\":[{\"networkType\":\"trustedNamedLocation\",\"networkNames\":[\"IP network\"]}],\"processingTimeInMilliseconds\":80,\"riskDetail\":\"none\",\"riskLevelAggregated\":\"none\",\"riskLevelDuringSignIn\":\"none\",\"riskState\":\"none\",\"riskEventTypes\":[],\"riskEventTypes_v2\":[],\"resourceDisplayName\":\"Windows Azure Active Directory\",\"resourceId\":\"00000002-0000-0000-c000-000000000000\",\"resourceTenantId\":\"34314e6e-4023-4e4b-a15e-143f63244e2b\",\"homeTenantId\":\"34314e6e-4023-4e4b-a15e-143f63244e2b\",\"authenticationDetails\":[{\"authenticationStepDateTime\":\"2022-03-31T12:26:46.0190957+00:00\",\"authenticationMethod\":\"Previously satisfied\",\"succeeded\":true,\"authenticationStepResultDetail\":\"First factor requirement satisfied by claim in the token\",\"authenticationStepRequirement\":\"Primary authentication\",\"StatusSequence\":0,\"RequestSequence\":0}],\"authenticationRequirementPolicies\":[],\"authenticationRequirement\":\"singleFactorAuthentication\",\"servicePrincipalId\":\"\",\"userType\":\"Member\",\"flaggedForReview\":false,\"isTenantRestricted\":false,\"autonomousSystemNumber\":48744,\"crossTenantAccessType\":\"none\",\"privateLinkDetails\":{},\"ssoExtensionVersion\":\"\",\"uniqueTokenIdentifier\":\"ODc5NTk5NGYtMGJiOC00NmQ3LTg3OTctOGM5YzM4NWQ1OTAw\",\"incomingTokenType\":\"none\",\"authenticationProtocol\":\"none\"}}",
        "event": {
            "category": [
                "authentication"
            ]
        },
        "@timestamp": "2022-03-31T12:26:46.019095Z",
        "service": {
            "type": "ldap",
            "name": "Windows Azure Active Directory"
        },
        "action": {
            "name": "Sign-in activity"
        },
        "azuread": {
            "resourceId": "/tenants/34314e6e-4023-4e4b-a15e-143f63244e2b/providers/Microsoft.aadiam",
            "operationName": "Sign-in activity",
            "operationVersion": "1.0",
            "category": "SignInLogs",
            "tenantId": "34314e6e-4023-4e4b-a15e-143f63244e2b",
            "durationMs": 0,
            "correlationId": "467c1340-0762-40d2-b6fb-339235633ebb",
            "identity": "Admin Jean Dupont",
            "Level": 4,
            "callerIpAddress": "11.11.11.11",
            "properties": {
                "id": "8795994f-0bb8-46d7-8797-8c9c385d5900",
                "correlationId": "467c1340-0762-40d2-b6fb-339235633ebb",
                "appDisplayName": "Microsoft App Access Panel",
                "authenticationProtocol": "none",
                "riskEventTypes": [],
                "riskEventTypes_v2": [],
                "riskLevelAggregated": "none",
                "riskLevelDuringSignIn": "none",
                "riskState": "none",
                "riskDetail": "none",
                "status": {
                    "errorCode": "0"
                }
            }
        },
        "source": {
            "ip": "11.11.11.11",
            "geo": {
                "city_name": "Bordeaux",
                "region_name": "Gironde",
                "country_iso_code": "FR",
                "location": {
                    "lon": -0.5805000066757202,
                    "lat": 44.84040069580078
                }
            },
            "address": "11.11.11.11"
        },
        "user": {
            "full_name": "Admin Jean Dupont",
            "email": "admin.jdupont@corp.net"
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "device": {
                "name": "Other"
            },
            "name": "Firefox",
            "version": "98.0",
            "os": {
                "name": "Windows",
                "version": "10"
            }
        },
        "related": {
            "ip": [
                "11.11.11.11"
            ]
        }
    }
    	
	```


=== "update_ststoken.json"

    ```json
	
    {
        "message": "{\"time\": \"2019-06-24T09:32:07.4637225Z\",\"resourceId\": \"/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam\",\"operationName\": \"Update StsRefreshTokenValidFrom Timestamp\",\"operationVersion\": \"1.0\",\"category\": \"AuditLogs\",\"tenantId\": \"f6b9ca1d-c995-41bd-ac32-5fba5580215d\",\"resultSignature\": \"None\",\"durationMs\": 0,\"callerIpAddress\": \"<null>\",\"correlationId\": \"fd39aead-f711-4c4f-b6a9-ced2c67f3fca\",\"level\": \"Informational\",\"properties\": {\"id\": \"Directory_1PF86_84995795\",\"category\": \"UserManagement\",\"correlationId\": \"fd39aead-f711-4c4f-b6a9-ced2c67f3fca\",\"result\": \"success\",\"resultReason\": \"\",\"activityDisplayName\": \"Update StsRefreshTokenValidFrom Timestamp\",\"activityDateTime\": \"2019-06-24T09:32:07.4637225+00:00\",\"loggedByService\": \"Core Directory\",\"operationType\": \"Update\",\"initiatedBy\": {\"user\": {\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"ipAddress\": \"<null>\"}},\"targetResources\": [{\"id\": \"bd8a55aa-6079-4742-8b1b-3f55a398dfc3\",\"displayName\": null,\"type\": \"User\",\"userPrincipalName\": \"jean.dupont@usergmail.onmicrosoft.com\",\"modifiedProperties\": []}],\"additionalDetails\": []}}",
        "event": {
            "category": [
                "iam"
            ]
        },
        "@timestamp": "2019-06-24T09:32:07.463722Z",
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "Update StsRefreshTokenValidFrom Timestamp",
            "properties": [
                {
                    "name": "jean.dupont@usergmail.onmicrosoft.com",
                    "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3",
                    "type": "targetedUser"
                }
            ],
            "target": "user",
            "outcome": "success",
            "type": "update"
        },
        "azuread": {
            "resourceId": "/tenants/f6b9ca1d-c995-41bd-ac32-5fba5580215d/providers/Microsoft.aadiam",
            "operationName": "Update StsRefreshTokenValidFrom Timestamp",
            "operationVersion": "1.0",
            "category": "AuditLogs",
            "tenantId": "f6b9ca1d-c995-41bd-ac32-5fba5580215d",
            "durationMs": 0,
            "correlationId": "fd39aead-f711-4c4f-b6a9-ced2c67f3fca",
            "properties": {
                "targetUserPrincipalName": "jean.dupont@usergmail.onmicrosoft.com",
                "id": "Directory_1PF86_84995795",
                "correlationId": "fd39aead-f711-4c4f-b6a9-ced2c67f3fca"
            }
        },
        "user": {
            "id": "bd8a55aa-6079-4742-8b1b-3f55a398dfc3",
            "name": "jean.dupont@usergmail.onmicrosoft.com"
        },
        "related": {
            "user": [
                "jean.dupont@usergmail.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "user_risk_detection.json"

    ```json
	
    {
        "message": "{\"time\":\"3/24/2022 2:42:35 PM\",\"resourceId\":\"/tenants/2d0c1986-ef7b-4bbf-8428-3c837471e7ad/providers/microsoft.aadiam\",\"operationName\":\"User Risk Detection\",\"operationVersion\":\"1.0\",\"category\":\"UserRiskEvents\",\"tenantId\":\"2d0c1986-ef7b-4bbf-8428-3c837471e7ad\",\"resultSignature\":\"None\",\"durationMs\":0,\"callerIpAddress\":\"11.22.33.44\",\"correlationId\":\"ef7868bd7e94b06ecd6cc965fc826c85d367bb5b9b083da9a26686786a791080\",\"identity\":\"bar foo\",\"Level\":4,\"location\":\"fr\",\"properties\":{\"id\":\"ef7868bd7e94b06ecd6cc965fc826c85d367bb5b9b083da9a26686786a791080\",\"requestId\":\"d38b6ab7-65b0-419c-b83a-a5787d6fa100\",\"correlationId\":\"325294e4-4026-4cc7-889d-b4be570b3254\",\"riskType\":\"unfamiliarFeatures\",\"riskEventType\":\"unfamiliarFeatures\",\"riskState\":\"dismissed\",\"riskLevel\":\"low\",\"riskDetail\":\"aiConfirmedSigninSafe\",\"source\":\"IdentityProtection\",\"detectionTimingType\":\"realtime\",\"activity\":\"signin\",\"ipAddress\":\"11.22.33.44\",\"location\":{\"city\":\"La Guaiserie\",\"state\":\"Loir-Et-Cher\",\"countryOrRegion\":\"FR\",\"geoCoordinates\":{\"altitude\":0.0,\"latitude\":47.45919,\"longitude\":2.21955}},\"activityDateTime\":\"2022-03-24T14:40:04.234Z\",\"detectedDateTime\":\"2022-03-24T14:40:04.234Z\",\"lastUpdatedDateTime\":\"2022-03-24T14:42:35.066Z\",\"userId\":\"4c64c30a-7a60-4211-bef1-5e4279854e85\",\"userDisplayName\":\"bar foo\",\"userPrincipalName\":\"foo.bar@corp.eu\",\"additionalInfo\":\"[{\\\"Key\\\":\\\"userAgent\\\",\\\"Value\\\":\\\"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148\\\"}]\",\"tokenIssuerType\":\"AzureAD\",\"resourceTenantId\":null,\"homeTenantId\":\"2d0c1986-ef7b-4bbf-8428-3c837471e7ad\",\"userType\":\"member\",\"crossTenantAccessType\":\"none\"}}",
        "event": {
            "reason": "unfamiliarFeatures",
            "type": [
                "connection"
            ],
            "category": [
                "iam"
            ]
        },
        "@timestamp": "2022-03-24T14:42:35.000000Z",
        "service": {
            "type": "ldap",
            "name": "Azure Active Directory"
        },
        "action": {
            "name": "User Risk Detection"
        },
        "azuread": {
            "resourceId": "/tenants/2d0c1986-ef7b-4bbf-8428-3c837471e7ad/providers/microsoft.aadiam",
            "operationName": "User Risk Detection",
            "operationVersion": "1.0",
            "category": "UserRiskEvents",
            "tenantId": "2d0c1986-ef7b-4bbf-8428-3c837471e7ad",
            "durationMs": 0,
            "correlationId": "ef7868bd7e94b06ecd6cc965fc826c85d367bb5b9b083da9a26686786a791080",
            "identity": "bar foo",
            "Level": 4,
            "callerIpAddress": "11.22.33.44",
            "properties": {
                "id": "ef7868bd7e94b06ecd6cc965fc826c85d367bb5b9b083da9a26686786a791080",
                "requestId": "d38b6ab7-65b0-419c-b83a-a5787d6fa100",
                "correlationId": "325294e4-4026-4cc7-889d-b4be570b3254",
                "riskEventType": "unfamiliarFeatures",
                "riskState": "dismissed",
                "riskLevel": "low",
                "riskDetail": "aiConfirmedSigninSafe",
                "source": "IdentityProtection",
                "detectionTimingType": "realtime",
                "activity": "signin"
            }
        },
        "source": {
            "ip": "11.22.33.44",
            "geo": {
                "city_name": "La Guaiserie",
                "region_name": "Loir-Et-Cher",
                "country_iso_code": "fr",
                "location": {
                    "lon": 2.21955,
                    "lat": 47.45919
                }
            },
            "address": "11.22.33.44"
        },
        "user": {
            "full_name": "bar foo",
            "email": "foo.bar@corp.eu"
        },
        "related": {
            "ip": [
                "11.22.33.44"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`action.properties` | `array` | action.properties |
|`action.target` | `keyword` | action.target |
|`azuread.Level` | `long` |  |
|`azuread.activityDateTime` | `keyword` |  |
|`azuread.additionalInfo` | `keyword` |  |
|`azuread.authenticationDetails` | `array` |  |
|`azuread.authenticationProtocol` | `keyword` |  |
|`azuread.authenticationRequirement` | `keyword` |  |
|`azuread.authenticationRequirementPolicies` | `array` |  |
|`azuread.autonomousSystemNumber` | `long` |  |
|`azuread.callerIpAddress` | `keyword` |  |
|`azuread.category` | `keyword` |  |
|`azuread.correlationId` | `keyword` |  |
|`azuread.crossTenantAccessType` | `keyword` |  |
|`azuread.detectedDateTime` | `keyword` |  |
|`azuread.durationMs` | `long` |  |
|`azuread.flaggedForReview` | `bool` |  |
|`azuread.homeTenantId` | `keyword` |  |
|`azuread.identity` | `keyword` |  |
|`azuread.incomingTokenType` | `keyword` |  |
|`azuread.isTenantRestricted` | `bool` |  |
|`azuread.lastUpdatedDateTime` | `keyword` |  |
|`azuread.operationName` | `keyword` |  |
|`azuread.operationVersion` | `keyword` |  |
|`azuread.privateLinkDetails` | `list` |  |
|`azuread.properties.activity` | `keyword` |  |
|`azuread.properties.appDisplayName` | `keyword` | appDisplayName |
|`azuread.properties.authenticationProtocol` | `keyword` | authenticationProtocol |
|`azuread.properties.correlationId` | `keyword` |  |
|`azuread.properties.detectionTimingType` | `keyword` |  |
|`azuread.properties.id` | `keyword` |  |
|`azuread.properties.requestId` | `keyword` |  |
|`azuread.properties.riskDetail` | `keyword` |  |
|`azuread.properties.riskEventType` | `keyword` |  |
|`azuread.properties.riskEventTypes` | `keyword` | riskEventTypes |
|`azuread.properties.riskEventTypes_v2` | `keyword` | riskEventTypes_v2 |
|`azuread.properties.riskLevel` | `keyword` |  |
|`azuread.properties.riskLevelAggregated` | `keyword` | riskLevelAggregated |
|`azuread.properties.riskLevelDuringSignIn` | `keyword` | riskLevelDuringSignIn |
|`azuread.properties.riskState` | `keyword` |  |
|`azuread.properties.source` | `keyword` |  |
|`azuread.properties.status.errorCode` | `keyword` |  |
|`azuread.properties.status.failureReason` | `keyword` |  |
|`azuread.properties.targetDevicePrincipalName` | `keyword` |  |
|`azuread.properties.targetUserPrincipalName` | `keyword` |  |
|`azuread.resourceId` | `keyword` |  |
|`azuread.resourceTenantId` | `keyword` |  |
|`azuread.resultSignature` | `keyword` |  |
|`azuread.servicePrincipalId` | `keyword` |  |
|`azuread.ssoExtensionVersion` | `keyword` |  |
|`azuread.tenantId` | `keyword` |  |
|`azuread.tokenIssuerType` | `keyword` |  |
|`azuread.uniqueTokenIdentifier` | `keyword` |  |
|`azuread.userType` | `keyword` |  |
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

