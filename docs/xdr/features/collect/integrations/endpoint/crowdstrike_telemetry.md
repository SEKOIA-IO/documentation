uuid: 10999b99-9a8d-4b92-9fbd-01e3fac01cd5
name: CrowdStrike Telemetry
type: intake

## Overview

[CrowdStrike] CrowdStrike provides cloud workload and endpoint security, threat intelligence, and cyberattack response services and products.

{!_shared_content/operations_center/detection/generated/suggested_rules_10999b99-9a8d-4b92-9fbd-01e3fac01cd5_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/10999b99-9a8d-4b92-9fbd-01e3fac01cd5.md!}

## Configure

### Transport to the collector

#### Prerequisites
The following prerequisites are needed in order to setup efficient events handling:

- Have Falcon Administrator
- Amazon Simple Storage Service (S3), which is the technology used to store event data outside of Falcon
- Amazon Simple Queue Service (SQS), which notifies you when new data is available from FDR

#### Configure the client

##### Install and configure CrowdStrike Telemetry

Please follow the [official documentation](https://falcon.eu-1.crowdstrike.com/documentation/9/falcon-data-replicator#falcon-data-replicator-setup).
You should be able to get `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `QUEUE_NAME` and `AWS_REGION` from the previous step.

Settup local environment:

```bash
### Install necessary dependencies
poetry install

### Run script
poetry run python main.py crowdstrike_telemetry
```

### Enjoy your events
Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.
