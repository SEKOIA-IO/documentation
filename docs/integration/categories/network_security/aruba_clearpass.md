uuid: bbbb10ea-72a1-4b60-8385-6543b588dc3f
name: Aruba ClearPass
type: intake

## Overview

Aruba ClearPass is a vendor-agnostic network access control (NAC) and policy management platform by HPE Aruba Networking that automates security compliance and role-based access for all users, devices, and IoT endpoints.
 
- **Vendor**: Aruba  Networks
- **Supported environment**: On-Prem
- **Detection based on**: Telemetry

## Configure

### Instructions on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

### Configure Aruba ClearPass syslog server
1. Sign in to the **ClearPass Policy Manager** console.
2. Select **Administration > External servers > Syslog targets**.
3. Click **Add**.
4. In the **Add syslog target** window that appears, specify the following details:
    - **Host address**: enter the syslog concentrator IP address.
    - **Server port**: enter the syslog concentrator port number.
    - **Protocol**: select **UDP** (you can also select **TCP**, depending on your syslog concentrator configuration).
5. Click **Save**. 

### Configure syslog export filters
1. Go to **Administration > External servers > Syslog export filters**.
2. Click **Add**.
3. In the **Add Syslog Filters** window that appears, specify the following in the **General** tab:
    - **Name**: enter the syslog export filter name based on the table in Export template items.
    - **Export template**: select the appropriate export template based on the table in Export template items.
    - **Export event format type**: select CEF.
    - **Syslog servers**: select the syslog concentrator IP address.
4. In the **Export template** list, when you select the **Session** or **Insight** export templates, the **Filter and columns** tab is enabled. Complete the following steps:
    - Click the **Filter and columns** tab.
    - **Data filter**: make sure the default value All requests is selected.
    - **Column selection**: select the predefined field groups you want to get.
    - Click the **Summary** tab.
    - Click **Save**.    
5. In the Export template list, when you select the System events and Audit records export templates, the Filter and columns tab is not enabled. Proceed to the Summary tab and click Save.
6. Repeat steps to add syslog export filters for all Session, Insight, Audit records and System events export templates based on the details from the table in Export template items.

{!_shared_content/operations_center/integrations/generated/bbbb10ea-72a1-4b60-8385-6543b588dc3f_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_bbbb10ea-72a1-4b60-8385-6543b588dc3f_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/bbbb10ea-72a1-4b60-8385-6543b588dc3f.md!}
