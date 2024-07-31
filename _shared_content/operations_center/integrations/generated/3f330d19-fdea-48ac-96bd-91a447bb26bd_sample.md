
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "event_application_blocked"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::Application::Blocked",
        "endpoint_type": "computer",
        "endpoint_id": "5da7691b-cc01-4330-bb8b-358362c3a5f1",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "Controlled application blocked: Google Software Reporter Tool (Security tool)",
        "id": "bc60c18b-dc21-43a3-bfd5-f28963f288e2",
        "group": "APPLICATION_CONTROL",
        "datastream": "event",
        "end": "2022-04-25T03:15:31.760Z",
        "suser": "n/a",
        "rt": "2022-04-25T03:15:31.777Z",
        "dhost": "DOMAIN-1234"
    }
    ```



=== "event_disk_non_encrypted"


    ```json
	{
        "severity": "medium",
        "type": "Event::Endpoint::Enc::DiskNotEncryptedEvent",
        "name": "Device is not encrypted.",
        "id": "f7c7e65a-a452-429c-9e0a-cdc16c5b50e9",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "endpoint_id": "92d4ef41-9c13-4041-bbed-952011796812",
        "endpoint_type": "computer",
        "group": "DENC",
        "datastream": "event",
        "end": "2022-04-27T13:23:07.981Z",
        "dhost": "DESKTOP-1234",
        "rt": "2022-04-27T13:24:08.662Z",
        "duid": "574fcff42ead810f5e43b0fc",
        "suser": "Elon Musk"
    }
    ```



=== "event_dlp_allowed"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::DataLossPreventionAutomaticallyAllowed",
        "endpoint_type": "computer",
        "endpoint_id": "5da7691b-cc01-4330-bb8b-358362c3a5f1",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "An \u2033allow file transfer\u2033 action was taken.  Username: DDDDD\\XXXXXXXXXX  Rule names: \u2032Multimedia file\u2032  User action: File open  Application Name: Firefox (V7 and higher)  Data Control action: Allow  File type: Media Container (TFT\u2215MPEG-4)  File size: 559316722  Source path: C:\\Users\\XXXXXXXX\\Downloads\\YYYYYYYYYYYYYYYYY.mp4",
        "id": "bc60c18b-dc21-43a3-bfd5-f28963f288e2",
        "group": "DATA_LOSS_PREVENTION",
        "datastream": "event",
        "end": "2022-04-25T03:15:31.760Z",
        "suser": "n/a",
        "rt": "2022-04-25T03:15:31.777Z",
        "dhost": "DOMAIN-1234"
    }
    ```



=== "event_dlp_allowed_remote_storage"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::DataLossPreventionAutomaticallyAllowed",
        "endpoint_type": "computer",
        "endpoint_id": "5da7691b-cc01-4330-bb8b-358362c3a5f1",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "An \u2033allow file transfer\u2033 action was taken.  Username: DDDDD\\XXXXXXXXXX  Rule names: \u2032Multimedia file\u2032  User action: File open  Application Name: Firefox (V7 and higher)  Data Control action: Allow  File type: Media Container (TFT\u2215MPEG-4)  File size: 559316722  Source path: C:\\Users\\XXXXXXXX\\Downloads\\YYYYYYYYYYYYYYYYY.mp4  Destination path: D:\\XXXXXXXXXXXXXXX\\Documents\\Videos\\YYYYY.mp4  Destination type: Removable storage",
        "id": "bc60c18b-dc21-43a3-bfd5-f28963f288e2",
        "group": "DATA_LOSS_PREVENTION",
        "datastream": "event",
        "end": "2022-04-25T03:15:31.760Z",
        "suser": "n/a",
        "rt": "2022-04-25T03:15:31.777Z",
        "dhost": "DOMAIN-1234"
    }
    ```



=== "event_encryption_information"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::Enc::DiskEncryptionInformation",
        "name": "Device Encryption information for volume with id: 63E6153A-3663-44E1-A200-F1CD4CB9EBCE. Message: Encryption has been postponed.",
        "id": "55726d81-213b-43b6-be18-48dee3add6f8",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "c0e1e239-8912-4cc9-a6ed-245a964dec10",
        "endpoint_id": "92d4ef41-9c13-4041-bbed-952011796812",
        "endpoint_type": "computer",
        "group": "DENC",
        "datastream": "event",
        "end": "2022-04-27T08:48:48.808Z",
        "dhost": "DESKTOP-1234",
        "rt": "2022-04-27T08:48:48.809Z",
        "duid": "62690353b62561118508746f",
        "suser": "TESLA\\user"
    }
    ```



