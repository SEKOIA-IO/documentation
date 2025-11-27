uuid: e04c988c-cbb7-4b6a-8025-7b80a301ac28
name: Ubika Cloud Protector Next Generation
type: intake

## Overview

Ubika Cloud Protector Next Generation offers cutting-edge security for cloud environments, leveraging artificial intelligence to detect and neutralize threats in real-time. Its user-friendly interface and seamless integration enhance overall cybersecurity, empowering businesses to safeguard their data effortlessly. Protect your cloud assets with unparalleled reliability and advanced defense capabilities.

- **Vendor**:Ubika
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Web application firewall logs

## Configure

### How to create refresh token

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


### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Ubika Cloud Protector Next Generation`.
2. Set the intake account configuration with the `namespace` and `refresh token` from the `How to create refresh token` step

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/e04c988c-cbb7-4b6a-8025-7b80a301ac28_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_e04c988c-cbb7-4b6a-8025-7b80a301ac28_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/e04c988c-cbb7-4b6a-8025-7b80a301ac28.md!}

