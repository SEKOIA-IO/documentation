# ubika\_cloud\_protector\_alerts

uuid: d0383e87-e054-4a21-8a2c-6a89635d8615 name: Ubika Cloud Protector Alerts type: intake

### Overview

Ubika Cloud Protector is a cloud-native security solution, providing advanced threat detection and data protection to secure cloud environments, enabling real-time monitoring and mitigation of risks in cloud-based infrastructures.

* **Vendor**:Ubika
* **Supported environment**: SaaS
* **Detection based on**: Alert
* **Supported application or feature**: Web application firewall logs

### Configure

#### How to get API keys info

3 information are required to collect data from Ubika:

* The `provider name` (available in Ubika interface)
* The `tenant name` (available in Ubika interface)
* A `token` (provided by Ubika support team)

!!! warning The following instructions are based on the old interface of Ubika Cloud Protector. Please, switch to the old interface if you use the new one. {: style="max-width:100%"}

To get API keys info:

1. Log in the Ubika Cloud protector
2.  Go to `Account` > `API Access`

    {: style="max-width:100%"}
3.  In the `API KEYS INFO` section, please note the `provider name` and the `tenant name`

    {: style="max-width:100%"}
4. Finally, contact `Ubika support` to request a `token` for the legacy API. This specific `token` cannot be retrieved through the Ubika interface at the moment.

#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Ubika Cloud Protector`.
2. Set the intake account configuration with the `provider`, `tenant` and `token` from the `How to get API keys info` step

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!\_shared\_content/operations\_center/integrations/generated/d0383e87-e054-4a21-8a2c-6a89635d8615\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_d0383e87-e054-4a21-8a2c-6a89635d8615\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/d0383e87-e054-4a21-8a2c-6a89635d8615.md!}
