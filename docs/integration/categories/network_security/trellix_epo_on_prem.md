uuid: 448f83c3-623d-4a07-a1d4-a1f96be1519b
name: Trellix ePO (on-prem)
type: intake

## Overview

Trellix ePO is a centralized security management platform to orchestrate and manage all endpoints.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.


- **Vendor**: Trellix
- **Supported environment**: On Prem
- **Version compatibility**: 5.10
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs


## Configure

This setup guide will show you how to forward your Trellix ePO events to Sekoia.io.

### Configure a new server

1. Sign in to the **Trellix ePO** platform with administrator permissions.
2. Click  **Menu**, and then click **Configuration** > **Registered Servers**.
3. Click **New Server**.
4. On the **Description** page, configure these settings :
    1. **Server type** — Select **Syslog Server**.
    2. **Name**
5. Click **Next**.
6. On the next **Registered Server Builder** page, configure these settings
    1. **Server name**
    2. **TCP port number**
    3. **Enable event forwarding**
7. Click **Test connection**.
8. Click **Save**.

### Forward logs to Sekoia.io

For more information on forwarding logs to Sekoia.io, see [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md)

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Trellix ePO (on-prem).


{!_shared_content/operations_center/integrations/generated/448f83c3-623d-4a07-a1d4-a1f96be1519b_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_448f83c3-623d-4a07-a1d4-a1f96be1519b_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/448f83c3-623d-4a07-a1d4-a1f96be1519b.md!}
