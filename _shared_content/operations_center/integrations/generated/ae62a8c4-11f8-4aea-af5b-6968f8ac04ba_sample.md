
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_event_certificate_create"


    ```json
	{
        "time": "2024-04-03T14:03:10.7886260Z",
        "category": "AuditEvent",
        "operationName": "CertificateCreate",
        "resultType": "Success",
        "correlationId": "1216de2d-b866-4950-983f-46775e7fe659",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/certificates/fdfdffffd",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 202,
            "requestUri": "https://testpermissionvault.vault.azure.net/certificates/fdfdffffd/create?api-version=7.0",
            "isAccessPolicyMatch": true,
            "certificateProperties": {
                "attributes": {
                    "enabled": true
                }
            },
            "certificatePolicyProperties": {
                "certificateProperties": {
                    "subject": "CN=GHEG FFF",
                    "validityInMonths": 12
                },
                "keyProperties": {
                    "type": "RSA",
                    "size": 2048,
                    "reuse": false,
                    "export": true
                },
                "secretProperties": {
                    "type": "application/x-pkcs12"
                },
                "certificateIssuerProperties": {
                    "name": "Self"
                },
                "attributes": {
                    "enabled": true
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "Accepted",
        "durationMs": "575"
    }
    ```



=== "test_event_certificate_import"


    ```json
	{
        "time": "2024-04-08T15:10:25.2996345Z",
        "category": "AuditEvent",
        "operationName": "CertificateImport",
        "resultType": "Success",
        "resultDescription": "Private key is not specified in the specified X.509 PEM certificate content. Please specify private key in the X.509 PEM certificate content.",
        "correlationId": "1de288da-53e4-4563-8b1a-626cbf008d8d",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXXXXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.152.109",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://myright3.vault.azure.net/certificates/mycertiii",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 400,
            "requestUri": "https://myright3.vault.azure.net/certificates/mycertiii/import?api-version=7.0",
            "isAccessPolicyMatch": true,
            "certificatePolicyProperties": {
                "secretProperties": {
                    "type": "application/x-pem-file"
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-92A6-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/MYRIGHT3",
        "operationVersion": "7.0",
        "resultSignature": "Bad Request",
        "durationMs": "16"
    }
    ```



=== "test_event_certificate_import_1"


    ```json
	{
        "time": "2024-04-08T15:13:06.9355325Z",
        "category": "AuditEvent",
        "operationName": "CertificateImport",
        "resultType": "Success",
        "correlationId": "fa80015d-9a44-4786-bf2f-1024a83c63cd",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXXXXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.152.109",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://myright3.vault.azure.net/certificates/yfuffuygu",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://myright3.vault.azure.net/certificates/yfuffuygu/import?api-version=7.0",
            "isAccessPolicyMatch": true,
            "keyProperties": {
                "type": "RSA",
                "size": 2048
            },
            "secretProperties": {
                "type": "application/x-pkcs12"
            },
            "certificateProperties": {
                "attributes": {
                    "enabled": true
                },
                "subject": "E=eff@ee.com, CN=sss, OU=cc, O=ffbb, L=bbdd, S=aabb, C=FR",
                "sha1": "8C593C21ABB940F7D334F927011B30519B2388BB",
                "sha256": "77C4C074B22B1DC59D4071128115BD43AE8FF4ABD1C539E0F0416E46BF037A4D",
                "nbf": "2024-04-08T15:09:12+00:00",
                "exp": "2027-01-03T15:09:12+00:00"
            },
            "certificatePolicyProperties": {
                "secretProperties": {
                    "type": "application/x-pkcs12"
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-92A6-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/MYRIGHT3",
        "operationVersion": "7.0",
        "resultSignature": "OK",
        "durationMs": "222"
    }
    ```



