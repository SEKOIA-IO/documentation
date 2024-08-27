
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_event_1"


    ```json
	{
        "temporary_id": "11111111111111",
        "affects_rating": true,
        "details": {
            "cvss": {
                "base": []
            },
            "check_pass": "",
            "diligence_annotations": {
                "modal_data": {
                    "type": "overridden",
                    "reason": "Software version in extended support"
                },
                "modal_tags": {
                    "Type": "MS IIS",
                    "Version": "7.5"
                },
                "server": "MS IIS",
                "version": "7.5"
            },
            "geo_ip_location": "test",
            "country": "test country",
            "grade": "BAD",
            "observed_ips": [
                "1.2.3.4"
            ],
            "port_list": [
                80,
                81,
                8443,
                8880
            ],
            "remediations": [
                {
                    "message": "Software version in extended support",
                    "help_text": "The software version is outside mainstream support and is currently in extended support.",
                    "remediation_tip": "Ensure the latest version of the software is installed. See <a href=\"https://help.bitsight.com/hc/en-us/articles/360010346733-Supported-Server-Software\">supported versions</a>."
                }
            ],
            "sample_timestamp": "2024-06-29T21:02:18Z",
            "dest_port": 80,
            "rollup_end_date": "2024-06-29",
            "rollup_start_date": "2023-10-04",
            "searchable_details": "Software version in extended support,MS IIS,7.5"
        },
        "evidence_key": "1.2.3.4",
        "first_seen": "2023-10-04",
        "last_seen": "2024-06-29",
        "related_findings": [],
        "risk_category": "Diligence",
        "risk_vector": "server_software",
        "risk_vector_label": "Server Software",
        "rolledup_observation_id": "11111111111",
        "severity": 8.0,
        "severity_category": "material",
        "tags": [],
        "remediation_history": {
            "last_requested_refresh_date": null,
            "last_refresh_status_date": null,
            "last_refresh_status_label": null,
            "last_refresh_reason_code": null
        },
        "asset_overrides": [],
        "duration": null,
        "comments": "User from Test, Inc. said: \"Test assignments\" at 2023-11-28 12:27 UTC",
        "remaining_decay": 57,
        "remediated": null,
        "impacts_risk_vector_details": "AFFECTS_RATING",
        "company_uuid": "111111111111111",
        "asset": {
            "asset": "1.2.3.4",
            "identifier": null,
            "category": "critical",
            "importance": 0.49,
            "is_ip": true,
            "asset_type": "IP"
        }
    }
    ```



=== "test_event_2"


    ```json
	{
        "temporary_id": "11111111111111111",
        "affects_rating": true,
        "details": {
            "cvss": {
                "base": []
            },
            "check_pass": "",
            "diligence_annotations": {
                "message": "Detected service: HTTP",
                "CPE": [
                    "a:amazon:amazon_cloudfront"
                ],
                "Tags": [],
                "Product": "CloudFront httpd",
                "Title": "ERROR: The request could not be satisfied",
                "transport": "tcp",
                "Status": "HTTP/1.1 400 Bad Request",
                "Server": "CloudFront"
            },
            "final_location": "http://1.2.3.4:12/",
            "geo_ip_location": "Location",
            "country": "Country",
            "grade": "NEUTRAL",
            "remediations": [
                {
                    "message": "Detected service: HTTP",
                    "help_text": "This port was observed running HTTP, which used for sending and receiving Internet traffic.",
                    "remediation_tip": ""
                }
            ],
            "sample_timestamp": "2024-06-29T08:37:25Z",
            "dest_port": 443,
            "rollup_end_date": "2024-06-29",
            "rollup_start_date": "2024-02-13",
            "searchable_details": "Detected service: HTTP,tcp,CloudFront httpd"
        },
        "evidence_key": "143.204.213.175:443",
        "first_seen": "2024-02-13",
        "last_seen": "2024-06-29",
        "related_findings": [],
        "risk_category": "Diligence",
        "risk_vector": "open_ports",
        "risk_vector_label": "Open Ports",
        "rolledup_observation_id": "1222222222222",
        "severity": 1.0,
        "severity_category": "minor",
        "tags": [],
        "remediation_history": {
            "last_requested_refresh_date": null,
            "last_refresh_status_date": null,
            "last_refresh_status_label": null,
            "last_refresh_reason_code": null
        },
        "asset_overrides": [],
        "duration": null,
        "comments": null,
        "remaining_decay": 57,
        "remediated": null,
        "impacts_risk_vector_details": "AFFECTS_RATING",
        "company_uuid": "1111111111111111111111111111",
        "asset": {
            "asset": "1.2.3.4",
            "identifier": null,
            "category": "low",
            "importance": 0.0,
            "is_ip": true,
            "asset_type": "IP"
        }
    }
    ```



