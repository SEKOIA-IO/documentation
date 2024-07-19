uuid: ba40ab72-1456-11ee-be56-0242ac120002
name: Trellix ePO
type: intake

## Overview
  - **Vendor**:
- **Plan**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

Trellix ePO - On-prem monitors and manages your network, collects data on events and alerts, creates reports, and automates workflow to streamline product deployments, patch installations, and security updates. As an open and comprehensive platform, Trellix ePO - On-prem integrates more than 150 third-party solutions for faster and more accurate responses.

!!! warning
    Important note - This format is currently in alpha. We highly value your feedback to improve its performance.
    


## Configure

This setup guide will show you how to forward your Trellix ePO events to Sekoia.io.

### Configure OAuth

1. Get `client_id`, `client_secret` and `x-api-token` from your Trellix profile. Ensure that the following scopes are associated to your credentials: epo.evt.r, epo.pevt.r, epo.pevt.rp, epo.qery.g, epo.qery.u, epo.reg_token, epo.resp.ra, epo.resp.ru
2. Make sure you have access to events by making a request from the [documentation](https://developer.manage.trellix.com/mvision/apis/v2-events)

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Trellix. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Trellix](../../../automate/library/trellix.md) trigger
2. Set up the module configuration with the Client Id and Client Secret. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_ba40ab72-1456-11ee-be56-0242ac120002_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/ba40ab72-1456-11ee-be56-0242ac120002.md!}