=== "event_encryption_suspended"


    ```json
	{
        "severity": "medium",
        "type": "Event::Endpoint::Denc::EncryptionSuspendedEvent",
        "name": "Device Encryption is suspended",
        "id": "80130549-e09e-46d3-ab98-919fbd625884",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "endpoint_id": "92d4ef41-9c13-4041-bbed-952011796812",
        "endpoint_type": "computer",
        "group": "DENC",
        "datastream": "event",
        "end": "2022-04-27T08:47:16.490Z",
        "dhost": "DESKTOP-1234",
        "rt": "2022-04-27T08:48:19.320Z",
        "duid": "624aabf253f2e60fda590556",
        "suser": "TESLA\\admin"
    }
    ```



=== "event_exploit_prevention"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::HmpaExploitPrevented",
        "endpoint_type": "computer",
        "endpoint_id": "5da7691b-cc01-4330-bb8b-358362c3a5f1",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "'CodeCave' exploit prevented in Essential Objects Worker Process",
        "id": "bc60c18b-dc21-43a3-bfd5-f28963f288e2",
        "group": "RUNTIME_DETECTIONS",
        "datastream": "event",
        "end": "2022-04-25T03:15:31.760Z",
        "suser": "n/a",
        "rt": "2022-04-25T03:15:31.777Z",
        "dhost": "DOMAIN-1234"
    }
    ```



=== "event_key_received"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::Enc::Recovery::KeyReceived",
        "name": "A BitLocker recovery key has been received from: DESKTOP-1234.",
        "id": "c8e0b5c9-69d0-4885-8964-5cefaa8ef13e",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "endpoint_id": "92d4ef41-9c13-4041-bbed-952011796812",
        "endpoint_type": "computer",
        "group": "DENC",
        "datastream": "event",
        "end": "2022-04-27T13:22:08.749Z",
        "dhost": "DESKTOP-1234",
        "rt": "2022-04-27T13:22:13.565Z",
        "duid": "574fcff42ead810f5e43b0fc",
        "suser": "admin tech"
    }
    ```



=== "event_outlook_plugin"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::Denc::OutlookPluginEnabledEvent",
        "name": "Outlook add-in is enabled",
        "id": "37d8c083-2342-4e88-9da6-4f47e3143c9d",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "endpoint_id": "92d4ef41-9c13-4041-bbed-952011796812",
        "endpoint_type": "computer",
        "group": "DENC",
        "datastream": "event",
        "end": "2022-04-27T13:22:06.909Z",
        "dhost": "DESKTOP-1234",
        "rt": "2022-04-27T13:22:13.226Z",
        "duid": "574fcff42ead810f5e43b0fc",
        "suser": "admin tech"
    }
    ```



=== "event_pua_detected"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::CorePuaDetection",
        "endpoint_type": "computer",
        "endpoint_id": "5da7691b-cc01-4330-bb8b-358362c3a5f1",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "PUA detected: 'Rule Generic PUA' at 'C:\\Users\\XXXXXXXXXX\\AppData\\Local\\Microsoft\\SquirrelTemp\\tempc'",
        "id": "bc60c18b-dc21-43a3-bfd5-f28963f288e2",
        "group": "PUA",
        "datastream": "event",
        "end": "2022-04-25T03:15:31.760Z",
        "suser": "n/a",
        "rt": "2022-04-25T03:15:31.777Z",
        "dhost": "DOMAIN-1234"
    }
    ```



=== "event_pua_detected_2"


    ```json
	{
        "appSha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "d9b11461-9678-4448-ab88-4b5211d2bf5e",
        "endpoint_id": "61092e0b-b6f5-46c5-b0a7-68ee3b2dc822",
        "endpoint_type": "computer",
        "threat": "Generic Reputation PUA",
        "origin": "ML",
        "type": "Event::Endpoint::CorePuaDetection",
        "id": "c39307f6-0c51-4a55-af23-f2ac7905416d",
        "group": "PUA",
        "rt": "2023-08-07T21:55:28.843Z",
        "severity": "medium",
        "duid": "63ed3118d043e176065be9ba",
        "end": "2023-08-07T21:55:27.508Z",
        "name": "PUA detected: 'Generic Reputation PUA' at 'C:\\Users\\John Doe\\Documents\\suspicious.zip'",
        "dhost": "LAPTOP-01",
        "suser": "LAPTOP-01\\John Doe"
    }
    ```