=== "test_event_certificate_update"


    ```json
	{
        "time": "2024-04-04T06:49:04.5484056Z",
        "category": "AuditEvent",
        "operationName": "CertificateUpdate",
        "resultType": "Success",
        "correlationId": "0beabe33-25ee-4b8f-91de-4c7e47645d7b",
        "callerIpAddress": "147.161.246.101",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/certificates/fdfdffffd/2b5dd56d53254413811cb3d3ea2529f1",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/certificates/fdfdffffd/2b5dd56d53254413811cb3d3ea2529f1?api-version=7.0",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-92A6-93068B9DE034/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "OK",
        "durationMs": "92"
    }
    ```



=== "test_event_key_backup"


    ```json
	{
        "time": "2024-04-04T06:47:31.2803447Z",
        "category": "AuditEvent",
        "operationName": "KeyBackup",
        "resultType": "Success",
        "correlationId": "49c05377-7187-4f18-8374-0e101bba261d",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg/backup?api-version=7.3",
            "isAccessPolicyMatch": true,
            "keyProperties": {
                "type": "RSA",
                "attributes": {
                    "hsmPlatform": "0"
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.3",
        "resultSignature": "OK",
        "durationMs": "46"
    }
    ```



=== "test_event_key_delete"


    ```json
	{
        "time": "2024-04-04T06:47:34.7178619Z",
        "category": "AuditEvent",
        "operationName": "KeyDelete",
        "resultType": "Success",
        "correlationId": "1822451f-ce87-4d9e-96bc-a723af8b5748",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg?api-version=7.3",
            "isAccessPolicyMatch": true,
            "keyProperties": {
                "type": "RSA",
                "attributes": {
                    "hsmPlatform": "0"
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.3",
        "resultSignature": "OK",
        "durationMs": "44"
    }
    ```



=== "test_event_key_delete_1"


    ```json
	{
        "time": "2024-04-04T06:47:34.7178619Z",
        "category": "AuditEvent",
        "operationName": "KeyDelete",
        "resultType": "Success",
        "correlationId": "1822451f-ce87-4d9e-96bc-a723af8b5748",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg?api-version=7.3",
            "isAccessPolicyMatch": true,
            "keyProperties": {
                "type": "RSA",
                "attributes": {
                    "hsmPlatform": "0"
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.3",
        "resultSignature": "OK",
        "durationMs": "44"
    }
    ```



=== "test_event_key_get"


    ```json
	{
        "time": "2024-04-03T14:02:45.0948723Z",
        "category": "AuditEvent",
        "operationName": "KeyGet",
        "resultType": "Success",
        "resultDescription": "A key with (name/id) egzghfgrrg was not found in this key vault. If you recently deleted this key you may be able to recover it using the correct recovery command. For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125182",
        "correlationId": "afabe187-cad6-4ca1-9698-e4ed73479b7c",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 404,
            "requestUri": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg?api-version=7.3&x-ms-include-der=true&_=1712126805788",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.3",
        "resultSignature": "Not Found",
        "durationMs": "22"
    }
    ```



=== "test_event_key_get_1"


    ```json
	{
        "time": "2024-04-04T06:47:42.7335214Z",
        "category": "AuditEvent",
        "operationName": "KeyGet",
        "resultType": "Success",
        "correlationId": "425dd404-f29a-4e68-9b88-2c3643b4462e",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXX",
                "appid": "3686488a-04fc-4d8a-b967-XXXXXXX",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/keys/MyFirstKey",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/keys/MyFirstKey?api-version=7.3&x-ms-include-der=true&_=1712127259288",
            "isAccessPolicyMatch": true,
            "keyProperties": {
                "type": "RSA",
                "attributes": {
                    "hsmPlatform": "0"
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-92A6-XXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.3",
        "resultSignature": "OK",
        "durationMs": "12"
    }
    ```



=== "test_event_key_list"


    ```json
	{
        "time": "2024-04-04T06:47:14.1959057Z",
        "category": "AuditEvent",
        "operationName": "KeyList",
        "resultType": "Success",
        "correlationId": "e6f5733d-2c7d-4d66-94bb-7d77a434a44c",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/keys?api-version=7.3&maxresults=25&_=1712126805807",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.3",
        "resultSignature": "OK",
        "durationMs": "57"
    }
    ```



