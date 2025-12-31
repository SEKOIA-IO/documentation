---
uuid: a0716ffd-5f9e-4b97-add4-30f1870e3d03
title: Netskope Transaction Events
name: Netskope Transaction Events
type: intake
---

## Overview

[Netskope](https://www.netskope.com/) is a cybersecurity company that provides solutions to protect data in cloud apps and network security while applying zero trust principles.

- **Vendor**: Netskope
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Network

## Prerequisites

- Access to the Netskope Admin console
- The **Event Streaming option activated** (Please contact the Netskope Support if not).
- Access to Sekoia.io Intakes and Playbook pages with write permissions

## Step-by-Step Configuration Procedure
### Instructions on the 3rd Party Solution

!!! Important
    The Netskope Event Streaming rely on [Google Pub/Sub lite](https://cloud.google.com/pubsub/lite/docs).

#### Create and download JSON keys

To collect transaction events, you will need a subscription key:

1. Connect to the Netskope Admin console
2. Go to `Settings > Tools`
3. On the left panel, click on the `Event Streaming`. If the section is not available in our Admin UI, please contact the Netskope Support.
4. Go to the `Subscription Key` section and click on `Generate and Download key`

Find more information about the subscription key on the [official google documentation](https://cloud.google.com/iam/docs/keys-create-delete).

**Example of JSON key file**

```JSON
{
  "type": "service_account",
  "project_id": "PROJECT_ID",
  "private_key_id": "KEY_ID",
  "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n",
  "client_email": "SERVICE_ACCOUNT_EMAIL",
  "client_id": "CLIENT_ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL"
}
```

5.  Also in the `Event Streaming` section, extract 4 sub-strings from the `Subscription Endpoint` as explained in the following example:

Example of Subcription Endoint: `projects/1023456728636/locations/europe-west3-a/subscriptions/prod-goskope-eu456-sub-streaming-12345-6706281495`

| Information to collect | Example of values contained in the Subscription Endpoint |
| --- | --- |
| Project ID | 1023456728636 |
| Subscription ID | prod-goskope-eu456-sub-streaming-12345-6706281495 |
| Cloud Region | europe-west3 |
| Zone ID | a |

### Instruction on Sekoia
#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Netskope Transaction Events`.
2. Set the intake configuration using:
    * Your service account credentials from your Google Cloud environment extracted on a JSON file
    * Subscription ID, Cloud Region and Zone ID extracted from the Subscription Endpoint on Netskope Event Streaming section
    * Select the `application name` what you to fetch events from
    * Type the `Admin email`
 
!!! Note
    Please copy past the whole private key value during the procedure, including the begining and ending separators.


{!_shared_content/operations_center/integrations/generated/a0716ffd-5f9e-4b97-add4-30f1870e3d03_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a0716ffd-5f9e-4b97-add4-30f1870e3d03_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/a0716ffd-5f9e-4b97-add4-30f1870e3d03.md!}

## Further readings

- [Configuring Netskope Transaction Events](https://docs.netskope.com/en/netskope-help/data-security/transaction-events/netskope-transaction-events/)
- [Create a service account](https://support.google.com/a/answer/7378726?hl=en)
- [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete)
