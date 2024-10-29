uuid: d11df984-840d-4c29-a6dc-b9195c3a24e3
name: Bitdefender GravityZone
type: intake

## Overview

Bitdefender GravityZone is an enterprise-level cybersecurity solution offering advanced threat prevention, detection, and response for endpoints, networks, and cloud environments. It features centralized management for streamlined security oversight.

- **Vendor**: Bitdefender
- **Supported environment**: Cloud
- **Version compatibility**: 6.55, 6.56 (Latest version as of now)
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**:
    - Antiphishing
    - Application Control
    - Application Inventory
    - Antimalware
    - Advanced Threat Control
    - Data Protection
    - Exchange Malware Detected
    - Invalid Exchange user credentials
    - Firewall
    - Hyper Detect
    - Sandbox Analyzer Detection
    - Antiexploit
    - Network Attack Defense
    - User Control/Content Control
    - Storage Antimalware Event
    - Login from new device
    - Authentication audit
    - SMTP Connection
    - Internet Connection
    - Malware Outbreak

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Configure

This setup guide will show you how to forward your Bitdefender GravityZone events to Sekoia.io.

{!_shared_content/operations_center/detection/generated/suggested_rules_d11df984-840d-4c29-a6dc-b9195c3a24e3_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d11df984-840d-4c29-a6dc-b9195c3a24e3.md!}

