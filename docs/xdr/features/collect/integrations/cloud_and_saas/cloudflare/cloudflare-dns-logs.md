uuid: bd9d0f51-114e-499a-bb7a-4f2d0a518b04
name: Cloudflare DNS logs
type: intake

## Overview

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable.

In this documentation, you will learn how to collect and send Cloudflare DNS logs to SEKOIA.IO.

{!_shared_content/operations_center/integrations/generated/cloudflare-dns-logs_do_not_edit_manually.md!}

## Configuration

### Create the intake on SEKOIA.IO

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cloudflare.

### Configure events forwarding on Cloudflare

{!_shared_content/operations_center/integrations/cloudflare_necessary_info.md!}

#### Configure Logpush

##### Retrieve all available fields with your subscription

Depending on your subscription, you first need to get all the fields that you can forward to SEKOIA.IO by using the Cloudflare API [Retrieve all available fields for a dataset](https://developers.cloudflare.com/logs/get-started/api-configuration/){:target="_blank"}.

With cURL you can use this command:
```bash
curl -s -H "X-Auth-Email: <Cloudflare Email Address>" \
-H "X-Auth-Key: <Cloudflare API Token>" \
"https://api.cloudflare.com/client/v4/zones/<Cloudflare Zone ID>/logpush/datasets/dns_logs/fields" \
| jq '.result' # (1)
```

1. will return
```json
{
  "ColoCode": "string; IATA airport code of data center that received the request",
  "EDNSSubnet": "string; EDNS Client Subnet (IPv4 or IPv6). See here: [EDNS Client Subnet](/logs/reference/glossary/#edns-client-subnet-ecs)",
  "EDNSSubnetLength": "int; EDNS Client Subnet length. See here: [EDNS Client Subnet](/logs/reference/glossary/#edns-client-subnet-ecs)",
  "QueryName": "string; name of the query that was sent",
  "QueryType": "int; integer value of query type. See here: [Query type](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4)",
  "ResponseCached": "bool; whether the response was cached or not",
  "ResponseCode": "int; integer value of response code. See here: [Response code](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6)",
  "SourceIP": "string; IP address of the client (IPv4 or IPv6)",
  "Timestamp": "int or string; timestamp at which the query occurred"
}
```

Save the fields you want to send to SEKOIA.IO. It will be used to [configure the Logpush job](#configure-logpush). It this example :
```bash
ColoCode,EDNSSubnet,EDNSSubnetLength,QueryName,QueryType,ResponseCached,ResponseCode,SourceIP,Timestamp
```

##### Create a Logpush job

Configure a [Logpush job](https://developers.cloudflare.com/logs/reference/logpush-api-configuration/){:target="_blank"} with the following destination:

`https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>`


To do so, you can manage Logpush with cURL:

```bash
$ curl -X POST https://api.cloudflare.com/client/v4/zones/<Cloudflare Zone ID>/logpush/jobs \
-h "X-Auth-Email: <Cloudflare Email Address>" \
-H "X-Auth-Key: <Cloudflare API Token>" \
-H "Content-Type: application/json" \
--data '{
    "dataset": "dns_logs",
    "enabled": true,
    "max_upload_bytes": 5000000,
    "max_upload_records": 1000,
    "logpull_options":"fields=<LIST_OF_FIELDS>&timestamps=rfc3339",
    "destination_conf": "https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>"
}' # (1)
```

1. will return
```json
{
  "errors": [],
  "messages": [],
  "result": {
    "id": 148,
    "dataset": "dns_log",
    "enabled": false,
    "name": "<DOMAIN_NAME>",
    "logpull_options": "fields=<LIST_OF_FIELDS>=rfc3339",
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

    - `<YOUR_INTAKE_KEY>` with the Intake key you generated in the [Create the intake on SEKOIA.IO](#create-the-intake-on-sekoiaio) step.
    - `<LIST_OF_FIELDS>` with the fields you identified in the [Retrieve all available fields with your subscription](#retrieve-all-available-fields-with-your-subscription) section (for instance `ColoCode,EDNSSubnet,EDNSSubnetLength,QueryName,QueryType,ResponseCached,ResponseCode,SourceIP,Timestamp`).

{!_shared_content/operations_center/integrations/cloudflare_useful_api_endpoints.md!}