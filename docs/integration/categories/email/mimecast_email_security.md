uuid: 041e915e-2fb6-4604-9b24-902c9daa2d3c
name: Mimecast Email Security
type: intake

## Overview
A secure email gateway to block spam, viruses, and malware.

- **Vendor**: Mimecast
- **Supported environment**: Cloud
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway


!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## High-Level Architecture Diagram

- **Type of integration**: PULL by Sekoia.io
- **Schema**

![mimecast_es_architecture](/assets/integration/mimecast_es_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Permissions**:
    - The Mimecast administrator must be assigned a Role with the following criteria.
        - Read and Edit API Application Permissions under the Service Menu.
        - Security Permissions setting must permit the Management of Application Roles.
    - The generated API key must be a Mimecast Administrator with at least the Security Events and Data Retrieval | Threat and Security Events (SIEM) and Threat and security statistics | Read permission.

### Transport Protocol/Method

- **Direct HTTP**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Create API credentials

1. Login to **Mimecast Administration Console**
2. Navigate to **Account** > **Roles** > **New Role**
3. Name the role as you wish, for instance "Sekoia"
4. Add the following roles under the section called **Security Events and Data Retrieval**:
    - **Threat and security svents (SIEM)** with READ permission,
    - **Threat and security statistics** with READ permission.
5. Navigate to **Services | API and Platform Integrations**
6. Locate the following **Mimecast API 2.0** tile and click on **Generate Keys.**
7. After reading the **Terms & Conditions**, complete the **I accept** check box to enable the **Next** button to progress onto the next step.
8. Complete the **Application Details** section by providing:
    - Application Name: Select **SIEM Integration**,
    - Description (Optional),
    - Integration Partner (Optional),
    - Products: Select all products,
    - Role: Select the "Sekoia" role created above.
9. Complete the **Notifications** section by providing:
    - Technical Point of Contact: Write the name of the administrator to be contacted if you encounter any issue with the API,
    - Email : Write the administrator's email.
10. Validate the form and Click on **Add and Generate Keys**
11. The wizard completes and displays a pop-up window including your `Client ID` and `Client Secret` key data.

### Instruction on Sekoia
#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Mimecast Email Security`.
2. Copy the associated Intake key

#### Pull your logs on Sekoia.io

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

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_041e915e-2fb6-4604-9b24-902c9daa2d3c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/041e915e-2fb6-4604-9b24-902c9daa2d3c.md!}

## Further Readings
- [Create API 2.0 Application](https://community.mimecast.com/s/article/api-integrations-managing-api-2-0-for-cloud-gateway)
