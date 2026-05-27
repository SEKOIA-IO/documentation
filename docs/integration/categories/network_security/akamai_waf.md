uuid: 4c4f3256-c3c7-415f-9515-75261514f861
name: Akamai WAF
type: intake

## Overview

Akamai Web Application Firewall (WAF) is a cloud-based security solution designed to protect web applications from a wide range of online threats, including SQL injection, cross-site scripting (XSS), and DDoS attacks. Leveraging Akamai's global content delivery network (CDN), the WAF provides real-time protection by filtering and monitoring HTTP traffic between the web application and the internet.
 
- **Vendor**: Akamai
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Web application firewall logs

## Configure

### Create EdgeGrid authentication credentials

1. Navigate to `Identity and Access Management`. In the Control Center, click the Main Menu icon (☰) and select `ACCOUNT ADMIN` > `Identity & access`.

    ![step 1](/assets/operation_center/integration_catalog/network_security/akamai_waf/identity_and_access_button.png){: style="max-width:100%"}

2. In the `Users and API Clients` section, click `Create API client`.

     ![step 2](/assets/operation_center/integration_catalog/network_security/akamai_waf/create_api_button.png){: style="max-width:100%"}

3. Select the `Quick` option to automatically generate an API client.
   
   ![step 3](/assets/operation_center/integration_catalog/network_security/akamai_waf/create_api_client_button.png){: style="max-width:100%"}

4. Click Show additional details to review and verify your accessible APIs and search if you have `SIEM` permission using the `Filter` field before creating this api key.

   ![step 4](/assets/operation_center/integration_catalog/network_security/akamai_waf/siem_permission.png){: style="max-width:100%"}

5. Copy and securely save the information displayed in the `Credentials` section.

### Enable data collection

1. Navigate to the `Security Configurations`. In the Control Center, click the Main Menu icon (☰) and select `WEB & DATA CENTER SECURITY` > `Security Configurations`.

    ![step 1](/assets/operation_center/integration_catalog/network_security/akamai_waf/security_configuration_button.png){: style="max-width:100%"}

2. Click on `Edit Configuration` for the app you want to enable data collection on.

    ![step 2](/assets/operation_center/integration_catalog/network_security/akamai_waf/edit_configuration_button.png){: style="max-width:100%"}

3. On the current version, under `Advanced settings`. Set `Data collection` for SIEM integration option to on and click on activate.

    ![step 3](/assets/operation_center/integration_catalog/network_security/akamai_waf/data_collection_siem.png){: style="max-width:100%"}

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Akamai WAF`
2. To fill the form, use the credentials acquired on  `Create EdgeGrid authentication credentials`

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)


{!_shared_content/operations_center/integrations/generated/4c4f3256-c3c7-415f-9515-75261514f861_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_4c4f3256-c3c7-415f-9515-75261514f861_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/4c4f3256-c3c7-415f-9515-75261514f861.md!}

### Further Readings
- [Create EdgeGrid authentication credentials](https://techdocs.akamai.com/developer/docs/set-up-authentication-credentials)
