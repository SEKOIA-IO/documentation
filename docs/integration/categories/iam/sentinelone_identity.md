# sentinelone\_identity

uuid: b502e522-6996-4b12-9538-f69326b68243 name: SentinelOne Identity type: intake

### Overview

SentinelOne Singularity Identity is a cybersecurity solution that provides identity protection and zero-trust security by continuously monitoring and analyzing user behaviors to detect and prevent potential threats.

* **Vendor**: SentinelOne
* **Supported environment**: Cloud
* **Detection based on**: Telemetry
* **Detection based on**: Alert

### Configure

This setup guide will show you how to pull events produced by SentinelOne Singularity Identity on [Sekoia.io](https://app.sekoia.io/).

#### Generate API token

1. Log in the SentinelOne Singularity console
2. On the left panel, click `Settings`
3. Click `Users`&#x20;
4. On the left, click `Service Users`
5. Click `Actions`, then click `Create New Service User`
6. Type a name, a description and Select the expiration duration for the Service User
7. Click `Next`
8. Select the scope of the access with the `viewer` role. We recommend using the `site` scope.
9. Click `Create User`
10. Copy and save the APIToken then click `Close`

#### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `SentinelOne Identity`. Copy the intake key.

{!\_shared\_content/operations\_center/integrations/generated/b502e522-6996-4b12-9538-f69326b68243.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_b502e522-6996-4b12-9538-f69326b68243\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/b502e522-6996-4b12-9538-f69326b68243.md!}
