uuid: 242e8c5e-5ced-4dba-b342-45898cb72b71
name: Broadcom Cloud Secure Web Gateway
type: intake

## Overview

Broadcom Cloud Secure Web Gateway is a cloud-native security solution providing advanced threat protection, content filtering, and data loss prevention, ensuring secure internet access and compliance for organizations with flexible deployment options and comprehensive web security features.

{!_shared_content/operations_center/detection/generated/suggested_rules_d626fec3-473a-44b3-9e3d-587fdd99a421_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d626fec3-473a-44b3-9e3d-587fdd99a421.md!}

## Configure

This setup guide will show you how to provide an integration between Broadcom Cloud Secure Web Gateway events and Sekoia.io.

### Prerequisites

- Broadcom Cloud Secure Web Gateway platform account
- Access to Sekoia.io Intakes and Playbook pages with write permissions

### Generate Broadcom Cloud SWG credentials credentials

This instruction will share all necessary steps you should follow to generate credentials to interact with API:

- In the Cloud SWG portal, select Account ConfigurationAPI Credentials.
- Click `Add API Credentials`. 
- The New API Credential dialog will contain randomly generated characters in the `Username` and `Password` fields. Save them.

    ![Broadcom Cloud SWG Credentials](/assets/instructions/broadcom/credentials.png){ align=center width=100% }

Find more information in official [Documentation](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/api-keys.html)

## Sekoia.io configuration procedure

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Broadcom Cloud SWG`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the `Get Broadcom Cloud SWG events` trigger
2. Set up the module configuration with the Api Key and Account Id. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events
 
## Further readings

- [Create API credentials](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/api-keys.html)
- [Use the Cloud SWG Sync API to Get Near-Real-Time Log Data](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/report-sync-about.html)
- [Extended Log File Format](https://www.w3.org/TR/WD-logfile.html)
- [Cloud SWG Reference: Access Log Formats](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/wss-reference/accesslogformats-ref.html)
