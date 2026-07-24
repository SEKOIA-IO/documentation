uuid: 584589c3-bdeb-4c62-8be9-b0ee34a3918f
name: Varonis Data Security SaaS
type: intake

## Overview
Varonis offers solutions to track and protect data.

- **Vendor**: Varonis
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Data loss prevention


## Configure

### How to create API token

1. Log in the Varonis console
2. Go to `Configuration` > `API Keys`
    
    ![Varonis Data Security SaaS configure - 1](/assets/integration/network/varonis_data_security_saas/Step_01.png){: style="max-width:100%"}
    
3. Click `+ New API Key`
    
    ![Varonis Data Security SaaS configure - 2](/assets/integration/network/varonis_data_security_saas/Step_02.png){: style="max-width:100%"}

4. Type a name 
5. Select `Threat Detection Integrator` as a role 
6. Type a description 
7. Click `Generate Key`
    
    ![Varonis Data Security SaaS configure - 3](/assets/integration/network/varonis_data_security_saas/Step_03.png){: style="max-width:100%"}

8. Copy the generated API Key 
9. Click `Done`
    
    ![Varonis Data Security SaaS configure - 4](/assets/integration/network/varonis_data_security_saas/Step_04.png){: style="max-width:100%"}

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Varonis Data Security SaaS`.
2. Set up the intake configuration with the Base URL (looks like `https://YOUR_TENANT.varonis.io`) and API token.


{!_shared_content/operations_center/integrations/generated/584589c3-bdeb-4c62-8be9-b0ee34a3918f.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_584589c3-bdeb-4c62-8be9-b0ee34a3918f_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/584589c3-bdeb-4c62-8be9-b0ee34a3918f.md!}