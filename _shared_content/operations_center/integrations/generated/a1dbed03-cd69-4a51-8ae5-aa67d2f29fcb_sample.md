
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "admin_login"


    ```json
	{
        "initiated_by": {
            "id": "61e536ebdbbe784cb2e55fb5",
            "type": "admin",
            "email": "john.doe@sekoia.io"
        },
        "geoip": {
            "country_code": "FR",
            "timezone": "Europe/Paris",
            "latitude": 48.8323,
            "continent_code": "EU",
            "region_name": "Paris",
            "longitude": 2.4075,
            "region_code": "75"
        },
        "useragent": {
            "os": "Mac OS X",
            "minor": "0",
            "os_minor": "15",
            "os_version": "10.15.7",
            "os_major": "10",
            "version": "114.0.0.0",
            "os_patch": "7",
            "patch": "0",
            "os_full": "Mac OS X 10.15.7",
            "major": "114",
            "name": "Chrome",
            "os_name": "Mac OS X",
            "device": "Mac"
        },
        "mfa": true,
        "event_type": "admin_login_attempt",
        "provider": null,
        "service": "directory",
        "success": true,
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "1.2.3.4",
        "id": "648c6c758c2ac07fa1fdee94",
        "timestamp": "2023-06-16T14:06:45.921Z"
    }
    ```



=== "association_change"


    ```json
	{
        "initiated_by": {
            "id": "61e536ebdbbe784cb2e55fb5",
            "type": "admin",
            "email": "maurice.moss@sekoia.io"
        },
        "geoip": {
            "country_code": "FR",
            "timezone": "Europe/Paris",
            "latitude": 48.8323,
            "continent_code": "EU",
            "region_name": "Paris",
            "longitude": 2.4075,
            "region_code": "75"
        },
        "useragent": {
            "minor": "0",
            "os": "Mac OS X",
            "os_minor": "15",
            "os_version": "10.15.7",
            "os_major": "10",
            "version": "114.0.0.0",
            "os_patch": "7",
            "patch": "0",
            "os_full": "Mac OS X 10.15.7",
            "major": "114",
            "name": "Chrome",
            "os_name": "Mac OS X",
            "device": "Mac"
        },
        "association": {
            "op": "add",
            "action_source": "manual",
            "connection": {
                "from": {
                    "name": "JDOE-DESKTOP",
                    "type": "system",
                    "object_id": "6447f8a7caa17d71c56b2dca"
                },
                "to": {
                    "name": "john.doe",
                    "type": "user",
                    "object_id": "636b8c40f03d374a5c7f6ceb"
                }
            },
            "attributes": null
        },
        "auth_method": "session",
        "event_type": "association_change",
        "provider": null,
        "service": "directory",
        "success": true,
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "176.161.221.161",
        "id": "64930a6d00466f31842811a1",
        "timestamp": "2023-06-21T14:34:21.089Z"
    }
    ```



=== "radius_auth_failure"


    ```json
	{
        "error_message": "mschap: MS-CHAP2-Response is incorrect",
        "initiated_by": {
            "type": "user",
            "username": "john.doe"
        },
        "auth_type": "eap",
        "nas_mfa_state": "DISABLED",
        "geoip": {
            "country_code": "FR",
            "timezone": "Europe/Paris",
            "latitude": 48.8323,
            "continent_code": "EU",
            "region_name": "Paris",
            "region_code": "75",
            "longitude": 2.4075
        },
        "eap_type": "MSCHAPv2",
        "outer": {
            "error_message": "eap_peap: The users session was previously rejected: returning reject (again.), eap: Failed continuing EAP PEAP (25) session.  EAP sub-module failed: mschap: MS-CHAP2-Response is incorrect",
            "eap_type": "PEAP",
            "username": "john.doe"
        },
        "mfa": false,
        "auth_meta": {
            "user_password_enabled": true,
            "device_cert_enabled": false,
            "user_cert_enabled": false,
            "auth_idp": "JUMPCLOUD",
            "userid_type": "USERNAME"
        },
        "event_type": "radius_auth_attempt",
        "success": false,
        "service": "radius",
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "13.14.15.16",
        "id": "E5223E70-F3DB-3CB4-B452-96FC2259B9EE",
        "timestamp": "2023-06-15T15:16:41Z",
        "username": "john.doe"
    }
    ```



