uuid: 16676d72-463e-4b8a-b13a-f8dd48cddc8c
name: Cloudflare Firewall Events
type: intake

## Overview

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable.

In this documentation, you will learn how to collect and send Cloudflare Firewall events to SEKOIA.IO.

{!_shared_content/operations_center/detection/generated/suggested_rules_16676d72-463e-4b8a-b13a-f8dd48cddc8c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/cloudflare-firewall-events_do_not_edit_manually.md!}

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
"https://api.cloudflare.com/client/v4/zones/<Cloudflare Zone ID>/logpush/datasets/firewall_events/fields" \
| jq '.result' # (1)
```

1. will return
```json
{
  "Action": "string; the code of the first-class action the Cloudflare Firewall took on this request. Possible actions are unknown | allow | block | challenge | jschallenge | log | connectionclose | challengesolved | challengefailed | challengebypassed | jschallengesolved | jschallengefailed | jschallengebypassed | bypass | managedchallenge | managedchallengeskipped | managedchallengenoninteractivesolved | managedchallengeinteractivesolved | managedchallengebypassed",
  "ClientASN": "int; the ASN number of the visitor",
  "ClientASNDescription": "string; the ASN of the visitor as string",
  "ClientCountry": "string; country from which request originated",
  "ClientIP": "string; the visitor's IP address (IPv4 or IPv6)",
  "ClientIPClass": "string; the classification of the visitor's IP address, possible values are: unknown | badHost | searchEngine | allowlist | monitoringService | noRecord | scan | tor",
  "ClientRefererHost": "string; the referer host",
  "ClientRefererPath": "string; the referer path requested by visitor",
  "ClientRefererQuery": "string; the referer query-string was requested by the visitor",
  "ClientRefererScheme": "string; the referer URL scheme requested by the visitor",
  "ClientRequestHost": "string; the HTTP hostname requested by the visitor",
  "ClientRequestMethod": "string; the HTTP method used by the visitor",
  "ClientRequestPath": "string; the path requested by visitor",
  "ClientRequestProtocol": "string; the version of HTTP protocol requested by the visitor",
  "ClientRequestQuery": "string; the query-string was requested by the visitor",
  "ClientRequestScheme": "string; the URL scheme requested by the visitor",
  "ClientRequestUserAgent": "string; visitor's user-agent string",
  "Datetime": "int or string; the date and time the event occurred at the edge",
  "EdgeColoCode": "string; the airport code of the Cloudflare datacenter that served this request",
  "EdgeResponseStatus": "int; HTTP response status code returned to browser",
  "Kind": "string; the kind of event, currently only possible values are: firewall",
  "MatchIndex": "int; rules match index in the chain",
  "Metadata": "object; additional product-specific information. Metadata is organized in key:value pairs. Key and Value formats can vary by Cloudflare security product and can change over time",
  "OriginResponseStatus": "int; HTTP origin response status code returned to browser",
  "OriginatorRayID": "string; the RayID of the request that issued the challenge/jschallenge",
  "RayID": "string; the RayID of the request",
  "RuleID": "string; the Cloudflare security product-specific RuleID triggered by this request",
  "Source": "string; the Cloudflare security product triggered by this request. Possible sources are unknown | asn | country | ip | iprange | securitylevel | zonelockdown | waf | firewallrules | uablock | ratelimit | bic | hot | l7ddos | validation | botfight | apishield | botmanagement | dlp | firewallmanaged | firewallcustom"
}
```

Save the fields you want to send to SEKOIA.IO. It will be used to [configure the Logpush job](#configure-logpush). It this example :
```bash
Action,ClientASN,ClientASNDescription,ClientCountry,ClientIP,ClientIPClass,ClientRefererHost,ClientRefererPath,ClientRefererQuery,ClientRefererScheme,ClientRequestHost,ClientRequestMethod,ClientRequestPath,ClientRequestProtocol,ClientRequestQuery,ClientRequestScheme,ClientRequestUserAgent,Datetime,EdgeColoCode,EdgeResponseStatus,Kind,MatchIndex,Metadata,OriginResponseStatus,OriginatorRayID,RayID,RuleID,Source
```

##### Create a Logpush job

Configure a [Logpush job](https://developers.cloudflare.com/logs/reference/logpush-api-configuration/){:target="_blank"} with the following destination:

`https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<YOUR_INTAKE_KEY>`

To do so, you can manage Logpush with cURL:

```bash
$ curl -X POST https://api.cloudflare.com/client/v4/zones/<Cloudflare Zone ID>/logpush/jobs \
-h "x-auth-email: <Cloudflare Email Address>" \
-H "X-Auth-Key: <Cloudflare API Token>" \
-H "Content-Type: application/json" \
--data '{
    "dataset": "firewall_events",
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
    "id": 147,
    "dataset": "firewall_events",
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

    - `<YOUR_INTAKE_KEY>` with the Intake key you generated in the [Create the intake on SEKOIA.IO](#create-the-intake-on-sekoiaio) step.
    - `<LIST_OF_FIELDS>` with the fields you identified in the [Retrieve all available fields with your subscription](#retrieve-all-available-fields-with-your-subscription) section (for instance `Action,ClientASN,ClientASNDescription,ClientCountry,ClientIP,ClientIPClass,ClientRefererHost,ClientRefererPath,ClientRefererQuery,ClientRefererScheme,ClientRequestHost,ClientRequestMethod,ClientRequestPath,ClientRequestProtocol,ClientRequestQuery,ClientRequestScheme,ClientRequestUserAgent,Datetime,EdgeColoCode,EdgeResponseStatus,Kind,MatchIndex,Metadata,OriginResponseStatus,OriginatorRayID,RayID,RuleID,Source`).

{!_shared_content/operations_center/integrations/cloudflare_useful_api_endpoints.md!}
