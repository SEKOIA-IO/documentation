uuid: f570dd30-854b-4a22-9c2d-e2cfa46bf0e5
name: Cloudflare Gateway HTTP
type: intake

## Overview

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable. In this documentation, you will learn how to collect and send Cloudflare Gateway HTTP logs to Sekoia.io.

- **Vendor**: Cloudflare
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Web logs

## Configuration

### Create the intake on Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cloudflare.

### Configure events forwarding on Cloudflare

{!_shared_content/operations_center/integrations/cloudflare_necessary_info.md!}

#### Create a Logpush job

Configure a [Logpush job](https://developers.cloudflare.com/logs/reference/logpush-api-configuration/){:target="_blank"} with the following destination:

`https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>`

!!! warning 
    The previous URL works for the FRA1 region. For any other region, replace the domain “intake.sekoia.io” with your region’s HTTP-intake domain—for example:

    https://app.usa1.sekoia.io/api/v1/intake-http

    You can find your region’s domain here: [https://docs.sekoia.io/getting_started/regions/](https://docs.sekoia.io/getting_started/regions/)

To do so, you can manage Logpush with cURL:

```bash
$ curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<CLOUDFLARE_ACCOUNT_ID>/logpush/jobs' \
-H 'Authorization: Bearer <CLOUDFLARE_API_TOKEN>' \
-H "Content-Type: application/json" \
-d '{
    "dataset": "gateway_http",
    "enabled": true,
    "max_upload_bytes": 5000000,
    "max_upload_records": 1000,
    "output_options":"timestamp_format=rfc3339",
    "destination_conf": "https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>"
    }' # (1)
```

1. will return
```json
{
  "errors": [],
  "messages": [],
  "result": {
    "id": "<ID>",
    "dataset": "gateway_http",
    "frequency":"high",
    "kind":"",
    "max_upload_bytes": 5000000,
    "max_upload_records": 1000,
    "enabled": true,
    "name": "<DOMAIN_NAME>",
    "output_options":"timestamp_format=rfc3339",
    "destination_conf": "https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>",
    "last_complete": null,
    "last_error": null,
    "error_message": null,
    "time_created":"<TIMESTAMP>"
  },
  "success": true
}
```

!!! Important
    Replace :

    - `<YOUR_INTAKE_KEY>` with the Intake key you generated in the [Create the intake on Sekoia.io](#create-the-intake-on-sekoiaio) step.
    - `<CLOUDFLARE_ACCOUNT_ID>` with the ACCOUNT_ID found on the overview page
    - `<CLOUDFLARE_API_TOKEN>` with the API Token you generated

{!_shared_content/operations_center/integrations/cloudflare_useful_accounts_scoped_api_endpoints.md!}

{!_shared_content/operations_center/integrations/generated/f570dd30-854b-4a22-9c2d-e2cfa46bf0e5_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_f570dd30-854b-4a22-9c2d-e2cfa46bf0e5_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f570dd30-854b-4a22-9c2d-e2cfa46bf0e5.md!}
