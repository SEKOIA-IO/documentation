# veeam\_backup

uuid: dbebefdd-dd2e-48a9-89e6-ee5a00ee0956 name: Veeam Backup type: intake

### Overview

* **Vendor**: Veeam
* **Supported environment**: On-premise
* **Version compatibility**: 12 and newer
* **Detection based on**: Telemetry
* **Supported application or feature**: Application Logs

Veeam Backup & Replication is a comprehensive data protection solution known for its robust backup, recovery, and replication capabilities, ensuring the secure and efficient management of data across various environments for businesses and organizations.

### Supported versions

This integration supports the following versions:

* 12
* 12.1

### Configure

This setup guide will show you how to forward your Veeam logs to Sekoia.io by means of a syslog transport channel.

#### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

#### Enable syslog forwarding

To enable syslog forwarding:

1. Open the burger menu in the Veeam Backup & Replication Console and select `Options`.
2. In the `Options` dialog, select the `Event Forwarding` tab.
3. Add a new syslog server.
4. Enter the log concentrator's address and port, then select the transport protocol you need.

#### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the Veeam Backup format.

#### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../../integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

{!\_shared\_content/operations\_center/integrations/generated/dbebefdd-dd2e-48a9-89e6-ee5a00ee0956\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_dbebefdd-dd2e-48a9-89e6-ee5a00ee0956\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/dbebefdd-dd2e-48a9-89e6-ee5a00ee0956.md!}
