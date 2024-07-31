
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_antivirus_alert"


    ```json
	{
        "rflId": 1,
        "time": "2022-10-28T12:03:08.954602+00:00",
        "lvl": 4,
        "module": "das",
        "eventName": "antivirusAlert",
        "ipSrc": "1.2.3.4",
        "ipDst": "5.6.7.8",
        "egKBId": 130161020000004,
        "domain__": "example.org",
        "location": "Task: \\Microsoft\\Windows\\InstallService\\ScanForUpdates",
        "atime": "2022-10-28T06:47:03.009122+00:00",
        "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "pid": null,
        "description": "Antivirus detection: 1/65 (1%)\nAutostart entry",
        "username": null,
        "hostname__": "MR11111",
        "os_architecture__": "x86_64",
        "os_release__": "10",
        "hash_last_update": "2022-10-27T14:45:12.038340+00:00",
        "tags": "",
        "cmdline": "C:\\Windows\\System32\\InstallServiceTasks.dll",
        "uid": "a262506e-3c9e-4afe-9233-f2335167ea86;windows;MR11111;example.org",
        "total": 65,
        "ppid": null,
        "ctime": "2021-09-13T07:11:02.365029+00:00",
        "os__": "windows",
        "os_version__": "10.0.19041",
        "positives": 1,
        "os_server__": false,
        "pCreateDatetime": null,
        "uuid__": "a262506e-3c9e-4afe-9233-f2335167ea86",
        "path": "C:\\WINDOWS\\System32\\InstallServiceTasks.dll",
        "tag": "TRI_AAA_WIN",
        "mtime": "2021-09-13T07:11:02.349390+00:00",
        "id": 999999999
    }
    ```



=== "test_heuristic_alert"


    ```json
	{
        "rflId": 1,
        "time": "2022-10-28T11:58:20.377350+00:00",
        "lvl": 5,
        "module": "das",
        "eventName": "HeuristicAlert",
        "ipSrc": "1.2.3.4",
        "ipDst": "5.6.7.8",
        "egKBId": 130181011000003,
        "ppid": 14172,
        "os_architecture__": "x86_64",
        "description": "Suspect spawn tree detected\n\u2500 (EXAMPLE-NT\\doe-j) C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe (14172)\n\u2500\u2500 (EXAMPLE-NT\\doe-j) C:\\Windows\\System32\\cmd.exe (10544)\n\nNo remediation taken",
        "os_version__": "10.0.19041",
        "pCreateDatetime": "2022-10-28T11:45:14.751830+00:00",
        "path": "C:\\Windows\\System32\\cmd.exe",
        "os_server__": false,
        "os__": "windows",
        "domain__": "example.org",
        "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "uuid__": "5c3ff0bc-5101-4152-a330-923e569c9229",
        "os_release__": "10",
        "username": "EXAMPLE-NT\\doe-j",
        "cmdline": "C:\\WINDOWS\\system32\\cmd.exe /d /c \"C:\\Users\\doe-j\\AppData\\Local\\Programs\\Fake Company\\program.exe\" chrome-extension://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ --parent-window=0 < \\\\.\\pipe\\LOCAL\\1111111111111111111111111111111111111111 > \\\\.\\pipe\\LOCAL\\11111111111111111111111111111111111111111",
        "location": "",
        "hostname__": "MR11111",
        "uid": "5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org",
        "tag": "TRI_AAA_WIN",
        "pid": 10544,
        "id": 888888888
    }
    ```



=== "test_oletools"


    ```json
	{
        "rflId": 1,
        "time": "2022-10-28T15:23:27.128665+00:00",
        "lvl": 5,
        "module": "das",
        "eventName": "oletools",
        "ipSrc": "1.2.3.4",
        "ipDst": "5.6.7.8",
        "egKBId": 130181040000001,
        "domain__": "example.org",
        "uid": "5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org",
        "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "os__": "windows",
        "maliciousMacro": null,
        "firstTimeMacro": null,
        "unknownMacro": null,
        "description": "URLs detected in a document file\n\nRemediation: no remediation taken\n\nSuspicious URLs:\n- http://www.google.com",
        "os_version__": "10.0.19041",
        "os_architecture__": "x86_64",
        "os_server__": false,
        "hostname__": "MR11111",
        "uuid__": "5c3ff0bc-5101-4152-a330-923e569c9229",
        "os_release__": "10",
        "path": "C:\\Users\\doe-j\\AppData\\Local\\Microsoft\\Windows\\INetCache\\Content.Outlook\\AAAAA\\suspicious.docx",
        "tag": "TRI_AAA_WIN",
        "report": "",
        "id": 555555555
    }
    ```



