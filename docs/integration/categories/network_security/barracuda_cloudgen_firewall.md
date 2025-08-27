uuid: fe9c462f-8907-4a4d-9a34-5ffff0a2c56f
name: Barracuda CloudGen Firewall
type: intake

## Overview

Barracuda NextGen Firewall is a unified network‐security appliance that combines stateful, application‐aware firewalling with intrusion prevention, malware protection, web‐filtering and full-mesh VPN/SD-WAN.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Vendor**: Barracuda
- **Supported environment**: OnPrem
- **Detection based on**: Telemetry
- **Supported application or feature**: Network device logs

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Barracuda device
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

## Configure

### Configure audit and reporting
1. Go to **CONFIGURATION > Configuration Tree > Box > Infrastructure Services > General Firewall Configuration**.
2. In the left menu, select **Audit and Reporting**.
3. Expand the **Configuration Mode** menu and select **Switch to Advanced View**.
4. Click **Lock**.
5. In the **LogPolicy** section, configure the following settings:
   1. For **Activity Log Mode** choose **Log-Pipe-Separated-Value-List**
   2. For **Activity Log Data** choose **Log-Info-Code**

6. To activate changes made to the audit and reporting configuration, you must perform a firmware restart.
    1. Click **Send Changes** and **Activate**. 
    2. Go to the **CONTROL > Box**. 
    3. Expand the **Operating System** section. 
    4. Click **Firmware Restart**.

### How to set up syslog forwarding
1. Go to **CONFIGURATION > Full Configuration > Box > Infrastructure Services > Syslog Streaming**.
2. Click **Lock**
3. Set **Enable Syslog Streaming** to **yes**.
4. Click **Send Changes** and **Activate**.
5. In the left menu, select **Logstream Destinations**. 
6. Expand the **Configuration Mode** menu and select **Switch to Advanced View**. 
7. Click **Lock**. 
8. Click the **+** icon to add a new entry. 
9. Enter a descriptive name in the upcoming dialog and click **OK**. The **Destinations** window opens. 
10. Select the **Logstream Destination** - **Explicit IP**. 
12. Enter the concentrator's IP address in the **Destination IP Address** field.
13. Enter the concentrator's port to **Destination Port** for delivering syslog messages.
14. Select the **Transmission Mode** (TCP or UDP - default; for TLS connections TCP is automatically set). 
15. Click **OK**. 
16. Click **Send Changes** and **Activate**.

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/fe9c462f-8907-4a4d-9a34-5ffff0a2c56f_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_fe9c462f-8907-4a4d-9a34-5ffff0a2c56f_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/fe9c462f-8907-4a4d-9a34-5ffff0a2c56f.md!}

## Further readings
- [How to configure audit and reporting](https://campus.barracuda.com/product/cloudgenfirewall/doc/170820911/how-to-configure-audit-and-reporting)
- [How to configure syslog streaming](https://campus.barracuda.com/product/cloudgenfirewall/doc/170820941/how-to-configure-syslog-streaming)

