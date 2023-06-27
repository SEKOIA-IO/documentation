uuid: ba40ab72-1456-11ee-be56-0242ac120002
name: Trellix ePO
type: intake

## Overview

Trellix ePO - On-prem monitors and manages your network, collects data on events and alerts, creates reports, and automates workflow to streamline product deployments, patch installations, and security updates. As an open and comprehensive platform, Trellix ePO - On-prem integrates more than 150 third-party solutions for faster and more accurate responses.

{!_shared_content/operations_center/detection/generated/suggested_rules_ba40ab72-1456-11ee-be56-0242ac120002_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ba40ab72-1456-11ee-be56-0242ac120002.md!}

## Configure

This setup guide will show you how to forward your Trellix ePO events to SEKOIA.IO.

### Configure OAuth

1. Get `client_id`, `client_secret` and `x-api-token` from your Trellix profile.
2. Make sure you have access to events from [apidoc](https://developer.manage.trellix.com/mvision/apis/v2-events)

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Trellix. Copy the intake key.

### Pull events

To start to pull events, you have to:
1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Trellix](../../../automate/library/trellix_epo.md) trigger
2. Set up the module configuration with the Client Id and Client Secret. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events

### Transport to SEKOIA.IO

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_docker_concentrator/) documentation to forward these logs to SEKOIA.IO.
