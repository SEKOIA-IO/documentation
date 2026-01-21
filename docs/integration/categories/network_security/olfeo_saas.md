---
uuid: ce4ab9ba-4ed7-420d-af30-f144229f37ee
title: Olfeo SAAS
name: Olfeo SAAS
type: intake
---

## Overview

Olfeo SaaS is a suite of cybersecurity features for analyzing, filtering and securing your web flows. Combining proxy filtering, flow antivirus and TLS decryption.

- **Vendor**: Olfeo
- **Supported environment**: SaaS
- **Version compatibility**: v3.14.0 and above
- **Detection based on**: Telemetry
- **Supported application or feature**: Network web traffic


## Specification

### Prerequisites

- **Licence**:

    - This feature requires a specific license. For more information, please contact your sales representative.

- **Permissions**:

    - Administrator rights on Olfeo SaaS

### Transport Protocol/Method

- HTTP event collector/JSON 

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Informational

## Step-by-Step Configuration Procedure

This setup guide will show you how to send your Olfeo SaaS logs to [homepage](https://www.sekoia.io/en/homepage/).

### Create a Log Connector

To create a Sekoia-type Log Connector in your SaaS  interface, follow these steps:

#### Connect a SIEM

1. Log in your Olfeo web interface.
2. Go to `Configuration > Log connector`.
3. Click the `Connect a SIEM` button in the top right of your screen.

#### Add the general Information

1. Enter the following values in the empty fields:
    - SIEM Name (< 60 characters)
    - Description (optional)
    - Connector Type (Choose Sekoia)
2. Click the `Following` button.

#### Add an endpoint URL

1.  Use the Sekoia documentation to locate and copy the public URL: [https://intake.sekoia.io/jsons](https://intake.sekoia.io/jsons)
2.  In the designated field, insert the endpoint URL.

!!!important
    Specify the sending data formats by adding /jsons to the end of the URL. 
    Follow the instructions provided on the Sekoia website.

#### Add a token authentication token

!!!important  
    The following programming code runs on Linux. You can perform the same task on Windows or macOS with few adjustments.

8. In your computer operating terminal:
    1. Paste your character strings.
    ```
    echo -n ":REPLACE_BY_INTAKE_KEY" | base64
    ```
    !!!note  
        Swap `REPLACE_BY_INTAKE_KEY` with your Sekoia-generated intake key.
    For example:
    Let's assume that:
    - **intake key**: 78Guihid-9ZE456Z-ghjk213
    
    Then, the terminal command in this scenario would be:
        ```
        echo -n ":78Guihid-9ZE456Z-ghjk213" | base64
        ```
   
    2. Copy the result.
9. In the Olfeo SaaS interface:
    1. Paste the previously obtained results into the authentication field.
10. Click the `Following` button.

#### Select data

10. Choose the data options you want to send.
11. Click `Save`

!!!note  
    Do not forget to activate the Log Connector in the list (`Configuration > Log connector`). 

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Olfeo SAAS`.
2. Set up the intake configuration. 

{!_shared_content/operations_center/integrations/generated/ce4ab9ba-4ed7-420d-af30-f144229f37ee_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ce4ab9ba-4ed7-420d-af30-f144229f37ee_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ce4ab9ba-4ed7-420d-af30-f144229f37ee.md!}
