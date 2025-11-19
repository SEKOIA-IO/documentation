
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "audit_success_login"


    ```json
	{
        "Type": "Audit",
        "MsgId": "L-LG-04-0",
        "Result": "Success",
        "User": "tata",
        "Category": "User",
        "Client": "2.2.2.2",
        "Action": "Session Login",
        "Description": "Successful user login - mwg-w7"
    }
    ```



=== "audit_success_logout"


    ```json
	{
        "Type": "Audit",
        "MsgId": "L-LG-05-0",
        "Result": "Success",
        "User": "tata",
        "Category": "User",
        "Client": "2.2.2.2",
        "Action": "Session Logout",
        "Description": "Successful user logout: mwg-w7"
    }
    ```



=== "failed_admin"


    ```json
	{
        "Type": "Audit",
        "MsgId": "M-MC-27-1",
        "Result": "Failure",
        "User": "tata",
        "Category": "Admin",
        "Client": "Localhost",
        "Action": "Manage Trusted Certificate",
        "Description": "MATD Web Certificate does not meet Security requirement"
    }
    ```



=== "success_admin"


    ```json
	{
        "Result": "Success",
        "Action": "Database Pruning",
        "User": "toto",
        "Client": "localhost",
        "Type": "Audit",
        "Category": "Admin",
        "Description": "Record threshold count not met",
        "MsgId": "B-DB-02-1"
    }
    ```



=== "success_login"


    ```json
	{
        "Action": "Successful user login",
        "User": "toto",
        "UserID": "65",
        "Timestamp": "2025-07-22 11:38:44",
        "Client": "2.2.2.2"
    }
    ```



=== "success_logout"


    ```json
	{
        "Action": "Successful user logout",
        "User": "toto",
        "UserID": "65",
        "Timestamp": "2025-07-22 11:38:45",
        "Client": "2.2.2.2",
        "HTTPAgent": "Skyhigh Secure Web Gateway 12.2.16.52651"
    }
    ```



