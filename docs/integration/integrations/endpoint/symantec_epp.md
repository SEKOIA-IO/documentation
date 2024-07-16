uuid: 419bd705-fa61-496c-94fa-28d6c1f2e2a8
name: Symantec Endpoint Protection
type: intake

## Overview
Symantec Endpoint Protection is a client-server solution that protects laptops, desktops, and servers in your network against malware, risks, and vulnerabilities.
This product is supported by Broadcom.

{!_shared_content/operations_center/detection/generated/suggested_rules_419bd705-fa61-496c-94fa-28d6c1f2e2a8_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/419bd705-fa61-496c-94fa-28d6c1f2e2a8.md!}

## Configure

In this guide, you will configure your Symantec Endpoint Protection Manager or your Symantec Endpoint Security to forward events through syslog.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

Log on the console of our management server and follow [this guide](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/Monitoring-Reporting-and-Enforcing-Compliance/viewing-logs-v7522439-d37e464/exporting-data-to-a-syslog-server-v8442743-d15e1107.html) to enable logs forwarding and provide the IP, the transport protocol (we are recommending `TCP`) and the listening port (`514`) of the concentrator.

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Symantec Endpoint Protection.


## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