=== "test_event_key_list_1"


    ```json
	{
        "time": "2024-04-02T08:21:11.5722907Z",
        "category": "AuditEvent",
        "operationName": "KeyList",
        "resultType": "Success",
        "resultDescription": "Caller is not authorized to perform action on resource.",
        "correlationId": "4f1a71d0-6490-49dd-a720-1fa8adfef495",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "clientInfo": "3686488a-04fc-4d8a-b967-61f98ec41efe",
            "httpStatusCode": 403,
            "requestUri": "https://keytestint.vault.azure.net/keys?api-version=7.3&maxresults=25&_=1712042263953",
            "isRbacAuthorized": false,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/KEYTESTINT",
        "operationVersion": "7.3",
        "resultSignature": "Forbidden",
        "durationMs": "22"
    }
    ```



=== "test_event_key_list_deleted"


    ```json
	{
        "time": "2024-04-04T06:47:38.2178774Z",
        "category": "AuditEvent",
        "operationName": "KeyListDeleted",
        "resultType": "Success",
        "correlationId": "733c65c4-338c-4ef5-9d95-25ae18b46fda",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/deletedkeys?api-version=7.0",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "OK",
        "durationMs": "46"
    }
    ```



=== "test_event_key_list_versions"


    ```json
	{
        "time": "2024-04-04T06:47:28.1709577Z",
        "category": "AuditEvent",
        "operationName": "KeyListVersions",
        "resultType": "Success",
        "correlationId": "e8f90224-0296-424e-99ba-c5dd9870d362",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/keys/egzghfgrrg/versions?api-version=7.3&maxresults=25&_=1712127259287",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.3",
        "resultSignature": "OK",
        "durationMs": "18"
    }
    ```



=== "test_event_key_purge"


    ```json
	{
        "time": "2024-04-04T06:47:52.0502260Z",
        "category": "AuditEvent",
        "operationName": "KeyPurge",
        "resultType": "Success",
        "resultDescription": "The user, group or application 'appid=3686488a-04fc-4d8a-b967-61f98ec41efe;oid=d4ba3e84-0444-4841-aaf7-XXXXXX;numgroups=2;iss=https://sts.windows.net/d91d59da-80cd-4224-baef-XXXXXXXX/' does not have keys purge permission on key vault 'testPermissionVault;location=francecentral'. For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125287",
        "correlationId": "3cff8050-bd18-4acd-94ba-c6196ffa3ad4",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/deletedkeys/MyFirstKey",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 403,
            "requestUri": "https://testpermissionvault.vault.azure.net/deletedkeys/MyFirstKey?api-version=7.0",
            "isAccessPolicyMatch": false,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "Forbidden",
        "durationMs": "4"
    }
    ```



=== "test_event_key_purge_1"


    ```json
	{
        "time": "2024-04-04T06:47:52.0502260Z",
        "category": "AuditEvent",
        "operationName": "KeyPurge",
        "resultType": "Success",
        "resultDescription": "The user, group or application 'appid=3686488a-04fc-4d8a-b967-XXXXXXX;oid=d4ba3e84-0444-4841-aaf7-XXXXX;numgroups=2;iss=https://sts.windows.net/d91d59da-80cd-4224-baef-10f72c103fc1/' does not have keys purge permission on key vault 'testPermissionVault;location=francecentral'. For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125287",
        "correlationId": "3cff8050-bd18-4acd-94ba-c6196ffa3ad4",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXX",
                "appid": "3686488a-04fc-4d8a-b967-XXXXXXX",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/deletedkeys/MyFirstKey",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 403,
            "requestUri": "https://testpermissionvault.vault.azure.net/deletedkeys/MyFirstKey?api-version=7.0",
            "isAccessPolicyMatch": false,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-92A6-XXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "Forbidden",
        "durationMs": "4"
    }
    ```



