uuid: ba40ab72-1456-11ee-be56-0242ac120002
name: Trellix ePO
type: intake

## Overview

Trellix ePO monitors and manages your network, collects data on events and alerts, creates reports, and automates workflow to streamline product deployments, patch installations, and security updates. As an open and comprehensive platform, Trellix ePO integrates more than 150 third-party solutions for faster and more accurate responses.

!!! warning
    Important note - This format is currently in alpha. We highly value your feedback to improve its performance.


- **Vendor**: Trellix
- **Supported environment**: SaaS
- **Version compatibility**: 5.10
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs


## Configure

This setup guide will show you how to forward your Trellix ePO events to Sekoia.io.

### Prerequisites

- You need to have access to the Trellix developer portal to be able to configure API.

### Configure OAuth

1. Get `client_id`, `client_secret` and `x-api-token` from your Trellix profile. Ensure that the following scopes are associated to your credentials: epo.evt.r, epo.pevt.r, epo.pevt.rp, epo.qery.g, epo.qery.u, epo.reg_token, epo.resp.ra, epo.resp.ru
2. Make sure you have access to events by making a request from the [documentation](https://developer.manage.trellix.com/mvision/apis/v2-events)

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Trellix.
2. Set up the intake configuration with the Client Id and Client Secret. 

{!_shared_content/operations_center/integrations/generated/ba40ab72-1456-11ee-be56-0242ac120002_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ba40ab72-1456-11ee-be56-0242ac120002_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/ba40ab72-1456-11ee-be56-0242ac120002.md!}