=== "event_registered"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::Registered",
        "name": "New computer registered: DESKTOP-1234",
        "id": "b3c9c053-6037-469d-9bee-49d39f7932d0",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "endpoint_id": "92d4ef41-9c13-4041-bbed-952011796812",
        "endpoint_type": "computer",
        "group": "PROTECTION",
        "datastream": "event",
        "end": "2022-04-27T13:17:10.188Z",
        "dhost": "DESKTOP-1234",
        "rt": "2022-04-27T13:17:10.197Z",
        "duid": "574fcff42ead810f5e43b0fc",
        "suser": "admin tech"
    }
    ```



=== "event_scan_complete"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::SavScanComplete",
        "name": "Scan 'Sophos Cloud Scheduled Scan' completed",
        "id": "fca84bd1-44df-4c30-ab79-103b971e714a",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "endpoint_id": "92d4ef41-9c13-4041-bbed-952011796812",
        "endpoint_type": "computer",
        "group": "PROTECTION",
        "datastream": "event",
        "end": "2022-04-27T08:59:59.000Z",
        "dhost": "DESKTOP-1234",
        "rt": "2022-04-27T09:00:03.548Z",
        "duid": "611cda48cf87290e90dfc1d1",
        "suser": "Elon Musk"
    }
    ```



=== "event_update_failure"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::UpdateFailure",
        "endpoint_type": "server",
        "endpoint_id": "350e274b-777f-4b67-b34b-10d17a6c6193",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "Download of WindowsCloudServer failed from server http:\u2215\u2215dci.sophosupd.com.",
        "id": "f68abcb6-c87f-46ae-a82a-7919bf313a66",
        "group": "UPDATING",
        "datastream": "event",
        "end": "2022-04-25T07:41:03.101Z",
        "suser": "n/a",
        "rt": "2022-04-25T07:41:03.118Z",
        "dhost": "DESKTOP-1234"
    }
    ```



=== "event_update_reboot_required"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::UpdateRebootRequired",
        "endpoint_type": "server",
        "endpoint_id": "5da7691b-cc01-4330-bb8b-358362c3a5f1",
        "source_info": {
            "ip": "1.2.3.4"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "Reboot to complete update; computer stays protected in the meantime",
        "id": "bc60c18b-dc21-43a3-bfd5-f28963f288e2",
        "group": "UPDATING",
        "datastream": "event",
        "end": "2022-04-25T03:15:31.760Z",
        "suser": "n/a",
        "rt": "2022-04-25T03:15:31.777Z",
        "dhost": "DOMAIN-1234"
    }
    ```



=== "event_update_success"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::UpdateSuccess",
        "endpoint_type": "server",
        "endpoint_id": "2ddff78e-27a1-40ff-8478-6c9be62e3b29",
        "source_info": {
            "ip": "4.5.6.7"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "Update succeeded",
        "id": "a4c6776e-2f47-4bea-b5b3-7f1914c03a70",
        "group": "UPDATING",
        "datastream": "event",
        "end": "2022-04-25T04:57:09.886Z",
        "suser": "n/a",
        "rt": "2022-04-25T04:57:09.900Z",
        "dhost": "ACLOUD-2K22"
    }
    ```



=== "event_user_auto_created"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::UserAutoCreated",
        "name": "New user added automatically: TESLA\\e.musk",
        "id": "1498e255-e9c1-4835-b0b9-8ae7b44ae6f7",
        "source_info": {
            "ip": "1.3.3.7"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "endpoint_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "endpoint_type": "computer",
        "group": "PROTECTION",
        "datastream": "event",
        "end": "2022-04-27T08:48:19.449Z",
        "dhost": "DESKTOP-1234",
        "rt": "2022-04-27T08:48:19.456Z",
        "duid": "62690353b62561118508746f",
        "suser": "TESLA\\e.musk"
    }
    ```



=== "event_webfiltering"


    ```json
	{
        "severity": "low",
        "type": "Event::Endpoint::WebFilteringBlocked",
        "endpoint_type": "computer",
        "endpoint_id": "3205420f-f05c-4f03-bb10-3ff6bf97b6ab",
        "source_info": {
            "ip": "1.3.3.7"
        },
        "customer_id": "36d5cd97-169e-490b-a2c4-bcd9d5d2a54b",
        "name": "Access was blocked to \"www.malicious-site.com\" because of \"Rulename\".",
        "id": "a91e11e2-1739-4f01-bf33-2dfd165e5ca3",
        "group": "WEB",
        "datastream": "event",
        "end": "2022-04-25T09:35:54.000Z",
        "suser": "Elon Musk",
        "rt": "2022-04-25T09:35:55.764Z",
        "duid": "615ff633eae9110e824c07b7",
        "dhost": "TESLA-SUPPORT"
    }
    ```



