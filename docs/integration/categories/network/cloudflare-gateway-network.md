uuid: d14567dd-56b1-42f8-aa64-fb65d4b0a4cf
name: Cloudflare Gateway Network
type: intake

## Overview

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable. In this documentation, you will learn how to collect and send Gateway Network logs to Sekoia.io.

- **Vendor**: Cloudflare
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Network device logs, Network protocol analysis

## Configuration

### Create the intake on Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cloudflare.

### Configure events forwarding on Cloudflare

{!_shared_content/operations_center/integrations/cloudflare_necessary_info.md!}

#### Create a Logpush job

Configure a [Logpush job](https://developers.cloudflare.com/logs/reference/logpush-api-configuration/){:target="_blank"} with the following destination:

`https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>`


To do so, you can manage Logpush with cURL:

```bash
$ curl -X POST https://api.cloudflare.com/client/v4/accounts/<CLOUDFLARE_ACCOUNT_ID>/logpush/jobs \
-H "Authorization: Bearer <CLOUDFLARE_API_TOKEN>" \
-H "Content-Type: application/json" \
--data '{
    "dataset": "gateway_network",
    "enabled": true,
    "max_upload_bytes": 5000000,
    "max_upload_records": 1000,
    "logpull_options":"fields=AccountID,Action,Datetime,DestinationIP,DestinationPort,DeviceID,DeviceName,Email,OverrideIP,OverridePort,PolicyID,PolicyName,SNI,SessionID,SourceIP,SourceInternalIP,SourcePort,Transport,UserID&timestamps=rfc3339",
    "destination_conf": "https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>"
}' # (1)
```

1. will return
```json
{
  "errors": [],
  "messages": [],
  "result": {
    "id": <ID>,
    "dataset": "gateway_network",
    "frequency": "high",
    "kind": "",
    "max_upload_bytes": 5000000,
    "max_upload_records": 1000,
    "enabled": true,
    "name": null,
    "logpull_options": "fields=<LIST_OF_FIELDS>",
    "destination_conf": "https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>",
    "last_complete": null,
    "last_error": null,
    "error_message": null,
    "time_created": "<TIMESTAMP>"
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

{!_shared_content/operations_center/integrations/generated/d14567dd-56b1-42f8-aa64-fb65d4b0a4cf_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d14567dd-56b1-42f8-aa64-fb65d4b0a4cf_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d14567dd-56b1-42f8-aa64-fb65d4b0a4cf.md!}