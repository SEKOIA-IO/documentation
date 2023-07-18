uuid: 07c556c0-0675-478c-9803-e7990afe78b6
name: SentinelOne
type: intake

## Overview

SentinelOne is an Endpoint Detection and Response (EDR) solution. By using the standard SentinelOne EDR logs collection by API, you will be provided with high level information on detection and investigation of your EDR.

Please find bellow a limited list of field types that are available with SentinelOne default EDR logs:

- Information about the Endpoint
- Information about the SentinelOne agent installed
- Activity type and its description (authentication access, user management, 2FA setup...)

And depending on the context of the log, additional content could be available, such as:

- Process information
- Network information
- File information

!!! Tip
    For advanced log collection, we suggest you to use SentinelOne Cloud Funnel 2.0 option, as described offered by the [SentinelOne Cloud Funnel 2.0 integration](sentinelone_cloudfunnel2.0.md).


{!_shared_content/operations_center/detection/generated/suggested_rules_07c556c0-0675-478c-9803-e7990afe78b6_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/07c556c0-0675-478c-9803-e7990afe78b6.md!}

## Configure

This setup guide will show you how to pull events produced by SentinelOne EDR on [SEKOIA.IO](https://app.sekoia.io/). To collect the SentinelOne logs, you must generate an API token from the SentinelOne Management Console. We recommend creating a Service User to use a dedicated account for the integration.

**Important**: If you have multiple SentinelOne Management Consoles, you must generate an API Token for each one.

!!! note
    The API token you generate is time limited. To regenerate a new token (and invalidate the old one), you will need to copy the Service User. Please refer to the SentinelOne documentation to obtain guidance on how to do this action.

1. In the SentinelOne management console, go to `Settings`, click on `USERS` and then on `Service Users`.
2. Create a new `Service User` by specifying a name and an expiration date.
3. Choose the `Scope` of the `Service User`: `Global`, `Account` or `Site`, select the appropriate `Account(s)` or `Site(s)` and the role to grant to the `Service User`
4. Click on `Create User` and copy the API token generated.

!!! note
    A `Service User` with a role of `Site Admin` or `IR Team` can mitigate threats from [Sekoia.io](https://app.sekoia.io/) using [SentinelOne playbook actions](../../../automate/library/sentinel-one.md). A user with a role of `Site Viewer` can view activity events and threats but cannot take action.

## Create a SentinelOne intake

In the [SEKOIA.IO Operation Center](https://app.sekoia.io/operations/intakes):

1. Click on the `Intake` page.
2. Search for `SentinelOne` by navigating the page or using the search bar.
3. Click `Create` on the relevant object.
4. Fulfil the `Name` of your intake that will be displayed, the related `Entity` and select `Automatically`:

![SentinelOne EDR Intake creation](/assets/operation_center/integration_catalog/endpoint/sentinelone/sentinelone_edr_auto.png){: style="max-width:60%"}

5. Fulfil the SentinelOne `API token` previously downloaded and the related `URL Domain`:

![SentinelOne EDR secret](/assets/operation_center/integration_catalog/endpoint/sentinelone/sentinelone_edr_api.png){: style="max-width:60%"}
