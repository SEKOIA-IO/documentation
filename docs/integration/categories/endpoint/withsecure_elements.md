---
uuid: 033cd098-b21b-4c9b-85c4-c8174c307e48
title: WithSecure Elements
name: WithSecure Elements
type: intake
---

## Overview

WithSecure Elements is an advanced cloud-based EDR/EPP platform that provides a unified solution to protect your organization from cyber threats. By integrating WithSecure Elements with Sekoia.io, you can easily monitor and correlate alerts across all endpoints, ensuring maximum security for your business.

This setup guide shows how to forward events produced by WithSecures Elements to Sekoia.io.

- **Vendor**: WithSecure
- **Supported environment**: Cloud
- **Detection based on**: Telemetry
- **Supported application or feature**: File monitoring, Process monitoring

## Configure

### Create WithSecure Elements Credentials

In the WithSecure Elements Central Admin console:

1. On the left panel, go to `Management` and select `API clients`.
2. Click on `Add new` to create a new API client dedicated to Sekoia.io.
3. Give it a description, check it is `Read-Only` and click on `Add`.
4. In the `API client` Summary, copy the `Client ID` and the `Secret` before checking the box `I have copied and stored the secret` and closing the windows. They will be used later in Sekoia.io to retrieve the events.

![WithSecure API Client Creation](/assets/integration/endpoint/withsecure/withsecure_create_api_client.png){: style="max-width:80%"}

### Create the intake

1. Go to the [Intake page](https://app.sekoia.io/operations/intakes) and create a new `WithSecure Elements` intake.
2. Set the intake account with your API Client credentials `Client ID`/`Secret`
3. After a couple of minutes check on the Events page that WithSecure Elements logs are being received.

{!_shared_content/operations_center/integrations/generated/033cd098-b21b-4c9b-85c4-c8174c307e48_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_033cd098-b21b-4c9b-85c4-c8174c307e48_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/033cd098-b21b-4c9b-85c4-c8174c307e48.md!}