uuid: 924470a7-ab0f-49e9-a9c2-d8d15c4fe78f
name: Olfeo Secure Web Gateway
type: intake

## Overview

Olfeo Secure Web Gateway is a web gateway offering malware detection, threat prevention and reputation filtering.
This product is supported by Olfeo.


{!_shared_content/operations_center/detection/generated/suggested_rules_924470a7-ab0f-49e9-a9c2-d8d15c4fe78f_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/924470a7-ab0f-49e9-a9c2-d8d15c4fe78f.md!}

## Configure

This setup guide will show you how to forward your Olfeo Secure Web Gateway logs
to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator

### Enable Syslog forwarding

To enable syslog forwarding:

1. Log in your Olfeo web interface.
2. Go to `Parameters > Monitoring > Syslog.`.
3. Click on `add a syslog` button.
4. Add `label, description and server adress`.
5. Click on `Create`.

Olfeo forward syslogs in UDP on port 514. You must setup your internal log concentrator to listen on this port and forward logs to Sekoia.io.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Olfeo Secure Web Gateway`.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.