
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Access tokens` | security identifiers are extracted from several events |
| `Authentication logs` | audit logon events are examined in detail |
| `File monitoring` | information about files are extracted from several events |
| `PowerShell logs` | Windows PowerShell logs are analyzed, and need to be specifically set up |
| `Process command-line parameters` | Windows Security Auditing logs provide information about process creation |
| `Process monitoring` | Windows Security Auditing records information on running process activities |
| `Process use of network` | information on processes having network activities are collected |
| `Windows event logs` | events related to Windows Event logs shutdown or restart are analyzed |
| `Windows Registry` | registry auditing events are examined in detail |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "Event_4719.json"

    ```json
	
    {
        "event": {
            "code": "4719",
            "created": "2021-01-11T10:48:46.476330800Z",
            "provider": "Microsoft-Windows-Security-Auditing",
            "id": "10f0afe9-98a1-4226-a6bd-8f70d461d430"
        },
        "message": "{\"time\":\"2021-01-11T10:48:46.4763308Z\",\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"DeploymentId\":\"e089eb44-8406-4be5-b134-3569ba534888\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZNTDC02\",\"ProviderGuid\":\"{54849625-5478-4994-A5BA-3E3B0328C30D}\",\"ProviderName\":\"Microsoft-Windows-Security-Auditing\",\"EventId\":4719,\"Level\":0,\"Pid\":592,\"Tid\":6452,\"Opcode\":0,\"Task\":13568,\"Channel\":\"Security\",\"Description\":\"System audit policy was changed.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tACMEAccountName$\\r\\n\\tAccount Domain:\\t\\tACME\\r\\n\\tLogon ID:\\t\\t0x3E7\\r\\n\\r\\nAudit Policy Change:\\r\\n\\tCategory:\\t\\tLogon/Logoff\\r\\n\\tSubcategory:\\t\\tLogon\\r\\n\\tSubcategory GUID:\\t{0CCE9215-69AE-11D9-BED3-505054503030}\\r\\n\\tChanges:\\t\\tFailure removed\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4719</EventID><Version>0</Version><Level>0</Level><Task>13568</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime='2021-01-11T10:48:46.476330800Z'/><EventRecordID>56204662</EventRecordID><Correlation ActivityID='{C42E760F-E51E-4CE7-9AF9-0AA6DA068F9B}'/><Execution ProcessID='592' ThreadID='6452'/><Channel>Security</Channel><Computer>WinAzureTest</Computer><Security/></System><EventData><Data Name='SubjectUserSid'>S-1-5-18</Data><Data Name='SubjectUserName'>Acmesubject$</Data><Data Name='SubjectDomainName'>ACME</Data><Data Name='SubjectLogonId'>0x3e7</Data><Data Name='CategoryId'>%%8273</Data><Data Name='SubcategoryId'>%%12544</Data><Data Name='SubcategoryGuid'>{0CCE9215-69AE-11D9-BED3-505054503030}</Data><Data Name='AuditPolicyChanges'>%%8450</Data></EventData></Event>\"}}",
        "process": {
            "pid": 592,
            "thread": {
                "id": 6452
            }
        },
        "action": {
            "id": 4719,
            "name": "System audit policy was changed",
            "record_id": 56204662,
            "type": "Security",
            "outcome": "success",
            "properties": [
                {
                    "AuditPolicyChanges": "%%8450",
                    "opcode": 0
                }
            ]
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "host": {
            "hostname": "WinAzureTest"
        },
        "log": {
            "hostname": "WinAzureTest"
        },
        "azure_windows": {
            "provider_guid": "54849625-5478-4994-A5BA-3E3B0328C30D",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "task": "13568",
            "opcode": "0",
            "event_data": {
                "AuditPolicyChanges": "%%8450",
                "CategoryId": "%%8273",
                "SubcategoryGuid": "{0CCE9215-69AE-11D9-BED3-505054503030}",
                "SubcategoryId": "%%12544",
                "SubjectDomainName": "ACME",
                "SubjectLogonId": "0x3e7",
                "SubjectUserName": "Acmesubject$",
                "SubjectUserSid": "S-1-5-18"
            }
        },
        "user": {
            "domain": "ACME",
            "id": "S-1-5-18",
            "name": "Acmesubject$"
        },
        "related": {
            "user": [
                "Acmesubject$"
            ]
        }
    }
    	
	```


=== "invalid_message.json"

    ```json
	
    {
        "message": "{\"time\":\"2022-03-25T09:08:59.2405321Z\",\"resourceId\":\"/subscriptions/6c5a0310-d590-4fb4-945a-bca5dc5e1417/resourceGroups/MyGroup/providers/Microsoft.Storage/storageAccounts/MyStorageAccount/blobServices/default\",\"category\":\"StorageRead\",\"operationName\":\"GetBlob\",\"schemaVersion\":\"1.0\",\"statusCode\":404,\"statusText\":\"BlobNotFound\",\"durationMs\":1,\"callerIpAddress\":\"1.2.3.4\",\"correlationId\":\"165e8a9d-e08f-43ca-b71b-c2738d24eb66\",\"identity\":{\"type\":\"SAS\",\"tokenHash\":\"system-1(D0B3B275891800D74D0362E6A5CEAEEDD93A110636EFF4CC84CFD05396904C1C),SasSignature(B35B17A0B56ABEDF5D04E11B2AE08EBEC2DEC076742040412D3C034880A3D745)\"},\"location\":\"MyLocation\",\"properties\":{\"accountName\":\"MyStorageAccount\",\"userAgentHeader\":\"AzSerialConsoleSvcPF\",\"serviceType\":\"blob\",\"objectKey\":\"/MyStorageAccount/bootdiagnostics-xxxxxx-84a8d62f-e62c-4001-9ce2-e6a3e25f4f88/XXXXXX.84a8d62f-e62c-4001-9ce2-e6a3e25f4f88.serialconsole-connectionmetadata\",\"lastModifiedTime\":\"1601/01/01 00:00:00.0000000\",\"metricResponseType\":\"ClientOtherError\",\"serverLatencyMs\":1,\"requestHeaderSize\":411,\"responseHeaderSize\":172,\"tlsVersion\":\"TLS 1.2\"},\"uri\":\"https://axenspiproddiag.blob.core.windows.net/bootdiagnostics-azntpi84a8d62f-e62c-4001-9ce2-e6a3e25f4f88/AZNTPI-04.84a8d62f-e62c-4001-9ce2-e6a3e25f4f88.serialconsole-connectionmetadata?sv=2018-03-28&sr=c&sk=system-1&sig=XXXXX&se=9999-01-01T00%3A00%3A00Z&sp=rwd\",\"protocol\":\"HTTPS\",\"resourceType\":\"Microsoft.Storage/storageAccounts/blobServices\"}",
        "os": {
            "family": "windows",
            "platform": "windows"
        }
    }
    	
	```


=== "kerberos.json"

    ```json
	
    {
        "event": {
            "code": "4624",
            "created": "2019-07-22T11:20:54.558577600Z",
            "provider": "Microsoft-Windows-Security-Auditing"
        },
        "message": "{\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"Channel\":\"Security\",\"DeploymentId\":\"cbfba34a-3d3d-4425-aefb-968ee470a8f4\",\"Description\":\"An account was successfully logged on.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-0-0\\r\\n\\tAccount Name:\\t\\t-\\r\\n\\tAccount Domain:\\t\\t-\\r\\n\\tLogon ID:\\t\\t0x0\\r\\n\\r\\nLogon Information:\\r\\n\\tLogon Type:\\t\\t3\\r\\n\\tRestricted Admin Mode:\\t-\\r\\n\\tVirtual Account:\\t\\tNo\\r\\n\\tElevated Token:\\t\\tYes\\r\\n\\r\\nImpersonation Level:\\t\\tIdentification\\r\\n\\r\\nNew Logon:\\r\\n\\tSecurity ID:\\t\\tS-1-5-21-1004336348-2052111302-725345543-33053\\r\\n\\tAccount Name:\\t\\tHOSTMON\\r\\n\\tAccount Domain:\\t\\tACME.LOCAL\\r\\n\\tLogon ID:\\t\\t0x6409B67A\\r\\n\\tLinked Logon ID:\\t\\t0x0\\r\\n\\tNetwork Account Name:\\t-\\r\\n\\tNetwork Account Domain:\\t-\\r\\n\\tLogon GUID:\\t\\t{FF0FDD6A-555D-EA36-45CB-9167DFB9C75D}\\r\\n\\r\\nProcess Information:\\r\\n\\tProcess ID:\\t\\t0x0\\r\\n\\tProcess Name:\\t\\t-\\r\\n\\r\\nNetwork Information:\\r\\n\\tWorkstation Name:\\t-\\r\\n\\tSource Network Address:\\t10.129.224.1\\r\\n\\tSource Port:\\t\\t55731\\r\\n\\r\\nDetailed Authentication Information:\\r\\n\\tLogon Process:\\t\\tKerberos\\r\\n\\tAuthentication Package:\\tKerberos\\r\\n\\tTransited Services:\\t-\\r\\n\\tPackage Name (NTLM only):\\t-\\r\\n\\tKey Length:\\t\\t0\\r\\n\\r\\nThis event is generated when a logon session is created. It is generated on the computer that was accessed.\\r\\n\\r\\nThe subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.\\r\\n\\r\\nThe logon type field indicates the kind of logon that occurred. The most common types are 2 (interactive) and 3 (network).\\r\\n\\r\\nThe New Logon fields indicate the account for whom the new logon was created, i.e. the account that was logged on.\\r\\n\\r\\nThe network fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.\\r\\n\\r\\nThe impersonation level field indicates the extent to which a process in the logon session can impersonate.\\r\\n\\r\\nThe authentication information fields provide detailed information about this specific logon request.\\r\\n\\t- Logon GUID is a unique identifier that can be used to correlate this event with a KDC event.\\r\\n\\t- Transited services indicate which intermediate services have participated in this logon request.\\r\\n\\t- Package name indicates which sub-protocol was used among the NTLM protocols.\\r\\n\\t- Key length indicates the length of the generated session key. This will be 0 if no session key was requested.\",\"EventId\":4624,\"Level\":0,\"Opcode\":0,\"Pid\":632,\"ProviderGuid\":\"{54849625-5478-4994-A5BA-3E3B0328C30D}\",\"ProviderName\":\"Microsoft-Windows-Security-Auditing\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4624</EventID><Version>2</Version><Level>0</Level><Task>12544</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime='2019-07-22T11:20:54.558577600Z'/><EventRecordID>9999727</EventRecordID><Correlation ActivityID='{32528DD5-0278-4450-AFD8-22FEBDA102F1}'/><Execution ProcessID='632' ThreadID='904'/><Channel>Security</Channel><Computer>AZNTPI-01.acme.local</Computer><Security/></System><EventData><Data Name='SubjectUserSid'>S-1-0-0</Data><Data Name='SubjectUserName'>-</Data><Data Name='SubjectDomainName'>-</Data><Data Name='SubjectLogonId'>0x0</Data><Data Name='TargetUserSid'>S-1-5-21-1004336348-2052111302-725345543-33053</Data><Data Name='TargetUserName'>HOSTMON</Data><Data Name='TargetDomainName'>ACME.LOCAL</Data><Data Name='TargetLogonId'>0x6409b67a</Data><Data Name='LogonType'>3</Data><Data Name='LogonProcessName'>Kerberos</Data><Data Name='AuthenticationPackageName'>Kerberos</Data><Data Name='WorkstationName'>-</Data><Data Name='LogonGuid'>{FF0FDD6A-555D-EA36-45CB-9167DFB9C75D}</Data><Data Name='TransmittedServices'>-</Data><Data Name='LmPackageName'>-</Data><Data Name='KeyLength'>0</Data><Data Name='ProcessId'>0x0</Data><Data Name='ProcessName'>-</Data><Data Name='IpAddress'>10.129.224.1</Data><Data Name='IpPort'>55731</Data><Data Name='ImpersonationLevel'>%%1832</Data><Data Name='RestrictedAdminMode'>-</Data><Data Name='TargetOutboundUserName'>-</Data><Data Name='TargetOutboundDomainName'>-</Data><Data Name='VirtualAccount'>%%1843</Data><Data Name='TargetLinkedLogonId'>0x0</Data><Data Name='ElevatedToken'>%%1842</Data></EventData></Event>\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZNTPI-01\",\"Task\":12544,\"Tid\":904},\"time\":\"2019-07-22T11:20:54.5585776Z\"}",
        "source": {
            "address": "10.129.224.1",
            "ip": "10.129.224.1",
            "port": 55731
        },
        "host": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "log": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "process": {
            "pid": 632,
            "thread": {
                "id": 904
            },
            "parent": {
                "pid": 0
            }
        },
        "action": {
            "id": 4624,
            "name": "An account was successfully logged on",
            "record_id": 9999727,
            "type": "Security",
            "outcome": "success",
            "target": "user",
            "properties": [
                {
                    "id": "S-1-5-21-1004336348-2052111302-725345543-33053",
                    "name": "HOSTMON",
                    "domain": "ACME.LOCAL",
                    "opcode": 0,
                    "type": "targetedUser"
                }
            ]
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "user": {
            "id": "S-1-0-0"
        },
        "azure_windows": {
            "provider_guid": "54849625-5478-4994-A5BA-3E3B0328C30D",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "task": "12544",
            "opcode": "0",
            "event_data": {
                "AuthenticationPackageName": "Kerberos",
                "ElevatedToken": "%%1842",
                "ImpersonationLevel": "%%1832",
                "IpAddress": "10.129.224.1",
                "IpPort": "55731",
                "KeyLength": "0",
                "LmPackageName": "-",
                "LogonGuid": "{FF0FDD6A-555D-EA36-45CB-9167DFB9C75D}",
                "LogonProcessName": "Kerberos",
                "LogonType": "3",
                "ProcessId": "0x0",
                "ProcessName": "-",
                "RestrictedAdminMode": "-",
                "SubjectDomainName": "-",
                "SubjectLogonId": "0x0",
                "SubjectUserName": "-",
                "SubjectUserSid": "S-1-0-0",
                "TargetDomainName": "ACME.LOCAL",
                "TargetLinkedLogonId": "0x0",
                "TargetLogonId": "0x6409b67a",
                "TargetOutboundDomainName": "-",
                "TargetOutboundUserName": "-",
                "TargetUserName": "HOSTMON",
                "TargetUserSid": "S-1-5-21-1004336348-2052111302-725345543-33053",
                "TransmittedServices": "-",
                "VirtualAccount": "%%1843",
                "WorkstationName": "-"
            },
            "user": {
                "domain": {
                    "name": "ACME.LOCAL"
                },
                "identifier": "S-1-5-21-1004336348-2052111302-725345543-33053",
                "name": "HOSTMON",
                "type": "targetedUser"
            }
        },
        "related": {
            "ip": [
                "10.129.224.1"
            ],
            "user": "HOSTMON"
        }
    }
    	
	```


=== "key_file_operation.json"

    ```json
	
    {
        "event": {
            "code": "5058",
            "created": "2019-06-24T09:20:18.054208500Z",
            "provider": "Microsoft-Windows-Security-Auditing"
        },
        "message": "{\"time\": \"2019-06-24T09:20:18.0542085Z\",\"category\": \"WindowsEventLogsTable\",\"level\": \"Informational\",\"properties\": {\"DeploymentId\": \"cdc4f011-0dd5-4969-95b1-8c7a914a82f6\",\"Role\": \"IaaS\",\"RoleInstance\": \"_WindowsDesktop\",\"ProviderGuid\": \"{54849625-5478-4994-a5ba-3e3b0328c30d}\",\"ProviderName\": \"Microsoft-Windows-Security-Auditing\",\"EventId\": 5058,\"Level\": 0,\"Pid\": 704,\"Tid\": 6864,\"Opcode\": 0,\"Task\": 12292,\"Channel\": \"Security\",\"Description\": \"Key file operation.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tWindowsDesktop$\\r\\n\\tAccount Domain:\\t\\tWORKGROUP\\r\\n\\tLogon ID:\\t\\t0x3E7\\r\\n\\r\\nProcess Information:\\r\\n\\tProcess ID:\\t\\t5396\\r\\n\\tProcess Creation Time:\\t\u200e2019\u200e-\u200e06\u200e-\u200e24T09:18:43.902454200Z\\r\\n\\r\\nCryptographic Parameters:\\r\\n\\tProvider Name:\\tMicrosoft Software Key Storage Provider\\r\\n\\tAlgorithm Name:\\tUNKNOWN\\r\\n\\tKey Name:\\t{3F1E0FA6-ACA6-4152-803B-976EF5816428}\\r\\n\\tKey Type:\\tMachine key.\\r\\n\\r\\nKey File Operation Information:\\r\\n\\tFile Path:\\tC:\\\\ProgramData\\\\Microsoft\\\\Crypto\\\\RSA\\\\MachineKeys\\\\5dc8d7cc0741b353e4e980818c304a9b_f67648d5-9dc6-457b-b947-f44d21889d9b\\r\\n\\tOperation:\\tRead persisted key from file.\\r\\n\\tReturn Code:\\t0x0\",\"RawXml\": \"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-a5ba-3e3b0328c30d}'/><EventID>5058</EventID><Version>1</Version><Level>0</Level><Task>12292</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime='2019-06-24T09:20:18.054208500Z'/><EventRecordID>249096</EventRecordID><Correlation ActivityID='{4ef44f5e-5539-0000-271e-87006b2ad501}'/><Execution ProcessID='704' ThreadID='6864'/><Channel>Security</Channel><Computer>WindowsDesktop</Computer><Security/></System><EventData><Data Name='SubjectUserSid'>S-1-5-18</Data><Data Name='SubjectUserName'>WindowsDesktop$</Data><Data Name='SubjectDomainName'>WORKGROUP</Data><Data Name='SubjectLogonId'>0x3e7</Data><Data Name='ClientProcessId'>5396</Data><Data Name='ClientCreationTime'>2019-06-24T09:18:43.902454200Z</Data><Data Name='ProviderName'>Microsoft Software Key Storage Provider</Data><Data Name='AlgorithmName'>UNKNOWN</Data><Data Name='KeyName'>{3F1E0FA6-ACA6-4152-803B-976EF5816428}</Data><Data Name='KeyType'>%%2499</Data><Data Name='KeyFilePath'>C:\\\\ProgramData\\\\Microsoft\\\\Crypto\\\\RSA\\\\MachineKeys\\\\5dc8d7cc0741b353e4e980818c304a9b_f67648d5-9dc6-457b-b947-f44d21889d9b</Data><Data Name='Operation'>%%2458</Data><Data Name='ReturnCode'>0x0</Data></EventData></Event>\"}}",
        "process": {
            "pid": 704,
            "thread": {
                "id": 6864
            }
        },
        "host": {
            "hostname": "WindowsDesktop"
        },
        "log": {
            "hostname": "WindowsDesktop"
        },
        "action": {
            "id": 5058,
            "name": "Key file operation",
            "record_id": 249096,
            "type": "Security",
            "outcome": "success",
            "properties": [
                {
                    "opcode": 0
                }
            ]
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "user": {
            "name": "WindowsDesktop$",
            "id": "S-1-5-18",
            "domain": "WORKGROUP"
        },
        "azure_windows": {
            "provider_guid": "54849625-5478-4994-a5ba-3e3b0328c30d",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "task": "12292",
            "opcode": "0",
            "event_data": {
                "AlgorithmName": "UNKNOWN",
                "ClientCreationTime": "2019-06-24T09:18:43.902454200Z",
                "ClientProcessId": "5396",
                "KeyFilePath": "C:\\ProgramData\\Microsoft\\Crypto\\RSA\\MachineKeys\\5dc8d7cc0741b353e4e980818c304a9b_f67648d5-9dc6-457b-b947-f44d21889d9b",
                "KeyName": "{3F1E0FA6-ACA6-4152-803B-976EF5816428}",
                "KeyType": "%%2499",
                "Operation": "%%2458",
                "ProviderName": "Microsoft Software Key Storage Provider",
                "ReturnCode": "0x0",
                "SubjectDomainName": "WORKGROUP",
                "SubjectLogonId": "0x3e7",
                "SubjectUserName": "WindowsDesktop$",
                "SubjectUserSid": "S-1-5-18"
            }
        },
        "related": {
            "user": [
                "WindowsDesktop$"
            ]
        }
    }
    	
	```


=== "loggedoff.json"

    ```json
	
    {
        "event": {
            "code": "4634",
            "created": "2019-07-23T15:33:09.199351700Z",
            "provider": "Microsoft-Windows-Security-Auditing"
        },
        "message": "{\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"Channel\":\"Security\",\"DeploymentId\":\"cbfba34a-3d3d-4425-aefb-968ee470a8f4\",\"Description\":\"An account was logged off.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tAZNTPI-01$\\r\\n\\tAccount Domain:\\t\\tACME\\r\\n\\tLogon ID:\\t\\t0x686007F9\\r\\n\\r\\nLogon Type:\\t\\t\\t3\\r\\n\\r\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.\",\"EventId\":4634,\"Level\":0,\"Opcode\":0,\"Pid\":632,\"ProviderGuid\":\"{54849625-5478-4994-A5BA-3E3B0328C30D}\",\"ProviderName\":\"Microsoft-Windows-Security-Auditing\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4634</EventID><Version>0</Version><Level>0</Level><Task>12545</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime='2019-07-23T15:33:09.199351700Z'/><EventRecordID>10036511</EventRecordID><Correlation/><Execution ProcessID='632' ThreadID='3136'/><Channel>Security</Channel><Computer>AZNTPI-01.acme.local</Computer><Security/></System><EventData><Data Name='TargetUserSid'>S-1-5-18</Data><Data Name='TargetUserName'>AZNTPI-01$</Data><Data Name='TargetDomainName'>ACME</Data><Data Name='TargetLogonId'>0x686007f9</Data><Data Name='LogonType'>3</Data></EventData></Event>\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZNTPI-01\",\"Task\":12545,\"Tid\":3136},\"time\":\"2019-07-23T15:33:09.1993517Z\"}",
        "process": {
            "pid": 632,
            "thread": {
                "id": 3136
            }
        },
        "action": {
            "id": 4634,
            "name": "An account was logged off",
            "record_id": 10036511,
            "type": "Security",
            "outcome": "success",
            "target": "user",
            "properties": [
                {
                    "name": "AZNTPI-01$",
                    "id": "S-1-5-18",
                    "domain": "ACME",
                    "type": "targetedUser",
                    "opcode": 0
                }
            ]
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "host": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "log": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "azure_windows": {
            "provider_guid": "54849625-5478-4994-A5BA-3E3B0328C30D",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "task": "12545",
            "opcode": "0",
            "user": {
                "domain": {
                    "name": "ACME"
                },
                "identifier": "S-1-5-18",
                "name": "AZNTPI-01$",
                "type": "targetedUser"
            },
            "event_data": {
                "LogonType": "3",
                "TargetDomainName": "ACME",
                "TargetLogonId": "0x686007f9",
                "TargetUserName": "AZNTPI-01$",
                "TargetUserSid": "S-1-5-18"
            }
        }
    }
    	
	```


=== "process_operation.json"

    ```json
	
    {
        "event": {
            "code": "4688",
            "created": "2019-07-16T14:16:10.209241300Z",
            "provider": "Microsoft-Windows-Security-Auditing"
        },
        "message": "{\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"Channel\":\"Security\",\"DeploymentId\":\"0ea500b5-def1-4e62-9020-b5dad9577dad\",\"Description\":\"A new process has been created.\\r\\n\\r\\nCreator Subject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tAZNTPI-02$\\r\\n\\tAccount Domain:\\t\\tACME\\r\\n\\tLogon ID:\\t\\t0x3E7\\r\\n\\r\\nTarget Subject:\\r\\n\\tSecurity ID:\\t\\tS-1-0-0\\r\\n\\tAccount Name:\\t\\t-\\r\\n\\tAccount Domain:\\t\\t-\\r\\n\\tLogon ID:\\t\\t0x0\\r\\n\\r\\nProcess Information:\\r\\n\\tNew Process ID:\\t\\t0x50\\r\\n\\tNew Process Name:\\tC:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\Health Service State\\\\Monitoring Host Temporary Files 52\\\\696\\\\pmfexe.exe\\r\\n\\tToken Elevation Type:\\t%%1936\\r\\n\\tMandatory Label:\\t\\tS-1-16-16384\\r\\n\\tCreator Process ID:\\t0x1568\\r\\n\\tCreator Process Name:\\tC:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\MonitoringHost.exe\\r\\n\\tProcess Command Line:\\t\\\"C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\Health Service State\\\\Monitoring Host Temporary Files 52\\\\696\\\\pmfexe.exe\\\" -PerfMode optimize -quickscan -event -json\\r\\n\\r\\nToken Elevation Type indicates the type of token that was assigned to the new process in accordance with User Account Control policy.\\r\\n\\r\\nType 1 is a full token with no privileges removed or groups disabled.  A full token is only used if User Account Control is disabled or if the user is the built-in Administrator account or a service account.\\r\\n\\r\\nType 2 is an elevated token with no privileges removed or groups disabled.  An elevated token is used when User Account Control is enabled and the user chooses to start the program using Run as administrator.  An elevated token is also used when an application is configured to always require administrative privilege or to always require maximum privilege, and the user is a member of the Administrators group.\\r\\n\\r\\nType 3 is a limited token with administrative privileges removed and administrative groups disabled.  The limited token is used when User Account Control is enabled, the application does not require administrative privilege, and the user does not choose to start the program using Run as administrator.\",\"EventId\":4688,\"Level\":0,\"Opcode\":0,\"Pid\":4,\"ProviderGuid\":\"{54849625-5478-4994-A5BA-3E3B0328C30D}\",\"ProviderName\":\"Microsoft-Windows-Security-Auditing\",\"RawXml\": \"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4688</EventID><Version>2</Version><Level>0</Level><Task>13312</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime='2019-07-16T14:16:10.209241300Z'/><EventRecordID>3892523</EventRecordID><Correlation/><Execution ProcessID='4' ThreadID='8060'/><Channel>Security</Channel><Computer>AZNTPI-02.acme.local</Computer><Security/></System><EventData><Data Name='SubjectUserSid'>S-1-5-18</Data><Data Name='SubjectUserName'>AZNTPI-02$</Data><Data Name='SubjectDomainName'>ACME</Data><Data Name='SubjectLogonId'>0x3e7</Data><Data Name='NewProcessId'>0x50</Data><Data Name='NewProcessName'>C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\Health Service State\\\\Monitoring Host Temporary Files 52\\\\696\\\\pmfexe.exe</Data><Data Name='TokenElevationType'>%%1936</Data><Data Name='ProcessId'>0x1568</Data><Data Name='CommandLine'>\\\"C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\Health Service State\\\\Monitoring Host Temporary Files 52\\\\696\\\\pmfexe.exe\\\" -PerfMode optimize -quickscan -event -json</Data><Data Name='TargetUserSid'>S-1-0-0</Data><Data Name='TargetUserName'>-</Data><Data Name='TargetDomainName'>-</Data><Data Name='TargetLogonId'>0x0</Data><Data Name='ParentProcessName'>C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\MonitoringHost.exe</Data><Data Name='MandatoryLabel'>S-1-16-16384</Data></EventData></Event>\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZNTPI-02\",\"Task\":13312,\"Tid\":8060},\"time\":\"2019-07-16T14:16:10.2092413Z\"}",
        "process": {
            "pid": 80,
            "name": "pmfexe.exe",
            "executable": "c:\\program files\\microsoft monitoring agent\\agent\\health service state\\monitoring host temporary files 52\\696\\pmfexe.exe",
            "command_line": "c:\\program files\\microsoft monitoring agent\\agent\\health service state\\monitoring host temporary files 52\\696\\pmfexe.exe -perfmode optimize -quickscan -event -json",
            "working_directory": "c:\\program files\\microsoft monitoring agent\\agent\\health service state\\monitoring host temporary files 52\\696",
            "parent": {
                "name": "monitoringhost.exe",
                "executable": "c:\\program files\\microsoft monitoring agent\\agent\\monitoringhost.exe",
                "working_directory": "c:\\program files\\microsoft monitoring agent\\agent",
                "pid": 5480
            },
            "thread": {
                "id": 8060
            }
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "user": {
            "name": "AZNTPI-02$",
            "id": "S-1-5-18",
            "domain": "ACME"
        },
        "action": {
            "id": 4688,
            "name": "A new process has been created",
            "record_id": 3892523,
            "type": "Security",
            "outcome": "success",
            "properties": [
                {
                    "ParentImage": "c:\\program files\\microsoft monitoring agent\\agent\\monitoringhost.exe",
                    "opcode": 0
                }
            ]
        },
        "host": {
            "hostname": "AZNTPI-02.acme.local"
        },
        "log": {
            "hostname": "AZNTPI-02.acme.local"
        },
        "azure_windows": {
            "provider_guid": "54849625-5478-4994-A5BA-3E3B0328C30D",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "task": "13312",
            "opcode": "0",
            "event_data": {
                "CommandLine": "\"C:\\Program Files\\Microsoft Monitoring Agent\\Agent\\Health Service State\\Monitoring Host Temporary Files 52\\696\\pmfexe.exe\" -PerfMode optimize -quickscan -event -json",
                "MandatoryLabel": "S-1-16-16384",
                "NewProcessId": "0x50",
                "NewProcessName": "C:\\Program Files\\Microsoft Monitoring Agent\\Agent\\Health Service State\\Monitoring Host Temporary Files 52\\696\\pmfexe.exe",
                "ParentProcessName": "C:\\Program Files\\Microsoft Monitoring Agent\\Agent\\MonitoringHost.exe",
                "ProcessId": "0x1568",
                "SubjectDomainName": "ACME",
                "SubjectLogonId": "0x3e7",
                "SubjectUserName": "AZNTPI-02$",
                "SubjectUserSid": "S-1-5-18",
                "TargetDomainName": "-",
                "TargetLogonId": "0x0",
                "TargetUserName": "-",
                "TargetUserSid": "S-1-0-0",
                "TokenElevationType": "%%1936"
            }
        },
        "related": {
            "user": [
                "AZNTPI-02$"
            ]
        }
    }
    	
	```


=== "process_operation2.json"

    ```json
	
    {
        "event": {
            "code": "4688",
            "created": "2019-07-22T12:54:05.281641000Z",
            "provider": "Microsoft-Windows-Security-Auditing"
        },
        "message": "{\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"Channel\":\"Security\",\"DeploymentId\":\"46c98274-e8d7-4247-a358-11a02975100a\",\"Description\":\"A new process has been created.\\r\\n\\r\\nCreator Subject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tAZSQL-02$\\r\\n\\tAccount Domain:\\t\\tACME\\r\\n\\tLogon ID:\\t\\t0x3E7\\r\\n\\r\\nTarget Subject:\\r\\n\\tSecurity ID:\\t\\tS-1-0-0\\r\\n\\tAccount Name:\\t\\t-\\r\\n\\tAccount Domain:\\t\\t-\\r\\n\\tLogon ID:\\t\\t0x0\\r\\n\\r\\nProcess Information:\\r\\n\\tNew Process ID:\\t\\t0x17b4\\r\\n\\tNew Process Name:\\tC:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\\r\\n\\tToken Elevation Type:\\tTokenElevationTypeDefault (1)\\r\\n\\tCreator Process ID:\\t0x1788\\r\\n\\tProcess Command Line:\\t\\\"C:\\\\Windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\\\" \\\"-ExecutionPolicy\\\" \\\"Unrestricted\\\" \\\"-Noninteractive\\\" \\\"-NoProfile\\\" \\\"-NoLogo\\\" \\\"-File\\\" \\\"C:\\\\Program Files\\\\Microsoft Dependency Agent\\\\plugins\\\\AzureMetadata.ps1\\\"\\r\\n\\r\\nToken Elevation Type indicates the type of token that was assigned to the new process in accordance with User Account Control policy.\\r\\n\\r\\nType 1 is a full token with no privileges removed or groups disabled.  A full token is only used if User Account Control is disabled or if the user is the built-in Administrator account or a service account.\\r\\n\\r\\nType 2 is an elevated token with no privileges removed or groups disabled.  An elevated token is used when User Account Control is enabled and the user chooses to start the program using Run as administrator.  An elevated token is also used when an application is configured to always require administrative privilege or to always require maximum privilege, and the user is a member of the Administrators group.\\r\\n\\r\\nType 3 is a limited token with administrative privileges removed and administrative groups disabled.  The limited token is used when User Account Control is enabled, the application does not require administrative privilege, and the user does not choose to start the program using Run as administrator.\",\"EventId\":4688,\"Level\":0,\"Opcode\":0,\"Pid\":4,\"ProviderGuid\":\"{54849625-5478-4994-A5BA-3E3B0328C30D}\",\"ProviderName\":\"Microsoft-Windows-Security-Auditing\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4688</EventID><Version>2</Version><Level>0</Level><Task>13312</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime='2019-07-22T12:54:05.281641000Z'/><EventRecordID>4948641</EventRecordID><Correlation/><Execution ProcessID='4' ThreadID='9396'/><Channel>Security</Channel><Computer>AZSQL-02.acme.local</Computer><Security/></System><EventData><Data Name='SubjectUserSid'>S-1-5-18</Data><Data Name='SubjectUserName'>AZSQL-02$</Data><Data Name='SubjectDomainName'>ACME</Data><Data Name='SubjectLogonId'>0x3e7</Data><Data Name='NewProcessId'>0x17b4</Data><Data Name='NewProcessName'>C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe</Data><Data Name='TokenElevationType'>%%1936</Data><Data Name='ProcessId'>0x1788</Data><Data Name='CommandLine'>\\\"C:\\\\Windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\\\" \\\"-ExecutionPolicy\\\" \\\"Unrestricted\\\" \\\"-Noninteractive\\\" \\\"-NoProfile\\\" \\\"-NoLogo\\\" \\\"-File\\\" \\\"C:\\\\Program Files\\\\Microsoft Dependency Agent\\\\plugins\\\\AzureMetadata.ps1\\\"</Data><Data Name='TargetUserSid'>S-1-0-0</Data><Data Name='TargetUserName'>-</Data><Data Name='TargetDomainName'>-</Data><Data Name='TargetLogonId'>0x0</Data></EventData></Event>\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZSQL-02\",\"Task\":13312,\"Tid\":9396},\"time\":\"2019-07-22T12:54:05.2816410Z\"}",
        "process": {
            "pid": 6068,
            "name": "powershell.exe",
            "executable": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe",
            "command_line": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe -executionpolicy unrestricted -noninteractive -noprofile -nologo -file c:\\program files\\microsoft dependency agent\\plugins\\azuremetadata.ps1",
            "working_directory": "c:\\windows\\system32\\windowspowershell\\v1.0",
            "parent": {
                "pid": 6024
            },
            "thread": {
                "id": 9396
            }
        },
        "host": {
            "hostname": "AZSQL-02.acme.local"
        },
        "log": {
            "hostname": "AZSQL-02.acme.local"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "action": {
            "id": 4688,
            "name": "A new process has been created",
            "record_id": 4948641,
            "type": "Security",
            "outcome": "success",
            "properties": [
                {
                    "opcode": 0
                }
            ]
        },
        "user": {
            "name": "AZSQL-02$",
            "id": "S-1-5-18",
            "domain": "ACME"
        },
        "azure_windows": {
            "provider_guid": "54849625-5478-4994-A5BA-3E3B0328C30D",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "event_data": {
                "CommandLine": "\"C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe\" \"-ExecutionPolicy\" \"Unrestricted\" \"-Noninteractive\" \"-NoProfile\" \"-NoLogo\" \"-File\" \"C:\\Program Files\\Microsoft Dependency Agent\\plugins\\AzureMetadata.ps1\"",
                "NewProcessId": "0x17b4",
                "NewProcessName": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "ProcessId": "0x1788",
                "SubjectDomainName": "ACME",
                "SubjectLogonId": "0x3e7",
                "SubjectUserName": "AZSQL-02$",
                "SubjectUserSid": "S-1-5-18",
                "TargetDomainName": "-",
                "TargetLogonId": "0x0",
                "TargetUserName": "-",
                "TargetUserSid": "S-1-0-0",
                "TokenElevationType": "%%1936"
            },
            "task": "13312",
            "opcode": "0"
        },
        "related": {
            "user": [
                "AZSQL-02$"
            ]
        }
    }
    	
	```


=== "restart_manager.json"

    ```json
	
    {
        "message": "{\"time\":\"2022-01-12T10:33:34.9717584Z\",\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"DeploymentId\":\"f329f776-83f1-4c79-95e5-6ad3f77f11e5\",\"Role\":\"IaaS\",\"RoleInstance\":\"_lab-vm\",\"ProviderGuid\":\"{0888e5ef-9b98-4695-979d-e92ce4247224}\",\"ProviderName\":\"Microsoft-Windows-RestartManager\",\"EventId\":10001,\"Level\":4,\"Pid\":3732,\"Tid\":2144,\"Opcode\":0,\"Task\":0,\"Channel\":\"Application\",\"Description\":\"Ending session 0 started \u200e2022\u200e-\u200e01\u200e-\u200e12T10:33:34.805069900Z.\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-RestartManager' Guid='{0888e5ef-9b98-4695-979d-e92ce4247224}'/><EventID>10001</EventID><Version>0</Version><Level>4</Level><Task>0</Task><Opcode>0</Opcode><Keywords>0x8000000000000000</Keywords><TimeCreated SystemTime='2022-01-12T10:33:34.9717584Z'/><EventRecordID>9379</EventRecordID><Correlation/><Execution ProcessID='3732' ThreadID='2144'/><Channel>Application</Channel><Computer>lab-vm</Computer><Security UserID='S-1-5-18'/></System><UserData><RmSessionEvent xmlns='http://www.microsoft.com/2005/08/Windows/Reliability/RestartManager/'><RmSessionId>0</RmSessionId><UTCStartTime>2022-01-12T10:33:34.8050699Z</UTCStartTime></RmSessionEvent></UserData></Event>\"}}",
        "action": {
            "id": 10001,
            "name": "no match",
            "outcome": "success",
            "record_id": 9379,
            "type": "Application"
        },
        "azure_windows": {
            "opcode": "0",
            "task": "0",
            "provider_guid": "0888e5ef-9b98-4695-979d-e92ce4247224",
            "provider_name": "Microsoft-Windows-RestartManager"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "process": {
            "pid": 3732,
            "thread": {
                "id": 2144
            }
        },
        "host": {
            "hostname": "lab-vm"
        },
        "log": {
            "hostname": "lab-vm"
        },
        "event": {
            "code": "10001",
            "provider": "Microsoft-Windows-RestartManager"
        }
    }
    	
	```


=== "sysmon.json"

    ```json
	
    {
        "event": {
            "code": "1",
            "created": "2019-08-30T14:53:03.064863900Z",
            "provider": "Microsoft-Windows-Sysmon"
        },
        "message": "{\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"Channel\":\"Microsoft-Windows-Sysmon/Operational\",\"DeploymentId\":\"86d017b9-31b7-47d4-98e0-667a2ac68873\",\"Description\":\"Process Create:\\r\\nRuleName: \\r\\nUtcTime: 2019-08-30 14:53:03.012\\r\\nProcessGuid: {f67648d5-384f-5d69-0000-00101bd8b501}\\r\\nProcessId: 6272\\r\\nImage: C:\\\\Windows\\\\System32\\\\cscript.exe\\r\\nFileVersion: 5.812.10240.16384\\r\\nDescription: Microsoft \\u00ae Console Based Script Host\\r\\nProduct: Microsoft \\u00ae Windows Script Host\\r\\nCompany: Microsoft Corporation\\r\\nOriginalFileName: cscript.exe\\r\\nCommandLine: \\\"C:\\\\windows\\\\system32\\\\cscript.exe\\\" /nologo \\\"MonitorKnowledgeDiscovery.vbs\\\"\\r\\nCurrentDirectory: C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\Health Service State\\\\Monitoring Host Temporary Files 3\\\\507\\\\\\r\\nUser: NT AUTHORITY\\\\SYSTEM\\r\\nLogonGuid: {f67648d5-e752-5d68-0000-0020e7030000}\\r\\nLogonId: 0x3E7\\r\\nTerminalSessionId: 0\\r\\nIntegrityLevel: System\\r\\nHashes: MD5=A45586B3A5A291516CD10EF4FD3EE768,SHA256=59D3CDC7D51FA34C6B27B8B04EA17992955466EB25022B7BD64880AB35DF0BBC\\r\\nParentProcessGuid: {f67648d5-e7c8-5d68-0000-00109ed81e00}\\r\\nParentProcessId: 10068\\r\\nParentImage: C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\MonitoringHost.exe\\r\\nParentCommandLine: \\\"C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\MonitoringHost.exe\\\" -Embedding\",\"EventId\":1,\"Level\":4,\"Opcode\":0,\"Pid\":3272,\"ProviderGuid\":\"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}\",\"ProviderName\":\"Microsoft-Windows-Sysmon\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Sysmon' Guid='{5770385f-c22a-43e0-bf4c-06f5698ffbd9}'/><EventID>1</EventID><Version>5</Version><Level>4</Level><Task>1</Task><Opcode>0</Opcode><Keywords>0x8000000000000000</Keywords><TimeCreated SystemTime='2019-08-30T14:53:03.064863900Z'/><EventRecordID>120166</EventRecordID><Correlation/><Execution ProcessID='3272' ThreadID='5036'/><Channel>Microsoft-Windows-Sysmon/Operational</Channel><Computer>WindowsDesktop</Computer><Security UserID='S-1-5-18'/></System><EventData><Data Name='RuleName'></Data><Data Name='UtcTime'>2019-08-30 14:53:03.012</Data><Data Name='ProcessGuid'>{f67648d5-384f-5d69-0000-00101bd8b501}</Data><Data Name='ProcessId'>6272</Data><Data Name='Image'>C:\\\\Windows\\\\System32\\\\cscript.exe</Data><Data Name='FileVersion'>5.812.10240.16384</Data><Data Name='Description'>Microsoft \\u00ae Console Based Script Host</Data><Data Name='Product'>Microsoft \\u00ae Windows Script Host</Data><Data Name='Company'>Microsoft Corporation</Data><Data Name='OriginalFileName'>cscript.exe</Data><Data Name='CommandLine'>\\\"C:\\\\windows\\\\system32\\\\cscript.exe\\\" /nologo \\\"MonitorKnowledgeDiscovery.vbs\\\"</Data><Data Name='CurrentDirectory'>C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\Health Service State\\\\Monitoring Host Temporary Files 3\\\\507\\\\</Data><Data Name='User'>NT AUTHORITY\\\\SYSTEM</Data><Data Name='LogonGuid'>{f67648d5-e752-5d68-0000-0020e7030000}</Data><Data Name='LogonId'>0x3e7</Data><Data Name='TerminalSessionId'>0</Data><Data Name='IntegrityLevel'>System</Data><Data Name='Hashes'>MD5=A45586B3A5A291516CD10EF4FD3EE768,SHA256=59D3CDC7D51FA34C6B27B8B04EA17992955466EB25022B7BD64880AB35DF0BBC</Data><Data Name='ParentProcessGuid'>{f67648d5-e7c8-5d68-0000-00109ed81e00}</Data><Data Name='ParentProcessId'>10068</Data><Data Name='ParentImage'>C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\MonitoringHost.exe</Data><Data Name='ParentCommandLine'>\\\"C:\\\\Program Files\\\\Microsoft Monitoring Agent\\\\Agent\\\\MonitoringHost.exe\\\" -Embedding</Data></EventData></Event>\",\"Role\":\"IaaS\",\"RoleInstance\":\"_WindowsDesktop\",\"Task\":1,\"Tid\":5036},\"time\":\"2019-08-30T14:53:03.0648639Z\"}",
        "host": {
            "hostname": "WindowsDesktop"
        },
        "log": {
            "hostname": "WindowsDesktop"
        },
        "process": {
            "pid": 3272,
            "name": "cscript.exe",
            "hash": {
                "md5": "a45586b3a5a291516cd10ef4fd3ee768",
                "sha256": "59d3cdc7d51fa34c6b27b8b04ea17992955466eb25022b7bd64880ab35df0bbc"
            },
            "command_line": "c:\\windows\\system32\\cscript.exe /nologo monitorknowledgediscovery.vbs",
            "working_directory": "c:\\windows\\system32",
            "executable": "c:\\windows\\system32\\cscript.exe",
            "parent": {
                "name": "monitoringhost.exe",
                "executable": "c:\\program files\\microsoft monitoring agent\\agent\\monitoringhost.exe",
                "command_line": "c:\\program files\\microsoft monitoring agent\\agent\\monitoringhost.exe -embedding",
                "working_directory": "c:\\program files\\microsoft monitoring agent\\agent",
                "pid": 6272
            },
            "thread": {
                "id": 5036
            }
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "user": {
            "name": "SYSTEM",
            "domain": "NT AUTHORITY"
        },
        "action": {
            "id": 1,
            "name": "Process creation",
            "record_id": 120166,
            "type": "Microsoft-Windows-Sysmon/Operational",
            "outcome": "success",
            "properties": [
                {
                    "ParentImage": "c:\\program files\\microsoft monitoring agent\\agent\\monitoringhost.exe",
                    "opcode": 0
                }
            ]
        },
        "azure_windows": {
            "provider_guid": "5770385f-c22a-43e0-bf4c-06f5698ffbd9",
            "provider_name": "Microsoft-Windows-Sysmon",
            "task": "1",
            "opcode": "0",
            "event_data": {
                "CommandLine": "\"C:\\windows\\system32\\cscript.exe\" /nologo \"MonitorKnowledgeDiscovery.vbs\"",
                "Company": "Microsoft Corporation",
                "CurrentDirectory": "C:\\Program Files\\Microsoft Monitoring Agent\\Agent\\Health Service State\\Monitoring Host Temporary Files 3\\507\\",
                "Description": "Microsoft \u00ae Console Based Script Host",
                "FileVersion": "5.812.10240.16384",
                "Hashes": "MD5=A45586B3A5A291516CD10EF4FD3EE768,SHA256=59D3CDC7D51FA34C6B27B8B04EA17992955466EB25022B7BD64880AB35DF0BBC",
                "Image": "C:\\Windows\\System32\\cscript.exe",
                "IntegrityLevel": "System",
                "LogonGuid": "{f67648d5-e752-5d68-0000-0020e7030000}",
                "LogonId": "0x3e7",
                "OriginalFileName": "cscript.exe",
                "ParentCommandLine": "\"C:\\Program Files\\Microsoft Monitoring Agent\\Agent\\MonitoringHost.exe\" -Embedding",
                "ParentImage": "C:\\Program Files\\Microsoft Monitoring Agent\\Agent\\MonitoringHost.exe",
                "ParentProcessGuid": "{f67648d5-e7c8-5d68-0000-00109ed81e00}",
                "ParentProcessId": "10068",
                "ProcessGuid": "{f67648d5-384f-5d69-0000-00101bd8b501}",
                "ProcessId": "6272",
                "Product": "Microsoft \u00ae Windows Script Host",
                "RuleName": null,
                "TerminalSessionId": "0",
                "User": "NT AUTHORITY\\SYSTEM",
                "UtcTime": "2019-08-30 14:53:03.012"
            }
        },
        "related": {
            "user": [
                "SYSTEM"
            ]
        }
    }
    	
	```


=== "sysmon_11.json"

    ```json
	
    {
        "event": {
            "code": "11",
            "created": "2019-11-27T15:25:45.123493500Z",
            "provider": "Microsoft-Windows-Sysmon"
        },
        "message": "{\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"Channel\":\"Microsoft-Windows-Sysmon/Operational\",\"DeploymentId\":\"cbfba34a-3d3d-4425-aefb-968ee470a8f4\",\"Description\":\"File created:\\r\\nRuleName: \\r\\nUtcTime: 2019-11-27 15:25:45.117\\r\\nProcessGuid: {4A43FA81-9578-5DDE-0000-0010490B8303}\\r\\nProcessId: 4000\\r\\nImage: C:\\\\windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\\r\\nTargetFilename: C:\\\\Windows\\\\Temp\\\\__PSScriptPolicyTest_tnklb3sm.oxn.ps1\\r\\nCreationUtcTime: 2019-11-27 15:25:45.117\",\"EventId\":11,\"Level\":4,\"Opcode\":0,\"Pid\":2232,\"ProviderGuid\":\"{5770385F-C22A-43E0-BF4C-06F5698FFBD9}\",\"ProviderName\":\"Microsoft-Windows-Sysmon\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Sysmon' Guid='{5770385F-C22A-43E0-BF4C-06F5698FFBD9}'/><EventID>11</EventID><Version>2</Version><Level>4</Level><Task>11</Task><Opcode>0</Opcode><Keywords>0x8000000000000000</Keywords><TimeCreated SystemTime='2019-11-27T15:25:45.123493500Z'/><EventRecordID>121811</EventRecordID><Correlation/><Execution ProcessID='2232' ThreadID='3592'/><Channel>Microsoft-Windows-Sysmon/Operational</Channel><Computer>AZNTPI-01.acme.local</Computer><Security UserID='S-1-5-18'/></System><EventData><Data Name='RuleName'></Data><Data Name='UtcTime'>2019-11-27 15:25:45.117</Data><Data Name='ProcessGuid'>{4A43FA81-9578-5DDE-0000-0010490B8303}</Data><Data Name='ProcessId'>4000</Data><Data Name='Image'>C:\\\\windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe</Data><Data Name='TargetFilename'>C:\\\\Windows\\\\Temp\\\\__PSScriptPolicyTest_tnklb3sm.oxn.ps1</Data><Data Name='CreationUtcTime'>2019-11-27 15:25:45.117</Data></EventData></Event>\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZNTPI-01\",\"Task\":11,\"Tid\":3592},\"time\":\"2019-11-27T15:25:45.1234935Z\"}",
        "process": {
            "pid": 2232,
            "name": "powershell.exe",
            "working_directory": "c:\\windows\\system32\\windowspowershell\\v1.0",
            "executable": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe",
            "thread": {
                "id": 3592
            },
            "parent": {
                "pid": 4000
            }
        },
        "action": {
            "id": 11,
            "name": "FileCreate",
            "record_id": 121811,
            "type": "Microsoft-Windows-Sysmon/Operational",
            "outcome": "success",
            "properties": [
                {
                    "opcode": 0
                }
            ]
        },
        "file": {
            "created": "2019-11-27 15:25:45.117",
            "name": "__psscriptpolicytest_tnklb3sm.oxn.ps1",
            "path": "c:\\windows\\temp"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "host": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "log": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "azure_windows": {
            "provider_guid": "5770385F-C22A-43E0-BF4C-06F5698FFBD9",
            "provider_name": "Microsoft-Windows-Sysmon",
            "task": "11",
            "opcode": "0",
            "event_data": {
                "CreationUtcTime": "2019-11-27 15:25:45.117",
                "Image": "C:\\windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "ProcessGuid": "{4A43FA81-9578-5DDE-0000-0010490B8303}",
                "ProcessId": "4000",
                "RuleName": null,
                "TargetFilename": "C:\\Windows\\Temp\\__PSScriptPolicyTest_tnklb3sm.oxn.ps1",
                "UtcTime": "2019-11-27 15:25:45.117"
            }
        }
    }
    	
	```


=== "sysmon_13.json"

    ```json
	
    {
        "event": {
            "code": "13",
            "created": "2020-04-01T06:34:15.214225000Z",
            "provider": "Microsoft-Windows-Sysmon"
        },
        "message": "{\"time\":\"2020-04-01T06:34:15.2142250Z\",\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"DeploymentId\":\"cbfba34a-3d3d-4425-aefb-968ee470a8f4\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZNTPI-01\",\"ProviderGuid\":\"{5770385F-C22A-43E0-BF4C-06F5698FFBD9}\",\"ProviderName\":\"Microsoft-Windows-Sysmon\",\"EventId\":13,\"Level\":4,\"Pid\":2140,\"Tid\":3628,\"Opcode\":0,\"Task\":13,\"Channel\":\"Microsoft-Windows-Sysmon/Operational\",\"Description\":\"Registry value set:\\r\\nRuleName: \\r\\nEventType: SetValue\\r\\nUtcTime: 2020-04-01 06:34:15.158\\r\\nProcessGuid: {4A43FA81-9258-5E74-0000-0010EB030000}\\r\\nProcessId: 4\\r\\nImage: System\\r\\nTargetObject: HKLM\\\\System\\\\CurrentControlSet\\\\Enum\\\\SWD\\\\PRINTENUM\\\\{8D2AEEAE-D27D-4E4D-8F57-A3DA76648B01}\\\\FriendlyName\\r\\nDetails: Microsoft Print to PDF (redirected 5)\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Sysmon' Guid='{5770385F-C22A-43E0-BF4C-06F5698FFBD9}'/><EventID>13</EventID><Version>2</Version><Level>4</Level><Task>13</Task><Opcode>0</Opcode><Keywords>0x8000000000000000</Keywords><TimeCreated SystemTime='2020-04-01T06:34:15.214225000Z'/><EventRecordID>530135</EventRecordID><Correlation/><Execution ProcessID='2140' ThreadID='3628'/><Channel>Microsoft-Windows-Sysmon/Operational</Channel><Computer>AZNTPI-01.acme.local</Computer><Security UserID='S-1-5-18'/></System><EventData><Data Name='RuleName'></Data><Data Name='EventType'>SetValue</Data><Data Name='UtcTime'>2020-04-01 06:34:15.158</Data><Data Name='ProcessGuid'>{4A43FA81-9258-5E74-0000-0010EB030000}</Data><Data Name='ProcessId'>4</Data><Data Name='Image'>System</Data><Data Name='TargetObject'>HKLM\\\\System\\\\CurrentControlSet\\\\Enum\\\\SWD\\\\PRINTENUM\\\\{8D2AEEAE-D27D-4E4D-8F57-A3DA76648B01}\\\\FriendlyName</Data><Data Name='Details'>Microsoft Print to PDF (redirected 5)</Data></EventData></Event>\"}}",
        "process": {
            "pid": 2140,
            "name": "system",
            "executable": "system",
            "thread": {
                "id": 3628
            },
            "parent": {
                "pid": 4
            }
        },
        "host": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "log": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "registry": {
            "data": {
                "strings": [
                    "Microsoft Print to PDF (redirected 5)"
                ],
                "type": "REG_SZ"
            },
            "hive": "HKLM",
            "key": "System\\CurrentControlSet\\Enum\\SWD\\PRINTENUM\\{8D2AEEAE-D27D-4E4D-8F57-A3DA76648B01}",
            "value": "FriendlyName",
            "path": "HKLM\\System\\CurrentControlSet\\Enum\\SWD\\PRINTENUM\\{8D2AEEAE-D27D-4E4D-8F57-A3DA76648B01}\\FriendlyName"
        },
        "action": {
            "id": 13,
            "name": "RegistryEvent (Value Set)",
            "record_id": 530135,
            "type": "Microsoft-Windows-Sysmon/Operational",
            "outcome": "success",
            "properties": [
                {
                    "opcode": 0
                }
            ]
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "azure_windows": {
            "event_data": {
                "Details": "Microsoft Print to PDF (redirected 5)",
                "EventType": "SetValue",
                "Image": "System",
                "ProcessGuid": "{4A43FA81-9258-5E74-0000-0010EB030000}",
                "ProcessId": "4",
                "RuleName": null,
                "TargetObject": "HKLM\\System\\CurrentControlSet\\Enum\\SWD\\PRINTENUM\\{8D2AEEAE-D27D-4E4D-8F57-A3DA76648B01}\\FriendlyName",
                "UtcTime": "2020-04-01 06:34:15.158"
            },
            "provider_guid": "5770385F-C22A-43E0-BF4C-06F5698FFBD9",
            "provider_name": "Microsoft-Windows-Sysmon",
            "task": "13",
            "opcode": "0"
        }
    }
    	
	```


=== "sysmon_22.json"

    ```json
	
    {
        "event": {
            "code": "22",
            "created": "2020-02-26T11:08:11.071181600Z",
            "provider": "Microsoft-Windows-Sysmon"
        },
        "message": "{\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"Channel\":\"Microsoft-Windows-Sysmon/Operational\",\"DeploymentId\":\"23fa1f98-e483-4ae2-a043-88cb9c91c426\",\"Description\":\"Dns query:\\r\\nRuleName: \\r\\nUtcTime: 2020-02-26 11:08:09.059\\r\\nProcessGuid: {f67648d5-4d39-5e56-0000-0010ec220200}\\r\\nProcessId: 3676\\r\\nQueryName: v10.events.data.microsoft.com\\r\\nQueryStatus: 0\\r\\nQueryResults: type:  5 v10.events.data.microsoft.com.aria.akadns.net;type:  5 onecollector.cloudapp.aria.akadns.net;::ffff:52.114.132.20;\\r\\nImage: C:\\\\Windows\\\\System32\\\\svchost.exe\",\"EventId\":22,\"Level\":4,\"Opcode\":0,\"Pid\":3780,\"ProviderGuid\":\"{5770385f-c22a-43e0-bf4c-06f5698ffbd9}\",\"ProviderName\":\"Microsoft-Windows-Sysmon\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Sysmon' Guid='{5770385f-c22a-43e0-bf4c-06f5698ffbd9}'/><EventID>22</EventID><Version>5</Version><Level>4</Level><Task>22</Task><Opcode>0</Opcode><Keywords>0x8000000000000000</Keywords><TimeCreated SystemTime='2020-02-26T11:08:11.071181600Z'/><EventRecordID>136242</EventRecordID><Correlation/><Execution ProcessID='3780' ThreadID='9096'/><Channel>Microsoft-Windows-Sysmon/Operational</Channel><Computer>WinAzureTest</Computer><Security UserID='S-1-5-18'/></System><EventData><Data Name='RuleName'></Data><Data Name='UtcTime'>2020-02-26 11:08:09.059</Data><Data Name='ProcessGuid'>{f67648d5-4d39-5e56-0000-0010ec220200}</Data><Data Name='ProcessId'>3676</Data><Data Name='QueryName'>v10.events.data.microsoft.com</Data><Data Name='QueryStatus'>0</Data><Data Name='QueryResults'>type:  5 v10.events.data.microsoft.com.aria.akadns.net;type:  5 onecollector.cloudapp.aria.akadns.net;::ffff:52.114.132.20;</Data><Data Name='Image'>C:\\\\Windows\\\\System32\\\\svchost.exe</Data></EventData></Event>\",\"Role\":\"IaaS\",\"RoleInstance\":\"_WindowsDesktop\",\"Task\":22,\"Tid\":9096},\"time\":\"2020-02-26T11:08:11.0711816Z\"}",
        "process": {
            "pid": 3780,
            "name": "svchost.exe",
            "working_directory": "c:\\windows\\system32",
            "executable": "c:\\windows\\system32\\svchost.exe",
            "thread": {
                "id": 9096
            },
            "parent": {
                "pid": 3676
            }
        },
        "action": {
            "id": 22,
            "name": "DNS query",
            "record_id": 136242,
            "type": "Microsoft-Windows-Sysmon/Operational",
            "outcome": "success",
            "properties": [
                {
                    "opcode": 0
                }
            ]
        },
        "dns": {
            "answers": [
                {
                    "name": "v10.events.data.microsoft.com.aria.akadns.net",
                    "type": "CNAME"
                },
                {
                    "name": "onecollector.cloudapp.aria.akadns.net",
                    "type": "CNAME"
                },
                {
                    "name": "::ffff:52.114.132.20",
                    "type": "AAAA"
                }
            ],
            "question": {
                "name": "v10.events.data.microsoft.com"
            },
            "size_in_char": 29,
            "response_code": "0",
            "type": "answer"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "host": {
            "hostname": "WinAzureTest"
        },
        "log": {
            "hostname": "WinAzureTest"
        },
        "azure_windows": {
            "provider_guid": "5770385f-c22a-43e0-bf4c-06f5698ffbd9",
            "provider_name": "Microsoft-Windows-Sysmon",
            "task": "22",
            "opcode": "0",
            "event_data": {
                "Image": "C:\\Windows\\System32\\svchost.exe",
                "ProcessGuid": "{f67648d5-4d39-5e56-0000-0010ec220200}",
                "ProcessId": "3676",
                "QueryName": "v10.events.data.microsoft.com",
                "QueryResults": "type:  5 v10.events.data.microsoft.com.aria.akadns.net;type:  5 onecollector.cloudapp.aria.akadns.net;::ffff:52.114.132.20;",
                "QueryStatus": "0",
                "RuleName": null,
                "UtcTime": "2020-02-26 11:08:09.059"
            }
        }
    }
    	
	```


=== "sysmon_3.json"

    ```json
	
    {
        "event": {
            "code": "3",
            "created": "2019-12-18T16:57:17.936358800Z",
            "provider": "Microsoft-Windows-Sysmon"
        },
        "message": "{\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"Channel\":\"Microsoft-Windows-Sysmon/Operational\",\"DeploymentId\":\"cbfba34a-3d3d-4425-aefb-968ee470a8f4\",\"Description\":\"Network connection detected:\\r\\nRuleName: \\r\\nUtcTime: 2019-12-18 16:57:18.516\\r\\nProcessGuid: {4A43FA81-5A68-5DFA-0000-0010A992AC18}\\r\\nProcessId: 4364\\r\\nImage: C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe\\r\\nUser: NT AUTHORITY\\\\SYSTEM\\r\\nProtocol: tcp\\r\\nInitiated: true\\r\\nSourceIsIpv6: false\\r\\nSourceIp: 10.100.8.36\\r\\nSourceHostname: AZNTPI-01.acme.local\\r\\nSourcePort: 55664\\r\\nSourcePortName: \\r\\nDestinationIsIpv6: false\\r\\nDestinationIp: 169.254.169.254\\r\\nDestinationHostname: \\r\\nDestinationPort: 80\\r\\nDestinationPortName: http\",\"EventId\":3,\"Level\":4,\"Opcode\":0,\"Pid\":2116,\"ProviderGuid\":\"{5770385F-C22A-43E0-BF4C-06F5698FFBD9}\",\"ProviderName\":\"Microsoft-Windows-Sysmon\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Sysmon' Guid='{5770385F-C22A-43E0-BF4C-06F5698FFBD9}'/><EventID>3</EventID><Version>5</Version><Level>4</Level><Task>3</Task><Opcode>0</Opcode><Keywords>0x8000000000000000</Keywords><TimeCreated SystemTime='2019-12-18T16:57:17.936358800Z'/><EventRecordID>189923</EventRecordID><Correlation/><Execution ProcessID='2116' ThreadID='3760'/><Channel>Microsoft-Windows-Sysmon/Operational</Channel><Computer>AZNTPI-01.acme.local</Computer><Security UserID='S-1-5-18'/></System><EventData><Data Name='RuleName'></Data><Data Name='UtcTime'>2019-12-18 16:57:18.516</Data><Data Name='ProcessGuid'>{4A43FA81-5A68-5DFA-0000-0010A992AC18}</Data><Data Name='ProcessId'>4364</Data><Data Name='Image'>C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe</Data><Data Name='User'>NT AUTHORITY\\\\SYSTEM</Data><Data Name='Protocol'>tcp</Data><Data Name='Initiated'>true</Data><Data Name='SourceIsIpv6'>false</Data><Data Name='SourceIp'>10.100.8.36</Data><Data Name='SourceHostname'>AZNTPI-01.acme.local</Data><Data Name='SourcePort'>55664</Data><Data Name='SourcePortName'></Data><Data Name='DestinationIsIpv6'>false</Data><Data Name='DestinationIp'>169.254.169.254</Data><Data Name='DestinationHostname'></Data><Data Name='DestinationPort'>80</Data><Data Name='DestinationPortName'>http</Data></EventData></Event>\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZNTPI-01\",\"Task\":3,\"Tid\":3760},\"time\":\"2019-12-18T16:57:17.9363588Z\"}",
        "process": {
            "pid": 2116,
            "name": "powershell.exe",
            "working_directory": "c:\\windows\\system32\\windowspowershell\\v1.0",
            "executable": "c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe",
            "thread": {
                "id": 3760
            },
            "parent": {
                "pid": 4364
            }
        },
        "network": {
            "transport": "tcp",
            "type": "ipv4"
        },
        "source": {
            "address": "AZNTPI-01.acme.local",
            "ip": "10.100.8.36",
            "port": 55664,
            "domain": "AZNTPI-01.acme.local",
            "subdomain": "AZNTPI-01.acme",
            "size_in_char": 20
        },
        "destination": {
            "address": "169.254.169.254",
            "ip": "169.254.169.254",
            "port": 80
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "user": {
            "name": "SYSTEM",
            "domain": "NT AUTHORITY"
        },
        "action": {
            "id": 3,
            "name": "Network connection",
            "record_id": 189923,
            "type": "Microsoft-Windows-Sysmon/Operational",
            "outcome": "success",
            "target": "network-traffic",
            "properties": [
                {
                    "opcode": 0
                }
            ]
        },
        "host": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "log": {
            "hostname": "AZNTPI-01.acme.local"
        },
        "azure_windows": {
            "provider_guid": "5770385F-C22A-43E0-BF4C-06F5698FFBD9",
            "provider_name": "Microsoft-Windows-Sysmon",
            "task": "3",
            "opcode": "0",
            "event_data": {
                "DestinationHostname": null,
                "DestinationIp": "169.254.169.254",
                "DestinationIsIpv6": "false",
                "DestinationPort": "80",
                "DestinationPortName": "http",
                "Image": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "Initiated": "true",
                "ProcessGuid": "{4A43FA81-5A68-5DFA-0000-0010A992AC18}",
                "ProcessId": "4364",
                "Protocol": "tcp",
                "RuleName": null,
                "SourceHostname": "AZNTPI-01.acme.local",
                "SourceIp": "10.100.8.36",
                "SourceIsIpv6": "false",
                "SourcePort": "55664",
                "SourcePortName": null,
                "User": "NT AUTHORITY\\SYSTEM",
                "UtcTime": "2019-12-18 16:57:18.516"
            }
        },
        "related": {
            "user": [
                "SYSTEM"
            ],
            "ip": [
                "10.100.8.36"
            ]
        }
    }
    	
	```


=== "working_dir.json"

    ```json
	
    {
        "user": {
            "id": "S-1-5-18",
            "name": "AZSQL-02$",
            "domain": "AXENS"
        },
        "host": {
            "hostname": "AZSQL-02.axens.local"
        },
        "log": {
            "hostname": "AZSQL-02.axens.local"
        },
        "azure_windows": {
            "provider_guid": "54849625-5478-4994-A5BA-3E3B0328C30D",
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "task": "13312",
            "opcode": "0",
            "event_data": {
                "CommandLine": "C:\\Windows\\system32\\svchost.exe -k wsappx",
                "NewProcessId": "0x12f0",
                "NewProcessName": "C:\\Windows\\System32\\svchost.exe",
                "ProcessId": "0x25c",
                "SubjectDomainName": "AXENS",
                "SubjectLogonId": "0x3e7",
                "SubjectUserName": "AZSQL-02$",
                "SubjectUserSid": "S-1-5-18",
                "TargetDomainName": "-",
                "TargetLogonId": "0x0",
                "TargetUserName": "-",
                "TargetUserSid": "S-1-0-0",
                "TokenElevationType": "%%1936"
            }
        },
        "process": {
            "pid": 4848,
            "name": "svchost.exe",
            "executable": "c:\\windows\\system32\\svchost.exe",
            "working_directory": "c:\\windows\\system32",
            "command_line": "c:\\windows\\system32\\svchost.exe -k wsappx",
            "thread": {
                "id": 8568
            },
            "parent": {
                "pid": 604
            }
        },
        "message": "{\"time\":\"2020-10-22T11:31:18.8344123Z\",\"category\":\"WindowsEventLogsTable\",\"level\":\"Informational\",\"properties\":{\"DeploymentId\":\"46c98274-e8d7-4247-a358-11a02975100a\",\"Role\":\"IaaS\",\"RoleInstance\":\"_AZSQL-02\",\"ProviderGuid\":\"{54849625-5478-4994-A5BA-3E3B0328C30D}\",\"ProviderName\":\"Microsoft-Windows-Security-Auditing\",\"EventId\":4688,\"Level\":0,\"Pid\":4,\"Tid\":8568,\"Opcode\":0,\"Task\":13312,\"Channel\":\"Security\",\"Description\":\"A new process has been created.\\r\\n\\r\\nCreator Subject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tAZSQL-02$\\r\\n\\tAccount Domain:\\t\\tAXENS\\r\\n\\tLogon ID:\\t\\t0x3E7\\r\\n\\r\\nTarget Subject:\\r\\n\\tSecurity ID:\\t\\tS-1-0-0\\r\\n\\tAccount Name:\\t\\t-\\r\\n\\tAccount Domain:\\t\\t-\\r\\n\\tLogon ID:\\t\\t0x0\\r\\n\\r\\nProcess Information:\\r\\n\\tNew Process ID:\\t\\t0x12f0\\r\\n\\tNew Process Name:\\tC:\\\\Windows\\\\System32\\\\svchost.exe\\r\\n\\tToken Elevation Type:\\tTokenElevationTypeDefault (1)\\r\\n\\tCreator Process ID:\\t0x25c\\r\\n\\tProcess Command Line:\\tC:\\\\Windows\\\\system32\\\\svchost.exe -k wsappx\\r\\n\\r\\nToken Elevation Type indicates the type of token that was assigned to the new process in accordance with User Account Control policy.\\r\\n\\r\\nType 1 is a full token with no privileges removed or groups disabled.  A full token is only used if User Account Control is disabled or if the user is the built-in Administrator account or a service account.\\r\\n\\r\\nType 2 is an elevated token with no privileges removed or groups disabled.  An elevated token is used when User Account Control is enabled and the user chooses to start the program using Run as administrator.  An elevated token is also used when an application is configured to always require administrative privilege or to always require maximum privilege, and the user is a member of the Administrators group.\\r\\n\\r\\nType 3 is a limited token with administrative privileges removed and administrative groups disabled.  The limited token is used when User Account Control is enabled, the application does not require administrative privilege, and the user does not choose to start the program using Run as administrator.\",\"RawXml\":\"<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-A5BA-3E3B0328C30D}'/><EventID>4688</EventID><Version>2</Version><Level>0</Level><Task>13312</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime='2020-10-22T11:31:18.834412300Z'/><EventRecordID>13259890</EventRecordID><Correlation/><Execution ProcessID='4' ThreadID='8568'/><Channel>Security</Channel><Computer>AZSQL-02.axens.local</Computer><Security/></System><EventData><Data Name='SubjectUserSid'>S-1-5-18</Data><Data Name='SubjectUserName'>AZSQL-02$</Data><Data Name='SubjectDomainName'>AXENS</Data><Data Name='SubjectLogonId'>0x3e7</Data><Data Name='NewProcessId'>0x12f0</Data><Data Name='NewProcessName'>C:\\\\Windows\\\\System32\\\\svchost.exe</Data><Data Name='TokenElevationType'>%%1936</Data><Data Name='ProcessId'>0x25c</Data><Data Name='CommandLine'>C:\\\\Windows\\\\system32\\\\svchost.exe -k wsappx</Data><Data Name='TargetUserSid'>S-1-0-0</Data><Data Name='TargetUserName'>-</Data><Data Name='TargetDomainName'>-</Data><Data Name='TargetLogonId'>0x0</Data></EventData></Event>\"}}",
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "action": {
            "id": 4688,
            "outcome": "success",
            "name": "A new process has been created",
            "type": "Security",
            "record_id": 13259890,
            "properties": [
                {
                    "opcode": 0
                }
            ]
        },
        "related": {
            "user": [
                "AZSQL-02$"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`action.properties` | `text` | None |
|`action.target` | `keyword` | None |
|`azure_windows.event_data` | `object` | None |
|`azure_windows.opcode` | `keyword` | None |
|`azure_windows.provider_guid` | `keyword` | None |
|`azure_windows.provider_name` | `keyword` | None |
|`azure_windows.task` | `keyword` | None |
|`azure_windows.user.domain.name` | `keyword` | None |
|`azure_windows.user.identifier` | `keyword` | None |
|`azure_windows.user.name` | `keyword` | None |
|`azure_windows.user.type` | `keyword` | None |
|`destination.domain` | `keyword` | The domain name of the destination. |
|`destination.ip` | `ip` | IP address of the destination. |
|`destination.port` | `long` | Port of the destination. |
|`destination.size_in_char` | `number` | None |
|`dns.answers` | `object` | Array of DNS answers. |
|`dns.question.name` | `keyword` | The name being queried. |
|`dns.response_code` | `keyword` | The DNS response code. |
|`dns.size_in_char` | `number` | None |
|`dns.type` | `keyword` | The type of DNS event captured, query or answer. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.provider` | `keyword` | Source of the event. |
|`file.created` | `date` | File creation time. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`file.path` | `keyword` | Full path to the file, including the file name. |
|`host.hostname` | `keyword` | Hostname of the host. |
|`network.transport` | `keyword` | Protocol Name corresponding to the field `iana_number`. |
|`network.type` | `keyword` | In the OSI Model this would be the Network Layer. ipv4, ipv6, ipsec, pim, etc |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.hash.md5` | `keyword` | MD5 hash. |
|`process.hash.sha1` | `keyword` | SHA1 hash. |
|`process.hash.sha256` | `keyword` | SHA256 hash. |
|`process.hash.sha384` | `keyword` |  |
|`process.hash.sha512` | `keyword` | SHA512 hash. |
|`process.name` | `keyword` | Process name. |
|`process.parent.command_line` | `wildcard` | Full command line that started the process. |
|`process.parent.executable` | `keyword` | Absolute path to the process executable. |
|`process.parent.name` | `keyword` | Process name. |
|`process.parent.pid` | `long` | Process id. |
|`process.parent.working_directory` | `keyword` | The working directory of the process. |
|`process.pid` | `long` | Process id. |
|`process.thread.id` | `long` | Thread ID. |
|`process.working_directory` | `keyword` | The working directory of the process. |
|`registry.data.strings` | `wildcard` | List of strings representing what was written to the registry. |
|`registry.data.type` | `keyword` | Standard registry type for encoding contents |
|`registry.hive` | `keyword` | Abbreviated name for the hive. |
|`registry.key` | `keyword` | Hive-relative path of keys. |
|`registry.path` | `keyword` | Full path, including hive, key and value |
|`registry.value` | `keyword` | Name of the value written. |
|`source.domain` | `keyword` | The domain name of the source. |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`source.size_in_char` | `number` | None |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |

