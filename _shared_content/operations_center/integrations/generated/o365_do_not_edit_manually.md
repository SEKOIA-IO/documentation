
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Office 365 account logs` | Authentication events |
| `Office 365 audit logs` | Some user actions are parsed (e.g. file access) |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `file`, `iam`, `network` |
| Type | `change`, `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "ad.json"

    ```json
	
    {
        "message": "{\"CreationTime\": \"2020-09-29T08:59:26\", \"Id\": \"e1717ca5-c13e-4382-ad7e-4864faa11e85\", \"Operation\": \"UserLoggedIn\", \"OrganizationId\": \"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\", \"RecordType\": 15, \"ResultStatus\": \"Succeeded\", \"UserKey\": \"10030000A9F382C6@sekoiacorp.onmicrosoft.com\", \"UserType\": 0, \"Version\": 1, \"Workload\": \"AzureActiveDirectory\", \"ClientIP\": \"1.2.3.4\", \"ObjectId\": \"cc15fd57-2c6c-4117-a88c-83b1d56b4bbe\", \"UserId\": \"user@company.onmicrosoft.com\", \"AzureActiveDirectoryEventType\": 1, \"ExtendedProperties\": [{\"Name\": \"UserAgent\", \"Value\": \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36\"}, {\"Name\": \"UserAuthenticationMethod\", \"Value\": \"1\"}, {\"Name\": \"RequestType\", \"Value\": \"OAuth2:Authorize\"}, {\"Name\": \"ResultStatusDetail\", \"Value\": \"Redirect\"}, {\"Name\": \"KeepMeSignedIn\", \"Value\": \"True\"}], \"ModifiedProperties\": [], \"Actor\": [{\"ID\": \"cb42ef6c-989f-49d0-86cd-7706b8d14528\", \"Type\": 0}, {\"ID\": \"user@company.onmicrosoft.com\", \"Type\": 5}, {\"ID\": \"10030000A9F382C6\", \"Type\": 3}], \"ActorContextId\": \"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\", \"ActorIpAddress\": \"1.2.3.4\", \"InterSystemsId\": \"d23dd5d2-ccc8-4928-b7a0-f446a2ca4a90\", \"IntraSystemId\": \"a196489a-9a7c-4824-b35a-5bfdec600c00\", \"SupportTicketId\": \"\", \"Target\": [{\"ID\": \"cc15fd57-2c6c-4117-a88c-83b1d56b4bbe\", \"Type\": 0}], \"TargetContextId\": \"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\", \"ApplicationId\": \"5e3ce6c0-2b1f-4285-8d4b-75ee78787346\"}",
        "event": {
            "action": "UserLoggedIn",
            "kind": "event",
            "code": "15",
            "category": [
                "authentication"
            ],
            "type": [
                "start"
            ]
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "user": {
            "name": "user@company.onmicrosoft.com",
            "email": "user@company.onmicrosoft.com"
        },
        "organization": {
            "id": "aa09a079-7796-46a8-a4d4-4d21b0dcf1b2"
        },
        "action": {
            "id": 15,
            "name": "UserLoggedIn",
            "target": "network-traffic",
            "outcome": "success"
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "office365": {
            "record_type": 15,
            "result_status": "Succeeded",
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "auth": {
                "user_authentication_method": 1,
                "request_type": "OAuth2:Authorize",
                "result_status_detail": "Redirect",
                "keep_me_signed_in": true
            },
            "audit": {
                "object_id": "cc15fd57-2c6c-4117-a88c-83b1d56b4bbe"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "user@company.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "exchange_event1.json"

    ```json
	
    {
        "service": {
            "name": "Exchange"
        },
        "organization": {
            "id": "7f7e5b97-b780-473c-9c76-9182a9d7f2b4"
        },
        "office365": {
            "record_type": 2,
            "result_status": "Succeeded",
            "user_type": {
                "code": 0,
                "name": "Regular"
            }
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        },
        "source": {
            "address": "d498:796:298e:be16:1b11:29eb:9996:8a36",
            "ip": "d498:796:298e:be16:1b11:29eb:9996:8a36"
        },
        "event": {
            "action": "Create",
            "kind": "event",
            "category": [
                "email",
                "file"
            ],
            "type": [
                "info",
                "creation"
            ],
            "code": "2"
        },
        "action": {
            "id": 2,
            "outcome": "success",
            "target": "user",
            "name": "Create"
        },
        "user": {
            "email": "email@example.org",
            "name": "email@example.org"
        },
        "related": {
            "ip": [
                "d498:796:298e:be16:1b11:29eb:9996:8a36"
            ],
            "user": [
                "email@example.org"
            ]
        }
    }
    	
	```


=== "file_previewed.json"

    ```json
	
    {
        "message": "{\"CreationTime\": \"2020-09-29T07:32:51\", \"Id\": \"4e597c8c-e185-4ea5-3413-08d86449df74\", \"Operation\": \"FilePreviewed\", \"OrganizationId\": \"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\", \"RecordType\": 6, \"UserKey\": \"i:0h.f|membership|10032000e70d7559@live.com\", \"UserType\": 0, \"Version\": 1, \"Workload\": \"OneDrive\", \"ClientIP\": \"1.2.3.4\", \"ObjectId\": \"https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/Documents/MyDocument.docx\", \"UserId\": \"jane.doe@company.onmicrosoft.com\", \"ApplicationId\": \"4345a7b9-9a63-4910-a426-35363201d503\", \"CorrelationId\": \"41af7e9f-30a8-9000-8f78-756aca9a7474\", \"DoNotDistributeEvent\": \"True\", \"EventSource\": \"SharePoint\", \"ItemType\": \"File\", \"ListId\": \"2db6ee74-6bd7-4d9b-a63f-26ae6eef9fb3\", \"ListItemUniqueId\": \"0e3f3538-8a03-4728-b431-225bc10687b6\", \"Site\": \"2d3c44c1-d225-499d-a47f-bda2751a00b9\", \"UserAgent\": \"OneDriveMpc-Transform_Thumbnail/1.0\", \"WebId\": \"c4b81f7e-4f91-4b3a-97a7-660709edef15\", \"HighPriorityMediaProcessing\": \"False\", \"SourceFileExtension\": \"xlsx\", \"SiteUrl\": \"https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/\", \"SourceFileName\": \"MyDocument.docx\", \"SourceRelativeUrl\": \"Documents\"}",
        "event": {
            "action": "FilePreviewed",
            "kind": "event",
            "code": "6",
            "category": [
                "file"
            ],
            "type": [
                "info"
            ]
        },
        "service": {
            "name": "OneDrive"
        },
        "user": {
            "name": "jane.doe@company.onmicrosoft.com",
            "email": "jane.doe@company.onmicrosoft.com"
        },
        "organization": {
            "id": "aa09a079-7796-46a8-a4d4-4d21b0dcf1b2"
        },
        "action": {
            "id": 6,
            "name": "FilePreviewed",
            "target": "user",
            "outcome": "success",
            "properties": [
                {
                    "SourceFileName": "MyDocument.docx",
                    "SourceRelativeUrl": "Documents",
                    "SiteUrl": "https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/",
                    "UserAgent": "OneDriveMpc-Transform_Thumbnail/1.0"
                }
            ]
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "office365": {
            "record_type": 6,
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "audit": {
                "object_id": "https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/Documents/MyDocument.docx"
            }
        },
        "file": {
            "name": "MyDocument.docx",
            "directory": "Documents"
        },
        "user_agent": {
            "original": "OneDriveMpc-Transform_Thumbnail/1.0"
        },
        "url": {
            "full": "https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/Documents/MyDocument.docx",
            "original": "https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/Documents/MyDocument.docx",
            "domain": "company-my.sharepoint.com",
            "top_level_domain": "com",
            "subdomain": "company-my",
            "registered_domain": "sharepoint.com",
            "scheme": "https",
            "path": "/personal/jane_doe_company_onmicrosoft_com/Documents/MyDocument.docx",
            "port": 443
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "jane.doe@company.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "file_sync_download_full.json"

    ```json
	
    {
        "message": "{\"AppAccessContext\":{\"AADSessionId\":\"0e042318-7c78-4acb-ae00-5ee74465bca3\",\"CorrelationId\":\"c299a0a0-14da-428a-b08d-481d562298cb\",\"UniqueTokenId\":\"0000000000000000000000\"},\"CreationTime\":\"2022-06-10T12:00:14\",\"Id\":\"7c13b5d5-aa8d-48d1-b3d1-5f4b657136ba\",\"Operation\":\"FileSyncDownloadedFull\",\"OrganizationId\":\"2d7585dc-97bc-4494-b98c-79f2a4946931\",\"RecordType\":6,\"UserKey\":\"i:0h.f|membership|0000000000000000@live.com\",\"UserType\":0,\"Version\":1,\"Workload\":\"SharePoint\",\"ClientIP\":\"1.2.3.4\",\"ObjectId\":\"https://company.sharepoint.com/sites/shared/public/assets/website/logo.png\",\"UserId\":\"marketing@company.com\",\"CorrelationId\":\"4b25e3d9-1e4f-4c62-a544-da747449f144\",\"EventSource\":\"SharePoint\",\"ItemType\":\"File\",\"ListId\":\"ca07dda5-0cdc-4399-94a6-303a7aa8ac00\",\"ListItemUniqueId\":\"ab5a159c-c8fd-409c-a48f-524c29df0341\",\"Site\":\"1a53ae0f-8405-42ec-8c43-724101fd34a2\",\"UserAgent\":\"Microsoft SkyDriveSync 22.099.0508.0001 ship; Windows NT 10.0 (19043)\",\"WebId\":\"ba71b4fe-22e8-41cf-9eaf-48b1787bad16\",\"MachineDomainInfo\":\"f059d209-e819-402b-a391-4941ff3860c6\",\"MachineId\":\"884ecccb-1e44-4dd4-a2b5-b60517893ce0\",\"FileSyncBytesCommitted\":\"1344200\",\"HighPriorityMediaProcessing\":false,\"SourceFileExtension\":\"png\",\"SiteUrl\":\"https://company.sharepoint.com/sites/shared\",\"SourceFileName\":\"logo.png\",\"SourceRelativeUrl\":\"public/assets/website\"}",
        "event": {
            "action": "FileSyncDownloadedFull",
            "kind": "event",
            "code": "6",
            "category": [
                "file"
            ],
            "type": [
                "info"
            ]
        },
        "service": {
            "name": "SharePoint"
        },
        "user": {
            "name": "marketing@company.com",
            "email": "marketing@company.com"
        },
        "organization": {
            "id": "2d7585dc-97bc-4494-b98c-79f2a4946931"
        },
        "action": {
            "id": 6,
            "name": "FileSyncDownloadedFull",
            "target": "user",
            "outcome": "success",
            "properties": [
                {
                    "SourceFileName": "logo.png",
                    "SourceRelativeUrl": "public/assets/website",
                    "SiteUrl": "https://company.sharepoint.com/sites/shared",
                    "UserAgent": "Microsoft SkyDriveSync 22.099.0508.0001 ship; Windows NT 10.0 (19043)"
                }
            ]
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "office365": {
            "record_type": 6,
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "audit": {
                "object_id": "https://company.sharepoint.com/sites/shared/public/assets/website/logo.png"
            },
            "context": {
                "aad_session_id": "0e042318-7c78-4acb-ae00-5ee74465bca3",
                "correlation": {
                    "id": "c299a0a0-14da-428a-b08d-481d562298cb"
                }
            }
        },
        "file": {
            "name": "logo.png",
            "directory": "public/assets/website"
        },
        "user_agent": {
            "original": "Microsoft SkyDriveSync 22.099.0508.0001 ship; Windows NT 10.0 (19043)"
        },
        "url": {
            "full": "https://company.sharepoint.com/sites/shared/public/assets/website/logo.png",
            "original": "https://company.sharepoint.com/sites/shared/public/assets/website/logo.png",
            "domain": "company.sharepoint.com",
            "top_level_domain": "com",
            "subdomain": "company",
            "registered_domain": "sharepoint.com",
            "scheme": "https",
            "path": "/sites/shared/public/assets/website/logo.png",
            "port": 443
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "marketing@company.com"
            ]
        }
    }
    	
	```


=== "microsoft_defender_threatintelligence_atp.json"

    ```json
	
    {
        "message": "{\"CreationTime\":\"2022-07-07T22:38:49\",\"Id\":\"266f5962-ffad-4fce-a101-3197581af3d4\",\"Operation\":\"AtpDetection\",\"OrganizationId\":\"7f7e5b97-b780-473c-9c76-9182a9d7f2b4\",\"RecordType\":47,\"UserKey\":\"ThreatIntel\",\"UserType\":4,\"Version\":1,\"Workload\":\"ThreatIntelligence\",\"UserId\":\"people@example.org\",\"DetectionDate\":\"2022-07-07T22:38:11\",\"DetectionMethod\":\"AntiMalware\",\"EventDeepLink\":\"https://protection.office.com/threatexplorer?dltarget=Explorer&dlstorage=Url&viewid=MalwareContent&query-Id=2ab4791e-fdd4-42f9-ad3c-c54ef7a4d548\",\"FileData\":{\"DocumentId\":\"03254108-f682-417d-f3e6-08da605bf091\",\"FileName\":\"malware\",\"FilePath\":\"https://example.sharepoint.com/personal/people_example_org/Documents/malware\",\"FileSize\":\"12345\",\"FileVerdict\":1,\"MalwareFamily\":\"iPhoneOS/Vortex.C\",\"SHA256\":\"SnltYq0lbVwFlAIf+lQugPXaMcDNV9t9pN/Zkhx7hQ8=\"},\"LastModifiedBy\":\"people@example.org\",\"LastModifiedDate\":\"2022-01-01T13:00:53\",\"SourceWorkload\":1}\n",
        "action": {
            "id": 47,
            "name": "AtpDetection",
            "outcome": "success",
            "target": "user"
        },
        "event": {
            "action": "AtpDetection",
            "code": "47",
            "kind": "event",
            "outcome": "success",
            "id": "00000000-0000-0000-0000-000000000000'",
            "url": "https://protection.office.com/threatexplorer?dltarget=Explorer&dlstorage=Url&viewid=MalwareContent&query-Id=2ab4791e-fdd4-42f9-ad3c-c54ef7a4d548"
        },
        "office365": {
            "defender": {
                "detection": {
                    "method": "AntiMalware"
                }
            },
            "record_type": 47,
            "user_type": {
                "code": 4,
                "name": "System"
            }
        },
        "organization": {
            "id": "7f7e5b97-b780-473c-9c76-9182a9d7f2b4"
        },
        "related": {
            "user": [
                "people@example.org"
            ]
        },
        "service": {
            "name": "ThreatIntelligence"
        },
        "user": {
            "email": "people@example.org",
            "name": "people@example.org"
        }
    }
    	
	```


=== "microsoft_defender_threatintelligence_mail.json"

    ```json
	
    {
        "message": "{\"CreationTime\":\"2022-07-08T09:10:19\",\"Id\":\"50906475-74dd-4447-ae4d-595d225d0055\",\"Operation\":\"TIMailData\",\"OrganizationId\":\"8a457951-a594-4607-a5dc-dfc72338eb13\",\"RecordType\":28,\"UserKey\":\"ThreatIntel\",\"UserType\":4,\"Version\":1,\"Workload\":\"ThreatIntelligence\",\"ObjectId\":\"4ca2df96-4488-4f3b-a265-b4edaa3c4d8f\",\"UserId\":\"ThreatIntel\",\"AdditionalActionsAndResults\":[\"OriginalDelivery: [N/A]\"],\"AttachmentData\":[{\"FileName\":\"malicious.pdf.exe\",\"FileType\":\"exe;zip\",\"FileVerdict\":1,\"MalwareFamily\":\"Trojan_Gen_FileWithSpoofedExtension_A\",\"SHA256\":\"E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855\"}],\"AuthDetails\":[{\"Name\":\"SPF\",\"Value\":\"Pass\"},{\"Name\":\"DKIM\",\"Value\":\"Fail\"},{\"Name\":\"DMARC\",\"Value\":\"Best guess pass\"},{\"Name\":\"Comp Auth\",\"Value\":\"pass\"}],\"DeliveryAction\":\"Blocked\",\"DetectionMethod\":\"File detonation\",\"DetectionType\":\"Inline\",\"Directionality\":\"Inbound\",\"EventDeepLink\":\"https://protection.office.com/?hash=/threatexplorer?messageParams=a4dbf74a-89e0-40de-b14d-df573f48aa45,a4dbf74a-89e0-40de-b14d-df573f48aa45-0000000000000000000-1,2022-07-08T00:00:00,2022-07-08T23:59:59&view=Malware\",\"InternetMessageId\":\"<4cc4a74e-a195-4222-abd7-a8adf2cd347d@sender.com>\",\"LatestDeliveryLocation\":\"Quarantine\",\"MessageTime\":\"2022-07-08T09:07:47\",\"NetworkMessageId\":\"7250ff78-fd13-45a2-bb5d-23a5d59c2699\",\"OriginalDeliveryLocation\":\"Quarantine\",\"P1Sender\":\"prvs=0000000000=human@sender.com\",\"P2Sender\":\"human@sender.com\",\"Policy\":\"SafeAttachements\",\"PolicyAction\":\"Quarantine\",\"Recipients\":[\"human@example.com\"],\"SenderIp\":\"1.2.3.4\",\"Subject\":\"Refund to you\",\"SystemOverrides\":[{\"Details\":\"Antimalware policy block by file type\",\"FinalOverride\":\"No\",\"Result\":\"Block\",\"Source\":\"Tenant\"}],\"ThreatsAndDetectionTech\":[\"Malware: [File detonation]\",\"Spam: [General filter]\"],\"Verdict\":\"Malware\"}\n",
        "event": {
            "action": "Blocked",
            "kind": "event",
            "code": "28",
            "url": "https://protection.office.com/?hash=/threatexplorer?messageParams=a4dbf74a-89e0-40de-b14d-df573f48aa45,a4dbf74a-89e0-40de-b14d-df573f48aa45-0000000000000000000-1,2022-07-08T00:00:00,2022-07-08T23:59:59&view=Malware"
        },
        "service": {
            "name": "ThreatIntelligence"
        },
        "user": {
            "name": "ThreatIntel"
        },
        "organization": {
            "id": "8a457951-a594-4607-a5dc-dfc72338eb13"
        },
        "action": {
            "id": 28,
            "name": "Blocked",
            "target": "user",
            "outcome": "success"
        },
        "office365": {
            "record_type": 28,
            "user_type": {
                "code": 4,
                "name": "System"
            },
            "audit": {
                "object_id": "4ca2df96-4488-4f3b-a265-b4edaa3c4d8f"
            },
            "defender": {
                "email": {
                    "verdict": {
                        "reason": "Malware"
                    },
                    "delivery": {
                        "action": "Blocked",
                        "original_location": "Quarantine",
                        "latest_location": "Quarantine"
                    },
                    "attachments": [
                        {
                            "name": "Trojan_Gen_FileWithSpoofedExtension_A",
                            "verdict": {
                                "code": "1",
                                "name": "bad"
                            }
                        }
                    ]
                },
                "detection": {
                    "type": "Inline",
                    "method": "File detonation",
                    "technology": [
                        "Malware: [File detonation]",
                        "Spam: [General filter]"
                    ]
                },
                "additional_actions": [
                    "OriginalDelivery: [N/A]"
                ],
                "auth_details": [
                    {
                        "Name": "SPF",
                        "Value": "Pass"
                    },
                    {
                        "Name": "DKIM",
                        "Value": "Fail"
                    },
                    {
                        "Name": "DMARC",
                        "Value": "Best guess pass"
                    },
                    {
                        "Name": "Comp Auth",
                        "Value": "pass"
                    }
                ],
                "system_overrides": [
                    {
                        "Details": "Antimalware policy block by file type",
                        "FinalOverride": "No",
                        "Result": "Block",
                        "Source": "Tenant"
                    }
                ]
            }
        },
        "email": {
            "local_id": "7250ff78-fd13-45a2-bb5d-23a5d59c2699",
            "subject": "Refund to you",
            "delivery_timestamp": "2022-07-08T09:07:47",
            "message_id": "4cc4a74e-a195-4222-abd7-a8adf2cd347d@sender.com",
            "reply_to": {
                "address": [
                    "prvs=0000000000=human@sender.com"
                ]
            },
            "from": {
                "address": [
                    "human@sender.com"
                ]
            },
            "to": {
                "address": [
                    "human@example.com"
                ]
            },
            "attachments": [
                {
                    "file": {
                        "name": "malicious.pdf.exe",
                        "mime_type": "exe;zip",
                        "hash": {
                            "sha256": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"
                        }
                    }
                }
            ]
        },
        "source": {
            "ip": "1.2.3.4",
            "address": "1.2.3.4"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ThreatIntel"
            ]
        }
    }
    	
	```


=== "microsoft_defender_threatintelligence_url_click.json"

    ```json
	
    {
        "message": "{\"CreationTime\":\"2022-07-07T10:10:52\",\"Id\":\"47bf7844-15bf-4cf2-91a3-15b32ceb89b5\",\"Operation\":\"TIUrlClickData\",\"OrganizationId\":\"0eaa2260-b241-410b-bcae-e38c8b68787f\",\"RecordType\":41,\"UserKey\":\"ThreatIntel\",\"UserType\":4,\"Version\":1,\"Workload\":\"ThreatIntelligence\",\"UserId\":\"human@example.org\",\"AppName\":\"Mail\",\"AppVersion\":\"0.0.0000\",\"EventDeepLink\":\"https://protection.office.com/threatexplorer?dltarget=Explorer&dlstorage=Url&viewid=Phish&query-Recipients=people@xample.org&query-NetworkMessageId=53b5da37-1893-4e78-a89f-a4d26b53184c\",\"SourceId\":\"8a8634d0-d803-4bc9-b221-2863bff6a001\",\"TimeOfClick\":\"2022-07-07T09:33:33\",\"Url\":\"https://malicious.domain.com\",\"UserIp\":\"1.2.3.4\"}\n",
        "action": {
            "id": 41,
            "name": "TIUrlClickData",
            "outcome": "success",
            "target": "user"
        },
        "event": {
            "action": "TIUrlClickData",
            "code": "41",
            "kind": "event",
            "outcome": "success",
            "id": "00000000-0000-0000-0000-000000000000'",
            "url": "https://protection.office.com/threatexplorer?dltarget=Explorer&dlstorage=Url&viewid=Phish&query-Recipients=people@xample.org&query-NetworkMessageId=53b5da37-1893-4e78-a89f-a4d26b53184c"
        },
        "office365": {
            "record_type": 41,
            "user_type": {
                "code": 4,
                "name": "System"
            }
        },
        "organization": {
            "id": "0eaa2260-b241-410b-bcae-e38c8b68787f"
        },
        "related": {
            "user": [
                "human@example.org"
            ]
        },
        "service": {
            "name": "ThreatIntelligence"
        },
        "user": {
            "email": "human@example.org",
            "name": "human@example.org"
        }
    }
    	
	```


=== "teams_message_has_link.json"

    ```json
	
    {
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "organization": {
            "id": "34314e6e-4023-4e4b-a15e-143f63244e2b"
        },
        "office365": {
            "record_type": 25,
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "teams": {
                "communication": {
                    "type": "OneOnOne"
                },
                "message": {
                    "id": "1649188295480",
                    "version": "1649188295480",
                    "urls": [
                        "https://www.amazon.fr/s?i=merchant-items&amp;me=A1TLEYKQIC7812&amp;marketplaceID=A13V1IB3VIYZZH&amp;qid=1649187214&amp;ref=sr_pg_1"
                    ]
                },
                "team": {
                    "members": [
                        {
                            "id": "admin@example.org",
                            "role": "Owner"
                        },
                        {
                            "id": "user1@example.org",
                            "role": "Member"
                        }
                    ]
                }
            }
        },
        "user": {
            "email": "email@example.org",
            "name": "email@example.org"
        },
        "service": {
            "name": "MicrosoftTeams"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
        },
        "event": {
            "action": "MessageCreatedHasLink",
            "kind": "event",
            "category": [
                "network"
            ],
            "type": [
                "info"
            ],
            "code": "25"
        },
        "action": {
            "target": "network-traffic",
            "id": 25,
            "outcome": "success",
            "name": "MessageCreatedHasLink"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "email@example.org"
            ]
        }
    }
    	
	```


=== "update_group.json"

    ```json
	
    {
        "message": "{\"CreationTime\": \"2019-11-18T13:40:24\", \"Id\": \"038ae875-ffd8-45e4-9dcf-6e385cfad349\", \"Operation\": \"Update group.\", \"OrganizationId\": \"3e49b082-62d5-4849-a5b0-86ed519287d2\", \"RecordType\": 8, \"ResultStatus\": \"Success\", \"UserKey\": \"10030000A96EA230@acme.onmicrosoft.com\", \"UserType\": 0, \"Version\": 1, \"Workload\": \"AzureActiveDirectory\", \"ClientIP\": \"<null>\", \"ObjectId\": \"Not Available\", \"UserId\": \"Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com\", \"AzureActiveDirectoryEventType\": 1, \"ExtendedProperties\": [{\"Name\": \"resultType\", \"Value\": \"Success\"}]}",
        "event": {
            "action": "Update group.",
            "kind": "event",
            "code": "8",
            "category": [
                "iam"
            ],
            "type": [
                "change"
            ]
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "user": {
            "name": "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com",
            "email": "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com"
        },
        "organization": {
            "id": "3e49b082-62d5-4849-a5b0-86ed519287d2"
        },
        "action": {
            "id": 8,
            "name": "Update group.",
            "target": "user",
            "outcome": "success"
        },
        "office365": {
            "record_type": 8,
            "result_status": "Success",
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "audit": {
                "object_id": "Not Available"
            }
        },
        "related": {
            "user": [
                "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "update_user.json"

    ```json
	
    {
        "message": "{\"CreationTime\": \"2019-12-09T14:18:19\", \"Id\": \"359154c4-72c5-4ba0-bbf9-7eb1dff88af7\", \"Operation\": \"Update user.\", \"OrganizationId\": \"3e49b082-62d5-4849-a5b0-86ed519287d2\", \"RecordType\": 8, \"ResultStatus\": \"Success\", \"UserKey\": \"10030000A96EA230@acme.onmicrosoft.com\", \"UserType\": 0, \"Version\": 1, \"Workload\": \"AzureActiveDirectory\", \"ClientIP\": \"<null>\", \"ObjectId\": \"bob.smith@acme.org\", \"UserId\": \"Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com\", \"AzureActiveDirectoryEventType\": 1, \"ExtendedProperties\": [{\"Name\": \"resultType\", \"Value\": \"Success\"}, {\"Name\": \"auditEventCategory\", \"Value\": \"UserManagement\"}, {\"Name\": \"nCloud\", \"Value\": \"<null>\"}]}",
        "event": {
            "action": "Update user.",
            "kind": "event",
            "code": "8",
            "category": [
                "iam"
            ],
            "type": [
                "change"
            ]
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "user": {
            "name": "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com",
            "email": "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com"
        },
        "organization": {
            "id": "3e49b082-62d5-4849-a5b0-86ed519287d2"
        },
        "action": {
            "id": 8,
            "name": "Update user.",
            "target": "user",
            "outcome": "success"
        },
        "office365": {
            "record_type": 8,
            "result_status": "Success",
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "audit": {
                "object_id": "bob.smith@acme.org"
            }
        },
        "related": {
            "user": [
                "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "update_user_empty_source_ip.json"

    ```json
	
    {
        "message": "{\"CreationTime\":\"2021-03-05T14:43:17\",\"Id\":\"21a107c2-2071-4ce3-8330-cf82f3caa79f\",\"Operation\":\"Update user.\",\"OrganizationId\":\"3e49b082-62d5-4849-a5b0-86ed519287d2\",\"RecordType\":8,\"ResultStatus\":\"Success\",\"UserKey\":\"10030000A96EA230@domain.onmicrosoft.com\",\"UserType\":0,\"Version\":1,\"Workload\":\"AzureActiveDirectory\",\"ClientIP\":\"\",\"ObjectId\":\"aaaa.bbbb@example.org\",\"UserId\":\"user@domain.onmicrosoft.com\",\"AzureActiveDirectoryEventType\":1,\"ExtendedProperties\":[{\"Name\":\"additionalDetails\",\"Value\":\"{\\\"UserType\\\":\\\"Member\\\"}\"},{\"Name\":\"extendedAuditEventCategory\",\"Value\":\"User\"}],\"ModifiedProperties\":[{\"Name\":\"LastDirSyncTime\",\"NewValue\":\"[\\r\\n  \\\"2021-03-05T14:43:17Z\\\"\\r\\n]\",\"OldValue\":\"[\\r\\n  \\\"2021-03-03T12:30:50Z\\\"\\r\\n]\"},{\"Name\":\"Included Updated Properties\",\"NewValue\":\"LastDirSyncTime\",\"OldValue\":\"\"},{\"Name\":\"Action Client Name\",\"NewValue\":\"DirectorySync\",\"OldValue\":\"\"},{\"Name\":\"TargetId.UserType\",\"NewValue\":\"Member\",\"OldValue\":\"\"}],\"Actor\":[{\"ID\":\"user@domain.onmicrosoft.com\",\"Type\":5},{\"ID\":\"10030000A96EA230\",\"Type\":3},{\"ID\":\"User_c96cf894-cca6-438b-b6f2-c2744c1680f5\",\"Type\":2},{\"ID\":\"c96cf894-cca6-438b-b6f2-c2744c1680f5\",\"Type\":2},{\"ID\":\"User\",\"Type\":2}],\"ActorContextId\":\"3e49b082-62d5-4849-a5b0-86ed519287d2\",\"ActorIpAddress\":\"\",\"InterSystemsId\":\"92d46438-1e67-43e3-91ca-039ff39d7217\",\"IntraSystemId\":\"bd8cc421-efe8-4a44-b61d-44670fc6f56e\",\"SupportTicketId\":\"\",\"Target\":[{\"ID\":\"User_de76d2a9-d8bf-47d4-8f74-2ba2b560f55e\",\"Type\":2},{\"ID\":\"de76d2a9-d8bf-47d4-8f74-2ba2b560f55e\",\"Type\":2},{\"ID\":\"User\",\"Type\":2},{\"ID\":\"aaaa.bbbb@example.org\",\"Type\":5},{\"ID\":\"1003200119762B26\",\"Type\":3}],\"TargetContextId\":\"3e49b082-62d5-4849-a5b0-86ed519287d2\"}",
        "event": {
            "action": "Update user.",
            "kind": "event",
            "code": "8",
            "category": [
                "iam"
            ],
            "type": [
                "change"
            ]
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "user": {
            "name": "user@domain.onmicrosoft.com",
            "email": "user@domain.onmicrosoft.com"
        },
        "organization": {
            "id": "3e49b082-62d5-4849-a5b0-86ed519287d2"
        },
        "action": {
            "id": 8,
            "name": "Update user.",
            "target": "user",
            "outcome": "success"
        },
        "office365": {
            "record_type": 8,
            "result_status": "Success",
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "audit": {
                "object_id": "aaaa.bbbb@example.org"
            }
        },
        "related": {
            "user": [
                "user@domain.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "user_logged_in.json"

    ```json
	
    {
        "message": "{\"CreationTime\": \"2019-11-18T10:15:52\", \"Id\": \"405f795f-8bff-45d2-98c9-ef675d7d2db6\", \"Operation\": \"UserLoggedIn\", \"OrganizationId\": \"3e49b082-62d5-4849-a5b0-86ed519287d2\", \"RecordType\": 15, \"ResultStatus\": \"Succeeded\", \"UserKey\": \"10037FFEA0A22006@company.onmicrosoft.com\", \"UserType\": 0, \"Version\": 1, \"Workload\": \"AzureActiveDirectory\", \"ClientIP\": \"1.2.3.4:8085\", \"ObjectId\": \"5f09333a-842c-47da-a157-57da27fcbca5\", \"UserId\": \"REDACTED@company.onmicrosoft.com\", \"AzureActiveDirectoryEventType\": 1, \"ExtendedProperties\": [{\"Name\": \"UserAgent\", \"Value\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763\"}, {\"Name\": \"UserAuthenticationMethod\", \"Value\": \"1\"}, {\"Name\": \"RequestType\", \"Value\": \"OAuth2:Authorize\"}, {\"Name\": \"ResultStatusDetail\", \"Value\": \"Redirect\"}, {\"Name\": \"KeepMeSignedIn\", \"Value\": \"True\"}], \"ModifiedProperties\": [], \"Actor\": [{\"ID\": \"3d0e7ff9-261e-440f-a2f8-9e1ec4072f3e\", \"Type\": 0}, {\"ID\": \"REDACTED@company.onmicrosoft.com\", \"Type\": 5}, {\"ID\": \"10037FFEA0A22006\", \"Type\": 3}], \"ActorContextId\": \"3e49b082-62d5-4849-a5b0-86ed519287d2\", \"ActorIpAddress\": \"1.2.3.4\", \"InterSystemsId\": \"794c9504-66fe-441c-831a-5fc2badfcdc8\", \"IntraSystemId\": \"99f54f6a-ddfe-4916-b89b-edd9fcac4500\", \"SupportTicketId\": \"\", \"Target\": [{\"ID\": \"5f09333a-842c-47da-a157-57da27fcbca5\", \"Type\": 0}], \"TargetContextId\": \"3e49b082-62d5-4849-a5b0-86ed519287d2\", \"ApplicationId\": \"89bee1f7-5e6e-4d8a-9f3d-ecd601259da7\"}",
        "event": {
            "action": "UserLoggedIn",
            "kind": "event",
            "code": "15",
            "category": [
                "authentication"
            ],
            "type": [
                "start"
            ]
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "user": {
            "name": "REDACTED@company.onmicrosoft.com",
            "email": "REDACTED@company.onmicrosoft.com"
        },
        "organization": {
            "id": "3e49b082-62d5-4849-a5b0-86ed519287d2"
        },
        "action": {
            "id": 15,
            "name": "UserLoggedIn",
            "target": "network-traffic",
            "outcome": "success"
        },
        "source": {
            "ip": "1.2.3.4",
            "port": 8085,
            "address": "1.2.3.4"
        },
        "office365": {
            "record_type": 15,
            "result_status": "Succeeded",
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "auth": {
                "user_authentication_method": 1,
                "request_type": "OAuth2:Authorize",
                "result_status_detail": "Redirect",
                "keep_me_signed_in": true
            },
            "audit": {
                "object_id": "5f09333a-842c-47da-a157-57da27fcbca5"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "REDACTED@company.onmicrosoft.com"
            ]
        }
    }
    	
	```


=== "user_login_failed.json"

    ```json
	
    {
        "message": "{\"CreationTime\":\"2022-10-14T13:48:03\",\"Id\":\"4af0b443-42dd-4dc6-9bd1-751a55441000\",\"Operation\":\"UserLoginFailed\",\"OrganizationId\":\"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\",\"RecordType\":15,\"ResultStatus\":\"Success\",\"UserKey\":\"785d81fb-82aa-4ff3-9cbc-e3280761f36a\",\"UserType\":0,\"Version\":1,\"Workload\":\"AzureActiveDirectory\",\"ClientIP\":\"20.250.8.183\",\"ObjectId\":\"00000003-0000-0ff1-ce00-000000000000\",\"UserId\":\"user@mycompany.com\",\"AzureActiveDirectoryEventType\":1,\"ExtendedProperties\":[{\"Name\":\"ResultStatusDetail\",\"Value\":\"Success\"},{\"Name\":\"UserAgent\",\"Value\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0\"},{\"Name\":\"UserAuthenticationMethod\",\"Value\":\"1\"},{\"Name\":\"RequestType\",\"Value\":\"SAS:EndAuth\"}],\"ModifiedProperties\":[],\"Actor\":[{\"ID\":\"785d81fb-82aa-4ff3-9cbc-e3280761f36a\",\"Type\":0},{\"ID\":\"user@mycompany.com\",\"Type\":5}],\"ActorContextId\":\"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\",\"ActorIpAddress\":\"20.250.8.183\",\"InterSystemsId\":\"d48e6ea0-40c1-5000-5eba-0ee33d13b1ca\",\"IntraSystemId\":\"4af0b443-42dd-4dc6-9bd1-751a55441000\",\"SupportTicketId\":\"\",\"Target\":[{\"ID\":\"00000003-0000-0ff1-ce00-000000000000\",\"Type\":0}],\"TargetContextId\":\"aa09a079-7796-46a8-a4d4-4d21b0dcf1b2\",\"ApplicationId\":\"00000003-0000-0ff1-ce00-000000000000\",\"DeviceProperties\":[{\"Name\":\"OS\",\"Value\":\"Windows 10\"},{\"Name\":\"BrowserType\",\"Value\":\"Firefox\"},{\"Name\":\"IsCompliantAndManaged\",\"Value\":\"False\"},{\"Name\":\"SessionId\",\"Value\":\"b3a9b2b4-57c9-406b-9a2d-106b7f612248\"}],\"ErrorNumber\":\"500121\",\"LogonError\":\"AuthenticationFailedSasError\"}",
        "event": {
            "action": "UserLoginFailed",
            "kind": "event",
            "code": "15",
            "category": [
                "iam"
            ],
            "type": [
                "info"
            ]
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "user": {
            "name": "user@mycompany.com",
            "email": "user@mycompany.com"
        },
        "organization": {
            "id": "aa09a079-7796-46a8-a4d4-4d21b0dcf1b2"
        },
        "action": {
            "id": 15,
            "name": "UserLoginFailed",
            "target": "network-traffic",
            "outcome": "success"
        },
        "source": {
            "ip": "20.250.8.183",
            "address": "20.250.8.183"
        },
        "office365": {
            "record_type": 15,
            "result_status": "Success",
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "audit": {
                "object_id": "00000003-0000-0ff1-ce00-000000000000"
            },
            "logon_error": "AuthenticationFailedSasError",
            "error_number": 500121,
            "auth": {
                "user_authentication_method": 1,
                "request_type": "SAS:EndAuth",
                "result_status_detail": "Success"
            }
        },
        "user_agent": {
            "original": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
        },
        "related": {
            "ip": [
                "20.250.8.183"
            ],
            "user": [
                "user@mycompany.com"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`action.properties` | `object` | A list of objects describing the action |
|`action.target` | `keyword` | The target of the action |
|`email.attachments` | `array` | A list of objects describing the attachment files sent along with an email message |
|`email.delivery_timestamp` | `date` | The date and time when the email message was received by the service or client |
|`email.from.address` | `keyword` | The email address of the sender, typically from the RFC 5322 From: header field |
|`email.local_id` | `keyword` | Unique identifier given to the email by the source that created the event |
|`email.message_id` | `keyword` | Identifier from the RFC 5322 Message-ID: email header that refers to a particular email message |
|`email.reply_to.address` | `keyword` | The address that replies should be delivered to based on the value in the RFC 5322 Reply-To: header |
|`email.subject` | `keyword` | A brief summary of the topic of the message |
|`email.to.address` | `keyword` | The email address of recipient |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`event.url` | `keyword` | Event investigation URL |
|`file.directory` | `keyword` | Directory where the file is located. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`office365.audit.object_id` | `keyword` | For Exchange admin audit logging, the name of the object that was modified by the cmdlet. For SharePoint activity, the full URL path name of the file or folder accessed by a user. For Azure AD activity, the name of the user account that was modified. |
|`office365.auth.keep_me_signed_in` | `boolean` | User KeepMeSignedIn choice |
|`office365.auth.request_type` | `keyword` | Authentifcation type |
|`office365.auth.result_status_detail` | `keyword` | Authentication result detail |
|`office365.auth.user_authentication_method` | `long` | User authentication method |
|`office365.context.aad_session_id` | `keyword` | The identifier of an Azure Active Directory session |
|`office365.context.api_id` | `keyword` | The identifier of the API pathway |
|`office365.context.client.id` | `keyword` | The identifier of Azure Active Directory application |
|`office365.context.client.name` | `keyword` | The name of Azure Active Directory application |
|`office365.context.correlation.id` | `keyword` | The identifier to correlate user's action across Microsoft 365 services |
|`office365.defender.additional_actions` | `array` | The additional actions taken on the email |
|`office365.defender.auth_details` | `array` | The authentication checks that are done for the email |
|`office365.defender.connectors` | `keyword` | Identifiers of connectors associated with the email |
|`office365.defender.detection.method` | `keyword` | The method or the technology used for the detection |
|`office365.defender.detection.technology` | `keyword` | The threats and technologies applied on the email |
|`office365.defender.detection.type` | `keyword` | The type of detection |
|`office365.defender.email.attachments` | `array` | The attachements of the email |
|`office365.defender.email.delivery.action` | `keyword` | The original action delivery on the email |
|`office365.defender.email.delivery.latest_location` | `keyword` | The latest location delivery of the email |
|`office365.defender.email.delivery.original_location` | `keyword` | The original location delivery of the email |
|`office365.defender.email.verdict.confidence` | `keyword` | The confidence in the verdict |
|`office365.defender.email.verdict.reason` | `keyword` | The verdict about the messahe |
|`office365.defender.system_overrides` | `array` | Overrides that are applicable to the email |
|`office365.error_number` | `long` | Error number |
|`office365.logon_error` | `keyword` | Logon error detailed reason |
|`office365.record_type` | `long` | The type of the operation |
|`office365.result_status` | `keyword` | Indicates whether the action was successful or not |
|`office365.scope.code` | `long` | The origin (saas or on-premise) of the event |
|`office365.teams.action` | `keyword` | The action taken by an invitee or the channel owner |
|`office365.teams.channel.id` | `keyword` | The identifier of the channel |
|`office365.teams.channel.name` | `keyword` | The name of the channel |
|`office365.teams.channel.type` | `keyword` | The type of the channel |
|`office365.teams.communication.type` | `keyword` | The type of communication |
|`office365.teams.invitee` | `keyword` | The identifier of an invitee |
|`office365.teams.message.id` | `keyword` | The identifier of the message |
|`office365.teams.message.size` | `long` | The size of the message in bytes with UTF-16 encoding |
|`office365.teams.message.urls` | `keyword` | A list of urls present in the message |
|`office365.teams.message.version` | `keyword` | The version of the message |
|`office365.teams.team.id` | `keyword` | The identifier of the team |
|`office365.teams.team.members` | `object` | The list of users in a team |
|`office365.teams.team.name` | `keyword` | The name of the team |
|`office365.user_type.code` | `long` | The type of user that performed the operation |
|`organization.id` | `keyword` | Unique identifier for the organization. |
|`rule.category` | `keyword` | Rule category |
|`service.name` | `keyword` | Name of the service. |
|`source.ip` | `ip` | IP address of the source. |
|`source.port` | `long` | Port of the source. |
|`url.full` | `wildcard` | Full unparsed URL. |
|`url.original` | `wildcard` | Unmodified original url as seen in the event source. |
|`user.email` | `keyword` | User email address. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

