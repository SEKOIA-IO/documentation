
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Network device logs` | Pradeo watch network traffic |
| `Process monitoring` | Pradeo analyze running processes |
| `Process use of network` | Pradeo watch network traffic |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "match_threats.json"

    ```json
	
    {
        "message": "Nov 15 08:51:42 subdomain.pradeo.net mtd-pradeosecuritysystems[6030]: {\"USER\":\"test_user\",\"SECTION\":\"MTD\\/Apps\",\"ACTION\":\"app_checking\",\"DESCRIPTION\":\"\",\"ITEM\":{\"APPLICATION_ID\":\"55936212\",\"APP_PKG_NAME\":\"com.an_app\",\"APP_VERSION\":\"4.394.10003\",\"APP_SHA1_SIG\":\"a92675ab3dafb37399c47a75ceac8effc4cb401d\"},\"ACTION_VALUES\":{\"ALLOWED\":\"true\",\"ACTION\":\"automatic\",\"POLICY\":\"Green\",\"MATCH_THREATS\":[\"cat_phone_cache_send\",\"cat_phone_device_info_send\",\"cat_phone_hardware_send\",\"cat_user_contact_info_send\",\"match_encrypt_with_key_downloaded_from_network\",\"match_exec_command_downloaded_from_network\",\"match_hide_app_icon_from_launcher\",\"match_priority\",\"match_rootkit\",\"match_rootkit_warning\",\"match_sms\"]}}\n",
        "user": {
            "name": "test_user"
        },
        "action": {
            "type": "automatic",
            "name": "app_checking"
        },
        "package": {
            "checksum": "a92675ab3dafb37399c47a75ceac8effc4cb401d",
            "version": "4.394.10003",
            "name": "com.an_app"
        },
        "pradeo": {
            "allowed": "true",
            "policy": "Green",
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
            ]
        },
        "related": {
            "user": [
                "test_user"
            ]
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
|`pradeo.allowed` | `keyword` | Indicates if the application is allowed (green/orange) or denied (red) |
|`pradeo.match_threats` | `keyword` | List of items detected in the application with a moderate/high alert associated. |
|`pradeo.policy` | `keyword` | Name of the policy used to classify the application. |
|`user.name` | `keyword` | Short name or login of the user. |

