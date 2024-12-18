uuid: 547234b3-82ea-4507-b28f-3ee3cd5b9a8e
name: Cisco Duo Security
type: intake


## Overview

Cisco Duo Security offers solutions for strong authentication.

- **Vendor**: Cisco
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication logs

## Configure

### Generate Credentials

1. [Sign up for a Duo account](https://signup.duo.com/).
2. Log in to the [Duo Admin Panel](https://admin.duosecurity.com/) and navigate to **Applications**.
3. Click **Protect an Application** and locate the entry for **Admin API** in the applications list. Click Protect to the far-right to configure the application and get your **integration key, secret key, and API hostname**. You'll need this information to complete your setup.
4. Check **Grant read log** permission
5. Click **Save changes**

More details in [Duo documentation](https://duo.com/docs/adminapi#first-steps)

### Create the intake in Sekoia.io

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Cisco Duo Security`.
2. Set up the intake account configuration with the Hostname, Integration Key and Secret Key

{!_shared_content/operations_center/integrations/generated/547234b3-82ea-4507-b28f-3ee3cd5b9a8e_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_547234b3-82ea-4507-b28f-3ee3cd5b9a8e_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/547234b3-82ea-4507-b28f-3ee3cd5b9a8e.md!}