=== "radius_auth_success"


    ```json
	{
        "initiated_by": {
            "type": "user",
            "username": "jane.doe"
        },
        "auth_type": "eap",
        "nas_mfa_state": "DISABLED",
        "geoip": {
            "country_code": "US",
            "timezone": "America/New_York",
            "latitude": 42.3797,
            "continent_code": "NA",
            "region_name": "Massachusetts",
            "longitude": -71.1034,
            "region_code": "MA"
        },
        "eap_type": "MSCHAPv2",
        "outer": {
            "eap_type": "PEAP",
            "username": "jane.doe"
        },
        "mfa": false,
        "auth_meta": {
            "user_password_enabled": true,
            "device_cert_enabled": false,
            "user_cert_enabled": false,
            "auth_idp": "JUMPCLOUD",
            "userid_type": "USERNAME"
        },
        "event_type": "radius_auth_attempt",
        "service": "radius",
        "success": true,
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "20.21.22.23",
        "id": "842B7B84-FE16-32AF-B257-9D508FB22D22",
        "username": "jane.doe",
        "timestamp": "2023-06-15T15:17:41Z"
    }
    ```



=== "ssoauth_failure_1"


    ```json
	{
        "initiated_by": {
            "id": "619294e65bb5c23fb2b1ce09",
            "type": "user",
            "username": "jane.doe"
        },
        "error_message": "application unreachable",
        "geoip": {
            "country_code": "US",
            "timezone": "America/New_York",
            "latitude": 42.059,
            "continent_code": "NA",
            "region_name": "Massachusetts",
            "longitude": -71.1123,
            "region_code": "MA"
        },
        "sso_token_success": false,
        "useragent": {
            "minor": "0",
            "os": "Mac OS X",
            "os_minor": "15",
            "os_major": "10",
            "os_version": "10.15.7",
            "version": "114.0.0.0",
            "os_patch": "7",
            "patch": "0",
            "os_full": "Mac OS X 10.15.7",
            "major": "114",
            "name": "Chrome",
            "os_name": "Mac OS X",
            "device": "Mac"
        },
        "auth_context": {
            "system": {
                "hostname": "JDOE-LAPTOP",
                "os": "Mac OS X",
                "displayName": "JDOE-LAPTOP",
                "id": "61958333dd6a1b033f2b4b95",
                "version": "13.4"
            },
            "auth_methods": {}
        },
        "mfa": false,
        "event_type": "sso_auth",
        "application": {
            "display_label": "",
            "sso_type": "saml",
            "name": "",
            "id": "",
            "sso_url": "https://sso.jumpcloud.com/saml2/google"
        },
        "provider": "",
        "service": "sso",
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "5.6.7.8",
        "id": "648b1e56c0b7fd51eb1d0938",
        "idp_initiated": false,
        "timestamp": "2023-06-15T14:21:10.34334445Z"
    }
    ```



=== "ssoauth_failure_2"


    ```json
	{
        "initiated_by": {
            "id": "627e7e94c17c5a34e72b862a",
            "type": "user",
            "username": "john.doe"
        },
        "error_message": "not authorized",
        "geoip": {
            "country_code": "FR",
            "timezone": "Europe/Paris",
            "latitude": 48.8138,
            "continent_code": "EU",
            "region_name": "Val-de-Marne",
            "longitude": 2.3873,
            "region_code": "94"
        },
        "sso_token_success": false,
        "useragent": {
            "os": "Mac OS X",
            "minor": "0",
            "os_minor": "15",
            "os_major": "10",
            "os_version": "10.15.7",
            "version": "114.0.0.0",
            "os_patch": "7",
            "patch": "0",
            "os_full": "Mac OS X 10.15.7",
            "major": "114",
            "name": "Chrome",
            "os_name": "Mac OS X",
            "device": "Mac"
        },
        "auth_context": {
            "system": {
                "hostname": "JPABLO-MAC",
                "os": "Mac OS X",
                "displayName": "PCONTRERAS-MAC",
                "id": "627e7d26e05f2c61150b5905",
                "version": "13.4"
            },
            "auth_methods": {}
        },
        "mfa": false,
        "event_type": "sso_auth",
        "application": {
            "display_label": "Salesforce",
            "sso_type": "saml",
            "name": "salesforce",
            "id": "5fbfaa559753353c0b83ecc0",
            "sso_url": "https://sso.jumpcloud.com/saml2/google"
        },
        "provider": "",
        "service": "sso",
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "9.10.11.12",
        "id": "648b24c48eae32f4adabc27e",
        "idp_initiated": false,
        "timestamp": "2023-06-15T14:48:36.495420839Z"
    }
    ```



