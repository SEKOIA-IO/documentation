uuid: dbebefdd-dd2e-48a9-89e6-ee5a00ee0956
name: Veeam Backup
type: intake

## Overview
- **Vendor**: Veeam
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: On-premise
- **Version compatibility**: 11 and newer
- **Detection based on**: Telemetry
- **Supported application or feature**: Application Logs

Veeam Backup & Replication is a comprehensive data protection solution known for its robust backup, recovery, and replication capabilities, ensuring the secure and efficient management of data across various environments for businesses and organizations.

## Supported versions

This integration supports the following versions:

- 12
- 12.1



## Configure

This setup guide will show you how to forward your Veeam logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable syslog forwarding

To enable syslog forwarding:

1. Open the burger menu in the Veeam Backup & Replication Console and select `Options`.

    ![step_1.png](/assets/operation_center/integration_catalog/application/veeam-backup/step_1.png)

2. In the `Options` dialog, select the `Event Forwarding` tab.

    ![step_2.png](/assets/operation_center/integration_catalog/application/veeam-backup/step_2.png)

3. Add a new syslog server.

    ![step_3.png](/assets/operation_center/integration_catalog/application/veeam-backup/step_3.png)

4. Enter the log concentrator's address and port, then select the transport protocol you need.

    ![step_4.png](/assets/operation_center/integration_catalog/application/veeam-backup/step_4.png)

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the Veeam Backup format.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/dbebefdd-dd2e-48a9-89e6-ee5a00ee0956_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_dbebefdd-dd2e-48a9-89e6-ee5a00ee0956_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/dbebefdd-dd2e-48a9-89e6-ee5a00ee0956.md!}

