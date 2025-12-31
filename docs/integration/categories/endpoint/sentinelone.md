---
uuid: 07c556c0-0675-478c-9803-e7990afe78b6
title: SentinelOne
name: SentinelOne
type: intake
---

## Overview

SentinelOne is an Endpoint Detection and Response (EDR) solution. By using the standard SentinelOne EDR logs collection by API, you will be provided with high-level information on the detection and investigation of your EDR.

- **Vendor**: SentinelOne
- **Supported environment**: Cloud
- **Detection based on**: Alert

Please find below a limited list of field types that are available with SentinelOne default EDR logs:

- Information about the Endpoint
- Information about the SentinelOne agent installed
- Activity type and its description (authentication access, user management, 2FA setup, etc.)

Depending on the context of the log, additional content could be available, such as:

- Process information
- Network information
- File information

!!! Tip
    For advanced log collection, we suggest you use the SentinelOne Cloud Funnel 2.0 option, as described in the [SentinelOne Cloud Funnel 2.0 integration](/integration/categories/endpoint/sentinelone_cloudfunnel2.0.md).


## Configure

This setup guide will show you how to pull events produced by SentinelOne EDR on [Sekoia.io](https://app.sekoia.io/). To collect the SentinelOne logs, you must generate an API token from the SentinelOne Management Console. We recommend creating a Service User to use a dedicated account for the integration.

**Important**: If you have multiple SentinelOne Management Consoles, you must generate an API Token for each one.

!!! note
    The API token you generate is time-limited. To generate a new token (and invalidate the old one), you will need to copy the Service User. Please refer to the SentinelOne documentation to obtain guidance on how to do this action.

1. In the SentinelOne management console, go to `Settings`, select `USERS`, and then select `Service Users`.
2. Create a new `Service User` by specifying a name and an expiration date.
3. Choose the `Scope` of the `Service User`: `Global`, `Account` or `Site`, select the appropriate `Account(s)` or `Site(s)` and the role to grant to the `Service User`
4. Select `Create User` and copy the generated API token.

!!! note
    A `Service User` with the `Site Admin` or `IR Team` role can mitigate threats from [Sekoia.io](https://app.sekoia.io/) using [SentinelOne playbook actions](/xdr/features/automate/library/sentinelone.md). A user with the `Site Viewer` role can view activity events and threats but cannot take action.

## Create a SentinelOne intake

In the [Sekoia.io Operation Center](https://app.sekoia.io/operations/intakes):

1. Go to the `Intakes` page.
2. Search for `SentinelOne` by navigating the page or using the search bar.
3. Click `Create` under the relevant object (SentinelOne EDR or SentinelOne Cloud Funnel).
4. Enter the `Name` of your intake that will be displayed, select the related `Entity` from the dropdown, and then select `Automatically`:

![SentinelOne EDR Intake creation](/assets/integration/endpoint/sentinelone/sentinelone-configure-intake.png){: style="max-width:60%"}

5. Enter the previously downloaded SentinelOne `API token` and the related `URL Domain`:

![SentinelOne EDR secret](/assets/integration/endpoint/sentinelone/sentinelone_edr_api.png){: style="max-width:60%"}

{!_shared_content/operations_center/integrations/generated/07c556c0-0675-478c-9803-e7990afe78b6_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_07c556c0-0675-478c-9803-e7990afe78b6_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/07c556c0-0675-478c-9803-e7990afe78b6.md!}
