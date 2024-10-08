uuid: ccf942fe-c839-42be-a081-5c3f946e80f5
name: Digital Shadows SearchLight
type: intake

## Overview

Digital Shadows SearchLight continuously searches and identifies any unwanted exposures, and provides contextualised alerts to better understand the associated risks.

- **Vendor**: Digital Shadows
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Social media monitoring, File monitoring

## Step-by-Step Configuration Procedure

In this documentation we will explain how to collect and send SearchLight logs to Sekoia.io.

### Instructions on the 3rd Party Solution

First of all, you will have to retrieve configuration information.
To do so, connect to the [Digital Shadows portal](https://portal-digitalshadows.com/) to get an API key under the heading `api` > "`tored Objects` > `Portal` > `Searchlight API doc`.

Then, you will need to retrieve the following information from the portal:

- `API URL`
- `Basicauth key`
- `Basicauth secret`
- Your Searchlight `account ID`

You now have all information to configure the Digital Shadows Searchlight module and its `Send events` action to Sekoia.io.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

{!_shared_content/operations_center/integrations/generated/ccf942fe-c839-42be-a081-5c3f946e80f5_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ccf942fe-c839-42be-a081-5c3f946e80f5_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/ccf942fe-c839-42be-a081-5c3f946e80f5.md!}

