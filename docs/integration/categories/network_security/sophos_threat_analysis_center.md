---
uuid: 99da26fc-bf7b-4e5b-a76c-408472fcfebb
title: Sophos Threat Analysis Center
name: Sophos Threat Analysis Center
type: intake
---

## Overview

The Sophos Threat Analysis Center (STAC), is a dedicated tool for research and analysis of cybersecurity threats. so it can help continuously on monitoring the cyber threat landscape and analyze new forms of malware, attack techniques, and cybercrime trends. which has also the most important part which the _live Discover_ , with usage of queries you can have device informations from Sophos data lake.

- **Vendor**: Sophos
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: File monitoring, Process monitoring, Process use of network




## Configure

### Prerequisites

You can find the system requirements for each respective platform below : <br />

- [Windows Requirements](https://support.sophos.com/support/s/article/KB-000035144?language=en_US)
- [Windows Server Requirements](https://support.sophos.com/support/s/article/KBA-000003024?language=en_US)
- [MacOS Requirements](https://support.sophos.com/support/s/article/KB-000034670?language=en_US)

!!! Warning
    It's also necessary to know that you have to install Sophos agents on the necessary machines.

### Create Sophos Threat Analysis Center Credentials

In the Sophos Central Admin console:

1. Go to `Global Settings` > `API Credentials Management`.
2. Click `Add Credential` and give the credential a name and description.
3. Choose which role you want to assign. You can choose from the following roles:
    - Service Principal Super Admin: Users with this role can perform all API operations with full CRUD (Create Read Update Delete) capabilities and have access to queries.
    - Service Principal Forensics: Users with this role can create, view, run, and delete Live Discover queries.
4. Click `Add`.

This generates the credential, together with a Client ID and a Client Secret.
Copy the Client ID and Client Secret.

### Enable logs to Sophos data lake

By default sophos central will not send logs to the Data Lake automatically, so you have to do it manually. you will need to enable hydration for both Endpoints and Servers as you want.

To enable hydrating the data lake for endpoint:

1. Click **Endpoint Protection**
2. Click **Settings**
3. Scroll down and click **Data Lake uploads**
4. Toggle the switch to enable **Upload to the Data Lake**
5. (OPTIONAL) - if you want to exclude any devices, select them from the available list and move them to the excluded list

To enable hydrating the data lake for server:

1. Click **Server Protection**
2. Click **Settings**
3. Scroll down and click **Data Lake uploads**
4. Toggle the switch to enable **Upload to the Data Lake**
5. **(OPTIONAL)** - if you want to exclude any devices, select them from the available list and move them to the excluded list

## Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Sophos Analysis Threat Center.
2. Set the intake account configuration with the `client_id` and `client_secret` from the Sophos console.

    !!! info
        - If you want to change the region with your own region, you can find your region via **protect devices field**, first click on **Protect Devices**, Then copy link of any download links and finally Check the region that appears as part of the URL.
        - No need to change the **Oauth2 Authorization Url** for the moment (this's the only endpoint to get a JWT token).

3. In the intake configuration section choose a `frequency` - Default is `60` -.


{!_shared_content/operations_center/integrations/generated/99da26fc-bf7b-4e5b-a76c-408472fcfebb_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_99da26fc-bf7b-4e5b-a76c-408472fcfebb_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/99da26fc-bf7b-4e5b-a76c-408472fcfebb.md!}

## Further Readings

- [Sophos Analysis Threat Center documentation](https://doc.sophos.com/central/customer/help/en-us/ManageYourProducts/ThreatAnalysisCenter/index.html)
- [Sophos Analysis Threat Center guide](https://community.sophos.com/intercept-x-endpoint/f/recommended-reads/130364/getting-started-with-sophos-xdr-data-lake-hydration)
- [Identify your region](https://support.sophos.com/support/s/article/KB-000044836?language=en_US)
