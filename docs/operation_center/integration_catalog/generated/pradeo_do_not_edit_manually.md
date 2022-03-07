


## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "match_threats.json"

    ```json
	
    {
        "package": {
            "checksum": "a92675ab3dafb37399c47a75ceac8effc4cb401d",
            "name": "com.an_app",
            "version": "4.394.10003"
        },
        "action": {
            "name": "app_checking",
            "type": "automatic"
        },
        "user": {
            "name": "test_user"
        },
        "pradeo": {
            "allowed": "true",
            "match_threats": [
                "cat_phone_cache_send",
                "cat_phone_device_info_send",
                "cat_phone_hardware_send",
                "cat_user_contact_info_send",
                "match_encrypt_with_key_downloaded_from_network",
                "match_exec_command_downloaded_from_network",
                "match_hide_app_icon_from_launcher",
                "match_priority",
                "match_rootkit",
                "match_rootkit_warning",
                "match_sms"
            ],
            "policy": "Green"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`package.checksum` | `keyword` | Checksum of the installed package for verification. |
|`package.name` | `keyword` | Package name |
|`package.version` | `keyword` | Package version |
|`pradeo.allowed` | `keyword` | None |
|`pradeo.match_threats` | `keyword` | None |
|`pradeo.policy` | `keyword` | None |
|`user.name` | `keyword` | Short name or login of the user. |

