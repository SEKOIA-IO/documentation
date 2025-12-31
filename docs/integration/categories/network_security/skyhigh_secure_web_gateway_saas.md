---
uuid: 40bac399-2d8e-40e3-af3b-f73a622c9687
title: McAfee Web Gateway / Skyhigh Secure Web Gateway - SaaS
name: McAfee Web Gateway / Skyhigh Secure Web Gateway - SaaS
type: intake
---

## Overview
Skyhigh Secure Web Gateway (SWG) (previously McAfee Web Gateway (MWG)) is a web gateway offering malware detection, threat prevention and reputation filtering.

- **Vendor**: Skyhigh Security
- **Supported environment**: SaaS
- **Version compatibility**: 12.2.10
- **Detection based on**: Telemetry
- **Supported application or feature**: Anti-virus, Web proxy,	Web logs


## Configure

#### Configure a Rule Set

Prior to the configuration, download the “Rule Set” configuration [`SEKOIAIO_SKYHIGH_swg.xml`](/assets/integration/network/skyhigh_secure_web_gateway/SEKOIAIO_SKYHIGH_swg.xml).

In your SWG console:

- Select `Policy` section then the `Rule sets` tab. From the menu, select `Log Handler`.
- Right-click on the `Default` Log Handler in the tree then select `Add > Rule Set from Library...`.
- Once the `Add from Rule Set library` window opened, under the `Rule Set Library` tree, click on the `Import from file...` button and import `SEKOIAIO_mwg.xml` file.
- Select the `Rule Set` `Sekoia.io` and ensure the rule `forward logs` is enabled.


#### Find your Customer ID
1. Go to `Settings > Infrastructure > Client Proxy Management`. 
2. Click `Global Configuration > Tenant Authentication`. 
3. The Customer ID is displayed under `Global Settings`.

{!_shared_content/integration/intake_configuration.md!}


#### Pull the logs to collect them on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

1. Click **+ PLAYBOOK** button to create a new one
2. Select **Create a playbook from scratch**
3. Give it a name in the field **Name**
4. Open the left panel, click **Fastly** then select the trigger `Fetch events from Skyhigh Security Secure Web Gateway (SWG) API`
5. Click **Create**
6. Create a **Module configuration**. Name the module configuration as you wish.
7. Create a **Trigger configuration** using:
   
      - `Intake key` created on the previous step
      - `customer Id` (from "Find your Customer ID" step), 
      - `account name`
      - `account password`
      - `api domain name` (`<region>.logapi.skyhigh.cloud`; e.g. Germany: de.logapi.skyhigh.cloud, North America: us.logapi.skyhigh.cloud, ...)

8. Click the **Save** button
9. **Activate the playbook** with the toggle button

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/40bac399-2d8e-40e3-af3b-f73a622c9687_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_40bac399-2d8e-40e3-af3b-f73a622c9687_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/40bac399-2d8e-40e3-af3b-f73a622c9687.md!}


## Further readings

- [Skyhigh Secure Web Gateway (Cloud) Documentation](https://success.skyhighsecurity.com/Skyhigh_Secure_Web_Gateway_(Cloud))
- [Region prefixes](https://success.skyhighsecurity.com/Skyhigh_Secure_Web_Gateway_(Cloud)/Using_the_Forensics_API_for_Reporting/Create_a_Report_with_the_Forensics_API)
