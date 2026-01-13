---
uuid: ae62a8c4-11f8-4aea-af5b-6968f8ac04ba
title: Azure Key Vault
name: Azure Key Vault
type: intake
---

## Overview

Azure Key Vault is a cloud service that securely stores and manages sensitive information such as passwords, encryption
keys, and certificates. It helps safeguard cryptographic keys and secrets used by cloud applications and services. This setup guide describe how to forward events produced by `Azure Key Vault` to Sekoia.io.

- **Vendor**: Microsoft Azure
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs

## Configure

### Prerequisites

- An access key for the Azure Blob Storage
- A storage token associated with the resources to share
- The name of the container where the Key Vault logs are stored
- Properly configured [Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview) with logging enabled.

### How to enable Azure Key Vault logging

You can enable logging for Key Vault by using the Azure CLI, Azure PowerShell, or the Azure portal.

Detailed instructions can be found in official docs [here](https://learn.microsoft.com/en-us/azure/key-vault/general/howto-logging?tabs=azure-portal#enable-logging).

### Create the intake in Sekoia.io

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Azure Key Vault`. 
2. Set up the intake configuration with `account_key`, `account_name` and the `container_name`.

{!_shared_content/operations_center/integrations/generated/ae62a8c4-11f8-4aea-af5b-6968f8ac04ba_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_ae62a8c4-11f8-4aea-af5b-6968f8ac04ba_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ae62a8c4-11f8-4aea-af5b-6968f8ac04ba.md!}
