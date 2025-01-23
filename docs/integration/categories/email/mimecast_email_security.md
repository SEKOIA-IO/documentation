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

#### Activate logging

1. Login to **Mimecast Administration Console**
2. Navigate to **Account** > **Account Settings** > **Enhanced Logging**
3. Select the Enhanced Logging option that you want:
![mimecast_logging](/assets/integration/mimecast_logging.png){: style="max-width:100%"}

### Instruction on Sekoia
#### Create your intake

1. Navigate to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake using the `Mimecast Email Security` integration.  
2. If you do not already have one, create an account by entering your `Client ID` and `Client Secret`. If you have an existing account, simply select it from the list.  
3. Configure the settings by choosing your preferred `Chunk Size` and `Frequency`.  
4. Copy the newly created Intake Key for use in your setup.  

!!! Note
    Mimecast provides events in batches every 15 minutes. In order to comply with the Mimecast ratelimiting (50 calls per 15 minutes), the default frequency is set to 8 minutes.


### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/041e915e-2fb6-4604-9b24-902c9daa2d3c_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_041e915e-2fb6-4604-9b24-902c9daa2d3c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/041e915e-2fb6-4604-9b24-902c9daa2d3c.md!}

## Further Readings
- [Create API 2.0 Application](https://community.mimecast.com/s/article/api-integrations-managing-api-2-0-for-cloud-gateway)
