uuid: 0ba58f32-7dba-4084-ab17-90c0be6b1f10
name: Cloudflare
type: intake

## Overview

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable.

In this documentation we will explain how to collect and send Cloudflare HTTP logs to SEKOIA.IO.

{!operation_center/integration_catalog/generated/cloudflare_do_not_edit_manually.md!}

## Configure


First, you will have to retrieve configuration information.
To do so, connect to [Cloudflare Console](https://dash.cloudflare.com/) to collect:
- `Cloudflare authentication key`
- `Cloudflare Zone ID`
- `Cloudflare account email`


You now have all information to configure the Cloudflare module and its `Send events` action to SEKOIA.IO.

You can now enable Cloudflare log retention (see [associated documentation](https://developers.cloudflare.com/logs/logpull/enabling-log-retention/)). 

To start your playbook with a template, go to: "Create a new playbook" > "Use a template" > Search for Cloudflare.

You can also create your own on the same basis. A typical playbook to retrieve and send Cloudflare logs to SEKOIA.IO will use this kind of chain:

- A "Cloudflare Logpull" trigger
- An action that sends events to SEKOIA.IO
