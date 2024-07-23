
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_blocked_file"


    ```json
	{
        "AccountID": "1d1e650b3385b95db72bba7cfb1287e9",
        "Action": "block",
        "BlockedFileHash": "7accd179e8a6b2fc907e7e8d087c52a7f48084852724b03d25bebcada1acbca5",
        "BlockedFileName": "",
        "BlockedFileReason": "avscan",
        "BlockedFileSize": 0,
        "BlockedFileType": "",
        "Datetime": "2023-05-02T12:43:26Z",
        "DestinationIP": "185.199.109.133",
        "DestinationPort": 443,
        "DeviceID": "b72ac397-e5c3-913e-11ed-03face9f2b6b",
        "DeviceName": "DESKTOP-ABCDEF",
        "DownloadedFileNames": [
            "mimikatz_trunk.zip"
        ],
        "Email": "john.doe@test.com",
        "FileInfo": {
            "files": [
                {
                    "direction": "download",
                    "file_name": "mimikatz_trunk.zip",
                    "file_size": 0,
                    "content_type": "application/octet-stream",
                    "action": "none"
                }
            ]
        },
        "HTTPHost": "objects.githubusercontent.com",
        "HTTPMethod": "GET",
        "HTTPStatusCode": 200,
        "HTTPVersion": "HTTP/2",
        "IsIsolated": false,
        "PolicyID": "",
        "PolicyName": "",
        "Referer": "https://github.com/gentilkiwi/mimikatz/releases",
        "RequestID": "184ee7e16800003d0d86472000000001",
        "SourceIP": "15.188.186.81",
        "SourceInternalIP": "",
        "SourcePort": 49907,
        "URL": "https://objects.githubusercontent.com/github-production-release-asset-2e65be/18496166/28e3acb5-ca66-40d5-bc68-f76f5bfabecf?X-Amz-Algorithm=AWS4-HMAC-SHA256&response-content-disposition=attachment%3B%20filename%3Dmimikatz_trunk.zip",
        "UntrustedCertificateAction": "none",
        "UploadedFileNames": [],
        "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64",
        "UserID": "2c46cdd9-92e3-5e5f-b3cf-67965d7c33e3"
    }
    ```



=== "test_http"


    ```json
	{
        "AccountID": "1d1e650b3385b95db72bba7cfb1287e9",
        "Action": "allow",
        "BlockedFileHash": "",
        "BlockedFileName": "",
        "BlockedFileReason": "unknown",
        "BlockedFileSize": 0,
        "BlockedFileType": "",
        "Datetime": "2023-02-24T16:32:58Z",
        "DestinationIP": "",
        "DestinationPort": 0,
        "DeviceID": "",
        "DeviceName": "",
        "DownloadedFileNames": [
            "<unknown file name>"
        ],
        "Email": "",
        "FileInfo": {
            "files": []
        },
        "HTTPHost": "www.facebook.com",
        "HTTPMethod": "GET",
        "HTTPVersion": "HTTP/2",
        "IsIsolated": false,
        "PolicyID": "",
        "PolicyName": "",
        "Referer": "",
        "RequestID": "1725de5f0b000021551771e400000001",
        "SourceIP": "15.188.186.81",
        "SourcePort": 39998,
        "URL": "https://www.facebook.com/",
        "UntrustedCertificateAction": "none",
        "UploadedFileNames": [],
        "UserAgent": "curl/7.81.0",
        "UserID": ""
    }
    ```



