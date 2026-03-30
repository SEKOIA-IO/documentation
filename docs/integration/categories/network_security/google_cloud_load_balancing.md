# google\_cloud\_load\_balancing

uuid: 4d50ae7e-ccac-4a5b-9a4c-58a7893f93bb name: Google Cloud Load Balancing type: intake

### Overview

Google Cloud Load Balancing is a fully distributed, software-defined managed service that distributes traffic across multiple backend instances in multiple regions, enhancing performance, reliability, and scalability.

* **Vendor**: Google Cloud
* **Supported environment**: SaaS
* **Detection based on**: Telemetry
* **Supported application or feature**: Web logs, Web application firewall logs, Googe Cloud Armor

### Specification

#### Prerequisites

* Google licence Enterprise standard or higher
* Access to Sekoia.io Intakes and Playbook pages with write permissions
* Administrator access to the Google Cloud console

#### Logs details

* **Supported functionalities**: See section [Overview](google_cloud_load_balancing.md#overview)
* **Supported type(s) of structure**: JSON
* **Supported verbosity level**: Informational

#### How to set up Google PubSub

{!\_shared\_content/operations\_center/integrations/google\_cloud.md!}

#### How to configure log forwarding

1. On the Google cloud console, go to **Monitoring**
2. On the left panel, Click **Log router**
3. On the top, Click **Create sink**
4. Type `name` for the sink and click **Next**
5. Select **Cloud Pub/Sub topic** as Sink service and select the Pub/Sub topic as destination. Click **Next**
6.  As **Build inclusion filter**, type:

    ```
    (resource.type="http_load_balancer" OR resource.type="http_external_regional_lb_rule")
    ```

and click **Next**

7. Click **Create sink**

{!\_shared\_content/operations\_center/integrations/generated/4d50ae7e-ccac-4a5b-9a4c-58a7893f93bb\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/integrations/generated/4d50ae7e-ccac-4a5b-9a4c-58a7893f93bb.md!}
