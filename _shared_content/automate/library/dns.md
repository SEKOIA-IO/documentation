uuid: 33e52bf6-642f-4230-acd5-751699077b84
name: DNS
type: playbook

# DNS

![DNS](/assets/playbooks/library/dns.png){ align=right width=150 }

Module for DNS-related automations and lookups

## Configuration

This module accepts no configuration.

## Actions

### Reverse DNS Lookup

Resolve an IP address into its corresponding hostname using a PTR request

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip_address` | `string` | The IP address to resolve |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip_address` | `string` |  |
| `hostname` | `['string', 'null']` |  |
| `aliases` | `array` |  |
| `error` | `['string', 'null']` | Error message if the resolution fails |


## Extra

Module **`DNS` v0.1.0**