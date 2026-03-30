# broadcom\_cloud\_swg

uuid: d626fec3-473a-44b3-9e3d-587fdd99a421 name: Broadcom Cloud Secure Web Gateway type: intake

### Overview

Broadcom Cloud Secure Web Gateway is a cloud-native security solution providing advanced threat protection, content filtering, and data loss prevention, ensuring secure internet access and compliance for organizations with flexible deployment options and comprehensive web security features. This integration collects access logs from the Broadcom Cloud platform.

* **Vendor**: Broadcom
* **Supported environment**: SaaS
* **Detection based on**: Alert, Telemetry
* **Supported application or feature**: Web logs

### Configure

This setup guide will show you how to provide an integration between Broadcom Cloud Secure Web Gateway events and Sekoia.io.

#### Prerequisites

* Broadcom Cloud Secure Web Gateway platform account
* Access to Sekoia.io Intakes and Playbook pages with write permissions

#### Generate Broadcom Cloud SWG credentials credentials

This instruction will share all necessary steps you should follow to generate credentials to interact with API:

* In the Cloud SWG portal, select Account ConfigurationAPI Credentials.
* Click `Add API Credentials`.
*   The New API Credential dialog will contain randomly generated characters in the `Username` and `Password` fields. Save them.

    { align=center width=100% }

Find more information in official [Documentation](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/api-keys.html)

### Sekoia.io configuration procedure

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/connector\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/d626fec3-473a-44b3-9e3d-587fdd99a421\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_d626fec3-473a-44b3-9e3d-587fdd99a421\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/d626fec3-473a-44b3-9e3d-587fdd99a421.md!}

### Further readings

* [Create API credentials](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/api-keys.html)
* [Use the Cloud SWG Sync API to Get Near-Real-Time Log Data](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/report-sync-about.html)
* [Extended Log File Format](https://www.w3.org/TR/WD-logfile.html)
* [Cloud SWG Reference: Access Log Formats](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/wss-reference/accesslogformats-ref.html)
