uuid: 8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d
name: SentinelOne Cloud Funnel 1.0 [Deprecated]
type: intake

## Overview

SentinelOne Deep Visibility extends the SentinelOne EDR to provide full visibility into endpoint data. Its patented kernel-based monitoring allows a near real-time search across endpoints for all indicators of compromise (IOC) to empower security teams to augment real-time threat detection capabilities with a powerful tool that enables threat hunting.

SentinelOne Deep Visibility logs provides in-depth logs that are useful for detection and investigation purposes.

**Important**: Please contact your point of contact at SentinelOne in order to subscribe to this option and collect the required technical information to retrieve those logs via a SentinelOne Kafka.

> No additional installation or configuration on the agents is needed.

Please find bellow a short list of activities that are available for security supervision thanks to SentinelOne Deep Visibility logs:

- File Modification
- File Creation
- File Deletion
- Process Creation
- Process Exit
- Process Termination
- Command line arguments
- DNS Query
- TCPv4 Connection
- TCPv4 Listen
- HTTP Request
- Registry Key Security Changed
- Registry Value Modified
- Registry Value Delete
- Scheduled Task Update
- Scheduled Task Start
- Scheduled Task Trigger

{!_shared_content/operations_center/detection/generated/suggested_rules_8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8c1bee36-d516-42f9-9b6f-a8e4dcac3d1d.md!}

## Configure

This setup guide will show you how to pull events produced by SentinelOne Deep Visibility on [Sekoia.io](https://app.sekoia.io/).

### Setup a SentinelOne Kafka server


To collect the SentinelOne Deep Visibility logs, the API format is not appropriate due to the Sentinel rate limits and high amount of logs to be pulled from SentinelOne instance.
Thus SentinelOne have a solution using Kafka technology which can be delivered after a subscription with SentinelOne.

**Important**: If you have multiple SentinelOne Management Consoles, you must subscribe to a Kafka topic for each one.

> Compared to the API connection with standard SentinelOne logs, there is no time limitation of the secrets to collect the logs wia Kafka.

### Create a SentinelOne Deep Visibility intake

In the [Sekoia.io Operation Center](https://app.sekoia.io/operations/intakes):

1. Click on the `Intake` page.
2. Search for `SentinelOne Deep Visibility` by navigating the page or using the search bar.
3. Click `Create` on the relevant object.
4. Fulfil the `Name` of your intake that will be displayed, the related `Entity` and select `Automatically`:

![SentinelOne Deep Visibility Intake creation](/assets/operation_center/integration_catalog/endpoint/sentinelone/sentinelone_dv_edr_auto.png){: style="max-width:60%"}

5. Fulfil the SentinelOne information that you collected with your SentinelOne Point of Contact:

![SentinelOne Deep Visibility secret](/assets/operation_center/integration_catalog/endpoint/sentinelone/sentinelone_dv_edr_kafka.png){: style="max-width:60%"}
