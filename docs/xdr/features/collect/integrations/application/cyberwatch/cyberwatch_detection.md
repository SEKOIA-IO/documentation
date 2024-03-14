uuid: 687993b4-2b9b-4a53-bb40-8729fa17638c
name: Cyberwatch Detection
type: intake

## Overview
Cyberwatch is a vulnerability detection and monitoring solution.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

{!_shared_content/operations_center/detection/generated/suggested_rules_687993b4-2b9b-4a53-bb40-8729fa17638c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/687993b4-2b9b-4a53-bb40-8729fa17638c.md!}

## Configure

This setup guide will show you how to forward your Cyberwatch logs to Sekoia.io by means of a syslog transport channel.

### Enable Syslog forwarding for Cyberwatch

Once configured, Cyberwatch will send hourly the latest CVEs detected to the remote Syslog server

1. Click Administration
2. Click External tools
3. Click Remote Syslog server

In the Remote Syslog server configuration, provide the address, the port and the transport to the syslog concentrator 

<video controls width="100%">
  <source src="/assets/operation_center/integration_catalog/application/cyberwatch/Cyberwatch.webm" type="video/webm">
</video>

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cyberwatch Detection.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/sekoiaio_forwarder/) documentation to set up the syslog concentrator.


## Further readings

- [Configure a remote Syslog server](https://docs.cyberwatch.fr/help/en/administration/remote_syslog_configuration/)
