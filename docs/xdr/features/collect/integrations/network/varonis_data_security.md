uuid: 7b75d498-4a65-4d44-aa81-31090d723a60
name: Varonis Data Security
type: intake

## Overview

Varonis offers solutions to track and protect data.


!!! warning
    This format is still in beta, please use it wisely.

{!_shared_content/operations_center/detection/generated/suggested_rules_7b75d498-4a65-4d44-aa81-31090d723a60_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/7b75d498-4a65-4d44-aa81-31090d723a60.md!}

## Configure

This setup guide will show you how to forward your Varonis Data Security logs
to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator (Rsyslog)

### Enable Syslog forwarding for Varonis Data Security

You can configure the Syslog server address in DatAlert so that alerts are sent to SEKOIA. To configure the
Syslog server address in DatAlert:

1. In DatAdvantage, select Tools > DatAlert. DatAlert is displayed.
2. From the left menu, select Configuration.
3. In Syslog Message Forwarding fill the Syslog server IP address and the Port with the ip address and the port of the log concentrator.
4. Click OK

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Varonis Data Security

### Transport to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_docker_concentrator/) documentation to forward these logs to Sekoia.io.