=== "test_event_key_update"


    ```json
	{
        "time": "2024-04-08T15:14:05.4057164Z",
        "category": "AuditEvent",
        "operationName": "KeyUpdate",
        "resultType": "Success",
        "correlationId": "bbd1b29d-5b8b-4639-9980-XXXXX",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXXXXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.152.109",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://myright3.vault.azure.net/keys/iiii/c0d4c7ec6efb4fbeaec16a3872519399",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://myright3.vault.azure.net/keys/iiii/c0d4c7ec6efb4fbeaec16a3872519399?api-version=7.3",
            "isAccessPolicyMatch": true,
            "keyProperties": {
                "type": "RSA",
                "operations": [
                    "sign",
                    "unwrapKey",
                    "encrypt",
                    "decrypt"
                ],
                "attributes": {
                    "enabled": true,
                    "exp": 1775660989,
                    "hsmPlatform": "0"
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-92A6-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/MYRIGHT3",
        "operationVersion": "7.3",
        "resultSignature": "OK",
        "durationMs": "66"
    }
    ```



=== "test_event_secret_backup"


    ```json
	{
        "time": "2024-04-04T06:43:32.2816869Z",
        "category": "AuditEvent",
        "operationName": "SecretBackup",
        "resultType": "Success",
        "correlationId": "1062c64b-12ce-4202-aa9f-c60599f19b29",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/secrets/keykey",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/secrets/keykey/backup?api-version=7.0",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "OK",
        "durationMs": "43"
    }
    ```



=== "test_event_secret_delete"


    ```json
	{
        "time": "2024-04-04T06:43:43.7508346Z",
        "category": "AuditEvent",
        "operationName": "SecretDelete",
        "resultType": "Success",
        "correlationId": "7c8262f7-6f52-4887-8eb2-fa32ec32409a",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/secrets/keykey",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/secrets/keykey?api-version=7.0",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "OK",
        "durationMs": "73"
    }
    ```



=== "test_event_secret_get"


    ```json
	{
        "time": "2024-04-03T14:08:43.4316531Z",
        "category": "AuditEvent",
        "operationName": "SecretGet",
        "resultType": "Success",
        "resultDescription": "A secret with (name/id) keykey was not found in this key vault. If you recently deleted this secret you may be able to recover it using the correct recovery command. For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125182",
        "correlationId": "c86f2715-79c5-433f-937c-ed76ddde840c",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/secrets/keykey",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 404,
            "requestUri": "https://testpermissionvault.vault.azure.net/secrets/keykey?api-version=7.0&_=1712126805801",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "Not Found",
        "durationMs": "183"
    }
    ```



=== "test_event_secret_get_1"


    ```json
	{
        "time": "2024-04-02T08:20:49.2681600Z",
        "category": "AuditEvent",
        "operationName": "SecretGet",
        "resultType": "Success",
        "resultDescription": "Caller is not authorized to perform action on resource.\nIf role assignments, deny assignments or role definitions were changed recently, please observe propagation time.\nCaller: appid=3686488a-04fc-4d8a-b967-XXXXX;oid=d4ba3e84-0444-4841-aaf7-XXXXX;iss=https://sts.windows.net/d91d59da-80cd-4224-baef-XXXXXXXX/\nAction: 'Microsoft.KeyVault/vaults/secrets/getSecret/action'\nResource: '/subscriptions/F40A1F1D-F2C6-4444-XXXX/resourcegroups/integration/providers/microsoft.keyvault/vaults/keytestint/secrets/a'\nAssignment: (not found)\nDenyAssignmentId: null\nDecisionReason: null \nVault: keyTestInt;location=francecentral",
        "correlationId": "1b3aa393-f142-4329-8b1f-c5222119ae35",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://keytestint.vault.azure.net/secrets/a",
            "clientInfo": "3686488a-04fc-4d8a-b967-61f98ec41efe",
            "httpStatusCode": 403,
            "requestUri": "https://keytestint.vault.azure.net/secrets/a?api-version=7.0&_=1712042263922",
            "isRbacAuthorized": false,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/KEYTESTINT",
        "operationVersion": "7.0",
        "resultSignature": "Forbidden",
        "durationMs": "27"
    }
    ```



