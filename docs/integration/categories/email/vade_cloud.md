uuid: 838ed6e5-6d5e-4a5b-b079-ab35ac6b2ab9
name: Vade Cloud
type: intake

## Overview

Vade Cloud offers all protections against threats for any email inbox.

In this documentation we will explain how to collect and send Vade Cloud logs to SEKOIA.IO.

- **Vendor**: Vade
- **Supported environment**: Cloud
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway, Anti-virus


## Configure

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Vade Cloud`. Copy the **intake key**.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the `Fetch new logs from Vade Cloud` trigger
2. Set up the module configuration with the:

     - Vade Cloud API hostname: the URL of your admin interface of Vade Cloud. Most of the time this is `https://cloud.vadesecure.com`; TO BE ADAPTED depending on your context.
     - The email of the user: the login you use to connect to the admin interface of Vade Cloud. The account type **MUST** be "Admin".
     - The user password: the password you use to connect to the admin interface of Vade Cloud.

3. Set up the trigger configuration with the **intake key** from the previous step.
4. Start the playbook and enjoy your events

!!! Info
     Please make sure that the login is your account email.

!!! Info
     The events collection will not take events older than 7 days into account.

{!_shared_content/operations_center/integrations/generated/838ed6e5-6d5e-4a5b-b079-ab35ac6b2ab9_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_838ed6e5-6d5e-4a5b-b079-ab35ac6b2ab9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/838ed6e5-6d5e-4a5b-b079-ab35ac6b2ab9.md!}