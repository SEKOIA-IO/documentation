uuid: 0ba58f32-7dba-4084-ab17-90c0be6b1f10
name: Cloudflare
type: intake

## Overview

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable.

In this documentation, you will learn how to collect and send Cloudflare HTTP logs to SEKOIA.IO.

{!xdr/features/collect/integrations/generated/cloudflare_do_not_edit_manually.md!}

## Configure

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cloudflare.

### Forward the events

First, you will have to retrieve configuration information.
To do so, connect to [Cloudflare Console](https://dash.cloudflare.com/) to collect:

- `Cloudflare authentication key`
- `Cloudflare Zone ID`
- `Cloudflare account email`

#### with logpush

!!! note

    It's the recommended way to get your events from Cloudflare.

Configure a [Logpush job](https://developers.cloudflare.com/logs/reference/logpush-api-configuration/) with the following destination:

`https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<your intake key>`


##### Manage logpush with cURL

```bash
$ curl -X POST https://api.cloudflare.com/client/v4/zones/<CLOUDFLARE_ZONE_ID>/logpush/jobs \
-H "X-Auth-Email: <CLOUDFLARE_EMAIL>" \
-H "X-Auth-Key: <CLOUDFLARE_API_KEY>" \
-H "Content-Type: application/json" \
--data '{
    "dataset": "http_requests",
    "enabled": true,
    "max_upload_bytes": 5000000,
    "max_upload_records": 1000,
    "destination_conf": "https://intake.sekoia.io/plain/batch?header_X-SEKOIAIO-INTAKE-KEY=<INTAKE_KEY>"
}'
```


#### with logpull

 To start using Logpull, start by enabling [Cloudflare log retention](https://developers.cloudflare.com/logs/logpull/enabling-log-retention/).

To pull events, go to [the playbook page](https://app.sekoia.io/operations/playbooks) and create your playbook with a template: "Create a new playbook" > "Use a template" > Search for Cloudflare.
Fill the module configuration with the information got from our Cloudflare Console.

You can also create your own on the same basis. A typical playbook to retrieve and send Cloudflare logs to SEKOIA.IO will use this kind of chain:

- A "Cloudflare Logpull" trigger
- An action that sends events to SEKOIA.IO
