uuid: d626fec3-473a-44b3-9e3d-587fdd99a421
name: Broadcom Cloud Secure Web Gateway
type: intake

## Overview

Broadcom Cloud Secure Web Gateway is a cloud-native security solution providing advanced threat protection, content filtering, and data loss prevention, ensuring secure internet access and compliance for organizations with flexible deployment options and comprehensive web security features. This integration collects access logs from the Broadcom Cloud platform.

- **Vendor**: Broadcom
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: Web logs

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

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

{!_shared_content/operations_center/integrations/generated/d626fec3-473a-44b3-9e3d-587fdd99a421_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d626fec3-473a-44b3-9e3d-587fdd99a421_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d626fec3-473a-44b3-9e3d-587fdd99a421.md!}

## Further readings

- [Create API credentials](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/api-keys.html)
- [Use the Cloud SWG Sync API to Get Near-Real-Time Log Data](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/report-sync-about.html)
- [Extended Log File Format](https://www.w3.org/TR/WD-logfile.html)
- [Cloud SWG Reference: Access Log Formats](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/wss-reference/accesslogformats-ref.html)
