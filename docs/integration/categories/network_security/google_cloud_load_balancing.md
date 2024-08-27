uuid: 4d50ae7e-ccac-4a5b-9a4c-58a7893f93bb
name: Google Cloud Load Balancing
type: intake

## Overview

Google Cloud Load Balancing is a fully distributed, software-defined managed service that distributes traffic across multiple backend instances in multiple regions, enhancing performance, reliability, and scalability.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Vendor**: Google Cloud
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Web logs, Web application firewall logs, Googe Cloud Armor
  
## Specification

### Prerequisites

- Google licence Enterprise standard or higher
- Access to Sekoia.io Intakes and Playbook pages with write permissions
- Administrator access to the Google Cloud console

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Informational

### How to set up Google PubSub
{!_shared_content/operations_center/integrations/google_cloud.md!}

### How to configure log forwarding
1. On the Google cloud console, go to **Monitoring**
2. On the left panel, Click **Log router**

    ![Click Log router](/assets/operation_center/integration_catalog/network_security/google_cloud_load_balancing/1_log_router.png)

3. On the top, Click **Create sink**

    ![Create sink](/assets/operation_center/integration_catalog/network_security/google_cloud_load_balancing/2_create_sink.png)

4. Type `name` for the sink and click **Next**

   ![Type name](/assets/operation_center/integration_catalog/network_security/google_cloud_load_balancing/3_enter_name.png)

5. Select **Cloud Pub/Sub topic** as Sink service and select the Pub/Sub topic as destination. Click **Next**

    ![Select destination](/assets/operation_center/integration_catalog/network_security/google_cloud_load_balancing/4_select_destination.png)

6. As **Build inclusion filter**, type:
    ```
    (resource.type="http_load_balancer" OR resource.type="http_external_regional_lb_rule")
    ```
and click **Next**

7. Click **Create sink**

{!_shared_content/operations_center/integrations/generated/4d50ae7e-ccac-4a5b-9a4c-58a7893f93bb_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/4d50ae7e-ccac-4a5b-9a4c-58a7893f93bb.md!}

