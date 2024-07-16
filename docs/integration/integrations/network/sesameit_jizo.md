uuid: 46e14ac3-0b79-42d6-8630-da4fcdb8d5f1
name: Sesame it Jizo NDR
type: intake

## Overview
Sesame it Jizo NDR is a network observability platform that enables decision-makers to anticipate, identify and block cyber-attacks.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.


{!_shared_content/operations_center/detection/generated/suggested_rules_46e14ac3-0b79-42d6-8630-da4fcdb8d5f1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/46e14ac3-0b79-42d6-8630-da4fcdb8d5f1.md!}


## Configure

In this guide, you will configure the Jizo NDR to forward events to syslog.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.

### Configure log settings

1. Log into jizo console
2. Configure Syslog Primary to receive alerts Logs

   ```shell
   syslog_conf set <log concentrator server ip> <PROTOCOL> <log concentrator port> 2
   ```

   with <Protocol> for protocol (tcp or udp) used to send Logs and 2 to indicate first IdsLog (syslog primary)


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Sesame it Jizo NDR`.


## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
