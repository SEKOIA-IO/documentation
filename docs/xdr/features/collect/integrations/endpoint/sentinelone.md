uuid: d8f6faa5-eb3d-4621-87f6-6903d4f80b3b
name: SentinelOne
type: intake

## Overview

SentinelOne is an Endpoint Detection and Response (EDR) solution. By using the standard SentinelOne EDR logs collection by API, you will be provided with high level information on detection and investigation of your EDR.

Please find bellow a limited list of field types that are available with SentinelOne default EDR logs:

- Information about the Endpoint
- Information about the SentinelOne agent installed
- Activity type and its description

And depending on the context of the log, additional content could be available, such as:

- Process information
- Network information
- File information

> For advanced log collection, we suggest you to use SentinelOne Deep Visibility kafka option, as described offered by the [SentinelOne DeepVisibility intergration](sentinelone_deepvisibility.md).

{!xdr/features/collect/integrations/generated/sentinelone_do_not_edit_manually.md!}

## Configure

This setup guide will show you how to pull events produced by SentinelOne EDR on [SEKOIA.IO](https://app.sekoia.io/). To collect the SentinelOne logs, you must generate an API token from the SentinelOne Management Console

**Important**: If you have multiple SentinelOne Management Consoles, you must generate an API Token for each one.

> The API token you generate is time limited. To regenerate a new token (and invalidate the old one), log in with the dedicated SentinelOne account. You do not need to create a new account.

1. In the SentinelOne management console, go to `Settings`, and then click `USERS`.
2. Click on the `Admin user` for which you want to generate the API token.

**Note**: A user with a role of "Site Admin" can mitigate threats from the [SEKOIA.IO](https://app.sekoia.io/). A user with a role of "Site Viewer" can view threats but cannot take action.
**Note**: You can generate a token only for your own user.

3. Click `Generate` next to API Token. It shows the token string and the date that the token expires.
4. Copy the token or click `Download` to save it.

## Create a SentinelOne intake

In the [SEKOIA.IO Operation Center](https://app.sekoia.io/operations/intakes):

1. Click on the `Intake` page.
2. Search for `SentinelOne` by navigating the page or using the search bar.
3. Click `Create` on the relevant object.
4. Fulfil the `Name` of your intake that will be displayed, the related `Entity` and select `Automatically`:

![SentinelOne EDR Intake creation](/assets/operation_center/integration_catalog/endpoint/sentinelone/sentinelone_edr_auto.png){: style="max-width:60%"}

5. Fulfil the SentinelOne `API token` previously downloaded and the related `URL Domain`:

![SentinelOne EDR secret](/assets/operation_center/integration_catalog/endpoint/sentinelone/sentinelone_edr_api.png){: style="max-width:60%"}