=== "test_event_secret_list"


    ```json
	{
        "time": "2024-04-04T06:43:25.5941616Z",
        "category": "AuditEvent",
        "operationName": "SecretList",
        "resultType": "Success",
        "correlationId": "58127e84-c72e-4f7c-9cd6-a68b8a5da547",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/secrets?api-version=7.0&maxresults=25&_=1712127259280",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "OK",
        "durationMs": "76"
    }
    ```



=== "test_event_secret_list_deleted"


    ```json
	{
        "time": "2024-04-04T06:44:25.3013619Z",
        "category": "AuditEvent",
        "operationName": "SecretListDeleted",
        "resultType": "Success",
        "correlationId": "d5f5868e-5280-41ba-a2e8-17bb3740ec1e",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/deletedsecrets?api-version=7.0",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "OK",
        "durationMs": "30"
    }
    ```



=== "test_event_secret_purge"


    ```json
	{
        "time": "2024-04-04T06:45:24.3756181Z",
        "category": "AuditEvent",
        "operationName": "SecretPurge",
        "resultType": "Success",
        "resultDescription": "The user, group or application 'appid=3686488a-04fc-4d8a-b967-61f98ec41efe;oid=d4ba3e84-0444-4841-aaf7-XXXXXX;numgroups=2;iss=https://sts.windows.net/d91d59da-80cd-4224-baef-XXXXXXXX/' does not have secrets purge permission on key vault 'testPermissionVault;location=francecentral'. For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125287",
        "correlationId": "524974e7-1a6f-4a01-aded-a0b846311986",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/deletedsecrets/mysecret",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 403,
            "requestUri": "https://testpermissionvault.vault.azure.net/deletedsecrets/mysecret?api-version=7.0",
            "isAccessPolicyMatch": false,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "Forbidden",
        "durationMs": "17"
    }
    ```



=== "test_event_secret_purge_1"


    ```json
	{
        "time": "2024-04-04T06:45:40.6759307Z",
        "category": "AuditEvent",
        "operationName": "SecretPurge",
        "resultType": "Success",
        "resultDescription": "The user, group or application 'appid=3686488a-04fc-4d8a-b967-XXXXXXX;oid=d4ba3e84-0444-4841-aaf7-XXXXX;numgroups=2;iss=https://sts.windows.net/d91d59da-80cd-4224-baef-10f72c103fc1/' does not have secrets purge permission on key vault 'testPermissionVault;location=francecentral'. For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125287",
        "correlationId": "ef7f13ed-3382-4838-990f-5947bd778835",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXX",
                "appid": "3686488a-04fc-4d8a-b967-XXXXXXX",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/deletedsecrets/mysecret",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 403,
            "requestUri": "https://testpermissionvault.vault.azure.net/deletedsecrets/mysecret?api-version=7.0",
            "isAccessPolicyMatch": false,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-92A6-XXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "Forbidden",
        "durationMs": "10"
    }
    ```



=== "test_event_secret_restore"


    ```json
	{
        "time": "2024-04-04T06:44:17.4857222Z",
        "category": "AuditEvent",
        "operationName": "SecretRestore",
        "resultType": "Success",
        "resultDescription": "There was a conflict restoring the secret 'https://testpermissionvault.vault.azure.net/secrets/keykey/8fbb0accbfbe4ee4b025649ebabae465'. This can happen if either: a second secret with the same name was created after the first secret was deleted; thus trying to restore a secret whose name is already in use. To fix this, rename the second secret to something else so that the restore works. The second probable cause of this exception is when multiple operations are performed in parallel against the secret. To avoid this error, perform operations against a secret in a sequential manner.",
        "correlationId": "00f4eafb-43a6-412f-a908-fd20d5aef64c",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/secrets/keykey",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 409,
            "requestUri": "https://testpermissionvault.vault.azure.net/secrets/restore?api-version=7.0",
            "isAccessPolicyMatch": true,
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "Conflict",
        "durationMs": "63"
    }
    ```



