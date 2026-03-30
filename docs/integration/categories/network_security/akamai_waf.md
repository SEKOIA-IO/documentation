# akamai\_waf

uuid: 4c4f3256-c3c7-415f-9515-75261514f861 name: Akamai WAF type: intake

### Overview

Akamai Web Application Firewall (WAF) is a cloud-based security solution designed to protect web applications from a wide range of online threats, including SQL injection, cross-site scripting (XSS), and DDoS attacks. Leveraging Akamai's global content delivery network (CDN), the WAF provides real-time protection by filtering and monitoring HTTP traffic between the web application and the internet.

* **Vendor**: Akamai
* **Supported environment**: SaaS
* **Detection based on**: Alert
* **Supported application or feature**: Web application firewall logs

### Configure

#### Create EdgeGrid authentication credentials

1.  Launch `Identity and Access Management`. In Control Center, select `☰ > ACCOUNT ADMIN > Identity & access`.

    {: style="max-width:100%"}
2. Under `Users and API Clients`, click `Create API client`.
3. Click `Quick` to create an API client with access levels, group roles, and permissions identical to your current login.
4. Click Show additional details to verify the APIs you can access.
5. Enter the API service's name in the `Filter` field to verify that it's included and that you have the proper level of access. Click Hide additional details to return to the Details and Credentials information.
6. Save information from the `Credentials` section.

#### Enable data collection

1.  Go to "Security Configurations" menu and click on "Version history"

    {: style="max-width:100%"}
2.  On the current version, click on action and select the option "Create new version from v"

    {: style="max-width:100%"}
3.  Set "Data collection for SIEM integration" option to on and click on activate.

    {: style="max-width:100%"}

#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Akamai WAF`
2. To fill the form, use the credentials acquired on `Create EdgeGrid authentication credentials`

**Enjoy your events on the** [**Events page**](https://app.sekoia.io/operations/events)

{!\_shared\_content/operations\_center/integrations/generated/4c4f3256-c3c7-415f-9515-75261514f861\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_4c4f3256-c3c7-415f-9515-75261514f861\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/4c4f3256-c3c7-415f-9515-75261514f861.md!}

#### Further Readings

* [Create EdgeGrid authentication credentials](https://techdocs.akamai.com/developer/docs/set-up-authentication-credentials)
