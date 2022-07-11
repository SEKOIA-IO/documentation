
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
| Category | `file`, `network` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "ad.json"

    ```json
	
    {
        "user": {
            "name": "user@company.onmicrosoft.com",
            "email": "user@company.onmicrosoft.com"
        },
        "organization": {
            "id": "aa09a079-7796-46a8-a4d4-4d21b0dcf1b2"
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "event": {
            "action": "UserLoggedIn",
            "kind": "event",
            "type": [
                "start"
            ],
            "category": [
                "authentication"
            ],
            "code": "15"
        },
        "action": {
            "name": "UserLoggedIn",
            "id": 15,
            "outcome": "success",
            "target": "network-traffic",
            "properties": [
                {
                    "value": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                    "name": "UserAgent"
                },
                {
                    "value": "1",
                    "name": "UserAuthenticationMethod"
                },
                {
                    "value": "OAuth2:Authorize",
                    "name": "RequestType"
                },
                {
                    "value": "Redirect",
                    "name": "ResultStatusDetail"
                },
                {
                    "value": "True",
                    "name": "KeepMeSignedIn"
                }
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "office365": {
            "record_type": 15,
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
        "event": {
            "action": "FilePreviewed",
            "kind": "event",
            "category": [
                "file"
            ],
            "type": [
                "info"
            ],
            "code": "6"
        },
        "organization": {
            "id": "aa09a079-7796-46a8-a4d4-4d21b0dcf1b2"
        },
        "office365": {
            "record_type": 6,
            "user_type": {
                "code": 0,
                "name": "Regular"
            }
        },
        "action": {
            "name": "FilePreviewed",
            "outcome": "success",
            "id": 6,
            "target": "user",
            "properties": [
                {
                    "SiteUrl": "https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/",
                    "SourceFileName": "MyDocument.docx",
                    "SourceRelativeUrl": "Documents",
                    "UserAgent": "OneDriveMpc-Transform_Thumbnail/1.0"
                }
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "file": {
            "directory": "Documents",
            "name": "MyDocument.docx"
        },
        "url": {
            "domain": "company-my.sharepoint.com",
            "full": "https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/Documents/MyDocument.docx",
            "original": "https://company-my.sharepoint.com/personal/jane_doe_company_onmicrosoft_com/Documents/MyDocument.docx",
            "path": "/personal/jane_doe_company_onmicrosoft_com/Documents/MyDocument.docx",
            "port": 443,
            "registered_domain": "sharepoint.com",
            "scheme": "https",
            "subdomain": "company-my",
            "top_level_domain": "com"
        },
        "user_agent": {
            "original": "OneDriveMpc-Transform_Thumbnail/1.0"
        },
        "service": {
            "name": "OneDrive"
        },
        "user": {
            "name": "jane.doe@company.onmicrosoft.com",
            "email": "jane.doe@company.onmicrosoft.com"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
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
        "event": {
            "action": "FileSyncDownloadedFull",
            "kind": "event",
            "category": [
                "file"
            ],
            "type": [
                "info"
            ],
            "code": "6"
        },
        "action": {
            "name": "FileSyncDownloadedFull",
            "outcome": "success",
            "id": 6,
            "target": "user",
            "properties": [
                {
                    "SiteUrl": "https://company.sharepoint.com/sites/shared",
                    "SourceFileName": "logo.png",
                    "SourceRelativeUrl": "public/assets/website",
                    "UserAgent": "Microsoft SkyDriveSync 22.099.0508.0001 ship; Windows NT 10.0 (19043)"
                }
            ]
        },
        "organization": {
            "id": "2d7585dc-97bc-4494-b98c-79f2a4946931"
        },
        "office365": {
            "record_type": 6,
            "user_type": {
                "code": 0,
                "name": "Regular"
            },
            "context": {
                "aad_session_id": "0e042318-7c78-4acb-ae00-5ee74465bca3",
                "correlation": {
                    "id": "c299a0a0-14da-428a-b08d-481d562298cb"
                }
            }
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "file": {
            "directory": "public/assets/website",
            "name": "logo.png"
        },
        "url": {
            "domain": "company.sharepoint.com",
            "full": "https://company.sharepoint.com/sites/shared/public/assets/website/logo.png",
            "original": "https://company.sharepoint.com/sites/shared/public/assets/website/logo.png",
            "path": "/sites/shared/public/assets/website/logo.png",
            "port": 443,
            "registered_domain": "sharepoint.com",
            "scheme": "https",
            "subdomain": "company",
            "top_level_domain": "com"
        },
        "user_agent": {
            "original": "Microsoft SkyDriveSync 22.099.0508.0001 ship; Windows NT 10.0 (19043)"
        },
        "service": {
            "name": "SharePoint"
        },
        "user": {
            "name": "marketing@company.com",
            "email": "marketing@company.com"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
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
        "action": {
            "id": 28,
            "name": "Blocked",
            "outcome": "success",
            "target": "user"
        },
        "event": {
            "action": "Blocked",
            "code": "28",
            "kind": "event",
            "outcome": "success",
            "id": "00000000-0000-0000-0000-000000000000'",
            "url": "https://protection.office.com/?hash=/threatexplorer?messageParams=a4dbf74a-89e0-40de-b14d-df573f48aa45,a4dbf74a-89e0-40de-b14d-df573f48aa45-0000000000000000000-1,2022-07-08T00:00:00,2022-07-08T23:59:59&view=Malware"
        },
        "email": {
            "attachments": [
                {
                    "file": {
                        "hash": {
                            "sha256": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"
                        },
                        "mime_type": "exe;zip",
                        "name": "malicious.pdf.exe"
                    }
                }
            ],
            "delivery_timestamp": "2022-07-08T09:07:47",
            "from": {
                "address": [
                    "human@sender.com"
                ]
            },
            "local_id": "7250ff78-fd13-45a2-bb5d-23a5d59c2699",
            "message_id": "4cc4a74e-a195-4222-abd7-a8adf2cd347d@sender.com",
            "reply_to": {
                "address": [
                    "prvs=0000000000=human@sender.com"
                ]
            },
            "subject": "Refund to you",
            "to": {
                "address": [
                    "human@example.com"
                ]
            }
        },
        "office365": {
            "defender": {
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
                "detection": {
                    "method": "File detonation",
                    "technology": [
                        "Malware: [File detonation]",
                        "Spam: [General filter]"
                    ],
                    "type": "Inline"
                },
                "email": {
                    "attachments": [
                        {
                            "name": "Trojan_Gen_FileWithSpoofedExtension_A",
                            "verdict": {
                                "code": "1",
                                "name": "bad"
                            }
                        }
                    ],
                    "delivery": {
                        "action": "Blocked",
                        "latest_location": "Quarantine",
                        "original_location": "Quarantine"
                    },
                    "verdict": {
                        "reason": "Malware"
                    }
                },
                "system_overrides": [
                    {
                        "Details": "Antimalware policy block by file type",
                        "FinalOverride": "No",
                        "Result": "Block",
                        "Source": "Tenant"
                    }
                ]
            },
            "record_type": 28,
            "user_type": {
                "code": 4,
                "name": "System"
            }
        },
        "organization": {
            "id": "8a457951-a594-4607-a5dc-dfc72338eb13"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "ThreatIntel"
            ]
        },
        "service": {
            "name": "ThreatIntelligence"
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "name": "ThreatIntel"
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
        "action": {
            "name": "Update group.",
            "id": 8,
            "outcome": "success",
            "target": "user"
        },
        "organization": {
            "id": "3e49b082-62d5-4849-a5b0-86ed519287d2"
        },
        "office365": {
            "record_type": 8,
            "result_status": "Success",
            "user_type": {
                "code": 0,
                "name": "Regular"
            }
        },
        "event": {
            "action": "Update group.",
            "kind": "event",
            "category": [
                "iam"
            ],
            "type": [
                "change"
            ],
            "code": "8"
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "user": {
            "name": "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com",
            "email": "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
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
        "action": {
            "name": "Update user.",
            "id": 8,
            "outcome": "success",
            "target": "user"
        },
        "organization": {
            "id": "3e49b082-62d5-4849-a5b0-86ed519287d2"
        },
        "office365": {
            "record_type": 8,
            "result_status": "Success",
            "user_type": {
                "code": 0,
                "name": "Regular"
            }
        },
        "event": {
            "name": "Update user.",
            "action": "Update user.",
            "kind": "event",
            "category": [
                "iam"
            ],
            "type": [
                "change"
            ],
            "code": "8"
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "user": {
            "name": "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com",
            "email": "Sync_V-WATT_83d3b7098669@acme.onmicrosoft.com"
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
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
        "user": {
            "name": "user@domain.onmicrosoft.com",
            "email": "user@domain.onmicrosoft.com"
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "organization": {
            "id": "3e49b082-62d5-4849-a5b0-86ed519287d2"
        },
        "office365": {
            "record_type": 8,
            "result_status": "Success",
            "user_type": {
                "code": 0,
                "name": "Regular"
            }
        },
        "event": {
            "action": "Update user.",
            "kind": "event",
            "category": [
                "iam"
            ],
            "type": [
                "change"
            ],
            "code": "8"
        },
        "action": {
            "name": "Update user.",
            "id": 8,
            "outcome": "success",
            "target": "user",
            "properties": [
                {
                    "value": null,
                    "name": "LastDirSyncTime"
                },
                {
                    "value": null,
                    "name": "Action Client Name"
                },
                {
                    "value": null,
                    "name": "TargetId.UserType"
                }
            ]
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
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
        "user": {
            "name": "REDACTED@company.onmicrosoft.com",
            "email": "REDACTED@company.onmicrosoft.com"
        },
        "organization": {
            "id": "3e49b082-62d5-4849-a5b0-86ed519287d2"
        },
        "office365": {
            "record_type": 15,
            "result_status": "Succeeded",
            "user_type": {
                "code": 0,
                "name": "Regular"
            }
        },
        "service": {
            "name": "AzureActiveDirectory"
        },
        "event": {
            "action": "UserLoggedIn",
            "kind": "event",
            "type": [
                "start"
            ],
            "category": [
                "authentication"
            ],
            "code": "15"
        },
        "action": {
            "name": "UserLoggedIn",
            "id": 15,
            "outcome": "success",
            "target": "network-traffic",
            "properties": [
                {
                    "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
                    "name": "UserAgent"
                },
                {
                    "value": "1",
                    "name": "UserAuthenticationMethod"
                },
                {
                    "value": "OAuth2:Authorize",
                    "name": "RequestType"
                },
                {
                    "value": "Redirect",
                    "name": "ResultStatusDetail"
                },
                {
                    "value": "True",
                    "name": "KeepMeSignedIn"
                }
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4",
            "port": 8085
        },
        "sekoiaio": {
            "intake": {
                "parsing_status": "success"
            }
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





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`action.properties` | `object` | None |
|`action.target` | `keyword` | None |
|`email.attachments` | `array` | None |
|`email.delivery_timestamp` | `date` | None |
|`email.from.address` | `keyword` | None |
|`email.local_id` | `keyword` | None |
|`email.message_id` | `keyword` | None |
|`email.reply_to.address` | `keyword` | None |
|`email.subject` | `keyword` | None |
|`email.to.address` | `keyword` | None |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.code` | `keyword` | Identification code for this event. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`event.url` | `keyword` | Event investigation URL |
|`file.directory` | `keyword` | Directory where the file is located. |
|`file.name` | `keyword` | Name of the file including the extension, without the directory. |
|`office365.context.aad_session_id` | `keyword` | None |
|`office365.context.api_id` | `keyword` | None |
|`office365.context.client.id` | `keyword` | None |
|`office365.context.client.name` | `keyword` | None |
|`office365.context.correlation.id` | `keyword` | None |
|`office365.defender.additional_actions` | `array` | None |
|`office365.defender.auth_details` | `array` | None |
|`office365.defender.connectors` | `keyword` | None |
|`office365.defender.detection.method` | `keyword` | None |
|`office365.defender.detection.technology` | `keyword` | None |
|`office365.defender.detection.type` | `keyword` | None |
|`office365.defender.email.attachments` | `array` | None |
|`office365.defender.email.delivery.action` | `keyword` | None |
|`office365.defender.email.delivery.latest_location` | `keyword` | None |
|`office365.defender.email.delivery.original_location` | `keyword` | None |
|`office365.defender.email.verdict.confidence` | `keyword` | None |
|`office365.defender.email.verdict.reason` | `keyword` | None |
|`office365.defender.system_overrides` | `array` | None |
|`office365.record_type` | `long` | None |
|`office365.result_status` | `keyword` | None |
|`office365.scope.code` | `long` | None |
|`office365.teams.action` | `keyword` | None |
|`office365.teams.channel.id` | `keyword` | None |
|`office365.teams.channel.name` | `keyword` | None |
|`office365.teams.channel.type` | `keyword` | None |
|`office365.teams.communication.type` | `keyword` | None |
|`office365.teams.invitee` | `keyword` | None |
|`office365.teams.message.id` | `keyword` | None |
|`office365.teams.message.size` | `long` | None |
|`office365.teams.message.urls` | `keyword` | None |
|`office365.teams.message.version` | `keyword` | None |
|`office365.teams.team.id` | `keyword` | None |
|`office365.teams.team.members` | `object` | None |
|`office365.teams.team.name` | `keyword` | None |
|`office365.user_type.code` | `long` | None |
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