=== "test_event_secret_update"


    ```json
	{
        "time": "2024-04-03T14:09:01.6116910Z",
        "category": "AuditEvent",
        "operationName": "SecretUpdate",
        "resultType": "Success",
        "correlationId": "0394c72d-e46d-4888-980a-434efc5bca3e",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "oid": "d4ba3e84-0444-4841-aaf7-XXXXXXXX",
                "appid": "3686488a-04fc-4d8a-b967-61f98ec41efe",
                "scp": "user_impersonation",
                "appidacr": "0",
                "xms_az_nwperimid": [],
                "upn": "john.doe@dummy.onmicrosoft.com",
                "ipaddr": "147.161.0.0",
                "unique_name": "john.doe@dummy.onmicrosoft.com",
                "amr": "pwd"
            }
        },
        "properties": {
            "id": "https://testpermissionvault.vault.azure.net/secrets/keykey/8fbb0accbfbe4ee4b025649ebabae465",
            "clientInfo": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/12.0",
            "httpStatusCode": 200,
            "requestUri": "https://testpermissionvault.vault.azure.net/secrets/keykey/8fbb0accbfbe4ee4b025649ebabae465?api-version=7.0",
            "isAccessPolicyMatch": true,
            "secretProperties": {
                "attributes": {
                    "enabled": true,
                    "exp": 1775199200
                }
            },
            "tlsVersion": "TLS1_3"
        },
        "resourceId": "/SUBSCRIPTIONS/F40a1f1d-f2c6-4444-92a6-XXXXXXXXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/TESTPERMISSIONVAULT",
        "operationVersion": "7.0",
        "resultSignature": "OK",
        "durationMs": "79"
    }
    ```



=== "test_event_vault_get"


    ```json
	{
        "time": "2024-04-02T08:20:41.7523185Z",
        "category": "AuditEvent",
        "operationName": "VaultGet",
        "resultType": "Success",
        "correlationId": "78d31457-b2b7-4da4-a76d-56bac62c1687",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "http://schemas.microsoft.com/identity/claims/objectidentifier": "d4ba3e84-0444-4841-aaf7-XXXXX",
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn": "john.doe@dummy.onmicrosoft.com",
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name": "john.doe@dummy.onmicrosoft.com",
                "appid": "c44b4083-3bb0-49c1-b47d-974e53cXXX"
            }
        },
        "properties": {
            "id": "https://keytestint.vault.azure.net/",
            "clientInfo": "Mozilla/5.0",
            "requestUri": "https://management.azure.com/subscriptions/F40A1F1D-F2C6-4444-XXXX/resourceGroups/Integration/providers/Microsoft.KeyVault/vaults/keyTestInt?api-version=2023-08-01-preview",
            "httpStatusCode": 200,
            "properties": {
                "sku": {
                    "Family": "A",
                    "Name": "Standard",
                    "Capacity": null
                },
                "tenantId": "d91d59da-80cd-4224-baef-XXXXXXXX",
                "networkAcls": null,
                "enabledForDeployment": false,
                "enabledForDiskEncryption": false,
                "enabledForTemplateDeployment": false,
                "enableSoftDelete": true,
                "softDeleteRetentionInDays": 90,
                "enableRbacAuthorization": true,
                "enablePurgeProtection": null
            }
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/KEYTESTINT",
        "operationVersion": "2023-08-01-preview",
        "resultSignature": "OK",
        "durationMs": "16"
    }
    ```



