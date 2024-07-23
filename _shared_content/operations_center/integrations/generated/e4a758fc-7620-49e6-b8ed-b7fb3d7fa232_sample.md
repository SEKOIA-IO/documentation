
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "action_overdict"


    ```json
	{
        "id": "abcdefgh",
        "date": "2024-01-31T10:11:13.974Z",
        "sender_ip": "1.2.3.4",
        "from": "user@test.fr",
        "from_header": "user user@test.fr",
        "to": "destuser@test.fr",
        "to_header": "header stuff",
        "subject": "subject",
        "message_id": "ABCDEF",
        "urls": [
            {
                "url": "https://www.test.com/"
            },
            {
                "url": "http://www.test.fr"
            },
            {
                "url": "https://www.test.io"
            }
        ],
        "attachments": [
            {
                "id": "abcdef",
                "filename": "image006.png",
                "extension": "png",
                "size": 477,
                "hashes": {
                    "md5": "abcdef",
                    "sha1": "abcdef",
                    "sha256": "abcdef",
                    "sha512": "abcdef"
                }
            },
            {
                "id": "abcdef",
                "filename": "sample.pdf",
                "extension": "pdf",
                "size": 237284,
                "hashes": {
                    "md5": "abcdef",
                    "sha1": "abcdef",
                    "sha256": "abcdef",
                    "sha512": "abcdef"
                }
            }
        ],
        "status": "LOW_SPAM",
        "substatus": "",
        "last_report": "none",
        "last_report_date": "0001-01-01T00:00:00Z",
        "remediation_type": "none",
        "remediation_ids": [],
        "action": "NOTHING",
        "folder": "",
        "size": 460793,
        "current_events": [],
        "whitelisted": true,
        "direction": "incoming",
        "remediation_message_read": false,
        "geo": {
            "country_name": "Ireland",
            "country_iso_code": "IE",
            "city_name": "Dublin"
        },
        "malware_bypass": false,
        "reply_to_header": "",
        "overdict": "clean",
        "auth_results_details": ""
    }
    ```



=== "email"


    ```json
	{
        "id": "zekfnzejnf576rge8768",
        "date": "2022-02-10T13:00:05.454Z",
        "sender_ip": "192.168.1.1",
        "from": "test@sekoia.io",
        "from_header": "<test@sekoia.io>",
        "to": "test@vadesecure.com",
        "to_header": "\"test@vadesecure.com\" <test@vadesecure.com>",
        "subject": "Lorem ipsum dolor",
        "message_id": "<01de2305-f75b-49db-8c61-f661bd498e63.protection.outlook.com>",
        "urls": [
            {
                "url": "https://sekoia.io"
            }
        ],
        "attachments": [
            {
                "id": "ca9ph2ostndl7735uht0",
                "filename": "image001.png",
                "extension": "png",
                "size": 12894
            },
            {
                "id": "ca9okt0kn1e8usdf633g",
                "filename": "archive.zip",
                "extension": "zip",
                "size": 10558
            }
        ],
        "status": "LEGIT",
        "substatus": "",
        "remediation_type": "none",
        "remediation_ids": [],
        "action": "NOTHING",
        "folder": "",
        "size": 113475,
        "current_events": [],
        "whitelisted": false
    }
    ```