=== "ssoauth_success"


    ```json
	{
        "initiated_by": {
            "id": "611d175820c84b11c28262e2",
            "type": "user",
            "username": "john.doe"
        },
        "error_message": "",
        "geoip": {
            "country_code": "US",
            "timezone": "America/New_York",
            "latitude": 42.3364,
            "continent_code": "NA",
            "region_name": "Massachusetts",
            "region_code": "MA",
            "longitude": -71.0326
        },
        "sso_token_success": true,
        "auth_context": {
            "system": {
                "hostname": "JDOE-DEKSTOP",
                "os": "Mac OS X",
                "displayName": "JDOE-DEKSTOP",
                "id": "611eadd78e9ce015fc53eb28",
                "version": "13.4"
            },
            "auth_methods": {},
            "policies_applied": [
                {
                    "metadata": {
                        "resource_type": "APPLICATION",
                        "action": "ALLOW"
                    },
                    "name": "Global Policy",
                    "id": ""
                }
            ]
        },
        "useragent": {
            "os_full": "Mac OS X 10.15",
            "minor": "0",
            "os": "Mac OS X",
            "major": "114",
            "os_minor": "15",
            "os_major": "10",
            "os_version": "10.15",
            "name": "Firefox",
            "os_name": "Mac OS X",
            "device": "Mac",
            "version": "114.0"
        },
        "mfa": false,
        "event_type": "sso_auth",
        "application": {
            "display_label": "Google Workspace",
            "sso_type": "saml",
            "name": "google",
            "id": "60d05c1385450d17af70308f",
            "sso_url": "https://sso.jumpcloud.com/saml2/google"
        },
        "provider": "",
        "service": "sso",
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "1.2.3.4",
        "id": "648b16171f40f190e2945fc1",
        "idp_initiated": false,
        "timestamp": "2023-06-15T13:45:59.812449824Z"
    }
    ```



=== "user_update"


    ```json
	{
        "initiated_by": {
            "id": "603e0c284295c570a179ef4a",
            "type": "admin",
            "email": "maurice.moss@sekoia.io"
        },
        "geoip": {
            "country_code": "IE",
            "timezone": "Europe/Dublin",
            "latitude": 53.3379,
            "continent_code": "EU",
            "region_name": "Leinster",
            "region_code": "L",
            "longitude": -6.2591
        },
        "resource": {
            "id": "6127579ec58b6d6144c06492",
            "type": "user",
            "username": "jane.doe"
        },
        "useragent": {
            "os_full": "Other",
            "os": "Other",
            "name": "Other",
            "os_name": "Other",
            "device": "Other"
        },
        "changes": [
            {
                "field": "attributes",
                "from": [
                    {
                        "name": "Division",
                        "id": "648f9f5f293ab1deaf28fa84",
                        "_id": "648f9f5f293ab1deaf28fa84",
                        "value": "Marketing"
                    }
                ],
                "to": [
                    {
                        "name": "Division",
                        "id": "6490f0f5a2d539837a30aaa0",
                        "_id": "6490f0f5a2d539837a30aaa0",
                        "value": "Sales"
                    }
                ]
            }
        ],
        "auth_method": "api key",
        "event_type": "user_update",
        "provider": null,
        "service": "directory",
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "1.2.3.4",
        "id": "6490f0f5a2d539837a30aaad",
        "timestamp": "2023-06-20T00:21:09.162Z"
    }
    ```



=== "user_update2"


    ```json
	{
        "initiated_by": {
            "source": "scim",
            "id": "5bf6defbdcd8233029e0c599",
            "type": "admin",
            "email": "maurice.moss@sekoia.io"
        },
        "geoip": {
            "country_code": "IE",
            "timezone": "Europe/Dublin",
            "latitude": 53.3379,
            "continent_code": "EU",
            "region_name": "Leinster",
            "region_code": "L",
            "longitude": -6.2591
        },
        "resource": {
            "id": "627232d9c2bb20373d84eb63",
            "type": "user",
            "username": "jane.doe"
        },
        "useragent": {
            "patch": "0",
            "os_full": "Other",
            "minor": "68",
            "major": "7",
            "os": "Other",
            "name": "curl",
            "os_name": "Other",
            "device": "Other",
            "version": "7.68.0"
        },
        "changes": [
            {
                "field": "addresses",
                "from": [
                    {
                        "country": "FR",
                        "poBox": "",
                        "streetAddress": "",
                        "postalCode": "",
                        "locality": "",
                        "id": "63bfde6bce2d30b9e8a6cb4c",
                        "_id": "63bfde6bce2d30b9e8a6cb4c",
                        "region": "",
                        "extendedAddress": "",
                        "type": "home"
                    },
                    {
                        "country": "FR",
                        "poBox": "",
                        "streetAddress": "54 rue des Petites Ecuries",
                        "postalCode": "75010",
                        "locality": "Paris",
                        "id": "63bfde6bce2d30b9e8a6cb4d",
                        "_id": "63bfde6bce2d30b9e8a6cb4d",
                        "region": "",
                        "extendedAddress": "",
                        "type": "work"
                    }
                ],
                "to": [
                    {
                        "country": "FR",
                        "poBox": "",
                        "streetAddress": "",
                        "postalCode": "",
                        "locality": "",
                        "id": "64907cb6e968be7fe5b14d74",
                        "_id": "64907cb6e968be7fe5b14d74",
                        "region": "",
                        "extendedAddress": "",
                        "type": "home"
                    },
                    {
                        "country": "FR",
                        "poBox": "",
                        "streetAddress": "54 rue des Petites Ecuries",
                        "postalCode": "75010",
                        "locality": "Paris",
                        "id": "64907cb6e968be7fe5b14d75",
                        "_id": "64907cb6e968be7fe5b14d75",
                        "region": "",
                        "extendedAddress": "",
                        "type": "work"
                    }
                ]
            },
            {
                "field": "company",
                "from": "SEKOIA.IO",
                "to": "Sekoia.io"
            },
            {
                "field": "location",
                "from": "Paris",
                "to": "France"
            }
        ],
        "auth_method": "api key",
        "event_type": "user_update",
        "correlation": {},
        "service": "directory",
        "success": true,
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "4.5.6.7",
        "id": "64907cb6e968be7fe5b14d80",
        "message_chain": {},
        "timestamp": "2023-06-19T16:05:10.657Z"
    }
    ```



