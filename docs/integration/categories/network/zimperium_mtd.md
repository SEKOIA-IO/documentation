uuid: a39e2515-a65b-42db-ab61-7785c8809c27
name: Zimperium Mobile Threat Defense - Threats
type: intake

## Overview
Zimperium Mobile Threat Defense (MTD) is an AI-powered security solution that provides real-time, on-device protection for iOS, Android, and ChromeOS devices. Using machine learning, it detects and remediates advanced threats across four key vectors : device, network, phishing, and applications, even when the device is offline. Designed for the enterprise, it secures both corporate and BYOD endpoints without compromising user privacy or battery life.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Vendor**: Zimperium
- **Detection based on**: Telemetry
- **Supported application or feature**: Threats

## Configure

### Create API keys

1. Click on the wheel in the upper right corner of your Zimperium console

    ![Management](/assets/integration/network/zimperium/management.png){ align=center width=100% }

2. Go to `Authorizations`, click on the `+ Generate API key` in the top right corner.
3. Choose `MTD` tab and check `View` in `Threats` group.

    ![Permissions](/assets/integration/network/zimperium/permission_threats.png){ align=center width=100% }

4. Be careful to save your secret key, as it will not be displayed again. However, you could always generate a new one here.

### Create an Intake

1. Navigate to the [Intake page](https://app.sekoia.io/operations/intakes) in Sekoia.io.  
2. Click **Create Intake** and select **Zimperium Mobile Threat Defense** from the dropdown.
3. Set up the intake configuration with client id and client secret acquired in the previous step.

{!_shared_content/operations_center/integrations/generated/a39e2515-a65b-42db-ab61-7785c8809c27_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a39e2515-a65b-42db-ab61-7785c8809c27_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a39e2515-a65b-42db-ab61-7785c8809c27.md!}
