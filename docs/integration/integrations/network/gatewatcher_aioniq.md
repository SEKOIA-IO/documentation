uuid: bba2bed2-d925-440f-a0ce-dbcae04eaf26
name: Gatewatcher AionIQ
type: intake

## Overview

Gatewatcher AionIQ is a detection and response platform for your network that identifies malicious actions and suspicious behaviors.

{!_shared_content/operations_center/integrations/generated/bba2bed2-d925-440f-a0ce-dbcae04eaf26.md!}


## Configure

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

Log on your GCenter and follow [this guide](https://docs.gatewatcher.com/en/gcenter/2.5.3/101/itg-ext/syslog.html) to enable syslog forwarding.
Set the hostname to your log concentrator and the port number to `514`.
Select `json` as the codec, `5424` as RFC and `tcp` as the protocol.

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Gatewatcher AionIQ.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

## Further Readings
- [GCenter Syslog configuration overview](https://docs.gatewatcher.com/en/gcenter/2.5.3/101/itg-ext/syslog.html)
