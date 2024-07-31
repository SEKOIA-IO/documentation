
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_block_user"


    ```json
	{
        "@timestamp": 1685465626150,
        "_document_id": "ioehzret57biefb87",
        "action": "org.block_user",
        "actor": "Admin",
        "actor_id": 6493123,
        "actor_location": {
            "country_code": "FR"
        },
        "blocked_user": "aaa",
        "created_at": 1685465626150,
        "operation_type": "create",
        "org": "Test-org",
        "org_id": 123123995,
        "user_agent": "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
    }
    ```



=== "test_disable_third_party_access_requests"


    ```json
	{
        "@timestamp": 1686150683340,
        "_document_id": "w-eifejgjg877jjf",
        "action": "org.allow_third_party_access_requests_from_outside_collaborators_disabled",
        "actor": "Admin",
        "actor_id": 6123123,
        "actor_location": {
            "country_code": "FR"
        },
        "created_at": 1686150683340,
        "operation_type": "modify",
        "org": "Test-org",
        "org_id": 123123995,
        "user_agent": "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
    }
    ```



=== "test_member_can_create_public_pages"


    ```json
	{
        "@timestamp": 1686150676330,
        "_document_id": "s-ioehzret57biefb87",
        "action": "members_can_create_public_pages.enable",
        "actor": "Admin",
        "actor_id": 6123123,
        "actor_location": {
            "country_code": "FR"
        },
        "created_at": 1686150676330,
        "operation_type": "modify",
        "org": "Test-org",
        "org_id": 123123995,
        "user": "Admin",
        "user_agent": "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
        "user_id": 6123123
    }
    ```



=== "test_update_member_repository_invitation_permission"


    ```json
	{
        "@timestamp": 1686150672357,
        "_document_id": "ioehzret57biefb87",
        "action": "org.update_member_repository_invitation_permission",
        "actor": "Admin",
        "actor_id": 6123123,
        "actor_location": {
            "country_code": "FR"
        },
        "created_at": 1686150672357,
        "operation_type": "modify",
        "org": "Test-org",
        "org_id": 123123995,
        "permission": false,
        "user_agent": "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
    }
    ```



