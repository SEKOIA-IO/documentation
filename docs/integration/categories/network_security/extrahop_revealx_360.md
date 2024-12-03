uuid: 1df44c62-33d3-41d4-8176-f1fa13589eea
name: ExtraHop Reveal(x) 360
type: intake

## Overview

ExtraHop Reveal(x) 360 is a cloud-based network detection and response platform offering protection and detections for on-premises and cloud environments. In this documentation we will explain how to collect and send Reveal(x) 360 events to Sekoia.io.

- **Vendor**: ExtraHop
- **Supported environment**: Cloud
- **Detection based on**: Telemetry, Alert

## Configure

### Prerequisites
- System and access administration privileges for ExtraHop Reveal(x) 360
- Access to Sekoia.io Intakes and Playbook pages with write permissions

### How to create REST API credentials
1. Log in to Reveal(x) 360.
2. Click the System Settings icon  at the top right of the page and then click **All Administration**.
3. Click **API Access**.
4. Click **Create Credentials**.
5. In the **Name** field, type a name for the credentials.
6. In the **Privileges** field, specify a privilege level for the credentials.

!!! Note
    The privilege level determines which actions can be performed with the credential. Do not grant more privileges to REST API credentials than needed because it can create a security risk. For example, applications that only retrieve metrics should not be granted credentials that grant administrative privileges. For more information about each privilege level, see [User privileges](https://docs.extrahop.com/9.5/users-overview/#user-privileges).

!!! Note
    System and Access Administration privileges are similar to Full write privileges and allow the credentials to connect self-managed sensors and Trace appliances to Reveal(x) 360.

7. In the **Packet Access** field, specify whether you can retrieve packets and session keys with the credentials. 
8. Click **Save**.
   The Copy REST API Credentials pane appears.
9. Under ID, click **Copy to Clipboard** and save the ID to your local machine.
10. Under Secret, click **Copy to Clipboard** and save the secret to your local machine.

!!! Important
    The secret cannot be viewed or retrieved later.

12. Click **Done**.


### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `ExtraHop Reveal(x) 360`.
2. Set the intake account configuration using your REST API credentials created on the *How to create REST API credentials* step.

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/1df44c62-33d3-41d4-8176-f1fa13589eea_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_1df44c62-33d3-41d4-8176-f1fa13589eea_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/1df44c62-33d3-41d4-8176-f1fa13589eea.md!}
