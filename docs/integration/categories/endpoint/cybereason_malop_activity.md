---
uuid: 0de050fb-3f56-4c7a-a9b6-76bf5298a617
title: Cybereason MalOp activity
name: Cybereason MalOp activity
type: intake
---

## Overview

Cybereason offers a set of Endpoint Detection and Response (EDR) solutions. Through the Cybereason platform, all suspicious operations will be gathered in MalOps, a multi-stage visualizations of device activities.

- **Vendor**: Cybereason
- **Supported environment**: SaaS
- **Detection based on**: Telemetry

Please find below information available in MalOp activities:

- the list of affected machines
- the list of affected users
- all suspicious network connections
- all suspicious executions


## Configure

This setup guide will lead you into forwarding all MalOp activities to Sekoia.io.

### Create your intake

On Sekoia.io, go to the [Intakes page](https://app.sekoia.io/operations/intakes/new) and generate a new intake with the `Cybereason MalOp Activities` format.
Keep aside the intake key.

### Setup the Syslog collector

Check the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to install and set up the syslog collector.

Once the setup has completed, write down the IP address and port. This information will be used in the next step.

### Setup the CybeReason CEF Forwarder

Contact the Cybereason Customer Success Manager to get the Cybereason CEF Forwarder.

Connect to the [Cybereason Partner Nest](https://nest.cybereason.com/user/login) and follow [these instructions](https://nest.cybereason.com/s/article/arcsight-configure) for the installation of the CEF forwarder.

Create or edit the configuration file (e.g: `cybereason-forwarders/config/sample_config.json`) and fill `host` and `port` with the address and the listening port of the syslog collector.

### Rebuild the Docker image

To apply the new configuration, you need to rebuild the Docker image of the Cybereason CEF Forwarder.

```bash
$ cd cybereason-forwarders/docker/
$ docker-compose build --build-arg COMPOSE_MODULE_NAME=cybereason-arcsight
```

### Start the forwarding

Start the CEF Forwarder

```bash
$ cd cybereason-forwarders/docker/
$ ./deploy_stack.sh docker-stack.yml CYBEREASON
```

### Enjoy your events

Go to the [Events page](https://app.sekoia.io/operations/events) and wait for your incoming events!

{!_shared_content/operations_center/integrations/generated/0de050fb-3f56-4c7a-a9b6-76bf5298a617_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_0de050fb-3f56-4c7a-a9b6-76bf5298a617_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/0de050fb-3f56-4c7a-a9b6-76bf5298a617.md!}
