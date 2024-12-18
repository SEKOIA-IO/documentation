uuid: ee6364a1-9e3c-4363-9cb6-2f574bd4ce51
name: Panda Security Aether
type: intake

## Overview
- **Vendor**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

Panda Security offers two Endpoint Detection and Response (EDR) solutions for companies:

- Adaptive Defense and Adaptive Defense 360
- Endpoint Protection and Endpoint Protection Plus

This setup guide shows how to forward security events collected on the Panda Security Aether platform to Sekoia.io.



## Configure

### Enable API Access

To enable API access, log in to your WatchGuard Cloud Account then select `Administration > Managed Access`.
Click `Enable API Access` and specify the passwords for readwrite access and readonly access. Agree the terms and the conditions of the WatchGuard APIs License Agreement then click `Save`.
Copy the access IDs, the API url and an API Key.


### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Panda Security Aether.
2. Set up the intake account with an access ID, the password of the access ID (`access_secret`), your WatchGuard Cloud account ID (`account_id`), the API Key (`api_key`). Set the `base_url` with the domain part of the API Url (e.g: for the API URL `https://api.usa.cloud.watchguard.com/rest/`, the `base_url` is `https://api.usa.cloud.watchguard.com`).
3. Set up the intake configuration with the frequency of the pull.

{!_shared_content/operations_center/integrations/generated/ee6364a1-9e3c-4363-9cb6-2f574bd4ce51_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ee6364a1-9e3c-4363-9cb6-2f574bd4ce51_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/ee6364a1-9e3c-4363-9cb6-2f574bd4ce51.md!}

## Further Readings

- [Get started with WatchGuard APIs](https://www.watchguard.com/help/docs/api/Content/en-US/api_get_started/get_started.html)
- [WatchGuard APIs](https://www.watchguard.com/help/docs/api/Content/en-US/home.html)
