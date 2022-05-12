uuid: 0de050fb-3f56-4c7a-a9b6-76bf5298a617
name: CybeReason MalOp
type: intake

## Overview

CybeReason offer a set of Endpoint Detection and Response (EDR) solutions. Through the CybeReason platform, all suspicious operations will be gather in MalOps, multi-stage visualizations of devices activities.

Please find bellow information available in MalOp activities:

- the list of affected machines
- the list of affected users
- all suspicious network connections
- all suspicious executions

{!operation_center/integration_catalog/generated/cybereason-malop_do_not_edit_manually.md!}

## Configure

This setup guide shows how to forward all MalOp activities to SEKOIA.IO.

### Create your intake

On SEKOIA.IO, go on the intake page and generate a new intake with the `CybeReason MalOp` format.
Keep aside the intake key.

### Setup the Syslog collector

Please, consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to install and to set up the syslog collector.

### Setup the CybeReason CEF Forwarder

Contact the CybeReason Custome Success Manager to get the CybeReason CEF Forwarder.

Connect to the [CybeReason Partner Nest](https://nest.cybereason.com/user/login) and follow [these instructions](https://nest.cybereason.com/node/3517551) for the installation of the CEF forwarder.

Create a [new configuration](https://nest.cybereason.com/node/3517426) to forward MalOp activities to the syslog collector: fill `host` and `port` with the address and the listening port of the syslog collector.

### Start the forwarding

Start the CEF Forwarder with your new configuration

```bash
$ cybereason-forwarders/scripts/run_forwarder.sh config/<my new configuration>.json
```

### Enjoy your events

Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.