=== "test_oletools2"


    ```json
	{
        "rflId": 1,
        "time": "2022-11-02T08:13:10.566734+00:00",
        "lvl": 6,
        "module": "das",
        "eventName": "oletools",
        "ipSrc": "1.2.3.4",
        "ipDst": "5.6.7.8",
        "egKBId": 130181041000003,
        "os_server__": false,
        "tag": "TRI_AAA_WIN",
        "report": "Document file sha256: 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "uid": "5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org",
        "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "hostname__": "MR11111",
        "maliciousMacro": 1,
        "os__": "windows",
        "domain__": "example.org",
        "os_version__": "10.0.19041",
        "uuid__": "5c3ff0bc-5101-4152-a330-923e569c9229",
        "description": "Potential malicious VBA code detected in a document file\n- Suspicious macros detected (1)\n\nRemediation: no remediation taken\n\nBehaviors:\n- Suspicious | May run PowerShell commands\n\nSuspicious macros sha1:\n- adc83b19e793491b1c6ea0fd8b46cd9f32e592fc",
        "os_release__": "10",
        "os_architecture__": "x86_64",
        "firstTimeMacro": 0,
        "unknownMacro": 28,
        "path": "C:\\Users\\doe-j\\AppData\\Local\\Analysis\\FUNCRES.XLAM",
        "id": 837562963
    }
    ```



=== "test_policy_alert"


    ```json
	{
        "rflId": 1,
        "time": "2022-10-28T14:49:14.869905+00:00",
        "lvl": 6,
        "module": "das",
        "eventName": "HeuristicAlert",
        "ipSrc": "1.2.3.4",
        "ipDst": "5.6.7.8",
        "egKBId": 130171010000001,
        "ppid": 12296,
        "os_architecture__": "x86_64",
        "description": "Application policy: COPS WINDOWS v2 ([I] T1204.001 User Execution: Web requests from unusual sources)",
        "os_version__": "10.0.19041",
        "pCreateDatetime": "2022-10-28T14:31:26.157008+00:00",
        "path": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\106.0.1370.52\\identity_helper.exe",
        "os_server__": false,
        "os__": "windows",
        "domain__": "example.org",
        "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "uuid__": "5c3ff0bc-5101-4152-a330-923e569c9229",
        "os_release__": "10",
        "username": "EXAMPLE-NT\\doe-j",
        "cmdline": "\"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\106.0.1370.52\\identity_helper.exe\" --type=utility --utility-sub-type=winrt_app_id.mojom.WinrtAppIdService --lang=fr --service-sandbox-type=none --unsafely-treat-insecure-origin-as-secure=http://astgedgecp.region.local,http://astgedgecq.region.local,http://astgedrheq.region.local,http://astgedrhep.region.local --mojo-platform-channel-handle=3564 --field-trial-handle=2140,i,6139612544440408755,5345815150035985187,131072 /prefetch:8",
        "location": "",
        "hostname__": "MR11111",
        "uid": "5c3ff0bc-5101-4152-a330-923e569c9229;windows;MR11111;example.org",
        "tag": "TRI_AAA_WIN",
        "pid": 2424,
        "id": 666666666
    }
    ```



=== "test_sandbox_alert"


    ```json
	{
        "rflId": 1,
        "time": "2022-10-28T11:58:20.778323+00:00",
        "lvl": 5,
        "module": "das",
        "eventName": "sandboxAlert",
        "ipSrc": "1.2.3.4",
        "ipDst": "5.6.7.8",
        "egKBId": 130181030000003,
        "ppid": 3520,
        "os_architecture__": "x86_64",
        "description": "Sandbox detection: 45%",
        "os_version__": "10.0.19041",
        "pCreateDatetime": "2022-10-28T11:48:08.373808+00:00",
        "path": "C:\\Program Files\\Vendor\\Product\\program.exe",
        "os_server__": false,
        "os__": "windows",
        "domain__": "example.org",
        "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "uuid__": "64a2fa85-0852-4745-81d6-0815eb2d5248",
        "os_release__": "10",
        "username": "EXAMPLE-NT\\doe-j",
        "cmdline": "program.exe",
        "hostname__": "MR11111",
        "signatures": "45%",
        "uid": "64a2fa85-0852-4745-81d6-0815eb2d5248;windows;MR11111;example.org",
        "tag": "TRI_AAA_WIN",
        "pid": 3920,
        "id": 777777777
    }
    ```



