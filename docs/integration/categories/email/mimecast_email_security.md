uuid: 041e915e-2fb6-4604-9b24-902c9daa2d3c
name: Mimecast Email Security
type: intake

## Overview
A secure email gateway to block spam, viruses, and malware.

- **Vendor**: Mimecast
- **Plan**: Defend Prime
- **Supported environment**: On Cloud / On Premise
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway
- **Coverage Score**: 3

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Configure

### Create API credentials

1. Login to **Mimecast Administration Console**
2. Navigate to **Services | API and Platform Integrations**
3. Locate the following **Mimecast API 2.0** tile and click on **Generate Keys.**
4. After reading the **Terms & Conditions**, complete the **I accept** check box to enable the **Next** button to progress onto the next step.
5. Complete the **Application Details** section.
6. Please provide details for a **Technical Point of Contact**.
7. Review the Summary information for the API application and click on **Add** if you are happy to proceed with creating the application.
8. The wizard completes and displays a pop-up window including your `Client ID` and `Client Secret` key data.

### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Mimecast Email Security`.
2. Copy the associated Intake key

### Pull your logs on Sekoia.io

Go to the Sekoia.io [playbook page](https://app.sekoia.io/operations/playbooks), and follow these steps:

- Click on **+ PLAYBOOK** button to create a new one
- Select **Create a playbook from scratch**
- Give it a name in the field **Name**
- Open the left panel, click **Mimecast** then select the trigger `[BETA] Fetch new email events from Mimecast`
- Click on **Create**

- Create a **Module configuration** using your `Client ID` and `Client Secret` created on the *How to create API credentials* step. Name the module configuration as you wish
- Create a **Trigger configuration** and Type the `Intake key` created on the previous step
- Click on the **Save** button
- **Activate the playbook** with the toggle button on the top right corner of the page

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/041e915e-2fb6-4604-9b24-902c9daa2d3c_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_041e915e-2fb6-4604-9b24-902c9daa2d3c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/041e915e-2fb6-4604-9b24-902c9daa2d3c.md!}

## Further Readings
- [Create API 2.0 Application](https://community.mimecast.com/s/article/api-integrations-managing-api-2-0-for-cloud-gateway)
