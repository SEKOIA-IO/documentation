uuid: 0ba58f32-7dba-4084-ab17-90c0be6b1f10
name: Cloudflare HTTP requests
type: intake

## Overview

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable. In this documentation, you will learn how to collect and send Cloudflare HTTP requests to Sekoia.io.

- **Vendor**: Cloudflare
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Web logs, Web application firewall logs

## Configure

### Create the intake on Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cloudflare.

### Configure events forwarding on Cloudflare

{!_shared_content/operations_center/integrations/cloudflare_necessary_info.md!}

#### Create a Logpush job

Configure a [Logpush job](https://developers.cloudflare.com/logs/reference/logpush-api-configuration/){:target="_blank"} with the following destination:

`https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>`

To do so, you can manage Logpush with cURL:

```bash
$ curl -X POST https://api.cloudflare.com/client/v4/zones/<CLOUDFLARE_ZONE_ID>/logpush/jobs \
-H "Authorization: Bearer <CLOUDFLARE_API_TOKEN>" \
-H "Content-Type: application/json" \
--data '{
    "dataset": "http_requests",
    "enabled": true,
    "max_upload_bytes": 5000000,
    "max_upload_records": 1000,
    "logpull_options":"fields=ClientIP,ClientRequestHost,ClientRequestMethod,ClientRequestURI,EdgeEndTimestamp,EdgeResponseBytes,EdgeResponseStatus,EdgeStartTimestamp,RayID&timestamps=unix",
    "destination_conf": "https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>"
}' # (1)
```

1. will return
```json
{
  "errors": [],
  "messages": [],
  "result": {
    "id": 146,
    "dataset": "http_requests",
    "enabled": false,
    "name": "<DOMAIN_NAME>",
    "logpull_options": "fields=<LIST_OF_FIELDS>&timestamps=rfc3339",
    "destination_conf": "https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>",
    "last_complete": null,
    "last_error": null,
    "error_message": null
  },
  "success": true
}
```

!!! Important
    Replace :

    - `<YOUR_INTAKE_KEY>` with the Intake key you generated in the [Create the intake on Sekoia.io](#create-the-intake-on-sekoiaio) step.
    - `<CLOUDFLARE_API_TOKEN>` with the API Token you generated
    - `<CLOUDFLARE_ZONE_ID>` with the Zone ID you grabbed

{!_shared_content/operations_center/integrations/cloudflare_useful_zones_scoped_api_endpoints.md!}

{!_shared_content/operations_center/integrations/generated/0ba58f32-7dba-4084-ab17-90c0be6b1f10_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_0ba58f32-7dba-4084-ab17-90c0be6b1f10_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/0ba58f32-7dba-4084-ab17-90c0be6b1f10.md!}