=== "test_event_3"


    ```json
	{
        "temporary_id": "11111111111111",
        "affects_rating": true,
        "details": {
            "cvss": {
                "base": []
            },
            "check_pass": "",
            "diligence_annotations": {
                "message": "Allows insecure protocol: TLSv1.0, Allows insecure protocol: TLSv1.1",
                "certchain": [
                    {
                        "dnsName": [
                            "*.test.test",
                            "test.test"
                        ],
                        "endDate": "2025-05-15 23:59:59",
                        "issuerName": "C=TestC,O=TestO,CN=TestCN RSA Domain Validation Secure Server CA 3",
                        "keyAlgorithm": "RSA",
                        "keyLength": 2048,
                        "serialNumber": "111111111111111111111111",
                        "signatureAlgorithm": "SHA384WITHRSA",
                        "startDate": "2024-05-07 00:00:00",
                        "subjectName": "CN=*.test.test"
                    },
                    {
                        "dnsName": [],
                        "endDate": "2033-08-01 23:59:59",
                        "issuerName": "C=TestC,ST=TestST,L=TestL,O=TestO,CN=TestCN RSA Certification Authority",
                        "keyAlgorithm": "RSA",
                        "keyLength": 3072,
                        "serialNumber": "1111111111111111111111111111",
                        "signatureAlgorithm": "SHA384WITHRSA",
                        "startDate": "2023-08-02 00:00:00",
                        "subjectName": "C=TestC,O=TestO,CN=TestCN RSA Domain Validation Secure Server CA 3"
                    }
                ]
            },
            "final_location": "https://1.2.3.4/",
            "geo_ip_location": "Test",
            "country": "Test country",
            "grade": "BAD",
            "observed_ips": [
                "1.2.3.4:443"
            ],
            "remediations": [
                {
                    "message": "Allows insecure protocol: TLSv1.0",
                    "help_text": "TLS version 1.0 has been deprecated.",
                    "remediation_tip": "Disable TLS 1.0. See our <a href=\"https://help.bitsight.com/hc/en-us/articles/9176707227031-TLS-SSL-Finding-Remediation-Remediation-Verification\">guide for remediating TLS/SSL Configuration findings</a>."
                },
                {
                    "message": "Allows insecure protocol: TLSv1.1",
                    "help_text": "TLS version 1.1 has been deprecated.",
                    "remediation_tip": "Disable TLS 1.1. See our <a href=\"https://help.bitsight.com/hc/en-us/articles/9176707227031-TLS-SSL-Finding-Remediation-Remediation-Verification\">guide on verifying TLS is disabled</a>."
                }
            ],
            "sample_timestamp": "2024-06-29T00:49:11Z",
            "dest_port": 443,
            "rollup_end_date": "2024-06-29",
            "rollup_start_date": "2024-06-20",
            "searchable_details": "test details"
        },
        "evidence_key": "18.134.200.62:443",
        "first_seen": "2024-06-20",
        "last_seen": "2024-06-29",
        "related_findings": [],
        "risk_category": "Diligence",
        "risk_vector": "ssl_configurations",
        "risk_vector_label": "SSL Configurations",
        "rolledup_observation_id": "122222222222222222",
        "severity": 10.0,
        "severity_category": "severe",
        "tags": [],
        "remediation_history": {
            "last_requested_refresh_date": null,
            "last_refresh_status_date": null,
            "last_refresh_status_label": null,
            "last_refresh_reason_code": null
        },
        "asset_overrides": [],
        "duration": null,
        "comments": null,
        "remaining_decay": 57,
        "remediated": null,
        "impacts_risk_vector_details": "AFFECTS_RATING",
        "company_uuid": "11111111111111111111111111111",
        "asset": {
            "asset": "1.2.3.4",
            "identifier": null,
            "category": "low",
            "importance": 0.0,
            "is_ip": true,
            "asset_type": "IP"
        }
    }
    ```