=== "test_event_vault_get_1"


    ```json
	{
        "time": "2024-03-30T22:29:57.2784858Z",
        "category": "AuditEvent",
        "operationName": "VaultGet",
        "resultType": "Success",
        "correlationId": "xxxxxxxxxxxxx",
        "callerIpAddress": "1.2.3.4",
        "identity": {
            "claim": {
                "http://schemas.microsoft.com/identity/claims/objectidentifier": "xxxxxxxxxxxxx",
                "appid": "app-id-xxxxxxxxxxxxx"
            }
        },
        "properties": {
            "id": "https://keytestint.vault.azure.net/",
            "clientInfo": "AzureResourceGraph.IngestionWorkerService.global/1.2.3.4",
            "requestUri": "https://brazilsouth.management.azure.com/subscriptions/xxxxxxxx/resourceGroups/Integration/providers/Microsoft.KeyVault/vaults/keyTestInt?api-version=2023-07-01&MaskCMKEnabledProperties=true",
            "httpStatusCode": 200,
            "properties": {
                "sku": {
                    "Family": "A",
                    "Name": "Standard",
                    "Capacity": null
                },
                "tenantId": "xxxxx-xxxx-xxxx-xxxx-xxxxxx",
                "networkAcls": null,
                "enabledForDeployment": false,
                "enabledForDiskEncryption": false,
                "enabledForTemplateDeployment": false,
                "enableSoftDelete": true,
                "softDeleteRetentionInDays": 90,
                "enableRbacAuthorization": true,
                "enablePurgeProtection": null
            }
        },
        "resourceId": "/SUBSCRIPTIONS/xxxxxx/xxxxx/xxxxxxx/xxxxx/MICROSOFT.KEYVAULT/VAULTS/xxxxxxx",
        "operationVersion": "2023-07-01",
        "resultSignature": "OK",
        "durationMs": "17"
    }
    ```



=== "test_event_vault_get_2"


    ```json
	{
        "time": "2016-01-05T01:32:01.2691226Z",
        "resourceId": "/SUBSCRIPTIONS/361DA5D4-A47A-4C79-AFDD-XXXXXXXXXXXX/RESOURCEGROUPS/CONTOSOGROUP/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/CONTOSOKEYVAULT",
        "operationName": "VaultGet",
        "operationVersion": "2015-06-01",
        "category": "AuditEvent",
        "resultType": "Success",
        "resultSignature": "OK",
        "resultDescription": "",
        "durationMs": "78",
        "callerIpAddress": "104.40.82.76",
        "correlationId": "",
        "identity": {
            "claim": {
                "http://schemas.microsoft.com/identity/claims/objectidentifier": "d9da5048-2737-4770-bd64-XXXXXXXXXXXX",
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn": "live.com#username@outlook.com",
                "appid": "1950a258-227b-4e31-a9cf-XXXXXXXXXXXX"
            }
        },
        "properties": {
            "clientInfo": "azure-resource-manager/2.0",
            "requestUri": "https://control-prod-wus.vaultcore.azure.net/subscriptions/361da5d4-a47a-4c79-afdd-XXXXXXXXXXXX/resourcegroups/contosoresourcegroup/providers/Microsoft.KeyVault/vaults/contosokeyvault?api-version=2015-06-01",
            "id": "https://contosokeyvault.vault.azure.net/",
            "httpStatusCode": 200
        }
    }
    ```



=== "test_event_vault_get_3"


    ```json
	{
        "time": "2016-01-05T01:32:01.2691226Z",
        "resourceId": "/SUBSCRIPTIONS/361DA5D4-A47A-4C79-AFDD-XXXXXXXXXXXX/RESOURCEGROUPS/CONTOSOGROUP/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/CONTOSOKEYVAULT",
        "operationName": "VaultGet",
        "operationVersion": "2015-06-01",
        "category": "AuditEvent",
        "resultType": "Success",
        "resultSignature": "Forbidden",
        "resultDescription": "",
        "durationMs": "78",
        "callerIpAddress": "104.40.82.76",
        "correlationId": "",
        "identity": {
            "claim": {
                "http://schemas.microsoft.com/identity/claims/objectidentifier": "d9da5048-2737-4770-bd64-XXXXXXXXXXXX",
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn": "live.com#username@outlook.com",
                "appid": "1950a258-227b-4e31-a9cf-XXXXXXXXXXXX"
            }
        },
        "properties": {
            "clientInfo": "azure-resource-manager/2.0",
            "requestUri": "https://control-prod-wus.vaultcore.azure.net/subscriptions/361da5d4-a47a-4c79-afdd-XXXXXXXXXXXX/resourcegroups/contosoresourcegroup/providers/Microsoft.KeyVault/vaults/contosokeyvault?api-version=2015-06-01",
            "id": "https://contosokeyvault.vault.azure.net/",
            "httpStatusCode": 200
        }
    }
    ```