=== "suspicious_file_report"


    ```json
	{
        "Summary": {
            "Event_Type": "ATD File Report",
            "MISversion": "5.2.0.16",
            "SUMversion": "5.2.0.16",
            "DETversion": "5.2.6.250110",
            "OSversion": "win10p0x64",
            "fileId": "Not Available",
            "Parent MD5": "Not Available",
            "ATD IP": "1.1.1.1",
            "Src IP": "2.2.2.2",
            "Dst IP": "",
            "TaskId": "144115188076224076",
            "JobId": "144115188076216640",
            "JSONversion": "1.003",
            "SubmitterName": "toto",
            "SubmitterType": "MWG",
            "hasDynamicAnalysis": "true",
            "Subject": {
                "Name": "file.xxx",
                "Type": "application/pdf",
                "FileType": "4",
                "md5": "AE299DBD8F796B8A5479E763BB00FB93",
                "sha-1": "A826D22E2FF0971FB932E88CFCB75CCB16D6B9C2",
                "sha-256": "229F83A69C6D7B8E10819762CBDE8AC45CC03B4BD0DD5EA54EC608AB6A85B89A",
                "size": "54620",
                "Timestamp": "2025-07-22 08:25:39",
                "parent_archive": "Not Available"
            },
            "Selectors": [
                {
                    "Engine": "Gateway Anti-Malware",
                    "MalwareName": "---",
                    "Severity": "0"
                },
                {
                    "Engine": "GTI File Reputation",
                    "MalwareName": "---",
                    "Severity": "0"
                },
                {
                    "Engine": "GTI URL Reputation",
                    "MalwareName": "Business ",
                    "Severity": "1"
                },
                {
                    "Engine": "Anti-Malware",
                    "MalwareName": "---",
                    "Severity": "0"
                },
                {
                    "Engine": "YARA",
                    "MalwareName": "---",
                    "Severity": "0"
                },
                {
                    "Engine": "Sandbox",
                    "MalwareName": "---",
                    "Severity": "2"
                }
            ],
            "Verdict": {
                "Severity": "2",
                "Description": "Sample is somewhat suspicious: final severity level 2"
            },
            "Processes": [
                {
                    "Name": "acrord32.exe",
                    "Md5": "",
                    "Sha1": "",
                    "Sha256": "",
                    "Severity": "2"
                },
                {
                    "Name": "splwow64.exe",
                    "Md5": "",
                    "Sha1": "",
                    "Sha256": "",
                    "Severity": "2"
                },
                {
                    "Name": "jst1.js",
                    "Md5": "",
                    "Sha1": "",
                    "Sha256": "",
                    "Severity": "2"
                }
            ],
            "Files": [
                {
                    "Processes": [
                        {
                            "RelType": "512",
                            "Name": "file.xxx",
                            "Sha256": "229F83A69C6D7B8E10819762CBDE8AC45CC03B4BD0DD5EA54EC608AB6A85B89A"
                        }
                    ],
                    "Md5": "D633AE9E8E94BC640AF6581B53D250FB",
                    "Sha1": "9BC9DBD1F9C23F9B9437F5E71B44FC8988971084",
                    "Sha256": "53CBA858F975AB69E9782745369E42DC7674A7B58C24EE10F2C65304C48B9BC8",
                    "Name": "file.xxx",
                    "FileType": "128"
                },
                {
                    "Processes": [
                        {
                            "RelType": "512",
                            "Name": "file.xxx",
                            "Sha256": "229F83A69C6D7B8E10819762CBDE8AC45CC03B4BD0DD5EA54EC608AB6A85B89A"
                        }
                    ],
                    "Md5": "B451FF15BA0A31EBDFB809D4E8929B3D",
                    "Sha1": "B81FA68215FAF82211F226325649BC717DBCAE40",
                    "Sha256": "B10D4CFF0E8F500510B412C9543CE8280B616ECA4B7F9FAE184B3095AB43AF53",
                    "Name": "file.xxx",
                    "FileType": "128"
                }
            ],
            "Urls": [
                {
                    "Processes": [
                        {
                            "RelType": "8",
                            "Name": "file.xxx",
                            "Sha256": ""
                        }
                    ],
                    "Category": "Business ",
                    "Functional": "Business/Services ",
                    "Risk": "Information ",
                    "Port": "80",
                    "Reputation": "3",
                    "Severity": "1",
                    "Url": "HTTPS://ODACE.APPARETE.FR/EDITIONS"
                },
                {
                    "Processes": [
                        {
                            "RelType": "8",
                            "Name": "file.xxx",
                            "Sha256": ""
                        }
                    ],
                    "Category": "Business ",
                    "Functional": "Business/Services ",
                    "Risk": "Information ",
                    "Port": "80",
                    "Reputation": "3",
                    "Severity": "1",
                    "Url": "HTTPS://ODACE.APPARETE.FR/EDITIONS/EDITION_CONSULT.ASPX?DXREP_FAKE=&EDITIONNUMARA=F73A9E66-DB7A-486F-A5E8-D86443F8CAC3&RELOAD=TRUE"
                }
            ],
            "Stats": [
                {
                    "ID": "0",
                    "Category": "Persistence, Installation Boot Survival ",
                    "Severity": "2"
                },
                {
                    "ID": "1",
                    "Category": "Hiding, Camouflage, Stealthiness, Detection and Removal Protection ",
                    "Severity": "2"
                },
                {
                    "ID": "2",
                    "Category": "Security Solution / Mechanism bypass, termination and removal, Anti Debugging, VM Detection ",
                    "Severity": "1"
                },
                {
                    "ID": "3",
                    "Category": "Spreading ",
                    "Severity": "1"
                },
                {
                    "ID": "4",
                    "Category": "Exploiting, Shellcode ",
                    "Severity": "2"
                },
                {
                    "ID": "5",
                    "Category": "Networking ",
                    "Severity": "1"
                },
                {
                    "ID": "6",
                    "Category": "Data spying, Sniffing, Keylogging, Ebanking Fraud ",
                    "Severity": "1"
                }
            ],
            "Behavior": [
                {
                    "ID": "2",
                    "Analysis": "Identified as --- by Gateway Anti-Malware"
                },
                {
                    "ID": "1",
                    "Analysis": "Identified as --- by GTI File Reputation"
                },
                {
                    "ID": "256",
                    "Analysis": "Identified as Business  by GTI URL Reputation"
                },
                {
                    "ID": "4",
                    "Analysis": "Identified as --- by Anti-Malware"
                },
                {
                    "ID": "128",
                    "Analysis": "Identified as --- by YARA"
                },
                {
                    "ID": "2803",
                    "Analysis": "Tracing System location"
                },
                {
                    "ID": "2859",
                    "Analysis": "Gathered system time information"
                },
                {
                    "ID": "25",
                    "Analysis": "Detected scripting content embedded in the sample"
                },
                {
                    "ID": "2905",
                    "Analysis": "Javascipt is executed using wscript or cscript"
                },
                {
                    "ID": "2883",
                    "Analysis": "Gathering system info via WMIC "
                }
            ],
            "Mitre": [
                {
                    "ID": "T1059",
                    "Technique Name": "Command and Scripting Interpreter",
                    "Tactics": "Execution",
                    "Subtechniques": [
                        {
                            "ID": "T1059.005",
                            "Sub-Technique Name": "Visual Basic",
                            "Rules": [
                                {
                                    "Description": "Detected scripting content embedded in the sample",
                                    "Severity": "2"
                                }
                            ]
                        },
                        {
                            "ID": "T1059.007",
                            "Sub-Technique Name": "JavaScript",
                            "Rules": [
                                {
                                    "Description": "Detected scripting content embedded in the sample",
                                    "Severity": "2"
                                },
                                {
                                    "Description": "Javascipt is executed using wscript or cscript",
                                    "Severity": "1"
                                }
                            ]
                        }
                    ]
                },
                {
                    "ID": "T1082",
                    "Technique Name": "System Information Discovery",
                    "Tactics": "Discovery",
                    "Rules": [
                        {
                            "Description": "Gathering system info via WMIC ",
                            "Severity": "2"
                        }
                    ]
                },
                {
                    "ID": "T1124",
                    "Technique Name": "System Time Discovery",
                    "Tactics": "Discovery",
                    "Rules": [
                        {
                            "Description": "Gathered system time information",
                            "Severity": "2"
                        }
                    ]
                },
                {
                    "ID": "T1614",
                    "Technique Name": "System Location Discovery",
                    "Tactics": "Discovery",
                    "Rules": [
                        {
                            "Description": "Tracing System location",
                            "Severity": "2"
                        }
                    ]
                }
            ]
        }
    }
    ```