=== "user_update3"


    ```json
	{
        "initiated_by": {
            "id": "5bf6defbdcd8233029e0c599",
            "source": "scim",
            "type": "admin",
            "email": "maurice.moss@sekoia.io"
        },
        "geoip": {
            "country_code": "IE",
            "timezone": "Europe/Dublin",
            "latitude": 53.3379,
            "continent_code": "EU",
            "region_name": "Leinster",
            "longitude": -6.2591,
            "region_code": "L"
        },
        "resource": {
            "id": "628cf9c0d6f4831f8192fa8d",
            "type": "user",
            "username": "john.wick"
        },
        "changes": [
            {
                "field": "addresses",
                "from": [
                    {
                        "country": "FR",
                        "poBox": "",
                        "streetAddress": "",
                        "postalCode": "",
                        "locality": "",
                        "_id": "63ebb4f66e98244ef78531d8",
                        "id": "63ebb4f66e98244ef78531d8",
                        "extendedAddress": "",
                        "type": "home",
                        "region": ""
                    },
                    {
                        "country": "FR",
                        "poBox": "",
                        "streetAddress": "54 Rue des Petites Ecuries",
                        "postalCode": "75010",
                        "locality": "Paris",
                        "_id": "63ebb4f66e98244ef78531d9",
                        "id": "63ebb4f66e98244ef78531d9",
                        "extendedAddress": "",
                        "type": "work",
                        "region": ""
                    }
                ],
                "to": [
                    {
                        "country": "FR",
                        "poBox": "",
                        "streetAddress": "",
                        "postalCode": "",
                        "locality": "",
                        "_id": "64908c2ef675033f5a7a5e0f",
                        "id": "64908c2ef675033f5a7a5e0f",
                        "extendedAddress": "",
                        "type": "home",
                        "region": ""
                    },
                    {
                        "country": "FR",
                        "poBox": "",
                        "streetAddress": "54 Rue des Petites Ecuries",
                        "postalCode": "75010",
                        "locality": "Paris",
                        "_id": "64908c2ef675033f5a7a5e10",
                        "id": "64908c2ef675033f5a7a5e10",
                        "extendedAddress": "",
                        "type": "work",
                        "region": ""
                    }
                ]
            },
            {
                "field": "company",
                "from": "SEKOIA.IO",
                "to": "Sekoia.io"
            },
            {
                "field": "location",
                "from": "Paris",
                "to": "France"
            },
            {
                "field": "state",
                "from": "ACTIVATED",
                "to": "SUSPENDED"
            },
            {
                "field": "suspended",
                "from": false,
                "to": true
            }
        ],
        "useragent": {
            "patch": "0",
            "os_full": "Other",
            "os": "Other",
            "minor": "68",
            "major": "7",
            "name": "curl",
            "os_name": "Other",
            "device": "Other",
            "version": "7.68.0"
        },
        "auth_method": "api key",
        "event_type": "user_update",
        "correlation": {},
        "service": "directory",
        "success": true,
        "organization": "641b3db57090821c0b2f8183",
        "@version": "1",
        "client_ip": "10.11.12.13",
        "id": "64908c2ef675033f5a7a5e1e",
        "message_chain": {},
        "timestamp": "2023-06-19T17:11:10.381Z"
    }
    ```



