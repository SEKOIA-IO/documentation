uuid: 954a6488-6394-4385-8427-621541e881d5
name: Trellix EDR
type: intake

## Overview
- **Vendor**:
- **Plan**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

Trellix has been involved in the detection and prevention of major cybersecurity attacks. It provides hardware, software, and services to investigate cybersecurity attacks, protect against malicious software, and analyze IT security risks.
    


## Configure

This setup guide will show you how to forward your Trellix EDR events to Sekoia.io.

### Configure OAuth

1. Get `client_id`, `client_secret` and `x-api-token` from your Trellix profile. Ensure that the following scopes are associated to your credentials: soc.act.tg
2. Make sure you have access to events by making a request from the [documentation](https://developer.manage.trellix.com/mvision/apis/threats)

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Trellix EDR. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Trellix](../../../automate/library/trellix.md) trigger
2. Set up the module configuration with the Client Id and Client Secret. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events

{!_shared_content/operations_center/integrations/generated/954a6488-6394-4385-8427-621541e881d5_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_954a6488-6394-4385-8427-621541e881d5_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/954a6488-6394-4385-8427-621541e881d5.md!}