=== "email_action_move"


    ```json
	{
        "id": "ch34aoqub3glupige13g",
        "date": "2023-04-24T09:01:23.666Z",
        "sender_ip": "163.172.240.104",
        "from": "test@sekoia.io",
        "from_header": "Test SEKOIA.IO <test@sekoia.io>",
        "to": "test@vadesecure.com",
        "to_header": "\"test@vadesecure.com\" <test@vadesecure.com>",
        "subject": "OneDrive- Document No.: 1928578 - VadeSecure",
        "message_id": "<5b13d2f4-6078-4ae6-afa9-0d023b89e85a@MR2FRA01FT001.eop-fra01.prod.protection.outlook.com>",
        "urls": [
            {
                "url": "https://www.facebo\u1ecdk.com/login.php"
            },
            {
                "url": "https://www.facelbo?k.com/login.php"
            },
            {
                "url": "https://www.vadesecure.com/"
            },
            {
                "url": "https://sites.google.com/view/gine-office/home"
            }
        ],
        "attachments": [
            {
                "id": "ch34aoqub3glupige170",
                "filename": "",
                "extension": "",
                "size": 10558,
                "hashes": {
                    "md5": "7bc2b146a309acbff2da55e6b4124a82",
                    "sha1": "299d5bf95adb52e640f9723c5f58b5a8e880be9b",
                    "sha256": "288093f2981e53222135c94d1d6179a069d6e539daa86f10d65f86958f793368",
                    "sha512": "7808b91ddf218cd9da382d42b2c5d07816964019976550f69aefe26182f6c324a5df8bafc9cd79167e09d4a339cfd33d5e7ba87342f459aae8e125fc64d42423"
                }
            },
            {
                "id": "ch34aoqub3glupige17g",
                "filename": "",
                "extension": "",
                "size": 12894,
                "hashes": {
                    "md5": "0eb4a83f99c2cd38d9d4decf809d1701",
                    "sha1": "4665fcc8f1433dda8cd62d1234ead5ee32d4dd5f",
                    "sha256": "f1e1783333718e2c937d7c694dacd518ccca9f219b31fbfda40e72ee16235dae",
                    "sha512": "c6c817094c207e2d7bd12803a875bda79274fbac1c745a81dbd886d25c4147f179209073425a2e8b2f800ec3415376ef38eab64680ecb16ba9820ecde4ea8156"
                }
            }
        ],
        "status": "PHISHING",
        "substatus": "",
        "last_report": "none",
        "last_report_date": "0001-01-01T00:00:00Z",
        "remediation_type": "none",
        "remediation_ids": [],
        "action": "MOVE",
        "folder": "JunkEmail",
        "size": 186849,
        "current_events": [],
        "whitelisted": false,
        "geo": {
            "country_name": "France",
            "country_iso_code": "FR",
            "city_name": ""
        },
        "malware_bypass": false
    }
    ```



=== "email_with_attachment"


    ```json
	{
        "id": "cgrqlp83v5prkopmecf0",
        "date": "2023-04-13T07:10:29.191Z",
        "sender_ip": "163.172.240.104",
        "from": "test@sekoia.io",
        "from_header": "Test SEKOIA.IO <test@sekoia.io>",
        "to": "test@vadesecure.com",
        "to_header": "\"test@vadesecure.com\" <test@vadesecure.com>",
        "subject": "Lorem ipsum dolor",
        "message_id": "<d0a5da95-4028-439b-b9d5-a4f220c59022@protection.outlook.com>",
        "urls": [],
        "attachments": [
            {
                "id": "cgrqlp83v5prkopmecfg",
                "filename": "commande.docm",
                "extension": "docm",
                "size": 96009,
                "hashes": {
                    "md5": "c1ea14accbb4f5ac66beac2d3f8de531",
                    "sha1": "bfd1de0e780a3d7f047f6de00f44eaa1868e05e2",
                    "sha256": "6ea92f15f697ef4c78ca02fd3d72b2531f047be00a588901b3d14578ccbd9424",
                    "sha512": "77eec978ebbc455892fbce3dafe78140962c6c25a8050a9c9f0155b27ff1a08588cbf74bb41df49c1413431d307f099547354eabb7e5f23a798192a3c673749d"
                }
            }
        ],
        "status": "LEGIT",
        "substatus": "",
        "last_report": "none",
        "last_report_date": "0001-01-01T00:00:00Z",
        "remediation_type": "none",
        "remediation_ids": [],
        "action": "NOTHING",
        "folder": "",
        "size": 179355,
        "current_events": [],
        "whitelisted": true,
        "geo": {
            "country_name": "France",
            "country_iso_code": "FR",
            "city_name": ""
        },
        "malware_bypass": true
    }
    ```



=== "remediation_auto"


    ```json
	{
        "id": "zekfnzejnf576rge8768",
        "date": "2022-02-01T23:30:33.982Z",
        "reason": "The email contains a URL that is flagged as Phishing by Vade Secure Global Threat Intelligence",
        "status": {
            "status": "PHISHING"
        },
        "actions": [
            {
                "action": "MOVE"
            }
        ],
        "nb_messages_remediated": 1,
        "nb_messages_remediated_read": 0,
        "nb_messages_remediated_unread": 1
    }
    ```



=== "remediation_manual"


    ```json
	{
        "id": "zekfnzejnf576rge8768",
        "date": "2021-11-18T15:59:39.368Z",
        "reason": "",
        "actions": [
            {
                "action": "DELETE"
            },
            {
                "action": "FAILED"
            }
        ],
        "nb_messages_remediated": 76,
        "nb_messages_remediated_read": 0,
        "nb_messages_remediated_unread": 76
    }
    ```