### Steps to follow
- [Create a BitDefender GravityZone API key](#create-a-bitdefender-gravityzone-api-key)
- [Create an intake](#create-an-intake)
- [Set the push events settings](#set-the-push-events-settings)

### Create a BitDefender GravityZone API key

- Log in the BitDefender GravityZone console
- On the top-right bar, open your personal panel and click `My Accout`

  ![My Account](/assets/operation_center/integration_catalog/endpoint/bitdefender_gravityzone/1_my_account.png){: style="max-width:100%"}

- Scroll down to the `API keys` section and click `+ Add`

  ![API Key Create](/assets/operation_center/integration_catalog/endpoint/bitdefender_gravityzone/2_api_key_create.png){: style="max-width:100%"}

- Type a name for the API Key, select the `Event Push Service` checkbox and click `Generate`

  ![API Key Generate](/assets/operation_center/integration_catalog/endpoint/bitdefender_gravityzone/3_api_key_generate.png){: style="max-width:100%"}

- Save the API Key

  ![API Key Result](/assets/operation_center/integration_catalog/endpoint/bitdefender_gravityzone/4_api_key_result.png){: style="max-width:100%"}

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Bitdefender GravityZone. Copy the intake key.

### Set the push events settings

Bitdefender GravityZone have an ability to setup push events settings using http request.

Two ways are suggested in order to set up the forwarding of your events to Sekoia.io.

If you are not a shell expert, we recommend to use the "pyton script" way as it is easier to set up.

So you can setup it in two ways:

=== "Using python script"

    1. Open terminal
    2. Create virtual env and install requests library:
      ```bash
        $ python3 -m venv /tmp/venv
        $ /tmp/venv/bin/pip install requests
      ```
    3. Export your API Key and Intake key to environment variables:
      ```bash
        $ export BITDEFENDER_APIKEY="your_api_key"
        $ export SEKOIAIO_INTAKE_KEY="your_intake_key"
      ```
    4. Create python script with the following content:
      ```python
      import base64
      import sys
      import argparse
      
      import requests
      
      
      BITDEFENDER_PUSH_URL = "https://cloudgz.gravityzone.bitdefender.com/api/v1.0/jsonrpc/push"
      
      def activate_forwarding(apikey: str, intake_key: str):
          key = base64.b64encode(b':'+intake_key.encode('utf-8'))
      
          payload = {
            "id": "be630db8-24c2-481c-b150-a79807dd6f7d",
            "jsonrpc": "2.0",
            "method": "setPushEventSettings",
            "params": {
              "status": 1,
              "serviceType": "cef",
              "serviceSettings": {
                "url": "https://intake.sekoia.io/jsons?path=%24.events&status_code=200",
                "requireValidSslCertificate": True,
                "authorization": f"Basic {key}"
              },
              "subscribeToEventTypes": {
                "adcloud": True,
                "antiexploit": True,
                "aph": True,
                "av": True,
                "avc": True,
                "dp": True,
                "endpoint-moved-in": True,
                "endpoint-moved-out": True,
                "exchange-malware": True,
                "exchange-user-credentials": True,
                "fw": True,
                "hd": True,
                "hwid-change": True,
                "install": False,
                "modules": False,
                "network-monitor": True,
                "network-sandboxing": True,
                "new-incident": True,
                "ransomware-mitigation": True,
                "registration": True,
                "security-container-update-available": False,
                "supa-update-status": False,
                "sva": False,
                "sva-load": False,
                "task-status": False,
                "troubleshooting-activity": True,
                "uc": True,
                "uninstall": False
              }
            }
          }
      
          response = requests.post(
              url=BITDEFENDER_PUSH_URL,
              auth=requests.auth.HTTPBasicAuth(apikey,""),
              json=payload,
          )
          if response.status_code == 200:
              setting_id = response.json().get("id")
              print(f"The push setting was successfully created. ID: {setting_id}")
          else:
              print(f"The creation of the forwarding failed. Reason: {response.content}")
      
      
      if __name__ == '__main__':
          parser = argparse.ArgumentParser(prog=sys.argv[0], description='activate the forwarding of events to Sekoia.io')
          parser.add_argument('apikey')
          parser.add_argument('intake_key')
          args = parser.parse_args()
          activate_forwarding(args.apikey, args.intake_key)
      ```
    5. Run the script with the following command:
      ```bash
        $ /tmp/venv/bin/python3 bitdefender_activate_forwarding.py "${BITDEFENDER_APIKEY}" "${SEKOIAIO_INTAKE_KEY}"
      ```

=== "Manual"

    1. Open your terminal
    2. Export your API Key and Intake key to environment variables:
      ```bash
        $ export BITDEFENDER_APIKEY="your_api_key"
        $ export SEKOIAIO_INTAKE_KEY="your_intake_key"
      ```
    3. Convert the Bitdefender APIKey into base64: 
      ```bash
        $ echo -n '${BITDEFENDER_APIKEY}:' | base64
      ```
    4. Convert the Intake Key into base64:
      ```bash
        $ echo -n ':${SEKOIA_INTAKE_KEY}' | base64
      ```
    5. Create `payload.json` with following content ( replace `base64_intake_key` with the value from the previous steps):
      ```json
      {
        "id": "be630db8-24c2-481c-b150-a79807dd6f7d",
        "jsonrpc": "2.0",
        "method": "setPushEventSettings",
        "params": {
          "status": 1,
          "serviceType": "cef",
          "serviceSettings": {
            "url": "https://intake.sekoia.io/jsons?path=%24.events&status_code=200",
            "authorization": "Basic <base64_intake_key>",
            "requireValidSslCertificate": true
          },
          "subscribeToEventTypes": {
            "adcloud": false,
            "antiexploit": true,
            "aph": true,
            "av": true,
            "avc": true,
            "dp": true,
            "endpoint-moved-in": true,
            "endpoint-moved-out": true,
            "exchange-malware": true,
            "exchange-user-credentials": true,
            "fw": true,
            "hd": true,
            "hwid-change": true,
            "install": false,
            "modules": false,
            "network-monitor": true,
            "network-sandboxing": true,
            "new-incident": true,
            "ransomware-mitigation": true,
            "registration": true,
            "security-container-update-available": false,
            "supa-update-status": false,
            "sva": false,
            "sva-load": false,
            "task-status": false,
            "troubleshooting-activity": true,
            "uc": true,
            "uninstall": false
          }
        }
      }
      ```
    6. Send the payload to the Bitdefender API (replace `base64_api_key` with the value from the previous steps):
      ```bash
      $ curl -k -X POST \
      https://cloudgz.gravityzone.bitdefender.com/api/v1.0/jsonrpc/push \
      -H "Authorization: Basic <base64_api_key>" \
      -H 'cache-control: no-cache' \
      -H 'content-type: application/json' \
      -d @payload.json
      ```
