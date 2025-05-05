uuid: 2e9d87ed-6606-445a-90d1-9c7695b28335
name: Trend Micro Email Security
type: intake

## Overview
Trend Micro Email Security is a robust email protection solution that safeguards against email-borne threats such as phishing, malware, and spam, offering advanced threat detection and content filtering to secure corporate email communications effectively.

- **Vendor**: Trend Micro
- **Supported environment**: Cloud 
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway


## Configure

For the configuration part, there are two methods because Trend Micro Email Security is migrating to Trend Vision One within the same product. For those still using the old solution, there is the first configuration method, and for those using the new one, there is a second method.

### How to create an API token ( Trend Micro Email Security )

1. Log on to the Trend Micro Email Security administrator console.
2. Go to **Administration**

    ![Step 1](/assets/integration/email/trend_micro/step_1.png)

3. Click on **Service Integration**. The API Access tab displays by default.

    ![Click on Service Integration](/assets/integration/email/trend_micro/step_2.png)
    
4. Click **Add** to generate an API Key.

    ![Click on Add](/assets/integration/email/trend_micro/step_3.png)

5. Copy the API Key value and save the value. Keep the API Key private

### How to create an API token ( Trend Vision One )

1. Log in the Trend Vision One console
2. On the left panel, click `Administration` then click `API keys`

    ![step 1](/assets/integration/cloud_and_saas/trend_micro_vision_one/01_administration.png)

3. Click `Add API key`

    ![step 2](/assets/integration/cloud_and_saas/trend_micro_vision_one/02_create_api_key.png)

4. Type a name for the API key
5. Select the `Email administrator` role and an expiration time
6. Check `status` to enable the API key
7. Copy the API key and click `Close`

    ![step 4](/assets/integration/cloud_and_saas/trend_micro_vision_one/04_save_api_key.png)


### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Trend Micro Email Security`.
2. Edit the intake configuration using your `Service URL`, `Username` and `Login ID`. All three  are required.

* `username` is your `Login ID` entered during account creating
* The value of `service URL` varies according to your location:

| Location                                      | Service URL                 |
|-----------------------------------------------|-----------------------------|
| North America, Latin America and Asia Pacific | api.tmes.trendmicro.com     |
| Europe, the Middle East and Africa            | api.tmes.trendmicro.eu      |
| Australia and New Zealand                     | api.tmes-anz.trendmicro.com |
| Japan                                         | api.tmems-jp.trendmicro.com |
| Singapore                                     | api.tmes-sg.trendmicro.com  |
| India                                         | api.tmes-in.trendmicro.com  |


### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/46ca6fc8-3d30-434c-92ff-0e1cde564161_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_2e9d87ed-6606-445a-90d1-9c7695b28335_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2e9d87ed-6606-445a-90d1-9c7695b28335.md!}