=== "test_event_vault_get_4"


    ```json
	{
        "time": "2024-04-17T13:34:17.9174081Z",
        "category": "AuditEvent",
        "operationName": "VaultGet",
        "resultType": "Success",
        "correlationId": "correlationIdValue",
        "callerIpAddress": "1.2.3.4",
        "identity": {
            "claim": {
                "http://schemas.microsoft.com/identity/claims/objectidentifier": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn": "test@test.com",
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name": "test@test.com",
                "appid": "appid-xxxxxxxxxxxxxxxxx"
            }
        },
        "properties": {
            "id": "https://testkey.vault.azure.net/",
            "clientInfo": "Mozilla/5.0",
            "requestUri": "https://management.azure.com/subscriptions/xxxxxxxxxxxxxxxx/resourceGroups/Integration/providers/Microsoft.KeyVault/vaults/testkey?api-version=2023-08-01-preview",
            "httpStatusCode": 200,
            "properties": {
                "sku": {
                    "Family": "A",
                    "Name": "Standard",
                    "Capacity": null
                },
                "tenantId": "tenantid-xxxxxxxxxxxxxxxxxxxxx",
                "networkAcls": {
                    "bypass": "AzureServices",
                    "defaultAction": "Allow"
                },
                "enabledForDeployment": false,
                "enabledForDiskEncryption": false,
                "enabledForTemplateDeployment": true,
                "enableSoftDelete": true,
                "softDeleteRetentionInDays": 90,
                "enableRbacAuthorization": true,
                "enablePurgeProtection": null
            }
        },
        "resourceId": "/SUBSCRIPTIONS/xxxxxxxxxxxxxxxx/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/testkey",
        "operationVersion": "2023-08-01-preview",
        "resultSignature": "OK",
        "durationMs": "29"
    }
    ```



=== "test_event_vault_patch"


    ```json
	{
        "time": "2024-04-08T15:15:50.6257670Z",
        "category": "AuditEvent",
        "operationName": "VaultPatch",
        "resultType": "Success",
        "correlationId": "eb6f7f30-b6ae-4ba6-a6cf-fbe90d4d5121",
        "callerIpAddress": "147.161.0.0",
        "identity": {
            "claim": {
                "http://schemas.microsoft.com/identity/claims/objectidentifier": "d4ba3e84-0444-4841-aaf7-XXXXXXXXXXXX",
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn": "john.doe@dummy.onmicrosoft.com",
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name": "john.doe@dummy.onmicrosoft.com",
                "appid": "c44b4083-3bb0-49c1-b47d-974e53cbdf3c"
            }
        },
        "properties": {
            "id": "https://myright3.vault.azure.net/",
            "clientInfo": "Mozilla/5.0",
            "requestUri": "https://management.azure.com/subscriptions/f40a1f1d-f2c6-4444-92a6-XXXX/resourceGroups/Integration/providers/Microsoft.KeyVault/vaults/myright3?api-version=2023-08-01-preview",
            "httpStatusCode": 200,
            "properties": {
                "sku": {
                    "Family": "A",
                    "Name": "Standard",
                    "Capacity": null
                },
                "tenantId": "d91d59da-80cd-4224-baef-10f72c103fc1",
                "networkAcls": {
                    "bypass": "AzureServices",
                    "defaultAction": "Allow"
                },
                "enabledForDeployment": true,
                "enabledForDiskEncryption": false,
                "enabledForTemplateDeployment": false,
                "enableSoftDelete": true,
                "softDeleteRetentionInDays": 90,
                "enableRbacAuthorization": false,
                "enablePurgeProtection": null
            }
        },
        "resourceId": "/SUBSCRIPTIONS/F40A1F1D-F2C6-4444-92A6-XXXX/RESOURCEGROUPS/INTEGRATION/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/MYRIGHT3",
        "operationVersion": "2023-08-01-preview",
        "resultSignature": "OK",
        "durationMs": "78"
    }
    ```



