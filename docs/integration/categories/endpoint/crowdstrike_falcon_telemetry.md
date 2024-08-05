uuid: 10999b99-9a8d-4b92-9fbd-01e3fac01cd5
name: CrowdStrike Falcon Telemetry
type: intake

## Overview

CrowdStrike provides cloud workload and endpoint security, threat intelligence, and cyberattack response services and products.

- **Vendor**: Cloudflare
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Process monitoring

CrowdStrike Falcon Telemetry gathers raw system logs, legitimate and suspicious activities. Below is a non-exhaustive list of activities that can be monitored using CrowdStrike Telemetry logs:

- Process creation and termination
- File path creation and deletion
- Events related to processes
- DNS requests
- HTTP connections

## Configure


### Prerequisites
The following prerequisites are needed in order to setup efficient events handling:

- Have a Falcon Administrator account

### Generate the Credentials

To set up the integration:

1. Contact your CrowdStrike account representative to set up your Falcon Data Replicator feed (This request may take 2 to 5 days)
2. Create the credentials for the feed:
   1. In the console, got to `Support and resources > Resources and tools > Falcon data replicator`.
   2. Click on the burger menu (the three vertical point) and select `Create credentials`
   3. Get the client ID, the client secret, the queue name and the region.


### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `CrowdStrike Falcon Telemetry`. Copy the intake key.


### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new events from CrowdStrike Data replication](/integration/action_library/endpoint/crowdstrike) trigger
2. Set up the module configuration with your client id, the client secret and the region. Set up the trigger configuration with the intake key and the queue name.
3. Start the playbook and enjoy your events

{!_shared_content/operations_center/integrations/generated/10999b99-9a8d-4b92-9fbd-01e3fac01cd5_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_10999b99-9a8d-4b92-9fbd-01e3fac01cd5_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/10999b99-9a8d-4b92-9fbd-01e3fac01cd5.md!}


## Further Readings

- [Falcon Data Replicator documentation](https://falcon.eu-1.crowdstrike.com/documentation/9/falcon-data-replicator#falcon-data-replicator-setup)
