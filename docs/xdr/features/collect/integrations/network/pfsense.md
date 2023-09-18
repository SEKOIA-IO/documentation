name: pfSense
type: intake

## Overview

pfSense is a firewall software distribution based on FreeBSD.

This intake ingest filterlog from pfSense.

{!_shared_content/operations_center/detection/generated/suggested_rules_8510051d-c7cf-4b0c-a398-031afe91faa0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8510051d-c7cf-4b0c-a398-031afe91faa0.md!}

## Configure

This setup guide will show you how to forward your Firewall logs
to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator

### Enable Syslog forwarding

1. Follow the [official guide](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/remote.html) to enable syslog forwarding from your pfSense firewall to the internal log concentrator.

2. Define your log concentrator as a remote syslog server and select `Firewall Events` as the remote syslog content.

3. Save your changes.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `OpenBSD Packet Filter`.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.