=== "test_event_4"


    ```json
	{
        "temporary_id": "11111111111111111111111111111111",
        "affects_rating": true,
        "details": {
            "cvss": {
                "base": []
            },
            "check_pass": "",
            "diligence_annotations": {
                "message": "Detected service: HTTPS",
                "CPE": [
                    "cpe:2.3:o:microsoft:windows:-:*:*:*:*:*:*:*"
                ],
                "Tags": [],
                "Title": "Service",
                "transport": "tcp",
                "Status": "HTTP/1.1 200 OK",
                "Server": "Microsoft-HTTPAPI/2.0"
            },
            "final_location": "https://1.2.3.4:8086/",
            "geo_ip_location": "Test",
            "country": "TestCountry",
            "grade": "GOOD",
            "remediations": [
                {
                    "message": "Detected service: HTTPS",
                    "help_text": "This port was observed running Hypertext Transfer Protocol Secure (HTTPS), which is used for sending and receiving secure internet traffic.",
                    "remediation_tip": ""
                }
            ],
            "sample_timestamp": "2024-06-29T11:52:03Z",
            "dest_port": 8086,
            "rollup_end_date": "2024-06-29",
            "rollup_start_date": "2023-05-13",
            "searchable_details": "Detected service: HTTPS,tcp"
        },
        "evidence_key": "1.2.3.4:8086",
        "first_seen": "2023-05-13",
        "last_seen": "2024-06-29",
        "related_findings": [],
        "risk_category": "Diligence",
        "risk_vector": "open_ports",
        "risk_vector_label": "Open Ports",
        "rolledup_observation_id": "1123123123123123123",
        "severity": 1.0,
        "severity_category": "minor",
        "tags": [],
        "remediation_history": {
            "last_requested_refresh_date": null,
            "last_refresh_status_date": null,
            "last_refresh_status_label": null,
            "last_refresh_reason_code": null
        },
        "asset_overrides": [],
        "duration": null,
        "comments": null,
        "remaining_decay": 57,
        "remediated": null,
        "impacts_risk_vector_details": "AFFECTS_RATING",
        "company_uuid": "1111111111111111111111111",
        "asset": {
            "asset": "1.2.3.4",
            "identifier": null,
            "category": "low",
            "importance": 0.0,
            "is_ip": true,
            "asset_type": "IP"
        }
    }
    ```



=== "test_event_domain"


    ```json
	{
        "temporary_id": "1111111111111111111111111111111111111111111111111111&",
        "affects_rating": false,
        "asset": {
            "asset": "1.2.3.4",
            "identifier": null,
            "category": "low",
            "importance": 0,
            "is_ip": true,
            "asset_type": "Domain"
        },
        "vulnerability": {
            "name": "CVE-2014-3566",
            "alias": "POODLE",
            "display_name": "POODLE",
            "description": "The SSLv3 protocol, as used in OpenSSL through 1.0.1i and other products, makes it easier for Man-in-the-middle (MITM) attackers to obtain cleartext data via a padding-oracle attack (a.k.a. POODLE).",
            "remediation_tip": "Ensure all of your TLS/SSL libraries on the affected machines are up-to-date. Disable SSLv3 support on those servers, as described in <a target=\"new\" href=\"https://disablessl3.com/\">Disable SSLv3</a>.",
            "confidence": "HIGH",
            "cvss": {
                "base": 3.4
            },
            "severity": "Minor"
        },
        "company_uuid": "399e55d6-eab2-438d-84cd-fb0d0b967fcd",
        "details": {
            "cvss": {
                "base": [
                    3.4
                ]
            },
            "check_pass": "",
            "diligence_annotations": {
                "remediation_dates": [
                    {
                        "first": "2022-08-14 21:04:42",
                        "last": "2022-08-14 21:04:42"
                    }
                ],
                "is_remediated": true
            },
            "remediations": [
                {
                    "message": "CVE-2014-3566 (POODLE)",
                    "help_text": "The SSLv3 protocol, as used in OpenSSL through 1.0.1i and other products, makes it easier for Man-in-the-middle (MITM) attackers to obtain cleartext data via a padding-oracle attack (a.k.a. POODLE).",
                    "remediation_tip": "Ensure all of your TLS/SSL libraries on the affected machines are up-to-date. Disable SSLv3 support on those servers, as described in <a target=\"new\" href=\"https://disablessl3.com/\">Disable SSLv3</a>."
                }
            ],
            "rollup_end_date": "2022-08-14",
            "rollup_start_date": "2022-08-14",
            "searchable_details": "CVE-2014-3566"
        },
        "evidence_key": "1.2.3.4:443",
        "first_seen": "2022-08-14",
        "last_seen": "2022-08-14",
        "related_findings": [],
        "risk_category": "Diligence",
        "risk_vector": "patching_cadence",
        "risk_vector_label": "Patching Cadence",
        "rolledup_observation_id": "ZxFoXXsV3gvZS0t0oTmxcA==",
        "severity": 4.3,
        "severity_category": "moderate",
        "tags": [],
        "remediation_history": {
            "last_requested_refresh_date": null,
            "last_refresh_status_date": null,
            "last_refresh_status_label": null,
            "last_refresh_reason_code": null
        },
        "asset_overrides": [],
        "duration": "1 day",
        "comments": null,
        "remaining_decay": null,
        "remediated": true,
        "impacts_risk_vector_details": "LIFETIME_EXPIRED"
    }
    ```



