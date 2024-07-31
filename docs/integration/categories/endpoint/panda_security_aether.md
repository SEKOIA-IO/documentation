uuid: ee6364a1-9e3c-4363-9cb6-2f574bd4ce51
name: Panda Security Aether
type: intake

## Overview
- **Vendor**:
- **Plan**: Defend Core & Defend Prime
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

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Panda Security Aether.


### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Panda Security trigger](../../../automate/library/panda-security.md#fetch-security-events). You can use the existing template to fasten and ease the creation of your playbook.

Set up the module configuration with an access ID, the password of the access ID (`access_secret`), your WatchGuard Cloud account ID (`account_id`), the API Key (`api_key`).
Set the `base_url` with the domain part of the API Url (e.g: for the API URL `https://api.usa.cloud.watchguard.com/rest/`, the `base_url` is `https://api.usa.cloud.watchguard.com`).
Set up the trigger configuration with the frequency of the pull.

At the end of the playbook, set up the action `Push events to intake` with a Sekoia.io API key and the intake key, from the intake previously created.

Start the playbook and enjoy your events.



{!_shared_content/operations_center/integrations/generated/ee6364a1-9e3c-4363-9cb6-2f574bd4ce51_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ee6364a1-9e3c-4363-9cb6-2f574bd4ce51_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/ee6364a1-9e3c-4363-9cb6-2f574bd4ce51.md!}

## Further Readings

- [Get started with WatchGuard APIs](https://www.watchguard.com/help/docs/api/Content/en-US/api_get_started/get_started.html)
- [WatchGuard APIs](https://www.watchguard.com/help/docs/api/Content/en-US/home.html)
