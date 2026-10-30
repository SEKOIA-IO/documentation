
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_cipher_deleted"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1102",
            "typeName": "Cipher_Deleted",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "53346505-2478-5954-0938-639445164520",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T14:12:15.5678901Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_cipher_password_visible"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1108",
            "typeName": "Cipher_ClientToggledPasswordVisible",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "e31a8c04-9812-4c21-b1e9-a3f1012de22a",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:32:10.1230000Z",
            "deviceName": "Chrome Extension",
            "device": "2",
            "ipAddress": "192.168.1.120",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_cipher_updated_missing_ip"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1101",
            "typeName": "Cipher_Updated",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "26902048-2171-5399-9494-223083753413",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T14:12:20.6789012Z",
            "deviceName": "",
            "device": "",
            "ipAddress": "",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_collection_created"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1300",
            "typeName": "Collection_Created",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "49592089-1612-5901-8305-563971413203",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:12:40.7890123Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_collection_management_setting"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1616",
            "typeName": "Organization_CollectionManagement_AllowAdminAccessToAllCollectionItemsEnabled",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:13:40.4444444Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_device_type_with_enrichment_template"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1114",
            "typeName": "Cipher_ClientAutofilled",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "95025527-4378-5000-0022-676165103353",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T14:16:00.1357913Z",
            "deviceType": "Firefox Extension",
            "device": "3",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_domain_not_verified"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "2003",
            "typeName": "OrganizationDomain_NotVerified",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "",
            "installationId": "",
            "date": "2026-10-29T02:00:00.6666666Z",
            "deviceName": "Server",
            "device": "22",
            "ipAddress": "",
            "systemUser": "2",
            "domainName": "corp.example.org",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_empty_fields"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1000",
            "typeName": "User_LoggedIn",
            "memberId": "",
            "organizationId": "",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "",
            "installationId": "",
            "date": "2026-10-29T14:15:00.0000000Z",
            "deviceName": "",
            "device": "",
            "ipAddress": "",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": ""
                }
            }
        }
    }
    ```



=== "test_group_updated"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1401",
            "typeName": "Group_Updated",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "14755408-0494-5740-0137-903672455227",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:13:00.8901234Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": "Engineering"
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_legacy_device_type_template"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1111",
            "typeName": "Cipher_ClientCopiedPassword",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "69520243-0052-5223-1111-985817155144",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T10:02:33.2718281Z",
            "deviceType": "Chrome Extension",
            "device": "2",
            "ipAddress": "192.168.1.120",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": ""
        }
    }
    ```



=== "test_legacy_event_message_template"


    ```json
	{
        "Event": "{\"Date\":\"2026-10-29T08:30:00.1122334Z\",\"Type\":1111,\"UserId\":null,\"OrganizationId\":\"org-12345678\",\"InstallationId\":null,\"ProviderId\":null,\"CipherId\":\"63548008-4792-5593-9820-754724344547\",\"CollectionId\":null,\"GroupId\":null,\"PolicyId\":null,\"OrganizationUserId\":null,\"ProviderUserId\":null,\"ProviderOrganizationId\":null,\"ActingUserId\":\"63433685-1129-5365-9291-307766514122\",\"DeviceType\":9,\"IpAddress\":\"198.51.100.42\",\"IdempotencyId\":\"20163122-3236-5387-0233-334192116230\",\"SystemUser\":null,\"DomainName\":null,\"SecretId\":null,\"ProjectId\":null,\"ServiceAccountId\":null,\"GrantedServiceAccountId\":null,\"SendId\":null,\"AccessRequestId\":null,\"AccessLeaseId\":null}",
        "Source": "Bitwarden",
        "Index": "main",
        "bw_serviceName": "Splunk"
    }
    ```



=== "test_legacy_flat_template"


    ```json
	{
        "bw_serviceName": "Splunk",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "OrganizationUser_UpdatedGroups",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T09:41:07.3141592Z",
            "device": "Chrome",
            "ipAddress": "198.51.100.42",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "actingUserName": "Jane Smith",
            "actingUserEmail": "jane.smith@example.org",
            "actingUserType": "Admin",
            "userName": "John Doe",
            "userEmail": "john.doe@example.org",
            "userType": "User",
            "groupName": ""
        }
    }
    ```