=== "test_event_ip"


    ```json
	{
        "temporary_id": "1111111111111111111111111111111111111111111111111111&",
        "affects_rating": false,
        "asset": {
            "asset": "1.2.3.4",
            "identifier": null,
            "category": "low",
            "importance": 0,
            "is_ip": true,
            "asset_type": "IP"
        },
        "vulnerability": {
            "name": "CVE-2014-3566",
            "alias": "POODLE",
            "display_name": "POODLE",
            "description": "The SSLv3 protocol, as used in OpenSSL through 1.0.1i and other products, makes it easier for Man-in-the-middle (MITM) attackers to obtain cleartext data via a padding-oracle attack (a.k.a. POODLE).",
            "remediation_tip": "Ensure all of your TLS/SSL libraries on the affected machines are up-to-date. Disable SSLv3 support on those servers, as described in <a target=\"new\" href=\"https://disablessl3.com/\">Disable SSLv3</a>.",
            "confidence": "HIGH",
            "cvss": {
                "base": 3.4
            },
            "severity": "Minor"
        },
        "company_uuid": "399e55d6-eab2-438d-84cd-fb0d0b967fcd",
        "details": {
            "cvss": {
                "base": [
                    3.4
                ]
            },
            "check_pass": "",
            "diligence_annotations": {
                "remediation_dates": [
                    {
                        "first": "2022-08-14 21:04:42",
                        "last": "2022-08-14 21:04:42"
                    }
                ],
                "is_remediated": true
            },
            "remediations": [
                {
                    "message": "CVE-2014-3566 (POODLE)",
                    "help_text": "The SSLv3 protocol, as used in OpenSSL through 1.0.1i and other products, makes it easier for Man-in-the-middle (MITM) attackers to obtain cleartext data via a padding-oracle attack (a.k.a. POODLE).",
                    "remediation_tip": "Ensure all of your TLS/SSL libraries on the affected machines are up-to-date. Disable SSLv3 support on those servers, as described in <a target=\"new\" href=\"https://disablessl3.com/\">Disable SSLv3</a>."
                }
            ],
            "rollup_end_date": "2022-08-14",
            "rollup_start_date": "2022-08-14",
            "searchable_details": "CVE-2014-3566"
        },
        "evidence_key": "1.2.3.4:443",
        "first_seen": "2022-08-14",
        "last_seen": "2022-08-14",
        "related_findings": [],
        "risk_category": "Diligence",
        "risk_vector": "patching_cadence",
        "risk_vector_label": "Patching Cadence",
        "rolledup_observation_id": "ZxFoXXsV3gvZS0t0oTmxcA==",
        "severity": 4.3,
        "severity_category": "moderate",
        "tags": [],
        "remediation_history": {
            "last_requested_refresh_date": null,
            "last_refresh_status_date": null,
            "last_refresh_status_label": null,
            "last_refresh_reason_code": null
        },
        "asset_overrides": [],
        "duration": "1 day",
        "comments": null,
        "remaining_decay": null,
        "remediated": true,
        "impacts_risk_vector_details": "LIFETIME_EXPIRED"
    }
    ```



