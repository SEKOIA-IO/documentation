=== "Manual installation"

    !!! warning
        The device code is valid during 10 minutes only

    1. Log in the [Ubika console](https://console.ubika.io/)
    2. Execute the following command to get the device code

        ```
        curl https://login.ubika.io/auth/realms/main/protocol/openid-connect/auth/device -d "client_id=rest-api" -d "grant_type=device" -d "scope=offline_access"
        ```

    3. Copy the `user code`, provided in the response, and paste it [on the Ubika authentication](https://login.ubika.io/auth/realms/main/protocol/openid-connect/auth/device) 
    4. Copy the `device code`, provided in the curl response
    5. Execute the following command to get the `refresh token`

        ```
        curl https://login.ubika.io/auth/realms/main/protocol/openid-connect/token -d "client_id=rest-api" -d "grant_type=urn:ietf:params:oauth:grant-type:device_code" -d "device_code=<device_code>"
        ```

    6. Copy the `refresh token`

=== "With the script"

    1. Log in the [Ubika console](https://console.ubika.io/)
    2. Save [the script](/assets/operation_center/integration_catalog/network_security/ubika/get_token.py) as `get_token.py`
    3. Create a virtual environment and execute the script

        ```
        python3 -m venv /tmp/venv
        /tmp/venv/bin/pip install requests
        /tmp/venv/bin/python3 get_token.py
        ```

    4. Copy the `refresh token`
