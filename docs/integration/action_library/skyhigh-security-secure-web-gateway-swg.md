# Skyhigh Security Secure Web Gateway (SWG)

![Skyhigh Security Secure Web Gateway (SWG)](/assets/playbooks/library/skyhigh-security-secure-web-gateway-swg.png){ align=right width=150 }

Skyhigh Security Secure Web Gateway (SWG)

## Configuration

This module accepts no configuration.

## Triggers

### Fetch events from Skyhigh Security Secure Web Gateway (SWG) API

Fetch events from Skyhigh Security Secure Web Gateway (SWG) API

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `customer_id` | `integer` | Customer ID (e.g. 1234567890) |
| `account_name` | `string` | Username |
| `account_password` | `string` | Password associated with the account |
| `frequency` | `integer` | Batch frequency in seconds |
| `api_domain_name` | `string` | Domain name to use (Europe :eu.msg.mcafeesaas.com, North America: us.msg.mcafeesaas.com) |
| `intake_server` | `string` | Address of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `chunk_size` | `integer` | The size of chunks for the batch processing (max is 1000) |


## Extra

Module **`Skyhigh Security Secure Web Gateway (SWG)` v1.0.6**