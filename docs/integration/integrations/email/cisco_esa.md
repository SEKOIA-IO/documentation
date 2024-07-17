uuid: 2ee6048e-8322-4575-8e47-1574946412b6
name: Cisco Email Security Appliance
type: intake

## Overview

Cisco Email Security Appliance (ESA) is a email gateway appliance that provides protection against spam, malware, viruses, and other email threats.

{!_shared_content/operations_center/detection/generated/suggested_rules_2ee6048e-8322-4575-8e47-1574946412b6_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2ee6048e-8322-4575-8e47-1574946412b6.md!}

## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

To enable log forwarding:

1. Log in your Cisco appliance
2. Go to `System Administration > Log Subscriptions`
3. In `Add Log Subscription`, Select `Consolidated Event Logs` as the log type
4. Select the fields that you want in the consolidated event logs
5. In `Retrieval Method`, Check `Syslog Push` and fill the form with the ip address and the port of your log concentrator
6. Submit and commit your changes

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Cisco Email Security Appliance`.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

## Further Readings
- [Single Log Line (SLL)](https://docs.ces.cisco.com/docs/single-log-line-sll)