=== "unverified_file_report"


    ```json
	{
        "Summary": {
            "Event_Type": "ATD File Report",
            "MISversion": "5.2.0.16",
            "SUMversion": "5.2.0.16",
            "DETversion": "5.2.6.250110",
            "OSversion": "win7sp1x64_Win7SP1x64-IANNG",
            "fileId": "Not Available",
            "Parent MD5": "Not Available",
            "ATD IP": "1.1.1.1",
            "Src IP": "2.2.2.2",
            "Dst IP": "",
            "TaskId": "144115188076224043",
            "JobId": "144115188076216607",
            "JSONversion": "1.003",
            "SubmitterName": "toto",
            "SubmitterType": "MWG",
            "hasDynamicAnalysis": "true",
            "Subject": {
                "Name": "file.xxx",
                "Type": "PE32+ executable (GUI) x86-64",
                "FileType": "0",
                "md5": "D0E38E34A8A648CB663FB75DBCC849D2",
                "sha-1": "8B86FAFB36D4A680121209C0EEABB606E6169B36",
                "sha-256": "6AB95CCECF9FF63EDC1FA183B4E85D52A24A078471D9E4AD8BC7D7739CA78957",
                "size": "1210009",
                "Timestamp": "2025-07-20 20:28:11",
                "parent_archive": "Not Available"
            },
            "Selectors": [
                {
                    "Engine": "Gateway Anti-Malware",
                    "MalwareName": "---",
                    "Severity": "0"
                },
                {
                    "Engine": "GTI File Reputation",
                    "MalwareName": "---",
                    "Severity": "0"
                },
                {
                    "Engine": "GTI URL Reputation",
                    "MalwareName": "---",
                    "Severity": "-1"
                },
                {
                    "Engine": "Anti-Malware",
                    "MalwareName": "---",
                    "Severity": "0"
                },
                {
                    "Engine": "YARA",
                    "MalwareName": "---",
                    "Severity": "0"
                },
                {
                    "Engine": "Sandbox",
                    "MalwareName": "---",
                    "Severity": "0"
                }
            ],
            "Verdict": {
                "Severity": "0",
                "Description": "Sample termination reason: Sample could not run successfully in the Windows system."
            },
            "Urls": [
                {
                    "Processes": [
                        {
                            "RelType": "8",
                            "Name": "file.xxx",
                            "Sha256": ""
                        }
                    ],
                    "Category": "Business ",
                    "Functional": "Business/Services ",
                    "Risk": "Information ",
                    "Port": "80",
                    "Reputation": "-2",
                    "Severity": "0",
                    "Url": "HTTP://MSEDGE.B.TLU.DL.DELIVERY.MP.MICROSOFT.COM/FILESTREAMINGSERVICE/FILES"
                },
                {
                    "Processes": [
                        {
                            "RelType": "8",
                            "Name": "file.xxx",
                            "Sha256": ""
                        }
                    ],
                    "Category": "Business ",
                    "Functional": "Business/Services ",
                    "Risk": "Information ",
                    "Port": "80",
                    "Reputation": "-2",
                    "Severity": "0",
                    "Url": "HTTP://MSEDGE.B.TLU.DL.DELIVERY.MP.MICROSOFT.COM/FILESTREAMINGSERVICE/FILES/5F16D794-76D1-4AAC-94C6-CCD95709A3EB?P1=1753647178&P2=404&P3=2&P4=LNT3D5CCNVBKF8PY170SO36YRX%2B%2BKLCTFWQOF80NDJW9WOEXHDFAKX"
                }
            ],
            "Behavior": [
                {
                    "ID": "2",
                    "Analysis": "Identified as --- by Gateway Anti-Malware"
                },
                {
                    "ID": "1",
                    "Analysis": "Identified as --- by GTI File Reputation"
                },
                {
                    "ID": "256",
                    "Analysis": "Identified as --- by GTI URL Reputation"
                },
                {
                    "ID": "4",
                    "Analysis": "Identified as --- by Anti-Malware"
                },
                {
                    "ID": "128",
                    "Analysis": "Identified as --- by YARA"
                }
            ]
        }
    }
    ```