=== "test_member_invited_scim"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1500",
            "typeName": "OrganizationUser_Invited",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "20138202-4204-5432-8065-855428611310",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "",
            "installationId": "",
            "date": "2026-10-29T14:13:05.9012345Z",
            "deviceName": "Server",
            "device": "22",
            "ipAddress": "",
            "systemUser": "1",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_member_removed"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1503",
            "typeName": "OrganizationUser_Removed",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "20138202-4204-5432-8065-855428611310",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:13:20.2222222Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_member_updated"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1502",
            "typeName": "OrganizationUser_Updated",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "20138202-4204-5432-8065-855428611310",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:13:10.1111111Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_policy_updated_provider_managed"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1700",
            "typeName": "Policy_Updated",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "03757203-3504-5022-9505-651204604408",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "48398861-7694-5114-1592-813193405245",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:13:45.5555555Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_secret_retrieved"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "2100",
            "typeName": "Secret_Retrieved",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "",
            "installationId": "",
            "date": "2026-10-29T14:14:00.7777777Z",
            "deviceName": "SDK",
            "device": "21",
            "ipAddress": "10.0.4.55",
            "systemUser": "",
            "domainName": "",
            "secretId": "94219396-1911-5436-1253-354062881605",
            "projectId": "75321928-4921-5130-8820-100745768422",
            "serviceAccountId": "15125118-3949-5055-0103-605374006322",
            "enrichment_details": {
                "actingUser": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_send_accessed_anonymous"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "2510",
            "typeName": "Send_Accessed_Text",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "",
            "installationId": "",
            "date": "2026-10-29T14:14:20.9999999Z",
            "deviceName": "Firefox",
            "device": "10",
            "ipAddress": "203.0.113.9",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "member": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_send_created_email_verification"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "2501",
            "typeName": "Send_Created_Text_WithEmailVerification",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T14:14:10.8888888Z",
            "deviceName": "Linux",
            "device": "8",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "member": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_service_account_user_added"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "2300",
            "typeName": "ServiceAccount_UserAdded",
            "memberId": "20138202-4204-5432-8065-855428611310",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:14:05.7654321Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "15125118-3949-5055-0103-605374006322",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_sponsorships_synced_installation"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1608",
            "typeName": "Organization_SponsorshipsSynced",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "",
            "installationId": "12345678-9012-3456-7890-123456789012",
            "date": "2026-10-29T03:00:00.4242424Z",
            "deviceName": "",
            "device": "",
            "ipAddress": "",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_unexpected_payload"


    ```json
	{
        "source": "other-application",
        "severity": "info",
        "message": "Service started"
    }
    ```



=== "test_unknown_event_code"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "2700",
            "typeName": "Unknown_FutureEvent",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:14:50.1212121Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_unknown_event_code_without_type_name"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "9999",
            "typeName": "",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:14:50.1212121Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_user_exported_vault"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1007",
            "typeName": "User_ClientExportedVault",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T14:12:00.4567890Z",
            "deviceName": "Windows",
            "device": "6",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "member": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_user_failed_login"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1005",
            "typeName": "User_FailedLogIn",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T14:11:02.2345678Z",
            "deviceName": "macOS",
            "device": "7",
            "ipAddress": "203.0.113.77",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "member": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_user_failed_login_2fa"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1006",
            "typeName": "User_FailedLogIn2fa",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T14:11:30.3456789Z",
            "deviceName": "iOS",
            "device": "1",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "member": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_user_logged_in"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1000",
            "typeName": "User_LoggedIn",
            "memberId": "63433685-1129-5365-9291-307766514122",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "63433685-1129-5365-9291-307766514122",
            "installationId": "",
            "date": "2026-10-29T14:10:05.1234567Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "member": {
                    "name": "John Doe",
                    "email": "john.doe@example.org",
                    "type": "User"
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_vault_exported"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1602",
            "typeName": "Organization_ClientExportedVault",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:35:00.0000000Z",
            "deviceName": "Android",
            "device": "0",
            "ipAddress": "10.0.1.10",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



=== "test_vault_purged"


    ```json
	{
        "bw_serviceName": "Generic HEC",
        "source": "bitwarden",
        "service": "event-logs",
        "event": {
            "object": "event",
            "type": "1601",
            "typeName": "Organization_PurgedVault",
            "memberId": "",
            "organizationId": "org-12345678",
            "providerId": "",
            "itemId": "",
            "collectionId": "",
            "groupId": "",
            "policyId": "",
            "organizationUserId": "",
            "providerUserId": "",
            "providerOrganizationId": "",
            "actingUserId": "69342302-7372-5446-0534-410088376301",
            "installationId": "",
            "date": "2026-10-29T14:13:30.3333333Z",
            "deviceName": "Chrome",
            "device": "9",
            "ipAddress": "198.51.100.42",
            "systemUser": "",
            "domainName": "",
            "secretId": "",
            "projectId": "",
            "serviceAccountId": "",
            "enrichment_details": {
                "actingUser": {
                    "name": "Jane Smith",
                    "email": "jane.smith@example.org",
                    "type": "Admin"
                },
                "member": {
                    "name": "",
                    "email": "",
                    "type": ""
                },
                "group": {
                    "name": ""
                },
                "organization": {
                    "name": "Example Corp"
                }
            }
        }
    }
    ```



